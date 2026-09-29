# Module 11: commerce across boundaries

**Outcome:** Reason about monetary values, server-owned totals, UI contracts, and cached reads. **Prerequisite:** AST-060. Allow 22-30 hours. All scenarios use local data and fake payment adapters.

## Lesson

Money needs an explicit currency, unit, and rounding policy. A display amount is not authority to charge or reserve stock. Catalog caching and checkout correctness solve different problems: a slightly stale browse result can be acceptable while a charge must be based on current server rules.

The inspected Storefront code contains catalog and money utilities, while its README describes later checkout work. Use its current catalog source for the first stories and the implemented `agora-net` checkout for payment flow study. A sibling project is a comparison, not a drop-in adapter.

## Guided lab

Read Storefront's `money` constructor and catalog view-model mapping. Then draw Agora Net's checkout service as read/validate/reserve/charge/commit or the actual phases you find. Mark database operations and external port calls separately. Never connect the exercises to real payment credentials.

<a id="ast-067"></a>

### AST-067 — Strengthen money input invariants

**Mode:** Extend · **Estimate:** 2.5 hours · **Depends on:** AST-060

**Story:** As a merchant, I want invalid monetary inputs rejected so that extreme or malformed values cannot silently lose precision.

**Start here:** [Storefront money](../../storefront/lib/money.ts), [money tests](../../storefront/lib/money.test.ts).

**Acceptance:**
- Specify safe-integer minor units and ensure constructor/arithmetic results reject unsafe or nonfinite values.
- Preserve documented negative-value behavior instead of banning refunds/adjustments without a requirement.
- Keep currency agreement and integer quantity rules intact.

**Verify:** Boundary examples around the safe-integer range, nonfinite inputs, and valid existing arithmetic; run `pnpm.cmd exec vitest run` from Storefront.

**Hint / review:** `Number.isInteger` alone accepts integers that JavaScript cannot represent with exact neighboring values.

<a id="ast-068"></a>

### AST-068 — Protect catalog view-model semantics

**Mode:** Characterize · **Estimate:** 2 hours · **Depends on:** AST-067

**Story:** As a shopper, I want price and availability displayed accurately so that a product card does not promise an unavailable variant.

**Start here:** [catalog service](../../storefront/server/services/catalog.ts), [catalog tests](../../storefront/server/services/catalog.test.ts), [product data](../../storefront/server/data/products.ts).

**Acceptance:**
- Explain cheapest variant, priceVaries, inStock, and image fallback behavior from current code.
- Add a missing mixed-variant or missing-image case within the actual data contract.
- Confirm view models remain serializable and do not expose raw Prisma rows to client components.

**Verify:** A focused service case distinguishes at least one misleading display from the intended result.

**Hint / review:** Verify whether zero-variant products are permitted before inventing a fixture the repository layer never returns.

<a id="ast-069"></a>

### AST-069 — Prove cache invalidation follows a write

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-068

**Story:** As a merchant changing catalog data, I want cached reads to update under their policy so that shoppers do not see indefinitely stale information.

**Start here:** [Bazaar cache policy](../../bazaar/packages/cache/src/policy.ts), [cache implementation](../../bazaar/packages/cache/src/index.ts), [cache tests](../../bazaar/packages/cache/src/index.test.ts).

**Acceptance:**
- Trace one implemented catalog write to its actual invalidation mechanism and reader.
- State the expected freshness boundary and cache-key scope before writing assertions.
- Add a missing write/read or cross-scope case with a controlled clock when expiry is involved.

**Verify:** Warm cache, perform the write/invalidation, and demonstrate the intended subsequent value under the documented policy.

**Hint / review:** Testing only an invalidation helper does not prove the write path invokes it.

<a id="ast-070"></a>

### AST-070 — Trace stock reservation and fake payment

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-069

**Story:** As a shopper, I want checkout to handle a failed charge coherently so that I do not receive an order for an unpaid purchase or lose stock indefinitely.

**Start here:** [Agora Net checkout](../../agora-net/src/Agora.Infrastructure/Services/CheckoutService.cs), [fake gateway](../../agora-net/src/Agora.Infrastructure/Services/FakePaymentGateway.cs), [tests](../../agora-net/tests/Agora.Tests).

**Acceptance:**
- Map implemented checkout phases and identify the database/external-call boundary.
- Select a missing failed-payment or retry case and define expected order/stock state.
- Verify totals derive from trusted server data, not a browser-supplied amount.

**Verify:** Use the existing injectable fake/test harness; assert resulting persisted state as well as response.

**Hint / review:** An external payment and a database transaction do not share an automatic atomic commit.

<a id="ast-071"></a>

### AST-071 — Check contract drift in two full-stack apps

**Mode:** Study · **Estimate:** 2.5 hours · **Depends on:** AST-070

**Story:** As a frontend contributor, I want to understand contract drift checks so that a server DTO change cannot quietly break the client.

**Start here:** [Agora web scripts](../../agora/web/package.json), [Agora contracts](../../agora/src/Agora.Contracts), [Bazaar App catalog DTOs](../../bazaar-app/server/Bazaar.Api/Contracts/CatalogDtos.cs), [Bazaar App client](../../bazaar-app/client/src).

**Acceptance:**
- Trace one catalog field from response definition to UI in each app.
- Explain Agora's checked-in type generation/check scripts using their implementation, and identify Bazaar App's actual type strategy.
- Write a proposed field-rename checklist covering wire compatibility, generated/manual types, tests, and rendering.

**Verify:** Run applicable existing contract checks after inspecting their prerequisites; record differences without modifying both apps for a paper exercise.

**Hint / review:** A generator is useful only when its source and generated output are kept in agreement.

<a id="ast-072"></a>

### AST-072 — Review a commerce change for failure behavior

**Mode:** Practice · **Estimate:** 2 hours · **Depends on:** AST-071

**Story:** As a commerce reviewer, I want evidence about failure and retry behavior so that a successful checkout demo does not hide data-integrity risks.

**Start here:** [Bazaar App checkout endpoints](../../bazaar-app/server/Bazaar.Api/Endpoints/CheckoutEndpoints.cs), AST-070 evidence, [review template](../templates/review.md).

**Acceptance:**
- Compare where validation, authorization, price authority, stock changes, and payment effects live in two implemented commerce paths.
- Identify one proven guarantee and one open question for each, citing source and tests.
- Propose one small follow-up story with measurable acceptance criteria; do not recommend broad rewrites from folder preferences.

**Verify:** Walk through a retry or stock-contention timeline during mentor review.

**Hint / review:** Treat all financial examples as application-domain exercises, not instructions for real payroll, tax, or payment operations.

## Exit check

Explain why browse data, money values, and charge authority have different constraints. Choose another elective or a [capstone](../capstones/README.md).
