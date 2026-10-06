# Module 08: preserve correctness when work overlaps

**Outcome:** Distinguish stale requests from genuinely overlapping writes, preserve user input, and complete migration cleanup. Allow 18-26 hours.

## Lesson

"Async" does not imply safe concurrency. Two requests can both read the same old state before either saves. A token compared only in application memory protects fewer cases than a conditional database write. Likewise, idempotency is about the effect of repeating an operation, while ordering determines which competing operation wins. Establish the actual invariant before choosing a mechanism.

## Guided lab

Read [optimistic-concurrency ADR](https://github.com/elirc/folio-app/blob/main/docs/adr/0009-optimistic-concurrency.md), [PageService](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/PageService.cs), and [ConcurrencyEdgeTests](https://github.com/elirc/folio-app/blob/main/server/Folio.Tests/ConcurrencyEdgeTests.cs). Label existing cases as sequential stale checks or overlapping-write evidence. Do not claim a vulnerability from a hunch: first build the reproduction or record exactly what remains unproven.

<a id="ast-049"></a>

### AST-049 — Reproduce a stale edit precisely

**Mode:** Characterize · **Estimate:** 2 hours · **Depends on:** AST-048

**Story:** As an editor, I want stale edits rejected so that an old browser view cannot overwrite a completed newer edit.

**Start here:** [ProductionReadinessTests](https://github.com/elirc/folio-app/blob/main/server/Folio.Tests/ProductionReadinessTests.cs), [PageView tests](https://github.com/elirc/folio-app/blob/main/client/src/components/PageView.test.tsx).

**Acceptance:**
- Read a version, complete a newer update, then submit the old version and observe 409.
- Verify the accepted title remains stored and the rejected title does not.
- Record the current behavior when expectedVersion is omitted as a separate compatibility case.

**Verify:** Reuse existing evidence or add a missing summary-update case; write the exact request timeline.

**Hint / review:** This proves rejection after a completed update, not simultaneous writes.

<a id="ast-050"></a>

### AST-050 — Preserve a user's conflicting draft

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-049

**Story:** As an editor encountering a conflict, I want my unsaved text preserved so that I can compare and deliberately reapply it.

**Start here:** [PageView](https://github.com/elirc/folio-app/blob/main/client/src/components/PageView.tsx), [PageView tests](https://github.com/elirc/folio-app/blob/main/client/src/components/PageView.test.tsx).

**Acceptance:**
- Replace the alert/reload conflict interaction with accessible inline feedback that retains the attempted value.
- Offer explicit reload/discard and deliberate reapply after fetching the latest version; never silently overwrite.
- A second conflict remains recoverable and does not erase the draft.

**Verify:** Component tests distinguish stored/latest value from draft through two conflicts, plus a two-session demo.

**Hint / review:** Fetching a newer version is not user consent to overwrite it.

<a id="ast-051"></a>

### AST-051 — Investigate the overlapping-write guarantee

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-050

**Story:** As a maintainer, I want evidence about simultaneous updates so that I do not overstate what the version check guarantees.

**Start here:** [PageService](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/PageService.cs), [DbContext](https://github.com/elirc/folio-app/blob/main/server/Folio.Infrastructure/Persistence/FolioDbContext.cs), [API factory](https://github.com/elirc/folio-app/blob/main/server/Folio.Tests/FolioApiFactory.cs).

**Acceptance:**
- Inspect whether Version is an EF concurrency token or part of a conditional update, and document the actual protection.
- Design two writes that both read the same version before either commits, using isolated contexts and explicit synchronization.
- Record whether the storage fixture can support the overlap; distinguish lock/fixture failures from the business outcome.

**Verify:** A deterministic reproduction or a precisely bounded investigation report establishes the missing guarantee.

**Hint / review:** Sharing the factory's single SQLite connection may be unsuitable for concurrent requests; use a disposable fixture designed for independent connections.

<a id="ast-052"></a>

### AST-052 — Enforce the agreed version invariant

**Mode:** Extend · **Estimate:** 4 hours · **Depends on:** AST-051

**Story:** As an editor, I want at most one competing edit based on the same version accepted so that overlapping requests cannot silently lose work.

**Start here:** [Page entity](https://github.com/elirc/folio-app/blob/main/server/Folio.Domain/Entities/Page.cs), [Block entity](https://github.com/elirc/folio-app/blob/main/server/Folio.Domain/Entities/Block.cs), [PageService](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/PageService.cs), [BlockService](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/BlockService.cs).

**Acceptance:**
- Add or verify database-enforced concurrency for versioned page/block updates, translating a detected conflict to the existing 409 contract.
- Define omitted-token compatibility explicitly and preserve unrelated access/error semantics.
- Rejected writes leave content/history/activity consistent; all mutation paths that rotate versions are reviewed.

**Verify:** The AST-051 overlapping fixture and sequential stale cases pass for the accepted invariant; run migration guards if mapping changes.

**Hint / review:** Handle the specific concurrency failure; a catch-all that turns every persistence exception into 409 hides defects.

<a id="ast-053"></a>

### AST-053 — Exercise concurrent favorite operations

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-052

**Story:** As a member retrying a star action, I want a stable final result so that duplicate requests cannot create duplicate shortcuts or an unexpected server error.

**Start here:** Your favorite relationship/write methods and [testing guidance](../handbook/testing.md).

**Acceptance:**
- Two duplicate favorites for the same member/page produce one row and the documented successful outcome.
- A different member's concurrent favorite remains independent.
- Define the expected policy for competing favorite/unfavorite requests; do not label final ordering as idempotency.

**Verify:** Use independent database connections and controlled overlap where required; fix a discovered violation in a separate focused patch.

**Hint / review:** A unique constraint protects rows; API exception translation determines whether the user sees success or 500.

<a id="ast-054"></a>

### AST-054 — Remove the obsolete shared-favorite field

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-053

**Story:** As a maintainer, I want one authoritative favorite model so that future features cannot accidentally revive workspace-wide stars.

**Start here:** [Page](https://github.com/elirc/folio-app/blob/main/server/Folio.Domain/Entities/Page.cs), [DbSeeder](https://github.com/elirc/folio-app/blob/main/server/Folio.Infrastructure/Persistence/DbSeeder.cs), your migrations and favorite projections.

**Acceptance:**
- After backfill/read/write verification, remove the old storage property through a new reviewed migration and update seed behavior.
- Retain caller-relative `isFavorite` DTO fields; distinguish them from the obsolete entity field.
- Update architecture/ADR notes and test upgrade through both introduction and cleanup migrations.

**Verify:** Search runtime source for remaining old storage reads, run migration/data/permission checks, and preserve historical migration files.

**Hint / review:** Do not rewrite already-applied migration history to make the final schema look cleaner.

## Exit check

Explain precisely what is guaranteed under retries and overlap, and show a conflict without lost draft text. Continue to [Module 09](09-performance-and-delivery.md).
