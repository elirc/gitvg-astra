# Mentor guide and assessment

Assess independence through explanations, diffs, and behavior. The objective is a learner who can own a scoped contribution with review, not a learner who finishes checkboxes quickly.

## Weekly rhythm

Begin with a 15-minute planning review: choose one outcome, confirm prerequisites, and name the evidence. Midweek, review one small diff or debugging hypothesis. End with a 20-30 minute demo and retrospective. Ask the learner to predict an edge case before running it. Keep one story active and use estimates to reveal scope, not to rank learners.

For early stories, provide a source path and one hint. In the middle modules, ask the learner to locate the path and propose a check. By the core handoff, give a behavior-level requirement and review the learner's plan. If you type the critical implementation yourself, record that assistance and reassess the skill in a later case.

## Four evidence levels

| Score | Demonstrated behavior |
| --- | --- |
| 0: not yet | Cannot explain or complete the behavior, or evidence is missing |
| 1: guided | Completes with specific directions and can explain the resulting code |
| 2: independent with review | Chooses a reasonable approach, handles the main failure paths, and responds constructively to review |
| 3: transferable | Predicts an unfamiliar variation, evaluates trade-offs, and helps another learner reason through it |

Record a score per competency with a link to evidence. Do not average away a missing core competency with a strong presentation score.

| Competency | Core evidence | Graduation expectation |
| --- | --- | --- |
| Environment and navigation | AST-001-006, AST-013-018 | 2: reproduce setup and trace a request |
| Git and scope | AST-007-012 | 2: preserve work and present a focused patch |
| UI and accessibility | AST-019-024, AST-047, AST-050 | 2: keyboard, state, validation, and draft recovery |
| API reasoning | AST-025-030, AST-034 | 2: contracts, errors, and compatibility |
| Data and migration | AST-031-036, AST-044, AST-054 | 2: preserve old data and justify constraints |
| Authorization | AST-037-042, AST-045-046 | 2: caller scope and indirect visibility |
| Testing and debugging | AST-049-053 | 2: meaningful assertions and precise concurrency claims |
| Delivery and communication | AST-055-060 | 2: honest checks, measurements, and usable handoff |
| Chosen specialization | One complete elective | 2 in the elective's stated outcome |

## Review prompts by checkpoint

After Module 01: "Show what is staged, explain why it belongs in this patch, and identify one working-tree edit that would not enter the commit."

After Module 04: "The browser receives a 403. Which state should the UI preserve, and why should the session remain valid?"

After Module 05: "An existing page has a summary. What happens when an old client renames it without sending that field? Show evidence."

After Module 07: "Ada stars a page. Where could Grace still see that star if you missed one projection?"

After Module 08: "Both requests read the same version before either saves. Which mechanism decides the winner? What did your test actually synchronize?"

After Module 09: "A migration removed the old favorite column. Can you safely run yesterday's executable against today's database? Explain the fallback."

## When a learner is stuck

Distinguish a concept gap, environment blocker, ambiguous requirement, and an oversized task. Ask for the smallest reproduction and first useful error. Give one next experiment rather than a complete patch. For a concept gap, return to a tiny scratch example; for ambiguity, decide the product policy together; for overscope, split the story. Do not punish an honest failure report or reward an unverified claim.

## Portfolio and final assessment

Keep one representative reviewed UI patch, one API/data patch, one regression investigation, one migration/ADR, and one handoff report. Redact operational secrets and identify solo/AI assistance accurately. A capstone demo should include a user journey, a denied/failing action, a data upgrade if relevant, and a five-minute live explanation of a small requirement variation.

Pass graduation when all core competencies and the chosen elective reach level 2, one capstone meets its criteria, and unresolved defects are explicitly bounded. If not, choose two targeted stories to repeat with new inputs. Completion of this program demonstrates these observed skills; job titles still depend on broader experience and the team's expectations.
