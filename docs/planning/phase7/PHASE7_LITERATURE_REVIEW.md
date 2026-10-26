# Phase 7 — LITERATURE_REVIEW

## Proverb / figurative-language benchmarks
- **ProverbEval** (Azime et al., NAACL 2025) — Ethiopian languages; MCQ + FiB + Generation. *Original comparison target; motivated the 3-format plan.* See `02_` §3 / memory competitor entity.
- **Jawaher** (NAACL 2025) — 10,037 Arabic proverbs, 20 dialects, translation + explanation.
- **PRONE** (CODI 2025) — 2,830 Nepali MCQs, human-written distractors.
- **MasalBench** (Kalhor et al., 2026) — Persian, LLM-generated distractors + curation.
- **Kinaya** (EACL 2026) — "Pragmatics Gap," Egyptian Arabic (14pp gap). Referenced in memory graph.

## Distractor generation methodology
- **DiVERT** (Fernandez, EMNLP 2024) — distractors anticipate learner misconceptions.
- **GSM-DC** (Yang, EMNLP 2025) — controlled distractor injection improves OOD robustness.
- **D-GEN** (ACL 2025) — explicitly forbids paraphrasing the correct answer (enforced in original S2).
- **Joint Generation of Distractors** (CMC 2025) — BERTScore/cosine relevance.
- **SEFD** (PMC 2025) — high semantic similarity persists after LLM paraphrasing (validates embedding gates).
- **SemEval 2025** — multi-qa-mpnet cosine 0.5 threshold for hallucination detection.
- **DG Survey** (EMNLP 2024) — plausibility/incorrectness/diversity/fluentness dimensions.
- **DISTO** (EDM 2024) — in-domain negative sampling effectiveness (basis of S1).

## Same-family / stylistic bias
- **Panickssery et al. (NeurIPS 2024):** evaluator models favor their own family's generations. *Root cause of v1 same-family exploitation.*
- **Ackerman & Panickssery (ICLR 2025):** chat/instruct retain family fingerprints; base models lack them.
- **Sun et al. (2025):** 97.1% cross-family vs 59.8% within-family detection.
- **Dubois et al. (EMNLP 2025):** nucleus (top-p) sampling least detectable; *justified temperature=0.7 in original S2.*
- **Krishna et al. (NeurIPS 2023):** DIPPER cross-model paraphrasing drops DetectGPT 70.3%→4.6%; *justified qwen3-32b generator ≠ Meta/Saudi committee.*

## Shortcut learning in MCQ
- **Du et al. (2022):** lexical/overlap/position/style shortcut taxonomy.
- **Zhou et al. (EMNLP 2024 Findings):** occurrence/style/concept shortcuts; length-normalization validity.
- **Zheng et al. (ICLR 2024):** token bias primary, position secondary.
- **Gupta et al. (2024):** answer reordering drops MMLU 13pp.

## LLM-as-a-judge / committee evaluation
- **Gu et al. (2024):** LLM-judge brittleness.
- **AgentProp-Bench** (Gurram, 2026): report agreement + bias + calibration.
- **Language Model Council** (Zhao, NAACL 2025): heterogeneous pools improve robustness — *basis of 4-model audit committee.*
- **Roundtable Policy (2025):** confidence-weighted consensus over flat majority — *not adopted; v68 uses ≥0.75 flat consensus.*

## Low-resource evaluation
- **AmharicStoryQA** (2026): 20–35% collapse on Amharic narrative.
- **EACL 2026** (Egyptian Arabic): 14pp Pragmatics Gap.
- **BEA 2025:** LLM performance correlates with training-data representation.
- **KNIGHT (2025):** 100-item human validity audit standard — *original human-validation target.*

## Notes
- The original `docs/ProverbGap_Paper_Draft.md` References (§8) list these; the v68 audit paper (`paper/proverbgap_eacl2027.md`) cites the same corpus plus the failure-taxonomy literature. No new external sources were fetched in Phase 1.
