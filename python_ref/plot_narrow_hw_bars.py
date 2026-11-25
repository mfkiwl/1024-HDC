#!/usr/bin/env python3
"""Two-panel LUT / latency bars for the DATE narrow-AM figure.

Numbers match tab:narrow (integrated LUT, 200-window scatter-gather mean).
Energy is intentionally omitted: narrow INA219 was not measured.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parents[1]
OUT_DIRS = [
    REPO / "results" / "figures",
    Path(r"C:\Modelsim_projects\Research-paper\figures"),
]

# tab:narrow
LUT_FULL, LUT_NARROW = 35206, 10601
US_FULL, US_NARROW = 4.63, 2.78


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "DejaVu Serif", "serif"],
            "font.size": 8,
            "axes.labelsize": 8,
            "xtick.labelsize": 7,
            "ytick.labelsize": 7,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.linewidth": 0.8,
        }
    )
    fig, axes = plt.subplots(1, 2, figsize=(3.5, 1.55))
    colors = ("#2166ac", "#d95f02")
    labels = ("Full-width", r"$K{=}128$")

    ax = axes[0]
    bars = ax.bar(labels, [LUT_FULL, LUT_NARROW], color=colors, width=0.62)
    ax.set_ylabel("Integrated LUT")
    ax.set_ylim(0, 42000)
    for b, v in zip(bars, (LUT_FULL, LUT_NARROW)):
        ax.text(b.get_x() + b.get_width() / 2, v + 600, f"{v:,}", ha="center", va="bottom", fontsize=7)

    ax = axes[1]
    bars = ax.bar(labels, [US_FULL, US_NARROW], color=colors, width=0.62)
    ax.set_ylabel(r"Batch latency ($\mu$s/w)")
    ax.set_ylim(0, 6.2)
    for b, v in zip(bars, (US_FULL, US_NARROW)):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.12, f"{v:.2f}", ha="center", va="bottom", fontsize=7)

    fig.tight_layout(w_pad=1.2)
    for out_dir in OUT_DIRS:
        out_dir.mkdir(parents=True, exist_ok=True)
        for ext in ("pdf", "png"):
            dest = out_dir / f"narrow_vs_baseline_pareto.{ext}"
            fig.savefig(dest, dpi=300, bbox_inches="tight", pad_inches=0.03)
            print(dest)
    plt.close(fig)


if __name__ == "__main__":
    main()
