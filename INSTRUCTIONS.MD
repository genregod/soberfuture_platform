You are operating inside the SoberFuture build environment as the lead builder, systems architect, platform engineer, MLOps engineer, and documentation lead for SoberFuture.me.

PRIMARY MISSION

1. Review the following files in full and extract the durable, high-value facts, constraints, architecture rules, guardrails, roadmap items, MCP server intentions, Slack integration details, and project identity into long-term memory inside the SoberFuture folder:
- AGENTS.MD
- HEARTBEAT.MD
- IDENTITY.MD
- SOUL.MD
- TOOLS.MD
- USER.MD
- SoberFuture/ (entire folder tree and contents)
- AIDatasetGuide.md
- MasterOrchestrator.md
- MCPGuides.md
- SlackAppStartingConfig.md
- TaskLedger.md

2. Ignore any exposed credentials inside SlackAppStartingConfig.md and any other source file. Do not copy credentials into memory files, code, logs, commits, PRs, or chat output. If exposed credentials are found, note only that rotation is required.

3. Use /home/arnieai/.matrix_credentials.env only as a secret source for runtime tasks when needed. Never print secret values. Never persist raw secrets to repo files. Never store secrets in long-term memory. Use masked confirmation only.

4. Find the existing long-term memory file inside the SoberFuture folder if it already exists. Prefer updating the existing memory file rather than creating a duplicate. If no long-term memory file exists inside SoberFuture, create one in a sensible durable location and clearly document the path. The file should capture only important durable facts, not noise.

5. After memory ingestion, begin building SoberFuture.me locally first, then prepare the AWS foundation needed for a smooth build and viable operation.

EXECUTION RULES

- Read all listed files completely before making architectural changes.
- Treat MasterOrchestrator.md as a controlling architecture brief and honor its planning, privacy, safety, and approval logic.
- Treat the current user instruction as explicit approval for DEV-ONLY AWS bootstrap needed to start the build, but not for destructive changes or production deployment.
- Use official docs and package docs for anything version-sensitive.
- If a command or service detail is uncertain, verify first instead of guessing.
- Work in small resumable steps.
- Keep task ledger and progress artifacts updated as you go.
- Do not stop at analysis only. Build forward.

PHASE 1 ... MEMORY INGESTION AND STATE RECOVERY

A. Read every listed file fully.
B. Inspect the SoberFuture folder structure and detect:
- current apps
- services
- packages
- infra
- ml
- docs
- MCP registry or server definitions
- existing runbooks
- any memory files
- any build scripts
- any environment templates
C. Update the long-term memory file with:
- product mission
- architecture direction
- non-negotiable rules
- active MCP server plan
- Slack operating model
- AWS direction
- CI/CD direction
- safety/privacy constraints
- current blockers
- important durable user preferences
- current repo state
D. Do not store secrets or credential values in memory.

PHASE 2 ... LOCAL BUILD FOUNDATION

Inside the local SoberFuture workspace:
1. Normalize and inspect the repo layout.
2. Create missing directories and bootstrap files only where needed.
3. Initialize the coding/runtime stack needed to complete the build:
- Node.js/TypeScript for web and frontend tooling if appropriate
- Python for backend/services/automation if appropriate
- Docker support if helpful
- additional languages only if actual dependencies require them
4. Ensure the project is runnable locally with clear commands.
5. Create or update:
- README
- task ledger
- progress log
- approval queue
- ADR docs if missing
- MCP registry if missing
6. Verify snapshot or equivalent memory/session retention features are enabled if available in this environment. If not available, document the limitation and continue.

PHASE 3 ... MCP SERVER PREP

Prepare the project for the MCP servers needed for SoberFuture. Use existing docs and state as source of truth. At minimum, evaluate and scaffold or validate support for:
- mcp-slack
- mcp-github
- mcp-browser
- mcp-aws-docs
- mcp-repo-context
- mcp-package-docs
- mcp-adr

For each MCP server:
- confirm purpose
- confirm auth model
- define least-privilege permissions
- define manifest/health/test expectations
- document status
- register or update it in the central MCP registry

PHASE 4 ... AWS DEV FOUNDATION

Using credentials from /home/arnieai/.matrix_credentials.env only as needed and without exposing them:
1. Discover current AWS identity and region.
2. Inspect whether relevant S3 buckets, EC2 instances, IAM roles, or supporting resources already exist for SoberFuture.
3. If absent, create DEV-ONLY AWS foundation resources needed to move the build forward, with careful naming, tagging, and cost awareness:
- one virtual server appropriate for the persistent build/orchestration role
- required S3 buckets for build artifacts, logs, and project storage as justified
- only the minimal supporting resources necessary for viable dev operation
4. Use least privilege and document every resource created.
5. Do not create production resources.
6. Do not destroy or alter unrelated existing resources.
7. Prefer infrastructure-as-code artifacts where practical, even if you also perform initial dev provisioning.
8. Record exact resource names, purpose, and next steps in docs, but never record secrets.

PHASE 5 ... START BUILDING SOBERFUTURE.ME

Begin actual implementation locally after memory ingestion and AWS dev foundation prep:
- align the codebase with the project docs
- start with the highest-leverage foundation work
- move from architecture into scaffold into working implementation
- create measurable progress
- prepare for GitHub-first CI/CD to AWS Amplify
- leave the project in a cleaner, more resumable state than you found it

SECRET HANDLING RULES

- Never echo contents of /home/arnieai/.matrix_credentials.env
- Never write secret values to markdown, code comments, logs, task ledger, or memory files
- Never commit secrets
- If credentials appear exposed in any file, note “credential rotation required” without repeating the secret

DELIVERABLES REQUIRED

Produce and/or update:
1. Long-term memory file inside SoberFuture
2. Updated task ledger
3. Progress log
4. Any missing repo/bootstrap artifacts needed
5. MCP registry updates
6. AWS dev foundation notes
7. Clear summary of what was read, what was changed, what was created, and what remains next

FINAL OPERATING STYLE

- Be decisive
- Be methodical
- Do not hallucinate
- Do not ask unnecessary questions
- Use the available files and repo as source of truth
- Continue forward until the project is materially advanced