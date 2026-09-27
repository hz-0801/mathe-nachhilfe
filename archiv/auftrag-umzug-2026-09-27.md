# Auftrag: Umzug 2026-09-27 – Übergabe ablegen

Modell: Sonnet. Ordner: mathe-nachhilfe. Kurz, eine Sitzung.
Voraussetzung: Der Testlauf (auftrag-testlauf.md) ist beendet –
die Datei liegt unter archiv/ und bericht-testlauf-<datum>.md in
der Wurzel. Läuft er noch, brich ab und melde es.

## Schritte

1. Datei uebergabe.md (Datei 1 dieses Blocks) liegt in der
   Wurzel. Die vorhandene uebergabe.md ist vor dem Anlegen nach
   archiv/uebergabe-2026-09-26.md zu verschieben (git mv); trifft
   der Name dort auf eine Datei, „b" anhängen. Falls die neue
   Datei schon über die alte geschrieben wurde: alte Fassung aus
   git (`git show HEAD:uebergabe.md`) nach archiv/ schreiben.
2. faellig.md § 2, neue Posten (Fundstelle uebergabe.md § 5):
   Zusammenbau-Skript Bank → Blatt (Prüfstein prozentrechnung);
   Katalogauftrag aus den Urteilen 26.09. (Liste in § 4 der
   Übergabe); Nachbesserung Bank-Prüfsteine gegen bank-pruef v0.2;
   Lückenlauf Lehrwerke gegen Einheiten; Aufräumen Wurzel und
   Belege; ziel.md auf die Linie Bank nachziehen; Bank-Einträge
   potenz und daten nach dem Katalogauftrag; e2/e3 von
   quadratische-gleichungen in der Bank umbenennen.
3. README.md: Absatz zu uebergabe.md auf Stand 2026-09-27; in
   der Landkarte einen Satz, dass hz-0801/aufgabenbank die
   Aufgabenbank hält (Verweis auf bank.md dort).
4. Diesen Auftrag nach archiv/auftrag-umzug-2026-09-27.md
   verschieben.
5. Commit „umzug: Übergabe 2026-09-27, Posten Bank" (commit -F,
   UTF-8, ohne BOM, LF). Kein Push.

## Regeln

PowerShell: WriteAllText mit UTF8Encoding($false); git.exe von
GitHub Desktop mit -c core.pager=cat; nichts löschen.

## Bericht

Erste Zeile das Modell; je Schritt eine Zeile; letzte Zeile
„Push origin drücken".
