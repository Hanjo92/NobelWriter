# Planning Stack Selection

Use this file when deciding which longform design documents to create first.

## Deterministic Selection Rule

Choose the stack in this order:

1. project state
2. dominant risk
3. scale

Project state wins when it clearly says the work is greenfield, rolling, repair, or audit. If two stacks still fit, let dominant risk pick the first failure point. If state and risk still leave more than one valid stack, use scale to add only the trackers the project can actually sustain.

When there is still a tie, choose the smaller stack that covers the first blocking problem. Do not add a document just because the project is large if a smaller recovery or drafting bundle already covers the next safe step.

## By Project State

- premise only: story engine sheet, series brief, story bible
- premise plus ending promise: story engine sheet, series brief, story bible, first volume or arc plan
- partial outline: story engine sheet, story bible, arc plan, chapter-range plan
- active drafting: chapter-range plan, continuity ledger, payoff tracker
- existing messy draft: canon extraction sheet, continuity audit report, history spine, knowledge-state tracker, revised active arc plan if the middle has lost direction

## By Dominant Risk

- premise too thin for long scale: story engine sheet, series brief, series expansion map
- world-rule drift: story bible, world rule sheet, continuity ledger
- cast flattening: core cast matrix, relationship map, arc plan
- timeline collision: history spine, continuity ledger
- weak middle escalation: volume or arc plan, chapter-range plan
- secret handling failure: knowledge-state tracker, payoff tracker
- setup with no return: payoff tracker, arc plan
- serialization fatigue: chapter-range plan, drafting packet

If more than one risk applies, choose the one that would break the next handoff first. That risk decides the first stack, and the other risks only add documents if they change the next safe output.

## By Scale

- under 40 chapters: story engine sheet, series brief, story bible, first arc plan
- 40 to 120 chapters: story engine sheet, story bible, cast matrix, volume or arc plan, continuity ledger
- 120 plus chapters or open serialization: story engine sheet, story bible, cast matrix, series expansion map, volume plan, chapter-range plan, continuity ledger, knowledge-state tracker, payoff tracker

If scale points to a larger stack but the project state is still greenfield, do not start with continuity tools. If scale points to a smaller stack but the project is already in active drafting or repair, keep the drafting or recovery tools that match the current state.

## Greenfield First Rule

If there is no draft yet, do not start with continuity tools. Start with story engine, series brief, and the smallest architecture layer that proves the project can sustain itself.

## Stop Rule

Stop adding documents when the next likely failure point is already covered. More files are not better if they are not being updated.
