# Failure And Re-entry

Snapshot before each run:

- `state/runtime.yaml`
- `state/active-slice.yaml`
- `state/handoff.md`

Block conditions:

- missing state
- contradictory state
- same slice QA fails twice without a changed repair direction
- recovery runs twice without changing `active-slice.yaml` or the recovery artifact
- approval bypass in `approval-gated` mode

Recovery rules:

- preserve manuscript files
- never auto-roll back manuscript output
- re-enter only from the last valid boundary after the runtime snapshot is available
