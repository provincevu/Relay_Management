import uuid


class RequestIdMiddleware:
    """Gắn correlation ID cho mỗi HTTP request để tra log và audit."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        supplied_id = request.headers.get("X-Request-ID", "")
        # Chỉ chấp nhận UUID để không đưa dữ liệu tùy ý vào log/header phản hồi.
        try:
            request.request_id = str(uuid.UUID(supplied_id)) if supplied_id else str(uuid.uuid4())
        except (ValueError, AttributeError):
            request.request_id = str(uuid.uuid4())

        response = self.get_response(request)
        response["X-Request-ID"] = request.request_id
        return response
