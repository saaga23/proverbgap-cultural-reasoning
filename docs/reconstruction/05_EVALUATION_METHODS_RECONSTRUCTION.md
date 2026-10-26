# Phase 1 — Document 05: Evaluation Methods Reconstruction

**Status:** Completed
**Purpose:** Reconstruct the evaluation methodology of BOTH research directions and map how the original "accuracy-based" metrics were replaced by the "shortcut-audit" gates. Covers the original S1/S2 accuracy design, encoder baselines, statistical testing, and the v68 blind-audit HCW gate — plus the unresolved S2 construct-validity issue.

---

## 1. Original evaluation design (May 2026, `docs/ProverbGap_Paper_Draft.md` §4–5)

### 1.1 Metric: MCQ accuracy (per strategy)
Models select A/B/C/D. Accuracy = correct selections / total. Two parallel metrics:

| Strategy | N (evals) | Accuracy | 95% CI |
|---|---|---|---|
| S1 (negative sampling, easy) | 750 | **86.8%** | [84.3%, 89.2%] |
| S2 (cross-family paraphrase, hard) | 590 | **62.5%** | [58.1%, 66.6%] |
| S2 fallback (placeholder) | 160 | 63.7% | — |
| Random | — | 25.0% | — |

**The Cultural/Literal Reasoning Gap:** S2 is significantly harder than S1 (McNemar χ²=131.3, p<0.001). The 24.3pp gap is the original central result.

### 1.2 Evaluation committee (original)
- `meta/llama-4-maverick-17b-128e-instruct` (NVIDIA API, 17B)
- `allam-2-7b` (Groq API, 7B, Arabic-centric)
- Originally 3–5 models; reduced to 2 by API instability (llama-3.3-70b 79% failure; qwen3-32b, gemma2-9b failed pre-flight).
- **Per-model:** llama-4-maverick 92.7%/82.0% (drop 10.7pp); allam-2-7b 82.9%/50.0% (drop 32.9pp).

### 1.3 Three prompting styles (evaluation only)
1. **Zero-shot** — reply only the letter. (Best: 91.7% S1 / 72.7% S2)
2. **Chain-of-thought (CoT)** — reason step-by-step. (89.3% / 55.3%; skipped for llama-4-maverick: 23/24 NaN)
3. **Few-shot** — 2 in-language examples. (80.7% / 56.7%)

### 1.4 Position-bias mitigation
- Base position `idx % 4`; per-model seeded shuffle `seed = hash(model) + idx`.
- χ² goodness-of-fit (df=3, min n=20): S1 p=0.739, S2 p=0.746 → **not significant** (mitigation effective in original design).

### 1.5 Encoder baselines (lower bound)
mBERT, XLM-RoBERTa, AraBERT, AfriBERTa — mean-pooled cosine similarity proverb↔option, pick highest. All scored ~29–36% (vs 86.8–62.5% API) → confirms task needs reasoning beyond similarity.

### 1.6 Statistical testing
- Position bias: χ² (df=3).
- McNemar's (continuity-corrected, df=1): S1 vs S2 per item + non-fallback subset.
- Bootstrap CIs: 1,000 resamples, 95%.
- Leakage heuristic: S1≥95% AND S1→S2 drop≥20pp → HIGH risk (none triggered; llama-4-maverick drop only 10.7pp).

---

## 2. Original evaluation — the S2 construct-validity problem (unresolved)

**Documented in two places:**
- `ProverbGap_Paper_Draft.md` is silent (reports 62.5% S2).
- `.archive/.../ProverbGap_MCQ_Project_History.docx` §4 (v3.1) + §6 (reviewer concerns) states: **"A later audit (June 4) raised a serious concern that the 62.5% S2 figure mixes real paraphrases (which scored only 24.9%, below random guessing) with fallback placeholder questions (which scored much higher)."**
- `docs/RESEARCH_HISTORY_AND_README_AUDIT.md` §2.4 "S2 Construct Validity" corroborates.

**Implication:** S2's headline 62.5% is not internally consistent. If real paraphrases score 24.9% (below random 25%), the difficulty gap that the whole original thesis rests on is compromised — *either* the paraphrases are not genuinely adversarial (models genuinely fail them because they're near-paraphrases of the gold, i.e., leaky), *or* the fallbacks inflate the score by substituting easy placeholder items.

**Status:** Not resolved before the pivot. The June 4 audit concern is a *contributing* reason the central thesis was invalidated May 18 / pivoted June 22. This is an **open evidence conflict** for any future paper that would cite 62.5%.

---

## 3. v68 shortcut-audit evaluation design (Jun 22)

The v68 design **replaces** accuracy scoring with a **blind options-only audit** that asks: "given only the four answer options, can a committee identify the correct one?" If the distractors are shortcut-prone, auditors converge on the wrong answer.

### 3.1 Audit committee (v68 — distinct from original)
- **Blind:** auditors see **only the 4 options** — no proverb text, no generator identity, no correct meaning.
- **4 models:** `meta-llama/llama-3.3-70b-instruct`, `mistralai/mistral-small-3.2-24b-instruct`, `google/gemma-3-27b-it`, `deepseek/deepseek-v3.2`
- 720 votes (180 × 4), **0 missing, 0 substitutions**.
- Individual accuracy vs gold: llama3.3 53.3%, mistral-small 56.7%, gemma-3-27b 45.6%, deepseek 56.1% (≈random 25% → audit is diagnostic, not validation).

### 3.2 v68 gates (targets)

