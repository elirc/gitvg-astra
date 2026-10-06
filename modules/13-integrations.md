# Module 13: reliable work across process boundaries

**Outcome:** Reason about retries, schedules, webhook verification, and delivery evidence. **Prerequisite:** AST-060. Allow 20-28 hours. Use the existing local fakes and test endpoints; no external messages or real connectors are required.

## Lesson

A timeout does not tell you whether a remote side effect happened. A retry policy needs classification, limits, delay, and a stable operation identity. A scheduler needs an explicit clock. A webhook needs verified bytes and a replay policy. An outbox records pending work durably, but its consumer must still handle redelivery.

## Guided lab

Read Relay App's execution tests and its fake clock/delayer/dispatcher. Draw an action that fails twice and then succeeds. Annotate attempts, delays, final status, and side effects. Use the fakes to move time and choose outcomes; never add sleeps simply to wait for a retry in a deterministic unit test.

<a id="ast-079"></a>

### AST-079 — Trace one fake connector run

**Mode:** Study · **Estimate:** 2 hours · **Depends on:** AST-060

**Story:** As a workflow operator, I want to understand a run's lifecycle so that I can distinguish configuration errors from failed actions.

**Start here:** [Relay App architecture](https://github.com/elirc/relay-app/blob/main/docs/architecture.md), [FlowExecutorTests](https://github.com/elirc/relay-app/blob/main/server/Relay.Tests/FlowExecutorTests.cs), [fake dispatcher](https://github.com/elirc/relay-app/blob/main/server/Relay.Tests/Support/FakeActionDispatcher.cs).

**Acceptance:**
- Trace a trigger through run creation, step execution, logs, and final status using real class names.
- Identify the adapter that prevents real connector calls in the exercise.
- Explain which failure stops or retries the run under current policy.

**Verify:** Run a focused existing executor test and connect its assertions to the timeline.

**Hint / review:** A fake is a controlled implementation of a boundary, not evidence a real vendor behaves identically.

<a id="ast-080"></a>

### AST-080 — Verify retry exhaustion and recovery

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-079

**Story:** As an operator, I want bounded retries and a clear final outcome so that failed runs do not continue indefinitely.

**Start here:** [RetriesExecutorTests](https://github.com/elirc/relay-app/blob/main/server/Relay.Tests/RetriesExecutorTests.cs), [FakeDelayer](https://github.com/elirc/relay-app/blob/main/server/Relay.Tests/Support/FakeDelayer.cs), [step execution contract](https://github.com/elirc/relay-app/blob/main/server/Relay.Domain/Execution/StepExecution.cs).

**Acceptance:**
- Extract the actual attempt-count and delay semantics before extending tests.
- Add a missing exhausted or eventual-success case with exact attempt and logged-outcome assertions.
- Confirm permanent/nonretryable failures follow their documented distinct policy.

**Verify:** The fake delayer records delays without wall-clock sleeping; final persisted/logged state matches the attempts.

**Hint / review:** Define whether "three retries" means three total attempts or one original attempt plus three retries.

<a id="ast-081"></a>

### AST-081 — Exercise webhook verification boundaries

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-080

**Story:** As an integration owner, I want forged or replayed webhook requests rejected so that only accepted deliveries trigger work.

**Start here:** [WebhookSignature](https://github.com/elirc/relay-app/blob/main/server/Relay.Domain/Security/WebhookSignature.cs), [security boundary tests](https://github.com/elirc/relay-app/blob/main/server/Relay.Tests/WebhookSecurityBoundaryTests.cs), [hardening tests](https://github.com/elirc/relay-app/blob/main/server/Relay.Tests/WebhookHardeningApiTests.cs).

**Acceptance:**
- Document the current signed bytes, timestamp/replay policy, and required headers from source.
- Select an uncovered tampered-body, timestamp-boundary, or duplicate-delivery case.
- Rejected input creates no unintended run; accepted duplicate behavior matches the current idempotency policy.

**Verify:** Sign with local fixture secrets and assert both response and run effects.

**Hint / review:** Re-serializing parsed JSON can change the bytes used for signature verification.

<a id="ast-082"></a>

### AST-082 — Test a scheduler boundary without waiting

**Mode:** Characterize · **Estimate:** 2.5 hours · **Depends on:** AST-081

**Story:** As an operator, I want scheduled flows to fire according to the declared time rules so that boundary times do not create missed or duplicate work.

**Start here:** [CronExpression](https://github.com/elirc/relay-app/blob/main/server/Relay.Domain/Scheduling/CronExpression.cs), [ScheduleDispatcherTests](https://github.com/elirc/relay-app/blob/main/server/Relay.Tests/ScheduleDispatcherTests.cs), [FakeClock](https://github.com/elirc/relay-app/blob/main/server/Relay.Tests/Support/FakeClock.cs).

**Acceptance:**
- State supported scheduling syntax, timezone assumptions, and due-time comparison from the implementation.
- Add a missing just-before/exactly-at/just-after boundary case or repeated dispatcher pass.
- Assert run count and next due time, not only a parser result.

**Verify:** Advance the fake clock; no test waits for real minutes to pass.

**Hint / review:** If a scheduler uses UTC only, document that limit instead of pretending it implements daylight-saving local-time rules.

<a id="ast-083"></a>

### AST-083 — Trace durable webhook redelivery

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-082

**Story:** As an issue-tracker integrator, I want failed outbound deliveries retried from durable state so that a temporary receiver outage does not lose an event.

**Start here:** [Tracer Net outbox](https://github.com/elirc/tracer-net/blob/main/src/Tracer.Api/Webhooks/WebhookOutbox.cs), [delivery tests](https://github.com/elirc/tracer-net/blob/main/tests/Tracer.Tests/Integration/WebhookDeliveryApiTests.cs), [stub endpoint](https://github.com/elirc/tracer-net/blob/main/tests/Tracer.Tests/Integration/StubWebhookEndpoint.cs).

**Acceptance:**
- Explain event persistence, attempt tracking, and success/retry transitions in the current outbox.
- Add a missing transient-failure-then-success or retry-limit case using the stub receiver.
- State what a consumer must deduplicate if a delivery succeeds but its acknowledgement is lost.

**Verify:** Assert durable delivery state and observed receiver calls across the chosen retry scenario.

**Hint / review:** A successful HTTP response recorded late can still result in duplicate delivery after a crash.

<a id="ast-084"></a>

### AST-084 — Write a duplicate-delivery support playbook

**Mode:** Practice · **Estimate:** 2 hours · **Depends on:** AST-083

**Story:** As support staff, I want a safe investigation procedure so that I can explain a repeated run without exposing connection secrets or repeating its side effect.

**Start here:** [Relay idempotency](https://github.com/elirc/relay/blob/main/apps/engine/src/idempotency.ts), [Relay redaction](https://github.com/elirc/relay/blob/main/packages/shared/src/redact.ts), your retry/outbox evidence.

**Acceptance:**
- Record identifiers needed to distinguish a trigger, run, step attempt, and external delivery.
- Explain what can be retried safely under the actual implementation and what needs an operator decision.
- Include redacted example logs and a local drill using fakes.

**Verify:** A mentor diagnoses your prepared duplicate scenario from the playbook without executing real external actions.

**Hint / review:** An operation key is useful only when its scope and retention cover the retry scenario.

## Exit check

Explain at-least-once delivery and idempotent effect with a concrete failure timeline. Choose another elective or a [capstone](../capstones/README.md).
