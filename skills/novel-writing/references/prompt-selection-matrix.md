# Prompt Selection Matrix

Use this file when you want a compact prompt block instead of assembling instructions from scratch.

## How To Use

1. Pick the closest genre.
2. Pick the target audience tendency.
3. Pick the scene or dialogue intent.
4. Copy the prompt block and adjust only the nouns specific to the scene.

Keep the block short. The goal is to steer output, not over-script it.

## Core Prompt Template

```text
Write this scene in Korean.
Genre: [genre]
Audience tendency: [male-oriented / female-oriented / neutral]
Scene intent: [intent]
Narrative priority: [hook / tension / intimacy / escalation / reassurance / suspicion]
Dialogue rule: Make every line react to the immediately prior line and sound like spoken Korean in this context.
Style rule: Preserve character intent, relationship status, and scene pressure. Avoid exposition disguised as dialogue.
```

## Genre Rows

### Traditional Fantasy

Use when:
- oath, rank, kingdom, war, prophecy, succession, court pressure

Prompt add-on:
```text
Use traditional fantasy diction with clear hierarchy, public consequence, and measured gravitas. Let dialogue carry duty, rank, and pressure without turning theatrical unless the scene explicitly requires it.
```

### Martial Arts

Use when:
- sects, masters, disciples, duels, jianghu conflict, honor, technique

Prompt add-on:
```text
Use murim-appropriate Korean with restrained intensity. Keep exchanges sharp, status-aware, and efficient. Let courtesy and threat coexist when needed.
```

### Modern Fantasy

Use when:
- urban setting, awakening, guilds, hunters, hidden powers, systems, anomalies

Prompt add-on:
```text
Use modern, spoken Korean with practical pacing. Keep the hook immediate, the stakes legible, and the dialogue tied to action, risk, and real-time decision making.
```

### Fusion Fantasy

Use when:
- mixed systems, regression, empire politics, magic engineering, status conflict

Prompt add-on:
```text
Use a hybrid fantasy tone where political calculation and power progression coexist. Let dialogue carry strategy, leverage, and layered threat or attraction.
```

### Romance

Use when:
- attraction, emotional push-pull, denial, confession, reassurance, relational tension

Prompt add-on:
```text
Use intimate spoken Korean that tracks hesitation, subtext, and emotional timing. Let attraction appear through reaction, avoidance, or small shifts in speech before explicit confession.
```

### Horror

Use when:
- haunted spaces, contamination, uncanny return, pursuit, body fear, violated safety

Prompt add-on:
```text
Use Korean prose that makes the threat concrete before it becomes ornate. Let fear appear through sensory mismatch, hesitation, and practical choices under dread. Avoid vague spooky language that does not change the scene.
```

Subgenre selectors:

- psychological horror: make ordinary details become unreliable and let dialogue carry denial, self-checking, and fear of sounding irrational
- ghost story: tie the dread to place memory, return, taboo, or unresolved grief; let recognition arrive before explanation
- creature horror: keep threat embodied and immediate; favor pursuit, contamination, warning, and survival choices

### Mystery

Use when:
- clues, hidden motives, disappearances, suspicious testimony, investigations, locked-room tension

Prompt add-on:
```text
Use clear, controlled Korean that keeps clues legible and suspicion active. Let dialogue probe motive, timing, and contradiction without turning into pure exposition.
```

Subgenre selectors:

- deduction mystery: foreground contradiction, inference, and clean clue logic
- suspense mystery: foreground pressure, unstable trust, and danger linked to missing information
- investigation mystery: foreground testimony, records, procedural steps, and accumulating evidence

## Audience Rows

### Male-Oriented

Prompt add-on:
```text
Prioritize momentum, clear conflict, practical leverage, and concise dialogue. Keep emotional pressure visible, but avoid over-explaining feelings.
```

### Female-Oriented

