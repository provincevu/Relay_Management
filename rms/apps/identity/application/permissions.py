from django.db.models import Q
from django.utils import timezone

from rms.apps.identity.models import RoleGrant


def user_has_role(user, role_codes, organization_id=None, station_id=None):
    """Kiểm tra vai trò đang hiệu lực trong đúng phạm vi được yêu cầu."""
    if not user or not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    if isinstance(role_codes, str):
        role_codes = [role_codes]

    now = timezone.now()
    grants = RoleGrant.objects.filter(
        user=user,
        role_code__in=role_codes,
    ).filter(Q(starts_at__isnull=True) | Q(starts_at__lte=now)).filter(
        Q(ends_at__isnull=True) | Q(ends_at__gt=now)
    )

    allowed_scopes = Q(scope_type=RoleGrant.ScopeType.GLOBAL)
    if organization_id:
        # Organization grant chỉ áp dụng cho đúng org; tài sản con phải truyền org sở hữu trực tiếp.
        allowed_scopes |= Q(
            scope_type=RoleGrant.ScopeType.ORGANIZATION,
            organization_id=organization_id,
            organization__is_active=True,
        )
    if station_id:
        allowed_scopes |= Q(
            scope_type=RoleGrant.ScopeType.STATION,
            station_id=station_id,
        )

    return grants.filter(allowed_scopes).exists()
