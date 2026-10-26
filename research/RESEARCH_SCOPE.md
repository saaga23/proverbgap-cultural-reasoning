# Research Scope — Original ProverbGap Cultural-Reasoning Programme

**Status labels used throughout:** `IMPLEMENTED` (evidence that it ran), `PARTIAL` (some evidence, incomplete or contested), `PLANNED` (documented intention, never executed), `UNKNOWN` (reported but unverifiable from surviving artifacts).

**Primary evidence:** the Phase 1 reconstruction dossier in [`docs/reconstruction/`](../docs/reconstruction/). This file summarizes the original programme; it does **not** report new results.

---

## Central research question

> **Can large language models understand the culturally grounded meanings of proverbs, rather than merely recognize their translations, familiar wording, or surface-level interpretations?**

The original benchmark design represents each proverb with three fields — original text, English translation, and a cultural explanation (usage/significance) — and evaluates models on *meaning*, not on reproducing proverb wording. Evidence: `docs/reconstruction/02_ORIGINAL_RESEARCH_RECONSTRUCTION.md` §1–3.

---

## The eight intended research directions

### 1. Representation of proverbs, translations, meanings, interpretations, contexts — `PARTIAL`
- Schema implemented: proverb + English translation + cultural explanation; MSA (fus-ha) for Arabic; tonal marks preserved for Yoruba where available (`02_` §3).
- Collection: 7,172 proverbs across six languages; three benchmarked (EN 2,278 / AR 913 / YO 3,931); FR (161) / DE (142) / ES (63) collected but excluded for insufficient sample size.
- Known data-quality defects: Arabic gold-meaning errors (≥4% of a 50-item sample), English meanings sometimes containing the proverb text itself (shortcut leak). See `docs/reconstruction/06_DATASET_PROVENANCE_AND_LINEAGE.md` §6.
- **Open:** no finalized representation standard for interpretations/contextual explanations beyond the three-field schema.

### 2. Model performance on cultural meaning vs translation alone — `PARTIAL` (contested)
- Two-strategy design (S1 in-domain negative sampling = translation/discrimination floor; S2 cross-family LLM paraphrase = meaning-level adversarial task). N=150 pilot: S1 86.8% vs S2 62.5%, McNemar p<0.001 (`02_` §5).
- **Contested:** the June 4 audit found S2's 62.5% mixes real paraphrases (24.9% — below the 25% random baseline) with high-scoring placeholder fallbacks; S2 construct validity was never resolved (`docs/reconstruction/05_EVALUATION_METHODS_RECONSTRUCTION.md` §2).
- Treat the difficulty-gap claim as **unproven until re-validated**.

### 3. Multiple evaluation formats (MCQ, fill-in-the-blank, sentence completion, generation) — `PARTIAL`
- **MCQ:** `IMPLEMENTED` (May pilot, 300 MCQs / 1,500 API evaluations).
- **Fill-in-the-blank:** `PLANNED` in the May draft (§7.3, future tense). A later exploration reportedly produced 16,439 rows before the May 18 thesis invalidation, but no artifacts were located in the repository (`docs/reconstruction/04_EXPERIMENT_REGISTER.md`, `06_` §4) — treat as `UNKNOWN/unverified`.
- **Generation / explanation:** `PLANNED` (§7.4). Same status as FiB (reported 25,190-row exploration; artifacts not located).
- **Sentence completion:** never separately documented; treat as `PLANNED` (not evidenced).

### 4. Prompting conditions (zero-shot / one-shot / few-shot) — `PARTIAL`
- Three evaluation styles were implemented for MCQ scoring: zero-shot, chain-of-thought, few-shot (`02_` §4; per-style results in `02_` §5.4: zero-shot best, CoT collapsed for one model, few-shot weakest).
- **One-shot** specifically is not documented in the evidence; do not claim it was run.

### 5. Comparisons across models, parameter sizes, families, open vs closed — `PARTIAL`
- Evidence exists for: a 2-model API committee (llama-4-maverick 17B vs allam-2-7b 7B), a 4-encoder zero-shot baseline sweep (mBERT / XLM-R / AraBERT / AfriBERTa), same-family exploitation (detected and fixed by switching generators), and per-model accuracy/error splits (`02_` §5.3, §5.5; `docs/reconstruction/07_MODEL_AND_EVALUATION_HISTORY.md`).
- A systematic size/family/open-vs-closed grid was **never run**; do not present committee comparisons as a controlled model-family study.

### 6. Role of task format, prompting strategy, language, cultural context — `PARTIAL`
- Language effects documented (EN strongest, YO weakest; Yoruba S2 fallback 36%); prompting-style effects documented; position-bias tested and mitigated (`02_` §5.2–5.6).
- Format effects **cannot** be analyzed from the evidence because only MCQ was implemented.

### 7. Internal team review, then external evaluator review — `PARTIAL` / `PLANNED`
- Internal audits occurred (e.g., the June 4 construct-validity audit that flagged S2; see `03_` Phase A).
- Human/external validation: `PLANNED` (100-item KNIGHT-style audit in the May draft; a 60-item stratified sample was later prepared in the old repo) — **never started**. No native-speaker review exists for any generated item.

### 8. Defensible protocol, documented limitations, reproducibility, venue preparation — `PARTIAL`
- Protocol documentation exists (methods, stats, limitations sections of the May draft; hardened retry/health-check mechanisms).
- Reproducibility: the original Groq pipeline is **deprecated** (corrupted-artifact window in June 2026); the reproducible pipeline that survives (v68, OpenRouter, pytest-verified 15/15) belongs to the shortcut-audit track in `saaga23/proverb_mcq` and evaluates *distractor quality*, not the cultural-reasoning question.
- Venue: the original direction had **no confirmed venue or submission**. (The later EACL 2027 ARR target belongs to the shortcut-audit track; submission status unconfirmed even there.) Candidate venues for this direction (e.g., ACL, AfricaNLP) remain an owner decision.

---

## Explicit non-claims

- This repository contains **no executed Phase 2 experiments**, no new literature review, no selected final methodology, and no conference draft.
- Headline pilot numbers are preserved **as historical evidence with their caveats**, not as validated findings.
- The fill-in-the-blank and generation tasks are **not** implemented here.

## Boundary with the shortcut-audit track

Everything under `saaga23/proverb_mcq` after the June 2026 pivot (v65–v70 runs, audit gates, failure taxonomy, EACL paper draft) addresses **distractor shortcut resistance**, not the cultural-understanding question directly. Methodologically reusable pieces for this programme are catalogued in `docs/reconstruction/08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md` §4.
