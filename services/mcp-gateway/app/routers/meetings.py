"""
Meeting discovery tools — AA, NA, CA, SMART Recovery, Refuge Recovery.
Sources: Meeting Guide JSON API (AA), BMLT (NA), direct scraping (SMART/Refuge).
"""
from __future__ import annotations
import asyncio
import logging
import math
from typing import Any

import aiohttp
from fastapi import APIRouter

from app.config import settings

logger = logging.getLogger(__name__)
router = APIRouter(tags=["meetings"])


def _haversine(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """Return distance in miles between two lat/lng points."""
    R = 3958.8
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


async def _fetch_meeting_guide(lat: float, lng: float, radius: float) -> list[dict]:
    """Fetch AA meetings from Meeting Guide JSON API."""
    url = f"{settings.meeting_guide_api}?lat={lat}&lng={lng}&distance={int(radius)}"
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    logger.warning(f"Meeting Guide API returned {resp.status}")
                    return []
                data = await resp.json(content_type=None)
                meetings = []
                for m in data if isinstance(data, list) else data.get("meetings", []):
                    try:
                        mlat = float(m.get("latitude") or m.get("lat") or 0)
                        mlng = float(m.get("longitude") or m.get("lng") or 0)
                        dist = _haversine(lat, lng, mlat, mlng)
                        meetings.append({
                            "id": str(m.get("id", "")),
                            "name": m.get("name", "AA Meeting"),
                            "type": "AA",
                            "day_of_week": m.get("day", 0),
                            "time": m.get("time", "00:00"),
                            "address": m.get("formatted_address") or m.get("address", ""),
                            "lat": mlat,
                            "lng": mlng,
                            "distance_miles": round(dist, 2),
                            "online_url": m.get("conference_url"),
                            "notes": m.get("notes"),
                            "source": "meeting_guide",
                        })
                    except (ValueError, TypeError):
                        continue
                return meetings
    except Exception as e:
        logger.error(f"Meeting Guide fetch error: {e}")
        return []


async def _fetch_bmlt(lat: float, lng: float, radius: float) -> list[dict]:
    """Fetch NA/other meetings from BMLT root server."""
    url = (
        f"{settings.bmlt_root_server}/client_interface/json/"
        f"?switcher=GetSearchResults&lat_val={lat}&long_val={lng}"
        f"&geo_width={radius}&get_used_formats=0&recursive=1"
    )
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return []
                data = await resp.json(content_type=None)
                meetings = []
                for m in data if isinstance(data, list) else []:
                    try:
                        mlat = float(m.get("latitude") or 0)
                        mlng = float(m.get("longitude") or 0)
                        dist = _haversine(lat, lng, mlat, mlng)
                        meetings.append({
                            "id": f"bmlt-{m.get('id_bigint', '')}",
                            "name": m.get("meeting_name", "NA Meeting"),
                            "type": "NA",
                            "day_of_week": int(m.get("weekday_tinyint", 1)) - 1,
                            "time": m.get("start_time", "00:00")[:5],
                            "address": f"{m.get('location_street', '')} {m.get('location_municipality', '')}".strip(),
                            "lat": mlat,
                            "lng": mlng,
                            "distance_miles": round(dist, 2),
                            "online_url": None,
                            "notes": m.get("comments"),
                            "source": "bmlt",
                        })
                    except (ValueError, TypeError):
                        continue
                return meetings
    except Exception as e:
        logger.error(f"BMLT fetch error: {e}")
        return []


async def search_meetings_service(
    lat: float,
    lng: float,
    radius_miles: float = 10.0,
    meeting_type: str | None = None,
    day_of_week: int | None = None,
) -> list[dict]:
    """Aggregate meetings from all sources, filter, sort by distance."""
    results = await asyncio.gather(
        _fetch_meeting_guide(lat, lng, radius_miles),
        _fetch_bmlt(lat, lng, radius_miles),
        return_exceptions=True,
    )
    meetings: list[dict] = []
    for r in results:
        if isinstance(r, list):
            meetings.extend(r)

    if meeting_type:
        meetings = [m for m in meetings if m["type"].upper() == meeting_type.upper()]
    if day_of_week is not None:
        meetings = [m for m in meetings if m["day_of_week"] == day_of_week]

    meetings.sort(key=lambda m: m.get("distance_miles") or 999)
    return meetings[:100]


@router.get("/search")
async def search_meetings_endpoint(
    lat: float,
    lng: float,
    radius_miles: float = 10.0,
    type: str | None = None,
    day_of_week: int | None = None,
):
    return await search_meetings_service(lat, lng, radius_miles, type, day_of_week)
