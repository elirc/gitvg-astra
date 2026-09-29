# Curriculum and pacing

The core sequence is cumulative. Each module has six stories; finish the preceding core story before starting the next unless a mentor accepts equivalent evidence. Each elective starts after AST-060 and is independent of the other electives. Within an elective, follow its six stories in order. No learner needs to operate all 17 projects simultaneously.

## Core path

| Module | Stories | Main skill | Demonstrable outcome |
| --- | --- | --- | --- |
| [00: Onboarding](modules/00-onboarding.md) | AST-001-006 | Tools, product, baseline | Run the app and explain a request |
| [01: Contribution](modules/01-contribution.md) | AST-007-012 | Git, scope, review, recovery | Deliver and review a small UI change |
| [02: Language and navigation](modules/02-language-and-navigation.md) | AST-013-018 | TypeScript, C#, asynchronous code | Trace values, types, and failures across layers |
| [03: React and accessibility](modules/03-react-and-accessibility.md) | AST-019-024 | State, forms, keyboard use | Make UI behavior usable and testable |
| [04: HTTP and contracts](modules/04-http-and-contracts.md) | AST-025-030 | Validation, errors, cancellation | Handle successful and failed API calls coherently |
| [05: Data and migrations](modules/05-data-and-migrations.md) | AST-031-036 | Relational modeling and persistence | Add an optional page summary through a migration |
| [06: Permissions](modules/06-permissions.md) | AST-037-042 | Identity, scope, policy | Prove who can read and write, including indirect reads |
| [07: Personal favorites](modules/07-personal-favorites.md) | AST-043-048 | Full-stack feature ownership | Replace shared favorites with caller-specific favorites |
| [08: Debugging and concurrency](modules/08-debugging-and-concurrency.md) | AST-049-054 | Reproduction, races, conflict UX | Preserve correctness under failures and competing edits |
| [09: Performance and delivery](modules/09-performance-and-delivery.md) | AST-055-060 | Measurement, repeatable checks, handoff | Demonstrate and hand off the core feature |

## Electives

| Module | Stories | Projects | Focus |
| --- | --- | --- | --- |
| [10: TypeScript systems](modules/10-typescript-systems.md) | AST-061-066 | tracer, relay, folio | Packages, pure functions, replicated state |
| [11: Commerce](modules/11-commerce.md) | AST-067-072 | storefront, bazaar, bazaar-app, agora, agora-net | Money, contracts, cached reads, checkout |
| [12: Domain design](modules/12-domain-design.md) | AST-073-078 | atlas, atlas-net | Invariants, effective dates, ports, architecture tests |
| [13: Integrations](modules/13-integrations.md) | AST-079-084 | relay-app, relay, tracer-net | Retries, schedules, signatures, outbox delivery |
| [14: Analytics and streams](modules/14-analytics-and-streams.md) | AST-085-090 | pulse, pulse-net | Deduplication, replay, query semantics, exports |
| [15: Support and AI evaluation](modules/15-support-and-evaluation.md) | AST-091-096 | harbor, harbor-net | Retrieval, evaluation, scope, human handoff |

## A suggested 16-week core schedule

Plan around 10-13 hours per week. Story estimates cover focused work; reserve roughly one quarter of the week for reading, review, and rework. Replan based on observed effort after the first two weeks.

| Week | Focus | Review checkpoint |
| --- | --- | --- |
| 1 | Module 00 | Reproduce setup without mentor keystrokes |
| 2 | Module 01 | Explain and review a complete small diff |
| 3-4 | Module 02 | Explain types, async flow, and a failure from memory |
| 5-6 | Module 03 | Demo keyboard use and meaningful component assertions |
| 7 | Module 04 | Show a contract table and one negative HTTP test |
| 8-9 | Module 05 | Upgrade an existing database without losing pages |
| 10 | Module 06 | Explain role, workspace, visibility, and public access |
| 11-12 | Module 07 | Demo personal favorites in two sessions |
| 13-14 | Module 08 | Reproduce a race deterministically and preserve unsaved input |
| 15-16 | Module 09 | Run the acceptance demo and give a teammate a usable handoff |

Add 2-3 weeks per elective and 2-4 weeks for a capstone at this cadence. A full-time learner can compress the calendar, but should retain separate review and recall sessions.

## How to execute a story

1. Read the lesson and linked source. Record the current behavior before changing it.
2. Restate the user benefit and identify the smallest observable improvement.
3. Write the acceptance examples in your own words. For an implementation story, name a plausible wrong implementation a check should catch.
4. Create the right project branch, implement a slice, and inspect the diff.
5. Run the indicated focused verification. Broaden to the affected project gates before integration.
6. Attach evidence in [TRACKER.md](TRACKER.md), complete a review, and answer the exit question aloud.

**Study** stories yield a trace, table, or explanation. **Characterize** stories establish current behavior with a new nonduplicate case or existing-test evidence. **Extend** stories implement a requested behavior. **Practice** stories use a disposable exercise or create delivery material. These labels prevent an existing feature from being mistaken for missing work.

If a requested extension already exists in a later checkout, prove that with source and behavior evidence, then agree a nearby edge case of the same difficulty. Do not remove working functionality to recreate a lesson. If a behavior described as existing has changed, record the discrepancy and adapt the exercise rather than changing the app to match old prose.

## Graduation requirements

Complete AST-060, one elective, and one [capstone](capstones/README.md). Present a working user journey, a failure path, a meaningful regression test, a reviewed diff, and an honest limitation. The mentor chooses one small requirement change during the demo to assess understanding beyond rehearsed steps. Use the [assessment rubric](handbook/mentoring-and-assessment.md); further practice is the right outcome when evidence is incomplete.
