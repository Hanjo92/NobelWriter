# Automation Prompts

## Production Run

- resolve exactly one selected `projects/<series-slug>/` runtime
- if no runtime is selected, report missing runtime only
- if multiple runtimes are plausible, report ambiguity only
- read `state/runtime.yaml`
- perform the next valid bounded action only
- never draft, bootstrap, or reconstruct state from chat context
- after any specialist handoff, validate required return evidence before updating runtime
- if specialist evidence is missing, out of batch, future-batch, or schema-mismatched, set `state: blocked` with `blocked_reason`; report only when the selected runtime cannot be safely written
- update `state/runtime.yaml`
- update `state/handoff.md`
- stop

Required closing fields:

- `state`
- `next_action`
- `current_batch_start`
- `current_batch_end`
- `last_run_at`
- artifact path or reviewed artifact path
- specialist return evidence accepted, or blocked mismatch evidence
- `last_completed_transition`
- `last_artifact_pointer`
- `last_proof_predicate`
- `specialist_return_accepted`
- `last_completed_stage` or `blocked_reason`

## Safety Run

- detect stalled `blocked`
- detect missing QA after drafting
- detect repeated recovery
- mark `state: blocked` when a block condition has exact evidence
- report only when the selected runtime is missing, ambiguous, or not safely writable
- do not force progress

Safety runs may write only the minimal `state/runtime.yaml` and `state/handoff.md` evidence needed to record `blocked`; otherwise they must report without changing project state.
