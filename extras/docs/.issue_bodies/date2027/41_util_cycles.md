## Priority: P1 · Paper 1 · Mock WR concern 6

Resource breakdown and timing so the 7.5× core LUT drop (28,600 → 3,794 OOC) is explainable.

The mock reviewer asked for:

- LUT/FF split: encoder vs associative memory vs DMA / supporting logic, both bitstreams.
- Core cycle counts (not only 200-window amortized µs).
- Integrated post-route timing for full-width and K=128.
- Distinguish batch 4.63 / 2.78 µs/window from single-window response (paper already has 58 µs lone scatter-gather and 3 µs AXI4-Lite poll).

## Goal

A table from **existing** Vivado reports and RTL, not a new place-and-route campaign unless the reports are missing.

## Requirements

- [ ] Locate OOC and integrated util reports for `hdc_core_top` and `hdc_core_top_narrow`.
- [ ] Hierarchical LUT/FF: encoder, popcount AM, AXI DMA, leftover.
- [ ] Cycles per window in PL (encode + score) at 100 MHz for both widths.
- [ ] Post-route WNS/WHS already quoted for full-width (+0.78 ns / +0.26 ns); add the narrow bitstream if the report exists.
- [ ] One body table or a short paragraph in Research-paper. Title/abstract frozen.
- [ ] Feed numbers into #37.

## Done when

- [ ] Breakdown is in the PDF, or this is waived because reports are not recoverable before Sunday.

## Related

- Mock WR tracker; #32 Pareto/util script; #31 board eval (closed).
- Do not use this issue to add a fake energy panel (#35).
