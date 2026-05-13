import os
import psutil
from fastapi import APIRouter
from kubernetes import client, config
from app.observability.prom_slo import get_error_rate, get_p95_latency

router = APIRouter()

MEMORY_WARN    = 70 #percent
MEMORY_CRIT    = 90
DISK_WARN      = 70
DISK_CRIT      = 90
ERROR_RATE_WARN  = 0.05  #5%
ERROR_RATE_CRIT  = 0.20  #20%
LATENCY_WARN_MS  = 500
LATENCY_CRIT_MS  = 1000


def classify(value, warn, crit):
    if value >= crit:
        return "critical"
    if value >= warn:
        return "warning"
    return "ok"


def worst(statuses):
    if "critical" in statuses:
        return "critical"
    if "warning" in statuses:
        return "warning"
    return "healthy"


def get_restart_count():
    try:
        config.load_incluster_config()
        v1 = client.CoreV1Api()
        pod = v1.read_namespaced_pod(
            name=os.environ.get("HOSTNAME", ""),
            namespace="default"
        )
        return pod.status.container_statuses[0].restart_count
    except Exception:
        return -1


def check_memory():
    m = psutil.virtual_memory()
    return {
        "status": classify(m.percent, MEMORY_WARN, MEMORY_CRIT),
        "used_mb": round(m.used / 1024**2, 1),
        "total_mb": round(m.total / 1024**2, 1),
        "percent": m.percent,
    }


def check_disk():
    d = psutil.disk_usage("/")
    return {
        "status": classify(d.percent, DISK_WARN, DISK_CRIT),
        "used_gb": round(d.used / 1024**3, 2),
        "total_gb": round(d.total / 1024**3, 2),
        "percent": d.percent,
    }


def check_slo():
    try:
        error_rate = get_error_rate()
        latency_ms = get_p95_latency() * 1000
        return {
            "status": worst([
                classify(error_rate, ERROR_RATE_WARN, ERROR_RATE_CRIT),
                classify(latency_ms, LATENCY_WARN_MS, LATENCY_CRIT_MS),
            ]),
            "error_rate_pct": round(error_rate * 100, 2),
            "p95_latency_ms": round(latency_ms, 2),
        }
    except Exception:
        return {"status": "unknown"}


@router.get("/health")
def health():
    memory = check_memory()
    disk   = check_disk()
    slo    = check_slo()

    return {
        "status": worst([memory["status"], disk["status"], slo["status"]]),
        "service": "crp-api",
        "restart_count": get_restart_count(),
        "checks": {
            "api": "running",
            "memory": memory,
            "disk": disk,
            "slo": slo,
        }
    }