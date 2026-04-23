# Draft Pipeline

Use this file when Korean fiction prose should be produced through explicit stage files rather than a single invisible pass.

## Goal

Make `초고 -> 개고 -> 원고` the default internal pipeline for fiction writing in this workspace.

The user should be able to open and edit every stage file directly.
If file writing is unavailable in the current environment, still run the same three-stage pipeline internally and return the requested stage text instead of stopping.
Exception: for `series-completion-loop` drafting handoffs, file writing is required because the orchestrator needs artifact paths. If stage files cannot be saved, return a blocker instead of a successful draft handoff.

## Folder Structure

Store stage files here:

- `drafts/초고`
- `drafts/개고`
- `drafts/원고`

Keep folder names in Korean exactly as above.

## File Naming Rule

Use ASCII file names for compatibility.

Default pattern:

```text
YYYYMMDD-HHMMSS-short-slug.md
```

Examples:

- `20260307-153000-ch01-opening.md`
- `20260307-153000-market-scene.md`
- `20260307-153000-romance-confession.md`

If the user gives a title or chapter id, reflect it in the slug.
If revising an existing set, keep the stem and add a short revision suffix only when necessary, such as `-r2`.
For orchestrated batch drafting, include the batch range in the slug when possible, such as `ch012-014-current-batch.md`.

## Orchestrated Batch Scope

When `series-completion-loop` sends a drafting handoff, the stage pipeline is still mandatory, but the scope is narrower and stricter.

Required before writing:

- selected `projects/<series-slug>/` runtime path
- `current_batch_start`
- `current_batch_end`
- matching active-slice range, goal, POV, active cast, `must_keep`, and `must_not_break`

If any required field is missing or contradictory, do not invent it. Return a blocker for the orchestrator.

Scope rules:

- write only chapters inside `current_batch_start` through `current_batch_end`
- do not draft future chapters, next batches, epilogues, or whole-series continuation
- keep continuity notes limited to current-batch exit state and unresolved items; do not plan next-batch beats
- do not update runtime, handoff, ledger, QA, or recovery files directly
- if planning, continuity repair, recovery direction, or QA is needed first, stop and name the correct handoff target

The saved stage files are the evidence the orchestrator records afterward.

## Stage Rules

### 초고

Purpose:
- capture scene movement, usable imagery, emotional direction, and rough prose quickly

Allow:
- rough phrasing
- temporary rhythm issues
- visible scaffolding if it secures the scene

Do not allow:
- broken logic
- inconsistent POV
- missing core scene movement
- dialogue that does not track who wants what

### 개고

Purpose:
- remove meaning-first scaffolding
- naturalize Korean prose
- fix dialogue, narration flow, rhythm, and register

Required work:
- run dialogue and narration quality checks
- fix translation-like syntax
- fix sentence drag and modifier pile-up
- fix tone mismatch against genre and audience
- sharpen paragraph order so the focal image or subject lands early

### 원고

Purpose:
- produce the user-facing readable version

Required work:
- read like publishable working copy
- remove obvious draft traces
- preserve style consistency through the whole piece
- be materially cleaner than both `초고` and `개고`

The default final response should be based on `원고`.
If the user explicitly asks for `초고` or `개고`, return that requested stage instead.

## Save Workflow

For any fiction generation task that produces real prose:

1. Create one shared stem.
2. Save `초고` first.
3. Revise and save `개고`.
4. Revise and save `원고`.
5. Return `원고` by default, or the explicitly requested stage if the user named one.
6. Tell the user where the files were saved.

Do not skip file creation unless the user explicitly asks for a one-off answer without saving.
Do not answer that you are unable to use the skill just because file saving is unavailable; saving is preferred, but the stage workflow is still mandatory.

## Minimum Metadata Header

At the top of each saved stage file, include a short header:

```text
# [title or working label]

- stage: [초고 / 개고 / 원고]
- date: [YYYY-MM-DD HH:MM:SS]
- genre:
- audience:
- scope:
```

Keep the header short. The prose should start immediately after it.
For orchestrated batches, the `scope` line must include the exact batch range, for example `scope: ch012-ch014 current batch`.

## When Revising Existing User Text

If the user gives an existing excerpt and asks for revision:

- preserve the original meaning unless they request deeper change
- save the revised versions into the same three stage folders using one shared stem
- make `초고` the minimally adjusted structural pass if the original already exists
- make `개고` the naturalized revision
- make `원고` the final polished version

## Final Response Rule

In the final response:

- mention that the files were saved
- provide the saved stage file path and, when helpful, the `초고`, `개고`, and `원고` file paths
- summarize the main difference between stages in one short sentence
- for orchestrated drafting, include `batch_range`, `chapters_drafted`, `stage_files`, `latest_manuscript_batch`, assumptions, continuity notes, and next handoff target for the orchestrator
