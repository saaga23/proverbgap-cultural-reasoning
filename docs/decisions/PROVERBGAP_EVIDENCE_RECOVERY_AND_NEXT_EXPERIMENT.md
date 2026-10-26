# Decision Memo — Evidence Recovery and the Next Cultural-Reasoning Experiment

**Date:** 2026-10-26 · **Author:** evidence-audit pass (Kilo) · **Status:** recommendation for owner review — no experiment has been run
**Evidence labels used throughout:** **Reproduced** (recalculated here from surviving primary data) · **Primary evidence recovered, analysis incomplete** · **Historically verified, not currently reproducible** · **Reported but unverified** · **Contradicted** · **Inaccessible** · **Not run**.
All artifact paths are in the source repository `saaga23/proverb_mcq` unless marked *(this repo)* or *(Kaggle)*. Supporting calculations: [`supporting/recompute_checks.py`](supporting/recompute_checks.py) + [`supporting/RESULTS.md`](supporting/RESULTS.md).

---

## Executive decision summary

1. **The original MCQ pilot cannot be independently recomputed today.** The surviving `evaluation_results.csv` is the *June 8/9 failed Kaggle run* (2,440/2,700 rows are API errors; every S2 evaluation failed) — not the May 23 pilot. Git history contains only the same June files, and the May kernel's successful run is an earlier version that the Kaggle CLI cannot export. The May figures (S1 651/750 = 86.8%; S2-strict 369/590 = 62.5%) are **historically verified, not currently reproducible**: the May 24 cross-verification report checked them against the then-live files and log, both since overwritten.
2. **The 24.9% claim is not reproducible and is internally inconsistent.** The memory-graph export attaches three different "real-paraphrase accuracy" figures (24.9%, 30.0%, 31.5%) to companion fallback accuracies (89.6%, 88.8%). Arithmetic shows 30.0% (Run 22) and 31.5% (Run 23) are consistent with their reported S2 overalls (35.6%, 36.9%) **but 24.9% fits neither**. Moreover, all three belong to the small N=50 runs of late May, not to the N=150 pilot — Phase 1 misattributed them. The claim stays **reported but unverified**, and the attribution error is now corrected.
3. **The FiB and Generation pilots establish feasibility, not findings.** FiB: a real 30-item, three-condition cloze pilot ran end-to-end (recovered from Kaggle), but every answer was extracted via last-line fallback and real-context vs sham-context performance was identical (EM 0.133 vs 0.133) — a feasibility result only. Generation: 2,160 attempts over 90 proverbs × 6 models completed with 77.6% success; gold-copying is 3.7–11.2% (the "DeepSeek-R1 100% gold copying" memory claim is **contradicted** — DeepSeek-R1 was not even in the run).
4. **Recommended next experiment:** a **small, pre-registered Generation-first pilot** (explanation of cultural meaning, with the translation-only condition as the control), with the FiB three-condition design as the fallback. Rationale and the ten validity gates are in §5. The single highest-leverage recovery action remains exporting the May 23 kernel version from the Kaggle web UI.

---

## Evidence inventory and access log

| Source | Status | What it establishes |
|---|---|---|
| Old-repo working tree (read-only) | inspected | Current artifacts incl. `actual_data/`, `kaggle/run_logs/v59–v70`, `annotation_app/`, `submission_package_2026-08-02/` |
| Old-repo Git history (22 commits, 2026-05-16 → 2026-08-11) | inspected | **No May v4.3.4 eval data was ever committed** (only the June failed run, first committed 2026-06-15). Recovers: full `memory.md` (220 KB), `GENERATION_QUALITY_REPORT.md`, `audit_behavior_report.md`, `verification_*.md`, April-era `_unzipped/mcq_*.csv` (see D-17), `original_data/` CSVs |
| May 24 verification reports (`docs/verification_paper|mentor|cross.md`) | inspected | Contemporaneous verification of the pilot numbers + found paper defects (consensus-table mislabel; 7,172 vs 7,488 arithmetic; allam error-excluded leakage) |
| Memory-graph export `.archive/memory_exports_2026-06-19/memory_proverbgap_filtered.json` | inspected | Source of the 24.9%/30.0%/31.5% claims and Run 22/23 records — narrative level |
| Kaggle API (authenticated; `python -m kaggle`) | inspected; **no executions launched** | Kernel list/status; dataset file lists; **output downloads** for the FiB and Generation kernels |
| Kaggle `proverbgap-mcq` earlier versions | **Inaccessible** via CLI | Needed to recover the May 23 raw outputs (see §A1) |
| Kaggle kernel sources (FiB, Generation) | pulled (code only) | Task/prompt/metric implementation verified |
| Supabase annotation backend | **Inaccessible** | Whether any human annotation was ever collected |

