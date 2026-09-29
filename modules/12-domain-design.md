# Module 12: design business rules for change

**Outcome:** Use invariants, effective dates, ports, and architecture checks deliberately. **Prerequisite:** AST-060. Allow 20-28 hours. Payroll/leave examples exercise the repository's simulated rules, not real-world legal entitlements.

## Lesson

A domain invariant is a condition the business model must maintain, such as currency compatibility or a legal state transition. A port expresses what a use case needs from an outside system. An adapter supplies one implementation. Architecture earns its complexity when a changed requirement stays local and tests can prove the dependency rules.

Atlas and Atlas Net both model employment but use different structures. Atlas has a separate Application layer and domain rule packs; Atlas Net offers a more compact backend with domain calculators. Learn from the difference instead of porting class hierarchies mechanically.

## Guided lab

Pick one calculation and one workflow in Atlas. Trace each from an input to an invariant failure or result. Find which dependencies are pure and which provide time, persistence, or external behavior. Then compare a related calculator in Atlas Net. Keep example dates, currencies, and policies grounded in the checked-in code.

<a id="ast-073"></a>

### AST-073 — Map a domain use case through its layers

**Mode:** Study · **Estimate:** 2 hours · **Depends on:** AST-060

**Story:** As a contributor joining Atlas, I want to understand dependency direction so that a business-rule change stays out of infrastructure code.

**Start here:** [Atlas README](../../atlas/README.md), [Application](../../atlas/src/Atlas.Application), [architecture tests](../../atlas/tests/Atlas.ArchitectureTests).

**Acceptance:**
- Trace one real use case through Contracts/API/Application/Domain and its persistence or vendor port.
- Identify an enforced forbidden dependency and the test that detects it.
- Compare the layout with Folio App's actual controller/service/DbContext flow.

**Verify:** Run the existing architecture test project and explain one assertion's practical effect.

**Hint / review:** A diagram is documentation; a passing architecture test establishes only the relationships its assertions inspect.

<a id="ast-074"></a>

### AST-074 — Add a meaningful money property example

**Mode:** Characterize · **Estimate:** 2.5 hours · **Depends on:** AST-073

**Story:** As a payroll maintainer, I want money rules exercised across inputs so that a single happy-path total does not hide rounding or currency errors.

**Start here:** [Atlas Money](../../atlas/src/Atlas.Domain/Money/Money.cs), [property tests](../../atlas/tests/Atlas.Domain.Tests/Money/MoneyPropertyTests.cs), [Atlas Net money tests](../../atlas-net/tests/Atlas.Tests/Domain/MoneyInvariantTests.cs).

**Acceptance:**
- State the actual units, allowed operations, currency rules, and rounding boundaries in each model.
- Add a missing invariant or boundary example within valid domain ranges.
- If using generated cases, constrain inputs and preserve a reproducible failing seed/counterexample.

**Verify:** Run the focused domain suite and explain why the property is a business rule rather than an algebraic assumption invalidated by rounding.

**Hint / review:** Floating-point approximations and decimal rounding do not permit every textbook identity unchanged.

<a id="ast-075"></a>

### AST-075 — Test effective dates at a boundary

**Mode:** Characterize · **Estimate:** 3 hours · **Depends on:** AST-074

**Story:** As a payroll operator, I want salary changes applied to the correct period so that a later amendment does not rewrite earlier results.

**Start here:** [Atlas employment terms](../../atlas/src/Atlas.Domain/Workforce/EmploymentTerms.cs), [Atlas Net salary record](../../atlas-net/src/Atlas.Domain/Entities/SalaryRecord.cs), [payroll calculator](../../atlas-net/src/Atlas.Domain/Services/PayrollCalculator.cs).

**Acceptance:**
- Derive interval inclusivity and effective-date behavior from one selected implementation.
- Add a missing boundary case involving a change on a period boundary or a gap/overlap rejected by the model.
- Assert historical inputs/results remain consistent with the chosen policy.

**Verify:** Use fixed dates and exact expected amounts; record which project owns the new test.

**Hint / review:** Write a date timeline before writing arithmetic. Do not assume both projects use identical date semantics.

<a id="ast-076"></a>

### AST-076 — Extend a simulated rule pack

**Mode:** Extend · **Estimate:** 3 hours · **Depends on:** AST-075

**Story:** As a product team testing a new policy variant, I want a synthetic rule pack so that I can add behavior through the intended extension point.

**Start here:** [ICountryRulePack](../../atlas/src/Atlas.Domain/Countries/ICountryRulePack.cs), [existing packs](../../atlas/src/Atlas.Domain/Countries/Packs), [CountryRulePacks](../../atlas/src/Atlas.Domain/Countries/CountryRulePacks.cs).

**Acceptance:**
- Introduce a clearly labeled test-only policy variant through the current extension mechanism.
- Use explicit synthetic values and avoid presenting them as real country law.
- Demonstrate which changes are needed for discovery/selection and which core calculation files remain untouched.

**Verify:** Focused tests select the variant and assert its outputs; architecture checks stay green.

**Hint / review:** If valid country identifiers are constrained, use a test fixture/variant for an existing supported identifier rather than weakening validation to invent one.

<a id="ast-077"></a>

### AST-077 — Exercise a workflow's illegal transitions

**Mode:** Characterize · **Estimate:** 2.5 hours · **Depends on:** AST-076

**Story:** As an approver, I want invalid repeated decisions rejected consistently so that a workflow cannot enter contradictory states.

**Start here:** [ApprovalWorkflow](../../atlas/src/Atlas.Domain/Approvals/ApprovalWorkflow.cs), [transitions](../../atlas/src/Atlas.Domain/Approvals/ApprovalTransitions.cs), [workflow tests](../../atlas/tests/Atlas.Domain.Tests/Approvals/ApprovalWorkflowTests.cs).

**Acceptance:**
- Draw the implemented states/transitions, including terminal states and error behavior.
- Add a missing repeated or forbidden transition case and check state remains valid afterward.
- Separate pure transition rules from caller permission and persistence concerns.

**Verify:** A compact matrix covers the selected boundary without duplicating the full existing suite.

**Hint / review:** A transition being legal does not mean every authenticated caller is allowed to request it.

<a id="ast-078"></a>

### AST-078 — Measure a requirement change's reach

**Mode:** Practice · **Estimate:** 2 hours · **Depends on:** AST-077

**Story:** As an architecture reviewer, I want evidence of change locality so that abstraction choices can be judged by maintenance cost.

**Start here:** Your rule-pack patch, [Atlas Application](../../atlas/src/Atlas.Application), [Atlas Net architecture](../../atlas-net/docs/architecture.md).

**Acceptance:**
- List changed files by responsibility and explain why each changed for the synthetic policy.
- Describe how a comparable requirement would enter Atlas Net, with actual source entry points.
- Record one benefit and one cost of the extra Application/port boundaries without declaring a universal winner.

**Verify:** Review a concrete diff and a second hypothetical rule change to test the explanation.

**Hint / review:** Fewer changed lines alone is not quality; hidden coupling and clear tests matter too.

## Exit check

Explain an invariant, a port, and a migration as different tools. Choose another elective or a [capstone](../capstones/README.md).
