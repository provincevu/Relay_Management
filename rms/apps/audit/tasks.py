import logging
from datetime import timedelta

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.conf import settings
from django.db import transaction
from django.utils import timezone

from rms.apps.audit.models import OutboxEvent

logger = logging.getLogger(__name__)
PLATFORM_HEARTBEAT_KEY = "rms:platform:celery-heartbeat"


@shared_task
def update_platform_heartbeat():
    """Beat gửi task định kỳ để readiness xác nhận beat, broker và worker cùng hoạt động."""
    import redis

    with redis.Redis.from_url(
        settings.REDIS_URL,
        socket_connect_timeout=2,
        socket_timeout=2,
    ) as client:
        client.set(PLATFORM_HEARTBEAT_KEY, timezone.now().isoformat(), ex=30)
    return "ok"


@shared_task
def publish_pending_outbox(batch_size=100):
    """Phát event tồn đọng tới user groups và chỉ đánh dấu sau khi gửi thành công."""
    channel_layer = get_channel_layer()
    published_count = 0

    with transaction.atomic():
        events = list(
            OutboxEvent.objects.select_for_update(skip_locked=True)
            .filter(published_at__isnull=True)
            .order_by("created_at")[:batch_size]
        )

        for event in events:
            try:
                for user_id in event.recipient_user_ids:
                    async_to_sync(channel_layer.group_send)(
                        f"user_{user_id}_notifications",
                        {
                            "type": "rms.event",
                            "event_id": str(event.event_id),
                            "event_type": event.event_type,
                            "payload": event.payload,
                        },
                    )
                event.published_at = timezone.now()
                event.last_error = ""
                event.save(update_fields=["published_at", "last_error"])
                published_count += 1
            except Exception as exc:  # pragma: no cover - lỗi phụ thuộc Redis runtime
                event.attempts += 1
                # Không lưu thông tin kết nối/secret có thể xuất hiện trong exception.
                event.last_error = f"{type(exc).__name__}: delivery failed"
                event.save(update_fields=["attempts", "last_error"])
                logger.error("Outbox event %s delivery failed (%s)", event.event_id, type(exc).__name__)

    return published_count


@shared_task
def delete_expired_idempotency_records(batch_size=1000):
    """Dọn response idempotency hết hạn theo lô để không làm phình bảng."""
    from rms.apps.audit.models import IdempotencyRecord

    cutoff = timezone.now() - timedelta(days=1)
    expired_ids = list(
        IdempotencyRecord.objects.filter(expires_at__lt=cutoff)
        .order_by("expires_at")
        .values_list("pk", flat=True)[:batch_size]
    )
    deleted_count, _ = IdempotencyRecord.objects.filter(pk__in=expired_ids).delete()
    return deleted_count
