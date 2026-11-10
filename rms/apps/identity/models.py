from django.conf import settings
from django.db import models
from django.db.models import Q


class Organization(models.Model):
    """Đơn vị trong cây tổ chức dùng để giới hạn phạm vi dữ liệu."""

    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=255)
    organization_type = models.CharField(max_length=64, blank=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class UserProfile(models.Model):
    """Thông tin RMS mở rộng cho user Django hiện có."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rms_profile",
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="user_profiles",
        null=True,
        blank=True,
    )
    # Giữ station ID dạng scalar để identity không phụ thuộc ngược vào module assets.
    home_station_id = models.PositiveBigIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=32, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"RMS profile: {self.user}"


class RoleGrant(models.Model):
    """Gán vai trò cho user theo phạm vi có thể mở rộng về sau."""

    class ScopeType(models.TextChoices):
        GLOBAL = "GLOBAL", "Global"
        ORGANIZATION = "ORGANIZATION", "Organization"
        STATION = "STATION", "Station"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rms_role_grants",
    )
    role_code = models.CharField(max_length=64)
    scope_type = models.CharField(max_length=16, choices=ScopeType.choices)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="role_grants",
        null=True,
        blank=True,
    )
    # Dùng scalar thay FK để giữ chiều phụ thuộc từ assets sang identity.
    station_id = models.PositiveBigIntegerField(null=True, blank=True)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    granted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="granted_rms_roles",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
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
