# Genre Alias Map

Use this file when the user names a genre in shorthand, platform slang, mixed Korean/English, or a subgenre label that should still resolve to one supported package.

## Mapping Rule

Normalize the user's label first. Then map it to one of the supported packages:

- `romance / romance fantasy`
- `progression / action fantasy`
- `mystery / thriller`
- `political / war / faction drama`
- `survival / apocalypse / horror`

If the user provides multiple labels, preserve the first clearly dominant one unless they explicitly ask for a hybrid.

## Romance / Romance Fantasy Aliases

Direct labels:

- 로맨스
- 로판
- 로맨스 판타지
- 궁정 로맨스
- 궁중 로맨스
- 계약연애물
- 계약결혼물
- 선결혼후연애
- 회귀 로판
- 빙의 로판
- 악녀물
- 후회남
- 집착남
- 구원서사 로맨스
- romance
- romance fantasy
- romantic fantasy
- court romance

Usually map here when dominant:

- 회귀물
- 빙의물
- 환생 로맨스
- 귀족물
- 황족물
- 궁정물
- 육아물
- 치정극

Map here only if return pressure is emotional or relational, not because noble costume appears.

## Progression / Action Fantasy Aliases

Direct labels:

- 성장형 판타지
- 성장물
- 정통 판타지
- 액션 판타지
- 전투 판타지
- 소드앤소서리
- 모험 판타지
- 아카데미물
- 헌터물
- 레이드물
- 던전물
- 시스템물
- 상태창물
- 레벨업물
- 회귀 헌터물
- 무협
- 선협
- 수련물
- cultivation
- progression fantasy
- action fantasy
- litRPG
- dungeon fantasy
- academy fantasy

Usually map here when dominant:

- 차원이동 후 성장
- 먼치킨물
- 빌드물
- 랭킹전
- 토너먼트물
- 복수 성장물

Map here only if rank climb, mastery, challenge clearing, or costed power growth drives continuation.

## Mystery / Thriller Aliases

Direct labels:

- 미스터리
- 추리
- 추리물
- 스릴러
- 심리 스릴러
- 범죄 스릴러
- 수사물
- 형사물
- 탐정물
- 서스펜스
- 반전물
- 사건물
- 음모 스릴러
- serial mystery
- mystery
- thriller
- crime thriller
- investigation
- suspense

Usually map here when dominant:

- 법정 스릴러
- 복수 스릴러
- 폐쇄공간 미스터리
- 호러 미스터리
- 음모론물

Map here only if clue meaning, hidden truth, suspect rotation, or reveal timing drives next-chapter pull.

## Political / War / Faction Drama Aliases

Direct labels:

- 정치극
- 정치물
- 궁중암투
- 궁정암투
- 세력물
- 파벌물
- 권력투쟁물
- 권모술수물
- 왕위계승물
- 황위쟁탈전
- 제국물
- 귀족 정치극
- 군상극
- 전쟁물
- 전란물
- faction drama
- political drama
- court intrigue
- war drama
- succession drama

Usually map here when dominant:

- 혁명물
- 반란물
- 외교물
- 책략물
- 황실정치물
- 군벌물
- 제후전

Map here only if leverage, decrees, alliances, tax or military movement, or faction balance drives continuation.

## Survival / Apocalypse / Horror Aliases

Direct labels:

- 서바이벌
- 생존물
- 아포칼립스
- 재난물
- 재해물
- 폐쇄공간 생존물
- 좀비물
- 감염물
- 괴물 재난물
- 호러
- 공포물
- 크리처물
- 탈출물
- 디스토피아 생존물
- survival
- apocalypse
- horror
- survival horror
- disaster thriller
- outbreak

Usually map here when dominant:

- 포스트아포칼립스
- 멸망물
- 종말물
- 재해 스릴러
- 감금 생존물
- 재난 군상극

Map here only if shelter loss, contamination, pursuit, bodily scarcity, or trust collapse drives continuation.

## Cross-Package Aliases

These labels are not enough by themselves. Resolve by return engine:

- 회귀물
- 빙의물
- 환생물
- 복수물
- 복수극
- 군상극
- 디스토피아
- 궁정물
- 학원물
- 사건물
- 현판
- 대체역사
- 피카레스크

Use quick resolution:

- if romance is the point of the return -> `romance / romance fantasy`
- if growth is the point of the return -> `progression / action fantasy`
- if truth is the point of the return -> `mystery / thriller`
- if leverage is the point of the return -> `political / war / faction drama`
- if survival is the point of the return -> `survival / apocalypse / horror`

## Ambiguous Label Rules

Use these when the user gives a label that frequently spans multiple packages.

### 현판

Default:

- map to `progression / action fantasy`

Use this default when:

- the hook centers on awakening, system acquisition, rank climb, dungeon, raid, hunter labor, or skill optimization
- readers return to see the next gain, next clear, next rank, or next build payoff

