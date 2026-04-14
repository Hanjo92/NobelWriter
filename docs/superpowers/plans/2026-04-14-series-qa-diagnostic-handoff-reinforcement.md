# Series QA Diagnostic-Handoff Reinforcement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reinforce `series-qa` as a diagnosis-only skill that isolates failures and hands deeper recovery work to `longform-story-design`.

**Architecture:** Tighten the main skill first so its ownership, diagnostic order, and output contract are explicit, then align the core diagnostic references so templates and recheck language stay QA-first and handoff-aware. Only touch prompt examples if the main wording still leaves repair ownership ambiguous.

**Tech Stack:** Markdown skill docs, repository conventions, GitHub issue tracking

---

### Task 1: Patch Main Series QA Contract

**Files:**
- Modify: `skills/series-qa/SKILL.md`

- [ ] **Step 1: Add hard diagnosis-only boundaries and handoff rules near the top**
- [ ] **Step 2: Add a canonical diagnostic order ending in handoff and re-audit gating**
- [ ] **Step 3: Narrow the output contract to QA artifacts and directional repair notes only**
- [ ] **Step 4: Self-review for overlap with `longform-story-design`, `novel-writing`, and `character-voice-bible`**

### Task 2: Align Diagnostic Workflow And Templates

**Files:**
- Modify: `skills/series-qa/references/diagnostic-workflow.md`
- Modify: `skills/series-qa/references/report-templates.md`
- Modify: `skills/series-qa/references/regression-checks.md`

- [ ] **Step 1: Make workflow end in diagnostic handoff rather than repair design**
- [ ] **Step 2: Update report templates to include repair direction and handoff target without becoming rebuild plans**
- [ ] **Step 3: Update recheck language so it distinguishes QA pass, needs longform recovery, and needs local rewrite**
- [ ] **Step 4: Self-review for consistency with the main skill**

### Task 3: Optional Trigger Example Check

**Files:**
- Inspect: `skills/series-qa/references/example-prompts.md`

- [ ] **Step 1: Re-read `example-prompts.md` after the main wording changes land**
- [ ] **Step 2: Patch only if the examples still imply broader repair ownership**

### Task 4: Verification

**Files:**
- Inspect: `skills/series-qa/SKILL.md`
- Inspect: `skills/series-qa/references/diagnostic-workflow.md`
- Inspect: `skills/series-qa/references/report-templates.md`
- Inspect: `skills/series-qa/references/regression-checks.md`
- Inspect: `skills/series-qa/references/example-prompts.md`
- Inspect: `docs/superpowers/specs/2026-04-14-series-qa-diagnostic-handoff-design.md`

- [ ] **Step 1: Read changed files end-to-end and check for contradictions**
- [ ] **Step 2: Confirm the approved spec is covered**
- [ ] **Step 3: Run `git diff --check` and `git diff --stat`**
- [ ] **Step 4: Report what changed, what was verified, and any remaining follow-up**
