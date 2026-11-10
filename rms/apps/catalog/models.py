from django.db import models


class CatalogType(models.Model):
    """Loại danh mục dùng chung, ví dụ cấp điện áp hoặc hãng sản xuất."""

    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class CatalogItem(models.Model):
    """Giá trị thuộc một loại danh mục, có thể được asset tham chiếu bằng FK."""

    catalog_type = models.ForeignKey(
        CatalogType,
        on_delete=models.PROTECT,
        related_name="items",
    )
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
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

    system = models.CharField(max_length=64)
    entity_type = models.CharField(max_length=128)
    entity_id = models.CharField(max_length=64)
    external_id = models.CharField(max_length=255)
    payload_hash = models.CharField(max_length=64, blank=True)
    last_synced_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
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
