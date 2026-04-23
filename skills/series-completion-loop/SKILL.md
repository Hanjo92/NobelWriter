---
name: series-completion-loop
description: Use when a Korean long-form project must keep progressing toward completion across many sessions or automation runs by moving the next valid 3~5화 batch through planning, drafting, QA, recovery, and state updates.
---

# Series Completion Loop

## Overview
Use this skill as a state-based orchestrator for Korean long-form fiction completion. It reads runtime state, chooses the next valid transition, and delegates the actual work to specialist skills instead of replacing them.

## Hard Ownership
Use this skill when the task is to keep a series moving through a bounded loop across sessions, runs, or automation. Hand work off immediately when the current step belongs to a specialist:

- `longform-story-design` for series framing, macro planning, and slice definition
- `novel-writing` for scene and chapter prose
- `series-qa` for continuity, pacing, and serialization checks
- `character-voice-bible` for dialogue and cast voice control

Do not use this skill to write the whole series in one pass, redesign the story world, or perform specialist QA inline when the specialist skill should own the step.

## Canonical Loop Order
Follow this order unless runtime state says a different valid transition is needed:

1. Bootstrap
2. Slice planning
3. Drafting
4. QA
5. Recovery or continue
6. State update
7. Schedule or wait

Each run should advance only the next valid 3~5화 batch, never the full series.

## Runtime Files
Read and update the project runtime files that govern the loop:

- `project.md`
- `state/runtime.yaml`
- `state/active-slice.yaml`
- `state/handoff.md`
- `ledger/continuity.md`
- `ledger/knowledge-state.md`
- `ledger/payoff-tracker.md`
- `qa/latest-report.md`
- `recovery/latest-recovery.md`

Treat manuscript output as separate from runtime state. Keep the draft in manuscript storage and keep orchestration decisions in the runtime files. Do not touch other project artifacts unless `project.md` or `state/runtime.yaml` explicitly names them as part of the current transition.

## States And Transitions
Use these states as the canonical loop states:

- `bootstrap_pending`
- `slice_planning`
- `drafting`
- `qa_review`
- `recovery_planning`
- `approval_waiting`
- `ready_next_slice`
- `completed`
- `blocked`

Main transitions:

- `bootstrap_pending -> slice_planning`
- `slice_planning -> drafting`
- `drafting -> qa_review`
- `qa_review -> ready_next_slice`
- `qa_review -> recovery_planning`
- `recovery_planning -> drafting`
- `recovery_planning -> slice_planning`
- `ready_next_slice -> approval_waiting`
- `ready_next_slice -> slice_planning`
- final accepted batch -> `completed`
- any state -> `blocked` when the runtime is contradictory, missing, or repeatedly failing

Enter `completed` only when the final arc or ending segment is finished, payoff tracker items are closed, `longform-story-design` yields no valid next slice, and final batch QA has no critical unresolved failure.

## Mode Rules
Support two operating modes:

- `autonomous`: continue automatically after accepted QA, then update state and move to the next valid slice
- `approval-gated`: stop in `approval_waiting` after a valid slice is ready, and wait for explicit approval recorded in `state/runtime.yaml` before continuing

Mode choice affects when the loop stops, not the specialist work delegated within the run.

## Run Boundary Rules
Keep every run tightly bounded:

- A run means one state-machine transition for one active `3~5화` batch, or one explicitly safe adjacent pair such as `slice_planning -> drafting` or `qa_review -> ready_next_slice`.
- Do one bounded action or one safe adjacent pair only
- Never attempt the entire series in one run
- Never replace specialist skills with a full manual rewrite
- Stop once the next valid transition is complete and the handoff files are updated

## Failure And Re-entry
Before each run, snapshot the current runtime state so re-entry is possible. At minimum, archive:

- `state/runtime.yaml`
- `state/active-slice.yaml`
- `state/handoff.md`

Preserve manuscript output even when state changes or recovery is needed.

Block the run when:

- the state files contradict each other
- a required runtime file is missing
- QA fails twice on the same slice without a changed repair direction
- recovery runs twice in a row without changing `state/active-slice.yaml` or `recovery/latest-recovery.md`
- approval is bypassed in `approval-gated` mode

On re-entry, set the next state explicitly, keep the manuscript intact, and continue only from the last valid boundary.
