# Data Dictionary

**Grounding rule:** every column below was read directly from the named file (header row) on 2026-10-26. Row counts exclude headers. Files live in the source repository `saaga23/proverb_mcq` — none are copied here (rights). Confidence levels: **Verified** (read from file/code), **Inferred** (semantics derived from usage), **Unknown** (needs owner/source).

Unit-of-observation warning: a *proverb record*, a *generated MCQ*, a *model response*, an *audit vote*, and an *evaluation row* are different units. Counts below are per the stated unit only.

---

## 1. Source proverb collections (`actual_data/` in proverb_mcq)

### 1.1 `English_cleaned.csv` — 2,278 rows × 3 cols (unit: proverb record)
| Column | Meaning | Type | Role | Notes |
|---|---|---|---|---|
| `Sample_ID` | Row identifier | string | key | |
| `Proverb` | English proverb text | string | input | |
| `Correct_Meaning` | Gold meaning/interpretation | string | gold label | Doubles as cultural context (no separate translation column — source is already English) |

### 1.2 `Arabic_cleaned.csv` — 913 rows × 4 cols
| Column | Meaning | Type | Role | Notes |
|---|---|---|---|---|
| `Sample_ID` | Row identifier | string | key | |
| `source_text` | Arabic proverb (MSA) | string | input | |
| `english_translation` | English translation | string | input/reference | |
| `Cultural_Context` | Cultural explanation/usage | string | gold label | |

### 1.3 `Yoruba_cleaned.csv` — 3,974 rows × 7 cols
| Column | Meaning | Type | Role | Notes |
|---|---|---|---|---|
| `Sample_ID` | Row identifier | string | key | |
| `Source_Text_Yo` | Yoruba proverb (tonal marks where available) | string | input | |
| `Target_Text_En` | English translation | string | input/reference | |
| `Cultural_Context` | Cultural explanation | string | gold label | |
| `Provenance` | Source-of-record field | string | metadata | Values not yet enumerated — **Unknown** |
| `QA_Flag` | Data-quality flag from cleaning | string/enum | metadata | Values not yet enumerated — **Unknown** |
| `Comments` | Cleaner notes | string | metadata | |

⚠️ **Count discrepancy:** 3,974 rows here vs "3,931 Yoruba proverbs" claimed in `docs/ProverbGap_Paper_Draft.md` §3.1 → see `docs/audit/EVIDENCE_DISCREPANCIES.md` (D-1).

### 1.4 Kaggle dataset `abrahamsunday123/original-data` (2026-05-16) — Verified via Kaggle API file list
Contains all six cleaned CSVs: `English_cleaned.csv` (274 KB), `Arabic_cleaned.csv` (228 KB), `Yoruba_cleaned.csv` (893 KB), `French_cleaned.csv` (27.8 KB), `German_cleaned.csv` (19.5 KB), `Spanish_cleaned.csv` (8.7 KB). This is the primary evidence that the six-language collection existed and was attached to the Kaggle notebooks. FR/DE/ES schemas and row counts **not yet inspected** (owner may download from Kaggle).

Earlier Kaggle datasets document the data-collection lineage: `proverbeval-data` (Mar 9), `proverb2` (Mar 10), `proverbeval-clean-data` (Mar 11), `proverb-all` (Mar 19), `proverbgap-checkpoint-v` (Apr 27, 8.4 MB). The `proverbeval-*` names indicate the collection started from the published ProverbEval data (Ethiopian languages) in March 2026.

---

## 2. Original MCQ pilot (v4.3.4, May 2026) — `kaggle/kaggle_analysis/input/` in proverb_mcq

⚠️ The May v4.3.4 outputs that once lived in `kaggle_analysis/Last_run/` were **overwritten by June-run files** (see `docs/audit/EVIDENCE_DISCREPANCIES.md` D-3). The files below are the **June 8/9 failed Kaggle run's** inputs and outputs, reused directory names notwithstanding.

### 2.1 `mcqs_strategy1.csv` — 150 MCQs × 13 cols (unit: generated MCQ)
| Column | Meaning | Type | Role |
|---|---|---|---|
| `sample_id` | Proverb id | string | key |
| `language` | English/Arabic/Yoruba | enum | metadata |
| `source_proverb` | Proverb in original language | string | input |
| `proverb_en` | English translation | string | input |
| `correct_text` | Gold meaning (correct option text) | string | gold label |
| `distractors` | The three wrong options (serialized list) | list | generated (S1: sampled from other proverbs) |
| `fallback` | Whether placeholder distractors were used | bool | status |
| `strategy` | `S1` | enum | metadata |
| `Choice_A..Choice_D` | The four option texts | string | generated |
| `Answer` | Correct option letter (A–D) | enum | gold label |

