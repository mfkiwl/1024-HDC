## Priority: P1 · DATE 2027 · Mock Weak Reject 2/5 leftover

Tracker for an external mock review (Weak Reject, 2/5) of the DATE manuscript.
Not an official DATE form.

Manuscript figure/text bugs are closed in Research-paper `4533804`. Remaining score movement needs **new experiments**. Title and abstract stay frozen.

## Review scores (their scale: 3 = borderline, 4 = accept)

| Criterion | Their score | After `4533804` | Notes |
|---|---|---|---|
| Relevance | 4/5 | 4 | FPGA HW–algorithm fit. |
| Originality | 2/5 | 2 | Still bake-selected-bits into a narrower AM. |
| Soundness | 3/5 | 3–4 | Protocol + INA219 + energy wording fixed. |
| Evaluation | 2/5 | 2 | Antonio compact + native width still missing. |
| Clarity | 2/5 | 4 | Fig. 2 / Fig. 3(b) no longer contradict tables. |
| Overall | **2/5** | **2–3** | Consistency fixed; competitive baselines not. |

## Their six concerns

| # | Concern | Status | Issue |
|---|---|---|---|
| 1 | Missing Antonio identical-across-prototypes compact | Open | #39 |
| 2 | Sparse encoder; need native D=128/256 and stronger encoder in HW | Open | #40 (Python); #42 (PL, post-DATE) |
| 3 | Fig. 2 latency/energy/caption; Fig. 3(b) 89.0 vs 90.48 | **Done** in `4533804` | — |
| 4 | Energy overclaim; INA219 128-avg vs 100 Hz | **Done** in text; measurement campaign is post-DATE | #35 |
| 5 | Split / overlap / what transfers | **Done** in `4533804` | — |
| 6 | LUT breakdown, core cycles, batch vs single-window | Open | #41 |

## Children

- [ ] #39 Antonio compact (weekend Python)
- [ ] #40 Native D=128 / D=256 (weekend Python)
- [ ] #41 LUT hierarchy + cycles (from existing reports)
- [ ] #42 Stage-B in PL (not this week)

## Do not

- Change title or abstract.
- Invent native D=128 accuracy.
- Claim unmeasured narrow INA219 energy.
- Start a new energy campaign this week.

## Related

- Submit checklist: #38
- Claim checker: #37
- Epic: #20
