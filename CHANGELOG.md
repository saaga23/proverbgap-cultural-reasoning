# Changelog

All notable changes to this repository are documented here.
This project does not yet use semantic versioning; entries are dated.

## [0.4.1] — 2026-10-26 (branch `docs/evidence-memo-2026-10-26`)

### Changed
- **README restructured as a first-reader entry point:** "At a glance" banner (what it is / what exists / what we learned / what's next / what's unresolved), "Start here" links, natural reading order (overview → question → what exists → findings → limitations → proposed method → proverb_mcq boundary → reproducibility → six-step roadmap → doc map); canonical provisional RQ adopted ("…automatic evaluation metrics align with blinded human judgments of meaning fidelity… vary by language and task"); Task A/B scope, no-pragmatic-claim boundary, and ≤$2 gated condition stated explicitly.
- `docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md`: candidate RQ aligned to the canonical wording (construct definitions retained; pragmatic axis deferred to the gated condition).

## [0.4.0] — 2026-10-26 (branch `docs/evidence-memo-2026-10-26`)

### Added
- **Phase 2 literature & methodology audit** — `docs/research/LITERATURE_AND_METHODOLOGY_AUDIT.md`: 13 verified prior works (ACL Anthology / arXiv primary sources), novelty-gap analysis, proposed construct-separation research question (meaning fidelity vs pragmatic appropriateness; English/Arabic/Yoruba), method sketch on recovered artifacts, model shortlist with verified evidence, and go/no-go gates. Search limitations recorded (Semantic Scholar HTTP 429; CulturalProbe/IlùBench unverified — not treated as evidence of absence).
- README §10 "Why we are reassessing the research direction" (with reviewer-challenge invitation) + six-step roadmap (§11).
- Yoruba rights wording corrected: source attribution marked **unresolved** (tracked `Strict_EMNLP_Yoruba_Corpus` workbook).

### Changed
- `research/RESEARCH_SCOPE.md`: dated direction-reassessment note; historical statuses unchanged.

## [0.3.1] — 2026-10-26 (branch `docs/evidence-memo-2026-10-26`)

