---
name: series-qa
description: Audit long-form Korean fiction manuscripts, chapter batches, story bibles, and serialized arcs for continuity breaks, pacing problems, payoff failures, character drift, POV instability, escalation weakness, and structural regressions. Use when Codex is asked to review, debug, diagnose, or triage what is not working in an existing novel, long manuscript, web novel run, or story package before revision, relaunch, or submission.
---

# Series QA

## Overview

Use this skill to inspect accumulated Korean fiction materials and identify the smallest set of failures causing reader-visible weakness. Focus on diagnosis, evidence, and repair priority rather than on fresh drafting.

This skill is diagnosis-only. Do not rebuild chapters, scenes, arcs, cast sheets, or story systems here.
Do not take ownership of downstream repair execution, rewrite architecture, or prose reconstruction.
If the request needs a design pass, drafting pass, or character rewrite pass, hand it off instead of expanding scope.

If the user needs the output to become a reusable reconstruction package rather than a ranked diagnosis, hand the work to `longform-story-design`.
If the problem is primarily chapter prose, narration, scene flow, or longform drafting shape, hand the work to `novel-writing`.
If the problem is primarily speaker voice, dialogue register, or cast interaction behavior, hand the work to `character-voice-bible`.

## Choose The Audit Mode

Match the depth of the audit to the user's real need:

- fast triage: identify the top one to three failures and the first break point
- arc checkpoint: audit one arc, season, or volume segment for drift before drafting continues
- full diagnosis: map structural, continuity, pacing, and payoff failures across a long range

Default to the smallest mode that can answer the complaint cleanly.

## Canonical Diagnostic Order

Use this order unless the user's complaint makes a narrower slice sufficient:

1. identify the visible failure
2. gather the minimum audit packet
3. read the smallest valid slice
4. sample only if the range is too large to inspect directly
5. run the required diagnostic passes
6. rank the root cause and downstream symptoms
7. state the directional repair needed
8. hand off reconstruction work to the correct downstream skill
9. apply the re-audit gate after revision

Stop at diagnosis, repair direction, and handoff. Do not cross the line into rebuilding the material inside this skill.

## Start From The Visible Failure

Identify what the user or reader would actually notice first:

- the story feels slow or repetitive
- setup never pays off
- the protagonist stops driving the plot
- the cast forgets what they know or feel
- world rules change for convenience
- romance or rivalry repeats the same beat
- POV or tone becomes unstable across chapters

Choose the narrowest audit that can confirm or reject that failure. Do not run every diagnostic pass if the problem is already localized.

## Gather The Minimum Audit Packet

Before diagnosing, collect:

- manuscript scope: chapters, arc range, or volume range
- planning docs available: bible, timeline, outline, ledger
- intended genre and audience
- user complaint or suspected weak point
- desired output: QA report, ranked issue list, triage note, arc snapshot, or serialization checkpoint

If the user has both a manuscript and planning documents, treat mismatches between them as evidence instead of assuming the plan is correct.

## Read The Smallest Valid Slice

Do not read a 200-chapter run by default. Start from:

- the chapters named by the user
- the first point where the symptom becomes visible
- the chapter immediately before the symptom if drift is suspected
- the planning artifact that should have prevented the failure

Expand the range only if the local evidence points backward.

## Sample Intelligently

When the manuscript range is large, sample with intent instead of reading randomly:

- the first chapter where the promise is set
- the first chapter where the user says quality drops
- one chapter immediately before that drop
- one chapter from the latest comparable state
- the planning document that should track the same material

If the sample already shows a repeated break, report that pattern before widening the audit.

## Audit In Passes

Pick only the passes required by the failure mode:

1. structural pass
2. pacing pass
3. continuity pass
4. character drift pass
5. payoff pass
6. POV and tone stability pass
7. serialization pass when the work is installment-driven

For the audit order, read [references/diagnostic-workflow.md](references/diagnostic-workflow.md).
For recurring failure signatures, read [references/failure-patterns.md](references/failure-patterns.md).
If the complaint is genre-promise specific, follow the routing links inside `failure-patterns.md` to the matching genre file before diagnosing fixes.

## Structural Pass

Check whether cause-and-effect still holds across the requested range:

- does each chapter create new pressure
- do conflicts escalate or merely restate themselves
- does the midpoint or equivalent shift the story materially
- does the climax cash the core promise

When the structure fails, identify the first chapter where momentum weakens rather than only describing the later symptom.

## Pacing Pass

Separate slow burn from stagnation. Diagnose:

- repeated scene function
- low-value recap
- delayed consequences
- cliffhangers that do not alter the next chapter
- exposition that pauses conflict instead of weaponizing it

