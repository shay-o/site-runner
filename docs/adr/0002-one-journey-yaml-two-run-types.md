# One Journey YAML serves both Run Types; `--type` selects the analysis pass

A Journey YAML is type-agnostic: it describes a path through a Site (Role, steps, success condition) without committing to how the resulting Run will be analysed. The Run Type — Usability Review or Analytics Data Collection — is chosen at invocation time via `--type`, and only the post-capture analysis pass differs between the two.

The obvious alternative was to have separate "usability journey" and "analytics journey" files (or separate top-level YAML fields). It was rejected because the actual browser driving is identical for both purposes — the same clicks produce both the screenshots a Usability Review needs and the network beacons an Analytics Data Collection Run decodes. Splitting at the YAML level would force every Journey to be authored (and kept in sync) twice for no behavioural difference.
