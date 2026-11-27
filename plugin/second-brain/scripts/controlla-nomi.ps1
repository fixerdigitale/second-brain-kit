# Lancia controlla_nomi.py con Python 3 su Windows (PowerShell).
# Se Windows blocca gli script, la persona sceglie se lanciarlo cosi', solo per questa volta:
#   powershell -ExecutionPolicy Bypass -File "controlla-nomi.ps1" [argomenti]
# Bypass vale solo per quel processo. Non usare mai Set-ExecutionPolicy.
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$script = Join-Path $dir "controlla_nomi.py"
foreach ($py in @("py", "python3", "python")) {
  $cmd = Get-Command $py -ErrorAction SilentlyContinue
  if (-not $cmd) { continue }
  if ($cmd.Source -like "*WindowsApps*") { continue }  # alias del Microsoft Store, non e' Python
  if ($py -eq "py") { & py -3 $script @args } else { & $py $script @args }
  exit $LASTEXITCODE
}
Write-Error "Python 3 non trovato / Python 3 not found."
exit 3
