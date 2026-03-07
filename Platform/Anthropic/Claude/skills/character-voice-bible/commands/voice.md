# /voice — Character Voice Design & Dialogue Revision

Invoke the `character-voice-bible` skill for dialogue-only revision, speaker differentiation, or relationship-based register tuning.

## When to use

Use this command to:
- Design a character's voice profile from scratch
- Revise dialogue lines for speaker differentiation
- Adjust honorifics, speech level, or relationship-based register
- Diagnose and repair dialogue drift across a chapter or arc
- Write a reaction-first dialogue exchange between two characters

## Behavior

When this command is called:
1. Read `skills/character-voice-bible/SKILL.md` first.
2. Read only the reference files needed for the specific request.
3. Do not produce narration-heavy prose — focus on dialogue lines and voice mechanics.
4. Apply the quality gate from `CLAUDE.md` specifically for dialogue items (items 2–4, 10–11).
5. Return the revised dialogue or voice profile with brief annotations if needed.

## Usage example

```
/voice 유아(18세, 냉소적 성격)와 민준(18세, 낙천적 성격)의 첫 대면 대화. 두 사람은 서로를 처음 만남. 반말 관계. 3교환.
```
