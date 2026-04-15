"""
Recovery resource search — geo-radius based.
Backed by a curated database; falls back to stub data in dev.
"""
from __future__ import annotations
import math
import logging
from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter(tags=["resources"])

# Stub resource data — replace with DB query in production
_STUB_RESOURCES = [
    {
        "id": "r-001",
        "name": "Hope Recovery Center",
        "category": "treatment",
        "address": "123 Main St, Anytown, USA",
        "phone": "555-0100",
        "website": "https://example.com",
        "lat": 0.0,
        "lng": 0.0,
        "hours": "Mon-Fri 8am-6pm",
    },
]


def _haversine(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    R = 3958.8
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


async def search_resources_service(
    lat: float,
    lng: float,
    radius_miles: float = 10.0,
    category: str | None = None,
) -> list[dict]:
    results = []
    for r in _STUB_RESOURCES:
        dist = _haversine(lat, lng, r["lat"], r["lng"])
        if dist <= radius_miles:
            if category and r["category"] != category:
                continue
            results.append({**r, "distance_miles": round(dist, 2)})
    results.sort(key=lambda r: r["distance_miles"])
    return results


@router.get("/search")
async def search_resources_endpoint(
    lat: float,
    lng: float,
    radius_miles: float = 10.0,
    category: str | None = None,
):
    return await search_resources_service(lat, lng, radius_miles, category)
