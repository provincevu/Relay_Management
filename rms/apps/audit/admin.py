from django.contrib import admin

from rms.apps.audit.models import AuditEvent, IdempotencyRecord, OutboxEvent


@admin.register(AuditEvent)
class AuditEventAdmin(admin.ModelAdmin):
    list_display = ["created_at", "action", "target_type", "target_id", "actor"]
    list_filter = ["action", "target_type"]
    search_fields = ["target_id", "request_id", "actor__username"]
    readonly_fields = [field.name for field in AuditEvent._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(OutboxEvent)
class OutboxEventAdmin(admin.ModelAdmin):
    list_display = ["created_at", "event_type", "published_at", "attempts"]
    list_filter = ["event_type", "published_at"]
    readonly_fields = [field.name for field in OutboxEvent._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(IdempotencyRecord)
class IdempotencyRecordAdmin(admin.ModelAdmin):
    list_display = ["created_at", "user", "method", "path", "key", "expires_at"]
    readonly_fields = [field.name for field in IdempotencyRecord._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
