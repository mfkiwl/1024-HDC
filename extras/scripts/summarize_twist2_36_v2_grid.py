#!/usr/bin/env python3
"""Aggregate Twist 2 HDC-2 36-subject keep-grid results (issue #2)."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = REPO / "results" / "protocol_v2" / "twist2_36_v2"


def load_point(keep_dir: Path) -> dict | None:
    path = keep_dir / "twist2_results.json"
    if not path.is_file():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    meta = payload["meta"]
    result = payload["result"]
    gap = result["mean_gap_local_minus_pooled_pp"]
    return {
        "keep_bits": result["n_keep"],
        "keep_ratio": result["keep_ratio"],
        "mean_unpruned_pct": 100.0 * result["mean_unpruned_accuracy"],
        "mean_local_pct": 100.0 * result["mean_local_oracle_accuracy"],
        "mean_pooled_pct": 100.0 * result["mean_pooled_transfer_accuracy"],
        "mean_random_pct": 100.0 * result.get("mean_random_accuracy", float("nan")),
        "gap_local_minus_pooled_pp": gap,
        "gap_pooled_minus_random_pp": result.get(
            "mean_gap_pooled_minus_random_pp", float("nan")
        ),
        "mean_jaccard": result.get("mean_jaccard_pooled_vs_local", float("nan")),
        "generalises": abs(gap) <= float(meta.get("target_gap_pp", 3.0)),
        "elapsed_s": meta.get("elapsed_s"),
        "protocol": meta.get("protocol"),
        "path": str(keep_dir),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    p.add_argument(
        "--out-csv",
        type=Path,
        default=None,
        help="Default: <root>/grid_summary.csv",
    )
    p.add_argument(
        "--out-md",
        type=Path,
        default=None,
        help="Default: <root>/README.md",
    )
    args = p.parse_args()
    root = args.root.resolve()
    out_csv = (args.out_csv or root / "grid_summary.csv").resolve()
    out_md = (args.out_md or root / "README.md").resolve()

    rows = []
    for keep_dir in sorted(root.glob("keep_*")):
        row = load_point(keep_dir)
        if row:
            rows.append(row)
    rows.sort(key=lambda r: r["keep_bits"])

    if not rows:
        print(f"No keep_* results under {root}")
        return 1

    fields = list(rows[0].keys())
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    lines = [
        "# Twist 2 — 36-subject HDC-2 keep-ratio stress grid (issue #2)",
        "",
        "Train S1–18 TRAIN → eval S19–36 TEST. Masks: Local oracle / Pooled Fisher / Random.",
        "",
        "| Keep bits | Unpruned | Local | Pooled | Random | Gap L−P (pp) | Gap P−R (pp) | Jaccard | Generalises |",
        "|-----------|----------|-------|--------|--------|--------------|--------------|---------|-------------|",
    ]
    for r in rows:
        lines.append(
            f"| {r['keep_bits']} | {r['mean_unpruned_pct']:.2f}% | "
            f"{r['mean_local_pct']:.2f}% | {r['mean_pooled_pct']:.2f}% | "
            f"{r['mean_random_pct']:.2f}% | {r['gap_local_minus_pooled_pp']:+.2f} | "
            f"{r['gap_pooled_minus_random_pp']:+.2f} | {r['mean_jaccard']:.3f} | "
            f"{'YES' if r['generalises'] else 'NO'} |"
        )
    lines.extend(
        [
            "",
            f"CSV: `{out_csv.relative_to(REPO)}`",
            "",
            "Regenerate: `bash scripts/run_twist2_36_v2_keep_grid.sh`",
            "",
        ]
    )
    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_csv}")
    print(f"Wrote {out_md}")
    for r in rows:
        print(
            f"  keep={r['keep_bits']:3d}: L={r['mean_local_pct']:.2f}% "
            f"P={r['mean_pooled_pct']:.2f}% R={r['mean_random_pct']:.2f}% "
            f"gapLP={r['gap_local_minus_pooled_pp']:+.2f} "
            f"J={r['mean_jaccard']:.3f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
