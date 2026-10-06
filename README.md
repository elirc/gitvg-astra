# Astra: a junior developer's field bootcamp

Learn to join a team, understand an unfamiliar application, and deliver changes that another developer can confidently review. This is a hands-on curriculum built around the code in this workspace: **96 progressively scoped user stories, 16 teaching modules, a continuous full-stack project, and three graduation capstones**.

Start with [your first day](onboarding/01-first-day.md), then [run the application](onboarding/02-local-setup.md). You do not need to understand every project or install every project's dependencies.

## Who this is for

You can write a function, use a terminal a little, and recognize HTML. You may never have opened a pull request, run a migration, debugged an HTTP request, or written an integration test. Those are taught here. If loops, objects, or functions are still unfamiliar, do the short exercises in [Foundations](handbook/foundations.md) before Module 02.

The primary application is [Folio App](https://github.com/elirc/folio-app/blob/main/README.md): React + TypeScript in the browser, C# + ASP.NET Core on the server, and SQLite for storage. Its pages, comments, search, and favorites are understandable without specialist business knowledge. Later modules transfer those skills into the other applications.

## Start here, in order

1. [First day and learning agreement](onboarding/01-first-day.md): orientation, diagnostic, and evidence notebook.
2. [Local setup](onboarding/02-local-setup.md): two terminals, seeded accounts, first HTTP request, and baseline checks.
3. [Code tour](onboarding/03-code-tour.md): follow a page rename from the browser to SQLite.
4. [Git and contribution workflow](onboarding/04-git-contribution.md): branch, inspect, stage, commit, review, and recover.
5. [Your first contribution](onboarding/05-first-change.md): a guided, deliberately small UI improvement.
6. [Curriculum and pacing](CURRICULUM.md): complete the core path, then choose an elective.
7. [User story index](stories/README.md) and [progress tracker](TRACKER.md): choose work and record evidence.

## What you will build

Modules 00-06 develop your working habits through small exercises in the existing app. Module 07 changes **workspace-wide favorites into personal favorites**. Modules 08-09 harden and hand off that feature. This is a proposed product change: the current shared-favorite behavior is documented and intentional, so you must explain the changed requirements instead of calling it a discovered defect.

Each module contains a short lesson, a guided lab, six concrete user stories, acceptance criteria, verification guidance, hints, and an exit check. Stories alternate between reading existing behavior, adding evidence, and implementing a requested extension. They are assignments for the learner; this folder does not implement the product features for you.

## Choose a route

| Route | Work | Suggested effort |
| --- | --- | --- |
| First contribution | Onboarding + Modules 00-01 | 12-20 focused hours |
| Core contributor | Modules 00-09, AST-001 through AST-060 | 140-200 hours including reading, review, and rework |
| Specialization | Any one of Modules 10-15 after the core | 18-30 hours per module |
| Graduation | One [capstone](capstones/README.md) after core + one elective | 20-35 hours |
| Extended program | All 96 stories + one capstone | About 300-420 hours |

Estimates are planning aids, not performance targets. At 10 hours per week, the core commonly occupies 14-20 weeks; at 25 hours per week, budget 6-8 weeks. Extend the calendar when a prerequisite needs practice. Completing a folder does not automatically confer a job level; demonstrate the behaviors in the [assessment rubric](handbook/mentoring-and-assessment.md).

## Useful references

- [Repository map](REPO-MAP.md): all 17 projects, their differences, and where to study them.
- [Foundations](handbook/foundations.md), [testing](handbook/testing.md), [debugging](handbook/debugging.md), [data and permissions](handbook/data-and-permissions.md), and [delivery](handbook/delivery.md).
- [Troubleshooting](onboarding/06-troubleshooting.md) and [glossary](handbook/glossary.md).
- [Reusable templates](templates/README.md) for PRs, stories, reviews, decisions, and learning notes.
- [Source audit](SOURCE-AUDIT.md): what was inspected and what has not been runtime-verified.

## Set up the workspace

> Status (2026-10-06): this repository is a standalone copy of the `astra/` folder in [elirc/gitvg](https://github.com/elirc/gitvg). Links to application source now point at each application's own repository (`github.com/elirc/<project>`), so they resolve from GitHub as well as locally.

The commands in this curriculum run from a **workspace root**: one folder holding this repository, cloned as `astra`, next to the application repositories you need. For the core path you need only Folio App:

```powershell
# Working directory: an empty folder of your choice; this becomes the workspace root
git clone https://github.com/elirc/gitvg-astra astra
git clone https://github.com/elirc/folio-app folio-app
```

Clone an elective's repositories the same way (for example `tracer-net` and `relay-app` for Module 13), using the folder names in the [repository map](REPO-MAP.md). The workspace root itself is not a Git repository, so never run `git add` from it. Keep all Astra learning materials under `astra`; make application exercises on a branch inside the relevant application repository.

To check the curriculum's local links and story structure, run `python astra/scripts/check_curriculum.py` from the workspace root. It requires only Python's standard library and does not run or change the applications.
