from django.urls import path

from rms.apps.assets.api.views import StationListView, StationTreeView

urlpatterns = [path("stations/", StationListView.as_view(), name="station-list")]
urlpatterns += [
    path(
        "stations/<int:station_id>/tree/",
        StationTreeView.as_view(),
        name="station-tree",
    )
]
