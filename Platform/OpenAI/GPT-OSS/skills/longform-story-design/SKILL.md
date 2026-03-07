# Longform Story Design for GPT-OSS

## Source

- 원본: `skills/longform-story-design/SKILL.md`

## Overview

Build only the planning layer needed to keep a long Korean fiction project coherent across many chapters. Prefer reusable working documents over lore essays.

Default to `greenfield build` when the user is starting from an idea, hook, synopsis, or loose cast concept. Treat repair and audit as secondary modes unless the request clearly starts from existing chapters.

## Start With Intake

Lock the minimum facts before designing anything large:

- format and scale
- structure mode, if relevant: linear arc, braided ensemble, omnibus, rotating-focus serial
- genre and audience tendency
- user-stated genre label, if any
- likely chapter-return engine
- alias resolution note, if the stated label is cross-package or ambiguous
- project state: premise only, partial outline, existing chapters, or repair request
- known ending or ending promise
- dominant risk: drift, escalation collapse, timeline collision, weak opposition, flat relationship motion, forgotten setup
- likely package selection reason
- requested output: bible, arc plan, chapter architecture, repair pass, drafting packet

If the prompt is vague, infer the smallest safe scope and state the assumption. For quick intake fields and risk triage, read [references/project-intake.md](references/project-intake.md).

After intake, choose one genre package before building the planning stack. Read [references/genre-packages.md](references/genre-packages.md) when the story's growth logic depends on genre pressure.
If the user says `옴니버스`, treat that as structure mode or format, not as a genre package. Keep it in `Format` and choose the genre package separately.

If the user explicitly names a genre or package, honor it first and map it to the closest supported genre package before running inference. If that mapped package has structural friction with the project, keep it and record a warning instead of silently switching packages.

## Choose One Primary Mode

Choose the main job first. Do not mix all modes unless the user clearly needs that.

- `greenfield build`
- `rolling outline`
- `drift repair`
- `continuity audit`

If the project is not yet drafted, stay in `greenfield build` long enough to lock the story engine, growth model, and first major architecture layer before producing chapter-by-chapter plans.

## Prioritize The Story Engine

Before building large bibles, confirm the story can generate longform movement:

- the protagonist has a durable pursuit, wound, hunger, or obligation
- the opposition can escalate in changing forms instead of repeating one obstacle
- the setting produces recurring pressure rather than serving as background decoration
- at least two escalation lanes can keep moving when one lane pauses
- the ending promise can already be felt from the opening hook

If this is still weak, design the engine first. Read [references/story-engine.md](references/story-engine.md).

## Choose A Genre Package Early

Do not treat all longform genres as structurally identical. After identifying the growth model, choose the closest genre package and let it change what the plan emphasizes.

Highest-priority rule: if the user directly says the genre, use that genre package first.

Choose package by priority order:

1. what makes the reader return next chapter
2. what kind of reversal hurts most
3. what the ending promise fundamentally resolves
4. what kind of expansion the middle requires

If these signals disagree, trust return engine over setting flavor.
If you need a stepwise lock instead of a prose judgment, run the checklist in [references/genre-selection-rules.md](references/genre-selection-rules.md).
If you need a one-page working form for that lock, use [references/genre-selection-decision-sheet.md](references/genre-selection-decision-sheet.md).

Default genre packages:

- `romance / romance fantasy`
- `progression / action fantasy`
- `mystery / thriller`
- `political / war / faction drama`
- `survival / apocalypse / horror`

If the project is hybrid, choose one dominant package and one secondary package. Do not give equal weight to three or more packages.

Do not classify by costume, setting, or structure label alone.

## Start From The Longform Risk

Identify what will break first if drafting continues without planning support:

- world rules drifting
- cast motivation or voice flattening over time
- timeline collisions
- power system escalation without cost
- secrets revealed too early or too late
- foreshadowing that never pays off
- chapter order that does not support arc momentum

Choose the smallest planning stack that solves that risk. Do not inflate the bible just because the story is long.

## Choose The Minimum Planning Stack

Pick only the deliverables the project actually needs. Use [references/planning-stack-selection.md](references/planning-stack-selection.md) when the correct stack is not obvious.

Default stacks:

- `greenfield build`: story engine sheet, series brief, story bible, core cast matrix, first arc or volume plan
- `rolling outline`: active arc plan, chapter-range plan, continuity ledger, payoff tracker
- `drift repair`: canon extraction sheet, history spine, continuity ledger, knowledge-state tracker
- `continuity audit`: continuity ledger, knowledge-state tracker, payoff tracker, drafting packet

