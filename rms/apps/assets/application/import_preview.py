import csv
import io
import logging

from django.conf import settings
from django.db import transaction
from django.utils import timezone

from rms.apps.assets.models import AssetImportRun
from rms.apps.audit.models import AuditEvent
from rms.apps.catalog.models import CatalogItem, CatalogType, ExternalReference

CATALOG_ITEM_HEADERS = {
    "catalog_type_code",
    "code",
    "name",
    "description",
    "sort_order",
    "is_active",
    "external_id",
}
CATALOG_ITEM_REQUIRED_HEADERS = {"catalog_type_code", "code", "name"}
CATALOG_ITEM_ENTITY_TYPE = "catalog.catalogitem"
logger = logging.getLogger(__name__)


def preview_catalog_item_import(run_id):
    """Đọc file nhập Catalog Item và lưu báo cáo xem trước, tuyệt đối không ghi CatalogItem."""
    run = AssetImportRun.objects.get(pk=run_id)
    if run.status != AssetImportRun.Status.QUEUED:
        return run.status

    run.status = AssetImportRun.Status.PROCESSING
    run.started_at = timezone.now()
    run.save(update_fields=["status", "started_at"])

    try:
        content = run.uploaded_file.read()
        rows, header_error = _read_csv_rows(content)
        if header_error:
            report = [_row_error(1, header_error[0], header_error[1])]
            _save_preview(run, report, total_rows=0)
            return run.status

        if len(rows) > settings.ASSET_IMPORT_MAX_ROWS:
            report = [
                _row_error(
                    1,
                    "row_limit_exceeded",
                    f"Tệp vượt quá giới hạn {settings.ASSET_IMPORT_MAX_ROWS} dòng dữ liệu.",
                )
            ]
            _save_preview(run, report, total_rows=len(rows))
            return run.status

        report = _validate_catalog_item_rows(rows, run.source_system)
        _save_preview(run, report, total_rows=len(rows))
        return run.status
    except (UnicodeDecodeError, csv.Error):
        report = [_row_error(1, "invalid_csv", "Tệp không phải CSV UTF-8 hợp lệ.")]
        _save_preview(run, report, total_rows=0)
        return run.status
    except Exception:  # Không lưu chi tiết exception có thể chứa nội dung tệp hoặc thông tin hệ thống.
        run.status = AssetImportRun.Status.FAILED
        run.failure_code = "preview_processing_failed"
        run.finished_at = timezone.now()
        run.error_count = max(run.error_count, 1)
        run.row_results = [
            _row_error(0, "preview_processing_failed", "Không thể xử lý tệp. Hãy thử lại hoặc liên hệ quản trị viên.")
        ]
        run.save(
            update_fields=["status", "failure_code", "finished_at", "error_count", "row_results"]
        )
        return run.status
    finally:
        # Tệp chỉ cần tồn tại trong lúc worker tạo báo cáo xem trước.
        try:
            if run.uploaded_file:
                run.uploaded_file.delete(save=False)
                run.save(update_fields=["uploaded_file"])
        except Exception as exc:  # Lỗi dọn tệp không được ghi đè kết quả xem trước đã lưu.
            logger.warning("Asset import file cleanup failed for run %s (%s)", run.pk, type(exc).__name__)


def _read_csv_rows(content):
    """Đọc header và các dòng CSV, phân biệt lỗi cấu trúc với lỗi dữ liệu từng dòng."""
    text = content.decode("utf-8-sig")
    reader = csv.reader(io.StringIO(text, newline=""), delimiter=",", strict=True)
    try:
        header = next(reader)
    except StopIteration:
        return [], ("missing_header", "Tệp CSV đang trống.")

    if len(header) != len(set(header)):
        return [], ("duplicate_header", "Tệp có tên cột bị lặp.")
    missing = CATALOG_ITEM_REQUIRED_HEADERS - set(header)
    unknown = set(header) - CATALOG_ITEM_HEADERS
    if missing or unknown:
        return [], ("invalid_header", "Header CSV không khớp với cấu trúc Catalog Item đã công bố.")

    rows = []
    for row_number, cells in enumerate(reader, start=2):
        if not cells or all(not value.strip() for value in cells):
            continue
        rows.append({"row_number": row_number, "headers": header, "cells": cells})
    return rows, None


