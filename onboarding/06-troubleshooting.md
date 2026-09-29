# Troubleshoot one boundary at a time

Start with the first actionable error and the last working boundary. Record the directory, command, expected result, actual result, and one hypothesis. Change one thing, then repeat the same check. Do not reinstall all tools as a first response.

| Symptom | Check | Likely next action |
| --- | --- | --- |
| Git lists files outside the app | `git rev-parse --show-toplevel` | Move into the intended nested repository or use `git -C` |
| `net10.0` is unsupported | `dotnet --list-sdks` | Install/select the SDK required by the project; do not retarget the app to bypass setup |
| NuGet restore fails | First failed feed/package and network error | Verify feed access and proxy; keep original error evidence |
| `pnpm.ps1` cannot execute | `pnpm.cmd --version` | Use the `.cmd` launcher; a machine-wide policy change is unnecessary |
| Frozen lockfile install fails | `package.json`, `pnpm-lock.yaml`, pnpm version | Determine whether versions or committed files disagree before regenerating anything |
| API connection refused | API terminal, listening URL, `/health` | Start the API or resolve its startup error |
| Port already in use | `Get-NetTCPConnection -LocalPort 5080 -ErrorAction SilentlyContinue` | Identify the owning process before stopping it; stop only your known dev process |
| Browser page loads but API calls fail | Network request path/status; Vite proxy target | Run both processes and use the documented development origin |
| Vite serves port 5174 | Startup output and port 5173 owner | Stop the known conflicting dev process or deliberately align origin/proxy configuration |
| Login returns 401 | Seed email/password, environment, database | Use local seed credentials; verify Development seeding actually ran |
| UI returns to login | The first 401 response; `AuthContext` | Log in again; inspect session lifecycle if it immediately recurs |
| Viewer cannot rename | Role and share permission | This can be expected behavior; reproduce as Owner and inspect the permission matrix |
| Foreign page returns 404 | Caller workspace and page workspace | Expected existence-hiding behavior, even if the id is valid |
| Rename returns 409 | Sent `expectedVersion` versus last read version | Reload current state and preserve the user's proposed text; do not blindly retry stale writes |
| Write returns 429 | `Program.cs` rate-limit configuration | Wait for the configured window; distinguish rate limiting from authorization |
| Migration guard fails | Entity change, snapshot, migration diff | Generate/review the missing migration; do not replace `Migrate` with `EnsureCreated` |
| SQLite is locked | Running writers, DB browser, debugger transaction | Close the known connection or finish the transaction; do not delete the live file |
| Test passes alone but fails in suite | Shared factory, global fetch/session stubs | Restore isolation and cleanup; do not add arbitrary sleeps |
| Frontend test passes, browser fails | Mock route/payload versus Network response | Verify the actual contract and proxy; mocks cannot establish live integration |
| Build fails after successful tests | TypeScript diagnostic and import path | Fix the contract/type error; tests and compilation catch different problems |

## Reset only a disposable development database

Confirm the API is stopped. Read the effective `ConnectionStrings:Folio` value and locate that exact file. The documented default is `folio-app/server/Folio.Api/folio.db`, but an environment override can change it. Back up the resolved file to a specifically named local backup before restarting against a new file. If SQLite journal/WAL files exist, make a consistent backup with all connections closed rather than copying a live database piecemeal. Never use recursive deletion as a schema repair strategy.

Database reset is for disposable seed data. When testing a migration, preserve the pre-change database and prove the upgrade works on it. Resetting to an empty database would erase the scenario you are supposed to verify.

## Escalate with a useful report

Use this shape: "From `folio-app/client`, `pnpm.cmd build` fails with diagnostic X in file Y. The same checkout's client tests pass. I verified the pnpm version and reproduced after restarting the terminal. I suspect the renamed response field disagrees with `types.ts`. Here is the smallest diff."

Avoid a raw dump of every log. Include the first meaningful failure, a minimal reproduction, and the question you need answered. See the [debugging handbook](../handbook/debugging.md) for a complete worked investigation.
