# Automation Prompts

## Production Run

- resolve exactly one selected `projects/<series-slug>/` runtime
- if no runtime is selected, report missing runtime only
- if multiple runtimes are plausible, report ambiguity only
- read `state/runtime.yaml`
- perform the next valid bounded action only
- never draft, bootstrap, or reconstruct state from chat context
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
- `last_completed_stage` or `blocked_reason`

## Safety Run

- detect stalled `blocked`
- detect missing QA after drafting
- detect repeated recovery
- report only
- do not force progress

Safety runs may write only a status note to `state/handoff.md` unless they are marking an already-detected unsafe condition as `blocked` in `state/runtime.yaml`.
