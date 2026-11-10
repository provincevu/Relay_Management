from django.apps import AppConfig


class MonitoringConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "rms.apps.monitoring"
    label = "rms_monitoring"
    verbose_name = "Monitoring (Giám sát)"
