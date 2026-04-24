---
name: character-voice-bible
description: Design, document, compare, and preserve distinct Korean character voices across fiction manuscripts by defining speech register, honorific use, address forms, reaction habits, emotional deflection, subtext behavior, and relationship-dependent dialogue shifts. Treat this as the primary skill for dialogue-centered work: script-like back-and-forth exchange, turn-by-turn reaction, spoken-line pressure, and speaker-labeled dialogue. Use it when Codex is asked to build or repair cast-specific speaking styles, keep voices distinct across chapters, prevent dialogue from collapsing into one authorial tone, or handle requests such as "인물 말투 정리", "캐릭터별 대사 차별화", "이 캐릭터 말투가 무너짐", "대본처럼 대사만 주고받게 써", or "관계 변화에 맞춰 존댓말/반말을 조정".
---

# Character Voice Bible

## Overview

Use this skill to build and maintain a cast-wide Korean dialogue system. Focus on stable speaker differentiation across chapters, scenes, and relationship changes rather than on isolated line polishing. Treat it as the dialogue layer, not the narration layer.

Default to dialogue-first execution. If the user wants active exchange, output speaker-labeled lines that read like a script before considering prose wrapping. Keep the center of gravity on what the characters say, how they react, and how their spoken turns collide.

## Orchestrated Voice Handoff Intake

When invoked by `series-completion-loop`, `novel-writing`, or `series-qa` for dialogue repair, act only as the voice specialist for the current batch or excerpt.

Before voice work, require the handoff to name:

- selected `projects/<series-slug>/` runtime path or explicit manuscript artifact path
- `current_batch_start` and `current_batch_end`, or a smaller explicit excerpt/range inside that batch
- affected speakers or pair/group
- current relationship state and register expectation
- scene pressure or voice failure being repaired
- existing dialogue lines, or a clear request for sample proof lines only

If the orchestrated handoff lacks batch/excerpt scope, affected speakers, or current relationship state, return a blocker. Do not infer project identity, batch range, future relationship state, or missing plot context from chat history.

Hard-limit orchestrated voice work to the named batch or excerpt.

- Repair only dialogue, speaker differentiation, register, address forms, and voice rules.
- Do not continue the chapter, write narration-heavy prose, draft new scenes, plan future chapters, or redesign plot beats.
- Do not mutate manuscript stage files directly; return proof rewrites for the caller to apply.
- Do not edit `state/runtime.yaml`, `state/active-slice.yaml`, `state/handoff.md`, ledgers, QA reports, recovery plans, or `초고`/`개고`/`원고` files.
- If the handoff needs plot planning, recovery direction, QA acceptance, continuity ledger repair, or full prose integration, stop and name the correct owner: `longform-story-design`, `series-qa`, or `novel-writing`.

For successful orchestrated voice work, return a compact `voice_handoff` block with:

- `source_artifact`
- `batch_range`
- `excerpt_range`
- `affected_speakers`
- `relationship_state`
- `voice_failure`
- `repair_rules`
- `proof_rewrites` with original line references or before/after mapping
- `register_notes`
- `assumptions`
- `unresolved_voice_risks`
- `next_handoff_target`, usually `novel-writing` for prose integration or `series-qa` for review

The `voice_handoff` block is the handoff artifact. If it must be persisted, the caller or orchestrator saves it; this skill should not write runtime or manuscript files during an orchestrated handoff.

## Assume Script-First Mode For Dialogue Requests

When the user asks for lines that feel like actors are trading dialogue, treat that as the default mode for this skill.

Do not bypass [references/composition-guide.md](references/composition-guide.md) for dialogue-building requests that involve more than one axis. Choose the stack there first, then load only the selected files.

In script-first mode:

- output with explicit speaker labels unless the user requests another format
- prioritize turn pressure, interruption, dodge, escalation, and deflection over descriptive prose
- keep narration to the minimum needed to preserve who is speaking or what immediate pressure changed
- test every line against the immediately previous line, not against abstract scene summary
- remove lines that only explain background and do not change the exchange