def _validate_catalog_item_rows(rows, source_system):
    """Kiểm tra từng dòng, khóa tự nhiên, CatalogType và ExternalReference hiện có."""
    type_codes = set()
    natural_keys = set()
    external_ids = set()
    for row in rows:
        values = _cells_to_dict(row)
        type_codes.add(values.get("catalog_type_code", "").strip())
        if values.get("code", "").strip():
            natural_keys.add((values.get("catalog_type_code", "").strip(), values["code"].strip()))
        if values.get("external_id", "").strip():
            external_ids.add(values["external_id"].strip())

    catalog_types = {
        item.code: item
        for item in CatalogType.objects.filter(code__in=type_codes)
    }
    existing_items = {
        (item.catalog_type.code, item.code): item
        for item in CatalogItem.objects.select_related("catalog_type").filter(
            catalog_type__code__in=type_codes,
            code__in={code for _, code in natural_keys},
        )
    }
    external_references = {}
    if source_system and external_ids:
        external_references = {
            item.external_id: item
            for item in ExternalReference.objects.filter(
                system=source_system,
                entity_type=CATALOG_ITEM_ENTITY_TYPE,
                external_id__in=external_ids,
            )
        }

    seen_keys = set()
    seen_external_ids = {}
    report = []
    for row in rows:
        values = _cells_to_dict(row)
        row_number = row["row_number"]
        if len(row["cells"]) != len(row["headers"]):
            report.append(_row_error(row_number, "invalid_column_count", "Số ô của dòng không khớp với header."))
            continue

        code = values.get("code", "").strip()
        type_code = values.get("catalog_type_code", "").strip()
        name = values.get("name", "").strip()
        description = values.get("description", "").strip()
        external_id = values.get("external_id", "").strip()
        key = (type_code, code)

        missing = [field for field, value in (
            ("catalog_type_code", type_code),
            ("code", code),
            ("name", name),
        ) if not value]
        if missing:
            report.append(
                _row_error(
                    row_number,
                    "required_field_missing",
                    f"Thiếu giá trị bắt buộc: {', '.join(missing)}.",
                    key,
                )
            )
            continue
        if key in seen_keys:
            report.append(_row_error(row_number, "duplicate_in_file", "Catalog Item bị lặp trong tệp.", key))
            continue
        seen_keys.add(key)

        catalog_type = catalog_types.get(type_code)
        if catalog_type is None:
            report.append(_row_error(row_number, "catalog_type_not_found", "Không tìm thấy Catalog Type (Loại danh mục).", key))
            continue

        sort_order = None
        if values.get("sort_order", "").strip():
            order_text = values["sort_order"].strip()
            if not order_text.isdecimal():
                report.append(_row_error(row_number, "invalid_integer", "Sort Order (Thứ tự sắp xếp) phải là số nguyên không âm.", key))
                continue
            try:
                sort_order = int(order_text, 10)
            except ValueError:
                report.append(_row_error(row_number, "invalid_integer", "Sort Order (Thứ tự sắp xếp) phải là số nguyên.", key))
                continue

        is_active = True
        if "is_active" in row["headers"]:
            bool_value = values.get("is_active", "").strip().lower()
            if bool_value not in {"true", "false"}:
                report.append(_row_error(row_number, "invalid_boolean", "Is Active chỉ nhận true hoặc false.", key))
                continue
            is_active = bool_value == "true"

        existing = existing_items.get(key)
        reference = external_references.get(external_id) if external_id else None
        if external_id and not source_system:
            report.append(_row_error(row_number, "missing_source_system", "Khi có External ID cần truyền source_system.", key))
            continue
        if external_id and source_system:
            prior_key = seen_external_ids.get(external_id)
            if prior_key is not None and prior_key != key:
                report.append(
                    _row_result(
                        row_number,
                        "conflict",
                        "duplicate_external_id_in_file",
                        "External ID bị gán cho nhiều Catalog Item trong cùng tệp.",
                        key,
                    )
                )
                continue
            seen_external_ids[external_id] = key
        if reference and (existing is None or str(reference.entity_id) != str(existing.pk)):
            report.append(_row_result(row_number, "conflict", "external_reference_conflict", "External ID đã liên kết với Catalog Item khác.", key))
            continue

        if existing is not None:
            matches = (
                existing.name == name
                and existing.description == description
                and existing.sort_order == sort_order
                and existing.is_active == is_active
            )
            if matches:
                if external_id and reference is None:
                    report.append(_row_result(row_number, "would_link_reference", None, "Catalog Item trùng khớp; cần tạo liên kết External Reference.", key))
                else:
                    report.append(_row_result(row_number, "unchanged", None, "Dữ liệu trùng khớp với Catalog Item hiện có.", key))
            else:
                report.append(_row_result(row_number, "conflict", "existing_value_conflict", "Catalog Item đã tồn tại nhưng có dữ liệu khác.", key))
            continue

        report.append(_row_result(row_number, "would_create", None, "Dòng hợp lệ; chưa ghi vào cơ sở dữ liệu.", key))

    return report


def _cells_to_dict(row):
    """Ghép từng ô theo header; ô thiếu được giữ thành chuỗi trống để báo lỗi rõ ràng."""
    return {
        header: row["cells"][index] if index < len(row["cells"]) else ""
        for index, header in enumerate(row["headers"])
    }


def _row_error(row_number, code, message, key=None):
    return _row_result(row_number, "error", code, message, key)


def _row_result(row_number, outcome, code, message, key=None):
    return {
        "row_number": row_number,
        "outcome": outcome,
        "error_code": code,
        "message": message,
        "natural_key": {"catalog_type_code": key[0], "code": key[1]} if key else None,
    }


def _save_preview(run, report, total_rows):
    """Ghi duy nhất trạng thái/báo cáo import; không tạo hoặc sửa dữ liệu Catalog Item."""
    errors = sum(item["outcome"] in {"error", "conflict"} for item in report)
    would_create = sum(item["outcome"] == "would_create" for item in report)
    would_link_reference = sum(item["outcome"] == "would_link_reference" for item in report)
    unchanged = sum(item["outcome"] == "unchanged" for item in report)
    with transaction.atomic():
        run.status = AssetImportRun.Status.PREVIEWED
        run.total_rows = total_rows
        run.would_create_count = would_create
        run.would_link_reference_count = would_link_reference
        run.unchanged_count = unchanged
        run.error_count = errors
        run.row_results = report
        run.finished_at = timezone.now()
        run.save(
            update_fields=[
                "status",
                "total_rows",
                "would_create_count",
                "would_link_reference_count",
                "unchanged_count",
                "error_count",
                "row_results",
                "finished_at",
            ]
        )
        AuditEvent.objects.create(
            actor=run.created_by,
            action="asset_import.previewed",
            target_type="assets.assetimportrun",
            target_id=str(run.pk),
            after={"entity_type": run.entity_type, "status": run.status, "row_count": total_rows},
        )
