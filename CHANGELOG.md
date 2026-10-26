# Changelog

All notable changes to this repository are documented here.
This project does not yet use semantic versioning; entries are dated.

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
