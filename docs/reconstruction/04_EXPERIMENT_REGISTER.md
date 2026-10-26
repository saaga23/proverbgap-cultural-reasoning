# Phase 1 — Document 04: Experiment Register

**Status:** Completed
**Purpose:** Authoritative register of every experiment/run, cross-referenced to artifacts, results, and status. Two eras: **Phase A (original Groq, v1–v4.3.4)** and **Phase B (OpenRouter shortcut-audit, v65–v70)**. Versions v1–v4.3.6 from `.archive/legacy_docs_2026-06-19/ProverbGap_MCQ_Project_History.docx` (extracted 2026-06-15); v65–v70 from `kaggle/run_logs/*` and `v68_detailed_analysis_report.md`.

---

## Phase A — Original Groq pipeline (v1 → v4.3.4)

| Version | Date | Key change | Results (S1 / S2) | Status | Artifact |
|---|---|---|---|---|---|
| v1 | Apr 24 2026 | Initial design: 3 langs (EN/AR/YO), S1/S2, MCQ-only, Groq, 3-eval styles, encoder baselines | — (design) | Superseded | Status Doc (Apr 24) |
| v1.1 | Apr 26 | Contamination filter (25 famous-proverb substrings, ~8.3% EN removed) | — | Superseded | |
| v2 | May 2 | Added 4 encoder baselines (mBERT/XLM-R/AraBERT/AfriBERTa) | — | Superseded | |
| v2.1 | May 5 | Added CoT style; added leakage heuristic (S1≥95% & drop≥20pp → HIGH risk) | — | Superseded | |
| v2.2 | May 8 | Added per-model seeded position shuffle (`seed=hash(model)+idx`); discovered same-family exploitation (Meta gen + Meta eval: 57.8% vs 26.7%) | — | Superseded | |
| v2.3 | May 10 | **Switched S2 generator to qwen3-32b (Alibaba)**, distinct from committee (Meta/Saudi) | — | Superseded | |
| v3 | May 15 | N=150 pilot complete (`run_20260523_224443`); dual-gate (length+Jaccard 0.25) + retries | **S1 86.8% / S2 62.5%** (750/1,500 evals) | Baseline | `docs/ProverbGap_Paper_Draft.md` §5 |
| v3.1 | May 18 | Central thesis invalidated; explored FiB (16,439 rows) & Generation (25,190 rows); both abandoned | S1 86.8% / S2 62.5% | Pivoted | memory graph entities |
| v4 | May 22 | Begin Groq→OpenRouter migration planning; cost/perf rationale | — | In progress→replaced | `create_project_history_doc.py` §8 |
| v4.1 | Jun 8 | OpenRouter pilot (early); **answer-key shuffle bug** | **S1 14.7% / S2 0.0%** | ❌ Corrupted | `main_results_table.csv`, `scale_readiness_report.md` |
| v4.2 | Jun 10 | Bug fix: locked answer-key generation; validated key consistency | S1 80.2% (S2 valid) | Recovered | history doc §7 |
| v4.3 | Jun 15 | Audit gates designed (HCW, perfect-consensus, partial+fallback, duplicates, key-balance); 4 variants defined | — | Framework | `v68_detailed_analysis_report.md` §1 |
| v4.3.1 | Jun 17 | v67 frozen baseline config; OpenRouter model roster finalized | — | Frozen | v68 report §1 |
| v4.3.2 | Jun 20 | v68 preparation (180-MCQ design: 15×4×3) | — | Ready | |
| v4.3.3 | Jun 21 | Pre-run; smoke validation of v67 config | — | Smoke | |
| v4.3.4 | Jun 22 00:30Z | **v68 run completed** (seed 20260615, 180 MCQs, $0.85) | Audit: 4/6 gates failed (HCW 27.8%) | ✅ Completed+audited | `pilot1_test_summary.json`, audit_results.csv |
| v4.3.5 | Jun 22 10:42Z | Paper-first outputs frozen; human-validation sample (60) prepared | — | Frozen | `data/production/paper_first_outputs_2026-06-22_10-42-02/` |
| v4.3.6 | Jun 23 | v69 ablation planned; v70 N=15 prep | — | Planned | v68 report §7 |

**Original headline result (Phase A, v3/v4.3.4):** S1 86.8% vs S2 62.5%, McNemar p<0.001 — **the Cultural/Literal Reasoning Gap**.

**Critical qualifier (v3.1 / June 4 audit):** the 62.5% S2 figure **mixes real paraphrases (scored only 24.9%, below random guessing 25%)** with fallback placeholder questions (scored much higher). S2 construct validity disputed; some items may be unanswerable. See Document 05.

---

## Phase B — OpenRouter shortcut-audit (v65 → v70)

