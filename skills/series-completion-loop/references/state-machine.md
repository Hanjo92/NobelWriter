# State Machine

States:

- `bootstrap_pending`
- `slice_planning`
- `drafting`
- `qa_review`
- `recovery_planning`
- `approval_waiting`
- `ready_next_slice`
- `completed`
- `blocked`

Transitions:

- `bootstrap_pending -> slice_planning`
- `slice_planning -> drafting`
- `drafting -> qa_review`
- `qa_review -> ready_next_slice`
- `qa_review -> recovery_planning`
- `recovery_planning -> drafting`
- `recovery_planning -> slice_planning`
- `ready_next_slice -> approval_waiting`
- `ready_next_slice -> slice_planning`
- `final accepted batch -> completed`
- `* -> blocked`

Use the canonical wildcard form `* -> blocked` for every safety stop. Do not rewrite it as `any state -> blocked` in runtime or handoff notes.

Run boundary:

- one run covers one state-machine transition for one active `3~5화` batch
- the only allowed adjacent pairs are `slice_planning -> drafting` and `qa_review -> ready_next_slice`
- do not expand a run beyond the current batch boundary
- if the next valid step would cross into a new batch, stop and hand off instead of continuing

Mode-specific transition authority:

- `autonomous` may use `ready_next_slice -> slice_planning` after runtime and handoff files are updated
- `approval-gated` must use `ready_next_slice -> approval_waiting` and stop
- `approval-gated` may leave `approval_waiting` only after explicit approval is recorded in `state/runtime.yaml`
- neither mode may skip `qa_review` after drafting
