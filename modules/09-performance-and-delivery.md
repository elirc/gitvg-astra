# Module 09: measure, verify, and hand off

**Outcome:** Deliver the core feature with reproducible checks, measured performance evidence, and a usable runbook. Allow 12-18 hours. Read [delivery](../handbook/delivery.md).

## Lesson

Performance work starts with a workload and a baseline. Count queries, rows, and requests before adding caching. Delivery starts with a reproducible environment and an honest check record. You do not need to deploy publicly to practice a release: a local release candidate, upgrade rehearsal, acceptance demo, and rollback decision are substantial engineering work.

## Guided lab

Seed a bounded disposable workspace with a stated number of pages/favorites. Measure tree/favorites reads with query logging or a test interceptor. Compare the number of database calls as the tree grows. Then run the same acceptance journey from a fresh setup and an upgraded database. Keep measurement instrumentation out of ordinary product responses.

<a id="ast-055"></a>

### AST-055 — Measure favorite projection cost

**Mode:** Characterize · **Estimate:** 2 hours · **Depends on:** AST-054

**Story:** As a member with many pages, I want favorites to remain responsive so that personal navigation scales beyond the tiny seed workspace.

**Start here:** Your tree/favorite queries, [DbContext](../../folio-app/server/Folio.Infrastructure/Persistence/FolioDbContext.cs).

**Acceptance:**
- Define a repeatable workload at two sizes and record query count, returned rows, and local timing context.
- Determine whether query count grows per page and inspect the relevant query plan/index usage.
- Separate observed results from assumptions about production-scale latency.

**Verify:** Save the fixture size, commands/instrumentation, and raw observations for comparison.

**Hint / review:** A faster second run can reflect warm caches rather than a better query.

<a id="ast-056"></a>

### AST-056 — Make one evidenced performance improvement

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-055

**Story:** As a workspace member, I want the largest demonstrated read inefficiency removed so that page navigation stays predictable.

**Start here:** AST-055 measurements and the actual favorite/tree query implementation.

**Acceptance:**
- Fix one evidenced issue, such as per-page membership reads, excessive projection, or a missing useful index.
- Preserve current-member and visibility filtering and return the same intended ordering.
- If no material issue is found, document the measurements and choose a larger bounded workload before proposing a change.

**Verify:** Repeat the same workload and permission cases, reporting query/row changes as well as timings.

**Hint / review:** A global cache keyed only by page id would be wrong for caller-relative favorite data.

<a id="ast-057"></a>

### AST-057 — Create a repeatable local verification command

**Mode:** Extend · **Estimate:** 2 hours · **Depends on:** AST-056

**Story:** As a reviewer, I want one documented way to run the required checks so that contributors do not omit a gate accidentally.

**Start here:** [client manifest](../../folio-app/client/package.json), [server solution](../../folio-app/server/Folio.slnx), [delivery guide](../handbook/delivery.md).

**Acceptance:**
- Add an application-local verification script or documented sequence for server build/test and client test/build using existing tools.
- It reports working-directory assumptions and exits nonzero on a failed command instead of continuing to report success.
- If adding CI, treat its workflow as a new deliverable and use these actual commands; do not claim a pre-existing Folio App workflow.

**Verify:** Run the command; inspect failure propagation with a controlled failing invocation in a disposable harness.

**Hint / review:** Native command failures in PowerShell need explicit exit-code handling; a printed red line is not automatically a failed script.

<a id="ast-058"></a>

### AST-058 — Write a local incident runbook

**Mode:** Practice · **Estimate:** 1.5 hours · **Depends on:** AST-057

**Story:** As the next on-call learner, I want a short runbook so that I can distinguish API unavailability, database degradation, and write conflicts.

**Start here:** [Program](../../folio-app/server/Folio.Api/Program.cs), [HealthEndpointTests](../../folio-app/server/Folio.Tests/HealthEndpointTests.cs), [debug template](../templates/debug-log.md).

**Acceptance:**
- Document symptoms, first probe, expected evidence, and recovery for unavailable API, 503 health, 409 write, and 429 throttle.
- Include correlation identifiers where the response/log actually exposes them; omit tokens and page contents.
- State when an issue requires diagnosis rather than automatic retry.

**Verify:** A teammate performs one local process-stop drill and follows the runbook to recovery.

**Hint / review:** A 409 is not fixed by restarting the server; the caller needs current state and a user decision.

<a id="ast-059"></a>

### AST-059 — Rehearse an upgrade and fallback

**Mode:** Practice · **Estimate:** 2 hours · **Depends on:** AST-058

**Story:** As a release owner, I want an upgrade rehearsal so that I understand how to preserve user data if the change needs to be withdrawn.

**Start here:** Your summary/favorites migrations, [delivery guide](../handbook/delivery.md), [baseline template](../templates/baseline.md).

**Acceptance:**
- Rehearse fresh install and old-data upgrade on disposable databases with the release candidate code.
- Explain why rolling back code alone may fail after dropping the old favorite column.
- Define a concrete local fallback using an inspected backup/compatible code pair or a forward fix; identify its data-loss window.

**Verify:** Execute the selected rehearsal on copies and record outcomes without touching shared infrastructure.

**Hint / review:** A migration's Down method existing does not make a data transformation lossless.

<a id="ast-060"></a>

### AST-060 — Deliver the core contributor demo

**Mode:** Practice · **Estimate:** 2 hours · **Depends on:** AST-059

**Story:** As a team lead, I want a complete feature handoff so that another developer can maintain the learner's work.

**Start here:** [assessment rubric](../handbook/mentoring-and-assessment.md), your PRs, ADRs, checks, and runbook.

**Acceptance:**
- Demo summary editing and personal favorites across two users, reload, access revocation, and conflict recovery.
- Show meaningful regression/upgrade evidence and measured performance results with limits.
- Explain a mentor-selected small requirement change and identify its likely code/test impact.

**Verify:** Record rubric scores with evidence and a next-practice plan; all core stories have a reviewed or accurately deferred status.

**Hint / review:** A polished demo cannot replace explaining a failure path or the source of caller identity.

## Exit check

You can own a scoped full-stack change with review. Choose any elective below, then one [capstone](../capstones/README.md). Electives are independent; you may start Module 15 immediately after this module if that is your chosen area.
