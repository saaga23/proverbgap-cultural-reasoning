# Experiment Register — Full Historical Research Program

**Status vocabulary (do not mix):** `PLANNED-NEVER-RUN` · `CODE-PRESENT-EXEC-UNVERIFIED` · `STARTED-INCOMPLETE` · `COMPLETED-WITH-OUTPUTS` · `COMPLETED-ANALYSIS-MISSING` · `RESULTS-REPRODUCED` · `FAILED-OR-INVALIDATED` · `UNRESOLVED`.

**Evidence levels:** 1 = primary data/output · 2 = logs/metadata · 3 = run code/config · 4 = reproducible analysis · 5 = contemporaneous verification notes · 6 = later summaries · 7 = prose/recollection.

All artifact paths are in the source repository `saaga23/proverb_mcq`. Dates are as recorded by artifacts (Kaggle metadata, file mtimes, document headers). "Recomputed" = recalculated from primary data during this audit (2026-10-26).

---

## 0. Register index

| ID | Experiment | Window | Status | Best evidence level |
|---|---|---|---|---|
| DATA-COLLECT | Proverb data collection & cleaning | Mar–May 2026 | COMPLETED-WITH-OUTPUTS (6 languages) | 1 |
| ER-A1 | April-era MCQ generation runs (large batches) | Apr–May 2026 (first committed 2026-05-16) | COMPLETED-WITH-OUTPUTS (recovered from Git history 2026-10-26) | 1 |
| MCQ-PILOT | v4.3.4 N=150 S1/S2 pilot (May) | 2026-05-23 | COMPLETED-WITH-OUTPUTS; **primary artifacts since overwritten** — figures verified at the time (level 5), not locally reproducible now | 5 |
| MCQ-PILOT-CHECK | Paper verification suite (3 reports) | 2026-05-24 | COMPLETED-WITH-OUTPUTS | 5 |
| FIB-PILOT | Fill-in-the-blank 30-item pilot | 2026-05-19 (Kaggle, COMPLETE) | COMPLETED-WITH-OUTPUTS (recovered) | 1 |
| GEN-PILOT | Generation/explanation pilot | 2026-05-19 (Kaggle, COMPLETE) | COMPLETED-WITH-OUTPUTS (recovered); **analysis missing** | 1 |
| MCQ-JUNE-RUN | June Kaggle Groq re-run | 2026-06-08/09 | FAILED-OR-INVALIDATED (API meltdown + answer-key bug) | 1 |
| OR-V59…V67 | OpenRouter iteration runs v59–v67 | 2026-06 (pre-v68) | COMPLETED-WITH-OUTPUTS (smoke/regression tests) | 1 |
| AUDIT-V68 | v68 N=5 production audit run | 2026-06-22 00:30Z | COMPLETED-WITH-OUTPUTS; **RESULTS-REPRODUCED** | 1 |
| ABL-V69 | v69 LLM-fallback ablation | designed 2026-06-22 | PLANNED-NEVER-RUN | 3 (design doc) |
| V70-HALT | v70 LLM-fallback attempt | 2026-06-22 ~09:10 local | STARTED-INCOMPLETE (83/180 rows, $0.42, OpenRouter 403) | 1 |
| IAA-PROXY | 7-model LLM-proxy IAA on 60 items | 2026-07-08 | COMPLETED-WITH-OUTPUTS | 1 |
| HUMAN-VAL | Human validation (60 + 30 samples; annotation app) | prepared 2026-06-22; app built ~Jun–Jul | PLANNED-NEVER-RUN (sampling + tooling done; zero annotations) | 1 |
| SUB-PKG | EACL 2027 ARR submission package | 2026-08-02 | COMPLETED-WITH-OUTPUTS (package); submission itself UNRESOLVED | 2 |

---

## 1. DATA-COLLECT — proverb data collection (Mar–May 2026)

