# Planning Sync Checks

Use this file when the main risk is that the manuscript and the planning layer no longer describe the same story state.

## Core Principle

Planning sync failure is not only contradiction. It is any case where the active manuscript has drifted away from the story bible, continuity ledger, payoff tracker, timeline, or arc plan in a way that weakens control.

## What To Compare

Check the manuscript against the relevant planning artifacts:

- story bible
- volume or arc outline
- chapter cards
- continuity ledger
- knowledge-state tracker
- payoff tracker
- timeline or history spine

Do not compare against every document by default. Read the smallest planning set that should govern the sampled range.

## Common Sync Failure Modes

### Planning Stale, Manuscript True

Symptoms:

- the manuscript has evolved in a coherent way, but the planning documents still describe the older version
- later drafting decisions are correct locally, but the tracker layer no longer supports them

Likely cause:

- drafting advanced faster than documentation updates

### Manuscript Drift, Planning True

Symptoms:

- the manuscript violates an established rule, planned turn, knowledge state, or relationship state
- a tracked promise or constraint disappears in execution

Likely cause:

- chapter drafting or revision ignored the active planning packet

### Split Truth

Symptoms:

- neither the manuscript nor the planning layer is fully authoritative
- multiple documents imply different versions of the same fact, timeline event, or payoff status

Likely cause:

- updates were made in parallel without a single source of truth

### Dead Planning Artifact

Symptoms:

- a document exists but no longer affects real drafting decisions
- the manuscript repeatedly bypasses the same tracker or outline field

Likely cause:

- the planning artifact is too broad, too stale, or no longer part of the working loop

### Promise Tracker Desync

Symptoms:

- the payoff tracker says a promise is active, but the manuscript stopped feeding it
- the manuscript pays something off, but the tracker still treats it as pending

Likely cause:

- delayed-return tracking is not being updated after chapter batches

## QA Questions

- Which document should currently be authoritative for this issue
- Does the manuscript violate that document, or is the document stale
- Is the mismatch local, systemic, or the result of split truth across multiple files
- If drafting continues now, which future errors will this desync multiply
- Which planning artifact should be updated first to restore a single working truth

## Evidence Standard

When reporting planning sync failure, name:

- manuscript evidence
- planning document evidence
- the exact field, fact, or tracked item that diverged
- which side should currently be treated as authoritative
- the risk created if the mismatch remains unresolved

Do not report "out of sync" without naming both sides of the mismatch.

## Repair Direction Rule

Report planning sync repair as a handoff direction, not as QA-owned file editing. Prefer:

1. identify the conflicting authority claim
2. name the stale or conflicting planning artifact
3. name the candidate downstream owner for planning-layer alignment
4. define the evidence needed to prove the next planning packet no longer diverges

Do not preserve multiple competing versions of the same fact just to avoid naming the conflict.
Do not update, retire, rewrite, or align planning files inside QA.

## Recheck Questions

- Does each checked planning document now match the sampled manuscript range
- Is there one clear source of truth for rules, state, and payoff status
- Would a new drafting session based on the current planning packet reproduce the manuscript accurately
- Have stale or dead planning artifacts been flagged as updated, replaced, or retired by the downstream owner
