# MCP Registry — SoberFuture

Last updated: 2026-04-15

This is the single source of truth for all MCP servers. A server must pass validation before `disabled` is set to `false` in `.kiro/settings/mcp.json`.

## Hosted on AWS (soberfuture_mcp gateway)

| Tool | Description | Status |
|------|-------------|--------|
| `health` | Gateway health + tool list | ✅ active |
| `list_servers` | All server statuses | ✅ active |
| `search_meetings` | AA/NA/SMART/Refuge meetings by location | ✅ active |
| `search_resources` | Recovery resources by location | ✅ active |
| `get_journal_prompts` | Reflection prompts | ✅ active |
| `analyze_entry` | Journal entry theme analysis | ✅ active |
| `get_user_streak` | Check-in streak | ✅ active |
| `get_milestones` | Milestone definitions | ✅ active |

**Endpoint:** `http://52.54.162.129:8100/mcp`
**Auth:** `X-API-Key` header — key in AWS Secrets Manager `soberfuture/dev/mcp-gateway-api-key`

## Kiro-managed MCP servers

| Server ID | Package | Status | Notes |
|-----------|---------|--------|-------|
| `filesystem_repo` | `@modelcontextprotocol/server-filesystem` | ✅ enabled | Write tools disabled |
| `github_ro` | `@modelcontextprotocol/server-github` | ✅ enabled | Write tools disabled |
| `fetch_docs` | `mcp-server-fetch` (uvx) | ✅ enabled | |
| `local_rag` | `mcp-local-rag` (npx) | ✅ enabled | BASE_DIR=docs/ |
| `playwright_ui` | `@playwright/mcp@latest` | ✅ enabled | Headless |
| `openapi_contracts` | `awslabs.openapi-mcp-server` (uvx) | ✅ enabled | Spec: docs/api/openapi.yaml |
| `aws_docs` | `awslabs.aws-documentation-mcp-server` (uvx) | ✅ enabled | |
| `terraform_iac` | `@hashicorp/terraform-mcp-server` | ✅ enabled | Apply disabled |
| `bravesearch_docs` | `@modelcontextprotocol/server-brave-search` | ⏸ disabled | Needs BRAVE_API_KEY |
| `slack_approvals` | `https://mcp.slack.com/mcp` | ⏸ disabled | Needs OAuth approval |
| `aws_location` | `awslabs.aws-location-mcp-server` (uvx) | ⏸ disabled | Needs approval + cost review |
| `mapbox_geo` | `@mapbox/mcp-server` | ⏸ disabled | Needs MAPBOX_ACCESS_TOKEN |
| `bedrock_data_automation` | `awslabs.aws-bedrock-data-automation-mcp-server` | ⏸ disabled | Needs privacy review |
| `aws_api_mutation` | `awslabs.aws-api-mcp-server` | ⏸ disabled | Approval-only, high risk |

## Validation protocol

For each server before enabling:
1. `python -m json.tool .kiro/settings/mcp.json` — validate JSON
2. Enable single server, check Kiro MCP panel shows it connected
3. Ask: "List available tools for `<server_id>`"
4. Run realistic SoberFuture query (see manifests in `docs/mcp/manifests/`)
5. If any error → set `disabled: true`, log in task-ledger.md