- **Objective:** assemble culturally grounded proverbs with translations and cultural meanings.
- **Artifacts:** Kaggle datasets `proverbeval-data` (Mar 9), `proverb2` (Mar 10), `proverbeval-clean-data` (Mar 11), `proverb-all` (Mar 19), `proverbgap-checkpoint-v` (Apr 27, 8.4 MB), `original-data` (May 16, 566 KB — contains all six cleaned CSVs, verified via Kaggle file list). Local: `actual_data/*_cleaned.csv`.
- **Verified counts:** EN 2,278 · AR 913 · YO 3,974 (+ FR/DE/ES present on Kaggle, counts unverified).
- **Hypotheses/quality gates:** none recorded at this stage. **Known defects:** Arabic gold-meaning errors (~4% of a 50-item sample, per June 15 history doc); Yoruba QA_Flag/Comments columns exist (semantics unenumerated); Yoruba count conflict 3,974 vs 3,931 (paper).
- **Next-decision influence:** enabled all three task tracks; the "7,172 proverbs" paper claim traces to this collection but is arithmetic-inconsistent (sum = 7,488; see D-2).
- **Cultural-reasoning relevance:** core. **Shortcut-audit relevance:** shared source.

## 2. MCQ-PILOT — v4.3.4 N=150 S1/S2 pilot (2026-05-23, run `run_20260523_224443`)

- **Research question:** do models show a measurable difficulty drop from S1 (same-language negative-sampling distractors) to S2 (cross-family qwen3-32b paraphrase distractors)? The drop = the original "cultural-reasoning gap" operationalization.
- **Data:** 50 proverbs/language × 3 languages; 300 MCQs (150 S1 + 150 S2); committee `meta/llama-4-maverick-17b-128e-instruct` (NVIDIA) + `allam-2-7b` (Groq); 3 styles (zero-shot/CoT/few-shot); CoT skipped for maverick; 4 encoder baselines (mBERT, XLM-R, AraBERT, AfriBERTa); position mitigation = per-model seeded shuffle.
- **Acceptance criteria:** implicit — significant S1>S2 gap + acceptable S2 fallback (<~20%).
- **Execution:** COMPLETED (May 23). **Verification at the time (May 24, `docs/verification_cross.md`, level 5):** S1 86.8% = **651/750**; S2 strict 62.5% = **369/590**; S2 fallback 32/150 = 21.3%; per-language S1 97.6/92.8/70.0, S2 strict 71.3/65.5/46.2 (EN/AR/YO); per-model S1 92.7 (maverick) / 82.9 (allam); McNemar χ²=131.3 p<0.001; encoders 29–36%.
- **What S1/S2 asked the model:** given proverb + question + 4 English meaning options, choose the correct meaning letter. S1's wrong options are other proverbs' meanings; S2's are LLM paraphrases with subtle shifts.
- **Current reproducibility:** **NOT locally reproducible** — `kaggle_analysis/Last_run/` now holds June-run files; `FINAL_AUDIT_v434.md`, `memory.md`, `original_data/`, `GENERATION_QUALITY_REPORT.md` are absent from the working tree. The May kernel's *latest* version re-run (May 21) failed at startup (no keys/missing dataset); the successful May 23 run is an earlier Kaggle kernel version not exposed by the CLI (needs web-UI version export). Status: **COMPLETED-WITH-OUTPUTS (historically verified), RESULTS-NOT-REPRODUCIBLE-LOCALLY**.
- **Audit update (2026-10-26):** the old repository's Git history was mined as a recovery route — the May evaluation/encoder files were **never committed** (only the June failed run, first committed 2026-06-15), so Git recovery is impossible; the Kaggle web-UI version export remains the only path. The McNemar claim (χ²=131.3, p<0.001) could not be reconstructed: the paired contingency table, the matched subset behind the differing denominators (750 vs 590), and the test variant are undocumented. A two-proportion χ² on the verified marginals gives 106.9 — plausible but not the reported statistic (see decision memo §A3). The "24.9% real-paraphrase" claim is **misattributed** to this pilot: it belongs to the N=50-era Run 22/23 and is internally inconsistent (memo §A4).
- **Validity concerns:** (a) the **S2 construct-validity dispute** — the June 15 history doc and memory export report a June 4 audit finding that S2's 62.5% mixes *real-paraphrase items (24.9%, below the 25% random baseline)* with high-scoring placeholder-fallback items; **no surviving artifact computes 24.9%** — the claim traces only to narrative docs (level 6) → `UNRESOLVED`; (b) cross-verification found the paper's consensus table mislabeled "any unanimous" as "unanimous correct" (true S2 unanimous-wrong = 22.7%); (c) abstract conflated earlier-iteration failures with the pilot.
- **Influence:** the construct-validity + scaling concerns fed the May 18 thesis invalidation and the June pivot to distractor-quality auditing.

