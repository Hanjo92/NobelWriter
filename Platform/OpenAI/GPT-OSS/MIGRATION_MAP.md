# Codex -> GPT-OSS Migration Map

## 목적

Codex 기준 운영 파일을 GPT-OSS 기준 운영 파일로 어떻게 분해하고 치환할지 정리한다.

## 핵심 차이

- Codex는 `AGENTS.md`와 `agents/openai.yaml` 같은 플랫폼 전용 운영 파일을 직접 사용한다.
- GPT-OSS는 같은 구조를 그대로 쓰기보다 시스템 프롬프트, 라우터, 작업층 문서로 나누어 쓰는 편이 자연스럽다.
- 따라서 Codex의 메타데이터 계층은 GPT-OSS에서 프롬프트 계층으로 이동한다.

## 파일 매핑

### 1. 루트 `AGENTS.md`

대상:

- `SYSTEM_PROMPT.md`
- `ROUTER.md`

이관 내용:

- 한국어 소설 작업 기본 원칙
- 대사층/서술층 역할 분리
- 최소 참조 원칙
- 초고/개고/원고 저장 규칙
- 품질 게이트

### 2. `skills/*/SKILL.md`

대상:

- `skills/*/SKILL.md`

작업:

- `Codex` 표현 제거
- `local skill` 표현 제거
- `$skill-name` 호출 문법 제거
- 플랫폼 종속 handoff 표현을 GPT-OSS용 작업 흐름 문구로 수정

### 3. `skills/*/agents/openai.yaml`

대상:

- 원칙적으로 GPT-OSS 패키지에서는 직접 사용하지 않음

처리 방식:

- 삭제하거나
- 별도 메타데이터 문서로 치환하거나
- 플랫폼 설명용 문서에만 정보 보존

## 우선 수정 대상

1. `SYSTEM_PROMPT.md`
2. `ROUTER.md`
3. 4개 `skills/*/SKILL.md`
4. `README.md`

## 공용 유지 대상

- 루트 `skills/*/references/*.md`
- `drafts/` 구조
- 대사 / 서술 / 구조 / 진단의 역할 분리

## 실제 이식 순서

1. `AGENTS.md`를 기반으로 `SYSTEM_PROMPT.md` 초안을 만든다.
2. `AGENTS.md`와 역할 분리 규칙을 기반으로 `ROUTER.md` 초안을 만든다.
3. 각 스킬의 `SKILL.md`에서 Codex 종속 표현만 걷어내며 GPT-OSS용으로 옮긴다.
4. `references/`는 가능한 수정 없이 공용으로 사용한다.
5. 파일 저장이 필요한 경우, 호스트 런타임이 파일 쓰기를 지원하는지 별도로 확인한다.

## 현재 상태

- `SYSTEM_PROMPT.md` 1차 초안 작성됨
- `ROUTER.md` 1차 초안 작성됨
- `skills/*/SKILL.md`는 아직 skeleton 단계
