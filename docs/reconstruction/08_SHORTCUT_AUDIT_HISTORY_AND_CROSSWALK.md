# Phase 1 — Document 08: Shortcut-Audit History & Original↔v68 Crosswalk

**Status:** Completed
**Purpose:** Map the **original accuracy-based** research direction onto the **v68 shortcut-audit** framing — and reconcile the two so Phase 2 can decide whether to (a) restore the original benchmark, (b) adopt the audit methodology, or (c) keep the hybrid. Also documents the July paper-first reframing and the EACL 2027 status.

---

## 1. The two framings, side by side

| Dimension | Original (May 2026) | v68 shortcut-audit (Jun 22) |
|---|---|---|
| **Paper title** | *ProverbGap: A Cross-Lingual MCQ Benchmark for Proverb Understanding with Adversarial Distractor Generation* | *Hardened Adversarial Distractor Generation for Low-Resource Figurative Language: A Case Study in Proverb Understanding* (reframed, July) |
| **Research question** | Do LLMs understand proverbs, or exploit shortcuts? → measured as S1 vs S2 *accuracy gap* | How do you build MCQ distractors that resist shortcut solutions? → measured as audit *gate pass/fail* |
| **Unit of evaluation** | Model answer accuracy on MCQs | Distractor quality (blind audit) |
| **Key number** | S1 86.8% vs S2 62.5% (McNemar p<0.001) | HCW 27.8% (target <10%), perfect-consensus 41.7% (target <30%) |
| **Committee role** | *Answer scorer* (sees proverb + question) | *Blind distractor auditor* (sees only 4 options) |
| **Difficulty signal** | Accuracy gap → scale to N=700 | HCW/fallback rates → do not scale / fix first |
| **Verdict** | "Gap is significant → proceed" | "4/6 gates failed → do not scale; v69 ablation first" |
| **Dataset size** | N=150 pilot (planned N=700) | N=180 (5/lang) / N=5 per language |
| **Formats** | MCQ (FiB/Gen planned, §7 — not built) | MCQ only |
| **Publication target** | (EMNLP-ambiguous; "top venues") | EACL 2027 ARR (deadline Aug 3 2026) |
| **Submission status** | — | **UNCROSSED** (no paper ID / decision) |

**Core divergence:** the original asks *"can models solve these MCQs?"* The v68 audit asks *"would these MCQs mislead a model that only sees the options?"* These are not comparable metrics — v68 does **not** reproduce 86.8%/62.5%, and it was never meant to.

---

## 2. Concept crosswalk (original → v68)

