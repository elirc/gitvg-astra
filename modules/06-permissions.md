# Module 06: prove who can do what

**Outcome:** Validate identity, workspace scope, roles, visibility, and indirect reads. Allow 12-18 hours. Use only the local seed accounts and disposable test data.

## Lesson

Permission is a relationship among caller, resource, and action. "Logged in" is insufficient. A workspace boundary differs from a role, and a private page differs from a workspace-visible page with View permission. Listings can reveal information even when detail endpoints are protected. Start with the existing policy and apply it consistently.

## Guided lab

Use separate browser profiles or sessions for Ada and Linus; login state is stored in localStorage, so two tabs in the same browser profile do not guarantee independent users. Compare a page read, rename, comment, and favorite. Then use Eve's Globex account against an Acme page and explain the intentional 404.

<a id="ast-037"></a>

### AST-037 — Build the actual permission matrix

**Mode:** Study · **Estimate:** 1.5 hours · **Depends on:** AST-036

**Story:** As a reviewer, I want a caller/action matrix so that access decisions can be assessed without scattered assumptions.

**Start here:** [PageAuthorization](../../folio-app/server/Folio.Api/Auth/PageAuthorization.cs), [PermissionMatrixTests](../../folio-app/server/Folio.Tests/PermissionMatrixTests.cs).

**Acceptance:**
- Map Owner/Editor/Viewer, same/foreign workspace, Private/Workspace/Public, and View/Edit for representative actions.
- Explicitly record that commenting/favoriting follow read-access rules.
- Identify which existing test establishes each representative boundary.

**Verify:** Explain four selected cells using the actual policy and test, including foreign-workspace 404.

**Hint / review:** Do not multiply every dimension blindly if a policy condition makes some combinations equivalent.

<a id="ast-038"></a>

### AST-038 — Verify session expiry behavior

**Mode:** Characterize · **Estimate:** 2 hours · **Depends on:** AST-037

**Story:** As a member with an expired session, I want to return to login cleanly so that I do not continue acting under stale identity.

**Start here:** [AuthContext](../../folio-app/client/src/auth/AuthContext.tsx), [RequireAuth](../../folio-app/client/src/auth/RequireAuth.tsx), [client](../../folio-app/client/src/api/client.ts).

**Acceptance:**
- A mocked 401 clears the client token and persisted session and routes through the existing auth guard.
- A 403 or 404 does not clear a valid session.
- Test cleanup prevents one case's identity leaking into another.

**Verify:** Use existing auth helpers and add missing lifecycle coverage; inspect one real expired/invalid local token response without sharing it.

**Hint / review:** Authentication failure and resource authorization failure require different recovery.

<a id="ast-039"></a>

### AST-039 — Prove a forbidden write changes nothing

**Mode:** Characterize · **Estimate:** 2 hours · **Depends on:** AST-038

**Story:** As a page owner, I want denied operations to preserve stored content so that a correct status code cannot hide a partial mutation.

**Start here:** [PageService](../../folio-app/server/Folio.Api/Services/PageService.cs), [PermissionGating tests](../../folio-app/client/src/components/PermissionGating.test.tsx), [API factory](../../folio-app/server/Folio.Tests/FolioApiFactory.cs).

**Acceptance:**
- A Viewer directly attempting a rename or summary update gets the expected denial.
- A fresh authorized read shows title, summary, and version unchanged.
- A foreign-workspace caller receives 404 without a mutation or leaked resource detail.

**Verify:** Integration assertions inspect both response and persisted state; reuse existing cases where they already prove this.

**Hint / review:** A disabled input cannot establish any of these server guarantees.

<a id="ast-040"></a>

### AST-040 — Audit indirect page visibility

**Mode:** Characterize · **Estimate:** 2.5 hours · **Depends on:** AST-039

**Story:** As an owner of a private page, I want its title hidden from unauthorized lists so that search and navigation cannot reveal it.

**Start here:** [SearchPermissionTests](../../folio-app/server/Folio.Tests/SearchPermissionTests.cs), [LinkLeakTests](../../folio-app/server/Folio.Tests/LinkLeakTests.cs), [SearchService](../../folio-app/server/Folio.Api/Services/SearchService.cs).

**Acceptance:**
- Trace filtering in tree, search, quick-open, favorites, and backlinks.
- Select a missing access-revocation case: visible page becomes private after being referenced or starred.
- Establish that an unauthorized caller cannot obtain the current private title through the selected read path.

**Verify:** Use integration evidence; if existing tests already cover it, choose a distinct boundary and document coverage.

**Hint / review:** A stored link token can already contain old visible text; distinguish that from disclosing a newly private title.

<a id="ast-041"></a>

### AST-041 — Verify public-link revocation

**Mode:** Characterize · **Estimate:** 2 hours · **Depends on:** AST-040

**Story:** As a page owner, I want a revoked public link to stop working so that changing visibility actually removes anonymous access.

**Start here:** [PublicController](../../folio-app/server/Folio.Api/Controllers/PublicController.cs), [SharingSearchTests](../../folio-app/server/Folio.Tests/SharingSearchTests.cs).

**Acceptance:**
- An explicitly public local page is readable without a token through its slug.
- After visibility changes away from Public, the old slug cannot retrieve the page.
- Authenticated access still follows the appropriate new page policy.

**Verify:** Use a fresh page per mutating test and check the old slug after the change; add only missing coverage.

**Hint / review:** Browser cache or a previously rendered page is not proof that the server still permits the old URL.

<a id="ast-042"></a>

### AST-042 — Review a new endpoint's access policy

**Mode:** Practice · **Estimate:** 1.5 hours · **Depends on:** AST-041

**Story:** As a team lead, I want the summary and future favorites changes reviewed against existing policy so that features do not introduce inconsistent access rules.

**Start here:** Your summary endpoint, [current member accessor](../../folio-app/server/Folio.Api/Auth/CurrentMember.cs), [review template](../templates/review.md).

**Acceptance:**
- Identify the source of caller identity and the resource's workspace before reviewing permission decisions.
- Confirm the summary uses write access and personal favorites will use read access.
- Document direct and indirect tests required for the new favorites relationship.

**Verify:** A reviewer follows your access reasoning without relying on UI checks.

**Hint / review:** The favorite request must not choose an arbitrary member id supplied by the browser.

## Exit check

Explain the difference between 401, 403, and existence-hiding 404 with local examples. Continue to [Module 07](07-personal-favorites.md).
