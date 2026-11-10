from django.db import models


class CatalogType(models.Model):
    """Loại danh mục dùng chung, ví dụ cấp điện áp hoặc hãng sản xuất."""

    code = models.CharField("Code (Mã)", max_length=64, unique=True)
    name = models.CharField("Name (Tên)", max_length=255)
    description = models.TextField("Description (Mô tả)", blank=True)
    is_active = models.BooleanField("Active Status (Trạng thái hoạt động)", default=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At (Thời điểm cập nhật)", auto_now=True)

    class Meta:
        verbose_name = "Catalog Type (Loại danh mục)"
        verbose_name_plural = "Catalog Types (Loại danh mục)"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class CatalogItem(models.Model):
    """Giá trị thuộc một loại danh mục, có thể được asset tham chiếu bằng FK."""

    catalog_type = models.ForeignKey(
        CatalogType,
        on_delete=models.PROTECT,
        related_name="items",
        verbose_name="Catalog Type (Loại danh mục)",
    )
    code = models.CharField("Code (Mã)", max_length=100)
    name = models.CharField("Name (Tên)", max_length=255)
    description = models.TextField("Description (Mô tả)", blank=True)
    sort_order = models.IntegerField("Sort Order (Thứ tự sắp xếp)", null=True, blank=True)
    is_active = models.BooleanField("Active Status (Trạng thái hoạt động)", default=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At (Thời điểm cập nhật)", auto_now=True)

    class Meta:
        verbose_name = "Catalog Item (Mục danh mục)"
        verbose_name_plural = "Catalog Items (Mục danh mục)"
        ordering = ["catalog_type__code", "sort_order", "code"]
        constraints = [
            models.UniqueConstraint(
                fields=["catalog_type", "code"],
                name="rms_catitem_type_code_uniq",
            )
        ]
        indexes = [
            models.Index(
                fields=["catalog_type", "is_active", "sort_order"],
                name="rms_catitem_type_active_idx",
            )
        ]

    def __str__(self):
        return f"{self.catalog_type.code}: {self.code} - {self.name}"


class ExternalReference(models.Model):
    """Liên kết một đối tượng RMS với ID của hệ thống bên ngoài."""

    system = models.CharField("System (Hệ thống)", max_length=64)
    entity_type = models.CharField("Entity Type (Loại thực thể)", max_length=128)
    entity_id = models.CharField("Entity ID (Mã thực thể)", max_length=64)
    external_id = models.CharField("External ID (Mã hệ thống ngoài)", max_length=255)
    payload_hash = models.CharField("Payload Hash (Mã băm dữ liệu)", max_length=64, blank=True)
    last_synced_at = models.DateTimeField("Last Synced At (Thời điểm đồng bộ gần nhất)", null=True, blank=True)
    created_at = models.DateTimeField("Created At (Thời điểm tạo)", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At (Thời điểm cập nhật)", auto_now=True)

    class Meta:
        verbose_name = "External Reference (Tham chiếu hệ thống ngoài)"
        verbose_name_plural = "External References (Tham chiếu hệ thống ngoài)"
        ordering = ["system", "entity_type", "external_id"]
        constraints = [
            models.UniqueConstraint(
                fields=["system", "entity_type", "external_id"],
                name="rms_extref_source_key_uniq",
            )
        ]
        indexes = [
            models.Index(
                fields=["entity_type", "entity_id"],
                name="rms_extref_entity_idx",
            )
        ]

    def __str__(self):
        return f"{self.system}: {self.entity_type}/{self.external_id}"
