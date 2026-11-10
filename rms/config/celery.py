import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rms.config.settings")

app = Celery("rms")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(
    ["rms.apps.audit", "rms.apps.ocr", "rms.apps.integrations", "rms.apps.monitoring"]
)
