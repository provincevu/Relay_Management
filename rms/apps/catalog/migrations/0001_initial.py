import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CatalogType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=64, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["code"]},
        ),
        migrations.CreateModel(
            name="ExternalReference",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("system", models.CharField(max_length=64)),
                ("entity_type", models.CharField(max_length=128)),
                ("entity_id", models.CharField(max_length=64)),
                ("external_id", models.CharField(max_length=255)),
                ("payload_hash", models.CharField(blank=True, max_length=64)),
                ("last_synced_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["system", "entity_type", "external_id"],
                "indexes": [
                    models.Index(fields=["entity_type", "entity_id"], name="rms_extref_entity_idx")
                ],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("system", "entity_type", "external_id"),
                        name="rms_extref_source_key_uniq",
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name="CatalogItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("sort_order", models.IntegerField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "catalog_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="items",
                        to="rms_catalog.catalogtype",
                    ),
                ),
            ],
            options={
                "ordering": ["catalog_type__code", "sort_order", "code"],
                "indexes": [
                    models.Index(fields=["catalog_type", "is_active", "sort_order"], name="rms_catitem_type_active_idx")
                ],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("catalog_type", "code"),
                        name="rms_catitem_type_code_uniq",
                    )
                ],
            },
        ),
    ]
