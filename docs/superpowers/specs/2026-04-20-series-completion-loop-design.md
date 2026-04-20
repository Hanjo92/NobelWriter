# Series Completion Loop Design

## Context

The current workspace already has strong specialist skills for long-form planning, prose drafting, QA diagnosis, and dialogue repair:

- `longform-story-design`
- `novel-writing`
- `series-qa`
- `character-voice-bible`

What it does not have yet is a reusable orchestration layer that can drive one project from premise to completion across many sessions and many automation runs.

The user wants a shared completion system for the whole repository, not a one-off workflow for one title. The system must support:

- long-running operation across many sessions
- a default execution unit of `3~5화`
- both `autonomous` and `approval-gated` operation
- scheduled automation that keeps progressing to the next batch
- safe pause, recovery, and re-entry when runs fail

The design must optimize for continuity, restart safety, and bounded execution rather than for one giant uninterrupted generation pass.

## Goal

Create a reusable series-completion system that can carry a Korean long-form project from bootstrap through repeated `3~5화` production loops until completion.

The system should:

1. orchestrate existing specialist skills instead of replacing them
2. externalize project state into files so work can resume after interruption
3. support both autonomous progression and approval-gated progression
4. run safely under scheduled automation
5. stop cleanly when recovery or human intervention is needed

## Decision

Use a state-based orchestration model with a new top-level shared skill tentatively named `series-completion-loop`.

This top-level skill does not become the new prose, planning, or QA expert. Instead, it:

- reads project state
- determines the next valid action
- dispatches work to the appropriate existing skill
- updates state files
- schedules or pauses the next run

This is preferred over a single giant all-in-one skill because:

- the repository already has good domain-specific boundaries
- restart safety depends on compact state files, not huge implicit context
- automation works better when each run performs one bounded transition or one small pair of transitions

## System Architecture

### Top-Level Orchestrator

Add one shared orchestration skill:

- `series-completion-loop`

Its responsibilities:

- read shared and per-project state
- decide the current state and next transition
- choose which specialist skill owns the next action
- write state updates and handoff artifacts
- enforce run boundaries and safety limits

### Existing Skill Ownership

- `longform-story-design`
  - bootstrap longform architecture
  - design the next active slice
  - perform structural recovery when QA shows long-range breakage
  - produce reusable recovery and re-entry planning artifacts

- `novel-writing`
  - draft the active `3~5화` batch
  - run `초고 -> 개고 -> 원고`
  - save manuscript-stage outputs into the existing draft folders

- `series-qa`
  - diagnose the latest finished batch
  - isolate the first break point and root cause
  - define directional repair guidance and handoff target
  - define re-audit gates

- `character-voice-bible`
  - run only when the issue is clearly dialogue-layer specific
  - repair cast voice separation, register, and spoken pressure

### Fixed Loop

The shared completion loop should follow this recurring order:

1. project bootstrap
2. next-slice planning
3. batch drafting
4. batch QA
5. recovery or continue
6. state update
7. schedule next run or wait for approval

The loop always operates on the current active batch, never on the whole series at once.

## Project State Layout

Each project gets a reusable runtime folder under:

- `projects/<series-slug>/`

Recommended contents:

- `projects/<series-slug>/project.md`
  - static project identity and high-level settings
  - genre, target scale, completion promise, mode
  - human-readable project summary

- `projects/<series-slug>/state/runtime.yaml`
  - current orchestration state
  - next action
  - mode: `autonomous` or `approval-gated`
  - approval pending flag
  - most recent run timestamp
  - failure counters
  - latest blocking reason

- `projects/<series-slug>/state/active-slice.yaml`
  - current `3~5화` batch scope
  - chapter range
  - purpose of the batch
  - success conditions
  - POV and active cast
  - explicit no-break constraints

- `projects/<series-slug>/state/handoff.md`
  - short operator note from the last finished step
  - what was completed
  - what failed
  - where the next run should resume

- `projects/<series-slug>/ledger/continuity.md`
- `projects/<series-slug>/ledger/knowledge-state.md`
- `projects/<series-slug>/ledger/payoff-tracker.md`

- `projects/<series-slug>/qa/latest-report.md`
  - most recent QA result

- `projects/<series-slug>/recovery/latest-recovery.md`
  - present only when active structural recovery exists

- `projects/<series-slug>/archive/runs/`
  - per-run snapshots and archived operator notes

### Separation Rule

Do not mix manuscript output and runtime state.

- manuscript stages continue to live in `drafts/초고`, `drafts/개고`, `drafts/원고`
- orchestration state lives under `projects/<series-slug>/...`

This separation keeps large manuscript text out of the minimal runtime context required for safe re-entry.

## State Machine

### States

- `bootstrap_pending`
  - project does not yet have sufficient longform design and baseline ledgers

- `slice_planning`
  - next `3~5화` active batch is being defined

- `drafting`
  - current batch is being written and staged

- `qa_review`
  - latest finished batch is being diagnosed

- `recovery_planning`
  - QA found structural or continuity damage that needs planning recovery

- `approval_waiting`
  - system is paused for user review

- `ready_next_slice`
  - current batch is accepted and the next batch may begin

- `completed`
  - series has reached its defined completion conditions

