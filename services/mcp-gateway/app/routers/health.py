from fastapi import APIRouter
from app.config import settings

router = APIRouter(tags=["system"])


@router.get("/health")
def health():
    return {"status": "ok", "service": "mcp-gateway", "version": settings.version}


@router.get("/")
def root():
    return {
        "service": settings.app_name,
        "version": settings.version,
        "docs": "/docs",
        "mcp_endpoint": "/mcp",
    }
