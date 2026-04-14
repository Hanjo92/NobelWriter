# Longform Recovery Audit Reinforcement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reinforce `longform-story-design` so it cleanly handles long-range audit plus rebuild requests and routes lighter report-only work away from it.

**Architecture:** Update the main skill first so routing and execution order become explicit, then align the supporting references so intake, stack choice, workflow, and drafting handoff all follow the same recovery-aware model. Keep `series-qa` distinct unless the main skill changes still leave overlap.

**Tech Stack:** Markdown skill docs, repository conventions, GitHub issue tracking

---

### Task 1: Patch Main Skill Contract

**Files:**
- Modify: `skills/longform-story-design/SKILL.md`

- [ ] **Step 1: Add hard routing and responsibility boundaries near the top**
- [ ] **Step 2: Add one canonical decision order for mode, package, risk, stack, depth, and drafting slice**
- [ ] **Step 3: Add recovery-aware modes and recovery artifact minimums**
- [ ] **Step 4: Rework output contract so audit-plus-rebuild requests end in a reusable package**

### Task 2: Align Intake And Stack Selection

**Files:**
- Modify: `skills/longform-story-design/references/project-intake.md`
- Modify: `skills/longform-story-design/references/planning-stack-selection.md`

- [ ] **Step 1: Map intake outcomes to first recovery bundles**
- [ ] **Step 2: Add tie-break and precedence rules across project state, dominant risk, and scale**
- [ ] **Step 3: Verify the intake and stack rules match the main skill's execution order**

### Task 3: Align Workflow And Drafting Handoff

**Files:**
- Modify: `skills/longform-story-design/references/longform-workflow.md`
- Modify: `skills/longform-story-design/references/handoff-to-drafting.md`

- [ ] **Step 1: Add stage exit criteria for planning and recovery layers**
- [ ] **Step 2: Add a recovery workflow that reaches a re-entry drafting packet**
- [ ] **Step 3: Make drafting handoff define the active repaired slice, including multi-POV or multi-chapter cases**

### Task 4: Boundary Verification

**Files:**
- Inspect: `skills/series-qa/SKILL.md`

- [ ] **Step 1: Re-read `series-qa` after the longform changes land**
- [ ] **Step 2: Patch only if the boundary is still ambiguous**
- [ ] **Step 3: Verify the final wording keeps `series-qa` useful for report-first diagnosis**

### Task 5: Verification

**Files:**
- Inspect: `skills/longform-story-design/SKILL.md`
- Inspect: `skills/longform-story-design/references/project-intake.md`
- Inspect: `skills/longform-story-design/references/planning-stack-selection.md`
- Inspect: `skills/longform-story-design/references/longform-workflow.md`
- Inspect: `skills/longform-story-design/references/handoff-to-drafting.md`
- Inspect: `skills/series-qa/SKILL.md`

- [ ] **Step 1: Read changed files end-to-end and check for contradictions**
- [ ] **Step 2: Confirm the approved spec is covered**
- [ ] **Step 3: Run `git diff --check` and `git diff --stat`**
- [ ] **Step 4: Report what changed, what was verified, and any remaining follow-up**