Read [references/composition-guide.md](references/composition-guide.md) first, then load only the narrowest files needed for:

- exchange size
- relationship
- emotion function
- micro voice
- genre or subgenre if the texture depends on it

Always start with [references/script-dialogue-rules.md](references/script-dialogue-rules.md). Add [references/script-dialogue-samples.md](references/script-dialogue-samples.md) only when a concrete speaker-labeled example helps.

## Route The Request First

Choose the smallest deliverable that solves the user's problem:

- build a full cast voice bible when the user is designing or resetting a whole cast
- build character voice cards when only one to three speakers matter
- build a relationship register matrix when hierarchy, intimacy, or address drift is the main risk
- build pairwise contrast notes when two speakers feel interchangeable
- build a dialogue drift report when existing chapters already flatten or mismatch voices
- build rewrite rules plus proof rewrites when the user needs forward-looking guardrails, not a full rewrite
- build a dialogue exchange sheet when the user wants pure back-and-forth lines with little or no narration
- build a relationship exchange when one pair dynamic is the main scene engine
- build an emotion function exchange when one speech act such as apology, threat, or evasion dominates
- build a micro voice sheet when the failure is mostly in line texture rather than scene logic
- build a composition recipe when the user needs an explicit axis-selection plan before drafting

For a routing table, read [references/request-router.md](references/request-router.md).
For reusable output skeletons, read [references/output-templates.md](references/output-templates.md).
For multi-axis file selection and ordering, read [references/composition-guide.md](references/composition-guide.md).

## Gather Only The Inputs That Matter

Lock the minimum evidence before designing voice:

- role, age band, and social position
- who each character is above, below, or emotionally exposed to
- one or two sample lines if manuscript dialogue already exists
- genre or audience tendency only when it changes speech texture
- the scene pressure that reveals the voice failure

If the user does not provide enough information, infer only what is structurally safe and label the assumption. Do not invent ornamental quirks to fill gaps.
Exception: for orchestrated voice handoffs, missing batch/excerpt scope, affected speakers, or current relationship state is a blocker, not a safe assumption.

For fast diagnostic prompts, read [references/voice-diagnostic-questions.md](references/voice-diagnostic-questions.md).

## Start From The Voice Failure

Identify the main reason the cast sounds flat:

- multiple characters share the same sentence rhythm
- honorific choice does not match status or intimacy
- reactions differ in topic but not in emotional handling
- everyone explains information with the author's wording
- conflict lines are too explicit and carry no deflection
- relationship changes do not affect address forms or speech level

Choose the smallest voice artifact that solves the problem. Do not build a full bible if the user only needs one character pair repaired.

## Define Voice From Pressure

Do not design voice from catchphrases first. Build each speaker from:

1. what they avoid saying directly
2. how they handle status difference
3. how they react under embarrassment, anger, fear, desire, or guilt
4. whether they compress, ramble, dodge, test, soothe, provoke, or retreat
5. when their speech level rises or drops under pressure

Treat recurring line-endings as a surface symptom, not the core of the voice.

## Build Voice Through Exchange, Not Isolated Quotes

Do not validate a character voice with one clever line. Validate it in collision.

Check:

- how the speaker opens a turn
- whether they answer directly or sidestep
- how they interrupt or refuse interruption
- whether they end with closure, threat, plea, bait, or residue
- what kind of line makes them lose register control

For exchange-level patterns, read [references/dialogue-exchange-patterns.md](references/dialogue-exchange-patterns.md).

## Build The Minimum Voice Card

For each important character, lock:

- how they address each major counterpart
- how others address them
- baseline speech level
- pressure shift pattern
- typical sentence length and rhythm
- how direct or indirect they are
- how they evade, lie, confess, threaten, comfort, and apologize
- taboo subjects or exposed emotional weak points

