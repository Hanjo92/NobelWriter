# Handoff To Drafting

Use this file when longform planning needs to be reduced into a drafting packet for the prose layer.

## Give Drafting Only The Active Slice

Do not pass the whole bible into every chapter draft. Reduce the planning layer to the active repaired slice: the smallest contiguous stretch of material that can be drafted without contradicting repaired canon.

The active repaired slice should usually be one chapter or one short chapter range, one focal pressure, and one clear emotional or practical turn. If the next safe unit is larger than that, define why it must stay contiguous.

If the caller is `series-completion-loop` `slice_planning`, the active repaired slice is exactly `current_batch_start` through `current_batch_end`, normally the next `3~5화`, and nothing beyond it.

Reduce the planning layer to:

- current arc purpose
- active repaired slice boundary
- active POV and cast
- current relationship state
- world rules active in this chapter
- secrets relevant to the scene
- continuity constraints that must not break
- setup or payoff items that must appear

For multi-chapter packets, include the chapter sequence inside the active repaired slice, the pressure change from chapter to chapter, and what state must carry forward at the end of the packet. Omit older arc history that does not change the next safe chapter.

For multi-POV packets, include only the POVs that actually act inside the active repaired slice. Mark which POV owns each scene or chapter, what each POV knows at entry, and where the knowledge boundary changes. Omit inactive POVs, inactive subplots, and backstory that does not alter the immediate pressure.

## Draft Packet Template

```text
Project:
Current arc:
Recovery package source:
Active repaired slice:
Chapter or range:
Re-entry reason:
POV:
Current emotional state:
Current practical goal:
Immediate opposition:
Relevant world rules:
Relevant secrets:
What this chapter must set up:
What this chapter may pay off:
Continuity constraints:
Do not contradict:
First safe draft objective:
```

For orchestrated handoff, also include:

```text
Current batch:
chapter_start:
chapter_end:
batch_goal:
success_conditions:
active_pov:
active_cast:
must_keep:
must_not_break:
handoff_target:
Proof artifact path(s):
Next state suggestion:
Must not plan beyond:
```

## After Drafting

After a draft batch exists, update:

- timeline markers
- changed relationship status
- revealed or newly suspected information
- injuries, items, or travel state
- payoff tracker status

When called as an orchestrated specialist, return these tracker update requirements in the packet instead of directly editing runtime state or manuscript files.

If the packet covered multiple chapters or multiple POVs, update each affected chapter or POV state separately so the next packet does not flatten them into one generic follow-up.

Longform drift usually happens because drafting moves forward but the planning layer does not.
