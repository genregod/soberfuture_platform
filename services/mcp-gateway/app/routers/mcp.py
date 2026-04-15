"""
MCP protocol endpoint — implements JSON-RPC 2.0 over HTTP.
Supports: initialize, tools/list, tools/call
"""
from __future__ import annotations
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from typing import Any
import logging

from app.services.tool_registry import TOOL_REGISTRY, call_tool

logger = logging.getLogger(__name__)
router = APIRouter(tags=["mcp"])

MCP_VERSION = "2024-11-05"
SERVER_INFO = {"name": "soberfuture-mcp-gateway", "version": "0.1.0"}


def _ok(id: Any, result: Any) -> dict:
    return {"jsonrpc": "2.0", "id": id, "result": result}


def _err(id: Any, code: int, message: str) -> dict:
    return {"jsonrpc": "2.0", "id": id, "error": {"code": code, "message": message}}


@router.post("/mcp")
async def mcp_endpoint(request: Request):
    try:
        body = await request.json()
    except Exception:
        return JSONResponse(_err(None, -32700, "Parse error"), status_code=400)

    rpc_id = body.get("id")
    method = body.get("method", "")
    params = body.get("params", {})

    logger.info(f"MCP method={method} id={rpc_id}")

    if method == "initialize":
        return JSONResponse(_ok(rpc_id, {
            "protocolVersion": MCP_VERSION,
            "serverInfo": SERVER_INFO,
            "capabilities": {"tools": {"listChanged": False}},
        }))

    if method == "notifications/initialized":
        return JSONResponse({"jsonrpc": "2.0"})

    if method == "tools/list":
        tools = [
            {
                "name": name,
                "description": meta["description"],
                "inputSchema": meta["inputSchema"],
            }
            for name, meta in TOOL_REGISTRY.items()
        ]
        return JSONResponse(_ok(rpc_id, {"tools": tools}))

    if method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        if tool_name not in TOOL_REGISTRY:
            return JSONResponse(_err(rpc_id, -32601, f"Unknown tool: {tool_name}"))
        try:
            result = await call_tool(tool_name, arguments)
            return JSONResponse(_ok(rpc_id, {
                "content": [{"type": "text", "text": str(result)}],
                "isError": False,
            }))
        except Exception as e:
            logger.error(f"Tool {tool_name} error: {e}", exc_info=True)
            return JSONResponse(_ok(rpc_id, {
                "content": [{"type": "text", "text": f"Error: {e}"}],
                "isError": True,
            }))

    return JSONResponse(_err(rpc_id, -32601, f"Method not found: {method}"))
