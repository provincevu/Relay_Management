from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.exceptions import ValidationError


class ApiError(APIException):
    """Lỗi API có mã ổn định do ứng dụng định nghĩa."""

    status_code = 400
    default_code = "request_error"
    default_detail = "The request could not be completed."

    def __init__(self, detail=None, *, code=None, status_code=None, details=None):
        if status_code is not None:
            self.status_code = status_code
        self.error_code = code or self.default_code
        self.details = details
        super().__init__(detail or self.default_detail, code=self.error_code)


def api_exception_handler(exc, context):
    """Chuẩn hóa lỗi DRF thành một cấu trúc ổn định có correlation ID."""
    response = drf_exception_handler(exc, context)
    if response is None:
        return None

    request = context.get("request")
    if isinstance(exc, ApiError):
        error_code = exc.error_code
        message = str(exc.detail)
        details = exc.details
    elif isinstance(exc, ValidationError):
        error_code = "validation_error"
        message = "One or more fields are invalid."
        details = response.data
    else:
        error_code = getattr(exc, "default_code", "request_error")
        message = str(exc.detail) if hasattr(exc, "detail") else "The request could not be completed."
        details = None

    response.data = {
        "error": {
            "code": str(error_code),
            "message": message,
            "details": details,
        },
        "request_id": getattr(request, "request_id", None),
    }
    return response
