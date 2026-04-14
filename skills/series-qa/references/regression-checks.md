# Regression Checks

Use this file when the user wants to know whether a revision actually fixed the diagnosed problem.

## Recheck Principle

Do not ask only whether the rewritten chapter reads better. Check whether the original failure mode is gone.

## Outcome Classes

Classify the recheck outcome before adding commentary:

- `QA pass`: the original failure mode is removed and no new blocking contradiction appears
- `needs longform recovery`: the local symptom moved, but the upstream structural break still requires `longform-story-design`
- `needs local rewrite`: the diagnosis still points to prose, scene, or dialogue work before the issue can clear

## Pass / Fail Questions

### Structural

- Does the flagged chapter now create new pressure
- Does the revised sequence alter later chapter value
- Is the protagonist now making a meaningful commitment or choice

### Continuity

- Is the contradiction removed without creating a new one
- Do knowledge, injury, object, and relationship states now align across adjacent chapters

### Payoff

- Does the return now connect to the original setup
- Does it land on the intended emotional or plot lane
- Does the payoff change decisions, stakes, or relationships

### Serialization

- Does the hook now lead into actual consequence
- Has recap load decreased
- Does the next episode feel different rather than merely louder

## Re-Audit Output

For each fixed issue, report:

- original failure
- revision checked
- outcome class
- residual risk
- next action if still unstable
- handoff target if the issue stays outside QA scope

## Stop Rule

If a revision removes the local symptom but preserves the upstream root cause, mark it as partial only. Cosmetic relief is not a full pass.

If the recheck shows that the manuscript now needs reconstruction planning rather than another local rewrite, stop the QA loop and hand the work to `longform-story-design`.
