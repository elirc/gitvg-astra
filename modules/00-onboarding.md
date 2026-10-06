# Module 00: become operational

**Outcome:** Run one app, identify its repository boundary, and record a trustworthy baseline. Read [first day](../onboarding/01-first-day.md) and [setup](../onboarding/02-local-setup.md). Allow 6-9 hours including explanations and setup troubleshooting.

## Lesson

An environment is a chain of dependencies: tools restore packages, compilation produces an executable, the process loads configuration, the API opens storage, and the browser calls the API. A failure at one link can look like a failure elsewhere. Check one boundary at a time. "It works" becomes useful when you attach a command, input, and observed output.

## Guided lab

Use three terminals: API, client, and commands. Create a page in the browser, read its request in Network, and locate the same route in the controller. Stop the API and predict what remains visible in the browser. Restart it and explain why stored pages survive while an in-flight request does not. Use only local seed data.

<a id="ast-001"></a>

### AST-001 — Identify the correct repository

**Mode:** Study · **Estimate:** 45 minutes · **Depends on:** None

**Story:** As a new contributor, I want to identify project boundaries so that my commits contain only the intended application's files.

**Start here:** [repository map](../REPO-MAP.md), [Git guide](../onboarding/04-git-contribution.md).

**Acceptance:**
- Record resolved Git roots for the workspace and `folio-app`, plus the app's branch and status.
- Explain why sibling `astra` notes will not enter a Folio App commit.
- Identify `folio` and `folio-app` as different implementations.

**Verify:** Attach the bounded command results to a baseline note; stage nothing.

**Hint / review:** Git searches parent directories. What would an unqualified root-level `git add -A` include in this checkout?

<a id="ast-002"></a>

### AST-002 — Establish a repeatable tool baseline

**Mode:** Practice · **Estimate:** 1 hour · **Depends on:** AST-001

**Story:** As a teammate, I want a recorded setup baseline so that I can distinguish environment failures from changes in a patch.

**Start here:** [setup](../onboarding/02-local-setup.md), [client manifest](https://github.com/elirc/folio-app/blob/main/client/package.json), [API project](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Folio.Api.csproj).

**Acceptance:**
- Record SDK, Node, and pnpm versions and the files that establish project requirements.
- Restore dependencies and record server build/test and client test/build results.
- Mark any failed or unrun check accurately, with its first useful error.

**Verify:** Another person can repeat the commands from the stated working directories.

**Hint / review:** Why can tests pass while the build fails? Does this client's manifest define a lint command?

<a id="ast-003"></a>

### AST-003 — Complete a product walkthrough

**Mode:** Practice · **Estimate:** 1 hour · **Depends on:** AST-002

**Story:** As a documentation user, I want to create and find a page so that I understand the product I will change.

**Start here:** [getting started](https://github.com/elirc/folio-app/blob/main/docs/getting-started.md).

**Acceptance:**
- Log in as Ada, create a practice page and paragraph, rename it, and find it again.
- Explain pages, blocks, workspace, tree, and trash using what you observed.
- Confirm the renamed page survives a browser refresh and API restart.

**Verify:** Record a concise walkthrough with the page id and observed persistence; do not save tokens.

**Hint / review:** Which observations prove browser state, and which prove database persistence?

<a id="ast-004"></a>

### AST-004 — Describe a request accurately

**Mode:** Study · **Estimate:** 1 hour · **Depends on:** AST-003

**Story:** As a developer investigating a rename, I want to understand its HTTP exchange so that I know where to begin debugging.

**Start here:** [code tour](../onboarding/03-code-tour.md), [typed endpoints](https://github.com/elirc/folio-app/blob/main/client/src/api/folio.ts).

**Acceptance:**
- Capture the rename method, path, status, request fields, and response fields without the authorization value.
- Locate the client function and matching controller method.
- Explain the difference between a browser URL and an API request URL.

**Verify:** Replay the rename through the setup guide's PowerShell example using a current version.

**Hint / review:** Where does `/api` go when requested through Vite on port 5173?

<a id="ast-005"></a>

### AST-005 — Recover from a stopped API

**Mode:** Practice · **Estimate:** 45 minutes · **Depends on:** AST-004

**Story:** As a developer supporting local setup, I want a precise recovery procedure so that a disconnected API does not cost a morning.

**Start here:** [troubleshooting](../onboarding/06-troubleshooting.md), [debug log](../templates/debug-log.md).

**Acceptance:**
- Stop only your API process and record the health probe and browser failure separately.
- Identify the missing boundary without editing application code.
- Restart the API, repeat the same probe/action, and record recovery.

**Verify:** A teammate can follow the written reproduction and recovery steps.

**Hint / review:** Why is an unavailable process different from an API returning 503?

<a id="ast-006"></a>

### AST-006 — Give a five-minute onboarding handoff

**Mode:** Practice · **Estimate:** 1 hour · **Depends on:** AST-005

**Story:** As the next junior joining the project, I want a concise setup explanation so that I can begin work without guessing.

**Start here:** [baseline template](../templates/baseline.md), [code tour](../onboarding/03-code-tour.md).

**Acceptance:**
- Explain the two processes, ports, storage, seed users, and project boundary from memory.
- Show one working request and one documented failure/recovery example.
- List remaining questions separately from established facts.

**Verify:** Mentor or solo recording checks your explanation against source/configuration.

**Hint / review:** Can you tell which facts are repository configuration and which are machine-specific observations?

## Exit check

Pass when you can run or precisely troubleshoot the app without hidden mentor steps. Continue to [Module 01](01-contribution.md). A blocked dependency restore is a setup blocker to resolve, not a reason to pretend subsequent runtime evidence exists.
