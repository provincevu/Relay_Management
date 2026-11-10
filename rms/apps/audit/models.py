import uuid

from django.conf import settings
from django.db import models


class AuditEvent(models.Model):
    """Lưu nối tiếp lịch sử thay đổi của người dùng trên đối tượng nghiệp vụ."""

    event_id = models.UUIDField("Event ID (Mã sự kiện)", default=uuid.uuid4, unique=True, editable=False)
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="rms_audit_events",
        null=True,
        blank=True,
        verbose_name="Actor (Người thực hiện)",
    )
    action = models.CharField("Action (Thao tác)", max_length=128)
    target_type = models.CharField("Target Type (Loại đối tượng)", max_length=128)
    target_id = models.CharField("Target ID (Mã đối tượng)", max_length=128)
    before = models.JSONField("Before (Dữ liệu trước)", null=True, blank=True)
    after = models.JSONField("After (Dữ liệu sau)", null=True, blank=True)
    reason = models.TextField("Reason (Lý do)", blank=True)
    request_id = models.CharField("Request ID (Mã yêu cầu)", max_length=64, blank=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Audit Event (Sự kiện kiểm toán)"
        verbose_name_plural = "Audit Events (Sự kiện kiểm toán)"
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

    event_id = models.UUIDField("Event ID (Mã sự kiện)", default=uuid.uuid4, unique=True, editable=False)
    event_type = models.CharField("Event Type (Loại sự kiện)", max_length=128)
    payload = models.JSONField("Payload (Dữ liệu sự kiện)", default=dict)
    recipient_user_ids = models.JSONField("Recipient User IDs (Mã người nhận)", default=list, blank=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True, db_index=True)
    published_at = models.DateTimeField("Published At (Thời điểm phát)", null=True, blank=True, db_index=True)
    attempts = models.PositiveIntegerField("Attempts (Số lần thử)", default=0)
    last_error = models.TextField("Last Error (Lỗi gần nhất)", blank=True)

    class Meta:
        verbose_name = "Outbox Event (Sự kiện chờ phát)"
        verbose_name_plural = "Outbox Events (Sự kiện chờ phát)"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.event_type}: {self.event_id}"


class IdempotencyRecord(models.Model):
    """Lưu response để phát lại khi API nhận cùng một request thay đổi dữ liệu."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rms_idempotency_records",
        verbose_name="User (Người dùng)",
    )
    key = models.CharField("Key (Khóa chống lặp)", max_length=255)
    method = models.CharField("Method (Phương thức)", max_length=10)
    path = models.CharField("Path (Đường dẫn)", max_length=512)
    request_hash = models.CharField("Request Hash (Mã băm yêu cầu)", max_length=64)
    response_status = models.PositiveSmallIntegerField("Response Status (Mã trạng thái phản hồi)", null=True, blank=True)
    response_body = models.JSONField("Response Body (Nội dung phản hồi)", null=True, blank=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    expires_at = models.DateTimeField("Expires At (Thời điểm hết hạn)", db_index=True)

    class Meta:
        verbose_name = "Idempotency Record (Bản ghi chống yêu cầu lặp)"
        verbose_name_plural = "Idempotency Records (Bản ghi chống yêu cầu lặp)"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "key", "method", "path"],
                name="rms_idemp_method_path_uniq",
            )
        ]
        indexes = [models.Index(fields=["expires_at"], name="rms_idempotency_expires_idx")]
