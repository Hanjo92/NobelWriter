# Dialogue Revision Selection

Use this file when a draft already exists and you need a compact prompt to revise dialogue rather than generate from zero.

## How To Use

1. Identify the main problem.
2. Pick the revision goal.
3. Pick the genre and audience if they materially affect the line texture.
4. Copy the block and revise only the minimum needed.

Preserve scene intent, relationship status, and plot meaning unless the user explicitly asks for a rewrite.

## Core Revision Prompt

```text
Revise this Korean dialogue.
Genre: [genre]
Audience tendency: [male-oriented / female-oriented / neutral]
Primary problem: [stiff / expository / same-voice / wrong register / too direct / too flat / melodramatic]
Revision goal: [naturalize / sharpen / soften / increase subtext / reduce exposition / differentiate voices]
Rule: Preserve scene intent, relationship dynamics, and factual meaning.
Dialogue rule: Make each line respond to the prior line or current pressure and sound like spoken Korean.
```

## Problem Rows

### Stiff

```text
Loosen written syntax into spoken Korean. Shorten where possible and remove sentence-complete logic that people would not actually say aloud.
```

### Expository

```text
Remove information both speakers already know. Shift explanation into subtext, gesture, or narration where possible.
```

### Same-Voice

```text
Differentiate rhythm, directness, vocabulary, and speech endings by personality, age, status, and emotional habit.
```

### Wrong Register

```text
Correct honorifics, titles, speech endings, and relationship distance. Make the social level consistent with the scene.
```

### Too Direct

```text
Add indirection, evasion, or emotional cover where the relationship or status would make blunt speech unlikely.
```

### Too Flat

```text
Increase pressure, reaction, or hidden intent without over-explaining emotion.
```

### Melodramatic

```text
Reduce decorative intensity and turn abstract feeling into speakable, scene-specific language.
```

## Revision Goal Rows

### Naturalize

```text
Make the dialogue easier to say than to read. Cut polish, keep pressure.
```

### Sharpen

```text
Shorten the line, remove padding, and place the sting or turn late in the sentence.
```

### Soften

```text
Reduce frontal accusation and add space for hesitation, retreat, or emotional protection.
```

### Increase Subtext

```text
Let characters imply, dodge, or redirect instead of naming the full emotional or factual content.
```

### Reduce Exposition

```text
Keep only what must be spoken aloud for the scene to work. Move the rest out of dialogue.
```

### Differentiate Voices

```text
Give each speaker a distinct level of brevity, politeness, emotional leakage, and choice of wording.
```

## Fast Selection Table

| Problem | Best goal | What to change first |
| --- | --- | --- |
| Too literary | Naturalize | Shorten syntax, remove written phrasing |
| Feels like explanation | Reduce exposition | Cut shared facts, add implication |
| Both characters sound same | Differentiate voices | Change rhythm, level, and diction |
| Too blunt for relationship | Soften or increase subtext | Add dodge, restraint, indirectness |
| No tension in exchange | Sharpen or increase subtext | Add turn, pressure, or withheld meaning |
| Feels overacted | Naturalize or soften | Remove abstract emotional labels |

## Genre Add-Ons

### Traditional Fantasy

```text
Preserve rank, decorum, oath pressure, and public consequence. Do not modernize the social texture.
```

### Martial Arts

```text
Preserve sect etiquette, rivalry heat, and tactical brevity. Let courtesy and threat coexist if needed.
```

### Modern Fantasy

```text
Use contemporary spoken Korean. Keep dialogue grounded in practical stakes and live response.
```

### Fusion Fantasy

```text
Preserve strategic calculation, leverage, and mixed-system confidence. Let lines carry more than one layer when useful.
```

### Romance

```text
Preserve hesitation, attraction, pride, and relational timing. Let emotional movement sit inside the exchange.
```

### Horror

```text
Preserve fear, denial, and survival logic. Keep lines reactive, slightly incomplete when pressure is high, and grounded in what the character can immediately sense or suspect.
```