### 2.2 `mcqs_strategy2.csv` — 150 MCQs × 14 cols
Same as S1 plus `info` (generation metadata from the LLM paraphraser; per-item JSON string). S2 distractors are LLM-paraphrased adversarial options (generator `qwen3-32b`).

### 2.3 `evaluation_results.csv` — 2,700 rows × 10 cols (unit: one model's answer to one MCQ under one prompting style)
| Column | Meaning | Type | Role |
|---|---|---|---|
| `strategy` | `S1`/`S2` | enum | metadata |
| `model` | Committee model id | string | metadata |
| `style` | `zero-shot` / `cot` / `few-shot` | enum | metadata |
| `sample_id` | Which MCQ | string | key |
| `language` | Item language | enum | metadata |
| `fallback` | Whether the MCQ used placeholder distractors | bool | status |
| `pred` | Model's chosen letter | enum(A–D) | model output |
| `hit` | 1 if pred == gold Answer else 0 | int | metric input |
| `raw` | Raw model response text | string | raw output |
| `error` | Error message if the API call failed | string | status |

**State of this file:** 2,440 of 2,700 rows carry provider-failure errors (Groq/NVIDIA 429s, "All providers failed … None"); only **260 valid rows, all S1** (76.2% correct among them). All 1,350 S2 evaluations failed. The "S1 14.7% / S2 0.0%" figures in `analysis_output/main_results_table.csv` and the deprecated `scale_readiness_report.md` come from counting failed calls as wrong answers (198/1350 = 14.7%). **This file cannot verify the May pilot numbers** (see E-1 in the discrepancies file).

### 2.4 `encoder_results.csv` — 1,200 rows × 8 cols (unit: one encoder's similarity choice on one MCQ)
`strategy, model, style, sample_id, language, pred, hit, similarities` — `similarities` holds the four cosine scores used to pick the argmax option. 300 MCQs × 4 encoders (mBERT, XLM-R, AraBERT, AfriBERTa).

### 2.5 `s2_semantic_scores_v2_baseline.csv` — 150 rows × 16 cols
S2 MCQ set plus generation diagnostics: `gold` (curated meaning used for scoring), `original_gold` (pre-curation meaning), `gen_attempts`, `gen_info`, `semantic_max_sim` (max embedding similarity between generated options and the gold meaning — the semantic-gate diagnostic). Basis for the S2 semantic-filter analysis; the construct-validity controversy hangs off exactly these fields (see `docs/experiments/EXPERIMENT_REGISTER.md`, experiment MCQ-PILOT).

---

## 3. OpenRouter v68 production run — `kaggle/run_logs/v68/openrouter_pilot1_test_output/` in proverb_mcq

### 3.1 `pilot1_test_generated_mcqs.csv` — **180 rows** × 20 cols (unit: generated MCQ)
| Column | Meaning | Type | Role |
|---|---|---|---|
| `generator_model` | Which of 3 generators produced the options | string | metadata |
| `variant` | Prompt variant: `adversarial-hard-negative` / `adversarial-length-locked` / `overgenerate-select` / `taxonomy-guided` | enum | metadata |
| `mcq_id` | `{generator}_{variant}_{language}_{index}` | string | key |
| `language` | English/Arabic/Yoruba | enum | metadata |
| `sample_id` | Proverb id | string | key |
| `proverb` | Proverb text | string | input |
| `correct_meaning` | Curated gold meaning shown as correct option | string | gold label |
| `original_meaning` | Pre-curation meaning (provenance) | string | metadata |
| `curated_meaning` | Final curated meaning (usually == correct_meaning) | string | gold label |
| `correct_label` | Correct option letter A–D | enum | gold label |
| `option_A..option_D` | Option texts (one is the gold meaning) | string | generated |
| `generation_status` | `generated` (101) / `partial` (50) / `length_fallback` (29) | enum | status |
| `fallback_count` | Number of corpus-fallback replacements | int | metric |
| `length_replaced` / `leak_replaced` / `nli_replaced` | Replacements per filter | int | metric |
| `duplicate_options` | Exact duplicate option pairs | int | metric (all 0) |

Distribution: 5 proverbs × 3 languages × 3 generators × 4 variants = 180. Key balance A/B/C/D = 45/45/45/45.

