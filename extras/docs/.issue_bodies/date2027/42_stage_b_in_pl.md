## Priority: P2 · Paper 1 · Mock WR concern 2 (hardware) · **not this week**

Put the stronger Stage-B BSC encoder (~90% spatial mean) in the PL, then repeat iso-density + narrow AM on that datapath.

Python Stage-B already exists (#21, #22): iso-density +2.82 pp at keep=0.125 (below the 5 pp target); rankings separate (MI 92.77% vs Fisher 90.48%). The mock reviewer asked whether the hardware benefit remains on a **competitive** encoder. That is a new bitstream, not a caption.

## Goal (post-DATE / journal)

RTL (or HLS) Stage-B bind records on Zynq-7020, bit-exact with the Python Stage-B golden model, then:

- Board accuracy vs ~90% export (0.5 pp gate).
- Iso-density informed vs random at K=128 on silicon.
- Optional: bake Stage-B Fisher bits into a narrow AM and quote LUT/latency.

## Requirements

- [ ] Encoder RTL matching Stage-B BSC (not the 20-bind `level21_to_grid` path).
- [ ] Co-sim vs Python Stage-B golden.
- [ ] Board replay on HDC-2 S1–S5.
- [ ] Do **not** mix RTL ~73% and Stage-B ~90% in one table without the encoder column.

## Done when

- [ ] Not required for DATE 2027 (20 Sep AoE). Track for a revision or journal.

## Blocked by

- DATE submit (#38). Encoder rewrite is larger than the weekend.

## Related

- Mock WR tracker; native D=128 (#41); #21 / #22 (Python done); #34 real per-feature encoder.
