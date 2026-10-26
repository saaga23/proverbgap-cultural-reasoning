# Phase 1 — Document 02: Original Research Reconstruction (May 2026)

**Status:** Completed
**Purpose:** Reconstruct the **original** ProverbGap research direction as designed in the May 2026 draft (`docs/ProverbGap_Paper_Draft.md` v1.0) — the "Cultural Reasoning Gap" benchmark that the later shortcut-audit reframing superseded. This document is the primary evidence that the May direction was a **literal/cultural understanding benchmark with an adversarial two-strategy difficulty design**, distinct from the June shortcut-resistance framing.

**Primary source:** `docs/ProverbGap_Paper_Draft.md` ("Draft v1.0 | May 2026") + `kaggle/kaggle_analysis/input/` (original Groq outputs) + `kaggle/kaggle_analysis/analysis_output/main_results_table.csv` (corrupted) + `scale_readiness_report.md` (deprecated) + `.archive/legacy_docs_2026-06-19/ProverbGap_Status_Document.docx` (extract) + `.archive/legacy_code_2026-06-19/create_project_history_doc.py:192`.

---

## 1. Research objective (original)

> **Central question:** Do LLMs genuinely understand proverbial figurative language, or do they exploit surface-level shortcuts?

The original ProverbGap is a **cross-lingual MCQ benchmark** that operationalizes this as a **two-strategy distractor-generation difficulty gradient**: an in-domain negative-sampling baseline (Easy) vs. cross-family LLM-paraphrasing adversarial distractors (Hard). The gap between the two strategies is the **Cultural/Literal Reasoning Gap** — a measurable difficulty signal, not a pass/fail gate.

The paper draft title ("Cross-Lingual MCQ Benchmark for Proverb Understanding") and abstract explicitly frame this as an **understanding** benchmark with a difficulty gap, **not** a shortcut-audit methodology paper.

---

## 2. The two-task literal/cultural design

The original design splits understanding into two difficulty strata via distractor origin:

| Strategy | Generation | Intended difficulty | Role in the gap |
|---|---|---|---|
| **S1** — In-domain negative sampling | 3 distractors sampled *without replacement* from **same-language** proverb pool; `SEED=42` + item index; placeholder fallback if <3 alternatives. | Easy | Baseline: measures whether the model can reject *random* same-language distractors = literal/discriminability floor. |
| **S2** — Cross-family LLM paraphrasing | Generator = `qwen3-32b` (Alibaba); committee = `llama-4-maverick` (Meta) + `allam-2-7b` (Saudi). Prompt returns 4 strings: 1 correct paraphrase + 3 subtle-shift incorrect. | Hard | Adversarial: distractors are *semantically close* to the gold meaning → measures genuine cultural/meaning understanding. |

**Two-task interpretation:** S1 ≈ "literal matching" task; S2 ≈ "cultural reasoning" task. The S1→S2 accuracy drop *is* the cultural-reasoning gap.

**Dual validation gate (§4.3):**
1. Length gate: relative length diff ≤ 35% char count.
2. Semantic gate: Jaccard(word sets, generated vs reference) ≥ 0.25.
Retry with exponential backoff (8 for EN/AR, 12 for YO); hard placeholder fallback ("Incorrect alternative", "Another wrong option", "Not the right choice") on exhaustion.

---

## 3. Data collection (original)

| Language | Count | Source | Prefix |
|---|---|---|---|
| English | 2,278 | Public proverb collections | ENG |
| Arabic | 913 | Classical Arabic (amsal) collections (MSA) | MID |
| Yoruba | 3,931 | Yoruba oral tradition / ethnographic records | YOR |

- Total collection = **7,172 proverbs across six languages** (EN/AR/YO/FR/DE/ES).
- **Current benchmark uses three languages (EN/AR/YO).** French (161), German (142), Spanish (63) "are collected but excluded from the current benchmark due to insufficient sample sizes for statistical validity."
- Each entry: original proverb text + English translation + cultural explanation.
- **Contamination filter:** hardcoded 25 famous-proverb substrings removed (≈8.3% of English).

