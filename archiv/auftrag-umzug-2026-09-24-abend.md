# Auftrag: Umzug 2026-09-24 (abends)

Ordner mathe-nachhilfe. Modell Sonnet.

Regeln: PowerShell (kein Heredoc, kein sed); git über die
git.exe von GitHub Desktop, -c core.pager=cat, commit -m, nicht
pushen. Nichts löschen. Keine Rückfragen.

1. Die bisherige uebergabe.md liegt schon überschrieben vor
   (Datei 1). Ihren alten Inhalt aus git holen:
   git -c core.pager=cat show HEAD:uebergabe.md und nach
   archiv/uebergabe-2026-09-24-vormittag.md schreiben (die alte
   Datei trug den Stand 25.09., war aber am 24.09. vormittags
   geschrieben).
2. befund-schwach-blatt-2026-09-24.md (Datei 3) liegt in der
   Wurzel. README.md, Abschnitt „Wo fange ich an": einen Satz
   dazu nach dem Muster der anderen Befunddateien; uebergabe.md
   ist dort schon genannt.
3. faellig.md: zwei Posten anhängen, Form wie die vorhandenen:
   - „Nach der Stunde ein Satz (Thema, wo der Schüler hing,
     was half) – Auslöser: erstes Blatt mit v4.3 am Tisch; liegt
     beim Lehrer; der Chat stellt die Frage dann wieder."
   - „\streifenfeld in mathblatt.sty aufnehmen – Auslöser: Umbau
     v4.3; Auftrag an blattbau; Quelle: blaetter/prozentrechnung/
     2026-09-24/src/fokus_a.tex, Vorspann."
4. Diesen Auftrag nach archiv/auftrag-umzug-2026-09-24-abend.md
   verschieben (git mv).
5. git status prüfen: uebergabe.md, archiv/ (zwei Dateien),
   befund-schwach-blatt-2026-09-24.md, README.md, faellig.md.
   Nichts unter hefte/.
6. Commit: „umzug: Übergabe 2026-09-24 abends, Befund
   schwach-Blatt".
7. Bericht: Modell, Liste der Dateien, letzte Zeile „Push origin
   drücken".
