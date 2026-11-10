import django.db.models.deletion
from django.db import migrations, models


def seed_voltage_level_type(apps, schema_editor):
    """Tạo loại catalog cấp điện áp cần thiết cho trường Station.voltage_level."""
    CatalogType = apps.get_model("rms_catalog", "CatalogType")
    CatalogType.objects.using(schema_editor.connection.alias).get_or_create(
        code="VOLTAGE_LEVEL",
        defaults={
            "name": "Cấp điện áp",
            "description": "Danh mục cấp điện áp tham chiếu bởi trạm.",
            "is_active": True,
        },
    )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("rms_catalog", "0001_initial"),
        ("rms_identity", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Station",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=64, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(blank=True, max_length=255)),
                ("commissioned_at", models.DateTimeField(blank=True, null=True)),
                ("installed_at", models.DateTimeField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="stations",
                        to="rms_identity.organization",
                    ),
                ),
                (
                    "voltage_level",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"catalog_type__code": "VOLTAGE_LEVEL"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="stations",
                        to="rms_catalog.catalogitem",
                    ),
                ),
            ],
            options={
                "ordering": ["code"],
                "indexes": [
                    models.Index(
                        fields=["organization", "is_active"],
                        name="rms_station_org_active_idx",
                    )
                ],
            },
        ),
        migrations.RunPython(seed_voltage_level_type, migrations.RunPython.noop),
    ]
