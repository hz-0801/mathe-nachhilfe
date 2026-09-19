# Auftrag: Projektarchiv ablegen, zwei Landkartenfehler korrigieren

Drei Sachen, ein Commit. Funde aus dem Projektarchiv Abitur-Prüfungssammlung.

## A Archivdatei

Im Repo-Ordner liegt `projekt-abitur-pruefungssammlung-2026-09-19.md`. Nach `archiv/`.

## B README.md, Zeile 53

Ersetzen:
`- \`abi-quellen.md\` – amtliche Dateien 2017/2018, Verlagsbände ab 2019, Heftordner \`hefte/abi/\` (lokal), Markdown-Korpus \`hefte-md/\` (lokal).`
durch
`- \`abi-quellen.md\` – amtliche Dateien 2011–2018 (44 Dateien, Serverpfade je Jahrgang), Verlagsbände ab 2019, Heftordner \`hefte/abi/\` (lokal), Markdown-Korpus \`hefte-md/\` (lokal).`

## C abitur/abi-quellen.md § 1

Nach dem Absatz „Verzeichnis der Dateien: https://…/abitur_bb/Zabi_Mathematik/" einen
zweiten Absatz einfügen:

```
Die zwölf gemeinsamen Hefte 2011–2013 liegen nicht dort, sondern je Jahr unter
https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/pruefungen/gemeinsames_Abitur_Be_BB/Abituraufgaben/Abituraufgaben_<Jahr>/
Die Regel „Verzeichnis aus § 1 + Serverdatei" gilt für diese zwölf Dateien mit dem
zweiten Verzeichnis. (Nachgetragen 19.09.2026, Fund des Projektarchivs
Abitur-Prüfungssammlung; der Pfad stammt aus dem Chat vom 07.09.2026 und ist nicht
erneut geprüft – bei Bedarf eine Datei probeweise holen.)
```

Vorher prüfen: Der alte README-Text kommt genau einmal vor; der Absatz „Verzeichnis der
Dateien" in abi-quellen.md § 1 ebenfalls. Sonst abbrechen und melden.

## D Abschluss

Diese Auftragsdatei nach `archiv/`. Commit: `Projektarchiv Abitur-Prüfungssammlung;
README und abi-quellen.md § 1 nachgezogen`. Push versuchen. Bericht: Commit-Hash und
„Push origin drücken", falls nötig.
