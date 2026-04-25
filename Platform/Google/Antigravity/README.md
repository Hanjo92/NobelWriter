# Google / Antigravity

이 폴더는 Google의 Antigravity 에이전트 환경에서 이 스킬 세트를 적용할 때 사용하는 플랫폼 전용 파일을 모아두는 자리입니다.

## 목적

- Antigravity에서 필요한 운영 파일을 분리해서 관리
- 공용 스킬 본문과 플랫폼별 설정을 분리
- 다른 플랫폼과 비교하면서 교체 적용 가능하게 유지

## 포함된 적용 파일

이 폴더에는 현재 Antigravity 적용에 필요한 운영 파일 사본이 들어 있습니다.

- `AGENTS.md`
- `JULES_NO_TOOLS_FALLBACK_TEMPLATE.md`
- `SHORT_NO_TOOLS_POLICY.md`
- `skills/character-voice-bible/agents/antigravity.yaml`
- `skills/longform-story-design/agents/antigravity.yaml`
- `skills/novel-writing/agents/antigravity.yaml`
- `skills/series-completion-loop/agents/antigravity.yaml`
- `skills/series-qa/agents/antigravity.yaml`

이 파일들은 루트 워크스페이스에서 사용하는 Antigravity용 운영 파일을 플랫폼 패키지로 따로 모아둔 것입니다.
Antigravity는 `<user_rules>`(AGENTS.md)를 통해 지침을 숙지하고, 스킬 시스템을 통해 특정 작업을 분리 수행할 수 있습니다.

## 적용 방식

권장 흐름:

1. 이 폴더의 `AGENTS.md`를 워크스페이스 루트의 `AGENTS.md`로 복사하거나 교체한다. (Antigravity는 이 파일을 자동으로 `user_rules`로 로드합니다)
2. 이 폴더의 `skills/*/agents/antigravity.yaml` 파일들을 대상 워크스페이스의 같은 경로에 복사하거나 교체한다.
3. `skills/` 본문과 `skills/*/references/`가 대상 워크스페이스에 함께 존재하는지 확인한다.
4. 지정된 저장 폴더(`drafts/초고` 등) 생성이 원활한지 확인한다.

도구 제한으로 인해 Jules가 "외부 API를 쓸 수 없어 작업할 수 없다"는 식으로 멈추는 경우에는 [JULES_NO_TOOLS_FALLBACK_TEMPLATE.md](./JULES_NO_TOOLS_FALLBACK_TEMPLATE.md)를 참고해, 저장 불가와 집필 불가를 분리한 응답 템플릿을 적용한다.
더 짧은 규칙 블록을 시스템 레이어에 바로 붙여 넣고 싶으면 [SHORT_NO_TOOLS_POLICY.md](./SHORT_NO_TOOLS_POLICY.md)를 사용한다.

## 플랫폼 전환 가이드

다른 플랫폼에서 Antigravity로 전환할 때 처리해야 하는 파일 목록입니다.

### OpenAI Codex → Antigravity

| 작업 | 대상 경로 |
|------|-----------|
| **교체** | `AGENTS.md` → 이 폴더의 `AGENTS.md`로 덮어쓴다 |
| **교체** | `skills/*/agents/openai.yaml` → 각각 `antigravity.yaml`로 교체한다 |
| **삭제** | `skills/*/agents/openai.yaml` 파일이 남아 있으면 제거한다 |

### Anthropic Claude → Antigravity

| 작업 | 대상 경로 |
|------|-----------|
| **교체** | 루트 `CLAUDE.md` → 이 폴더의 `AGENTS.md`로 교체한다 (`CLAUDE.md`는 삭제) |
| **추가** | `skills/*/agents/antigravity.yaml` 파일들을 각 스킬 폴더에 추가한다 |
| **삭제** | `.claude/commands/` 폴더 전체를 삭제한다 (Antigravity에서는 사용 안 함) |
| **삭제** | `skills/*/commands/*.md` 파일들을 삭제한다 |

## 체크리스트

- Antigravity에서 `AGENTS.md`를 `user_rules`로 읽는 구조인지
- `skills/*/agents/antigravity.yaml` 파일이 각 스킬 폴더에 들어 있는지
- `skills/`와 `skills/*/references/` 경로가 상대경로 기준으로 맞는지
- `drafts/초고`, `drafts/개고`, `drafts/원고` 저장 규칙이 유지되는지

## 메모

- 이 폴더는 Antigravity 운영 파일만 담습니다.
- `SKILL.md`와 `skills/*/references/`는 공용 자산이므로 기본적으로 루트 `skills/`를 사용합니다.
- 루트 파일이 변경되면 이 패키지 사본도 함께 갱신해야 합니다.
