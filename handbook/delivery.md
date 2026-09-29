# Deliver a change another developer can operate

Delivery includes the code, the explanation, the evidence, and the recovery path. A learner can practice all four locally. Public deployment is not a requirement of this bootcamp.

## Definition of ready

A story is ready when its user benefit is understandable, current behavior is recorded, acceptance examples are observable, source/test entry points are identified, prerequisites are satisfied, and ambiguous data-policy decisions are resolved. A list of files to edit is not a requirement. If a story exceeds about one or two focused sessions, identify an independently reviewable slice.

## Definition of done

- Acceptance criteria have evidence: test names, request examples, or an appropriate manual demonstration.
- Existing behavior affected by the patch still works, including relevant permission and failure paths.
- The diff contains only this work and has been read after staging.
- Types, migrations, seed data, and documentation agree with the implementation where affected.
- Relevant focused checks and required project gates have recorded results; inherited failures are identified separately.
- A real review or explicitly labeled self-review has considered the changed behavior and trade-offs.
- The learner can explain the code, one failure path, and one material limitation.

For study stories, a source-backed explanation and reviewed exercise output replace a product-code diff. For low-impact copy/documentation changes, direct inspection can be enough; do not generate artificial unit tests for prose. For permissions, persistence, retries, and races, require meaningful behavioral evidence.

## Folio App verification sequence

From the workspace root, run server checks:

```powershell
dotnet build .\folio-app\server\Folio.slnx
dotnet test .\folio-app\server\Folio.slnx
```

From `folio-app/client`, after dependencies are installed:

```powershell
pnpm.cmd test
pnpm.cmd build
```

After entity/mapping changes, include the migration guard and an upgrade fixture when existing-data behavior changes. After UI/API integration changes, replay the primary flow with both processes running. The inspected Folio App does not have a checked-in CI workflow or browser E2E harness. AST-057 may add repeatable verification; record that as a new deliverable rather than claiming it already existed.

When implementing a PowerShell runner, capture/check `$LASTEXITCODE` after each native command and exit with failure when required. Use a task-specific directory variable, restore the caller's directory in a `finally` block if you change it, and quote paths. A script that prints failures but exits zero is not a verification gate.

## Write a useful PR

Lead with the problem and resulting behavior. Example: "Favorites previously used one boolean per page. They now belong to the current member, so Ada's star no longer changes Grace's sidebar. Tree, detail, favorites list, and filtered search use the same caller-relative meaning."

Then give verification and the key review decision: "Upgrade backfills stars for current members who can read each historically starred page. This preserves their visible shortcuts without claiming to know the original actor. The obsolete column is removed only after the new reads/writes are established."

Do not recount every abandoned implementation. Include a trade-off when it helps a reviewer assess the final design. Use the [PR template](../templates/pull-request.md), and use actual issue/CI links only when they exist.

## Migration and release rehearsal

Make a disposable pre-change database, apply the release candidate, verify its data, and record the schema/code pair. Rehearse a fresh install too; the two paths test different things. Back up the database consistently with connections closed or an appropriate database backup operation. Never assume an arbitrary live file copy is a consistent SQLite snapshot.

Discuss code rollback and data rollback separately. Dropping `Page.IsFavorite` means an older executable may no longer understand the schema. Restoring a backup may lose writes made since the backup. A forward fix may be preferable. The local exercise should state a chosen fallback, its prerequisites, and its data-loss window, and prove it on copies.

## Operational handoff

A short runbook should identify the affected feature, how to start/check it, a healthy response, useful logs/identifiers, known failure symptoms, and recovery actions with their limits. Separate diagnosis from actions that mutate data. Do not include tokens, full page content, or real connection secrets in examples.

Useful local observations include HTTP status, request duration, query count, a trace identifier, and a job's state/attempt count. Do not add user ids or page titles as arbitrary high-cardinality metric labels merely to make a dashboard detailed. The observation should answer a concrete support question.
