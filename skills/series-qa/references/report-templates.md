# Report Templates

Use these templates when the user wants a structured diagnostic output.

For a completed example in the same document style, read [sample-qa-report.md](sample-qa-report.md).
For a serialized fiction example, read [sample-serialization-qa-report.md](sample-serialization-qa-report.md).
For a one-page triage example, read [sample-short-triage.md](sample-short-triage.md).
For genre-specific completed examples, read [sample-romance-qa-report.md](sample-romance-qa-report.md), [sample-mystery-qa-report.md](sample-mystery-qa-report.md), [sample-progression-fantasy-qa-report.md](sample-progression-fantasy-qa-report.md), and [sample-political-intrigue-qa-report.md](sample-political-intrigue-qa-report.md).

## Reporting Rules

Write in QA language, not workshop language.

- state scope before judgment
- separate confirmed findings from hypotheses
- cite evidence by chapter, scene, or document location
- rank by severity and repair priority
- define what a passing recheck would require

Avoid:

- mood-only judgments
- praise that does not help triage
- rewrite suggestions without naming the failure they fix
- certainty beyond the sampled range

## QA Report

```text
Audit scope:
- Manuscript range:
- Planning documents checked:
- Audit mode:
- Sampling limit:

Complaint under test:
- Reported symptom:
- Working hypothesis:

Scope note:
- What was checked:
- What was not checked:
- Confidence limit:

Confirmed findings:
1. Finding title:
   Severity:
   Confidence:
   Root cause or symptom:
   First break point:
   Evidence:
   Expected function:
   Observed failure:
   Reader-visible damage:
   Smallest viable fix:
   Recheck condition:

2. Finding title:
   Severity:
   Confidence:
   Root cause or symptom:
   First break point:
   Evidence:
   Expected function:
   Observed failure:
   Reader-visible damage:
   Smallest viable fix:
   Recheck condition:

Hypotheses needing broader review:
- ...

What is still working:
- ...

Revision priority:
1. ...
2. ...
3. ...
```

## Revision Brief

```text
Revision target:
- Chapter / arc / volume range:
- Goal of this pass:

Fix first:
1. Issue:
   Why it comes first:
   Minimum change required:
   Do not break:
   Recheck after revision:

2. Issue:
   Why it comes first:
   Minimum change required:
   Do not break:
   Recheck after revision:

Changes that can wait:
- ...

Planning documents to update:
- ...

Open risks after this pass:
- ...
```

## Arc Health Snapshot

```text
Arc checked:
Audit basis:

Status:
- Structural health:
- Pacing health:
- Continuity health:
- Payoff health:
- Character stability:

Primary failure:
- ...

First break point:
- ...

Immediate action:
- ...

Recheck gate:
- ...
```

## Serialization Checkpoint

```text
Episode range checked:
Sampling basis:

Retention-facing finding:
- Hook quality:
- Recap burden:
- Consequence carryover:
- Reward cadence:

Story-health finding:
- Core failure:
- Evidence:
- Reader trust risk:

Immediate repair:
- ...

Pass condition on recheck:
- ...
```

## Short Triage Form

```text
Range checked:
Complaint:

Top issue:
- Severity:
- Evidence:
- First break point:
- Minimal fix:

Second issue:
- Severity:
- Evidence:
- First break point:
- Minimal fix:

Not checked:
- ...
```
