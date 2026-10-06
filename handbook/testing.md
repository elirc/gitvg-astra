# Test behavior at the boundary that can prove it

A useful test fails for a plausible wrong implementation and passes for acceptable implementations. "The helper was called" is weaker than "a Viewer cannot rename this page and the stored title is unchanged." Choose the least expensive test that can establish the requirement.

## What each kind can establish

| Kind | Folio example | Proves | Does not prove |
| --- | --- | --- | --- |
| Pure unit | Parser or transformation with a table of inputs | Local rules, edge cases | HTTP wiring or storage |
| Component | `PageView.test.tsx` with fetch stubs | Accessible UI and request intent | A live server accepts the payload |
| API integration | xUnit through `FolioApiFactory` | Routing, auth, services, EF, migrated SQLite | Browser behavior or another DB provider's behavior |
| Migration | `MigrationGuardTests` plus an upgrade fixture | Model/schema agreement and upgrade behavior | Every historical data shape |
| Manual full journey | Browser + running local API | The assembled local flow | Repeatable coverage of all negative cases |

Folio App does not currently include a dedicated Playwright E2E harness or a client lint script. Adding a harness is an explicit later task, not a hidden prerequisite for your first contribution. Do not invent command names or claim that component tests are browser E2E tests.

## Existing harnesses

[FolioApiFactory](https://github.com/elirc/folio-app/blob/main/server/Folio.Tests/FolioApiFactory.cs) holds an open SQLite in-memory connection for the factory lifetime. That makes the database available to multiple request-scoped DbContexts. Startup uses migrations and Development seed data. `CreateAuthenticatedClient` exercises real login and adds a bearer token. A new factory per mutating test isolates state; use the existing read-only fixture pattern where appropriate.

[fetchMock.ts](https://github.com/elirc/folio-app/blob/main/client/src/test/fetchMock.ts) maps method/path combinations to responses. A mocked 204 has no body. [authTestUtils.ts](https://github.com/elirc/folio-app/blob/main/client/src/test/authTestUtils.ts) provides session helpers. Clean up stubs and session state after each case so one test cannot authenticate another accidentally.

## Write acceptance examples before mechanics

For personal favorites, start with this table:

| Setup | Action | Observable outcome |
| --- | --- | --- |
| Ada and Grace can read page P | Ada favorites P | Ada sees P starred; Grace does not |
| Ada already favorites P | Ada favorites P again | One membership row, same visible result |
| Linus can read P | Linus favorites P | Success under the read-access policy |
| Eve belongs to Globex | Eve favorites Acme P | 404; no membership created |
| P becomes unreadable | Former reader lists favorites | P is absent; title is not leaked |

For each case, decide whether HTTP, component interaction, or database inspection is needed. A join-table uniqueness test alone does not prove caller isolation in the tree DTO.

## Arrange, act, assert

Arrange only what the example requires. Act once at the public boundary. Assert the important result and, for denied writes, the absence of mutation. Prefer `getByRole`/`findByRole` and accessible names for controls. Avoid class names, private helper structure, and enormous snapshots unless those are themselves the contract.

Use data-driven tests for genuine rule matrices. Give failures descriptive case names. Do not duplicate an existing test merely to claim coverage; inspect the nearest test first and choose a missing dimension.

## Regression workflow

Reproduce the defect. Add a test that fails for the observed wrong behavior. Confirm the failure is the intended assertion, not an invalid fixture or missing import. Implement the change. Show the focused test passes, then run affected suites. If the task is characterization and the existing behavior is correct, a green first run is expected; do not manufacture a red failure.

For a UI copy change or a documentation correction, direct inspection and existing checks can suffice. Spend new-test effort on data integrity, permissions, asynchronous state, contract changes, and meaningful reusable behavior.

## Commands and evidence

```powershell
# Working directory: workspace root
dotnet test .\folio-app\server\Folio.slnx --filter 'FullyQualifiedName~PageEndpointTests'
dotnet test .\folio-app\server\Folio.slnx --filter 'FullyQualifiedName~MigrationGuardTests'
```

```powershell
# Working directory: folio-app/client
pnpm.cmd exec vitest run src/components/PageView.test.tsx
pnpm.cmd test
pnpm.cmd build
```

Record command, directory, result, and test name/assertion. Counts in old documentation can become stale; use the output you actually observed. A failure is useful evidence when you explain it. A skipped check is not a pass.

## Determinism and concurrency

Use controlled promises for request races, fake clocks/delayers where a project provides them, and explicit synchronization for competing writes. Launching two promises with `Promise.all` or two tasks together does not ensure they overlap at the database read/write boundary. A sequential stale-token test proves a narrower case. Name that limit honestly.

Watch out for shared state, order dependence, fixed sleeps, swallowed errors, and assertions that accept every status code. Run a flaky case alone and with its neighbors to find which dependency leaks. Do not solve instability by increasing arbitrary delays or disabling the test.
