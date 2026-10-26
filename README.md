# ProverbGap: Do language models understand what proverbs *mean*?

> **Status: a reconstructed research foundation — documentation only.** No new experiments have been run here. Every number below carries a status label saying exactly how well it is verified. And one thing to be clear about up front: the repository being public does not mean the underlying data is cleared for redistribution.

## At a glance

- **What this is:** the documented evidence behind an attempt to test whether language models understand the culturally grounded *meaning* of proverbs — as opposed to their translations or familiar wording — in English, Arabic, and Yoruba.
- **What exists today:** cleaned proverb collections in three languages (with unresolved rights questions), three piloted task formats, and recovered pilot outputs — but no human annotations at all.
- **What we have learned:** the early headline results can no longer be independently checked, because their raw files were overwritten; the one result we *can* fully recompute (the v68 audit) answers a different question — distractor quality, not cultural understanding.
- **What we are considering next:** having blinded human raters judge the recovered model explanations, then checking how well the automatic metrics agree with them. This is a hypothesis we want criticized, not an approved protocol.
- **What remains unresolved:** where the proverb data actually came from and whether it may be redistributed (especially Yoruba), the exact significance test behind the original pilot's headline claim, and the entire human-validation plan.

## Start here

Read this README first (about five minutes), then, in this order:

1. [`docs/GETTING_STARTED_FOR_RESEARCHERS.md`](docs/GETTING_STARTED_FOR_RESEARCHERS.md) — the 8-step onboarding path.
2. [`docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md`](docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md) — the current literature audit and proposed method.
3. [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) — the rights/provenance gate that blocks everything downstream.

---

## 1. What ProverbGap is

A proverb like *"A friend in need is a friend indeed"* does not describe friendship literally — it compresses cultural wisdom into figurative language. A model can **pass a translation test** (knowing the words) while failing the real test: knowing what the saying *means* in its culture, when it applies, and why. Standard benchmarks mostly check translation or surface wording, so they can overestimate understanding.

**Original research question (May 2026):**

> **Can large language models understand the culturally grounded meanings of proverbs, rather than merely recognize their translations, familiar wording, or surface-level interpretations?**

Each item was built from a **proverb record**: the original text, an English translation, and a cultural meaning/context. The original MCQ design created difficulty via two distractor strategies — **S1** (wrong options = meanings of other same-language proverbs) vs **S2** (wrong options = near-miss paraphrases written by a different model family).

**Proposed research question (2026-10-26 — provisional, open to critique):**

> **Across English, Arabic, and Yoruba proverb-generation outputs, how well do automatic evaluation metrics align with blinded human judgments of meaning fidelity, and how does that alignment vary by language and task?**

In practice this would mean: take the generation outputs we already have (no new model calls), have blinded raters judge how faithfully each one states the proverb's meaning, and measure how closely each automatic metric — BLEU, chrF, embedding similarity, possibly an LLM judge — matches those human judgments. Task A (literal-meaning explanations) and Task B (culturally equivalent translations) would be analyzed separately, since they were different prompts with different reference fields.

Two boundaries matter. First, the pilot prompts never asked about usage, so these outputs say nothing about *pragmatic appropriateness*; testing that would need a new usage-scenario generation run, proposed separately with its own small budget cap (≤$2). Second, the three languages use different proverbs and would use different rater pools, so comparisons across languages stay descriptive.

Studying proverbs in African languages is not novel on its own, and we are not claiming it is. What would make this worth doing is the evaluator-validity angle, and that claim has to survive the related-work audit. If you know of work we have missed — or think this framing is wrong — we would rather hear it now than after the protocol is frozen.

## 2. What exists today

