"""Reproducible re-computation checks backing PROVERBGAP_EVIDENCE_RECOVERY_AND_NEXT_EXPERIMENT.md.

All inputs are read-only. Paths point into the source repository `saaga23/proverb_mcq`
or to artifacts recovered from Kaggle (see README in this folder). No API calls.

Usage:
  python recompute_checks.py --old-repo <path-to-proverb_mcq> [--kaggle-fib <csv>] [--kaggle-gen <csv>]
"""
import argparse, csv, io, subprocess, sys
from collections import Counter, defaultdict


def june_eval_run(repo):
    """June 8/9 Kaggle run: the only evaluation_results.csv that survives."""
    p = repo + r"/kaggle/kaggle_analysis/input/evaluation_results.csv"
    rows = list(csv.DictReader(open(p, encoding="utf-8-sig")))
    def valid(r):
        return r["error"] in ("", "None", "none", "nan", None)
    s1 = [r for r in rows if r["strategy"] == "S1"]
    s2 = [r for r in rows if r["strategy"] == "S2"]
    v1 = [r for r in s1 if valid(r)]
    v2 = [r for r in s2 if valid(r)]
    out = {
        "rows_total": len(rows),
        "S1_rows": len(s1), "S1_valid": len(v1),
        "S1_valid_acc": round(100 * sum(int(r["hit"]) for r in v1) / len(v1), 1) if v1 else None,
        "S1_all_as_miss_acc": round(100 * sum(int(r["hit"]) for r in s1) / len(s1), 1),
        "S2_rows": len(s2), "S2_valid": len(v2),
        "note": "All S2 rows failed => S2 accuracy undefined in this artifact.",
    }
    return out


def v68_metrics(repo):
    p = repo + r"/kaggle/run_logs/v68/openrouter_pilot1_test_output/pilot1_test_audit_results.csv"
    rows = list(csv.DictReader(open(p, encoding="utf-8-sig")))
    n = len(rows)
    ca = sum(r["consensus_correct"] == "1" for r in rows)
    pc = sum(float(r["consensus_frac"]) >= 1.0 for r in rows)
    hcw = [r for r in rows if float(r["consensus_frac"]) >= 0.75 and r["consensus_correct"] == "0"]
    return {"n": n, "consensus_acc": f"{ca}/{n}={100*ca/n:.1f}%",
            "perfect_consensus": f"{pc}/{n}={100*pc/n:.1f}%",
            "HCW": f"{len(hcw)}/{n}={100*len(hcw)/n:.1f}%"}


def two_prop_chi2(x1, n1, x2, n2):
    """Plausibility check for the reported S1-vs-S2 significance (NOT McNemar)."""
    p = (x1 + x2) / (n1 + n2)
    se = (p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5
    z = (x1 / n1 - x2 / n2) / se
    return {"diff": round(x1 / n1 - x2 / n2, 4), "z": round(z, 2), "chi2_1df": round(z * z, 1)}


def decomposition_check():
    """Arithmetic identity test for the '24.9% / 30.0% / 31.5%' claims (Run 22 / Run 23)."""
    res = {}
    for name, fb_rate, fb_acc, real_acc, overall in [
        ("Run22", 0.093, 89.6, 30.0, 35.6),
        ("Run23", 0.093, 88.8, 31.5, 36.9),
        ("claimed_24.9", 0.093, 89.6, 24.9, None),
    ]:
        mix = fb_rate * fb_acc + (1 - fb_rate) * real_acc
        res[name] = {"mixture": round(mix, 1), "reported_overall": overall,
                     "consistent": (overall is None) or abs(mix - overall) <= 0.5}
    return res


def fib_descriptives(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig")))
    out = {"rows": len(rows), "unique_sample_ids": len(set(r["sample_id"] for r in rows)),
           "languages": dict(Counter(r["language"] for r in rows)),
           "task": dict(Counter(r["task"] for r in rows)),
           "extraction_status": dict(Counter(r["status_a"] for r in rows))}
    for c in "abc":
        em = [float(r[f"em_{c}"]) for r in rows if r[f"em_{c}"] not in ("", "nan")]
        out[f"cond_{c}_mean_em"] = round(sum(em) / len(em), 3)
        out[f"cond_{c}_mean_chrf"] = round(sum(float(r[f"chrf_{c}"]) for r in rows if r[f"chrf_{c}"] not in ("", "nan")) / len(em), 3)
    return out


def generation_descriptives(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig")))
    ok = [r for r in rows if r["status"] == "SUCCESS"]
    per_model = {}
    for m in sorted(set(r["display"] for r in rows)):
        sub = [r for r in rows if r["display"] == m]
        s = [r for r in sub if r["status"] == "SUCCESS"]
        cg = sum(1 for r in s if r["contains_gold"] == "True")  # string compare; 'False' is truthy
        bleu = [float(r["bleu"]) for r in s if r["bleu"] not in ("", "nan")]
        sem = [float(r["semantic_sim"]) for r in s if r["semantic_sim"] not in ("", "nan")]
        per_model[m] = {"success": f"{len(s)}/{len(sub)}", "gold_copy": f"{cg}/{len(s)} ({100*cg/max(1,len(s)):.1f}%)",
                        "mean_bleu": round(sum(bleu) / len(bleu), 1), "mean_sem": round(sum(sem) / len(sem), 3)}
    return {"rows": len(rows), "unique_sample_ids": len(set(r["sample_id"] for r in rows)),
            "success": f"{len(ok)}/{len(rows)}", "per_model": per_model,
            "deepseek_r1_present": any("deepseek" in r["display"].lower() or "deepseek" in r["model"].lower() for r in rows)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--old-repo", required=True)
    ap.add_argument("--kaggle-fib")
    ap.add_argument("--kaggle-gen")
    a = ap.parse_args()
    print("JUNE_EVAL_RUN:", june_eval_run(a.old_repo))
    print("V68_METRICS:", v68_metrics(a.old_repo))
    print("TWO_PROP_PLAUSIBILITY(S1 651/750 vs S2strict 369/590):", two_prop_chi2(651, 750, 369, 590))
    print("DECOMPOSITION_CHECK:", decomposition_check())
    if a.kaggle_fib:
        print("FIB:", fib_descriptives(a.kaggle_fib))
    if a.kaggle_gen:
        print("GENERATION:", generation_descriptives(a.kaggle_gen))
