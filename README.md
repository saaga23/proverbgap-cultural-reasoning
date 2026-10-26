# ProverbGap: Cultural-Reasoning Research (Reconstructed Foundation)

> **This repository is a reconstructed research foundation, not a finished benchmark.**
> It preserves the *original* ProverbGap cultural-reasoning direction and its Phase 1 historical evidence so a future research team can pick up the work. **No new experiments have been run here.** See [`docs/planning/phase7/PHASE7_NEXT_STEPS.md`](docs/planning/phase7/PHASE7_NEXT_STEPS.md) and the "Status" section below.

## Why this repository exists

This is a **new, independent** repository for the original ProverbGap research question, kept **separate** from [`saaga23/proverb_mcq`](https://github.com/saaga23/proverb_mcq), which now houses the project's later *shortcut-audit* work. This split is intentional:

- `proverbgap-cultural-reasoning` (this repo) → the **original cultural-reasoning objective**.
- `proverb_mcq` → the **shortcut-resistance methodology + v68 audit dataset** (a distinct research track that emerged later).

A brief, evidence-backed account of how the two projects relate historically is in [`docs/reconstruction/08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md`](docs/reconstruction/08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md). The full reconstruction dossier lives in [`docs/reconstruction/`](docs/reconstruction/).

## The original research question

> **Can large language models understand the culturally grounded meanings of proverbs, rather than merely recognize their translations, familiar wording, or surface-level interpretations?**

The original design operationalizes this as a **two-strategy distractor-generation difficulty gradient** over culturally grounded proverbs:

- **S1 (baseline):** distractors are *real meanings from other proverb in the same language* (in-domain negative sampling). Tests basic discriminability.
- **S2 (adversarial):** distractors are *subtle, near-meaningful shifts* produced by a cross-family LLM paraphrase of the correct meaning. Tests deeper cultural/meaning understanding.

The **S1 → S2 difficulty gap** is the original measure of "genuine cultural reasoning vs surface recognition."

## Cultural meaning vs. translation-only evaluation

A translation can be literally correct without capturing the **cultural significance** of a proverb. This benchmark is built around evaluating models on *meaning-in-context*:

- Each proverb record includes: **original text**, **English translation**, and a **cultural explanation** (usage, significance, social function).
- Evaluation is on **cultural meaning**, not on reproducing the proverb's wording.

The distinction matters because a model can match a translation while failing the underlying cultural reasoning (the "shortcut" failure mode that the later audit work studied).

## Evaluation formats originally planned

The original plan encompassed **multiple task formats** (not all were implemented):

1. **Multiple-choice questions (MCQs)** — implemented in the May 2026 pilot.
2. **Fill-in-the-blank** — planned (complete a proverb from partial context; tests recall/cultural knowledge).
3. **Generation / explanation** — planned (explain a proverb's meaning in context).

> The May 2026 working draft describes formats 2 and 3 as *future work* and did not ship them. See [`02_ORIGINAL_RESEARCH_RECONSTRUCTION.md`](docs/reconstruction/02_ORIGINAL_RESEARCH_RECONSTRUCTION.md) §2–3.

## Historical status at the end of Phase 1

Phase 1 (read-only inspection) reconstructed what **actually exists**. The honest status:

| What existed (May 2026) | Status |
|---|---|
| N=150 pilot: S1 86.8% vs S2 62.5% (McNemar p<0.001) | ✅ Ran, but S2 construct validity later questioned |
| 3 languages benchmarked (EN/AR/YO) | ✅ Data collected (see rights note) |
| Fill-in-the-blank task | ⏸️ Planned, not implemented |
| Generation/explanation task | ⏸️ Planned, not implemented |
| Human validation (100 items) | ⛔ Never started |
| N=700 scale-up | ⛔ Never started |
| Additional languages (FR/DE/ES) | ⛔ Collected but excluded (small samples) |

**Important caveat:** the May S2 result and its interpretation are **contested** (see [`05_EVALUATION_METHODS_RECONSTRUCTION.md`](docs/reconstruction/05_EVALUATION_METHODS_RECONSTRUCTION.md) §2 and [`08_…`](docs/reconstruction/08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md)). Do not treat the headline numbers as a finalized, unqualified finding.

## What lives in this repository

```text
docs/reconstruction/      # 8 evidence-backed reconstruction documents (Phase 1)
docs/planning/phase7/     # 14 planning documents (Phase 7: overview, state, questions, ...)
docs/decisions/           # future: Phase-2 decisions as they are made
docs/repository_transfer/ # source map + transfer manifest (audit trail)
research/                 # research scope & future-work planning (NOT executed)
DATA_RIGHTS_AND_PROVENANCE.md  # blocking data-rights & provenance issues
```

Quick entry points:
- Newcomer orientation → [`docs/reconstruction/01_REPOSITORY_AND_ARTIFACT_INVENTORY.md`](docs/reconstruction/01_REPOSITORY_AND_ARTIFACT_INVENTORY.md) and [`docs/planning/phase7/PHASE7_RESEARCH_OVERVIEW.md`](docs/planning/phase7/PHASE7_RESEARCH_OVERVIEW.md)
- Original objective & history → [`docs/reconstruction/02_ORIGINAL_RESEARCH_RECONSTRUCTION.md`](docs/reconstruction/02_ORIGINAL_RESEARCH_RECONSTRUCTION.md)
- Timeline & pivots → [`docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md`](docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md)
- Experiments → [`docs/reconstruction/04_EXPERIMENT_REGISTER.md`](docs/reconstruction/04_EXPERIMENT_REGISTER.md)
- Evaluation methods → [`docs/reconstruction/05_EVALUATION_METHODS_RECONSTRUCTION.md`](docs/reconstruction/05_EVALUATION_METHODS_RECONSTRUCTION.md)
- Data provenance & rights → [`06_DATASET_PROVENANCE_AND_LINEAGE.md`](docs/reconstruction/06_DATASET_PROVENANCE_AND_LINEAGE.md) and [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md)

## What is deliberately **not** in this repository

To avoid reproducing unresolved liabilities, the following are **not** copied here (their locations are recorded for reference only):

- Raw proverb datasets (EN/AR/YO CSVs).
- Generated MCQ CSVs and audit-vote files.
- Shortcut-audit paper text, analysis corpus, and experimental code (these remain in `saaga23/proverb_mcq`).
- API keys, tokens, credentials, `.env` files, or unrelated personal data.

See [`docs/repository_transfer/TRANSFER_MANIFEST.md`](docs/repository_transfer/TRANSFER_MANIFEST.md) for the full exclusion list and rationale.

## How the shortcut-audit work relates (historically)

Around June 2026 the original "cultural-reasoning gap" framing came under pressure (the S2 result was contested and scaling stalled on budget/provider limits). The work evolved into a **distractor shortcut-resistance** study (the v68 N=5 audit: 180 MCQs, blind options-only committee, HCW gate). That track lives in [`saaga23/proverb_mcq`](https://github.com/saaga23/proverb_mcq). It is **methodologically informative** for this project (same filter/audit concepts) but it is not this repo's core objective, and it should not define this repo's README narrative.

Methodologically useful carry-over (from `proverb_mcq`, referenced, not duplicated): the blind-audit / HCW gate concept, the four adversarial distractor variants, and the failure taxonomy of `corpus-fallback` / `near-paraphrase trap` / `idiom shortcut`.

## Outstanding limitations (before any new experiments)

1. **Data rights** — Yoruba is copyrighted (Owomoyela, 2005); ISBN conflict; Arabic source/license unknown; English scraping source unrecovered. See [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md). **Do not redistribute proverb data from here.**
2. **S2 construct validity** — the original 62.5% figure is contested; resolve before treating S2 as a valid metric.
3. **No human validation** — zero native-speaker review of items.
4. **Irreproducible original numbers** — the May pilot used the deprecated Groq pipeline; current state depends on the v68 OpenRouter audit in `proverb_mcq`.
5. **Budget** — new API experiments require owner-approved OpenRouter credits.

## What should happen next (Phase 2)

Phase 2 must **review this reconstruction package first**, then decide. Per the task charter, Phase 2 deliberately does **not** start here:

- [ ] Do **not** perform a new literature review yet.
- [ ] Do **not** select a final evaluation methodology yet.
- [ ] Do **not** run new MCQ / fill-in-the-blank / generation experiments yet.
- [ ] Do **not** spend API credits, modify the old dataset, recruit evaluators, or draft a submission yet.

The concrete next gate is owner agreement on: (a) which evaluation format(s) to implement, (b) which model(s)/providers to use, (c) resolution of the Yoruba/Arabic/English rights questions, and (d) a venue and human-validation budget. Until then this repository is a **read-only evidence base**.

## Repository metadata

- Visibility: **private** (until data rights are reviewed).
- License: the original code in `proverb_mcq` is MIT-licensed; **this repository's data is not cleared for redistribution.** A license for the documentation will be set once the owner approves scope; nothing here is released under CC BY until provenances are verified.
- Remote: `saaga23/proverbgap-cultural-reasoning` (private, default branch `main`).

---

*This repository is a reconstructed foundation. Treat the contents as a dossier for decision-making, not as a completed study.*
