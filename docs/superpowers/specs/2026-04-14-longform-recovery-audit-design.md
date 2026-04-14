# Longform Recovery Audit Skill Reinforcement

## Context

`longform-story-design` is already strong for greenfield planning, but it is weak when the user brings a damaged long-running draft and expects both diagnosis and reconstruction in one pass. Right now the main skill distributes decisions across intake, package choice, risk choice, stack choice, and output depth without a single controlling order. That makes `audit + repair` requests inconsistent.

The adjacent `series-qa` skill also overlaps with diagnosis, which creates routing ambiguity: a user can describe a broken serial and either skill could plausibly answer.

## Goal

Reinforce `longform-story-design` so it becomes the primary skill for long-form Korean fiction requests that need structural audit plus recovery planning across many chapters, arcs, or volumes.

Keep `series-qa` as the lighter diagnostic skill for quick QA, narrow-range audits, and ranked issue reports that do not need a rebuild package.

## Decision

Use a layered integration model:

1. `longform-story-design` handles long-range `audit + recovery`.
2. `series-qa` handles `fast diagnosis`, `range-limited QA`, and `issue-first reporting`.
3. The deciding factor is not whether diagnosis is present, but whether the requested output must become a reusable reconstruction package.

## Scope

### Files to update

- `skills/longform-story-design/SKILL.md`
- `skills/longform-story-design/references/project-intake.md`
- `skills/longform-story-design/references/planning-stack-selection.md`
- `skills/longform-story-design/references/longform-workflow.md`
- `skills/longform-story-design/references/handoff-to-drafting.md`

### Optional follow-up

- `skills/series-qa/SKILL.md`

This follow-up is only for boundary clarification if the main skill changes make overlap too visible.

## Target Behavior

When the user says things like:

- "중반부터 무너졌다"
- "설정 충돌이 쌓여서 못 쓰겠다"
- "연재가 길어지면서 캐릭터와 떡밥이 다 퍼졌다"
- "이 장편을 어떻게 다시 세워야 할지 봐줘"

the main skill should:

1. route the request into a recovery-aware mode immediately
2. extract canon before inventing fixes
3. diagnose root damage and scope of breakage
4. choose the minimum recovery stack
5. produce a reconstruction-ready artifact package
6. hand off only the active repaired slice to drafting

It should not stop at a symptom list unless the user explicitly asked for diagnosis only.

## Design Changes

### 1. Hard routing near the top of the skill

Add an explicit `Use this when / Do not use this when` block close to the overview:

- use `longform-story-design` for multi-arc drift, canon conflicts, broken middle, failed escalation, continuity collapse, and long-run recovery
- use `series-qa` for quick issue ranking, narrow-scope audit, pre-release QA, and report-only diagnostics
- use `novel-writing` for scene/chapter prose
- use `character-voice-bible` for dialogue-layer repair

### 2. One canonical decision order

Add a top-level execution order:

1. lock request mode
2. lock genre package
3. lock dominant longform risk
4. choose planning or recovery stack
5. choose output depth
6. choose drafting handoff slice

This replaces the current feeling that multiple selection blocks compete equally.

### 3. Recovery-aware modes

Expand or rename modes so recovery work becomes first-class:

- `greenfield build`
- `rolling outline`
- `recovery audit`
- `recovery rebuild`

Mode rule:

- `recovery audit` when the user needs long-range diagnosis plus repair priority
- `recovery rebuild` when the user needs a forward-looking reconstruction packet

### 4. Recovery artifact minimums

Define minimum deliverables and completion criteria for the core recovery artifacts:

- `canon extraction sheet`
- `continuity ledger`
- `knowledge-state tracker`
- `recovery plan`
- `re-entry drafting packet`

Each needs:

- required fields
- what counts as complete enough to hand off
- when to omit it

### 5. Reference precedence

Clarify which file governs each decision:

- `project-intake.md` for intake and first routing clues
- `planning-stack-selection.md` for stack choice
- `longform-workflow.md` for phase order and stage exits
- `planning-output-format.md` for package shape
- `handoff-to-drafting.md` for the active drafting slice

## Acceptance Criteria

The reinforced skill should satisfy all of these:

1. A damaged-longform request can be routed without ambiguity in under one top-level decision sequence.
2. A response can distinguish `report-only QA` from `rebuild-needed recovery`.
3. Recovery requests produce at least one reusable planning package, not just observations.
4. The drafting handoff explains what part of the repaired plan is active now.
5. The main skill no longer leaves `audit + repair` behavior implicit or scattered.

## Implementation Plan

1. Patch `SKILL.md` to add routing boundaries, decision order, recovery modes, and artifact completion rules.
2. Patch `project-intake.md` to map intake outcomes to first recovery bundles.
3. Patch `planning-stack-selection.md` to add precedence rules between project state, risk, and scale.
4. Patch `longform-workflow.md` to add stage exit criteria and recovery flow.
5. Patch `handoff-to-drafting.md` to clarify active-slice handoff after recovery.
6. Re-read `series-qa/SKILL.md` and patch only if a narrow boundary note is still necessary.

## Risks

- If recovery scope becomes too broad, `longform-story-design` may absorb `series-qa`.
- If boundary language is too soft, users will still get inconsistent routing.
- If artifact minimums are too heavy, the skill may become slower and overproduce.

## Review Checklist

- No contradictory routing between main skill and references
- Recovery mode is explicit, not inferred
- `series-qa` remains useful and distinct
- Output contract stays practical for real drafting workflows
