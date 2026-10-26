# ProverbGap: Do language models understand what proverbs *mean*?

> **Status: reconstructed research foundation — awaiting Phase 2 review.** No new experiments have been run in this repository. Historical numbers below come with explicit caveats; see [What has actually been established](#7-the-findings-and-what-they-actually-show).
>
> **New here?** Read sections 1–9 below in order, then [`docs/GETTING_STARTED_FOR_RESEARCHERS.md`](docs/GETTING_STARTED_FOR_RESEARCHERS.md). For the evidence-backed recommendation on what to run next, see [`docs/decisions/PROVERBGAP_EVIDENCE_RECOVERY_AND_NEXT_EXPERIMENT.md`](docs/decisions/PROVERBGAP_EVIDENCE_RECOVERY_AND_NEXT_EXPERIMENT.md).

## 1. The problem

A proverb like *"A friend in need is a friend indeed"* does not describe friendship literally — it compresses cultural wisdom into figurative language. A model can **pass a translation test** (knowing the words) while failing the real test: knowing what the saying *means* in its culture, when it applies, and why. Standard benchmarks mostly check translation or surface wording, so they can overestimate understanding.

## 2. The research question

> **Can large language models understand the culturally grounded meanings of proverbs, rather than merely recognize their translations, familiar wording, or surface-level interpretations?**

## 3. The benchmark concept

Each item is built from a **proverb record**: the original proverb, its English translation, and a **cultural meaning/context** (the gold answer). Models are asked to work from *meaning*, not wording — for example by picking the correct meaning from four options, completing a partially hidden proverb, or explaining the proverb in their own words.

The original design created difficulty through **two distractor strategies**:
- **S1 (baseline):** wrong options are meanings of *other proverbs in the same language* — clearly wrong, tests basic discrimination.
- **S2 (adversarial):** wrong options are *near-miss paraphrases* of the correct meaning, written by a different model family — tests whether the model truly parses the cultural meaning or just rejects obviously-wrong text.

## 4. The dataset

Collected March–May 2026 and preserved as the Kaggle dataset [`original-data`](https://www.kaggle.com/datasets/abrahamsunday123/original-data) (2026-05-16) plus local copies in the source repository:

| Language | Rows (verified) | Fields |
|---|---|---|
| English | 2,278 | Sample_ID, Proverb, Correct_Meaning |
| Arabic | 913 | Sample_ID, source_text, english_translation, Cultural_Context |
| Yoruba | 3,974 | Sample_ID, Source_Text_Yo, Target_Text_En, Cultural_Context, Provenance, QA_Flag, Comments |
| French / German / Spanish | present on Kaggle (counts unverified) | — |

Every column of every dataset is documented in **[`docs/data/DATA_DICTIONARY.md`](docs/data/DATA_DICTIONARY.md)**; how records flow through the pipeline is in **[`docs/data/DATASET_LINEAGE.md`](docs/data/DATASET_LINEAGE.md)**.

⚠️ **Rights:** Yoruba text is *attributed* to a copyrighted book (Owomoyela 2005), but a tracked workbook named "Strict_EMNLP_Yoruba_Corpus" makes the exact source **unresolved**; the Arabic source is unidentified; English scraping sources were not recorded. **No raw data is distributed here.** Note: proverb data in the source repository — including files removed from its working tree — remains retrievable from that repository's public Git history (verified 2026-10-26); see [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) §3.1.

## 5. Evaluation formats — planned vs actually run

| Format | What the model does | Historical status |
|---|---|---|
| **MCQ** | Pick the correct meaning (A–D) | ✅ Run (May 2026 pilot, N=150 proverbs → 300 questions) |
| **Fill-in-the-blank** | Complete a word masked in the proverb | ✅ 30-item pilot ran on Kaggle (May 19, 2026); never scaled. All 90 answers were extracted via a fallback parser, and real-context vs sham-problem performance was identical — **feasibility only, no cultural signal at this size** |
| **Generation/explanation** | Explain the proverb's meaning | ✅ Pilot ran on Kaggle (May 19, 2026; 2,160 attempts over 90 proverbs × 6 models); outputs recovered and analyzed (77.6% success; gold-copying 3.7–11.2% per model) — but no scoring rubric or human reference exists yet |
| **Human validation** | Native speakers review items | 🛠️ Sampling + a full annotation web app exist; **zero annotations collected** |

## 6. The experiments

The full, verified register is in **[`docs/experiments/EXPERIMENT_REGISTER.md`](docs/experiments/EXPERIMENT_REGISTER.md)**; the historical timeline in [`docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md`](docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md). In brief:

1. **Data collection** (Mar–May 2026) — completed; six-language Kaggle dataset verified.
2. **May MCQ pilot** (May 23, 2026) — completed; verified at the time, primary files later overwritten.
3. **May task pilots** (May 19, 2026) — FiB + Generation ran on Kaggle; outputs recovered during this audit.
4. **June Groq re-run** (Jun 8–9) — collapsed (2,440/2,700 API failures); project migrated to OpenRouter.
5. **OpenRouter iterations v59–v68** (June 2026) — v68 (Jun 22) produced the completed 180-question audit dataset.
6. **v69** (planned fix) — never run (budget). **v70** — halted mid-run (83/180 items, $0.42).
7. **Human validation & submission prep** (Jun–Aug 2026) — tooling and an Aug 2 submission package exist; no annotations; submission itself unconfirmed.

## 7. The findings — and what they actually show

| Claim | Evidence status |
|---|---|
| S1 86.8% (651/750) vs S2 strict 62.5% (369/590) — a difficulty gap | ✅ Verified on 2026-05-24 against the run's files; ❌ **those files were later overwritten** — the figures rest on contemporaneous verification reports, not raw data. The paired significance test ("McNemar") is **unresolved**: its exact form and pairing are undocumented (a two-proportion χ² on the same marginals gives 106.9 — plausible but not the reported 131.3) |
| "S2 real-paraphrase accuracy **24.9%** (below random) — construct-validity failure" | ⚠️ **Reported but unverified — and misattributed.** It belongs to the small N=50 runs of late May (where the companion figures are at least arithmetically coherent: 30.0%→35.6% overall; 31.5%→36.9%), **not** to the N=150 pilot. The 24.9% figure fits neither run's arithmetic. The pilot's strict S2 was 62.5% — far above chance |
| v68 shortcut audit: committee accuracy 56.7% (102/180), perfect consensus 41.7%, **HCW 27.8%** (50/180) — corpus fallback distractors often trap the committee | ✅ **Independently reproduced** from raw audit data (2026-10-26) — but this measures *distractor quality*, **not** cultural understanding |
| Generation pilot (May 19): 77.6% success across 6 models; gold-copying 3.7–11.2%; Qwen3-32B succeeded on only 34.7% of attempts | ✅ **Reproduced** from the recovered Kaggle output — describes task feasibility, not yet cultural understanding |
| FiB/Generation at scale; N=700; human validation; FR/DE/ES | ❌ Never run |

## 8. Failures and limitations (why the project paused)

- **S2 construct validity:** the headline S2 number mixes real paraphrases with placeholder-fallback items; never resolved.
- **Infrastructure:** June 2026 API meltdown; answer-key shuffle bug; OpenRouter budget exhaustion (v69/v70).
- **Human validation:** never executed despite prepared samples and a built annotation app.
- **Data rights:** Yoruba copyright (+ an unresolved ISBN conflict), unidentified Arabic source, undocumented English sources.
- **Small final dataset:** the shortcut-audit production set is 180 items (N=5 proverbs/language).

Details: [`docs/audit/EVIDENCE_DISCREPANCIES.md`](docs/audit/EVIDENCE_DISCREPANCIES.md) (16 documented discrepancies).

## 9. Relationship to the shortcut-audit repository

After the original track stalled, the work pivoted to a **separate, verifiable question** — "how do we generate distractors that resist shortcuts?" — which lives in [`saaga23/proverb_mcq`](https://github.com/saaga23/proverb_mcq) (v68 dataset, failure taxonomy, EACL 2027 paper draft). That track is **methodologically useful** (generation code, filters, annotation app) but does **not** answer the cultural-understanding question, and its results are not treated as evidence about cultural competence here. See [`docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md`](docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md).

## 10. Why we are reassessing the research direction

The field has moved since this project's first experiments: multicultural proverb reasoning was evaluated in [MAPS](https://aclanthology.org/2024.naacl-long.112/) (NAACL 2024); the **understanding-vs-pragmatic-use** distinction was already measured for models in Arabic and English in [Beyond Understanding / Kinayat](https://aclanthology.org/2026.eacl-long.341/) (EACL 2026); [ADAGE](https://arxiv.org/abs/2607.23058) (2026) built translation-free, native-speaker-curated proverb benchmarks; [Afri-MCQA](https://aclanthology.org/2026.acl-long.1869/) (ACL 2026) created native-speaker-built African cultural QA with linguistic-competence controls; and [Fu & Liu](https://aclanthology.org/2025.findings-emnlp.587/) (EMNLP Findings 2025) showed multilingual LLM judges are inconsistent (Fleiss κ ≈ 0.3). The original broad claims are therefore no longer sufficient novelty — and our historical results cannot yet establish cultural understanding (unresolved validity, reproducibility, annotation, provenance). We are provisionally considering a **validity and construct-separation study** across **English, Arabic, and Yoruba**: whether existing evaluation approaches distinguish *meaning fidelity* from *pragmatic appropriateness*, and how sensitive conclusions are to language, context, shortcuts, contamination, and evaluator choice. **This is a proposed direction, not a finalized methodology** — the full comparison is in [`docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md`](docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md). Researchers and reviewers are explicitly invited to challenge the claimed novelty, the three-language scope, the construct definitions, annotation feasibility, and the design before the protocol is frozen.

## 11. Current status and next steps

**Done:** Phase 1 reconstruction; evidence audit; literature audit (Oct 2026). **Not done:** everything below — no new experiments have been run.

1. **Complete the literature/novelty decision** — review [`docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md`](docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md) and confirm or narrow the proposed research question.
2. **Resolve source provenance and permissible use** for Yoruba, Arabic, and English (Yoruba source attribution is unresolved — see [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) §3.2 disposition sheet) — this gates everything downstream.
3. **Finalize the construct definitions, human rubric, and preregistered analysis** (meaning fidelity vs pragmatic appropriateness; annotator protocol; agreement targets).
4. **Complete deterministic reproducibility and evaluator-validity checks** (no-cost; e.g., `docs/decisions/supporting/recompute_checks.py`).
5. **Run a small, controlled human-anchored pilot** only once gates 1–4 pass, with a written budget cap.
6. **Scale and prepare a paper** only if the evidence supports the contribution.

Newcomers: start at [`docs/GETTING_STARTED_FOR_RESEARCHERS.md`](docs/GETTING_STARTED_FOR_RESEARCHERS.md).

## Repository map

```text
README.md, CHANGELOG.md, DATA_RIGHTS_AND_PROVENANCE.md
research/RESEARCH_SCOPE.md                  ← the 8 intended research directions, status-labeled
docs/GLOSSARY.md                            ← every term defined
docs/GETTING_STARTED_FOR_RESEARCHERS.md     ← 8-step onboarding
docs/reconstruction/            (8 docs)    ← Phase 1 evidence dossier
docs/planning/phase7/           (14 docs)   ← planning artifacts (not findings)
docs/data/                                  ← DATA_DICTIONARY.md, DATASET_LINEAGE.md
docs/experiments/                           ← EXPERIMENT_REGISTER.md, LOCAL_AND_KAGGLE_ARTIFACT_CROSSWALK.md
docs/research/                              ← ORIGINAL_VS_SHORTCUT_RESEARCH.md
docs/newcomer_audit/                        ← NEWCOMER_COMPREHENSION_AUDIT.md
docs/audit/                                 ← EVIDENCE_DISCREPANCIES.md
docs/decisions/, docs/repository_transfer/  ← decision records; transfer audit trail
```

*Raw datasets, generated MCQ files, and the shortcut-audit corpus remain in `saaga23/proverb_mcq` and are deliberately not copied here (see the transfer manifest for the full exclusion list).*
