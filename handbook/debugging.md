# Debug with hypotheses and evidence

Debugging is narrowing the difference between what should happen and what did happen. Start with a reproducible observation, not a preferred fix.

## Worked investigation: search appears to show an old result

Suppose the user types `install`, then `architecture`, and the dropdown later shows Installation. First record the exact keystrokes, workspace, and whether the behavior happens with a slow API. Do not label it a database defect before looking at requests.

1. In browser Network, record request start and finish order. Confirm the query strings actually differ.
2. Locate [SearchBox](https://github.com/elirc/folio-app/blob/main/client/src/components/SearchBox.tsx). Read its effect dependencies, debounce timer, abort controller, and catch branch.
3. Form a hypothesis: a response for an obsolete query updates the latest view, or a failed query leaves previous results visible. These are different mechanisms.
4. Reproduce each mechanism separately with controlled promises or a deterministic error response. A mock that ignores the signal is useful for testing the component's own guard; label this setup accurately.
5. Define the desired UI: canceled requests are quiet; a real failure gets an error state; obsolete results cannot masquerade as the latest query's results.
6. Add the focused regression, change the smallest responsible logic, and rerun the same scenario. Then verify normal success and empty results still work.

The current code's broad catch leaves prior results on aborted or failed requests. That is a source observation. Whether it produces the reported visible symptom in a specific browser is something your reproduction must establish.

## The debugging loop

Write expected versus actual behavior. Reduce the input or flow. Find the last boundary whose output is correct. Predict an observation that would distinguish your hypotheses. Run that experiment. Update your explanation, then fix the responsible behavior. Afterward, remove temporary instrumentation and document what evidence changed your mind.

| Boundary | Tool | Useful question |
| --- | --- | --- |
| Rendered interface | Browser DOM/accessibility inspection | Is the state absent, hidden, disabled, or mislabeled? |
| Browser request | Network tab | Did the method, URL, body, and status match the contract? |
| Client callback | Breakpoint/controlled test response | Which request owns this update? |
| API entry | Controller breakpoint | Did routing/validation/auth reject before the service? |
| Service | Locals and call stack | Which rule led to this result? |
| Persistence | Scoped DbContext/query logging | Was a change tracked and committed? |
| History | `git log`, `git show`, `git blame` | When and why did this behavior change? |

## Reading a failure

Read the first relevant exception and the application frame nearest your change. A stack trace is a call history, not a to-do list. For an HTTP error, inspect status, ProblemDetails, and request identifier. A 400 with field errors differs from a 500 with a trace identifier. Keep sensitive request headers and page content out of shared logs.

When debugging tests, check the fixture before changing production code. A fetch mock with the wrong method/path can make a valid request appear broken. A reused integration factory can make a later test depend on a prior write. When debugging startup, separate restore/build errors from migration errors and port binding errors.

## Better help requests

Use the [debug-log template](../templates/debug-log.md). Provide minimal reproduction, expected and actual outcomes, relevant diff, first useful failure, and hypotheses already checked. Ask a bounded question such as "Does this factory isolate writes between these two tests?" instead of "Why is everything broken?"

## Exercises

- Explain a 401, 403, 404, 409, and 429 in Folio using one concrete caller/action for each.
- Take a failing client mock route and predict whether the API debugger will be hit.
- Explain why a successful unit test of a title validator cannot establish that the controller invokes the validator.
- Reproduce a stale rename in two sessions and record the server result separately from the UI's treatment of the unsaved text.
