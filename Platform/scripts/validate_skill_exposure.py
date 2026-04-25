#!/usr/bin/env python3
"""Validate that platform packs expose every root skill.

The check is intentionally text/file based and dependency-free. It catches
packaging drift when root `skills/*/SKILL.md` entries change.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


ROOT_FROM_SCRIPT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class FilePattern:
    label: str
    template: str
    required_text: tuple[str, ...] = ()
    allow_multiple: bool = False


@dataclass(frozen=True)
class DocCheck:
    path: str
    label: str
    required_text: tuple[str, ...]


FILE_PATTERNS: tuple[FilePattern, ...] = (
    FilePattern(
        label="Codex openai metadata",
        template="Platform/OpenAI/Codex/skills/{skill}/agents/openai.yaml",
        required_text=("interface:", "display_name:", "short_description:", "default_prompt:"),
    ),
    FilePattern(
        label="Antigravity metadata",
        template="Platform/Google/Antigravity/skills/{skill}/agents/antigravity.yaml",
        required_text=("interface:", "display_name:", "short_description:", "default_prompt:"),
    ),
    FilePattern(
        label="Claude slash command",
        template="Platform/Anthropic/Claude/skills/{skill}/commands/*.md",
        required_text=("skills/{skill}/SKILL.md",),
        allow_multiple=True,
    ),
    FilePattern(
        label="GPT-OSS skill layer",
        template="Platform/OpenAI/GPT-OSS/skills/{skill}/SKILL.md",
    ),
)


SKILL_DOCS: tuple[DocCheck, ...] = (
    DocCheck(
        path="Platform/OpenAI/Codex/README.md",
        label="Codex README applied files",
        required_text=("skills/{skill}/agents/openai.yaml",),
    ),
    DocCheck(
        path="Platform/Google/Antigravity/README.md",
        label="Antigravity README applied files",
        required_text=("skills/{skill}/agents/antigravity.yaml",),
    ),
    DocCheck(
        path="Platform/Anthropic/Claude/README.md",
        label="Claude README command files",
        required_text=("skills/{skill}/commands/",),
    ),
    DocCheck(
        path="Platform/OpenAI/GPT-OSS/README.md",
        label="GPT-OSS README skill files",
        required_text=("skills/{skill}/SKILL.md",),
    ),
    DocCheck(
        path="Platform/OpenAI/GPT-OSS/ROUTER.md",
        label="GPT-OSS router skill names",
        required_text=("`{skill}`", "projects/<series-slug>"),
    ),
    DocCheck(
        path="Platform/OpenAI/GPT-OSS/SYSTEM_PROMPT.md",
        label="GPT-OSS system prompt skill names",
        required_text=("`{skill}`", "projects/<series-slug>"),
    ),
    DocCheck(
        path="Platform/Local/Ollama/SYSTEM_PROMPT.md",
        label="Ollama system prompt skill names",
        required_text=("`{skill}`", "projects/<series-slug>"),
    ),
    DocCheck(
        path="Platform/Local/Ollama/MODEL_PRESETS.md",
        label="Ollama model presets skill names",
        required_text=("`{skill}`", "projects/<series-slug>"),
    ),
    DocCheck(
        path="Platform/Local/Ollama/MODELFILE_EXAMPLE.md",
        label="Ollama Modelfile skill names",
        required_text=("`{skill}`", "projects/<series-slug>"),
    ),
    DocCheck(
        path="Platform/Local/Ollama/OPEN_WEBUI_SETUP.md",
        label="Ollama Open WebUI skill names",
        required_text=("`{skill}`", "projects/<series-slug>"),
    ),
    DocCheck(
        path="Platform/OpenAI/Codex/AGENTS.md",
        label="Codex runtime gate",
        required_text=("`series-completion-loop`", "projects/<series-slug>"),
    ),
    DocCheck(
        path="Platform/Google/Antigravity/AGENTS.md",
        label="Antigravity runtime gate",
        required_text=("`series-completion-loop`", "projects/<series-slug>"),
    ),
    DocCheck(
        path="Platform/Anthropic/Claude/CLAUDE.md",
        label="Claude runtime gate",
        required_text=("`series-completion-loop`", "projects/<series-slug>"),
    ),
    DocCheck(
        path="Platform/OpenAI/GPT-OSS/skills/series-completion-loop/SKILL.md",
        label="GPT-OSS series loop runtime gate",
        required_text=("projects/<series-slug>", "`novel-writing`", "state/runtime.yaml"),
    ),
)


GLOBAL_DOCS: tuple[DocCheck, ...] = (
    DocCheck(
        path="README.md",
        label="root README layer count",
        required_text=("series-completion-loop",),
    ),
    DocCheck(
        path="Platform/README.md",
        label="Platform README validation command",
        required_text=("validate_skill_exposure.py",),
    ),
    DocCheck(
        path="Platform/OpenAI/GPT-OSS/MIGRATION_MAP.md",
        label="GPT-OSS migration skill count",
        required_text=("skills/*/SKILL.md",),
    ),
)


FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "4개 `agents/openai.yaml`",
    "4개 `skills/*/SKILL.md`",
    "4개 `SKILL.md`",
    "4개의 전문 스킬",
    "4계층",
    "4-Tier",
    "only four",
    "four skill",
)


FORBIDDEN_DOCS: tuple[str, ...] = (
    "README.md",
    "Platform/README.md",
    "Platform/OpenAI/Codex/README.md",
    "Platform/OpenAI/GPT-OSS/README.md",
    "Platform/OpenAI/GPT-OSS/MIGRATION_MAP.md",
    "Platform/OpenAI/GPT-OSS/ROUTER.md",
    "Platform/OpenAI/GPT-OSS/SYSTEM_PROMPT.md",
    "Platform/Local/Ollama/SYSTEM_PROMPT.md",
    "Platform/Local/Ollama/MODELFILE_EXAMPLE.md",
    "Platform/Local/Ollama/MODEL_PRESETS.md",
    "Platform/Local/Ollama/OPEN_WEBUI_SETUP.md",
)


def repo_root_from_args(argv: list[str]) -> Path:
    if len(argv) > 2:
        raise SystemExit("usage: validate_skill_exposure.py [repo-root]")
    if len(argv) == 2:
        return Path(argv[1]).resolve()
    return ROOT_FROM_SCRIPT


def discover_skills(root: Path) -> list[str]:
    skill_root = root / "skills"
    if not skill_root.exists():
        raise SystemExit(f"missing skill root: {skill_root}")
    return sorted(
        path.parent.name
        for path in skill_root.glob("*/SKILL.md")
        if not path.parent.name.startswith(".")
    )


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_file_pattern(root: Path, skills: list[str], pattern: FilePattern) -> list[str]:
    failures: list[str] = []
    for skill in skills:
        rendered = pattern.template.format(skill=skill)
        matches = sorted(root.glob(rendered))
        if not matches:
            failures.append(f"{pattern.label}: missing {rendered}")
            continue
        if pattern.allow_multiple:
            texts = [read_text(match) for match in matches]
            for required in pattern.required_text:
                rendered_required = required.format(skill=skill)
                if not any(rendered_required in text for text in texts):
                    failures.append(
                        f"{pattern.label}: {rendered} missing {rendered_required!r}"
                    )
            continue
        if len(matches) > 1:
            failures.append(f"{pattern.label}: multiple matches for {rendered}")
            continue
        text = read_text(matches[0])
        for required in pattern.required_text:
            rendered_required = required.format(skill=skill)
            if rendered_required not in text:
                failures.append(
                    f"{pattern.label}: {matches[0].relative_to(root)} missing {rendered_required!r}"
                )
    return failures


def check_doc(root: Path, skills: list[str], check: DocCheck) -> list[str]:
    path = root / check.path
    if not path.exists():
        return [f"{check.label}: missing {check.path}"]
    text = read_text(path)
    failures: list[str] = []
    for required in check.required_text:
        values = skills if "{skill}" in required else [""]
        for skill in values:
            rendered = required.format(skill=skill)
            if rendered not in text:
                failures.append(f"{check.label}: {check.path} missing {rendered!r}")
    return failures


def check_forbidden(root: Path) -> list[str]:
    failures: list[str] = []
    for relative in FORBIDDEN_DOCS:
        path = root / relative
        if not path.exists():
            continue
        text = read_text(path)
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in text:
                failures.append(f"stale wording: {path.relative_to(root)} contains {pattern!r}")
    return failures


def main(argv: list[str]) -> int:
    root = repo_root_from_args(argv)
    skills = discover_skills(root)
    failures: list[str] = []

    for pattern in FILE_PATTERNS:
        failures.extend(check_file_pattern(root, skills, pattern))
    for check in (*SKILL_DOCS, *GLOBAL_DOCS):
        failures.extend(check_doc(root, skills, check))
    failures.extend(check_forbidden(root))

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print("OK platform skill exposure validation passed")
    print("skills: " + ", ".join(skills))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