### Verified (release-risk milestone; old repo inspected read-only, nothing changed)
- Public retrievability proven end-to-end: HEAD proverb CSV and the historical `_unzipped/mcq_a_zs_yoruba.csv` blob (commit `198253b`, removed at `3450d98`, still in `main`'s ancestry) both return HTTP 200 unauthenticated.
- 142 tracked CSVs categorized (~90 item-level proverb content/keys; 18 `paper/tables` aggregates).
- `.env.local`: local-only (ignored, 0 commits; no DSN in history; `supabase.co` refs at HEAD are public client URLs) — rotation downgraded to routine hygiene.
- Old-repo licensing claims (`DATASET_CARD.md`) verified accurate; residual MIT-file ambiguity noted with a recommended one-line README clarifier (owner-approved edit required).
- `DATA_RIGHTS_AND_PROVENANCE.md` §3.1 now records the verified exposure facts; README rights note updated.

## [0.3.0] — 2026-10-26 (branch `docs/evidence-memo-2026-10-26`)

### Added
- **Decision memo** `docs/decisions/PROVERBGAP_EVIDENCE_RECOVERY_AND_NEXT_EXPERIMENT.md` — evidence recovery and next-experiment recommendation, with ten go/no-go validity gates.
- **Supporting calculations** `docs/decisions/supporting/` (`recompute_checks.py`, `RESULTS.md`) — reproducible recomputation of the June failed run, v68 metrics, the 24.9% decomposition check, and FiB/Generation pilot descriptives.
- Git-history mining (old repo): recovered full `memory.md`, `GENERATION_QUALITY_REPORT.md`, `audit_behavior_report.md`; proved the May v4.3.4 eval data was never committed; discovered the April-era 2,000-item MCQ batches (registered as ER-A1).
- Kaggle notebook sources pulled (code only) for the FiB and Generation kernels; output descriptives recomputed.

### Corrected (dated audit updates; historical records preserved, not rewritten)
- **24.9% claim:** misattributed to the N=150 pilot — belongs to the N=50-era Run 22/23 and is internally inconsistent (D-17). Pilot's strict S2 = 62.5%.
- **"DeepSeek-R1 100% gold copying" and "25,190 generation rows":** contradicted by the recovered artifact (D-18).
- **"16,439 FiB rows":** unsupported; recovered pilot = 30 items; all predictions used last-line fallback extraction; real-context ≈ sham-context (D-19).
- **McNemar claim:** explicitly marked unresolved (test form/pairing undocumented; two-prop χ² = 106.9 as plausibility check only).
- **April-era MCQ runs:** added to register and data dictionary (D-20); flagged as a public-history redistribution exposure.
- Release audit: no live secrets in either repository's Git history (verified); three rights questions (citation ≠ redistribution ≠ code licence) now separated in `DATA_RIGHTS_AND_PROVENANCE.md` §4.

## [0.2.0] — 2026-10-26

### Added
- **Evidence audit pass** (local + Kaggle, read-only): recovered the May 19, 2026
  fill-in-the-blank (30 items) and generation (2,160 attempts) Kaggle pilot outputs;
  verified all v68 metrics from primary data; determined that the surviving
  `evaluation_results.csv` is the June failed run, not the May pilot; located the
  May 24 verification reports; inventoried 19 notebooks with execution metadata;
  mapped Kaggle kernels/datasets (`original-data` 6-language set; `mcq-pass-shortcut`
  kernel; private key dataset flagged).
- `docs/data/DATA_DICTIONARY.md` — column-level documentation for every dataset.
- `docs/data/DATASET_LINEAGE.md` — record-flow diagram with evidence labels.
- `docs/experiments/EXPERIMENT_REGISTER.md` — 13 experiments with explicit statuses,
  verified numerators/denominators, and metric definitions.
- `docs/experiments/LOCAL_AND_KAGGLE_ARTIFACT_CROSSWALK.md` — local↔Kaggle artifact map.
- `docs/research/ORIGINAL_VS_SHORTCUT_RESEARCH.md` — track separation and reusable elements.
- `docs/audit/EVIDENCE_DISCREPANCIES.md` — 16 documented discrepancies (D-1…D-16).
- `docs/newcomer_audit/NEWCOMER_COMPREHENSION_AUDIT.md` — 20 comprehension issues, fix status.
- `docs/GLOSSARY.md`, `docs/GETTING_STARTED_FOR_RESEARCHERS.md`.
- Root `README.md` rewritten to the 10-section newcomer flow.
- Repository made **public** after release checks (no secrets, no data artifacts).

### Corrected (historical evidence — recorded, not rewritten)
- Phase 1's "FiB/Generation planned only" and "v70 halted June 26" and the
  `evaluation_results.csv` misattribution are superseded by artifact evidence;
  corrections live in the discrepancy register with pointers to the original claims.

## [0.1.0] — 2026-10-26

### Added
- Initial repository created as an **independent** home for the original ProverbGap
  cultural-reasoning research direction, separated from
  [`saaga23/proverb_mcq`](https://github.com/saaga23/proverb_mcq) (which retains the
  shortcut-audit track and all raw experimental artifacts).
- Transferred, byte-identical and hash-verified, the complete 22-document Phase 1
  reconstruction package from `proverb_mcq:docs/Phase1_Reconstruction/`:
  - 8 evidence-backed reconstruction documents → `docs/reconstruction/`
  - 14 Phase-7 planning documents (13 `PHASE7_*` + the package index `README.md`)
    → `docs/planning/phase7/`
- `docs/repository_transfer/SOURCE_MAP.md` — source-to-destination mapping with SHA-256 hashes.
- `docs/repository_transfer/TRANSFER_MANIFEST.md` — transfer audit trail (date, source
  repository state, copied files, exclusions, integrity results).
- `research/RESEARCH_SCOPE.md` — the original research programme, with each intended
  direction labelled as *implemented*, *planned*, or *never run* according to the evidence.
- `DATA_RIGHTS_AND_PROVENANCE.md` — blocking data-rights and provenance issues
  (Yoruba copyright, ISBN conflict, unidentified Arabic source, undocumented English
  scraping sources, missing human validation).
- Root `README.md` — newcomer orientation; explicitly labels the repository as a
  reconstructed foundation awaiting Phase 2 review. **No Phase 2 work has been performed.**

### Deliberately excluded
- Raw proverb datasets, generated MCQ CSVs, audit-vote files, figures, and all
  shortcut-audit experimental code/paper material (remain in `saaga23/proverb_mcq`;
  locations documented in the transfer manifest).
- Any licence file — pending owner approval; nothing here is cleared for redistribution.
