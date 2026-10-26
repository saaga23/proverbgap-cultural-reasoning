# TRANSFER_MANIFEST

**Transfer date:** 2026-10-26
**Operator:** Kilo agent session (repository-separation task)
**Purpose:** audit trail for transferring the Phase 1 reconstruction package out of `saaga23/proverb_mcq` into this independent repository.

---

## 1. Source repository state (recorded before any action)

| Item | Value |
|---|---|
| Repository | `https://github.com/saaga23/proverb_mcq` |
| Local path | `C:\Users\USER\Downloads\Papers_water\Papers\BlindSpot-Hackathon\THe proverbeval container\MCQ` |
| Branch | `main` |
| HEAD commit | `716e525` — "docs: polish ProverbGap for first-time readers and fix evidence discrepancies" |
| Remote | `origin → https://github.com/saaga23/proverb_mcq.git` (fetch + push) |
| Working-tree status | Clean except one untracked path: `?? docs/Phase1_Reconstruction/` (the 22-document package itself) |
| `.git` type | Real directory (not a linked worktree) |

The transferred documents were **untracked** in the source repo; the transfer therefore took them from the working tree, not from a commit. They were left untracked in the source repo (nothing staged, committed, reset, or discarded there).

## 2. Destination repository

| Item | Value |
|---|---|
| Local path | `C:\Users\USER\Downloads\Papers_water\Papers\BlindSpot-Hackathon\proverbgap-cultural-reasoning` |
| Independence check | Directory is a **sibling** of the source repo; parents `…\BlindSpot-Hackathon` and `…\Papers` verified to contain no `.git`, so the new repo's history is independent and not nested inside `proverb_mcq` |
| Remote (intended) | `origin → https://github.com/saaga23/proverbgap-cultural-reasoning.git`, **private** |
| Default branch | `main` |
| Name availability | Verified available before creation (`gh api repos/saaga23/proverbgap-cultural-reasoning` → 404 Not Found) |

## 3. Files copied (22) — see `SOURCE_MAP.md` for per-file SHA-256

| Destination set | Count | Integrity |
|---|---|---|
| `docs/reconstruction/` (01–08 reconstruction documents) | 8 | SHA-256 re-computed after copy: **0 mismatches** |
| `docs/planning/phase7/` (13 `PHASE7_*` + package index `README.md`) | 14 | SHA-256 re-computed after copy: **0 mismatches** |
| **Total** | **22** | Byte-identical transfer |

## 4. Files authored new in this repository (not transferred)

| File | Purpose |
|---|---|
| `README.md` (root) | Newcomer orientation per repository charter; labels the repo as a reconstructed foundation awaiting Phase 2 |
| `CHANGELOG.md` | Transfer history entry |
| `.gitignore` | Blocks data artifacts, secrets, OS junk |
| `.gitattributes` | `* -text` — disables Git EOL rewriting so transferred files round-trip byte-exactly and the SHA-256 hashes in `SOURCE_MAP.md` stay verifiable after clone |
| `research/RESEARCH_SCOPE.md` | Original 8-direction research programme with implemented/planned/never-run status labels |
| `DATA_RIGHTS_AND_PROVENANCE.md` | Blocking rights/provenance issues and the no-data-redistribution policy |
| `docs/repository_transfer/SOURCE_MAP.md` | Source→destination mapping with hashes |
| `docs/repository_transfer/TRANSFER_MANIFEST.md` | This file |
| `docs/decisions/README.md` | Placeholder for future Phase 2 decision records |

## 5. Exclusions (deliberately NOT copied)

| Excluded (source-repo paths) | Reason |
|---|---|
| `actual_data/**` (incl. `*_cleaned.csv`, `inventory.json`, `data_inventory.txt`) | Raw proverb datasets with unresolved rights: Yoruba copyrighted (Owomoyela 2005), Arabic source unidentified, English scraping undocumented |
| `kaggle/run_logs/v68/**` (generated MCQ CSVs, audit votes, summary JSON, figures) | Data-derived artifacts of the shortcut-audit track; same rights basis; stay in source repo |
| `kaggle/run_logs/v69/**`, `kaggle/run_logs/v70/**` | Never-executed / halted runs; no usable results |
| `kaggle/kaggle_analysis/**` | Shortcut-audit analysis corpus; includes known-corrupted `main_results_table.csv` (S1 14.7% / S2 0.0%) |
| `paper/**`, `src/**`, `tests/**` | Shortcut-audit paper, experimental code, tests — the distinct research track this repo must not absorb |
| `.archive/**` (legacy code/data/docs snapshots) | Historical source snapshots; legacy material also implicated in the hardcoded-API-key finding — excluded as a precaution |
| `kilo.json`, `.kilo/**`, `AGENTS.md` | Agent/tooling configuration, not research documentation |
| Any `.env`, token, key, or credential file | Never copied; none present in the transferred set (verified by scan) |

The two historical Word documents cited by the dossier (`ProverbGap_Status_Document.docx`, `ProverbGap_MCQ_Project_History.docx`, under `.archive/legacy_docs_2026-06-19/` in the source repo) were **not** copied: they are outside the 22-document package, and their content is already summarized inside the transferred dossier with pointers to their source location.

## 6. Validation performed

1. New directory outside the source repository — verified (no `.git` in any parent of the destination).
2. Independent Git history — fresh `git init`; source repo's `.git` never referenced, cloned, or copied.
3. Source repo untouched — post-transfer `git status --short` identical to pre-transfer (`?? docs/Phase1_Reconstruction/` only); HEAD and remotes unchanged; no commits made to the source repo.
4. Document counts — 8 reconstruction + 14 planning confirmed by listing both source and destination.
5. Content integrity — 22/22 SHA-256 matches (0 mismatches).
6. No raw data / no secrets in destination — inventory scan plus key-pattern grep over all destination files.
7. Relative links inside root `README.md` resolve to existing destination files.
8. No claim of completed Phase 2 work anywhere in the destination documentation.

## 7. Known limitations of this transfer

- The transferred dossier contains historical links into `saaga23/proverb_mcq` that will not resolve here (see `SOURCE_MAP.md` note 2). This is intentional: the dossier is preserved verbatim.
- The dossier's factual claims were verified during Phase 1 against the source repo's artifacts; this transfer did not re-verify them against the live repository beyond the state recorded in §1.
- Nothing in this repository constitutes a data release; see `DATA_RIGHTS_AND_PROVENANCE.md`.
