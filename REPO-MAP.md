# Map of the workspace

Astra draws on **17 independent application repositories**, each at `github.com/elirc/<project>`; clone the ones a module needs beside `astra` (see [Set up the workspace](README.md#set-up-the-workspace)). The same 17 also sit together, with the shared specifications, in [elirc/gitvg](https://github.com/elirc/gitvg). Matching names do not mean matching implementations. `folio` and `folio-app`, for example, have different stacks and data models. Cross-project exercises compare ideas; they do not assume interchangeable schemas or APIs.

| Project | What you can study here | Start with | Astra module |
| --- | --- | --- | --- |
| `folio-app` | React/TypeScript, .NET 10 controllers/services, EF Core SQLite, document collaboration | [README](https://github.com/elirc/folio-app/blob/main/README.md), [architecture](https://github.com/elirc/folio-app/blob/main/docs/architecture.md) | 00-09 |
| `folio` | TypeScript workspaces, collaboration packages, a small text CRDT | [README](https://github.com/elirc/folio/blob/main/README.md), [RGA](https://github.com/elirc/folio/blob/main/packages/crdt-101/src/rga.ts) | 10 |
| `tracer` | TypeScript issue tracker, local store and synchronization | [README](https://github.com/elirc/tracer/blob/main/README.md), [store](https://github.com/elirc/tracer/blob/main/packages/shared/src/store.ts) | 10 |
| `tracer-net` | .NET issue tracker, state transitions, ranking, saved views, webhooks | [README](https://github.com/elirc/tracer-net/blob/main/README.md), [ranker](https://github.com/elirc/tracer-net/blob/main/src/Tracer.Domain/IssueRanker.cs) | 13, capstone |
| `relay` | TypeScript workflow engine, connector packages, fake vendors | [README](https://github.com/elirc/relay/blob/main/README.md), [redaction](https://github.com/elirc/relay/blob/main/packages/shared/src/redact.ts) | 10, 13 |
| `relay-app` | React/.NET flow builder, fake execution adapters, schedules and retry policy | [README](https://github.com/elirc/relay-app/blob/main/README.md), [architecture](https://github.com/elirc/relay-app/blob/main/docs/architecture.md) | 13 |
| `storefront` | Next.js catalog, view models, integer money, server/client boundaries | [manifest](https://github.com/elirc/storefront/blob/main/package.json), [catalog service](https://github.com/elirc/storefront/blob/main/server/services/catalog.ts) | 11 |
| `bazaar` | TypeScript commerce workspaces, cache policy, storefront/admin separation | [README](https://github.com/elirc/bazaar/blob/main/README.md), [cache policy](https://github.com/elirc/bazaar/blob/main/packages/cache/src/policy.ts) | 11 |
| `bazaar-app` | React/.NET commerce, catalog and checkout endpoints | [README](https://github.com/elirc/bazaar-app/blob/main/README.md), [checkout endpoints](https://github.com/elirc/bazaar-app/blob/main/server/Bazaar.Api/Endpoints/CheckoutEndpoints.cs) | 11 |
| `agora` | .NET layered commerce + React, API contract generation, architecture tests | [README](https://github.com/elirc/agora/blob/main/README.md), [web scripts](https://github.com/elirc/agora/blob/main/web/package.json) | 11 |
| `agora-net` | .NET commerce backend, stock reservation, fake payments, returns | [README](https://github.com/elirc/agora-net/blob/main/README.md), [checkout service](https://github.com/elirc/agora-net/blob/main/src/Agora.Infrastructure/Services/CheckoutService.cs) | 11, capstone |
| `atlas` | .NET domain/Application/Infrastructure layers, rule packs, ports, outbox | [README](https://github.com/elirc/atlas/blob/main/README.md), [Money](https://github.com/elirc/atlas/blob/main/src/Atlas.Domain/Money/Money.cs) | 12 |
| `atlas-net` | .NET employment backend, calculators, effective salary history | [README](https://github.com/elirc/atlas-net/blob/main/README.md), [payroll calculator](https://github.com/elirc/atlas-net/blob/main/src/Atlas.Domain/Services/PayrollCalculator.cs) | 12 |
| `pulse` | TypeScript analytics ingestion, streams, consumers, deduplication | [README](https://github.com/elirc/pulse/blob/main/README.md), [memory stream](https://github.com/elirc/pulse/blob/main/packages/stream/src/memory.ts) | 14 |
| `pulse-net` | .NET analytics, ingestion/query services, feature flags and exports | [README](https://github.com/elirc/pulse-net/blob/main/README.md), [query service](https://github.com/elirc/pulse-net/blob/main/src/Pulse.Infrastructure/Services/QueryService.cs) | 14 |
| `harbor` | TypeScript support system, retrieval, deterministic evaluation, autonomy policies | [README](https://github.com/elirc/harbor/blob/main/README.md), [retrieval](https://github.com/elirc/harbor/blob/main/packages/rag/src/retrieve.ts) | 15 |
| `harbor-net` | .NET support backend, SLA policies, assignment, webhook delivery | [README](https://github.com/elirc/harbor-net/blob/main/README.md), [SLA policies](https://github.com/elirc/harbor-net/blob/main/src/Harbor.Infrastructure/SlaPolicies.cs) | 15 |

## Current code versus course plans

The [SPEC](https://github.com/elirc/gitvg/blob/main/SPEC.md) and [shared sprint index](https://github.com/elirc/gitvg/blob/main/docs/sprints/README.md) at the root of elirc/gitvg describe a Meridian curriculum. They are useful historical context, not instructions for a runnable application. No shared package manifest or solution builds these projects together.

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
