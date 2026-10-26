# ProverbGap: Do language models understand what proverbs *mean*?

> **Status: reconstructed research foundation — documentation only.** No new experiments have been run in this repository. Historical numbers below carry explicit status labels; **public visibility does not mean the underlying data is cleared for redistribution.**

## At a glance

- **What this is:** a preserved evidence base for studying whether large language models understand the *culturally grounded meaning* of proverbs — not just their translations or familiar wording — in **English, Arabic, and Yoruba**.
- **What exists today:** cleaned tri-lingual proverb collections (rights unresolved), three piloted task formats, and recovered pilot outputs — but **zero human annotations**.
- **What we have learned:** the historical headline results are only *partially verified*; the one fully reproduced dataset (v68) measures distractor quality, **not** cultural understanding.
- **What we are investigating next (provisional):** a blinded, human-anchored audit of how well automatic metrics track human judgments of **meaning fidelity** — a hypothesis to be critiqued, not an approved protocol.
- **What remains unresolved:** data provenance and rights (especially Yoruba), the original significance-test reconstruction, and all human validation.

## Start here

1. This README (5 minutes).
2. [`docs/GETTING_STARTED_FOR_RESEARCHERS.md`](docs/GETTING_STARTED_FOR_RESEARCHERS.md) — the 8-step onboarding path.
3. [`docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md`](docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md) — the current literature audit and proposed method.
4. [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) — the rights/provenance gate that blocks everything downstream.

---

## 1. What ProverbGap is

A proverb like *"A friend in need is a friend indeed"* does not describe friendship literally — it compresses cultural wisdom into figurative language. A model can **pass a translation test** (knowing the words) while failing the real test: knowing what the saying *means* in its culture, when it applies, and why. Standard benchmarks mostly check translation or surface wording, so they can overestimate understanding.

**Original research question (May 2026):**

> **Can large language models understand the culturally grounded meanings of proverbs, rather than merely recognize their translations, familiar wording, or surface-level interpretations?**

Each item was built from a **proverb record**: original text + English translation + a cultural meaning/context. The original MCQ design created difficulty via two distractor strategies — **S1** (wrong options = meanings of other same-language proverbs) vs **S2** (wrong options = near-miss paraphrases written by a different model family).

**Proposed research question (2026-10-26 — provisional, open to critique):**

> **Across English, Arabic, and Yoruba proverb-generation outputs, how well do automatic evaluation metrics align with blinded human judgments of meaning fidelity, and how does that alignment vary by language and task?**

Scope boundary of that proposal: it analyzes **existing generation outputs only** (no new model inference), treats Task A (*literal-meaning explanation*, reference = translation) and Task B (*culturally equivalent English translation/idiom*, reference = cultural context) separately, uses **blinded human judgments as the reference** for scoring the automatic metrics, and makes **no claim about pragmatic appropriateness or contextual use** — the verified Task A/B prompts never request usage scenarios, so a pragmatic axis would require a separately proposed, separately capped (**≤$2**) usage-scenario-generation condition. This is a research hypothesis to be tested against the related-work audit — novelty is not claimed merely because the project studies proverbs, African languages, cultural understanding, or human validation. **Reviewers are invited to challenge the framing, flag missed related work, and propose stronger experiments before the protocol is frozen.**

## 2. What exists today

**Data** (collected Mar–May 2026; preserved as the Kaggle dataset [`original-data`](https://www.kaggle.com/datasets/abrahamsunday123/original-data) and local copies in the source repository `saaga23/proverb_mcq`):

| Language | Rows (verified) | Rights status |
|---|---|---|
| English | 2,278 | scrape sources undocumented |
| Arabic | 913 | source unidentified |
| Yoruba | 3,974 | source attribution **unresolved** (copyrighted book vs a tracked "Strict_EMNLP_Yoruba_Corpus" workbook) |
| French/German/Spanish | on Kaggle (counts unverified) | outside current scope |

Column-level schemas: [`docs/data/DATA_DICTIONARY.md`](docs/data/DATA_DICTIONARY.md); record flow: [`docs/data/DATASET_LINEAGE.md`](docs/data/DATASET_LINEAGE.md). **No raw data is distributed here.** Proverb data — including files removed from the old repository's working tree — remains retrievable from its public Git history (verified 2026-10-26): [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) §3.1.

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

- **No human annotations** — nothing about cultural understanding has been validated by native speakers.
- **S2 construct validity** was disputed and never resolved; the May primary response files were overwritten, so headline figures rest on contemporaneous verification reports only.
- **Data provenance/rights** unresolved for all three core languages (§2 table); this gates any public release and any annotation use of source items.
- **Prompt-design boundary:** the recovered Task A/B prompts elicit meaning-side outputs only — pragmatic appropriateness is **not assessable** from them.
- **Uneven model success rates** (34.7%–96.9%) require a prespecified missing-data rule; the 90 items are **different proverbs per language**, so cross-language contrasts are descriptive only.
- Full discrepancy record: [`docs/audit/EVIDENCE_DISCREPANCIES.md`](docs/audit/EVIDENCE_DISCREPANCIES.md).

## 5. The proposed method (provisional)

If gates pass (rights → rubric freeze → annotators κ ≥ 0.6 → deterministic checks):

- **Design:** blinded human raters (2/language) judge **meaning fidelity** of a stratified subsample of the recovered generations (10–15 proverbs/language × 3–4 models × 2 tasks × 2 strategies ≈ 360–720 outputs → **720–1,440 rating events**, ≈9–24 h per rater).
- **Primary outcome:** per-language, per-task agreement between human meaning-fidelity ratings and each automatic metric (BLEU, chrF, embeddings; optional ≤$2 LLM-judge run). Cross-language contrasts reported **descriptively only**.
- **Deferred:** pragmatic appropriateness (needs the gated usage-scenario condition).
- Full reasoning, prior-work comparison, and go/no-go gates: [`docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md`](docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md).

## 6. Relationship to `proverb_mcq` (separate track)

After the original track stalled, the work pivoted to distractor **shortcut resistance** — that track (v68 dataset, failure taxonomy, EACL 2027 draft) lives in [`saaga23/proverb_mcq`](https://github.com/saaga23/proverb_mcq). It is methodologically useful (generation code, filters, annotation app) but does **not** answer the cultural-understanding question, and its results are not evidence about cultural competence here. See [`docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md`](docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md).

## 7. Data and reproducibility notes

- **Deterministic, no-cost recheck** of every reproduced number: `python docs/decisions/supporting/recompute_checks.py --old-repo <proverb_mcq path>` (details: [`docs/decisions/supporting/RESULTS.md`](docs/decisions/supporting/RESULTS.md)).
- Recovered Kaggle pilot outputs are re-downloadable with `python -m kaggle kernels output …` (commands in RESULTS.md). The May pilot's raw responses are **not recoverable locally** — only a Kaggle web-UI version export could restore them.
- Historical context: [`docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md`](docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md) and the full register: [`docs/experiments/EXPERIMENT_REGISTER.md`](docs/experiments/EXPERIMENT_REGISTER.md).

## 8. Next steps (all pending owner decisions — nothing has started)

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
