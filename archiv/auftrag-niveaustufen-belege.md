# Auftrag: Belege für Niveaustufe (Sek I) und Kursart (Sek II)

Modell: Opus (Lesarten offen, Zitate aus Prosa).

## Ausgangslage

Der Unterrichtsblatt-Prompt soll ab v4.3 vor dem Bau fragen, wenn
der Katalogeintrag eine Spanne trägt, die die Eingabe nicht
auflöst – in der Sekundarstufe I die Niveaustufe des Rahmenlehr-
plans (Oberschule/Gesamtschule bis F, in Teilen G; Gymnasium G
und H), in der Sekundarstufe II die Kursart (Grundkurs oder
Leistungskurs). Dafür müsste je Lerneinheit und je Sprosse eine
Marke im Eintrag stehen. Ob der Katalog das hergibt, ist die
Frage dieses Auftrags. Du änderst keinen Eintrag: Du schreibst
zwei Vorschlagsdateien, aus denen der Lehrer die Marken
entscheidet – nach dem Muster von katalog/_blatt0-belege.md
(die Datei schlägt vor, sie entscheidet nicht).

Quellen im Repo:
- quellen/quelle-rlp-teil-c-mathematik-2023.txt – der Rahmenlehr-
  plan 1–10, Teil C Mathematik. Die Zuordnung Bildungsgang →
  Niveaustufe steht auf S. 13–14 der Quelle (Zeilen um 580–605
  des Texts): Integrierte Sekundarschule grundlegendes Niveau
  7–8 D–E in Teilen F, 9–10 F in Teilen G; erweitertes Niveau
  7–8 E in Teilen F, 9–10 F–G; Gymnasium 7 E, 8 F, 9 G, 10 H.
  Die Standards stehen in Kapitel 3 als Tabellen je Leitidee:
  am linken Rand der Zeile der Buchstabe der Niveaustufe A–H, in
  den Spalten die Standards in Worten. Die Inhalte je Themen-
  bereich folgen als Listen mit Niveaustufenangabe.
- quellen/quelle-lisum-planungshilfen-7bis10.txt – die LISUM-
  Planungshilfen: je Thema Unterrichtsreihen, teils getrennt
  nach EBR/FOR und GYM, teils mit dem Hinweis „Differenzierung
  zwischen EBR-, FOR- und GYM-Klassen über Tiefgründigkeit".
