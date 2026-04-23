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

- `failure_count >= 2` on the same `current_batch_start` and `current_batch_end` means the same slice has failed twice
- a changed repair direction means `qa/latest-report.md` or `recovery/latest-recovery.md` names a different root cause, handoff target, or next safe move from the previous failed run
- repeated recovery means two consecutive runs have `state: recovery_planning` without changing `state/active-slice.yaml` or `recovery/latest-recovery.md`
- active-slice divergence means `state/active-slice.yaml` chapter range does not match the newest saved manuscript batch named in `state/runtime.yaml`
- undefined completion means `project.md` has no ending promise, target scale, or completion condition while `next_action` is `slice_planning`

Recovery rules:

- preserve manuscript files
- never auto-roll back manuscript output
- re-enter only from the last valid boundary after the runtime snapshot is available
