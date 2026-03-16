# Local / Ollama

이 폴더는 Ollama 같은 로컬 LLM 호스트에서 NobelWriter를 사용할 때 붙여 넣을 수 있는 운영 문서를 모아둔 자리입니다.

## 목적

- Ollama 환경에서 한국어 소설 작업을 멈추지 않게 하기
- 도구 없음, 파일 저장 없음, 스킬 메타데이터 없음 같은 조건에서도 fallback 집필이 가능하게 하기
- 시스템 프롬프트와 보조 템플릿을 짧게 재사용할 수 있게 하기

## 포함된 파일

- `SYSTEM_PROMPT.md`
- `NO_TOOLS_FALLBACK_TEMPLATE.md`
- `SHORT_NO_TOOLS_POLICY.md`
- `MODELFILE_EXAMPLE.md`
- `OPEN_WEBUI_SETUP.md`
- `MODEL_PRESETS.md`

## Ollama에서 왜 별도 처리가 필요한가요?

Ollama 기반 호스트는 실행 앱마다 기능 차이가 큽니다.

- 어떤 호스트는 파일 쓰기를 지원하지 않음
- 어떤 호스트는 워크스페이스 도구가 없음
- 어떤 호스트는 `agents/openai.yaml` 같은 메타데이터를 읽지 않음
- 어떤 호스트는 시스템 프롬프트만 주입 가능하고, 스킬 라우터는 별도로 없음

그래서 이 환경에서는 "도구가 없어서 작업 불가"라는 잘못된 거절을 막는 문구를 따로 넣어두는 것이 안전합니다.

## 권장 적용 순서

1. `SYSTEM_PROMPT.md`를 로컬 호스트의 시스템 프롬프트 또는 상위 지침에 넣는다.
2. 거절 응답이 반복되면 `SHORT_NO_TOOLS_POLICY.md`를 같은 레이어에 추가한다.
3. 실제 응답이 흔들릴 때는 `NO_TOOLS_FALLBACK_TEMPLATE.md`를 few-shot 예시처럼 함께 넣는다.
4. 루트 `skills/`와 `skills/*/references/`는 가능한 함께 제공한다.

복붙 가능한 예시는 아래 문서를 참고한다.

- Ollama `Modelfile`: [MODELFILE_EXAMPLE.md](./MODELFILE_EXAMPLE.md)
- Open WebUI 시스템 프롬프트: [OPEN_WEBUI_SETUP.md](./OPEN_WEBUI_SETUP.md)
- 모델별 짧은 프롬프트: [MODEL_PRESETS.md](./MODEL_PRESETS.md)

## 핵심 원칙

- 저장 불가와 집필 불가는 다르다.
- 스킬 메타데이터가 없어도 요청 의미를 보고 내부적으로 작업층을 선택한다.
- 실제 산문 요청이면 `초고 -> 개고 -> 원고`를 메모리에서 수행하고 기본적으로 `원고`를 반환한다.
- 파일 저장이 안 되면 그 사실만 짧게 알리고, 본문은 직접 제공한다.
