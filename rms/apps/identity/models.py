from django.conf import settings
from django.db import models
from django.db.models import Q


class Organization(models.Model):
    """Đơn vị trong cây tổ chức dùng để giới hạn phạm vi dữ liệu."""

    code = models.CharField("Code (Mã)", max_length=64, unique=True)
    name = models.CharField("Name (Tên)", max_length=255)
    organization_type = models.CharField("Organization Type (Loại đơn vị)", max_length=64, blank=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        verbose_name="Parent Organization (Đơn vị cấp trên)",
    )
    is_active = models.BooleanField("Active Status (Trạng thái hoạt động)", default=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At (Thời điểm cập nhật)", auto_now=True)

    class Meta:
        verbose_name = "Organization (Đơn vị)"
        verbose_name_plural = "Organizations (Đơn vị)"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class UserProfile(models.Model):
    """Thông tin RMS mở rộng cho user Django hiện có."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rms_profile",
        verbose_name="User (Người dùng)",
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="user_profiles",
        null=True,
        blank=True,
        verbose_name="Organization (Đơn vị)",
    )
    # Giữ station ID dạng scalar để identity không phụ thuộc ngược vào module assets.
    home_station_id = models.PositiveBigIntegerField("Home Station ID (Mã trạm chính)", null=True, blank=True)
    phone_number = models.CharField("Phone Number (Số điện thoại)", max_length=32, blank=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At (Thời điểm cập nhật)", auto_now=True)

    class Meta:
        verbose_name = "User Profile (Hồ sơ người dùng)"
        verbose_name_plural = "User Profiles (Hồ sơ người dùng)"

    def __str__(self):
        return f"RMS profile: {self.user}"


class RoleGrant(models.Model):
    """Gán vai trò cho user theo phạm vi có thể mở rộng về sau."""

    class ScopeType(models.TextChoices):
        GLOBAL = "GLOBAL", "Global (Toàn cục)"
        ORGANIZATION = "ORGANIZATION", "Organization (Đơn vị)"
        STATION = "STATION", "Station (Trạm)"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rms_role_grants",
        verbose_name="User (Người dùng)",
    )
    role_code = models.CharField("Role Code (Mã vai trò)", max_length=64)
    scope_type = models.CharField("Scope Type (Phạm vi áp dụng)", max_length=16, choices=ScopeType.choices)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="role_grants",
        null=True,
        blank=True,
        verbose_name="Organization (Đơn vị)",
    )
    # Dùng scalar thay FK để giữ chiều phụ thuộc từ assets sang identity.
    station_id = models.PositiveBigIntegerField("Station ID (Mã trạm)", null=True, blank=True)
    starts_at = models.DateTimeField("Starts At (Có hiệu lực từ)", null=True, blank=True)
    ends_at = models.DateTimeField("Ends At (Có hiệu lực đến)", null=True, blank=True)
    granted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="granted_rms_roles",
        null=True,
        blank=True,
        verbose_name="Granted By (Người cấp)",
    )
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)

    class Meta:
        verbose_name = "Role Grant (Lần cấp vai trò)"
        verbose_name_plural = "Role Grants (Lần cấp vai trò)"
        constraints = [
            models.CheckConstraint(
                condition=(
                    Q(scope_type="GLOBAL", organization__isnull=True, station_id__isnull=True)
                    | Q(
                        scope_type="ORGANIZATION",
                        organization__isnull=False,
                        station_id__isnull=True,
                    )
                    | Q(scope_type="STATION", station_id__isnull=False)
                ),
                name="rms_role_grant_scope_valid",
            ),
            models.CheckConstraint(
                condition=Q(ends_at__isnull=True) | Q(starts_at__isnull=True) | Q(ends_at__gt=models.F("starts_at")),
                name="rms_role_grant_dates_ordered",
            ),
        ]
        indexes = [
            models.Index(fields=["user", "role_code", "scope_type"], name="rms_user_role_scope_idx"),
            models.Index(fields=["organization", "role_code"], name="rms_org_role_idx"),
        ]

    def __str__(self):
        return f"{self.user}: {self.role_code} ({self.scope_type})"
