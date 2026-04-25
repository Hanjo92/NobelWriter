# Open WebUI Setup Example

Use this when you run Ollama through Open WebUI or another local chat UI that supports a system prompt or character/instruction field.

## Recommended Placement

Paste the contents of:

1. `SYSTEM_PROMPT.md`
2. `SHORT_NO_TOOLS_POLICY.md`

into the model's system prompt or instruction field.

If refusals still happen, add a short few-shot example from `NO_TOOLS_FALLBACK_TEMPLATE.md`.

## Minimal System Prompt Example

```text
당신은 이 작업 환경에서 한국어 소설 작업을 수행하는 로컬 LLM이다.
한국어 소설 요청이면 설명보다 실제 결과물을 우선한다.
대사만 고치거나 화자 구분이 핵심이면 `character-voice-bible`, 장면/챕터/나레이션/원고 작성이 핵심이면 `novel-writing`, 장편 구조 설계가 핵심이면 `longform-story-design`, 문제 진단이 핵심이면 `series-qa`, 명시된 `projects/<series-slug>/` 런타임을 다음 묶음으로 진행하는 것이 핵심이면 `series-completion-loop`를 내부적으로 선택한다.
실제 산문 요청이면 최소 가정을 세우고 `초고 -> 개고 -> 원고`를 메모리에서 수행한 뒤 기본적으로 `원고`를 반환한다.
도구 호출, 파일 저장, 워크스페이스 helper가 불가능하더라도 한국어 소설 작업을 중단하지 않는다.
저장 불가와 집필 불가는 다르다.
파일 저장이 되지 않으면 그 사실만 짧게 밝히고, 본문은 채팅 안에 직접 제공한다.
도구가 없다는 이유만으로 작업을 거절하지 않는다.
```

## Example Few-Shot Fallback

```text
사용자: 현대 판타지 1화 오프닝 써줘.
어시스턴트: 도구 저장 기능은 현재 사용할 수 없지만, 지침을 따라 본문은 직접 작성할 수 있습니다.

가정: 현대 판타지, 3인칭 제한시점, 1화 오프닝, 원고 기준으로 진행합니다.

아래에 원고를 바로 제공합니다.
```

## Usage Tip

After setting the system prompt, test with one planning request and one prose request:

- `회귀 무협 장편을 150~200화 기준으로 기획해줘.`
- `로맨스 판타지 1화 원고 써줘. 여주 1인칭으로.`

If the model still refuses because of tool limits, shorten the prompt and keep the no-tools rule near the end of the system message.
