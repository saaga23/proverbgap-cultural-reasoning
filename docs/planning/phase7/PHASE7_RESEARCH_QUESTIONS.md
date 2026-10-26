# Phase 7 — RESEARCH_QUESTIONS

## Direction A (original, May 2026) — `02_ORIGINAL_RESEARCH_RECONSTRUCTION.md`
- **RQ1.** Can LLMs distinguish a proverb's correct meaning from same-language distractors (S1)?
- **RQ2.** Can LLMs reject cross-family LLM-paraphrased adversarial distractors (S2)?
- **RQ3.** Is the S1→S2 accuracy gap a genuine Cultural/Literal Reasoning Gap (not a shortcut)?
- **RQ4.** Do same-family generator/evaluator pairs inflate accuracy (exploitation)?
- **RQ5.** Do the four prompting styles (zero-shot/CoT/few-shot) and four encoder baselines change discrimination?
- **H1–H4 / C1–C5:** see `ProverbGap_Status_Document.docx` (Apr 24) extract, captured in `03_CHRONOLOGICAL_RESEARCH_TIMELINE.md`.

## Direction B (v68 shortcut audit) — `08_SHORTCUT_AUDIT_HISTORY_AND_CROSSWALK.md`
- **RQ-A1.** Do generated distractors resist the "longest answer / echo / position" shortcuts?
- **RQ-A2.** Which of the four generation variants produces the most shortcut-resistant distractors?
- **RQ-A3.** Which of the three generators is most robust (lowest HCW)?
- **RQ-A4.** Does the corpus-fallback sampler create confident-wrong (HCW) traps more than generators?
- **RQ-A5.** Does the blind options-only committee agree with eventual human validation (IAA)?

> The May RQs framed *accuracy*; the v68 RQs frame *distractor quality*. The pivot swapped RQ3's "is there a gap" for "are the distractors trustworthy."
