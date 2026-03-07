# OpenAI / GPT-OSS

이 폴더는 GPT-OSS 환경에서 이 스킬 세트를 재패키징해서 적용할 때 사용하는 플랫폼 전용 파일을 모아두는 자리입니다.

## 목적

- Codex 전용 운영 레이어와 GPT-OSS용 운영 레이어를 분리
- 공용 스킬/레퍼런스 자산은 유지하고 플랫폼 종속 부분만 교체
- 사용자가 플랫폼에 맞는 파일만 골라 적용할 수 있게 정리

## 포함된 변환 대상 파일

이 폴더에는 GPT-OSS 이식 작업을 시작하기 위한 뼈대 파일이 들어 있습니다.

- `SYSTEM_PROMPT.md`
- `ROUTER.md`
- `MIGRATION_MAP.md`
- `skills/character-voice-bible/SKILL.md`
- `skills/longform-story-design/SKILL.md`
- `skills/novel-writing/SKILL.md`
- `skills/series-qa/SKILL.md`

이 파일들은 Codex 운영 파일을 GPT-OSS 방식으로 나누어 옮기기 위한 작업 시작점입니다.

## 적용 방식

권장 흐름:

1. `MIGRATION_MAP.md`를 읽고 Codex 파일이 GPT-OSS에서 어떤 파일로 분해되는지 확인한다.
2. `SYSTEM_PROMPT.md`와 `ROUTER.md`를 현재 GPT-OSS 환경에 맞게 채운다.
3. 4개 `skills/*/SKILL.md`를 GPT-OSS용 문구로 다듬는다.
4. 공용 자산인 루트 `skills/*/references/`와 연결한다.
5. 초고/개고/원고 저장 규칙은 별도 스크립트나 운영 절차로 보완한다.

## 플랫폼 전환 가이드

다른 플랫폼에서 GPT-OSS 패키지로 전환할 때 처리해야 하는 파일 목록입니다.

### OpenAI Codex → GPT-OSS

| 작업 | 대상 경로 |
|------|-----------|
| **대체** | 루트 `AGENTS.md`의 역할을 `SYSTEM_PROMPT.md` + `ROUTER.md`로 분리한다 |
| **대체** | `skills/*/agents/openai.yaml`은 직접 사용하지 않고 제거하거나 보관만 한다 |
| **추가** | 이 폴더의 `skills/*/SKILL.md`를 GPT-OSS용 작업층 문서로 사용한다 |
| **유지** | 루트 `skills/*/references/`와 `drafts/` 구조는 공용 자산으로 유지한다 |

### Google Antigravity → GPT-OSS

| 작업 | 대상 경로 |
|------|-----------|
| **대체** | 루트 `AGENTS.md`의 역할을 `SYSTEM_PROMPT.md` + `ROUTER.md`로 분리한다 |
| **대체** | `skills/*/agents/antigravity.yaml`은 직접 사용하지 않고 제거하거나 보관만 한다 |
| **추가** | 이 폴더의 `skills/*/SKILL.md`를 GPT-OSS용 작업층 문서로 사용한다 |
| **유지** | 루트 `skills/*/references/`와 `drafts/` 구조는 공용 자산으로 유지한다 |

### Anthropic Claude → GPT-OSS

| 작업 | 대상 경로 |
|------|-----------|
| **대체** | 루트 `CLAUDE.md`의 역할을 `SYSTEM_PROMPT.md` + `ROUTER.md`로 분리한다 (`CLAUDE.md`는 제거하거나 별도 보관) |
| **삭제** | `.claude/commands/` 및 `skills/*/commands/*.md`는 GPT-OSS에서 직접 사용하지 않는다 |
| **추가** | 이 폴더의 `skills/*/SKILL.md`를 GPT-OSS용 작업층 문서로 사용한다 |
| **유지** | 루트 `skills/*/references/`와 `drafts/` 구조는 공용 자산으로 유지한다 |

## 체크리스트

- Codex 전용 표현이 제거되었는지
- `$skill-name` 같은 호출 문법을 새 환경 방식으로 치환했는지
- 스킬 선택 규칙이 별도 라우터로 재구성되었는지
- 파일 저장 정책을 실제로 실행할 수 있는지

## 메모

이 README는 GPT-OSS용 이식 작업을 정리하기 위한 시작점입니다.  
실제 패키징이 시작되면 아래 섹션을 채워 넣습니다.

### 적용 파일 목록

- `SYSTEM_PROMPT.md`
- `ROUTER.md`
- `MIGRATION_MAP.md`
- `skills/character-voice-bible/SKILL.md`
- `skills/longform-story-design/SKILL.md`
- `skills/novel-writing/SKILL.md`
- `skills/series-qa/SKILL.md`

### 적용 순서

1. `MIGRATION_MAP.md` 확인
2. `SYSTEM_PROMPT.md` 정리
3. `ROUTER.md` 정리
4. 4개 `SKILL.md` 정리
5. 실제 GPT-OSS 환경에 주입 테스트

### 주의사항

- 이 폴더는 Codex 메타데이터를 그대로 복사하지 않습니다.
- `agents/openai.yaml`은 GPT-OSS 구조에 맞게 대체하거나 제거 대상입니다.
- `skills/*/references/`는 공용 자산으로 보고 기본적으로 루트 `skills/`를 그대로 사용합니다.
- GPT-OSS는 Codex나 Antigravity처럼 고정 메타데이터 파일 하나로 끝나는 구조가 아니므로, 실제 호스트 환경에 맞춘 주입 방식이 별도로 필요합니다.
