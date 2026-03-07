# Project Intake

Use this file when the user's request does not yet make clear what kind of longform planning support is needed.

## Intake Fields

Extract or infer these fields first:

- format: long novel, web novel, trilogy, saga, season-based serial
- structure mode, if relevant: linear arc, braided ensemble, omnibus, rotating-focus serial
- scale: expected chapter count, arc count, or volume count
- genre and audience tendency
- user-stated genre label, if any
- likely chapter-return engine
- current material state: idea only, synopsis, outline, drafted chapters, broken draft
- protagonist engine: what keeps the story moving for many chapters
- opposition engine: what keeps pushing back in changing forms
- escalation lanes: external, relational, internal, system/world
- ending status: fixed, rough, or open
- current pain point: drift, repetition, contradiction, weak middle, flat ensemble, weak payoff
- requested deliverable

## Quick Triage

Match the dominant problem to the first artifact:

- weak scale or vague premise -> series brief
- unstable setting logic -> story bible or world rule sheet
- flat ensemble or relationship repetition -> cast matrix and relationship map
- history confusion -> history spine
- weak long-run movement -> volume or arc plan
- active chapter drafting drift -> continuity ledger and chapter-range plan
- secrets or misunderstandings breaking -> knowledge-state tracker
- setup not landing -> payoff tracker
- existing contradictory draft -> canon extraction sheet and continuity audit report

## Genre Package Intake

Decide the genre package before artifact depth if possible.

Use priority:

1. explicit genre label from the user
2. chapter-return engine
3. arc-ending type
4. middle expansion logic

Extract these signals:

- what the user most wants readers to anticipate next
- whether arc endings should land as confession, breakthrough, reveal, coup, or safe-zone loss
- whether the middle expands through relationships, ranks, clues, factions, or survival pressure
- whether failure feels most like heartbreak, stagnation, misread truth, loss of leverage, or collapse

If the user explicitly names a genre, map that label first and record the reason. If the mapped package fits awkwardly, keep it and record a structural warning instead of reclassifying. If the prompt gives only a setting label, do not lock the package yet. Wait until the return engine is clearer.
If the user says `옴니버스`, record that under format or structure mode, not under genre package.

For shorthand or platform labels, normalize with [genre-alias-map.md](genre-alias-map.md) before deciding the package.
For concrete examples of ambiguous label resolution, use the `Ambiguous Alias Resolution Samples` section in [genre-package-samples.md](genre-package-samples.md).
For a reusable one-page lock sheet, use [genre-selection-decision-sheet.md](genre-selection-decision-sheet.md).

If the user gives an ambiguous alias such as `현판`, `대체역사`, `복수극`, or `피카레스크`, keep the raw label visible during intake and record why the final package differs.

Quick checklist:

- [ ] record the raw label
- [ ] classify it as direct label, ambiguous alias, setting label, or no label
- [ ] finish `the reader comes back next chapter to see...`
- [ ] finish `this volume should end by...`
- [ ] finish `the middle expands through...`
- [ ] lock the package by return engine first
- [ ] if the user directly named the genre, keep that mapped package even when another package would fit more cleanly
- [ ] keep an `Alias resolution note` if raw label and locked package differ
- [ ] record a structural warning if direct user label and return engine pull in different directions
- [ ] write `Likely package selection reason` before moving to artifact choice

## Intake Output Template

```text
Project state:
Format and scale:
Structure mode:
Genre / audience:
User-stated genre label:
Label type:
Likely chapter-return engine:
Volume-end sentence:
Middle-expansion sentence:
Likely package selection reason:
Alias resolution note:
Structural warning:
Known ending status:
Dominant longform risk:
Requested output:
Assumptions used:
```

## Missing Information Rule

If key facts are missing, do not stop unless the gap makes planning unsafe. Make the smallest reasonable assumption, expose it, and build the minimum artifact that can later expand without rewrite.
