# Site — Redo.io

The Redo.io product at `tool.redoio.info`, a free AI-assisted platform for exploring and generating insights about the California prison population. This file holds language specific to Redo.io. General terms (Journey, Run, Use Case, Criteria, etc.) live in the [root CONTEXT.md](../../CONTEXT.md).

## Language

### Site vocabulary

**Tool** (Redo.io):
A named component within the Site accessed from the shared sidebar. Current Tools include Scenario Builder, Data Analysis, Case Explorer, Bias Analysis, Justice Reform Q&A, and Custom Query. The canonical list is whatever the live left nav exposes.
_Avoid_: Feature, module, page.

**Role** (Redo.io):
The three values selectable from the Role selector in the left nav — **Technical**, **Legal**, **General** — plus the implicit default Role used by Journeys traversing Tools where the selector is absent (see [open question 4 in purpose.md](./purpose.md)). The selectable values are declared in [roles.yaml](./roles.yaml).
_Avoid_: User type, profile, mode.

**Persona** (Redo.io):
A specific job under a Role, illustrative only. Examples surfaced by the Site's Role selector:
- **Legal** — Public Defender, District Attorney, Paralegal, Legal Assistant
- **Technical** — Data Scientist, Engineer, Analyst
- **General** — Journalist, Academic Researcher, Community Advocate

The Site's About section names a narrower set — district attorneys, public defenders, academic researchers — and reconciling the two lists is an open question (see [open question 2 in purpose.md](./purpose.md)).

### Site-specific findings

**"Start here" contradiction**:
The homepage tags Scenario Builder as the entry point; the left nav's "How to Use" lists Dashboard + Data Analysis first. Tracked as [open question 1 in purpose.md](./purpose.md). Journeys must commit to one entry-point mental model and the choice should be recorded as a finding.

**Role-selector inconsistency**:
The Role selector is present on some Tools and absent from others. Whether this is intentional, legacy, or a bug is [open question 3 in purpose.md](./purpose.md). Affects how Journeys through selector-less Tools declare their Role (see [ADR-0001](./docs/adr/0001-three-layer-purpose-criteria-report-stack.md) and the implicit-default-Role rule in the [root CONTEXT.md](../../CONTEXT.md)).

## Notes on the engine

- Redo.io is Streamlit-based. All app behaviour flows over a persistent WebSocket (`wss://tool.redoio.info/_stcore/stream`) carrying binary protobuf. Internal navigation does **not** issue HTTP requests — it sends WebSocket frames. Journeys cannot rely on `networkidle` settles; use `wait_for_selector` or `wait_ms`.
- The only telemetry is JSON POSTs to `webhooks.fivetran.com/webhooks/<id>` (event types: `viewReport`, `updateReport`, `pageProfile`). No GA4, GTM, or Meta Pixel. Analytics Data Collection Runs against Redo.io exercise the Streamlit/Fivetran decoder, not the e-com decoders.
- The `pageProfile` beacon includes an `isWebdriver` field. The engine launches Chromium with `--disable-blink-features=AutomationControlled` and hides `navigator.webdriver` so captured beacons report `isWebdriver: false` and don't pollute the Site's own telemetry.
- Redo.io has no consent banner. Journeys default `consent.strategy: ignore`.
