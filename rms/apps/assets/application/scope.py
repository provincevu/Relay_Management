from django.conf import settings
from django.db.models import Q
from django.utils import timezone

from rms.apps.assets.models import Station
from rms.apps.identity.models import RoleGrant


def get_active_role_grants(user):
    """Trả về các grant có hiệu lực tại thời điểm hiện tại."""
    now = timezone.now()
    return RoleGrant.objects.filter(user=user).filter(
        Q(starts_at__isnull=True) | Q(starts_at__lte=now)
    ).filter(Q(ends_at__isnull=True) | Q(ends_at__gt=now))


def get_asset_read_grants(user):
    """Chỉ nhận grant thuộc các role được phép đọc asset trong cấu hình."""
    return get_active_role_grants(user).filter(role_code__in=settings.ASSET_READ_ROLE_CODES)


def user_can_import_catalog(user):
    """Chỉ cho phép superuser hoặc role được cấu hình có grant toàn cục nhập Catalog."""
    if user.is_superuser:
        return True
    return get_active_role_grants(user).filter(
        role_code__in=settings.ASSET_IMPORT_ROLE_CODES,
        scope_type=RoleGrant.ScopeType.GLOBAL,
    ).exists()


def get_accessible_station_queryset(user):
    """Lọc trạm theo grant toàn cục, tổ chức trực tiếp hoặc trạm cụ thể."""
    stations = Station.objects.filter(
        is_active=True,
        organization__is_active=True,
    )
    if user.is_superuser:
        return stations

    grants = get_asset_read_grants(user)
    if grants.filter(scope_type=RoleGrant.ScopeType.GLOBAL).exists():
        return stations

    # Organization grant chỉ khớp org trực tiếp; không kế thừa xuống node con.
    organization_ids = grants.filter(
        scope_type=RoleGrant.ScopeType.ORGANIZATION,
        organization__is_active=True,
    ).values("organization_id")
    station_ids = grants.filter(
        scope_type=RoleGrant.ScopeType.STATION,
    ).values("station_id")
    return stations.filter(
        Q(organization_id__in=organization_ids) | Q(pk__in=station_ids)
    )


def user_can_access_organization(user, organization_id):
    """Kiểm tra quyền vào org trực tiếp, kể cả org chưa có trạm nào."""
    if user.is_superuser:
        return True

    grants = get_asset_read_grants(user)
    if grants.filter(scope_type=RoleGrant.ScopeType.GLOBAL).exists():
        return True
    if grants.filter(
        scope_type=RoleGrant.ScopeType.ORGANIZATION,
        organization_id=organization_id,
        organization__is_active=True,
    ).exists():
        return True

    station_ids = grants.filter(
        scope_type=RoleGrant.ScopeType.STATION,
    ).values("station_id")
    return Station.objects.filter(
        pk__in=station_ids,
        organization_id=organization_id,
        is_active=True,
        organization__is_active=True,
    ).exists()
