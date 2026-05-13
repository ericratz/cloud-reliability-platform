from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def root(request: Request):
    base = str(request.base_url).rstrip("/")
    return f"""
    <html>
    <head><title>Cloud Reliability Platform</title></head>
    <body>
        <h2>Cloud Reliability Platform</h2>
        <ul>
            <li><a href="{base}/health">Health</a></li>
            <li><a href="{base}/metrics">Metrics</a></li>
            <li><a href="{base}/slo">SLO</a></li>
            <li><a href="{base}/reliability/status">Reliability Status</a></li>
            <li><a href="{base}/docs">API Docs (Swagger)</a></li>
        </ul>
    </body>
    </html>
    """