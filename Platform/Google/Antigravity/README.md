# Google / Antigravity

이 폴더는 Google의 Antigravity 에이전트 환경에서 NobelWriter 스킬 세트를 적용할 때 사용하는 플랫폼 전용 파일을 모아두는 자리입니다.

## 목적

- Antigravity에서 필요한 운영 파일을 분리해서 관리
- 공용 스킬 본문과 플랫폼별 설정을 분리
- 다른 플랫폼과 비교하면서 교체 적용 가능하게 유지

## 포함된 적용 파일

이 폴더에는 현재 Antigravity 적용에 필요한 운영 파일 사본이 들어 있습니다.

- `AGENTS.md`
- `skills/character-voice-bible/agents/antigravity.yaml`
- `skills/longform-story-design/agents/antigravity.yaml`
- `skills/novel-writing/agents/antigravity.yaml`
- `skills/series-qa/agents/antigravity.yaml`

이 파일들은 루트 워크스페이스에서 사용하는 Antigravity용 운영 파일을 플랫폼 패키지로 따로 모아둔 것입니다.
Antigravity는 `<user_rules>`(AGENTS.md)를 통해 지침을 숙지하고, 스킬 시스템을 통해 특정 작업을 분리 수행할 수 있습니다.

## 적용 방식

권장 흐름:

1. 이 폴더의 `AGENTS.md`를 워크스페이스 루트의 `AGENTS.md`로 복사하거나 교체한다. (Antigravity는 이 파일을 자동으로 `user_rules`로 로드합니다)
2. 이 폴더의 `skills/*/agents/antigravity.yaml` 파일들을 대상 워크스페이스의 같은 경로에 복사하거나 교체한다.
3. `skills/` 본문과 `references/`가 대상 워크스페이스에 함께 존재하는지 확인한다.
4. 지정된 저장 폴더(`drafts/초고` 등) 생성이 원활한지 확인한다.
