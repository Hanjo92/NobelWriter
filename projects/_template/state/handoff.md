# Handoff

## Runtime Stop Evidence

- state:
- next_action:
- current_batch_start:
- current_batch_end:
- last_run_at:
- last_completed_stage:
- last_completed_transition:
- last_artifact_pointer:
- last_proof_predicate:
- specialist_return_accepted:
- last_valid_boundary:
- last_snapshot_paths:
- last_mismatch_evidence:

## Specialist Return Evidence

- specialist:
- transition:
- source_artifact:
- returned_artifact:
- batch_range:
- excerpt_range:
- required_fields_checked:
- proof_artifact_paths:
- next_handoff_target:

## Evidence By Specialist Type

### Slice Planning

- chapter_start:
- chapter_end:
- batch_goal:
- success_conditions:
- active_pov:
- active_cast:
- must_keep:
- must_not_break:
- handoff_target:
- planning_artifact:
- proof_artifact_paths:

### Drafting

- chapters_drafted:
- stage_files:
- latest_manuscript_batch:
- assumptions:
- continuity_notes:
- next_handoff_target:

### QA Review

- reviewed_batch_range:
- outcome:
- evidence:
- root_cause:
- repair_direction:
- re_audit_gate:
- handoff_target:

### Recovery Planning

- root_cause:
- repair_order:
- next_safe_move:
- handoff_target:
- must_not_break_constraints:
- proof_artifact_paths:
- exact_re_entry_slice:

### Voice Handoff

- voice_handoff:
- source_artifact:
- affected_speakers:
- relationship_state:
- voice_failure:
- repair_rules:
- proof_rewrites:
- register_notes:
- assumptions:
- unresolved_voice_risks:
- next_handoff_target:

## Blocked Evidence

- block_type:
- blocked_reason:
- proof_artifact_path:
- proof_predicate:
- mismatch_type:
- mismatch_evidence:

## Snapshot And Re-entry Evidence

- snapshot_paths:
- last_valid_boundary:
- re_entry_state:
- re_entry_batch:

## Notes

- Last completed step:
- Last failed step:
- Resume from:
- Notes:
