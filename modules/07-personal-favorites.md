# Module 07: own a full-stack feature

**Outcome:** Convert shared favorites into personal favorites through six reviewable slices. Allow 22-30 hours, including data-policy review and integration. This is the core project's largest module.

## Lesson

The current app stores `Page.IsFavorite`, so everyone sees the same star. The requested behavior belongs to a member/page relationship. Changing the table alone is insufficient: tree DTOs, detail responses, favorites lists, search filters, and UI refresh behavior all expose the meaning of "favorite." A feature is complete when those surfaces agree for the current caller.

## Product contract and guided lab

Use [the data guide's backfill policy](../handbook/data-and-permissions.md) as the default. Members may star pages they can read; repeated favorite/unfavorite requests have the same final effect as one; foreign-workspace access is hidden; unreadable and trashed pages stay absent from results. Soft delete retains relationships for a later permitted restore. New members do not automatically inherit future stars from others.

Map every `IsFavorite` occurrence before editing. Run `rg -n 'IsFavorite|isFavorite|favorites'` within the app's source directories. Record each write and projection, then track it through the six slices. Preserve the old schema until the backfill and transition are tested; cleanup comes in AST-054.

<a id="ast-043"></a>

### AST-043 — Decide ownership and historical-data policy

**Mode:** Practice · **Estimate:** 2 hours · **Depends on:** AST-042

**Story:** As a workspace member, I want my favorites independent of others so that my navigation reflects my own work.

**Start here:** [shared-favorite architecture](https://github.com/elirc/folio-app/blob/main/docs/architecture.md), [PageService](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/PageService.cs), [ADR template](../templates/adr.md).

**Acceptance:**
- Record current behavior with Ada and Grace, then specify the desired independent behavior.
- Accept/document the default readable-member backfill or an explicitly reviewed alternative.
- Define repeated requests, soft delete/restore, access revocation, and new-member behavior.

**Verify:** Review example tables before implementation; identify every caller-visible projection that needs changing.

**Hint / review:** The old boolean cannot tell you who originally clicked the star. Do not invent that history.

<a id="ast-044"></a>

### AST-044 — Add the member-page relationship

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-043

**Story:** As a maintainer, I want persistent favorite ownership so that independent preferences survive restarts and upgrades.

**Start here:** [Domain entities](https://github.com/elirc/folio-app/tree/main/server/Folio.Domain/Entities), [DbContext](https://github.com/elirc/folio-app/blob/main/server/Folio.Infrastructure/Persistence/FolioDbContext.cs), [migrations](https://github.com/elirc/folio-app/tree/main/server/Folio.Infrastructure/Persistence/Migrations).

**Acceptance:**
- Introduce a new favorite entity/relationship with member/page references and a database uniqueness guarantee.
- Add a reviewed migration/backfill; keep legacy storage during transition.
- Fresh and pre-change databases reach the expected rows without duplicates or inaccessible backfill entries.

**Verify:** Migration guard, old-data upgrade test, and constraint test all establish distinct requirements.

**Hint / review:** A service-level existence check does not replace a unique key under competing requests.

<a id="ast-045"></a>

### AST-045 — Make favorite writes belong to the caller

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-044

**Story:** As a member, I want starring and unstarring to change only my preferences so that I cannot alter another member's navigation.

**Start here:** [PageService favorite methods](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/PageService.cs), [PagesController](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Controllers/PagesController.cs), [CurrentMember](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Auth/CurrentMember.cs).

**Acceptance:**
- Keep existing favorite routes while taking member identity from the authenticated accessor.
- Favorite/unfavorite apply read-access policy and change only that member/page relationship.
- Repeated operations succeed consistently and duplicate races cannot create two rows.

**Verify:** API cases cover two members, Viewer read access, cross-workspace denial, repeated operations, and unchanged other-member state.

**Hint / review:** Define how a unique-constraint race becomes the intended idempotent API outcome instead of an accidental 500.

<a id="ast-046"></a>

### AST-046 — Make every favorite read caller-specific

**Mode:** Extend · **Estimate:** 4 hours · **Depends on:** AST-045

**Story:** As a member, I want the tree, detail, list, and search to agree about my favorites so that switching views never shows another person's stars.

**Start here:** [PageService](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/PageService.cs), [SearchService](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/SearchService.cs), [Page DTOs](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Contracts/PageDtos.cs).

**Acceptance:**
- Existing `isFavorite` response fields become caller-relative without changing their wire type.
- Favorite listing and favorite-filtered search join/filter by the current member and current visibility.
- No per-row lookup is required to project a page tree's favorite membership.

**Verify:** For two members, compare tree/detail/favorites/search before and after one member stars a page; include access revocation.

**Hint / review:** The sidebar derives favorites from tree data. Updating only the dedicated favorites endpoint is insufficient.

<a id="ast-047"></a>

### AST-047 — Integrate personal favorites into the UI

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-046

**Story:** As a member, I want accurate star feedback in the page and sidebar so that I can trust my saved shortcuts.

**Start here:** [PageView](https://github.com/elirc/folio-app/blob/main/client/src/components/PageView.tsx), [FavoritesList](https://github.com/elirc/folio-app/blob/main/client/src/components/FavoritesList.tsx), [WorkspacePage](https://github.com/elirc/folio-app/blob/main/client/src/pages/WorkspacePage.tsx).

**Acceptance:**
- Update help text to explain personal favorites now that the server implements them.
- A successful toggle refreshes page and tree consistently; a failed toggle displays an error without a false saved state.
- Changing sessions does not retain the previous member's displayed favorite state.

**Verify:** Component failure/session cases plus a two-profile manual demonstration and reload.

**Hint / review:** An optimistic toggle is optional. If you use it, define rollback and prevent uncontrolled competing toggles.

<a id="ast-048"></a>

### AST-048 — Demonstrate the feature end to end

**Mode:** Practice · **Estimate:** 2 hours · **Depends on:** AST-047

**Story:** As a reviewer, I want one coherent favorites demonstration so that I can approve the complete behavior across its separate patches.

**Start here:** Your AST-043 contract, [PR template](../templates/pull-request.md), [testing guide](../handbook/testing.md).

**Acceptance:**
- Demonstrate independent stars, repeated requests, refresh/restart, filtered search, and loss of visibility.
- Show old-data upgrade evidence and note that the obsolete boolean remains until cleanup.
- Explain any residual risk in overlapping operations and link follow-up work in Module 08.

**Verify:** Run affected server suites, the client suite/build, and record all outcomes against acceptance criteria.

**Hint / review:** A complete feature can span several patches, but its final review needs evidence that they work together.

## Exit check

Two independently authenticated sessions see their own stars on every specified surface. Continue to [Module 08](08-debugging-and-concurrency.md).
