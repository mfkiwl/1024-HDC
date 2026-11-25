## Priority: P1 · Both · Mock WR concern 2 (native width)

Native encode-and-classify at **D=128** and **D=256**, not gathering 128 bits from a D=1024 query.

The DATE paper already reports D=256 encode-and-classify at **69.82%** spatial mean vs **72.65%** at K=128 gather (`docs/H1_narrow_datapath_design.md`). Native **D=128** is explicitly not in the manuscript. Do **not** invent it.

## Goal

Protocol HDC-2 Python sweep, RTL-style encoder (and Stage-B if cheap): D ∈ {128, 256, 1024} full-width vs K=128 Fisher-gather from D=1024.

## Requirements

- [ ] Same split, seed 42, CNT_W=6, S1–S5 spatial mean + pooled.
- [ ] Native D=128 and D=256: item memory and bind at that width (not a mask on D=1024).
- [ ] Report vs Option-E K=128 (bit-exact with masked 1024).
- [ ] Commit under `results/protocol_v2/native_d_sweep/`.
- [ ] If the D=256 number matches 69.82%, cite the artifact in the paper; if it differs, do not silently keep 69.8%.
- [ ] Add claims to `scripts/check_paper_numbers.py` (#37).
- [ ] Body-only paper row if it lands before SoftConf. Title/abstract frozen.

## Done when

- [ ] Native D=128 accuracy exists as a committed artifact, or the issue is waived as post-DATE.

## Do not

- Treat K=128 gather as native D=128.
- Synthesize a D=128 encoder bitstream unless the Python number is already in the PDF.

## Related

- Mock WR tracker; Antonio compact; Stage-B-in-PL.