### Three evaluation formats (original plan)
The original pipeline is designed for **three formats**, but the May v1.0 draft only **implements MCQ** and describes the other two as **future work** (§7.3–7.4):

1. **MCQ** — *implemented* (multiple-choice, 4 options).
2. **Fill-in-the-blank (FiB)** — §7.3: "a fill-in-the-blank variant where the model must complete a proverb given partial context. This tests recall and cultural knowledge rather than discrimination." → **planned, future tense.**
3. **Generation** — §7.4: "a generation task will ask models to explain the meaning of a proverb in context." → **planned, future tense.**

> **Evidence conflict (flagged):** the legacy `create_project_history_doc.py:192` and the June 19 memory graph assert v4.3.6 had "6 languages, two tasks, three formats (MCQ/FiB/Generation)" with 16,439 (FiB) and 25,190 (Generation) rows. The contemporaneous May paper draft contradicts this (3 langs, FiB/Gen = future). Resolution: the 16K/25K-row FiB/Generation outputs are a **later (post-May-18) exploration** that was abandoned when the central thesis was invalidated; the May v1.0 draft is the contemporaneous authority.

---

## 4. Methodology (original pipeline)

### Committee evaluation
- `meta/llama-4-maverick-17b-128e-instruct` (NVIDIA API, 17B active params)
- `allam-2-7b` (Groq API, 7B, Arabic-centric)
- Originally 3–5 models; reduced by API instability (llama-3.3-70b dropped at 79% API failure; qwen3-32b & gemma2-9b failed pre-flight).

### Three prompting styles (evaluation)
1. **Zero-shot** — reply only with A/B/C/D.
2. **Chain-of-thought (CoT)** — "think step by step, final answer on last line." (Skipped for llama-4-maverick: 23/24 NaN, 29% accuracy.)
3. **Few-shot** — 2 in-language examples precede the target.

### Answer extraction
Multi-stage: strip `</tool_call>`/`<reasoning>`; first-char shortcut; fallback regex (`answer is X`, `Answer: X`, `\boxed{X}`, `FINAL ANSWER: X`, word-boundary `[A-D]`, prefer last match).

### Position-bias mitigation
Base position `idx % 4`; each model gets a model-specific seeded shuffle (`seed = hash(model)+idx`) → different orderings per model.

### Encoder baselines (lower bound)
mBERT, XLM-RoBERTa, AraBERT (aubmindlab/bert-base-arabertv2), AfriBERTa (castorini/afriberta_large). Mean-pooled cosine similarity proverb↔option.

### Statistical testing
- Position bias: χ² (df=3), min n=20.
- McNemar's (continuity-corrected, df=1): S1 vs S2 accuracy per item (+ non-fallback subset).
- Bootstrap CIs: 1,000 resamples, 95%.
- Leakage heuristic: S1 accuracy ≥95% AND S1→S2 drop ≥20pp → HIGH risk.

---

## 5. Original results (May N=150 pilot)

Source: `docs/ProverbGap_Paper_Draft.md` §5 (run `run_20260523_224443`, Groq Kaggle notebook).

### 5.1 Primary accuracy

| Strategy | Accuracy | N | 95% Bootstrap CI |
|---|---|---|---|
| S1 (baseline) | **86.8%** | 750 | [84.3%, 89.2%] |
| S2 (strict) | **62.5%** | 590 | [58.1%, 66.6%] |
| S2 fallback rate | 21.3% | 32/150 | — |
| S2 fallback accuracy | 63.7% | 160 | — |
| Random baseline | 25.0% | — | — |

**McNemar:** χ²=131.3, p<0.001 (all items); χ²=110.8, p<0.001 (non-fallback). → Statistically significant difficulty gap = the cultural-reasoning gap.

### 5.2 Per-language

| Language | S1 | S2 strict | S2 fallback rate | S2 evaluated |
|---|---|---|---|---|
| English | 97.6% | 71.3% | 8.0% (4/50) | 46 |
| Arabic | 92.8% | 65.5% | 20.0% (10/50) | 40 |
| Yoruba | 70.0% | 46.2% | 36.0% (18/50) | 32 |

