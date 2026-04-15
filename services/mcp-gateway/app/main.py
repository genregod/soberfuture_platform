"""
MCP Gateway — SoberFuture
Exposes SoberFuture-specific MCP tools over HTTP (JSON-RPC 2.0 compatible).
Implements the MCP protocol: initialize, tools/list, tools/call.
"""
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

from app.config import settings
from app.routers import health, mcp, meetings, resources, journal_tools

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def verify_api_key(request: Request):
    key = request.headers.get("X-API-Key") or request.headers.get("Authorization", "").removeprefix("Bearer ")
    if key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return key


app.include_router(health.router)
app.include_router(mcp.router, dependencies=[Depends(verify_api_key)])
app.include_router(meetings.router, prefix="/meetings", dependencies=[Depends(verify_api_key)])
app.include_router(resources.router, prefix="/resources", dependencies=[Depends(verify_api_key)])
app.include_router(journal_tools.router, prefix="/journal", dependencies=[Depends(verify_api_key)])


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"error": "internal_error", "message": str(exc)})
