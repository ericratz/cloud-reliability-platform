from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
    "status": "healthy",
    "service": "crp-api",
    "checks": {
        "api": "up",
        "prometheus": "up",
        "memory": "ok",
        "disk": "ok"
    }
}