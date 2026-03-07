# NobelWriter

한국어 소설 작업을 위한 로컬 Codex 스킬 워크스페이스입니다.  
이 저장소는 장편 설계, 대사 설계, 원고 작성, 연재 QA를 분리해서 다루도록 구성되어 있습니다.

## 구성

이 저장소의 핵심은 `skills/` 아래의 4개 스킬입니다.

- `character-voice-bible`
  - 대사 중심 스킬
  - 캐릭터별 말투 분리, 화자 차별화, 관계별 존대/반말, 대사 드리프트 점검에 사용
- `novel-writing`
  - 서술 중심 스킬
  - 나레이션, 장면 본문, 챕터 초고/개고/원고, 문장 흐름, 설명 문장 정리에 사용
- `longform-story-design`
  - 설계 중심 스킬
  - 장편/시리즈 구조, 장르 패키지 선택, 볼륨/아크 설계, 연속성 문서화에 사용
- `series-qa`
  - 진단 중심 스킬
  - 연재 원고나 장편 원고의 연속성, 페이싱, payoff, 캐릭터 드리프트 문제 점검에 사용

## 작업 원칙

이 워크스페이스는 `AGENTS.md`를 기준으로 동작합니다.

- 한국어 소설 작업은 일반적인 답변 대신 로컬 스킬을 우선 사용합니다.
- 실제 산문 생성 시 `초고`, `개고`, `원고` 3단계 파일 저장 정책을 따릅니다.
- 대사 중심 문제는 `character-voice-bible`, 서술 중심 문제는 `novel-writing`으로 분리합니다.
- 장편 구조 설계는 `longform-story-design`, 문제 진단은 `series-qa`로 분리합니다.

## 디렉터리 구조

```text
NobelWriter/
├─ AGENTS.md
├─ Platform/
├─ README.md
├─ drafts/
│  ├─ 초고/
│  ├─ 개고/
│  └─ 원고/
└─ skills/
   ├─ character-voice-bible/
   ├─ longform-story-design/
   ├─ novel-writing/
   └─ series-qa/
```

## Platform 구조

이 저장소는 플랫폼별 운영 파일을 [Platform](/C:/Nobels/NobelWriter/Platform) 아래에 분리해서 관리할 수 있도록 확장 중입니다.

- [Platform/README.md](/C:/Nobels/NobelWriter/Platform/README.md)
  - 플랫폼 팩 전체 구조 설명
- [Platform/OpenAI/README.md](/C:/Nobels/NobelWriter/Platform/OpenAI/README.md)
  - OpenAI 계열 환경 선택 가이드
- [Platform/OpenAI/Codex/README.md](/C:/Nobels/NobelWriter/Platform/OpenAI/Codex/README.md)
  - Codex 적용용 메모
- [Platform/OpenAI/GPT-OSS/README.md](/C:/Nobels/NobelWriter/Platform/OpenAI/GPT-OSS/README.md)
  - GPT-OSS 적용용 메모

공용 스킬 자산은 가능한 유지하고, 플랫폼별로 달라지는 운영 파일만 `Platform/` 아래에서 분리 관리하는 방식입니다.

## 사용 예시

다음처럼 작업을 나눠 쓰는 것을 기준으로 설계되어 있습니다.

- 캐릭터 둘의 말투가 비슷해서 대사를 분리하고 싶다
  - `character-voice-bible`
- 장면 서술이 번역투 같고 나레이션이 무겁다
  - `novel-writing`
- 웹소설 초반 30화를 장편 구조로 다시 정리하고 싶다
  - `longform-story-design`
- 40화 이후 전개가 늘어지고 복선 회수가 약한지 진단하고 싶다
  - `series-qa`

## 다른 컴퓨터에서 사용하기

가장 쉬운 방법은 이 저장소를 그대로 클론해서 같은 워크스페이스로 여는 것입니다.

1. 저장소를 다른 컴퓨터에 클론합니다.
2. Codex에서 이 폴더를 워크스페이스로 엽니다.
3. 필요하면 `drafts/` 디렉터리까지 함께 유지합니다.

주의:

- 현재 설정은 저장소 루트 기준 상대경로를 사용합니다.
- 다른 컴퓨터에서도 저장소 구조만 유지하면 같은 방식으로 사용할 수 있습니다.
- 다른 레포로 옮길 때도 `AGENTS.md`, `skills/`, `drafts/` 구조를 함께 유지하는 것이 가장 안전합니다.

## 포함 파일

실제로 옮길 때는 아래 항목이 필요합니다.

- `AGENTS.md`
- `skills/` 전체
- `drafts/` 디렉터리

## 목적

이 저장소는 한국어 소설 작업을 다음 4층으로 분리하기 위해 만들어졌습니다.

1. 대사
2. 서술
3. 구조
4. 진단

한 스킬이 모든 문제를 처리하는 대신, 역할이 다른 스킬들이 서로 handoff 하도록 설계되어 있습니다.
