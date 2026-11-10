import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("rms_assets", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Bay",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=64)),
                ("name", models.CharField(max_length=255)),
                ("rated_voltage", models.CharField(blank=True, max_length=50)),
                ("rated_current", models.CharField(blank=True, max_length=50)),
                (
                    "legacy_sdm",
                    models.CharField(
                        blank=True,
                        help_text="Giá trị nguồn SDM; chưa chuẩn hóa ý nghĩa hoặc đơn vị.",
                        max_length=50,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="bays",
                        to="rms_assets.station",
                    ),
                ),
            ],
            options={
                "ordering": ["station__code", "code"],
                "indexes": [
                    models.Index(
                        fields=["station", "is_active"],
                        name="rms_bay_station_active_idx",
                    )
                ],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("station", "code"),
                        name="rms_bay_station_code_uniq",
                    )
                ],
            },
        )
    ]
