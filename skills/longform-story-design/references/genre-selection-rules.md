# Genre Selection Rules

Use this file when genre-package choice is ambiguous and a stricter rule is needed.

## One-Line Rule

Pick the package that best explains why a reader opens the next chapter, not the package that best describes the wallpaper.

Override rule: if the user directly names the genre, honor that label first and map it to the supported package set.
If the mapped package has strong structural tension with the project, keep it anyway and record a warning instead of silently reclassifying.

Examples:

- `로판으로 해줘` -> `romance / romance fantasy`
- `정치극으로 짜줘` -> `political / war / faction drama`
- `성장형 판타지로 설계해줘` -> `progression / action fantasy`

For a denser shorthand dictionary, use [genre-alias-map.md](genre-alias-map.md).
For ambiguous label resolution examples, use the `Ambiguous Alias Resolution Samples` section in [genre-package-samples.md](genre-package-samples.md).
For a compact working template, use [genre-selection-decision-sheet.md](genre-selection-decision-sheet.md).

## Automatic Selection Checklist

Run this in order. Do not skip ahead unless the user gave a direct package label.

### Step 1: Capture the label state

- [ ] Record the raw user label, if any
- [ ] Mark it as one of: direct package label, ambiguous alias, setting label, or no label
- [ ] If it is a direct package label, lock that package first, skip reclassification, and move to Step 6 only for warning checks
- [ ] If it is an ambiguous alias, keep the raw label visible and continue

### Step 2: Write the return sentence

Finish this sentence in one line:

- [ ] `The reader comes back next chapter to see...`

Then classify the return engine:

- [ ] intimacy, confession, jealousy, attachment pressure -> `romance / romance fantasy`
- [ ] advancement, mastery, rank, challenge clear -> `progression / action fantasy`
- [ ] truth, culprit, clue meaning, reveal -> `mystery / thriller`
- [ ] faction movement, decrees, alliances, public consequence -> `political / war / faction drama`
- [ ] food, shelter, infection, pursuit, survival outcome -> `survival / apocalypse / horror`

### Step 3: Check the arc-ending promise

Finish this sentence in one line:

- [ ] `This volume should end by...`

Then match the ending type:

- [ ] union, separation, confession, emotional reversal -> `romance / romance fantasy`
- [ ] breakthrough, victory over a ceiling, new tier entry -> `progression / action fantasy`
- [ ] reveal, culprit exposure, truth inversion -> `mystery / thriller`
- [ ] coup, succession shift, alliance break, reform lock -> `political / war / faction drama`
- [ ] safe-zone loss, escape, containment failure, survival regroup -> `survival / apocalypse / horror`

### Step 4: Check the middle-expansion engine

Finish this sentence in one line:

- [ ] `The middle expands through...`

Then match the expansion type:

- [ ] relationship escalation -> `romance / romance fantasy`
- [ ] training ladder, enemy ladder, cost curve -> `progression / action fantasy`
- [ ] clue chain, suspect spread, information control -> `mystery / thriller`
- [ ] leverage exchange, institution spread, faction rebalancing -> `political / war / faction drama`
- [ ] scarcity cycle, territory loss, trust collapse -> `survival / apocalypse / horror`

### Step 5: Resolve conflicts

- [ ] If return engine, ending promise, and middle expansion agree, lock that package
- [ ] If they disagree, let return engine outrank the other two
- [ ] If return engine is still unclear, let volume-end promise break the tie
- [ ] If the label is ambiguous, keep the raw label in the note even after locking the package

### Step 6: Run anti-misclassification checks

- [ ] If all romance beats were removed, would the project still basically work
- [ ] If all progression beats were removed, would the project still basically work
- [ ] If all mystery beats were removed, would the project still basically work
- [ ] If all faction beats were removed, would the project still basically work
- [ ] If all survival pressure were removed, would the project still basically work
- [ ] If the package came from inference, lock the package whose removal breaks the project most severely
- [ ] If the package came from a direct user label, do not override it here; write a structural warning if another package would fit more cleanly

### Step 7: Write the output line

- [ ] State `Genre package:` explicitly
- [ ] State `Package selection reason:` in one sentence
- [ ] If the package came from a direct user label, say that directly
- [ ] If the package came from an ambiguous alias, name both the raw label and the resolved package
- [ ] If a direct user label causes structural tension, add a warning note instead of changing the package
- [ ] Point to continuation pressure, not setting wallpaper

## Selection Output Template

```text
Raw label:
Label type:
Return engine sentence:
Volume-end sentence:
Middle-expansion sentence:
Locked genre package:
Package selection reason:
Structural warning:
```

## Decision Ladder

Run this ladder in order:

0. check whether the user explicitly named the genre
1. finish the sentence "the reader comes back to see..."
2. finish the sentence "the worst possible turn would be..."
3. finish the sentence "the volume should end by..."
4. finish the sentence "the middle expands through..."

Match the answers:

- if answer 1 is about intimacy, confession, jealousy, or attachment pressure -> `romance / romance fantasy`
- if answer 1 is about advancement, mastery, rank, or challenge clearing -> `progression / action fantasy`
- if answer 1 is about truth, culprit, clue meaning, or reveal -> `mystery / thriller`
- if answer 1 is about faction movement, decrees, alliances, or public consequence -> `political / war / faction drama`
- if answer 1 is about food, shelter, infection, pursuit, or who makes it out alive -> `survival / apocalypse / horror`

## Strong Signals

Signals that should usually override setting:

- marriage contract + jealousy + confession pacing -> romance
- academy + rank system + skill bottleneck -> progression
- serial case + hidden network + clue reinterpretation -> mystery
- imperial court + succession + tax or military leverage -> political
- sealed building + contamination + water or air shortage -> survival

## Weak Signals

Signals that should not decide the package by themselves:

- fantasy setting
- noble titles
- monsters
- detective protagonist
- sword fights
- plague backdrop

These matter only if they also control return pressure.

Explicit user genre labels are not weak signals. They are primary selection input.
If the explicit label maps to a package with visible structural friction, keep that package and record the friction as a warning rather than reclassifying.

## Anti-Misclassification Checks

Before locking the package, ask:

- if all romance beats were removed, would the story still basically work
- if all progression beats were removed, would the story still basically work
- if all mystery beats were removed, would the story still basically work
- if all faction beats were removed, would the story still basically work
- if all survival pressure were removed, would the story still basically work

The package whose removal breaks the project most severely is usually dominant.

## Output Rule

Once chosen, state the package explicitly in `project frame` and explain the reason in one sentence in `design decision`.

Also include a dedicated `Package selection reason:` line in `project frame`.

If the package came from an explicit user label, say so directly in that reason line.
If the explicit user label creates structural tension, add one warning line in risk diagnosis or design decision, but keep the package.

Good:

- `Package selection reason: Readers return for who will choose whom next under status pressure, so romance fantasy outranks the court backdrop.`
- `Package selection reason: The next-chapter engine is clue reinterpretation, so mystery thriller outranks the disaster setting.`
- `Package selection reason: The user explicitly asked for political drama, so the package is locked there and the structure is built around faction leverage.`

Bad:

- `Package selection reason: This story is in an empire.`
- `Package selection reason: There are monsters.`

For direct-label mismatch examples that still keep the chosen package, use the `Structural Warning Samples` section in [genre-package-samples.md](genre-package-samples.md).