English strong; Yoruba weakest (36% S2 fallback — qwen3-32b struggles with low-resource figurative paraphrase).

### 5.3 Per-model

| Model | S1 | S2 | S1→S2 drop | Leakage | Error rows |
|---|---|---|---|---|---|
| llama-4-maverick | 92.7% | 82.0% | 10.7pp | LOW | 0 |
| allam-2-7b | 82.9% | 50.0% | 32.9pp | none (not flagged) | 221 |

### 5.4 Per-style

| Style | S1 | S2 |
|---|---|---|
| Zero-shot | 91.7% | 72.7% |
| Chain-of-thought | 89.3% | 55.3% |
| Few-shot | 80.7% | 56.7% |

### 5.5 Encoder baselines (all ≪ API committee)

| Encoder | S1 | S2 | S1 gap | S2 gap |
|---|---|---|---|---|
| AfriBERTa | 56.7% | 30.0% | −30.1pp | −32.8pp |
| AraBERT | 54.0% | 29.3% | −32.8pp | −33.5pp |
| mBERT | 54.7% | 29.3% | −32.1pp | −33.5pp |
| XLM-R | 55.3% | 36.0% | −31.5pp | −26.8pp |

---

## 6. Original negative results (lessons baked into design)

1. **Same-family exploitation** — early llama-4-scout generator + llama-3.3-70b evaluator scored 57.8% S2 vs 26.7% S1 (smoking gun). Fixed by switching generator to qwen3-32b (Alibaba), distinct from committee families.
2. **CoT reasoning collapse** — 48% pilot → 52.7% N=50 vs 82–92% zero-shot; llama-4-maverick 23/24 NaN. → CoT skipped for that model.
3. **API infrastructure fragility** — DeepInfra 402/404, SambaNova timeout, Cerebras 404, Groq rate limiting (1,040 implied failures in v4.3.4). → Hardened health-check retry, provider cooldown, worker-cap (v4.3.4).

---

## 7. Original future work plan (§7)

| Item | Plan | Language |
|---|---|---|
| Scale to N=700 | ~1.7h Kaggle runtime; reduce Groq workers 8→4–5, add jitter, rotate providers | Future |
| Additional languages | Integrate FR (161), DE (142), ES (63) | Future |
| **Fill-in-the-blank** | Complete proverb given partial context; recall/cultural knowledge | **Future (§7.3)** |
| **Generation** | Explain proverb meaning in context; deeper comprehension | **Future (§7.4)** |
| Human evaluation | 100 items audited for unambiguity, answerability, option uniqueness (KNIGHT 2025) | Future |
| Embedding-based distractor diversity | BERTScore/cosine distinctness among options | Future |

**Key point:** FiB and Generation are explicitly *future*, not implemented in the May draft. The "three formats" claim in the legacy history doc is a later over-statement.

---

## 8. Original publication intent (May)

The May draft positions ProverbGap as a **benchmark + negative-results paper** targeting venues like EMNLP. It does **not** mention EACL 2027 ARR. The EACL 2027 reframing was a July pivot (see Document 03, Document 08).

---

## 9. Evidence summary table

| Fact | Source | Confidence |
|---|---|---|
| S1 86.8%, S2 62.5% @ N=150 | Paper Draft §5.2 | High (contemporaneous) |
| 3 languages benchmarked (EN/AR/YO) | Paper Draft §3.1 | High |
| FiB/Generation planned, not implemented | Paper Draft §7.3–7.4 | High |
| qwen3-32b generator, llama-4-mav/ allam-2-7b committee | Paper Draft §4.3–4.5 | High |
| Same-family exploitation, CoT collapse, API fragility | Paper Draft §6.2 | High |
| 7,172 proverbs across 6 languages | Paper Draft §3.1 | High (collection); benchmarked=3 |
| 16,439 FiB / 25,190 Generation rows | Memory graph entities | Medium (later exploration, post-May-18) |
| FR/DE/ES excluded "insufficient sample size" | Paper Draft §3.1 | High |