---

## Investigation A — the original MCQ pilot

### A1. Exact run and recovery status

- **Run:** `run_20260523_224443` (v4.3.4), 2026-05-23; N=50 proverbs/language × 3 languages; 150 S1 + 150 S2 MCQs; committee `meta/llama-4-maverick-17b-128e-instruct` + `allam-2-7b`; styles zero-shot/CoT/few-shot (CoT skipped for maverick); 4 encoder baselines; per-model seeded position shuffle. **Historically verified, not currently reproducible.**
- **What survives:** the MCQ *question sets* structure (the committed `mcqs_strategy1/2.csv` are June-era but share all 150 sample_ids across S1/S2), the May 24 verification reports, and the April-era MCQ generation data in Git history (below). The May *responses* (`evaluation_results.csv` with 1,500 valid API evaluations), the run log, and `FINAL_AUDIT_v434.md` were in `kaggle_analysis/Last_run/` and were overwritten by June-run downloads; they were never committed to Git.
- **Recovery route (owner, ~15 minutes):** Kaggle web UI → kernel `proverbgap-mcq` → **Versions** → the 2026-05-23 version → download output. The CLI exposes only the latest version, whose retrieved log shows a *failed* May 21 re-run (no API keys attached; `original-data` dataset not attached). This export would make S1/S2, per-language, per-model, and the significance test fully recomputable.
- **New discovery (D-17):** the repo's first commit (2026-05-16) contains a **large April-era MCQ generation run** — `_unzipped/mcq_a_{zs,cot,cot_xl}_{language}.csv` with **2,000 Yoruba / 803 Arabic** rows × 22 columns (options, answer key, parse/complete/length-ratio/distinctness/quality scores), plus `_all_mcq_analysis.txt`. Notably `cultural_context_available = False` throughout — the earliest MCQ items were built **without cultural-context fields**, directly relevant to the research question. Register updated (ER-A1).

### A2. Recomputation attempts (all Reproduced, on what *does* survive)

Using [`supporting/recompute_checks.py`](supporting/recompute_checks.py):

- **June failed run (the surviving eval file):** 2,700 rows; S1 1,350 attempted → 260 valid (76.2% among valid); counting failures as misses reproduces the deprecated **14.7%**; **S2 valid = 0**. Conclusion: the surviving eval file cannot yield May numbers. (Reproduced.)
- **v68 audit (for calibration of what *can* be reproduced):** consensus accuracy 102/180 = 56.7%, perfect consensus 75/180 = 41.7%, HCW 50/180 = 27.8% — exact match to the register. (Reproduced.)

### A3. The McNemar claim — audited, not reproduced

The reported result is S1 651/750 (86.8%) vs S2-strict 369/590 (62.5%), "McNemar χ² = 131.3, p < 0.001" (`docs/ProverbGap_Paper_Draft.md` §5; verified 2026-05-24 in `verification_cross.md` against the then-live log). Audit findings:

1. **Unit of analysis:** S1 and S2 item sets share all 150 sample_ids (verified on the June-era files, which inherit the design), so pairing at (proverb × model × style) is structurally possible. But the two reported denominators differ (750 vs 590), so the reported test necessarily used some matched subset whose definition is not documented.
2. **Not reconstructable:** the contingency table (discordant pairs b, c), the pairing subset, the handling of API errors, and whether a continuity correction or exact binomial variant was used — the log that contained the test was overwritten.
3. **Plausibility check (not a substitute):** a two-proportion χ² on the verified marginals gives χ²(1) = **106.9** (z = 10.34) — the same order as the reported 131.3. This is consistent with a strongly significant gap but is **not** the reported statistic; it is possible the original analysis mislabeled a two-proportion test as McNemar. Both possibilities remain open.
4. **Classification:** **Historically verified, not currently reproducible.** The May 24 verifier did check the test against the run log, so this is stronger than anecdote — but a newcomer cannot re-derive it today.
5. **Analysis plan for any future paired comparison:** pre-register the unit (item × model × prompting-condition), require identical denominators across arms, define fallback/error exclusion **before** unblinding, report the 2×2 paired table (b, c) with continuity-corrected McNemar **and** the exact binomial version, and always report a bootstrap CI on the paired difference.

