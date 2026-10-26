# Phase 1 — Document 06: Dataset Provenance & Data Lineage

**Status:** Completed
**Purpose:** Document every data source in the project, licensing status, the 6-language→3-language reduction, and the unresolved copyright exposure (Yoruba / Owomoyela). Cross-references `actual_data/`, `.archive/legacy_data_2026-06-19/`, the memory graph, and README §8.

**Authoritative source:** `docs/ProverbGap_Paper_Draft.md` §3.1; README §8 "Data, Code, and License"; `actual_data/data_inventory.txt` ("CATASTROPHIC DATA MISMATCH DISCOVERY"); `actual_data/inventory.json`; memory graph "Yoruba Proverbs" entity.

---

## 1. Original collection (7,172 proverbs, 6 languages)

| Language | Count | Source | Prefix | Status |
|---|---|---|---|---|
| English | 2,278 | Public-domain proverb collections (scraped) | ENG | Rights pending (URLs unrecovered) |
| Arabic | 913 | Classical Arabic (amsal) collections | MID | Source unidentified (academic dataset, MID prefix) |
| Yoruba | 3,931 | Yoruba oral tradition + ethnographic records | YOR | **Copyrighted** — see §3 |
| French | 161 | — | — | Collected but EXCLUDED (insufficient N) |
| German | 142 | — | — | Collected but EXCLUDED |
| Spanish | 63 | — | — | Collected but EXCLUDED |

> All entries include: original proverb text, English translation, cultural explanation. Arabic = Modern Standard Arabic (fus-ha), not dialectal.

---

## 2. Benchmarked subset (3 languages, N=150 May pilot / N=5 v68)

The original May paper draft §3.1 states unambiguously: **"The current benchmark uses three languages"**; FR/DE/ES are "collected but excluded from the current benchmark due to insufficient sample sizes for statistical validity."

### May pilot (v3 / v4.3.4, Groq)
- 50 proverbs per language × 2 strategies × 3 styles = 300 MCQs, 1,500 API evals, 1,200 encoder evals.
- Sources: `kaggle/kaggle_analysis/input/strategy1_*.csv`, `strategy2_*.csv`, `evaluation_results.csv`.

### v68 production (OpenRouter, 180 MCQs)
- 5 proverbs per language × 4 variants × 3 generators = **180 MCQs**.
- `pilot1_test_generated_mcqs.csv`: **180 rows** = 60 EN + 60 AR + 60 YO (README §5.2: 60 each).
- `pilot1_test_audit_results.csv`: 180 × 4 = 720 blind audit votes.

**Conflict flag (data_inventory.txt "CATASTROPHIC DATA MISMATCH"):** `actual_data/data_inventory.txt` header declares a catastrophic mismatch — the *current* `actual_data/*_cleaned.csv` schemas/formats differ from legacy usage. The `actual_data/inventory.json` records the mismatch and liability notes but the canonical generation inputs for v68 live under `kaggle/run_logs/v68/` and `kaggle/kaggle_analysis/input/`.

---

## 3. Copyright & licensing (BLOCKED)

Per README §8 and LICENSE: **data licensing is BLOCKED pending provenance/rights review; datasets are NOT released under CC BY 4.0.**

| Language | Status | Detail |
|---|---|---|
| **English** | Scraped public-domain | Specific URLs **not recovered**; rights verification pending. |
| **Arabic** | MID-prefix academic dataset | Source **unidentified**; licensing under review. |
| **Yoruba** | **Copyrighted** | Derived from Owomoyela (2005), *Yoruba Proverbs*, University of Nebraska Press. **No redistribution permission obtained.** |

### Yoruba ISBN conflict (must reconcile)
| Source | ISBN | Note |
|---|---|---|
| `docs/ProverbGap_Paper_Draft.md` §3.1 + memory graph "Yoruba Proverbs" entity | **0-8032-3576-3** (10-digit); "5,235 proverbs in book, 3,974 extracted, OCR'd" | Lowercase-L ISBN form |
| `README.md` §8 + `DATA_PROVENANCE_TEMPLATE.md` | **978-0-8032-1843-7** (13-digit) | Different ISBN digits |

These are **different ISBNs** (neither is a trivial 10↔13 conversion — `0-8032-3576-3` ↔ `978-0-8032-3576-5`, not `1843-7`). At least one is wrong. **Action item:** verify which Owomoyela (2005) volume/editions these map to (UNL Press bibliography). This affects legal clearance.

