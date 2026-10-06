# Module 14: event pipelines and analytical correctness

**Outcome:** Test ingestion, deduplication, replay, queries, and export boundaries. **Prerequisite:** AST-060. Allow 20-28 hours.

## Lesson

An event pipeline separates acceptance from processing. Consumers can stop after a write but before acknowledging a message, causing redelivery. Stable event identity, checkpoint policy, and deduplication decide the eventual effect. Analytics adds another challenge: time windows, identity, and counting semantics can produce plausible but incorrect results.

## Guided lab

Inspect Pulse's in-memory stream and consumer tests before starting infrastructure. Build a five-event fixture with a duplicate and a boundary timestamp. Predict accepted events, processed unique events, and the final metric. Then locate analogous ingestion/query behavior in Pulse Net. Use deterministic adapters where provided; only launch Redis/Postgres or other services when the selected project's documented integration path requires them.

<a id="ast-085"></a>

### AST-085 — Map an event's lifecycle

**Mode:** Study · **Estimate:** 2 hours · **Depends on:** AST-060

**Story:** As an analytics developer, I want to understand acceptance versus processing so that I can explain where an event may be delayed or redelivered.

**Start here:** [Pulse README](https://github.com/elirc/pulse/blob/main/README.md), [stream types](https://github.com/elirc/pulse/blob/main/packages/stream/src/types.ts), [memory stream](https://github.com/elirc/pulse/blob/main/packages/stream/src/memory.ts), [consumer source](https://github.com/elirc/pulse/tree/main/apps/consumer/src).

**Acceptance:**
- Draw the actual producer/stream/consumer/storage path and identify acknowledgements/checkpoints.
- Name event identity and scope fields from the types.
- Mark two crash points and predict the work visible after restart under the current design.

**Verify:** Link each claimed transition to source or an existing test.

**Hint / review:** A successful capture response may establish durable acceptance without promising that every report already includes the event.

<a id="ast-086"></a>

### AST-086 — Prove deduplication scope

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-085

**Story:** As an analytics customer, I want repeated event delivery counted once within its intended scope so that retries do not inflate reports.

**Start here:** [consumer dedup tests](https://github.com/elirc/pulse/blob/main/apps/consumer/src/dedup.test.ts), [stream tests](https://github.com/elirc/pulse/blob/main/packages/stream/src/memory.test.ts).

**Acceptance:**
- Extract the deduplication key/scope and retention assumptions from the implementation.
- Add a missing duplicate-within-batch or across-batches case and a separate scope case.
- Assert aggregate effect and acknowledgement progress as appropriate to the selected pipeline layer.

**Verify:** Deliver a deterministic sequence containing repeat ids and compare it with the unique canonical sequence.

**Hint / review:** Two customers may legitimately use the same external event id; establish whether scope is part of identity.

<a id="ast-087"></a>

### AST-087 — Exercise a poison event and replay

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-086

**Story:** As an operator, I want malformed events isolated so that one bad payload does not indefinitely stop valid events behind it.

**Start here:** [dead-letter implementation](https://github.com/elirc/pulse/blob/main/apps/consumer/src/dlq.ts), [dead-letter tests](https://github.com/elirc/pulse/blob/main/apps/consumer/src/dlq.test.ts), [backfill tests](https://github.com/elirc/pulse/blob/main/apps/consumer/src/backfill.test.ts).

**Acceptance:**
- Define the current invalid-event, retry, and dead-letter behavior from source.
- Add a missing bad-event-followed-by-good-event case, checking progress and diagnostic information.
- Explain how replay interacts with deduplication and original event identity.

**Verify:** Use deterministic failure injection; assert valid work proceeds and failed work remains inspectable under the current policy.

**Hint / review:** Dropping a failing event and acknowledging it is progress, but without a recovery record it may also be silent data loss.

<a id="ast-088"></a>

### AST-088 — Verify analytics time-window boundaries

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-087

**Story:** As a report reader, I want time filters to count the intended events so that adjacent periods do not accidentally double-count boundaries.

**Start here:** [Pulse Net query service](https://github.com/elirc/pulse-net/blob/main/src/Pulse.Infrastructure/Services/QueryService.cs), [ingestion pipeline](https://github.com/elirc/pulse-net/blob/main/src/Pulse.Infrastructure/Services/IngestionPipeline.cs), [Pulse Net tests](https://github.com/elirc/pulse-net/tree/main/tests/Pulse.Tests).

**Acceptance:**
- Document the selected query's interval inclusivity and timestamp interpretation.
- Use fixed events before, at, inside, and after the interval to establish exact expected counts.
- Include customer/project scoping and distinguish event count from unique-identity count.

**Verify:** An integration test checks the public query result against a hand-calculated fixture.

**Hint / review:** Do not impose half-open intervals silently if the existing API specifies a different contract; propose a versioned change when needed.

<a id="ast-089"></a>

### AST-089 — Bound an export job's behavior

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-088

**Story:** As a customer exporting analytics, I want clear job completion and scoped results so that a background export is trustworthy.

**Start here:** [ExportService](https://github.com/elirc/pulse-net/blob/main/src/Pulse.Infrastructure/Services/ExportService.cs), [ExportJobProcessor](https://github.com/elirc/pulse-net/blob/main/src/Pulse.Infrastructure/Services/ExportJobProcessor.cs), [tests](https://github.com/elirc/pulse-net/tree/main/tests/Pulse.Tests).

**Acceptance:**
- Trace actual job states, ownership checks, output location, and implemented size/cancellation limits.
- Add a missing failure/retry or foreign-owner access case with deterministic fixture data.
- Record any missing limit as a scoped follow-up rather than implying the current implementation supports it.

**Verify:** Check state transitions and artifact contents/visibility, not just a queued response.

**Hint / review:** A 202 response can acknowledge a job that later fails; the completion contract matters separately.

<a id="ast-090"></a>

### AST-090 — Measure a pipeline under a controlled workload

**Mode:** Practice · **Estimate:** 2.5 hours · **Depends on:** AST-089

**Story:** As an operator, I want reproducible throughput and lag observations so that I can compare changes without misleading benchmark claims.

**Start here:** [Pulse load guide](https://github.com/elirc/pulse/blob/main/load/README.md), [load generator](https://github.com/elirc/pulse/tree/main/packages/loadgen), your lifecycle map.

**Acceptance:**
- Choose a bounded local workload and record event size/rate, duration, environment, accepted count, processed count, and failures.
- Observe lag/recovery after pausing a controlled consumer or using an existing test drill.
- Explain which results are synthetic and which infrastructure paths were actually exercised.

**Verify:** Repeat the same workload once for comparison and write a short report with limits.

**Hint / review:** Higher accepted throughput is not success if unprocessed backlog grows without bound.

## Exit check

Reconcile input events, unique effects, and report counts by hand. Choose another elective or a [capstone](../capstones/README.md).
