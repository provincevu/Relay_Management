from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from rms.apps.identity.models import Organization, RoleGrant, UserProfile

User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    extra = 0


class RoleGrantInline(admin.TabularInline):
    model = RoleGrant
    fk_name = "user"
    extra = 0


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    inlines = [UserProfileInline, RoleGrantInline]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "organization_type", "parent", "is_active"]
    list_filter = ["organization_type", "is_active"]
    search_fields = ["code", "name"]


@admin.register(RoleGrant)
class RoleGrantAdmin(admin.ModelAdmin):
    list_display = ["user", "role_code", "scope_type", "organization", "station_id", "starts_at", "ends_at"]
    list_filter = ["role_code", "scope_type"]
    search_fields = ["user__username", "role_code", "organization__code"]
    readonly_fields = ["granted_by", "created_at"]
