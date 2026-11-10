from celery import shared_task

from rms.apps.assets.application.import_preview import preview_catalog_item_import


@shared_task
def preview_catalog_item_import_task(run_id):
    """Chạy kiểm tra xem trước trong worker để API có thể trả mã job ngay."""
    return preview_catalog_item_import(run_id)
