from django.db.models import Q
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rms.apps.assets.api.serializers import StationListParamsSerializer, StationListSerializer
from rms.apps.assets.application.scope import (
    get_accessible_station_queryset,
    get_asset_read_grants,
    user_can_access_organization,
)
from rms.apps.assets.models import Station


class StationPagination(PageNumberPagination):
    page_size = 25
    max_page_size = 100


class StationListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StationPagination

    def get(self, request):
        """Trả danh sách trạm đang hoạt động trong phạm vi user được cấp."""
        allowed_params = {"q", "organization", "voltage", "page", "format"}
        unknown_params = set(request.query_params.keys()) - allowed_params
        if unknown_params:
            raise ValidationError(
                {"query_params": f"Unsupported parameter(s): {', '.join(sorted(unknown_params))}."}
            )

        params = StationListParamsSerializer(data=request.query_params)
        params.is_valid(raise_exception=True)
        query = params.validated_data.get("q", "").strip()

        active_grants = get_asset_read_grants(request.user)
        if not request.user.is_superuser and not active_grants.exists():
            raise PermissionDenied("No active role grant provides asset access.")

        stations = get_accessible_station_queryset(request.user).select_related(
            "organization",
            "voltage_level",
            "voltage_level__catalog_type",
        )

        organization_id = params.validated_data.get("organization")
        if organization_id is not None:
            if not user_can_access_organization(request.user, organization_id):
                raise PermissionDenied("You do not have access to this organization.")
            stations = stations.filter(organization_id=organization_id)

        voltage_id = params.validated_data.get("voltage")
        if voltage_id is not None:
            stations = stations.filter(voltage_level_id=voltage_id)

        if query:
            stations = stations.filter(
                Q(code__icontains=query)
                | Q(name__icontains=query)
                | Q(location__icontains=query)
            )

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(stations.order_by("code", "pk"), request, view=self)
        data = StationListSerializer(page, many=True).data
        return paginator.get_paginated_response(data)
