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

Completed-entry guards:

- final arc or ending segment is finished
- required payoff tracker items are closed
- `longform-story-design` yields no valid next slice
- final batch QA has no critical unresolved failure

Run boundary:

- one run covers one state-machine transition for one active `3~5화` batch
- the only allowed adjacent pairs are `slice_planning -> drafting` and `qa_review -> ready_next_slice`
- do not expand a run beyond the current batch boundary
- if the next valid step would cross into a new batch, stop and hand off instead of continuing
- before and after specialist handoff, verify that `state/active-slice.yaml` matches `current_batch_start` and `current_batch_end`

Stop evidence:

- `state/runtime.yaml` records the completed transition, batch range, next state, next action, timestamp, and artifact pointer
- `state/handoff.md` records what finished, what artifact proves it, and where the next run resumes
- machine-checkable runtime fields are `last_completed_transition`, `last_artifact_pointer`, `last_proof_predicate`, and `specialist_return_accepted`
- `completed` and `blocked` require the exact predicate and proof artifact path before the run may stop
- after every specialist handoff, the state may advance only if required return evidence is present and matches the active batch
- missing, out-of-batch, future-batch, or schema-mismatched specialist returns must use `* -> blocked`

Mode-specific transition authority:

- `autonomous` may use `ready_next_slice -> slice_planning` after runtime and handoff files are updated
- `approval-gated` must use `ready_next_slice -> approval_waiting` and stop
- `approval-gated` may leave `approval_waiting` only after `last_approval_at` is recorded in `state/runtime.yaml` for the current batch and `approval_pending` is set to `false`
- neither mode may skip `qa_review` after drafting
