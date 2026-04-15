"""
Tool registry — maps MCP tool names to handlers.
All tools exposed via the /mcp JSON-RPC endpoint.
"""
from __future__ import annotations
from typing import Any, Callable, Awaitable

from app.routers.meetings import search_meetings_service
from app.routers.resources import search_resources_service
from app.routers.journal_tools import get_prompts, analyze_entry


TOOL_REGISTRY: dict[str, dict] = {
    "health": {
        "description": "Check MCP gateway health and list available tools.",
        "inputSchema": {"type": "object", "properties": {}, "required": []},
    },
    "list_servers": {
        "description": "List all registered MCP servers and their status.",
        "inputSchema": {"type": "object", "properties": {}, "required": []},
    },
    "search_meetings": {
        "description": (
            "Search for AA, NA, CA, SMART Recovery, and Refuge Recovery meetings "
            "near a given location. Returns meetings sorted by distance."
        ),
        "inputSchema": {
            "type": "object",
            "required": ["lat", "lng"],
            "properties": {
                "lat": {"type": "number", "description": "Latitude"},
                "lng": {"type": "number", "description": "Longitude"},
                "radius_miles": {"type": "number", "default": 10, "description": "Search radius in miles"},
                "type": {"type": "string", "enum": ["AA", "NA", "CA", "SMART", "Refuge", "other"], "description": "Filter by meeting type"},
                "day_of_week": {"type": "integer", "minimum": 0, "maximum": 6, "description": "0=Sunday, 6=Saturday"},
            },
        },
    },
    "search_resources": {
        "description": "Search for recovery resources (treatment, counseling, housing, etc.) near a location.",
        "inputSchema": {
            "type": "object",
            "required": ["lat", "lng"],
            "properties": {
                "lat": {"type": "number"},
                "lng": {"type": "number"},
                "radius_miles": {"type": "number", "default": 10},
                "category": {"type": "string", "enum": ["treatment", "counseling", "housing", "food", "legal", "peer_support", "other"]},
            },
        },
    },
    "get_journal_prompts": {
        "description": "Get reflection prompts for journal check-ins. Returns 3 random prompts by default.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "count": {"type": "integer", "default": 3, "minimum": 1, "maximum": 10},
            },
        },
    },
    "analyze_entry": {
        "description": (
            "Analyze a journal entry for themes and patterns. "
            "Returns observations only — NOT diagnosis or medical advice."
        ),
        "inputSchema": {
            "type": "object",
            "required": ["text"],
            "properties": {
                "text": {"type": "string", "description": "Journal entry text"},
                "mood": {"type": "integer", "minimum": 1, "maximum": 5},
            },
        },
    },
    "get_user_streak": {
        "description": "Get a user's current check-in streak and milestone status.",
        "inputSchema": {
            "type": "object",
            "required": ["user_id"],
            "properties": {
                "user_id": {"type": "string", "format": "uuid"},
            },
        },
    },
    "get_milestones": {
        "description": "Get milestone definitions and descriptions for recovery journeys.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "days_sober": {"type": "integer", "description": "Days sober to check milestones for"},
            },
        },
    },
}

MILESTONES = [
    {"days": 1, "label": "First Day", "emoji": "🌱"},
    {"days": 7, "label": "One Week", "emoji": "🌿"},
    {"days": 30, "label": "One Month", "emoji": "🌳"},
    {"days": 90, "label": "Three Months", "emoji": "💪"},
    {"days": 180, "label": "Six Months", "emoji": "⭐"},
    {"days": 365, "label": "One Year", "emoji": "🏆"},
]


async def call_tool(name: str, arguments: dict) -> Any:
    if name == "health":
        return {"status": "ok", "tools": list(TOOL_REGISTRY.keys())}

    if name == "list_servers":
        return {
            "servers": [
                {"id": "soberfuture_mcp", "status": "active", "url": "http://52.54.162.129:8100"},
                {"id": "filesystem_repo", "status": "active"},
                {"id": "github_ro", "status": "active"},
                {"id": "fetch_docs", "status": "active"},
                {"id": "local_rag", "status": "active"},
                {"id": "playwright_ui", "status": "active"},
                {"id": "openapi_contracts", "status": "active"},
                {"id": "aws_docs", "status": "active"},
                {"id": "terraform_iac", "status": "active"},
                {"id": "slack_approvals", "status": "disabled_pending_oauth"},
                {"id": "aws_location", "status": "disabled_pending_approval"},
                {"id": "mapbox_geo", "status": "disabled_pending_token"},
                {"id": "bedrock_data_automation", "status": "disabled_pending_approval"},
                {"id": "aws_api_mutation", "status": "disabled_approval_only"},
            ]
        }

    if name == "search_meetings":
        return await search_meetings_service(
            lat=arguments["lat"],
            lng=arguments["lng"],
            radius_miles=arguments.get("radius_miles", 10.0),
            meeting_type=arguments.get("type"),
            day_of_week=arguments.get("day_of_week"),
        )

    if name == "search_resources":
        return await search_resources_service(
            lat=arguments["lat"],
            lng=arguments["lng"],
            radius_miles=arguments.get("radius_miles", 10.0),
            category=arguments.get("category"),
        )

    if name == "get_journal_prompts":
        return get_prompts(count=arguments.get("count", 3))

    if name == "analyze_entry":
        return await analyze_entry(arguments)

    if name == "get_user_streak":
        # Stub — replace with DB query
        return {"user_id": arguments["user_id"], "streak_days": 0, "longest_streak": 0}

    if name == "get_milestones":
        days = arguments.get("days_sober", 0)
        achieved = [m for m in MILESTONES if days >= m["days"]]
        next_milestone = next((m for m in MILESTONES if days < m["days"]), None)
        return {
            "days_sober": days,
            "achieved": achieved,
            "next_milestone": next_milestone,
            "all_milestones": MILESTONES,
        }

    raise ValueError(f"Tool not implemented: {name}")
