---
name: novel-writing
description: Plan, draft, revise, and critique Korean-language fiction with emphasis on manuscript production, chapter execution, scene design, narration, continuity, pacing, tone, and natural Korean prose. Use when Codex is asked to create or improve Korean novels, web novels, serialized fiction, synopses, chapter plans, scene lists, openings, manuscript pages, narration, or revision passes in Korean, including requests such as 기획, 시놉시스, 초고, 개고, 원고, 문장 수정, 장면 수정, and chapter drafting. Treat this as the primary skill for narration-heavy and description-heavy manuscript work. Exclude standalone dialogue-only revision, character voice tuning, or spoken-exchange texture design, which should route to `character-voice-bible`.
---

# Novel Writing

## Immediate Execution Protocol

Treat this file as an action manual, not background reading.
If the user asks for Korean fiction work, do not answer that you are unsure how to use the skill. Start by routing the task, load only the minimum needed references, and produce the requested deliverable.

Execute in this order:

1. Identify the deliverable.
2. Route the request into one primary lane.
3. State only the smallest necessary assumption set.
4. Load only the references required for that lane.
5. Produce the planning packet or manuscript.
6. If prose is requested, run `초고 -> 개고 -> 원고`.
7. Return the requested stage, or `원고` by default.

If the request says `써줘`, `초고`, `개고`, `원고`, `장면`, `챕터`, `오프닝`, `도입부`, or `이어 써줘`, treat it as writing work, not as a request for explanation.

Do not stop to ask broad process questions if a narrow assumption will let you proceed safely.
If information is missing, make one-line assumptions and continue.

## Default Assumptions When The User Omits Details

Use these defaults so the skill remains executable for lightweight models:

- language: Korean
- primary lane: `fresh drafting` for direct writing requests, `planning` for outline requests, `stage revision` for rewrite requests, `critique-only` for feedback requests
- return stage: `원고`
- chapter target length: 5000~6000 characters including spaces
- project scale for longform/web novels: 150~200 chapters
- POV: keep the user's POV if given; otherwise default to `3인칭 제한시점`
- tone: contemporary commercial Korean fiction matched to the requested genre
- assumption policy: prefer the smallest assumption set that does not distort the user's premise

If the environment supports file writing, save stage files.
If the environment does not support file writing, still perform the same internal stage pipeline and return the final stage text.

## Overview

Use this skill to turn a rough fiction idea into a workable Korean-language story package, produce chapter-ready scene plans, draft narration-led manuscript prose with controlled assumptions, and revise it in deliberate passes.

Default to manuscript-first execution when the user wants actual prose. Planning, critique, and story development still matter, but they should support stronger scene and chapter delivery instead of replacing it. Treat this skill as the prose layer for narration, blocking, image landing, exposition control, and paragraph rhythm.

## Start From The Deliverable

Identify the immediate output before writing:

- premise or logline
- synopsis or pitch
- worldbuilding or story bible
- character sheet or relationship map
- act outline, chapter outline, or scene list
- scene, opening, or chapter manuscript
- revision pass, critique, or line edit

If the user asks for prose, treat the task as manuscript production unless they explicitly want notes only.
Default to returning `원고`. If the user explicitly asks for `초고`, `개고`, or another intermediate stage, return that requested stage instead while still saving the full stage set unless the user says not to.

Lock the operating constraints early: genre, target audience, point of view, tense, tone, target length (default to 5000~6000 characters per chapter unless specified otherwise), completion state, and any banned content or required themes. If the user omits these, make the smallest useful assumption set explicit before drafting.
When POV matters, decide not only `1인칭` or `3인칭`, but also narration distance, knowledge limit, and whether the voice is character-colored or relatively neutral.

Assume the output language is Korean unless the user explicitly requests bilingual or translated material.

## Quick Lane Map

Use this fast map before opening deeper references:

