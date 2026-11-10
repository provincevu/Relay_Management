from django.contrib import admin
from django.urls import include, path

from rms.config.health import health, not_found, readiness, server_error_json

urlpatterns = [
    path("health", health, name="health"),
    path("health/", health, name="health-slash"),
    path("ready", readiness, name="readiness"),
    path("ready/", readiness, name="readiness-slash"),
    path("admin/", admin.site.urls),
    path("api/v2/", include("rms.config.api_urls")),
]

handler404 = not_found
handler500 = server_error_json
