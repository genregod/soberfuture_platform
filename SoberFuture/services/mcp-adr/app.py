"""
mcp-adr: Architecture Decision Registry lookup.
Reads ADR markdown files from docs/adr/ and returns structured context.
Allowed: read, list, search ADRs.
Forbidden: writes without approval workflow.
"""
import os
import re

ADR_DIR = os.environ.get("ADR_DIR", "/home/arnieai/soberfuture/docs/adr")


def list_adrs() -> list[dict]:
    adrs = []
    for fname in sorted(os.listdir(ADR_DIR)):
        if fname.endswith(".md"):
            path = os.path.join(ADR_DIR, fname)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            status_match = re.search(r"\*\*Status\*\*[:\s]+(\w+)", content, re.IGNORECASE)
            adrs.append({
                "file":   fname,
                "title":  title_match.group(1) if title_match else fname,
                "status": status_match.group(1) if status_match else "unknown",
            })
    return adrs


def get_adr(filename: str) -> str:
    path = os.path.join(ADR_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def health():
    return {"status": "ok", "service": "mcp-adr"}
