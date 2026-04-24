#!/usr/bin/env python3
"""Validate series-completion runtime template fields.

This is a text-level drift guard, not a YAML parser. It intentionally has no
external dependencies so agents can run it before merging template changes.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


@dataclass(frozen=True)
class Check:
    path: str
    label: str
    needles: tuple[str, ...]
    forbidden: tuple[str, ...] = ()


@dataclass(frozen=True)
class SectionCheck:
    path: str
    heading: str
    label: str
    needles: tuple[str, ...]


CHECKS: tuple[Check, ...] = (
    Check(
        "projects/_template/project.md",
        "project fields",
        (
            "- Title:",
            "- Slug:",
            "- Target scale:",
            "- Completion mode: autonomous | approval-gated",
            "- Default batch size: 3~5",
            "- Ending promise:",
        ),
    ),
    Check(
        "projects/_template/state/runtime.yaml",
        "runtime state keys",
        (
            "mode:",
            "state:",
            "next_action:",
            "approval_pending:",
            "last_approval_at:",
            "last_approval_batch_start:",
            "last_approval_batch_end:",
            "last_approval_note:",
            "current_batch_start:",
            "current_batch_end:",
            "latest_manuscript_batch:",
            "last_run_at:",
            "failure_count:",
            "blocked_reason:",
            "last_completed_stage:",
            "last_completed_transition:",
            "last_artifact_pointer:",
            "last_proof_predicate:",
            "specialist_return_accepted:",
            "last_valid_boundary:",
            "last_snapshot_paths:",
            "last_mismatch_evidence:",
        ),
    ),
    Check(
        "projects/_template/state/active-slice.yaml",
        "active slice keys",
        (
            "chapter_start:",
            "chapter_end:",
            "batch_goal:",
            "success_conditions:",
            "active_pov:",
            "active_cast:",
            "must_keep:",
            "must_not_break:",
            "handoff_target:",
            "planning_artifact:",
            "proof_artifact_paths:",
        ),
    ),
    Check(
        "projects/_template/state/handoff.md",
        "handoff evidence fields",
        (
            "## Runtime Stop Evidence",
            "- state:",
            "- next_action:",
            "- current_batch_start:",
            "- current_batch_end:",
            "- last_run_at:",
            "- last_completed_stage:",
            "- last_completed_transition:",
            "- last_artifact_pointer:",
            "- last_proof_predicate:",
            "- specialist_return_accepted:",
            "- last_valid_boundary:",
            "- last_snapshot_paths:",
            "- last_mismatch_evidence:",
            "## Specialist Return Evidence",
            "- specialist:",
            "- transition:",
            "- source_artifact:",
            "- returned_artifact:",
            "- batch_range:",
            "- excerpt_range:",
            "- required_fields_checked:",
            "- proof_artifact_paths:",
            "- next_handoff_target:",
            "## Evidence By Specialist Type",
            "### Slice Planning",
            "- chapter_start:",
            "- chapter_end:",
            "- batch_goal:",
            "- success_conditions:",
            "- active_pov:",
            "- active_cast:",
            "- must_keep:",
            "- must_not_break:",
            "- handoff_target:",
            "- planning_artifact:",
            "- proof_artifact_paths:",
            "### Drafting",
            "- chapters_drafted:",
            "- stage_files:",
            "- latest_manuscript_batch:",
            "- assumptions:",
            "- continuity_notes:",
            "- next_handoff_target:",
            "### QA Review",
            "- reviewed_batch_range:",
            "- outcome:",
            "- evidence:",
            "- root_cause:",
            "- repair_direction:",
            "- re_audit_gate:",
            "- handoff_target:",
            "### Recovery Planning",
            "- root_cause:",
            "- repair_order:",
            "- next_safe_move:",
            "- handoff_target:",
            "- must_not_break_constraints:",
            "- proof_artifact_paths:",
            "- exact_re_entry_slice:",
            "### Voice Handoff",
            "- voice_handoff:",
            "- source_artifact:",
            "- affected_speakers:",
            "- relationship_state:",
            "- voice_failure:",
            "- repair_rules:",
            "- proof_rewrites:",
            "- register_notes:",
            "- assumptions:",
            "- unresolved_voice_risks:",
            "- next_handoff_target:",
            "## Blocked Evidence",
            "- block_type:",
            "- blocked_reason:",
            "- proof_artifact_path:",
            "- proof_predicate:",
            "- mismatch_type:",
            "- mismatch_evidence:",
            "## Snapshot And Re-entry Evidence",
            "- snapshot_paths:",
            "- last_valid_boundary:",
            "- re_entry_state:",
            "- re_entry_batch:",
        ),
    ),
    Check(
        "projects/_template/qa/latest-report.md",
        "QA report fields",
        (
            "- Reviewed batch range:",
            "- Outcome: [ready_next_slice | needs_recovery | blocked]",
            "- Evidence:",
            "- Root cause:",
            "- Repair direction:",
            "- Handoff target:",
            "- Re-audit gate:",
            "- Artifact evidence:",
            "- Blocked reason:",
        ),
    ),
    Check(
        "projects/_template/recovery/latest-recovery.md",
        "recovery report fields",
        (
            "- Root cause:",
            "- Repair order:",
            "- Next safe move:",
            "- Handoff target:",
            "- Must-not-break constraints:",
            "- Proof artifact path(s):",
            "- Exact re-entry slice:",
            "- Affected ledgers:",
            "- Blocked reason:",
        ),
    ),
    Check(
        "projects/README.md",
        "project runtime README rules",
        (
            "Runtime stop evidence is recorded in `state/runtime.yaml`",
            "Specialist return evidence should stay machine-checkable",
            "Fresh template copies start with empty batch fields.",
            "block as missing state",
            "Manuscript files stay in `drafts/`.",
        ),
    ),
    Check(
        "skills/series-completion-loop/SKILL.md",
        "skill validation instruction",
        (
            "## Template Drift Check",
            "python3 skills/series-completion-loop/scripts/validate_runtime_template.py",
            "- `* -> blocked`",
            "`planning_artifact`",
            "`proof_artifact_paths`",
        ),
        ("- any state -> `blocked`",),
    ),
    Check(
        "skills/series-completion-loop/references/runtime-layout.md",
        "runtime layout validation instruction",
        (
            "## Template Drift Check",
            "python3 skills/series-completion-loop/scripts/validate_runtime_template.py",
            "`planning_artifact`",
            "`proof_artifact_paths`",
        ),
    ),
    Check(
        "skills/series-completion-loop/references/failure-reentry.md",
        "failure re-entry required field contract",
        (
            "required `project.md` fields are Title, Slug, Target scale, Completion mode, Default batch size, and Ending promise",
            "required `state/active-slice.yaml` keys are `chapter_start`, `chapter_end`, `batch_goal`, `success_conditions`, `active_pov`, `active_cast`, `must_keep`, `must_not_break`, `handoff_target`, `planning_artifact`, and `proof_artifact_paths`",
        ),
    ),
    Check(
        "skills/series-completion-loop/references/state-machine.md",
        "state machine wildcard block contract",
        (
            "- `* -> blocked`",
            "Use the canonical wildcard form `* -> blocked`",
        ),
    ),
)


SECTION_CHECKS: tuple[SectionCheck, ...] = (
    SectionCheck(
        "projects/_template/state/handoff.md",
        "## Runtime Stop Evidence",
        "handoff runtime stop evidence section",
        (
            "- state:",
            "- next_action:",
            "- current_batch_start:",
            "- current_batch_end:",
            "- last_run_at:",
            "- last_completed_stage:",
            "- last_completed_transition:",
            "- last_artifact_pointer:",
            "- last_proof_predicate:",
            "- specialist_return_accepted:",
            "- last_valid_boundary:",
            "- last_snapshot_paths:",
            "- last_mismatch_evidence:",
        ),
    ),
    SectionCheck(
        "projects/_template/state/handoff.md",
        "## Specialist Return Evidence",
        "handoff specialist return evidence section",
        (
            "- specialist:",
            "- transition:",
            "- source_artifact:",
            "- returned_artifact:",
            "- batch_range:",
            "- excerpt_range:",
            "- required_fields_checked:",
            "- proof_artifact_paths:",
            "- next_handoff_target:",
        ),
    ),
    SectionCheck(
        "projects/_template/state/handoff.md",
        "### Slice Planning",
        "handoff slice planning section",
        (
            "- chapter_start:",
            "- chapter_end:",
            "- batch_goal:",
            "- success_conditions:",
            "- active_pov:",
            "- active_cast:",
            "- must_keep:",
            "- must_not_break:",
            "- handoff_target:",
            "- planning_artifact:",
            "- proof_artifact_paths:",
        ),
    ),
    SectionCheck(
        "projects/_template/state/handoff.md",
        "### Drafting",
        "handoff drafting section",
        (
            "- chapters_drafted:",
            "- stage_files:",
            "- latest_manuscript_batch:",
            "- assumptions:",
            "- continuity_notes:",
            "- next_handoff_target:",
        ),
    ),
    SectionCheck(
        "projects/_template/state/handoff.md",
        "### QA Review",
        "handoff QA review section",
        (
            "- reviewed_batch_range:",
            "- outcome:",
            "- evidence:",
            "- root_cause:",
            "- repair_direction:",
            "- re_audit_gate:",
            "- handoff_target:",
        ),
    ),
    SectionCheck(
        "projects/_template/state/handoff.md",
        "### Recovery Planning",
        "handoff recovery planning section",
        (
            "- root_cause:",
            "- repair_order:",
            "- next_safe_move:",
            "- handoff_target:",
            "- must_not_break_constraints:",
            "- proof_artifact_paths:",
            "- exact_re_entry_slice:",
        ),
    ),
    SectionCheck(
        "projects/_template/state/handoff.md",
        "### Voice Handoff",
        "handoff voice section",
        (
            "- voice_handoff:",
            "- source_artifact:",
            "- affected_speakers:",
            "- relationship_state:",
            "- voice_failure:",
            "- repair_rules:",
            "- proof_rewrites:",
            "- register_notes:",
            "- assumptions:",
            "- unresolved_voice_risks:",
            "- next_handoff_target:",
        ),
    ),
    SectionCheck(
        "projects/_template/state/handoff.md",
        "## Blocked Evidence",
        "handoff blocked evidence section",
        (
            "- block_type:",
            "- blocked_reason:",
            "- proof_artifact_path:",
            "- proof_predicate:",
            "- mismatch_type:",
            "- mismatch_evidence:",
        ),
    ),
    SectionCheck(
        "projects/_template/state/handoff.md",
        "## Snapshot And Re-entry Evidence",
        "handoff snapshot and re-entry section",
        (
            "- snapshot_paths:",
            "- last_valid_boundary:",
            "- re_entry_state:",
            "- re_entry_batch:",
        ),
    ),
)


def repo_root_from_args(argv: list[str]) -> Path:
    if len(argv) > 2:
        raise SystemExit("usage: validate_runtime_template.py [repo-root]")
    if len(argv) == 2:
        return Path(argv[1]).resolve()
    return Path(__file__).resolve().parents[3]


def run_check(root: Path, check: Check) -> list[str]:
    target = root / check.path
    if not target.exists():
        return [f"{check.path}: missing file"]

    text = target.read_text(encoding="utf-8")
    missing = [
        f"{check.path}: missing {needle!r} for {check.label}"
        for needle in check.needles
        if needle not in text
    ]
    forbidden = [
        f"{check.path}: forbidden {needle!r} for {check.label}"
        for needle in check.forbidden
        if needle in text
    ]
    return missing + forbidden


def heading_level(heading: str) -> int:
    return len(heading) - len(heading.lstrip("#"))


def extract_section(text: str, heading: str) -> str | None:
    lines = text.splitlines()
    start = next(
        (index for index, line in enumerate(lines) if line.strip() == heading),
        None,
    )
    if start is None:
        return None

    level = heading_level(heading)
    end = len(lines)
    for index in range(start + 1, len(lines)):
        stripped = lines[index].lstrip()
        if not stripped.startswith("#"):
            continue
        next_level = heading_level(stripped)
        if next_level <= level and stripped[next_level : next_level + 1] == " ":
            end = index
            break
    return "\n".join(lines[start:end])


def run_section_check(root: Path, check: SectionCheck) -> list[str]:
    target = root / check.path
    if not target.exists():
        return [f"{check.path}: missing file"]

    text = target.read_text(encoding="utf-8")
    section = extract_section(text, check.heading)
    if section is None:
        return [f"{check.path}: missing section {check.heading!r}"]

    return [
        f"{check.path}: missing {needle!r} in {check.heading!r} for {check.label}"
        for needle in check.needles
        if needle not in section
    ]


def main(argv: list[str]) -> int:
    root = repo_root_from_args(argv)
    failures: list[str] = []

    for check in CHECKS:
        failures.extend(run_check(root, check))
    for section_check in SECTION_CHECKS:
        failures.extend(run_section_check(root, section_check))

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print("OK series runtime template validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
