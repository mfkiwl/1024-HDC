# DATE paper draft (IEEEtran)

## Build

From this directory:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or with `latexmk`:

```bash
latexmk -pdf main.tex
```

Figures are included from `../results/figures/` via `\graphicspath`.

## Draft order (recommended)

1. Fill **§Results** (numbers already stubbed from repo).
2. Expand **§Methodology** (protocol, energy, Hook A / Twist defs).
3. Add **architecture figure** (replace TODO box in `main.tex`).
4. Write **§Introduction** and **§Related Work** prose.
5. Tighten **§Limitations** with advisor feedback.
6. Write **abstract last** (keep IEEE rule: no math/symbols in abstract).

## Evidence map

| Section | Repo sources |
|---------|----------------|
| Verification | `results/phase3/board_emg_replay.txt`, cosim harnesses |
| Hook A | `results/hook_a/sweep_summary.csv`, `hookA_pareto_measured.png` |
| Energy | `results/phase3/energy_summary.txt` |
| Anchors | `results/phase3/anchors/anchor_*/board_emg_replay.txt` |
| Twist 1 | `results/twist1_keep0125/` |
| Twist 2 | `results/twist2/` |
| Encoder story | `docs/Baseline_vs_RTL_Encoder.md` |

## Title (locked)

**Informed Bit-Position Pruning for Streaming Hyperdimensional Computing on Zynq**

Subtitle: *A Verified Silicon Study of Accuracy, Energy, and Cross-Subject Mask Transfer*

Fix before submit: co-author email, funding acknowledgment, complete bibliography entries.
