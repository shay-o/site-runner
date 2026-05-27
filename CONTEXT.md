# site-runner

A general-purpose tool that drives a real browser through a scripted path on a Site, captures everything that happens (screenshots, HTTP, WebSocket frames, console, dataLayer), and analyses the result for one of two purposes: assessing whether the Site is fit for its Purpose, or recording what usage-analytics data the Site emits.

The engine is site-agnostic. Each Site under review lives in its own workspace under `sites/<slug>/`. See [CONTEXT-MAP.md](./CONTEXT-MAP.md) once a second Site exists.

## Language

### Domain

**Site**:
A specific product under review, identified by a slug under `sites/`. Has its own Purpose, Journeys, Use Cases, Roles, and Criteria.
_Avoid_: App, platform, product, target.

**Tool**:
A named component within a Site (e.g. a Site might expose a "Scenario Builder" and a "Data Analysis" tool). Tools are traversed by Journeys; they are not the organising principle for review work. The vocabulary of Tools is site-specific and defined in each Site's CONTEXT.md.
_Avoid_: Feature, module, page.

**Use Case**:
A user need or job-to-be-done expressed in the user's own world, independent of any current Site implementation. Stable over time. A Use Case may be served by zero, one, or many Journeys.
_Avoid_: Requirement, feature request, user story.

**Journey**:
The specific path through a Site that accomplishes a single Use Case for a single Role. Authored as a YAML file under `sites/<slug>/journeys/`; the filename slug is the stable Journey ID used by both Reviews and usage analytics. Includes: Role, start state, ordered steps, success condition. One Journey serves exactly one Use Case and exactly one Role; one Use Case may have multiple Journeys (one per Role that needs a distinct path).
_Avoid_: Flow, workflow, path, action script.

**Role**:
A user-selectable UI state on the Site that affects what data and controls are exposed. The set of Roles is site-specific and declared in the Site's `roles.yaml`. Every Journey names exactly one Role. When a Site has no Role selector, it still declares a single implicit Role that all Journeys reference.
_Avoid_: User type, profile, mode.

**Persona**:
A specific job or identity within a Role (e.g. "Public Defender" within a "Legal" Role). Personas are illustrative descriptions for context — they are not selectable, and the engine does not switch on them.
_Avoid_: User type, segment.

**Unserved Use Case**:
A Use Case with zero Journeys — a user need the Site does not currently support. A first-class finding in Usability Review Reports, not an absence to be glossed over.
_Avoid_: Gap, missing feature.

### Review artifacts

**Purpose**:
A canonical written statement of what a Site should do and for whom, owned jointly by the consultant and the Site team. Lives at `sites/<slug>/purpose.md`. References Use Cases. Versioned with a date and changelog. Refining Purpose is itself a consulting deliverable. Tools do not have their own Purpose — a Tool's job is fully defined by the Journey steps that traverse it.
_Avoid_: Spec, requirements, brief.

**Criteria**:
A versioned set of review questions derived from a specific Purpose version and the Journeys it references, used to score a Site or a Tool. Each Criteria document records the Purpose version it was derived from and is human-reviewed before use.
_Avoid_: Heuristics, checklist, rubric.

**Run**:
A single execution of the engine against one Journey, capturing screenshots, network traffic, WebSocket frames, console, and dataLayer. Every Run has exactly one **Run Type** — either Usability Review or Analytics Data Collection — chosen at invocation time via `--type`. The Run Type determines which analysis pass runs and which Report is produced. The Journey YAML itself is type-agnostic; the same Journey can be executed under either Run Type.
_Avoid_: Session, scan, pass.

**Usability Review Run**:
A Run whose analysis pass evaluates the captured screenshots and step sequence against a specific Criteria version, producing a Usability Review Report. Infrequent and on-demand, typically after meaningful changes to a Site. A consulting deliverable.
_Avoid_: Review Run (ambiguous now that two types exist), UX run.

**Analytics Data Collection Run**:
A Run whose analysis pass decodes captured network beacons (GA4, Meta Pixel, Streamlit/Fivetran, etc.) into normalised events and produces an Analytics Data Collection Report. Factual rather than scored — it records what tracking data the Site actually generated for the Journey. Suitable for frequent, regression-oriented execution.
_Avoid_: Audit run, tracking run, analytics run (informal — use the full name in artifacts).

**Usability Review Report**:
The output of a Usability Review Run — a scored assessment against a specific Criteria version. Headers record the Criteria and Purpose versions. Reports are comparable across Runs only when they share a Criteria version. Unserved Use Cases are flagged explicitly.
_Avoid_: Audit, assessment, review document.

**Analytics Data Collection Report**:
The output of an Analytics Data Collection Run — a structured record of every decoded tracking event fired during the Journey, attributed to the step that triggered it, with any unknown beacons flagged. Comparable across Runs of the same Journey to detect tracking regressions.
_Avoid_: Tracking report, analytics report (informal — use the full name in artifacts).

**Criteria Refresh**:
The deliberate act of re-deriving Criteria from a new Purpose version. Starts a new regression-comparison baseline; prior Reports remain as historical context but are not diffed against post-refresh Reports.
_Avoid_: Reset, rebase.

### Review scope

**Site-level review**:
A Review whose scope is the whole Site — cross-Tool Journeys, global navigation, role selectors, AI assistants.
_Avoid_: Global review, overall review.

**Tool-level review**:
A Review scoped to a single Tool. Its Criteria are derived from the steps of every Journey that traverses the Tool — not from a Tool-specific Purpose.
_Avoid_: Module review, page review.

## Example dialogue

> **Consultant**: I want to add a Use Case — "compare two cohorts side by side." I don't think any current Journey serves it.
> **Team**: Agreed, that's unserved today. Should we add it to the Site Purpose anyway?
> **Consultant**: Yes — then the next Usability Review Run will flag it as an Unserved Use Case in the Report, and we have a record that we knew about it.
> **Team**: And when we build the path for it, we define a new Journey with a stable slug so an Analytics Data Collection Run can track its tracking from day one.