For pacing-specific checks, read [references/pacing-checks.md](references/pacing-checks.md).

## Continuity Pass

Track contradictions in:

- timeline math
- travel or location state
- injuries, items, and resources
- relationship state
- world rules
- knowledge state

For continuity and state checks, read [references/continuity-checks.md](references/continuity-checks.md).
For planning-layer sync checks, read [references/planning-sync-checks.md](references/planning-sync-checks.md).

## Character Drift Pass

Check for:

- motivation resets between arcs
- protagonists becoming reactive without payoff
- secondary cast flattening into functional dialogue devices
- relationship changes not affecting behavior
- emotional consequences disappearing too quickly

Describe the drift in behavioral terms, not just in adjectives.

For character drift-specific checks, read [references/character-drift-checks.md](references/character-drift-checks.md).

## Payoff Pass

Audit promises, delayed returns, and setup density:

- setup with no return
- return with insufficient setup
- payoff on the wrong emotional lane
- reveals that do not reframe prior material
- repeatedly postponed threads that stop feeling intentional

For payoff-specific failure types, read [references/payoff-checks.md](references/payoff-checks.md).

## POV And Tone Stability Pass

Check for:

- focal drift across the scene
- unstable narrative distance
- knowledge leaking outside the active access frame
- aftermath chapters losing tonal residue too quickly
- genre tone blur over time

For POV and tone-specific checks, read [references/pov-tone-stability-checks.md](references/pov-tone-stability-checks.md).

## Serialization Pass

When the project is a web novel, serial, or installment-driven work, also check:

- episode-end hooks that stop changing reader expectation
- recap burden at the top of chapters
- delayed consequence after cliffhangers
- bait scenes that create clicks but not story value
- reward cadence for readers following week to week

For installment-specific checks, read [references/serialization-checks.md](references/serialization-checks.md).

## Output Format

Default to this structure unless the user requests a different format:

1. what is working
2. highest-risk failures
3. severity and confidence
4. chapter or scene evidence
5. likely reader-visible symptom
6. smallest viable repair direction
7. downstream handoff target
8. optional re-audit note

For reusable report layouts, read [references/report-templates.md](references/report-templates.md).
Keep the output QA-first: it should support decision-making, not imply that this skill is responsible for reconstruction.

## Evidence Standard

Every major finding should answer:

- where the failure is visible
- what earlier promise, setup, or state it breaks
- what symptom the reader would feel
- why this is a story-function problem rather than just a taste preference

If a claim cannot be tied to evidence, downgrade it to a hypothesis.

## Root Cause Rule

Do not list five symptoms as five separate problems if one upstream break explains them. Cluster issues into:

- root cause
- downstream symptoms
- likely collateral risks

Examples:

- broken payoff tracker -> missing return, weak reveal timing, forgotten promises
- protagonist desire drift -> repetitive chapters, low escalation, passive scene entries
- continuity ledger failure -> knowledge mistakes, object drift, unstable consequences

The report should make clear what to repair first to collapse the largest number of downstream failures.
Describe the repair only as a direction, dependency, or constraint. Do not turn it into a rebuild plan or step-by-step reconstruction inside this skill.

## Severity Rule

Rank issues by damage, not by annoyance:

- critical: breaks comprehension, trust, or core promise
- high: damages momentum or emotional investment across multiple chapters
- medium: weakens a scene, chapter, or local payoff but does not collapse the spine
- low: polish issue or localized inefficiency

Prefer one critical issue over five medium ones in the revision order.

For scoring guidance, read [references/severity-matrix.md](references/severity-matrix.md).

## QA Judgment Rule

Treat this as quality assurance, not taste ranking. A finding is strongest when it can show:

- expected function
- observed failure
- evidence location
- user-visible damage
- minimal repair path

Avoid vague judgments such as "weak" or "boring" without attaching them to a broken story function.
Do not phrase the output as if this skill will execute the fix; phrase it as a diagnostic recommendation that points to the next owner.

## Recheck Rule

After proposing fixes, define what would count as success on a second pass:

- contradiction removed
- chapter sequence produces new pressure
- payoff now returns on the promised lane
- protagonist regains initiative in the flagged range
- episode hook leads to changed next-episode value instead of recap

For re-audit gates, read [references/regression-checks.md](references/regression-checks.md).
Use the re-audit gate as the end of the diagnostic loop: once the issue is repaired downstream, recheck whether the original failure and its collateral symptoms actually cleared.

## Operating Rules

