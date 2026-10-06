# Module 15: support systems and evidence-based AI features

**Outcome:** Evaluate retrieval and support automation with deterministic fixtures, scope checks, and explicit handoff. **Prerequisite:** AST-060. Allow 20-28 hours. Use checked-in fakes and synthetic content; real model credentials are not required for these assignments.

## Lesson

A support assistant can produce a fluent answer from irrelevant evidence. Retrieval quality, permission filtering, abstention, and action policy need separate evaluation. A single aggregate score can hide a critical regression on a small class of cases. Test both the evaluator and the behavior it measures.

Harbor's TypeScript packages contain retrieval and evaluation code. Harbor Net provides a separate support backend with SLA and assignment behavior; it is not assumed to implement the same AI stack. The comparison is about trustworthy automation and operations.

## Guided lab

Read `retrieveRelevant`, its threshold tests, and the evaluation dataset schema. Construct a tiny corpus where you know the relevant document ids. Predict retrieval, top score, and sufficiency before running it. Then add one query with no supporting document and explain the required downstream behavior.

<a id="ast-091"></a>

### AST-091 — Map retrieval and evaluation separately

**Mode:** Study · **Estimate:** 2 hours · **Depends on:** AST-060

**Story:** As a support engineer, I want to distinguish retrieval from answer evaluation so that I can locate the cause of an unsupported answer.

**Start here:** [retrieval](https://github.com/elirc/harbor/blob/main/packages/rag/src/retrieve.ts), [eval types](https://github.com/elirc/harbor/blob/main/packages/eval/src/types.ts), [graders](https://github.com/elirc/harbor/blob/main/packages/eval/src/graders.ts).

**Acceptance:**
- Explain vector ranking, rank fusion, relevance threshold, and the actual metric definitions.
- Trace one dataset case through the evaluation runner and identify where the expected outcome is checked.
- Distinguish retrieval correctness, answer support, and action policy in a diagram.

**Verify:** Compute recall/reciprocal rank manually for one tiny ranked list and compare to the functions.

**Hint / review:** A high top similarity score is not itself proof that an answer is entailed by a source.

<a id="ast-092"></a>

### AST-092 — Add no-evidence and near-threshold cases

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-091

**Story:** As a support customer, I want unsupported questions recognized so that the assistant does not invent an answer from weak context.

**Start here:** [threshold tests](https://github.com/elirc/harbor/blob/main/packages/rag/src/threshold.test.ts), [retrieval tests](https://github.com/elirc/harbor/blob/main/packages/rag/src/retrieve.test.ts), [dataset](https://github.com/elirc/harbor/blob/main/packages/eval/src/dataset.ts).

**Acceptance:**
- Add synthetic empty-corpus, below-threshold, and boundary-score cases not already covered.
- Establish the `sufficient` result and which chunks are returned.
- Record the downstream expected abstention/handoff separately from the retrieval function's own guarantee.

**Verify:** Use deterministic vectors and known relevance ids; do not call a live embedding/model service.

**Hint / review:** Changing a threshold to make one case pass needs a broader dataset comparison, not a guessed constant.

<a id="ast-093"></a>

### AST-093 — Verify the evaluator catches a bad answer

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-092

**Story:** As a developer changing support automation, I want the evaluation itself tested so that a green score cannot result from a grader that accepts everything.

**Start here:** [grader meta-tests](https://github.com/elirc/harbor/blob/main/packages/eval/src/graders.meta.test.ts), [grader tests](https://github.com/elirc/harbor/blob/main/packages/eval/src/graders.test.ts), [runner tests](https://github.com/elirc/harbor/blob/main/packages/eval/src/runner.test.ts).

**Acceptance:**
- Add a missing clearly-correct/clearly-incorrect pair for one existing grader's documented contract.
- Explain how the bad fixture fails and ensure the result is recorded by the runner.
- State what the grader cannot judge reliably rather than overstating semantic understanding.

**Verify:** Deliberately invalid output receives the expected failure; restoring valid output passes under the same setup.

**Hint / review:** A test of the production answer is different from a test of whether the grader can detect an error.

<a id="ast-094"></a>

### AST-094 — Test instruction-like retrieved content

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-093

**Story:** As a support operator, I want retrieved text treated as evidence so that a document's embedded instruction cannot authorize an unrelated action.

**Start here:** [injection tests](https://github.com/elirc/harbor/blob/main/packages/eval/src/injection.test.ts), [autonomy tests](https://github.com/elirc/harbor/blob/main/packages/eval/src/autonomy.test.ts), [bot tests](https://github.com/elirc/harbor/blob/main/packages/eval/src/bot.test.ts).

**Acceptance:**
- Add a synthetic retrieved snippet asking for an action outside the configured support policy.
- Verify the configured policy boundary blocks the action or hands off as implemented, without real external calls.
- Retain useful supported content handling and record the test's specific scope.

**Verify:** Assert action/trace results through existing fakes, not only that the answer contains a polite refusal phrase.

**Hint / review:** Passing one adversarial fixture establishes a regression guard for that scenario, not universal resistance to malicious input.

<a id="ast-095"></a>

### AST-095 — Test a support SLA boundary

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-094

**Story:** As a support lead, I want SLA status to follow explicit time and assignment rules so that urgent conversations are not misclassified.

**Start here:** [Harbor Net SLA policies](https://github.com/elirc/harbor-net/blob/main/src/Harbor.Infrastructure/SlaPolicies.cs), [SLA breaches](https://github.com/elirc/harbor-net/blob/main/src/Harbor.Infrastructure/SlaBreaches.cs), [assignment](https://github.com/elirc/harbor-net/blob/main/src/Harbor.Infrastructure/AutoAssigner.cs), [tests](https://github.com/elirc/harbor-net/tree/main/tests/Harbor.Tests).

**Acceptance:**
- Choose one implemented SLA clock/breach rule and document its actual timezone/pause assumptions.
- Add a missing boundary or assignment-state case using deterministic time where the harness permits.
- Check workspace scope and avoid inventing business-hours behavior not present in the code.

**Verify:** Hand-calculate the expected due/breach outcome and compare with the public/service result.

**Hint / review:** This backend is a distinct implementation; use its existing abstractions rather than assuming TypeScript Harbor's policy structure.

<a id="ast-096"></a>

### AST-096 — Write an evaluation-backed rollout proposal

**Mode:** Practice · **Estimate:** 2.5 hours · **Depends on:** AST-095

**Story:** As a support product owner, I want evidence and limits for an automation change so that I can decide whether it is ready for a controlled trial.

**Start here:** [eval regression code](https://github.com/elirc/harbor/blob/main/packages/eval/src/regression.ts), your new cases, [ADR template](../templates/adr.md).

**Acceptance:**
- Compare baseline and changed behavior on the same deterministic dataset, reporting per-case regressions as well as aggregate results.
- Specify permitted actions, handoff behavior, trial scope, observation criteria, and a concrete disable/fallback path.
- Distinguish simulated evidence from real user/model performance; do not publish or enable a live trial as part of the exercise.

**Verify:** A mentor can make a decision from the report and challenge one withheld counterexample.

**Hint / review:** A regression on unauthorized action handling can outweigh an improvement in average answer score.

## Exit check

Explain an unsupported answer, a retrieval miss, a failed grader, and an unauthorized action as different failures. Proceed to a [capstone](../capstones/README.md) or another elective.
