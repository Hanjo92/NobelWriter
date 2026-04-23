---
name: series-completion-loop
description: Use when a Korean long-form project already has an explicit projects/<series-slug>/ runtime and must progress safely across sessions, automation runs, approval gates, QA recovery, or bounded 3~5화 batches.
---

# Series Completion Loop

## Overview
Use this skill as a state-based orchestrator for Korean long-form fiction completion. It reads runtime state, chooses the next valid transition, and delegates the actual work to specialist skills instead of replacing them.

## Entry Gate
Operate only on one explicit, pre-existing `projects/<series-slug>/` runtime selected by the user, automation prompt, or current runtime files.

- If no runtime is selected, stop and report the missing project runtime.
- If multiple runtimes are plausible, stop and report the ambiguity.
- Never infer project identity, batch scope, or story intent from chat context.
- Never draft, bootstrap, or create `projects/<series-slug>/` from implicit conversation context.
- Bootstrap means enriching an existing runtime, not inventing one.

## Hard Ownership
Use this skill when the task is to keep a series moving through a bounded loop across sessions, runs, or automation. Hand work off immediately when the current step belongs to a specialist:

- `longform-story-design` for series framing, macro planning, and slice definition
- `novel-writing` for scene and chapter prose
- `series-qa` for continuity, pacing, and serialization checks
- `character-voice-bible` for dialogue and cast voice control

Do not use this skill to write the whole series in one pass, redesign the story world, or perform specialist QA inline when the specialist skill should own the step.

## Specialist Handoff Contract
When delegating, pass only the current batch context:

- `project.md`
- `state/runtime.yaml`
- `state/active-slice.yaml`
- `state/handoff.md`
- relevant ledgers for the active transition
- the minimum current artifact required by the state, such as the latest manuscript batch for `qa_review`

The specialist owns the domain work product for the current state. The orchestrator may update only runtime, handoff, and artifact pointers afterward; it must not rewrite specialist output except to persist the returned artifact as-is.

Scope every delegated task to `current_batch_start` through `current_batch_end`. Do not include future-slice material. Before and after each handoff, verify that `state/active-slice.yaml` still matches the current manuscript batch. If the batch boundary moved or next-slice work was pulled forward, stop at `blocked` or re-enter from the last valid boundary.

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

## Stop Evidence
Do not stop a production run until `state/runtime.yaml` and `state/handoff.md` show:

- the completed transition
- `state`
- `next_action`
- `current_batch_start` and `current_batch_end`
- artifact paths created, reviewed, or accepted in the run
- `last_run_at`
- `last_completed_stage` or `blocked_reason`

When marking `completed` or `blocked`, name the exact predicate satisfied and the artifact path that proves it. If no proof exists, stay in the prior valid state or mark `blocked` rather than pretending the transition completed.

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