Subgenre selectors:

- psychological horror: increase self-doubt, hesitation, and fear of naming the wrongness too directly
- ghost story: let recognition, taboo, and half-belief sit inside the line
- creature horror: favor warning, command, breath-short denial, and physical immediacy

### Mystery

```text
Preserve clue logic, suspicion, and conversational testing. Let lines probe contradiction, motive, or timing without dumping the entire explanation.
```

Subgenre selectors:

- deduction mystery: make lines fact-led and inference-aware
- suspense mystery: let danger and mistrust warp how much each speaker says
- investigation mystery: keep testimony, procedure, and omission clearly separable

## Ready-Made Blocks

### Naturalize Expository Modern Fantasy Dialogue

```text
Revise this Korean dialogue.
Genre: modern fantasy
Audience tendency: neutral
Primary problem: expository
Revision goal: naturalize and reduce exposition
Rule: Preserve plot meaning, but remove information the speakers would not naturally say aloud.
Dialogue rule: Make each line short, reactive, and grounded in the immediate danger or task.
```

### Sharpen Male-Oriented Martial Arts Dialogue

```text
Revise this Korean dialogue.
Genre: martial arts
Audience tendency: male-oriented
Primary problem: too flat
Revision goal: sharpen
Rule: Preserve challenge and rivalry.
Dialogue rule: Make each line brief, confrontational, and status-aware.
```

### Soften Female-Oriented Romance Dialogue

```text
Revise this Korean dialogue.
Genre: romance
Audience tendency: female-oriented
Primary problem: too direct
Revision goal: soften and increase subtext
Rule: Preserve attraction and hurt without flattening either.
Dialogue rule: Let hesitation, reaction, and emotional self-protection shape the lines.
```

### Tighten Neutral Horror Dialogue

```text
Revise this Korean dialogue.
Genre: horror
Audience tendency: neutral
Primary problem: too flat
Revision goal: naturalize and sharpen
Rule: Preserve fear and uncertainty, but make each line sound like it is spoken under immediate unease.
Dialogue rule: Keep lines short, sensory-aware, and responsive to the latest sound, sight, or movement.
```

### Increase Subtext In Female-Oriented Mystery Dialogue

```text
Revise this Korean dialogue.
Genre: mystery
Audience tendency: female-oriented
Primary problem: expository
Revision goal: increase subtext and reduce exposition
Rule: Preserve the clue and motive tension, but let suspicion move through observation and implication.
Dialogue rule: Make the speakers test each other instead of explaining the whole case aloud.
```

### Naturalize Psychological Horror Dialogue

```text
Revise this Korean dialogue.
Genre: horror
Audience tendency: female-oriented
Primary problem: too direct
Revision goal: increase subtext and naturalize
Rule: Preserve the fear, but make the speaker sound unsure whether they should trust what they noticed.
Dialogue rule: Let the line circle the wrongness before naming it. Keep the speech intimate and speakable.
```

### Tighten Creature Horror Dialogue

```text
Revise this Korean dialogue.
Genre: horror
Audience tendency: male-oriented
Primary problem: stiff
Revision goal: sharpen
Rule: Preserve the urgency and survival information.
Dialogue rule: Cut every line down to what could actually be shouted, warned, or refused while running or hiding.
```

### Sharpen Deduction Mystery Dialogue

```text
Revise this Korean dialogue.
Genre: mystery
Audience tendency: neutral
Primary problem: expository
Revision goal: sharpen and reduce exposition
Rule: Preserve the clue logic, but move from lecture-like explanation to observable contradiction.
Dialogue rule: Let each line introduce, test, or reject one fact.
```

### Tense Suspense Mystery Dialogue

```text
Revise this Korean dialogue.
Genre: mystery
Audience tendency: female-oriented
Primary problem: too flat
Revision goal: increase subtext
Rule: Preserve the surface topic, but let the danger come from what neither speaker will say plainly.
Dialogue rule: Make trust feel unstable line by line.
```
