# Phase 7 — DECISION_LOG

| # | Decision | Date | Rationale | Outcome / Status |
|---|---|---|---|---|
| D1 | qwen3-32b as S2 generator (Alibaba, ≠ committee) | May 2026 | Eliminate same-family exploitation | ✅ Successful |
| D2 | Skip CoT for llama-4-maverick | May 2026 | 23/24 NaN, 29% accuracy | ✅ Successful |
| D3 | API-only committee (drop 3–5→2) | May 2026 | API instability | ✅ Functional |
| D4 | Pivot May 18: methodology over benchmark | May 18 2026 | Central thesis invalidated | 🔄 Locked scaling |
| D5 | Groq→OpenRouter migration | May→Jun 2026 | Cost + reliability | ✅ Enabled v65–v70 |
| D6 | Do NOT scale N=15; run v69 ablation first | Jun 22 2026 | v68 failed 4/6 gates | ⛔ v69 never run |
| D7 | v68 = production dataset | Jun 26 2026 | Budget exhausted; v69/v70 inconclusive | ✅ Final |
| D8 | English+Arabic only; Yoruba excluded pending rights | Jul 2026 | Copyright exposure | ⚠️ 60 YO rows still in CSV |
| D9 | Human validation = planned-only | Jul 10 2026 | Budget | 📋 60-sample prepared |
| D10 | EACL 2027 ARR target | Jul 2026 | Aug 3 2026 deadline | ❓ Submission unconfirmed |
| D11 | Archive legacy (Jun 19) under `.archive/` | Jun 19 2026 | Preserve originals, unclutter repo | ✅ Done |

Owner decisions still pending: D-fork (A/B/C) — see `PHASE7_MIGRATION_PLAN.md` §Pre-conditions; S2 validity (Q2); Yoruba rights (Q3); EACL status (Q7).
