#!/usr/bin/env python3
"""Validate series-qa diagnosis-only boundary wording."""

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
        "skills/series-qa/SKILL.md",
        "series-qa hard boundary",
        (
            "This skill is diagnosis-only.",
            "Do not produce reconstruction packages, re-entry drafting packets, or rewrite plans in this skill.",
            "python3 skills/series-qa/scripts/validate_diagnostic_boundaries.py",
            "`longform-story-design`",
            "`novel-writing`",
            "`character-voice-bible`",
        ),
    ),
    RequiredText(
        "skills/series-qa/references/diagnostic-workflow.md",
        "diagnostic workflow handoff",
        (
            "## End At Diagnostic Handoff",
            "`repair direction`",
            "`handoff target`",
            "`re-audit gate`",
        ),
    ),
    RequiredText(
        "skills/series-qa/references/report-templates.md",
        "QA report output contract",
        (
            "Repair direction:",
            "Handoff target:",
            "Recheck condition:",
            "Reader-visible damage:",
            "Classification: root cause | downstream symptom",
            "Diagnostic priority:",
        ),
    ),
    RequiredText(
        "skills/series-qa/references/regression-checks.md",
        "recheck outcome contract",
        (
            "`QA pass`",
            "`needs longform recovery`",
            "`needs local rewrite`",
            "original evidence",
            "prior re-audit gate",
            "revised evidence",
            "pass/fail comparison against the prior gate",
            "hand the work to `longform-story-design`",
        ),
    ),
    RequiredText(
        "Platform/OpenAI/GPT-OSS/skills/series-qa/SKILL.md",
        "GPT-OSS series-qa boundary",
        (
            "This skill is diagnosis-only.",
            "repair direction",
            "downstream handoff target",
            "re-audit gate",
            "Do not produce reconstruction packages, re-entry drafting packets, or rewrite plans in this skill.",
        ),
    ),
    RequiredText(
        "Platform/OpenAI/GPT-OSS/ROUTER.md",
        "GPT-OSS router series-qa boundary",
        (
            "repair direction",
            "handoff target",
            "re-audit gate",
        ),
    ),
)


FORBIDDEN_TEXTS: tuple[ForbiddenText, ...] = (
    ForbiddenText(
        "skills/series-qa",
        "series-qa repair-planning labels",
        (
            "Smallest viable fix:",
            "Minimal fix:",
            "Revision priority:",
            "## Repair Rule",
            "High-level fix type:",
            "Downstream owner:",
            "Recheck after downstream revision:",
            "minimal repair path",
            "revision brief",
        ),
    ),
    ForbiddenText(
        "Platform/OpenAI/GPT-OSS/skills/series-qa/SKILL.md",
        "GPT-OSS repair-planning labels",
        (
            "smallest viable fix",
            "Smallest viable fix",
            "revision brief",
            "Revision priority:",
        ),
    ),
    ForbiddenText(
        "Platform/OpenAI/GPT-OSS/ROUTER.md",
        "GPT-OSS router repair-planning labels",
        (
            "smallest viable fix",
            "Smallest viable fix",
            "revision brief",
            "Revision priority:",
        ),
    ),
)


def repo_root_from_args(argv: list[str]) -> Path:
    if len(argv) > 2:
        raise SystemExit("usage: validate_diagnostic_boundaries.py [repo-root]")
    if len(argv) == 2:
        return Path(argv[1]).resolve()
    return ROOT_FROM_SCRIPT


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def markdown_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(path.rglob("*.md"))


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
    if not path.exists():
        return [f"{check.path}: missing path for {check.label}"]
    failures: list[str] = []
    for file_path in markdown_files(path):
        text = read_text(file_path)
        for needle in check.needles:
            if needle in text:
                failures.append(
                    f"{file_path.relative_to(root)}: forbidden {needle!r} for {check.label}"
                )
    return failures


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

    print("OK series-qa diagnostic boundary validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
