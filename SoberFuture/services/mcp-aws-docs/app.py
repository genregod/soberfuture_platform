"""
mcp-aws-docs: AWS documentation context lookup.
Fetches and caches AWS service docs for grounded infrastructure decisions.
Allowed: read-only doc fetching, summarization context.
Forbidden: making AWS API calls, mutating infrastructure.
"""
import os
import requests

AWS_DOCS_BASE = "https://docs.aws.amazon.com"


def fetch_service_overview(service_slug: str) -> str:
    """
    Fetch the landing page text for an AWS service.
    service_slug examples: 'AmazonECS', 'AmazonRDS', 'IAM'
    """
    url = f"{AWS_DOCS_BASE}/{service_slug}/latest/userguide/what-is.html"
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        return r.text[:4000]  # return first 4k chars as context
    return f"Could not fetch docs for {service_slug}: HTTP {r.status_code}"


def health():
    return {"status": "ok", "service": "mcp-aws-docs"}
