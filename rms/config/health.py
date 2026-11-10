import logging

import redis
from django.conf import settings
from django.db import connection
from django.http import JsonResponse
from django.views.defaults import page_not_found, server_error

logger = logging.getLogger(__name__)


def health(request):
    """Liveness probe: tiến trình HTTP còn nhận và phản hồi request."""
    return JsonResponse({"status": "ok", "service": "rms-backend"})


def readiness(request):
    """Readiness probe: xác nhận các dependency đồng bộ bắt buộc đang sẵn sàng."""
    checks = {"database": "ok", "redis": "ok"}
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except Exception:
        logger.warning("Database readiness check failed")
        checks["database"] = "unavailable"

    try:
        with redis.Redis.from_url(
            settings.REDIS_URL,
            socket_connect_timeout=2,
            socket_timeout=2,
        ) as redis_client:
            redis_client.ping()
            checks["celery"] = (
                "ok"
                if redis_client.get("rms:platform:celery-heartbeat")
                else "unavailable"
            )
    except Exception:
        logger.warning("Redis readiness check failed")
        checks["redis"] = "unavailable"
        checks["celery"] = "unavailable"

    ready = all(value == "ok" for value in checks.values())
    response = JsonResponse(
        {
            "status": "ready" if ready else "not_ready",
            "service": "rms-backend",
            "checks": checks,
        },
        status=200 if ready else 503,
    )
    return response


def not_found(request, exception):
    """Giữ lỗi route API cùng định dạng JSON; giao diện admin dùng handler Django."""
    if request.path.startswith("/api/"):
        return JsonResponse(
            {
                "error": {
                    "code": "not_found",
                    "message": "The requested API resource was not found.",
                    "details": None,
                },
                "request_id": getattr(request, "request_id", None),
            },
            status=404,
        )
    return page_not_found(request, exception)


def server_error_json(request):
    """Không đưa stack trace lên client; correlation ID giúp tìm lỗi trong log."""
    if request.path.startswith("/api/"):
        return JsonResponse(
            {
                "error": {
                    "code": "internal_error",
                    "message": "An unexpected error occurred.",
                    "details": None,
                },
                "request_id": getattr(request, "request_id", None),
            },
            status=500,
        )
    return server_error(request)
