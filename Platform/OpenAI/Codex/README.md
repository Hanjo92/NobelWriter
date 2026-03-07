# OpenAI / Codex

이 폴더는 Codex 환경에서 NobelWriter 스킬 세트를 적용할 때 사용하는 플랫폼 전용 파일을 모아두는 자리입니다.

## 목적

- Codex에서 필요한 운영 파일을 분리해서 관리
- 공용 스킬 본문과 플랫폼별 설정을 분리
- 다른 플랫폼과 비교하면서 교체 적용 가능하게 유지

## 포함된 적용 파일

이 폴더에는 현재 Codex 적용에 필요한 운영 파일 사본이 들어 있습니다.

- `AGENTS.md`
- `skills/character-voice-bible/agents/openai.yaml`
- `skills/longform-story-design/agents/openai.yaml`
- `skills/novel-writing/agents/openai.yaml`
- `skills/series-qa/agents/openai.yaml`

이 파일들은 루트 워크스페이스에서 사용하는 Codex용 운영 파일을 플랫폼 패키지로 따로 모아둔 것입니다.

## 적용 방식

권장 흐름:

1. 이 폴더의 `AGENTS.md`를 워크스페이스 루트의 `AGENTS.md`로 복사하거나 교체한다.
2. 이 폴더의 `skills/*/agents/openai.yaml` 파일들을 대상 워크스페이스의 같은 경로에 복사하거나 교체한다.
3. `skills/` 본문과 `references/`가 대상 워크스페이스에 함께 존재하는지 확인한다.
4. 적용 후 스킬 호출, 라우팅, 파일 저장 규칙이 정상 동작하는지 확인한다.

## 체크리스트

- Codex에서 `AGENTS.md`를 읽는 구조인지
- 스킬 라우팅 규칙이 현재 저장소 구조와 맞는지
- `skills/` 경로 기준이 상대경로로 유지되는지
- `drafts/초고`, `drafts/개고`, `drafts/원고` 저장 규칙이 유지되는지

## 메모

이 README는 Codex용 플랫폼 파일을 정리하기 위한 시작점입니다.  
실제 적용 파일이 생기면 아래 섹션을 추가해 구체적으로 기록합니다.

### 적용 파일 목록

- `AGENTS.md`
- `skills/character-voice-bible/agents/openai.yaml`
- `skills/longform-story-design/agents/openai.yaml`
- `skills/novel-writing/agents/openai.yaml`
- `skills/series-qa/agents/openai.yaml`

### 적용 순서

1. `AGENTS.md` 적용
2. 4개 `agents/openai.yaml` 적용
3. `skills/`와 `drafts/` 구조 확인
4. Codex에서 실제 호출 테스트

### 주의사항

- 이 폴더는 Codex 운영 파일만 담습니다.
- `SKILL.md`와 `references/`는 공용 자산이므로 기본적으로 루트 `skills/`를 사용합니다.
- 루트 파일이 변경되면 이 패키지 사본도 함께 갱신해야 합니다.
