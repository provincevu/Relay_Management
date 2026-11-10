from django.contrib import admin

from rms.apps.assets.models import Station


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
