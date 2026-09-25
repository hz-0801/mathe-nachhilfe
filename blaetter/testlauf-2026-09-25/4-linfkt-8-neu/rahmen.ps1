param([string]$name, [string]$ziel, [string]$stempel)
Set-Location $PSScriptRoot
$env:PATH = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64;" + $env:PATH
$env:PYTHONPATH = "C:\Users\holge\AppData\Local\Temp\claude\C--Users-holge-mathe-mathe-nachhilfe\c6924aab-9c6f-4c6b-96fc-d8fbcd8c8855\scratchpad\pylib"
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
if ($name -ne "loesungen") {
  & $py rahmen.py abhaken
  & $py rahmen.py inhalt $name | Out-Null
  xelatex -interaction=nonstopmode "$name.tex" | Out-Null
  pdftotext -layout -enc UTF-8 "$name.pdf" "$name.txt"
  "== Verzeichnis aus Lauf 1"
  & $py rahmen.py inhalt $name "$name.txt"
}
xelatex -interaction=nonstopmode "$name.tex" | Out-Null
xelatex -interaction=nonstopmode "$name.tex" | Out-Null
pdftotext -layout -enc UTF-8 "$name.pdf" "$name.txt"
"== Log"
Select-String -Path "$name.log" -Pattern "^!|mathblatt Warning|Overfull|Undefined|Rerun" | ForEach-Object { $_.Line }
pdfinfo "$name.pdf" | Select-String "Pages"
Get-ChildItem "$name-*.png" -ErrorAction SilentlyContinue | Remove-Item
pdftoppm -png -r 60 "$name.pdf" $name
if ($name -ne "loesungen") {
  "== Kontrolle Verzeichnis gegen Endkompilat"
  Copy-Item "inhalt_$name.tex" "inhalt_$name.alt"
  & $py rahmen.py inhalt $name "$name.txt" | Out-Null
  if ((Get-Content "inhalt_$name.tex" -Raw) -eq (Get-Content "inhalt_$name.alt" -Raw)) { "Verzeichnis stimmt mit Endkompilat" } else { "VERZEICHNIS WEICHT AB" }
  Remove-Item "inhalt_$name.alt"
  & $py -c "import pypdf; r=pypdf.PdfReader('$name.pdf'); p=r.pages[0]; ids={id(pg.indirect_reference):i for i,pg in enumerate(r.pages)}; nd=r.named_destinations; [print('Link', a.get_object().get('/Dest') or a.get_object().get('/A',{}).get('/D'), '-> Seite', r.get_destination_page_number(nd[str(a.get_object()['/A']['/D'])])+1 if '/A' in a.get_object() else '?') for a in p.get('/Annots',[])]"
}
$txt = Get-Content "$name.txt" -Raw -Encoding UTF8
$seiten = $txt -split "`f"; $i = 0
foreach ($s in $seiten) { $i++; if ($s.Trim().Length -gt 0) { $nrs = ([regex]::Matches($s, "(?m)^\s*(\d+)\.\s+Ich")) | ForEach-Object { $_.Groups[1].Value }; "Seite $i : $($s.Length) Zeichen, Nummern: $($nrs -join ',')" } }
Copy-Item "$name.pdf" $ziel -Force
Add-Content -Encoding ascii zeiten.txt ("$stempel " + [DateTimeOffset]::UtcNow.ToUnixTimeSeconds())
