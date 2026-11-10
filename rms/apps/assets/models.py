from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models

from rms.apps.catalog.models import CatalogItem
from rms.apps.identity.models import Organization

VOLTAGE_LEVEL_CATALOG_CODE = "VOLTAGE_LEVEL"
MANUFACTURER_CATALOG_CODE = "MANUFACTURER"


class Station(models.Model):
    """Trạm thuộc một đơn vị, có mã nội bộ và cấp điện áp chính tùy chọn."""

    code = models.CharField("Code (Mã)", max_length=64, unique=True)
    name = models.CharField("Name (Tên)", max_length=255)
    location = models.CharField("Location (Địa điểm)", max_length=255, blank=True)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="stations",
        verbose_name="Organization (Đơn vị)",
    )
    voltage_level = models.ForeignKey(
        CatalogItem,
        on_delete=models.PROTECT,
        related_name="stations",
        null=True,
        blank=True,
        limit_choices_to={"catalog_type__code": VOLTAGE_LEVEL_CATALOG_CODE},
        verbose_name="Voltage Level (Cấp điện áp)",
    )
    commissioned_at = models.DateTimeField("Commissioned At (Thời điểm đưa vào vận hành)", null=True, blank=True)
    installed_at = models.DateTimeField("Installed At (Thời điểm lắp đặt)", null=True, blank=True)
    is_active = models.BooleanField("Active Status (Trạng thái hoạt động)", default=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At (Thời điểm cập nhật)", auto_now=True)

    class Meta:
        verbose_name = "Station (Trạm)"
        verbose_name_plural = "Stations (Trạm)"
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
        verbose_name="Station (Trạm)",
    )
    code = models.CharField("Code (Mã)", max_length=64)
    name = models.CharField("Name (Tên)", max_length=255)
    rated_voltage = models.CharField("Rated Voltage (Điện áp định mức)", max_length=50, blank=True)
    rated_current = models.CharField("Rated Current (Dòng điện định mức)", max_length=50, blank=True)
    # Giữ nguyên giá trị SDM cũ đến khi ý nghĩa và đơn vị của nó được xác định.
    legacy_sdm = models.CharField(
        "Legacy SDM (Giá trị SDM cũ)",
        max_length=50,
        blank=True,
        help_text="Giá trị nguồn SDM; chưa chuẩn hóa ý nghĩa hoặc đơn vị.",
    )
    is_active = models.BooleanField("Active Status (Trạng thái hoạt động)", default=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At (Thời điểm cập nhật)", auto_now=True)

    class Meta:
        verbose_name = "Bay (Ngăn lộ)"
        verbose_name_plural = "Bays (Ngăn lộ)"
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
        verbose_name="Bay (Ngăn lộ)",
    )
    code = models.CharField("Code (Mã)", max_length=64)
    name = models.CharField("Name (Tên)", max_length=255)
    model_name = models.CharField("Model Name (Tên model)", max_length=100, blank=True)
    manufacturer = models.ForeignKey(
        CatalogItem,
        on_delete=models.PROTECT,
        related_name="relays",
        null=True,
        blank=True,
        limit_choices_to={"catalog_type__code": MANUFACTURER_CATALOG_CODE},
        verbose_name="Manufacturer (Nhà sản xuất)",
    )
    is_active = models.BooleanField("Active Status (Trạng thái hoạt động)", default=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At (Thời điểm cập nhật)", auto_now=True)

    class Meta:
        verbose_name = "Relay (Rơ-le)"
        verbose_name_plural = "Relays (Rơ-le)"
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


class AssetImportRun(models.Model):
    """Lưu trạng thái và báo cáo của một lần nhập danh mục/tài sản."""

    class EntityType(models.TextChoices):
        CATALOG_ITEM = "catalog_item", "Catalog Item (Mục danh mục)"
        STATION = "station", "Station (Trạm)"
        BAY = "bay", "Bay (Ngăn lộ)"
        RELAY = "relay", "Relay (Rơ-le)"

    class Mode(models.TextChoices):
        PREVIEW = "preview", "Preview (Xem trước)"
        APPLY = "apply", "Apply (Áp dụng)"

    class Status(models.TextChoices):
        QUEUED = "QUEUED", "Queued (Đang chờ)"
        PROCESSING = "PROCESSING", "Processing (Đang xử lý)"
        PREVIEWED = "PREVIEWED", "Previewed (Đã xem trước)"
        COMPLETED = "COMPLETED", "Completed (Đã hoàn tất)"
        REJECTED = "REJECTED", "Rejected (Bị từ chối)"
        FAILED = "FAILED", "Failed (Thất bại)"

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="asset_import_runs",
        null=True,
        verbose_name="Created By (Người tạo)",
    )
    entity_type = models.CharField(
        "Entity Type (Loại thực thể)",
        max_length=32,
        choices=EntityType.choices,
    )
    mode = models.CharField("Mode (Chế độ)", max_length=16, choices=Mode.choices)
    status = models.CharField(
        "Status (Trạng thái)",
        max_length=16,
        choices=Status.choices,
        default=Status.QUEUED,
        db_index=True,
    )
    source_system = models.CharField("Source System (Hệ thống nguồn)", max_length=64, blank=True)
    uploaded_file = models.FileField(
        "Uploaded File (Tệp đã tải lên)",
        upload_to="asset-imports/pending/",
        blank=True,
    )
    total_rows = models.PositiveIntegerField("Total Rows (Tổng số dòng)", default=0)
    would_create_count = models.PositiveIntegerField("Would Create (Số mục dự kiến tạo)", default=0)
    would_link_reference_count = models.PositiveIntegerField(
        "Would Link Reference (Số liên kết dự kiến tạo)",
        default=0,
    )
    unchanged_count = models.PositiveIntegerField("Unchanged (Số mục không đổi)", default=0)
    error_count = models.PositiveIntegerField("Errors (Số dòng lỗi)", default=0)
    row_results = models.JSONField("Row Results (Kết quả từng dòng)", default=list, blank=True)
    failure_code = models.CharField("Failure Code (Mã lỗi xử lý)", max_length=64, blank=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    started_at = models.DateTimeField("Started At (Thời điểm bắt đầu)", null=True, blank=True)
    finished_at = models.DateTimeField("Finished At (Thời điểm kết thúc)", null=True, blank=True)

    class Meta:
        verbose_name = "Asset Import Run (Lần nhập tài sản)"
        verbose_name_plural = "Asset Import Runs (Các lần nhập tài sản)"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["created_by", "created_at"], name="rms_asset_import_user_idx"),
        ]

    def __str__(self):
        return f"{self.entity_type}/{self.mode}: {self.pk} ({self.status})"
