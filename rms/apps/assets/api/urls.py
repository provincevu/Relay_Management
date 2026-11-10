from django.urls import path

from rms.apps.assets.api.views import StationListView

urlpatterns = [path("stations/", StationListView.as_view(), name="station-list")]
