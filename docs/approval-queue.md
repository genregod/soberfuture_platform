# SoberFuture — Approval Queue

**Last updated:** 2026-04-15

---

## Pending Approvals

---

### APPROVAL-001: Slack Credential Rotation

**What is changing:** Rotate all Slack tokens (Bot Token, App Token, Signing Secret) that were exposed in SlackAppStartingConfig.md

**Why it is needed:** Credentials are exposed in a plaintext file in the repo. Must be rotated before the bot is restarted or the repo is pushed to GitHub.

**Evidence:** SlackAppStartingConfig.md contains plaintext xoxb-*, xapp-*, and signing secret values.

**Risks:** If not rotated, exposed tokens could be used by unauthorized parties to post to Slack channels or impersonate the bot.

**Rollback:** N/A — rotation is the remediation.

**Decision required:** User must go to api.slack.com → App settings → rotate Bot Token, App Token, and Signing Secret. Then update /home/arnieai/soberfuture/SoberFuture/.env.local with new values.

**STATUS:** BLOCKED — awaiting user action

---

### APPROVAL-002: GitHub Repo Initialization

**What is changing:** Create a new GitHub repository for SoberFuture and push the local codebase.

**Why it is needed:** No GitHub repo exists yet. CI/CD, branch protection, and team collaboration require it.

**Evidence:** No GitHub remote configured in local repo.

**Risks:** If repo is public, any remaining secrets in files would be exposed. Must ensure .gitignore is correct and no secrets are in tracked files before push.

**Rollback:** Delete repo if pushed incorrectly.

**Decision required:** Approve repo creation. Confirm: repo name (soberfuture-platform?), visibility (private), org or personal account.

**STATUS:** PENDING — awaiting approval

---

### APPROVAL-003: AWS DEV Foundation Resources

**What is changing:** Create DEV-only AWS resources:
- S3 bucket: soberfuture-dev-artifacts (us-east-1, versioning on, private)
- S3 bucket: soberfuture-dev-logs (us-east-1, private)
- S3 bucket: soberfuture-tfstate (us-east-1, versioning on, private — Terraform state)
- EC2 t3.small instance (Amazon Linux 2023, tagged Project=SoberFuture Env=dev)
- IAM role: soberfuture-dev-role (least privilege, EC2 instance profile)
- Billing alert: $50/month

**Why it is needed:** Build/orchestration needs a persistent runner. Artifacts and logs need storage. Terraform needs state storage.

**Evidence:** AWS identity confirmed (account 973028704465). No existing SoberFuture resources found.

**Risks:** Cost if instance left running. Misconfigured IAM could over-privilege.

**Rollback:** `terraform destroy` or manual deletion. All resources tagged for easy identification.

**Decision required:** APPROVED by INSTRUCTIONS.MD ("explicit approval for DEV-ONLY AWS bootstrap"). Proceeding.

**STATUS:** APPROVED — executing

---

## Completed Approvals

| ID | Item | Decision | Date |
|----|------|---------|------|
| — | DEV-ONLY AWS bootstrap | Approved (INSTRUCTIONS.MD) | 2026-04-15 |
