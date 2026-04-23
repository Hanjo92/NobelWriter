# NobelWriter Usage FAQ

## NobelWriter는 전용 CLI 도구인가요?

아니요.
NobelWriter는 기본적으로 독립 실행형 CLI 앱이 아니라, 에이전트가 읽는 `skills/`, `AGENTS.md`, `CLAUDE.md`, `agents/openai.yaml` 같은 운영 파일과 집필 규칙 세트입니다.

즉, 이 저장소 안에 기본적으로 아래 같은 명령이 들어 있는 것은 아닙니다.

```text
nobelwriter write-chapter
nobelwriter draft
nobelwriter run novel-writing
```

그 대신 호환되는 에이전트 런타임이 이 워크스페이스를 열고 운영 파일을 읽은 뒤, 사용자의 자연어 요청을 적절한 스킬로 라우팅하는 구조입니다.

## 그럼 사용자는 어떻게 챕터를 쓰나요?

보통은 다음 순서로 사용합니다.

1. NobelWriter 저장소를 호환되는 에이전트 환경에서 연다.
2. 해당 플랫폼용 운영 파일이 적용되어 있는지 확인한다.
3. 채팅 입력창에 자연어로 집필 요청을 보낸다.

예시:

```text
현대 판타지 웹소설 1화 원고 써줘. 주인공은 구조조정 당일 각성하고, 3인칭 제한시점으로.
```

```text
아래 초고를 개고해서 원고 수준으로 정리해줘.
```

```text
회귀 무협 장편을 150~200화 기준으로 기획해줘.
```

## 작품 하나를 끝날 때까지 계속 돌릴 수 있나요?

가능합니다. 단, 한 번의 무한 생성 런이 아니라 `series-completion-loop`가
`3~5화` 배치 단위로 상태를 읽고 다음 액션만 수행하는 방식입니다.

- `autonomous`
- `approval-gated`
- runtime state in `projects/<series-slug>/`
- manuscript output remains in `drafts/`

## 스킬 이름을 직접 호출해야 하나요?

환경에 따라 다를 수 있지만, NobelWriter의 기본 설계는 암시적 호출을 허용하는 쪽입니다.
즉, 한국어 소설 집필 요청이면 에이전트가 `novel-writing` 같은 적절한 스킬을 우선 사용하도록 설계되어 있습니다.

일부 환경에서는 `$novel-writing` 같은 명시적 호출 문법을 쓸 수도 있지만, 그게 기본 전제는 아닙니다.

## `novel-writing` 스킬은 챕터 작성 시 실제로 어떻게 동작하나요?

연결된 에이전트는 보통 다음 흐름으로 작업합니다.

1. 요청을 `planning`, `fresh drafting`, `continuation`, `stage revision`, `critique-only` 같은 작업 유형으로 라우팅한다.
2. 필요한 최소 가정을 세운다.
3. 실제 원고 요청이면 `초고 -> 개고 -> 원고` 순서로 진행한다.
4. 기본적으로 `원고`를 사용자에게 반환한다.
5. 쓰기 가능한 환경이면 `drafts/초고`, `drafts/개고`, `drafts/원고`에 파일도 저장한다.

## API 스크립트를 직접 작성해야 하나요?

필수는 아닙니다.
기본 사용 방식은 API 스크립트를 직접 짜는 것이 아니라, Codex, Claude Code, Antigravity 같은 에이전트 환경에서 이 저장소를 열고 자연어로 요청하는 것입니다.

다만 아래가 필요하다면 별도 래퍼를 직접 추가해야 합니다.

- 전용 CLI 명령
- 배치 실행 자동화
- 외부 앱에서 NobelWriter를 호출하는 스크립트
- 커스텀 API 파이프라인

즉, NobelWriter는 기본적으로 “바로 실행되는 앱”보다는 “에이전트가 읽고 행동하는 작업 규칙 세트”에 가깝습니다.

## 로컬 LLM에서도 같은 문제가 생길 수 있나요?

그럴 수 있습니다. 오히려 더 자주 생길 수 있습니다.

이유:

- 로컬 호스트마다 파일 저장 지원 여부가 다름
- 워크스페이스 도구 호출을 아예 지원하지 않는 경우가 있음
- `agents/openai.yaml` 같은 메타데이터를 그대로 읽지 못할 수 있음
- `$skill-name` 같은 호출 문법이 호스트마다 다르거나 아예 없을 수 있음

그래서 로컬 LLM 환경에서는 "도구가 없으니 작업 불가"라고 오답을 내지 않도록 fallback 지침을 함께 넣는 것이 중요합니다.
원칙은 같습니다. 저장과 호출이 막혀도, 지침을 읽을 수 있으면 한국어 소설 본문은 직접 작성해야 합니다.

## 어떤 파일이 실제 호출에 관여하나요?

플랫폼마다 조금 다르지만, 보통 아래 파일들이 핵심입니다.

- `AGENTS.md`
- `CLAUDE.md`
- `skills/*/agents/openai.yaml`
- `skills/*/SKILL.md`
- `skills/*/references/*.md`

역할을 나누면:

- 운영 파일: 에이전트에게 어떤 스킬을 언제 어떻게 쓰라고 지시
- 스킬 본문: 해당 스킬의 작업 절차와 품질 기준 설명
- 참조 문서: 장르, 문체, 수정 방식 같은 세부 규칙 제공

## 플랫폼별로 어디서 시작하면 되나요?

- Codex: [Platform/OpenAI/Codex/README.md](./Platform/OpenAI/Codex/README.md)
- GPT-OSS: [Platform/OpenAI/GPT-OSS/README.md](./Platform/OpenAI/GPT-OSS/README.md)
- Claude Code: [Platform/Anthropic/Claude/README.md](./Platform/Anthropic/Claude/README.md)
- Antigravity: [Platform/Google/Antigravity/README.md](./Platform/Google/Antigravity/README.md)
- Ollama / Local LLM: [Platform/Local/Ollama/README.md](./Platform/Local/Ollama/README.md)

## 한 줄 요약

NobelWriter는 전용 챕터 작성 CLI가 아니라, 호환 에이전트가 읽고 사용하는 집필 운영 시스템입니다.
사용자는 보통 워크스페이스를 연 뒤 자연어로 “1화 원고 써줘”, “이 초고를 개고해줘”처럼 요청하면 됩니다.
