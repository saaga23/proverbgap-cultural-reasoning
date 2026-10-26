# Phase 7 — FAILURE_LOG

## Phase A failures (Groq) — `07_MODEL_AND_EVALUATION_HISTORY.md` §7 + history doc §2/§6
1. **Position bias (v1):** A chosen 85.6% vs B/C/D 64–67%. → seeded per-model shuffle.
2. **Same-family exploitation (v2.2):** Meta gen + Meta eval scored 57.8% vs 26.7% S1 (57.8% on generated vs 26.7% on human-written). → switched gen to qwen3-32b.
3. **GPU model collapse:** ALLaM-7B garbled, AfroLLaMA memorization, BLOOM OOM. → API-only.
4. **API meltdown (v2):** DeepInfra 402, SambaNova timeout, Cerebras 404, Groq 15,131 rate-limited. → 8-key rotation + health retries; committee 5→2.
5. **S2 fallback explosion (v3):** 37.8% (Yo 43.3%). → dual-gate (length+Jaccard 0.25) + retries → 21.3%.
6. **kNN→numeric distractors (v3):** produced "20/23/30" options. → abandoned.
7. **MSP→trivial 100% (v3):** explanations, not paraphrases. → abandoned.
8. **S2 construct invalidity (Jun 4 audit):** 62.5% mixes 24.9% real-paraphrase (below random) + high fallback. → pivoted (never fixed). See `05_` §2.
9. **Answer-key corruption (v4.1):** S1 generated twice; MCQ file ≠ eval results → S1 14.7%/S2 0.0%. → v4.2 fix + `audit_answer_key_consistency.py`.
10. **v4.3.3 catastrophic regression:** (85.4/69.3→24.2/0.0) infrastructure cascade (NVIDIA timeout → Groq flood → 769/790 failed). → v4.3.4 hardened (health retries, worker-cap).

## Phase B failures (OpenRouter audit) — v68 report §6 + `05_` §3
11. **v68 gates fail (4/6):** HCW 27.8% (vs <10%), perfect-consensus 41.7% (vs <30%), partial+fallback 43.9% (vs <15%), hard-fallback 16.1% (vs <5%). Root: **corpus-fallback sampler** (43.9% touch; NLI+leak reject 71% of replacements).
12. **v69 never executed:** budget exhausted before start.
13. **v70 halted ($0.42):** OpenRouter 403 budget limit at 83/180 rows, before audit.
14. **Cross-lingual asymmetry:** Arabic 1.52 vs English 0.43 fallback/MCQ; Yoruba 1.03, HCW 33.3%.

See `03_CHRONOLOGICAL_RESEARCH_TIMELINE.md` §Decision log rows D1–D9.
