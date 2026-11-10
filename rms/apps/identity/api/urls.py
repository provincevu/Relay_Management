from django.urls import path

from rms.apps.identity.api.views import CurrentUserView, OrganizationCreateView

urlpatterns = [
    path("me/", CurrentUserView.as_view(), name="identity-current-user"),
    path("organizations/", OrganizationCreateView.as_view(), name="organization-create"),
]
