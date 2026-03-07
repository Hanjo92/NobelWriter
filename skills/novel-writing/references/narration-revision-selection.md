# Narration Revision Selection

Use this file when the prose meaning is correct but the narration feels heavy, awkward, or hard to read.

## How To Use

1. Identify the main reading problem.
2. Pick the revision goal.
3. Keep the scene meaning and emotional function fixed.
4. Rewrite for flow, not for bigger plot change.

Do not confuse sentence-level repair with scene-level rewrite.

## Core Revision Prompt

```text
Revise this Korean narration.
POV mode: [1인칭 / 3인칭 제한 / distant third-person]
Primary problem: [stiff / tangled / overwritten / repetitive / flat / translation-like / weak rhythm]
Revision goal: [naturalize / simplify / improve rhythm / sharpen image / compress / clarify subject / fix POV drift]
Rule: Preserve the meaning, scene function, emotional direction, and POV ownership.
Narration rule: Make the sentence read smoothly in Korean without sounding translated or over-assembled, and keep it inside the selected POV boundary.
```

## Problem Rows

### Stiff

```text
Rewrite into more natural Korean syntax. Prefer the order a Korean reader expects on first read.
```

### Tangled

```text
Untangle nested clauses and overloaded modifiers. Split only where needed to recover readability.
```

### Overwritten

```text
Remove decorative phrasing that does not sharpen image, mood, or pressure.
```

### Repetitive

```text
Reduce repeated rhythm, repeated emotional labels, and repeated connective patterns.
```

### Flat

```text
Restore texture with one clear image, one sharper verb, or one more precise emotional angle.
```

### Translation-Like

```text
Replace English-shaped logic and connective flow with idiomatic Korean movement.
```

### Weak Rhythm

```text
Adjust sentence length and stress placement so the line lands cleanly when read once.
```

### POV Drift

```text
Re-anchor the sentence to the chosen POV. Remove knowledge, judgment, or camera distance that the current narration mode cannot legitimately hold.
```

## Revision Goal Rows

### Naturalize

```text
Make the sentence feel written by a Korean novelist, not converted from another language.
```

### Simplify

```text
Reduce syntactic load and keep only what the reader needs for this beat.
```

### Improve Rhythm

```text
Vary sentence weight and place the important word or image where it lands best.
```

### Sharpen Image

```text
Replace generic abstraction with one concrete, scene-relevant image.
```

### Compress

```text
Make the sentence shorter without dropping meaning or pressure.
```

### Clarify Subject

```text
Make it immediately clear who acts, feels, or notices.
```

### Fix POV Drift

```text
Keep the sentence inside the selected narrator or perceiver's access, tone, and distance.
```

## Narration Checks

Run these checks during revision:

- Does the sentence read cleanly on the first pass?
- Is the subject immediately identifiable?
- Is the modifier chain longer than the image can support?
- Would the line improve if one abstract noun became a concrete verb or image?
- Does the sentence end on the strongest word, or does it trail off?
- Could two similar beats be merged into one cleaner sentence?
- Is the sentence still owned by the chosen `1인칭` or `3인칭` perceiver?
- Does the line claim knowledge this POV cannot legitimately have?

## Frequent Failure Patterns

### Meaning Correct, Rhythm Bad

Awkward:
```text
그는 자신에게 다가오고 있는 불안과 함께 점점 더 무거워지는 공기의 감각을 느끼고 있었다.
```

Better:
```text
불안이 가까워질수록 공기도 묵직해졌다.
```

Why it works:
- removes stacked perception phrasing
- lands the image faster

### Modifier Pile-Up

Awkward:
```text
창밖으로 희미하게 번져 나오고 있는 새벽빛이 그녀의 떨리고 있는 손끝 위로 조용하게 내려앉았다.
```

Better:
```text
희미한 새벽빛이 떨리는 손끝 위에 조용히 내려앉았다.
```

Why it works:
- keeps the image, removes redundant progressive phrasing

### Abstract Emotion Load

Awkward:
```text
그 말은 그녀에게 설명하기 어려운 종류의 복잡한 슬픔과 체념을 동시에 안겨 주었다.
```

Better:
```text
그 말에 그녀는 잠깐 웃을 뻔하다가, 그대로 입을 다물었다.
```

Why it works:
- shows the feeling through reaction
- reduces abstract labeling

### Subject Drift

Awkward:
```text
문이 닫히는 소리와 함께 그제야 가라앉기 시작한 것은 방 안의 소란이 아니라 그의 표정이었다.
```

Better:
```text
문이 닫히자 방 안은 조용해졌다. 그런데 정작 가라앉은 건 소란이 아니라 그의 표정이었다.
```

