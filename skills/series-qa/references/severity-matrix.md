# Severity Matrix

Use this file when findings need consistent ranking.

## Score By Damage First

Rank severity by what the failure does to the reading experience:

- Critical: breaks comprehension, trust, or the work's central promise
- High: damages momentum or emotional investment across multiple chapters
- Medium: weakens a chapter, scene, or local thread without collapsing the main spine
- Low: localized inefficiency, polish problem, or narrow missed opportunity

## Urgency Modifier

Within the same severity band, raise priority when:

- one fix would remove several downstream symptoms
- the failure sits near the first break point
- the failure contaminates future drafting if left alone
- the user is about to revise or submit that exact range

## Confidence Modifier

Pair severity with confidence:

- high confidence: directly evidenced, repeatable, and text-grounded
- medium confidence: strongly supported but partly inferential
- low confidence: plausible but needs wider sampling

High severity with low confidence should trigger broader checking, not instant certainty.

## Ranking Rule

Prefer this order when preparing a QA report or diagnostic handoff note:

1. high-severity root cause
2. high-severity contradiction
3. medium-severity repeated symptom
4. low-severity polish issue
