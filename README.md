# ProverbGap: Do language models understand what proverbs *mean*?

> **Status: a reconstructed research foundation — documentation only.** No new experiments have been run here. Every number below carries a status label saying exactly how well it is verified. And one thing to be clear about up front: the repository being public does not mean the underlying data is cleared for redistribution.

## At a glance

- **What this is:** the documented evidence behind an attempt to test whether language models understand the culturally grounded *meaning* of proverbs — as opposed to their translations or familiar wording — in English, Arabic, and Yoruba.
- **What exists today:** cleaned proverb collections in three languages (with unresolved rights questions), three piloted task formats, and recovered pilot outputs — but no human annotations at all.
- **What we have learned:** the early headline results can no longer be independently checked, because their raw files were overwritten; the one result we *can* fully recompute (the v68 audit) answers a different question — distractor quality, not cultural understanding.
- **What we are considering next:** having blinded human raters judge the recovered model explanations, then checking how well the automatic metrics agree with them. This is a hypothesis we want criticized, not an approved protocol.
- **What remains unresolved:** where the proverb data actually came from and whether it may be redistributed (especially Yoruba), the exact significance test behind the original pilot's headline claim, and the entire human-validation plan.

## Start here

Read this README first (about ten minutes now that it explains the design), then, in this order:

1. [`docs/GETTING_STARTED_FOR_RESEARCHERS.md`](docs/GETTING_STARTED_FOR_RESEARCHERS.md) — the 8-step onboarding path.
2. [`docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md`](docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md) — the current literature audit and proposed method.
3. [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) — the rights/provenance gate that blocks everything downstream.

---

## 1. What ProverbGap is

A proverb like *"A friend in need is a friend indeed"* does not describe friendship literally — it compresses cultural wisdom into figurative language. A model can **pass a translation test** (knowing the words) while failing the real test: knowing what the saying *means* in its culture, when it applies, and why. Standard benchmarks mostly check translation or surface wording, so they can overestimate understanding.

**Original research question (May 2026):**

> **Can large language models understand the culturally grounded meanings of proverbs, rather than merely recognize their translations, familiar wording, or surface-level interpretations?**

To test this, each proverb was stored as a **proverb record** with three parts: the original proverb, its English translation, and a **cultural meaning/context** — a sentence or two explaining what the proverb actually teaches and when it is used. That cultural explanation was intended to serve as the **reference** — the recorded text that a model's answer is scored against, as opposed to anything shown to the model.

The original multiple-choice design created difficulty through two distractor strategies. (**Distractor** = one of the wrong options in a multiple-choice question.)

- **S1 (baseline):** the three wrong options are real meanings of *other proverbs from the same language*. They are clearly wrong once you know what the proverb means, so this mostly tests whether a model can reject obviously wrong text.
- **S2 (adversarial):** the three wrong options are near-miss paraphrases of the correct meaning, written by a model from a *different* family than the ones being evaluated. Doing well here should require actually understanding the meaning, because the wrong options look plausible.

The idea was that the drop in accuracy from S1 to S2 would measure how much of a model's apparent proverb skill is real understanding.

That reasoning has a catch, and it is the reason the project changed course. A low S2 score does not by itself prove poor understanding, because the S2 options were *machine-generated*: if the paraphrases were subtly wrong, or so close to the correct meaning that no answer could be trusted, then a low score reflects bad test items rather than a model that fails to understand. Whether the test items themselves are sound is called **construct validity** — whether a test actually measures what it claims to measure — and that question was never settled for S2 (§3, §4).

