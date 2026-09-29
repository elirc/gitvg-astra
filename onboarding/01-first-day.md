# Your first day

Your first job is to make your environment and your understanding observable. You are ready to contribute when you can run the product, locate a behavior, describe a small change, and show another person what you checked.

## The first 90 minutes

| Time | Activity | Evidence |
| --- | --- | --- |
| 0-15 minutes | Read the Astra README and identify `folio-app` | A one-paragraph description of the app's users |
| 15-30 minutes | Read the repository boundary section in the Git guide | The resolved project root and current branch |
| 30-60 minutes | Follow local setup; record blockers precisely | Tool versions and the health response, or a reproducible setup failure |
| 60-90 minutes | Log in, create a page, rename it, then reload | A short walkthrough and one observed HTTP request |

Do not spend the day installing every stack in this workspace. The initial track needs Git, the .NET SDK, Node, and pnpm. Docker is needed only for electives whose own instructions require it.

## Make a learning notebook

Create `astra/work/<your-name>/` and copy the [baseline](../templates/baseline.md), [journal](../templates/learning-journal.md), and [weekly plan](../templates/weekly-plan.md) there. The directory and personal files are learner-created; examples in templates are not completed evidence. Use `AST-001` style identifiers in entries so a mentor can find the relevant assignment.

Record commands with their working directory, date, exit result, and a short explanation. A screenshot is useful for a rendered interface, but a test command and assertion are better evidence for server behavior. Remove bearer tokens, real personal data, and connection secrets from shared notes. Seed account names from the course are fine.

## A 20-minute diagnostic

Try these without an assistant writing the answers. Mark each as comfortable, needs practice, or new.

1. Write a function that counts completed items in an array without changing the array.
2. Explain why a missing value differs from an empty string.
3. Explain a function call, a returned value, and a thrown exception.
4. Describe what a browser sends when you submit a form.
5. Explain what a primary key identifies.
6. Read a small diff and separate added lines from removed lines.
7. Describe a test that would distinguish a correct implementation from a plausible wrong one.
8. Explain what you would do after a command fails.

This is a placement exercise, not an entrance exam. For items 1-3, work through [Foundations](../handbook/foundations.md). For 4-5, use the code tour and data guide. For 6-8, use the contribution and debugging guides. Ask a mentor to explain one unfamiliar item, then explain it back with a different example.

## A normal learning session

Spend 10 minutes recalling yesterday's concept without notes, 15 minutes reading a small source slice, 45-75 minutes implementing or investigating, and 15 minutes checking and recording the result. End by writing the next smallest action. Keep one story in progress; park unrelated discoveries in a backlog.

When stuck, spend about 20 minutes forming and testing hypotheses before asking for help. Do not let that timer prevent you from asking immediately about an ambiguous requirement or an action that could affect shared data. Use the [debug log](../templates/debug-log.md): expected behavior, actual behavior, minimal steps, first useful error, and what you already tried.

## Working with a mentor or an AI assistant

Ask for an explanation, a test case, or a review of your diff before asking for an entire implementation. Predict an answer before reading it. If an assistant generates code, trace it, run it, and explain the failure case it handles. Never report an unrun command as passing. A solo learner can write a self-review, wait until the next session, and review the patch again; label it a self-review rather than inventing a second person's approval.

## End-of-day checkpoint

You should be able to show the correct Git root, a running app or a precise setup blocker, a named source file for a visible behavior, and one question you could not yet answer. Continue with [local setup](02-local-setup.md) and [Module 00](../modules/00-onboarding.md).