Why it works:
- clarifies the turn
- separates setup from emphasis

## Fast Selection Table

| Problem | Best goal | First fix |
| --- | --- | --- |
| 문장은 맞는데 잘 안 읽힘 | Naturalize or simplify | 어순과 절 길이 정리 |
| 수식이 과함 | Compress or clarify subject | 수식어와 진행형 정리 |
| 감정이 추상적임 | Sharpen image | 반응, 동작, 이미지로 치환 |
| 리듬이 늘어짐 | Improve rhythm | 끝어절과 문장 길이 재배치 |
| 번역투 느낌 | Naturalize | 연결 방식과 추상명사 줄이기 |

## Ready-Made Blocks

### Naturalize Heavy Narration

```text
Revise this Korean narration.
Primary problem: stiff and translation-like
Revision goal: naturalize
Rule: Preserve the meaning and mood, but rewrite into smoother Korean prose.
Narration rule: Remove translated syntax, stacked perception phrasing, and unnecessary abstract nouns.
```

### Improve Chapter Rhythm

```text
Revise this Korean narration.
Primary problem: weak rhythm
Revision goal: improve rhythm and compress
Rule: Preserve scene meaning and emotional tone.
Narration rule: Make the paragraph read cleanly in one pass with stronger sentence landing points.
```

### Repair First-Person Drift

```text
Revise this Korean narration.
POV mode: 1인칭
Primary problem: POV drift
Revision goal: fix POV drift and naturalize
Rule: Preserve meaning, but make the line sound like something the narrator could actually think or narrate from within their own awareness.
Narration rule: Remove outside diagnosis, impossible self-observation, and knowledge the narrator could not hold directly.
```

### Repair Third-Person Limited Drift

```text
Revise this Korean narration.
POV mode: 3인칭 제한
Primary problem: POV drift
Revision goal: fix POV drift and clarify subject
Rule: Preserve meaning, but keep the narration inside the active perceiver's knowledge and distance.
Narration rule: Remove unexplained access to non-POV interior states and re-anchor the line to observable or focalized detail.
```

### Sharpen Emotional Narration

```text
Revise this Korean narration.
Primary problem: flat or abstract emotion
Revision goal: sharpen image
Rule: Preserve the feeling, but express it through reaction, detail, or pressure instead of abstract labeling.
Narration rule: Prefer concrete movement over explanation.
```

## Genre-Grounded Narration Transformations

Use these when the sentence is semantically acceptable but does not yet sound native to the requested genre.

### Traditional Fantasy

Awkward:
```text
왕궁 전체를 덮고 있는 긴장감은 모두의 움직임을 점점 더 조심스럽게 만들고 있었다.
```

Natural:
```text
왕궁에는 숨소리마저 낮아진 듯한 긴장이 내려앉아 있었다.
```

Why it works:
- removes mechanical abstraction
- replaces generic tension phrasing with a court-scale image

### Martial Arts

Awkward:
```text
그가 칼을 쥐는 방식에는 지금까지 겪어 온 수많은 싸움의 경험이 담겨 있는 것처럼 보였다.
```

Natural:
```text
그가 검을 쥔 순간, 잔흔처럼 밴 실전의 버릇이 먼저 드러났다.
```

Why it works:
- tightens the sentence
- sounds closer to murim observation than generic explanation

### Modern Fantasy

Awkward:
```text
그 순간 사무실 안의 공기는 설명하기 어려운 종류의 비현실적인 감각으로 천천히 바뀌고 있었다.
```

Natural:
```text
그 순간, 사무실 공기가 현실에서 반 발짝 밀려난 것처럼 어긋났다.
```

Why it works:
- removes vague abstraction
- gives the anomaly a quick, readable shape

### Fusion Fantasy

Awkward:
```text
그의 머릿속에서는 여러 시대의 지식과 감각들이 서로 충돌하면서 복잡한 혼란을 만들어 내고 있었다.
```

Natural:
```text
머릿속에서는 전장의 감각과 마도식 계산이 한꺼번에 맞부딪쳤다.
```

Why it works:
- compresses the idea
- makes the mixed-system concept legible in one pass

### Romance

Awkward:
```text
그가 미소를 지은 이후로 그녀의 마음속에는 설명하기 어려운 동요가 계속해서 남아 있었다.
```

Natural:
```text
그가 한 번 웃은 뒤로, 그녀는 자꾸 그 장면에서 마음이 걸렸다.
```

Why it works:
- keeps emotional effect but removes abstract emotional packaging
- sounds more like living Korean prose

## Genre X Audience Narration Examples

### Traditional Fantasy Male-Oriented

