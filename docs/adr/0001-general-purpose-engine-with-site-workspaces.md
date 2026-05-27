# site-runner stays general-purpose; Sites live under `sites/<slug>/`

The engine (`src/runner/`) is site-agnostic. Each Site under review gets its own workspace at `sites/<slug>/` containing its Purpose, Journeys, Use Cases, Roles, Criteria, and Runs. The first Site is `sites/redoio/`.

The obvious alternative was to make this repo Redo.io-specific, since Redo.io is currently the only target. It was rejected because (a) the engine has no Redo.io-specific behaviour, (b) future Sites would either fork the repo or force a rename, and (c) keeping site-specific language (Roles, Tool names, Purpose copy) out of the engine code prevents drift between what the engine knows and what each Site cares about.
