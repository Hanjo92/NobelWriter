# Series Completion Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a reusable repository-wide completion loop that can progress Korean long-form projects through bounded `3~5화` batches using the existing fiction skills plus scheduled automation.

**Architecture:** Create a new shared orchestration skill named `series-completion-loop` that reads per-project runtime files, decides the next valid transition, and hands the actual work to `longform-story-design`, `novel-writing`, `series-qa`, or `character-voice-bible`. Keep manuscript output in `drafts/` and move orchestration state into reusable per-project templates under `projects/_template/`, then document production and safety automation prompts for both `autonomous` and `approval-gated` modes.

**Tech Stack:** Markdown skill docs, YAML interface metadata, YAML runtime templates, repository documentation, automation prompt documentation

---

### Task 1: Scaffold The Shared Orchestrator Skill

**Files:**
- Create: `skills/series-completion-loop/SKILL.md`
- Create: `skills/series-completion-loop/agents/openai.yaml`
- Create: `skills/series-completion-loop/references/`

- [ ] **Step 1: Create the new skill directory and agent metadata**

Create `skills/series-completion-loop/agents/openai.yaml` with an explicit-orchestrator interface:

```yaml
interface:
  display_name: "Series Completion Loop"
  short_description: "State-based orchestration for long-running Korean fiction completion."
  default_prompt: "Use $series-completion-loop to move a Korean long-form project through the next valid 3~5화 batch by reading runtime state, dispatching the correct specialist skill, updating handoff files, and stopping after a bounded transition."
```

Run: `mkdir -p skills/series-completion-loop/agents skills/series-completion-loop/references`
Expected: directories exist with no shell errors

- [ ] **Step 2: Write the orchestrator skill body**

Create `skills/series-completion-loop/SKILL.md` with these sections and content constraints:

```markdown
---
name: series-completion-loop
description: Use when a Korean long-form project must keep progressing toward completion across many sessions or automation runs by moving the next valid 3~5화 batch through planning, drafting, QA, recovery, and state updates.
---

# Series Completion Loop

## Overview
- state-based orchestrator
- delegates specialist work instead of replacing it

## Hard Ownership
- when to use this skill
- when to hand work to `longform-story-design`
- when to hand work to `novel-writing`
- when to hand work to `series-qa`
- when to hand work to `character-voice-bible`

## Canonical Loop Order
- bootstrap
- slice planning
- drafting
- QA
- recovery or continue
- state update
- schedule or wait

## Runtime Files
- `project.md`
- `state/runtime.yaml`
- `state/active-slice.yaml`
- `state/handoff.md`
- ledgers
- QA/recovery files

## States And Transitions
- `bootstrap_pending`
- `slice_planning`
- `drafting`
- `qa_review`
- `recovery_planning`
- `approval_waiting`
- `ready_next_slice`
- `completed`
- `blocked`

## Mode Rules
- `autonomous`
- `approval-gated`

## Run Boundary Rules
- one bounded action or one safe adjacent pair only
- never attempt the entire series in one run

## Failure And Re-entry
- snapshot before run
- preserve manuscript output
- block on contradictions or repeated failure
```

Run: `sed -n '1,260p' skills/series-completion-loop/SKILL.md`
Expected: frontmatter, ownership section, state machine, mode rules, and failure/re-entry sections are all present

- [ ] **Step 3: Verify the new skill references the right owners and does not absorb their responsibilities**

Run:

```bash
rg -n "longform-story-design|novel-writing|series-qa|character-voice-bible|autonomous|approval-gated|blocked|3~5화" \
  skills/series-completion-loop/SKILL.md \
  skills/series-completion-loop/agents/openai.yaml
```

Expected: matches for all four downstream skills, both modes, the blocked state, and the batch-size rule

- [ ] **Step 4: Commit the scaffold**

Run:

```bash
git add skills/series-completion-loop/SKILL.md skills/series-completion-loop/agents/openai.yaml
git commit -m "feat(skills): add series completion loop scaffold"
```

Expected: commit succeeds with only the new orchestrator skill files staged

