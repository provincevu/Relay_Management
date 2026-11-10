import uuid

from django.conf import settings
from django.db import models


class AuditEvent(models.Model):
    """Lưu nối tiếp lịch sử thay đổi của người dùng trên đối tượng nghiệp vụ."""

    event_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="rms_audit_events",
        null=True,
        blank=True,
    )
    action = models.CharField(max_length=128)
    target_type = models.CharField(max_length=128)
    target_id = models.CharField(max_length=128)
    before = models.JSONField(null=True, blank=True)
    after = models.JSONField(null=True, blank=True)
    reason = models.TextField(blank=True)
    request_id = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=["target_type", "target_id", "created_at"],
                name="rms_audit_target_created_idx",
            )
        ]

    def __str__(self):
        return f"{self.action}: {self.target_type}/{self.target_id}"


class OutboxEvent(models.Model):
    """Lưu event bền vững để phát bất đồng bộ sau khi transaction commit."""

    event_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    event_type = models.CharField(max_length=128)
    payload = models.JSONField(default=dict)
    recipient_user_ids = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    published_at = models.DateTimeField(null=True, blank=True, db_index=True)
    attempts = models.PositiveIntegerField(default=0)
    last_error = models.TextField(blank=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.event_type}: {self.event_id}"


class IdempotencyRecord(models.Model):
    """Lưu response để phát lại khi API nhận cùng một request thay đổi dữ liệu."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rms_idempotency_records",
    )
    key = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=512)
    request_hash = models.CharField(max_length=64)
    response_status = models.PositiveSmallIntegerField(null=True, blank=True)
    response_body = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "key", "method", "path"],
                name="rms_idemp_method_path_uniq",
            )
        ]
        indexes = [models.Index(fields=["expires_at"], name="rms_idempotency_expires_idx")]
