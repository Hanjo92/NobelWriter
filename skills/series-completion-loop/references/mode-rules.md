# Mode Rules

## Autonomous

- continue automatically after accepted QA
- update the runtime state and handoff artifacts before stopping

## Approval-Gated

- stop in `approval_waiting`
- require explicit user approval before moving to the next slice
- do not advance past `approval_waiting` on your own