### 3.2 `pilot1_test_audit_results.csv` — **180 rows** × 16 cols (unit: committee verdict on one MCQ, aggregating 4 votes)
| Column | Meaning | Type | Role |
|---|---|---|---|
| `generator_model`,`variant`,`mcq_id`,`language`,`correct_label` | As above | | metadata/gold |
| `consensus_label` | Majority choice of the 4 blind auditors | enum(A–D) | model output |
| `consensus_frac` | Fraction of auditors agreeing with consensus_label | float 0–1 | metric |
| `consensus_correct` | `1` if consensus_label == correct_label else `0` | int(0/1) | metric input |
| `vote_<auditor>` / `hit_<auditor>` | Per-auditor vote and correctness (auditor ∈ llama-3.3-70b-instruct, mistral-small-3.2-24b-instruct, gemma-3-27b-it, deepseek-v3.2; slashes in model ids replaced by underscores in column names) | enum/int | raw votes |

**HCW (High-Consensus-Wrong)** = rows with `consensus_frac ≥ 0.75` AND `consensus_correct == 0` → 50/180 = 27.8% (recomputed 2026-10-26 from this file; matches README).

### 3.3 `pilot1_test_raw_outputs.csv` — 903 rows × 20 cols (unit: one API call)
`stage` (generation vs audit), generator/variant/language/proverb/meanings, `raw_model_output`, `finish_reason`, `status`, filter-replacement counters, `mcq_id`, `model`, `prompt` (full prompt text), `extracted_vote`. This is the raw evidence trail for every generation call and every audit vote.

### 3.4 `pilot1_test_human_annotation_sample.csv` — 30 rows × 20 cols (unit: annotation task)
Columns include `human_answer`, `human_confidence`, `human_notes` — **all empty (0/30 filled)**. Proof the human annotation was prepared but never executed on this sample.

### 3.5 `pilot1_test_summary.json` / `pool_state.json`
Run configuration and state: seed 20260615, generator pool (10 configured / 3 active), committee pool (6 configured / 4 active), `substitutions: {generators: [], auditors: []}` (⇒ `USE_LLM_FALLBACK=False` path taken), cost cap $5.00, estimated cost $0.8539 (v68) / $0.4201 (v70 halt), per-variant comparison, distractor metrics (avg distractor–key cosine 0.2468; option-length CV 0.3011), 7 figure paths.

### 3.6 v68 analysis tables — `kaggle/run_logs/v68/table_*.csv` (analysis layer)
- `table_llm_proxy_iaa.csv`: 7 proxy models × 60 items; Fleiss κ = **0.4845**, mean pairwise Cohen κ = 0.4846 (source `iaa_report_20260708_121120.json`, dated 2026-07-08). This is the "LLM-proxy calibration anchor", **not** human agreement.
- `table_statistical_tests_corrected.csv`: all pairwise McNemar tests (Holm-corrected p = 1.0) and Wilcoxon tests (p ≥ 0.31) — **no significant differences** between variants/generators at N=45/60.
- Also: bootstrap CIs, auditor-vs-gold, position-bias χ², length bias, cost efficiency, single-generator ablation, variant×language interaction, shuffling robustness.

---

## 4. Human-validation preparation

### 4.1 `data/production/paper_first_outputs_2026-06-22_10-42-02/human_validation_sample_60.csv` — 60 items × 32 cols (unit: annotation task)
Same core fields as v68 MCQs plus per-auditor vote/hit columns and `consensus_*`. **No human-response columns present** — sample prepared, never annotated.

### 4.2 `annotation_app/` (in proverb_mcq) — human-annotation web application
Next.js 16 + React 19 + Supabase (Postgres/RLS) + Playwright E2E tests; deployed via Vercel (`.vercel/`). Task design per its README: read proverb in original language → choose correct option (A–D, English options) → rate each distractor's plausibility 1–5 → flag shortcut patterns. `ANNOTATOR_ONBOARDING.md` provides the annotator guide. **Status:** built and E2E-tested; **no annotation records found in the repository**; whether any annotator ever submitted through the deployed app is **Unknown** (would require Supabase access). ⚠️ `.env.local` (real secrets) exists in the old repo — excluded from any transfer.

---

## 5. Kaggle-recovered task pilots (May 19, 2026) — downloaded to temp, **not** committed anywhere

### 5.1 Fill-in-the-blank pilot — `nb_pilot_30_results.csv` (kernel `proverb-gap-fill-in-the-blank`, status COMPLETE) — 30 rows × 26 cols (unit: one item × one condition)
| Column | Meaning |
|---|---|
| `sample_id`,`language`,`task`,`proverb` | Item identity; `proverb` = original text |
| `displayed_proverb` | The cloze form shown to the model (a word masked) |
| `gold_word` | The masked word (fill target) |
| `paraphrase_ok` | A paraphrase-based distractor word/condition |
| `sham_proverb` | A sham-proverb condition |
| `pred_a/status_a/em_a/nem_a/chrf_a/latency_a` (+ `_b`, `_c`) | Three conditions (a/b/c): model prediction, status, Exact Match, Normalized EM, ChrF score, latency |

