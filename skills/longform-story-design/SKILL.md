---
name: longform-story-design
description: Design and stabilize long-form Korean fiction at series, volume, and chapter-batch level by building story engines, bibles, world rules, cast matrices, history timelines, arc plans, continuity ledgers, knowledge trackers, and payoff maps. Use when Codex is asked to plan a Korean long novel, web novel, saga, or multi-arc serial; turn a premise into a scalable longform structure; expand a short hook into volume architecture; repair an existing long draft that is drifting; or prepare continuity-safe drafting packets across many chapters.
---

# Longform Story Design

Build only the planning layer needed to keep a long Korean fiction project coherent across many chapters. Prefer reusable working documents over lore essays.

Default to `greenfield build` when the user is starting from an idea, hook, synopsis, or loose cast concept. Treat repair and audit as secondary modes unless the request clearly starts from existing chapters.

## Start With Intake

Lock the minimum facts before designing anything large:

- format and scale
- genre and audience tendency
- user-stated genre label, if any
- likely chapter-return engine
- project state: premise only, partial outline, existing chapters, or repair request
- known ending or ending promise
- dominant risk: drift, escalation collapse, timeline collision, weak opposition, flat relationship motion, forgotten setup
- likely package selection reason
- requested output: bible, arc plan, chapter architecture, repair pass, drafting packet

If the prompt is vague, infer the smallest safe scope and state the assumption. For quick intake fields and risk triage, read [references/project-intake.md](references/project-intake.md).

After intake, choose one genre package before building the planning stack. Read [references/genre-packages.md](references/genre-packages.md) when the story's growth logic depends on genre pressure.

If the user explicitly names a genre or package, honor it first and map it to the closest supported genre package before running inference.

## Choose One Primary Mode

Choose the main job first. Do not mix all modes unless the user clearly needs that.

- `greenfield build`: turn a premise into a scalable longform planning stack
- `rolling outline`: support active drafting with the next arc or chapter-range packet
- `drift repair`: recover canon and structure from an existing, unstable draft
- `continuity audit`: check timeline, knowledge, rules, and payoff consistency without rebuilding the whole project

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

Highest-priority rule: if the user directly says the genre, use that genre package first. Infer only when the user did not specify it, or when they specified multiple genres and a dominant package still has to be chosen.

Choose package by priority order:

1. what makes the reader return next chapter
2. what kind of reversal hurts most
3. what the ending promise fundamentally resolves
4. what kind of expansion the middle requires

If these signals disagree, trust return engine over setting flavor.

Default genre packages:

- `romance / romance fantasy`: relationship pressure, hierarchy friction, secrecy, emotional reversals
- `progression / action fantasy`: power ceiling, cost curve, training or trial structure, enemy ladder
- `mystery / thriller`: question chain, information control, suspicion spread, reveal timing
- `political / war / faction drama`: leverage map, alliance movement, public versus private goals, consequence spread
- `survival / apocalypse / horror`: scarcity rhythm, trust fracture, environment pressure, collapse thresholds

If the project is hybrid, choose one dominant package and one secondary package. Do not give equal weight to three or more packages.

If the user explicitly says `로판`, `로맨스`, `정치극`, `성장형 판타지`, `스릴러`, `아포칼립스`, `호러` or an equivalent direct label, do not override that with setting-based inference.

Do not classify by costume or setting label alone. Court setting does not automatically mean political drama. Fantasy world does not automatically mean progression fantasy. Apocalypse backdrop does not automatically mean survival horror if the real engine is investigation or romance.

Use hard tie-breaks:

- if relationship union, separation, jealousy, confession timing, or status imbalance drives return, choose `romance / romance fantasy`
- if rank climbing, training, trials, mastery, or costed power growth drives return, choose `progression / action fantasy`
- if question chain, clue interpretation, suspect rotation, or reveal timing drives return, choose `mystery / thriller`
- if factions, alliances, succession, public decrees, or leverage exchange drive return, choose `political / war / faction drama`
- if scarcity, contamination, pursuit, safe-zone loss, or trust breakdown drives return, choose `survival / apocalypse / horror`

If still tied, choose the package that most strongly determines the volume-end promise.

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

For longform workflow defaults, read [references/longform-workflow.md](references/longform-workflow.md).
For premise-to-series build order, read [references/greenfield-architecture.md](references/greenfield-architecture.md).
For story engine design, read [references/story-engine.md](references/story-engine.md).
For genre-specific package emphasis, read [references/genre-packages.md](references/genre-packages.md).
For strict genre-package selection rules, read [references/genre-selection-rules.md](references/genre-selection-rules.md).
For dense genre-label alias mapping, read [references/genre-alias-map.md](references/genre-alias-map.md).
For ambiguous alias resolution samples, read [references/genre-package-samples.md](references/genre-package-samples.md).
For a reusable project frame template, read [references/project-frame-template.md](references/project-frame-template.md).
For answer packaging and output density, read [references/planning-output-format.md](references/planning-output-format.md).
For genre-specific sample packages, read [references/genre-package-samples.md](references/genre-package-samples.md).
For reusable planning formats, read [references/longform-templates.md](references/longform-templates.md).
For continuity and state tracking, read [references/continuity-ledger.md](references/continuity-ledger.md).
For handoff into chapter drafting, read [references/handoff-to-drafting.md](references/handoff-to-drafting.md).
For existing-manuscript rescue, read [references/repair-existing-draft.md](references/repair-existing-draft.md).

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

