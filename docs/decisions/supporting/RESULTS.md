# Supporting Results — Recomputation Log (2026-10-26)

Run command (no API calls; read-only):

```bash
python docs/decisions/supporting/recompute_checks.py \
  --old-repo "<local path to saaga23/proverb_mcq>" \
  --kaggle-fib <nb_pilot_30_results.csv> \
  --kaggle-gen <pilot_results.csv>
```

The two Kaggle CSVs are re-downloadable with:
`python -m kaggle kernels output abrahamsunday123/proverb-gap-fill-in-the-blank -p <dir>`
`python -m kaggle kernels output abrahamsunday123/proverbgap-generation -p <dir>`

## Output (verbatim)

- **JUNE_EVAL_RUN:** rows_total 2700; S1 rows 1350 (valid 260, valid-accuracy **76.2%**; failures-counted-as-misses **14.7%**); S2 rows 1350 (**valid 0** — accuracy undefined). This proves the surviving `evaluation_results.csv` is the June failed run and cannot yield the May pilot numbers.
- **V68_METRICS (reproduced):** consensus accuracy **102/180 = 56.7%**; perfect consensus **75/180 = 41.7%**; HCW **50/180 = 27.8%**.
- **TWO_PROP_PLAUSIBILITY** (S1 651/750 vs S2-strict 369/590): diff 0.2426, z = 10.34, χ²(1df) = **106.9** — same order as the reported χ² = 131.3 but *not the same statistic*; the reported test's exact form and pairing are not reconstructable (see memo §A3).
- **DECOMPOSITION_CHECK:** Run 22 mixture 0.093×89.6 + 0.907×30.0 = **35.5** vs reported overall **35.6** → consistent. Run 23: 0.093×88.8 + 0.907×31.5 = **36.8** vs **36.9** → consistent. Claimed 24.9% in the same mixture = **30.9**, matching *neither* 35.6 nor 36.9 → the 24.9% figure is internally inconsistent with its companion numbers.
- **FIB:** 30 rows = 30 unique items (10 EN / 10 AR / 10 YO); task a=20, b=10; extraction status FALLBACK_LINE for all 90 predictions (answer taken from last line rather than the structured format); mean EM 0.133 (A) / 0.100 (B) / 0.133 (C); mean ChrF 0.169 / 0.140 / 0.190. Real-context (A) ≈ sham-context (C) at this scale.
- **GENERATION:** 2,160 rows = 90 unique items × 6 models × 2 tasks × 2 strategies; SUCCESS 1,677/2,160 (77.6%); per-model success and gold-copying: Gemma-4-31B 349/360 (3.7% copy), LLaMA-3.1-8B 258/360 (11.2%), LLaMA-3.3-70B 261/360 (10.0%), LLaMA-4-Maverick 337/360 (8.0%), Nemotron-120B 347/360 (6.1%), Qwen3-32B **125/360 success (34.7%)** (8.0% copy); mean BLEU 2.7–4.3; mean semantic_sim 0.153–0.182; **DeepSeek-R1 absent from the run** (memory claim contradicted).
