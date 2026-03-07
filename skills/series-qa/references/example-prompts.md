# Example Prompts

Use this file when you need concrete examples of requests that should trigger `series-qa`.

## Fast Triage

- "장편 1권 후반부가 갑자기 힘이 빠지는데 어디서부터 망가졌는지 진단해줘."
- "12화 이후 독자 반응이 떨어졌는데 상위 3개 문제만 추려서 우선순위로 잡아줘."
- "이 원고가 왜 지루하게 느껴지는지 페이싱 기준으로만 빠르게 봐줘."

## Arc Checkpoint

- "31화부터 45화까지 아크만 읽고 연속성, 감정선, 떡밥 회수 쪽 문제를 찾아줘."
- "2부 초반 아크가 반복적으로 느껴지는데 어떤 비트가 재탕되는지 짚어줘."
- "중반부에서 주인공 동력이 사라졌다는 느낌이 있는데 실제로 어디서 수동적으로 변하는지 봐줘."

## Continuity And Payoff Audit

- "설정집이랑 실제 원고가 충돌하는 부분이 있는지 찾아서 정리해줘."
- "초반에 깔아둔 떡밥들이 후반에서 제대로 회수되는지 점검해줘."
- "등장인물들이 알면 안 되는 정보를 너무 빨리 아는지 지식 상태 기준으로 봐줘."

## Serialization Check

- "웹소설 기준으로 최근 10화가 왜 다음 화를 덜 궁금하게 만드는지 진단해줘."
- "회차 말미 훅은 많은데 다음 화에서 김이 빠진다는 피드백이 있다. 어디가 문제인지 봐줘."
- "연재형 기준으로 초반 요약이 과한지, 낚시만 있고 보상이 부족한지 체크해줘."

## Revision Brief

- "전체를 갈아엎지 말고, 최소 수정으로 살릴 수 있는 문제부터 순서대로 정리해줘."
- "이 원고를 개고하기 전에 수정 지시서처럼 써줘. 무엇을 왜 고쳐야 하는지 우선순위로."
- "출판 투고 전에 구조적 리스크만 걸러내는 QA 리포트를 만들어줘."

## Romance-Focused Triggers

- "로맨스는 있는데 관계가 앞으로 안 나간다. 어디서부터 감정선이 제자리걸음인지 봐줘."
- "고백 직전만 반복되고 실제 관계 변화가 없다. 로맨스 아크 QA 해줘."
- "둘의 케미는 살아 있는데 왜 독자가 답답해하는지 관계 진전 기준으로 진단해줘."

## Mystery-Focused Triggers

- "추리물인데 단서는 많은데 수사가 앞으로 나가는 느낌이 없다. 어디가 문제인지 봐줘."
- "범인 공개는 됐는데 반전이 약하다는 피드백이 있다. 리빌이 왜 약한지 QA 해줘."
- "수사 주인공이 직접 끌고 가는 느낌이 없는데 중반부 조사 파트를 점검해줘."

## Progression Fantasy Triggers

- "성장형 판타지인데 강해지긴 하는데 시원한 맛이 줄었다. 성장 엔진이 어디서 약해졌는지 봐줘."
- "수련 에피소드가 반복적으로 느껴진다. 파워업과 훈련 루프를 QA 관점으로 봐줘."
- "랭크업은 하는데 다음 전투가 예전이랑 별 차이가 없다. progression fantasy 기준으로 진단해줘."

## Political Intrigue Triggers

- "정치물이인데 세력은 많은데 누가 왜 움직이는지 흐려졌다. faction QA 해줘."
- "배신 장면은 큰데 납득이 약하다. 계략과 레버리지 빌드가 어디서 부족한지 봐줘."
- "궁정 암투가 말만 복잡하고 실제 권력이 움직이는 느낌이 없다. 정치 파트만 떼서 진단해줘."

## Prompt Shape Rule

Strong prompts for this skill usually specify:

- audit range
- suspected failure or reader complaint
- desired output format
- whether the work is serial, volume-based, or one long manuscript
- whether the complaint is genre-general or genre-specific

If those are missing, infer the narrowest valid audit and state the assumption.
