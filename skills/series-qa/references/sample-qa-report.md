# Sample QA Report

Use this file when you want to see a completed `series-qa` report in the intended document style.

## Example

```text
Audit scope:
- Manuscript range: Chapters 31-45
- Planning documents checked: arc outline, continuity ledger, payoff tracker
- Audit mode: arc checkpoint
- Sampling limit: full read of Chapters 31-45, spot check of Chapters 28-30

Complaint under test:
- Reported symptom: the mid-arc run feels slower and less addictive than the opening arcs
- Working hypothesis: pacing drag and payoff drift are reducing chapter-end momentum

Scope note:
- What was checked: chapter sequence, end hooks, continuity carryover, named setup threads
- What was not checked: full Volume 1 relaunch logic, line-level prose polish
- Confidence limit: high confidence for the sampled arc, medium confidence for root causes earlier than Chapter 28

Confirmed findings:
1. Repeated hesitation beat is flattening the middle of the arc
   Severity: High
   Confidence: High
   Root cause or symptom: Root cause
   First break point: Chapter 34
   Evidence: Chapters 34, 36, and 38 all end with the protagonist delaying the same commitment without a new cost, reversal, or information shift.
   Expected function: Each chapter should escalate the commitment problem or alter the cost of refusal.
   Observed failure: The plot replays the same emotional hesitation beat three times with only minor surface variation.
   Reader-visible damage: The arc feels stalled even though events are still happening, and chapter endings stop increasing urgency.
   Smallest viable fix: Convert one of the repeated hesitation chapters into an irreversible choice or external consequence chapter.
   Recheck condition: The revised Chapter 34-38 sequence must show a new cost or changed decision state in each chapter.

2. Early setup around the sealed archive pays off too late and too weakly
   Severity: High
   Confidence: Medium
   Root cause or symptom: Root cause
   First break point: Chapter 33
   Evidence: The archive is framed as a major risk in Chapters 31-33, but the return in Chapter 41 provides information only and does not alter trust, strategy, or faction balance.
   Expected function: A promised high-risk reveal should materially shift character decisions or power relations.
   Observed failure: The payoff returns as exposition rather than as a story-changing event.
   Reader-visible damage: The reveal reads as smaller than the buildup, so the arc loses force near the point where it should tighten.
   Smallest viable fix: Tie the archive reveal to an immediate relational break, tactical cost, or changed pursuit objective.
   Recheck condition: The Chapter 41 reveal must force a different decision path within the next two chapters.

3. Continuity tracking around injury state is drifting
   Severity: Medium
   Confidence: High
   Root cause or symptom: Downstream symptom
   First break point: Chapter 37
   Evidence: The shoulder injury limits combat movement in Chapter 37, is ignored during the pursuit sequence in Chapter 39, and returns as active pain in Chapter 40 without explanation.
   Expected function: Injury state should either persist consistently or be explicitly reset.
   Observed failure: The injury behaves according to scene convenience rather than tracked state.
   Reader-visible damage: Trust in consequence handling weakens, especially during action scenes.
   Smallest viable fix: Either preserve the limitation through Chapter 39 or add a clear reason the limitation temporarily changes.
   Recheck condition: Adjacent action chapters must now show one consistent injury state or an explicit recovery/change trigger.

Hypotheses needing broader review:
- The protagonist's passivity may begin before Chapter 31, but the sampled evidence is not wide enough to confirm the first onset with high confidence.

What is still working:
- The antagonist's pressure remains legible and escalates cleanly.
- Chapter 42 restores strong forward motion once the pursuit objective becomes concrete.
- Relationship tension between the protagonist and the archivist still carries reader value even when the plot slows.

Revision priority:
1. Remove the repeated hesitation loop in Chapters 34-38.
2. Strengthen the archive payoff in Chapter 41 so it changes action, trust, or stakes.
3. Repair injury-state continuity in Chapters 37-40 and update the ledger.
```

## Why This Example Works

- It states scope and sampling limits before making claims.
- It distinguishes confirmed findings from wider hypotheses.
- It separates root causes from downstream symptoms.
- It gives a concrete recheck condition for each major finding.
