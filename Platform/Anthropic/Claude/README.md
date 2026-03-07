# Anthropic / Claude Code

이 폴더는 Claude Code 환경에서 이 스킬 세트를 적용할 때 사용하는 플랫폼 전용 파일을 모아두는 자리입니다.

## Claude Code 규칙 파일 컨벤션

Claude Code는 세션 시작 시 `CLAUDE.md`를 자동으로 읽어 프로젝트 규칙으로 적용합니다.
이 파일이 OpenAI Codex의 `AGENTS.md`, Google Antigravity의 `AGENTS.md`(user_rules)에 해당합니다.

계층적으로 여러 `CLAUDE.md`를 배치할 수 있으며, 하위 폴더의 파일이 상위를 덮어씁니다.

## 목적

- Claude Code에서 필요한 운영 파일을 분리해서 관리
- 공용 스킬 본문과 플랫폼별 설정을 분리
- 다른 플랫폼과 비교하면서 교체 적용 가능하게 유지

## 포함된 적용 파일

- `CLAUDE.md` — 워크스페이스 루트에 복사하여 사용
- `skills/character-voice-bible/commands/voice.md` — `/voice` 슬래시 커맨드 정의
- `skills/longform-story-design/commands/plot.md` — `/plot` 슬래시 커맨드 정의
- `skills/novel-writing/commands/draft.md` — `/draft` 슬래시 커맨드 정의
- `skills/series-qa/commands/qa.md` — `/qa` 슬래시 커맨드 정의

## 적용 방식

1. 이 폴더의 `CLAUDE.md`를 워크스페이스 루트의 `CLAUDE.md`로 복사하거나 교체한다.
2. 이 폴더의 `skills/*/commands/*.md` 파일들을 대상 워크스페이스 `.claude/commands/` 경로에 복사한다.
3. `skills/` 본문과 `skills/*/references/`가 대상 워크스페이스에 함께 존재하는지 확인한다.
4. Claude Code 세션을 새로 열어서 `CLAUDE.md`가 자동으로 로드되는지 확인한다.

## 플랫폼 전환 가이드

다른 플랫폼에서 Claude Code로 전환할 때 처리해야 하는 파일 목록입니다.

### OpenAI Codex → Claude

| 작업 | 대상 경로 |
|------|-----------|
| **교체** | 루트 `AGENTS.md` → 이 폴더의 `CLAUDE.md`로 교체한다 (`AGENTS.md`는 삭제) |
| **추가** | 이 폴더의 `skills/*/commands/*.md` → 워크스페이스 `.claude/commands/`에 복사한다 |
| **삭제** | `skills/*/agents/openai.yaml` 파일들을 삭제한다 (Claude Code에서는 사용 안 함) |

### Google Antigravity → Claude

| 작업 | 대상 경로 |
|------|-----------|
| **교체** | 루트 `AGENTS.md` → 이 폴더의 `CLAUDE.md`로 교체한다 (`AGENTS.md`는 삭제) |
| **추가** | 이 폴더의 `skills/*/commands/*.md` → 워크스페이스 `.claude/commands/`에 복사한다 |
| **삭제** | `skills/*/agents/antigravity.yaml` 파일들을 삭제한다 (Claude Code에서는 사용 안 함) |

## 체크리스트

- [ ] 루트에 `CLAUDE.md`가 존재하는가
- [ ] `.claude/commands/` 안에 슬래시 커맨드 파일이 들어 있는가
- [ ] `skills/`와 `skills/*/references/` 경로가 상대경로 기준으로 맞는가
- [ ] `drafts/초고`, `drafts/개고`, `drafts/원고` 저장 규칙이 유지되는가

## 메모

- `CLAUDE.md`는 세션 시작 시 자동으로 한 번 읽힙니다. 세션 도중 변경해도 즉시 반영되지 않습니다.
- 슬래시 커맨드 파일(`.claude/commands/`)은 Claude Code 전용 기능입니다. Claude.ai 웹 등 다른 환경에서는 작동하지 않습니다.
- `SKILL.md`와 `skills/*/references/`는 공용 자산이므로 루트 `skills/`를 그대로 사용합니다.
