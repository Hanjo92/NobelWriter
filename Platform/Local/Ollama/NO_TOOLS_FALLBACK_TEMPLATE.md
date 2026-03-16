# Ollama No-Tools Fallback Template

Use this when an Ollama-based local host says tools, file writes, or external helpers are unavailable.

## Standard Template

```text
현재 이 로컬 실행 환경에서는 파일 저장이나 보조 도구 호출을 사용할 수 없지만, 이 워크스페이스의 한국어 소설 집필 지침은 직접 적용할 수 있습니다.

가정: [장르], [시점], [톤], [반환 단계] 기준으로 진행합니다.

파일 저장은 이번 실행에서 생략하고, 아래에 요청하신 원고를 바로 제공합니다.
```

## Short Template

```text
도구 저장 기능은 현재 사용할 수 없지만, 지침을 따라 본문은 직접 작성할 수 있습니다.

가정: [최소 가정].

아래에 원고를 바로 제공합니다.
```

## Required Behavior

- 도구 제한을 짧게만 언급한다
- 최소 가정을 세운다
- 실제 산문 요청이면 `초고 -> 개고 -> 원고`를 메모리에서 수행한다
- 기본적으로 `원고`를 반환한다
- 파일 저장 불가를 이유로 작업을 거절하지 않는다
