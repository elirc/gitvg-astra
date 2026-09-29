# Guided lab: make the empty favorites area useful

The current [FavoritesList](../../folio-app/client/src/components/FavoritesList.tsx) flattens the page tree, filters `isFavorite`, and returns `null` when there are no favorites. Your first change is small: help a new user discover how to add their first favorite.

**User story:** As a new workspace member, I want an explanation in an empty Favorites section so that I know how to make useful pages easy to find.

## Before coding

1. Complete setup and the Git boundary checks.
2. Open the component and its caller in [Sidebar](../../folio-app/client/src/components/Sidebar.tsx).
3. Inspect the existing star control in [PageView](../../folio-app/client/src/components/PageView.tsx) so the new wording matches a real action.
4. Predict the JSX that renders when the input tree is empty, contains only unstarred pages, and contains a starred descendant.
5. Create a contribution branch inside `folio-app`.

## Acceptance criteria

- An empty tree and a tree with zero favorites both show a Favorites label and concise help text.
- A nonempty favorites list still links to the same workspace/page routes.
- The help text describes the actual star control and does not imply favorites are personal yet; current favorites are shared.
- The text is readable at a narrow viewport and does not become a fake interactive control.
- The diff is limited to the empty-state behavior and directly related evidence.

## Implement in four steps

First keep the existing derived `favorites` array. Do not add state for a value already determined by props. Next render the section shell in both states and use a condition inside it for the empty explanation or list. Then check the heading/label semantics against the sidebar's existing structure. Finally inspect the populated state again; an empty-state improvement must not break the working branch.

Do not copy a complete answer from this guide. Sketch the two branches yourself. If stuck, remember that returning `null` removes the whole component from the DOM, while a conditional inside the wrapper preserves the section label.

## Check the change

Inspect the sidebar in the browser with no favorites, then star one page and verify the link appears. Resize the window and use the keyboard to open the link. Run the existing sidebar test file from `folio-app/client`:

```powershell
pnpm.cmd exec vitest run src/components/Sidebar.test.tsx
pnpm.cmd build
```

For this small presentation change, a recorded manual check plus existing relevant tests is sufficient. In Module 03 you will learn to add a behavior-focused component test for nested favorites; do not add a snapshot merely to encode the exact markup you just wrote.

## Review and handoff

Inspect the diff, stage the specific changed files, and write a commit whose subject describes the user-visible result. Fill in the PR template, including both empty and populated demonstrations and the actual commands you ran. Ask a reviewer whether the copy accurately describes the current shared-favorite behavior.

In your journal answer: Why is this derived data? What does a key do in the list? What behavior could a screenshot fail to establish? Where would an API change belong if the product requirement became personal favorites?

This lab supplies the implementation context for AST-007 and AST-008. Do it once and reuse the evidence; those story IDs divide the implementation and review work, not two repetitions of the lab.
