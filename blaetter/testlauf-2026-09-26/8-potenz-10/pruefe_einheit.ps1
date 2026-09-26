param([string]$e, [string]$render = "", [string]$stempel = "")
Set-Location $PSScriptRoot
$env:PATH = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64;" + $env:PATH
$env:PYTHONPATH = "C:\Users\holge\AppData\Local\Temp\claude\C--Users-holge-mathe-mathe-nachhilfe\45e0e91d-0488-42ce-92c5-21c7c65e3c84\scratchpad\pylib"
"== pruef.py $e"
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" pruef.py $e | Where-Object { $_ -match "ABWEICHUNG|Abweichungen|Error|Traceback" }
xelatex -interaction=nonstopmode "-jobname=probe_${e}_a" "\def\probedatei{${e}_a}\input{probe_a}" | Out-Null
xelatex -interaction=nonstopmode "-jobname=probe_${e}_l" "\def\probedatei{${e}_l}\input{probe_l}" | Out-Null
foreach ($j in "probe_${e}_a", "probe_${e}_l") {
  "== $j"
  Select-String -Path "$j.log" -Pattern "^!|mathblatt Warning|Overfull|Undefined control" -Context 0,1 | ForEach-Object { $_.Line; $_.Context.PostContext }
  pdfinfo "$j.pdf" | Select-String Pages
}
pdftotext -layout -enc UTF-8 "probe_${e}_a.pdf" "probe_${e}_a.txt"
pdftotext -layout -enc UTF-8 "probe_${e}_l.pdf" "probe_${e}_l.txt"
# Seiten mit Hauptnummern je Seite
$seiten = (Get-Content -Raw -Encoding UTF8 "probe_${e}_a.txt") -split "`f"
for ($i = 0; $i -lt $seiten.Count; $i++) {
  $nrs = [regex]::Matches($seiten[$i], "(?m)^\s*(\d{1,2})\. Ich") | ForEach-Object { $_.Groups[1].Value }
  $len = ($seiten[$i] -replace "\s", "").Length
  if ($len -gt 0) { "Seite $($i+1): Nr. $($nrs -join ', ') · Zeichen $len" }
}
if ($render -ne "") {
  Remove-Item "render_${e}_p*.png" -ErrorAction SilentlyContinue
  foreach ($p in $render.Split(",")) { pdftoppm -png -r 60 -f $p -l $p "probe_${e}_a.pdf" "render_${e}_p$p" }
  Get-ChildItem "render_${e}_p*.png" | ForEach-Object { $_.Name }
}
if ($stempel -ne "") { Add-Content -Encoding ascii zeiten.txt ("$stempel " + [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()); "Stempel: $stempel" }
