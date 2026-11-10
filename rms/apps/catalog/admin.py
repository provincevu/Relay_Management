from django.contrib import admin

from rms.apps.catalog.models import CatalogItem, CatalogType, ExternalReference


class CatalogItemInline(admin.TabularInline):
    model = CatalogItem
    extra = 0
    fields = ["code", "name", "sort_order", "is_active", "description"]


@admin.register(CatalogType)
class CatalogTypeAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "is_active", "updated_at"]
    list_filter = ["is_active"]
    search_fields = ["code", "name"]
    readonly_fields = ["created_at", "updated_at"]
    inlines = [CatalogItemInline]


@admin.register(CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "catalog_type", "sort_order", "is_active", "updated_at"]
    list_filter = ["catalog_type", "is_active"]
    search_fields = ["code", "name", "catalog_type__code", "catalog_type__name"]
    list_select_related = ["catalog_type"]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(ExternalReference)
class ExternalReferenceAdmin(admin.ModelAdmin):
    list_display = ["system", "entity_type", "entity_id", "external_id", "last_synced_at"]
    list_filter = ["system", "entity_type"]
    search_fields = ["system", "entity_type", "entity_id", "external_id"]
    readonly_fields = ["created_at", "updated_at"]
