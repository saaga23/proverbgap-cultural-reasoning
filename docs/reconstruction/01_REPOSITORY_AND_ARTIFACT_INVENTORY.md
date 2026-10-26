# Phase 1 — Document 01: Repository & Artifact Inventory

**Status:** Completed (read-only inspection)
**Purpose:** Orienting map of every artifact that bears on (a) the original ProverbGap research direction (May 2026) and (b) the later shortcut-audit reframing (June–July 2026). Paths are relative to repo root.
**Source of truth marker:** `docs/RESEARCH_HISTORY_AND_README_AUDIT.md` ("claims audit + evidence file index") and `README.md` (authoritative for v68 numbers).

---

## A. Top-level layout

| Path | Contents | Notes |
|---|---|---|
| `README.md` | Current (shortcut-audit) framing. Authoritative v68 numbers (180 MCQs, $0.85, HCW 27.8%). | Reconciled vs. original claims in §C. |
| `kilo.json` | Kilo agent config. | Not analysis-relevant. |
| `LICENSE` | MIT for code. Data licensing BLOCKED pending provenance review. | See §E. |
| `AGENTS.md`, `.kilo/` | Agent config. | Not analysis-relevant. |
| `docs/` | Research docs incl. original paper draft and reconciliation. | Core evidence dir. |
| `kaggle/` | All Kaggle-produced artifacts (legacy Groq + OpenRouter). | Primary evidence archive. |
| `actual_data/` | Curated proverbs (EN/AR/YO), 3 cleaned CSVs. | See §E, licensing conflict. |
| `.archive/` | Frozen June 19 2026 snapshot: code, docs, data, memory. | Original pipeline source. |
| `src/` | Active generation code (OpenRouter v68+). | See §D. |
| `tests/` | pytest suite. | `test_v68_metrics.py` key for v68. |
| `data/production/` | Frozen paper-first outputs (v68 audit gate set, human-validation sample). | See §G. |
| `paper/` | EACL 2027 draft + tables. | Current paper framing. |

---

## B. `docs/` directory (key evidence)

| File | Role | Original / Audit |
|---|---|---|
| `ProverbGap_Paper_Draft.md` | **Original paper draft v1.0, May 2026.** S1 86.8% vs S2 62.5% @ N=150. MCQ-only with FiB/Generation as future work §7.3/7.4. 3 languages (EN/AR/YO). | ORIGINAL |
| `ProverbGap_Reframed_Title_Abstract.md` | July 2026 EACL 2027 reframing (shortcut-audit). | AUDIT |
| `gap_liability_analysis_2026-07-10.md` | Flags inconsistency: paper claims 2,313 MCQs / 86.8%-62.5% vs v68 production 180 MCQs. | AUDIT |
| `EXECUTION_ITINERARY_2026-07-10.md` | EACL 2027 ARR execution plan (budget exhausted, human-validation planned-only). | AUDIT |
| `RESEARCH_HISTORY_AND_README_AUDIT.md` | Claims audit + evidence file index. | AUDIT |
| `RESEARCH_OVERVIEW.md` (if present) | See §Phase-7. | — |
| `DATA_PROVENANCE_TEMPLATE.md` | All three language sources + liability notes. | ORIGINAL→AUDIT |

**Original-direction evidence (May 2026):** `ProverbGap_Paper_Draft.md` §1–8, §5 Results (S1 86.8%, S2 62.5%), §3 Data (EN/AR/YO used; FR/DE/ES excluded "insufficient sample size"), §4 Methodology (S1 negative sampling, S2 qwen3-32b cross-family paraphrase), §7 Future Work (FiB §7.3, Generation §7.4 — *future tense*).

---

## C. Conflicts between original claims and current state

| Claim (original) | Current reality (v68+) | Resolution status |
|---|---|---|
| "6 languages, two tasks (literal/cultural), three formats (MCQ/FiB/Generation)" (RESEARCH_HISTORY v4.3.6) | May paper draft v1.0: only 3 languages (EN/AR/YO) benchmarked; FiB & Generation described as **planned future work** (§7.3–7.4) | **CONFLICT.** Legacy history doc over-claims; paper draft is contemporaneous authority. FiB/Generation outputs (16,439 / 25,190 rows per memory graph) appear to be a *later* exploration (post-May-18 thesis invalidation). |
| N=150 pilot, 300 MCQs, 1,500 evals, S1 86.8% / S2 62.5% | v68 N=5 smoke test: 180 MCQs, $0.85 | **Different experiments.** May pilot (Groq) ≠ v68 OpenRouter. |
| S2 62.5% difficulty | v68 "HCW 27.8%" blind-audit framing | **Reframed.** Original "accuracy" metric replaced by shortcut-audit HCW/consensus gates. |
| `main_results_table.csv` shows S1 14.7%, S2 0.0% | Deprecated v4.1 scale-readiness report (Groq corruption, June 13 note) | **Stale artifact.** Do not cite. |

---

## D. `src/generation/` — active code

