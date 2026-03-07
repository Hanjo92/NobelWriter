# Novel Writing Workflow

Use this workflow when the request spans more than a single scene or requires disciplined revision.

## 1. Frame The Assignment

Capture the minimum brief:

- target format: outline, scene, chapter, synopsis, or critique
- genre and audience
- POV and tense
- if POV is important, decide `1인칭`, `3인칭 제한`, or a more distant third-person stance before drafting
- Korean register target: literary, commercial, web novel, YA, etc.
- desired length
- must-include and must-avoid elements
- current manuscript state

If critical information is missing, state a narrow assumption set and proceed.

Before loading deeper references, classify the request with [task-router.md](task-router.md) if the lane is not obvious.
Pick one primary lane: planning, fresh drafting, continuation, stage revision, dialogue-only revision, narration-only revision, or critique-only.

If the user names a genre or target audience with strong market expectations, load [genre-audience-samples.md](genre-audience-samples.md) and align hook placement, emotional framing, conflict texture, and dialogue density to that combination.
If the user asks to soften, sharpen, naturalize, masculinize, feminize, or rebalance dialogue tone, delegate that dialogue work to `character-voice-bible` and use [dialogue-tone-transforms.md](dialogue-tone-transforms.md) only as fallback guidance if that skill is unavailable.
If you need a ready-made instruction block for generation, load [prompt-selection-matrix.md](prompt-selection-matrix.md) and choose the closest genre, audience, and intent row before drafting.
If the user asks specifically for a chapter opener, load [chapter-opening-selection.md](chapter-opening-selection.md) before drafting the first lines.
If the user asks to fix or polish existing dialogue, delegate that work to `character-voice-bible` and use [dialogue-revision-selection.md](dialogue-revision-selection.md) only as fallback guidance if that skill is unavailable.
If the user asks to fix awkward narration or prose flow, load [narration-revision-selection.md](narration-revision-selection.md) before revising.
If you need a compact rule lookup for awkward narration, load [narration-tone-matrix.md](narration-tone-matrix.md) before rewriting sentences.
If the user specifies `1인칭` or `3인칭`, or the existing manuscript shows POV drift, load [korean-prose.md](korean-prose.md) and keep the narration inside that POV's knowledge and distance rules.
If concrete POV examples would help, load [pov-narration-examples.md](pov-narration-examples.md) before rewriting.
Do not introduce a POV shift inside the same chapter by default. Allow POV changes only at chapter boundaries unless the user explicitly asks for a different structure.
If the prose or dialogue feels semantically correct but artificially assembled, treat it as meaning-first scaffolding and rebuild from pressure, image, or focalized reaction rather than surface-editing.
If you need concrete before-and-after references for this failure mode, load [meaning-first-examples.md](meaning-first-examples.md) before rewriting.
If the user wants a chapter 1 launch package, first-scene starter, or subgenre-specific opener, load [starter-sets.md](starter-sets.md) first and then open the matching genre starter file before drafting.
If the task is actual fiction writing rather than advice only, load [draft-pipeline.md](draft-pipeline.md) and [manuscript-quality-gate.md](manuscript-quality-gate.md) before replying.
If the user explicitly asks for `초고`, `개고`, or `원고`, treat that as the return target. Otherwise, return `원고`.
If the wording sounds unnaturally purified, restore ordinary literary vocabulary rather than forcing native-only alternatives.
If you need concrete diction replacements for this issue, load [lexical-normalization-examples.md](lexical-normalization-examples.md) before revising.

### Routing Defaults

