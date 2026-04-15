"""
Journal AI tools — reflection prompts, entry analysis.
IMPORTANT: No diagnosis, no medical advice, no claims of being a therapist.
"""
from __future__ import annotations
import random
from fastapi import APIRouter

router = APIRouter(tags=["journal_tools"])

REFLECTION_PROMPTS = [
    "What's one thing you're grateful for today?",
    "What was the hardest moment today, and how did you handle it?",
    "What would your future self say to you right now?",
    "What's one small win you had today, no matter how small?",
    "What triggered you today, and what helped you stay grounded?",
    "Who supported you today, or who could you reach out to?",
    "What does your body feel like right now? Where do you feel tension?",
    "What's one thing you want to let go of today?",
    "What does recovery mean to you today — not yesterday, today?",
    "If you could tell your past self one thing, what would it be?",
    "What boundaries did you honor today?",
    "What are you looking forward to tomorrow?",
]


@router.get("/prompts")
def get_prompts(count: int = 3):
    """Return a random selection of reflection prompts."""
    return {"prompts": random.sample(REFLECTION_PROMPTS, min(count, len(REFLECTION_PROMPTS)))}


@router.post("/analyze")
async def analyze_entry(body: dict):
    """
    Analyze a journal entry for themes and patterns.
    Returns structured observations — NOT diagnosis or medical advice.
    """
    text = body.get("text", "")
    mood = body.get("mood", 3)

    # Stub — replace with actual LLM call via agent-orchestrator
    themes = []
    if any(w in text.lower() for w in ["grateful", "thankful", "appreciate"]):
        themes.append("gratitude")
    if any(w in text.lower() for w in ["hard", "difficult", "struggle", "tough"]):
        themes.append("challenge")
    if any(w in text.lower() for w in ["proud", "accomplished", "did it"]):
        themes.append("achievement")
    if any(w in text.lower() for w in ["trigger", "urge", "craving"]):
        themes.append("trigger_awareness")

    return {
        "themes": themes,
        "mood_label": {1: "very low", 2: "low", 3: "neutral", 4: "good", 5: "great"}.get(mood, "neutral"),
        "reflection": "Thank you for checking in today. Your consistency matters.",
        "disclaimer": "This is a reflection tool, not medical advice. If you're in crisis, please contact a professional.",
    }
