# SoberFuture — Task Ledger

**Last updated:** 2026-04-15

---

## Template

```
TASK: <one-line>
STATUS: not started | in progress | blocked | complete
PHASE: 0–10
APPROVAL NEEDED: yes/no
ARTIFACTS: <paths>
BLOCKERS: <list>
NEXT: <next bounded task>
```

---

## Active Tasks

---

### T-001: Memory ingestion and state recovery
**STATUS:** complete
**PHASE:** 0
**APPROVAL NEEDED:** no
**ARTIFACTS:**
- SoberFuture/LongTermMemory.md (updated)
- docs/inception-brief.md
- docs/risk-register.md
- docs/assumptions.md
- docs/milestones.md
**BLOCKERS:** none
**NEXT:** T-002

---

### T-002: ADR creation (Chain 1)
**STATUS:** complete
**PHASE:** 1
**APPROVAL NEEDED:** no (planning artifacts)
**ARTIFACTS:**
- docs/adr/ADR-001-monorepo.md
- docs/adr/ADR-002-app-stack.md
- docs/adr/ADR-003-infra-stack.md
- docs/adr/ADR-004-agent-architecture.md
- docs/adr/ADR-005-data-boundaries.md
**BLOCKERS:** none
**NEXT:** T-003

---

### T-003: Fix hardcoded paths in MCP servers
**STATUS:** complete
**PHASE:** 2
**APPROVAL NEEDED:** no
**ARTIFACTS:**
- SoberFuture/services/mcp-repo-context/app.py (REPO_ROOT updated)
- SoberFuture/services/mcp-adr/app.py (ADR_DIR updated)
- SoberFuture/services/mcp-slack/soberfuture-bot.service (paths updated)
**BLOCKERS:** none
**NEXT:** T-004

---

### T-004: Create README and .gitignore
**STATUS:** complete
**PHASE:** 2
**APPROVAL NEEDED:** no
**ARTIFACTS:**
- README.md
- .gitignore
- .env.example
**BLOCKERS:** none
**NEXT:** T-005

---

### T-005: Create GitHub Actions CI workflow
**STATUS:** complete
**PHASE:** 4
**APPROVAL NEEDED:** no (workflow file only — no secrets or branch protection yet)
**ARTIFACTS:**
- .github/workflows/ci.yml
**BLOCKERS:** none
**NEXT:** T-006

---

### T-006: Create Terraform DEV foundation
**STATUS:** complete
**PHASE:** 5
**APPROVAL NEEDED:** YES — before `terraform apply`
**ARTIFACTS:**
- infra/terraform/main.tf
- infra/terraform/variables.tf
- infra/terraform/outputs.tf
**BLOCKERS:** Needs approval before apply
**NEXT:** T-007

---

### T-007: Create AWS DEV resources
**STATUS:** in progress
**PHASE:** 5
**APPROVAL NEEDED:** Granted by INSTRUCTIONS.MD (DEV-ONLY bootstrap)
**ARTIFACTS:** TBD — S3 buckets, EC2 instance, IAM role
**BLOCKERS:** none (approval granted)
**NEXT:** T-008

---

### T-008: Rotate Slack credentials
**STATUS:** blocked
**PHASE:** 8
**APPROVAL NEEDED:** YES — requires Slack dashboard access
**ARTIFACTS:** Updated .env.local (masked)
**BLOCKERS:** User must rotate tokens in Slack dashboard
**NEXT:** T-009

---

### T-009: Initialize GitHub repo and push
**STATUS:** not started
**PHASE:** 4
**APPROVAL NEEDED:** YES — external action
**ARTIFACTS:** GitHub repo URL
**BLOCKERS:** Needs GITHUB_TOKEN and repo name confirmation
**NEXT:** T-010

---

### T-010: Bootstrap web app (Next.js)
**STATUS:** not started
**PHASE:** 6
**APPROVAL NEEDED:** no
**ARTIFACTS:** apps/web/
**BLOCKERS:** T-009 (GitHub repo) preferred first
**NEXT:** T-011

---

## Completed Tasks

| ID | Task | Date |
|----|------|------|
| T-001 | Memory ingestion | 2026-04-15 |
| T-002 | ADR creation | 2026-04-15 |
| T-003 | Fix hardcoded paths | 2026-04-15 |
| T-004 | README + .gitignore | 2026-04-15 |
| T-005 | CI workflow | 2026-04-15 |
| T-006 | Terraform DEV stubs | 2026-04-15 |