### A4. The 24.9% claim — resolved as misattributed and internally inconsistent

Findings (memory-graph export, entities "MCQ Task", "S2 Construct Validity Failure", "Run 22 N=50 Results", "Run 23 Unified Results"):

| Claim | Companion numbers | Arithmetic check | Verdict |
|---|---|---|---|
| "Real paraphrase accuracy **24.9%** (below 25% random)" — attributed to the June 4 FINAL_AUDIT | Fallback acc 89.6%, fallback rate 9.3% | Mixture 0.093×89.6 + 0.907×24.9 = **30.9** — matches **neither** reported overall (35.6, 36.9) | **Reported but unverified; internally inconsistent** |
| "Real paraphrases **30.0%** vs fallback **89.6%**" (Run 22, N=50) | S2 overall 35.6% | Mixture = **35.5 ≈ 35.6** ✔ | Internally coherent, still unverified (no raw data) |
| "Real paraphrases **31.5%** vs fallback **88.8%**" (Run 23) | S2 overall 36.9% | Mixture = **36.8 ≈ 36.9** ✔ | Internally coherent, still unverified |
| N=150 pilot S2-strict = **62.5%** (369/590) | Fallback acc 63.7% (102/160), overall 62.8% (471/750) | Verified 2026-05-24 | **Historically verified, not currently reproducible** |

Implications, stated conservatively:

- The "S2 is broken / below random" alarm belongs to the **small late-May runs**, not to the final pilot. In the final pilot the non-fallback S2 accuracy (62.5%) is far above chance; what remains disputed there is *why* (real cultural reasoning vs distractor artifacts) — not whether the number is near-random.
- The June 4 "CRITICAL — do not submit without fundamental redesign" verdict (memory entity) was therefore based on the N=50-era evidence. It is a real recorded decision, but its quantitative basis is unverified and partly inconsistent.
- **Phase 1 misattributed 24.9% to the N=150 pilot** — corrected here and in the discrepancy register (D-17/D-18). The claim's class: **Reported but unverified** (with the 30.0/31.5 variants *recomputable after recovery* of the Run 22/23 raw outputs, if they exist anywhere; none were found locally or in Git history — **Inaccessible/possibly lost**).

---

## Investigation B — what the FiB and Generation pilots establish

Recovered from Kaggle on 2026-10-26 (temp copies; re-download commands in [`supporting/RESULTS.md`](supporting/RESULTS.md)). Notebook sources pulled and inspected (code only).

### B1. Fill-in-the-blank pilot — **Primary evidence recovered, analysis incomplete → now analyzed descriptively**

- **Verified structure:** `nb_pilot_30_results.csv` = **30 unique proverbs** (10 EN / 10 AR / 10 YO), task a=20 / b=10; notebook implements a two-step cloze (reasoning then answer) with three conditions: **A** = original proverb context, **B** = paraphrased context, **C** = *sham-proverb control*. Metrics: Exact Match, Normalized EM, ChrF (sacrebleu; NFC normalization for Yoruba tone marks / Arabic diacritics — verified in code).
- **Recomputed descriptives (Reproduced):** all 90 predictions have extraction status `FALLBACK_LINE` (the parser fell back to "last line" — a protocol weakness, not a run failure); mean EM A **0.133** / B 0.100 / C **0.133**; mean ChrF A 0.169 / B 0.140 / C 0.190.
- **What this establishes:** (i) the FiB pipeline — masking, conditions, normalization, metrics — was **implemented and executed end-to-end**; (ii) at n=30 with a single model and last-line extraction, performance is near-floor and **condition A ≈ condition C**, i.e., this pilot provides **no evidence** that word-cloze performance tracks cultural meaning; (iii) it does **not** establish cultural understanding, generalization, or any model comparison. The "16,439 rows" memory claim remains unsupported (**Contradicted** in scale: no artifact of that size exists anywhere we can access).
- **Design lesson worth keeping:** condition C (sham proverb) is a genuinely good control — any future FiB run should keep it and pre-register "A ≫ C" as the validity signal.

