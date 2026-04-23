# Manuscript Quality Gate

Use this file when the task is direct Korean fiction prose generation or prose revision.

Run this check after `원고` is drafted and before replying.

## 1. Confirm The Draft Type

Apply this gate when the deliverable is:

- a scene
- a chapter opening
- a full chapter
- a rewritten excerpt
- any user-facing prose that should read like manuscript pages

Do not use this file for outline-only or critique-only requests.

## 2. Verify The Minimum Manuscript Packet

Before final cleanup, confirm that the draft still has:

- a visible focal character or stable POV
- a concrete want or pressure in the scene
- active resistance or friction
- a change by the end of the scene
- continuity hooks for what comes next

If any item is missing, fix structure before polishing sentences.

## 3. Confirm Orchestrated Batch Fence

Apply this section only when the draft came from a `series-completion-loop` drafting handoff.

Before final cleanup, confirm that:

- every drafted chapter is within `current_batch_start` and `current_batch_end`
- no future batch, next-slice teaser chapter, epilogue, or whole-series continuation was drafted
- continuity notes describe only current-batch exit state and unresolved items, not next-batch plot beats
- `초고`, `개고`, and `원고` share one ASCII file stem
- final response includes `stage_files` and `latest_manuscript_batch`
- runtime, handoff, ledger, QA, and recovery files were not edited by this skill

If any item fails, revise the output back inside the active batch or return a blocker to the orchestrator.

## 4. Run The Dialogue Check

Check each exchange for:

- speech level, honorifics, and address forms that fit the relationship
- lines that react to the immediately prior line or current pressure
- spoken compression, hesitation, or evasion where the moment needs it
- exposition that both speakers already know
- short lines that sound like actual speech rather than labels
- speaker differentiation driven by reaction, register, and emotional handling

If a line sounds semantically correct but not speakable, rewrite the turn rather than trimming words mechanically.

## 5. Run The Narration Check

Check narration for:

- translation-like sentence order
- subjects or images buried under modifiers
- abstraction that arrives before sensation, action, or focalized perception
- paragraph rhythm that drags because every sentence carries equal weight
- genre mismatch in texture, distance, or emotional framing

If a sentence feels meaning-first, rebuild it from image, pressure, or viewpoint rather than line-editing the surface.

## 6. Compare Stage Separation

Verify that each stage does different work:

- `초고` secures movement, pressure, and usable raw prose
- `개고` naturalizes Korean, fixes register, and removes scaffolding
- `원고` reads as the clean user-facing copy

If `원고` is only a lightly reformatted `개고`, revise again before replying.

## 7. Final Release Rules

Before returning the draft:

- ensure the requested genre and audience tendency are visible on the page
- ensure paragraphing supports readability on first pass
- ensure the ending lands on change, tension, or a forward pull
- ensure diction sounds like actual Korean fiction rather than translated explanation
- ensure no awkward wording exists only because a common Sino-Korean term was forcibly replaced

Return `원고` by default. If the user explicitly asked for `초고` or `개고`, return that requested stage instead and mention the saved stage file paths.
For orchestrated drafting, also return the batch range, chapters drafted, `stage_files`, `latest_manuscript_batch`, assumptions, continuity notes, and next handoff target.
