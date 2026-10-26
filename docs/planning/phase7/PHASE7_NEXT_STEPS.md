# Phase 7 — NEXT_STEPS

## Phase 1 is complete (inspection only — no code changed, no budget spent)
All Phase-1 evidence is in `docs/Phase1_Reconstruction/`:

| Doc | Covers |
|---|---|
| `01_REPOSITORY_AND_ARTIFACT_INVENTORY.md` | Repo map + evidence file index, conflicts table |
| `02_ORIGINAL_RESEARCH_RECONSTRUCTION.md` | Original May direction: S1/S2, 3 formats, 86.8%/62.5% |
| `03_CHRONOLOGICAL_RESEARCH_TIMELINE.md` | Full timeline + 4 pivots + decision log |
| `04_EXPERIMENT_REGISTER.md` | v1–v4.3.4 + v65–v70 register |
| `05_EVALUATION_METHODS_RECONSTRUCTION.md` | Original vs v68 metrics; S2 validity issue |
| `06_DATASET_PROVENANCE_AND_LINEAGE.md` | 6→3 langs, copyright, ISBN conflict, Yoruba exposure |
| `07_MODEL_AND_EVALUATION_HISTORY.md` | Rosters, provider migration, failures, competitors |
| `08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md` | Original↔v68 mapping, pivot chain, decision fork |
| `PHASE7_RESEARCH_OVERVIEW.md` | One-paragraph canonical overview |
| `PHASE7_CURRENT_STATE.md` | Frozen/verified/blocked status |
| `PHASE7_OPEN_QUESTIONS.md` | 16 owner decisions required |
| `PHASE7_MIGRATION_PLAN.md` | Paths A/B/C with pre-conditions |

## Phase 2 cannot start until owner resolves
These are **not** code tasks; they are owner decisions (see `PHASE7_OPEN_QUESTIONS.md`):

1. **Pick a path** (A restore-benchmark / B adopt-audit / C hybrid) — `PHASE7_MIGRATION_PLAN.md`.
2. **Resolve Yoruba copyright** (ISBN conflict; 60 rows in v68 CSV) — `06_` §3.
3. **Decide on OpenRouter budget** (v69 ~$1; human validation $200–300).
4. **Confirm EACL 2027 ARR submission status** (Aug 3 2026 deadline; unconfirmed).
5. **Resolve S2 construct validity** if Path A/C — `05_` §2.

## If owner picks Path B (lowest-friction, no budget)
Ready to execute immediately:
- [ ] Run 60-item human validation sample → ground HCW gate (README §9).
- [ ] `pytest tests/ -v` (already green; add variant-HCW tests per README §10).
- [ ] Freeze `paper/proverbgap_eacl2027.md` tables from `kaggle/run_logs/v68/`.
- [ ] Reconcile README §8 Yoruba exposure note with actual CSV.

## If owner picks Path A (restore original)
Ready to execute after decisions 1–3:
- [ ] Re-validate S1 key integrity; restart v69 ablation.
- [ ] Locate or regenerate FiB/Generation artifacts.
- [ ] Recover EN/AR provenance + Yoruba ISBN.
- [ ] Scale v70 → N=15 → N=700.

## Repo hygiene (safe to do now, no owner decision)
- [ ] Add deprecation header to `kaggle/kaggle_analysis/analysis_output/main_results_table.csv` (corrupted 14.7%/0.0%; see `04_` §Phase A v4.1).
- [ ] Confirm `.archive/` is read-only (git tag or note).
- [ ] Add `docs/Phase1_Reconstruction/README.md` index linking all docs.

## Verification command (Phase 1 — re-run to confirm reproducibility)
```bash
pytest tests/ -v
python kaggle/run_logs/v68/openrouter_pilot1_test_output/analyze_v68.py
```
Both read-only, no API.
