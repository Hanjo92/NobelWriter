# Korean Fiction GPT-OSS Router

이 문서는 사용자 요청을 어떤 작업층으로 보낼지 결정하는 GPT-OSS용 라우팅 규칙이다.

## 1차 분류

먼저 요청의 1차 목적을 하나 고른다.

- 대사 설계
- 서술/원고 작성
- 장편 구조 설계
- 문제 진단/QA
- 완주 오케스트레이션

한 요청에 여러 목적이 섞여 보여도 가장 먼저 막히는 병목 하나를 우선 선택한다.

## 라우팅 규칙

### 0. `series-completion-loop`

아래 중 하나라도 핵심이면 이 층을 우선한다.

- 명시된 `projects/<series-slug>/` 런타임을 다음 묶음으로 진행하고 싶다
- `state/runtime.yaml`, `state/active-slice.yaml`, `state/handoff.md`를 기준으로 이어 달라고 한다
- approval-gated 또는 autonomous 완주 모드를 유지해야 한다
- 3~5화 단위의 다음 전이, QA 복구, 승인 대기, 세션 간 재진입이 핵심이다
- specialist handoff 결과를 검증하고 런타임 증거를 갱신해야 한다

기본 출력:

- selected runtime
- starting state and batch
- attempted transition
- specialist handoff target
- accepted evidence or blocked reason
- updated state and next action

기본 참조 시작점:

- `skills/series-completion-loop/SKILL.md`

주의:

- 명시된 런타임이 없으면 이 층으로 진행하지 않는다.
- 직접 원고를 쓰거나 장편 설계를 대신하지 않는다.
- 필요한 경우 `longform-story-design`, `novel-writing`, `series-qa`, `character-voice-bible`로 넘긴다.

### 1. `character-voice-bible`

아래 중 하나라도 핵심이면 이 층을 우선한다.

- 대사만 고치고 싶다
- 캐릭터 말투가 비슷하다
- 화자가 구분되지 않는다
- 관계 변화에 따라 존댓말/반말을 조정하고 싶다
- 특정 인물의 말투가 무너졌다
- 대본처럼 대사만 주고받는 형식이 필요하다
- spoken exchange의 압력, 회피, 반응, 감정 누출이 핵심 문제다

기본 출력:

- 대사 시트
- 화자 카드
- 관계별 register 규칙
- proof rewrite
- speaker-labeled exchange

기본 참조 시작점:

- `skills/character-voice-bible/SKILL.md`
- 필요 시 `references/request-router.md`
- 필요 시 `references/composition-guide.md`
- 필요 시 `references/script-dialogue-rules.md`

### 2. `novel-writing`

아래 중 하나라도 핵심이면 이 층을 우선한다.

- 장면이나 챕터를 실제 산문으로 써 달라
- 나레이션이 무겁거나 번역투다
- 문장 흐름, 문단 리듬, 이미지 착지가 어색하다
- 초고/개고/원고를 만들고 싶다
- 기존 원고를 같은 목소리로 이어 쓰고 싶다
- 설명 문장, 장면 본문, 서술 시점이 핵심 문제다

기본 출력:

- 시놉시스
- 장면 계획
- 초고
- 개고
- 원고
- 산문 수정본

기본 참조 시작점:

- `skills/novel-writing/SKILL.md`
- 필요 시 `references/task-router.md`
- 필요 시 `references/korean-prose.md`
- 필요 시 `references/draft-pipeline.md`
- 필요 시 `references/manuscript-quality-gate.md`

### 3. `longform-story-design`

아래 중 하나라도 핵심이면 이 층을 우선한다.

- 장편 구조를 잡고 싶다
- 시리즈, 볼륨, 아크를 설계하고 싶다
- 장르 패키지 선택이 모호하다
- 연재가 길어지며 구조가 흔들린다
- 설정집, 연속성 문서, payoff tracker가 필요하다
- drafting 전에 story engine을 먼저 세워야 한다

기본 출력:

- project frame
- story engine sheet
- story bible
- cast matrix
- arc/volume plan
- continuity ledger

기본 참조 시작점:

- `skills/longform-story-design/SKILL.md`
- 필요 시 `references/project-intake.md`
- 필요 시 `references/story-engine.md`
- 필요 시 `references/planning-stack-selection.md`

### 4. `series-qa`

아래 중 하나라도 핵심이면 이 층을 우선한다.

- 어디가 문제인지 먼저 진단하고 싶다
- 전개가 늘어진다
- 복선 회수가 약하다
- 캐릭터 드리프트가 있다
- 세계관 규칙이나 연속성이 흔들린다
- POV나 톤이 무너진다
- 진단 우선순위와 다음 handoff target을 정하고 싶다

기본 출력:

- ranked issue list
- root cause analysis
- QA report
- repair direction
- handoff target
- re-audit gate

기본 참조 시작점:

- `skills/series-qa/SKILL.md`
- 필요 시 `references/diagnostic-workflow.md`
- 필요 시 `references/failure-patterns.md`
- 필요 시 `references/report-templates.md`

## 복합 요청 우선순위

### 장편 설계 + 초안 작성

1. `longform-story-design`
2. 필요 시 `character-voice-bible`
3. `novel-writing`

### 런타임 완주 진행 + 전문 작업

1. `series-completion-loop`
2. 현재 상태에 따라 `longform-story-design`, `novel-writing`, `series-qa`, `character-voice-bible`
3. 다시 `series-completion-loop`에서 반환 증거를 검증하고 상태를 갱신

### QA + 실제 수정

1. `series-qa`
2. 대사 문제가 핵심이면 `character-voice-bible`
3. 서술 문제가 핵심이면 `novel-writing`

### 대사 개선 + 장면 산문화

1. `character-voice-bible`
2. `novel-writing`

### 챕터 작성 + 장기 구조 불안

1. 구조 불안이 먼저면 `longform-story-design`
2. 바로 써야 하는 산문이 더 급하면 `novel-writing`
3. 다만 대사 병목이 눈에 띄면 중간에 `character-voice-bible`을 끼운다

## 최소 참조 원칙

- 항상 `SKILL.md`부터 읽는다.
- 그 다음에는 요청 해결에 필요한 가장 좁은 레퍼런스만 읽는다.
- 예시가 필요할 때만 sample 문서를 읽는다.
- 라우팅이 분명하면 다른 스킬 레퍼런스를 불필요하게 읽지 않는다.

## 반환 원칙

- 사용자가 결과물을 원하면 실제 결과물을 반환한다.
- 사용자가 진단을 원하면 진단과 우선순위를 먼저 반환한다.
- 사용자가 여러 단계를 한 번에 요구해도, 현재 병목을 먼저 해결하는 순서로 응답을 조직한다.

## 예외 처리

- 대사와 서술이 함께 있지만 핵심 병목이 대사 자체면 `character-voice-bible`을 먼저 쓴다.
- 대사가 많아도 목적이 완성 산문이라면 최종 결과는 `novel-writing` 형식으로 정리한다.
- 사용자가 명시적으로 특정 층을 요청하면 특별한 충돌이 없는 한 그 요청을 우선 존중한다.
