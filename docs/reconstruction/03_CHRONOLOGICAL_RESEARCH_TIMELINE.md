# Phase 1 — Document 03: Chronological Research Timeline & Pivot Mechanisms

**Status:** Completed
**Purpose:** Document the full timeline from original ProverbGap (Apr–May 2026) through the June shortcut-audit pivot (v65–v70), the July paper-first reframing, and the Aug 3 2026 EACL deadline. Identifies *when* each pivot decision was made and by what evidence.

**Sources:** `docs/ProverbGap_Paper_Draft.md` (May), `.archive/legacy_docs_2026-06-19/ProverbGap_Status_Document.docx` (Apr 24 extract), `.archive/legacy_docs_2026-06-19/ProverbGap_MCQ_Project_History.docx` extract, `.archive/legacy_docs_2026-06-19/create_project_history_doc.py`, `kaggle/run_logs/*` (v65–v70), README §10 "Status and Next Steps", `docs/EXECUTION_ITINERARY_2026-07-10.md`, `docs/gap_liability_analysis_2026-07-10.md`, `docs/ProverbGap_Reframed_Title_Abstract.md`, `memory_proverbgap_filtered.json`.

---

## Timeline

### Phase A — Original Design (Apr 24 → May 2026)

| Date | Event | Evidence |
|---|---|---|
| Apr 24 2026 | **Status Document** authored. Defines 5 RQs (RQ1–RQ5), 4 H1–H4, 5 C1–C5. 6-language plan (EN/AR/FR/DE/ES/YO), MCQ + FiB + Generation, two-task literal/cultural. | `.archive/legacy_docs_2026-06-19/ProverbGap_Status_Document.docx` (extract) |
| Apr → May 2026 | Groq-based pipeline built: MCQ generation (S1/S2), committee eval (3 styles), encoder baselines, statistical testing. | `docs/ProverbGap_Paper_Draft.md` §4 |
| May (early) | N=150 pilot run (`run_20260523_224443`): 300 MCQs, 1,500 API evals, 1,200 encoder evals, ~22 min, 7 checkpoints, 6 figures. S1 86.8%, S2 62.5%, McNemar p<0.001. | `docs/ProverbGap_Paper_Draft.md` §5 |
| May 18 2026 | **Central thesis invalidated.** Paper-draft memory entity: "Central thesis invalidated May 18 2026 — pivoted to standalone methodology paper." FiB (16,439 rows) and Generation (25,190 rows) tasks explored and abandoned same window. | Memory graph "FiBFiBlank Task" / "Generation Task" entities |
| May 20 2026 | `ProverbGap_MCQ_Project_History.docx` authored (records v1–v4.3.4 history). | `.archive/legacy_docs_2026-06-19/` |

**Pivot #1 (May 18):** Original "Cultural Reasoning Gap" benchmark → "standalone methodology paper." The difficulty-gap design (S1 vs S2) was no longer the central claim; methodology/negative-results became the focus.

### Phase B — Provider Migration (May → Jun 22, 2026)

| Date | Event | Evidence |
|---|---|---|
| May 20 → Jun | Migration Groq → OpenRouter (cost + stability). v64, v65, v66 development. | `memory_proverbgap_filtered.json`; `create_project_history_doc.py` |
| Jun (early) | v65 (N=1 smoke): HCW 11.1%. | `kaggle/run_logs/v68/v68_detailed_analysis_report.md` §2 |
| Jun (mid) | v66 (N=1 regression): perfect-consensus 55.6%, HCW 22.2%. | v68 report §2 |
| Jun 13 2026 | **Corruption note.** `ProverbGap_MCQ_Project_History.docx` records answer-key shuffle bug producing S1 14.7%, S2 0.0% in `main_results_table.csv`. Deprecated `scale_readiness_report.md` (v4.1) carries these numbers. | `kaggle/kaggle_analysis/analysis_output/main_results_table.csv`; `scale_readiness_report.md` |

### Phase C — Shortcut Audit (Jun 13 → Jun 22, 2026)

