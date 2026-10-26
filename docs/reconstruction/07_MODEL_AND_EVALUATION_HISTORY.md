# Phase 1 — Document 07: Model & Evaluation History

**Status:** Completed
**Purpose:** Trace the model rosters, provider migrations, and failure modes across both research directions; map competitors documented in the memory graph.

**Sources:** `docs/ProverbGap_Paper_Draft.md` §2, §4; `.archive/.../ProverbGap_MCQ_Project_History.docx` extract; `kaggle/run_logs/v68/v68_detailed_analysis_report.md` §1, §8.1; `kaggle/kaggle_analysis/input/evaluation_results.csv`; `memory_proverbgap_filtered.json` (competitor entities).

---

## 1. Original model pipeline (May 2026, Groq)

### S2 generator (adversarial distractors)
- `qwen3-32b` (Alibaba) via Groq — chosen to be **architecturally distinct** from the committee (Meta + Saudi).

### Evaluation committee (MCQ accuracy, 3 styles)
| Model | Provider | Params | Role | Failure |
|---|---|---|---|---|
| `meta/llama-4-maverick-17b-128e-instruct` | NVIDIA API | 17B (active) | S2 committee | stable |
| `allam-2-7b` | Groq API | 7B (Arabic-centric) | S2 committee | 14.7% error (Groq rate limit) |
| `meta/llama-3.3-70b-instruct` | Groq | 70B | early committee | **dropped** (API 79% failure / rate limit) |
| `qwen3-32b` | Groq | 32B | early committee (as evaluator) | dropped (failed pre-flight) |
| `google/gemma2-9b` | — | 9B | early committee | dropped (failed pre-flight) |

Original plan was 3–5 models; **reduced to 2** by API instability. GPU local models (ALLaM-7B garbled; AfroLLaMA memorization suspicion; BLOOM-7B OOM) → **API-only**.

### Encoder baselines (4, CPU-free)
mBERT (`bert-base-multilingual-cased`), XLM-RoBERTa (`xlm-roberta-base`), AraBERT (`aubmindlab/bert-base-arabertv2`), AfriBERTa (`castorini/afriberta_large`).

---

## 2. Provider migration: Groq → OpenRouter (May→Jun 2026)

Motivation (`history doc` §8): single-point-of-failure cost + 8-key Groq rotation already fragile at Kaggle shared IP.

### OpenRouter plan (Jun 15)
- Diversify committee (Claude/Gemini/Mistral via one API).
- Replace `gpt-oss-120b` (45% empty-response for AR/YO).
- S2 generation failover (if qwen3-32b Groq rate-limited).
- Hard daily budget cap.

### Budget priorities (never fully executed)
1. N=10/20 model test first (failure rate, cost/question, accuracy).
2. Add 1–2 OpenRouter models → 4-model committee.
3. Keep Groq primary; OpenRouter = failover/diversity.
4. Track cost/question; hard daily cap.
5. **Do NOT** do large-scale generation until S1 answer-key bug fixed.

---

## 3. v68 model rosters (OpenRouter, Jun 22)

### Generator pool (10 proposed, 3 active)
- Pool: `qwen/qwen3.7-max`, `google/gemma-4-31b-it`, `google/gemini-2.5-flash`, `google/gemini-2.5-pro`, `openai/gpt-4.1-mini`, `openai/gpt-4.1-nano`, `anthropic/claude-sonnet-4`, `qwen/qwen3.5-397b-a17b`, `meta-llama/llama-4-maverick`, `deepseek/deepseek-v4-pro`.
- **Active (3):** `qwen/qwen3.7-max`, `google/gemma-4-31b-it`, `google/gemini-2.5-flash`. Others benched/unused.

### Audit committee (4, blind options-only)
| Model | Family | Accuracy vs gold (v68) |
|---|---|---|
| `meta-llama/llama-3.3-70b-instruct` | Meta | 53.3% (96/180) |
| `mistralai/mistral-small-3.2-24b-instruct` | Mistral | 56.7% (102/180) |
| `google/gemma-3-27b-it` | Google | 45.6% (82/180) |
| `deepseek/deepseek-v3.2` | DeepSeek | 56.1% (101/180) |

**Note:** This audit committee ≠ original accuracy committee. Original = answer scorer; v68 = blind distractor auditor seeing options only. The model *names* overlap (llama-3.3-70b) but the **roles differ**.

### v68 per-generator audit performance (180/3 = 60 MCQs each)
| Generator (for MCQ production) | Audit accuracy | Perfect consensus | HCW | Fully generated |
|---|---|---|---|---|
| `google/gemma-4-31b-it` | 65.0% | 46.7% | 21.7% | 40/60 (66.7%) |
| `google/gemini-2.5-flash` | 53.3% | 41.7% | 31.7% | 30/60 (50.0%) |
| `qwen/qwen3.7-max` | 51.7% | 36.7% | 30.0% | 31/60 (51.7%) |

