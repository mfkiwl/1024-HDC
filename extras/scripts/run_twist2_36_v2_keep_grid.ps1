# Twist 2 @ 36 UCI subjects under Protocol HDC-2 - keep-ratio stress grid (issue #2).
# Encodes subjects ONCE, then evaluates all keep ratios.
#
# Usage (from repo root):
#   .\scripts\run_twist2_36_v2_keep_grid.ps1
#   .\scripts\run_twist2_36_v2_keep_grid.ps1 -Quick
#   .\scripts\run_twist2_36_v2_keep_grid.ps1 -KeepBits "32,64,128"
#
param(
    [switch]$Quick,
    [string]$KeepBits = "32,64,96,128,192,256"
)

$ErrorActionPreference = "Stop"
$Repo = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Repo
$Cfg = Join-Path $Repo "python_ref\config\twist2_36_v2_sweep.json"
$EmgCfg = Join-Path $Repo "python_ref\config\emg_baseline_v2.json"
$OutRoot = Join-Path $Repo "results\protocol_v2\twist2_36_v2"
$Dataset = Join-Path $Repo "python_ref\HDC-EMG\dataset_36.mat"
$Summarize = Join-Path $Repo "scripts\summarize_twist2_36_v2_grid.py"

if (-not (Test-Path $Dataset)) {
    throw "Missing $Dataset - run: python scripts/build_uci_emg_dataset.py"
}

New-Item -ItemType Directory -Force -Path $OutRoot | Out-Null
$env:PYTHONIOENCODING = "utf-8"

Write-Host "=== Twist 2 36-subj HDC-2 keep-bits=$KeepBits (encode once) ==="
$pyArgs = @(
    "python_ref\run_twist2_sweep.py",
    "--config", $Cfg,
    "--emg-config", $EmgCfg,
    "--keep-bits", $KeepBits,
    "--out-dir", $OutRoot
)
if ($Quick) { $pyArgs += "--quick" }
$log = Join-Path $OutRoot "full_grid.log"
& python @pyArgs 2>&1 | Tee-Object -FilePath $log

Write-Host "Grid complete under $OutRoot"
& python $Summarize --root $OutRoot
