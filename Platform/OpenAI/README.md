# OpenAI Platform Pack

이 폴더는 OpenAI 계열 환경에서 NobelWriter를 사용할 때 필요한 플랫폼별 운영 파일을 분리해서 관리하는 공간입니다.

## 목적

- 같은 스킬 자산을 여러 OpenAI 환경에 맞게 재사용
- 공용 콘텐츠와 플랫폼별 운영 파일을 분리
- 사용자가 현재 쓰는 환경에 맞는 폴더만 골라 적용

## 하위 구조

- [Codex](./Codex)
  - Codex 환경용 운영 파일
- [GPT-OSS](./GPT-OSS)
  - GPT-OSS 환경용 운영 파일

## 사용 방식

1. 현재 사용하는 환경이 Codex인지 GPT-OSS인지 먼저 결정합니다.
2. 해당 폴더의 README를 읽고 필요한 파일을 확인합니다.
3. 플랫폼 전용 운영 파일을 워크스페이스 루트 또는 대상 환경에 맞게 복사하거나 반영합니다.
4. 공용 자산인 `skills/`, `skills/*/references/`, `drafts/` 구조는 가능한 유지합니다.

## 공용 원칙

- 스킬의 핵심 콘텐츠는 가능한 공용으로 유지합니다.
- 플랫폼에 따라 달라지는 것은 운영 규칙, 시스템 프롬프트, 라우터, 메타데이터 계층입니다.
- 대사, 서술, 구조, 진단이라는 역할 분리는 플랫폼이 바뀌어도 유지합니다.

## 권장 흐름

- Codex를 쓸 때
  - `Platform/OpenAI/Codex/README.md`부터 확인
- GPT-OSS를 쓸 때
  - `Platform/OpenAI/GPT-OSS/README.md`부터 확인

## 메모

앞으로 OpenAI 계열의 다른 환경이 추가되면 같은 방식으로 하위 폴더를 늘립니다.

예:

- `Platform/OpenAI/SomeFutureRuntime/`