## 3. MCQ-PILOT-CHECK — verification suite (2026-05-24)

Three reports in old-repo `docs/`: `verification_paper.md`, `verification_mentor.md`, `verification_cross.md`. Verified all paper numbers against then-current CSVs/log; found the consensus-table mislabel, the 7,172-vs-7,488 arithmetic error, placeholder `original_data/` (~669 rows), the allam error-excluded leakage result (S1 98.9% = 373/377, S2 74.5% = 225/302, drop 24.4pp → would trigger the HIGH-leakage flag), and degenerate p=1.000 position tests. **Status: COMPLETED-WITH-OUTPUTS.** These reports are now the best surviving evidence for the May pilot.

## 4. FIB-PILOT — fill-in-the-blank pilot (2026-05-19, Kaggle kernel `proverb-gap-fill-in-the-blank`, status COMPLETE)

- **Task:** cloze on the proverb — model completes the masked word (`gold_word`) in `displayed_proverb` under 3 conditions (gold word / `paraphrase_ok` / `sham_proverb`); metrics EM, NEM (normalized EM), ChrF, latency per condition.
- **Data:** 30 items (`nb_pilot_30_results.csv`, recovered from Kaggle output 2026-10-26).
- **Execution:** COMPLETED-WITH-OUTPUTS. **Analysis:** none found (no summary/figures).
- **Significance:** proves the FiB format was actually implemented and run — the Phase 1 dossier's "planned only" framing was **wrong** (it followed the stale May draft). The "16,439 rows" memory figure is unverified; the surviving pilot is 30 items.
- **Influence:** set aside after May 18 thesis invalidation; remains the most direct format for testing cultural recall.
- **Audit update (2026-10-26):** notebook source pulled from Kaggle and inspected. The three conditions are: **A** = original proverb context, **B** = paraphrased context, **C** = *sham-proverb control* (a genuine design strength). Recomputed descriptives: all 90 predictions extracted via last-line fallback (`FALLBACK_LINE` — a parser weakness, not a run failure); mean EM A 0.133 / B 0.100 / **C 0.133** — real-context and sham-context performance identical at this scale. The pilot therefore establishes **feasibility only**, with no cultural signal at n=30; a future run should fix extraction and pre-register "A ≫ C" as the validity signal. (Decision memo §B1.)

## 5. GEN-PILOT — generation/explanation pilot (2026-05-19, Kaggle kernel `proverbgap-generation`, status COMPLETE)

- **Task:** model generates the proverb's explanation; scored vs gold with BLEU, ChrF, embedding `semantic_sim`; `contains_gold` flags gold-copying; `retry_queue.jsonl` (483 retries).
- **Data/output:** `pilot_results.csv` — **2,160 generation attempts** × 23 cols, multiple models/providers/languages/strategies (recovered 2026-10-26).
- **Status:** COMPLETED-WITH-OUTPUTS; **ANALYSIS-MISSING** (no aggregate table/figures found).
- **Known claim:** memory export asserts "DeepSeek-R1 100% gold-copying" and "25,190 clean Task A rows" — neither verified against this artifact (row count here = 2,160). See D-6.
- **Influence:** supported the May 18 invalidation narrative (models copying gold explanations instead of explaining), but the quantitative basis is currently unverifiable → recompute from `pilot_results.csv` in Phase 2 if the question is revived.
- **Audit update (2026-10-26):** recomputed from the recovered artifact (`supporting/recompute_checks.py`): 2,160 attempts = **90 unique proverbs (30/language) × 6 models × 2 tasks × 2 strategies**; SUCCESS 1,677/2,160 (77.6%); the 483 failures match `retry_queue.jsonl` (queued, never executed). Per-model success: Gemma-4-31B 96.9%, Nemotron-120B 96.4%, Maverick 93.6%, LLaMA-3.3-70B 72.5%, LLaMA-3.1-8B 71.7%, **Qwen3-32B 34.7%**. **Gold-copying among successes = 3.7–11.2% per model** (max: LLaMA-3.1-8B 11.2%). The memory claims "DeepSeek-R1 100% gold copying" (model absent from the run) and "25,190 clean Task A rows" (2,160 here) are **Contradicted** — see D-18. Status upgraded to: primary evidence recovered **and descriptively analyzed**; conclusions about cultural reasoning still require a scoring rubric and human validation. (Decision memo §B2.)

