from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": "Cloud Reliability Platform running",
        "status": "ok"
    }