For reusable templates, read [references/voice-profile-template.md](references/voice-profile-template.md).
For workflow order, read [references/voice-design-workflow.md](references/voice-design-workflow.md).

## Track Relationship-Specific Variants

The same speaker should not sound identical with every counterpart. Record at least the differences for:

- superior
- subordinate
- peer
- family
- love interest
- enemy or rival

When relationship state changes, update address forms, politeness, interruption tolerance, and how much subtext the speaker allows.

For relationship-dependent register control, read [references/relationship-register-matrix.md](references/relationship-register-matrix.md).

## Compare Voices Across The Cast

Test distinctness by contrast, not by isolated profile quality.

Check whether two characters:

- deliver bad news the same way
- dodge questions the same way
- show anger with the same structure
- use the same level of explicitness
- close conversations with the same emotional posture

If overlap is too high, separate them by reaction behavior before changing vocabulary.

For contrast patterns and repair examples, read [references/cast-differentiation-examples.md](references/cast-differentiation-examples.md).

## Repair Dialogue Drift

When auditing existing manuscript dialogue, diagnose:

1. voice flattening
2. register mismatch
3. implausible honorific use
4. exposition disguised as conversation
5. emotional reactions that belong to the author, not the speaker

Report the smallest viable repair rule first, then rewrite only the lines that need proof.

For long-run drift checks, read [references/dialogue-drift-checks.md](references/dialogue-drift-checks.md).
For bad-vs-fixed drift pairs only, read [references/dialogue-drift-lexicon.md](references/dialogue-drift-lexicon.md).
For reaction-level repair options, read [references/reaction-patterns.md](references/reaction-patterns.md).
For Korean before-and-after samples, read [references/korean-voice-samples.md](references/korean-voice-samples.md).
For genre-specific Korean dialogue texture, read [references/genre-voice-samples.md](references/genre-voice-samples.md).
For finer Korean fiction subgenre calibration excluding BL and GL, read [references/subgenre-voice-samples.md](references/subgenre-voice-samples.md).

## Script-First Quality Check

When delivering speaker-to-speaker dialogue, reject lines that fail any of these tests:

- the line could be moved to another speaker without anyone noticing
- the line explains what both speakers already know
- the line does not react to the immediate prior pressure
- the line sounds like summary disguised as speech
- every turn has the same length, energy, or degree of directness
- the exchange reaches the point too cleanly and leaves no friction

Keep the scene moving through speech acts such as refusal, baiting, appeasement, delay, pressure, misdirection, and partial admission.

Also check the exchange shape:

- in two-person dialogue, verify that pressure bounces cleanly without dead turns
- in three-person dialogue, verify that the third speaker changes alignment, pace, or information flow
- in group dialogue, verify that not everyone speaks at equal weight or in the same register
- in relationship-specific dialogue, verify that address, permission, and emotional exposure match the pair
- in emotion-function dialogue, verify that every turn performs the intended function rather than merely naming the feeling
- in micro-voice dialogue, verify that filler words, line length, pauses, and turn edges support the voice instead of becoming gimmicks

## Run A Distinctness Check Before Finalizing

Do not stop after writing profiles. Stress-test whether the voices remain distinct when names are removed.

Check whether a blind reader could still identify:

- who answers too fast
- who buys time before answering
- who protects face or hierarchy first
- who leaks worry while refusing
- who escalates openly versus politely
- who leaves emotional residue at the end of the turn
- who uses clipped lines versus expanding under pressure
- who buys time with pauses, fillers, or repeated starts
- who opens and closes turns in a recognizable way

If the distinction depends mainly on repeated catchphrases, rebuild the reaction logic.

## Output Contract

Choose the output that matches the request:

- cast voice bible
- character voice cards
- relationship register matrix
- pairwise contrast notes
- dialogue drift report
- dialogue exchange sheet
- relationship exchange
- emotion function exchange
- micro voice sheet
- composition recipe
- rewrite rules for future chapters
- orchestrated `voice_handoff`