- asks for synopsis, outline, setting, cast, chapter list: `planning`
- asks to write a scene, opening, chapter, or first episode: `fresh drafting`
- asks to continue existing prose: `continuation`
- asks to turn rough text into better manuscript stages: `stage revision`
- asks to fix only dialogue or speaker voice: delegate to `character-voice-bible`
- asks to fix only narration or sentence flow: `narration-only revision`
- asks for diagnosis without rewrite: `critique-only`

If two lanes appear possible, choose the one closest to the user's requested final deliverable.

## Route The Task Before Writing

Before choosing references or generating output, classify the request into one primary lane:

- planning: premise, synopsis, cast, worldbuilding, chapter plan, scene list
- fresh drafting: opening, scene, chapter, multi-chapter manuscript
- continuation: continue or extend existing manuscript pages in the same voice
- stage revision: turn material into `초고`, `개고`, or `원고`
- dialogue-only revision: hand off line, register, subtext, and speaker-separation work to `character-voice-bible`
- narration-only revision: fix sentence flow, image landing, rhythm, or readability
- critique-only: diagnose issues without rewriting unless asked

Choose one primary lane first. Only mix lanes when the user clearly asks for both diagnosis and rewrite, or both planning and drafting.
If the task is dialogue-only revision or character voice tuning, delegate that lane to `character-voice-bible` and keep `novel-writing` focused on planning, manuscript drafting, stage revision, narration, and critique. If both layers matter, let `character-voice-bible` stabilize spoken lines first, then use `novel-writing` to integrate them into finished prose.

Read [references/task-router.md](references/task-router.md) when the request could fit more than one lane or when you need exact routing defaults.

## Build The Smallest Useful Story Packet

Before writing long prose, establish only what the draft needs:

1. Core premise: protagonist, goal, opposition, stakes, hook.
2. Story engine: what keeps generating conflict and forward motion.
3. Character pressure: desire, fear, contradiction, change vector.
4. Structural spine: opening disturbance, midpoint shift, crisis, climax, resolution.
5. Continuity anchors: timeline marker, current relationship state, what the POV character knows, and what must carry into the next scene.
6. Scene promise: what the specific chapter or scene must accomplish.

Keep the packet short unless the user asks for deep preproduction. Prefer compact, reusable notes over ornate lore.

For structured planning artifacts, read [references/templates.md](references/templates.md).

## Prioritize Manuscript Mode

When the user asks for a scene, opening, chapter, or direct prose revision:

1. Confirm the minimal manuscript brief.
2. Define the scene objective and exit change.
3. Decide who wants what right now.
4. Introduce resistance quickly.
5. Draft the prose in stage files.
6. Run a final manuscript quality gate before replying.

If the user asks for multiple chapters, outline each chapter first, then draft in sequence so continuity does not drift.

When the request is actual prose rather than advice only, read [references/draft-pipeline.md](references/draft-pipeline.md) and [references/manuscript-quality-gate.md](references/manuscript-quality-gate.md).
If the user explicitly names a stage such as `초고`, `개고`, or `원고`, honor that as the return target. Otherwise, return `원고`.

For lightweight models, use this minimum manuscript loop:

1. write a usable `초고`
2. remove obvious scaffolding and awkward Korean in `개고`
3. polish rhythm, POV stability, and readability in `원고`
4. return `원고` unless another stage was requested

## Draft Scene-First

During drafting:

- enter late enough that pressure is already active
- keep POV, tense, and voice stable within a scene
- keep narration inside the selected POV's knowledge boundary
- let desire shape description
- use exposition only when it changes reader understanding or raises stakes
- end with a change in information, power, emotion, or commitment

For `1인칭`, let the narration sound like this specific speaker could plausibly think or narrate it, and do not report inaccessible interior states from outside them.
For `3인칭`, decide whether the scene is close-limited or more distant, then keep the perceiver stable unless the user explicitly asks for omniscient narration.
Do not shift POV inside the same chapter by default. Treat POV switching as a special-case move allowed only at a chapter boundary unless the user explicitly requests a different structure.