### Task 2: Add Orchestrator Reference Docs

**Files:**
- Create: `skills/series-completion-loop/references/runtime-layout.md`
- Create: `skills/series-completion-loop/references/state-machine.md`
- Create: `skills/series-completion-loop/references/mode-rules.md`
- Create: `skills/series-completion-loop/references/automation-prompts.md`
- Create: `skills/series-completion-loop/references/failure-reentry.md`

- [ ] **Step 1: Add runtime layout guidance**

Create `skills/series-completion-loop/references/runtime-layout.md` with:

```markdown
# Runtime Layout

- `projects/<series-slug>/project.md`
- `projects/<series-slug>/state/runtime.yaml`
- `projects/<series-slug>/state/active-slice.yaml`
- `projects/<series-slug>/state/handoff.md`
- `projects/<series-slug>/ledger/...`
- `projects/<series-slug>/qa/latest-report.md`
- `projects/<series-slug>/recovery/latest-recovery.md`
- `projects/<series-slug>/archive/runs/`

Separation rule:
- manuscript in `drafts/`
- runtime state in `projects/`
```

Run: `sed -n '1,220p' skills/series-completion-loop/references/runtime-layout.md`
Expected: runtime file list and separation rule are visible

- [ ] **Step 2: Add state-machine guidance**

Create `skills/series-completion-loop/references/state-machine.md` with the approved states and transitions:

```markdown
# State Machine

States:
- `bootstrap_pending`
- `slice_planning`
- `drafting`
- `qa_review`
- `recovery_planning`
- `approval_waiting`
- `ready_next_slice`
- `completed`
- `blocked`

Transitions:
- `bootstrap_pending -> slice_planning`
- `slice_planning -> drafting`
- `drafting -> qa_review`
- `qa_review -> ready_next_slice`
- `qa_review -> recovery_planning`
- `recovery_planning -> drafting`
- `recovery_planning -> slice_planning`
- `ready_next_slice -> approval_waiting`
- `ready_next_slice -> slice_planning`
- `* -> blocked`
```

Run: `sed -n '1,240p' skills/series-completion-loop/references/state-machine.md`
Expected: all approved states and transitions appear verbatim

- [ ] **Step 3: Add mode and automation guidance**

Create `skills/series-completion-loop/references/mode-rules.md` and `automation-prompts.md` with explicit distinctions:

```markdown
# Mode Rules

## Autonomous
- continue automatically after accepted QA

## Approval-Gated
- stop in `approval_waiting`
- require explicit user approval
```

```markdown
# Automation Prompts

## Production Run
- read `runtime.yaml`
- perform the next valid bounded action only
- update `handoff.md`
- stop

## Safety Run
- detect stalled `blocked`
- detect missing QA after drafting
- detect repeated recovery
- report only, do not force progress
```

Run:

```bash
rg -n "Autonomous|Approval-Gated|Production Run|Safety Run|bounded action only|approval_waiting" \
  skills/series-completion-loop/references/mode-rules.md \
  skills/series-completion-loop/references/automation-prompts.md
```

Expected: all mode and automation control phrases are present

- [ ] **Step 4: Add failure and re-entry rules**

Create `skills/series-completion-loop/references/failure-reentry.md` with:

```markdown
# Failure And Re-entry

Snapshot before each run:
- `runtime.yaml`
- `active-slice.yaml`
- `handoff.md`

Block conditions:
- missing state files
- contradictory state
- repeated QA failure on same slice
- repeated recovery
- approval bypass in gated mode

Re-entry:
- preserve manuscript files
- set next state explicitly
- never auto-roll back manuscript output
```

Run: `sed -n '1,220p' skills/series-completion-loop/references/failure-reentry.md`
Expected: snapshot rule, block conditions, and re-entry rules all exist

- [ ] **Step 5: Commit the references**

Run:

```bash
git add skills/series-completion-loop/references
git commit -m "feat(skills): add series completion loop references"
```

Expected: commit succeeds with only the reference docs staged

