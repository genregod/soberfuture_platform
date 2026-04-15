# SoberFuture Build Bot — Long Term Memory

> Last updated: 2026-04-15. Updated every 8 iterations or on significant state change.

---

## Product Identity

- **Product:** SoberFuture.me
- **Mission:** AI-powered interactive recovery journal and clinician support platform
- **Domain:** Health-adjacent, addiction recovery. Treat all user content as sensitive.
- **Builder identity:** Arnie (Lobster AI) — precise, structured, formal but not stiff
- **Human:** Anthony Navarro (realgenregod@gmail.com)
- **Workspace:** arnieai.slack.com

---

## Architecture Direction

### Monorepo Layout (confirmed)
```
/
  apps/web, mobile, clinician
  services/api, agent-orchestrator, worker, notifications, audit, mcp-*/
  packages/ui, design-tokens, config, schemas, sdk, prompts, evals
  infra/terraform, environments
  ml/datasets, evaluations, prompts, policies
  docs/adr, runbooks, diagrams, compliance
  .github/workflows
```

### Technology Candidates (pending ADR lock)
- Web: Next.js (React)
- Mobile: Expo React Native
- Backend: FastAPI (Python) + TypeScript service layer
- DB: PostgreSQL
- Cache/Queue: Redis
- Async: Temporal or equivalent
- Infra: Terraform (preferred) or AWS CDK — ADR-003 pending
- CI/CD: GitHub Actions
- Containers: Docker
- AWS Runtime: ECS/Fargate or EKS — ADR pending
- Edge/Static: S3 + CloudFront
- Auth: Cognito (evaluate alternatives)
- Secrets: AWS Secrets Manager / SSM
- MLOps: lightweight, production-ready path

---

## Non-Negotiable Rules

1. Plan before code. No implementation without written architecture plan + ADR + approval checkpoint.
2. No hallucinated code. Retrieve official docs for every version-sensitive decision.
3. Human-in-the-loop for: Slack app install, OAuth scopes, secrets creation, AWS mutations, IAM, DNS, prod deploys, destructive actions, billing changes.
4. Privacy/safety: encryption in transit + at rest, PII/PHI segregated, no training on customer data by default, explicit opt-in for research use, de-identification pipeline required, full audit logging, RBAC, least-privilege IAM.
5. API first, browser automation second. Browser tasks require before/after screenshots + DOM snapshot + approval before irreversible submit.
6. Small, resumable tasks with clear inputs/outputs/success criteria/rollback notes.
7. Every change must prove itself: typecheck, lint, test, security scan, document.

---

## AI / Agent Policy

### Allowed AI capabilities
- Journaling support and reflection prompts
- Future-self reflection prompts
- Structured pattern extraction
- Clinician-facing summaries
- Longitudinal trend detection
- Relapse-risk signal support (with human review)
- Notification triage support
- Retrieval-grounded guidance from approved materials only

### Explicit prohibitions
- No diagnosis
- No claims of being a therapist or sponsor
- No unsupported medical advice
- No autonomous crisis intervention without approved escalation workflow
- No opaque risk scoring without explanation and audit trail

### Data policy
- Customer data is NOT training data by default
- Strict separation: operational / analytics / research-evaluation datasets
- De-identify before any secondary use
- Support deletion, retention, and access control workflows

---

## MCP Server Plan

| Server | Purpose | Status | Auth |
|--------|---------|--------|------|
| mcp-slack | Slack comms, approval workflows | active (Socket Mode) | SLACK_BOT_TOKEN + SLACK_SIGNING_SECRET + SLACK_APP_TOKEN |
| mcp-github | GitHub repo context and actions | scaffolded — needs GITHUB_TOKEN | GITHUB_TOKEN |
| mcp-browser | Headless browser + screenshots + DOM | scaffolded — needs `playwright install` | none |
| mcp-aws-docs | AWS documentation context (read-only) | scaffolded | none |
| mcp-repo-context | Codebase search and context | scaffolded | none |
| mcp-package-docs | PyPI + npm package metadata | scaffolded | none |
| mcp-adr | ADR markdown registry reader | scaffolded | none |

Registry: `SoberFuture/mcp-registry.json`

---

## Slack Operating Model

