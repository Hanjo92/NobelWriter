# Genre Selection Rules

Use this file when genre-package choice is ambiguous and a stricter rule is needed.

## One-Line Rule

Pick the package that best explains why a reader opens the next chapter, not the package that best describes the wallpaper.

Override rule: if the user directly names the genre, honor that label first and map it to the supported package set.

Examples:

- `로판으로 해줘` -> `romance / romance fantasy`
- `정치극으로 짜줘` -> `political / war / faction drama`
- `성장형 판타지로 설계해줘` -> `progression / action fantasy`

For a denser shorthand dictionary, use [genre-alias-map.md](genre-alias-map.md).

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

Good:

- `Package selection reason: Readers return for who will choose whom next under status pressure, so romance fantasy outranks the court backdrop.`
- `Package selection reason: The next-chapter engine is clue reinterpretation, so mystery thriller outranks the disaster setting.`
- `Package selection reason: The user explicitly asked for political drama, so the package is locked there and the structure is built around faction leverage.`

Bad:

- `Package selection reason: This story is in an empire.`
- `Package selection reason: There are monsters.`
