"""
mcp-package-docs: Package and framework documentation lookup.
Fetches PyPI / npm package metadata and README for grounded dependency decisions.
Allowed: read-only registry queries.
Forbidden: installing packages, mutating lockfiles.
"""
import requests


def pypi_info(package: str) -> dict:
    r = requests.get(f"https://pypi.org/pypi/{package}/json", timeout=10)
    r.raise_for_status()
    data = r.json()
    info = data["info"]
    return {
        "name":        info["name"],
        "version":     info["version"],
        "summary":     info["summary"],
        "home_page":   info["home_page"],
        "license":     info["license"],
        "requires_python": info["requires_python"],
    }


def npm_info(package: str) -> dict:
    r = requests.get(f"https://registry.npmjs.org/{package}/latest", timeout=10)
    r.raise_for_status()
    data = r.json()
    return {
        "name":        data.get("name"),
        "version":     data.get("version"),
        "description": data.get("description"),
        "license":     data.get("license"),
        "homepage":    data.get("homepage"),
    }


def health():
    return {"status": "ok", "service": "mcp-package-docs"}