## 6. MCQ-JUNE-RUN — June Kaggle Groq re-run (2026-06-08/09)

- **Setup:** 8 Groq keys, committee `llama-3.3-70b-versatile` + `llama-4-maverick` + `allam-2-7b`; N=50/lang; 2,700 evaluations attempted.
- **Execution:** FAILED-OR-INVALIDATED. Recomputed from the surviving `evaluation_results.csv`: **2,440/2,700 rows error** (Groq 429s, "All providers failed"); only 260 valid rows, all S1 (76.2% correct among them); **all 1,350 S2 rows failed**. The "S1 14.7% / S2 0.0%" deprecated figures = counting failures as misses (198/1350). Additionally the June 13 note records an S1 answer-key shuffle bug (saved MCQ file ≠ evaluation file).
- **Influence:** killed the Groq-based path → OpenRouter migration (June 15 plan).

## 7. OR-V59…V67 — OpenRouter pipeline iterations (June 2026)

- **Artifacts:** `kaggle/run_logs/v59, v60, v61, v63, v64, v65, v66, v67` each with full output sets (audit_results, generated_mcqs, human_annotation_sample, prompt_comparison, raw_outputs, summary.json, pool_state.json, prompt_variants.json). Note: **v62 has no run directory** — numbering is not continuous (UNRESOLVED: v62's fate unknown).
- **Roles:** v65/v66/v67 = N=1 smoke/regression tests during config freezing (v65 HCW 11.1%, v66 perfect-consensus 55.6% / HCW 22.2% per `v68_detailed_analysis_report.md` §2); earlier versions iterated prompts/filters. Detailed per-version diffs **not yet reconstructed** (would require diffing the summary.json files — Phase 2 candidate).
- **Status:** COMPLETED-WITH-OUTPUTS (individual runs); REGISTER-LEVEL DETAIL UNRESOLVED.

## 8. AUDIT-V68 — v68 production audit run (2026-06-22 00:30Z, seed 20260615)

- **Research question (shortcut track):** do generated distractors resist shortcuts? A blind 4-auditor committee sees **only the four options**; HCW (consensus ≥0.75 on the wrong answer) is the failure signal.
- **Design:** 15 proverbs (5/lang) × 4 variants × 3 generators = 180 MCQs; auditors llama-3.3-70b / mistral-small-3.2 / gemma-3-27b / deepseek-v3.2; `USE_LLM_FALLBACK=False` (corpus fallback); cost $0.8539/$5.00; 720 votes, 0 missing, 0 substitutions.
- **Gates:** hard-fallback<5% (got 16.1% ❌), partial+fallback<15% (43.9% ❌), HCW<10% (27.8% ❌), perfect-consensus<30% (41.7% ❌), duplicates=0 ✅, key balance 45/45/45/45 ✅.
- **Recomputed 2026-10-26 from `pilot1_test_audit_results.csv`** (unit: committee verdict): consensus accuracy **102/180 = 56.7%**; perfect consensus **75/180 = 41.7%**; HCW **50/180 = 27.8%**; per-language HCW EN 11/60 (18.3%), AR 19/60 (31.7%), YO 20/60 (33.3%); per-generator HCW gemma-4-31b-it 13/60 (21.7%), gemini-2.5-flash 19/60 (31.7%), qwen3.7-max 18/60 (30.0%); per-variant HCW hard-negative 11/45 (24.4%), length-locked 16/45 (35.6%), overgenerate-select 10/45 (22.2%), taxonomy-guided 13/45 (28.9%). Generation status: 101 generated / 50 partial / 29 length_fallback / 0 parse or hard fallback. All figures match the README/v68 report exactly → **RESULTS-REPRODUCED**.
- **Statistics:** pairwise McNemar (Holm) and Wilcoxon all null (`table_statistical_tests_corrected.csv`) — no significant variant/generator differences at this N.
- **Interpretation at the time:** corpus-fallback sampler is the bottleneck; do not scale. **Influence:** v69 ablation decision → budget halt → paper-first pivot.
- **Relevance to cultural-reasoning question:** indirect — it audits distractor quality, not model cultural understanding. It does NOT show that models do or don't understand cultural meaning.

## 9. ABL-V69 — LLM-fallback ablation (`PLANNED-NEVER-RUN`)

- **Design (documented, `v68_detailed_analysis_report.md` §7.2):** `N_PER_LANG=5`, `USE_LLM_FALLBACK=True`, fallback generator `openai/gpt-4.1-nano`, cost ≈$0.10–0.20 extra; gates HCW<15%, partial+fallback<30%, perfect-consensus ≤45%, cost<$1.50.
- **Evidence of non-execution:** `kaggle/run_logs/v69/` contains only analysis scripts/templates (no CSVs, no summary.json). v69 is a saved *notebook version* of `mcq-pass-shortcut`, never executed.

## 10. V70-HALT — LLM-fallback attempt (`STARTED-INCOMPLETE`)

- **Artifacts:** `kaggle/run_logs/v70/` — partial `pilot1_test_generated_mcqs.csv` (83 rows), `raw_outputs.csv`, `pool_state.json` (`cost_spent` 0.4201, `generation_done=False`, `audit_done=False`, `fallback=None`), log dated **2026-06-22 09:10 local**.
- **Status:** halted by OpenRouter 403 (budget limit) mid-generation; audit never started. Note: Phase 1 dated this June 26; file mtimes + Kaggle last-run (June 22 02:03 UTC, status ERROR) indicate **June 22** — see D-8.

## 11. IAA-PROXY — 7-model LLM-proxy inter-annotator agreement (2026-07-08)

- **Design:** 7 proxy models (Qwen2.5-7B, claude-3-haiku, DS-R1-Distill-Qwen-32B, gemini-2.5-flash, Llama-3.2-3B, Phi-3.5-mini, gpt-4o-mini) answer the 60-item sample blind; agreement computed between models.
- **Verified output:** `table_llm_proxy_iaa.csv` — Fleiss κ **0.4845**, mean pairwise Cohen κ **0.4846** (range 0.2952–0.7988), n=60 items × 7 models, source `iaa_report_20260708_121120.json`.
- **What it means (and not):** a calibration anchor for what *model* agreement looks like; **not** human agreement and not a substitute for human validation.

## 12. HUMAN-VAL — human validation (`PLANNED-NEVER-RUN`; tooling COMPLETED)

- Prepared: 60-item stratified sample (32 cols, no human columns) + 30-item v68 sample (human columns **0/30 filled** — verified).
- Tooling: `annotation_app/` (Next.js 16 + Supabase + Playwright; annotator flow = read proverb, choose A–D from English options, rate distractor plausibility 1–5, flag shortcuts; `ANNOTATOR_ONBOARDING.md`; Vercel deployment artifacts).
- **Execution:** zero annotation records found in the repository; whether the deployed app ever collected data requires Supabase access → owner action.

## 13. SUB-PKG — EACL 2027 ARR submission package (2026-08-02)

- **Contents (verified):** full paper draft (`proverbgap_eacl2027.md`, ~12,000 words), reviewer risk checklist (P0/P1/P2), provenance template, execution itinerary, budget-dependent Phase-3 plan, 18 tables, 4 figures, reproducibility lockfile + output hashes.
- **Status:** package COMPLETED-WITH-OUTPUTS; **actual ARR submission UNRESOLVED** (no submission record in either repo; deadline was Aug 3, 2026).

---

## 14. Metric definitions used above (plain English)

| Metric | Numerator / denominator | First defined |
|---|---|---|
| Strategy accuracy (May) | # correct letters / # valid (non-error) evaluations for that strategy | May pilot |
| S2 strict accuracy | same, restricted to MCQs whose distractors were real paraphrases (fallback=False) | May pilot |
| Consensus accuracy (v68) | # MCQs where committee majority = gold / 180 | v68 |
| Perfect consensus | # MCQs with all 4 auditors agreeing (frac = 1.0) / 180 | v68 |
| HCW | # MCQs with consensus_frac ≥ 0.75 AND consensus ≠ gold / 180 | v68 lineage (v65+) |
| Fallback rate | # MCQs using any corpus/placeholder replacement / total MCQs | May + v68 |
| EM / NEM / ChrF (FiB) | exact / normalized string match / character n-gram F-score vs gold word | FiB pilot |
| BLEU / ChrF / semantic_sim (Generation) | n-gram overlap / char n-gram F-score / embedding cosine vs gold explanation | Gen pilot |
| Fleiss κ / Cohen κ (IAA-PROXY) | standard multi-rater / pairwise agreement corrections | IAA-PROXY |

**Do not cross-use:** e.g., v68 HCW says nothing about whether models understand cultural meaning; the May S1/S2 gap is about option difficulty, not distractor-quality auditing.

---

## 15. ER-A1 — April-era MCQ generation runs (2026-04; first committed 2026-05-16, later removed from working tree)

- **What:** large MCQ generation batches predating the May pilot — `_unzipped/mcq_a_{zs,cot,cot_xl}_{language}.csv` recovered from the repository's first commit (`198253b`): **2,000 Yoruba** and **803 Arabic** rows × 22 columns (options, answer key, `raw_response`, and per-item quality scores `parse`, `complete`, `len_r`, `distinct`, `quality`), plus `_all_mcq_analysis.txt` with per-language descriptive statistics. Six languages appear in the file set (FR/DE/ES included).
- **Status:** COMPLETED-WITH-OUTPUTS (generation + quality scoring); these are *generated MCQs with item-quality metrics*, not model-accuracy results.
- **Significance for the research question:** `cultural_context_available = False` throughout — the earliest items were built from translations **without cultural-context fields**, i.e., before the cultural-meaning representation existed. This makes ER-A1 the earliest documented state of the benchmark concept and a useful baseline for measuring how the item design evolved.
- **Evidence quality:** schema and counts **Verified** (files read from Git history); generation code for this era not yet located — provenance of the quality metrics **Inferred**.
- **Caveat:** these files contain proverb texts and meanings and remain in the **public** repository's Git history — flagged as a redistribution-rights exposure in `DATA_RIGHTS_AND_PROVENANCE.md` §3.

## 16. Claims reclassification (audit of 2026-10-26)

Consolidated status changes following the evidence-recovery audit (full reasoning in `docs/decisions/PROVERBGAP_EVIDENCE_RECOVERY_AND_NEXT_EXPERIMENT.md`):

| Claim | Old status | New status | Basis |
|---|---|---|---|
| S1 86.8% / S2-strict 62.5%, McNemar p<0.001 (May pilot) | Historically verified, not currently reproducible | Unchanged; McNemar sub-claim now **explicitly unresolved** (test form/pairing undocumented; two-prop χ² = 106.9 is a plausibility check only) | Memo §A3 |
| "S2 real-paraphrase accuracy 24.9% (below random)" | Reported but unverified (misattributed to the pilot) | **Misattributed + internally inconsistent** — belongs to N=50-era Run 22/23 (30.0%/31.5%, which *are* arithmetically coherent); pilot's strict S2 = 62.5% | Memo §A4; D-17 |
| "DeepSeek-R1 100% gold copying" | Reported but unverified | **Contradicted** (model absent; max observed 11.2%) | D-18 |
| "16,439 FiB rows" / "25,190 generation rows" | Reported but unverified | **Unsupported by any located artifact** (recovered: 30 items / 2,160 attempts) | D-18, D-19 |
| FiB pilot | COMPLETED-WITH-OUTPUTS | COMPLETED-WITH-OUTPUTS **and descriptively analyzed** — feasibility only; A≈C at n=30 | Memo §B1 |
| Generation pilot | COMPLETED-ANALYSIS-MISSING | Primary evidence recovered **and descriptively analyzed** (success/gold-copy per model) | Memo §B2 |
| April-era MCQ runs | undocumented | ER-A1 added (COMPLETED-WITH-OUTPUTS, Git-history recovery) | D-20 |
