from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from rms.apps.assets.application.scope import user_can_import_catalog


@method_decorator(login_required(login_url="/admin/login/"), name="dispatch")
class StationBrowserView(TemplateView):
    """Hiển thị màn hình tra cứu cây Trạm–Ngăn lộ–Rơ-le cho user đã đăng nhập."""

    template_name = "assets/station_browser.html"


@method_decorator(login_required(login_url="/admin/login/"), name="dispatch")
class AssetImportPageView(TemplateView):
    """Hiển thị biểu mẫu CSV cho người có quyền xem trước nhập danh mục."""

    template_name = "assets/catalog_import.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["max_file_bytes"] = settings.ASSET_IMPORT_MAX_BYTES
        context["max_file_size_label"] = f"{settings.ASSET_IMPORT_MAX_BYTES / 1024 / 1024:g} MiB"
        return context

    def dispatch(self, request, *args, **kwargs):
        if not user_can_import_catalog(request.user):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
