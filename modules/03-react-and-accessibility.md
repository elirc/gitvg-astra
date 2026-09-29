# Module 03: build usable interface states

**Outcome:** Make existing UI behavior understandable with a keyboard, a slow request, and an error. Allow 12-18 hours. Read the component sections of [testing](../handbook/testing.md).

## Lesson

Props are inputs, state is local memory, and derived values should normally be computed from those inputs. A component also has a user-facing state machine: idle, loading, success, empty, error, or saving. Accessibility is part of that behavior. Labels, focus, keyboard operation, and honest feedback determine whether a user can complete a task.

## Guided lab

Inspect the empty Favorites change and the Quick Open modal. Draw each UI state before editing. Use a native button for an action and a link for navigation. Test through accessible names. When adding an error or dialog, decide where focus starts, where it goes next, and how the user can recover.

<a id="ast-019"></a>

### AST-019 — Protect nested favorite navigation

**Mode:** Characterize · **Estimate:** 1.5 hours · **Depends on:** AST-018

**Story:** As a member, I want starred nested pages to remain reachable so that reorganizing documentation does not hide my shortcuts.

**Start here:** [FavoritesList](../../folio-app/client/src/components/FavoritesList.tsx), [router test helper](../../folio-app/client/src/test/renderWithRouter.tsx).

**Acceptance:**
- Cover a starred grandchild under unstarred ancestors and two pages with the same title.
- Assert correct link destinations and absence of unstarred pages in the favorites section.
- Preserve the input tree; avoid asserting private traversal helpers.

**Verify:** Add a focused component case where existing coverage is absent and run it plus Sidebar tests.

**Hint / review:** Scope queries to the Favorites section if the sidebar also renders the ordinary tree.

<a id="ast-020"></a>

### AST-020 — Make notification loading honest

**Mode:** Extend · **Estimate:** 2 hours · **Depends on:** AST-019

**Story:** As a member opening my inbox, I want loading and failure feedback so that I do not confuse an unavailable inbox with zero notifications.

**Start here:** [NotificationInbox](../../folio-app/client/src/components/NotificationInbox.tsx), [inbox tests](../../folio-app/client/src/components/NotificationInbox.test.tsx).

**Acceptance:**
- Show distinct loading, empty, success, and recoverable-error states, retaining existing states that already satisfy this.
- A retry after failure can show notifications; pending feedback is accessible.
- Mark-read behavior remains scoped to the displayed notification.

**Verify:** Use controlled fetch responses for pending, failure, and recovery; add only missing behavior coverage.

**Hint / review:** An empty array cannot by itself tell you whether loading finished successfully.

<a id="ast-021"></a>

### AST-021 — Help users enter valid page titles

**Mode:** Extend · **Estimate:** 2 hours · **Depends on:** AST-020

**Story:** As an editor, I want title validation before saving so that I can correct my input without losing it.

**Start here:** [PageView](../../folio-app/client/src/components/PageView.tsx), [PageDtos](../../folio-app/server/Folio.Api/Contracts/PageDtos.cs).

**Acceptance:**
- Show a character count and an associated message for a blank/whitespace title or a title over 400 characters.
- Invalid input does not send a rename request and remains editable.
- A valid boundary-length title follows the existing save and version behavior.

**Verify:** Component cases for whitespace, 400, and 401 characters, then a manual valid rename.

**Hint / review:** Browser validation improves feedback; the server must still reject invalid direct requests.

<a id="ast-022"></a>

### AST-022 — Keep Quick Open focus predictable

**Mode:** Extend · **Estimate:** 2.5 hours · **Depends on:** AST-021

**Story:** As a keyboard user, I want focus managed inside Quick Open so that I can choose a page and return to my previous place.

**Start here:** [QuickOpenModal](../../folio-app/client/src/components/QuickOpenModal.tsx), [WorkspacePage](../../folio-app/client/src/pages/WorkspacePage.tsx).

**Acceptance:**
- Opening focuses search; Tab/Shift+Tab remain within the modal's interactive controls.
- Escape closes it and returns focus to the opener when that element still exists.
- Dialog semantics match modal behavior; closing by selection still navigates correctly.

**Verify:** Add missing keyboard component coverage and manually traverse the dialog with no mouse.

**Hint / review:** Initial focus already exists. Focus containment and restoration are separate requirements.

<a id="ast-023"></a>

### AST-023 — Handle empty keyboard results safely

**Mode:** Extend · **Estimate:** 2 hours · **Depends on:** AST-022

**Story:** As a keyboard user, I want result selection to stay valid when search results change so that Enter opens only an actual current result.

**Start here:** [QuickOpenModal](../../folio-app/client/src/components/QuickOpenModal.tsx), [modal tests](../../folio-app/client/src/components/QuickOpenModal.test.tsx).

**Acceptance:**
- Arrow keys with zero results cause no navigation and leave selection in a valid empty state.
- When a result set shrinks, the active option and visual selection agree.
- Announce selection through a coherent listbox/focus pattern; do not combine incompatible patterns.

**Verify:** Exercise zero-to-many and many-to-zero transitions, arrows, and Enter with accessible assertions.

**Hint / review:** `results.length - 1` is negative for an empty array. Test the transition, not just a static list.

<a id="ast-024"></a>

### AST-024 — Review the UI as a complete journey

**Mode:** Practice · **Estimate:** 1.5 hours · **Depends on:** AST-023

**Story:** As a member using a narrow screen and keyboard, I want the edited UI to work together so that individual improvements do not create a broken journey.

**Start here:** [Sidebar](../../folio-app/client/src/components/Sidebar.tsx), your changed inbox/title/modal components.

**Acceptance:**
- Complete login, page navigation, valid rename, inbox open, and Quick Open without a mouse.
- Inspect focus visibility, associated error text, overflow, and loading feedback at a narrow viewport.
- Fix one evidenced integration issue or record a clean review with concrete observations.

**Verify:** Record the journey and run the client suite/build for the integrated patch.

**Hint / review:** A collection of isolated component tests does not prove that their focus behavior composes.

## Exit check

Demo loading, empty, failure, and keyboard paths. Continue to [Module 04](04-http-and-contracts.md).
