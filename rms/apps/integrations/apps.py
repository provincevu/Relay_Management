from django.apps import AppConfig


class IntegrationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "rms.apps.integrations"
    label = "rms_integrations"
    verbose_name = "Integrations (Tích hợp hệ thống)"
