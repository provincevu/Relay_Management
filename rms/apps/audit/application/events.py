from django.db import connection

from rms.apps.audit.models import AuditEvent, OutboxEvent

SENSITIVE_MARKERS = ("password", "token", "secret", "authorization", "apikey")


def _redact_sensitive_data(value):
    """Ẩn các trường bí mật trước khi lưu snapshot audit hoặc event payload."""
    if isinstance(value, dict):
        return {
            key: (
                "[REDACTED]"
                if any(marker in str(key).lower().replace("_", "").replace("-", "") for marker in SENSITIVE_MARKERS)
                else _redact_sensitive_data(item)
            )
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_redact_sensitive_data(item) for item in value]
    return value


def record_event(
    *,
    actor,
    action,
    target_type,
    target_id,
    request_id,
    event_type,
    before=None,
    after=None,
    reason="",
    payload=None,
    recipient_user_ids=None,
):
    """Ghi audit và outbox nguyên tử cùng thay đổi nghiệp vụ."""
    if not connection.in_atomic_block:
        raise RuntimeError("record_event must run inside transaction.atomic().")

    audit_event = AuditEvent.objects.create(
        actor=actor,
        action=action,
        target_type=target_type,
        target_id=str(target_id),
        before=_redact_sensitive_data(before),
        after=_redact_sensitive_data(after),
        reason=reason,
        request_id=request_id or "",
    )
    outbox_event = OutboxEvent.objects.create(
        event_type=event_type,
        payload=_redact_sensitive_data(payload or {}),
        recipient_user_ids=recipient_user_ids or [],
    )
    return audit_event, outbox_event
