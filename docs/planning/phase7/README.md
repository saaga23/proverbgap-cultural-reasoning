# Phase 1 Reconstruction — Index

**Status:** COMPLETE (read-only inspection; no code changed, no budget spent).
**Goal:** Reconstruct the original ProverbGap research project and reconcile it with the current shortcut-audit framing, so Phase 2 starts from verified facts.

## Quick links

| Doc | One-line summary |
|---|---|
| `01_REPOSITORY_AND_ARTIFACT_INVENTORY.md` | Repo map + evidence file index + conflicts table |
| `02_ORIGINAL_RESEARCH_RECONSTRUCTION.md` | Original May direction: S1/S2, 3 languages, 86.8%/62.5%, FiB/Generation planned |
| `03_CHRONOLOGICAL_RESEARCH_TIMELINE.md` | Full timeline (Apr→Jul) + 4 pivots + 9-row decision log |
| `04_EXPERIMENT_REGISTER.md` | Version register v1→v4.3.6 + v65→v70 + v68/v69/v70 specs |
| `05_EVALUATION_METHODS_RECONSTRUCTION.md` | Original accuracy metrics vs v68 audit gates; S2 validity issue |
| `06_DATASET_PROVENANCE_AND_LINEAGE.md` | 6→3 languages; Yoruba copyright/ISBN conflict; 60-row exposure |
| `07_MODEL_AND_EVALUATION_HISTORY.md` | Model rosters, provider migration, failures, competitors |
| `08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md` | Original↔v68 mapping + pivot chain + decision fork |
| `PHASE7_RESEARCH_OVERVIEW.md` | Canonical two-direction overview |
| `PHASE7_CURRENT_STATE.md` | Frozen/verified/blocked status |
| `PHASE7_OPEN_QUESTIONS.md` | 16 owner decisions required |
| `PHASE7_MIGRATION_PLAN.md` | Paths A (restore), B (adopt audit), C (hybrid) |
| `PHASE7_NEXT_STEPS.md` | Phase-1→2 handoff |
| `PHASE7_RESEARCH_QUESTIONS.md` | RQs for both directions |
| `PHASE7_RESEARCH_HISTORY.md` | Version history summary |
| `PHASE7_METHODOLOGY.md` | Methods + reproducibility |
| `PHASE7_EXPERIMENT_REGISTER.md` | Run register summary |
| `PHASE7_DATA_PROVENANCE.md` | Provenance summary table |
| `PHASE7_FAILURE_LOG.md` | 14 failures (Phase A + B) |
| `PHASE7_DECISION_LOG.md` | 11 decisions (D1–D11) |
| `PHASE7_LITERATURE_REVIEW.md` | Benchmark / distractor / bias / judge / low-resource refs |

## Headline findings
1. **Two incompatible narratives** coexist: May paper draft (benchmark, 86.8%/62.5%) vs July README/paper (v68 audit, HCW 27.8%).
2. **v68 is the verified production dataset:** 180 MCQs ($0.85, seed 20260615), 720 votes (0 missing), 4/6 gates failed. v69 never run; v70 halted at $0.42.
3. **Original direction was invalidated** May 18 (S2 construct validity: 62.5% mixes 24.9% real-paraphrase < random + high fallback).
4. **Yoruba copyright exposure** is unresolved: 60 Yoruba rows in v68 CSV despite "exclude pending approval"; ISBN `0-8032-3576-3` vs `978-0-8032-1843-7` conflict.
5. **EACL 2027 ARR submission status unconfirmed** (Aug 3 2026 deadline).

## Verification (read-only, no API)
```bash
pytest tests/ -v
python kaggle/run_logs/v68/openrouter_pilot1_test_output/analyze_v68.py
```