Do not collapse too early into detailed chapter summaries. If the engine or volume ladder is still unstable, detailed chapter beats create false certainty.

## Extract Canon Before Inventing More

When the user brings existing chapters, notes, or mixed canon:

1. extract confirmed facts first
2. separate hard canon from rumor, public version, and guesswork
3. note the last chapter or range that confirms each fact
4. mark contradictions explicitly instead of smoothing them over
5. repair only after the conflict is visible

Do not quietly invent canon to hide uncertainty. If the manuscript is the authority, derive from it before proposing new structure.

## Use Stable Documents

Every longform design artifact should answer one question cleanly:

- `story bible`: what is true in the setting and cast
- `timeline`: what happened when
- `continuity ledger`: what changed and what must stay consistent
- `knowledge tracker`: who knows what, and from when
- `payoff tracker`: what was promised, delayed, or cashed

Prefer revisable tables and bullet structures over lore essays.

## Keep The Documents Operational

Make each artifact easy to update during serialization:

- use chapter, range, or arc references when facts come from existing material
- separate current truth from future intent
- mark unresolved items as open instead of pretending they are solved
- state what changes the next update must record
- keep emotional, relational, and political state visible, not just plot logistics

For Korean longform fiction, preserve genre pressure and audience expectation in the planning layer. Relationship heat, secrecy, hierarchy, revenge logic, power ceilings, and episode-end promise should remain legible in the documents.

When planning for Korean serialized reading habits, keep return hooks visible at multiple scales:

- opening-hook promise
- arc-end emotional or strategic reversal
- volume-end expansion or rupture
- repeatable chapter-end pressure

## Relationship To Drafting

This skill is for planning, stabilization, and continuity control. It is not the primary skill for final prose.

When the user wants actual scenes or chapters:

1. finish or update the longform planning artifacts here
2. hand the active subset to the drafting layer
3. after drafting, update continuity, knowledge state, and payoff status

Use this skill before drafting when the manuscript is likely to drift. Use it after drafting when accumulated chapters need coherence repair.

## Default Answer Shape

When delivering greenfield planning work, prefer a named package rather than loose notes. Default order:

1. project frame
2. primary risk diagnosis
3. design decision
4. planning stack
5. artifact package
6. next design step

Inside `artifact package`, present documents in stable order:

1. story engine sheet
2. series brief
3. story bible
4. core cast matrix
5. series expansion map
6. volume ladder
7. first arc or chapter-range plan

Do not omit the package label if more than two artifacts are present.

Inside `project frame`, surface the chosen genre package. Inside `design decision`, state how that package changes the architecture.

Always include `package selection reason` in `project frame`.

- write exactly one sentence
- justify the package by chapter-return engine, volume-end promise, or dominant failure mode
- if hybrid, explain why the dominant package outranks the secondary one

Do not omit this line even when the package looks obvious from the setting.

## Match Output Density To Scope

Choose one depth level:

- `concept pass`: engine sheet, series brief, and one first-arc sketch
- `development pass`: add story bible, cast matrix, and volume ladder
- `production pass`: add chapter-range plan, trackers, and drafting handoff

Do not jump to production-pass density unless the user asked for detailed structure or the project is already stabilized.

## Use Declarative Planning Language

Planning output should read like working design material:

- use short labeled sections
- state decisions directly instead of narrating your reasoning at length
- separate confirmed design from optional variants
- when offering options, cap at two and say what changes structurally
- keep each artifact internally scannable

Avoid turning the plan into an essay about the plan.

## Resource Map

- Read [references/project-intake.md](references/project-intake.md) when the prompt is underspecified or the planning stack must be chosen from incomplete information.
- Read [references/longform-workflow.md](references/longform-workflow.md) when you need the end-to-end planning order for long novels or series.
- Read [references/greenfield-architecture.md](references/greenfield-architecture.md) when you are turning a premise or hook into series, volume, and arc architecture from scratch.
- Read [references/story-engine.md](references/story-engine.md) when premise strength, escalation durability, opposition design, or ending promise are still unclear.
- Read [references/genre-packages.md](references/genre-packages.md) when the package should change by genre rather than staying genre-neutral.
- Read [references/genre-selection-rules.md](references/genre-selection-rules.md) when more than one package seems plausible and you need a stricter decision rule.
- Read [references/genre-alias-map.md](references/genre-alias-map.md) when the user uses shorthand, platform slang, or mixed Korean/English genre labels that need to map to a supported package.
- Read [references/project-frame-template.md](references/project-frame-template.md) when you need the reusable top block for planning output and do not want `project frame` fields to drift.
- Read [references/planning-output-format.md](references/planning-output-format.md) when you need a denser, repeatable output package for longform design work.
- Read [references/genre-package-samples.md](references/genre-package-samples.md) when you need concrete examples of how the same planning format changes by genre package.
- Read [references/planning-stack-selection.md](references/planning-stack-selection.md) when you need to choose the minimum viable document set for a given scale, risk, or manuscript state.
- Read [references/longform-templates.md](references/longform-templates.md) when you need fill-in templates for bibles, arcs, timelines, or ledgers.
- Read [references/continuity-ledger.md](references/continuity-ledger.md) when the main risk is contradiction, forgotten setup, drifting rules, or unstable knowledge state.
- Read [references/repair-existing-draft.md](references/repair-existing-draft.md) when the user already has chapters, outlines, or conflicting canon and needs recovery before more drafting.
- Read [references/handoff-to-drafting.md](references/handoff-to-drafting.md) when planning output needs to be reduced into drafting-ready packets for the prose layer.
