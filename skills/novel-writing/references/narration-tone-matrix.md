# Narration Tone Matrix

Use this file when you need a compact rule table for fixing Korean narration that is meaningful but awkward to read.

## How To Use

1. Identify the main sentence problem.
2. Identify the target effect.
3. Apply the matching rule row.
4. Add the genre and audience modifiers only if they materially change the line.

Keep meaning fixed unless the user explicitly asks for broader rewriting.

## Core Rule

Do not preserve awkwardness in the name of literal meaning.
Do not preserve narration that still shows the scaffolding of note-first thinking.

Keep these fixed:

- factual meaning
- emotional direction
- scene function
- POV ownership
- POV distance unless the user explicitly asks to change it

Change these when needed:

- word order
- sentence length
- clause order
- image choice
- abstraction level
- landing word

## Meaning-First Trace Table

| If the sentence feels like... | Likely trace | Rewrite move |
| --- | --- | --- |
| an outline sentence expanded into prose | meaning blocks still visible | reduce to one image, one action, one pressure |
| a summary of feeling | abstract emotional diagnosis | show reaction, posture, or sensory shift |
| a summary of thought | thought explained from outside | move into focalized perception or decision |
| a summary of tension | conflict named instead of dramatized | let setting, action, or timing carry pressure |

## Problem -> Fix Table

| Problem | First fix | What to remove | What to add |
| --- | --- | --- | --- |
| Translation-like | Rebuild in Korean word order | English-shaped logic, abstract connectors | direct movement, natural connective flow |
| Lexically purified | Restore expected literary vocabulary | forced native replacements, clumsy paraphrases | ordinary high-frequency words |
| Subject arrives too late | Pull subject forward | long lead-in clauses | early actor or focal point |
| Modifier pile-up | Cut or split modifiers | stacked adjectives, progressives | one main image |
| Rhythm drags | Rebalance sentence weight | repeated similar phrasing | cleaner landing word |
| Too abstract | Convert emotion/thought to reaction | abstract nouns, explanation | gesture, image, verb |
| Too flat | Sharpen one image or verb | generic labels | pressure, concrete detail |
| Overwritten | Compress | decorative fillers | precision |
| Hard to track POV | Re-anchor perception | floating observations | clear perceiver |
| First-person drift | Rebuild inside narrator voice | outside diagnosis, impossible self-observation | plausible self-noticing, thought texture |
| Third-person drift | Re-anchor limited access | stray mind-reading, ownerless summary | focalized observation, stable perceiver |
| Meaning-first scaffolding | Rebuild from scene pressure | explicit semantic staging | one natural line of prose |

## Goal -> Rule Table

| Goal | Rule |
| --- | --- |
| Naturalize | Rewrite into the order and cadence a Korean reader expects on first pass. |
| Simplify | Keep only what this beat needs; cut any structure that delays comprehension. |
| Improve rhythm | Vary weight and place the strongest word or image at the sentence end. |
| Sharpen image | Replace summary nouns with one visible, audible, or physical detail. |
| Compress | Merge duplicated meaning and remove explanatory padding. |
| Clarify subject | Make it instantly clear who acts, feels, notices, or changes. |
| Repair first-person ownership | Make the line sound thinkable or narratable by this specific narrator rather than by an outside analyst. |
| Repair third-person ownership | Keep the sentence inside the active focal character's access and remove unexplained entry into other interiors. |
| Increase atmosphere | Add one setting-charged image without slowing the sentence. |
| Increase emotional clarity | Show feeling through reaction or pressure, not diagnosis language. |
| Remove scaffolding | Rewrite from image, movement, or focal perception rather than abstract plan language. |
| Normalize diction | Replace conspicuous word choices with the vocabulary a Korean fiction reader would expect. |

## Genre Modifier Table

| Genre | Narration bias |
| --- | --- |
| Traditional fantasy | measured gravity, rank-aware texture, public consequence |
| Martial arts | lean observation, force and posture, tactical clarity |
| Modern fantasy | practical immediacy, urban readability, anomaly clarity |
| Fusion fantasy | compressed strategy, layered systems, political leverage |
| Romance | emotional timing, reaction texture, relational focus |
| Horror | sensory mismatch, unsafe familiarity, delayed confirmation |
| Mystery | clue legibility, contradiction pressure, motive-aware restraint |

