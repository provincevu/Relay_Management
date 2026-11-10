import hashlib
import json
from datetime import timedelta

from django.db import IntegrityError, transaction
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_409_CONFLICT

from rms.apps.audit.models import IdempotencyRecord
from rms.shared.api.exceptions import ApiError


def _request_hash(request):
    """Tạo hash từ method, path và body để key không bị dùng cho input khác."""
    request_content = b"\0".join(
        [request.method.encode(), request.path.encode(), request.body]
    )
    return hashlib.sha256(request_content).hexdigest()


def _replay_or_conflict(record, request_hash):
    """Phản hồi lại kết quả cũ hoặc từ chối nếu cùng key nhưng payload khác."""
    if record.request_hash != request_hash:
        raise ApiError(
            "This Idempotency-Key was already used for a different request.",
            code="idempotency_key_reused",
            status_code=HTTP_409_CONFLICT,
        )
    if record.response_status is None:
        raise ApiError(
            "An identical request is still being processed.",
            code="idempotency_request_in_progress",
            status_code=HTTP_409_CONFLICT,
        )
    return Response(record.response_body, status=record.response_status)


def execute_idempotent(request, action, *, retention_hours=24):
    """Thực hiện command một lần và lưu response để request retry có thể phát lại."""
    key = request.headers.get("Idempotency-Key", "").strip()
    if not key:
        raise ApiError(
            "The Idempotency-Key header is required.",
            code="idempotency_key_required",
        )
    if len(key) > 255:
        raise ApiError("Idempotency-Key is too long.", code="idempotency_key_invalid")

    request_hash = _request_hash(request)
    identity = {
        "user": request.user,
        "key": key,
        "method": request.method.upper(),
        "path": request.path,
    }

    try:
        with transaction.atomic():
            existing = IdempotencyRecord.objects.select_for_update().filter(**identity).first()
            if existing:
                if existing.expires_at > timezone.now():
                    return _replay_or_conflict(existing, request_hash)
                existing.delete()

            try:
                # Savepoint cô lập lỗi unique khi hai request cùng key chạy đồng thời.
                with transaction.atomic():
                    record = IdempotencyRecord.objects.create(
                        **identity,
                        request_hash=request_hash,
                        expires_at=timezone.now() + timedelta(hours=retention_hours),
                    )
            except IntegrityError:
                existing = IdempotencyRecord.objects.select_for_update().get(**identity)
                return _replay_or_conflict(existing, request_hash)

            response = action()
            if response.status_code >= 500:
                # Không lưu lỗi server làm kết quả cuối để client có thể retry an toàn.
                record.delete()
                return response

            rendered_body = JSONRenderer().render(response.data)
            record.response_status = response.status_code
            record.response_body = json.loads(rendered_body.decode("utf-8"))
            record.save(update_fields=["response_status", "response_body"])
            return response
    except IdempotencyRecord.DoesNotExist:
        # Request cạnh tranh đầu tiên có thể rollback; lần sau phải chạy command mới.
        raise ApiError(
            "The previous request did not finish; retry with the same key.",
            code="idempotency_retry_required",
            status_code=HTTP_409_CONFLICT,
        )
