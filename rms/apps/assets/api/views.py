from django.db.models import Prefetch, Q
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rms.apps.assets.api.serializers import (
    BayTreeSerializer,
    StationListParamsSerializer,
    StationListSerializer,
    StationTreeParamsSerializer,
)
from rms.apps.assets.application.scope import (
    get_accessible_station_queryset,
    get_asset_read_grants,
    user_can_access_organization,
)
from rms.apps.assets.models import Bay, Relay, Station


class StationPagination(PageNumberPagination):
    page_size = 25
    max_page_size = 100


class StationTreePagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
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


class StationTreeView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StationTreePagination

    def get(self, request, station_id):
        """Trả cây tài sản một trạm; scope được kiểm tra trước khi truy xuất Bay."""
        allowed_params = {"depth", "q", "page", "page_size", "format"}
        unknown_params = set(request.query_params.keys()) - allowed_params
        if unknown_params:
            raise ValidationError(
                {"query_params": f"Unsupported parameter(s): {', '.join(sorted(unknown_params))}."}
            )

        params = StationTreeParamsSerializer(data=request.query_params)
        params.is_valid(raise_exception=True)
        depth = params.validated_data["depth"]
        query = params.validated_data.get("q", "").strip()

        station = (
            get_accessible_station_queryset(request.user)
            .select_related("organization", "voltage_level", "voltage_level__catalog_type")
            .filter(pk=station_id)
            .first()
        )
        if station is None:
            station_exists = Station.objects.filter(
                pk=station_id,
                is_active=True,
                organization__is_active=True,
            ).exists()
            if station_exists:
                raise PermissionDenied("You do not have access to this station.")
            raise NotFound("Station not found.")

        bays = Bay.objects.filter(station=station, is_active=True)
        if query:
            bays = bays.filter(Q(code__icontains=query) | Q(name__icontains=query))
        bays = bays.order_by("code", "pk")

        if depth == "relays":
            active_relays = Relay.objects.filter(is_active=True).select_related(
                "manufacturer",
                "manufacturer__catalog_type",
            ).order_by("code", "pk")
            bays = bays.prefetch_related(
                Prefetch("relays", queryset=active_relays, to_attr="active_relays")
            )

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(bays, request, view=self)
        bay_data = BayTreeSerializer(
            page,
            many=True,
            context={"depth": depth},
        ).data
        response = paginator.get_paginated_response(bay_data)
        response.data["station"] = StationListSerializer(station).data
        response.data["depth"] = depth
        return response
