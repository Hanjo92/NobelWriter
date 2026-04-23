# Runtime Layout

Runtime files live under `projects/<series-slug>/` and are the only project-scoped orchestration artifacts this loop should read or update:

- `projects/<series-slug>/project.md`
- `projects/<series-slug>/state/runtime.yaml`
- `projects/<series-slug>/state/active-slice.yaml`
- `projects/<series-slug>/state/handoff.md`
- `projects/<series-slug>/ledger/continuity.md`
- `projects/<series-slug>/ledger/knowledge-state.md`
- `projects/<series-slug>/ledger/payoff-tracker.md`
- `projects/<series-slug>/qa/latest-report.md`
- `projects/<series-slug>/recovery/latest-recovery.md`
- `projects/<series-slug>/archive/runs/`

Separation rule:

- manuscript stays in `drafts/`
- runtime state stays in `projects/`

Touching rule:

- only touch the current runtime/project references needed for the active transition
- do not reach into unrelated project artifacts or manuscript files from the orchestrator