| Gate | v68 value | Target | Pass? |
|---|---|---|---|
| Hard fallback rate (`length_fallback`) | 16.1% (29/180) | <5% | ❌ |
| Partial + fallback | 43.9% (79/180) | <15% | ❌ |
| **High-consensus-wrong (HCW ≥0.75)** | **27.8% (50/180)** | **<10%** | ❌ |
| Perfect consensus | 41.7% (75/180) | <30% | ❌ |
| Per-language correctness ≥50% | EN 65.0 / AR 53.3 / YO 51.7 | ≥50 | ⚠️ fragile |
| Duplicate options | 0 | 0 | ✅ |
| Correct-key balance | 45/45/45/45 | ~25% each | ✅ |

**HCW definition (v68):** consensus fraction ≥ 0.75 (≥3 of 4 auditors agree) AND consensus label ≠ correct label = auditors collectively pick the wrong answer with high confidence. This is the **shortcut signal**: a plausible-but-wrong distractor that traps the committee.

> Note on threshold: 43.3% = "all-incorrect consensus" (100−56.7% accuracy). HCW (27.8%) is the *high-confidence* subset (≥0.75). README §5 and v68 report §2 both use ≥0.75 consistently.

### 3.3 Generation-status taxonomy (v68)

| Status | Count | % | Meaning |
|---|---|---|---|
| `generated` | 101 | 56.1% | All 3 distractors passed filters, no fallback |
| `partial` | 50 | 27.8% | ≥1 distractor replaced by filter |
| `length_fallback` | 29 | 16.1% | Length-parity fallback invoked |
| `parse_fallback` | 0 | 0.0% | — |
| `hard_fallback` | 0 | 0.0% | — |

Mean replacements/MCQ: **0.99** total; NLI 0.36, leak 0.35, length 0.15, duplicate 0.00. → 43.9% of MCQs touch the corpus fallback sampler.

### 3.4 v68 position check (audit, not mitigation)
Key balance A/B/C/D = 15/15/15/15 per language (perfect). Committee accuracy by position: A 73.3%, B 57.8%, C 48.9%, D 46.7%; χ²=3.49, df=3, **p=0.322** → not significant at α=0.05 (README §5.5; v68 report does not restate χ² but table matches).

### 3.5 v68 filter breakdown (drives fallbacks)
| Filter | Mean recl./MCQ |
|---|---|
| NLI paraphrase | 0.36 |
| Correct-meaning leak | 0.35 |
| Length parity | 0.15 |
| Untracked residual | ~0.13 |
| Blocklist | 3 triggers (all AR "Charity begins at home"); 0 exact dups; 3 Jaccard>0.50 near-dups |

→ Semantic filters (NLI+leak = 71%) dominate; length/blocklist minor.

---

## 4. Five failure modes (v68 taxonomy, `v68_detailed_analysis_report.md` §7.3)

1. **Generic reversal / idiom shortcut** — English distractors too easy (65% audit accuracy, distractors don't tempt); corpus fallbacks leak English idioms ("Charity begins at home", "Bird in the hand") into Arabic items (see Appendix 8.2 examples).
2. **Near-paraphrase trap** — NLI filters reject tempting near-paraphrases of the gold, removing hard negatives; surviving corpus fallbacks then look plausible.
3. **Confident-wrong fallback** — corpus-fallback distractors attract ≥0.75 auditor consensus on the *wrong* answer (HCW).
4. **Cultural mismatch** — Yoruba/Arabic fallbacks drawn from other languages' proverbs; cultural grounding lost.
5. **Length/register imbalance** — `length_fallback` and `partial` items flagged (29 + 50 = 79/180).

---

## 5. Methods comparison: original vs v68

| Aspect | Original (May) | v68 shortcut-audit (Jun) |
|---|---|---|
| Unit of analysis | Model MCQ accuracy | Distractor shortcut-resistance |
| Key metric | S1 86.8% / S2 62.5% | HCW 27.8% (target <10%) |
| Committee role | Answer scorer | *Blind* distractor auditor (options-only) |
| Difficulty signal | S1→S2 accuracy gap | HCW + perfect-consensus + fallback rates |
| Committee size | 2 (API-unstable) | 4 (OpenRouter, 0 missing) |
| Prompt styles | 3 (zero/CoT/few-shot) | None at audit stage (blind options-only) |
| Position handling | Mitigation (seeded shuffle) | Balance check only (A/B/C/D=45 each) |
| Construct-validity check | Leakage heuristic (S1≥95% & drop≥20pp) | HCW gate (≥0.75 wrong consensus) |
| Statistical testing | McNemar, χ², bootstrap CIs | Bootstrap CIs (10,000 resamples) |
| Verdict framework | "Gap is significant → proceed to N=700" | "4 of 6 gates fail → do not scale" |

**Methodological conclusion:** the original *accuracy* framing and the v68 *audit* framing answer different questions. The original asks "can models solve?"; v68 asks "are the *distractors* shortcut-resistant?". The pivot replaced a benchmark-accuracy paper with a distractor-generation-methodology + failure-taxonomy paper.

---

## 6. Reproducibility (v68 — no API calls)

Per README §11:
```bash
python kaggle/run_logs/v68/openrouter_pilot1_test_output/analyze_v68.py            # HCW at >=0.75
python kaggle/run_logs/v68/analysis_scripts/analyze_bootstrap_cis.py                # 10,000-resample CIs
python kaggle/run_logs/v68/analysis_scripts/analyze_statistical_tests.py          # McNemar/Wilcoxon/Holm
pytest tests/ -v                                                                  # includes test_v68_metrics.py
```
All read canonical CSVs (`audit_results.csv`, `generated_mcqs.csv`). No generation/API.