Prefer compact tables and bullet rules over abstract theory.
Always include enough concrete proof that another Codex instance could apply the result without re-deriving the logic.

Unless the user explicitly asks for prose outside an orchestrated handoff, keep outputs diagnostic and operational:

- identify the failure
- state the repair rule
- show one or two proof rewrites or sample contrasts
- prefer speaker-labeled turns over narrated explanation
- end with guardrails for future chapters

For orchestrated voice work, keep future guardrails limited to reusable voice rules. Do not include future-batch plot beats, next-scene instructions, or unresolved-story planning.

If the user asks for scene or chapter prose, use this skill to define the voices first, then hand off narration, scene blocking, and prose execution to `novel-writing`.
In orchestrated handoffs, even explicit prose pressure should be reduced to voice rules and proof rewrites, then handed to `novel-writing` for integration.

## Operating Rules

- For any dialogue-building request that combines exchange size, relationship, emotion function, micro voice, genre, or repair, route through [references/composition-guide.md](references/composition-guide.md) first.
- Differentiate speakers by reaction logic, social handling, and emotional leakage before changing word choice.
- Keep Korean honorifics, titles, and address forms tied to hierarchy, intimacy, and the immediate scene temperature.
- Let voice shift under pressure, but keep the direction of the shift consistent.
- Treat silence, delay, hedging, and partial answers as part of voice design.
- In dialogue-first requests, make each turn do work against the previous turn.
- When revising, preserve scene intent and information flow before beautifying the line.
- If a line sounds distinct only because of a gimmick phrase, rebuild the underlying reaction pattern.
- Do not drift into narration-heavy scene polish when the user's real need is spoken-line control.
- For orchestrated voice handoffs, return repair guidance and proof rewrites only; leave manuscript editing, runtime updates, QA acceptance, and recovery planning to their owning skills.

## Relationship To Other Skills

Use this skill for cast voice architecture, spoken-line design, and dialogue drift repair.

- Use `novel-writing` for narration, scene drafting, prose revision, and chapter execution.
- Use `longform-story-design` for series bibles, continuity ledgers, and chapter-range planning.

This skill should feed those layers by giving them stable speaking behavior and register rules.

## Resource Map

