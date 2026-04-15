# SoberFuture — Milestone Map

**Date:** 2026-04-15

## Phase 0 — Foundation (Current)
- [x] Read all source docs and extract durable facts
- [x] Update LongTermMemory.md
- [x] Create inception brief, risk register, assumptions log
- [x] Create ADRs 001–005
- [x] Create task ledger, progress log, approval queue
- [x] Normalize repo structure
- [ ] Rotate exposed Slack credentials
- [ ] Initialize GitHub repo
- [ ] Create AWS DEV foundation resources

## Phase 1 — Local Build Foundation
- [ ] Bootstrap web app (Next.js scaffold)
- [ ] Bootstrap mobile app (Expo scaffold)
- [ ] Bootstrap API service (FastAPI scaffold)
- [ ] Bootstrap agent-orchestrator service
- [ ] Bootstrap shared packages (ui, schemas, config, sdk)
- [ ] Docker Compose for local dev
- [ ] README with local dev instructions

## Phase 2 — MCP Server Activation
- [ ] Fix REPO_ROOT path in mcp-repo-context
- [ ] Fix systemd service paths
- [ ] Install playwright for mcp-browser
- [ ] Configure GITHUB_TOKEN for mcp-github
- [ ] Validate all 7 MCP servers pass health checks
- [ ] Update mcp-registry.json with validation dates

## Phase 3 — GitHub + CI/CD
- [ ] Initialize GitHub repo (soberfuture or soberfuture-platform)
- [ ] Set branch protection (main + develop)
- [ ] CI workflow: typecheck + lint + test + security scan
- [ ] PR template
- [ ] Issue templates
- [ ] CODEOWNERS

## Phase 4 — AWS DEV Foundation
- [ ] S3 buckets: soberfuture-dev-artifacts, soberfuture-dev-logs
- [ ] EC2 t3.small build/orchestration instance
- [ ] IAM role: soberfuture-dev-role (least privilege)
- [ ] Billing alert at $50/month
- [ ] Terraform state bucket

## Phase 5 — Product Surfaces MVP
- [ ] Marketing landing page
- [ ] Client journal auth flow
- [ ] Clinician workspace scaffold
- [ ] Design system tokens

## Phase 6 — AI + MLOps Foundation
- [ ] Prompt registry
- [ ] Evaluation dataset schema
- [ ] Safety policy document
- [ ] Model usage matrix
- [ ] Offline eval plan

## Phase 7 — Slack Integration
- [ ] Rotate tokens
- [ ] Restart bot with clean credentials
- [ ] Test all 4 channels
- [ ] Approval workflow end-to-end test