- Diagnose with evidence tied to chapters, scenes, or planning artifacts.
- Prefer the earliest break point over the loudest downstream symptom.
- Suggest the smallest revision direction that can restore function before proposing broader downstream work.
- Distinguish between genre-appropriate repetition and accidental beat reuse.
- If the user's complaint is vague, convert it into testable failure hypotheses.
- Keep diagnosis separate from rewriting unless the user asks for proof-of-fix examples.
- Separate reader-facing failure from market speculation unless the user explicitly asks for platform strategy.
- When several failures share one root cause, report the root cause first and list downstream symptoms under it.
- If the manuscript is too large for full confidence, mark the scope limit instead of overstating certainty.
- Prefer a narrower but defensible finding over a broad but weak conclusion.
- Name the downstream owner when the next step is structural recovery, prose rewrite, or dialogue-layer repair.
- Do not produce reconstruction packages, re-entry drafting packets, or rewrite plans in this skill.

## Relationship To Other Skills

Use this skill for diagnosis and revision prioritization across existing long-form material.

- Use `longform-story-design` to build or repair the planning layer when the diagnosis points to structural recovery.
- Use `character-voice-bible` when the fix is mainly in dialogue differentiation, spoken-line pressure, or relationship-based register repair.
- Use `novel-writing` when the fix is mainly in narration, scene prose, chapter execution, or exposition control after the diagnosis is clear.

This skill should tell those layers what to fix first and why, but it should not do their planning for them.

## Resource Map

- Read [references/diagnostic-workflow.md](references/diagnostic-workflow.md) when you need the full order for auditing a long manuscript or arc batch.
- Read [references/failure-patterns.md](references/failure-patterns.md) when the symptom is visible but the root cause is unclear.
- Read [references/romance-failures.md](references/romance-failures.md) when romantic progression, chemistry, confession timing, or relationship reset is the main failure.
- Read [references/mystery-failures.md](references/mystery-failures.md) when clues, deduction, reveal force, or investigative logic are the main risk.
- Read [references/progression-fantasy-failures.md](references/progression-fantasy-failures.md) when training arcs, rank-ups, power costs, or growth momentum are underperforming.
- Read [references/political-intrigue-failures.md](references/political-intrigue-failures.md) when faction clarity, betrayal logic, leverage flow, or institutional power is the main failure.
- Read [references/report-templates.md](references/report-templates.md) when the user needs a reusable QA report, triage artifact, or directional handoff note.
- Read [references/character-drift-checks.md](references/character-drift-checks.md) when motivation reset, agency loss, relationship residue, or side-character flattening is the main risk.
- Read [references/continuity-checks.md](references/continuity-checks.md) when contradictions, knowledge drift, or rule inconsistency are the main risk.
- Read [references/planning-sync-checks.md](references/planning-sync-checks.md) when the manuscript and planning documents may no longer describe the same active story state.
- Read [references/pov-tone-stability-checks.md](references/pov-tone-stability-checks.md) when focal drift, narrative distance instability, tone reset, or genre-tone blur is the main risk.
- Read [references/pacing-checks.md](references/pacing-checks.md) when the story feels slow, repetitive, or weakly sequenced.
- Read [references/payoff-checks.md](references/payoff-checks.md) when setup, foreshadowing, reveals, or returns are not landing.
- Read [references/serialization-checks.md](references/serialization-checks.md) when the manuscript is published or planned as episode-by-episode fiction.
- Read [references/example-prompts.md](references/example-prompts.md) when you need trigger examples or user-facing request patterns for this skill.
- Read [references/severity-matrix.md](references/severity-matrix.md) when findings need sharper ranking by damage and repair urgency.
- Read [references/regression-checks.md](references/regression-checks.md) when you need pass/fail gates for a second audit after revision.
- Read [references/sample-qa-report.md](references/sample-qa-report.md) when you want a completed example of the intended QA report voice and structure.
- Read [references/sample-serialization-qa-report.md](references/sample-serialization-qa-report.md) when you want a completed example focused on serialized web fiction.
- Read [references/sample-short-triage.md](references/sample-short-triage.md) when you want a very short first-pass diagnosis example.
- Read [references/sample-romance-qa-report.md](references/sample-romance-qa-report.md) when you want a completed romance-focused diagnosis example.
- Read [references/sample-mystery-qa-report.md](references/sample-mystery-qa-report.md) when you want a completed mystery-focused diagnosis example.
- Read [references/sample-progression-fantasy-qa-report.md](references/sample-progression-fantasy-qa-report.md) when you want a completed progression-fantasy diagnosis example.
- Read [references/sample-political-intrigue-qa-report.md](references/sample-political-intrigue-qa-report.md) when you want a completed political-intrigue diagnosis example.
