# Module 02: read and change code with confidence

**Outcome:** Explain types, transformations, errors, and asynchronous control flow in this application. Read [Foundations](../handbook/foundations.md). Allow 10-15 hours with scratch exercises and review.

## Lesson

TypeScript and C# express many of the same ideas with different syntax. Match concepts before memorizing punctuation: arrays/collections, nullable values, records/objects, promises/tasks, and discriminated results. Trace a single value across the API and notice which checks happen at compile time and which happen at runtime.

## Guided lab

Trace `title` and `expectedVersion` through the rename path. Annotate each type, identify where JSON loses compile-time guarantees, and predict the result of sending null, an empty string, and a stale version. Use scratch exercises for syntax practice; avoid broad application refactors just to demonstrate a language construct.

<a id="ast-013"></a>

### AST-013 — Map one value across both languages

**Mode:** Study · **Estimate:** 1 hour · **Depends on:** AST-012

**Story:** As a maintainer, I want the rename contract mapped across layers so that a field change does not leave one consumer behind.

**Start here:** [client types](https://github.com/elirc/folio-app/blob/main/client/src/api/types.ts), [PageDtos](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Contracts/PageDtos.cs).

**Acceptance:**
- Map title, icon, id, and version from UI value to request DTO, entity, and response.
- Explain nullability and optionality at each boundary.
- Identify one place a TypeScript cast trusts runtime JSON.

**Verify:** Present the mapping with actual type/member names and a request capture.

**Hint / review:** A C# Guid is serialized as text; a TypeScript string alone does not validate Guid syntax.

<a id="ast-014"></a>

### AST-014 — Transform a tree without mutating it

**Mode:** Practice · **Estimate:** 1.5 hours · **Depends on:** AST-013

**Story:** As a developer displaying favorites, I want to understand tree traversal so that nested pages are handled correctly.

**Start here:** [FavoritesList](https://github.com/elirc/folio-app/blob/main/client/src/components/FavoritesList.tsx), [PageTreeItem](https://github.com/elirc/folio-app/blob/main/client/src/components/PageTreeItem.tsx).

**Acceptance:**
- In scratch code, collect favorite ids from a root/child/grandchild fixture.
- Handle an empty tree and duplicate titles without losing distinct ids.
- Explain why the result must not mutate the input or store a second copy of derived state.

**Verify:** Compare expected ids and unchanged input before/after the function.

**Hint / review:** Explain recursion's base case. What would happen if the input graph contained a cycle?

<a id="ast-015"></a>

### AST-015 — Read a C# service as a decision sequence

**Mode:** Study · **Estimate:** 1.5 hours · **Depends on:** AST-014

**Story:** As a reviewer, I want to understand the page-update rule order so that I can see whether invalid or forbidden input mutates state.

**Start here:** [PageService](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/PageService.cs), [ServiceResult](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Services/ServiceResult.cs).

**Acceptance:**
- Annotate `UpdateAsync` as read, caller check, validation/version check, mutation, and save.
- Explain `Task`, `await`, nullable pattern matching, and cancellation in this method.
- Identify which returns occur before persistence.

**Verify:** Walk a success, denied access, and stale version through the actual branches.

**Hint / review:** Do not assume a method name proves its implementation; read its body and invoked policy.

<a id="ast-016"></a>

### AST-016 — Explain HTTP error translation

**Mode:** Characterize · **Estimate:** 1.5 hours · **Depends on:** AST-015

**Story:** As a client developer, I want consistent error translation so that I can present the correct recovery action.

**Start here:** [PagesController](https://github.com/elirc/folio-app/blob/main/server/Folio.Api/Controllers/PagesController.cs), [client.ts](https://github.com/elirc/folio-app/blob/main/client/src/api/client.ts), [HardeningTests](https://github.com/elirc/folio-app/blob/main/server/Folio.Tests/HardeningTests.cs).

**Acceptance:**
- Build a table mapping service status to HTTP status to client error shape.
- Include a non-JSON failure and a no-content success when examining the fetch wrapper.
- State which cases already have tests and which are candidates for Module 04.

**Verify:** Cite test names or controlled responses; do not add duplicate tests for the table alone.

**Hint / review:** A response's title and detail have different purposes. Which does the current wrapper prefer?

<a id="ast-017"></a>

### AST-017 — Trace an asynchronous request lifecycle

**Mode:** Study · **Estimate:** 1.5 hours · **Depends on:** AST-016

**Story:** As a developer maintaining loaded views, I want to understand request cleanup so that old requests cannot update an obsolete view.

**Start here:** [useAsync](https://github.com/elirc/folio-app/blob/main/client/src/hooks/useAsync.ts), [SearchBox](https://github.com/elirc/folio-app/blob/main/client/src/components/SearchBox.tsx).

**Acceptance:**
- Draw start, resolution, rejection, dependency change, and unmount timelines.
- Explain the different jobs of AbortController, the active guard, and debounce timers.
- Predict reverse-order completion and a real network error separately.

**Verify:** Use a scratch controlled-promise example or debugger observations with explicitly recorded timing.

**Hint / review:** Cancellation is not evidence that no callback can ever run; identify the state-write guard.

<a id="ast-018"></a>

### AST-018 — Explain a small code change without tools

**Mode:** Practice · **Estimate:** 1 hour · **Depends on:** AST-017

**Story:** As a mentor, I want the learner to explain a change independently so that I can assess understanding rather than copied output.

**Start here:** Your AST-007 patch and [foundations](../handbook/foundations.md).

**Acceptance:**
- Explain every changed line and one unchanged caller it relies on.
- Predict behavior for empty input, nested favorites, and a route with a different workspace id.
- Propose one alternate implementation and explain its trade-off.

**Verify:** Five-minute teach-back followed by a mentor-selected input variation.

**Hint / review:** If you cannot explain an abstraction, simplify or study it before building on it.

## Exit check

Follow a value and a failure from UI to database without guessing. Continue to [Module 03](03-react-and-accessibility.md).
