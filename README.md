![NobelWriter Hero](hero.png)

# NobelWriter ✍️✨

**NobelWriter**는 전문 소설가와 웹소설 작가를 위한 프리미엄 AI 집필 워크스페이스입니다. 소설 창작의 복잡한 과정을 **대사(Dialogue)**, **서술(Narration)**, **설계(Structure)**, **진단(Diagnosis)**, **완주 오케스트레이션(Completion Orchestration)**의 5가지 계층으로 분리하여 체계적인 집필 환경을 제공합니다.

---

## 🚀 주요 특징 (Key Features)

- **5계층 모듈형 시스템**: 소설의 모든 요소와 장기 완주 루프를 전문적으로 처리하는 특화된 AI 스킬 제공.
- **체계적인 핸드오프**: 구조 설계부터 본문 집필까지 끊김 없는 작업 흐름.
- **3단계 집필 프로세스**: `초고` → `개고` → `원고`로 이어지는 엄격한 품질 관리.
- **플랫폼 독립성**: Antigravity, Codex, Claude 등 다양한 AI 환경에 최적화.
- **프로급 한국어 문체**: 번역투 제거 및 서사적 리듬감을 극대화한 한국어 문장 자동 교정.

---

## 🏗️ 5계층 아키텍처 (The 5-Tier Architecture)

NobelWriter는 `skills/` 디렉토리에 위치한 5개의 전문 스킬을 통해 창작 과정을 분담합니다.

| 스킬 (Skill) | 역할 (Role) | 주요 집중 분야 (Focus Areas) |
| :--- | :--- | :--- |
| **🗣️ Character Voice Bible** | **대사 (Dialogue)** | 캐릭터별 말투 차별화, 관계별 존대/반말, 대사 드리프트 방지. |
| **📖 Novel Writing** | **서술 (Narration)** | 장면 묘사, 나레이션 흐름, 문체 및 톤 컨트롤. |
| **🗺️ Longform Design** | **설계 (Structure)** | 시리즈 구조, 권차/아크 설계, 설정 및 개연성 관리. |
| **🔍 Series QA** | **진단 (Diagnosis)** | 전개 속도(Pacing), 복선 회수, 캐릭터 일관성 및 플롯 진단. |
| **🔁 Series Completion Loop** | **완주 오케스트레이션 (Completion)** | `projects/<series-slug>/` 런타임 기반 3~5화 배치 진행, 승인 대기, QA 복구, 상태 갱신. |

---

## 🔁 Series Completion Loop

NobelWriter는 개별 챕터 작성 외에도 저장소 전체를 대상으로 하는 `series-completion-loop` 오케스트레이션을 지원합니다.

- 한 번에 무한 생성하지 않고 `3~5화` 배치 단위로 다음 진행분만 처리합니다.
- `autonomous`와 `approval-gated` 모드를 지원합니다.
- 런타임 상태는 `projects/<series-slug>/`에 보관합니다.
- 자동화는 매번 다음에 필요한 bounded action만 수행하도록 설계됩니다.

---

## 🛠️ 워크스페이스 구조 (Workspace Structure)

작가가 오직 이야기에만 집중할 수 있도록 정리된 환경을 제공합니다.

- **`AGENTS.md`**: 핵심 운영 규칙 및 품질 표준 가이드.
- **`Platform/`**: 다양한 AI 서비스용 배포 팩 모음.
- **`skills/`**: 모든 전문 지식이 담긴 NobelWriter의 '두뇌'.
- **`drafts/`**: 단계별로 정리된 작가의 원고 저장소.

---

## 💻 지원 플랫폼 (Supported Platforms)

NobelWriter는 이동성과 적응성을 고려하여 설계되었습니다. 여러 AI 플랫폼에서 동일한 로직을 사용하세요.

- [x] **Google Antigravity** (Native Optimization)
- [x] **OpenAI Codex / GPT-4**
- [x] **Anthropic Claude Code**
- [x] **Local Models** (Platform Packs를 통한 커스텀 구현)

자세한 설정 방법은 [Platform/README.md](./Platform/README.md)를 참고하세요.

---

## 🎯 빠른 시작 (Quick Start)

