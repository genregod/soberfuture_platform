from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

router = APIRouter(tags=["journal"])


class EntryCreate(BaseModel):
    mood: int  # 1-5
    body: str
    prompt: Optional[str] = None


class EntryResponse(BaseModel):
    id: str
    mood: int
    body: str
    created_at: datetime


@router.get("/entries", response_model=list[EntryResponse])
def list_entries():
    # TODO: fetch from DB for authenticated user
    return []


@router.post("/entries", response_model=EntryResponse, status_code=201)
def create_entry(body: EntryCreate):
    # TODO: persist entry, trigger async AI analysis
    return EntryResponse(
        id="stub-id",
        mood=body.mood,
        body=body.body,
        created_at=datetime.utcnow(),
    )
