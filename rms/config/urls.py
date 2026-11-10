from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from rms.apps.assets.ui.views import StationBrowserView
from rms.config.health import health, not_found, readiness, server_error_json

urlpatterns = [
    path("health", health, name="health"),
    path("health/", health, name="health-slash"),
    path("ready", readiness, name="readiness"),
    path("ready/", readiness, name="readiness-slash"),
    path("admin/", admin.site.urls),
    path("assets/", StationBrowserView.as_view(), name="asset-browser"),
    path("api/v2/", include("rms.config.api_urls")),
]

admin.site.site_header = "RMS (Hệ thống quản lý rơ-le)"
admin.site.site_title = "Administration (Quản trị) · RMS"
admin.site.index_title = "Business Data (Dữ liệu nghiệp vụ)"

# Django Admin và trang asset dùng staticfiles trong môi trường local DEBUG.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

handler404 = not_found
handler500 = server_error_json
