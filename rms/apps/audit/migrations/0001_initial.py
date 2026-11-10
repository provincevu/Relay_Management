import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="AuditEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("event_id", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("action", models.CharField(max_length=128)),
                ("target_type", models.CharField(max_length=128)),
                ("target_id", models.CharField(max_length=128)),
                ("before", models.JSONField(blank=True, null=True)),
                ("after", models.JSONField(blank=True, null=True)),
                ("reason", models.TextField(blank=True)),
                ("request_id", models.CharField(blank=True, max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "actor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rms_audit_events",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "indexes": [
                    models.Index(fields=["target_type", "target_id", "created_at"], name="rms_audit_target_created_idx")
                ],
            },
        ),
        migrations.CreateModel(
            name="OutboxEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("event_id", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("event_type", models.CharField(max_length=128)),
                ("payload", models.JSONField(default=dict)),
                ("recipient_user_ids", models.JSONField(blank=True, default=list)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("published_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("attempts", models.PositiveIntegerField(default=0)),
                ("last_error", models.TextField(blank=True)),
            ],
            options={"ordering": ["created_at"]},
        ),
        migrations.CreateModel(
            name="IdempotencyRecord",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key", models.CharField(max_length=255)),
                ("method", models.CharField(max_length=10)),
                ("path", models.CharField(max_length=512)),
                ("request_hash", models.CharField(max_length=64)),
                ("response_status", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("response_body", models.JSONField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("expires_at", models.DateTimeField(db_index=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rms_idempotency_records",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "indexes": [models.Index(fields=["expires_at"], name="rms_idempotency_expires_idx")],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("user", "key", "method", "path"),
                        name="rms_idemp_method_path_uniq",
                    )
                ],
            },
        ),
    ]
