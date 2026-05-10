import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.observability.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY,
    ERROR_COUNT,
)

class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()

        endpoint = request.url.path
        method = request.method
        status_code = 500

        try:
            response = await call_next(request)
            status_code = response.status_code
            return response

        except Exception:
            try:
                ERROR_COUNT.labels(endpoint=endpoint).inc()
            except Exception:
                pass
            raise

        finally:
            duration = time.time() - start

            #latency
            try:
                REQUEST_LATENCY.labels(
                    endpoint=endpoint,
                    status=str(status_code)
                ).observe(duration)
            except Exception:
                pass

            #request counter
            try:
                REQUEST_COUNT.labels(
                    method=method,
                    endpoint=endpoint,
                    status=str(status_code),
                ).inc()
            except Exception:
                pass

            if status_code >= 500:
                try:
                    ERROR_COUNT.labels(endpoint=endpoint).inc()
                except Exception:
                    pass