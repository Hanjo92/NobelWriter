# Composition Guide

Use this file when one dialogue task needs more than one axis at once.

## Goal

Build the smallest working stack of references instead of loading every file.

This file is the required entry point for any dialogue-building request that combines two or more axes. Do not bypass it by loading multiple axis files directly unless the user explicitly asks for that override.

## Composition Order

Choose files in this order:

1. `script-dialogue-rules.md`
2. one exchange-size file:
   `two-person-dialogue.md` or `three-person-dialogue.md` or `group-dialogue.md`
3. zero or one relationship file
4. zero or one emotion-function file
5. zero or one micro-voice file
6. zero or one genre or subgenre file
7. optional repair overlay:
   `dialogue-drift-checks.md` or `dialogue-drift-lexicon.md`

Do not load more than one file from the same axis unless the user explicitly asks for a hybrid or the scene clearly needs two independent pressures from that axis.

## Selection Rules

### Exchange Size

Choose the file that matches how many speakers actively shape the pressure.

- `two-person-dialogue.md`: one-on-one collision
- `three-person-dialogue.md`: third speaker changes alignment or register
- `group-dialogue.md`: four or more active speakers or room dynamics

### Relationship

Choose a relationship file only when permission, intimacy, or face-management is part of the problem.

- `relationship-superior-subordinate.md`
- `relationship-rivals.md`
- `relationship-pre-romance.md`
- `relationship-family.md`
- `relationship-colleagues.md`

### Emotion Function

Choose the main speech act driving the exchange.

- `emotion-function-interrogation.md`
- `emotion-function-evasion.md`
- `emotion-function-seduction.md`
- `emotion-function-apology.md`
- `emotion-function-threat.md`
- `emotion-function-soothing.md`

### Micro Voice

Choose only the one micro layer that is most visible in the failure.

- `micro-voice-catchphrases.md`
- `micro-voice-sentence-length.md`
- `micro-voice-pauses.md`
- `micro-voice-question-style.md`
- `micro-voice-turn-edges.md`

### Genre

Add genre or subgenre only when the same exchange would materially sound different by setting or audience expectation.

- `genre-voice-samples.md`
- `subgenre-voice-samples.md`

### Repair Overlay

Add a repair file only when revising existing dialogue instead of building fresh dialogue.

- `dialogue-drift-checks.md`: audit checklist
- `dialogue-drift-lexicon.md`: bad/fixed repair pairs

## Fast Recipes

### Tight Rival Interrogation

Load:

- `script-dialogue-rules.md`
- `two-person-dialogue.md`
- `relationship-rivals.md`
- `emotion-function-interrogation.md`
- `micro-voice-sentence-length.md`

Use when:

- two rivals corner each other
- turns should tighten fast
- one speaker cuts short while the other stays pointed

### Pre-Romance With Evasion

Load:

- `script-dialogue-rules.md`
- `two-person-dialogue.md`
- `relationship-pre-romance.md`
- `emotion-function-evasion.md`
- `micro-voice-pauses.md`

Use when:

- attraction must leak through avoidance
- neither side can answer cleanly
- pauses and partial replies matter more than overt confession

### Hierarchy Conflict In Office Drama

Load:

- `script-dialogue-rules.md`
- `two-person-dialogue.md`
- `relationship-superior-subordinate.md`
- `relationship-colleagues.md`
- `emotion-function-interrogation.md`
- `genre-voice-samples.md`

Use when:

- work hierarchy and procedural conflict both matter
- the subordinate must push back without casual collapse

This is an intentional hybrid stack inside the relationship axis.
If the stack feels too heavy, keep the stricter relationship file and drop the softer one.

### Three-Person Family Blowup

Load:

- `script-dialogue-rules.md`
- `three-person-dialogue.md`
- `relationship-family.md`
- `emotion-function-threat.md` or `emotion-function-apology.md`
- `micro-voice-turn-edges.md`

Use when:

- one family member changes the alignment
- old history leaks through how turns begin and end

### Group Crisis Scene

Load:

- `script-dialogue-rules.md`
- `group-dialogue.md`
- one relationship file only if the hierarchy is central
- one emotion-function file only if a single speech act dominates
- `subgenre-voice-samples.md` if the setting is hunter, academy, murim, or similar

Use when:

- a room or squad needs differentiated functions
- not everyone should speak at equal weight

## Conflict Resolution Between Axes

When two files pull in different directions, prioritize in this order:

1. exchange size
2. relationship
3. emotion function
4. genre or subgenre
5. micro voice

Micro voice should decorate the deeper structure, not override it.

## Stop Rule

Stop loading files once you can answer these five questions:

- Who controls pace?
- Who may interrupt whom?
- What is the scene's main speech act?
- What one micro habit makes each important speaker feel different?
- What setting texture must stay audible?

If all five are answerable, write the dialogue.
