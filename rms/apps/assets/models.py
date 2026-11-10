from django.core.exceptions import ValidationError
from django.db import models

from rms.apps.catalog.models import CatalogItem
from rms.apps.identity.models import Organization

VOLTAGE_LEVEL_CATALOG_CODE = "VOLTAGE_LEVEL"


class Station(models.Model):
    """Trạm thuộc một đơn vị, có mã nội bộ và cấp điện áp chính tùy chọn."""

    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="stations",
    )
    voltage_level = models.ForeignKey(
        CatalogItem,
        on_delete=models.PROTECT,
        related_name="stations",
        null=True,
        blank=True,
        limit_choices_to={"catalog_type__code": VOLTAGE_LEVEL_CATALOG_CODE},
    )
    commissioned_at = models.DateTimeField(null=True, blank=True)
    installed_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["code"]
        indexes = [
            models.Index(
                fields=["organization", "is_active"],
                name="rms_station_org_active_idx",
            )
        ]

    def clean(self):
        """Chặn chọn nhầm loại CatalogItem làm cấp điện áp của trạm."""
        super().clean()
        if self.voltage_level_id and self.voltage_level.catalog_type.code != VOLTAGE_LEVEL_CATALOG_CODE:
            raise ValidationError(
                {"voltage_level": "Chỉ chọn mục thuộc danh mục cấp điện áp (VOLTAGE_LEVEL)."}
            )

    def __str__(self):
        return f"{self.code} - {self.name}"