Awkward:
```text
전투가 시작되기 직전의 상황은 그에게 앞으로 닥칠 거대한 책임과 부담을 명확하게 인식하게 만들었다.
```

Natural:
```text
전투가 열리기 직전, 그의 어깨엔 물러설 수 없는 책임이 먼저 올라탔다.
```

Why it works:
- pushes the line forward
- fits a pressure-first heroic tone

### Traditional Fantasy Female-Oriented

Awkward:
```text
연회장의 차가운 분위기는 그녀에게 자신이 더 이상 예전과 같은 위치에 있지 않다는 사실을 깨닫게 해 주었다.
```

Natural:
```text
연회장에 들어선 순간, 그녀는 자신을 향하던 시선의 온도부터 달라졌다는 걸 알아차렸다.
```

Why it works:
- routes status change through social perception
- better suits relational court tension

### Martial Arts Male-Oriented

Awkward:
```text
상대의 기세는 그가 결코 만만하게 상대할 수 없는 수준이라는 사실을 알려 주고 있었다.
```

Natural:
```text
마주 선 것만으로도 알 수 있었다. 이번엔 대충 넘길 상대가 아니었다.
```

Why it works:
- strips explanatory phrasing
- lands as a quick combat read

### Martial Arts Female-Oriented

Awkward:
```text
사형의 침묵은 그녀에게 말보다 더 깊은 배신감과 거리감을 느끼게 만들었다.
```

Natural:
```text
사형은 끝내 아무 말도 하지 않았다. 그 침묵이 오히려 가장 늦게 와서 가장 깊게 박혔다.
```

Why it works:
- keeps emotion layered but readable
- lets hurt arrive through rhythm

### Modern Fantasy Male-Oriented

Awkward:
```text
몬스터가 등장한 이후 그는 자신이 선택해야 하는 행동의 우선순위를 매우 빠르게 정리하기 시작했다.
```

Natural:
```text
몬스터가 튀어나오자 그는 도망칠 사람, 막을 길, 쓸 스킬부터 먼저 셌다.
```

Why it works:
- makes thought process concrete
- fits fast, capability-driven pacing

### Modern Fantasy Female-Oriented

Awkward:
```text
그의 태도 변화는 그녀로 하여금 지금까지 믿고 있던 안정감이 흔들리고 있다는 사실을 깨닫게 했다.
```

Natural:
```text
그가 평소와 다르게 말을 고르는 순간, 그녀는 자신이 믿고 있던 평온이 먼저 금 가는 소리를 들었다.
```

Why it works:
- keeps the emotional shift but gives it an image
- suits relationally sensitive urban fantasy

### Fusion Fantasy Male-Oriented

Awkward:
```text
그는 이 회담이 단순한 대화가 아니라 힘의 주도권을 결정짓는 중요한 분기점이라는 사실을 알고 있었다.
```

Natural:
```text
그는 알고 있었다. 이번 회담은 말 몇 마디가 아니라 판의 주인을 가르는 자리였다.
```

Why it works:
- sharpens dominance and stakes
- keeps strategic weight without bloat

### Fusion Fantasy Female-Oriented

Awkward:
```text
그녀는 그의 친절 속에 감춰져 있는 계산적인 의도를 점점 더 분명하게 느끼고 있었다.
```

Natural:
```text
다정한 말투 아래에 계산이 깔려 있다는 걸, 그녀는 이제 모른 척할 수 없었다.
```

Why it works:
- preserves layered reading
- makes the sentence more direct and elegant

### Romance Male-Oriented

Awkward:
```text
그녀가 떠나려고 하자 그는 자신이 예상했던 것보다 훨씬 더 크게 흔들리고 있다는 사실을 깨달았다.
```

Natural:
```text
그녀가 돌아서자, 생각보다 먼저 흔들린 건 그의 발이 아니라 속이었다.
```

Why it works:
- keeps the emotional beat but lands it with a cleaner turn
- avoids flat self-report

### Romance Female-Oriented

Awkward:
```text
그의 무심한 배려는 그녀의 마음속에 조용하지만 분명한 파문을 만들어 내고 있었다.
```

Natural:
```text
무심하게 건넨 배려 하나가 이상하리만치 오래 마음에 남았다.
```

Why it works:
- softens the abstraction
- reads more naturally in emotional prose

### Romance Neutral

Awkward:
```text
두 사람 사이에는 예전과는 달라진 공기와 쉽게 정의하기 어려운 감정의 흐름이 남아 있었다.
```

Natural:
```text
예전과 같지 않다는 건 둘 다 알았다. 문제는 그걸 뭐라고 불러야 할지만 남아 있었다.
```

Why it works:
- turns abstract emotional summary into readable narrative movement
- keeps broad accessibility