### B2. Generation/explanation pilot — **Primary evidence recovered, analysis incomplete → now analyzed descriptively**

- **Verified structure:** `pilot_results.csv` = **2,160 attempts = 90 unique proverbs (30/language) × 6 models × 2 tasks × 2 strategies** (task a = literal-meaning explanation in English; task b = fixed cultural variant; strategies zs / cot_en). Models: LLaMA-3.1-8B, LLaMA-3.3-70B, Qwen3-32B, Gemma-4-31B, LLaMA-4-Maverick, Nemotron-120B (Groq-primary with NVIDIA/OpenRouter fallbacks — verified in code). 1,677 SUCCESS / 483 FAILED; the 483 failures match `retry_queue.jsonl` (483 records) — retries were queued, never executed.
- **Recomputed descriptives (Reproduced):** success by model — Gemma-4-31B 96.9%, Nemotron-120B 96.4%, Maverick 93.6%, LLaMA-3.3-70B 72.5%, LLaMA-3.1-8B 71.7%, **Qwen3-32B 34.7%** (the S2 generator model failed two-thirds of generation attempts — an important operational finding). **Gold-copying among successes: 3.7–11.2%** per model (highest: LLaMA-3.1-8B 11.2%). Mean BLEU 2.7–4.3; mean embedding similarity 0.153–0.182 (raw values; no threshold analysis exists).
- **Memory claim check:** "DeepSeek-R1 100% gold copying" — **Contradicted.** DeepSeek-R1 is absent from the run; the observed maximum gold-copy rate is 11.2%. The "25,190 clean Task A rows" claim is unsupported at this artifact (2,160 attempts).
- **What this establishes:** the generation task ran at moderate scale with a workable metric suite and a gold-copy detector; outputs are analyzable **today without new inference**. It establishes **nothing yet** about cultural reasoning: no aggregated analysis, no human reference for "good explanation", and low BLEU/semantic-similarity values are uninterpretable without a validated scoring rubric.

### B3. Format comparison

| Criterion | MCQ | FiB (cloze) | Generation |
|---|---|---|---|
| What is measured | Forced-choice meaning discrimination | Recall of the exact culturally salient word | Ability to explain cultural meaning in words |
| Primary evidence available | May responses overwritten; v68 audit-vote data yes (different question) | ✅ 30-item pilot output | ✅ 2,160 attempts |
| Independent recomputation possible | **No** (May) / Yes (v68, but that is the other track) | Yes (done, descriptive) | Yes (done, descriptive) |
| Major validity threats | Distractor quality, fallback contamination, key errors, position cues, translation shortcuts | Word choice ≠ meaning understanding; extraction fragility (90/90 fallback); sham-control needed | Reference-free scoring is hard; gold-copying; judge bias; verbosity effects |
| Human validation needed | Yes — distractor + key review | Yes — verify gold word uniqueness | Yes — rubric + graded explanations |
| Cost/implementation | Cheapest per item; pipeline exists (v68 code) | Medium; pipeline exists but needs extraction fix | Medium; pipeline exists; scoring needs rubric/LLM-judge validation |
| Suitable for the next pilot? | Only after distractor+key validity gate | Good **fallback** after extraction fix | **Primary** — closest to the construct, reusable data |

### B4. Four claim levels, stated separately

1. *Implemented & executed:* all three formats (MCQ May; FiB May 19; Generation May 19) — **Reproduced** from artifacts.
2. *Outputs analyzable:* FiB yes (done); Generation yes (done); MCQ-May no.
3. *Task/metric quality:* FiB extraction weak; Generation metrics implemented correctly but unvalidated against human judgment.
4. *Cultural reasoning:* **no format has yet produced a defensible measurement** of it. This is the honest headline.

---

## Investigation C — public-release boundary audit

Three questions kept separate: **(1)** citing a published work is ordinary scholarship and does not by itself require a university's approval; **(2)** redistributing copied text or derived datasets is a separate permission question; **(3)** code licensing is a separate, owner-controlled decision. Current documentation (this repo, `DATA_RIGHTS_AND_PROVENANCE.md`) already mostly respects this; the memo tightens the wording.

### Release-risk table (old repo = `proverb_mcq`, public; new repo = this one, public)