Prompt add-on:
```text
Prioritize emotional interpretation, relational pressure, subtext, and reaction beats. Let dialogue register what is felt as well as what is said.
```

### Neutral

Prompt add-on:
```text
Balance plot readability, emotional clarity, and natural dialogue. Avoid leaning too hard into market-coded diction on either side.
```

## Intent Rows

### Hook Opening

Prompt add-on:
```text
Open with a situation change, pressure point, or revelation within the first few lines. Do not spend the opening on explanation.
```

### Suspicion

Prompt add-on:
```text
Make dialogue probe, dodge, and test. Let distrust appear through what is withheld, not only what is said directly.
```

### Comfort

Prompt add-on:
```text
Make reassurance feel speakable and specific to the moment. Prefer presence, action, or shared burden over abstract encouragement.
```

### Threat

Prompt add-on:
```text
Keep threat economical. Let the danger land through certainty, leverage, or implied consequence rather than long declarations.
```

### Flirtation

Prompt add-on:
```text
Keep attraction in timing, deflection, and reaction. Avoid generic compliments unless the character would realistically say them.
```

### Refusal

Prompt add-on:
```text
Preserve the refusal clearly, but shape it through the speaker's status, emotional restraint, and relationship to the listener.
```

### Controlled Anger

Prompt add-on:
```text
Show anger through clipped lines, restraint, or sharpened wording. Do not let the dialogue become melodramatic unless the scene earns it.
```

## Fast Selection Table

| Need | Choose | Add |
| --- | --- | --- |
| Fast hook with power pressure | Traditional fantasy or fusion fantasy + male-oriented + hook opening | Emphasize consequence and forward momentum |
| Emotional confrontation with decorum | Traditional fantasy or martial arts + female-oriented + controlled anger or refusal | Keep courtesy while letting hurt show |
| Urban banter under danger | Modern fantasy + neutral or male-oriented + suspicion or threat | Keep lines short and tactical |
| Slow-burn attraction | Romance + female-oriented or neutral + flirtation | Use subtext and reaction beats |
| Tactical dominance | Fusion fantasy + male-oriented + threat | Use leverage and calculation |
| Gentle reassurance | Romance or modern fantasy + neutral or female-oriented + comfort | Use presence and concrete action |
| Claustrophobic dread | Horror + neutral or female-oriented + threat or suspicion | Use sensory mismatch and delayed confirmation |
| Fast clue pressure | Mystery + male-oriented or neutral + suspicion | Keep clues concrete and questions escalating |
| Unstable inner dread | Horror + psychological + female-oriented or neutral + suspicion | Use intimate wrongness and self-doubt |
| Ritual return dread | Horror + ghost story + neutral + hook opening | Use place memory, recurrence, and taboo |
| Chase-first fear | Horror + creature horror + male-oriented + threat | Use body risk and survival decisions |
| Elegant clue break | Mystery + deduction + male-oriented or neutral + suspicion | Use contradiction before theory |
| Hidden liar pressure | Mystery + suspense + female-oriented or neutral + suspicion | Use motive-reading and unstable trust |
| Case-building scene | Mystery + investigation + neutral + hook opening or suspicion | Use testimony, records, and procedural friction |

## Ready-Made Prompt Blocks

### Traditional Fantasy Female-Oriented Comfort

```text
Write this scene in Korean.
Genre: traditional fantasy
Audience tendency: female-oriented
Scene intent: comfort under status pressure
Dialogue rule: Make each line respond to the immediately prior line and preserve formal distance where appropriate.
Style rule: Let reassurance pass through trust, decorum, and emotional restraint. Avoid blunt modern phrasing.
```

### Martial Arts Male-Oriented Challenge

```text
Write this scene in Korean.
Genre: martial arts
Audience tendency: male-oriented
Scene intent: challenge before conflict
Dialogue rule: Keep lines short, sharp, and speakable.
Style rule: Let rivalry, pride, and technique drive the exchange. Avoid long explanatory lines.
```

