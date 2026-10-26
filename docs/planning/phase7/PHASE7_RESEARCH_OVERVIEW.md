# Phase 7 — RESEARCH_OVERVIEW

> Companion to `docs/Phase1_Reconstruction/`. This file is the canonical project overview; the `01_..08_` docs are the evidence-backed detail.

## Project: ProverbGap

**Domain:** NLP evaluation of figurative-language (proverb) understanding by large language models.

**Two coexisting research directions (reconstructed in Phase 1):**

| | Direction A — Original benchmark (May 2026) | Direction B — Shortcut audit (Jun 22) |
|---|---|---|
| Title (draft) | *ProverbGap: A Cross-Lingual MCQ Benchmark… with Adversarial Distractor Generation* | *Hardened Adversarial Distractor Generation for Low-Resource Figurative Language* |
| Paper draft | `docs/ProverbGap_Paper_Draft.md` (v1.0, May) | `paper/proverbgap_eacl2027.md` |
| Core question | Do LLMs understand proverbs or exploit shortcuts? (accuracy gap) | How to build & audit distractors that resist shortcuts? |
| Metric | S1 86.8% vs S2 62.5% (N=150 pilot; McNemar p<0.001) | v68 audit: HCW 27.8% (4/6 gates failed) |
| Data | 7,172 proverbs / 6 langs; 3 benchmarked (EN/AR/YO) | 15 proverbs / 3 langs (N=5/lang) → 180 MCQs |
| Committee | 2-model (Meta + Saudi) answer scorer | 4-model blind options-only distractor auditor |
| Status | Thesis invalidated May 18 (S2 construct validity); 62.5% disputed | Completed dataset + methodology + failure taxonomy |
| Publication | EMNLP-ambiguous | EACL 2027 ARR (deadline Aug 3 2026 — **submission unconfirmed**) |

**Decision fork (owner):** restore Direction A (needs S2-validity fix + budget for N=700 + human validation) **or** adopt Direction B (v68 + audit is publishable now; needs v69 ablation to strengthen) **or** keep hybrid (needs v69 + careful number reconciliation). See `07_OPEN_QUESTIONS.md` and `08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md` §7.

## Why Phase 1 matters
The repo carries **two incompatible narratives** (May benchmark vs June audit) with conflicting sizes (2,313 MCQs vs 180), metrics (86.8%/62.5% vs HCW 27.8%), and datasets. Phase 1 inspects/verifies/documents so Phase 2 can choose a single coherent narrative without re-deriving facts.
