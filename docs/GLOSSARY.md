# Glossary

Plain-English definitions. Terms are used consistently across this repository's documents.

## Tasks and items
- **Proverb record** — one source row: original proverb + English translation + cultural meaning/context (the gold meaning).
- **MCQ (multiple-choice question)** — a proverb question with four English meaning options; exactly one is the gold meaning. Options labeled A–D; the gold letter is the *answer key*.
- **Distractor** — one of the three wrong options.
- **S1 (Strategy 1)** — MCQ variant whose distractors are *meanings of other proverbs in the same language* (in-domain negative sampling). The "easy" baseline.
- **S2 (Strategy 2)** — MCQ variant whose distractors are *LLM-paraphrased near-misses* of the gold meaning (generator qwen3-32b, cross-family from the committee). The "hard" adversarial condition.
- **Fill-in-the-blank (FiB)** — cloze task: a word is masked in the proverb; the model supplies the missing word. Scored with EM/NEM/ChrF under three conditions (gold word / paraphrase / sham proverb).
- **Generation task** — the model writes the proverb's explanation; scored with BLEU, ChrF, embedding similarity, and a gold-copying detector (`contains_gold`).
- **Prompt variant (v68)** — one of four distractor-generation instruction styles: `adversarial-hard-negative`, `adversarial-length-locked`, `overgenerate-select`, `taxonomy-guided`.
- **Prompting style (May pilot)** — how the *evaluator* is prompted: `zero-shot`, `cot` (chain-of-thought), `few-shot`.

## Models
- **Committee (May)** — the models whose answers were scored: `meta/llama-4-maverick-17b-128e-instruct` (NVIDIA), `allam-2-7b` (Groq, Arabic-centric), plus `llama-3.3-70b-versatile` in June.
- **Generator** — model that creates distractors (May: `qwen3-32b`; v68: `qwen/qwen3.7-max`, `google/gemma-4-31b-it`, `google/gemini-2.5-flash`).
- **Auditors / blind committee (v68)** — 4 models that see only the four options (no proverb): llama-3.3-70b-instruct, mistral-small-3.2-24b-instruct, gemma-3-27b-it, deepseek-v3.2.
- **Encoders** — embedding models used as similarity baselines: mBERT, XLM-RoBERTa, AraBERT, AfriBERTa.
- **Same-family exploitation** — an evaluator recognizing/favoring its own family's generated text (observed: Meta generator + Meta evaluator scored 57.8% on generated vs 26.7% on human-written distractors).

## Metrics
- **Accuracy (strategy)** — correct letters ÷ valid (non-error) evaluations.
- **S2 strict** — S2 accuracy restricted to items with real paraphrase distractors (fallback=False).
- **Fallback rate** — share of items whose distractors were replaced by generic placeholders or corpus samples.
- **Consensus accuracy (v68)** — share of MCQs where the blind committee's majority vote equals the gold letter.
- **Perfect consensus** — share where all 4 auditors agree.
- **HCW (High-Consensus-Wrong)** — share where ≥75% of auditors agree on the *wrong* answer; the core shortcut-failure signal.
- **EM / NEM / ChrF** — exact match / normalized exact match / character n-gram F-score (FiB; ChrF also in Generation).
- **BLEU** — n-gram overlap score (Generation).
- **`contains_gold`** — flag that a generated explanation copies the gold explanation.
- **Fleiss κ / Cohen κ** — standard agreement coefficients among many / two raters.
- **McNemar's test** — paired statistical test comparing two conditions on the same items (used for S1 vs S2).
- **Holm correction** — multiple-comparison p-value adjustment.

## Pipeline and infrastructure
- **Contamination filter** — removal of ~25 famous proverbs that LLMs have memorized (~8.3% of English).
- **Corpus fallback sampler** — when filters reject generated distractors, replacements are sampled from *other proverbs' meanings*; identified as the main quality bottleneck in v68.
- **NLI filter / leak filter / length parity** — semantic checks that reject near-paraphrases of the gold, gold-echoing text, and length-mismatched options.
- **Pre-flight health check** — trivial probe call ("reply B") before evaluation to drop dead models.
- **OpenRouter** — multi-provider LLM API gateway used from June 2026 (replaced direct Groq/NVIDIA after the June meltdown).
- **Kaggle kernel** — a Kaggle notebook execution. Versions v59–v70 are versions of the same kernel `mcq-pass-shortcut`.

## Versions and runs
- **v1–v4.3.4** — the original Groq-based pipeline's internal versions (Apr–May 2026); v4.3.4 = the May 23 N=150 pilot.
- **v59–v70** — OpenRouter notebook versions (June 2026). v68 = the completed 180-MCQ audit run (seed 20260615). v69 = planned ablation, never run. v70 = halted attempt (83/180 rows, $0.42).
- **run_20260523_224443** — the May v4.3.4 pilot run ID.

## Status labels
`PLANNED-NEVER-RUN` · `CODE-PRESENT-EXEC-UNVERIFIED` · `STARTED-INCOMPLETE` · `COMPLETED-WITH-OUTPUTS` · `COMPLETED-ANALYSIS-MISSING` · `RESULTS-REPRODUCED` · `FAILED-OR-INVALIDATED` · `UNRESOLVED` — defined in `docs/experiments/EXPERIMENT_REGISTER.md`.

## Files and places
- **`proverb_mcq`** — the source repository (shortcut-audit track + all raw artifacts).
- **`actual_data/`** — cleaned 3-language proverb CSVs in proverb_mcq.
- **`original-data`** — the 6-language Kaggle dataset (2026-05-16) attached to the kernels.
- **`annotation_app/`** — the human-annotation web application (Next.js + Supabase) in proverb_mcq.
- **`Phase1_Reconstruction`** — the 22-document Phase 1 dossier (transferred here).
