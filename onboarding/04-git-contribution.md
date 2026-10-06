# Contribute a small, reviewable change

Git tracks snapshots inside a repository boundary. A branch gives your work a name; a commit records a coherent change; a pull request presents the difference for review. Start by proving which repository you are in.

## 1. Verify the boundary and preserve existing work

```powershell
# Start at the workspace directory containing folio-app
git -C .\folio-app rev-parse --show-toplevel
git -C .\folio-app status --short
git -C .\folio-app branch --show-current
git -C .\folio-app remote -v
```

The first command should end in `folio-app`. The workspace root itself is not a repository; if Git answers from there at all, it has found some unrelated repository further up the directory tree. Do not use `git add .` or `git add -A` from the workspace root. `astra` is a sibling of the app repositories, so it will not be included in a Folio App commit. Save a PR-ready write-up in Astra and copy only application-specific documentation into the app when that is part of the story.

If the project has existing changes, inspect them and determine who owns them. Do not discard them to make the status clean. A separate checkout or agreed branch is preferable to mixing unrelated changes. Use the project's actual remote names and default branch; inspect them instead of assuming `origin/main` exists.

## 2. Understand the task before branching

Read the story, name its user benefit, and turn each acceptance criterion into a demonstration or assertion. Find the owning component/service and a nearby test. Decide what this patch will leave for a follow-up. An estimate is permission to split a story when it becomes too broad.

The older `CONTRIBUTING.md` files in some sibling projects describe an AI-authored course with staged persona reviews and one large sprint per PR. Astra is an active learner track: use small real contributions and honestly attributed reviews. Preserve the application's technical conventions. Do not manufacture issue numbers, approvals, or review comments to imitate course history.

## 3. Create a branch in the application

```powershell
Set-Location .\folio-app
git status --short
git switch -c astra/AST-007-first-contribution
```

This branches from your current commit. If you need the latest shared base, first inspect remotes, fetch the chosen remote, and integrate the agreed base with a clean working tree. For example, `git fetch origin` and `git merge --ff-only origin/main` apply only when those names are verified and you are on the intended base branch. Do not reset to match a remote when you have unpreserved work.

Branch names in this guide are examples; choose the story you are actually implementing. Read history with `git log --oneline -8`, `git show <commit>`, and `git blame -- <path>`. A historical comment is context, not proof that a design still fits today's requirement.

## 4. Edit, check, and inspect

Implement the smallest useful slice. Run the focused check for the behavior you changed. Before committing:

```powershell
# Working directory: folio-app
git diff --stat
git diff --check
git diff -- client/src/components/FavoritesList.tsx
git status --short
```

`git diff` shows unstaged tracked changes; newly created files also need direct inspection. Whitespace checks do not validate behavior. For a text-only UI change, inspect it in the browser and run the existing relevant component checks if affected. For data, authorization, or concurrency changes, add a meaningful regression test and run the relevant integration suite.

## 5. Stage specific files and commit

```powershell
# Example after the guided FavoritesList change; adjust paths to your patch
git add -- client/src/components/FavoritesList.tsx
git diff --cached --stat
git diff --cached
git commit -m "feat(favorites): explain how to add the first favorite"
```

Stage each new test or document explicitly as well. Read the staged diff as if you had not written it. Confirm that it contains no database files, generated build output, credentials, unrelated formatting, or another story's work. `git restore --staged -- <path>` unstages a file while preserving its working copy. `git restore -- <path>` discards working changes: use it only when you intentionally want to lose that edit.

## 6. Prepare and respond to review

Use the [PR template](../templates/pull-request.md): user problem, resulting behavior, evidence, architectural impact if any, and unresolved limitations. A draft stored in your notebook is enough until you are ready and authorized to publish in the target project. Opening issues, sending comments, pushing branches, and merging are external collaboration actions; follow your team's contribution arrangement. There is no requirement to publish every practice exercise.

If you publish, push the verified branch to your authorized remote. Use a PR tool's structured description field or a UTF-8 body file so multiline Markdown survives intact. Only include `Closes #123` when that is a real issue you intend to close. A local passing test does not establish that remote CI passed; link the actual run when available.

For each review comment: restate the concern, investigate, then either change the patch or explain the trade-off with evidence. Re-run checks affected by your response. Do not mark a peer's concern resolved while its requested behavior is still missing. The mentor can use the [review template](../templates/review.md).

## 7. Recover without panic

| Situation | First action | Next step |
| --- | --- | --- |
| Wrong file staged | `git diff --cached` | Unstage that path; preserve the edit |
| Need unrelated work temporarily | Inspect all changes | Use an explicitly named stash including new files if appropriate, or a separate checkout; inspect before applying it later |
| Merge conflict | `git status` | Read both sides and intended behavior; resolve, stage, and test |
| Need to abandon an in-progress merge | Preserve any new work first | `git merge --abort` if you intend to return to the pre-merge state |
| Shared commit has a defect | Find its dependent changes | Prefer a corrective commit or a deliberate revert over rewriting shared history |
| Suspect a lost commit | `git reflog` | Identify it before taking recovery action |

Practice conflicts and recovery in a disposable training repository created inside your personal `astra/work` directory, not in a dirty application checkout. The module explains how to construct the exercise.
