# Local ↔ Kaggle Artifact Crosswalk

**Audit date:** 2026-10-26. Old repo = `saaga23/proverb_mcq` (local working tree inspected read-only). Kaggle account: `abrahamsunday123` (authenticated via existing local `kaggle.json`; **CLI was not installed** and was installed locally by this audit — `python -m kaggle`). Only **metadata/output-download** calls were made; **no new kernel executions, no credential contents read or printed**.

Execution levels used: **L1** file exists · **L2** saved outputs present · **L3** executed (execution metadata/outputs) · **L4** execution corroborated by logs/run records · **L5** independently reproduced.

---

## 1. Kaggle kernels (verified via API, 2026-10-26)

| Kernel | Title | Last run (UTC) | Status | Local counterpart | Output recovery |
|---|---|---|---|---|---|
| `proverbgap` | proverbgap | 2026-04-12 | — | `.archive/legacy_code_2026-06-19/proverbgap-mcq.ipynb`? | not attempted (earliest prototype) |
| `proverbgap-generation` | Proverbgap Generation | 2026-05-19 19:52 | **COMPLETE** | `.archive/legacy_code_2026-06-19/` generation notebooks | ✅ `pilot_results.csv` (2,160×23), `retry_queue.jsonl` (483), 5.5 MB log — downloaded to temp |
| `proverb-gap-fill-in-the-blank` | proverb gap fill in the blank | 2026-05-19 20:28 | **COMPLETE** | `.archive/legacy_code_2026-06-19/` FiB notebooks | ✅ `nb_pilot_30_results.csv` (30×26), `pilot_checkpoint.csv` — downloaded to temp |
| `proverbgap-mcq` | ProverbGap -- MCQ | 2026-05-21 20:10 | COMPLETE (but the run in the retrieved log **failed at startup**: no API keys, `original-data` dataset not attached) | `.archive/legacy_code_2026-06-19/proverbgap_kaggle_final.ipynb` family | ⚠️ log only (4.8 KB); the successful **May 23 v4.3.4 run is an earlier kernel version**, not reachable via CLI output download |
| `mcq-pass-shortcut` | MCQ_pass_shortcut | 2026-06-22 02:03 | **ERROR** (final version; consistent with the v70 budget halt) | `kaggle/kaggle_analysis/Last_run/mcq-pass-shortcut.ipynb` (3 cells, **all with saved outputs + execution counts** — executed) + `kaggle/run_logs/v59…v70/` per-version outputs | local v59–v70 outputs already present; no re-download needed |

**Version-numbering caveat:** v59–v70 are **versions of the same notebook** (`mcq-pass-shortcut`), not separate kernels. Kaggle records only the latest run per kernel (June 22 02:03, ERROR). v69 = saved-but-never-executed version.

## 2. Kaggle datasets (verified via API)

| Dataset | Updated | Size | Role | Notes |
|---|---|---|---|---|
| `proverbeval-data` | 2026-03-09 | 663 KB | source collection start | ProverbEval-derived |
| `proverb2` | 2026-03-10 | 613 KB | collection | |
| `proverbeval-clean-data` | 2026-03-11 | 766 KB | collection | |
| `proverb-all` | 2026-03-19 | 647 KB | collection | |
| `proverbgap-checkpoint-v` | 2026-04-27 | 8.4 MB | working checkpoint | |
| `original-data` | 2026-05-16 | 566 KB | **kernel input data** | contains `English/Arabic/Yoruba/French/German/Spanish_cleaned.csv` (file list verified) |
| `openrouter-key-mcq` | 2026-06-20 | — | **credential transport** | contains `OPENROUTER_API_KEY.txt` (74 B) — **private** dataset; do not download/commit; security note in `docs/audit/EVIDENCE_DISCREPANCIES.md` |
| `dr-ehsan-openrouter-key` | 2026-10-21 | 217 B | credential transport (different project) | out of scope; flagged |

## 3. Local artifacts (old repo) ↔ experiments