- `blocked`
  - automation or orchestration must stop until a problem is resolved

### State Transitions

- `bootstrap_pending -> slice_planning`
- `slice_planning -> drafting`
- `drafting -> qa_review`
- `qa_review -> ready_next_slice`
  - when the batch passes QA without requiring structural recovery

- `qa_review -> recovery_planning`
  - when QA shows continuity collapse, payoff failure, momentum collapse, or similar structural damage

- `recovery_planning -> drafting`
  - when the current active slice should be redrafted with repaired constraints

- `recovery_planning -> slice_planning`
  - when the next batch definition itself must be rebuilt before drafting

- `ready_next_slice -> approval_waiting`
  - when mode is `approval-gated`

- `ready_next_slice -> slice_planning`
  - when mode is `autonomous`

- any state -> `blocked`
  - when safety rules or required state integrity fail

- final accepted batch -> `completed`

### Run Boundary Rule

One automated run should perform only one bounded action or at most one safe pair of adjacent actions.

Examples:

- `slice_planning -> drafting`
- `qa_review -> ready_next_slice`

Avoid long multi-stage autonomous runs that try to consume the whole loop at once. Restart safety matters more than per-run throughput.

## Modes

### Autonomous

In `autonomous` mode:

- accepted QA results allow the system to continue toward the next slice without waiting for a human
- automation may keep scheduling the next bounded run
- safety limits still apply

### Approval-Gated

In `approval-gated` mode:

- the system pauses after a completed batch or other configured checkpoint
- `runtime.yaml` enters `approval_waiting`
- automation must stop progressing and only surface waiting status
- explicit approval reactivates the next transition

## Automation Model

Use scheduled automation per project rather than one global unbounded writing prompt.

### Production Automation

Purpose:

- read current runtime state
- perform the next valid bounded action
- update runtime and handoff files

Suggested behavior:

- if `slice_planning`, update `active-slice.yaml` and stop
- if `drafting`, produce the current batch and stop
- if `qa_review`, diagnose only the newest batch and stop
- if `recovery_planning`, produce the recovery artifact needed for the next step and stop

### Safety Automation

Purpose:

- detect stalled or unsafe runtime conditions
- report them without forcing progress

Examples:

- runtime stuck in `blocked` too long
- drafting files changed but QA did not run afterward
- recovery has repeated without clearing
- approval-gated project is waiting indefinitely

### Automation Prompt Rule

Automation prompts must be narrow.

Good pattern:

- read current state
- perform the next action only
- update runtime files
- stop

Bad pattern:

- keep writing until the series is done
- continue the story as long as possible
- do everything needed automatically

## Failure Recovery And Re-Entry

### Snapshot Rule

Before each run, archive the current orchestrator state:

- `runtime.yaml`
- `active-slice.yaml`
- `handoff.md`

Store snapshots in:

- `projects/<series-slug>/archive/runs/<timestamp>/`

### Failure Handling Rule

Do not treat failure as a reason to erase manuscript output.

Instead:

- preserve already-written draft files
- mark state as `blocked` or return to the last safe state
- record the failure in `handoff.md`
- require a clean next entry point

### Immediate Block Conditions

Force `blocked` when:

- required state files are missing
- state files contradict each other
- same slice fails QA repeatedly
- structural recovery is required multiple times in a row
- active slice and actual manuscript range diverge
- approval-gated mode attempts to progress without approval
- completion conditions are still undefined but next-slice generation continues

### Re-Entry Rules

- if `blocked`
  - a human or recovery run must resolve the cause and explicitly set the next state

- if `approval_waiting`
  - approval resumes from the existing active slice, not from a newly inferred one

- if `drafting` failed
  - evaluate whether the saved manuscript stages can continue or should move to QA or recovery

- if `qa_review` failed
  - preserve the QA artifact and route only to `recovery_planning` or bounded redraft

- if `recovery_planning` failed
  - do not generate a new slice; remain blocked until recovery state is repaired

## Completion Conditions

A project may enter `completed` only when all of these are true:

- final arc or ending segment is finished
- required payoff tracker items are closed
- `longform-story-design` no longer yields a valid next slice
- final batch QA shows no critical unresolved failure

## Safety Philosophy

This system is not a limitless “keep generating forever” engine.

It is a reusable completion loop that:

- keeps bounded context
- externalizes continuity-critical state
- survives interruption
- resumes safely
- progresses in repeatable batches until the series is complete

## Proposed Deliverables

This design implies the following future implementation units:

1. new shared skill: `series-completion-loop`
2. shared templates for `runtime.yaml`, `active-slice.yaml`, and `handoff.md`
3. project runtime folder convention under `projects/<series-slug>/`
4. automation prompt(s) for production and safety runs
5. documentation for autonomous and approval-gated operation

## Acceptance Criteria

The system should satisfy all of these:

1. One repository-level completion system can be reused across multiple series projects.
2. The default execution unit is a `3~5화` batch.
3. Both `autonomous` and `approval-gated` modes are supported.
4. Automation runs can resume from file state without relying on long implicit chat context.
5. A failed run leaves the project in a restartable state without corrupting manuscript output.
6. The orchestrator delegates specialist work instead of absorbing the responsibilities of all existing skills.
