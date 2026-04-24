# Projects Runtime Layout

Use `projects/<series-slug>/` for orchestrator state, not manuscript text.

Required subfolders:
- `state/`
- `ledger/`
- `qa/`
- `recovery/`
- `archive/runs/`

Runtime stop evidence is recorded in `state/runtime.yaml` and summarized in `state/handoff.md`.
Specialist return evidence should stay machine-checkable enough for `series-completion-loop` to accept or block the next transition.
Fresh template copies start with empty batch fields. Until `current_batch_start`, `current_batch_end`, and `state/active-slice.yaml` are populated, block as missing state rather than judging specialist output against an invented batch.

Manuscript files stay in `drafts/`.