- Workspace: arnieai.slack.com (Team ID: T0ASULPBNDN)
- Bot: soberfuture_build_bot (User ID: U0AS5DAU5CK)
- Transport: Socket Mode

### Channels
| Channel | ID | Purpose |
|---------|----|---------|
| #soberfuture-build | C0ASFCL4012 | Build summaries and progress |
| #soberfuture-approvals | C0ASBG9JGAJ | Approval requests |
| #soberfuture-alerts | C0AT7S4RUJC | Alerts and errors |
| #soberfuture-architecture | C0AT7S6JADN | Architecture review threads |

### Credential rotation required
SlackAppStartingConfig.md contains exposed credentials. Rotate all Slack tokens immediately.

---

## AWS Direction

- Account: 973028704465
- IAM user: damndogodaddy@gmail.com
- Default region: us-east-1
- Credentials source: /home/arnieai/.matrix_credentials.env (never print, never persist)
- No SoberFuture AWS resources exist yet (confirmed 2026-04-15)
- DEV-ONLY bootstrap approved by user instruction
- No production resources to be created
- Prefer IaC (Terraform) even for initial dev provisioning

### DEV resources created (2026-04-15)

| Resource | ID / Name | Notes |
|----------|-----------|-------|
| S3 | soberfuture-tfstate | Terraform state, versioned, private |
| S3 | soberfuture-dev-artifacts | Build artifacts, versioned, private |
| S3 | soberfuture-dev-logs | Logs, private |
| IAM Role | soberfuture-dev-role (AROA6FDIHYDI4MD6RUVDQ) | EC2 instance role, least privilege |
| IAM Profile | soberfuture-dev-profile | EC2 instance profile |
| Security Group | sg-07ad01923ba9d2800 | SSH port 22 (dev only) |
| EC2 | i-0e98ce07bd8ccbb07 | t3.small, AL2023, 20GB encrypted, IP: 52.54.162.129 |
| Budget | soberfuture-dev-monthly | $50/month, 80% alert → realgenregod@gmail.com |

---

## CI/CD Direction

- GitHub Actions
- Protected branch strategy (main + develop)
- Preview environments per PR
- Changelog automation
- Test matrix: typecheck + lint + unit + integration + security scan

---

## Current Blockers

- [ ] GITHUB_TOKEN — needed to activate mcp-github
- [ ] Slack token rotation — exposed credentials in SlackAppStartingConfig.md
- [ ] Socket Mode daemon — needs persistent runner (Docker or systemd)
- [ ] ADRs (Chain 1) — in progress
- [ ] AWS DEV foundation — approved, not yet created
- [ ] GitHub repo — not yet initialized

---

## Important User Preferences

- Work in small resumable steps
- Keep task ledger and progress artifacts updated continuously
- Do not stop at analysis — build forward
- Decisive, methodical, no hallucination, no unnecessary questions
- Use files as source of truth, not mental notes

---

## Session Log

### Session 1 (2026-04-12)
- Scaffolded 7 MCP servers in SoberFuture/services/
- Created mcp-registry.json
- Created .env.example, .env.local (gitignored)
- Confirmed Slack bot credentials and channel IDs
- Wrote mcp-slack/app.py (Socket Mode, full dispatcher)
- Wrote soberfuture-bot.service (systemd unit)

### Session 2 (2026-04-15)
- Read all source files: AGENTS.MD, HEARTBEAT.MD, IDENTITY.MD, SOUL.MD, TOOLS.MD, USER.MD, AIDatasetGuides.md, MasterOrchestrator.md, MCPGuides.md, SlackAppStartingConfig.md, TaskLedger.md
- Confirmed AWS identity (account 973028704465, us-east-1)
- Confirmed no existing SoberFuture AWS resources
- Updated LongTermMemory.md (this file)
- Created docs/inception-brief.md, risk-register.md, assumptions.md, milestones.md
- Created ADR-001 through ADR-005
- Created task-ledger.md, progress.md, approval-queue.md
- Created README.md
- Created .gitignore, .env.example
- Created infra/terraform/ DEV foundation stubs
- Created .github/workflows/ci.yml
- Next: AWS DEV resource creation (approval already granted by INSTRUCTIONS.MD)
