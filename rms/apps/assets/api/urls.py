from django.urls import path

from rms.apps.assets.api.imports import AssetImportCreateView, AssetImportRunDetailView
from rms.apps.assets.api.views import StationListView, StationTreeView

urlpatterns = [path("stations/", StationListView.as_view(), name="station-list")]
urlpatterns += [
    path("imports/", AssetImportCreateView.as_view(), name="asset-import-create"),
    path("imports/<int:run_id>/", AssetImportRunDetailView.as_view(), name="asset-import-detail"),
    path(
        "stations/<int:station_id>/tree/",
        StationTreeView.as_view(),
        name="station-tree",
    )
]
