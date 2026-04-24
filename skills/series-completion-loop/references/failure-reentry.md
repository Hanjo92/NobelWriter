# Failure And Re-entry

Snapshot before each run:

- `state/runtime.yaml`
- `state/active-slice.yaml`
- `state/handoff.md`

Block conditions:

- missing or ambiguous selected project runtime
- missing state
- contradictory state
- same slice QA fails twice without a changed repair direction
- recovery runs twice without changing `active-slice.yaml` or the recovery artifact
- approval bypass in `approval-gated` mode
- active slice and actual manuscript range diverge
- completion conditions are undefined while next-slice generation continues
- specialist return evidence is missing, out of batch, future-batch, schema-mismatched, or contradicts the active slice

Operational checks:

- missing selected runtime means no explicit, pre-existing `projects/<series-slug>/` path was supplied by the user, automation prompt, or current runtime files
- ambiguous selected runtime means more than one `projects/<series-slug>/` path could plausibly match the request; do not choose from chat context
- missing state means any required file is absent, or a required key is absent from the file that owns it
- required `project.md` fields are Title, Slug, Target scale, Completion mode, Default batch size, and Ending promise
- required `state/runtime.yaml` keys are `mode`, `state`, `next_action`, `approval_pending`, `last_approval_at`, `last_approval_batch_start`, `last_approval_batch_end`, `last_approval_note`, `current_batch_start`, `current_batch_end`, `latest_manuscript_batch`, `last_run_at`, `failure_count`, `blocked_reason`, `last_completed_stage`, `last_completed_transition`, `last_artifact_pointer`, `last_proof_predicate`, and `specialist_return_accepted`
- required `state/active-slice.yaml` keys are `chapter_start`, `chapter_end`, `batch_goal`, `success_conditions`, `active_pov`, `active_cast`, `must_keep`, `must_not_break`, and `handoff_target`
- contradictory state means the runtime `state` is not one of the approved states, `mode` is not `autonomous` or `approval-gated`, `current_batch_start` is greater than `current_batch_end`, `approval_pending: true` appears outside `approval_waiting`, `approval_pending: false` leaves `approval_waiting` without `last_approval_at` and matching approval batch fields, or `state: completed` still has a non-empty `next_action`
- `failure_count >= 2` on the same `current_batch_start` and `current_batch_end` means the same slice has failed twice
- a changed repair direction means `qa/latest-report.md` or `recovery/latest-recovery.md` names a different root cause, handoff target, or next safe move from the previous failed run
- repeated recovery means two consecutive runs have `state: recovery_planning` without changing `state/active-slice.yaml` or `recovery/latest-recovery.md`
- active-slice divergence means `state/active-slice.yaml` chapter range does not match the newest saved manuscript batch named in `state/runtime.yaml`
- undefined completion means `project.md` has no ending promise, target scale, or completion condition while `next_action` is `slice_planning`
- unproven stop means `state/runtime.yaml` or `state/handoff.md` lacks the artifact path or predicate that proves `completed`, `blocked`, or the completed transition; stay in the prior valid state or mark `blocked`
- machine-checkable stop evidence means `last_completed_transition`, `last_artifact_pointer`, `last_proof_predicate`, and `specialist_return_accepted` are populated consistently with the state transition, or `blocked_reason` names why they cannot be accepted
- specialist return mismatch means the returned planning packet, manuscript batch, QA report, recovery artifact, or `voice_handoff` lacks required fields, has present-but-empty or semantically invalid values, lacks proof paths, points outside `current_batch_start` through `current_batch_end`, is schema-mismatched, or asks the orchestrator to repair specialist output inline

Recovery rules:

- preserve manuscript files
- never auto-roll back manuscript output
- re-enter only from the last valid boundary after the runtime snapshot is available