| Date | Event | Evidence |
|---|---|---|
| Jun 13–18 2026 | Design audit gates (HCW, perfect-consensus, partial+fallback, hard-fallback, duplicates, key-balance) as *minimum viable quality bars*, plus 4 variants (adversarial-hard-negative, adversarial-length-locked, overgenerate-select, taxonomy-guided) and blind options-only committee. v67 frozen baseline. | `kaggle/run_logs/v68/v68_detailed_analysis_report.md` §1, §7 |
| **Jun 22, 2026 00:30Z** | **v68 completed & audited.** 180 MCQs (15 proverbs × 4 variants × 3 generators), seed 20260615, $0.85. `USE_LLM_FALLBACK=False`. 720 audit votes, 0 missing, 0 substitutions. | `pilot1_test_summary.json`, audit_results.csv |
| Jun 22, ~10:42Z | Paper-first outputs frozen: `data/production/paper_first_outputs_2026-06-22_10-42-02/`. Human-validation sample (60 items) prepared. | README §9; `data/production/` |

**v68 gate verdict (all but 2 failed):**

| Gate | v68 | Target | Pass? |
|---|---|---|---|
| Hard fallback rate | 16.1% | <5% | ❌ |
| Partial + fallback | 43.9% | <15% | ❌ |
| HCW (≥0.75) | 27.8% | <10% | ❌ |
| Perfect consensus | 41.7% | <30% | ❌ |
| Per-language correctness ≥50% | EN 65 / AR 53.3 / YO 51.7 | ≥50 | ⚠️ fragile |
| Duplicate options | 0 | 0 | ✅ |
| Correct-key balance | 45/45/45/45 | ~25% each | ✅ |

**Pivot #2 (Jun 22):** Original "scale to N=15 if gates pass" → **"do not scale; v69 ablation (USE_LLM_FALLBACK=True) at N=5 first"** (v68 report §7.1–7.2). If v69 improves HCW <15% → scale to v70; else publish v68 as the dataset and frame corpus-fallback failure as a contribution.

### Phase D — Ablation Attempt (Jun 22 → Jun 26, 2026)

| Date | Event | Evidence |
|---|---|---|
| Jun 22 late | v69 planned (LLM fallback via openai/gpt-4.1-nano). | v68 report §7.2; README §5 v68 summary |
| Jun ~24–26 2026 | **v69 never executed.** OpenRouter budget exhausted before start. No CSVs/summary.json produced — only analysis scripts & templates (all TBD blanks). | `kaggle/run_logs/v69/` tree; `RESEARCH_HISTORY_AND_README_AUDIT.md` |
| Jun 26 2026 (approx) | **v70 attempted** (USE_LLM_FALLBACK=True) but **HALTED**: 83/180 rows, $0.42, `generation_done=False`, `audit_done=False`. OpenRouter 403 budget limit; adversarial-hard-negative 11/15 rows. | `kaggle/run_logs/v70/pool_state.json`, partial CSV |

**Pivot #3 (Jun 26):** Original "scale via v69→v70" → **"v68 is the production dataset; budget exhausted."** Paper-first reframing solidified.

### Phase E — July Paper-First Reconciliation

| Date | Event | Evidence |
|---|---|---|
| Jul 10 2026 | `gap_liability_analysis_2026-07-10.md`: flags fatal inconsistency — paper draft claims 2,313 MCQs / 86.8%-62.5% but v68 production = 180 MCQs. | `docs/gap_liability_analysis_2026-07-10.md` |
| Jul 10 2026 | `EXECUTION_ITINERARY_2026-07-10.md`: EACL 2027 ARR plan; budget exhausted; human validation "planned-only", depends on external funding. | `docs/EXECUTION_ITINERARY_2026-07-10.md` |
| Jul 2026 | `docs/ProverbGap_Reframed_Title_Abstract.md`: reframes as "Hardened Adversarial Distractor Generation for Low-Resource Figurative Language" — methodology + failure taxonomy, with v68 as dataset. | `docs/ProverbGap_Reframed_Title_Abstract.md` |
| Jul (ongoing) | README rewritten; `data_inventory.txt` "CATASTROPHIC DATA MISMATCH DISCOVERY" written; legacy code/data/docs archived to `.archive/legacy_*_2026-06-19/`. | `actual_data/data_inventory.txt`, `.archive/` |

