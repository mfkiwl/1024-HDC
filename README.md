# 1024-HDC

Streaming **1024-bit Hyperdimensional Computing (HDC)** on Xilinx Zynq-7020 (ZedBoard), with **bit-position pruning** for EMG hand-gesture classification.

**Platform:** `xc7z020clg484-1` @ 100 MHz · Vivado 2024.2 · [GitHub](https://github.com/harsha240yeager/1024-HDC)

---

## Idea

FPGA HDC work usually trades accuracy by changing hypervector dimension \(D\). This project asks a different question:

> At a **fixed number of kept bits**, does *which* bit positions you keep matter?

We implement a streaming HDC core (bind → permute → bundle → masked Hamming search), verify it bit-exact against a Python golden model, then study **Fisher-informed** pruning masks versus **random** masks at the same density on silicon.

| Path | Role |
|------|------|
| [`rtl/`](rtl/) | SystemVerilog HDC datapath + `pruning_mask` |
| [`python_ref/`](python_ref/) | Golden model and pruning sweeps |
| [`results/protocol_v2/`](results/protocol_v2/) | Current (Protocol HDC-2) results |
| [`results/figures/`](results/figures/) | Paper figures |
| [`extras/`](extras/) | Legacy experiments, plans, briefings, scratch |

---

## Results

Protocol **HDC-2** (disjoint train/test; cite these numbers):

| Result | Value |
|--------|-------|
| Silicon accuracy | **72.78%** over **493,512** test windows |
| Bit-exact vs golden | **Δ 0.00%** (every label matched) |
| Throughput / latency | **~216k win/s** · **4.63 µs**/window (PL DMA batch) |
| Resources | **35.2k LUT**, **0 DSP**, **0 BRAM** |
| Energy (INA219 @ J21) | PL **11.98 µJ**/w vs ARM **2088 µJ**/w (~175×) |
| Pruning (Hook A) | Accuracy **flat** from 0% → **87.5%** prune |
| Informed vs random (Twist 1) | Fisher beats random by **+6.90 pp** at 128 bits (Python, 30 seeds); **+10.33 pp** on silicon (seed 0) |
| Cross-subject mask (Twist 2) | Pooled mask transfers with **+1.02 pp** gap (S1–3 → S4–5) |

Evidence: [`results/protocol_v2/`](results/protocol_v2/) · board logs in [`results/phase3/`](results/phase3/) · figures in [`results/figures/`](results/figures/).

**Note:** ~73% is the **deployed RTL encoder**. A different Python encoding reaches ~90% (Rahimi-class spatial). This repo’s claim is systems + pruning, not accuracy SOTA. Reproduce: [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

---

## Conclusion

1. A streaming 1024-bit HDC classifier can be **bit-exact on Zynq** and ~175× faster / lower energy than ARM software HDC on the same board.
2. **Bit position matters:** informed masks keep accuracy under aggressive pruning where random iso-density masks fail.
3. A pooled Fisher mask can **transfer across subjects** with small loss.
4. Runtime masks alone do not shrink LUTs; **compile-time / narrower keep-sets** are what buy hardware — the research value is *which bits* to keep.

Legacy experiments, DATE planning docs, presentation decks, and one-off scripts live under [`extras/`](extras/) so the main tree stays focused on the idea, results, and conclusion above.

---

## Layout

```
rtl/  tb/  sim/     hardware + co-sim
python_ref/         golden model
sw/  board/         bare-metal + Vivado project
scripts/            reproduce / export / energy helpers
results/            protocol_v2 + figures + phase3 + dsweep
docs/               reproducibility + energy methodology
paper/              manuscript skeleton
extras/             everything else (archived)
```