| Original concept | v68 equivalent | Changed? |
|---|---|---|
| S1 in-domain negative sampling (easy baseline) | — (no S1 in v68) | ❌ Dropped from audit framing |
| S2 cross-family LLM paraphrase (hard) | 4 adversarial generation *variants* (hard-negative, length-locked, overgenerate-select, taxonomy-guided) × 3 generators | ⚠️ Transformed: "S2" split into a 4-variant × 3-generator factorial |
| Committee answers MCQ (accuracy) | Committee votes blind, options-only (distractor audit) | ✅ **Role inversion** |
| S1→S2 accuracy gap = cultural-reasoning gap | HCW ≥0.75 wrong-consensus = shortcut leak | ✅ **Metric inversion** |
| 3 prompting styles (zero/CoT/few-shot) | None at audit stage | ❌ Dropped (eval styles ≠ gen variants) |
| Leakage heuristic (S1≥95% & drop≥20pp) | HCW gate (≥0.75 wrong consensus) | ✅ Renamed/replaced |
| Position-bias mitigation (seeded shuffle) | Position-balance *check* only (A/B/C/D=45 each, χ² p=0.322) | ⚠️ Mitigation → monitoring |
| Scale plan: N=150 → N=700 if gap significant | Scale plan: do NOT scale; v69 ablation first | ✅ **Blocked** |
| Corpus fallback (placeholder "Incorrect alternative") | Corpus-fallback *sampler* (other proverbs' meanings) | ⚠️ Evolved: became the *diagnosed bottleneck* |
| S2 fallback rate 21.3% (acceptable) | Hard-fallback 16.1%, partial+fallback 43.9% (gates failed) | ✅ Same mechanism, now a *failure mode* |

**The corpus fallback sampler** is the single continuous thread: in the original it was a minor 21.3% placeholder, accepted as part of S2; in v68 it is the **diagnosed bottleneck** (43.9% of MCQs touch it; produces confident-wrong HCW items).

---

## 3. The pivot chain (why original → audit)

1. **May 18, 2026 — Central thesis invalidated.** Memory graph: "Central thesis invalidated May 18 2026 — pivoted to standalone methodology paper." Trigger: FiB (16,439 rows) and Generation (25,190 rows) tasks explored and *abandoned*; DeepSeek-R1 100% gold-copying confirmed. The literal/cultural gap premise was no longer robust.
2. **June 4 audit — S2 construct validity flagged.** 62.5% S2 mixes real paraphrases (only 24.9%, below random 25%) with placeholder fallbacks (high). The headline number is internally inconsistent.
3. **June 13 — data corruption.** Answer-key shuffle bug → S1 14.7%, S2 0.0% in `main_results_table.csv` (deprecated `scale_readiness_report.md`).
4. **June 22 — v68 gates fail.** 4/6 shortcut-resistance gates fail (HCW 27.8%). v68 report §7 verdict: "corpus fallback sampler is the bottleneck."
5. **June 26 — budget exhaustion.** v69 never run; v70 halted at $0.42 (83/180 rows, OpenRouter 403).
6. **July 10 — paper-first reconciliation.** `gap_liability_analysis` exposes "2,313 MCQs / 86.8%-62.5%" vs v68 "180 MCQs" inconsistency. `EXECUTION_ITINERARY` caps human validation as "planned-only / external funding."

→ The shortcut-audit methodology (failure taxonomy, HCW gate) was **retrofit** to give publishable content *after* the original accuracy framing was found unsound.

---

## 4. Reconciliation: what was lost, what was gained

### Lost (original direction abandoned)
- The **Cultural/Literal Reasoning Gap** (S1 vs S2) as a publishable core result.
- **FiB and Generation tasks** (planned §7.3/7.4; 16K/25K rows produced then abandoned).
- **6-language plan** (reduced to 3: EN/AR/YO).
- **N=700 scaling** (never reached; stuck at N=5).
- **Human validation** (planned 100 items; never started; v68 plan-only 60 items).
- **S2 as a valid adversarial metric** (construct validity disputed).

### Gained (audit framing)
- **Blind options-only audit** — a cleaner distractor-quality diagnostic.
- **4-variant × 3-generator factorial** — richer generation-side analysis.
- **Failure taxonomy** (5 modes) grounded in real v68 data.
- **Bootstrap CIs** (10,000 resamples) and **statistical tests** (McNemar/Wilcoxon/Holm) on v68.
- **Reproducible pytest** (`test_v68_metrics.py`) + no-API recomputation scripts.

---

## 5. Current repo framing (README + paper/)

- **README.md** (current) faithfully reports v68 (HCW 27.8%, gates, 4 variants, blind audit) but **does not claim** the original 86.8%/62.5%. It only *historically* notes "Strategy 1 vs Strategy 2" in §3 as legacy context.
- **paper/proverbgap_eacl2027.md** — reframed as methodology + failure taxonomy (EACL 2027 ARR).
- **docs/gap_liability_analysis_2026-07-10.md** — explicitly documents the inconsistency between the May paper draft (2,313 MCQs claimed, 86.8%/62.5%) and v68 (180 MCQs) and recommends **not** carrying forward the 2,313-MCQ/86.8% numbers.
- **DATASET_CARD.md / GETTING_STARTED.md** — adopt the v68 audit framing; data blocked pending provenance.

**Net:** the repo has **two incompatible narratives** coexisting: the May paper draft (benchmark + accuracy gap) and the July README/paper (audit + failure taxonomy). They reference different datasets, metrics, and sizes. Phase 2 must choose one narrative (or explicitly reconcile).

---

## 6. EACL 2027 ARR status

| Item | Value |
|---|---|
| Target | EACL 2027 ARR |
| Deadline | **August 3, 2026** |
| Submission record in repo | **None** — no paper ID, no submission confirmation, no reviewer decision |
| README §10 | "submission status is **unconfirmed** and must be verified by the owner" |
| Paper draft location | `paper/proverbgap_eacl2027.md` (methodology + failure taxonomy frame) |

→ **EACL 2027 ARR submission is unconfirmed.** If the deadline has passed (Aug 3 2026 is in the past relative to "today" Oct 26 2026 per this session), the window was missed unless a resubmission/late path exists. **Open question for owner.**

---

## 7. Decision fork for Phase 2

| Option | Restore original benchmark | Adopt audit methodology | Keep hybrid |
|---|---|---|---|
| Keep May paper draft? | ✅ Yes (86.8/62.5) | ❌ No | ⚠️ Requires S2 validity fix |
| Scale to N=15/N=700? | ✅ Planned (needs budget) | ❌ N=5 only | ⚠️ Conditional on v69 |
| FiB / Generation? | ✅ Planned (§7) | ❌ Drop | ⚠️ Re-explore if valid |
| Human validation? | ✅ 100 items | ⚠️ 60-item audit-only | ✅ Both |
| Publishable now? | ❌ (S2 validity) | ✅ (v68 + failure taxonomy) | ⚠️ Needs v69 |
| Budget needed | High (N=700 + humans) | Low (v68 done; v69 ~$1) | Medium |

**Recommendation (Phase 1):** Do not resolve this fork in Phase 1 — it is a **planning decision** requiring the owner's venue/budget call. Document the fork here; flag as the single most important Phase-2 decision.
