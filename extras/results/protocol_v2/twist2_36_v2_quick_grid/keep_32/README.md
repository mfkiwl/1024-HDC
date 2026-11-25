# Twist 2 — cross-subject Fisher mask transfer

Generated: 2026-07-21T06:03:10Z
Train subjects: [1, 2]  ·  Test subjects: [19, 20]
Config: D=1024, CNT_W=6, keep=0.03125 (32 bits)
Pooled TRAIN windows (mask source): 4000
Random seeds: 2 (seed0=0)

## Headline (held-out test subjects, mean)

| Condition | Spatial mean accuracy |
|-----------|----------------------|
| Unpruned | **76.40%** |
| Local oracle (own-subject mask) | **76.40%** |
| Pooled transfer (train-subject mask) | **76.40%** |
| Random (iso-density mean) | **76.40%** |
| **Gap (local − pooled)** | **+0.00 pp** |
| **Gap (pooled − random)** | **+0.00 pp** |
| Mean Jaccard(pooled, local) | **0.455** |

Target |gap| <= 3 pp: **GENERALISES**

## Per held-out subject

| Subject | Local | Pooled | Random | Gap L-P (pp) | Gap P-R (pp) | Jaccard | Unpruned |
|---------|-------|--------|--------|--------------|--------------|---------|----------|
| S19 | 85.60% | 85.60% | 85.60% | +0.00 | +0.00 | 0.488 | 85.60% |
| S20 | 67.20% | 67.20% | 67.20% | +0.00 | +0.00 | 0.422 | 67.20% |

## Regenerate

```bash
python3 python_ref/run_twist2_sweep.py --quick
python3 python_ref/run_twist2_sweep.py
bash scripts/run_twist2_36_v2_keep_grid.sh
```