Available deliverables:

- series brief
- story engine sheet
- story bible
- world rule sheet
- cast matrix and relationship map
- history timeline
- series expansion map
- volume plan
- arc spine
- chapter architecture
- continuity ledger
- knowledge-state tracker
- promise/payoff tracker
- canon extraction sheet
- continuity audit report

## Work In Layers

Build longform projects in this order unless the user requests otherwise:

1. Story engine and ending promise
2. Series premise and scale
3. World constraints and pressure sources
4. Core cast and relationship tensions
5. History spine and present-day trigger
6. Volume or major-arc structure
7. Chapter-range architecture
8. Continuity and knowledge tracking

Do not jump to 100-chapter planning before the story engine is stable.

## Expand Outward, Not Downward

For greenfield planning, expand in widening layers:

1. premise and ending promise
2. story engine
3. series or season growth model
4. volume or arc ladder
5. chapter-range objectives

Do not collapse too early into detailed chapter summaries.

## Extract Canon Before Inventing More

When the user brings existing chapters, notes, or mixed canon:

1. extract confirmed facts first
2. separate hard canon from rumor, public version, and guesswork
3. note the last chapter or range that confirms each fact
4. mark contradictions explicitly instead of smoothing them over
5. repair only after the conflict is visible

Do not quietly invent canon to hide uncertainty.

## Use Stable Documents

Every longform design artifact should answer one question cleanly:

- `story bible`
- `timeline`
- `continuity ledger`
- `knowledge tracker`
- `payoff tracker`

Prefer revisable tables and bullet structures over lore essays.

## Keep The Documents Operational

Make each artifact easy to update during serialization:

- use chapter, range, or arc references when facts come from existing material
- separate current truth from future intent
- mark unresolved items as open instead of pretending they are solved
- state what changes the next update must record
- keep emotional, relational, and political state visible, not just plot logistics

## Relationship To Drafting

This skill is for planning, stabilization, and continuity control. It is not the primary layer for final prose.

When the user wants actual scenes or chapters:

1. finish or update the longform planning artifacts here
2. if cast voice or dialogue differentiation is a visible risk, hand the dialogue layer to `character-voice-bible`
3. hand narration, scene execution, and chapter prose to `novel-writing`
4. after drafting, update continuity, knowledge state, and payoff status

## Default Answer Shape

When delivering greenfield planning work, prefer a named package rather than loose notes. Default order:

1. project frame
2. primary risk diagnosis
3. design decision
4. artifact package
5. next design step

State the planning stack inside `design decision` or as a short line before `artifact package` only when the chosen depth level or document scope would otherwise be unclear.

## Match Output Density To Scope

Choose one depth level:

- `concept pass`
- `development pass`
- `production pass`

Do not jump to production-pass density unless the user asked for detailed structure or the project is already stabilized.

## Use Declarative Planning Language

Planning output should read like working design material:

- use short labeled sections
- state decisions directly instead of narrating reasoning at length
- separate confirmed design from optional variants
- when offering options, cap at two
- keep each artifact internally scannable

## Resource Map

- Read [references/project-intake.md](references/project-intake.md) when the prompt is underspecified.
- Read [references/longform-workflow.md](references/longform-workflow.md) when you need the end-to-end planning order.
- Read [references/greenfield-architecture.md](references/greenfield-architecture.md) when turning a premise into series, volume, and arc architecture.
- Read [references/story-engine.md](references/story-engine.md) when premise strength or escalation durability is unclear.
- Read [references/genre-packages.md](references/genre-packages.md) when the package should change by genre.
- Read [references/genre-selection-rules.md](references/genre-selection-rules.md) when more than one package seems plausible.
- Read [references/genre-alias-map.md](references/genre-alias-map.md) when shorthand or mixed labels need mapping.
- Read [references/project-frame-template.md](references/project-frame-template.md) when you need a reusable top block.
- Read [references/planning-output-format.md](references/planning-output-format.md) when you need a denser output package.
- Read [references/planning-stack-selection.md](references/planning-stack-selection.md) when you need the minimum viable document set.
- Read [references/longform-templates.md](references/longform-templates.md) when you need fill-in templates.
- Read [references/continuity-ledger.md](references/continuity-ledger.md) when the main risk is contradiction or unstable knowledge state.
- Read [references/repair-existing-draft.md](references/repair-existing-draft.md) when the user already has chapters or conflicting canon.
- Read [references/handoff-to-drafting.md](references/handoff-to-drafting.md) when planning output needs to be reduced into dialogue-ready and prose-ready packets.
