# Graduation capstones

Complete the core path through AST-060 and at least one elective, then choose **one** capstone. Budget 20-35 focused hours including review and rework. These are larger assignments with less prescribed implementation; they are separate from the 96 module stories.

Before building, fill in the [proposal template](../templates/capstone-proposal.md). Inspect the current source and record the baseline. A mentor should review the product contract and scope, especially migration or ownership decisions. Solo learners can write and revisit a self-review before implementation.

## Capstone A: organize Folio pages with workspace tags

**Best fit:** Full-stack work, with any elective. **Target:** `folio-app`.

**User story:** As a workspace member, I want to label pages with reusable tags and find readable pages by tag so that I can organize knowledge beyond its folder tree.

### Scope and proposed contract

Add workspace-owned tags and page/tag relationships. Use a display name trimmed to 1-40 characters and a documented normalized key unique within a workspace. For this capstone, use an explicit invariant normalization policy consistently in service validation and database uniqueness; do not rely on whichever collation happens to be the default. An Owner or Editor can create a workspace tag. Attaching/removing a tag from a page requires that caller's existing page-write permission. Reading tags for a page requires page-read permission. Workspace tag definitions are shared metadata; tag-filtered page results must still hide private/foreign/trashed pages.

Keep tag deletion, renaming, color selection, bulk import, full-text ranking, and collaborative live editing out of the initial scope. One list/create tag endpoint, page attach/remove operations, and a bounded readable-page filter are sufficient. A repeated attach/remove should have the documented idempotent effect.

### Starting points

- [Page entity](../../folio-app/server/Folio.Domain/Entities/Page.cs) and [DbContext](../../folio-app/server/Folio.Infrastructure/Persistence/FolioDbContext.cs).
- [PageAuthorization](../../folio-app/server/Folio.Api/Auth/PageAuthorization.cs) and [SearchService](../../folio-app/server/Folio.Api/Services/SearchService.cs).
- [PageView](../../folio-app/client/src/components/PageView.tsx) and [SearchPage](../../folio-app/client/src/components/SearchPage.tsx).
- [API factory](../../folio-app/server/Folio.Tests/FolioApiFactory.cs) and existing component test helpers.

### Acceptance scenarios

| Given | When | Then |
| --- | --- | --- |
| Ada is in Acme | Creates `Runbooks` and then its normalized equivalent | Only one tag identity exists; duplicate behavior follows the documented API contract |
| Eve is in Globex | Creates `Runbooks` | It is independent of Acme's tag |
| Grace can edit a workspace page | Attaches a tag twice | One relationship exists; page and filter agree |
| Linus is a Viewer | Attempts an attachment directly through HTTP | Denied; no relationship changes |
| A tagged page becomes private | Linus filters by its tag | The private page/title is absent |
| A page is soft-deleted | A permitted user filters by tag | The page stays absent until a permitted restore |
| An old database has pages and personal favorites | The tag migration is applied | Existing pages, summaries, and favorites survive |
| The UI attachment request fails | The user tries again | Error feedback is clear and there is no false persisted tag |

### Delivery slices

1. Contract, data model, normalization decision, and baseline.
2. Migration plus tag create/list operations and ownership tests.
3. Page relationships and filtered reads with permission/duplicate evidence.
4. Accessible UI picker/filter, pending/error states, and typed client changes.
5. Upgrade rehearsal, complete demo, focused performance observation, and handoff.

**Reviewer variation:** Ask the learner how tag renaming would affect the normalized unique key, page relationships, and URL-based filters. An implementation is optional during the review; an accurate impact analysis is required.

## Capstone B: copy a saved view without copying ownership

**Best fit:** Integration or domain-design elective. **Target:** `tracer-net`.

**User story:** As an issue-tracker user, I want to copy a saved view I am allowed to read into a view I own so that I can customize its filters without changing someone else's view.

The project already has saved views. Your work extends that feature; first prove its current ownership, visibility, and filter rules from source. Do not build a parallel saved-view subsystem. The new copy must use the current caller as owner and stay in an authorized team. Start with same-team copies only. A readable public/team view may be copied under the existing policy; a foreign or unreadable view must not leak its filter/title through a copy response. The new view receives a fresh id and the caller-supplied validated name. Changes to the copy never alter the source.

### Starting points

