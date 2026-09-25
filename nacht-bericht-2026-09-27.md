Modell: Opus 5.5 (claude-opus-5-5)

# Bericht Auftrag Nacht 2026-09-27

Auftrag und Standdatei: archiv/auftrag-nacht-2026-09-27.md, archiv/nacht-stand-2026-09-27.md. Alle zehn Teile erledigt, mit Commits; offen bleiben 6.2 (Fundamente B Q-Phase nicht gefunden), die vier Pool-Vormerkungen der CAS-Nachträge (Teil 9), die nicht unabhängige Eichung 2017-ga-B und der Nachzug der Sek-II-Einträge (Teil 10) – je mit Posten in faellig.md § 2. Hilfsagenten (Opus) für Teil 7 Abschnitte 1–2, Teil 9 und Teil 10, nacheinander, wo sie dieselben Dateien berührten.

## Teil 1: Belegskripte auf die drei neuen Katalogstellen, Marken neu (Commit 265ce68)

Geändert: `werkzeuge/klassen-belege-daten.py` (23 Ersetzungen), `werkzeuge/pruefungswort-belege-daten.py` (Vorrat-Typ 1.11 gestrichen, 1.13 → 1.12, zwei Kommentarblöcke zu Einheit 5 und 7), `werkzeuge/marken-bau-stellen.txt` (8 Potenzfunktionen-Zeilen auf Einheit 5 und „gilt“, 5 Vierfeldertafel-Zeilen auf Einheit 7 und „gilt“, 28 Klasseneinteilungs-Typzeilen von Einheit 6 auf Einheit 1), `werkzeuge/marken-bau.py` (Datei-2-Prüfung liest die neue Einheit aus der Entscheidungsspalte). Neu gebaut: `katalog/_klassen-belege.md`, `werkzeuge/klassen-belege-typen.txt`, `katalog/_pruefungswort-belege.md`, `werkzeuge/pruefungswort-belege-typen.txt`, `katalog/_klassen-ermessen.md`.

Zahlen: `klassen-belege.py` und `pruefungswort-belege.py` laufen ohne die bisherigen Abbrüche (sieben Fehler Vorrat-Typ, zwei Prüffehler). Lerneinheiten in `_klassen-belege.md` 116 → 118, Typzeilen 649 → 678, Ermessensfälle 250 → 236 (15 Gründe „nur Vorrat“/„nur Sek-II-Deutungstyp“/„gehört zu Einheit 6“ entfallen, einer kommt dazu). `_pruefungswort-belege.md`: 116 Sek-I-Lerneinheiten, 1 334 Typen, Einheiten ohne P10-Typ 21 → 23 (potenz-exponentialfunktionen 5, daten 7). `marken-bau.py --probe` und der Lauf ohne `--probe`: „nichts zu ändern“.

**Neue Zahl der Marken-Zeilen: 273, Typklammern: 262** – unverändert. Die drei Stellen bringen nichts dazu, weil der Auftrag Marken sie schon über die Stellenliste („Einheit 5“, „Einheit 7“, „Typ daten 1: …“) auf die neuen Einheiten gelenkt hatte; jetzt stehen sie in den Belegen selbst dort.

