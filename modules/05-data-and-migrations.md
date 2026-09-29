# Module 05: change persisted data deliberately

**Outcome:** Add an optional page summary through the schema, API, and UI without losing existing data. Allow 15-22 hours. Read [data and permissions](../handbook/data-and-permissions.md).

## Lesson

An entity edit changes the model the program expects; a migration changes a database that already exists. You need both. Nullability, constraints, query filters, and indexes each encode different rules. A fresh seed test is useful but cannot establish that an upgrade preserves existing user-created data.

## Guided lab

Draw Workspace -> Page -> Block, plus Page's optional parent. Locate keys, foreign keys, positions, timestamps, and soft-delete filtering. Then plan one additive feature: a nullable summary of at most 280 characters. This feature is smaller than personal favorites but exercises the full data path. Keep it out of version snapshots, search ranking, and export for this initial slice, and explicitly document those limits.

<a id="ast-031"></a>

### AST-031 — Explain the current relational model

**Mode:** Study · **Estimate:** 1.5 hours · **Depends on:** AST-030

**Story:** As a maintainer, I want a correct data diagram so that I can reason about page changes and deletion.

**Start here:** [Page entity](../../folio-app/server/Folio.Domain/Entities/Page.cs), [DbContext](../../folio-app/server/Folio.Infrastructure/Persistence/FolioDbContext.cs).

**Acceptance:**
- Draw Workspace, Member, Page, and Block with primary/foreign keys and cardinality.
- Explain null parent ids, sibling positions, and the page soft-delete filter.
- Identify one database constraint and one rule enforced by service code.

**Verify:** Point to the corresponding mapping or service statement for each claimed rule.

**Hint / review:** A foreign key is not a guarantee that a move cannot create a logical cycle.

<a id="ast-032"></a>

### AST-032 — Specify page summaries before implementation

**Mode:** Practice · **Estimate:** 1 hour · **Depends on:** AST-031

**Story:** As a page reader, I want a short summary so that I can understand a page's purpose before reading its blocks.

**Start here:** [PageDtos](../../folio-app/server/Folio.Api/Contracts/PageDtos.cs), [ADR template](../templates/adr.md).

**Acceptance:**
- Specify nullable summary, maximum 280 characters, and whitespace-only normalization to null.
- Define compatibility: existing create/rename clients omit summary without unintentionally erasing it.
- Choose a separately named summary update endpoint or an explicit field-presence strategy; name out-of-scope history/search/export behavior.

**Verify:** Write create/read/edit/clear and old-client examples before changing the schema.

**Hint / review:** Optional JSON input and "set this value to null" need distinguishable meanings for a partial update.

<a id="ast-033"></a>

### AST-033 — Add a reviewed summary migration

**Mode:** Extend · **Estimate:** 2 hours · **Depends on:** AST-032

**Story:** As an existing workspace owner, I want the summary feature added without losing pages so that an upgrade preserves my work.

**Start here:** [Page](../../folio-app/server/Folio.Domain/Entities/Page.cs), [migration folder](../../folio-app/server/Folio.Infrastructure/Persistence/Migrations), [migration guide](../handbook/data-and-permissions.md).

**Acceptance:**
- Add the nullable property and matching mapping/migration/snapshot.
- Existing rows acquire a null summary without changes to title, ids, hierarchy, or blocks.
- Review generated operations, including downgrade data-loss implications.

**Verify:** Run migration guards and inspect a migration applied to a disposable pre-change database fixture.

**Hint / review:** Generating a migration is not proof its upgrade behavior is correct.

<a id="ast-034"></a>

### AST-034 — Expose summary behavior through the API

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-033

**Story:** As an authorized editor, I want to read and edit summaries so that page introductions stay useful.

**Start here:** [PagesController](../../folio-app/server/Folio.Api/Controllers/PagesController.cs), [PageService](../../folio-app/server/Folio.Api/Services/PageService.cs), [PageDtos](../../folio-app/server/Folio.Api/Contracts/PageDtos.cs).

**Acceptance:**
- Page detail exposes summary; the agreed update operation validates/normalizes and uses existing write authorization.
- Updating summary rotates the page version and rejects a supplied stale expected version consistently with the current pattern.
- Existing title-only rename requests preserve summary; clear explicitly produces null.

**Verify:** API tests cover create/read, edit, clear, 280/281 lengths, legacy rename, Viewer denial, and stale version.

**Hint / review:** Reuse service policy instead of implementing a second permission system in the controller.

<a id="ast-035"></a>

### AST-035 — Edit summaries in the page view

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-034

**Story:** As an editor, I want an accessible summary field so that I can save or correct it without confusing it with page blocks.

**Start here:** [PageView](../../folio-app/client/src/components/PageView.tsx), [API types](../../folio-app/client/src/api/types.ts), [typed endpoints](../../folio-app/client/src/api/folio.ts).

**Acceptance:**
- Add matching client types/endpoint function and a labeled summary input with count and validation feedback.
- Render appropriate read-only behavior for callers who cannot edit.
- Preserve unsaved text on failure, and display the server's accepted value/version after success.

**Verify:** Component coverage for success, clear, denial/read-only display, and error; manual reload proves persistence.

**Hint / review:** Display state can be local while the server remains the source of accepted values.

<a id="ast-036"></a>

### AST-036 — Prove an old-data upgrade and hand it off

**Mode:** Characterize · **Estimate:** 2.5 hours · **Depends on:** AST-035

**Story:** As a teammate deploying the change, I want upgrade evidence so that I can distinguish a tested migration from a fresh-install demonstration.

**Start here:** [MigrationGuardTests](../../folio-app/server/Folio.Tests/MigrationGuardTests.cs), [delivery guide](../handbook/delivery.md).

**Acceptance:**
- Create a disposable database at the pre-summary migration, insert representative user data, and upgrade to the current migration.
- Verify old values and relationships survive and summaries begin null.
- Update API/application documentation and state that history/search/export do not yet include summary.

**Verify:** Record the old and new migration identifiers, assertions, and complete affected suite results.

**Hint / review:** Resetting to a fresh seed cannot substitute for this upgrade scenario.

## Exit check

Show a persisted summary and an upgrade fixture. Continue to [Module 06](06-permissions.md).