Before writing dialogue-heavy scenes, calibrate each speaker's wording against age, relationship, status gap, current emotion, and what they are trying not to say. If the main problem is the spoken exchange itself rather than the surrounding prose, route that work to `character-voice-bible` first.
Treat dialogue as turn-by-turn spoken language shaped by the immediately preceding line, current tension, and the social cost of speaking too directly, but keep this skill centered on how that dialogue lives inside narration and scene prose.

For Korean prose control, read [references/korean-prose.md](references/korean-prose.md).
For genre and audience-specific tone control, read [references/genre-audience-samples.md](references/genre-audience-samples.md).
For dialogue tone conversion, delegate to `character-voice-bible` first and read [references/dialogue-tone-transforms.md](references/dialogue-tone-transforms.md) only as fallback guidance if that skill is unavailable.
For reusable drafting instructions, read [references/prompt-selection-matrix.md](references/prompt-selection-matrix.md).
For chapter starts, read [references/chapter-opening-selection.md](references/chapter-opening-selection.md).
For chapter 1 launch packages by genre and subgenre, read [references/starter-sets.md](references/starter-sets.md) first, then open the matching genre starter file.
For concrete start patterns when a lightweight model hesitates, read [references/lightweight-execution-examples.md](references/lightweight-execution-examples.md).
For meaning-first scaffolding examples, read [references/meaning-first-examples.md](references/meaning-first-examples.md).
For diction normalization examples, read [references/lexical-normalization-examples.md](references/lexical-normalization-examples.md).

## Revise In Passes

Do not mix every revision goal into one pass. Choose the smallest pass that matches the request:

- structural pass: plot logic, escalation, payoff, chapter order
- character pass: motivation, agency, arc, relational tension
- scene pass: objective, conflict, turning point, exit value
- prose pass: clarity, rhythm, imagery, repetition, dialogue sharpness
- continuity pass: timeline, names, rules, wounds, possessions, knowledge state

For revision defaults and checklists, read [references/workflow.md](references/workflow.md).
For dialogue fixes, delegate to `character-voice-bible` first and read [references/dialogue-revision-selection.md](references/dialogue-revision-selection.md) only as fallback guidance if that skill is unavailable.
For narration fixes, read [references/narration-revision-selection.md](references/narration-revision-selection.md).
For narration rule lookup, read [references/narration-tone-matrix.md](references/narration-tone-matrix.md).

When critiquing, point to concrete breaks in cause-and-effect, character logic, pacing, or tonal control. Offer fixes that preserve the user's intent before proposing larger rewrites.

## Operating Rules

- Prefer production-usable output over lecture-style explanation.
- Summarize assumptions before long-form drafting.
- Preserve the user's chosen genre conventions unless they ask to subvert them.
- Track named entities, timeline markers, unresolved promises, and scene exits while drafting.
- When continuing an existing manuscript, mirror established POV, tense, diction, and paragraph density before introducing changes.
- Do not let `1인칭` narration drift into external diagnosis of the narrator, and do not let `3인칭 제한시점` drift into unexplained mind-reading.
- Treat mid-chapter POV switching as a continuity error unless the user explicitly asks for it; default to allowing POV changes only across chapter boundaries.
- When the user asks for feedback only, critique first and rewrite only if requested.
- Default to returning `원고`, but when the user explicitly requests `초고` or `개고`, return that stage after saving the full pipeline.
- Default to natural Korean syntax over translation-like sentence structure.
- Treat narration, exposition control, paragraph rhythm, and image clarity as primary responsibilities of this skill.
- Keep speech level, honorific choice, and relationship-dependent address forms consistent.
- Prefer Korean-native phrasing unless foreign diction is an intentional voice choice.
- Make dialogue sound speakable in context, not merely grammatically correct.
- Prefer lines a real person in that exact relationship and situation would plausibly say.
- Avoid drama-like exposition in dialogue unless the style target explicitly calls for heightened speech.
- Make each reply react to the prior utterance instead of sounding like an isolated prepared sentence.
- Default to colloquial Korean phrasing when characters are speaking, unless the scene clearly requires formal or stylized diction.
- Ensure `원고` is materially cleaner than `초고` and `개고`, not just a duplicate save.
- When the requested change is mainly about speaker differentiation, line-by-line pressure, or relationship-dependent dialogue texture, use `character-voice-bible` as the dialogue layer instead of solving it here by narration edits alone.

