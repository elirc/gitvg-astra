# Module 04: work across the HTTP boundary

**Outcome:** Treat requests, validation, errors, and asynchronous responses as an explicit contract. Allow 12-18 hours.

## Lesson

An endpoint is more than its happy-path JSON. Its method, path, authentication requirement, status codes, response shape, and failure semantics are all observable. A typed wrapper helps callers agree, but its generic type does not inspect incoming JSON. Think about how each failure changes what the user should do.

## Guided lab

Make a table for page detail, rename, and delete. Include 200/204 and applicable 400/401/403/404/409 cases. Replay a valid request, invalid title, and stale rename. Then study how the client distinguishes them. Keep request construction centralized in the existing client instead of inventing per-component fetch behavior.

<a id="ast-025"></a>

### AST-025 — Document three live contracts

**Mode:** Study · **Estimate:** 1 hour · **Depends on:** AST-024

**Story:** As a client developer, I want exact page endpoint contracts so that I can implement predictable interactions.

**Start here:** [PagesController](../../folio-app/server/Folio.Api/Controllers/PagesController.cs), [API reference](../../folio-app/docs/api-reference.md).

**Acceptance:**
- Document page GET, PUT, and DELETE with request fields, successful response/body, auth, and relevant errors.
- Identify which contract details come from source and which you exercised.
- Correct or note any mismatch between reference prose and the current implementation.

**Verify:** Replay representative requests using local seed data and redact authorization values.

**Hint / review:** A DELETE may return no content; do not assume every successful endpoint returns JSON.

<a id="ast-026"></a>

### AST-026 — Preserve useful API error detail

**Mode:** Extend · **Estimate:** 2 hours · **Depends on:** AST-025

**Story:** As a user correcting a failed action, I want a useful error message so that I know what went wrong and what to change.

**Start here:** [client.ts](../../folio-app/client/src/api/client.ts), [ProblemDetails server setup](../../folio-app/server/Folio.Api/Program.cs).

**Acceptance:**
- For ProblemDetails with title and detail, prefer useful detail for the Error message while retaining the structured problem.
- Preserve field errors for callers and use a safe status-based fallback for non-JSON or empty error bodies.
- A 401 still invokes the session-expiry handler; errors do not expose raw response markup.

**Verify:** Focused client tests cover detail+title, title-only, malformed body, and 401 lifecycle.

**Hint / review:** The current wrapper prefers title. Changing message precedence is an intentional extension, not a serialization rewrite.

<a id="ast-027"></a>

### AST-027 — Verify no-content and JSON successes

**Mode:** Characterize · **Estimate:** 1.5 hours · **Depends on:** AST-026

**Story:** As a client maintainer, I want no-content responses handled correctly so that a successful delete is not displayed as a failure.

**Start here:** [client.ts](../../folio-app/client/src/api/client.ts), [fetchMock](../../folio-app/client/src/test/fetchMock.ts).

**Acceptance:**
- A real-shaped 204 response resolves without parsing a body.
- A 200 JSON response returns the expected value; an empty successful body follows the wrapper's documented behavior.
- Distinguish a malformed success payload from a valid no-content response.

**Verify:** Add missing wrapper tests using `Response` objects with legal status/body combinations.

**Hint / review:** Do not construct a 204 with a JSON body; an invalid fixture teaches the wrong contract.

<a id="ast-028"></a>

### AST-028 — Reject invalid titles on the server

**Mode:** Characterize · **Estimate:** 2 hours · **Depends on:** AST-027

**Story:** As a workspace owner, I want invalid direct requests rejected so that bypassing browser validation cannot corrupt page titles.

**Start here:** [PageDtos](../../folio-app/server/Folio.Api/Contracts/PageDtos.cs), [PageService](../../folio-app/server/Folio.Api/Services/PageService.cs), [HardeningTests](../../folio-app/server/Folio.Tests/HardeningTests.cs).

**Acceptance:**
- Establish behavior for missing, empty, whitespace, 400-character, and 401-character titles.
- Denied updates leave the original title and relevant version unchanged.
- Explain which cases fail binding/validation and which are checked in the service.

**Verify:** Extend an existing test matrix with missing cases; prove persisted state through a fresh read.

**Hint / review:** Do not move record validation attributes to a different target without understanding the existing project convention.

<a id="ast-029"></a>

### AST-029 — Distinguish search failure from cancellation

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-028

**Story:** As a member searching pages, I want accurate feedback for my latest query so that stale results and failed requests do not mislead me.

**Start here:** [SearchBox](../../folio-app/client/src/components/SearchBox.tsx), [search tests](../../folio-app/client/src/components/SearchBox.test.tsx), [debugging](../handbook/debugging.md).

**Acceptance:**
- The latest query owns displayed results even when an obsolete promise completes later.
- Aborted requests stay quiet; real failures display a recoverable state associated with the latest query.
- Clearing the query closes/clears results and prevents a late response reopening them.

**Verify:** Controlled promises establish reverse completion; explicit failure/recovery establishes error UX.

**Hint / review:** Cleanup must guard state writes as well as cancel work; do not rely on wall-clock sleeps.

<a id="ast-030"></a>

### AST-030 — Review an API change from both sides

**Mode:** Practice · **Estimate:** 1.5 hours · **Depends on:** AST-029

**Story:** As a reviewer, I want client and server expectations checked together so that an apparently safe type change does not break the wire contract.

**Start here:** Your contract table, changed client tests, and [testing guide](../handbook/testing.md).

**Acceptance:**
- Compare mocked response shapes to real API responses for the changed behavior.
- Demonstrate valid rename, invalid rename, no-content delete, and recoverable search failure.
- Explain which guarantees remain unverified by mocks and record actual full-suite/build outcomes.

**Verify:** A reviewer can reproduce at least one success and one failure from the PR draft.

**Hint / review:** Keep compatibility separate from internal refactoring: consumers observe the wire, not your class names.

## Exit check

Explain the path from an invalid request to visible user feedback. Continue to [Module 05](05-data-and-migrations.md).