**Why the direction is being reassessed.** Since 2024 the field has produced several close relatives of this idea: [MAPS](https://aclanthology.org/2024.naacl-long.112/) (NAACL 2024) evaluated proverb understanding across six languages; [Kinayat](https://aclanthology.org/2026.eacl-long.341/) (EACL 2026) measured the gap between *understanding* a figurative expression and *using it appropriately* in Arabic and English; [ADAGE](https://arxiv.org/abs/2607.23058) (2026) built translation-free proverb benchmarks curated by native speakers; and [Fu & Liu](https://aclanthology.org/2025.findings-emnlp.587/) (EMNLP Findings 2025) showed that LLM judges are inconsistent across languages. Building *another* proverb benchmark is therefore not obviously a contribution. The direction this repository now proposes (§5) instead asks a question about **evaluation itself**: not "which model is best?" but "are the automatic scores people use to grade models actually tracking what humans think?" None of the verified papers reviewed so far answer that — though several related-work leads remain unverified, so this is a *candidate* contribution rather than an established gap, and the framing stays open to challenge.

**A note on the other repository.** [`saaga23/proverb_mcq`](https://github.com/saaga23/proverb_mcq) is a separate project that grew out of this one: it studies whether *distractors* can be generated so that they resist shortcut answers (see §6). Its results are about distractor quality. They must not be read as evidence about whether any model understands proverbs.

## 2. What exists today

**Data** (collected Mar–May 2026; preserved as the Kaggle dataset [`original-data`](https://www.kaggle.com/datasets/abrahamsunday123/original-data) and local copies in `saaga23/proverb_mcq`):

| Language | Rows (verified) | Rights status |
|---|---|---|
| English | 2,278 | scrape sources undocumented |
| Arabic | 913 | source unidentified |
| Yoruba | 3,974 | source attribution **unresolved** (copyrighted book vs a tracked "Strict_EMNLP_Yoruba_Corpus" workbook) |
| French/German/Spanish | on Kaggle (counts unverified) | outside current scope |

Each row in these files is one proverb record as described in §1. One count conflict should be known: an earlier project document says 3,931 Yoruba proverbs, while the file that actually exists contains 3,974 rows — the file is authoritative for what exists, and what explains the difference (most likely a later filtering step) is unresolved. Column-level schemas are documented in [`docs/data/DATA_DICTIONARY.md`](docs/data/DATA_DICTIONARY.md), and the record flow in [`docs/data/DATASET_LINEAGE.md`](docs/data/DATASET_LINEAGE.md). No raw data is distributed from this repository. One caveat worth knowing early: proverb data — including files that were later removed from the old repository — is still retrievable from its public Git history; we verified this in October 2026 ([`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) §3.1).

**Experiments actually run.** Three task formats were piloted; "recovered outputs" below means the models' answer texts, downloaded back from Kaggle after the local copies were lost.

| Format | Status |
|---|---|
| **MCQ** (multiple choice: pick the correct meaning from four options) | ✅ May 2026 pilot (150 proverbs × 2 strategies → 300 questions); model responses not preserved |
| **FiB** (fill-in-the-blank: complete a word that was masked in the proverb) | ✅ 30-item Kaggle pilot (2026-05-19) — feasibility only. Two caveats a newcomer should know: every one of the 90 answers was recovered by the parser's *fallback* method (it could not find the answer where the prompt told the model to put it, so it grabbed the model's last line instead — which limits trust in the extracted answers); and **exact match** (the completed word matching the reference word letter-for-letter) was equally poor whether the surrounding proverb was real or a meaningless sham |
| **Generation** (write an explanation or a cultural equivalent) | ✅ Kaggle pilot (2026-05-19): 2,160 attempts, 90 proverbs × 6 models; **outputs recovered — the basis of the proposed audit** |
| **Human validation** | 🛠️ A 60-item sample and a working annotation web app exist; **zero annotations have been collected** |

Also: a completed 180-question **shortcut-audit dataset** (v68, June 2026) — but it measures distractor quality, not cultural understanding (see §6).

## 3. What we have learned — and what each result actually means

| What was tested | Result | What this means | Status |
|---|---|---|---|
| **May MCQ pilot** — can models pick the correct meaning when the wrong options are other proverbs' meanings (S1) versus near-miss paraphrases (S2)? | S1 86.8% (651/750) vs S2-strict 62.5% (369/590) — "strict" means the S2 average was taken only over items whose wrong options were genuine paraphrases, excluding items that used placeholder filler | A large drop, consistent with S2 being harder — but it does not prove *why*, and the construct-validity concerns (§1) were never resolved | ⚠️ Verified on 2026-05-24 against files that were later overwritten. The reported significance test ("McNemar") is unresolved: its pairing and exact form are undocumented; a two-proportion χ² on the same marginals gives 106.9 |
| **The "24.9% real-paraphrase accuracy" claim** — an alarm that S2's correct-answer rate on genuinely paraphrased items was below the 25% random-guessing baseline | Does not fit the arithmetic of any run we can trace (mixing 24.9% with its companion numbers gives 30.9%, but the runs in question scored 35.6% and 36.9% overall) | The alarm belongs to small N=50 test runs, not to the pilot above — but it was never verified from raw data either way | ⚠️ Reported but unverified — and misattributed |
| **v68 shortcut audit** — a blind committee of 4 models saw only the four answer options (no proverb text) and voted on the correct one; if most vote wrong, the distractors exploit a shortcut | Committee accuracy 56.7% (102/180); **HCW** ("high-consensus-wrong": ≥3 of 4 auditors agree on the *wrong* answer) 27.8% (50/180) | Distractors from that pipeline often trap a model that only sees the options. This says the *generation pipeline* has a problem — it says nothing about whether models understand proverbs | ✅ Recomputed from surviving raw data |
| **Generation pilot** — six models wrote proverb explanations or cultural equivalents; automated scores were computed | 77.6% of 2,160 attempts succeeded; in 3.7–11.2% of successful cases the generated answer simply reproduced the reference text ("gold-copying" — which would flatter automatic similarity scores without any real explanation being produced); one model succeeded on only 34.7% of attempts | The task ran and its outputs are usable — this is a feasibility result, not a comprehension result | ✅ Recomputed from the recovered Kaggle output |
| **FiB pilot** — models completed a word masked in the proverb, under real-proverb and sham-proverb conditions | Exact match ≈ 13%, and identical for real and sham proverbs | Word-completion may not tap cultural meaning at all; feasibility check only | ✅ Recomputed from the recovered Kaggle output |
| Scale-ups (N=700), human validation, French/German/Spanish | — | Never run | ❌ |

Status labels used above: ✅ **Reproduced** = we recalculated the number from surviving raw data during this audit; ⚠️ = the figure was checked when the files existed but the primary data was later lost, or it rests on an unverified written claim; ❌ = never run.

## 4. Limitations and open problems

- **No human annotations** — nothing about cultural understanding has yet been checked by human raters.
- **S2 construct validity** was disputed and never resolved; the May primary response files were overwritten, so headline figures rest on contemporaneous verification reports only.
- **Rights and provenance are unresolved for all three languages** (see §2); until they are, neither a public data release nor annotation of the source items can go ahead.
- **The pilot prompts only ever asked about meaning.** Task A requested a literal explanation and Task B a cultural equivalent; neither asked when or where the proverb applies, so the outputs cannot say anything about pragmatic use.
- **Model success rates varied widely** (34.7%–96.9%), so missing outputs need a prespecified rule; and since the 90 items are different proverbs per language, cross-language contrasts can only be descriptive.
- Full discrepancy record: [`docs/audit/EVIDENCE_DISCREPANCIES.md`](docs/audit/EVIDENCE_DISCREPANCIES.md).

## 5. The proposed study, step by step (provisional)

Nothing below has been approved or executed. The steps are in the order the work would actually happen, and each one can stop the project.

### Step 1 — Resolve permissions and confirm usable data

Human annotation and any release both require knowing where the data came from and whether it may be used. **English** was scraped from public collections, but the sources were never recorded, so the public-domain claim is unverified. **Arabic** comes from an academic dataset that has never been identified. **Yoruba** is attributed to a copyrighted book (Owomoyela 2005), but a tracked workbook named "Strict_EMNLP_Yoruba_Corpus" suggests an additional or alternative source — the true provenance is unknown. Yoruba is **not** being dropped: if its rights cannot be resolved, the study would run on English and Arabic and report Yoruba as blocked-by-rights, rather than quietly pretending the tri-lingual design is complete. The full disposition sheet is in [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) §3.2.

### Step 2 — Define exactly what is being evaluated

Two constructs, in plain English:

- **Meaning fidelity** — does a model's answer preserve the proverb's intended meaning?
- **Pragmatic appropriateness** — does an answer identify a suitable situation in which the proverb would be used?

The pilot generated model answers under **two tasks × two prompting strategies**. Everything below is verified from the recovered notebook code and output file.

#### Task A — explain the proverb's literal meaning

- **Instruction to the model:** "Provide a clear, concise explanation of the literal meaning… Explain the literal meaning of this proverb in 1–2 sentences" (system prompt sets a "linguistic expert" role).
- **Inputs given to the model:** the original proverb and its English translation. Nothing else.
- **Reference used for scoring:** the English translation — used *only* during scoring, never shown to the model as text to copy.
- **A successful answer** would restate the intended meaning in plain English in 1–2 sentences. This task tests whether the model can restate a meaning it is given materials for; it does not test when the proverb should be used.

#### Task B — give a culturally equivalent English expression

- **Instruction to the model:** "Provide a culturally equivalent English translation or idiom… Output ONLY the translation itself. Do not explain the proverb."
- **Inputs given to the model:** the same two fields — original proverb and English translation. The cultural context was **not** given to the model.
- **Reference used for scoring:** the recorded **cultural context** — the field describing what the proverb teaches and how it is used. Verified from the recovered output file, this reference was genuinely different from Task A's translation reference for **all 60 Yoruba items and 56 of 60 Arabic items**; for **English** (and 4 Arabic items) it was identical to the translation, because the English source file has no separate cultural-context column and the code fell back to the translation. This asymmetry is disclosed so it can be handled in analysis rather than discovered later.
- **How this differs from Task A:** Task A restates what the proverb says; Task B re-expresses it as the way an English speaker would say the same thing — usually an idiom, which is a harder, more culture-loaded transformation.

*Illustration (invented for explanation only — not a pilot output or result):* imagine a proverb that literally says "The hyena does not eat hyena meat." A Task A answer might be "People from the same group do not harm each other." A Task B answer might be the English idiom "honor among thieves." Whether a proposed idiom is a *culturally valid* equivalent is precisely the kind of judgment the proposed human rating would check.

#### The two prompting strategies

- **`zs` — zero-shot prompting:** the model receives the task instruction and answers directly, with no worked examples (verified from the prompt code).
- **`cot_en` — English chain-of-thought prompting:** the model is asked to reason step by step *in English* about the meaning, wrap that reasoning in `<reasoning>` tags, and give a final answer; the validation code strips the tagged reasoning before the final answer is scored (verified).

What changes between them is only *how the model is prompted to produce its answer* — the same proverb, the same task instruction, and the same scoring reference. Whether chain-of-thought helps or hurts is an empirical question the recovered data can be examined for; it is not an established conclusion.

#### The four task–strategy combinations

| Task | Zero-shot (`zs`) | Chain-of-thought (`cot_en`) |
|---|---|---|
| **Task A:** literal-meaning explanation | Task A answered directly | Task A with step-by-step reasoning prompted |
| **Task B:** culturally equivalent expression | Task B answered directly | Task B with step-by-step reasoning prompted |

Each proverb/model pair was attempted under all **four combinations**. The strategies are prompting conditions — not separate datasets and not languages. The two tasks vary *what kind of answer* is requested; the two strategies vary *how* the model is prompted to produce it; keeping the dimensions distinct is what allows task-related and prompt-related differences to be examined separately.

#### How this connects to the proposed study

- The recovered pilot contains outputs for these four combinations for each selected proverb/model pair — though failed generations mean not every expected output exists.
- The proposed study compares automatic metric scores with blinded human judgments of meaning fidelity, **analyzing Task A and Task B separately**.
- Any difference between `zs` and `cot_en` outputs is a secondary comparison of prompting conditions — not evidence of cultural understanding.
- Task A and Task B metric scores must **not be pooled** without justification: the prompts differ, and the references differ too (identical for English, distinct for Yoruba and most Arabic items, as verified above).
- Pragmatic appropriateness remains out of scope for the existing outputs, because neither task explicitly asks for a usage scenario. The primary study analyzes the existing generations and requires no new inference; the usage-scenario run is a separate, optional extension needing explicit approval and a maximum budget of $2.

### Step 3 — Which models, and how they would be chosen

The recovered pilot already contains generations from **six existing instruction-tuned models** — models that have been fine-tuned to follow instructions, as opposed to raw base models — run through APIs (no new training involved): LLaMA-3.1-8B, LLaMA-3.3-70B, Qwen3-32B, Gemma-4-31B, LLaMA-4-Maverick, and Nemotron-120B. The proposed audit would rate a **subset of 3–4 of these six** — not six newly selected models.

Selection is **not yet decided**, and the criteria in ordinary language are: the model must handle English, Arabic, and Yoruba plausibly; it must have enough *successful* outputs to support the comparison (Qwen3-32B succeeded on only 34.7% of attempts); its exact checkpoint and licence must be documented; and the set should form a consistent multilingual baseline rather than a mixed bag. The methodology audit discusses Arabic-centric models (ALLaM-7B, Fanar-1-9B) and African-focused models (AfriqueQwen-14B; N-ATLaS, InkubaLM, YorubaLlama as unverified leads) only as *possible future additions* — appearing in the pilot does not automatically make a model a suitable multilingual baseline, and no model is selected by name alone. Final selection is a decision to make after examining language coverage and successful-row counts.

### Step 4 — What would be sampled, and how big the annotation effort is

The plan is to select **10–15 proverb items per language, 3–4 selected models, both tasks, and both strategies**. The cross-product of those choices gives the *maximum planned sample*, if every selected output exists and succeeded:

- Smaller design: 10 proverbs × 3 models × 2 tasks × 2 strategies = **120 outputs per language**, or **360 across the three languages**.
- Larger design: 15 × 4 × 2 × 2 = **240 outputs per language**, or **720 overall**.

These are **generated answers to be rated** — not 360–720 unique proverbs. There are three language-specific sets of proverb items; the recovered data contains no parallel (shared/translated) items across languages. Only successful generations can be rated and success rates were uneven, so the final selection must be drawn from real successful outputs under a predeclared missing-output rule; the intended sample and the achieved sample would be reported separately.

With **two raters per language — six raters in total** — and each rater judging only their assigned language:

- Smaller design: 360 outputs × 2 ratings = **720 rating events**; each rater rates 120 outputs, ≈ **3–4 hours** at 1.5–2 minutes per rating.
- Larger design: 720 outputs × 2 ratings = **1,440 rating events**; each rater rates 240 outputs, ≈ **6–8 hours**.

These are planning estimates, not measured annotation times. Adding a third rater per language would be a different design with proportionally more work (1.5× the rating events) and is not part of this baseline.

### Step 5 — What the human raters would actually do

1. Raters receive written instructions and a rubric for judging whether an output preserves the proverb's intended meaning.
2. Judgments are **blinded**: raters see the output (and whatever reference the task design specifies) but not which model produced it, so brand familiarity cannot influence them.
3. Two competent raters independently assess every selected output.
4. Agreement between raters is recorded (Fleiss' kappa is one standard way to summarize agreement among multiple raters; **κ ≥ 0.6 is a proposed target, not a result already obtained and not a universal guarantee of good annotation**), disagreements are resolved by a prespecified adjudication procedure, and the records are kept auditable.
5. The rubric is piloted on a small batch before any scale-up.

The annotation web app in the old repository is *code that exists* — it does not mean annotations have been collected, and none have.

### Step 6 — How the automatic metrics get evaluated

This is the heart of the proposal. The automatic metrics have **already produced scores** for the recovered generations — but a score is not self-validating. The study asks whether those scores actually track what trained human raters say.

The metrics, briefly:

- **BLEU** — counts overlapping word sequences between a candidate answer and its reference.
- **chrF** — counts overlapping character sequences, which can catch partial spelling and word-form matches.
- **Embedding similarity** — compares numeric vector representations of the candidate and reference texts to estimate semantic closeness.

The comparison would work like this:

1. Select the successful outputs under the prespecified sampling and missing-data rules (Step 4).
2. Score those answers with the specified metrics using reproducible scripts.
3. Compare each metric's scores against the blinded human meaning-fidelity ratings — **correlation** here means how closely two sets of scores move together.
4. Run the comparison **separately for Task A and Task B**, because their prompts and reference fields differ.
5. Report agreement/correlation with **uncertainty intervals** — ranges that show how precise an estimate is, e.g., a 95% confidence interval — under a prespecified analysis plan that accounts for many outputs coming from the same proverb.
6. Interpret any language-level differences cautiously (Step 7): the languages have different proverbs and different rater pools.

BLEU, chrF, and embedding similarity are **not** treated as ground truth — the human ratings are the anchor, though their own reliability must be checked first (Step 5). An LLM judge is **not automatically part of the core study**: the recovered notebook contains a judge prompt, but the recovered output file contains no saved judge scores, so any judging run would be a new, separately approved step capped at **$2** and calibrated against the human ratings. (That judging run is distinct from the usage-scenario generation extension in Step 2, which has its own proposed $2 cap.)

### Step 7 — What could and could not be concluded

- The study evaluates **metric validity** against human meaning-fidelity judgments on a sample of generation outputs. It does not measure general model intelligence or cultural competence.
- Task A vs Task B differences would be meaningful but descriptive: the prompts and reference types differ.
- Cross-language differences are descriptive only — different proverbs and separate rater pools mean the design cannot establish that a language *causes* better or worse agreement.
- Nothing in the existing outputs supports conclusions about pragmatic appropriateness or contextual use.
- The study is provisional and proceeds only if the rights, sampling, annotation, and analysis gates are all satisfied.

If it works, the result would be a statement of the form: *these automatic metrics track human judgments of proverb-meaning fidelity reliably; these do not; here is where the limits are.* That is useful and publishable — and it is not a declaration that any model understands a culture.

## 6. Relationship to `proverb_mcq` (separate track)

After the original track stalled, the work pivoted to distractor **shortcut resistance** — that track (the v68 dataset, its failure taxonomy, and an EACL 2027 paper draft) lives in [`saaga23/proverb_mcq`](https://github.com/saaga23/proverb_mcq). The two projects answer different questions: proverb_mcq asks "can we build distractors that don't give the answer away?"; ProverbGap asks "do models understand what proverbs mean?". A distractor set can be shortcut-resistant without anyone understanding anything, so proverb_mcq's results — however solid — are not evidence about cultural understanding. The audit app and generation code built there are reusable here. See [`docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md`](docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md).

## 7. Data and reproducibility notes

- **What can be recomputed from surviving files** (deterministically, at no cost): the v68 audit metrics, the June-run failure counts, and the recovered FiB/Generation descriptives — `python docs/decisions/supporting/recompute_checks.py --old-repo <proverb_mcq path>` (details: [`docs/decisions/supporting/RESULTS.md`](docs/decisions/supporting/RESULTS.md)).
- **What cannot:** the May MCQ pilot's model responses (overwritten; only a Kaggle web-UI version export could restore them) and the LLM-judge scores (never saved).
- **What is re-downloadable:** the FiB and Generation pilot outputs, via `python -m kaggle kernels output …` (commands in RESULTS.md).
- Historical context: [`docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md`](docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md); full register: [`docs/experiments/EXPERIMENT_REGISTER.md`](docs/experiments/EXPERIMENT_REGISTER.md).

## 8. Next steps (all pending owner decisions — nothing has started)

The Phase 1 reconstruction, the evidence audit, and the October 2026 literature audit are complete. Everything in this list is still to do — no new experiments have been run. The order is the dependency order: nothing later can start until the earlier gates pass.

1. **Resolve source provenance and permissible use** for Yoruba, Arabic, and English (disposition sheet: [`DATA_RIGHTS_AND_PROVENANCE.md`](DATA_RIGHTS_AND_PROVENANCE.md) §3.2) — this gates annotation and any release, so it comes first.
2. **Confirm the provisional research question and finalize the methodology** — narrow the evaluator-validity framing ([audit](docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md)), select the 3–4 models from the recovered pilot, and write down the sampling and missing-data rules.
3. **Freeze the construct definitions, the human rating rubric, and a preregistered analysis plan** — "preregistered" means the analysis is written down before anyone looks at results, so choices cannot be tuned to the outcome. The rubric covers meaning fidelity first; the pragmatic axis enters only via the gated ≤$2 usage-scenario condition.
4. **Complete deterministic reproducibility and evaluator-validity checks** (no-cost) — verifying that the scoring pipeline behaves as intended, before trusting it.
5. **Run the small, blinded pilot** — "human-anchored" meaning the reference standard against which the metrics are judged is human judgment — once gates 1–4 pass, under a written budget cap.
6. **Optional paid extensions and scale-up** — the usage-scenario generation run and/or the LLM-judge run (each ≤$2, each separately approved), then scaling and paper preparation only if the evidence supports the contribution.

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
