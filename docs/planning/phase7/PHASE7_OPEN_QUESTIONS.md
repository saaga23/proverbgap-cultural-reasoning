# Phase 7 — OPEN_QUESTIONS

**Status:** Open — require owner decision. None can be resolved by further read-only inspection.

## Research-direction (the fork)
1. **One narrative or two?** Does the owner want (A) a *benchmark* paper (restore May direction: S1/S2 accuracy, N=700, FiB/Generation), (B) a *methodology + failure-taxonomy* paper (v68 audit), or (C) a hybrid? Each mandates different number sets and a different dataset scale. See `08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md` §7.
2. **S2 validity:** Accept the disputed 62.5% (with caveat), re-analyze the 24.9%-real-paraphrase figure, or drop S2 entirely in favor of the HCW gate? Blocks using May numbers in any paper.

## Data & rights
3. **Yoruba copyright:** Reconcile ISBN `0-8032-3576-3` vs `978-0-8032-1843-7`; confirm whether 60 Yoruba rows may remain in v68 CSV or must be purged. Blocks data release.
4. **English/Arabic provenance:** Recover scraped URLs and the MID-prefix Arabic source. Blocks rights-compliant release.
5. **FiBFiBlank / Generation outputs** (16,439 / 25,190 rows): located anywhere, or treated as permanently lost? Blocks restoring the original 3-format claim.

## Budget & publication
6. **OpenRouter budget:** Any new credits available for v69 (~$1) / v70 scale (~$2.56) / human validation ($200–300)?
7. **EACL 2027 ARR:** Was anything submitted by the Aug 3 2026 deadline? If missed, what's the next venue (EMNLP, ACL, NAACL rolling)? Submission status unconfirmed in repo.
8. **Human validation:** Proceed with the 60-item audit sample (prepared) or wait for full 100-item KNIGHT-standard budget?

## Technical (Phase 2 decisions)
9. **v69 ablation design:** The v68 report proposes `USE_LLM_FALLBACK=True`, `openai/gpt-4.1-nano`. Confirm, or iterate on NLI/leak filter thresholds (§7.5) instead?
10. **Same-family audit:** v69 plans a qwen vs other-families same-family experiment. Confirm inclusion.
11. **Position-bias treatment:** v68 only *checks* balance (no mitigation). Restore seeded per-model shuffle for the next generation run?

## Repo hygiene
12. **Two live READMEs:** Reconcile `docs/ProverbGap_Paper_Draft.md` (May) vs `README.md`/`paper/proverbgap_eacl2027.md` (July) — which is canonical going forward?
13. **Stale `main_results_table.csv`** shows corrupted 14.7%/0.0% numbers. Confirm deprecation and add a warning header, or delete.
14. **`.archive/legacy_code_2026-06-19/`** is frozen; should Phase-2 edits branch from `main` or from the archive snapshot?

## Evidence gaps that could not be resolved (Phase 1)
15. The v68 summary lacks a top-level `config`/`generators`/`variants` key (those live under `generator_pool`/`committee_pool`/`substitutions`); some docs that generically cite "v68 summary shows X%" were cross-checked against `pilot1_test_summary.json` directly. Flagged where sources disagreed.
16. `actual_data/data_inventory.txt` header reads "CATASTROPHIC DATA MISMATCH DISCOVERY" but the file body is terse; full schema diff vs. legacy usage not re-derived.
