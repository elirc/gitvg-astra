# Module 01: make and review a contribution

**Outcome:** Produce a small patch with an understandable review trail. Read the [contribution guide](../onboarding/04-git-contribution.md). Allow 6-10 hours. The first-change tutorial maps to the first two stories; reuse that work.

## Lesson

A patch should tell a reviewer which behavior changed and how you know. Branches separate lines of work, staging selects the next snapshot, and commits make progress inspectable. Small scope is a tool for reasoning: the reviewer should not need to understand five unrelated features to approve an empty-state improvement.

## Guided lab

Complete [the FavoritesList first change](../onboarding/05-first-change.md). Before coding, describe the current behavior. After coding, compare the empty and populated states. Write a PR description before opening a remote PR; ambiguity in the description often reveals ambiguity in the patch.

<a id="ast-007"></a>

### AST-007 — Explain an empty favorites section

**Mode:** Extend · **Estimate:** 1 hour · **Depends on:** AST-006

**Story:** As a new member, I want an empty Favorites explanation so that I know how to add my first favorite.

**Start here:** [first-change lab](../onboarding/05-first-change.md), [FavoritesList](https://github.com/elirc/folio-app/blob/main/client/src/components/FavoritesList.tsx).

**Acceptance:**
- Show a section label and truthful instruction when there are no favorites.
- Preserve links for starred descendants and the existing populated layout.
- Describe shared favorites accurately; do not imply they are personal yet.

**Verify:** Inspect empty/populated/narrow layouts and run the existing sidebar checks and client build.

**Hint / review:** Keep the filtered list derived from props; avoid an additional state variable.

<a id="ast-008"></a>

### AST-008 — Package the first patch for review

**Mode:** Practice · **Estimate:** 1 hour · **Depends on:** AST-007

**Story:** As a reviewer, I want a focused diff and verification record so that I can assess a new contributor's change efficiently.

**Start here:** [PR template](../templates/pull-request.md), [Git guide](../onboarding/04-git-contribution.md).

**Acceptance:**
- Stage only the intended component and any directly related evidence/documentation.
- Write a behavior-focused commit and PR draft with actual verification outcomes.
- Include a before/after explanation and one considered edge case.

**Verify:** Review `git diff --cached` before committing and record the resulting commit id in your notes.

**Hint / review:** Do not publish fabricated issue links or imply CI ran when only local checks ran.

<a id="ast-009"></a>

### AST-009 — Respond to a real review concern

**Mode:** Practice · **Estimate:** 1 hour · **Depends on:** AST-008

**Story:** As a reviewer, I want my concern investigated so that review improves the implementation instead of becoming a checklist ritual.

**Start here:** [review template](../templates/review.md), your AST-008 diff.

**Acceptance:**
- Obtain a mentor review or label a next-session self-review honestly.
- Address one concrete concern about wording, semantics, scope, or evidence.
- Explain the resulting change or an evidence-based decision to retain the design.

**Verify:** Recheck behavior affected by the response and update the PR draft.

**Hint / review:** "Done" is insufficient when the reviewer cannot see what changed or why.

<a id="ast-010"></a>

### AST-010 — Resolve a training conflict

**Mode:** Practice · **Estimate:** 1 hour · **Depends on:** AST-009

**Story:** As a contributor, I want to resolve overlapping edits so that I preserve both authors' intended behavior.

**Start here:** [Git recovery](../onboarding/04-git-contribution.md).

**Acceptance:**
- Create a disposable Git repository under your personal `astra/work` folder with a committed two-line text file.
- Branch twice from that commit, edit the same line differently, and merge to create a conflict.
- Resolve it to preserve the agreed combined meaning; commit the resolution and explain each conflict marker.

**Verify:** Show final file content and graph history; the actual application repository stays outside this exercise.

**Hint / review:** Resolve intent, not merely the markers. Inspect status before choosing continue or abort.

<a id="ast-011"></a>

### AST-011 — Recover an accidentally staged file

**Mode:** Practice · **Estimate:** 30 minutes · **Depends on:** AST-010

**Story:** As a contributor, I want to correct staging mistakes so that unrelated notes never enter a product patch.

**Start here:** Your disposable repository from AST-010 and the [Git guide](../onboarding/04-git-contribution.md).

**Acceptance:**
- Create two harmless text edits, stage both, and inspect the staged diff.
- Unstage one specific path while preserving its working copy.
- Commit only the intended edit and explain index versus working tree.

**Verify:** Show the commit diff and remaining working-tree change.

**Hint / review:** Why would `git restore -- <path>` be the wrong command for this requirement?

<a id="ast-012"></a>

### AST-012 — Split an oversized requirement

**Mode:** Practice · **Estimate:** 1 hour · **Depends on:** AST-011

**Story:** As a team lead, I want a large favorites change divided into reviewable slices so that a junior can progress with feedback.

**Start here:** [story template](../templates/user-story.md), [shared-favorite architecture](https://github.com/elirc/folio-app/blob/main/docs/architecture.md).

**Acceptance:**
- Turn "make favorites personal and reliable" into discovery, data, API, UI, and verification slices.
- Identify which slices depend on a product policy decision about existing shared stars.
- Give each slice an observable outcome rather than a filename-only task.

**Verify:** Compare your proposal with Module 07 after writing it; record one improvement to your decomposition.

**Hint / review:** A migration can be reviewable separately while the complete feature still requires an integrated demo.

## Exit check

Present the first diff and explain branch, working tree, index, commit, and PR. Continue to [Module 02](02-language-and-navigation.md).
