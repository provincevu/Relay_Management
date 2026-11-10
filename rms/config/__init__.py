"""Gói cấu hình dự án Django."""

from .celery import app as celery_app

__all__ = ("celery_app",)