| Version | Date | Key change | Results | Status | Artifact |
|---|---|---|---|---|---|
| v65 | Jun (early) | N=1 smoke test (OpenRouter) | HCW 11.1% | Completed | v68 report §2 |
| v66 | Jun (mid) | N=1 regression | Perfect-consensus 55.6%, HCW 22.2% | Completed (regression) | v68 report §2 |
| v67 | Jun 17 | Frozen baseline: `USE_LLM_FALLBACK=False`, N_PER_LANG=5, 4 variants, 3 gen + 4 audit | — | Frozen config | v68 report §1 |
| v68 | **Jun 22** | **Production run**: 180 MCQs (15×4×3), seed 20260615, $0.85, 720 votes, 0 missing/replacements | HCW 27.8%, perfect-consensus 41.7%, partial+fallback 43.9%, hard-fallback 16.1%; 4/6 gates ❌; dup=0 ✅; key 45/45/45/45 ✅ | ✅ Completed+audited | `run_logs/v68/` |
| v69 | Jun 22 (planned) | Planned ablation: `USE_LLM_FALLBACK=True`, fallback=model `openai/gpt-4.1-nano`, N=5 | Success gates: HCW<15%, partial+fallback<30%, cost<$1.50 | ❌ **Never executed** (budget exhausted) | `run_logs/v69/` — only scripts/templates, no CSV/summary |
| v70 | Jun 26 | First attempt at LLM-fallback at N=5 (USE_LLM_FALLBACK=True) | 83/180 rows, $0.42, `generation_done=False`, `audit_done=False`, OpenRouter 403 budget limit, adversarial-hard-negative 11/15 rows | ⛔ **HALTED** mid-generation | `run_logs/v70/` — partial CSV + `pool_state.json` |

**v68 is the final audited production dataset.** N=5 per language (15 proverbs). 180 MCQs, $0.85. v69/v70 never reached a complete audited state.

---

## v68 experiment spec (canonical)

From `v68_detailed_analysis_report.md` §1 + `pilot1_test_summary.json`:

- **Seed:** 20260615
- **Config:** `v67 frozen baseline` (`USE_LLM_FALLBACK = False`), `N_PER_LANG = 5`
- **Proverbs:** 15 (5 English + 5 Arabic + 5 Yoruba)
- **Variants (4):** `adversarial-hard-negative`, `adversarial-length-locked`, `overgenerate-select`, `taxonomy-guided`
- **Generators (3 active):** `qwen/qwen3.7-max`, `google/gemma-4-31b-it`, `google/gemini-2.5-flash`
- **Auditors (4):** `meta-llama/llama-3.3-70b-instruct`, `mistralai/mistral-small-3.2-24b-instruct`, `google/gemma-3-27b-it`, `deepseek/deepseek-v3.2`
- **Output:** 180 MCQs × 4 auditors = 720 votes; 0 missing; 0 substitutions
- **Cost:** $0.8539 / $5.00 cap
- **Files:** `pilot1_test_generated_mcqs.csv` (180 rows), `pilot1_test_audit_results.csv` (720 votes), `pilot1_test_summary.json`, 7 figures

---

## v69 ablation spec (planned, never run)

From `v68_detailed_analysis_report.md` §7.2:
```python
N_PER_LANG = 5
USE_LLM_FALLBACK = True
FALLBACK_GENERATOR_MODEL = "openai/gpt-4.1-nano"
# all other v68 constants unchanged
```
Success gates: HCW < 15%, partial+fallback < 30%, perfect-consensus ≤ 45%, cost < $1.50.

---

## v70 status (halted)

From `kaggle/run_logs/v70/openrouter_pilot1_test_output/pool_state.json`:
- `cost_spent` = **$0.4201** (of $5.00 cap)
- `generation_done` = **False**
- `audit_done` = False
- `fallback` = None
- Partial `pilot1_test_raw_outputs.csv`: 83 rows (halted mid-variant-set; adversarial-hard-negative reached 11/15 rows)
- Failure mode: **OpenRouter 403 budget limit** at runtime.

---

## Cross-era result translation table

| Original (Phase A) | Shortcut-audit (Phase B, v68) | Notes |
|---|---|---|
| s1_accuracy | — (S1 not re-run in v68; v68 is generation-audit only) | v68 tests *distractor quality* via blind audit, not model accuracy |
| s2_accuracy / 62.5% | — | Not reproduced; v68 reframes difficulty as HCW |
| MCQ difficulty (S1 vs S2 gap) | **HCW 27.8%, perfect-consensus 41.7%, partial+fallback 43.9%** | Shortcut audit gates |
| Committee accuracy | — | Original committee (2 models) ≠ v68 audit committee (4 models) |
| Leakage heuristic | — | Replaced by blind options-only HCW gate |
| McNemar / position-bias χ² | — | Original stats; v68 uses χ² for position (p=0.322, not significant) |
| 6 languages (planned) | 3 languages (EN/AR/YO) | v68 reduced from planned 6 |
| FiB / Generation (future) | Not in v68 | v68 MCQ-only |

**v68 does NOT reproduce the original 86.8%/62.5% accuracy figures.** v68 measures distractor *shortcut-resistance* (audit committee on options-only), a different question than model *accuracy* (original MCQ solving). This is the central methodological divergence.
