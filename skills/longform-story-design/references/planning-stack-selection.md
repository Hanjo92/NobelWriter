# Planning Stack Selection

Use this file when deciding which longform design documents to create first.

## Deterministic Selection Rule

Use this file only after the top-level order has already locked `mode -> package -> dominant risk`. Then choose the stack in this order:

1. locked mode
2. dominant risk
3. scale

Locked mode wins when it clearly says the work is greenfield, rolling, recovery, or report-only QA. If the user only wants ranked findings, route to `series-qa` instead of building a reconstruction stack. If two longform stacks still fit, let dominant risk pick the first failure point. If mode and risk still leave more than one valid stack, use scale to add only the trackers the project can actually sustain.

When there is still a tie, choose the smaller stack that covers the first blocking problem. Do not add a document just because the project is large if a smaller recovery or drafting bundle already covers the next safe step.

## Orchestrated Slice Rule

When the caller is `series-completion-loop` in `slice_planning`, ignore scale-based expansion stacks beyond the active batch. Select only the smallest packet needed to plan `current_batch_start` through `current_batch_end`, normally the next `3~5화`, and carry forward no future-batch commitments.

## By Locked Mode Or Project State

- premise only: story engine sheet, series brief, story bible
- premise plus ending promise: story engine sheet, series brief, story bible, first volume or arc plan
- partial outline: story engine sheet, story bible, arc plan, chapter-range plan
- active drafting: chapter-range plan, continuity ledger, payoff tracker
- existing messy draft: canon extraction sheet, continuity ledger, knowledge-state tracker, recovery plan, re-entry drafting packet, plus a history spine or revised active arc plan only if chronology or arc shape must be reset

## By Dominant Risk

- premise too thin for long scale: story engine sheet, series brief, series expansion map
- world-rule drift: story bible, world rule sheet, continuity ledger
- cast flattening: core cast matrix, relationship map, arc plan
- timeline collision: history spine, continuity ledger
- weak middle escalation: volume or arc plan, chapter-range plan
- secret handling failure: knowledge-state tracker, payoff tracker
- setup with no return: payoff tracker, arc plan
- serialization fatigue: chapter-range plan, drafting packet
- report-only QA: route to `series-qa`; do not build recovery artifacts here

If more than one risk applies, choose the one that would break the next handoff first. That risk decides the first stack, and the other risks only add documents if they change the next safe output.

## By Scale

- under 40 chapters: story engine sheet, series brief, story bible, first arc plan
- 40 to 120 chapters: story engine sheet, story bible, cast matrix, volume or arc plan, continuity ledger
- 120 plus chapters or open serialization: story engine sheet, story bible, cast matrix, series expansion map, volume plan, chapter-range plan, continuity ledger, knowledge-state tracker, payoff tracker

Do not apply the scale expansion rule to an orchestrated `slice_planning` handoff unless the handoff explicitly re-authorizes series-level planning.

If scale points to a larger stack but the project state is still greenfield, do not start with continuity tools. If scale points to a smaller stack but the project is already in active drafting or repair, keep the drafting or recovery tools that match the current state.

## Greenfield First Rule

If there is no draft yet, do not start with continuity tools. Start with story engine, series brief, and the smallest architecture layer that proves the project can sustain itself.

## Stop Rule

Stop adding documents when the next likely failure point is already covered. More files are not better if they are not being updated.
