from django.db.models import Q
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rms.apps.identity.api.serializers import (
    OrganizationSerializer,
    RoleGrantSerializer,
    UserProfileSerializer,
)
from rms.apps.identity.application.organizations import create_organization
from rms.apps.identity.models import RoleGrant, UserProfile
from rms.shared.api.idempotency import execute_idempotent


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Trả về user, đơn vị và các vai trò đang hiệu lực của phiên hiện tại."""
        now = timezone.now()
        profile = UserProfile.objects.select_related("organization").filter(user=request.user).first()
        grants = RoleGrant.objects.filter(user=request.user).filter(
            Q(starts_at__isnull=True) | Q(starts_at__lte=now)
        ).filter(
            Q(ends_at__isnull=True) | Q(ends_at__gt=now)
        )
        return Response(
            {
                "id": request.user.pk,
                "username": request.user.get_username(),
                "email": request.user.email,
                "is_staff": request.user.is_staff,
                "profile": UserProfileSerializer(
                    {
                        "organization_id": profile.organization_id if profile else None,
                        "organization_name": profile.organization.name if profile and profile.organization else None,
                        "home_station_id": profile.home_station_id if profile else None,
                        "phone_number": profile.phone_number if profile else "",
                    }
                ).data,
                "roles": RoleGrantSerializer(
                    [
                        {
                            "role_code": grant.role_code,
                            "scope_type": grant.scope_type,
                            "organization_id": grant.organization_id,
                            "station_id": grant.station_id,
                            "starts_at": grant.starts_at,
                            "ends_at": grant.ends_at,
                        }
                        for grant in grants.select_related("organization")
                    ],
                    many=True,
                ).data,
            }
        )


class OrganizationCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        """Tạo Organization quản trị với kiểm tra trùng lặp theo Idempotency-Key."""

        def create():
            serializer = OrganizationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            organization = create_organization(
                actor=request.user,
                data=serializer.validated_data,
                request_id=request.request_id,
            )
            return Response(OrganizationSerializer(organization).data, status=status.HTTP_201_CREATED)

        return execute_idempotent(request, create)
