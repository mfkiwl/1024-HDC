# Paper outline — section checklist

Target: DATE 2027 (~6 pages IEEE two-column + references).

## §I Introduction [TODO expand prose]

- [x] Contribution bullets (in main.tex)
- [ ] Motivation paragraph (edge EMG, HDC, gap in bit-position pruning)
- [ ] Paper organization sentence

## §II Background and Related Work [TODO]

- [ ] HDC primitives (bind, permute, bundle, AM)
- [ ] Rahimi FPGA-HDC EMG
- [ ] Pruning: dimension reduction vs Fisher bit selection
- [ ] Position vs MLP baseline (different deployment class)

## §III Architecture [TODO figure]

- [x] Utilization numbers
- [ ] Block diagram (PS + AXI-Lite + DMA + encoder + pruning_mask + AM)
- [ ] Streaming batch path (200-window SG)

## §IV Methodology [partial]

- [x] P-may2026, two-encoder story (stub)
- [x] Energy measurement summary
- [x] Hook A / Twist 1 / Twist 2 definitions
- [ ] Fisher mask construction equation
- [ ] Cosim harness table (optional, appendix)

## §V Results [mostly stubbed]

- [x] Table: baselines
- [x] Hook A Pareto figure
- [x] Fisher heatmap figure
- [x] Twist 1 figure (keep=0.125)
- [x] Twist 2 figure
- [ ] Optional: baselines_bar.png in text
- [ ] Silicon anchor accuracy table (A/B/C)

## §VI Discussion and Limitations [stub]

- [x] Static-dominated energy
- [x] 74 vs 90 encoder
- [x] Five subjects
- [ ] Fisher pooled (silicon) vs per-subject (Hook A Python)

## §VII Conclusion [stub]

- [x] One paragraph skeleton

## Back matter

- [ ] Acknowledgment (funding, HDC-EMG credit)
- [ ] refs.bib complete (Rahimi, Kanerva, FPGA-HDC pruning papers)
- [ ] Remove any template boilerplate
- [ ] Page limit check
