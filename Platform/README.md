# Platform Packs

이 폴더는 이 스킬 세트를 여러 AI 서비스와 런타임 환경에 맞게 적용하기 위한 플랫폼별 운영 파일 모음입니다.

## 목적

- 공용 스킬 자산과 플랫폼별 운영 레이어를 분리
- 사용자가 현재 쓰는 AI 서비스에 맞는 파일만 선택해서 적용
- 같은 소설 작업 체계를 여러 환경에서 재사용 가능하게 유지

## 기본 개념

이 스킬 세트는 크게 두 층으로 나뉩니다.

1. 공용 자산
   - `skills/`
   - `skills/*/references/`
   - 소설 작업 규칙과 예시
2. 플랫폼별 운영 레이어
   - 시스템 프롬프트
   - 라우터
   - 메타데이터
   - 적용 가이드

이 `Platform/` 폴더는 두 번째 층을 정리하는 자리입니다.

## 현재 구조

- [OpenAI](./OpenAI)
  - OpenAI 계열 런타임용 파일
  - 하위에 `Codex`, `GPT-OSS` 같은 환경별 폴더를 둠
- [Google](./Google)
  - Google 계열 런타임용 파일
  - 하위에 `Antigravity` 환경별 폴더를 둠
- [Anthropic](./Anthropic)
  - Anthropic Claude Code 런타임용 파일
  - 하위에 `Claude` 환경별 폴더를 둠 (`CLAUDE.md` + 슬래시 커맨드 기반)
- [Local](./Local)
  - Ollama 같은 로컬 LLM 호스트용 파일
  - 하위에 호스트별 시스템 프롬프트와 no-tools fallback 문서를 둠

## 사용 방식

1. 현재 사용할 AI 서비스 또는 런타임을 결정합니다.
2. 해당 플랫폼 폴더의 README를 읽습니다.
3. 필요한 운영 파일만 워크스페이스 또는 대상 환경으로 반영합니다.
4. 공용 자산인 `skills/`, `skills/*/references/`, `drafts/` 구조는 가능한 유지합니다.

전용 CLI가 있는지, 자연어 요청으로 어떻게 챕터를 쓰는지 같은 공통 질문은 [USAGE_FAQ.md](../USAGE_FAQ.md)를 먼저 보면 빠릅니다.

## 확장 방식

새 플랫폼을 추가할 때는 아래처럼 폴더를 늘립니다.

```text
Platform/
├─ README.md
├─ OpenAI/
│  ├─ README.md
│  ├─ Codex/          ← AGENTS.md + openai.yaml
│  └─ GPT-OSS/
├─ Google/
│  ├─ README.md
│  └─ Antigravity/    ← AGENTS.md + antigravity.yaml
├─ Anthropic/
│  ├─ README.md
│  └─ Claude/         ← CLAUDE.md + .claude/commands/ 슬래시 커맨드
└─ Local/
   ├─ README.md
   └─ Ollama/         ← SYSTEM_PROMPT + no-tools fallback docs
```

## 운영 원칙

- 플랫폼마다 달라지는 부분만 여기서 관리합니다.
- 스킬의 핵심 내용은 가능한 공용으로 유지합니다.
- 대사, 서술, 구조, 진단, 완주 오케스트레이션의 역할 분리는 모든 플랫폼에서 유지합니다.

## 메모

이 폴더는 배포용 운영 계층을 정리하기 위한 인덱스입니다.  
실제 적용 파일은 각 플랫폼 하위 폴더에서 관리합니다.
