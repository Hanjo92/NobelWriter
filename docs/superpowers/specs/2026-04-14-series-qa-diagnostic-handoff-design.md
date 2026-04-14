# Series QA Diagnostic-Handoff Reinforcement

## Context

`series-qa` already has solid audit categories, but it still leans too close to revision planning. Its current output language includes `revision brief`, `smallest viable fix`, and other wording that can drift toward repair design instead of staying inside pure diagnosis.

After strengthening `longform-story-design` for long-range `audit + recovery`, the adjacent role for `series-qa` should become sharper, not broader. The user wants this skill to stay diagnostic-first: isolate the break, rank the damage, define what needs rechecking, and hand off deeper repair work to the proper downstream skill.

## Goal

Reinforce `series-qa` as the primary skill for pure diagnosis of existing long-form Korean fiction.

The skill should:

1. diagnose with evidence
2. locate the first break point
3. rank root causes before symptoms
4. define repair direction only at the level needed for handoff
5. route actual reconstruction to `longform-story-design`

## Decision

Use a `diagnosis + minimal handoff` model.

- `series-qa` owns diagnosis, severity, confidence, scope limits, and re-audit gates.
- `series-qa` may state repair direction, but only as a short directional note.
- `series-qa` must not produce reusable reconstruction packages, canon recovery packets, or drafting re-entry plans.
- When those are needed, the output should explicitly hand off to `longform-story-design`.

## Scope

### Files to update

- `skills/series-qa/SKILL.md`
- `skills/series-qa/references/diagnostic-workflow.md`
- `skills/series-qa/references/report-templates.md`
- `skills/series-qa/references/regression-checks.md`

### Optional follow-up

- `skills/series-qa/references/example-prompts.md`

Only update this if the trigger examples still imply broader repair ownership after the main wording changes.

## Target Behavior

When the user says things like:

- "어디가 무너졌는지 진단해줘"
- "몇 화부터 꼬였는지 봐줘"
- "수정 전에 어떤 문제가 가장 큰지 먼저 순위 매겨줘"
- "이 구간이 왜 재미가 빠지는지 분석해줘"

the skill should:

1. define scope and sampling limits
2. form testable failure hypotheses
3. locate the first break point
4. cluster issues into root cause and downstream symptoms
5. produce a ranked diagnostic report
6. state the minimum repair direction
7. name the correct downstream handoff target

It should not silently expand into rebuild planning.

## Design Changes

### 1. Hard boundary near the top of the skill

Add a short `Use this when / Hand off when` boundary block:

- use `series-qa` for ranked diagnosis, root-cause isolation, range-limited audit, and recheck criteria
- hand off to `longform-story-design` when the user needs canon recovery, reusable reconstruction documents, or a forward drafting packet
- hand off to `novel-writing` when the issue is already diagnosed and the next step is prose revision
- hand off to `character-voice-bible` when the issue is mainly dialogue differentiation or register repair

### 2. Make diagnosis order explicit

Add a canonical audit order that keeps this skill from drifting into solution mode too early:

1. lock scope
2. capture complaint
3. form hypotheses
4. find first break point
5. rank root causes
6. define minimal repair direction
7. assign handoff target
8. define re-audit gate

### 3. Narrow the output contract

Make the default outputs clearly diagnostic:

- QA report
- short triage
- arc health snapshot
- serialization checkpoint
- handoff note

Keep `revision brief` only if it stays directional and does not become a rebuild plan.

### 4. Standardize handoff language

Every serious finding should be able to say:

- what is broken
- why it matters
- what kind of fix is needed at a high level
- which downstream skill should take the next step

Examples:

- structural recovery -> `longform-story-design`
- prose or scene rewrite after diagnosis -> `novel-writing`
- dialogue-layer differentiation fix -> `character-voice-bible`

### 5. Strengthen recheck discipline

`regression-checks.md` should stay verification-oriented:

- did the failure mode disappear
- did the fix create a new contradiction
- should this return to QA, or move to planning recovery

## Acceptance Criteria

The reinforced skill should satisfy all of these:

1. A user can tell within the first section that this is a diagnosis-only skill.
2. The skill does not imply ownership of reconstruction packages or drafting re-entry packets.
3. A major finding includes root cause, evidence, reader-visible damage, minimal repair direction, and handoff target.
4. The templates read like QA artifacts rather than workshop notes or redesign plans.
5. Recheck rules verify removal of the original failure mode instead of subjective improvement only.

## Implementation Plan

1. Patch `SKILL.md` with sharper boundaries, diagnosis order, and output contract.
2. Patch `diagnostic-workflow.md` so the workflow ends in diagnostic handoff, not repair design.
3. Patch `report-templates.md` so templates include `repair direction` and `handoff target` without becoming reconstruction plans.
4. Patch `regression-checks.md` so recheck output distinguishes `QA pass`, `needs longform recovery`, and `needs local rewrite`.
5. Re-read `example-prompts.md` and patch it only if the examples still overreach into repair ownership.

## Risks

- If the wording becomes too narrow, the skill may stop being useful after diagnosis.
- If the handoff language is too soft, the skill will drift back into repair planning.
- If templates still say `revision brief` without constraints, users may keep treating the skill as a repair planner.

## Review Checklist

- diagnosis-first boundary is explicit
- `longform-story-design` is named as the reconstruction owner
- templates remain practical for real audits
- repair direction stays high-level and does not become a rebuild package
