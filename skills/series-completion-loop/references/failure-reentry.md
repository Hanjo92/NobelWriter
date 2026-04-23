# Failure And Re-entry

Snapshot before each run:

- `state/runtime.yaml`
- `state/active-slice.yaml`
- `state/handoff.md`

Block conditions:

- missing state
- contradictory state
- same slice QA fails twice without a changed repair direction
- recovery runs twice without changing `active-slice.yaml` or the recovery artifact
- approval bypass in `approval-gated` mode
- active slice and actual manuscript range diverge
- completion conditions are undefined while next-slice generation continues

Operational checks:

- missing state means any required file is absent, or a required key is absent from the file that owns it
- required `project.md` fields are Title, Slug, Target scale, Completion mode, Default batch size, and Ending promise
- required `state/runtime.yaml` keys are `mode`, `state`, `next_action`, `approval_pending`, `current_batch_start`, `current_batch_end`, `last_run_at`, `failure_count`, `blocked_reason`, and `last_completed_stage`
- required `state/active-slice.yaml` keys are `chapter_start`, `chapter_end`, `batch_goal`, `success_conditions`, `active_pov`, `active_cast`, `must_keep`, `must_not_break`, and `handoff_target`
- contradictory state means the runtime `state` is not one of the approved states, `mode` is not `autonomous` or `approval-gated`, `current_batch_start` is greater than `current_batch_end`, `approval_pending: true` appears outside `approval_waiting`, or `state: completed` still has a non-empty `next_action`
- `failure_count >= 2` on the same `current_batch_start` and `current_batch_end` means the same slice has failed twice
- a changed repair direction means `qa/latest-report.md` or `recovery/latest-recovery.md` names a different root cause, handoff target, or next safe move from the previous failed run
- repeated recovery means two consecutive runs have `state: recovery_planning` without changing `state/active-slice.yaml` or `recovery/latest-recovery.md`
- active-slice divergence means `state/active-slice.yaml` chapter range does not match the newest saved manuscript batch named in `state/runtime.yaml`
- undefined completion means `project.md` has no ending promise, target scale, or completion condition while `next_action` is `slice_planning`

Recovery rules:

- preserve manuscript files
- never auto-roll back manuscript output
- re-enter only from the last valid boundary after the runtime snapshot is available
