# Sample Mystery QA Report

Use this file when you want a completed example focused on investigation and reveal control.

## Example

```text
Audit scope:
- Manuscript range: Chapters 9-18
- Planning documents checked: case outline, clue ledger
- Audit mode: arc checkpoint
- Sampling limit: full read of Chapters 9-18, spot check of Chapters 6-8 for clue setup

Complaint under test:
- Reported symptom: the case is readable, but the reveal lands flat and the investigation feels less sharp in the middle
- Working hypothesis: clues are accumulating without enough leverage and the reveal is not reframing prior material

Scope note:
- What was checked: clue arrival, suspect movement, theory change, reveal impact
- What was not checked: secondary conspiracy thread beyond Chapter 18, line-level tension writing
- Confidence limit: high confidence for the main case arc through Chapter 18, medium confidence for longer conspiracy setup

Confirmed findings:
1. Mid-arc clues add information but do not change investigative behavior
   Severity: High
   Confidence: High
   Classification: Root cause
   First break point: Chapter 11
   Evidence: Chapters 11, 13, and 15 each deliver new case details, but the protagonist's theory, suspect priority, and risk profile remain effectively unchanged after each discovery.
   Expected function: Each significant clue should alter suspicion, decision-making, or pressure.
   Observed failure: The clue chain expands the file but not the investigation.
   Reader-visible damage: The case feels busy rather than sharper, and mid-arc movement loses force.
   Repair direction: At least one clue beat needs leverage that forces a wrong turn, narrowed suspect field, or riskier investigative move.
   Handoff target: `longform-story-design`
   Recheck condition: Revised clue chapters must each produce a visible theory change, suspect shift, or tactical consequence.

2. The Chapter 18 reveal answers the question without reframing prior scenes
   Severity: High
   Confidence: High
   Classification: Root cause
   First break point: Chapter 18
   Evidence: The solution identifies the culprit and explains motive, but earlier clue scenes read the same after the reveal and no previously ambiguous behavior gains new meaning.
   Expected function: A mystery reveal should answer and recontextualize.
   Observed failure: The reveal closes the plot mechanically without deepening the reader's understanding of earlier material.
   Reader-visible damage: Readers can follow the logic but do not feel the payoff snap into place.
   Repair direction: At least one earlier clue needs planted or reframed meaning so the Chapter 18 reveal changes how prior scenes read.
   Handoff target: `longform-story-design`
   Recheck condition: After revision, at least two prior scenes should read differently once the reveal is known.

3. Investigator agency drops during the mid-case run
   Severity: Medium
   Confidence: Medium
   Classification: Downstream symptom
   First break point: Chapter 12
   Evidence: The investigation advances through witness convenience and villain disclosure more often than through deliberate probing by the protagonist.
   Expected function: The investigator should generate pressure by choosing tests, risks, and lines of inquiry.
   Observed failure: The case moves toward the protagonist instead of because of them.
   Reader-visible damage: Suspense weakens because discovery starts to feel prearranged.
   Repair direction: The middle run needs protagonist-driven investigation pressure, such as a failed probe or high-risk inference.
   Handoff target: `longform-story-design`
   Recheck condition: The revised middle run must include at least one investigative advance caused by protagonist initiative rather than by delivered information.

Hypotheses needing broader review:
- The suspect field may be too thin overall, but the current sample is not wide enough to judge the full-case fairness structure.

What is still working:
- The atmosphere of suspicion remains intact.
- The victim network provides credible motive density.
- Chapter 16 briefly restores momentum by tying a clue to immediate personal risk.

Handoff priority:
1. Root cause: mid-arc clues lack leverage over theory and action.
2. Root cause: Chapter 18 reveal answers without reframing earlier material.
3. Downstream symptom: investigator agency drops in the middle stretch.
```

## Why This Example Works

- It distinguishes clue density from clue leverage.
- It treats reveal force as reframe value, not just answer delivery.
- It checks whether the investigator is actually driving the inquiry.
