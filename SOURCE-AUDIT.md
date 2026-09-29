# Curriculum source audit

Prepared against the local workspace on **2026-09-04**. This bootcamp is based on checked-in source, project manifests, configuration, tests, architecture notes, and contribution documents. It is not a generic syllabus with substituted project names.

## Observed workspace facts

- Seventeen application directories have their own Git repositories. The workspace root has no local `.git`; Git from this directory resolves to the user-profile repository in the inspected environment.
- No applicable `AGENTS.md` was found in the checked ancestor locations or the workspace search, including hidden directories outside Git internals/dependencies.
- `folio-app` is a React/TypeScript client and .NET 10/EF Core SQLite backend. Its services are in the API project; it does not have Atlas's separate Application layer.
- Folio App's `http` launch profile uses port 5080 and Development. Vite uses port 5173 and proxies `/api` and `/health` to 5080.
- The Folio client manifest defines dev/build/preview/test/test:watch/typecheck. It has no lint or E2E script, and no checked-in `.github` workflow directory was found in that project.
- `Page.IsFavorite` is shared storage. Personal favorites, optional page summaries, and several UX improvements in this bootcamp are explicitly proposed learner work.
- The current request contracts make `ExpectedVersion` optional. The curriculum asks learners to investigate the real database concurrency protection instead of equating sequential stale checks with overlapping-write guarantees.
- Storefront's tracked code is focused on catalog functionality, while its README/course plans describe a larger eventual product. Its exercises use current catalog/money source; checkout exercises use Agora Net's implemented services.

## Verification performed for this documentation change

Source paths, package scripts, solution files, launch settings, relevant implementation/test entry points, and existing architecture caveats were inspected. Local tools reported .NET SDK 10.0.302, Node 22.16.0, and pnpm 9.12.3. Folio App's initial inspected HEAD was `c7b6ffd` and its worktree was clean.

The curriculum's checker verifies local Markdown links/fragments, unique sequential story ids, six stories per module, required story fields, valid earlier prerequisites, complete story index/tracker coverage, consistent table columns, and balanced code fences. See [the checker](scripts/check_curriculum.py) for its exact scope. Its latest run is reported in the task handoff, not treated as a permanent guarantee for future edits.

**Application dependencies were not installed and application builds/tests/dev servers were not run for this documentation-only task.** The application commands are grounded in source/configuration; their results must be established by the learner's setup baseline. Historical passing counts in application docs were deliberately not copied into current verification claims. No application features, Git history, remotes, or published issues/PRs were changed.

## Maintain the bootcamp

When an app evolves, first update the affected current-behavior statement and source links, then adapt the story while preserving its learning objective. For an already-implemented extension, require evidence and choose a comparable missing edge case. Keep the index and tracker aligned with story ids. Do not mark a student's work complete when regenerating navigation.

Use the [repository map](REPO-MAP.md) for all project entry points. Running `python astra/scripts/check_curriculum.py` from the workspace root checks documentation structure without opening app servers or contacting external services.
