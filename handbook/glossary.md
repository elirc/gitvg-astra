# Working glossary

| Term | Meaning in these exercises | Concrete place to look |
| --- | --- | --- |
| Acceptance criterion | An observable condition that establishes a story's outcome | Any module's story checklist |
| Adapter | Implementation of a boundary to storage, time, or a vendor | Relay App fake action dispatcher |
| ADR | Short record of a design decision, alternatives, and consequences | Folio App `docs/adr` |
| API | Interface one program calls to interact with another | Folio `/api/pages/{id}` |
| Authentication | Establishing who the caller is | Folio login/JWT setup |
| Authorization | Deciding whether a caller may act on a resource | `PageAuthorization.cs` |
| Backfill | Populate a new data structure from existing data | Shared-star to member/page migration |
| Baseline | Observed state before your change | Tool and test record from AST-002 |
| Branch | Named line of Git history | `astra/AST-007-first-contribution` inside Folio App |
| Cache invalidation | Make an obsolete cached value unavailable or refreshable | Bazaar cache package |
| Cancellation | Request to stop obsolete asynchronous work | `AbortController` and `CancellationToken` |
| Cardinality | Number of related records or distinct metric-label values, depending on context | Page children; metric dimensions |
| Characterization | Establish what the current implementation does | Existing-case investigations in modules |
| CI | Automated checks triggered on shared changes | Sibling projects' workflow files; new work in AST-057 |
| Composite key | Key formed from multiple fields | Proposed `(MemberId, PageId)` favorite identity |
| Concurrency | Work overlapping in time | Two updates based on the same stored version |
| Contract | Observable request/response behavior and constraints | DTOs, status codes, and typed client |
| CRDT | Replicated data structure with merge/application rules designed for convergence | Folio's teaching RGA |
| Derived data | Value computed from current inputs | Favorites filtered from a page tree |
| DTO | Data shape crossing an interface | `UpdatePageRequest` |
| EF Core | Data-access framework mapping .NET objects to database queries/changes | `FolioDbContext` |
| Entity | Business object represented in persisted state | Page, Block, Member |
| Fixture | Controlled input/environment used by a test | `FolioApiFactory` and seed data |
| Foreign key | Database constraint linking a row to an existing referenced row | Block's Page reference |
| Idempotency | Repeating an operation has the same intended effect as one application | Repeated favorite; duplicate delivery processing |
| Integration test | Test spanning assembled boundaries | HTTP through the real API and migrated SQLite |
| Invariant | Rule that must remain true | Unique member/page favorite; compatible money currency |
| Migration | Ordered transition from one database schema/data state to another | Folio migration files |
| Mock/stub/fake | Controlled replacements with different testing roles | Fetch stubs, fake clocks, fake gateways |
| N+1 query | One list query followed by a query for each item | Favorite membership looked up per page |
| Optimistic concurrency | Attempt a write with a version condition and detect conflicting changes | Page/block versioned updates |
| Outbox | Persisted pending messages tied to business work for later delivery | Tracer Net webhook outbox |
| Pagination | Return a bounded slice with navigation metadata | Folio `PaginationQuery` |
| Port | Contract stating what outside behavior a use case needs | Atlas Application interfaces |
| PR | Proposed diff plus discussion/evidence for integration | Learner contribution review |
| Projection | Shape selected/computed for a read consumer | Caller-relative `isFavorite` in a tree DTO |
| Regression | Previously correct behavior becomes incorrect | A refactor exposing another member's favorites |
| RRF | Rank fusion combining result lists by rank rather than incomparable raw scores | Harbor retrieval package |
| RGA | A sequence CRDT retaining stable element ids and deletion markers | Folio `crdt-101` |
| Soft delete | Mark data as deleted while retaining stored records | `Page.IsDeleted` query filter |
| Staging/index | Selected content for the next Git commit | `git diff --cached` |
| Tenant/workspace scope | Boundary separating customers' or teams' data | Acme versus Globex |
| Tombstone | Retained deletion marker for references/convergence | Deleted RGA element |
| Transaction | Database operations committed or rolled back together | Consistent mutation and activity persistence |
| Upgrade test | Exercise migration from old schema/data | AST-036 and AST-044 fixtures |

Use the [repository map](../REPO-MAP.md) to reach the named projects and [code tour](../onboarding/03-code-tour.md) for the primary request path.
