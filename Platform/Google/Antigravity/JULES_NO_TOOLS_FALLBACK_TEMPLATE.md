# Jules No-Tools Fallback Template

Use this template when Google Jules or a similar external agent says it cannot use external APIs, tools, file writers, or workspace helper functions.

Goal:
- do not stop at tool unavailability
- do not answer with a pure refusal
- continue by reading the local writing instructions already provided in the workspace
- write the Korean fiction text directly in the reply

This template is for Korean fiction requests that should still be completed even when file-writing or external tool access is blocked.

## Core Rule

If the user asked for Korean fiction writing, do not say the task cannot be done just because external tools are unavailable.

Instead:

1. briefly acknowledge the tool limitation
2. state that you can still follow the local writing instructions directly
3. make the smallest useful assumptions
4. write the requested Korean fiction output in-chat
5. if file saving is unavailable, say that stage files could not be saved in this run

## Short Standard Template

```text
외부 도구 또는 파일 저장 기능은 현재 사용할 수 없지만, 이 워크스페이스의 집필 지침을 직접 따라 원고는 계속 작성할 수 있습니다.

가정: [장르/시점/분량/톤에 대한 최소 가정].

아래에 요청하신 [장면 / 오프닝 / 챕터 / 원고]를 바로 작성합니다.
```

Then immediately continue with the actual Korean fiction text.

## Slightly Longer Standard Template

```text
현재 이 실행 환경에서는 외부 API, 파일 저장 도구, 보조 워크스페이스 도구를 사용할 수 없습니다. 다만 이 워크스페이스에 포함된 집필 지침과 스킬 규칙은 그대로 따를 수 있으므로, 요청하신 한국어 소설 원고는 이 대화 안에서 직접 작성하겠습니다.

가정: [장르], [시점], [톤], [반환 단계] 기준으로 진행합니다.

파일 저장은 이번 실행에서 생략되지만, 본문은 아래에 바로 제공합니다.
```

Then immediately continue with the actual Korean fiction text.

## What To Avoid

Do not answer like this:

```text
외부 API를 사용할 수 없어서 작업을 진행할 수 없습니다.
```

```text
파일 저장 도구가 없으므로 스킬을 사용할 수 없습니다.
```

```text
이 환경에서는 지원되지 않아 챕터를 작성할 수 없습니다.
```

These responses are wrong for prose-generation requests because the model can still read instructions and produce text directly.

## Default Fallback Behavior For Fiction Requests

When tools are unavailable:

- keep the lane routing in memory
- keep the `초고 -> 개고 -> 원고` refinement logic in memory
- return the final `원고` text by default
- mention the missing file save only briefly
- do not over-explain the limitation

Recommended phrasing:

```text
파일 저장은 이번 실행에서 할 수 없어 본문만 직접 제공합니다.
```

## Copy-Paste Templates By Request Type

### 1. Chapter Draft Request

```text
외부 도구와 파일 저장 기능은 현재 사용할 수 없지만, 이 워크스페이스의 한국어 소설 집필 지침을 따라 챕터 원고 자체는 바로 작성할 수 있습니다.

가정: [장르], [시점], [분량], [톤] 기준의 원고로 진행합니다.

아래에 원고를 바로 제공합니다.
```

### 2. Opening Request

```text
현재 도구 호출과 파일 저장은 불가능하지만, 지침을 직접 적용해 오프닝 원고는 바로 작성할 수 있습니다.

가정: [장르], [시점], [1화 도입부] 기준으로 진행합니다.

아래는 원고 버전입니다.
```

### 3. Revision Request

```text
현재 실행 환경에서는 외부 도구와 파일 저장을 사용할 수 없지만, 제공된 텍스트를 바탕으로 개고/원고 수준의 문장 수정은 직접 수행할 수 있습니다.

가정: 핵심 사건과 의미는 유지하고, 원고 기준으로 정리합니다.

아래에 수정본을 제공합니다.
```

### 4. Planning Request

```text
외부 도구는 사용할 수 없지만, 기획안 작성 자체는 지침에 따라 바로 진행할 수 있습니다.

가정: [장르], [대상 독자], [150~200화 규모] 기준으로 기획합니다.

아래에 기획안을 정리합니다.
```

## Recommended One-Line Policy For Jules

If a host environment tends to over-prioritize tool restrictions, prepend this policy to the response behavior:

```text
도구 사용 불가와 집필 수행 불가는 같은 의미가 아니다. 저장과 호출이 막혀도, 지침 해석과 본문 작성은 계속 진행한다.
```

## Final Reminder

For Korean fiction tasks, tool unavailability should downgrade file output, not block manuscript writing itself.
