# Module 10: transfer skills into TypeScript systems

**Outcome:** Navigate pnpm workspaces, strengthen a pure utility, and explain replicated state. **Prerequisite:** AST-060. Allow 18-26 hours. Work inside one project's repository at a time.

## Lesson

A workspace groups packages with explicit names and dependency boundaries. A shared package is useful when it owns a stable concept, not merely because several folders import it. TypeScript monorepos in this workspace often use Turbo to orchestrate package scripts. Inspect the package's own test script before choosing a filter; a green command with no matching package or no tests is weak evidence.

Replicated state adds a new dimension: delivery can duplicate, omit, or reorder operations. Idempotent application, stable identifiers, and explicit ordering turn network behavior into a testable input. The Folio `crdt-101` package is a plain-text learning model, not a replacement for a rich-text collaboration engine.

## Guided lab

Read Tracer's workspace and package manifests. Install in the Tracer project root, then run its shared package's existing test command using the package name you verified. Trace a store update and read the nearest test. For the Relay and Folio stories, repeat that project-local setup; do not assume dependencies installed in Tracer also install its siblings.

<a id="ast-061"></a>

### AST-061 — Navigate a TypeScript workspace

**Mode:** Study · **Estimate:** 2 hours · **Depends on:** AST-060

**Story:** As a contributor switching stacks, I want a package map so that I change and test the correct unit of the system.

**Start here:** [Tracer manifest](../../tracer/package.json), [workspace config](../../tracer/pnpm-workspace.yaml), [shared manifest](../../tracer/packages/shared/package.json).

**Acceptance:**
- Identify app/package names, dependencies, test scripts, and Turbo's role.
- Run a bounded shared-package check and record the package actually selected.
- Compare this boundary with Folio App's client/server split.

**Verify:** Show command output identifying real tests, not only a successful process exit.

**Hint / review:** `--filter` uses package identity/patterns; inspect the name field before copying a command.

<a id="ast-062"></a>

### AST-062 — Characterize local issue filtering

**Mode:** Characterize · **Estimate:** 2 hours · **Depends on:** AST-061

**Story:** As an issue-tracker user, I want filters to combine predictably so that I see the issues I intended to select.

**Start here:** [filter](../../tracer/packages/shared/src/filter.ts), [filter tests](../../tracer/packages/shared/src/filter.test.ts), [store](../../tracer/packages/shared/src/store.ts).

**Acceptance:**
- Extract the actual filter contract and explain combinations of at least two supported criteria.
- Add a missing edge case involving empty criteria, multiple matches, or a missing optional issue field.
- Verify filtering does not mutate source issue data.

**Verify:** A table-driven case fails for a plausible wrong combination of the selected criteria.

**Hint / review:** Read whether each criterion uses AND or OR; do not impose your preferred semantics silently.

<a id="ast-063"></a>

### AST-063 — Harden redaction for overlapping known secrets

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-062

**Story:** As a workflow operator, I want known secrets removed from nested run payloads so that useful debugging output does not reveal credentials.

**Start here:** [Relay redaction](../../relay/packages/shared/src/redact.ts), [redaction tests](../../relay/packages/shared/src/redact.test.ts).

**Acceptance:**
- Define deterministic handling when one known secret is a substring of another; no suffix of the longer secret leaks because the shorter one was replaced first.
- Preserve the existing minimum-length policy and ordinary nonsecret values in nested arrays/objects.
- Do not mutate input or broaden this task into arbitrary object serialization.

**Verify:** Cover overlapping secrets in both input orders, repeats, nested values, and a unchanged source object.

**Hint / review:** Sequential replacement order matters. This utility only removes known values under its policy; do not call it complete secret detection.

<a id="ast-064"></a>

### AST-064 — Trace duplicated and reordered server deltas

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-063

**Story:** As an offline issue-tracker user, I want duplicate delivery to converge so that reconnecting does not duplicate my work.

**Start here:** [Tracer store](../../tracer/packages/shared/src/store.ts), [store tests](../../tracer/packages/shared/src/store.test.ts), [sync types](../../tracer/packages/shared/src/sync.ts).

**Acceptance:**
- Explain operation identity, sequence handling, and the actual duplicate policy from the source.
- Select a missing duplicate/reorder example and compare final state to the documented canonical application order.
- Include an explicit assertion about pending local work when relevant to the selected contract.

**Verify:** Deterministically replay the same operation set with the chosen delivery variation.

**Hint / review:** If the store buffers gaps, a partial sequence may intentionally remain incomplete until the missing delta arrives.

<a id="ast-065"></a>

### AST-065 — Explore a small CRDT's convergence

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-064

**Story:** As a collaborative writer, I want concurrent text operations to converge so that replicas eventually show the same document.

**Start here:** [Folio RGA](../../folio/packages/crdt-101/src/rga.ts), [convergence tests](../../folio/packages/crdt-101/src/convergence.test.ts), [resurrection tests](../../folio/packages/crdt-101/src/resurrection.test.ts).

**Acceptance:**
- Explain immutable operation ids, tombstones, and pending causal dependencies using two replicas.
- Add a missing small sequence involving concurrent insertion plus deletion or delayed origin delivery.
- Assert equal final visible text and no resurrection after all operations are delivered.

**Verify:** Replay all permutations of a deliberately small operation set or use the package's existing seeded test pattern.

**Hint / review:** Convergence of final text does not by itself prove every user-intent property of a rich-text editor.

<a id="ast-066"></a>

### AST-066 — Compare three consistency approaches

**Mode:** Practice · **Estimate:** 2 hours · **Depends on:** AST-065

**Story:** As a design reviewer, I want a grounded comparison so that I choose consistency mechanisms according to the product's needs.

**Start here:** Your Folio App version work, [Tracer store](../../tracer/packages/shared/src/store.ts), [Folio RGA](../../folio/packages/crdt-101/src/rga.ts).

**Acceptance:**
- Compare rejection on stale version, sequenced mutation replay, and CRDT operation merging using one user scenario each.
- State identity/order requirements, failure recovery, storage cost, and what each test actually proved.
- Recommend an approach for a simple summary edit and a collaborative text buffer with reasons.

**Verify:** A mentor introduces a duplicate or delayed message and you predict each system's behavior.

**Hint / review:** More sophisticated merging brings more protocol and data-model commitments; keep the recommendation tied to the requirement.

## Exit check

Explain a deterministic replay without invoking "exactly once" as a magical network guarantee. Choose another elective or a [capstone](../capstones/README.md).
