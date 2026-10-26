# Getting Started for Researchers

You are joining a **reconstructed research project**. Nothing here is a finished benchmark. This guide tells you what to read, in what order, and what you should be able to say after each step. Estimated total time: 60–90 minutes.

---

## Step 1 — Root `README.md` (5 min)
Learn the one-sentence research question (can models understand the *culturally grounded meaning* of proverbs, not just translations?), the two-strategy idea (S1 easy baseline vs S2 adversarial distractors), and the honest status box. **After this step you can state the project's goal and its status to a colleague.**

## Step 2 — Original research reconstruction (`docs/reconstruction/02_ORIGINAL_RESEARCH_RECONSTRUCTION.md`) (15 min)
The May 2026 design: data schema, S1/S2 construction rules, committee, prompting styles, statistics, and the N=150 pilot numbers **with their caveats**. **You should now know:** what an item looks like, what S1/S2 actually ask the model, and why the S2 headline number is contested.

## Step 3 — Data documentation (`docs/data/DATA_DICTIONARY.md`, `docs/data/DATASET_LINEAGE.md`) (20 min)
Every dataset's columns, meanings, row counts, and how records flow from source proverb → MCQ → model response → metric. **You should now know:** the three source CSV schemas (and that they differ per language), how many MCQs/responses/votes exist per experiment, and which units of observation must not be mixed.

## Step 4 — Experiment register and timeline (`docs/experiments/EXPERIMENT_REGISTER.md`, `docs/reconstruction/03_CHRONOLOGICAL_RESEARCH_TIMELINE.md`) (20 min)
Every experiment with an explicit status: the May pilot (completed, historically verified, not locally reproducible), the May 19 FiB/Generation Kaggle pilots (completed, recovered), the June failed run, v59–v68 (OpenRouter), v69 (never run), v70 (halted), IAA proxy, human-validation prep, submission package. **You should now know:** which numbers are independently reproduced (v68: yes; May pilot: no) and which claims rest only on narrative documents.

## Step 5 — Local/Kaggle artifact crosswalk (`docs/experiments/LOCAL_AND_KAGGLE_ARTIFACT_CROSSWALK.md`) (10 min)
Where every artifact lives, what was executed, what was recovered from Kaggle, and what needs the owner (kernel-version export, Supabase check). **You should now know:** exactly which evidence is reachable without the owner and which is not.

## Step 6 — Open questions and discrepancies (`docs/planning/phase7/PHASE7_OPEN_QUESTIONS.md`, `docs/audit/EVIDENCE_DISCREPANCIES.md`) (10 min)
The 16 open owner decisions and the material contradictions (e.g., Yoruba row counts, the 24.9% claim, v70's date, the 7,172-vs-7,488 arithmetic). **You should now know:** what is genuinely unknown versus merely unwritten.

## Step 7 — What has and has not been validated
- **Independently reproduced (trust):** all v68 metrics (recomputed from `pilot1_test_audit_results.csv`); the FiB and Generation pilot descriptives (recomputed 2026-10-26 from recovered Kaggle outputs — see `docs/decisions/supporting/RESULTS.md`).
- **Verified at the time, primary data since overwritten (trust with care):** May pilot S1 86.8% (651/750), S2 strict 62.5% (369/590). The McNemar significance claim is **explicitly unresolved** (test form/pairing undocumented).
- **Narrative-only or corrected claims:** the "24.9% real-paraphrase" figure is **misattributed** — it belongs to the small N=50 runs and is internally inconsistent (decision memo §A4); "16,439 FiB rows" and "25,190 generation rows" are unsupported; "DeepSeek-R1 100% gold copying" is contradicted (max observed 11.2%).
- **Never executed:** v69; human validation; N=700 scale-up; FR/DE/ES benchmarking.

## Step 8 — Before running anything, discuss with the team
Do **not** start experiments on your own. The open gates (owner decisions): (a) which task format(s) to pursue first (MCQ fix vs FiB vs Generation); (b) whether to keep or replace S2; (c) data-rights resolution (Yoruba ISBN conflict, Arabic source, English URLs); (d) budget for API runs; (e) venue. Useful context: `docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md` §6 and `docs/planning/phase7/PHASE7_MIGRATION_PLAN.md`.

## Rules of engagement
1. Raw data lives in `saaga23/proverb_mcq` — read it there; do not copy datasets into this repository.
2. Never commit secrets (note: the old repo contains `.env.local` and a private Kaggle key dataset — do not reproduce either).
3. Every new numeric claim needs a source artifact + script path (see `docs/audit/` conventions).
4. Record decisions in `docs/decisions/` using the DR-NNN template.
5. Update `CHANGELOG.md` when you change documentation structure or claims.
