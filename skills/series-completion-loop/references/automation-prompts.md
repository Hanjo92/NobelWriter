# Automation Prompts

## Production Run

- read `runtime.yaml`
- perform the next valid bounded action only
- update `handoff.md`
- stop

## Safety Run

- detect stalled `blocked`
- detect missing QA after drafting
- detect repeated recovery
- report only
- do not force progress
