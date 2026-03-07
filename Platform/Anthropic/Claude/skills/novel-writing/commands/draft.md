# /draft — Korean Fiction Drafting

Invoke the `novel-writing` skill to draft or revise Korean fiction prose.

## When to use

Use this command to:
- Draft a new scene or chapter in Korean
- Revise narration, paragraph rhythm, or sentence flow
- Switch genre or audience tendency
- Produce 초고 → 개고 → 원고 stage files

## Behavior

When this command is called:
1. Read `skills/novel-writing/SKILL.md` first.
2. Read only the reference files needed for the specific request.
3. Draft the 초고 internally.
4. Revise to 개고, then polish to 원고.
5. Save all three stage files to `drafts/초고/`, `drafts/개고/`, `drafts/원고/` using the Write tool.
6. Run the 11-item quality gate from `CLAUDE.md`.
7. Return only the 원고 text, followed by the saved file paths.

## Usage example

```
/draft 3장 오프닝. 주인공 유아가 첫 등교일에 교문 앞에서 멈춰 서는 장면. 1인칭 현재형. 현대 청소년 로맨스.
```