## Resource Map

- Read [references/templates.md](references/templates.md) when you need reusable planning formats or a structured `개고` brief.
- Read [references/task-router.md](references/task-router.md) when you need to decide whether the task is planning, fresh drafting, continuation, stage revision, dialogue-only revision, narration-only revision, or critique-only.
- Read [references/workflow.md](references/workflow.md) when you need a fuller end-to-end fiction workflow or revision checklist.
- Read [references/draft-pipeline.md](references/draft-pipeline.md) when prose should be produced and saved as `초고`, `개고`, and `원고` files.
- Read [references/manuscript-quality-gate.md](references/manuscript-quality-gate.md) when the task is direct manuscript drafting or prose revision and you need the final quality checklist.
- Read [references/korean-prose.md](references/korean-prose.md) when you need Korean-specific register, naming, style guidance, or POV-specific narration rules for `1인칭`, `3인칭 제한`, or more distant third-person control.
- Read [references/pov-narration-examples.md](references/pov-narration-examples.md) when you need small concrete examples comparing `1인칭` and `3인칭 제한` narration on the page.
- Read [references/genre-audience-samples.md](references/genre-audience-samples.md) when the requested genre or target audience should materially change tone, hooks, pacing, or dialogue texture.
- Read [references/dialogue-tone-transforms.md](references/dialogue-tone-transforms.md) only as fallback guidance when `character-voice-bible` is unavailable and dialogue work cannot be delegated.
- Read [references/prompt-selection-matrix.md](references/prompt-selection-matrix.md) when you need a compact prompt formula for a given genre, audience, scene intent, or dialogue task.
- Read [references/chapter-opening-selection.md](references/chapter-opening-selection.md) when you need a focused prompt for the first lines of a chapter.
- Read [references/lightweight-execution-examples.md](references/lightweight-execution-examples.md) when the model still hesitates about how to begin after routing the task.
- Read [references/dialogue-revision-selection.md](references/dialogue-revision-selection.md) only as fallback guidance when `character-voice-bible` is unavailable and dialogue work cannot be delegated.
- Read [references/narration-revision-selection.md](references/narration-revision-selection.md) when narration is meaningful but awkward, heavy, tangled, or rhythmically weak.
- Read [references/narration-tone-matrix.md](references/narration-tone-matrix.md) when you need a quick rule table for fixing awkward narration by problem type, target effect, genre, or audience tendency.
- Read [references/meaning-first-examples.md](references/meaning-first-examples.md) when dialogue or narration still sounds like abstract meaning was arranged first and only afterward phrased in Korean.
- Read [references/lexical-normalization-examples.md](references/lexical-normalization-examples.md) when wording sounds awkward because common literary or Sino-Korean vocabulary was replaced by forced native-only diction.
- Read [references/starter-sets.md](references/starter-sets.md) when the user asks for a chapter 1 start, first-scene launch, or a genre/subgenre-specific opening package, then follow its link to the matching genre starter file.

## Minimum Response Shapes

When replying, keep the structure aligned to the lane:

- planning: brief assumption line, then the requested planning artifact
- drafting: brief assumption line, then the final prose stage
- continuation: brief assumption line, then continued prose matching the existing voice
- stage revision: brief assumption line, then the requested revised stage
- critique-only: concrete issue list first, rewrite only if asked

When prose was generated in a writable environment, mention where `초고`, `개고`, and `원고` were saved.
