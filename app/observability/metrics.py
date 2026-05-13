from prometheus_client import Counter, Histogram, Gauge, CollectorRegistry, disable_created_metrics

disable_created_metrics()

REGISTRY = CollectorRegistry()

REQUEST_COUNT = Counter(
    "crp_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
    registry=REGISTRY
)

REQUEST_LATENCY = Histogram(
    "crp_request_duration_seconds",
    "Request latency in seconds",
    ["endpoint", "status"],
    registry=REGISTRY
)

ERROR_COUNT = Counter(
    "crp_errors_total",
    "Total application errors",
    ["endpoint"],
    registry=REGISTRY
)

APP_INFO = Gauge(
    "crp_app_info",
    "Application metadata",
    ["service"],
    registry=REGISTRY
)

SYSTEM_HEALTH = Gauge(
    "crp_system_health",
    "Overall system health status",
    registry=REGISTRY
)