### Task 3: Add Reusable Project Runtime Templates

**Files:**
- Create: `projects/README.md`
- Create: `projects/_template/project.md`
- Create: `projects/_template/state/runtime.yaml`
- Create: `projects/_template/state/active-slice.yaml`
- Create: `projects/_template/state/handoff.md`
- Create: `projects/_template/ledger/continuity.md`
- Create: `projects/_template/ledger/knowledge-state.md`
- Create: `projects/_template/ledger/payoff-tracker.md`
- Create: `projects/_template/qa/latest-report.md`
- Create: `projects/_template/recovery/latest-recovery.md`
- Create: `projects/_template/archive/runs/.gitkeep`

- [ ] **Step 1: Create the top-level projects guide**

Create `projects/README.md` with:

```markdown
# Projects Runtime Layout

Use `projects/<series-slug>/` for orchestrator state, not manuscript text.

Required subfolders:
- `state/`
- `ledger/`
- `qa/`
- `recovery/`
- `archive/runs/`

Manuscript files stay in `drafts/`.
```

Run: `sed -n '1,200p' projects/README.md`
Expected: project runtime purpose and folder list are present

- [ ] **Step 2: Create the static project template**

Create `projects/_template/project.md` with fields the orchestrator can rely on:

```markdown
# Project

- Title:
- Slug:
- Genre package:
- Audience:
- Target scale:
- Completion mode: autonomous | approval-gated
- Default batch size: 3~5화
- Ending promise:
- Current status:
```

Run: `sed -n '1,200p' projects/_template/project.md`
Expected: title, slug, mode, batch size, and ending promise fields all appear

- [ ] **Step 3: Create runtime and active-slice YAML templates**

Create `projects/_template/state/runtime.yaml`:

```yaml
mode: approval-gated
state: bootstrap_pending
next_action: bootstrap
approval_pending: false
current_batch_start: null
current_batch_end: null
last_run_at: null
failure_count: 0
blocked_reason: null
last_completed_stage: null
```

Create `projects/_template/state/active-slice.yaml`:

```yaml
chapter_start: null
chapter_end: null
batch_goal: ""
success_conditions: []
active_pov: []
active_cast: []
must_keep: []
must_not_break: []
handoff_target: null
```

Run:

```bash
sed -n '1,200p' projects/_template/state/runtime.yaml
printf '\n---\n'
sed -n '1,220p' projects/_template/state/active-slice.yaml
```

Expected: runtime state keys and active-slice guardrail keys are present exactly once

- [ ] **Step 4: Create handoff and ledger templates**

Create these minimal templates:

```markdown
# Handoff

- Last completed step:
- Last failed step:
- Resume from:
- Notes:
```

```markdown
# Continuity Ledger
| Range | Fact | Status | Source |
| --- | --- | --- | --- |
```

```markdown
# Knowledge State
| Character | Knows | Since | Notes |
| --- | --- | --- | --- |
```

```markdown
# Payoff Tracker
| Setup | Introduced | Expected Return | Status |
| --- | --- | --- | --- |
```

Create:
- `projects/_template/state/handoff.md`
- `projects/_template/ledger/continuity.md`
- `projects/_template/ledger/knowledge-state.md`
- `projects/_template/ledger/payoff-tracker.md`

Run:

```bash
rg -n "Last completed step|Continuity Ledger|Knowledge State|Payoff Tracker" projects/_template
```

Expected: all four template markers are found in the new files

- [ ] **Step 5: Create QA/recovery placeholders and archive folder**

Create:

```markdown
# Latest QA Report

- Status:
- Highest-risk failure:
- Re-audit gate:
```

```markdown
# Latest Recovery

- Trigger:
- Owner:
- Next safe move:
```

Also create the archive directory marker:

```bash
mkdir -p projects/_template/archive/runs
touch projects/_template/archive/runs/.gitkeep
```

Run:

```bash
test -f projects/_template/qa/latest-report.md
test -f projects/_template/recovery/latest-recovery.md
test -f projects/_template/archive/runs/.gitkeep
echo "template-runtime-ok"
```

