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

Run boundary:

- one run covers one state-machine transition for one active `3~5화` batch, or one safe adjacent pair that stays within the same bounded batch
- do not expand a run beyond the current batch boundary
- if the next valid step would cross into a new batch, stop and hand off instead of continuing
