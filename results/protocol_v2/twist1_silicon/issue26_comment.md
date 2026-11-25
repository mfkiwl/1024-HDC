**Python silicon prediction complete** (export-ref calibrated on seed 0 Δ0.00 pp).

493,512 windows, pooled random @ keep=0.125, seeds 0–9:
- **Predicted gap (informed − random): +7.44 ± 2.59 pp** (mean acc 65.40% ± 2.59)
- Seed 0 **board measured**: 62.51% (+10.33 pp) ✅
- Seeds 1–9: predicted only (board replay pending)

Artifacts: `results/protocol_v2/twist1_silicon/seed_summary.json`

Board: `bash scripts/run_silicon_random_seeds.sh --board --seeds 1-9 --resume`
