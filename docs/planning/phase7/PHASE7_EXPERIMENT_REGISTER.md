# Phase 7 — EXPERIMENT_REGISTER
Canonical register: `04_EXPERIMENT_REGISTER.md`.

**Phase A (Groq):** v1→v4.3.4 (Apr 24 → Jun 22). Headline: v3/v4.3.4 N=150 pilot, S1 86.8% / S2 62.5% (McNemar p<0.001).

**Phase B (OpenRouter audit):** v65→v70 (Jun). Production = **v68**: 180 MCQs (15 proverbs × 4 variants × 3 generators), seed 20260615, $0.85, 720 votes (0 missing). Gates: 4/6 fail (HCW 27.8% vs <10%).

**v69:** planned LLM-fallback ablation, `USE_LLM_FALLBACK=True`, `openai/gpt-4.1-nano` — **never executed** (v69/ has no CSV/summary; `04_` Phase B row confirms).

**v70:** halted — 83/180 rows, $0.42, `generation_done=False`, `audit_done=False`, OpenRouter 403 (`04_` Phase B row + `pool_state.json`).

All specs (config, model pools, gates) in `04_` and in-source comments.
