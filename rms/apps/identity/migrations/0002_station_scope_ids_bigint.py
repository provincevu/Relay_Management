from django.db import migrations, models

MAX_BIGINT = 9223372036854775807
BATCH_SIZE = 500


def validate_and_normalize_station_ids(apps, schema_editor):
    """Kiểm tra ID cũ trước, rồi chuẩn hóa chuỗi số để PostgreSQL đổi kiểu an toàn."""
    database = schema_editor.connection.alias
    UserProfile = apps.get_model("rms_identity", "UserProfile")
    RoleGrant = apps.get_model("rms_identity", "RoleGrant")
    fields_to_check = [
        (UserProfile, "home_station_id"),
        (RoleGrant, "station_id"),
    ]
    invalid_values = []

    # Kiểm tra toàn bộ dữ liệu trước khi sửa bất kỳ dòng nào.
    for model, field_name in fields_to_check:
        rows = model.objects.using(database).values_list("pk", field_name).iterator(
            chunk_size=BATCH_SIZE
        )
        for row_id, value in rows:
            if value is None or not str(value).strip():
                continue
            normalized_value = str(value).strip()
            if (
                not normalized_value
                or not normalized_value.isascii()
                or not normalized_value.isdigit()
                or int(normalized_value) < 1
                or int(normalized_value) > MAX_BIGINT
            ):
                if len(invalid_values) < 20:
                    invalid_values.append(
                        f"{model._meta.label}.{field_name} pk={row_id}: {value!r}"
                    )

    if invalid_values:
        details = "\n".join(invalid_values)
        raise RuntimeError(
            "Không thể đổi station ID sang số nguyên dương. "
            "Hãy kiểm tra các giá trị sau (tối đa 20 dòng), đặt về NULL hoặc sửa thành ID Station dạng số dương, "
            "rồi chạy lại migrate:\n" + details
        )

    # Chuyển chuỗi rỗng thành NULL và loại bỏ khoảng trắng/zero đầu để cast ổn định.
    for model, field_name in fields_to_check:
        batch = []
        rows = model.objects.using(database).values_list("pk", field_name).iterator(
            chunk_size=BATCH_SIZE
        )
        for row_id, value in rows:
            normalized_value = (
                None
                if value is None or not str(value).strip()
                else str(int(str(value).strip()))
            )
            if normalized_value == value:
                continue
            instance = model(pk=row_id)
            setattr(instance, field_name, normalized_value)
            batch.append(instance)
            if len(batch) >= BATCH_SIZE:
                model.objects.using(database).bulk_update(batch, [field_name], batch_size=BATCH_SIZE)
                batch.clear()
        if batch:
            model.objects.using(database).bulk_update(batch, [field_name], batch_size=BATCH_SIZE)


class Migration(migrations.Migration):
    dependencies = [("rms_identity", "0001_initial")]

    operations = [
        migrations.RunPython(
            validate_and_normalize_station_ids,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="home_station_id",
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="rolegrant",
            name="station_id",
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