### Modern Fantasy Neutral Suspicion

```text
Write this scene in Korean.
Genre: modern fantasy
Audience tendency: neutral
Scene intent: suspicion during live danger
Dialogue rule: Make characters test each other while staying grounded in the immediate situation.
Style rule: Use practical spoken Korean. Let distrust show through incomplete answers and redirected questions.
```

### Fusion Fantasy Male-Oriented Threat

```text
Write this scene in Korean.
Genre: fusion fantasy
Audience tendency: male-oriented
Scene intent: strategic threat
Dialogue rule: Keep the line economical and dominant.
Style rule: Let power, leverage, and tactical certainty shape the voice.
```

### Romance Female-Oriented Soft Refusal

```text
Write this scene in Korean.
Genre: romance
Audience tendency: female-oriented
Scene intent: soft refusal with lingering affection
Dialogue rule: Let each line carry hesitation, self-protection, and reaction to the other person's emotional state.
Style rule: Use intimate spoken Korean with subtext. Avoid flat confession language.
```

### Romance Neutral Reassurance

```text
Write this scene in Korean.
Genre: romance
Audience tendency: neutral
Scene intent: honest reassurance
Dialogue rule: Make the reassurance short, natural, and responsive.
Style rule: Favor clarity and warmth over ornate sentiment.
```

### Horror Neutral Threat

```text
Write this scene in Korean.
Genre: horror
Audience tendency: neutral
Scene intent: threat inside a confined space
Dialogue rule: Keep each line short, reactive, and shaped by immediate fear or denial.
Style rule: Make the dread concrete through sound, space, and what the characters notice too late. Avoid decorative horror wording.
```

### Mystery Female-Oriented Suspicion

```text
Write this scene in Korean.
Genre: mystery
Audience tendency: female-oriented
Scene intent: suspicion during a socially constrained conversation
Dialogue rule: Let each line test motive, timing, or emotional inconsistency without stating the whole theory outright.
Style rule: Balance clue-reading with relational tension. Use natural Korean that sounds observant, not essay-like.
```

### Psychological Horror Female-Oriented Suspicion

```text
Write this scene in Korean.
Genre: horror
Audience tendency: female-oriented
Scene intent: suspicion inside intimate wrongness
Dialogue rule: Let each line sound half-confirming and half-doubting, as if the speaker fears both the answer and their own interpretation.
Style rule: Make the dread enter through memory mismatch, changed behavior, and small sensory details. Avoid broad abstract fear language.
```

### Ghost Story Neutral Hook

```text
Write this scene in Korean.
Genre: horror
Audience tendency: neutral
Scene intent: hook opening tied to a returning trace
Dialogue rule: If dialogue appears, keep it brief, wary, and shaped by recognition before certainty.
Style rule: Use one recurring place detail, one impossible return, and one immediate practical reaction.
```

### Creature Horror Male-Oriented Threat

```text
Write this scene in Korean.
Genre: horror
Audience tendency: male-oriented
Scene intent: immediate threat under pursuit
Dialogue rule: Keep lines command-driven, short, and physically urgent.
Style rule: Make the threat embodied and close. Use sound, distance, obstruction, and bodily risk over decorative atmosphere.
```

### Deduction Mystery Neutral Suspicion

```text
Write this scene in Korean.
Genre: mystery
Audience tendency: neutral
Scene intent: suspicion triggered by one contradiction
Dialogue rule: Let each line move from observation to inference without dumping the whole explanation.
Style rule: Keep clues crisp, legible, and consequential. Let the theory stay one step behind the evidence.
```

### Investigation Mystery Neutral Hook

```text
Write this scene in Korean.
Genre: mystery
Audience tendency: neutral
Scene intent: procedural hook with case pressure
Dialogue rule: Keep exchanges practical, precise, and shaped by what can or cannot be confirmed yet.
Style rule: Use one record, one testimony gap, and one next action to create forward pull.
```
