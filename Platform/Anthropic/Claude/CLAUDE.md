# Korean Fiction Writing Rules

## Korean Fiction Default

When the user asks for Korean fiction work in this workspace, do not answer from generic writing instincts alone.

Treat these requests as covered by the local `novel-writing` skill, even if the user does not explicitly invoke a skill name:

- planning or outlining a Korean novel, web novel, or serialized fiction
- drafting a scene, chapter, opening, synopsis, or character material in Korean
- revising Korean narration, tone, or chapter flow
- changing genre or audience tendency for Korean fiction

Treat `novel-writing` as the primary skill for narration, scene/chapter prose, exposition control, paragraph rhythm, and other description-heavy manuscript work.

Treat `character-voice-bible` as the primary skill for dialogue-only revision, character voice tuning, cast-wide speaker differentiation, relationship-dependent speech/register work, and other line-by-line spoken exchange tasks.

Treat `longform-story-design` as the primary skill for continuity architecture, volume design, character arc management, and world-building structural planning that spans multiple chapters or arcs.

Treat `series-qa` as the primary skill for diagnosing continuity breaks, pacing problems, payoff failures, narration instability, or dialogue drift across a long-form manuscript or web novel arc.

Before drafting or revising, read only the references you need. Use the Read tool to inspect only the minimum relevant files from `skills/`. Do not read every reference file if the request is narrow.

For `novel-writing` tasks, use only the smallest relevant subset of:

- `skills/novel-writing/SKILL.md`
- `skills/novel-writing/references/task-router.md`
- `skills/novel-writing/references/templates.md`
- `skills/novel-writing/references/workflow.md`
- `skills/novel-writing/references/korean-prose.md`
- `skills/novel-writing/references/genre-audience-samples.md`
- `skills/novel-writing/references/dialogue-tone-transforms.md`
- `skills/novel-writing/references/prompt-selection-matrix.md`
- `skills/novel-writing/references/chapter-opening-selection.md`
- `skills/novel-writing/references/starter-sets.md`
- `skills/novel-writing/references/dialogue-revision-selection.md`
- `skills/novel-writing/references/narration-revision-selection.md`
- `skills/novel-writing/references/narration-tone-matrix.md`
- `skills/novel-writing/references/pov-narration-examples.md`
- `skills/novel-writing/references/meaning-first-examples.md`
- `skills/novel-writing/references/draft-pipeline.md`
- `skills/novel-writing/references/manuscript-quality-gate.md`
- `skills/novel-writing/references/lexical-normalization-examples.md`

For `character-voice-bible` tasks, use only the smallest relevant subset of:

- `skills/character-voice-bible/SKILL.md`
- `skills/character-voice-bible/references/request-router.md`
- `skills/character-voice-bible/references/composition-guide.md`
- `skills/character-voice-bible/references/output-templates.md`
- `skills/character-voice-bible/references/script-dialogue-rules.md`
- `skills/character-voice-bible/references/script-dialogue-samples.md`
- `skills/character-voice-bible/references/voice-diagnostic-questions.md`
- `skills/character-voice-bible/references/voice-profile-template.md`
- `skills/character-voice-bible/references/relationship-register-matrix.md`
- `skills/character-voice-bible/references/dialogue-drift-checks.md`
- `skills/character-voice-bible/references/reaction-patterns.md`
- `skills/character-voice-bible/references/korean-voice-samples.md`
- `skills/character-voice-bible/references/genre-voice-samples.md`

## Stage File Policy

For Korean fiction writing requests that produce actual prose in this workspace:

1. Create and save `초고`, `개고`, and `원고` files using the Write tool into:
   - `drafts/초고/`
   - `drafts/개고/`
   - `drafts/원고/`
2. Use one shared ASCII file stem across all three stages.
3. Default to the pattern `YYYYMMDD-HHMMSS-short-slug.md`, using the current timestamp.
4. Return the `원고` text to the user, but keep all three files saved on disk.
5. Mention the saved file paths at the end of the response.

Do not skip stage files unless the user explicitly says not to save files.

## Mandatory Quality Pass

For Korean fiction generation in this workspace, always run a final self-check before responding:

1. Remove translation-like Korean syntax.
2. Remove dialogue that explains information both speakers already know.
3. Check speech level, honorifics, and relationship-based address.
4. Check that each line of dialogue reacts to the immediately prior line or current pressure.
5. Check that the output matches the requested genre and audience tendency.
6. Check that narration reads cleanly on first pass and does not bury the subject or image under modifiers.
7. Check that neither dialogue nor narration sounds like abstract meaning was decided first and only then turned into Korean.
8. Check that `원고` is materially cleaner than `초고` and `개고`, not just a duplicate save.
9. Check that no word sounds awkward only because a common Sino-Korean term was forcibly replaced with an unusual native-Korean alternative.
10. Check that short dialogue still sounds like something a person would actually say aloud, not like a label or heading fragment.
11. Check that speaker differentiation comes from reaction, register, and emotional behavior, not just from varying sentence length.

If the draft fails the check, revise it before writing the `원고` file and returning it.