### Yoruba copyright exposure (UNRESOLVED)
README §8: public release planned as **English + Arabic only** ("Yoruba excluded pending owner approval").  
**However:** `kaggle/run_logs/v68/openrouter_pilot1_test_output/pilot1_test_generated_mcqs.csv` contains **60 Yoruba MCQ rows** (60 EN + 60 AR + 60 YO). The CSV was generated and frozen at `data/production/paper_first_outputs_2026-06-22_10-42-02/`.  
→ **Copyright exposure is active** until Yoruba rows are removed or permission is obtained. `data_inventory.txt` flags this as a data-rights issue pending owner approval.

---

## 4. Data lineage: original → v68

```
7,172 proverbs (6 langs)
  └─> Benchmarked 3 langs: EN 2,278 / AR 913 / YO 3,931   (Paper Draft §3.1)
      ├─> May pilot (v3): 50 proverbs/lang × 2 strat × 3 styles = 300 MCQs
      │     outputs: kaggle_analysis/input/strategy1|2_*.csv, evaluation_results.csv
      └─> v68 (OpenRouter): 5 proverbs/lang × 4 variants × 3 gen = 180 MCQs
            outputs: pilot1_test_generated_mcqs.csv (180), pilot1_test_audit_results.csv (720)
```

### Format lineage
- Original May pipeline: MCQ-only (paper draft §7.3/7.4 mark FiB & Generation as **future**).
- `.archive/legacy_data_2026-06-19/` contains the frozen source proverbs (snapshot).
- `actual_data/*_cleaned.csv` = current curated proverbs (3 langs). `cleaned/` subdir duplicates. `Arabic_cleaned (1).csv` = duplicate (disambiguated by space-paren).

### The 16,439 / 25,190 row question (FiB / Generation)
Memory graph entities "FiBFiBlank Task" (16,439 valid rows, 3 metrics EM/NEM/ChrF++) and "Generation Task" (25,190 clean Task A rows, 8 models, DeepSeek-R1 100% gold-copying) report **real outputs** that are **not** found in `kaggle/` or `.archive/`. They correspond to the post-May-18 FiB/Generation exploration that was abandoned when the central thesis was invalidated. **No CSV artifacts recovered** for these — likely lost or never committed. (See Document 03 §Phase A v3.1.)

---

## 5. Contamination handling
- English: hardcoded filter of 25 famous-proverb substrings removes ≈8.3% (paper draft §3.2).
- Arabic/Yoruba: no explicit contamination filter documented (lower pretraining risk; tonal/morphology differences).

---

## 6. Provenance gaps / reviewer concerns (from history doc §6)
1. Sources not fully documented → **publication blocker**.
2. Yoruba permissions unclear → **resolved only by exclusion**, but 60 Yoruba rows still shipped (§3).
3. ≥2/50 (4%) Arabic items have wrong/misleading gold meanings → **quality defect**.
4. No human validation → serious weakness for top venues.
5. Hardcoded API keys in code → security risk, blocks public sharing.

---

## 7. Evidence map (provenance)

| Claim | Source file | Confidence |
|---|---|---|
| 7,172 proverbs, 6 languages | Paper Draft §3.1 | High |
| EN 2,278 / AR 913 / YO 3,931 | Paper Draft §3.1 | High |
| FR/DE/ES excluded (insufficient N) | Paper Draft §3.1 | High |
| EN scraped, URLs unrecovered | README §8 | High |
| AR MID-prefix, source unidentified | README §8 | High |
| YO = Owomoyela 2005 (UNL Press) | README §8, Paper Draft §3.1 | High |
| Owomoyela ISBN 0-8032-3576-3 / 5,235→3,974 | memory "Yoruba Proverbs" entity | Medium |
| Owomoyela ISBN 978-0-8032-1843-7 | README §8 | Medium (conflicts above) |
| 60 Yoruba rows in v68 CSV | README §5.2; pilot1_test_generated_mcqs.csv row count | High |
| "CATASTROPHIC DATA MISMATCH DISCOVERY" | actual_data/data_inventory.txt (header) | High |
| FiB 16,439 / Gen 25,190 rows | memory graph entities | Medium (no CSVs found) |