- Read [references/request-router.md](references/request-router.md) when you need to decide the smallest useful deliverable and the minimum files to load.
- Read [references/composition-guide.md](references/composition-guide.md) when you need to combine exchange size, relationship, emotion function, micro voice, and genre without loading unnecessary files.
- Read [references/output-templates.md](references/output-templates.md) when you need compact output shapes for bibles, cards, reports, or rewrite rules.
- Read [references/voice-diagnostic-questions.md](references/voice-diagnostic-questions.md) when the brief or manuscript is too thin and you need the minimum follow-up prompts.
- Read [references/script-dialogue-rules.md](references/script-dialogue-rules.md) when the user wants actor-like back-and-forth dialogue with minimal narration.
- Read [references/script-dialogue-samples.md](references/script-dialogue-samples.md) when you need compact speaker-labeled examples that move only through spoken turns.
- Read [references/two-person-dialogue.md](references/two-person-dialogue.md) when the scene is a tight one-on-one exchange and every line should strike the counterpart directly.
- Read [references/three-person-dialogue.md](references/three-person-dialogue.md) when a third speaker should complicate alignment, authority, or pacing rather than just take turns.
- Read [references/group-dialogue.md](references/group-dialogue.md) when handling four or more speakers, meeting scenes, squads, classrooms, or family confrontations.
- Read [references/relationship-superior-subordinate.md](references/relationship-superior-subordinate.md) when hierarchy, permission, deference, or controlled pushback drive the exchange.
- Read [references/relationship-rivals.md](references/relationship-rivals.md) when conflict, comparison, or face protection should sharpen every turn.
- Read [references/relationship-pre-romance.md](references/relationship-pre-romance.md) when attraction must leak through restraint, misdirection, and incomplete admission.
- Read [references/relationship-family.md](references/relationship-family.md) when familiarity, old grievances, kinship address, or role fatigue shape the dialogue.
- Read [references/relationship-colleagues.md](references/relationship-colleagues.md) when shared work, professional caution, and procedural conflict carry the scene.
- Read [references/emotion-function-interrogation.md](references/emotion-function-interrogation.md) when one speaker must corner, narrow, or force specificity from another.
- Read [references/emotion-function-evasion.md](references/emotion-function-evasion.md) when a speaker must hide, deflect, stall, or substitute answers under pressure.
- Read [references/emotion-function-seduction.md](references/emotion-function-seduction.md) when attraction, temptation, or strategic intimacy should move indirectly through tone and pace.
- Read [references/emotion-function-apology.md](references/emotion-function-apology.md) when hurt, accountability, resistance, and changed behavior must shape the exchange.
- Read [references/emotion-function-threat.md](references/emotion-function-threat.md) when danger should be conveyed through leverage, certainty, or implied consequence rather than volume alone.
- Read [references/emotion-function-soothing.md](references/emotion-function-soothing.md) when one speaker must calm, stabilize, or lower the other's temperature without flattening voice.
- Read [references/micro-voice-catchphrases.md](references/micro-voice-catchphrases.md) when repeated fillers, habitual phrasing, or speech tics need to be constrained so they support voice without becoming parody.
- Read [references/micro-voice-sentence-length.md](references/micro-voice-sentence-length.md) when voice should separate through compression, expansion, and how much information fits in one turn.
- Read [references/micro-voice-pauses.md](references/micro-voice-pauses.md) when silence, ellipses, false starts, or interruption behavior need to carry personality.
- Read [references/micro-voice-question-style.md](references/micro-voice-question-style.md) when characters differ mainly in how they ask, press, test, or feign questions.
- Read [references/micro-voice-turn-edges.md](references/micro-voice-turn-edges.md) when speakers need distinct ways of entering and leaving a turn.
- Read [references/dialogue-exchange-patterns.md](references/dialogue-exchange-patterns.md) when you need repeatable turn structures for confrontation, flirting, concealment, persuasion, or apology.
- Read [references/voice-design-workflow.md](references/voice-design-workflow.md) when you need the order for building or repairing a cast-wide voice system.
- Read [references/voice-profile-template.md](references/voice-profile-template.md) when you need fill-in templates for character voice cards.
- Read [references/relationship-register-matrix.md](references/relationship-register-matrix.md) when honorifics, titles, intimacy shifts, or hierarchy handling are the main risk.
- Read [references/reaction-patterns.md](references/reaction-patterns.md) when distinctness should come from emotional behavior rather than vocabulary swaps.
- Read [references/dialogue-drift-checks.md](references/dialogue-drift-checks.md) when existing chapters need an audit for flattening, mismatch, or drift.
- Read [references/dialogue-drift-lexicon.md](references/dialogue-drift-lexicon.md) when you need a fast repair dictionary made only of bad examples and tightened fixes.
- Read [references/cast-differentiation-examples.md](references/cast-differentiation-examples.md) when two or more speakers still sound too similar after basic cleanup.
- Read [references/korean-voice-samples.md](references/korean-voice-samples.md) when you need concrete Korean dialogue samples for contrast, drift repair, or relationship-driven register shifts.
- Read [references/genre-voice-samples.md](references/genre-voice-samples.md) when genre expectations should change dialogue temperature, directness, status texture, or emotional pacing.
- Read [references/subgenre-voice-samples.md](references/subgenre-voice-samples.md) when broad genre labels are too loose and the user needs Korean web-fiction subgenre texture such as rom-fantasy, regression, hunter, academy, revenge, thriller, or office drama, excluding BL and GL.
