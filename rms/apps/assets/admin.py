from django.contrib import admin

from rms.apps.assets.models import Bay, Station


class BayInline(admin.TabularInline):
    model = Bay
    extra = 0
    fields = ["code", "name", "rated_voltage", "rated_current", "legacy_sdm", "is_active"]


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "name",
        "organization",
        "voltage_level",
        "is_active",
        "updated_at",
    ]
    list_filter = ["organization", "voltage_level", "is_active"]
    search_fields = ["code", "name", "location", "organization__code", "organization__name"]
    list_select_related = ["organization", "voltage_level", "voltage_level__catalog_type"]
    readonly_fields = ["created_at", "updated_at"]
    inlines = [BayInline]


@admin.register(Bay)
class BayAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "station", "rated_voltage", "rated_current", "is_active"]
    list_filter = ["station", "is_active"]
    search_fields = ["code", "name", "station__code", "station__name"]
    list_select_related = ["station"]
    readonly_fields = ["created_at", "updated_at"]
