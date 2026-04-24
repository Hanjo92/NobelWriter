# Request Router

Use this file to choose the smallest useful deliverable and the smallest reference set.

## Orchestrated Handoff Route

When `series-completion-loop`, `novel-writing`, or `series-qa` sends a dialogue or voice repair handoff, route to `orchestrated voice_handoff`.

Required scope:

- current batch range or explicit excerpt/range
- affected speakers or pair/group
- current relationship state
- scene pressure or visible voice failure

If any required scope is missing, return a blocker. Do not infer batch range, relationship progression, or plot context.

Allowed output:

- source artifact or excerpt reference
- batch range and excerpt range as separate fields when available
- repair rules
- proof rewrites with original-to-rewrite mapping
- register notes
- assumptions
- unresolved voice risks
- next handoff target

Forbidden output:

- future-batch plot beats
- narration-heavy prose
- chapter continuation
- direct manuscript or stage-file mutation
- runtime, ledger, QA, recovery, or stage-file edits

## Route By User Intent

Start with `composition-guide.md` whenever the request clearly combines more than one axis.
Do not jump straight into multiple axis files from this router. If two or more axes are active, route through `composition-guide.md` first and let it decide the stack.

- "Build the cast voices" or "set up speaking styles for the novel":
  deliver `cast voice bible`
  read `voice-design-workflow.md`, `voice-profile-template.md`, and `relationship-register-matrix.md`
- "This one character's voice is weak" or "make this person sound consistent":
  deliver `character voice card` plus `rewrite rules`
  read `voice-profile-template.md` and `reaction-patterns.md`
- "These two sound the same":
  deliver `pairwise contrast notes`
  read `cast-differentiation-examples.md` and `reaction-patterns.md`
- "The honorifics feel wrong" or "adjust 존댓말/반말":
  deliver `relationship register matrix`
  read `relationship-register-matrix.md`
- "Later chapters all sound the same" or "voice drift audit":
  deliver `dialogue drift report`
  read `dialogue-drift-checks.md` and `reaction-patterns.md`
- "Rewrite this dialogue so each speaker sounds distinct":
  deliver `repair rule` plus `proof rewrites`
  read `reaction-patterns.md`, then whichever file covers the main failure
- "Write it like a script" or "mostly dialogue with names":
  deliver `dialogue exchange sheet`
  read `composition-guide.md`, then `script-dialogue-rules.md`, then the narrowest additional files needed
- "How should I combine these axes?" or "조합부터 짜줘":
  deliver `composition recipe`
  read `composition-guide.md`
- "Make it a two-person scene":
  read `two-person-dialogue.md`
- "Make it a three-person scene":
  read `three-person-dialogue.md`
- "Make it feel like a group scene" or "meeting/family/squad dialogue":
  read `group-dialogue.md`
- "Make the hierarchy audible" or "boss-subordinate tension":
  read `relationship-superior-subordinate.md`
- "Make them feel like rivals":
  read `relationship-rivals.md`
- "Make it feel like they're not dating yet" or "썸 직전":
  read `relationship-pre-romance.md`
- "Make it sound like family":
  read `relationship-family.md`
- "Make it sound like coworkers":
  read `relationship-colleagues.md`
- "Make it feel like questioning" or "추궁하게":
  read `emotion-function-interrogation.md`
- "Make one side dodge" or "회피하게":
  read `emotion-function-evasion.md`
- "Make it tempting" or "유혹하듯":
  read `emotion-function-seduction.md`
- "Make it an apology scene" or "사과하게":
  read `emotion-function-apology.md`
- "Make it threatening" or "협박하듯":
  read `emotion-function-threat.md`
- "Make one side calm the other" or "달래듯":
  read `emotion-function-soothing.md`
- "Give them distinct filler words" or "말버릇 살려":
  read `micro-voice-catchphrases.md`
- "Separate them by sentence length" or "문장 길이 다르게":
  read `micro-voice-sentence-length.md`
- "Use pauses or cut-ins better" or "뜸/끊김 살려":
  read `micro-voice-pauses.md`
- "Different question style" or "질문 말투 다르게":
  read `micro-voice-question-style.md`
- "Different turn openings or endings" or "말머리/말끝 다르게":
  read `micro-voice-turn-edges.md`

## Escalate Only When Needed

Do not build a full cast bible when the user only needs:

- one speaker repaired
- one relationship recalibrated
- one scene audited
- one pair separated

Expand scope only if the localized failure clearly comes from missing cast-wide rules.
For orchestrated voice handoffs, expansion can only widen voice rules inside the active batch or excerpt. Broader planning, recovery, or prose execution belongs to the caller or another specialist.