- planning: load [templates.md](templates.md) first and stop before manuscript-mode references unless the user also wants prose
- fresh drafting: load [draft-pipeline.md](draft-pipeline.md) and [manuscript-quality-gate.md](manuscript-quality-gate.md)
- continuation: sample the existing manuscript voice first, then use the fresh drafting path
- stage revision: load [templates.md](templates.md) for a `개고` brief if useful, then load [draft-pipeline.md](draft-pipeline.md), keep the requested return stage explicit, and revise through the full stage set
- dialogue-only revision: delegate to `character-voice-bible`; only use [dialogue-revision-selection.md](dialogue-revision-selection.md) as fallback if that skill is unavailable
- narration-only revision: load [narration-revision-selection.md](narration-revision-selection.md) and only load manuscript-mode references if the user wants full prose output
- critique-only: diagnose concrete issues first; do not rewrite unless the user asks

## 2. Stabilize The Story Engine

Before writing long prose, verify:

- the protagonist wants something concrete
- opposition can actively interfere
- stakes worsen over time
- the story can generate multiple scenes, not just one premise

If the engine is weak, fix desire, opposition, or stakes before expanding the outline.

## 3. Outline At The Lowest Useful Resolution

Choose the smallest outline that reduces risk:

- use a 1-paragraph synopsis for concept exploration
- use act beats for macro structure
- use chapter cards for medium-length drafting
- use scene cards for continuity-heavy drafting

Do not over-outline if the user wants exploratory drafting, but always record enough to preserve cause-and-effect.

## 4. Draft With Control

During drafting:

- enter late into the scene
- let character desire shape description
- keep dialogue active and directional
- end scenes on change, not summary
- reserve exposition for leverage, not decoration
- keep honorifics, speech endings, and forms of address consistent with relationship and tension
- check whether each line sounds sayable aloud by that speaker in that moment
- make the line respond to the prior line's emotional pressure, not just its factual content
- favor spoken Korean compression, interruption, hesitation, and partial answers where the moment calls for them
- do not shorten dialogue into heading-like fragments just to make it feel punchy
- separate speakers by reaction style, register, and emotional handling, not only by line length or vocabulary tier

When continuing existing prose, sample the established voice first and match sentence density, formality, and imagery habits.

When writing prose in this workspace, default to:

1. capture the minimum manuscript packet
2. produce `초고`
3. revise into `개고`
4. revise into `원고`
5. run the final manuscript quality gate
6. save all three files
7. return the `원고` version by default, or the explicitly requested stage if the user named one

## 5. Revise In Separate Passes

### Structural Pass

Check:

- missing setup or payoff
- weak escalation
- repetitive scene function
- climax that does not cash the central promise

### Character Pass

Check:

- actions that contradict motivation without explanation
- passive protagonists
- flat secondary cast
- relationships that do not evolve under pressure

### Prose Pass

Check:

- vague verbs and generic emotional labels
- overwritten description
- repeated sentence rhythm
- dialogue that explains what both characters already know
- translated-English syntax that sounds unnatural in Korean
- honorific drift or mismatched speech level
- dialogue that exists only to explain background to the reader
- lines that ignore the immediate emotional temperature of the scene
- narration that takes too long to land its subject or image
- sentences that are semantically correct but hard to read in one pass
- lines that still show the trace of abstract meaning being pre-arranged before phrasing
- words that are technically Korean but lexically unnatural in actual fiction prose
- short lines that are semantically functional but not plausibly speakable
- dialogue texture that is uniformly literary or uniformly clipped regardless of character difference
- abstract phrasing that is not supported by scene sensation, behavior, or genre-appropriate interiority

### Continuity Pass

Check:

- timeline drift
- naming inconsistencies
- injuries that disappear
- knowledge characters should not have yet
- object location errors

## 6. Deliver The Right Level Of Help

Match the response to the user's intent:

- for planning requests, provide artifacts and decision points
- for drafting requests, provide usable prose
- for critique requests, prioritize diagnosis over rewriting
- for rewrite requests, preserve intent and identify what changed

Default to concise, production-usable output instead of lecture-style explanation.

If dialogue quality is the main concern, diagnose the problem by line type:

- unnatural phrasing
- wrong register for the relationship
- exposition disguised as conversation
- emotion that is too explicit or too flat
- no subtext or turn inside the exchange