gemma-4-31b-it is the strongest generator on the audit (highest accuracy, lowest HCW). qwen3.7-max has worst length-fallback (30.0%, i.e., 18/60).

---

## 4. v68 per-variant audit performance (45 MCQs each)

| Variant | Accuracy | Perfect consensus | HCW | Fully generated | Length fallback |
|---|---|---|---|---|---|
| `adversarial-hard-negative` | 60.0% | 31.1% | 24.4% | 12/45 (26.7%) | 42.2% |
| `adversarial-length-locked` | 55.6% | 53.3% | 35.6% | 27/45 (60.0%) | 20.0% |
| `overgenerate-select` | 53.3% | 35.6% | 22.2% | 32/45 (71.1%) | 2.2% |
| `taxonomy-guided` | 57.8% | 46.7% | 28.9% | 30/45 (66.7%) | 0.0% |

Key: `overgenerate-select` has cleanest generation (71.1%) but still 22.2% HCW (distractors too tempting); `adversarial-hard-negative` rejects most via filters (42.2% length fallback) yet HCW stays high.

---

## 5. v69/v70 model intent (planned/never completed)

- **v69** (never run): would enable LLM fallback via `openai/gpt-4.1-nano` as the fallback generator (replacing corpus sampler). `USE_LLM_FALLBACK=True`.
- **v70** (halted @ $0.42/83 rows): same LLM-fallback intent; `pool_state.json` shows `fallback=None` (never invoked before halt — the OpenRouter 403 hit during generation, before fallback stage). 

---

## 6. Competitors (documented in memory graph)

| Benchmark | Venue | Languages | Formats | Relevance |
|---|---|---|---|---|
| **ProverbEval** | NAACL 2025 | Ethiopian languages | MCQ + FiB + Generation | Original comparison target; motivated 3-format plan |
| **Jawaher** | NAACL 2025 | Arabic (20 dialects) | translation + explanation | 10,037 proverbs; AR baseline |
| **PRONE** | CODI 2025 | Nepali | MCQ (human distractors) | 2,830 items |
| **MasalBench** | 2026 | Persian | MCQ + LLM distractors | 4-lang |
| **DiVERT** | EMNLP 2024 | — | distractor generation | distractor-quality theory |
| **GSM-DC** | EMNLP 2025 | — | injected distractors | robustness |
| **D-GEN** | ACL 2025 | — | constrained generation | forbids paraphrasing gold |
| **KNIGHT** (2025) | — | — | human validation | 100-item audit standard |
| **Language Model Council** | NAACL 2025 | — | heterogeneous judges | committee design |
| **Roundtable Policy** | 2025 | — | confidence-weighted consensus | audit voting |

Memory graph also records: **Kinaya (EACL 2026)** — not detailed; referenced for "Pragmatics Gap."

---

## 7. Failure-mode history (who/when)

| Failure | Era | When | Detection | Fix |
|---|---|---|---|---|
| Same-family exploitation (Meta gen + Meta eval: 57.8% vs 26.7%) | A (v1→v2.3) | v2.2 | paper Draft §6.2 | Switched gen to qwen3-32b |
| CoT reasoning collapse (llama-4: 23/24 NaN) | A (v2.1) | May pilot | paper Draft §6.2 | Skip CoT for llama-4-maverick |
| API meltdown (DeepInfra 402/SambaNova timeout/Cerebras 404/Groq 15,131) | A (v2) | May | history doc §2 | 8-key Groq rotation; health retries |
| kNN → numeric distractors ("20","23","30") | A (v3) | May 15 | history doc §2 | Dual-gate validation |
| MSP → trivial 100% (explanation not paraphrase) | A (v3) | May 15 | history doc §2 | Abandoned MSP |
| S2 construct validity (62.5% mixes 24.9% real-paraphrase + high fallback) | A (June 4 audit) | post-May | history doc §4, §6 | Pivoted (never fixed) |
| v4.3.3 catastrophic regression (86.8/62.5 → 24.2/0.0) | A (Jun) | Jun 8 | main_results_table.csv corruption | health retries + worker-cap |
| v68 corpus-fallback HCW (27.8% vs <10% target) | B (v68) | Jun 22 | audit gate | v69 ablation planned |
| OpenRouter 403 budget (v70 halt @ $0.42) | B (v70) | Jun 26 | pool_state.json | Budget exhaustion |

---

## 8. Cost summary

| Run | Cost | Cap | Status |
|---|---|---|---|
| v68 (180 MCQs, 720 votes) | **$0.8539** | $5.00 | ✅ Complete |
| v69 ablation (planned) | ~$0.10–$0.20 add'l | < $1.50 | ❌ Never run |
| v70 (halted) | **$0.4201** | $5.00 | ⛔ Halted (403) |

Extrapolated N=15 (v70 if green): ~**$2.56** (still under cap).
