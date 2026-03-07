# /qa — Series QA & Manuscript Diagnosis

Invoke the `series-qa` skill to diagnose and triage problems in a Korean long-form manuscript or web novel arc.

## When to use

Use this command to:
- Diagnose continuity breaks, timeline inconsistencies, or logic gaps
- Identify pacing problems, tension collapses, or payoff failures
- Detect narration instability or POV drift across chapters
- Flag dialogue drift or character regression in a specific arc
- Produce a triage report with prioritized repair recommendations

## Behavior

When this command is called:
1. Read `skills/series-qa/SKILL.md` first.
2. Read only the reference files needed for the specific request.
3. Ask the user to provide the manuscript excerpt, chapter range, or problem description if not supplied.
4. Output a structured diagnostic report: problem type, severity, location, and recommended fix.
5. Do not rewrite prose unless explicitly requested. Diagnosis first.

## Usage example

```
/qa 7~9화 구간. 주인공의 감정선이 6화와 충돌하는 것 같음. 대사 톤도 달라진 것 같은데 진단해줘.
```
