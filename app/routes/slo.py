from fastapi import APIRouter
from app.observability.prom_slo import (
    get_availability,
    get_error_rate,
    get_p95_latency,
)

router = APIRouter()

@router.get("/slo")
def slo():
    availability = get_availability()
    error_rate = get_error_rate()
    latency = get_p95_latency()

    return {
        "availability_percent": round(availability * 100, 2),
        "error_rate_percent": round(error_rate * 100, 2),
        "p95_latency_ms": round(latency * 1000, 2),
    }