So the FiB task = word-level cloze on the proverb text, scored with EM/NEM/ChrF across three conditions. **This is a 30-item pilot, not the 16,439-row dataset** quoted in the Phase 1 memory export (unverified figure — see discrepancies D-6, now D-19).

**Audit note (2026-10-26):** `FALLBACK_LINE` (the value in every `status_*` column) is an **answer-extraction fallback** — the parser fell back to taking the model's last line because the structured answer format was absent; it does **not** mean generation failed. Conditions: A = original context, B = paraphrased context, C = sham-proverb control. Recomputed means: EM 0.133 / 0.100 / 0.133 (A/B/C) — real-context and sham-context performance are identical at this scale (decision memo §B1).

### 5.2 Generation pilot — `pilot_outputs/pilot_results.csv` (kernel `proverbgap-generation`, status COMPLETE) — **2,160 rows** × 23 cols (unit: one model's generated explanation attempt)
| Column | Meaning |
|---|---|
| `model`,`display`,`provider`,`model_id_used` | Which model generated |
| `task`,`strategy`,`language`,`sample_id`,`proverb`,`gold` | Item identity + gold explanation |
| `generated` | Model's generated explanation (raw) |
| `raw_len`,`cleaned_len` | Lengths |
| `semantic_sim` | Embedding similarity of generated vs gold |
| `bleu`,`chrf` | n-gram overlap metrics vs gold |
| `status`,`reason` | Generation status / failure reason |
| `contains_gold` | Whether the output copies the gold explanation (gold-copying detector) |
| `length_ratio`,`timestamp`,`attempt` | Diagnostics |

2,160 generation attempts across models/languages/strategies. The "25,190 clean Task A rows" figure from the Phase 1 memory export is **not supported** by this artifact (D-6).

### 5.3 `retry_queue.jsonl` — 483 retry records (`mk, task, strat, lang, row, attempt, first_reason`).

---

## 6. April-era MCQ generation batches (Git history only — first commit `198253b`, 2026-05-16)

Recovered during the 2026-10-26 evidence audit; **not present in the current working tree** (removed after early May; still in public Git history).

### `_unzipped/mcq_a_{zs,cot,cot_xl}_{language}.csv` — e.g., 2,000 Yoruba rows, 803 Arabic rows × 22 cols (unit: generated MCQ item with quality metrics)
| Column | Meaning | Type | Role |
|---|---|---|---|
| `task`, `strategy`, `language`, `sample_id` | Batch/task identifiers (e.g., `a`, `zs`, `YOR0001`) | string/enum | metadata |
| `source_proverb` / `proverb_en` | Proverb and its English rendering | string | input |
| `correct_meaning` | Gold meaning used as the correct option | string | gold label |
| `cultural_context_available` | Whether a cultural-context field was present | bool | metadata — **False throughout** (pre-dates the cultural-context schema) |
| `Choice_A..Choice_D`, `Answer` | Options and key | string/enum | generated + gold |
| `distractor_1..3` | The three distractor texts (same as the non-key options) | string | generated |
| `raw_response` | Generator's raw output (includes candidate lists) | string | raw output |
| `parse`, `complete` | Whether output parsed / all fields present | float 0–1 | quality |
| `len_r`, `distinct`, `quality` | Length ratio, option distinctness, composite quality score | float | quality metrics |

Also recovered: `_all_mcq_analysis.txt` (per-language descriptive statistics) and `_mcq_nb_dump.txt` (notebook dump). Generation code for this era **not located** — metric provenance is **Inferred**. Six languages appear in the file set; FR/DE/ES row counts not yet counted.

## 7. Explicit unknowns (do not guess)

1. FR/DE/ES CSV schemas and row counts (Kaggle `original-data`).
2. Values/categories of `Provenance`, `QA_Flag` in Yoruba_cleaned.csv.
3. May v4.3.4 pilot raw artifacts (see D-3) — only the May 24 verification reports attest them.
4. Whether any human annotation was ever collected via the deployed annotation app (needs Supabase access).
5. Contents semantics of `gen_info`/`info` fields (JSON blobs; structure undocumented).
6. The 16,439 (FiB) and 25,190 (Generation) figures from the memory export — no artifact supports them.
