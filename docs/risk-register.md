# SoberFuture — Risk Register

**Date:** 2026-04-15

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|-----------|--------|------------|
| R-001 | Privacy breach of recovery journal content | Medium | Critical | Encryption at rest + in transit, RBAC, audit logging, PII segregation |
| R-002 | AI output causes harm (unsupported clinical guidance) | Medium | Critical | Rules/policy layer, prohibited behaviors list, human review for high-risk outputs, no diagnosis claims |
| R-003 | Credential exposure | High (already occurred) | High | Rotate all Slack tokens immediately. Use AWS Secrets Manager. Never commit secrets. |
| R-004 | AWS cost overrun | Medium | Medium | Tag all resources Project=SoberFuture Env=dev. Set billing alerts. Use t3.small for dev. |
| R-005 | Scope creep delays MVP | High | Medium | Phase gates, approval checkpoints, bounded tasks, task ledger discipline |
| R-006 | Hallucinated code in health-adjacent product | Medium | High | Anti-hallucination protocol: retrieve docs, cite sources, validate with build+lint+test |
| R-007 | Slack bot running with exposed tokens | High | High | Rotate tokens before next bot restart. Document rotation runbook. |
| R-008 | No GitHub repo yet | High | Medium | Initialize repo, set branch protection, push existing code |
| R-009 | mcp-repo-context hardcoded to /mnt/c/SoberFuture | High | Medium | Update REPO_ROOT env var to /home/arnieai/soberfuture |
| R-010 | systemd service hardcoded to /mnt/c/SoberFuture | High | Medium | Update service file paths to /home/arnieai/soberfuture |
