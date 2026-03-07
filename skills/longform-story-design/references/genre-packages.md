# Genre Packages

Use this file when the planning package should change according to genre pressure rather than staying generically "longform."

## Selection Rule

Choose one dominant package first. Add one secondary package only if it materially changes escalation, not just surface aesthetics.

If the user explicitly names the genre or package, that explicit label outranks inference. Map the user label to the closest supported package first, then refine only if the user asked for a hybrid.

Ask:

- what keeps the reader returning chapter to chapter
- what kind of reversal matters most
- what kind of failure would feel most damaging
- what the ending promise fundamentally resolves

Use those questions in that order. The first question has the highest priority.

## Explicit User Label Rule

When the user directly names a genre, choose the matching package before using any diagnostic ladder.

Common mappings:

- `로맨스`, `로판`, `romance`, `romance fantasy` -> `romance / romance fantasy`
- `성장형 판타지`, `액션 판타지`, `progression`, `action fantasy` -> `progression / action fantasy`
- `미스터리`, `스릴러`, `추리`, `mystery`, `thriller` -> `mystery / thriller`
- `정치극`, `전쟁물`, `세력물`, `궁중암투`, `political`, `war`, `faction drama` -> `political / war / faction drama`
- `서바이벌`, `아포칼립스`, `호러`, `survival`, `apocalypse`, `horror` -> `survival / apocalypse / horror`

For broader alias coverage, use [genre-alias-map.md](genre-alias-map.md).

If the user names two genres together, treat the first or more strongly emphasized one as dominant unless they explicitly ask for equal hybrid weighting.

## Fast Decision Order

Decide in this sequence:

1. check for explicit user genre label
2. identify the chapter-return engine
3. identify the volume-end promise
4. identify the main expansion logic for the middle
5. identify the most painful failure mode
6. assign one dominant package

If the explicit user label and inferred engine disagree, prefer the explicit user label unless the user is clearly using the label loosely and asks you to decide the better structural package.

## Negative Rule

Do not choose by surface marker alone:

- palace, empire, nobles -> not automatically political
- magic school, dungeon, swordsmanship -> not automatically progression
- plague, ruins, monsters -> not automatically survival horror
- engagement, marriage, courtship -> not automatically romance
- detective, case, serial murder -> not automatically mystery

Choose by what actually drives continuation pressure.

Exception: an explicit user genre label is not a surface marker. It is a user constraint and should be honored.

## Trigger Map

Use these triggers as hard indicators:

- `romance / romance fantasy`: confession delay, jealousy, status gap, contractual intimacy, emotional misread, attachment under social constraint
- `progression / action fantasy`: training loop, rank climb, cultivation stage, trial clearing, build optimization, power-cost management
- `mystery / thriller`: clue chain, suspect rotation, hidden truth, misdirection, pursuit of proof, reveal sequencing
- `political / war / faction drama`: alliance trade, succession, decree fallout, tax or military leverage, faction balance, public-private goal split
- `survival / apocalypse / horror`: resource depletion, infection spread, pursuit, shelter loss, unsafe environment, trust collapse

## Tie-Break Rules

Use these only when two packages both fit:

### Romance vs Political

- choose `romance` if arc closure is measured by emotional redefinition
- choose `political` if arc closure is measured by changed leverage or faction position

### Progression vs Mystery

- choose `progression` if the main question is "how do we get stronger or higher"
- choose `mystery` if the main question is "what is really happening or who is behind it"

### Mystery vs Survival

- choose `mystery` if information control drives dread
- choose `survival` if environment pressure drives dread

### Political vs Survival

- choose `political` if resource scarcity is mainly negotiated through institutions
- choose `survival` if scarcity is mainly immediate and bodily

### Romance vs Mystery

- choose `romance` if concealment exists to delay intimacy
- choose `mystery` if concealment exists to delay truth exposure

## Hybrid Permission Rule

Allow a secondary package only if it changes one of these:

- volume order
- type of reversal
- end-of-volume promise
- artifact emphasis

If it changes only styling, do not add it.

## Default Fallbacks

When signals remain incomplete, default conservatively:

- relationship-first fantasy -> `romance fantasy`
- rank-first fantasy -> `progression fantasy`
- case-first modern suspense -> `mystery thriller`
- throne or faction-first court story -> `political faction drama`
- shelter and scarcity-first disaster story -> `survival apocalypse horror`

Use these fallbacks only when the user did not directly provide a genre label.

## Romance / Romance Fantasy

Use when emotional leverage, hierarchy friction, secrecy, jealousy, marriage politics, or relational reversals are carrying the series.

Prioritize:

- core relationship engine
- status and leverage imbalance
- secrecy, misunderstanding, and confession timing
- emotional reversal at arc ends
- social cost of desire

Emphasize in the package:

- story engine sheet
- core cast matrix
- first arc sketch
- volume ladder with relationship movement

Add these questions:

- why can they not separate cleanly
- what social or political barrier keeps pressure active
- what changes intimacy without resolving the main tension

## Progression / Action Fantasy

Use when ascent, combat growth, trials, rankings, cultivation, dungeon, academy, or power mastery drives the project.

Prioritize:

- cost curve for growth
- power ceiling and bottleneck design
- enemy or challenge ladder
- reward economy
- escalation beyond simple stat inflation

Emphasize in the package:

- story engine sheet
- story bible
- series expansion map
- volume ladder

Add these questions:

- what does every gain cost
- what prevents progression from becoming linear
- how does each volume change the scale of challenge

## Mystery / Thriller

Use when the reader return engine depends on uncertainty, investigation, pursuit, or hidden truth.

Prioritize:

- question chain
- clue control
- suspect or threat spread
- false pattern versus true pattern
- reveal timing

Emphasize in the package:

- story engine sheet
- story bible
- knowledge-state tracker
- first arc sketch or chapter-range plan

Add these questions:

- what is the first question, deeper question, and final question
- who knows the wrong version and why
- what reveal should reframe earlier material

## Political / War / Faction Drama

Use when institutions, alliances, power blocs, succession, rebellion, or public-private conflict dominate.

Prioritize:

- leverage structure
- faction goals
- alliance volatility
- consequence spread
- public action versus hidden intent

Emphasize in the package:

- story bible
- series expansion map
- history spine
- volume ladder

Add these questions:

- who gains if nothing changes
- what public move causes private fallout
- how does scale widen from personal struggle to factional conflict

## Survival / Apocalypse / Horror

Use when scarcity, environment, contagion, pursuit, collapse, or trust breakdown carries the series.

Prioritize:

- resource pressure
- safety illusion versus actual danger
- trust fracture
- environment or system hostility
- collapse threshold

Emphasize in the package:

- story engine sheet
- story bible
- chapter-range plan
- continuity ledger if drafting exists

Add these questions:

- what runs out first
- what breaks the group's trust
- how does each arc remove one layer of safety

## Hybrid Rule

For hybrid projects, phrase the package like:

- dominant package: romance fantasy
- secondary package: political drama

Then state one sentence explaining which package controls endings and which controls expansion.

## Sample Impact Rule

Any later sample output should visibly reflect the chosen package in:

- project frame labels
- design decision sentence
- artifact emphasis
- volume-end or arc-end promise style

For concrete examples, read [genre-package-samples.md](genre-package-samples.md).
