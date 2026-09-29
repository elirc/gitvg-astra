# User story backlog

This is the assignment index for all **96 stories**. Follow Modules 00-09 in order. Each elective begins after AST-060 and can be chosen independently of the other electives; follow its six stories in order. Open a story for its lesson context, source links, acceptance criteria, verification, and hint.

**Study** explains existing code. **Characterize** proves current behavior with nonduplicate evidence. **Extend** implements an explicit improvement. **Practice** develops contribution and delivery habits. Estimates cover focused work; the [curriculum](../CURRICULUM.md) includes additional reading/review time.

Use the [tracker](../TRACKER.md) for status and evidence. Capstones are [separate graduation assignments](../capstones/README.md), not part of these 96 story ids.

## [Module 00: become operational](../modules/00-onboarding.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-001](../modules/00-onboarding.md#ast-001) | Identify the correct repository | Study | 45 minutes | None |
| [AST-002](../modules/00-onboarding.md#ast-002) | Establish a repeatable tool baseline | Practice | 1 hour | AST-001 |
| [AST-003](../modules/00-onboarding.md#ast-003) | Complete a product walkthrough | Practice | 1 hour | AST-002 |
| [AST-004](../modules/00-onboarding.md#ast-004) | Describe a request accurately | Study | 1 hour | AST-003 |
| [AST-005](../modules/00-onboarding.md#ast-005) | Recover from a stopped API | Practice | 45 minutes | AST-004 |
| [AST-006](../modules/00-onboarding.md#ast-006) | Give a five-minute onboarding handoff | Practice | 1 hour | AST-005 |

## [Module 01: make and review a contribution](../modules/01-contribution.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-007](../modules/01-contribution.md#ast-007) | Explain an empty favorites section | Extend | 1 hour | AST-006 |
| [AST-008](../modules/01-contribution.md#ast-008) | Package the first patch for review | Practice | 1 hour | AST-007 |
| [AST-009](../modules/01-contribution.md#ast-009) | Respond to a real review concern | Practice | 1 hour | AST-008 |
| [AST-010](../modules/01-contribution.md#ast-010) | Resolve a training conflict | Practice | 1 hour | AST-009 |
| [AST-011](../modules/01-contribution.md#ast-011) | Recover an accidentally staged file | Practice | 30 minutes | AST-010 |
| [AST-012](../modules/01-contribution.md#ast-012) | Split an oversized requirement | Practice | 1 hour | AST-011 |

## [Module 02: read and change code with confidence](../modules/02-language-and-navigation.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-013](../modules/02-language-and-navigation.md#ast-013) | Map one value across both languages | Study | 1 hour | AST-012 |
| [AST-014](../modules/02-language-and-navigation.md#ast-014) | Transform a tree without mutating it | Practice | 1.5 hours | AST-013 |
| [AST-015](../modules/02-language-and-navigation.md#ast-015) | Read a C# service as a decision sequence | Study | 1.5 hours | AST-014 |
| [AST-016](../modules/02-language-and-navigation.md#ast-016) | Explain HTTP error translation | Characterize | 1.5 hours | AST-015 |
| [AST-017](../modules/02-language-and-navigation.md#ast-017) | Trace an asynchronous request lifecycle | Study | 1.5 hours | AST-016 |
| [AST-018](../modules/02-language-and-navigation.md#ast-018) | Explain a small code change without tools | Practice | 1 hour | AST-017 |

## [Module 03: build usable interface states](../modules/03-react-and-accessibility.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-019](../modules/03-react-and-accessibility.md#ast-019) | Protect nested favorite navigation | Characterize | 1.5 hours | AST-018 |
| [AST-020](../modules/03-react-and-accessibility.md#ast-020) | Make notification loading honest | Extend | 2 hours | AST-019 |
| [AST-021](../modules/03-react-and-accessibility.md#ast-021) | Help users enter valid page titles | Extend | 2 hours | AST-020 |
| [AST-022](../modules/03-react-and-accessibility.md#ast-022) | Keep Quick Open focus predictable | Extend | 2.5 hours | AST-021 |
| [AST-023](../modules/03-react-and-accessibility.md#ast-023) | Handle empty keyboard results safely | Extend | 2 hours | AST-022 |
| [AST-024](../modules/03-react-and-accessibility.md#ast-024) | Review the UI as a complete journey | Practice | 1.5 hours | AST-023 |

## [Module 04: work across the HTTP boundary](../modules/04-http-and-contracts.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-025](../modules/04-http-and-contracts.md#ast-025) | Document three live contracts | Study | 1 hour | AST-024 |
| [AST-026](../modules/04-http-and-contracts.md#ast-026) | Preserve useful API error detail | Extend | 2 hours | AST-025 |
| [AST-027](../modules/04-http-and-contracts.md#ast-027) | Verify no-content and JSON successes | Characterize | 1.5 hours | AST-026 |
| [AST-028](../modules/04-http-and-contracts.md#ast-028) | Reject invalid titles on the server | Characterize | 2 hours | AST-027 |
| [AST-029](../modules/04-http-and-contracts.md#ast-029) | Distinguish search failure from cancellation | Extend | 3 hours | AST-028 |
| [AST-030](../modules/04-http-and-contracts.md#ast-030) | Review an API change from both sides | Practice | 1.5 hours | AST-029 |

## [Module 05: change persisted data deliberately](../modules/05-data-and-migrations.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-031](../modules/05-data-and-migrations.md#ast-031) | Explain the current relational model | Study | 1.5 hours | AST-030 |
| [AST-032](../modules/05-data-and-migrations.md#ast-032) | Specify page summaries before implementation | Practice | 1 hour | AST-031 |
| [AST-033](../modules/05-data-and-migrations.md#ast-033) | Add a reviewed summary migration | Extend | 2 hours | AST-032 |
| [AST-034](../modules/05-data-and-migrations.md#ast-034) | Expose summary behavior through the API | Extend | 3 hours | AST-033 |
| [AST-035](../modules/05-data-and-migrations.md#ast-035) | Edit summaries in the page view | Extend | 3 hours | AST-034 |
| [AST-036](../modules/05-data-and-migrations.md#ast-036) | Prove an old-data upgrade and hand it off | Characterize | 2.5 hours | AST-035 |

## [Module 06: prove who can do what](../modules/06-permissions.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-037](../modules/06-permissions.md#ast-037) | Build the actual permission matrix | Study | 1.5 hours | AST-036 |
| [AST-038](../modules/06-permissions.md#ast-038) | Verify session expiry behavior | Characterize | 2 hours | AST-037 |
| [AST-039](../modules/06-permissions.md#ast-039) | Prove a forbidden write changes nothing | Characterize | 2 hours | AST-038 |
| [AST-040](../modules/06-permissions.md#ast-040) | Audit indirect page visibility | Characterize | 2.5 hours | AST-039 |
| [AST-041](../modules/06-permissions.md#ast-041) | Verify public-link revocation | Characterize | 2 hours | AST-040 |
| [AST-042](../modules/06-permissions.md#ast-042) | Review a new endpoint's access policy | Practice | 1.5 hours | AST-041 |

## [Module 07: own a full-stack feature](../modules/07-personal-favorites.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-043](../modules/07-personal-favorites.md#ast-043) | Decide ownership and historical-data policy | Practice | 2 hours | AST-042 |
| [AST-044](../modules/07-personal-favorites.md#ast-044) | Add the member-page relationship | Extend | 3 hours | AST-043 |
| [AST-045](../modules/07-personal-favorites.md#ast-045) | Make favorite writes belong to the caller | Extend | 3 hours | AST-044 |
| [AST-046](../modules/07-personal-favorites.md#ast-046) | Make every favorite read caller-specific | Extend | 4 hours | AST-045 |
| [AST-047](../modules/07-personal-favorites.md#ast-047) | Integrate personal favorites into the UI | Extend | 3 hours | AST-046 |
| [AST-048](../modules/07-personal-favorites.md#ast-048) | Demonstrate the feature end to end | Practice | 2 hours | AST-047 |

## [Module 08: preserve correctness when work overlaps](../modules/08-debugging-and-concurrency.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-049](../modules/08-debugging-and-concurrency.md#ast-049) | Reproduce a stale edit precisely | Characterize | 2 hours | AST-048 |
| [AST-050](../modules/08-debugging-and-concurrency.md#ast-050) | Preserve a user's conflicting draft | Extend | 3 hours | AST-049 |
| [AST-051](../modules/08-debugging-and-concurrency.md#ast-051) | Investigate the overlapping-write guarantee | Characterize | 3 hours | AST-050 |
| [AST-052](../modules/08-debugging-and-concurrency.md#ast-052) | Enforce the agreed version invariant | Extend | 4 hours | AST-051 |
| [AST-053](../modules/08-debugging-and-concurrency.md#ast-053) | Exercise concurrent favorite operations | Characterize | 3 hours | AST-052 |
| [AST-054](../modules/08-debugging-and-concurrency.md#ast-054) | Remove the obsolete shared-favorite field | Extend | 3 hours | AST-053 |

## [Module 09: measure, verify, and hand off](../modules/09-performance-and-delivery.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-055](../modules/09-performance-and-delivery.md#ast-055) | Measure favorite projection cost | Characterize | 2 hours | AST-054 |
| [AST-056](../modules/09-performance-and-delivery.md#ast-056) | Make one evidenced performance improvement | Extend | 3 hours | AST-055 |
| [AST-057](../modules/09-performance-and-delivery.md#ast-057) | Create a repeatable local verification command | Extend | 2 hours | AST-056 |
| [AST-058](../modules/09-performance-and-delivery.md#ast-058) | Write a local incident runbook | Practice | 1.5 hours | AST-057 |
| [AST-059](../modules/09-performance-and-delivery.md#ast-059) | Rehearse an upgrade and fallback | Practice | 2 hours | AST-058 |
| [AST-060](../modules/09-performance-and-delivery.md#ast-060) | Deliver the core contributor demo | Practice | 2 hours | AST-059 |

## [Module 10: transfer skills into TypeScript systems](../modules/10-typescript-systems.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-061](../modules/10-typescript-systems.md#ast-061) | Navigate a TypeScript workspace | Study | 2 hours | AST-060 |
| [AST-062](../modules/10-typescript-systems.md#ast-062) | Characterize local issue filtering | Characterize | 2 hours | AST-061 |
| [AST-063](../modules/10-typescript-systems.md#ast-063) | Harden redaction for overlapping known secrets | Extend | 3 hours | AST-062 |
| [AST-064](../modules/10-typescript-systems.md#ast-064) | Trace duplicated and reordered server deltas | Characterize | 3 hours | AST-063 |
| [AST-065](../modules/10-typescript-systems.md#ast-065) | Explore a small CRDT's convergence | Characterize | 3 hours | AST-064 |
| [AST-066](../modules/10-typescript-systems.md#ast-066) | Compare three consistency approaches | Practice | 2 hours | AST-065 |

## [Module 11: commerce across boundaries](../modules/11-commerce.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-067](../modules/11-commerce.md#ast-067) | Strengthen money input invariants | Extend | 2.5 hours | AST-060 |
| [AST-068](../modules/11-commerce.md#ast-068) | Protect catalog view-model semantics | Characterize | 2 hours | AST-067 |
| [AST-069](../modules/11-commerce.md#ast-069) | Prove cache invalidation follows a write | Characterize | 3 hours | AST-068 |
| [AST-070](../modules/11-commerce.md#ast-070) | Trace stock reservation and fake payment | Characterize | 3 hours | AST-069 |
| [AST-071](../modules/11-commerce.md#ast-071) | Check contract drift in two full-stack apps | Study | 2.5 hours | AST-070 |
| [AST-072](../modules/11-commerce.md#ast-072) | Review a commerce change for failure behavior | Practice | 2 hours | AST-071 |

## [Module 12: design business rules for change](../modules/12-domain-design.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-073](../modules/12-domain-design.md#ast-073) | Map a domain use case through its layers | Study | 2 hours | AST-060 |
| [AST-074](../modules/12-domain-design.md#ast-074) | Add a meaningful money property example | Characterize | 2.5 hours | AST-073 |
| [AST-075](../modules/12-domain-design.md#ast-075) | Test effective dates at a boundary | Characterize | 3 hours | AST-074 |
| [AST-076](../modules/12-domain-design.md#ast-076) | Extend a simulated rule pack | Extend | 3 hours | AST-075 |
| [AST-077](../modules/12-domain-design.md#ast-077) | Exercise a workflow's illegal transitions | Characterize | 2.5 hours | AST-076 |
| [AST-078](../modules/12-domain-design.md#ast-078) | Measure a requirement change's reach | Practice | 2 hours | AST-077 |

## [Module 13: reliable work across process boundaries](../modules/13-integrations.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-079](../modules/13-integrations.md#ast-079) | Trace one fake connector run | Study | 2 hours | AST-060 |
| [AST-080](../modules/13-integrations.md#ast-080) | Verify retry exhaustion and recovery | Characterize | 3 hours | AST-079 |
| [AST-081](../modules/13-integrations.md#ast-081) | Exercise webhook verification boundaries | Characterize | 3 hours | AST-080 |
| [AST-082](../modules/13-integrations.md#ast-082) | Test a scheduler boundary without waiting | Characterize | 2.5 hours | AST-081 |
| [AST-083](../modules/13-integrations.md#ast-083) | Trace durable webhook redelivery | Characterize | 3 hours | AST-082 |
| [AST-084](../modules/13-integrations.md#ast-084) | Write a duplicate-delivery support playbook | Practice | 2 hours | AST-083 |

## [Module 14: event pipelines and analytical correctness](../modules/14-analytics-and-streams.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-085](../modules/14-analytics-and-streams.md#ast-085) | Map an event's lifecycle | Study | 2 hours | AST-060 |
| [AST-086](../modules/14-analytics-and-streams.md#ast-086) | Prove deduplication scope | Characterize | 3 hours | AST-085 |
| [AST-087](../modules/14-analytics-and-streams.md#ast-087) | Exercise a poison event and replay | Characterize | 3 hours | AST-086 |
| [AST-088](../modules/14-analytics-and-streams.md#ast-088) | Verify analytics time-window boundaries | Characterize | 3 hours | AST-087 |
| [AST-089](../modules/14-analytics-and-streams.md#ast-089) | Bound an export job's behavior | Characterize | 3 hours | AST-088 |
| [AST-090](../modules/14-analytics-and-streams.md#ast-090) | Measure a pipeline under a controlled workload | Practice | 2.5 hours | AST-089 |

## [Module 15: support systems and evidence-based AI features](../modules/15-support-and-evaluation.md)

| Story | Outcome | Mode | Estimate | Depends on |
| --- | --- | --- | --- | --- |
| [AST-091](../modules/15-support-and-evaluation.md#ast-091) | Map retrieval and evaluation separately | Study | 2 hours | AST-060 |
| [AST-092](../modules/15-support-and-evaluation.md#ast-092) | Add no-evidence and near-threshold cases | Characterize | 3 hours | AST-091 |
| [AST-093](../modules/15-support-and-evaluation.md#ast-093) | Verify the evaluator catches a bad answer | Characterize | 3 hours | AST-092 |
| [AST-094](../modules/15-support-and-evaluation.md#ast-094) | Test instruction-like retrieved content | Characterize | 3 hours | AST-093 |
| [AST-095](../modules/15-support-and-evaluation.md#ast-095) | Test a support SLA boundary | Characterize | 3 hours | AST-094 |
| [AST-096](../modules/15-support-and-evaluation.md#ast-096) | Write an evaluation-backed rollout proposal | Practice | 2.5 hours | AST-095 |
