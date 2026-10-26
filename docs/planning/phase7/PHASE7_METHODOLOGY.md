# Phase 7 — METHODOLOGY

**Original (May):** two-strategy MCQ generation → 3-eval-styles (zero/CoT/few-shot) committee scoring + 4 encoder baselines → McNemar/χ²/bootstrap stats. See `02_ORIGINAL_RESEARCH_RECONSTRUCTION.md` §4 and `05_EVALUATION_METHODS_RECONSTRUCTION.md` §1.

**v68 (shortcut audit):** 4 variants × 3 generators → semantic filters (NLI/leak/length/blocklist) → corpus fallback sampler → **blind options-only** 4-model audit committee → HCW gate (≥0.75 wrong consensus). See `05_` §3 and `04_EXPERIMENT_REGISTER.md` v68 spec.

**Crosswalk:** `08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md` §2 (committee role inversion; metric inversion; S2→4-variant transform; corpus fallback as diagnosed bottleneck).

**Reproducibility:** `analyze_v68.py` / `analyze_bootstrap_cis.py` / `analyze_statistical_tests.py` + `pytest tests/ -v` — all no-API. See `05_` §6.