| Finding | Reference | Evidence confidence | Risk | Owner action |
|---|---|---|---|---|
| **Confirmed** — 142 CSVs tracked in the public old repo, incl. cleaned proverb collections and MCQ files with answer keys (EN/AR/YO) | `git ls-files` count | High (verified) | Redistribution of material with unresolved provenance (Yoruba book; Arabic source unknown) | Decide: keep (accept exposure), prune, or obtain permissions; dataset release separately gated |
| **Confirmed** — April-era `_unzipped/mcq_*.csv` (2,000 Yoruba + 803 Arabic items with meanings) **remain in public Git history** though removed from HEAD | first commit `198253b`; `git ls-files` = 0 at HEAD | High | Same as above, plus "deleted" ≠ gone | Owner decision: accept, or history rewrite (destructive — needs explicit approval; out of scope here) |
| **Confirmed — no live secrets** in current HEAD or any historical blob | `git grep` counts: 0 high-entropy matches for `gsk_*`, `sk-or-*`, `AIza*`, SSH keys across all 22 commits | High | None from Git itself | Keep credentials in untracked files / private Kaggle datasets; rotate `OPENROUTER_API_KEY` periodically since it transits a Kaggle dataset |
| **Confirmed** — `annotation_app/.env.local` exists **untracked** (ignored) in old-repo working tree | `git check-ignore` | High | Local-only exposure | Rotate Supabase/other keys; never commit |
| **Confirmed** — `kaggle/kaggle_openrouter_key/dataset-metadata.json` untracked; the key itself lives in a **private** Kaggle dataset | file listing; Kaggle file list | High | Low (metadata only) | Keep dataset private; consider renaming (`CC0` license tag on a credentials dataset is a mislabel worth fixing) |
| **Suspected** — Kaggle notebooks may embed data in saved outputs (`__results__.html` ~200 MB for Generation) | notebook conversion logs | Medium | Public leakage depends on notebook visibility | Owner: review kernel visibility settings |
| **New repo (this one): no raw data, no secrets** — verified again on this branch | secret scan + file inventory | High | — | Maintain documentation-only boundary |

### Recommended wording fixes (applied in the reconciliation below)

- Say: "The repository is public **documentation**; no dataset is released, and visibility does not assert redistribution rights."
- Cite Owomoyela (2005) as a bibliographic source with page-level provenance where known, while stating plainly that **the Yoruba text collection itself is not cleared for redistribution**.
- Do not imply the FR/DE/ES files are validated data; they are present but uninspected.

---

## 5. Recommended next experiment (recommendation only — not executed)

**Primary recommendation — "Explanation-with-controls" Generation pilot (G1), small and pre-registered.**

- **Design:** 30 proverbs/language (EN/AR/YO; the same 90 used in May keep continuity), 2–3 strong models (e.g., one open-weight + one closed), two conditions per item: **(C1) real proverb** → explain its cultural meaning; **(C2) translation-only baseline** → the model sees only the English translation (no proverb text) and must produce the same explanation; optionally **(C3) sham-proverb control** carried over from the FiB design. Scoring: (i) blind pairwise preference of C1 vs C2 outputs by human raters on "does the answer use cultural, non-literal knowledge", plus (ii) an LLM-judge calibrated against a small human-labeled set (the κ≈0.48 proxy-IAA anchor warns this needs calibration).
- **Why this format:** it is the only format whose evidence is fully recoverable and analyzable today; it directly targets the construct (cultural meaning beyond translation); the C1-vs-C2 contrast is the cleanest test of "understanding beyond translation"; and the generation pipeline (with gold-copy detection) already exists. It also avoids re-inheriting the S2 distractor-validity problems.
- **Fallback — FiB-v2:** the same 90 items with the **extraction fix** (structured answer format, no last-line fallback), the A/B/C conditions retained, and the pre-registered signal "A ≫ C on normalized EM". Run it only if the owner prefers cheaper runs first; treat its output as directional.

**Must-pass validity gates (go/no-go before any paid run):**

