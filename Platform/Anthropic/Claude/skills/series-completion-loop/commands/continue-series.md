# /continue-series - Series Completion Loop

Invoke the `series-completion-loop` skill only for an explicit `projects/<series-slug>/` runtime that already exists.

## When to use

Use this command to:
- Continue a long-running Korean fiction project through the next safe 3~5화 batch
- Resume from `state/runtime.yaml`, `state/active-slice.yaml`, and `state/handoff.md`
- Respect approval-gated or autonomous completion mode
- Route the current transition to `longform-story-design`, `novel-writing`, `series-qa`, or `character-voice-bible`
- Record runtime, handoff, QA, or recovery evidence after specialist validation

Do not use this command to invent a project runtime, write an entire series in one pass, or bypass specialist skills.

## Behavior

When this command is called:
1. Read `skills/series-completion-loop/SKILL.md` first.
2. Resolve exactly one explicit `projects/<series-slug>/` runtime.
3. Read only the runtime files and ledgers needed for the next valid transition.
4. Perform one bounded transition or one allowed adjacent pair.
5. Delegate specialist work instead of doing it inline.
6. Validate required return evidence before updating runtime or handoff files.
7. Stop after the transition evidence is recorded.

## Usage example

```text
/continue-series projects/black-lotus 12~15화 다음 묶음 진행해줘. approval-gated 유지.
```
