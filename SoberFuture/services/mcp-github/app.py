"""
mcp-github: GitHub repository context and actions.
Allowed: read repo, list PRs/issues, post comments, trigger workflows.
Forbidden: delete repos, force push, modify branch protection without approval.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv("../../.env.local")

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_ORG   = os.environ.get("GITHUB_ORG", "")
GITHUB_REPO  = os.environ.get("GITHUB_REPO", "")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
BASE = "https://api.github.com"


def get_repo():
    r = requests.get(f"{BASE}/repos/{GITHUB_ORG}/{GITHUB_REPO}", headers=HEADERS)
    r.raise_for_status()
    return r.json()


def list_open_prs():
    r = requests.get(f"{BASE}/repos/{GITHUB_ORG}/{GITHUB_REPO}/pulls?state=open", headers=HEADERS)
    r.raise_for_status()
    return r.json()


def list_open_issues():
    r = requests.get(f"{BASE}/repos/{GITHUB_ORG}/{GITHUB_REPO}/issues?state=open", headers=HEADERS)
    r.raise_for_status()
    return r.json()


def post_issue_comment(issue_number: int, body: str):
    r = requests.post(
        f"{BASE}/repos/{GITHUB_ORG}/{GITHUB_REPO}/issues/{issue_number}/comments",
        headers=HEADERS,
        json={"body": body},
    )
    r.raise_for_status()
    return r.json()


def health():
    return {"status": "ok", "service": "mcp-github"}
