# GPT-OSS / Local LLM No-Tools Fallback Template

Use this template when a local LLM host or GPT-OSS-style runtime cannot use file writers, tool calls, workspace helpers, or explicit skill metadata.

Goal:
- prevent false refusals
- separate tool limits from writing ability
- keep Korean fiction drafting executable in-chat

## Core Policy

Tool unavailability is not the same as manuscript unavailability.
If the model can read the workspace instructions, it can still route the task, apply the writing rules, and produce Korean fiction directly in the reply.

## Standard Fallback Response

```text
현재 이 실행 환경에서는 파일 저장이나 보조 도구 호출을 사용할 수 없지만, 이 워크스페이스의 한국어 소설 작성 지침은 직접 적용할 수 있습니다.

가정: [장르], [시점], [톤], [반환 단계] 기준으로 진행합니다.

파일 저장은 이번 실행에서 생략하고, 아래에 요청하신 원고를 바로 제공합니다.
```

Then immediately continue with the requested Korean output.

## Short Version

```text
도구 저장 기능은 현재 사용할 수 없지만, 지침을 따라 본문은 직접 작성할 수 있습니다.

가정: [최소 가정].

아래에 원고를 바로 제공합니다.
```

## For Planning Requests

```text
현재 도구 호출은 불가능하지만, 기획안 작성 자체는 지침에 따라 바로 진행할 수 있습니다.

가정: [장르], [대상 독자], [150~200화 규모] 기준으로 정리합니다.

아래에 기획안을 제공합니다.
```

## For Revision Requests

```text
현재 파일 저장 도구는 사용할 수 없지만, 제공된 원고를 바탕으로 개고/원고 수준의 수정은 직접 수행할 수 있습니다.

가정: 핵심 사건과 의미는 유지하고, 원고 기준으로 정리합니다.

아래에 수정본을 제공합니다.
```

## What To Avoid

Do not answer like this:

```text
이 환경에서는 외부 도구를 쓸 수 없어서 작업이 불가능합니다.
```

```text
스킬을 호출할 수 없으므로 원고 작성이 어렵습니다.
```

```text
파일 저장 기능이 없어서 이 요청을 처리할 수 없습니다.
```

These are incorrect for Korean fiction requests if direct text generation is still possible.

## Required Behavior

When tools are unavailable:

1. route internally
2. make the smallest useful assumptions
3. keep `초고 -> 개고 -> 원고` as an internal refinement loop
4. return `원고` by default
5. mention missing file save only briefly

Recommended one-line policy:

```text
저장 불가나 도구 불가는 출력 불가를 뜻하지 않는다. 본문 작성은 계속 진행한다.
```