1. **Gold validity:** ≥2 independent reviewers (1 native/context-competent speaker per language where possible) confirm each proverb's meaning/context is defensible; disagreements adjudicated and logged.
2. **Task validity:** items where the gold explanation is recoverable from the translation alone are flagged and excluded or analyzed separately (this is C2's role).
3. **Control validity:** C2 (and C3 for the fallback) defined and pre-registered.
4. **Distractor validity:** n/a for Generation; if MCQ is ever revived, the v68 filter suite + independent distractor review are mandatory.
5. **Human review:** annotation protocol document, reviewer qualifications, agreement statistic (Fleiss κ), adjudication rule, and disagreement logging — reuse `annotation_app/` (proverb_mcq) rather than building new tooling.
6. **Data integrity:** immutable input snapshot (the Kaggle `original-data` dataset version + SHA-256 of the 90 selected records), row-ID audit, deduplication, leakage check against famous-proverb list.
7. **Statistical design:** unit = (proverb × model × condition); primary outcome = human-judged cultural-knowledge win-rate of C1 vs C2; exclusion rules pre-registered; bootstrap CIs; no unregistered post-hoc slices.
8. **Reproducibility:** pinned model IDs/temperatures, prompts committed as files, raw outputs saved per call with finish reasons, cost log.
9. **Budget gate:** a 5-proverb dry run; written maximum spend before the full run (previous burn: v68 $0.85 for 180 generation + 720 audit calls — the same order of magnitude is a sensible cap).
10. **Interpretation gate:** predefine, in writing, that a C1>C2 win-rate with CI excluding 0 supports "models use cultural knowledge beyond translation"; C1≈C2, or wins driven by verbosity/length, does not.

**Useful but deferrable:** model-family grid; additional languages (FR/DE/ES); CoT variants; automatic metric development; scaling beyond 90 items.

---

## Documentation corrections required (factual, evidence-backed)

| # | Current claim (where) | Evidence | Correction | Type |
|---|---|---|---|---|
| C-1 | Phase 1 register/dossier: 24.9% belongs to the N=150 pilot | Decomposition arithmetic (§A4) | 24.9/30.0/31.5 belong to N=50-era runs; pilot's strict S2 = 62.5%; label all variants "reported but unverified" | Factual correction |
| C-2 | Memory export: "DeepSeek-R1 100% gold copying" | Recovered pilot data: model absent; max 11.2% | Mark **Contradicted** | Factual correction |
| C-3 | Memory export: "16,439 FiB rows / 25,190 generation rows" | Recovered: 30 items / 2,160 attempts | Mark scale figures unsupported | Factual correction |
| C-4 | Register: FiB pilot "completed" (unqualified) | 90/90 last-line-fallback extractions; A≈C | Add "extraction fell back on every item; no cultural signal at n=30" | Status clarification |
| C-5 | Register: June-run eval file provenance | §A1 | Already corrected in this repo; keep (no change) | — |
| C-6 | New-discovery gap: April-era 2,000-item MCQ run undocumented | First-commit artifacts | Add to register (ER-A1) and data dictionary | Factual addition |
| C-7 | README: results table mixes verified and narrative claims | §A2–A4, §B2 | Add status column and evidence labels; note May data loss explicitly | Status clarification |

These are applied to the current-facing files in the reconciliation commit accompanying this memo (branch `docs/evidence-memo-2026-10-26`); historical documents are annotated, not rewritten.

## Ranked next steps with go/no-go gates

| # | Action | Gate to pass | Owner input needed |
|---|---|---|---|
| 1 | Export May 23 kernel version outputs (Kaggle web UI) | Files open + row counts match (1,500/1,200/150+150) | Yes — web UI access |
| 2 | Recompute S1/S2 + McNemar on recovered data | Contingency table derivable; pairing subset documented | No (once files exist) |
| 3 | Approve G1 pilot design + budget cap | Gates 1–10 checklist signed off | Yes |
| 4 | Gold-validity review of the 90 items (annotation app) | κ ≥ 0.6 among reviewers; adjudication log | Yes — recruit reviewers |
| 5 | 5-proverb dry run → full G1 | Dry-run cost ≤ agreed cap; extraction/parse rate ≥ 95% | Yes — budget approval |
| 6 | Analysis + memo update | Pre-registered analysis only | — |
| 7 | Only then: decide MCQ revival vs generation-scale-up | G1 outcome + recovered May analysis | Yes |

---

*Prepared without running any experiment, spending credits, executing any Kaggle notebook, or modifying the old repository. Every number above is either recomputed here (Reproduced), quoted from an inspected artifact (level noted), or explicitly marked unverified.*