**Pivot #4 (Jul 10):** "Complete human validation + scale" → **"human validation is planned-only / depends on external funding."** Methodology + failure taxonomy becomes the paper's core, with v68 N=5 as the production dataset (not N=150 pilot).

### Phase F — August Deadline

| Date | Event | Evidence |
|---|---|---|
| Aug 3 2026 | EACL 2027 ARR submission deadline. | README §10; paper target |
| Aug 2026 (target) | Submission status in repo: **UNCROSSED** — no paper ID, no reviewer decision, no submission confirmation record. | README §10 ("status unconfirmed … must be verified by owner") |

---

## Pivot decision trace (who / where)

| Pivot | Decision maker | Where recorded | Trigger |
|---|---|---|---|
| #1 May 18 | (author) | memory "FiBFiBlank Task" / "Generation Task" entities | Central thesis invalidated (FiB/Gen tasks showed gold-copying; S2 not robustly harder) |
| #2 Jun 22 | v68 run lead | `v68_detailed_analysis_report.md` §7 | 4/6 shortcut-resistance gates failed |
| #3 Jun 26 | (owner) | README §10; v70 pool_state | Budget exhausted; v69 unrun |
| #4 Jul 10 | (owner) | `gap_liability_analysis`, `EXECUTION_ITINERARY` | Inconsistency exposed; scope reduced to methodology/failure taxonomy |

---

## Key contradictions resolved in this timeline

| Apparent contradiction | Resolution |
|---|---|
| "v68 README says 11.1% HCW" vs "other docs show 27.8%" | No contradiction: README §5 says HCW **rose from 11.1% in v65 (N=1) to 27.8% at N=5 (v68)**. The 11.1% is v65's value, 27.8% is v68's. |
| "scale_readiness_report shows S1 14.7%, S2 0.0%" | Those are **corrupted** v4.1 (Groq) numbers from the June 13 answer-key-shuffle bug; carried into `main_results_table.csv`. Deprecated 2026-06-19. Not v68. |
| "6 languages / 3 formats in v4.3.6" vs "3 languages / MCQ-only in May draft" | The May v1.0 draft is contemporaneous authority: 3 languages benchmarked, FiB/Gen planned. 6-lang/3-format is a later over-claim; the 16K/25K FiB/Gen rows are a post-May-18 abandoned exploration. |
| "v69 summary shows 9.3% LLM fallback" (some docs) | v68 itself had `substitutions={generators:[],auditors:[]}` → 0% fallback (`USE_LLM_FALLBACK=False`). The "9.3%" figure belongs to the **original May Run-22 N=50** results (memory "Run 22" entity), not v68. Mis-attribution in some docs. |
| "v70 halted at 83 vs 11 rows" | 83 = total generation rows written to CSV; 11/15 = the *final* adversarial-hard-negative variant's rows at halt (the run was mid-variant-set, on the last variant when budget cut it off). Both describe the same halt. |

---

## Decision log (condensed)

| # | Decision | Date | Rationale | Outcome |
|---|---|---|---|---|
| D1 | Use qwen3-32b (not llama-4) as S2 generator | May 2026 | Eliminated same-family exploitation (llama gen + llama eval = 57.8% vs 26.7% S1) | Successful |
| D2 | Skip CoT for llama-4-maverick | May 2026 | 23/24 NaN, 29% accuracy | Successful |
| D3 | 2-model committee (dropped to 2 from 3–5) | May 2026 | API instability | Fragile but functional |
| D4 | Pivot May 18: methodology paper over benchmark-scaling | May 18 2026 | Central thesis invalidated | Locked original scaling |
| D5 | Migration Groq→OpenRouter | May→Jun 2026 | Cost/perf | Enabled v65–v70 |
| D6 | Do NOT scale to N=15; run v69 ablation first | Jun 22 2026 | v68 failed 4/6 gates | v69 never run |
| D7 | v68 = production dataset; frame failure as contribution | Jun 26 2026 | Budget exhausted, v69/v70 inconclusive | Final |
| D8 | Publish English+Arabic only; Yoruba excluded pending rights | Jul 2026 | Copyright exposure (Owomoyela) | Yoruba still in v68 CSV — UNRESOLVED |
| D9 | Human validation = planned-only | Jul 10 2026 | Budget | Blocks full paper framing |
