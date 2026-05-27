# site-runner

Drive a Site through a Journey, capture everything the browser sees (screenshots, HTTP, WebSocket frames, console, dataLayer), and analyse the result for one of two purposes:

1. **Usability Review** — does the Site let a user accomplish the Journey? (consulting deliverable)
2. **Analytics Data Collection** — what tracking data does the Site emit during the Journey? (regression-style audit)

See [CONTEXT.md](CONTEXT.md) for the project's language and [ARCHITECTURE.md](ARCHITECTURE.md) for design details.

## Quickstart

```bash
# One-time setup
uv venv
source .venv/bin/activate
uv pip install -e .
playwright install chromium

# Record a Journey interactively (opens a browser, close it when done)
site-runner record https://tool.redoio.info/ sites/redoio/journeys/my-flow.yaml --role legal

# Run a Journey as an Analytics Data Collection Run (the default Run Type)
site-runner run sites/redoio/journeys/bias_analysis.yaml

# Run a Journey as a Usability Review Run (analysis pass not yet implemented)
site-runner run sites/redoio/journeys/bias_analysis.yaml --type usability

# Output appears under sites/<slug>/runs/<journey>_<run-type>_<timestamp>/
```

## Repo layout

```
site-runner/
├── CONTEXT.md              ← general glossary (Journey, Run, Criteria, etc.)
├── ARCHITECTURE.md         ← engine architecture
├── docs/adr/               ← decisions about the engine
├── src/runner/             ← engine code (site-agnostic)
└── sites/
    └── redoio/
        ├── CONTEXT.md      ← site-specific language (Roles, Tools)
        ├── purpose.md      ← what the Site is for, and for whom
        ├── roles.yaml
        ├── journeys/       ← Journey YAMLs; filename slug = Journey ID
        ├── use-cases/
        ├── criteria/
        ├── runs/           ← Run artifacts (gitignored)
        └── docs/adr/       ← decisions specific to this Site's review
```

## Authoring a Journey

A Journey YAML names a Role, references a Use Case (optional for now), declares a `success_condition`, and lists ordered steps. Filename stem must match the `journey:` slug.

```yaml
journey: bias_analysis
role: legal
use_case: null
start_url: https://tool.redoio.info/bias_analysis
success_condition:
  description: Bias Analysis Report renders for the chosen cohort and ethnic groups.
  check:
    type: selector_visible
    selector: 'text=Bias Analysis Report'
steps:
  - id: ...
```

`success_condition.description` is required and is human-readable. `success_condition.check` is optional — when present, the runner evaluates it at the end of the Run and records the result in `run.json`.

## Recording tips

**Prefer sidebar / persistent navigation over inline recommendation links.**
Links inside AI-generated or dynamic content (e.g. `st.page_link` widgets that appear after a query) may not be present on every replay. Use sidebar nav links or add a `goto` step directly:

```yaml
- id: open_bias_analysis
  action: goto
  url: https://tool.redoio.info/bias_analysis
  wait_for: load
  settle: {wait_ms: 2000}
```

**After recording, review the YAML before running.** Step IDs and locators are editable — if a locator looks fragile (e.g. a CSS fallback like `css: div > span:nth-of-type(3)`), replace it with a more stable one. The recorder writes a placeholder `success_condition.description` — fill it in.

## Troubleshooting

**`ModuleNotFoundError: No module named 'runner'`**
macOS marks `.pth` files created by `uv` as hidden, and Python 3.12+ skips them. If you see this error after `uv pip install -e .`, run:
```bash
chflags -R nohidden .venv
```

## Status

Phase 1 (MVP) — recorder + runner + capture pipeline. Analytics Data Collection Runs capture artifacts; no decoder or LLM report yet. Usability Review Runs capture artifacts but the analysis pass is stubbed.

Open issues: [github.com/shay-o/Automated-Web-Tracking-Analysis/issues](https://github.com/shay-o/Automated-Web-Tracking-Analysis/issues)
