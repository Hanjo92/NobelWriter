# Sample Political Intrigue QA Report

Use this file when you want a completed example focused on faction play, leverage, and institutional power struggle.

## Example

```text
Audit scope:
- Manuscript range: Chapters 48-60
- Planning documents checked: faction matrix, succession outline, knowledge-state tracker
- Audit mode: arc checkpoint
- Sampling limit: full read of Chapters 48-60, spot check of Chapters 44-47 for coup setup

Complaint under test:
- Reported symptom: the politics feel busy, but betrayals and negotiations are no longer hitting as hard
- Working hypothesis: faction incentives are blurring and major reversals are landing without enough leverage build

Scope note:
- What was checked: faction goals, negotiation outcomes, betrayal setup, knowledge flow, institutional constraint
- What was not checked: military campaign logic outside the capital plot, line-level dialogue polish
- Confidence limit: high confidence for the sampled court arc, medium confidence for deeper setup issues before Chapter 44

Confirmed findings:
1. Faction goals are no longer distinct enough to produce sharp conflict
   Severity: High
   Confidence: High
   Classification: Root cause
   First break point: Chapter 50
   Evidence: By Chapters 50-54, three court factions are all effectively pushing for generic stability language, while their risk tolerance, preferred methods, and succession preferences stop producing clearly different strategic moves.
   Expected function: Each major faction should create pressure through distinct incentives, acceptable costs, and preferred tools.
   Observed failure: The factions remain named and present, but their decisions no longer feel meaningfully differentiated.
   Reader-visible damage: Negotiation scenes feel verbose rather than sharp because the reader cannot feel why each side must move differently.
   Repair direction: Each active faction needs one non-overlapping incentive and one non-overlapping red line in the sampled arc.
   Handoff target: `longform-story-design`
   Recheck condition: In the next three faction scenes, each group must pursue a visibly different objective or accept a visibly different cost.

2. The Chapter 56 betrayal lands as surprise rather than as earned strategic outcome
   Severity: High
   Confidence: High
   Classification: Root cause
   First break point: Chapter 56
   Evidence: The betraying minister has presence in earlier chapters, but the sampled range does not build enough visible pressure, leverage, or narrowing options to make the turn feel inevitable in retrospect.
   Expected function: A political betrayal should read as both surprising in the moment and legible after review.
   Observed failure: The betrayal changes the board, but the preconditions are too thin for it to feel strategically earned.
   Reader-visible damage: The twist creates motion, but reader trust in the intrigue engine weakens because the move feels author-granted.
   Repair direction: The betrayal needs prior pressure evidence: concession failure, leverage dependency, and fear trigger.
   Handoff target: `longform-story-design`
   Recheck condition: After revision, the Chapter 56 betrayal should be traceable to at least two earlier pressures in the sampled range.

3. Institutional rules stop constraining elite action
   Severity: Medium
   Confidence: Medium
   Classification: Downstream symptom
   First break point: Chapter 53
   Evidence: Council procedure, succession protocol, and guard authority matter heavily in earlier chapters, but Chapters 53-58 allow high-ranking characters to bypass formal limits whenever speed is needed.
   Expected function: Institutions in political fiction should shape what can be attempted and at what cost.
   Observed failure: The court system keeps its decorative language while losing procedural force.
   Reader-visible damage: Power starts to feel personal only, which flattens the intrigue layer into ordinary confrontation.
   Repair direction: The court action needs a visible procedural barrier that forces alliance cost, legitimacy spend, or reputational risk.
   Handoff target: `longform-story-design`
   Recheck condition: The next major power move must show an institutional cost, gate, or dependency instead of proceeding by narrative convenience.

Hypotheses needing broader review:
- The succession stakes may already have blurred in the previous arc handoff, but the current sample is not wide enough to confirm the earliest point of dilution.

What is still working:
- The crown heir remains a strong pressure source because their indecision creates real instability.
- Private negotiation scenes still carry tension when leverage is concrete.
- Chapter 59 regains force once the failed alliance produces a public reputational cost.

Handoff priority:
1. Root cause: faction incentives no longer produce distinct pressure.
2. Root cause: Chapter 56 betrayal lacks enough leverage and constraint evidence.
3. Downstream symptom: institutional rules stop constraining elite action.
```

## Why This Example Works

- It checks whether named factions are actually producing differentiated strategy.
- It treats betrayal as a leverage event, not just a twist event.
- It tests whether institutions still function as force multipliers and constraints.
