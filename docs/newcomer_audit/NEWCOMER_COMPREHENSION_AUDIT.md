# Newcomer Comprehension Audit

**Method:** the repository was read as a first-time researcher would (start at README → follow links → reconstruction dossier → data docs → register). Every point where a reader would have to guess was recorded, then fixed in this pass or marked unresolved. "Fixed" means the information now exists in the repository and is linked from the README.

| ID | Location | What a newcomer saw | Why confusing | Evidence needed | Correction | Status |
|---|---|---|---|---|---|---|
| N-1 | Phase 1 docs (transferred) | Paths like `kaggle/run_logs/v68/...`, `actual_data/...` | Links resolve nowhere in this repo | SOURCE_MAP note | Explicit note that these are old-repo references (SOURCE_MAP note 2; DATA_DICTIONARY header) | ✅ Fixed (documented, links intentionally preserved) |
| N-2 | Old root README | "S1/S2", "HCW", "MCQ" used before definition | Acronyms undefined at first use | Glossary | New README defines S1/S2/HCW inline; `docs/GLOSSARY.md` covers all terms | ✅ Fixed |
| N-3 | Old README §5 | "Consensus accuracy 56.7%", "HCW 27.8%" | No numerator/denominator, no source file | audit_results.csv | `docs/experiments/EXPERIMENT_REGISTER.md` §8 gives 102/180, 75/180, 50/180 + file path + recomputation date | ✅ Fixed |
| N-4 | Phase 1 docs 02/04 | "S1 86.8% / S2 62.5%" | Not traceable to any surviving artifact | verification_cross.md | Register §2 states figures were verified 2026-05-24 against since-overwritten files (651/750, 369/590) and are **not locally reproducible now** | ✅ Fixed (honest provenance) |
| N-5 | Phase 1 docs | "v59–v67", "v65/v66/v67" mentioned without definition | Version semantics unknown | run_logs dirs | Register §7 defines them as notebook versions of `mcq-pass-shortcut` with smoke/regression roles | ✅ Fixed |
| N-6 | Phase 1 docs 01/04 | evaluation_results.csv described as May pilot output | File is actually the June failed run | Recomputation (2,440 errors; all S2 failed) | Discrepancy D-3 + register §6 correct the attribution | ✅ Fixed |
| N-7 | Phase 1 docs 02; paper draft §7 | FiB/Generation "planned, future tense" | Contradicted by Kaggle kernels that ran May 19 | Kaggle API + recovered outputs | Register §4–5; discrepancy D-5 | ✅ Fixed |
| N-8 | (absent) | No column-level dataset documentation anywhere | Newcomer cannot interpret any CSV | File headers read 2026-10-26 | `docs/data/DATA_DICTIONARY.md` (all schemas, counts, unknowns flagged) | ✅ Fixed |
| N-9 | (absent) | No explanation of record flow (proverb → MCQ → vote → metric) | Lineage had to be guessed | Artifacts + code | `docs/data/DATASET_LINEAGE.md` with mermaid diagram, units-of-observation table | ✅ Fixed |
| N-10 | run_logs listing | v62 missing between v61 and v63 | Numbering gap unexplained | Directory listing | Recorded as D-8 (unresolved, note only) | ⏸️ Unresolved (documented) |
| N-11 | Phase 1 NEXT_STEPS | "what happens next" mixed owner decisions with executable tasks | Reader can't tell what they may do | — | New README "What should happen next" + GETTING_STARTED Step 8 gates | ✅ Fixed |
| N-12 | v68 human_annotation_sample.csv | Human columns exist | Could be mistaken for completed annotation | File read: 0/30 filled | DATA_DICTIONARY §3.4 + register §12 state "prepared, never executed" | ✅ Fixed |
| N-13 | (absent) | `annotation_app/` (a whole web app) undocumented in Phase 1 | Human-validation tooling invisible | README + .vercel + onboarding doc inspected | Register §12 + crosswalk §3 document the app, its stack, deployment, and that no annotation records exist | ✅ Fixed |
| N-14 | (absent) | Kaggle side of the project entirely missing | Can't find where runs actually executed | Kaggle API metadata | `docs/experiments/LOCAL_AND_KAGGLE_ARTIFACT_CROSSWALK.md` (kernels, datasets, statuses, recovery) | ✅ Fixed |
| N-15 | (absent) | Security exposure (.env.local; private Kaggle key dataset) unknown | Newcomer might copy secrets | Presence-only checks | D-13 documents without reproducing contents; GETTING_STARTED rule 2 warns | ✅ Fixed |
| N-16 | Phase 1 docs 03 | "Central thesis invalidated May 18" — cause never explained | Pivot reason is folklore | Memory export + June-4 audit claim | ORIGINAL_VS_SHORTCUT §2 + D-4 mark the mechanism as narrative-only | ✅ Fixed (uncertainty made explicit) |
| N-17 | Paper draft / docs | "7,172 proverbs" repeated | Arithmetic error propagates | verification_mentor.md | Discrepancy D-2; README no longer repeats 7,172 uncritically | ✅ Fixed |
| N-18 | (absent) | Which results can be trusted? | No evidence hierarchy | — | Register evidence levels + GETTING_STARTED Step 7 trust table | ✅ Fixed |
| N-19 | GLOSSARY (needed) | Many project-specific terms | Jargon | — | `docs/GLOSSARY.md` created | ✅ Fixed |
| N-20 | Kaggle dataset `original-data` | FR/DE/ES presence | Counts unknown | File sizes only | DATA_DICTIONARY §1.4 marks counts unverified | ⏸️ Partially (owner can download) |

## Remaining gaps a newcomer still hits

1. The May pilot's raw files are gone locally (D-3) — a reader must trust the May 24 verification reports or ask the owner to export the Kaggle kernel version.
2. The 24.9% construct-validity claim has no artifact (D-4).
3. FR/DE/ES schemas/counts unverified (N-20).
4. Whether the deployed annotation app ever collected data (Supabase access needed).
5. v62's fate (D-8) and the content differences among v59–v67 runs (diffable, but not yet done).
