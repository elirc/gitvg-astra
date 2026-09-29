# Map of the workspace

This workspace is a collection of **17 independent application repositories**, plus shared specifications and teaching material. Matching names do not mean matching implementations. `folio` and `folio-app`, for example, have different stacks and data models. Cross-project exercises compare ideas; they do not assume interchangeable schemas or APIs.

| Project | What you can study here | Start with | Astra module |
| --- | --- | --- | --- |
| `folio-app` | React/TypeScript, .NET 10 controllers/services, EF Core SQLite, document collaboration | [README](../folio-app/README.md), [architecture](../folio-app/docs/architecture.md) | 00-09 |
| `folio` | TypeScript workspaces, collaboration packages, a small text CRDT | [README](../folio/README.md), [RGA](../folio/packages/crdt-101/src/rga.ts) | 10 |
| `tracer` | TypeScript issue tracker, local store and synchronization | [README](../tracer/README.md), [store](../tracer/packages/shared/src/store.ts) | 10 |
| `tracer-net` | .NET issue tracker, state transitions, ranking, saved views, webhooks | [README](../tracer-net/README.md), [ranker](../tracer-net/src/Tracer.Domain/IssueRanker.cs) | 13, capstone |
| `relay` | TypeScript workflow engine, connector packages, fake vendors | [README](../relay/README.md), [redaction](../relay/packages/shared/src/redact.ts) | 10, 13 |
| `relay-app` | React/.NET flow builder, fake execution adapters, schedules and retry policy | [README](../relay-app/README.md), [architecture](../relay-app/docs/architecture.md) | 13 |
| `storefront` | Next.js catalog, view models, integer money, server/client boundaries | [manifest](../storefront/package.json), [catalog service](../storefront/server/services/catalog.ts) | 11 |
| `bazaar` | TypeScript commerce workspaces, cache policy, storefront/admin separation | [README](../bazaar/README.md), [cache policy](../bazaar/packages/cache/src/policy.ts) | 11 |
| `bazaar-app` | React/.NET commerce, catalog and checkout endpoints | [README](../bazaar-app/README.md), [checkout endpoints](../bazaar-app/server/Bazaar.Api/Endpoints/CheckoutEndpoints.cs) | 11 |
| `agora` | .NET layered commerce + React, API contract generation, architecture tests | [README](../agora/README.md), [web scripts](../agora/web/package.json) | 11 |
| `agora-net` | .NET commerce backend, stock reservation, fake payments, returns | [README](../agora-net/README.md), [checkout service](../agora-net/src/Agora.Infrastructure/Services/CheckoutService.cs) | 11, capstone |
| `atlas` | .NET domain/Application/Infrastructure layers, rule packs, ports, outbox | [README](../atlas/README.md), [Money](../atlas/src/Atlas.Domain/Money/Money.cs) | 12 |
| `atlas-net` | .NET employment backend, calculators, effective salary history | [README](../atlas-net/README.md), [payroll calculator](../atlas-net/src/Atlas.Domain/Services/PayrollCalculator.cs) | 12 |
| `pulse` | TypeScript analytics ingestion, streams, consumers, deduplication | [README](../pulse/README.md), [memory stream](../pulse/packages/stream/src/memory.ts) | 14 |
| `pulse-net` | .NET analytics, ingestion/query services, feature flags and exports | [README](../pulse-net/README.md), [query service](../pulse-net/src/Pulse.Infrastructure/Services/QueryService.cs) | 14 |
| `harbor` | TypeScript support system, retrieval, deterministic evaluation, autonomy policies | [README](../harbor/README.md), [retrieval](../harbor/packages/rag/src/retrieve.ts) | 15 |
| `harbor-net` | .NET support backend, SLA policies, assignment, webhook delivery | [README](../harbor-net/README.md), [SLA policies](../harbor-net/src/Harbor.Infrastructure/SlaPolicies.cs) | 15 |

## Current code versus course plans

The workspace [SPEC](../SPEC.md) and [shared sprint index](../docs/sprints/README.md) describe a Meridian curriculum. They are useful historical context, not instructions for a runnable root application. The root has no common package manifest or solution that builds all these projects together.

The Storefront README describes a complete multi-sprint product, including checkout and admin. In the inspected checkout, its tracked implementation is focused on catalog/list/detail pages and related money utilities. Astra's Storefront stories use those existing files. Payment exercises use `agora-net` instead. Do not assume a planned Stripe route exists because it appears in a roadmap.

The original Folio App architecture explicitly documents shared favorites through `Page.IsFavorite`. Personal favorites are Astra's requested extension. Also, its concurrency request field is optional; this is a compatibility decision you will examine rather than silently rewrite during onboarding.

## Finding the next file

```powershell
# Working directory: workspace root
rg --files .\folio-app\client\src
rg -n 'renamePage|expectedVersion' .\folio-app\client\src
rg -n 'SetFavoriteAsync|GetFavoritesAsync|IsFavorite' .\folio-app\server
git -C .\folio-app log --oneline -8
```

Start with `rg` and a narrow project/path. Generated migrations are useful for schema history, but you normally begin with an entity and its model configuration. Read the nearest test after locating an implementation.

Before an elective, inspect that project's manifest or solution, launch settings, database configuration, and existing test harness. Stop the previous application's processes if their ports overlap. Use per-project installation and check commands; a pnpm script from one folder is not guaranteed to exist in another.
