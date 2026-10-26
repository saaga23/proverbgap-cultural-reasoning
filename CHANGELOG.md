# Changelog

All notable changes to this repository are documented here.
This project does not yet use semantic versioning; entries are dated.

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
