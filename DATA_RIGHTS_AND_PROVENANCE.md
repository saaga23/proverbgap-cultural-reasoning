# Data Rights and Provenance — Blocking Issues

> **This repository distributes no proverb data.** Every raw dataset, generated MCQ file, and copyrighted extract remains in the source repository [`saaga23/proverb_mcq`](https://github.com/saaga23/proverb_mcq). This file records the outstanding rights questions so no future contributor assumes the data is cleared.

**Evidence base:** `docs/reconstruction/06_DATASET_PROVENANCE_AND_LINEAGE.md` (transferred, hash-verified) and `docs/planning/phase7/PHASE7_DATA_PROVENANCE.md`.

---

## 1. Collection summary (as documented by Phase 1)

| Language | Count | Documented source | Rights status |
|---|---|---|---|
| English | 2,278 | "Public proverb collections" (scraped) | ⚠️ Specific URLs **not recovered**; rights verification pending |
| Arabic | 913 | Academic dataset with `MID` prefix | ⚠️ Source **unidentified**; licensing under review |
| Yoruba | 3,931 | Owomoyela (2005), *Yoruba Proverbs*, University of Nebraska Press | 🚫 **Copyrighted; no redistribution permission obtained** |
| French | 161 | collected, excluded | n/a (insufficient sample) |
| German | 142 | collected, excluded | n/a |
| Spanish | 63 | collected, excluded | n/a |

## 2. Specific unresolved questions

1. **Yoruba copyright (blocking).** The source book is under copyright. Despite documentation claiming Yoruba would be excluded from public release, the v68 production CSV in the old repository contains **60 Yoruba MCQ rows**. Removal or permission is an owner-level decision; this exposure is unresolved.
2. **Conflicting ISBN.** Sources disagree on the Owomoyela (2005) ISBN: `0-8032-3576-3` (10-digit form, per the Phase 1 dossier's memory-graph evidence) vs `978-0-8032-1843-7` (per the old repo's README/data provenance template). These are **not** trivially equivalent encodings; at least one is wrong. Must be verified against the publisher's record before any rights clearance.
3. **Arabic source.** The `MID`-prefix academic dataset has never been identified. Until it is, no license can be asserted for Arabic proverbs or for MCQs derived from them.
4. **English scraping provenance.** The public-domain claim is plausible but undocumented (URLs not recovered). Verification required before redistribution.
5. **Human validation absent.** No native-speaker review of any generated item has occurred; planned validation (100-item audit; later a prepared 60-item sample) never started. This is both a scientific and an ethical limitation for any future release.
6. **Failed/stopped runs.** v69 (LLM-fallback ablation) was never executed; v70 halted mid-generation at 83/180 rows ($0.42 spent) on an OpenRouter budget limit. No usable evaluation results exist from either; do not cite them as findings.

## 3. Transfer policy applied to this repository

**Copied here:** the 22 Phase 1 reconstruction/planning documents only (markdown; no data). See `docs/repository_transfer/TRANSFER_MANIFEST.md`.

### 3.1 Verified exposure status (release-risk audit, 2026-10-26 — source repo `saaga23/proverb_mcq`, public)

- **142 tracked CSVs at HEAD**, by directory: 79 `kaggle/run_logs/` (v59–v70 generated MCQs with options and answer keys, audit votes, raw outputs), 30 `kaggle/kaggle_analysis/` (June-run inputs/outputs + diagnostics), 18 `paper/tables/` (aggregates), 8 `data/production/` (tables + `human_validation_sample_60.csv`, which contains full item text), 6 `actual_data/` (cleaned proverb collections incl. one duplicate `Arabic_cleaned (1).csv`). Roughly **~90 files carry item-level proverb content or answer keys**; the `paper/tables` aggregates do not.
- **Public retrievability verified end-to-end:** an unauthenticated fetch of `raw.githubusercontent.com/saaga23/proverb_mcq/main/actual_data/Yoruba_cleaned.csv` returns HTTP 200.
- **Historical blobs:** the April-era `_unzipped/mcq_a_*.csv` set (100 files — six languages, proverb texts, meanings, answer keys; e.g., 2,000 Yoruba and 803 Arabic items) was added in the first commit (`198253b`), removed from the working tree at `3450d98`, and **remains in `main`'s ancestry**. Verified: unauthenticated fetch of `raw.githubusercontent.com/saaga23/proverb_mcq/198253bfb62cd337e6f81ddb54c035547973c824/_unzipped/mcq_a_zs_yoruba.csv` returns **HTTP 200 (2.0 MB)**. **Deleting a file does not scrub Git history.**
- **Secrets: no Git exposure.** `annotation_app/.env.local` is present **locally only** — never committed (0 commits in `git log --all`), ignored via `annotation_app/.gitignore` (`.env*`). No `postgres://` DSN appears in any commit; `supabase.co` references at HEAD are public client URLs in `SECURITY.md`, the app README, and test scripts (by design). Credential rotation is therefore **routine hygiene, not an emergency response**.
- **Licensing claims in the old repo are accurate as written:** `DATASET_CARD.md` states code = MIT, data = "BLOCKED PENDING PROVENANCE/RIGHTS REVIEW", Yoruba = copyrighted with no redistribution permission, Arabic source unidentified. Residual ambiguity: the blanket MIT `LICENSE` file sits in a tree that also contains data files — a one-sentence README clarifier ("data files and Git history are not covered by the MIT licence / not cleared for redistribution") would remove misreading risk (owner-approved edit; the old repo must not be modified without approval).
- The OpenRouter key is transported via a **private** Kaggle dataset (`openrouter-key-mcq`) whose metadata declares a `CC0-1.0` licence — a labelling inconsistency on a credentials artifact (the dataset itself is private; keep it that way; consider renaming). Full audit: `docs/decisions/PROVERBGAP_EVIDENCE_RECOVERY_AND_NEXT_EXPERIMENT.md` §C.

**Deliberately not copied (locations recorded, contents not duplicated):**

| Artifact group | Old-repo location | Reason |
|---|---|---|
| Raw proverb datasets | `actual_data/*_cleaned.csv`, `actual_data/inventory.json`, `actual_data/data_inventory.txt` | Unresolved rights (Yoruba copyright; Arabic/English provenance) |
| Generated MCQs + audit votes | `kaggle/run_logs/v68/openrouter_pilot1_test_output/*.csv` (+ summary/figures) | Derived from unlicensed source data; belongs to shortcut-audit track |
| Halted/partial run artifacts | `kaggle/run_logs/v70/`, `kaggle/run_logs/v69/` | Incomplete; no usable results; same data-rights basis |
| Analysis corpus (incl. corrupted table) | `kaggle/kaggle_analysis/**` | Shortcut-audit outputs; `main_results_table.csv` contains known-corrupted numbers (S1 14.7% / S2 0.0%) |
| Shortcut-audit paper + code + tests | `paper/**`, `src/**`, `tests/**` | Distinct research track; must not define this repository |
| Legacy pipeline snapshots | `.archive/legacy_code_2026-06-19/**`, `.archive/legacy_data_2026-06-19/**`, `.archive/legacy_docs_2026-06-19/**` | Historical source snapshots; legacy docs also contain the hardcoded-API-key concern — excluded as a precaution |

**Secrets hygiene:** no API keys, tokens, `.env` files, or credentials were copied. Note for future workers: the Phase 1 dossier records that the old repository's *history* contains hardcoded API keys in legacy code — a further reason not to mirror that history here.

## 4. Licence position

Three distinct questions must not be conflated (per the 2026-10-26 release audit):

1. **Bibliographic citation** — citing Owomoyela (2005) or any published collection as a *source* is ordinary scholarship and does not by itself require permission from a publisher or university.
2. **Reproduction/redistribution** — citing a source does **not** establish permission to redistribute copied proverb texts, cultural explanations, substantial extracts, or derived datasets. That is the open question for Yoruba (copyrighted book), Arabic (source unidentified), and English (scraping undocumented).
3. **Code vs data licensing** — the old repository's MIT licence covers **code** only; it does not extend to datasets. This repository currently carries **no licence file** pending owner approval, and no dataset release.

- **No licence file is included in this repository.** A blanket MIT/CC BY licence is **not** applied without a justified scope and owner approval.
- The old repository's **code** is MIT-licensed; that statement does **not** extend to its datasets, and nothing here represents the historical data as cleared for redistribution.
- Until items 1–4 above are resolved by the owner, the correct posture is: **public repository, documentation only, no data release** — public visibility of these documents does not assert that any underlying dataset is cleared for redistribution.
