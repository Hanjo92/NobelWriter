#!/usr/bin/env python3
"""Validate longform-story-design recovery routing boundaries."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


ROOT_FROM_SCRIPT = Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class RequiredText:
    path: str
    label: str
    needles: tuple[str, ...]


@dataclass(frozen=True)
class ForbiddenText:
    path: str
    label: str
    needles: tuple[str, ...]


REQUIRED_TEXTS: tuple[RequiredText, ...] = (
    RequiredText(
        "skills/longform-story-design/SKILL.md",
        "root recovery ownership",
        (
            "report-only QA",
            "`recovery audit`",
            "`recovery rebuild`",
            "reusable planning package",
            "re-entry drafting packet",
            "active repaired slice",
            "python3 skills/longform-story-design/scripts/validate_recovery_boundaries.py",
        ),
    ),
    RequiredText(
        "skills/longform-story-design/references/project-intake.md",
        "project intake recovery routing",
        (
            "recovery package first",
            "re-entry drafting packet",
            "active repaired slice",
            "long damaged draft with no clear safe chapter boundary -> canon extraction sheet, continuity ledger, recovery plan, isolate the active repaired slice, then create a re-entry drafting packet before any prose drafting",
        ),
    ),
    RequiredText(
        "skills/longform-story-design/references/repair-existing-draft.md",
        "existing draft recovery package",
        (
            "reusable recovery package",
            "continuity ledger",
            "recovery plan",
            "re-entry drafting packet naming the active repaired slice",
            "continuity audit report only as supporting evidence",
            "recovery/latest-recovery.md",
        ),
    ),
    RequiredText(
        "skills/longform-story-design/references/planning-stack-selection.md",
        "stack selection recovery routing",
        (
            "report-only QA",
            "`series-qa`",
            "recovery plan",
            "re-entry drafting packet",
        ),
    ),
    RequiredText(
        "skills/longform-story-design/references/longform-workflow.md",
        "workflow recovery flow",
        (
            "Recovery Flow For Damaged Longform Drafts",
            "define the active repaired slice",
            "recovery plan",
            "re-entry drafting packet",
        ),
    ),
    RequiredText(
        "skills/longform-story-design/references/handoff-to-drafting.md",
        "drafting handoff active slice",
        (
            "active repaired slice",
            "Recovery package source:",
            "Re-entry reason:",
            "First safe draft objective:",
        ),
    ),
    RequiredText(
        "Platform/OpenAI/GPT-OSS/skills/longform-story-design/SKILL.md",
        "GPT-OSS recovery ownership",
        (
            "report-only QA",
            "`recovery audit`",
            "`recovery rebuild`",
            "reusable planning package",
            "re-entry drafting packet",
            "active repaired slice",
        ),
    ),
    RequiredText(
        "Platform/OpenAI/GPT-OSS/ROUTER.md",
        "GPT-OSS router recovery routing",
        (
            "recovery audit",
            "recovery rebuild",
            "re-entry drafting packet",
        ),
    ),
    RequiredText(
        "Platform/OpenAI/GPT-OSS/SYSTEM_PROMPT.md",
        "GPT-OSS system recovery routing",
        (
            "recovery audit/recovery rebuild",
            "`longform-story-design`",
        ),
    ),
)


FORBIDDEN_TEXTS: tuple[ForbiddenText, ...] = (
    ForbiddenText(
        "Platform/OpenAI/GPT-OSS/skills/longform-story-design/SKILL.md",
        "GPT-OSS stale recovery labels",
        (
            "`drift repair`",
            "repair pass",
        ),
    ),
    ForbiddenText(
        "Platform/OpenAI/GPT-OSS/ROUTER.md",
        "GPT-OSS router stale recovery labels",
        (
            "`drift repair`",
            "repair pass",
        ),
    ),
    ForbiddenText(
        "skills/longform-story-design/references/repair-existing-draft.md",
        "stale existing draft recovery bundle",
        (
            "drafting packet for the next safe chapter range",
        ),
    ),
)


def repo_root_from_args(argv: list[str]) -> Path:
    if len(argv) > 2:
        raise SystemExit("usage: validate_recovery_boundaries.py [repo-root]")
    if len(argv) == 2:
        return Path(argv[1]).resolve()
    return ROOT_FROM_SCRIPT


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required(root: Path, check: RequiredText) -> list[str]:
    path = root / check.path
    if not path.is_file():
        return [f"{check.path}: missing file for {check.label}"]
    text = read_text(path)
    return [
        f"{check.path}: missing {needle!r} for {check.label}"
        for needle in check.needles
        if needle not in text
    ]


def check_forbidden(root: Path, check: ForbiddenText) -> list[str]:
    path = root / check.path
    if not path.is_file():
        return [f"{check.path}: missing file for {check.label}"]
    text = read_text(path)
    return [
        f"{check.path}: forbidden {needle!r} for {check.label}"
        for needle in check.needles
        if needle in text
    ]


def main(argv: list[str]) -> int:
    root = repo_root_from_args(argv)
    failures: list[str] = []

    for check in REQUIRED_TEXTS:
        failures.extend(check_required(root, check))
    for check in FORBIDDEN_TEXTS:
        failures.extend(check_forbidden(root, check))

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print("OK longform recovery boundary validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
