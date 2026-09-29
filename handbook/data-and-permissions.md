# Data changes and permission boundaries

Data modeling begins with a sentence about the product. "A page is a favorite" suggests a boolean on Page. "A member favorites a page" suggests a relationship between Member and Page. Neither structure is universally correct; the second supports independent user preferences.

## Model the relationship

For Astra's personal favorites, propose a membership identified by `(MemberId, PageId)`. A composite key or unique constraint prevents duplicate favorites even if two requests race. Foreign keys prevent relationships to missing members/pages. The service must also verify both belong to the allowed workspace and that the caller can read the page; two separate foreign keys do not establish this cross-entity rule by themselves.

Decide whether the relationship needs a creation timestamp. Decide what happens to rows when a page is soft-deleted, restored, made private, or eventually hard-deleted. For this course's default policy, retain favorites across soft delete, hide unreadable/trashed pages on reads, and show retained favorites after restore only when access is still allowed. Alternative policies need explicit acceptance examples.

## Evolve a schema in stages

1. Add the new relationship and migration while keeping old reads operational.
2. Define how historical `Page.IsFavorite` values become personal relationships. The old boolean contains no information about who clicked it.
3. Switch writes and all caller-visible projections to the new meaning.
4. Verify the fresh-database and upgrade paths, including idempotent seed behavior.
5. Remove the obsolete boolean in a later migration once the transition is complete.

Astra's default backfill is to seed a relationship for each current member who can read each historically starred page. This preserves visible stars for current readers but does not reconstruct historical intent. State that trade-off in an ADR. For private pages, the current policy permits workspace Owners only; do not backfill inaccessible pages for other roles. Do not make SQL migrations call a running API to decide access. Translate the stable policy carefully, or use a deliberate migration-time data operation with equivalent tests.

If the learner chooses an empty-backfill policy instead, the mentor must accept the changed UX and the upgrade acceptance tests must reflect it. Do not silently choose a policy while writing schema code.

## Generate and inspect migrations

The current EF package version is 10.0.10 in Folio's project files. First check `dotnet ef --version` and any existing tool manifest. If no local tool exists, a project-local tool manifest is a reviewable way to pin it:

```powershell
# Working directory: folio-app/server; only if no tool manifest already applies
dotnet new tool-manifest
dotnet tool install dotnet-ef --version 10.0.10
```

If a manifest already defines the tool, use `dotnet tool restore`. Do not overwrite existing tool configuration. For an agreed model change:

```powershell
# Working directory: folio-app/server
dotnet ef migrations add AddPageSummary --project Folio.Infrastructure --startup-project Folio.Api
dotnet test Folio.slnx --filter 'FullyQualifiedName~MigrationGuardTests'
```

Use the actual migration name for your story. Inspect both migration directions and the snapshot. Review data loss, nullability, default values, indexes, foreign keys, and provider-specific SQL. The design-time factory currently uses its own SQLite connection string; before any database-update command, verify which connection the tooling will target. The normal app startup migration path is distinct from generating a migration file.

An `EnsureCreated` database bypasses migration history. A model that works there can still fail on upgrade. Folio's existing [migration guard](../../folio-app/server/Folio.Tests/MigrationGuardTests.cs) checks model/snapshot agreement, but a real old-data upgrade fixture is still needed for backfill semantics.

## Authenticate, authorize, and filter

Authentication establishes who the caller is. Authorization decides whether that caller can perform this action on this resource. The authenticated member id should come from server-resolved claims, not an arbitrary `memberId` supplied in a favorite request.

Read [PageAuthorization](../../folio-app/server/Folio.Api/Auth/PageAuthorization.cs) and the [permission tests](../../folio-app/server/Folio.Tests/PermissionMatrixTests.cs). Existing rules include foreign-workspace 404s, private pages restricted to Owners, Viewer writes denied, and comments/favorites allowed with read access. "All writes require Editor" would therefore be an incorrect simplification for this application.

Use both direct and indirect tests: page detail, tree, favorites list, search, quick-open, backlinks, export, and notifications can all reveal information. A hidden edit button is a helpful cue but cannot stop a forged HTTP request. Recheck visibility when listing favorites so revoking access removes a page from the result immediately.

## Transactions and concurrency

A transaction makes a set of database operations commit or roll back together. It does not automatically include an external network call. A unique key protects an invariant against competing inserts. An application-side "exists?" check alone can race. An optimistic concurrency token must be part of the actual conditional write or equivalent database protection to cover overlapping writers; comparing tokens in memory covers only the cases that comparison actually observes.

Ask of every invariant: which layer makes it true under two simultaneous requests, and what evidence proves that? Keep fake payment calls and real money completely separate in the commerce electives.
