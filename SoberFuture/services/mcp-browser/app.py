"""
mcp-browser: Headless browser automation with screenshot + DOM capture.
Allowed: navigate, screenshot, DOM snapshot, form fill (with approval before submit).
Forbidden: irreversible submits without approval, storing credentials in logs.
"""
import os
import json
from datetime import datetime
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = os.path.join(os.path.dirname(__file__), "artifacts")
os.makedirs(ARTIFACT_DIR, exist_ok=True)


def _timestamp():
    return datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


def capture(url: str, label: str = "capture") -> dict:
    """Navigate to URL, take screenshot, capture DOM. Returns artifact paths."""
    ts = _timestamp()
    screenshot_path = os.path.join(ARTIFACT_DIR, f"{label}_{ts}.png")
    dom_path        = os.path.join(ARTIFACT_DIR, f"{label}_{ts}.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page    = browser.new_page()
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=screenshot_path, full_page=True)
        dom = page.content()
        browser.close()

    with open(dom_path, "w", encoding="utf-8") as f:
        f.write(dom)

    manifest = {
        "url": url,
        "timestamp": ts,
        "screenshot": screenshot_path,
        "dom": dom_path,
    }
    manifest_path = os.path.join(ARTIFACT_DIR, f"{label}_{ts}_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    return manifest


def health():
    return {"status": "ok", "service": "mcp-browser"}