Gegenprobe im Wortlaut (Belegdateien bericht-marken.md, katalog/_klassen-belege.md, katalog/_pruefungswort-belege.md): „git diff über katalog/*.md zeigt geänderte Marken-Zeilen und Typklammern nur in potenz-exponentialfunktionen.md und daten.md“ – **erfüllt im stärkeren Sinn: kein Eintrag ändert sich** (Einträge: 0 geändert). „lineare-funktionen Einheit 4 trägt weiter „P10“ (3 von 13)“ – erfüllt: „OS Kl. 8 · GYM Kl. 8 · P10 · nicht für alle: Mathematik 2023 8 Vertiefen“. „quadratische-gleichungen Einheit 2 weiter „GYM Kl. 8–9““ – erfüllt: „OS Kl. 10 · GYM Kl. 8–9 (LS 9, Fundamente 9, Elemente 8) · P10“. Die im Skript fest eingebaute GEGENPROBE meldet für diese beiden und kreis 1 (Typ) weiter „ABWEICHUNG“, weil dort die falschen Sollwerte der Übergabe vom 26.09. stehen (bericht-marken.md); Skript nicht geändert. potenz-exponentialfunktionen 5: „OS Kl. 10 · GYM Kl. 9 · keine P10-Aufgabe · nicht für alle: Sekundo 10 Zusatzstoff“, daten 7: „OS Kl. 9 · GYM Kl. 9–10 (LS 9, Fundamente 10, mathe.delta 10) · keine P10-Aufgabe“ – beide jetzt aus `_pruefungswort-belege.md`, nicht mehr aus der Ersatzregel.

Eigene Entscheidungen:
- Neun statt acht Potenzfunktionen-Stellen verschoben: dazu Fundamente 2017 Kl. 9 „6.1 Potenzfunktionen mit natürlichen Exponenten“ (Nebenquelle, zählt in keiner Marke). Alle Erm-Texte „nur Vorrat in Einheit 1“ und „nur Sek-II-Deutungstyp“ gestrichen, weil die Zuordnung jetzt wörtlich ist.
- Klasseneinteilung: acht Stellen (Sekundo 8 LVL, Mathematik heute 9, Fundamente 6 und 7, Elemente 2016 und 2025 je Kl. 7, Fundamente 2017 Kl. 7 und 9) von Einheit 6 nach Einheit 1 mit Typzeilen an allen vier Klassen-Typen; Fundamente 10 „4.1 Häufigkeitsverteilungen“ bleibt Stelle für Einheit 6 und steht zusätzlich als Typzeile unter Einheit 1 (mit Ermessen). Die Stellenliste führt diese Typzeilen unter Einheit 1 ohne „gilt“, sie setzen also keine Klasse (Regel A wie bisher).
- `marken-bau.py`: Datei 2 nennt die Fälle mit der alten Einheit (potenz 1, daten 1 und 6). Die Prüfung `pruefe_datei2` nimmt jetzt auch jede Einheit an, die die Spalte „Entscheidung“ nennt („gelten für die neue Einheit 5“). NEUE_EINHEITEN bleibt als Rückfall, greift aber nicht mehr.
- Prüfungswort der neuen Einheiten: **keine P10-Zuordnung** in `pruefungswort-belege-daten.py`. Nach der Lesart „prüft“ hätte der Typ 5.14 („Potenzfunktion vom exponentiellen Term unterscheiden“, bisher 1.11 mit 2017-OS-K7c → „Exponentialfunktion aufstellen“) Einheit 5 zu „P10“ (4 Jahrgänge) gemacht, 7.4 („Anteil an allen …“ = „Relative Häufigkeit angeben“) Einheit 7 ebenso. Datei 3 sagt „Kein P10-Original zu allen dreien; das Prüfungswort sagt das“ – die Entscheidung des Chats geht vor; die alte Begründung steht als Kommentar in den Daten, der Vorschlag in katalog/_vorschlaege-2026-09-27.md Abschnitt 1.
- `daten` Einheit 1 „umnummerieren“: keine Daten betroffen (die T-Zuordnungen reichen bis 1.8; die Sek-II-Typen 1.12–1.16 heißen jetzt 1.16–1.20, tragen aber keine S-Daten).
- `_klassen-ermessen.md` im selben Commit neu gebaut (Zahl 236), weil die README-Regel „nach jedem Neubau von _klassen-belege.md“ gilt; Teil 4 hat sie nach der Skriptänderung noch einmal gebaut.
- Die Stand-Zeile von `_pruefungswort-belege.md` bleibt „unbekannt“ (das Skript sucht `git` nur im PATH); nicht geändert, weil ein Hash dort bei jedem Neubau nach einem Commit wechseln würde (die Eingabe „katalog“ schließt die Ausgabedatei ein).

## Teil 2: FHR-Wort an den acht Sek-I-Einheiten mit Sek-II-Zeilen (Commit cba84ca)

`werkzeuge/marken-bau.py`: hinter dem P10-Wort „FHR“, wenn der Sek-II-Teil der Einheit in `_pruefungswort-belege.md` („### <eintrag> (Sek-II-Teil eines Sek-I-Eintrags)“, Zeile „FHR-Jahrgänge n von 8“) mindestens einen FHR-Jahrgang hat (`FHR_SCHWELLE = 1`). Form wie bei den Sek-II-Einträgen („… · Abitur GK · Abitur LK · FHR“): ein eigenes Wort „FHR“, durch „ · “ getrennt, vor „nicht für alle“. Geändert: fünf Marken-Zeilen – einheiten 1 (7 von 8), einheiten 3 (7 von 8), einheiten 4 (1 von 8), daten 1 (7 von 8), daten 4 (7 von 8). lineare-gleichungssysteme 1, 3, 4 haben keinen FHR-Jahrgang (ihre Sek-II-Zeilen sind abi/iqb) und bleiben ohne Wort.

Gegenprobe im Wortlaut (bericht-marken.md Punkt 15): „daten 1 und daten 4 tragen danach „FHR““ – erfüllt: „OS Kl. 5–6 (Mathematik 2023 5, Schnittpunkt 5, Mathematik heute 6) · GYM Kl. 5 · P10 · FHR · nicht für alle: …“ und „OS Kl. 6 · GYM Kl. 6–7 (…) · P10 oft · FHR · nicht für alle: …“. „außer den acht Einheiten ändert sich keine Marken-Zeile“ – erfüllt (git diff: nur einheiten.md drei Zeilen, daten.md zwei Zeilen); zweiter Lauf „nichts zu ändern“.

Eigene Entscheidung: nur „FHR“, kein „Abitur GK/LK“ für die Sek-II-Zeilen der Sek-I-Einheiten (der Auftrag nennt nur FHR; lineare-gleichungssysteme hätte sonst „Abitur …“ bekommen).

## Teil 3: potenz-exponentialfunktionen.md an Einheit 5 angleichen (Commit 1036af9)

Geändert: Nummernzeile Einheit 1 ohne „Potenzfunktion als zweiter Funktionstyp mit Potenz im Term (Vorrat, H)“ und ohne Eingabe „potenzfunktion“; Verortung ([LS-AA]: „Einheit 5 = Kl. 9 III 7“; LISUM-Absatz: Satz zur neuen Einheit 5 mit den Klassenbelegen statt „Der Vorrat-Ausblick dieses Eintrags bleibt deshalb Sek I“); „Offene Punkte“: Gliederung (fünf Einheiten, Alternative A am 26.09. im Chat umgekehrt entschieden, Einheit 5 ohne Merkkasten, Sprossen, Blatt 0 – Posten in faellig.md) und Potenzfunktion (seit 26.09. Einheit 5, der Rest der Reihe 2417 offen); katalog/index.md Tabellenzeile („Potenzfunktionen mit natürlichem Exponenten (Einheit 5 seit 26.09.2026 …)“ statt „Potenzfunktion als Vorrat, H/GYM“).

Prüfung: `themen-pruef.py` „Alle Prüfungen bestanden“; `verweis-pruef.py` ohne neuen Befund (Gruppe (c) weiter 16 auf 5 Namen; drei neue Verweise auf _klassen-belege.md, _marken-neue-einheiten.md, faellig.md); `_pruef_struktur.py` „Strukturprüfung: ok“; `_pruef_katalog.py potenz-exponentialfunktionen.md` „ERGEBNIS: ok“. `_verweise.md` mitcommittet.

Eigene Entscheidung: einen ersten Verweis auf die Vorschlagsdatei aus Teil 7 wieder herausgenommen – er hätte bis Teil 7 einen Verweis auf eine fehlende Datei erzeugt. Nicht angefasst (so der Auftrag): die Sprosse „Potenzfunktion einordnen (Einheit 1, Vorrat)“ und der Vorrat-Satz unter „Für schwache Schüler“ – beide gehören zum Ausbau in Teil 7.

## Teil 4: Kleinposten (Commits de503c9, f9632e3)

1. flaechen.md, Prüfungsform: nach `msa/msa-katalog-basis.csv` ist 2014-OS-B1g das Kreuz aus Quadraten (u = 16a), 2022-OS-B1e das rechtwinklige Dreieck (A = d · e : 2), 2025-OS-B1i das geteilte Rechteck (Ankreuzen A = a · (b + c)); die Aufzählung lautet jetzt „2019-OS-B1e und 2025-OS-B1i geteilte Rechtecke, 2014-OS-B1g Kreuz aus Quadraten, 2024-OS-B1c gleichseitiges Dreieck …, 2022-OS-B1e rechtwinkliges Dreieck“. Dazu (außerhalb der genannten Zeile, derselbe Fehler) die Zielmarke Einheit 1: „(Fläche 2025-OS-B1i, Umfang 2014-OS-B1g)“ statt „(2025-OS-B1i, 2024-OS-B1c)“ – 2024-OS-B1c ist ein Dreieck (Einheit 3). Die Fehlerzeilen und Blatt-0-Klammern mit diesen ids waren schon richtig.
2. GYM-Typen (msa-typen.csv, Thema des Eintrags, im Eintrag fehlend). Lesart „Typenzeile der passenden Lerneinheit“: die Zuordnungszeile der Prüfungsform (dort stehen die P10-Typen je Einheit; die Zeile „Typen je Lerneinheit“ führt Katalogtypen, eine Einfügung dort hätte die Typnummern verschoben). zuordnungen.md: „Antiproportionale Zuordnung Dreisatz“ (2014-GYM-B1c, Futtervorrat, Niveau II) → Einheit 3 (umgekehrter Dreisatz über das Produkt); Satz „kommen im Prüfungskatalog nicht als eigener Typ vor“ → „haben damit einen eigenen Typ, aber kein Original im Oberschulpapier“, „mit vier Typen“ → „mit fünf Typen“, Zielmarke Einheit 3 um das GYM-Original ergänzt. terme.md: „Term durch Zusammenfassen gleichartiger Glieder vereinfachen“ (2025-GYM-B2a) → Einheit 2 (gleichartige Glieder, auch x²); „Term mit Klammern und Potenzen vereinfachen“ (2022-GYM-B2b, Niveau III) → Einheit 3 (Klammer mit Minus davor auflösen und zusammenfassen; die binomische Formel darin → binomische-formeln.md Einheit 2); „Binomische Formel anwenden“ (2019-GYM-B1f) → keiner Einheit (Verfahren in binomische-formeln.md Einheit 2, Original hier nach seinem typen.csv-Thema, Muster flaechen.md mit den Kreistypen); Satz „Der einzige Typ dieses Eintrags“ → „Das typen.csv-Thema „Terme umformen“ hat vier Typen …“, „Einheit 2 bis 4 – kein Typ“ → je Einheit; Zielmarken Einheit 2 und 3 um die GYM-Originale ergänzt. U-Daten in `pruefungswort-belege-daten.py` nachgezogen (zuordnungen 3, terme 2 und 3); die T-Zuordnungen kannten die Typen schon.
3. themen.csv: Zeile „zuordnungen;…;Maßstab“ → „strahlensaetze;…;Maßstab“; die Zeile „strahlensaetze;…;kein Prüfungsthema“ entfällt (sonst stünde der Vermerk „kein Prüfungsthema“ neben einem Prüfungsthema), 157 statt 158 Zeilen. Folgen: `themen-pruef.py` bestanden; `rohdaten/zuordnungen.md` neu und `rohdaten/strahlensaetze.md` neu (Nachzug f9632e3, README 66 → 68 Dateien – die README-Zahl war schon vorher überholt, 67); `_verweise.md` Prüfung 3 (b): H1-Abweichungen 27 → 28 (strahlensaetze trägt jetzt das thema „Maßstab“).
4. `werkzeuge/klassen-ermessen.py` v0.2: bei gleichem Grund an mehreren Stellen kommt das Zitat aus der Stelle der eigenen Reihe und Einheit. Neu gebaut: zwei Zitate berichtigt (trigonometrie 2, Elemente Kl. 9: jetzt „4.3 Berechnungen in rechtwinkligen Dreiecken“ statt der Mathematik-2023-Zeile; potenz-exponentialfunktionen 2, Fundamente Kl. 10: jetzt „2.1 Exponentielles Wachstum“ statt der LS-Zeile). Die fünf Potenzfunktionen-Fälle des Nebenbefunds gibt es seit Teil 1 nicht mehr.
5. katalog/index.md, Absatz „Belege der Blatt-0-Fertigkeiten ohne Ziel“: „131 … ein Ziel und 16 keins“, „22 Einträge 147/131/16 …, übrige 51 Einträge 316/308/8; … Kennzahl 9 (24 von 463)“, Stand 795ca0a mit Freigabe.

Gegenprobe im Wortlaut (nacht-bericht-2026-09-26.md): „msa/msa-typen.csv zählt zum Thema „Zuordnungen“ den Typ „Antiproportionale Zuordnung Dreisatz“; er steht danach in zuordnungen.md“ – erfüllt (Typenliste und Zuordnungszeile Einheit 3). `_pruef_katalog.py` für flaechen, terme, zuordnungen, strahlensaetze: Ausgabe gleich dem Stand vor der Änderung (terme „Befunde“ wie vorher); `_pruef_struktur.py` ok, Kennzahl 5 unverändert 48 von 2908. Mitgebaut: `_tragfaehigkeit.md` (fünf Zeilen „Katalogzeilen“ mit GYM – war seit dem GYM-Auftrag überholt).

## Teil 5: Vorrat-Verweise auf die Sek-II-Einträge (Commit 99da689)

Zählung vorher (grep `(gost|fos)-[a-z0-9-]+\.md` über katalog/*.md): 43 Verweise auf zwölf Dateien in zwölf Dateien – 16 in acht Einträgen, 17 in index.md, 3 in _offen.md, 2 in _quellenprotokoll.md, 5 im abgeleiteten _verweise.md; dazu acht Wortform-Stellen „gost-*.md“, „gost-Einträge“ (reelle-zahlen, trigonometrische-funktionen, wahrscheinlichkeit, _fragen.md zweimal, _offen.md, _quellenprotokoll.md zweimal), mit umgestellt.

Zuordnung alte Datei → Eintrag (Stelle: Datei und Zeile vor der Änderung):

| alte Datei (nie gebaut) | Stelle | heute |
|---|---|---|
| gost-funktionen-grundlagen.md | binomische-formeln 5 | funktionsklassen-und-eigenschaften.md Einheit 2 |
| gost-funktionen-grundlagen.md | quadratische-funktionen 5 | rekonstruktion-von-funktionsgleichungen.md Einheit 1 |
| gost-funktionen-grundlagen.md | quadratische-gleichungen 5, 128 | funktionsklassen-und-eigenschaften.md Einheit 2 |
| gost-funktionen-grundlagen.md | reelle-zahlen 101 | gleichungen-loesen.md |
| gost-funktionen-grundlagen.md | trigonometrische-funktionen 7, 130, 135 | funktionsklassen-und-eigenschaften.md Einheit 5; gleichungen-loesen.md Einheit 3; ableitungsregeln.md (LK) – Tangens, Additionstheoreme u. a. stehen in keinem Eintrag (so vermerkt) |
| gost-funktionen-grundlagen.md | _offen 122 | gleichungen-loesen.md |
| gost-funktionen-grundlagen.md | _offen 148 | wie trigonometrische-funktionen 135 |
| gost-funktionen-grundlagen.md | _quellenprotokoll 235 | funktionsklassen-und-eigenschaften.md |
| gost-ableitung.md | trigonometrische-funktionen 135, _offen 148 | ableitungsregeln.md (LK-Zusatz) |
| gost-exponential-e.md | potenz-exponentialfunktionen 7 | funktionsklassen-und-eigenschaften.md, gleichungen-loesen.md Einheit 2 |
| gost-exponential-e.md | potenz-exponentialfunktionen 125 | gleichungen-loesen.md Einheit 2, umkehrfunktion.md |
| gost-exponential-e.md | potenz-exponentialfunktionen 129 | funktionsklassen-und-eigenschaften.md, ableitungsregeln.md Einheit 2, ableitung-und-aenderungsrate.md |
| gost-exponential-e.md | _quellenprotokoll 200 | funktionsklassen-und-eigenschaften.md |
| gost-stochastik.md, fos-stochastik.md | wahrscheinlichkeit 5 | zufallsgroessen-und-verteilungen.md, kenngroessen-von-verteilungen.md, daten.md Einheit 7 und vierfeldertafel.md, bedingte-wahrscheinlichkeit-und-bayes.md, unabhaengigkeit.md, zufallsexperimente-und-pfadregeln.md (Simulation) |
| gost-stochastik.md | kombinatorik 110 | Satz ohne Dateinamen umformuliert (Sek-II-Stochastik-Einträge) |
| gost-kurvendiskussion, gost-integral, gost-vektoren, gost-ebenen, fos-funktionen, fos-differential, fos-integral (.md) | nur index.md, Gliederungsentwürfe | Spalte „heute (kanonische Einträge nach themen.csv)“ der beiden Tabellen |
| alle zwölf | _verweise.md (5) | abgeleitet, neu gebaut |

Gliederungsentwürfe in index.md: gegen themen.csv geprüft; beide Tabellen bleiben als Herkunft, Spalte „Datei“ → „Entwurf“ (Name ohne Dateiendung), neue Spalte „heute (kanonische Einträge nach themen.csv)“, Überschriften „– alter Gliederungsentwurf, ersetzt“. Befund: jeder Entwurf ist abgedeckt; kein Entwurf sah die Matrizen vor; die FOS-Umkehrfunktion hat keine fhr-Zeile (umkehrfunktion.md nur abi/iqb). Der Absatz vor „Gymnasiale Oberstufe“ sagt jetzt, dass die Dateien nie gebaut wurden, geprüft sind und die Verweise auf die kanonischen Einträge zeigen.

Gegenprobe im Wortlaut: „grep über katalog/*.md findet danach kein „gost-“ und kein „fos-“ mehr“ – **erfüllt für Verweise und Wortformen** (0 Treffer für `(gost|fos)-…\.md`, 0 für „gost-*“, „gost-Einträge“); ein grep auf die bloße Zeichenfolge findet weiter die Dateinamen der Planquellen `quellen/quelle-rlp-gost-bb-2022-mathematik.txt`, `…-gost-be-2022-…`, `…-gost-2022-mathematik-anlage-ohimi.txt` und `…-rlp-fos-bb-2019-…` (41 Sek-II-Einträge, _quellen.md, _kursart-belege.md, _sek2-ordnung-belege.md) – das sind vorhandene Dateien und keine Vorrat-Verweise. „verweis-pruef.py zählt in Gruppe „Ziel fehlt“ 43 weniger“ – **Abweichung mit Erklärung**: die Gruppe zählte vorher 16 (auf 5 Namen) und jetzt 0, also 16 weniger; `verweis-pruef.py` liest nur die 73 Einträge, nicht index.md und die _-Dateien, auf die 27 der 43 Verweise entfallen. Kennzahl 8 von `_pruef_struktur.py`: 16 → 0 Verweise auf fehlende Dateien.

## Teil 6: Netz und Pfade (Commit 2f52c77)

1. cosh: Version 3.1 (2025, Datei Mai 2026, 43 Seiten, CC BY-SA 4.0 laut Abschnitt „Lizenz“) von https://cosh-bw.de/wp-content/uploads/2026/05/makV3.1.pdf (die ältere Adresse …/2025/07/makV3.1.pdf liefert 404; Version 3.0 unter https://cosh-mathe.de/wp-content/uploads/2021/12/makV3.0.pdf, 40 Seiten, nicht abgelegt). Abgelegt: `quellen/quelle-cosh-mindestanforderungskatalog-v3.1.pdf` und `.txt` (pdftotext -layout -eol unix), Abschnitt in quellen/quellen.md, README-Zeile; konzept.md § 4 Entscheidung 36 und die Registerzeile [COSH] in katalog/_quellen.md zeigen auf die Datei (dort mit „Gliederung noch nicht daran geprüft“).
2. Fundamente B Qualifikationsphase: **nicht gefunden (offen)**. Zehn SRU-Abfragen: tit + „Qualifikationsphase“ (18 Treffer 2018–2025), drei Titelsätze mit Feld 926 (2025 GK und LK: Nordrhein-Westfalen; 2018 GK: ohne Land), jhr 2025, 2024, 2026 (2026 „Q1/Q2“ GK und LK: Hessen, zwei Abfragen für 926), ISBN-Kreis der Ausgabe B 9783060098* (nur Einführungsphase 2023 und Klasse 9/10). Kein Band ist nachweislich Ausgabe B, deshalb nichts abgelegt und die Lehrwerksliste in _sek2-ordnung-belege.md nicht geändert; Befund in quellen/quellen.md, der Posten in faellig.md § 2 bleibt mit Zusatz.
3. `abitur/iqb-quellen.py` v0.6: Standard-Cache `hefte/iqb/` (über den Ort des Skripts bestimmt, damit er aus `abitur/` und aus der Wurzel gleich ist), dazu `--help`. README (beide Stellen), konzept.md § 2, .gitignore (Kommentar; `iqb-pdf/` bleibt ausgeschlossen für alte Aufrufe), werkzeuge/tragfaehigkeit.py (Kommentar, Menge unverändert; `_tragfaehigkeit.md` danach nur Stand-Zeile anders, zurückgesetzt).

Gegenprobe im Wortlaut: „python abitur/iqb-quellen.py --help … darf nichts holen und muss hefte/iqb als Standard nennen“ – erfüllt: Ausgabe „Standard-Cache: C:\Users\holge\mathe\mathe-nachhilfe\hefte\iqb (hefte/iqb/ im Repo, lokal)“, kein Netzzugriff. Vorher hätte `--help` als Cache-Name gegolten und den Abruf gestartet; deshalb die Option neu.

## Teil 7: Vorschläge für das Urteil im Chat (Commit 1d53833)

Neu: `katalog/_vorschlaege-2026-09-27.md` (Kopf: Zweck, Stand b9683ed, „Vorschlag, nicht entschieden“), README-Zeile. Zeilen je Abschnitt:

- Abschnitt 1 Ausbau der neuen Einheiten (potenz-exponentialfunktionen 5, daten 7; Merkkasten, Sprossen, Zielmarke, Blatt 0, P10-Lesart): 199 Zeilen
- Abschnitt 2 Niveaustufe G (Sinussatz in beliebigen Dreiecken; Lösbarkeit quadratischer Gleichungen): 60 Zeilen
- Abschnitt 3 2025-GYM-K5d Nebentyp-Etikett: 10 Zeilen
- Abschnitt 4 Namensabweichungen H1 ↔ `thema`: 36 Zeilen (Tabelle mit 28 Einträgen = `_verweise.md` Prüfung 3 (b); der Posten nannte 27, der 28. ist strahlensaetze seit dem Maßstab-Umzug in Teil 4)

Gegenprobe im Wortlaut (katalog/_verweise.md Prüfung 3 (b)): „Abschnitt 4 hat so viele Zeilen, wie _verweise.md Prüfung 3 (b) Einträge nennt“ – erfüllt: **28** Einträge dort nachgezählt, 28 Tabellenzeilen in Abschnitt 4. Die Fundstelle nannte 27 und die Überschrift 28, weil Teil 4 (Maßstab nach strahlensaetze) den 28. Eintrag erst erzeugt hat; `_verweise.md` ist seitdem in sich einig. Die vier Posten stehen in faellig.md § 2 mit dem Zusatz „Vorschlag liegt vor (katalog/_vorschlaege-2026-09-27.md Abschnitt n), Entscheidung im Chat“; kein Katalogeintrag geändert.

Eigene Entscheidung: Abschnitte 1 und 2 von einem Hilfsagenten (Opus) entworfen, Abschnitte 3 und 4 selbst; beide Entwürfe gegen die Einträge und die Belegdateien gelesen, bevor sie in die Datei kamen.

## Teil 8: Prüfskript, Kennzahlen, Testlauf-Vorlage (Commit b9683ed)

1. `werkzeuge/blatt-pruef.py` v0.3. `../blattbau/mathblatt.sty` trägt noch Version 2026-09-22h ohne Stufe-5-Bausteine; die Namen stammen aus dem Auftrag (\zweigzeile, Umgebung abhakseite mit \abhak, \verzeichniszeile mit \verz, \swfrage). \swfrage zählt als Teilaufgabe; für Blätter mit einem dieser Bausteine drei neue Kennzahlen je Blatt: 10 „Einheitenköpfe n · Zweigzeilen m“ (mit Zahl der \swfrage), 11 Abhakseite ja/nein mit Zahl der \abhak, 12 Verzeichniszeile ja/nein mit Zahl der \verz; dazu die Zuordnung Einheitenkopf → Lerneinheit mit Vermerk, wenn kein Kopf trifft, und die „weiteren Köpfe“ (Inhalt, Das kennst du schon, Das kann ich). Zuordnung über den Titel hinter dem letzten „·“ (Blattnummer „Einheit n von m“ zählt nicht), Sprungmarken im Kopf und eine Ich-Form am Titelanfang abgelöst. **Alter Modus byteidentisch**: Lauf von v0.2 und v0.3 über alle 22 PDFs unter blaetter/ gleich (Hash). Am Testlauf 25.09. (nur zur Probe nach scratch geschrieben, blaetter/testlauf-2026-09-25/ unberührt): Eingabe 3 zählt jetzt 38 statt 34 Teilaufgaben (die Sitzung benutzte \swfrage), die Kopfzuordnung trifft bei 1, 2, 3, 5, 7, 8, 9; Eingabe 6 und 10 nutzen den blatteigenen \zweigkopf und bleiben ohne Zuordnung.
2. `blaetter/kennzahlen.md` neu gebaut (Freigabe 25.09.); 14 Zeilen anders als der eingecheckte Stand (Katalogänderungen seit 7613213).
3. `werkzeuge/testlauf-auftrag.md`: Kopie von archiv/auftrag-testlauf-2026-09-25.md mit Kopfzeile „Vorlage; für einen Lauf in die Wurzel als auftrag-testlauf.md kopieren, Datum eintragen.“ und den drei Änderungen – Blätter nacheinander (Regelweg `claude -p` zuerst mit Probeaufruf, Ersatzweg Sub-Agent als zweite Stufe, nie parallel), Uhrzeiten in stand.md nur aus Get-Date (Start- und Endzeit je Zeile), Ordner `blaetter/testlauf-<datum>/` und `bericht-testlauf-<datum>.md` mit dem Datum des Laufs (bei zweitem Lauf am Tag „b“). README: Zeile für die Vorlage, archiv-Absatz verweist auf sie; faellig.md: Posten „Testlauf wiederholen“ zeigt auf die Vorlage. Der Testlauf lief nicht.

Gegenprobe im Wortlaut (nacht-bericht-2026-09-26.md Teil 1, bericht-testlauf-2026-09-25.md Nebenbefund): „fokus_a.pdf: 4 Seiten, 16 Hauptnummern, 54 Teilaufgaben“ – erfüllt („| prozentrechnung | 2026-09-24 | v4.2 | fokus_a.pdf | 4 | 16 | 54 | …“). „Daten_E1.pdf (2026-09-22) „Typen ohne Treffer“ 7 von 15 mit dem heutigen Katalog“ – erfüllt („7 von 15 (gebaute Einheiten)“).

## Teil 9: CAS-Nachtrag 2017-bb-ea-cas und 2018-bb-ea-cas (Commits 11d31b9, 4624fc9)

`abitur/abi-bau.py` v0.14 mit Nachtragsmodus (KONFIG `nachtrag_zu`, `unveraendert`, `uebernommen`, `be_angeboten`): erfasst werden nur die Teilaufgaben der „CAS:“-Aufgaben, die vom WTR-Heft abweichen; wortgleiche Teilaufgaben und Aufgaben ohne Präfix werden gegen das WTR-Heft geprüft und nicht doppelt geschrieben. Regel in abi.md v0.30.

| Heft | Zeilen | BE der Zeilen | neue Typen | „?“ | Poolquote | Eichung |
|---|---|---|---|---|---|---|
| 2017-bb-ea-cas | 14 (2.1 a, b, c, e, f; 2.2 b, d, g; 3.1 c, e, f; 4.2 a, b, d) | 87 (dazu 63 übernommen, 35 unverändert = 185) | 1 („Identische Graphen einer Schar zu entgegengesetzten Parameterwerten begründen“) | 0 | 3 von 14; 13 von 87 BE (15 %), alle „Poolaufgabe (nicht erfasst)“ | – (kein Maßstab) |
| 2018-bb-ea-cas | 14 (2.1 c–h; 2.2 b, d, e, f, g, i; 3.1 f; 4.2 d) | 77 (dazu 73 übernommen, 35 unverändert = 185) | 3 (u. a. „Rotationsvolumen um die x-Achse berechnen“) | 0 | 1 von 14; 6 von 77 BE (8 %), „Poolaufgabe (nicht erfasst)“ | – (kein Maßstab) |

Gegenprobe im Wortlaut (abi-pruefungen.md § 2): „Seiten 10 bzw. 12, BE 100 je Heft“ – erfüllt (Zeilen „| 2017 | 2017-bb-ea-cas | BB | erhöht | CAS | 10 | 270 | 100 |“ und „| 2018 | 2018-bb-ea-cas | BB | erhöht | CAS | 12 | 270 | 100 |“, die PDFs unter hefte/abi/ haben 10 und 12 Seiten). **„CAS:“-Aufgaben je Heft: 4 und 4** (2017: 2.1 Eisbecher, 2.2 Straßenverlauf, 3.1 Zelt, 4.2 Freizeit; 2018: 2.1 Vase, 2.2 Gartenteich, 3.1 Museum, 4.2 Brillenträger). Dazu beide Heftläufe „Alle Prüfungen bestanden.“, Selbstprüfung abi und iqb fehlerfrei, Lauf aus frischer Repo-Kopie byteidentisch.

Offen, mit Grund: **vier Pool-Vormerkungen nicht geschlossen** (2017-bb-ea-cas B3.1 c, e, f auf 2017MerhoehtBAGLAA2CAS2; 2018-bb-ea-cas B3.1 f auf 2018MerhoehtBAGLAA2CAS1). Die Regel „Eine Vormerkung überlebt keinen Auftrag“ ist damit in diesem Auftrag nicht eingelöst: die Poolaufgaben liegen in den CAS-Zweigen von 2017-ea-B und 2018-ea-B, die die Stapelliste nicht als Stapel führt (Delta-Stapel nach iqb.md, für 2017 zuerst der WTR-Stapel 2017-ea-B); der Auftrag sah diese Läufe nicht vor. Nebenbefund: den WTR-Zeilen 2017-bb-ea-B3.1 und 2018-bb-ea-B3.1 fehlt der Poolverweis, weil der frühere Pool-Abgleich nur WTR-Pooldateien durchsuchte. Beides als Posten in faellig.md § 2. Der Posten „CAS-Nachtrag 2017/2018“ bleibt für die vier Berliner Hefte in § 2.

Eigene Entscheidung: Erfassung durch einen Hilfsagenten (Opus) je Heft, nacheinander; Heftlauf, Selbstprüfung und Commit von mir geprüft.

## Teil 10: Stapel 2017-ga-A und 2017-ga-B, Heft 2017-be-gk, Abgleichlauf 24 (Commits 3981ec3, 5814acc, 25322c5, 6074aed)

Vor dem Heft der Poolabgleich: 2017-be-gk 3.1 (Smartphone) steht in 2017-ga-B (Stochastik WTR 1), aus 2017-ga-A nimmt das Heft nichts (kein hilfsmittelfreier Teil). Nach der Regel „Eine Vormerkung überlebt keinen Auftrag“ wurden beide Reserve-Stapel im selben Auftrag erfasst (eigene Commits, Abbruchkriterium unberührt), das Heft danach ohne Vormerkung.

| Einheit | Zeilen | neue Typen | „?“ | ersatzweise | Poolquote / Landesheftverweise | Eichung |
|---|---|---|---|---|---|---|
| Stapel 2017-ga-A (10 Dateien) | 20 | 7 (35 %) | 0 | 0 | 0 Landesheftverweise | 17 von 20 (85 %); erster Lauf 15 |
| Stapel 2017-ga-B WTR (5 Dateien) | 39 | 10 (26 %) | 0 | 0 | 6 „Dublette von“ aus 2017-be-gk, 1 abgewandelt | 34 von 39 (87 %); erster Lauf 23 (59 %) |
| Heft 2017-be-gk | 33 (beide Wahlwege, 160 BE angeboten) | 5 (12 %) | 0 | 0 | 6 von 33 Zeilen, 18 von 160 BE (11 %), dazu 1 abgewandelt (3.1 e, 2 BE) | 6 von 6 |

Punktprüfung Soll/Ist: 2017-ga-A 10 × 5 BE; 2017-ga-B 40, 20, 20, 20, 20; 2017-be-gk 40-40-20-20-20-20 – alle gleich.

Abgleichlauf 24 (`abitur-abgleich.py` v0.25): die 26 neuen Typen der fünf Läufe gegen alle Typen derselben Leitidee; 13 Umstellungen (9 Umbenennungen, 4 Zusammenziehungen), 34 abi- und 22 iqb-Zeilen, Typenliste 1349 → 1345. Liste alt → neu in abi-pruefungen.md und iqb-pruefungen.md § 5. Die alten Typnamen standen in elf Sek-II-Katalogeinträgen; dort mitgezogen (funktionsscharen-und-ortskurven Einheit 1: zwei Typen zu einem, Zählung 99 Haupttypen), themen.csv-Zählung (51 Profilzeilen), Rohdateien, `_pruefungswort-belege.md` und die Marken (rotationsvolumen) neu gebaut.

Gegenprobe im Wortlaut (abi-pruefungen.md § 2, iqb-pruefungen.md § 2): „2017-be-gk 80 BE über alle Aufgaben“ – erfüllt (Zeile „| 2017 | 2017-be-gk | BE | grundlegend | WTR | 8 | 210 | 80 |“; 80 BE je Wahlweg, 160 angeboten). „jeder Stapel vollständig laut iqb-quellen.csv (Skript prüft es)“ – erfüllt: iqb-bau.py schrieb beide Stapel erst nach der Vollständigkeitsprüfung (2017-ga-A 10 Dateien, 2017-ga-B WTR 5 Dateien), und die Selbstprüfung nach dem Abgleich meldet keinen unvollständigen Stapel. Dazu alle Läufe „Alle Prüfungen bestanden.“, Läufe aus frischer Repo-Kopie byteidentisch, `themen-pruef.py` und `pruefungswort-belege.py` bestanden.

Offen, mit Grund:
- **Eichung 2017-ga-B nicht unabhängig**: im ersten Lauf 59 %, unter der Schwelle; elf von sechzehn abweichenden eigenen Schätzungen wurden nach der engen Fassung und der Deutungsliste korrigiert (erste Schätzung und Grund je Zeile in `bemerkung`). Die Schwelle wurde nicht geändert. Posten „Eichung Pool 2017 grundlegend prüfen“ in faellig.md § 2 (Frage: liegt die I/II-Grenze des Pools 2017 anders; Deutungslisten-Zeile „Mindestanzahl für eine Mindestwahrscheinlichkeit = III“).
- **Sek-II-Einträge nicht nachgezogen**: die 120 neuen Zeilen (28 + 59 + 33) stehen in keinem Katalogeintrag; `_pruef_struktur.py` Kennzahl 5 steigt von 48 auf 168 von 3028, `_pruef_katalog.py` meldet für 31 Sek-II-Einträge „Zeilensumme ≠ themen.csv“. Das ist die Folge der Erfassung, kein Fehler der Einträge; Posten in faellig.md § 2.

Eigene Entscheidungen: Stapel, Heft und Abgleichlauf je durch einen Hilfsagenten (Opus), streng nacheinander (gleiche Dateien); Nachzug der Katalogeinträge nach dem Abgleich selbst. Der Eintrag des Abgleichlaufs in den Änderungslogs von abi-pruefungen.md und iqb-pruefungen.md trägt das Get-Date-Datum 2026-09-25, die übrigen Einträge des Auftrags das Auftragsdatum 27.09.2026 – im Commit 6074aed so geschrieben und nicht nachträglich geändert; hier vermerkt.

## Abschluss

faellig.md: zwölf Einträge in § 4 für die Teile 1–10, die vier Posten aus Teil 7 in § 2 mit „Vorschlag liegt vor, Entscheidung im Chat“, der Posten „270 Paare ohne Gegenrichtung“ nach § 4 („erledigt, kein Bedarf – Entscheidung des Lehrers 25.09.2026 …“), drei neue Posten (Pool-Vormerkungen der CAS-Nachträge, Eichung Pool 2017, Sek-II-Einträge nachziehen). Standdatei und Auftrag nach `archiv/` (keine Namensgleichheit), README ohne ihre Zeilen, mit der Zeile für diesen Bericht.

Allgemein: Get-Date zeigte während des ganzen Laufs den 25.09.2026 (15:47 bis 2026-09-25 18:53); Daten in Dateien und Einträgen tragen das Auftragsdatum 27.09.2026, Uhrzeiten in der Standdatei Get-Date. Nichts gelöscht, kein Push, kein Prompt und nichts unter blaetter/testlauf-*/ und ../blattbau geändert.

Push origin drücken
