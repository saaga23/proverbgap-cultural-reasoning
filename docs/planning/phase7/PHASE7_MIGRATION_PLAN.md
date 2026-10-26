# Phase 7 — MIGRATION_PLAN

**Goal:** A single coherent narrative must be chosen before any Phase-2 code or writing (the repo currently holds two incompatible narratives). This plan has one path per fork option; pick **one**.

---

## Path A — Restore the original benchmark (May direction)

**When to choose:** owner wants a *benchmark* paper with the S1/S2 accuracy gap as the core result.

### Pre-conditions (all must pass before new generation)
1. **S2 validity resolution** — re-analyze whether 62.5% is real or inflated by 24.9%-below-random paraphrases; document both numbers transparently (Document 05 §2). If S2 is unsalvageable, redefine "difficulty" via a new hard-negative set.
2. **Data clearance** — resolve Yoruba ISBN + remove 60 Yoruba rows from any public CSV OR obtain permission; recover EN scraped URLs + AR MID source.
3. **Budget** — OpenRouter credits for N=5 ablation (v69) → N=15 (v70) → N=700 scale (~$2.56 at N=15; higher at N=700); plus human validation budget ($200–300).
4. **S1 answer-key integrity** — re-confirm `audit_answer_key_consistency.py` passes before scaling (history doc §7).

### Steps
1. Restart v69 ablation at N=5 (`USE_LLM_FALLBACK=True`, gpt-4.1-nano); verify HCW<15% & partial+fallback<30%.
2. If pass → v70 at N=15; if fail → iterate NLI/leak thresholds (v68 report §7.5).
3. If N=15 gates pass → scale to N=700 (1.7h Kaggle; reduce workers, jitter, provider rotation).
4. Restore FiB (§7.3) and Generation (§7.4) as real tasks; locate or regenerate the 16K/25K-row artifacts.
5. Re-add 3 eval styles (zero/CoT/few-shot) and leakage heuristic (Document 05 §1); skip CoT for models with NaN.
6. Run 100-item KNIGHT-style human validation.
7. Rewrite README/paper to **single narrative**; delete or archive the July audit framing.

**Risk:** S2 may be unrecoverable; EN/AR/YO release depends on rights. **Do not start until pre-conditions 1–2 clear.**

---

## Path B — Adopt the v68 shortcut-audit methodology (July direction)

**When to choose:** owner wants a *methodology + failure-taxonomy* paper, publishable from v68 alone.

### Pre-conditions
1. **Human validation** — run the 60-item audit sample (`paper_first_outputs_2026-06-22_10-42-02/human_validation_sample_60.csv`) to ground the HCW gate in human labels (Fleiss κ ≥ 0.6 target).
2. **Yoruba rows** — decide purge vs. retain; document liability.

### Steps
1. Finalize v68 metrics via existing no-API scripts (`analyze_v68.py`, `analyze_bootstrap_cis.py`, `analyze_statistical_tests.py`; pytest).
2. Add formal tests for variant-specific HCW + per-variant replacement breakdowns (README §10 "next steps (no budget needed)").
3. Write failure taxonomy (5 modes) with v68 examples (Document 05 §4; v68 report App. 8.2).
4. Freeze citation bundle: generated MCQs, audit votes, summary, 7 figures, bootstrap CIs.
5. Set submission venue (EACL 2027 ARR if resubmit path; else EMNLP/ACL rolling).

**Risk:** N=5 is small for a benchmark claim; paper is methodology-only.

---

## Path C — Hybrid (v69 bridges both)

**When to choose:** owner wants S2 accuracy *and* distractor-audit quality.

### Pre-conditions
1. Same as A (S2 validity, rights, budget).
2. v69 must pass: HCW<15%, partial+fallback<30%, cost<$1.50 (v68 report §7.2 gates).

### Steps
1. Run v69 ablation (USE_LLM_FALLBACK=True). **If gates pass → Path A at scale.** **If fail → fall back to Path B.**
2. Report both the v68 audit (HCW) AND, where valid, the S1/S2 accuracy gap — with explicit caveats on S2.
3. Reconcile numbers: May draft (86.8/62.5) is **N=150 Groq**; v68 is **N=5 OpenRouter audit**; never mix.

**Risk:** Highest budget/complexity; requires v69 to succeed to avoid a thin paper.

---

## Recommendation (Phase 1 level)
- If budget is **tight / uncertain**: **Path B** — v68 + failure taxonomy is publishable now; human validation is the only blocker.
- If budget is **available AND S2 validity is resolved**: **Path C** → A.
- Never ship both narratives in one paper — pick one and archive the other (`docs/Phase1_Reconstruction/` already separates them).
