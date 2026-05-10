from prometheus_client import Counter, Histogram, Gauge

REQUEST_COUNT = Counter(
    "crp_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "crp_request_duration_seconds",
    "Request latency in seconds",
    ["endpoint", "status"]
)

ERROR_COUNT = Counter(
    "crp_errors_total",
    "Total application errors",
    ["endpoint"]
)

APP_INFO = Gauge(
    "crp_app_info",
    "Application metadata",
    ["service"]
)

SYSTEM_HEALTH = Gauge(
    "crp_system_health",
    "Overall system health status"
)