1. 저장소를 **클론(Clone)** 합니다.
2. [Platform 가이드](./Platform/README.md)에 따라 환경을 **설정(Setup)** 합니다.
3. 이제 글을 쓰세요! `skills/`를 당신의 전문 집필 어시스턴트로 활용하세요.

자주 묻는 실제 사용법은 [USAGE_FAQ.md](./USAGE_FAQ.md)를 참고하세요.

---

## ❓ 어떻게 실제로 호출하나요? (How To Actually Use It)

NobelWriter는 기본적으로 **독립 실행형 CLI 앱이 아닙니다.**
이 저장소 안에 `nobelwriter write-chapter` 같은 전용 명령이 들어 있는 구조가 아니라, **호환되는 에이전트 런타임이 이 저장소의 운영 파일을 읽어서 스킬을 자동 호출하는 방식**입니다.

즉:

- `skills/`는 집필 지식과 작업 규칙입니다.
- `AGENTS.md`, `CLAUDE.md`, `agents/openai.yaml` 같은 파일은 에이전트가 그 지식을 어떻게 쓸지 알려주는 운영 레이어입니다.
- 사용자는 보통 별도 스크립트를 직접 짜는 대신, **Codex / Claude Code / Antigravity 같은 에이전트 환경에서 이 워크스페이스를 열고 자연어로 요청**합니다.

예를 들어 Codex 계열에서는:

1. 이 저장소를 워크스페이스로 엽니다.
2. 루트 `AGENTS.md`와 `skills/*/agents/openai.yaml`이 적용된 상태인지 확인합니다.
3. 에이전트에게 그냥 자연어로 요청합니다.

예시 요청:

```text
현대 판타지 웹소설 1화 원고 써줘. 주인공은 해고당한 날 각성하고, 3인칭 제한시점으로.
```

```text
이 초고를 개고해서 원고 수준으로 정리해줘.
```

```text
회귀 무협 150~200화 기준 기획안 잡아줘.
```

이때 사용자가 `$novel-writing` 같은 호출 문법을 직접 입력해야 하는 환경도 있을 수 있지만, 이 저장소의 기본 설계는 **암시적 호출(implicit invocation)** 을 허용하는 쪽입니다. 즉, 한국어 소설 집필 요청이면 에이전트가 `novel-writing`을 우선 사용하도록 설계되어 있습니다.

## 🧭 챕터 작성은 어떤 식으로 진행되나요?

`novel-writing` 스킬이 연결된 에이전트라면 보통 아래 순서로 동작합니다.

1. 요청을 `planning`, `fresh drafting`, `continuation`, `stage revision` 같은 작업 유형으로 라우팅합니다.
2. 필요한 최소 가정을 세웁니다.
3. 실제 원고 요청이면 `초고 -> 개고 -> 원고` 순서로 작성합니다.
4. 기본적으로 `원고`를 반환합니다.
5. 쓰기 가능한 환경이면 `drafts/초고`, `drafts/개고`, `drafts/원고`에 파일도 저장합니다.

즉, 사용자가 해야 할 일은 보통 **스킬 이름을 외우는 것보다, 원하는 결과를 자연어로 분명히 요청하는 것**에 가깝습니다.

## 🚫 없는 것 / 있는 것

없는 것:

- NobelWriter 전용 단일 CLI 명령
- 이 저장소만으로 바로 실행되는 범용 `write chapter` 실행 파일

있는 것:

- 에이전트가 읽는 운영 파일
- 스킬 본문과 참조 문서
- 단계별 원고 저장 규칙
- 플랫폼별 적용 가이드

전용 명령어가 필요한 경우에는 이 저장소 위에 별도 래퍼 CLI를 추가로 만들어야 합니다.
현재 저장소는 그보다는 **에이전트가 읽고 행동하는 작업 규칙 세트**에 가깝습니다.

---

## 🪪 라이선스 및 원칙 (License & Principles)

이 프로젝트는 **"인간이 주도하고 AI가 증폭하는(Human-Led, AI-Augmented)"** 창의성을 원칙으로 합니다. NobelWriter는 단순히 대신 써주는 도구가 아니라, 당신이 더 좋은 글을 쓸 수 있도록 돕는 **시스템**을 제공합니다.

---

<p align="center">
  <i>한국어 창작자들이 자신만의 세계를 더 완벽하게 구축할 수 있도록 돕습니다.</i>
</p>