- katalog/<sek-i-eintrag>.md – 29 Sek-I-Einträge (Liste in
  katalog/index.md, Tabelle Sek I). Abschnitte: Verortung (dort
  stehen schon [RLP]-Zitate mit Niveaustufe, etwa „Zuordnungen
  und Funktionen G (S. 61)"), Lerneinheiten, Typen je Lern-
  einheit, Für schwache Schüler (dort „Mindeststoff (D/E)" und
  „Sprossen je Verfahrenstyp"), Prüfungsform (P10).
- katalog/<sek-ii-eintrag>.md – 44 Sek-II-Einträge (Tabelle
  Sek II in katalog/index.md). Abschnitt „Prüfungsform (fhr /
  abi / iqb)" mit Geltung je Zielprüfung; Verortung mit [GOST]-
  Zitaten, die Grund- und Leistungskurs trennen.
- abitur/abi-be-gk-geltung.md, abi-be-lk-geltung.md,
  abi-bb-gk-geltung.md, abi-bb-ea-geltung.md – je Zielprüfung
  Thema ja/nein.
- quellen/quelle-rlp-gost-be-2022-mathematik.txt und
  quelle-rlp-gost-bb-2022-mathematik.txt – Rahmenlehrpläne der
  gymnasialen Oberstufe; Leistungskursinhalte sind dort als
  Zusatz zum Grundkurs gekennzeichnet.

## Schritte

1. Lies katalog/_blatt0-belege.md Kopf und Abschnitt 1 als
   Formmuster, katalog/_quellen.md Zeile 23 ([RLP]) und die
   Bildungsgang-Tabelle des RLP-Texts.
2. Schreibe katalog/_niveaustufen-belege.md. Kopf: Titel, Stand
   (Datum, Commit des Katalogs), Quellen, Lesart. Dann je Sek-I-
   Eintrag ein Abschnitt „### <datei> – Stufe <Stufe aus
   index.md>" mit:
   a) Verortung: jede [RLP]-Klammer des Eintrags, die eine
      Niveaustufe nennt, wortgleich, mit Zeilennummer.
   b) Je Lerneinheit (Nummer und Titel aus dem Abschnitt
      Lerneinheiten): die Niveaustufe, die der RLP-Text für den
      Inhalt der Einheit hergibt – mit Fundstelle (Zeilennummer
      des Texts, Leitidee, Tabellenzeile oder Inhaltsliste) und
      dem Standard wortgleich, höchstens zwei Zeilen Zitat.
      Gibt der Text keine Stelle her: „keine Stelle". Passt der
      Inhalt zu mehreren Stufen (etwa Grundfall F, Sonderfall
      G): beide nennen, je mit Zitat.
   c) Je Sprosse aus „Sprossen je Verfahrenstyp" (Abschnitt Für
      schwache Schüler): die Niveaustufe wie in b, kürzer –
      „Sprosse n · <Wortlaut gekürzt> → F [Zeile 1974]" oder
      „→ keine Stelle". Wo der Eintrag die Sprosse schon als
      F-Stoff, Vorrat, D/E-Mindeststoff oder mit einer
      Niveaustufe markiert, nenne das daneben („Eintrag: Vorrat").
   d) LISUM: ob die Planungshilfe das Thema mit getrennten Reihen
      EBR/FOR und GYM führt oder mit dem Differenzierungshinweis;
      Fundstelle und ein Satz, worin sich die Reihen unter-
      scheiden, wenn getrennt.
   e) Eine Zeile „Spanne: ja/nein" – ja, wenn mindestens eine
      Einheit oder Sprosse auf G oder H liegt und mindestens eine
      auf F oder darunter; sonst nein. Das ist die Zeile, die
      später die Frage auslöst.
   Am Ende der Datei ein Abschnitt „## Zahlen": Einträge gesamt,
   Einheiten und Sprossen gesamt, davon mit Stelle, davon ohne;
   Einträge mit Spanne ja/nein; Liste der Einträge ohne jede
   Stelle.
3. Schreibe katalog/_kursart-belege.md. Kopf wie oben. Je Sek-II-
   Eintrag ein Abschnitt mit:
   a) Geltung je Zielprüfung aus den vier Geltungstabellen
      (be-gk, be-lk, bb-gk, bb-ea: ja/nein, wortgleich die Zeile
      der Tabelle, mit Zeilennummer); fehlt das Thema in einer
      Tabelle: „nicht geführt".
   b) Je Lerneinheit: ob der Eintrag oder der GOST-Text sie als
      Leistungskurs-Zusatz führt – Zitat aus Verortung oder
      Prüfungsform des Eintrags („LK-Zusatz", „nur be-lk und
      bb-ea", „Leistungskursfach") mit Zeilennummer; dazu die
      Stelle im GOST-Text (Berlin und Brandenburg, je Zeilen-
      nummer), die den Inhalt dem Grundkurs, dem Leistungskurs
      oder beiden zuordnet, wortgleich, höchstens zwei Zeilen.
      Keine Stelle: „keine Stelle".
   c) Je Haupttyp der Prüfungsform: ob die Zeilen im Eintrag nur
      aus LK-Heften oder erhöhtem Niveau stammen (Kürzel in den
      Zeilen: be-lk, bb-ea, iqb erhöht) oder auch aus GK-Heften.
      Zählung je Typ: Zeilen GK / Zeilen LK.
   d) Zeile „Spanne: ja/nein" – ja, wenn der Eintrag Einheiten
      oder Typen beider Kursarten hat; „nur LK", wenn alles LK;
      „nur GK", wenn nichts LK; „kein Planinhalt", wenn die
      Geltung viermal nein ist.
   Abschnitt „## Zahlen" am Ende wie in Schritt 2.
