# Automation Prompts

## Production Run

- read `runtime.yaml`
- perform the next valid bounded action only
- update `state/runtime.yaml`
- update `state/handoff.md`
- stop

Required closing fields:

- `state`
- `next_action`
- `last_run_at`
- `last_completed_stage` or `blocked_reason`

## Safety Run

- detect stalled `blocked`
- detect missing QA after drafting
- detect repeated recovery
- report only
- do not force progress

Safety runs may write only a status note to `state/handoff.md` unless they are marking an already-detected unsafe condition as `blocked` in `state/runtime.yaml`.
