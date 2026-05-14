import os
import requests
from app.observability.logger import get_logger
logger = get_logger("crp.slo")

PROM_URL = os.getenv(
    "PROM_URL",
    "http://prometheus-server.default.svc.cluster.local:80"
)

def safe_query(promql: str):
    try:
        resp = requests.get(
            f"{PROM_URL}/api/v1/query",
            params={"query": promql},
            timeout=5,
        )
        resp.raise_for_status()
        data = resp.json().get("data", {})
        result = data.get("result", [])

        if not result:
            return 0.0

        value = result[0].get("value", [None, "0"])[1]
        return float(value)

    except Exception as e:
        logger.error("slo_query_failed", extra={"error": str(e), "query": promql})
        return 0.0


def get_availability():
    query = """
    1 - (
        sum(rate(crp_requests_total{status=~"5.."}[2m]))
        /
        clamp_min(sum(rate(crp_requests_total[2m])), 1)
    )
    """
    return safe_query(query)


def get_error_rate():
    query = """
    sum(rate(crp_requests_total{status=~"5.."}[2m]))
    /
    clamp_min(sum(rate(crp_requests_total[2m])), 1)
    """
    return safe_query(query)


def get_p95_latency():
    query = """
    histogram_quantile(
        0.95,
        sum(rate(crp_request_duration_seconds_bucket[2m])) by (le)
    )
    """
    return safe_query(query)