| File | Role |
|---|---|
| `openrouter_pilot_distractor_generation_test_nano_opus.py` | v68/v69/v70 implementation. Config flag `USE_LLM_FALLBACK` gates `generate_llm_fallback_distractor()` (openai/gpt-4.1-nano). v68 ran `False`; v69/v70 were to run `True`. |
| `src/generation/` (other files) | Helper modules (prompts, sanitizers, audit committee). |

**Key config evidence:** v68 `pilot1_test_summary.json` → `substitutions = {"generators":[],"auditors":[]}` → 0 fallback invocations → `USE_LLM_FALLBACK=False` confirmed in production data.

---

## E. `actual_data/` — curations (licensing BLOCKED)

| File | Lang | Proverbs | License status |
|---|---|---|---|
| `English_cleaned.csv` | English | 2,278 | Public-domain scraped; URLs unrecovered; rights pending. |
| `Arabic_cleaned.csv` | Arabic (MSA) | 913 | MID-prefix academic dataset; source unidentified; review. |
| `Yoruba_cleaned.csv` | Yoruba | 3,931 | Owomoyela (2005), *Yoruba Proverbs*, UNL Press. **Copyrighted.** No permission. |
| `data_inventory.txt` | — | — | Contains literal "CATASTROPHIC DATA MISMATCH DISCOVERY" header. |
| `inventory.json` | — | — | Structured provenance + liability notes. |

**Copyright conflict:** README §8 cites Owomoyela ISBN `978-0-8032-1843-7`; paper draft §3.1 & memory graph cite `0-8032-3576-3`. Different editions/ISBNs to verify. Yoruba rows present in v68 CSV (60 rows) despite documentation claiming exclusion — unresolved data-rights exposure.

**Public release (per README §8):** English + Arabic only. Yoruba excluded pending owner approval, yet 60 Yoruba rows shipped in v68 CSV.

---

## F. `kaggle/` — Kaggle execution artifacts

| Path | Contents | Date |
|---|---|---|
| `kaggle_analysis/input/` | strategy1/strategy2 CSVs, evaluation_results.csv, evaluation_styles | Original Groq pilot |
| `kaggle_analysis/analysis_output/main_results_table.csv` | CORRUPTED S1 14.7% / S2 0.0% | June 8–13 (bug: answer-key shuffle) |
| `kaggle_analysis/analysis_output/report.html` | v4.1 dashboard | |
| `kaggle_analysis/reports/scale_readiness_report.md` | Deprecated v4.1 N=50 readiness (BLOCKERS) | 2026-06-19 |
| `kaggle_analysis/reports/unified_analysis_report.md` | | |
| `kaggle_analysis/reports/MENTOR_REPORT.md` | | |
| `kaggle/run_logs/v65/` | N=1 smoke (HCW 11.1%) | |
| `kaggle/run_logs/v66/` | N=1 regression (HCW 22.2%) | |
| `kaggle/run_logs/v67/` | Frozen baseline config | |
| `kaggle/run_logs/v68/` | **Completed & audited** — 180 MCQs, $0.85. `pilot1_test_summary.json`, `pilot1_test_generated_mcqs.csv` (180 rows), `pilot1_test_audit_results.csv` (720 votes), `v68_detailed_analysis_report.md`, figures (7). | 2026-06-22 |
| `kaggle/run_logs/v69/` | Planned LLM-fallback ablation. **NO CSVs / NO summary.json.** Only: analysis plan, report, comparison, checklist, py scripts. → **NEVER executed.** | |
| `kaggle/run_logs/v70/` | Partial run. `pool_state.json` (cost $0.42, `generation_done=False`, `audit_done=False`), 83-row CSV, prompt_variants. → **HALTED** at 11/15 hard-negative rows. | |

---

## G. `.archive/legacy_*_2026-06-19/` — frozen original

| Path | Contents |
|---|---|
| `legacy_code/kaggle_full_pipeline.py` (39KB) | Original 3-format (MCQ/FiB/Generation) + S1/S2 pipeline. |
| `legacy_code/pilot_v2.py` (59KB) | Pilot/evaluation runner (Groq). |
| `legacy_docs/` | ProverbGap_Status_Document.docx (Apr 24), Project_History.docx, plans. |
| `legacy_data/` | Snapshot of source data. |
| `memory_exports_2026-06-19/memory_proverbgap_filtered.json` | Entity graph: original Run-22 N=50 results, human-validation plan, competitor map. |

**Original pipeline grep evidence:** `create_project_history_doc.py:192` flags "benchmark only uses MCQ; competitors use MCQ+FiB+Generation" as a noted gap — corroborating FiB/Generation as planned-but-not-yet-implemented in the May draft.

---

## H. `paper/` — EACL 2027 draft

`paper/proverbgap_eacl2027.md`, `paper/tables/` (statistical tests, bootstrap CIs). Current submission-target = **EACL 2027 ARR, Aug 3 2026 deadline. Submission status UNCROSSED** (no paper ID / decision in repo).

---

## I. Quick test surface (pytest)

`pytest tests/ -v` — `test_v68_metrics.py`, `test_p0_filters.py`, `test_p1_nli.py`, `test_pilot1_nano_opus_local.py`, `test_pilot2_local.py`, `test_integration.py`. Re-runs compute v68 metrics from raw CSVs (no API calls).