### Subgenre Modifiers

Use these after the genre modifier when the user asks for a narrower horror or mystery texture.

| Subgenre | Narration bias |
| --- | --- |
| Psychological horror | intimate wrongness, unstable certainty, inward recoil |
| Ghost story | recurrence, place memory, ritual residue, familiar impossibility |
| Creature horror | embodied threat, motion, contamination, immediate bodily stakes |
| Deduction mystery | precise observation, inference discipline, elegant contradiction |
| Suspense mystery | withheld motive, unstable trust, danger under partial knowledge |
| Investigation mystery | procedural sequence, testimony friction, accumulating trace |

## Audience Modifier Table

| Audience tendency | Narration bias |
| --- | --- |
| Male-oriented | faster motion, capability pressure, less emotional explanation |
| Female-oriented | relational reading, emotional implication, social texture |
| Neutral | broad readability, balanced pressure and feeling |

## Formula Table

Use this formula:

```text
Base meaning
+ problem fix
+ goal rule
+ genre modifier
+ audience modifier
= revised sentence direction
```

Example:

```text
Base meaning: she realized the room had changed
+ problem fix: subject arrives too late
+ goal rule: clarify subject
+ genre modifier: romance
+ audience modifier: female-oriented
= put her perception first, show the room change through emotional atmosphere
```

## Fast Decision Table

| If the line feels like... | Choose problem | Choose goal |
| --- | --- | --- |
| 번역한 문장 | Translation-like | Naturalize |
| 너무 길어서 걸림 | Modifier pile-up or rhythm drags | Simplify or compress |
| 무슨 말인지는 알겠는데 맛이 없음 | Too flat | Sharpen image |
| 감정 설명만 있음 | Too abstract | Increase emotional clarity |
| 시점이 흐림 | Hard to track POV | Clarify subject |
| 분위기는 있는데 안 읽힘 | Overwritten | Improve rhythm |
| 뜻은 맞는데 작위적으로 조립한 느낌 | Meaning-first scaffolding | Remove scaffolding |
| 한국어화가 과해서 단어가 튐 | Lexically purified | Normalize diction |

## Ready-Made Prompt Blocks

### Naturalize Korean Narration

```text
Revise this Korean narration.
Primary problem: translation-like or awkward flow
Goal: naturalize
Rule: Preserve meaning and emotional direction, but rebuild the sentence in natural Korean order and cadence.
Check: The sentence should read cleanly on first pass.
```

### Sharpen Genre Narration

```text
Revise this Korean narration.
Primary problem: too flat
Goal: sharpen image
Genre modifier: apply the requested genre's narrative bias without bloating the sentence.
Rule: Replace abstraction with one concrete, scene-relevant image or verb.
```

### Compress Emotional Narration

```text
Revise this Korean narration.
Primary problem: overwritten or too abstract
Goal: compress and increase emotional clarity
Rule: Keep the feeling, but show it through reaction, pressure, or one clean image instead of explanation.
```

### Normalize Over-Purified Diction

```text
Revise this Korean narration.
Primary problem: lexically purified diction
Goal: normalize diction
Rule: Preserve the meaning, but replace awkward native-only substitutions with the natural vocabulary a Korean fiction reader would expect.
Check: No single word should feel like it was chosen to prove Koreanness rather than to serve the scene.
```

### Repair First-Person Narration

```text
Revise this Korean narration.
Primary problem: first-person drift
Goal: repair first-person ownership
Rule: Preserve meaning, but make the line sound like the narrator's own perception, memory, or judgment rather than outside commentary.
Check: The sentence should not claim knowledge or camera distance the narrator cannot plausibly hold.
```

### Repair Third-Person Limited Narration

```text
Revise this Korean narration.
Primary problem: third-person drift
Goal: repair third-person ownership
Rule: Preserve meaning, but keep the sentence inside the active focal character's access and distance.
Check: Remove unexplained access to non-POV interior states and re-anchor the line to the current perceiver.
```

### Remove Meaning-First Scaffolding

```text
Revise this Korean narration.
Primary problem: meaning-first scaffolding
Goal: remove scaffolding
Rule: Preserve the meaning, but rewrite as if the sentence were first conceived in Korean prose rather than in abstract outline language.
Check: The revised line should feel discovered through scene perception, not assembled from semantic parts.
```
