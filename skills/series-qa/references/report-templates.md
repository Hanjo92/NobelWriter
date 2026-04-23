# Report Templates

Use these templates when the user wants a structured diagnostic output.

For a completed example in the same document style, read [sample-qa-report.md](sample-qa-report.md).
For a serialized fiction example, read [sample-serialization-qa-report.md](sample-serialization-qa-report.md).
For a one-page triage example, read [sample-short-triage.md](sample-short-triage.md).
For genre-specific completed examples, read [sample-romance-qa-report.md](sample-romance-qa-report.md), [sample-mystery-qa-report.md](sample-mystery-qa-report.md), [sample-progression-fantasy-qa-report.md](sample-progression-fantasy-qa-report.md), and [sample-political-intrigue-qa-report.md](sample-political-intrigue-qa-report.md).

## Reporting Rules

Write in QA language, not workshop language.

- state scope before judgment
- name the active batch first when invoked by `series-completion-loop`
- separate confirmed findings from hypotheses
- cite evidence by chapter, scene, or document location
- cite artifact evidence by file path or state pointer when the output feeds an orchestrator
- rank by severity and repair priority
- define what a passing recheck would require
- keep repair language directional, not reconstructive
- name the downstream owner when the next step leaves QA scope
- include an outcome: `ready_next_slice`, `needs_recovery`, or `blocked`

Avoid:

- mood-only judgments
- praise that does not help triage
- rewrite suggestions without naming the failure they fix
- step-by-step rebuild plans
- certainty beyond the sampled range

## QA Report

```text
Audit scope:
- Active batch:
- Manuscript range:
- Planning documents checked:
- Audit mode:
- Sampling limit:
- Earlier material sampled:

Complaint under test:
- Reported symptom:
- Working hypothesis:

Orchestrator outcome:
- Outcome: ready_next_slice | needs_recovery | blocked
- Artifact evidence:
- Repair direction status: unchanged | narrowed | changed | first pass
- Handoff target:
- Re-audit gate:

Scope note:
- What was checked:
- What was not checked:
- Confidence limit:

Confirmed findings:
1. Finding title:
   Severity:
   Confidence:
   Classification: root cause | downstream symptom:
   First break point:
   Evidence:
   Artifact evidence:
   Expected function:
   Observed failure:
   Reader-visible damage:
   Repair direction:
   Repair direction status:
   Handoff target:
   Recheck condition:

2. Finding title:
   Severity:
   Confidence:
   Classification: root cause | downstream symptom:
   First break point:
   Evidence:
   Artifact evidence:
   Expected function:
   Observed failure:
   Reader-visible damage:
   Repair direction:
   Repair direction status:
   Handoff target:
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

## Diagnostic Handoff Note

```text
Handoff range:
- Active batch:
- Chapter / arc / volume range:
- Core diagnosed failure:
- Outcome: ready_next_slice | needs_recovery | blocked
- Artifact evidence:

Directional repair:
1. Issue:
   Classification: root cause | downstream symptom:
   Why it comes first:
   High-level fix type:
   Repair direction status:
   Downstream owner:
   Recheck after downstream revision:

2. Issue:
   Classification: root cause | downstream symptom:
   Why it comes first:
   High-level fix type:
   Repair direction status:
   Downstream owner:
   Recheck after downstream revision:

Changes that can wait:
- ...

Open risks after this pass:
- ...
```

## Arc Health Snapshot

```text
Arc checked:
Active batch:
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

Outcome:
- ready_next_slice | needs_recovery | blocked

Artifact evidence:
- ...

Repair direction:
- ...

Handoff target:
- ...

Recheck gate:
- ...
```

## Serialization Checkpoint

```text
Episode range checked:
Active batch:
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

Outcome:
- ready_next_slice | needs_recovery | blocked

Artifact evidence:
- ...

Repair direction:
- ...

Handoff target:
- ...

Pass condition on recheck:
- ...
```

## Short Triage Form

```text
Range checked:
Active batch:
Complaint:

Top issue:
- Severity:
- Classification: root cause | downstream symptom:
- Evidence:
- Artifact evidence:
- First break point:
- Repair direction:
- Repair direction status:
- Handoff target:

Second issue:
- Severity:
- Classification: root cause | downstream symptom:
- Evidence:
- Artifact evidence:
- First break point:
- Repair direction:
- Repair direction status:
- Handoff target:

Not checked:
- ...
```
