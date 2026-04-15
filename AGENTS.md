# SoberFuture Agent Policy

You are operating in a governed workspace for a **health-adjacent, privacy-sensitive** product. Follow these rules without exception.

## Required workflow order

1. Read ADRs: `docs/adr/**` — understand architecture decisions before writing code
2. Read task ledger: `docs/task-ledger.md` — understand current state and blockers
3. Ground in official docs via MCP — never rely on memory for package APIs, versions, or flags
4. Check OpenAPI spec (`docs/api/openapi.yaml`) before touching any API client or server code
5. Plan: write what files change, migration steps, test plan, rollback
6. Implement only after steps 1–5 complete
7. Validate: lint + typecheck + tests + (for web UI) Playwright screenshots
8. Update task ledger and progress log

## Non-negotiable safety rules

- **Never guess** package names, CLI flags, config paths, or API versions — use MCP + official docs
- **No production AWS mutations** without a human approval checkpoint recorded in `docs/approval-queue.md`
- **No Slack workspace mutations** (app install, mass message, settings) without human approval
- **No UI implementation** without design-token alignment
- **No API client code** without OpenAPI schema grounding
- **No merge** without: lint, typecheck, tests, and screenshot evidence for UI changes
- **No training on user data** — customer journal content is never used for model training
- **No diagnosis, no medical advice, no claims of being a therapist** — ever
- **Crisis signals** must trigger the approved escalation workflow, never autonomous AI response
- If uncertain: STOP, document the uncertainty in task-ledger.md, request approval

## Product context

SoberFuture.me is a mobile-first recovery journal + clinician support platform.
- Primary users: people in addiction recovery, on phones and tablets
- Secondary users: clinicians and admins on web
- All user content is treated as sensitive — encryption at rest + in transit always
- Privacy-first: no PII/PHI in analytics, no cross-tier data flow without de-identification

## MCP servers available

See `.kiro/settings/mcp.json` for the full list. Key servers:
- `filesystem_repo` — read repo files (write tools disabled)
- `github_ro` — read GitHub context (write tools disabled)
- `fetch_docs` — fetch official documentation pages
- `local_rag` — semantic search over docs/adr
- `playwright_ui` — browser screenshots + a11y snapshots
- `openapi_contracts` — ground API work in OpenAPI spec
- `aws_docs` — official AWS documentation
- `terraform_iac` — Terraform provider docs (apply disabled)
- `soberfuture_mcp` — SoberFuture's own hosted MCP gateway on AWS