**Data** (collected Mar–May 2026; preserved as the Kaggle dataset [`original-data`](https://www.kaggle.com/datasets/abrahamsunday123/original-data) and local copies in the source repository `saaga23/proverb_mcq`):

| Language | Rows (verified) | Rights status |
|---|---|---|
| English | 2,278 | scrape sources undocumented |
| Arabic | 913 | source unidentified |
| Yoruba | 3,974 | source attribution **unresolved** (copyrighted book vs a tracked "Strict_EMNLP_Yoruba_Corpus" workbook) |
| French/German/Spanish | on Kaggle (counts unverified) | outside current scope |

Column-level schemas are documented in [`docs/data/DATA_DICTIONARY.md`](docs/data/DATA_DICTIONARY.md), and the record flow in [`docs/data/DATASET_LINEAGE.md`](docs/data/DATASET_LINEAGE.md). No raw data is distributed from this repository. One caveat worth knowing early: proverb data — including files that were later removed from the old repository — is still retrievable from its public Git history; we verified this in October 2026 ([`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) §3.1).

**Experiments actually run:**

| Format | Status |
|---|---|
| **MCQ** (pick the meaning, A–D) | ✅ May 2026 pilot (150 proverbs × 2 strategies → 300 questions); responses not preserved |
| **Fill-in-the-blank** (complete a masked word) | ✅ 30-item Kaggle pilot (2026-05-19) — feasibility only; all 90 predictions used fallback extraction; real-context = sham-context EM |
| **Generation** (explain / culturally translate) | ✅ Kaggle pilot (2026-05-19): 2,160 attempts, 90 proverbs × 6 models; **outputs recovered — the basis of the proposed audit** |
| **Human validation** | 🛠️ Sampling + annotation app exist; **zero annotations collected** |

Also: a completed 180-question **shortcut-audit dataset** (v68, June 2026) — but it measures distractor quality, not cultural understanding (see §5).

## 3. What we have learned — and the evidence behind each claim

| Claim | Evidence status |
|---|---|
| May pilot: S1 86.8% (651/750) vs S2-strict 62.5% (369/590) | ⚠️ **Historically verified, not reproducible** — checked on 2026-05-24 against files later overwritten; the reported "McNemar" test is **unresolved** (form/pairing undocumented; a two-proportion χ² on the same marginals gives 106.9) |
| "S2 real-paraphrase accuracy 24.9% (below random)" | ⚠️ **Reported but unverified — and misattributed** to the pilot; it belongs to small N=50 runs and fits neither run's arithmetic |
| v68 audit: committee accuracy 56.7% (102/180), HCW 27.8% (50/180) | ✅ **Reproduced** from raw audit data — measures *distractor quality*, **not** cultural understanding |
| Generation pilot: 77.6% success across 6 models; gold-copying 3.7–11.2% | ✅ **Reproduced** from the recovered Kaggle output — task feasibility, not cultural understanding |
| FiB/Generation at scale; N=700; human validation; FR/DE/ES | ❌ Never run |

## 4. Limitations and open problems

- **No human annotations** — nothing about cultural understanding has yet been checked by human raters.
- **S2 construct validity** was disputed and never resolved; the May primary response files were overwritten, so headline figures rest on contemporaneous verification reports only.
- **Rights and provenance are unresolved for all three languages** (see §2); until they are, neither a public data release nor annotation of the source items can go ahead.
- **The pilot prompts only ever asked about meaning.** Task A requested a literal explanation and Task B a cultural equivalent; neither asked when or where the proverb applies, so the outputs cannot say anything about pragmatic use.
- **Model success rates varied widely** (34.7%–96.9%), so missing outputs need a prespecified rule; and since the 90 items are different proverbs per language, cross-language contrasts can only be descriptive.
- Full discrepancy record: [`docs/audit/EVIDENCE_DISCREPANCIES.md`](docs/audit/EVIDENCE_DISCREPANCIES.md).

## 5. The proposed method (provisional)

The pilot would only start after four gates: data rights sorted, the rating rubric frozen, raters recruited (target Fleiss κ ≥ 0.6), and the deterministic checks green.

Two raters per language would judge how faithfully each output states the proverb's meaning, on a stratified slice of the recovered generations — 10–15 proverbs per language × 3–4 models × 2 tasks × 2 strategies, roughly 360–720 outputs in total. With two raters that is 720–1,440 individual ratings, or about 9–24 hours of work per rater.

The primary outcome is the agreement between those human ratings and each automatic metric, computed per language and per task (BLEU, chrF, embedding similarity; an LLM judge only as a small ≤$2 add-on). Differences across languages would be reported as observations, not causal findings. Pragmatic appropriateness stays out of scope until the separately capped usage-scenario run is approved.

Full reasoning, the prior-work comparison, and the go/no-go gates are in [`docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md`](docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md).

## 6. Relationship to `proverb_mcq` (separate track)

After the original track stalled, the work pivoted to distractor **shortcut resistance** — that track (v68 dataset, failure taxonomy, EACL 2027 draft) lives in [`saaga23/proverb_mcq`](https://github.com/saaga23/proverb_mcq). It is methodologically useful (generation code, filters, annotation app) but does **not** answer the cultural-understanding question, and its results are not evidence about cultural competence here. See [`docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md`](docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md).

## 7. Data and reproducibility notes

- **Deterministic, no-cost recheck** of every reproduced number: `python docs/decisions/supporting/recompute_checks.py --old-repo <proverb_mcq path>` (details: [`docs/decisions/supporting/RESULTS.md`](docs/decisions/supporting/RESULTS.md)).
- Recovered Kaggle pilot outputs are re-downloadable with `python -m kaggle kernels output …` (commands in RESULTS.md). The May pilot's raw responses are **not recoverable locally** — only a Kaggle web-UI version export could restore them.
- Historical context: [`docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md`](docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md) and the full register: [`docs/experiments/EXPERIMENT_REGISTER.md`](docs/experiments/EXPERIMENT_REGISTER.md).

## 8. Next steps (all pending owner decisions — nothing has started)

The Phase 1 reconstruction, the evidence audit, and the October 2026 literature audit are complete. Everything in this list is still to do — no new experiments have been run.

1. **Complete the literature/novelty decision** — confirm or narrow the provisional research question ([audit](docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md)).
2. **Resolve source provenance and permissible use** for Yoruba, Arabic, and English (disposition sheet: [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) §3.2) — this gates everything downstream.
3. **Finalize construct definitions, human rubric, and preregistered analysis** (meaning fidelity first; pragmatic axis only via the gated ≤$2 condition).
4. **Complete deterministic reproducibility and evaluator-validity checks** (no-cost).
5. **Run the small, blinded human-anchored pilot** only once gates 1–4 pass, under a written budget cap.
6. **Scale and prepare a paper** only if the evidence supports the contribution.

## Documentation map

```text
README.md, CHANGELOG.md, DATA_RIGHTS_AND_PROVENANCE.md
research/RESEARCH_SCOPE.md                  ← the 8 original research directions, status-labeled
docs/GLOSSARY.md                            ← every term defined
docs/GETTING_STARTED_FOR_RESEARCHERS.md     ← 8-step onboarding
docs/reconstruction/            (8 docs)    ← Phase 1 evidence dossier
docs/planning/phase7/           (14 docs)   ← planning artifacts (not findings)
docs/data/                                  ← DATA_DICTIONARY.md, DATASET_LINEAGE.md
docs/experiments/                           ← EXPERIMENT_REGISTER.md, LOCAL_AND_KAGGLE_ARTIFACT_CROSSWALK.md
docs/research/                              ← LITERATURE_AND_METHODOLOGY_AUDIT.md, ORIGINAL_VS_SHORTCUT_RESEARCH.md
docs/newcomer_audit/                        ← NEWCOMER_COMPREHENSION_AUDIT.md
docs/audit/                                 ← EVIDENCE_DISCREPANCIES.md
docs/decisions/                             ← evidence-recovery memo + supporting calculations
```

*Raw datasets, generated MCQ files, and the shortcut-audit corpus remain in `saaga23/proverb_mcq` and are deliberately not copied here (see `docs/repository_transfer/TRANSFER_MANIFEST.md`).*
