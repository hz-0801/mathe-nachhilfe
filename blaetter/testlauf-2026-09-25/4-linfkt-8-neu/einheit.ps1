param([string]$e, [string]$stempel = "")
Set-Location $PSScriptRoot
$env:PATH = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64;" + $env:PATH
$env:PYTHONPATH = "C:\Users\holge\AppData\Local\Temp\claude\C--Users-holge-mathe-mathe-nachhilfe\c6924aab-9c6f-4c6b-96fc-d8fbcd8c8855\scratchpad\pylib"
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
"== pruef $e"
& $py pruef.py $e | Select-Object -Last 3
Get-Content "pruef_out_$e.txt" | Select-String "ABWEICHUNG" | ForEach-Object { $_.Line }
"== xelatex"
$job = "probe_$e"
xelatex -interaction=nonstopmode "-jobname=$job" "\def\einheit{$e}\input{probe}" | Out-Null
Select-String -Path "$job.log" -Pattern "^!|mathblatt Warning|Overfull|Undefined" | ForEach-Object { $_.Line }
pdfinfo "$job.pdf" | Select-String "Pages"
Get-ChildItem "$job-*.png" -ErrorAction SilentlyContinue | Remove-Item
pdftoppm -png -r 60 "$job.pdf" $job
pdftotext -layout -enc UTF-8 "$job.pdf" "$job.txt"
$txt = Get-Content "$job.txt" -Raw -Encoding UTF8
$seiten = $txt -split "`f"
$i = 0
foreach ($s in $seiten) { $i++; if ($s.Trim().Length -gt 0) { $nrs = ([regex]::Matches($s, "(?m)^\s*(\d+)\.\s+Ich")) | ForEach-Object { $_.Groups[1].Value }; "Seite $i : $($s.Length) Zeichen, Nummern: $($nrs -join ',')" } }
if ($stempel -ne "") { Add-Content -Encoding ascii zeiten.txt ("$stempel " + [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()) }
