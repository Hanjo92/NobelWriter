# Output Templates

Use this file when you need compact, reusable output shapes.

## Orchestrated Voice Handoff

```text
voice_handoff

source_artifact:
batch_range:
excerpt_range:
affected_speakers:
relationship_state:
voice_failure:
repair_rules:
- rule
proof_rewrites:
- original_ref:
  before:
  after:
  reason:
register_notes:
assumptions:
unresolved_voice_risks:
next_handoff_target:
```

Use this only for orchestrated handoffs from `series-completion-loop`, `novel-writing`, or `series-qa`. Keep it limited to dialogue and voice repair. The block is the handoff artifact; the caller may persist it. Do not include future-batch plot beats, narration-heavy prose, manuscript stage-file edits, runtime updates, QA acceptance, or recovery planning.

## Cast Voice Bible

```text
Cast Voice Bible

Core cast:
- Name / story role / baseline speech level / pressure shift

Voice rules by character:
- address forms
- reaction logic
- avoidance pattern
- anger, fear, care, apology behavior
- drift risk

Relationship-sensitive shifts:
- pair / public register / private register / conflict shift / intimacy shift

Distinctness guardrails:
- who compresses
- who hedges
- who escalates
- who exposes emotion

Proof contrasts:
- same situation, different reaction for two or three speakers
```

## Character Voice Card

```text
Character Voice Card

Name:
Function in cast:
Baseline speech level:
Address map:
Pressure shift:
Typical rhythm:
Avoidance habit:
Care pattern:
Conflict pattern:
Confession pattern:
Taboo or weak point:
Common drift risk:
Keep distinct from:
```

## Pairwise Contrast Notes

```text
Pairwise Contrast

Shared scene pressure:
Speaker A default move:
Speaker B default move:
Key difference in hierarchy handling:
Key difference in emotional leakage:
Do not let both speakers:
Proof rewrite or sample contrast:
```

## Dialogue Drift Report

```text
Dialogue Drift Report

Scene or chapter:
Speaker or pair:
Visible symptom:
Likely cause:
Minimal repair:
One proof rewrite:
Future guardrail:
```

For orchestrated handoffs, `Future guardrail` means a reusable voice rule only, not a future chapter or plot instruction.

## Dialogue Exchange Sheet

```text
Dialogue Exchange Sheet

Scene pressure:
Relationship state:
Register rule:

Speaker A: line
Speaker B: line
Speaker A: line
Speaker B: line

Repair note or guardrail:
```

## Two-Person Exchange

```text
Two-Person Exchange

Pressure source:
Speaker A wants:
Speaker B wants:

Speaker A: line
Speaker B: line
Speaker A: line
Speaker B: line

Who owns pace:
Who leaks emotion:
```

## Three-Person Exchange

```text
Three-Person Exchange

Pressure source:
Speaker A role:
Speaker B role:
Speaker C role:

Speaker A: line
Speaker B: line
Speaker C: line
Speaker A or B: line

Alignment shift:
Register shift:
```

## Group Scene Exchange

```text
Group Scene Exchange

Scene pressure:
Driver:
Blocker:
Amplifier:
Cooler:
Witness:

Speaker: line
Speaker: line
Speaker: line
Speaker: line

Topic control note:
Noise or redundancy to cut:
```

## Relationship Exchange

```text
Relationship Exchange

Pair type:
Current pressure:
Address rule:
Who may interrupt:
Who may expose emotion first:

Speaker A: line
Speaker B: line
Speaker A: line
Speaker B: line

Relationship guardrail:
```

## Emotion Function Exchange

```text
Emotion Function Exchange

Function:
Current pressure:
Who holds initiative:
What the other speaker is trying to avoid:

Speaker A: line
Speaker B: line
Speaker A: line
Speaker B: line

Function check:
```

## Micro Voice Sheet

```text
Micro Voice Sheet

Speaker:
Default filler or softener:
Pressure filler:
Typical line length:
Pause habit:
Question style:
Turn opening tendency:
Turn closing tendency:
Overuse warning:
```

## Composition Recipe

```text
Composition Recipe

Exchange size:
Relationship:
Emotion function:
Micro voice:
Genre or subgenre:
Repair overlay:

Why these files:
Files to skip:
```

## Rewrite Rules

```text
Rewrite Rules

- preserve scene intent
- fix address and speech level first
- separate reaction direction second
- compress or expand sentence rhythm third
- change vocabulary last
```
