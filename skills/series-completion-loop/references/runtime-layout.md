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

Selection rule:

- operate only on one explicit, pre-existing `projects/<series-slug>/` runtime
- do not infer the slug, project identity, or batch scope from chat context
- do not create project runtime folders, state files, or ledgers unless the user explicitly requested project setup outside this loop

Separation rule:

- manuscript stays in `drafts/`
- runtime state stays in `projects/`

Touching rule:

- only touch the current runtime/project references needed for the active transition
- do not reach into unrelated project artifacts or manuscript files from the orchestrator

## Transition Ownership Matrix

Use this as the default read/write boundary. Specialist skills may write their own outputs, but the orchestrator should only touch these runtime files directly.

Delegation rule:

- pass only current-batch runtime context to specialist skills
- specialists own prose, QA, dialogue, design, and recovery artifacts
- after a specialist returns, the orchestrator updates only runtime, handoff, and artifact pointers
- if specialist work would require the next batch, stop and hand off instead of extending scope

| State | Read | Write |
| --- | --- | --- |
| `bootstrap_pending` | `project.md`, `state/runtime.yaml` | `state/runtime.yaml`, `state/handoff.md`, baseline ledger files |
| `slice_planning` | `project.md`, `state/runtime.yaml`, ledgers, `qa/latest-report.md`, `recovery/latest-recovery.md` | `state/active-slice.yaml`, `state/runtime.yaml`, `state/handoff.md` |
| `drafting` | `state/runtime.yaml`, `state/active-slice.yaml`, `state/handoff.md` | `state/runtime.yaml`, `state/handoff.md` |
| `qa_review` | `state/runtime.yaml`, `state/active-slice.yaml`, latest manuscript batch | `qa/latest-report.md`, `state/runtime.yaml`, `state/handoff.md` |
| `recovery_planning` | `project.md`, `state/runtime.yaml`, `state/active-slice.yaml`, ledgers, `qa/latest-report.md` | `recovery/latest-recovery.md`, affected ledgers, `state/runtime.yaml`, `state/handoff.md` |
| `approval_waiting` | `project.md`, `state/runtime.yaml`, `state/handoff.md` | `state/runtime.yaml`, `state/handoff.md` only after explicit approval |
| `ready_next_slice` | `state/runtime.yaml`, `qa/latest-report.md`, `state/handoff.md` | `state/runtime.yaml`, `state/handoff.md` |
| `completed` | `project.md`, `state/runtime.yaml`, ledgers, `qa/latest-report.md` | `state/runtime.yaml`, `state/handoff.md` |
| `blocked` | `state/runtime.yaml`, `state/handoff.md`, relevant failure artifact | `state/runtime.yaml`, `state/handoff.md` only when recording the block reason |
