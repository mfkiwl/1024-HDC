## Priority: P1 · Both · Mock WR concern 1

Exact redundancy-compaction baseline from Antonio and Alvarez (ISCAS 2022): drop every coordinate that is **identical across all class prototypes**, then report accuracy (and hardware if a bitstream exists).

Prototype-disagreement *ranking* in the paper is **not** this baseline. The mock reviewer asked for the exact compact: those bits cannot change the nearest-prototype decision.

## Goal

A committed Python result under Protocol HDC-2: how many bits survive, spatial-mean / pooled accuracy vs unpruned, vs Fisher keep=128, vs support-restricted random.

Optional (only if it finishes before Sunday 20 Sep AoE): synth a compact AM at that width and quote LUT/latency. Do **not** invent silicon numbers.

## Requirements

- [ ] On TRAIN-built prototypes (RTL encoder, S1–S5, HDC-2), mark bits identical across all 5 prototypes.
- [ ] Keep the complement as the compact mask (no Fisher ranking).
- [ ] Report kept-bit count, accuracy, and overlap with Fisher-128 and with the live support (~209).
- [ ] Repeat on Stage-B prototypes (Python only) as a denser-AM control.
- [ ] Commit JSON/README under `results/protocol_v2/antonio_compact/`.
- [ ] If time: add one table row to Research-paper (body only; title/abstract frozen).
- [ ] Add the numbers to `scripts/check_paper_numbers.py` (#37).

## Done when

- [ ] Numbers are from a committed run, not estimated.
- [ ] Paper either cites the row or this issue is waived as post-DATE.

## Blocked by

- None for Python. Hardware synth blocked by weekend clock, not by code.

## Related

- Mock WR tracker; native D=128/256; Stage-B-in-PL.
- Cite: Antonio and Alvarez, “Redundancy Pruning for Binary HDC Architectures,” ISCAS 2022 (`antonio2022iscas`).
