# Planning Output Format

Use this file when the user wants the planning result itself to feel tighter, denser, and more reusable.

## Default Package Order

Present greenfield longform planning in this order unless the user explicitly asks for another format:

1. project frame
2. risk diagnosis
3. core design decision
4. artifact package
5. next step

Do not start with a long explanatory preface.

## Project Frame

Use [project-frame-template.md](project-frame-template.md) for the reusable field order.

`Package selection reason` is mandatory. Use one sentence that points to the actual continuation pressure, not the wallpaper.
If the user started from an ambiguous alias label, keep that raw label visible in the reason line and state why the resolved package still wins.
If the user directly named a genre that maps awkwardly to the structure, keep that package and place the warning in `risk diagnosis` or `core design decision` instead of changing the package.
If the user says `옴니버스`, keep that in `Format` or `Structure mode`, not in `Genre package`.

## Risk Diagnosis

State only the one or two pressures most likely to break the project:

- premise too thin for long scale
- opposition too static
- escalation lane imbalance
- ensemble spread without center
- ending promise not visible enough

## Core Design Decision

This is the sentence that explains the plan's shape.

Examples:

- "Make the series run on revenge deepening, not pure power progression."
- "Keep volume one relationship-centered and delay the faction spread until volume two."
- "Anchor the longform engine in political debt rather than hidden bloodline revelation."

Include the genre package effect when relevant:

- "Run this as romance fantasy first, political expansion second."
- "Let survival pressure govern the first volume before the mystery widens."

## Artifact Package Rules

Each artifact should follow four rules:

- start with a label
- keep fields in fixed order
- keep each line decision-oriented
- avoid duplicate information across artifacts

If an artifact repeats another artifact, compress or remove it.

Let genre package change emphasis inside the same package:

- romance / romance fantasy: place cast matrix and first arc sketch earlier
- progression / action fantasy: place story bible and volume ladder earlier
- mystery / thriller: place knowledge-state material earlier once reveals matter
- political / war: place history spine and expansion map earlier
- survival / apocalypse / horror: place chapter-range pressure and environment rules earlier

## Depth Levels

### Concept Pass

Use when the user is still testing viability.

Include:

- story engine sheet
- series brief
- first arc sketch

### Development Pass

Use when the user wants a solid planning packet.

Include:

- story engine sheet
- series brief
- story bible
- core cast matrix
- series expansion map
- volume ladder
- first arc plan

### Production Pass

Use when the plan is about to feed drafting.

Include:

- development-pass package
- chapter-range plan
- drafting packet
- continuity or payoff trackers if relevant

If the caller supplies an active batch boundary, treat that boundary as the outer limit. The chapter-range plan must cover only the current batch and must not pre-plan later ranges beyond what is needed to maintain continuity.

## Density Rules

Keep artifact density high but not bloated:

- engine sheet: 8 to 12 lines
- series brief: 8 to 12 lines
- story bible: 4 labeled blocks
- core cast matrix: 1 block per major cast member
- volume ladder: 3 to 7 entries for planned scale
- chapter-range plan: one row or block per range, not per chapter unless requested

For `series-completion-loop` `slice_planning`, density is capped by the current `3~5화` batch even when the whole project is 150~200 chapters.

Genre-specific density shifts:

- romance / romance fantasy: add one extra line for relationship leverage in cast and arc outputs
- progression / action fantasy: add one extra line for cost and ceiling in engine and volume outputs
- mystery / thriller: add one extra line for reveal control in arc outputs
- political / war: add one extra line for faction consequence in bible and volume outputs
- survival / apocalypse / horror: add one extra line for scarcity or safety loss in chapter-range outputs

## Option Rule

If giving options, give at most two:

- `recommended`: structurally cleaner default
- `alternative`: only if it changes the engine or growth model in a meaningful way

Do not present multiple cosmetic variants.

## Final Line Rule

End with the next design move, not generic encouragement.

Examples:

- "Next, lock the four major cast tensions before expanding volume two."
- "Next, break volume one into three chapter ranges and assign reveals."
- "Next, test whether the ending promise still holds if the rivalry becomes romantic."

For full sample packages using this format, read [genre-package-samples.md](genre-package-samples.md).
For direct-label mismatch examples that still preserve the chosen package, read the `Structural Warning Samples` section in [genre-package-samples.md](genre-package-samples.md).
