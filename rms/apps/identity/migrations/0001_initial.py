import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=64, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("organization_type", models.CharField(blank=True, max_length=64)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="rms_identity.organization",
                    ),
                ),
            ],
            options={"ordering": ["code"]},
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("home_station_id", models.CharField(blank=True, max_length=64, null=True)),
                ("phone_number", models.CharField(blank=True, max_length=32)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "organization",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_profiles",
                        to="rms_identity.organization",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rms_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RoleGrant",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("role_code", models.CharField(max_length=64)),
                ("scope_type", models.CharField(choices=[("GLOBAL", "Global"), ("ORGANIZATION", "Organization"), ("STATION", "Station")], max_length=16)),
                ("station_id", models.CharField(blank=True, max_length=64, null=True)),
                ("starts_at", models.DateTimeField(blank=True, null=True)),
                ("ends_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "granted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="granted_rms_roles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="role_grants",
                        to="rms_identity.organization",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rms_role_grants",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(fields=["user", "role_code", "scope_type"], name="rms_user_role_scope_idx"),
                    models.Index(fields=["organization", "role_code"], name="rms_org_role_idx"),
                ],
                "constraints": [
                    models.CheckConstraint(
                        condition=(
                            models.Q(scope_type="GLOBAL", organization__isnull=True, station_id__isnull=True)
                            | models.Q(scope_type="ORGANIZATION", organization__isnull=False, station_id__isnull=True)
                            | models.Q(scope_type="STATION", station_id__isnull=False)
                        ),
                        name="rms_role_grant_scope_valid",
                    ),
                    models.CheckConstraint(
                        condition=models.Q(ends_at__isnull=True)
                        | models.Q(starts_at__isnull=True)
                        | models.Q(ends_at__gt=models.F("starts_at")),
                        name="rms_role_grant_dates_ordered",
                    ),
                ],
            },
        ),
    ]