Expected: `template-runtime-ok`

- [ ] **Step 6: Commit the runtime templates**

Run:

```bash
git add projects/README.md projects/_template
git commit -m "feat(runtime): add reusable series completion templates"
```

Expected: commit succeeds with only `projects/` runtime templates staged

### Task 4: Integrate Repository Documentation

**Files:**
- Modify: `README.md`
- Modify: `USAGE_FAQ.md`

- [ ] **Step 1: Update README to add the orchestration layer**

Add a fifth system layer or a clearly separated orchestration note to `README.md`:

```markdown
## 🔁 Series Completion Loop

NobelWriter can also run a repository-wide completion loop that:
- progresses one project in `3~5화` batches
- supports `autonomous` and `approval-gated` modes
- keeps runtime state in `projects/<series-slug>/`
- uses automation to perform the next bounded action only
```

Run: `rg -n "Series Completion Loop|3~5화|autonomous|approval-gated|projects/<series-slug>" README.md`
Expected: all new orchestration keywords are present

- [ ] **Step 2: Update FAQ to explain long-running completion mode**

Add an FAQ entry to `USAGE_FAQ.md`:

```markdown
## 작품 하나를 끝날 때까지 계속 돌릴 수 있나요?

가능합니다. 단, 한 번의 무한 생성 런이 아니라 `series-completion-loop`가
`3~5화` 배치 단위로 상태를 읽고 다음 액션만 수행하는 방식입니다.

- `autonomous`
- `approval-gated`
- runtime state in `projects/<series-slug>/`
- manuscript output remains in `drafts/`
```

Run: `rg -n "끝날 때까지|series-completion-loop|autonomous|approval-gated|projects/<series-slug>" USAGE_FAQ.md`
Expected: all completion-loop FAQ keywords are present

- [ ] **Step 3: Commit the docs integration**

Run:

```bash
git add README.md USAGE_FAQ.md
git commit -m "docs: document series completion loop usage"
```

Expected: commit succeeds with only repo documentation staged

### Task 5: Verification

**Files:**
- Inspect: `skills/series-completion-loop/SKILL.md`
- Inspect: `skills/series-completion-loop/agents/openai.yaml`
- Inspect: `skills/series-completion-loop/references/*.md`
- Inspect: `projects/README.md`
- Inspect: `projects/_template/**`
- Inspect: `README.md`
- Inspect: `USAGE_FAQ.md`

- [ ] **Step 1: Verify required phrases and files exist**

Run:

```bash
rg -n "series-completion-loop|3~5화|autonomous|approval-gated|blocked|ready_next_slice|approval_waiting" \
  skills/series-completion-loop \
  projects/_template \
  README.md \
  USAGE_FAQ.md
```

Expected: matches in the skill, references, runtime templates, README, and FAQ

- [ ] **Step 2: Verify the file tree**

Run:

```bash
find skills/series-completion-loop -maxdepth 3 | sort
printf '\n---\n'
find projects/_template -maxdepth 4 | sort
```

Expected: skill body, agent metadata, references, state templates, ledger templates, QA/recovery placeholders, and archive folder all appear

- [ ] **Step 3: Run diff hygiene checks**

Run:

```bash
git diff --check
git diff --stat
```

Expected: no diff-check errors; stat shows the new skill, new project templates, and documentation updates

- [ ] **Step 4: Final review against the spec**

Run:

```bash
sed -n '1,260p' docs/superpowers/specs/2026-04-20-series-completion-loop-design.md
```

Then verify manually that the implementation covers:

- shared orchestrator skill
- reusable project runtime folder
- bounded state machine
- automation prompt guidance
- failure recovery and re-entry
- both `autonomous` and `approval-gated`

- [ ] **Step 5: Commit the verification touch-up if needed**

If verification required fixes, run:

```bash
git add skills/series-completion-loop projects README.md USAGE_FAQ.md
git commit -m "chore: finalize series completion loop integration"
```

Expected: commit succeeds only if a post-review fix was necessary
