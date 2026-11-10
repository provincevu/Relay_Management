from django.conf import settings
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from rms.apps.assets.application.scope import user_can_import_catalog
from rms.apps.assets.models import AssetImportRun
from rms.shared.api.exceptions import ApiError


class CatalogItemPreviewRequestSerializer(serializers.Serializer):
    """Kiểm tra các trường yêu cầu trước khi tạo job xem trước Catalog Item."""

    entity_type = serializers.ChoiceField(choices=["catalog_item"])
    mode = serializers.ChoiceField(choices=["preview"])
    file = serializers.FileField()
    source_system = serializers.CharField(required=False, allow_blank=True, max_length=64)


class AssetImportRunSerializer(serializers.ModelSerializer):
    """Chỉ trả trạng thái và báo cáo; không trả đường dẫn/nội dung tệp đã tải lên."""

    status_url = serializers.SerializerMethodField()

    class Meta:
        model = AssetImportRun
        fields = [
            "id",
            "entity_type",
            "mode",
            "status",
            "total_rows",
            "would_create_count",
            "would_link_reference_count",
            "unchanged_count",
            "error_count",
            "row_results",
            "failure_code",
            "created_at",
            "started_at",
            "finished_at",
            "status_url",
        ]
        read_only_fields = fields

    def get_status_url(self, run):
        return f"/api/v2/assets/imports/{run.pk}/"


class AssetImportCreateView(APIView):
    """Nhận file CSV và xếp job xem trước; lát cắt này chưa ghi dữ liệu danh mục."""

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        if not user_can_import_catalog(request.user):
            raise PermissionDenied("An active global asset import grant is required.")

        serializer = CatalogItemPreviewRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uploaded_file = serializer.validated_data["file"]
        if uploaded_file.size > settings.ASSET_IMPORT_MAX_BYTES:
            raise ApiError(
                "The uploaded file exceeds the configured size limit.",
                code="upload_too_large",
                status_code=413,
            )

        with transaction.atomic():
            run = AssetImportRun.objects.create(
                created_by=request.user,
                entity_type=AssetImportRun.EntityType.CATALOG_ITEM,
                mode=AssetImportRun.Mode.PREVIEW,
                source_system=serializer.validated_data.get("source_system", "").strip(),
                uploaded_file=uploaded_file,
            )
            transaction.on_commit(lambda: self._enqueue_preview(run.pk))

        return Response(
            AssetImportRunSerializer(run).data,
            status=status.HTTP_202_ACCEPTED,
        )

    @staticmethod
    def _enqueue_preview(run_id):
        """Đưa job vào Celery; nếu broker lỗi thì lưu trạng thái lỗi và xóa file tạm."""
        from rms.apps.assets.tasks import preview_catalog_item_import_task

        try:
            preview_catalog_item_import_task.delay(run_id)
        except Exception:
            run = AssetImportRun.objects.filter(pk=run_id).first()
            if run is None:
                return
            if run.uploaded_file:
                run.uploaded_file.delete(save=False)
            run.status = AssetImportRun.Status.FAILED
            run.failure_code = "job_queue_unavailable"
            run.finished_at = timezone.now()
            run.error_count = 1
            run.row_results = [
                {
                    "row_number": 0,
                    "outcome": "error",
                    "error_code": "job_queue_unavailable",
                    "message": "Không thể xếp job xử lý. Hãy thử lại sau.",
                    "natural_key": None,
                }
            ]
            run.save(
                update_fields=[
                    "uploaded_file",
                    "status",
                    "failure_code",
                    "finished_at",
                    "error_count",
                    "row_results",
                ]
            )


class AssetImportRunDetailView(APIView):
    """Trả tiến độ và báo cáo cho người tạo job hoặc superuser."""

    permission_classes = [IsAuthenticated]

    def get(self, request, run_id):
        if not user_can_import_catalog(request.user):
            raise PermissionDenied("An active global asset import grant is required.")
        run = get_object_or_404(AssetImportRun, pk=run_id)
        if not request.user.is_superuser and run.created_by_id != request.user.pk:
            raise NotFound("Import run not found.")
        return Response(AssetImportRunSerializer(run).data)