Override to `mystery / thriller` when:

- the modern fantasy shell mainly supports investigation, hidden organization exposure, serial incidents, or clue reinterpretation

Override to `survival / apocalypse / horror` when:

- the modern fantasy shell mainly supports collapse, contamination, shelter loss, or citywide survival pressure

Override to `political / war / faction drama` when:

- guilds, corporations, state organs, or factions are the real longform engine and public consequence matters more than growth

Sample reference:

- See `Ambiguous Alias Sample 1: 현판 -> Mystery Thriller` in `genre-package-samples.md`

### 대체역사

Default:

- map to `political / war / faction drama`

Use this default when:

- the hook centers on regime change, court decisions, war planning, diplomatic leverage, institutional reform, or historical branching through power

Override to `progression / action fantasy` when:

- the alternate-history shell mainly exists to support ascent, conquest efficiency, military build-up as personal progression, or repeated capability upgrades

Override to `mystery / thriller` when:

- the branch point is mainly a hidden truth, conspiracy, sabotage chain, or historical cover-up to be uncovered

Override to `survival / apocalypse / horror` when:

- the alternate-history premise is driven by collapse, famine, plague, siege survival, or environmental catastrophe more than governance

Sample reference:

- See `Ambiguous Alias Sample 2: 대체역사 -> Political Faction Drama` in `genre-package-samples.md`

### 복수극

Default:

- do not map by revenge alone; resolve by the revenge delivery mechanism

Map to `romance / romance fantasy` when:

- revenge is carried by attachment, betrayal, jealousy, ex-lovers, marriage, or emotional redefinition

Map to `progression / action fantasy` when:

- revenge is carried by training, rank climb, build optimization, martial ascent, or repeatedly overcoming stronger opposition

Map to `mystery / thriller` when:

- revenge is carried by hidden truth exposure, culprit tracing, evidence assembly, or trap-and-reveal sequencing

Map to `political / war / faction drama` when:

- revenge is carried by regime reversal, faction destruction, succession blocking, or public consequence through institutions

Map to `survival / apocalypse / horror` when:

- revenge exists inside collapse pressure and the reader primarily returns for survival decisions, not score-settling

Sample reference:

- See `Ambiguous Alias Sample 3: 복수극 -> Romance Fantasy` in `genre-package-samples.md`

### 피카레스크

Default:

- do not lock a package from this label alone

Usually lean:

- `mystery / thriller` if episodic scams, investigations, cons, and hidden motives drive continuation
- `political / war / faction drama` if the rogue's movement mainly exposes institutions, class systems, and leverage structures
- `survival / apocalypse / horror` if drifting episode structure is mainly about making it through unsafe spaces

Only map to `romance / romance fantasy` when:

- episodic movement is still fundamentally organized around attachment and relational escalation

Only map to `progression / action fantasy` when:

- episodic movement is still fundamentally organized around capability climb, stronger opponents, or challenge ladders

Sample reference:

- See `Ambiguous Alias Sample 4: 피카레스크 -> Political Faction Drama` in `genre-package-samples.md`

## Resolution Examples

- `현판인데 헌터 랭킹전 중심` -> `progression / action fantasy`
- `현판인데 연쇄 실종 수사물` -> `mystery / thriller`
- `대체역사인데 궁정 개혁과 외교전 중심` -> `political / war / faction drama`
- `대체역사인데 역병과 피난 생존 중심` -> `survival / apocalypse / horror`
- `복수극인데 파혼과 재회 감정선 중심` -> `romance / romance fantasy`
- `복수극인데 증거 추적과 배후 폭로 중심` -> `mystery / thriller`
- `피카레스크인데 사기와 잠입이 에피소드 엔진` -> `mystery / thriller`
- `피카레스크인데 각 도시 권력 구조를 흔들며 이동` -> `political / war / faction drama`

## Platform-Slang Notes

Common shorthand that should normalize fast:

- 로판 -> romance fantasy
- 현판 -> usually progression / action fantasy unless the user frames it as thriller or survival
- 헌판 -> progression / action fantasy
- 대역 -> usually political / war / faction drama unless the user frames it as survival, mystery, or progression
- 복수극 -> resolve by delivery mechanism, not revenge alone
- 피카레스크 -> resolve by episode engine, not drifter tone alone
- 궁로판 -> romance fantasy
- 궁정물 -> romance fantasy or political drama depending on return engine
- 아카데미 -> usually progression / action fantasy
- 사건추리물 -> mystery / thriller
- 궁중암투물 -> political / war / faction drama
- 종말생존물 -> survival / apocalypse / horror

## User Constraint Rule

If the user says "이건 정치극으로", "로판으로", "스릴러 톤으로", or equivalent direct intent, honor that explicit choice first even if a neighboring package could also fit.
