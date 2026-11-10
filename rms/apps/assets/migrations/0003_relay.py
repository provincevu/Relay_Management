import django.db.models.deletion
from django.db import migrations, models


def seed_manufacturer_type(apps, schema_editor):
    """Tạo loại danh mục hãng sản xuất dùng bởi Relay.manufacturer."""
    CatalogType = apps.get_model("rms_catalog", "CatalogType")
    CatalogType.objects.using(schema_editor.connection.alias).get_or_create(
        code="MANUFACTURER",
        defaults={
            "name": "Hãng sản xuất",
            "description": "Danh mục hãng sản xuất tham chiếu bởi rơ-le.",
            "is_active": True,
        },
    )


class Migration(migrations.Migration):
    dependencies = [
        ("rms_assets", "0002_bay"),
        ("rms_catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Relay",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=64)),
                ("name", models.CharField(max_length=255)),
                ("model_name", models.CharField(blank=True, max_length=100)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bay",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="relays",
                        to="rms_assets.bay",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"catalog_type__code": "MANUFACTURER"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="relays",
                        to="rms_catalog.catalogitem",
                    ),
                ),
            ],
            options={
                "ordering": ["bay__station__code", "bay__code", "code"],
                "indexes": [
                    models.Index(
                        fields=["bay", "is_active"],
                        name="rms_relay_bay_active_idx",
                    )
                ],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("bay", "code"),
                        name="rms_relay_bay_code_uniq",
                    )
                ],
            },
        ),
        migrations.RunPython(seed_manufacturer_type, migrations.RunPython.noop),
    ]