- [Saved-view rules tests](../../tracer-net/tests/Tracer.Tests/Unit/SavedViewRulesTests.cs).
- [Saved-view API tests](../../tracer-net/tests/Tracer.Tests/Integration/SavedViewsApiTests.cs).
- [API source](../../tracer-net/src/Tracer.Api) and [domain source](../../tracer-net/src/Tracer.Domain), searched for `SavedView`.
- [Getting started](../../tracer-net/docs/getting-started.md) and [API reference](../../tracer-net/docs/api-reference.md).

### Acceptance and boundaries

- Copying a readable saved view creates a new independent id, current-caller ownership, same authorized team, and equivalent supported filters.
- Invalid new names/filters produce the existing ProblemDetails style and create no partial row.
- Foreign-team/unreadable sources follow the existing existence-hiding policy.
- The request cannot select another user's ownership by supplying an arbitrary owner field.
- Editing/removing the new view leaves the original untouched.
- Specify retry behavior: this is a create operation, so either repeated requests create distinct copies by contract, or add an explicitly scoped idempotency mechanism. Do not call accidental duplicate creation idempotent.
- Return a documented response and add an example HTTP walkthrough; there is no frontend requirement for this backend capstone.

### Delivery slices

Inspect existing behavior and decide the endpoint contract; implement the copy use case through current validation/authorization; add independent-copy and denied-copy integration cases; update API docs; demonstrate a full create-source/copy/change-copy/read-source journey. Include a migration only if the implementation needs schema changes, and justify that need.

**Reviewer variation:** Ask whether a copied filter should retain a reference to a deleted label, and how the current query contract treats that reference. The learner should locate the existing semantics before choosing a new policy.

## Capstone C: preview a checkout without side effects

**Best fit:** Commerce elective. **Target:** `agora-net`.

**User story:** As a shopper, I want a server-calculated checkout preview so that I can understand the total before a payment attempt.

First inspect whether a preview/quote operation already exists. If it does, retain it and choose a missing contract case such as quote expiry or discount-change feedback with equivalent scope. Use the existing checkout calculation rules and fake payment boundaries. The preview must never reserve stock, consume a gift-card balance, create a paid order, or call the gateway. It is a current estimate, not a promise to honor old prices later. Submission recalculates from server data under the existing checkout policy.

### Starting points

- [CheckoutService](../../agora-net/src/Agora.Infrastructure/Services/CheckoutService.cs).
- [TaxService](../../agora-net/src/Agora.Infrastructure/Services/TaxService.cs) and [Money](../../agora-net/src/Agora.Domain/Common/Money.cs).
- [FakePaymentGateway](../../agora-net/src/Agora.Infrastructure/Services/FakePaymentGateway.cs).
- [Test projects](../../agora-net/tests/Agora.Tests) and [API reference](../../agora-net/docs/api-reference.md).

### Acceptance scenarios

- A valid owned/guest-authorized cart yields line amounts and supported discount/tax/shipping totals using the existing Money conventions.
- Client-supplied prices/totals are not authoritative inputs.
- Empty/invalid/foreign carts follow a documented consistent contract.
- Preview repeated twice leaves order count, inventory/reservations, gift-card balance, and payment call count unchanged.
- A price, availability, or applicable discount change after preview is re-evaluated by actual checkout, with the documented user-visible result.
- Shared calculation logic has one clear owner; do not copy a large checkout method and let the two implementations drift.
- All tests run with fake payments and local disposable data. No payment keys, cloud deployment, or real charges are required.

### Delivery slices

Map calculation versus side effects and write the contract; extract only the pure/read calculation boundary needed for reuse; implement the preview endpoint with existing access rules; prove side-effect absence and calculation consistency; update API docs and record a preview-then-change-then-submit walkthrough.

**Reviewer variation:** Ask whether a preview should be valid for a fixed time and what stronger guarantee would require. The learner should distinguish displaying an expiry from actually reserving price/stock.

## Final evidence pack for any capstone

Submit a reviewed proposal, scoped commits/diffs, applicable ADR, acceptance-to-evidence table, actual check outcomes, and a short handoff with limitations. Demo the main journey and a failure/denial, then answer the reviewer variation. Use the [rubric](../handbook/mentoring-and-assessment.md). Public publishing or deployment is optional and outside the required learning exercise.
