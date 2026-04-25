# Series Completion Loop for GPT-OSS

## Source

- 원본: `skills/series-completion-loop/SKILL.md`

## Overview

Use this skill only when a Korean long-form project already has an explicit `projects/<series-slug>/` runtime and the user wants the next safe completion-loop transition.

This is the orchestration layer, not a prose, planning, QA, or dialogue layer. It reads runtime state, chooses the next valid bounded move, delegates specialist work, validates the return evidence, and records the state update.

## Entry Gate

Proceed only if exactly one existing project runtime is explicit in the request or current runtime files.

- If no runtime is selected, stop and report the missing `projects/<series-slug>/` path.
- If multiple runtimes are plausible, stop and report the ambiguity.
- Do not infer project identity, batch scope, or story intent from chat context.
- Do not create, bootstrap, or enrich a runtime unless the user explicitly requested setup outside this loop.

## Specialist Ownership

Delegate domain work instead of doing it inline:

- `longform-story-design` for slice planning, macro planning, and recovery planning
- `novel-writing` for current-batch scene or chapter prose
- `series-qa` for continuity, pacing, serialization, and payoff checks
- `character-voice-bible` for dialogue and cast voice repair

Scope every handoff to `current_batch_start` through `current_batch_end`. Do not include next-batch work.

## Valid Loop Order

Follow runtime state. When state is missing, use this order:

1. Bootstrap
2. Slice planning
3. Drafting
4. QA
5. Recovery or continue
6. State update
7. Schedule or wait

Each run should advance only one state-machine transition for one active 3~5화 batch, or one explicitly safe adjacent pair such as `slice_planning -> drafting` or `qa_review -> ready_next_slice`.

## Required Runtime Files

Read and update only the relevant files under the selected runtime:

- `project.md`
- `state/runtime.yaml`
- `state/active-slice.yaml`
- `state/handoff.md`
- `ledger/continuity.md`
- `ledger/knowledge-state.md`
- `ledger/payoff-tracker.md`
- `qa/latest-report.md`
- `recovery/latest-recovery.md`

Manuscript text stays outside runtime state.

## Stop Conditions

Stop rather than continuing when:

- the runtime is missing or ambiguous
- required state files or keys are absent
- state files contradict one another
- approval is required but not recorded
- specialist return evidence is missing, out of batch, future-batch, schema-mismatched, or semantically invalid
- the next valid action would cross into a new batch

When stopping as blocked, record the exact blocked reason and proof artifact path when file writing is available. If file writing is unavailable, report what should be recorded.

## Output Rule

Return a compact run report:

- selected runtime
- starting state and batch
- transition attempted
- specialist handoff target
- evidence accepted or blocked reason
- updated state and next action

Do not write prose directly from this layer. If drafting is needed, hand off to `novel-writing`.
