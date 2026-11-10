from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required(login_url="/admin/login/"), name="dispatch")
class StationBrowserView(TemplateView):
    """Hiển thị màn hình tra cứu cây Trạm–Ngăn lộ–Rơ-le cho user đã đăng nhập."""

    template_name = "assets/station_browser.html"
