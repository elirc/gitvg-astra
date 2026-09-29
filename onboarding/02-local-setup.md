# Run Folio App locally

These instructions target **`folio-app`**, not the separate TypeScript project named `folio`. Commands use PowerShell. Open each terminal at the workspace directory containing both `astra` and `folio-app`; replace the example absolute directory with your own checkout when needed.

## 1. Inspect the tools and project

```powershell
# Working directory: workspace root
git -C .\folio-app rev-parse --show-toplevel
git -C .\folio-app status --short
git --version
dotnet --list-sdks
node --version
pnpm.cmd --version
```

The project files target `net10.0`. The project README records .NET SDK 10.0.302, Node 22.x, and pnpm 9.x; these are the repository's documented versions, not a claim about the newest available releases. The inspected machine has .NET 10.0.302, Node 22.16.0, and pnpm 9.12.3. Match the project before considering an upgrade. `pnpm.cmd` avoids PowerShell blocking the `pnpm.ps1` launcher; on macOS/Linux use `pnpm`.

If a tool is missing, install the matching tool through your team's normal installation process, reopen the terminal, and repeat the version check. If pnpm is missing but npm works, `npm install --global pnpm@9.12.3` installs the course's recorded pnpm version. This is a machine-level setup step; it is not required when pnpm already works. Dependency downloads need network access the first time.

## 2. Restore and establish a baseline

```powershell
# Working directory: workspace root
dotnet restore .\folio-app\server\Folio.slnx
dotnet build .\folio-app\server\Folio.slnx --no-restore
dotnet test .\folio-app\server\Folio.slnx --no-build
```

Run each command after the preceding command succeeds. `--no-build` is appropriate here because you just built; omit it after changing code unless you build again. Tests create private in-memory SQLite databases and authenticate through the real API. They do not require a separately running server.

```powershell
# New terminal, initially at workspace root
Set-Location .\folio-app\client
pnpm.cmd install --frozen-lockfile
pnpm.cmd test
pnpm.cmd build
```

`test` runs Vitest once. `build` runs TypeScript and Vite. There is no `lint` script in this client's package manifest; do not copy another project's gate list. If frozen installation fails, record the error and inspect the manifest/lockfile pair before changing either. Use [baseline.md](../templates/baseline.md) to separate inherited failures from failures introduced by your patch.

## 3. Start the API

```powershell
# Terminal A, initially at workspace root
Set-Location .\folio-app\server
dotnet run --project Folio.Api --launch-profile http
```

Leave this terminal open. The checked-in `http` launch profile selects Development and listens on `http://localhost:5080`. Startup applies EF migrations and seeds the database in Development. The documented default database is `server/Folio.Api/folio.db`; the configured connection string controls the actual location. A launch error is not a successful setup.

## 4. Start the browser client

```powershell
# Terminal B, initially at workspace root
Set-Location .\folio-app\client
pnpm.cmd dev
```

Open `http://localhost:5173`. Vite forwards `/api` and `/health` to port 5080. Vite may choose another port if 5173 is occupied; read the terminal output and resolve the port conflict before assuming the documented URL is serving your process. The API's CORS configuration explicitly names the development origin.

## 5. Prove the API is responding

```powershell
# Terminal C; any directory
Invoke-RestMethod -Uri 'http://localhost:5080/health'
```

Expect an object with `status: ok`, `database: up`, and a timestamp. A 503 indicates a degraded database probe; a connection refusal means the process/port is unavailable. See [troubleshooting](06-troubleshooting.md).

## 6. Log in and inspect one request

All of these are local seed accounts with password `password`:

| Account | Role | Workspace |
| --- | --- | --- |
| `ada@acme.test` | Owner | Acme Docs |
| `grace@acme.test` | Editor | Acme Docs |
| `linus@acme.test` | Viewer | Acme Docs |
| `eve@globex.test` | Owner | Globex |

Log in as Ada. Create a page named `Astra practice`, add a paragraph, rename the page, and refresh. Open browser developer tools, select Network, and repeat the rename. Record the method, path, status, JSON fields, and initiating component. Keep the authorization header out of your notes.

Here is the equivalent server-only exercise in PowerShell:

```powershell
$folioBase = 'http://localhost:5080'
$folioLoginBody = @{ email = 'ada@acme.test'; password = 'password' } | ConvertTo-Json
$folioSession = Invoke-RestMethod -Method Post -Uri "$folioBase/api/auth/login" -ContentType 'application/json' -Body $folioLoginBody
$folioHeaders = @{ Authorization = "Bearer $($folioSession.token)" }
$folioWorkspace = '11111111-1111-1111-1111-111111111111'
$folioPageBody = @{ title = 'Astra API practice' } | ConvertTo-Json
$folioPage = Invoke-RestMethod -Method Post -Uri "$folioBase/api/workspaces/$folioWorkspace/pages" -Headers $folioHeaders -ContentType 'application/json' -Body $folioPageBody
$folioPage | Select-Object id, title, version
$folioRenameBody = @{ title = 'Astra renamed'; expectedVersion = $folioPage.version } | ConvertTo-Json
Invoke-RestMethod -Method Put -Uri "$folioBase/api/pages/$($folioPage.id)" -Headers $folioHeaders -ContentType 'application/json' -Body $folioRenameBody
```

The login result stays in a terminal variable; do not print the entire session. The rename response contains a new version. Reusing the original version for another rename should return 409. PowerShell reports non-success HTTP responses as errors; inspect the status and response rather than concluding that the request was never sent.

## 7. Stop and restart

Press Ctrl+C in the two running terminals. Start them again and verify your practice page persists. The browser development server and API are separate processes; stopping one does not stop the other. The test harness's in-memory database is separate from your development file.

For a fresh local seed, first stop the API and identify the actual configured database file. Back up or rename that specific file, then restart. Do not delete a directory, run a broad cleanup command, or reset a shared database. Details are in the troubleshooting guide.

Your setup is complete when the health probe works, login works, a change survives refresh/restart, and the baseline checks have recorded outcomes. Continue with [the code tour](03-code-tour.md).
