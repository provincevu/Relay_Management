from django.urls import include, path
from rest_framework.response import Response
from rest_framework.views import APIView


class ApiIndexView(APIView):
    """Temporary API index while feature endpoints are added by vertical slice."""

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response({"service": "rms-api", "version": "v2", "status": "scaffold"})


urlpatterns = [
    path("", ApiIndexView.as_view(), name="api-index"),
    path("identity/", include("rms.apps.identity.api.urls")),
    path("catalog/", include("rms.apps.catalog.api.urls")),
    path("assets/", include("rms.apps.assets.api.urls")),
    path("sheets/", include("rms.apps.sheets.api.urls")),
    path("ocr/", include("rms.apps.ocr.api.urls")),
    path("monitoring/", include("rms.apps.monitoring.api.urls")),
    path("integrations/", include("rms.apps.integrations.api.urls")),
    path("notifications/", include("rms.apps.notifications.api.urls")),
    path("audit/", include("rms.apps.audit.api.urls")),
]
