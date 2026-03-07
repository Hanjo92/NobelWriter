# Workspace Rules

## Korean Fiction Default

When the user asks for Korean fiction work in this workspace, do not answer from generic writing instincts alone.

Treat these requests as covered by the local `novel-writing` skill, even if the user does not explicitly invoke a skill name:

- planning or outlining a Korean novel, web novel, or serialized fiction
- drafting a scene, chapter, opening, synopsis, or character material in Korean
- revising Korean narration, tone, or chapter flow
- changing genre or audience tendency for Korean fiction

Treat `novel-writing` as the primary skill for narration, scene/chapter prose, exposition control, paragraph rhythm, and other description-heavy manuscript work.

Treat `character-voice-bible` as the primary skill for dialogue-only revision, character voice tuning, cast-wide speaker differentiation, relationship-dependent speech/register work, and other line-by-line spoken exchange tasks.

Treat `longform-story-design` as the primary skill for story continuity, volume design, character arc progression, and world-building structural work.

Treat `series-qa` as the primary skill for diagnosing pacing problems, continuity breaks, character drift, or narrative tension issues across an entire web novel series.

Before drafting or revising, read only the references needed for the task using the `view_file` tool to inspect the minimum relevant files inside `skills/`.

For `novel-writing` tasks, use only the smallest relevant subset of:

- `skills/novel-writing/SKILL.md`
- `skills/novel-writing/references/task-router.md`
- `skills/novel-writing/references/templates.md`
... *(and all corresponding reference paths as dictated by your assessment)* ...

Choose the smallest relevant subset. Do not load every file if the request is narrow.

## Stage File Policy

For Korean fiction writing requests in this workspace:

1. Create and save `초고`, `개고`, and `원고` files using the `write_to_file` tool into:
   - `drafts/초고/`
   - `drafts/개고/`
   - `drafts/원고/`
2. Use one shared ASCII file stem across all three stages.
3. Default to the pattern `YYYYMMDD-HHMMSS-short-slug.md`, using your current timestamp.
4. Return the `원고` text to the user, but keep all three files saved on disk via the tool.
5. Provide markdown links to the local files in the final response.

Do not skip stage files unless the user explicitly says not to save files.

## Mandatory Quality Pass

For Korean fiction generation in this workspace, always run a final self-check before answering:

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

If the draft fails the check, revise it by generating a new string in memory/scratchpad before writing the final `원고` file and returning it.
