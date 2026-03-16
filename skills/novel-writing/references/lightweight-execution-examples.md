# Lightweight Execution Examples

Use this file when the model understands the rules in principle but still hesitates about how to start.

The goal is not to copy the wording below verbatim. The goal is to follow the same execution pattern:

1. identify the lane
2. state a narrow assumption set
3. produce the requested artifact immediately
4. if prose is requested, run `초고 -> 개고 -> 원고`

## Example 1. Fresh Drafting

User request:

```text
현대 판타지 첫 화 오프닝 써줘. 남주가 퇴사 당한 날 각성하는 장면이야.
```

Correct first move:

```text
가정: 현대 판타지 웹소설 톤, 3인칭 제한시점, 1화 오프닝, 원고 기준으로 진행한다.
```

Then do:

- route to `fresh drafting`
- load `draft-pipeline.md`
- load `manuscript-quality-gate.md`
- load `chapter-opening-selection.md` if needed
- write prose, not process explanation

Do not do:

- ask broad questions like "어떤 스타일로 쓸까요?"
- answer that the skill usage is unclear
- return an outline when the user asked for prose

## Example 2. Planning

User request:

```text
회귀 무협 장편 기획안 잡아줘.
```

Correct first move:

```text
가정: 150~200화 규모의 회귀 무협 웹소설을 기준으로 핵심 기획안을 구성한다.
```

Then do:

- route to `planning`
- load `templates.md`
- return a compact planning artifact
- do not force manuscript prose unless requested

## Example 3. Continuation

User request:

```text
아래 원고 다음 장면 이어 써줘.
```

Correct first move:

```text
가정: 제공된 원고의 시점, 문체, 문단 밀도를 유지한 채 다음 장면을 원고 기준으로 잇는다.
```

Then do:

- route to `continuation`
- sample the existing prose first
- load `draft-pipeline.md`
- load `manuscript-quality-gate.md`
- continue in the same voice before introducing new texture

## Example 4. Stage Revision

User request:

```text
이 초고를 개고해서 원고 수준으로 정리해줘.
```

Correct first move:

```text
가정: 핵심 사건과 의미는 유지하고, 초고를 개고와 원고 단계까지 정리한다.
```

Then do:

- route to `stage revision`
- load `draft-pipeline.md`
- load `manuscript-quality-gate.md`
- load `workflow.md` if pass selection is needed
- preserve meaning unless the user asked for deeper change

## Example 5. Critique-Only

User request:

```text
이 장면 뭐가 어색한지 피드백만 해줘.
```

Correct first move:

```text
가정: 진단만 수행하고, 재작성은 요청될 때만 제안한다.
```

Then do:

- route to `critique-only`
- diagnose concrete issues first
- do not rewrite the scene unless the user asked for it

## Failure Pattern To Avoid

Bad response pattern:

```text
이 스킬을 어떻게 적용해야 하는지 정보가 부족합니다.
```

Replace it with:

```text
가정: [smallest useful assumption].
```

Then proceed with the appropriate lane immediately.
