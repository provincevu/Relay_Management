from django.core.exceptions import ValidationError
from django.db import models

from rms.apps.catalog.models import CatalogItem
from rms.apps.identity.models import Organization

VOLTAGE_LEVEL_CATALOG_CODE = "VOLTAGE_LEVEL"
MANUFACTURER_CATALOG_CODE = "MANUFACTURER"


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


class Bay(models.Model):
    """Ngăn lộ thuộc đúng một trạm, với mã duy nhất trong phạm vi trạm đó."""

    station = models.ForeignKey(
        Station,
        on_delete=models.PROTECT,
        related_name="bays",
    )
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    rated_voltage = models.CharField(max_length=50, blank=True)
    rated_current = models.CharField(max_length=50, blank=True)
    # Giữ nguyên giá trị SDM cũ đến khi ý nghĩa và đơn vị của nó được xác định.
    legacy_sdm = models.CharField(
        max_length=50,
        blank=True,
        help_text="Giá trị nguồn SDM; chưa chuẩn hóa ý nghĩa hoặc đơn vị.",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["station__code", "code"]
        constraints = [
            models.UniqueConstraint(
                fields=["station", "code"],
                name="rms_bay_station_code_uniq",
            )
        ]
        indexes = [
            models.Index(
                fields=["station", "is_active"],
                name="rms_bay_station_active_idx",
            )
        ]

    def __str__(self):
        return f"{self.station.code} / {self.code} - {self.name}"


class Relay(models.Model):
    """Rơ-le thuộc đúng một ngăn lộ, có thể gắn model và hãng sản xuất."""

    bay = models.ForeignKey(
        Bay,
        on_delete=models.PROTECT,
        related_name="relays",
    )
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    model_name = models.CharField(max_length=100, blank=True)
    manufacturer = models.ForeignKey(
        CatalogItem,
        on_delete=models.PROTECT,
        related_name="relays",
        null=True,
        blank=True,
        limit_choices_to={"catalog_type__code": MANUFACTURER_CATALOG_CODE},
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["bay__station__code", "bay__code", "code"]
        constraints = [
            models.UniqueConstraint(
                fields=["bay", "code"],
                name="rms_relay_bay_code_uniq",
            )
        ]
        indexes = [
            models.Index(
                fields=["bay", "is_active"],
                name="rms_relay_bay_active_idx",
            )
        ]

    def clean(self):
        """Chặn chọn CatalogItem không thuộc loại hãng sản xuất."""
        super().clean()
        if self.manufacturer_id and self.manufacturer.catalog_type.code != MANUFACTURER_CATALOG_CODE:
            raise ValidationError(
                {"manufacturer": "Chỉ chọn mục thuộc danh mục hãng sản xuất (MANUFACTURER)."}
            )

    def __str__(self):
        return f"{self.bay.station.code} / {self.bay.code} / {self.code} - {self.name}"
