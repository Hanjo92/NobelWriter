# Task Router

Use this file when a Korean fiction request could fit more than one workflow and you need to choose the primary execution lane before loading references or drafting.

## Goal

Route the request early so planning, drafting, revision, and critique do not collapse into one generic response pattern.

Pick one primary lane first. Add a secondary lane only when the user clearly requests both.

## Primary Lanes

### 1. Planning

Use when the user asks for:

- 기획
- 로그라인, 시놉시스, 줄거리
- 세계관 정리
- 인물 시트, 관계도
- 장별 구성, 화별 구성, 장면 리스트

Default output:

- compact planning artifact
- no manuscript prose unless requested

Load first:

- [templates.md](templates.md)
- [genre-audience-samples.md](genre-audience-samples.md) if market texture matters

Do not load by default:

- [draft-pipeline.md](draft-pipeline.md)
- [manuscript-quality-gate.md](manuscript-quality-gate.md)

### 2. Fresh Drafting

Use when the user asks for:

- 초고 작성
- 장면 써줘
- 첫 화 써줘
- 챕터 써줘
- 오프닝, 도입부, 본문 원고

Default output:

- save `초고`, `개고`, `원고`
- return `원고` unless a stage is explicitly requested

Load first:

- [draft-pipeline.md](draft-pipeline.md)
- [manuscript-quality-gate.md](manuscript-quality-gate.md)
- [korean-prose.md](korean-prose.md) when dialogue or narration control matters

Optional:

- [chapter-opening-selection.md](chapter-opening-selection.md) for opener requests
- [starter-sets.md](starter-sets.md) for chapter 1 or subgenre-specific launch requests

### 3. Continuation

Use when the user asks for:

- 이어 써줘
- 다음 장면 이어서
- 이 원고 다음 분량 작성
- 같은 문체로 계속

Default output:

- match existing voice first
- then follow the fresh drafting path

Load first:

- existing user text
- [draft-pipeline.md](draft-pipeline.md)
- [manuscript-quality-gate.md](manuscript-quality-gate.md)

Extra rule:

- sample sentence density, dialogue texture, and paragraph rhythm before generating new prose

### 4. Stage Revision

Use when the user asks for:

- 초고를 개고로
- 개고를 원고로
- 이 장면 퇴고
- 이 문단을 원고 수준으로

Default output:

- save the full stage set
- return `원고` by default
- return the explicitly requested stage if named

Load first:

- [templates.md](templates.md) when you need a structured `개고` brief or pass card
- [draft-pipeline.md](draft-pipeline.md)
- [manuscript-quality-gate.md](manuscript-quality-gate.md)
- [workflow.md](workflow.md) for pass selection

Extra rule:

- preserve meaning unless the user asks for deeper structural change

### 5. Dialogue-Only Revision

Delegate this lane to `character-voice-bible`.

Use when the user asks for:

- 대사 수정
- 말투 다듬기
- 대사만 자연스럽게
- 캐릭터 말투 구분
- 존댓말/반말 정리

Default output:

- hand off dialogue revision, register tuning, and speaker separation to `character-voice-bible`
- do not expand into full-scene rewriting unless the user explicitly asks for manuscript-level revision too

Primary action:

- use `character-voice-bible` for dialogue-only revision and character voice tuning

Fallback only if `character-voice-bible` is unavailable:

- [dialogue-revision-selection.md](dialogue-revision-selection.md)
- [korean-prose.md](korean-prose.md)

Optional:

- [dialogue-tone-transforms.md](dialogue-tone-transforms.md) when the user wants a tonal shift and the voice skill is unavailable

Do not load by default:

- [draft-pipeline.md](draft-pipeline.md) unless the user wants full prose output saved through stages

### 6. Narration-Only Revision

Use when the user asks for:

- 문장 수정
- 문체 다듬기
- 서술만 손봐줘
- 문단 호흡 정리
- 번역투 제거

Default output:

- revise narration and sentence flow
- keep plot meaning fixed

Load first:

- [templates.md](templates.md) when you need a non-dialogue sentence or exposition revision card
- [narration-revision-selection.md](narration-revision-selection.md)
- [korean-prose.md](korean-prose.md)

Optional:

- [narration-tone-matrix.md](narration-tone-matrix.md) for problem-specific lookup
- [meaning-first-examples.md](meaning-first-examples.md) when the prose is semantically correct but assembled

Do not load by default:

- [draft-pipeline.md](draft-pipeline.md) unless the user wants full prose output saved through stages

### 7. Critique-Only

Use when the user asks for:

- 피드백
- 문제점 검토
- 어디가 어색한지 봐줘
- 분석만 해줘

Default output:

- diagnose first
- do not rewrite unless requested

Load first:

- [workflow.md](workflow.md)
- [korean-prose.md](korean-prose.md) if the critique depends on Korean line quality

## Fast Routing Questions

Ask these silently before acting:

1. Is the user asking for notes or for usable prose?
2. Is the source text missing, partial, or already written?
3. Does the user want planning, generation, revision, or diagnosis?
4. Is the scope full prose, dialogue only, or narration only?
5. Did the user explicitly name a return stage such as `초고`, `개고`, or `원고`?

## Combined Requests

Use one primary lane and one secondary lane only when necessary.

Common combinations:

- planning + fresh drafting: make a compact plan first, then draft
- critique-only + stage revision: diagnose the main breaks first, then revise if requested in the same prompt
- dialogue-only revision + narration-only revision: hand dialogue to `character-voice-bible`, handle non-dialogue prose in `novel-writing`, and keep the ownership of each pass explicit

If the combined request becomes too broad, shrink the first deliverable instead of skipping routing discipline.