| Artifact (old repo path) | Type | Executed? | Experiment | Agrees with register? |
|---|---|---|---|---|
| `kaggle/run_logs/v59…v67/*/pilot1_test_*.csv|*.json` | raw output + config | yes (per-run outputs) | OR-V59…V67 | yes |
| `kaggle/run_logs/v68/openrouter_pilot1_test_output/*` | raw output | yes | AUDIT-V68 | yes — metrics recomputed, exact match |
| `kaggle/run_logs/v68/table_*.csv` (18 files) | analysis | yes (scripts in `analysis_scripts/`) | AUDIT-V68 + IAA-PROXY | yes |
| `kaggle/run_logs/v68/reproducibility/openrouter_catalog_snapshot_2026-06-22.json` | config evidence | n/a | AUDIT-V68 | yes |
| `kaggle/run_logs/v70/*` | partial output | halted | V70-HALT | yes (83 rows, $0.42, mtime 2026-06-22 09:10 local) |
| `kaggle/kaggle_analysis/input/evaluation_results.csv` | raw output (June failed run) | yes | MCQ-JUNE-RUN | **corrected register**: file = June run, not the May pilot (Phase 1 misattributed it) |
| `kaggle/kaggle_analysis/input/mcqs_strategy1/2.csv` | task data | yes (June run inputs; 150+150) | MCQ-JUNE-RUN (and structurally the May design) | yes |
| `kaggle/kaggle_analysis/input/encoder_results.csv` | raw output | yes | MCQ-JUNE-RUN | yes |
| `kaggle/kaggle_analysis/s2_semantic_scores_v2_baseline.csv` | derived diagnostics | yes | MCQ-JUNE-RUN / S2 validity | schema verified; semantics of `semantic_max_sim` inferred |
| `kaggle/kaggle_analysis/agents/*.py`, `analyze_kaggle_run.py` | analysis code | n/a | MCQ-JUNE-RUN analysis | yes |
| `kaggle/kaggle_analysis/Last_run/mcq-pass-shortcut.ipynb` | notebook w/ saved outputs (3/3 cells) | **L3 executed** | AUDIT-V68 era | yes |
| `kaggle/kaggle_analysis/Last_run/{last_run_latest,pilot 1,results_extracted,last_run_june_19th}/` | downloaded Kaggle results (4 snapshots) | yes | OR-V59…V68 | yes; multiple copies of similar outputs — distinguish by folder |
| `src/generation/openrouter_pilot_distractor_generation_test_nano_opus.ipynb` | notebook | **code-only** (0 outputs, 0 exec counts) | v68/v69/v70 source | yes |
| `src/evaluation/openrouter_pilot_s1_s2_evaluator.ipynb` | notebook | **code-only** | May S1/S2 evaluation design | yes |
| `data/production/paper_first_analysis_2026-06-22_10-42-02.ipynb` | analysis notebook | **code-only** (0 outputs) | AUDIT-V68 analysis | code present; execution unverified locally (tables exist as CSV) |
| `data/production/paper_first_outputs_2026-06-22_10-42-02/*` (7 tables + `human_validation_sample_60.csv`) | analysis + sampling | yes | AUDIT-V68 + HUMAN-VAL | yes |
| `annotation_app/**` (Next.js/Supabase/Playwright, `.vercel/`, `ANNOTATOR_ONBOARDING.md`) | application | built + E2E-tested; **no annotation records** | HUMAN-VAL | yes |
| `submission_package_2026-08-02/**` (paper, checklist, 18 tables, figures, lockfile+hashes) | package | n/a | SUB-PKG | yes |
| `model_cache/**` (NLI cross-encoder, MiniLM paraphrase, 4 encoder tokenizers) | model caches | n/a | v68 filters + encoder baselines | consistent |
| `.archive/legacy_code_2026-06-19/*.ipynb` (9 notebooks) | legacy code | **code-only** (0 outputs) | early Groq pipeline | yes |
| `.archive/legacy_docs_2026-06-19/ProverbGap_Status_Document.docx`, `ProverbGap_MCQ_Project_History.docx` | contemporaneous docs | n/a | all | yes (confirmed present) |
| `kaggle/kaggle_upload_pilot1_test/*` (kernel-metadata.json + notebook) | upload package | n/a | AUDIT-V68 | yes |

## 4. Access limitations & owner actions

1. **May v4.3.4 primary outputs** (evaluation_results/encoder_results/mcqs CSVs + `FINAL_AUDIT_v434.md` + execution log): overwritten locally; recoverable only from the `proverbgap-mcq` kernel's **version history via the Kaggle web UI** (CLI exposes only the latest version). Owner action: export the 2026-05-23 version's output.
2. **FiB/Generation at scale**: only the kernels' small pilots are retrievable; if larger runs existed, they are not in kernel outputs — check Kaggle working-directory snapshots / `proverbgap-checkpoint-v` dataset contents (8.4 MB, uninspected).
3. **Supabase annotation backend**: no local records; owner must check the Supabase project for submitted annotations.
4. **`dr-ehsan-openrouter-key` and other credential datasets**: out of scope; owner should review their existence/permissions.
5. **Kaggle CLI**: was not installed on this machine; installed locally during this audit (`python -m kaggle`). No new executions launched.
