# Phase 7 — CURRENT_STATE

## What is frozen / verified (read-only)
| Artifact | State | Evidence |
|---|---|---|
| v68 dataset (180 MCQs) | ✅ Complete + audited | `pilot1_test_generated_mcqs.csv` (180 rows incl. 60 Yoruba), `pilot1_test_audit_results.csv` (720 votes, 0 missing, 0 substitutions), `pilot1_test_summary.json` |
| v68 metrics (4/6 gates fail) | ✅ Recomputed from raw CSVs | HCW 27.8%, perfect-consensus 41.7%, partial+fallback 43.9%, hard-fallback 16.1%, dup=0, key 45/45/45/45; χ² position p=0.322 |
| v69 LLM-fallback ablation | ❌ **Never executed** | `run_logs/v69/` has no CSV/summary; only analysis scripts & templates (TBD blanks) |
| v70 LLM-fallback run | ⛔ **Halted** | 83/180 rows, $0.42, `generation_done=False`, `audit_done=False`, OpenRouter 403 |
| Human validation (60-item sample) | 📋 Prepared, not started | `data/production/paper_first_outputs_2026-06-22_10-42-02/human_validation_sample_60.csv`; 9 annotators (3/lang) recruitment pending budget |
| EACL 2027 ARR submission | ❓ Unconfirmed | No paper ID / decision; deadline Aug 3 2026 (past per session date) |
| Reproducibility (pytest) | ✅ Green, no-API | `pytest tests/ -v` incl. `test_v68_metrics.py` |

## What is BLOCKED / at risk
1. **Yoruba copyright exposure** — 60 Yoruba MCQ rows shipped in v68 CSV despite "exclude pending owner approval" (README §8). ISBN conflict (0-8032-3576-3 vs 978-0-8032-1843-7) blocks clearance.
2. **S2 construct validity** — original 62.5% mixes 24.9% real-paraphrase (below random) + high fallback. Not resolved before pivot.
3. **OpenRouter budget** — exhausted; v69/v70 cannot restart without new credits.
4. **Human validation** — depends on external funding (~$200–300).
5. **Submission status** — EACL 2027 ARR Aug 3 2026 deadline; unconfirmed.

## Current repo framing (live)
- `README.md` reports **v68 only** (audits out the May numbers); mentions S1/S2 only as historical context.
- `docs/ProverbGap_Paper_Draft.md` (May) coexists with `paper/proverbgap_eacl2027.md` (July reframing) — **two narratives**.
- `docs/gap_liability_analysis_2026-07-10.md` explicitly flags the 2,313-MCQ/86.8% vs 180-MCQ inconsistency and recommends not carrying forward old numbers.

## Test surface (verified working)
`pytest tests/ -v` → `test_v68_metrics.py`, `test_p0_filters.py`, `test_p1_nli.py`, `test_pilot1_nano_opus_local.py`, `test_pilot2_local.py`, `test_integration.py`.