4. README.md: Im Abschnitt „## katalog/ – Themenkatalog" nach der
   Zeile zu `_blatt0-belege.md` zwei Zeilen einfügen, im Stil der
   Nachbarzeilen: `_niveaustufen-belege.md` – Belege der
   Niveaustufe je Lerneinheit und Sprosse der Sek-I-Einträge aus
   RLP und LISUM (seit 24.09.2026), Vorschlag für die Marke, die
   der Prompt ab v4.3 für die Schulformfrage braucht; nie von
   Hand ändern, entscheidet nicht. `_kursart-belege.md` – Belege
   der Kursart je Einheit und Typ der Sek-II-Einträge aus
   Geltungstabellen, GOST und Prüfungsform (seit 24.09.2026),
   Vorschlag für die LK-Marke; ebenso. Sonst nichts ändern.
5. git mv auftrag-niveaustufen-belege.md archiv/.
6. Commit „Vorschlagsdateien Niveaustufe (Sek I) und Kursart
   (Sek II)". Nicht pushen.

## Prüfungen (Gegenprobe mit bekannten Werten)

Eine Abweichung ist ein Befund für den Bericht, kein Grund, die
Datei anzupassen:
- quadratische-funktionen: der Eintrag sagt „beginnt auf G;
  Linearfaktoren, quadratische Ergänzung als Verfahren und die
  allgemeine Form mit a erst auf H". Deine Datei muss für die
  Einheiten mit Scheitelpunktform G und für die Sprossen zu
  Linearfaktoren und quadratischer Ergänzung H liefern; Spanne ja.
- prozentrechnung: Verortung nennt Klasse 7; erwartet D/E für
  Grundwert, Prozentwert, Prozentsatz und F für Veränderung und
  Zinsen, Spanne nein oder ja – Ergebnis nennen, nicht raten.
- normalverteilung-und-sigma-regeln, hypothesentests, scharen-
  von-geraden-und-ebenen: Eintrag sagt „nur be-lk und bb-ea";
  erwartet Geltung be-gk nein, bb-gk nein, be-lk ja, bb-ea ja,
  „nur LK".
- matrizen-und-uebergangsprozesse, konfidenzintervalle: Geltung
  viermal nein → „kein Planinhalt".
- kurvenuntersuchung: Einheiten in beiden Kursarten → Spanne ja.
- Beide Dateien: jede Zitatzeile trägt eine Zeilennummer, die im
  Quelltext existiert – stichprobenartig zehn je Datei mit sed
  nachschlagen und im Bericht nennen.
- katalog/_pruef_struktur.py läuft danach unverändert durch
  (Aufruf über den vollen Python-Pfad aus katalog/); die
  Kennzahlen 1–9 sind gleich wie vor dem Auftrag – die neuen
  Dateien beginnen mit „_" und werden nicht als Einträge gezählt.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann:
- die Zahlen-Abschnitte beider Dateien wortgleich;
- Ergebnis jeder Gegenprobe;
- die zehn Stichproben je Datei;
- Kennzahlen 1–9 vor und nach dem Auftrag;
- Stellen, an denen Du Ermessen gebraucht hast (Inhalt passt zu
  keiner Tabellenzeile wörtlich), mit einer Zeile je Fall –
  diese Liste ist das Wichtigste des Berichts;
- Abweichungen und Annahmen; Laufzeit.
Letzte Zeile: „Push origin drücken".

## Regeln

- Python 3.12 liegt nicht im PATH der Claude-Code-Shell, py -3
  gibt es nicht: nur der volle Pfad
  %LocalAppData%\Programs\Python\Python312\python.exe.
- git über die git.exe von GitHub Desktop.
- Kein Eintrag in katalog/ wird geändert, kein Skript, keine
  Quelle. Neu sind nur die zwei Vorschlagsdateien und zwei
  README-Zeilen. Nichts löschen.
- Zitate wortgleich aus dem Quelltext, mit Zeilennummer, nie aus
  dem Gedächtnis; keine Zeilennummer ohne Nachschlagen.
- Wo Du raten müsstest, schreibst du „keine Stelle" oder
  „Ermessen:" mit Begründung. Eine ehrliche Lücke ist mehr wert
  als eine plausible Stufe.
- Die Datei nennt Stufen, sie setzt keine Marke im Katalog und
  formuliert keine Prompt-Regel.
