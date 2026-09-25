Modell: Claude Opus 5.5 (claude-opus-5-5) in Claude Code

# Bericht zum Auftrag Marken (26.09.2026)

Auftrag: `archiv/auftrag-marken-2026-09-26.md`. Eingaben: `katalog/_marken-entscheidungen.md` (Datei 2), `katalog/_marken-neue-einheiten.md` (Datei 3), die drei Belegdateien. Neu: `werkzeuge/marken-bau.py`, `werkzeuge/marken-bau-stellen.txt`.

## Zahlen

- Einträge geändert: 72 von 73 (29 Sek I, 43 Sek II; `ableitungsgraph-und-funktionsgraph.md` hat keine Lerneinheiten). Datei 3 ist in `potenz-exponentialfunktionen.md` (Einheit 5 neu, Vorrat-Typ aus Einheit 1 entfernt) und `daten.md` (Einheit 7 neu, Einheit 1 um Klassen erweitert) eingearbeitet.
- Marken-Zeilen: 273 – 116 Sek-I-Einheiten (114 und die 2 neuen) und 157 Sek-II-Einheiten (155 in den 44 Sek-II-Einträgen, dazu daten 6 und lineare-gleichungssysteme 5). Jede Nummernzeile trägt genau eine Marken-Zeile. Der Auftrag erwartete 114 + 2 + 162 = 278; beide Zahlen: **278 erwartet, 273 gezählt**. Die 162 im Zahlenblock von `_pruefungswort-belege.md` zählen die acht Sek-I-Einheiten mit Sek-II-Zeilen (einheiten 1, 3, 4; lineare-gleichungssysteme 1, 3, 4; daten 1, 4) als Sek-II-Einheiten mit und lassen die drei Sek-II-Einheiten ohne Typ weg (integrationsregeln 1, uneigentliche-integrale 1, linearkombination-und-lineare-abhaengigkeit 1): 162 − 8 + 3 = 157.
- Typklammern: 262.
- Klammern „(Kl. n)“ entfernt: 78.
- Klammern stehen geblieben: 173 (36 in Sek-I-Einheiten, 137 in Sek-II-Einheiten), Liste am Schluss. Dazu 20 Endklammern ohne Klassen- oder Halbjahresangabe, unberührt (Liste am Schluss).
- Zeilen mit „nicht für alle“: 77.
- Stellenliste: 80 Zeilen für 53 Stellen – 38 Stellen aus Datei 2 (28 Tabellenzeilen), 15 im Lauf entschieden.
- Wirkung von Regel A und B gegenüber den Zusammenfassungen „OS:“/„GYM:“ in `_klassen-belege.md`: 20 Angaben in 18 Einheiten anders (Liste am Schluss).
- Wiederholbarkeit: ein zweiter Lauf meldet „nichts zu ändern“.

## Gegenproben

1. lineare-funktionen 4 – Soll „OS Kl. 8 · GYM Kl. 8 · P10 oft“. Ist „OS Kl. 8 · GYM Kl. 8 · P10 · nicht für alle: Mathematik 2023 8 Vertiefen“. **Abweichung beim Prüfungswort:** `_pruefungswort-belege.md` führt „Einheit 4 · Gleichung bestimmen“ mit 3 von 13 P10-Jahrgängen, unter der Schwelle 7.
2. quadratische-gleichungen 2 – Soll „OS Kl. 10 · GYM Kl. 9“. Ist „OS Kl. 10 · GYM Kl. 8–9 (LS 9, Fundamente 9, Elemente 8) · P10“. **Abweichung bei GYM:** Elemente Kl. 8 (Ausgabe 2016) „1.12 Gleichungen vom Typ T v T2 = 0“ ist der Satz vom Nullprodukt im Kapitel Terme, also der Kern der Einheit; der Ermessenstext trägt kein Stichwort der Regel A, Datei 2 nennt die Stelle nicht – sie zählt. OS Kl. 10 stimmt, weil „Sonderfälle“ nicht als Verlagsmarke gilt (Entscheidung 6); sonst stünde „OS –“.
3. prozentrechnung 1 – Soll „GYM Kl. 5“. Ist „OS Kl. 6 · GYM Kl. 5 · P10 oft · nicht für alle: Mathematik 2023 5 Vertiefen, Schnittpunkt 7 EXTRA“. Stimmt.
4. kreis 1 – Soll: weder OS noch GYM nennt Klasse 5 oder 6; Typ „Kreis mit gegebenem Radius oder Durchmesser zeichnen“ trägt „[OS 5, GYM 6]“. Ist „OS Kl. 7–8 (Sekundo 8, Mathematik 2023 7, Schnittpunkt 8, Mathematik heute 8) · GYM Kl. 7–8 (LS 8, Fundamente 8, Elemente 7, mathe.delta 7)“ – stimmt; Typ „[OS 5–8, GYM 5–6]“ – **Abweichung:** die Stellen, die ich nach Regel A wie Mathematik 2023 Kl. 5 gelesen habe, kommen in die Klammer: Mathematik heute Kl. 8 „Kreis - Kreisornamente“ (OS 8), Elemente Kl. 5 „5.4 Kreise“ (GYM 5), dazu LS 6 und Fundamente 6 und 7. Mehrere Reihen einer Schulform in verschiedenen Klassen ergeben nach dem Auftrag die Spanne.
5. potenz-exponentialfunktionen 5 – Soll „OS Kl. 10 · GYM Kl. 9 · keine P10-Aufgabe“. Ist „OS Kl. 10 · GYM Kl. 9 · keine P10-Aufgabe · nicht für alle: Sekundo 10 Zusatzstoff“. Stimmt.
6. daten 7 – Soll „keine P10-Aufgabe“. Ist „OS Kl. 9 · GYM Kl. 9–10 (LS 9, Fundamente 10, mathe.delta 10) · keine P10-Aufgabe“. Stimmt.
7. kurvenuntersuchung 1 – Soll „BE Q1 · BB Q1 · GK“. Ist „BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK“. Stimmt.
8. Zahl der Marken-Zeilen – Soll 278, Ist 273 (Zählweise des Zahlenblocks, siehe Zahlen).

Die Gegenprobe steht im Skript (`GEGENPROBE`) und wird bei jedem Lauf ausgegeben; weder Skript noch Stellenliste sind ihretwegen geändert.

## Regel A

Von 22 Stellen mit „Vorstufe“, „Einstieg“, „Wiederaufnahme“, „Zeichnen“ oder „Benennen“ im Ermessenstext (Suche ohne Rücksicht auf Groß- und Kleinschreibung) stehen 11 in Datei 2. Die übrigen 11 habe ich entschieden; das Skript bricht ab, wenn eine solche Stelle in der Stellenliste fehlt.

Als Vorstufe gelesen (werden Typzeile, setzen keine Klasse der Einheit):

| Eintrag | Einheit | Reihe | Zitat | Wirkung | Grund |
|---|---|---|---|---|---|
| kreis | 1 | Mathematik heute Kl. 8 | „Kreis - Kreisornamente“ | Typzeile an „Kreis mit gegebenem Radius oder Durchmesser zeichnen“ | Kreise mit dem Zirkel zeichnen vor „Umfang und Flächeninhalt eines Kreises“ (S. 115); Kern der Einheit ist der Umfang (Nummernzeile „Kreisumfang“) |
| kreis | 1 | LS Kl. 6 | „3 Kreise und Kreisfiguren“ | Typzeile an „Kreis mit gegebenem Radius oder Durchmesser zeichnen“ | wie Mathematik 2023 Kl. 5 „Kreise“ in Datei 2; der Umfang folgt Kl. 8 (Kapitel VI 5) |
| kreis | 1 | Fundamente Kl. 6 | „3.1 Kreis“ | Typzeilen an „Radius, Durchmesser, Mittelpunkt in einer Figur benennen und einzeichnen“ und „Kreis mit gegebenem Radius oder Durchmesser zeichnen“ | Zeichnen und Benennen wie Mathematik 2023 Kl. 5; der Umfang folgt Kl. 8 (7.3) |
| kreis | 1 | Fundamente Kl. 7 | „4.1 Kreis“ | Typzeile an „Kreis mit gegebenem Radius oder Durchmesser zeichnen“ | Kreis als Werkzeug im Kapitel Geometrische Konstruktionen; der Umfang folgt Kl. 8 |
| kreis | 1 | Elemente Kl. 5 (Ausgabe 2025) | „5.4 Kreise“ | Typzeilen an beiden Typen wie Fundamente Kl. 6 | Zeichnen und Benennen wie Mathematik 2023 Kl. 5; der Umfang folgt Kl. 7 (7.5) |

Als Kern gelesen (gelten, Entscheidung außerhalb von Datei 2):

| Eintrag | Einheit | Reihe | Zitat | Grund |
|---|---|---|---|---|
| koerper | 1 | Sekundo Kl. 7 | „Würfel- und Quadernetze“ | Netze stehen in der Nummernzeile („Körper erkennen, Netze, Schrägbilder“); die Typzeile am Würfelnetz-Typ bleibt |
| koerper | 1 | Mathematik 2023 Kl. 8 | „Eigenschaften eines Prismas“ | Körper erkennen und Flächen benennen ist Kern; ohne Wirkung, Mathematik 2023 führt die Einheit schon Kl. 5 |
| terme | 1 | Mathematik 2023 Kl. 8 | „Terme“ | Einstieg im Kapitel, gleiche Klasse wie seine Fortsetzung (wie lineare-gleichungen 2 in Datei 2); ohne Wirkung, Mathematik 2023 führt die Einheit schon Kl. 6 |
| quadratische-gleichungen | 1 | Sekundo Kl. 10 | „Quadratische Gleichungen“ | Einstieg im selben Kapitel, gleiche Klasse (wie lineare-gleichungen 2 und trigonometrische-funktionen 4 in Datei 2) |
| quadratische-gleichungen | 1 | Schnittpunkt Kl. 10 | „5 Quadratische Gleichungen“ | Einstieg im Kapitel; die Lösungsformel folgt S. 20 in derselben Klasse |
| quadratische-gleichungen | 1 | Mathematik heute Kl. 9 | „Quadratische Gleichungen“ | Einstieg im Kapitel; das rechnerische Lösen folgt S. 204 in derselben Klasse |

## Regel B

- Zeilen mit „nicht für alle“: 77.
- Beispiele:
  - kreis 1: „… · P10 · nicht für alle: Sekundo 8 LVL, Sekundo 9 Zusatzstoff, Sekundo 9 LVL, Mathematik 2023 7 Arbeiten mit dem Computer“ – die LVL-Seite „Messen und Entdecken am Kreis“ setzt Sekundo nicht, Sekundo führt den Umfang regulär in Kl. 8.
  - terme 1: „OS Kl. 6–7 (Mathematik 2023 6, Schnittpunkt 6, Mathematik heute 7) · GYM Kl. 6–7 (LS 6, Fundamente 7, Elemente 6) · P10 oft · nicht für alle: Fundamente 5 Streifzug“ – der Streifzug in Kl. 5 setzt die Gymnasialklasse nicht mehr (vorher GYM Kl. 5–6).
  - daten 1: „OS Kl. 5–6 (Mathematik 2023 5, Schnittpunkt 5, Mathematik heute 6) · GYM Kl. 5 · P10 · nicht für alle: Sekundo 7 LVL, Sekundo 8 LVL, Mathematik 2023 6 Üben“ – Sekundo 8 „LVL: Klasseneinteilung“ ist nach Datei 2 Typzeile an den neuen Klassen-Typen und steht deshalb hier.
- Verlagsmarken (Datei 2 und Markenwörter der Lesart von `_klassen-belege.md`): LVL, Streifzug, Vertiefen, Üben, EXTRA, Exkursion, Themenseite, Im Blickpunkt, Zusatzstoff „*“, fakultativ, Werkzeug, Mathematisch arbeiten, Mit Medien arbeiten, Arbeiten mit dem Computer, Projekt, Wissen kompakt, Bleib fit, Diagnosetest, Training, Vertiefung, Zum Selbstlernen, Sonderseite. Keine Marke: Wiederholung (Datei 2), unerklärte Symbolzeichen, „Sonderfälle“ (Entscheidung 6).

## Einheiten mit „OS –“ oder „GYM –“

- einheiten 4 (Mit Größen rechnen im Sachzusammenhang): „OS Kl. 8 · GYM – · P10 · nicht für alle: Sekundo 7 LVL, Mathematik 2023 8 Üben“ – keine Gymnasialreihe führt die Einheit (in `_klassen-belege.md` schon „Ohne GYM-Stelle“).
- Keine Einheit mit „OS –“.

## Was Datei 2 oder der Auftrag nicht regelte – so entschieden

1. **Datei 3, Form.** Die Zeilenumbrüche der Chatfassung sind zu einer Zeile je Einheit und je Typzeile zusammengezogen, die Anführungszeichen in der Form der Einträge („…“). daten Einheit 1: die Ergänzung „; Daten zu Klassen zusammenfassen … auszählen.“ steht am Ende des Inhalts, der Punkt nach „Gesamtzahl“ entfällt, weil die Ergänzung mit Strichpunkt beginnt und mit Punkt endet; „(Kl. 5–7)“ fiel danach im Markenlauf. Die vier Klassen-Typen stehen am Ende des Sek-I-Teils der Typzeile vor „— Sek II“, nicht hinter dem Sek-II-Teil: dort hätten die Werkzeuge (`typen_des_eintrags`) sie als didaktische Sek-II-Typen gelesen, Datei 2 nennt sie Sek I. „Einheit 7:“ steht zwischen „Einheit 6:“ und „Zählung:“.
2. **Zwei Textstellen außerhalb der genannten Stellen**, damit die Prüfskripte nicht brechen: in `daten.md` die Zählung um „+ 0“ für Einheit 7 (sonst meldet `_pruef_katalog.py` „ABWEICHUNG Haupttypen je Einheit“); in den Zuordnungszeilen unter „Prüfungsform (P10)“ „; Einheit 5 – kein P10-Typ (kein P10-Original)“ (`potenz-exponentialfunktionen.md`) und „; Einheit 7 – kein P10-Typ (kein P10-Original)“ (`daten.md`), sonst meldet `_pruef_struktur.py` „ZUORDNUNGSZEILE NENNT EINHEIT NICHT“. Wortlaut nach dem Muster „Einheit 6 – kein P10-Typ (…)“. Beides lässt sich zurücknehmen; dann melden die Skripte wieder.
3. **Reste der alten Lesart** in `potenz-exponentialfunktionen.md` (Nummernzeile Einheit 1 „Potenzfunktion als zweiter Funktionstyp … (Vorrat, H)“, Eingabe „potenzfunktion“ jetzt in Einheit 1 und 5, Zeile in `index.md`) und die fehlenden Abschnitte der neuen Einheiten (Merkkasten, Sprossen, Zielmarke, Blatt 0) sind nicht angefasst – je ein Posten in `faellig.md` § 2.
4. **themen.csv:** kein Eintrag. Die Datei führt je kanonischem Thema die Prüfungsthemen der Profile mit Zeilen- und Typenzahl, kein Stichwort je Einheit; die neuen Einheiten bringen kein Prüfungsthema (kein P10-Original, Datei 3). Die Eingabewörter stehen im Eintrag („← Eingabe …“).
5. **index.md und README.md:** die Zeilen von daten und potenz-exponentialfunktionen in `katalog/index.md` nennen keine Einheitenzahl – unverändert. `README.md` nannte „daten sechs“ – auf sieben gestellt, potenz-exponentialfunktionen fünf ergänzt.
6. **Markenwörter.** „Sonderfälle“ steht in der Markenliste der Lesart, ist aber an beiden Fundstellen (Sekundo 8 „Sonderfälle linearer Funktionen“, Sekundo 10 „Sonderfälle quadratischer Gleichungen“) Anfang eines Inhaltstitels, keine Seitenart – keine Marke. Unerklärte Symbolzeichen (Sekundo „M“, „W“, „•“ und andere, 26 Nennungen) sind kein Markenwort und ohne bekannte Bedeutung – keine Marke; sonst fielen reguläre Sekundo-Stellen weg (etwa „Exponentialfunktion“ Kl. 10). Das Zeichen „$“ bei Elemente, das die Belegdatei als „Symbol des Originals für Sonderseiten“ liest, gilt als Marke „Sonderseite“ (wie Themenseite). „Zum Selbstlernen“ ist Markenwort der Lesart und zählt nach Regel B als Marke.
7. **Marken nachgetragen.** Fünf Stellen beginnen mit einer Verlagsmarke, die die Marken-Zeile von `_klassen-belege.md` nicht führt, weil ein verstümmeltes Zeichen davorsteht oder ein Strichpunkt statt eines Doppelpunkts folgt („M LVL:“, „Q LVL:“, „O LVL:“, „Im Blickpunkt;“); das Skript erkennt und meldet sie (Liste am Schluss).
8. **Reihenliste.** Sie nennt nur die Reihen, die in die Spanne zählen, mit ihrer Einführungsklasse; Reihen ohne Stelle und Reihen, die nach der Lesart von `_klassen-belege.md` nicht zählen (Sekundo und mathe.delta mit Klasse 7, wenn eine andere Reihe derselben Schulform früher einführt), stehen nicht darin. Dieselbe Regel gilt in der Typklammer. Fundamente 2017 (Nebenquelle) und die Förderhefte zählen nirgends. Folge: wo Sekundos Kl.-7-Stelle eine Marke trägt, zählt seine nächste Stelle (potenzen-wurzeln 1: „OS Kl. 5–9 (Sekundo 9, …)“, Kl. 7 ist Zusatzstoff).
9. **Typklammer.** Typzeilen mit Verlagsmarke zählen mit (Datei 2 macht LVL- und Üben-Stellen ausdrücklich zu Typzeilen). Eine Schulform ohne Typzeile fehlt in der Klammer („[OS 7]“, nicht „[OS 7, GYM –]“). Steht ein Typ am Satzende, kommt die Klammer vor den Punkt.
10. **„nicht für alle“** nennt alle Stellen der Einheit mit Verlagsmarke, auch in späteren Klassen, dazu Stellen mit Marke, die nach der Stellenliste Typzeile an einem Typ der Einheit sind (einheiten 4 und koerper 5 „Mathematik 2023 8 Üben“, daten 1 „Sekundo 8 LVL“). Stellen „ohne Klasse“ (Vorstufe ohne Typ) stehen nicht darin (winkel-dreiecke 4 Sekundo 7 LVL; Datei 2 nennt dort nur „keine Klassenwirkung“). Form „<Reihe> <Klasse> <Marke>“, bei Elemente ohne Ausgabe; zwei Marken einer Stelle stehen als zwei Teile.
11. **Verschobene Stellen.** Zu den sieben Potenzfunktionen-Stellen aus Datei 2 kommt Fundamente Kl. 10 „1.2 Potenzfunktionen mit natürlichen Exponenten“ (Kapitel „Wiederholung aus Klasse 9“) nach Einheit 5. Zu den fünf Klasseneinteilungs-Stellen aus Datei 2 kommen Fundamente Kl. 7 „7.3 Klasseneinteilung und Histogramme“ und Elemente Kl. 7 „3.3 Klasseneinteilung bei Stichproben“ (2016) und „9.4 Klasseneinteilung von Stichproben“ (2025) als Typzeilen an die Klassen-Typen von daten 1 – dieselbe Sache, nur ohne Ermessenszeile und deshalb nicht in Datei 2. „Typzeile an den neuen Klassen-Typen“ heißt: an allen vier („[OS 8–9, GYM 6–7]“). Die sieben Typzeilen am entfernten Vorrat-Typ von potenz-exponentialfunktionen Einheit 1 entfallen; in Einheit 5 werden diese Stellen nicht Typzeile, weil sie die ganze Einheit nennen („Potenzfunktionen mit natürlichen Exponenten“), keinen einzelnen Typ.
12. **Prüfungswort der neuen Einheiten.** `_pruefungswort-belege.md` führt sie noch nicht; das Skript setzt „keine P10-Aufgabe“ nach Datei 3 („Kein P10-Original zu allen dreien“) und meldet es. Nach dem Neubau der Belegdatei gilt deren Zahl.
13. **Sek II ohne Typ.** integrationsregeln 1, uneigentliche-integrale 1, linearkombination-und-lineare-abhaengigkeit 1 („Einheit 1: kein Typ – …“) fehlen in `_pruefungswort-belege.md`: „keine Prüfungsaufgabe“.
14. **Sek II, Halbjahr und Kursart.** Halbjahr je Land aus der Zeile „Halbjahr:“ der Belegdatei, „Q1/Q2“ als „Q1/2“; die Bände von Bigalke/Köhler stehen nicht in der Marke. Kursart „GK“, wenn ein Land Grund- und Leistungskurs nennt; bei Länderunterschied (6 Einheiten) mit Zusatz „GK (BE nur LK)“ bzw. „GK (BB nur LK)“ – der Zusatz geht über die drei Wörter des Auftrags hinaus, trägt aber, dass ein Berliner bzw. Brandenburger Grundkurs die Einheit nicht hat. „FOS“ kommt nicht vor: jede Einheit mit FOS-Stelle hat auch eine Planstelle. Zwei Einheiten ohne Plan- und FOS-Stelle (gleichungen-loesen 4, matrizen-und-uebergangsprozesse 5) tragen „BE – · BB – · Kursart –“.
15. **Sek-I-Einheiten mit Sek-II-Zeilen** (einheiten 1, 3, 4; lineare-gleichungssysteme 1, 3, 4; daten 1, 4) tragen nur die Sek-I-Form; ihre FHR-Jahrgänge (daten 1 und 4: 7 von 8) stehen nicht in der Marke.
16. **Klammern.** „(Kl. n)“ entfällt nur, wenn die Endklammer genau „Kl. n“, „Kl. n/m“ oder „Kl. n–m“ enthält. Als „mit mehr Inhalt“ gilt eine Endklammer mit „Kl.“, „Klasse“ oder einem Halbjahr Q1–Q4; Endklammern ohne solche Angabe (20, etwa „(Pool AG/LA 1)“) sind keine Klassenklammern.
17. **Werkzeuge außerhalb des Auftrags.** `klassen-belege.py` und `pruefungswort-belege.py` (damit auch `blatt-pruef.py`) streifen die Klassenklammer beim Lesen eines Typnamens ab, je eine Zeile. Ohne das bräche `klassen-belege.py` beim nächsten Lauf an Typen mit Satzpunkt (reelle-zahlen 1 „Begründen (…)“), `pruefungswort-belege.py` meldete jeden Typ mit Klammer als „Wortlaut weicht ab“ und `blatt-pruef.py` zählte ihn als „ohne Treffer“. Nach der Änderung melden die Probeläufe nur noch die Folgen von Datei 3: `klassen-belege.py` sieben Fehler (Typzeilen am entfernten Vorrat-Typ), `pruefungswort-belege.py` zwei Prüffehler (Nummern in potenz-exponentialfunktionen Einheit 1), `blatt-pruef.py` die vier neuen Klassen-Typen als „ohne Treffer“ im Daten-Blatt. Die Umstellung der Zuordnungsdaten ist Posten in `faellig.md` § 2; die Belegdateien sind nicht neu gebaut. `sek2-ordnung-belege.py --probe`: unverändert.
18. **Abgeleitete Dateien.** `katalog/_verweise.md` ist mit dem Lauf von `verweis-pruef.py` neu geschrieben und mitcommittet; der Neubau zieht auch Unterschiede aus Commits vor diesem Auftrag nach (Stand-Zeile, Fundort von index.md, Name „Sinus- und Kosinussatz“ u. a.). `blaetter/kennzahlen.md` hat `blatt-pruef.py` beim Gegencheck überschrieben; zurückgesetzt, nicht committet.
19. **Datei 2 im Skript.** Das Skript liest aus Datei 2 die Verlagsmarken der Regel B, die Ausnahme Wiederholung, die Schwelle „7 von 13“ und die Tabelle der 38 Fälle (28 Zeilen; „sieben Stellen …“ zählt sieben) und bricht ab, wenn ein Fall nicht in der Stellenliste steht.

## Befunde der Prüfskripte

- `python werkzeuge/themen-pruef.py`: alle vier Prüfungen bestanden (158 Zeilen, 74 kanonische Themen, 73 Katalogdateien) – wie vor dem Auftrag.
- `python werkzeuge/verweis-pruef.py`: keine neuen Befunde. Prüfung 1: 2975 Verweise (vorher 2974; +1, daten Einheit 7 verweist auf vierfeldertafel.md), weiter 16 ohne Datei (5 Namen). Prüfung 2: 515 Angaben direkt hinter einem Verweis, weiter genau eine größer als vorhanden (lineare-gleichungssysteme.md, jetzt Zeile 122 statt 117 – bekannter Befund), 24 nicht eindeutig; 3861 Einheitenangaben insgesamt (vorher 3857: die Typzeilen „Einheit 5:“ und „Einheit 7:“ und die beiden Zuordnungsvermerke). Die Zeilennummern der Befunde sind um die eingefügten Marken-Zeilen verschoben. Prüfung 5: 0 von 73 Einträgen ohne Verweis in Blatt 0.
- Dazu, nicht verlangt: `katalog/_pruef_struktur.py` „Strukturprüfung: ok“, Kennzahlen 1–9 gleich dem Stand vor dem Auftrag; `katalog/_pruef_katalog.py` über alle 73 Einträge 71-mal „ok“ wie vorher (lineare-gleichungen.md und terme.md mit Befunden schon vorher).

## Listen

### Klassenklammern mit mehr Inhalt, stehen geblieben (173)

Sek-I-Einheiten (36):

- brueche-dezimalzahlen.md Z. 19 (Einheit 5): (Kl. 6–10, Prüfungsvorbereitung)
- zinsrechnung.md Z. 11 (Einheit 1): (Kl. 7 im Lehrwerk, Kl. 8 in der Planungshilfe; RLP F)
- zinsrechnung.md Z. 13 (Einheit 2): (Kl. 7 im Lehrwerk, Kl. 8 in der Planungshilfe; keine eigene RLP-Zeile)
- potenzen-wurzeln.md Z. 11 (Einheit 1): (Kl. 9; RLP F, negative Exponenten G; LISUM-PH führt sie in der Jg.-8-Reihe nur GYM, in der Jg.-9-Reihe für …)
- potenzen-wurzeln.md Z. 13 (Einheit 2): (Kl. 9; RLP F, negative Exponenten G, situationsangemessen H; LISUM-PH Jg.-8-Reihe „nur GYM“ für negative E …)
- potenzen-wurzeln.md Z. 15 (Einheit 3): (Kl. 8; RLP F, Näherungswerte G)
- reelle-zahlen.md Z. 11 (Einheit 1): (Kl. 8 im Lehrwerk, Kl. 9 in der Planungshilfe; RLP G, Einschachtelung H)
- reelle-zahlen.md Z. 13 (Einheit 2): (Kl. 9; RLP G)
- reelle-zahlen.md Z. 15 (Einheit 3): (Kl. 8 IV 4 und Kl. 9 III 6 im Lehrwerk; RLP H; LISUM-PH nur GYM)
- einheiten.md Z. 13 (Einheit 1): (Kl. 5 im Lehrwerk; RLP D, Vergleichen und Ordnen D/E; Sek II fhr „Größen und Einheiten“)
- einheiten.md Z. 15 (Einheit 2): (Kl. 5 im Lehrwerk; RLP B/C/D)
- einheiten.md Z. 17 (Einheit 3): (Kl. 5 im Lehrwerk; RLP D, Vorsätze F/G; Sek II fhr „Größen und Einheiten“)
- einheiten.md Z. 19 (Einheit 4): (Kl. 6–10; RLP E, berufsorientiert F; Sek II fhr „Größen und Einheiten“)
- pythagoras.md Z. 11 (Einheit 1): (Kl. 9; RLP E)
- pythagoras.md Z. 13 (Einheit 2): (Kl. 9; RLP E)
- trigonometrie.md Z. 11 (Einheit 1): (Kl. 10; RLP F)
- trigonometrie.md Z. 13 (Einheit 2): (Kl. 10; RLP F)
- trigonometrie.md Z. 15 (Einheit 3): (Kl. 10; RLP F „Zerlegung in rechtwinklige Teildreiecke“)
- trigonometrie.md Z. 17 (Einheit 4): (Kl. 10; RLP G)
- winkel-dreiecke.md Z. 11 (Einheit 1): (Kl. 6; Oberschule 7)
- winkel-dreiecke.md Z. 15 (Einheit 3): (Kl. 7; Vierecke Kl. 5)
- symmetrie-abbildungen.md Z. 11 (Einheit 1): (Kl. 5/6 im Lehrwerk; RLP D erster Quadrant, E vier Quadranten)
- symmetrie-abbildungen.md Z. 13 (Einheit 2): (Kl. 5 im Lehrwerk; RLP C/D, Dreiecksarten E)
- symmetrie-abbildungen.md Z. 15 (Einheit 3): (Kl. 5/6 im Lehrwerk; RLP C/D)
- strahlensaetze.md Z. 11 (Einheit 1): (Kl. 5 im Lehrwerk; RLP E = Kl. 7 Gymnasium, 7–8 Oberschule; Rasterpapier C)
- strahlensaetze.md Z. 13 (Einheit 2): (Kl. 9; RLP E, Modellbau G)
- strahlensaetze.md Z. 15 (Einheit 3): (Kl. 9; nicht im RLP 1–10, Lehrwerk IV 3)
- terme.md Z. 15 (Einheit 4): (Kl. 7/8; Terme mit mehreren Variablen und Klammer mal Klammer → binomische-formeln.md Einheit 1)
- quadratische-funktionen.md Z. 15 (Einheit 3): (Kl. 9; bis 11g Kl. 9/10, siehe Verortung)
- quadratische-funktionen.md Z. 17 (Einheit 4): (Kl. 9, nach quadratische-gleichungen.md)
- quadratische-gleichungen.md Z. 20 (Einheit 4): (Kl. 9/10; Vorrat, kein P10-Original)
- trigonometrische-funktionen.md Z. 11 (Einheit 1): (Kl. 10; RLP H für das Bogenmaß, Einheitskreis als Zugang zu G)
- trigonometrische-funktionen.md Z. 13 (Einheit 2): (Kl. 10; RLP G)
- trigonometrische-funktionen.md Z. 15 (Einheit 3): (Kl. 10; RLP G für a und b, H für c und d)
- trigonometrische-funktionen.md Z. 17 (Einheit 4): (Kl. 10; RLP G)
- wahrscheinlichkeit.md Z. 11 (Einheit 1): (Kl. 5–8; Grundschulstoff, für die Oberschule 7–8 regulär)

Sek-II-Einheiten (137):

- lineare-gleichungssysteme.md Z. 22 (Einheit 5): (GOST Q1 L1 „Gauß-Verfahren“, „Lösbarkeit“, Q3 „bis zu drei Variablen“; OHiMi 2.1 „Lösbarkeit und Lösungsme …)
- daten.md Z. 24 (Einheit 6): (FOS Pflichtthema 4 „Beschreibende Statistik“; GOST Q2 „Lage- und Streumaße einer Stichprobe“; RLP H „Streu …)
- kurvenuntersuchung.md Z. 11 (Einheit 1): (Q1, GK-Kern; FOS „Monotonie und 1. Ableitung“)
- kurvenuntersuchung.md Z. 13 (Einheit 2): (Q1, GK-Kern; FOS „lokale Extrempunkte“, „Sattelpunkte“)
- kurvenuntersuchung.md Z. 15 (Einheit 3): (Q1, GK-Kern; FOS „Krümmung und 2. Ableitung“, „Wendepunkte und Sattelpunkte“)
- kurvenuntersuchung.md Z. 17 (Einheit 4): (Q1, GK-Kern „den Ableitungsgraphen aus dem Funktionsgraphen entwickeln“; FOS nur „grafische Darstellung“ u …)
- kurvenuntersuchung.md Z. 19 (Einheit 5): (Q1, GK-Kern „lokale Änderungsrate auch in Sachzusammenhängen“, „Randextrema“; FOS „Modellierung von Verläu …)
- binomialverteilung.md Z. 11 (Einheit 1): (Q2, GK-Kern; OHiMi 2.4 „Ansätze zur Berechnung“)
- binomialverteilung.md Z. 13 (Einheit 2): (Q2, GK-Kern; OHiMi 2.4 Bernoulli-Formel auswendig)
- binomialverteilung.md Z. 15 (Einheit 3): (Q2, GK-Kern „Punkt- und Intervallwahrscheinlichkeiten“, „kumulative Darstellungen“; Teil B mit Rechner)
- binomialverteilung.md Z. 17 (Einheit 4): (Q2, GK-Kern; LS-AA „Problemlösen mit der Binomialverteilung“; Landeshefte mit Logarithmus, Pool mit Probie …)
- binomialverteilung.md Z. 19 (Einheit 5): (Q2, GK-Kern „Binomialverteilung im Histogramm, auch kumulative Darstellungen“, „Eigenschaften auf der Grun …)
- ebenen.md Z. 11 (Einheit 1): (Q3, GK-Kern „Spannvektoren“, „Parameterform“; OHiMi 2.3 „Ebenen: Parameterform“)
- ebenen.md Z. 13 (Einheit 2): (Q3, GK-Kern „Normalenvektor“, „Koordinatenform“, „Normalenform“, „Zusammenhang zwischen Parameter-, Normal …)
- ebenen.md Z. 15 (Einheit 3): (Q3, GK-Kern „Darstellung von ... Ebenen ... in dreidimensionalen kartesischen Koordinatensystemen“; OHiMi  …)
- ebenen.md Z. 17 (Einheit 4): (Q3, GK-Kern „Lagebeziehungen zwischen: ... Ebenen“; OHiMi 2.3 „Lagebeziehungen zwischen Punkten, Geraden u …)
- ableitung-und-aenderungsrate.md Z. 11 (Einheit 1): (Q1, GK-Kern „Differenzenquotient“, „mittlere Steigung einer Kurve in einem Intervall“; FOS „mittlere Änder …)
- ableitung-und-aenderungsrate.md Z. 13 (Einheit 2): (Q1, GK-Kern „Ableitung einer Funktion an einer Stelle“, „lokale Änderungsrate und Anstieg der Tangente“, „ …)
- ableitung-und-aenderungsrate.md Z. 15 (Einheit 3): (Q1, GK-Kern „Zusammenhang zwischen mittlerer bzw. lokaler Änderungsrate und Differenzenquotient bzw. Diffe …)
- ableitung-und-aenderungsrate.md Z. 17 (Einheit 4): (Q1, GK-Kern „Ableitungsfunktion auch in Sachzusammenhängen“, „Änderungsrate im Sachzusammenhang“; FOS „Mod …)
- ableitungsregeln.md Z. 11 (Einheit 1): (Q1, GK-Kern „Konstanten-, Potenz-, Faktor-, Summenregel“; FOS „Ableitungsregeln: Konstanten-, Faktor-, Sum …)
- ableitungsregeln.md Z. 13 (Einheit 2): (Q1, GK-Kern „Kettenregel mit linearer bzw. quadratischer innerer Funktion“, „Verkettungen von ganzrational …)
- ableitungsregeln.md Z. 15 (Einheit 3): (Q1, GK-Kern „Produktregel“, „multiplikative Verknüpfungen zweier Funktionen“; OHiMi 2.2 „Produktregel“; FO …)
- grenzwerte-und-verhalten-im-unendlichen.md Z. 11 (Einheit 1): (Q1, GK-Kern „Verhalten im Unendlichen“, „Axialsymmetrie bzgl. der Ordinatenachse“; FOS „Verhalten im Unend …)
- grenzwerte-und-verhalten-im-unendlichen.md Z. 13 (Einheit 2): (Q1, GK-Kern „Grenzwertverhalten von Funktionsgraphen (x → ±∞)“, „Verhalten im Unendlichen“, „Nullstellen“, …)
- grenzwerte-und-verhalten-im-unendlichen.md Z. 15 (Einheit 3): (Q1, GK-Kern „Grenzwertverhalten“, „Monotonie“, „Nullstellen“; OHiMi 2.2 „Zusammenhang zwischen Funktionsgr …)
- gleichungen-loesen.md Z. 11 (Einheit 1): (Q1, GK-Kern „lineare, allgemeine quadratische und biquadratische Gleichungen sowie Gleichungen höheren Gra …)
- gleichungen-loesen.md Z. 13 (Einheit 2): (Q1, GK-Kern „natürliche Exponentialgleichungen (natürlicher Logarithmus und Logarithmengesetze)“; OHiMi 2. …)
- gleichungen-loesen.md Z. 15 (Einheit 3): (Q1, GK-Kern „Änderungsrate im Sachzusammenhang“, „Nullstellen“; OHiMi 2.1 „einfache Bruchgleichungen“; LK  …)
- gleichungen-loesen.md Z. 17 (Einheit 4): (Q1, GK-Kern „Funktionseigenschaften“ als Herkunft; OHiMi 2.1 „Gleichungen durch Faktorisieren lösen“, „ein …)
- umkehrfunktion.md Z. 11 (Einheit 1): (Eingangsvoraussetzung L4; Q2 LK „ln als Umkehrfunktion der e-Funktion“; OHiMi 2.2 „Zusammenhang zwischen F …)
- umkehrfunktion.md Z. 13 (Einheit 2): (OHiMi 2.2 „Zusammenhang zwischen Funktion und Umkehrfunktion“; Q1 LK-Klassen; Pool erhöht 2025–2026)
- tangente-normale-schnittwinkel.md Z. 11 (Einheit 1): (Q1, GK-Kern „Gleichung der Tangente in einem Punkt des Funktionsgraphen“; FOS „Tangentenanstieg“, „Bestimm …)
- tangente-normale-schnittwinkel.md Z. 13 (Einheit 2): (Q1, GK-Kern; FOS „Bestimmung einer Tangentengleichung“ nur als Grundform; OHiMi 2.2 „Gleichungen von Sekan …)
- tangente-normale-schnittwinkel.md Z. 15 (Einheit 3): (Q1, GK-Kern „Tangenten- und Normalengleichungen“; FOS „Bestimmung … einer Normalengleichung“; OHiMi 2.2 „G …)
- tangente-normale-schnittwinkel.md Z. 17 (Einheit 4): (Q1, GK-Kern „Schnittwinkel zwischen Funktionsgraphen“ – im Plan, nicht in der Anlage; kein FOS-Stoff)
- tangente-normale-schnittwinkel.md Z. 19 (Einheit 5): (Q1, GK-Kern; Sek-I-Geometrie als Werkzeug; fhr nur die Dreiecksfläche an einer Geraden)
- extremalprobleme.md Z. 11 (Einheit 1): (Q1, GK-Kern; FOS „Umfang und Flächeninhalt ebener Figuren in Zusammenhang mit Funktionsgraphen“)
- extremalprobleme.md Z. 13 (Einheit 2): (Q1, GK-Kern „Extremalprobleme“; FOS „Ermitteln der Zielfunktion“)
- extremalprobleme.md Z. 15 (Einheit 3): (Q1, GK-Kern „Extremalprobleme“, „Randextrema“; FOS „Untersuchung auf lokale Extrema“)
- funktionsklassen-und-eigenschaften.md Z. 11 (Einheit 1): (Q1, GK-Kern „Funktionseigenschaften, auch in Anwendungszusammenhängen“; FOS „Funktionsbegriff“, „Achsensch …)
- funktionsklassen-und-eigenschaften.md Z. 13 (Einheit 2): (Q1, GK-Kern „Nullstellen“, „Schnittpunkte mit den Koordinatenachsen“; FOS „Lösungsverfahren ganzrationaler …)
- funktionsklassen-und-eigenschaften.md Z. 15 (Einheit 3): (Q1, GK-Kern „Definitions- und Wertebereich“; LK-Zusatz ln als Funktionsklasse; FOS „Funktionsbegriff“ mit  …)
- funktionsklassen-und-eigenschaften.md Z. 17 (Einheit 4): (Q1, GK-Kern „Punktsymmetrie bzgl. des Koordinatenursprungs und Axialsymmetrie bzgl. der Ordinatenachse“; F …)
- funktionsklassen-und-eigenschaften.md Z. 19 (Einheit 5): (Q1, GK-Kern „Sinus- und Kosinusfunktionen: Einfluss der Parameter auf den Verlauf der Funktionsgraphen“; O …)
- funktionsklassen-und-eigenschaften.md Z. 21 (Einheit 6): (Q1, GK-Kern „Funktionseigenschaften“; FOS „Wertetabelle, Darstellung der Funktionsgraphen“; OHiMi 2.2 „qua …)
- funktionsscharen-und-ortskurven.md Z. 11 (Einheit 1): (Q1 LK „Funktionsscharen mit einem Parameter“; Pool prüft auch grundlegend)
- funktionsscharen-und-ortskurven.md Z. 13 (Einheit 2): (Q1 LK; L4)
- funktionsscharen-und-ortskurven.md Z. 15 (Einheit 3): (Q1 LK; Kriterien aus kurvenuntersuchung.md)
- funktionsscharen-und-ortskurven.md Z. 19 (Einheit 5): (Q1 LK „Ortskurven von Extrem- und Wendepunkten“)
- stammfunktion-und-hauptsatz.md Z. 11 (Einheit 1): (Q2 GK-Kern „Integrieren als Umkehrung des Differenzierens“; OHiMi „Stammfunktionen elementarer Funktionen“)
- stammfunktion-und-hauptsatz.md Z. 13 (Einheit 2): (Q2 GK-Kern „Hauptsatz der Differential- und Integralrechnung“, „Integrale von Funktionen mittels Stammfunk …)
- stammfunktion-und-hauptsatz.md Z. 15 (Einheit 3): (Q2 GK-Kern „Zusammenhang zwischen den Funktionsgraphen der Funktion, der Ableitungsfunktion und der Stammf …)
- integrationsregeln.md Z. 11 (Einheit 1): (Q2 GK-Kern; OHiMi „Integrationsregeln“)
- flaecheninhalt-durch-integration.md Z. 11 (Einheit 1): (Q2 GK-Kern L2; FOS „Fläche zwischen dem Graphen einer Funktion und der x-Achse“, „Orientierung von Flächen …)
- flaecheninhalt-durch-integration.md Z. 13 (Einheit 2): (Q2 GK-Kern L2 „von Funktionsgraphen … begrenzt“; FOS „Fläche zwischen zwei Funktionsgraphen“)
- flaecheninhalt-durch-integration.md Z. 17 (Einheit 4): (Q2 GK-Kern L2 „auch in Anwendungszusammenhängen“; Teil-A-Belege, siehe Kasten)
- rekonstruktion-von-bestaenden.md Z. 11 (Einheit 1): (Q2 GK-Kern L2 „Bestände aus Änderungsraten und Anfangsbestand berechnen“)
- rekonstruktion-von-bestaenden.md Z. 13 (Einheit 2): (Q2 GK-Kern L4 „das bestimmte Integral deuten, insbesondere als (re-)konstruierten Bestand“)
- rekonstruktion-von-bestaenden.md Z. 15 (Einheit 3): (Q2 GK-Kern L4; Bildarbeit des Pools)
- uneigentliche-integrale.md Z. 11 (Einheit 1): (Q2 LK „Inhalte unbegrenzter Flächen mittels uneigentlicher Integrale“)
- punkte-und-strecken-im-koordinatensystem.md Z. 11 (Einheit 1): (Q3, GK-Kern „geometrische Sachverhalte … koordinatisieren und im Koordinatensystem darstellen“; OHiMi 2.3  …)
- punkte-und-strecken-im-koordinatensystem.md Z. 13 (Einheit 2): (Q3, GK-Kern L2 „Betrag eines Vektors bzw. Länge einer Strecke“, „Mittelpunkt einer Strecke“, „Abstände zwi …)
- punkte-und-strecken-im-koordinatensystem.md Z. 15 (Einheit 3): (Q3, Eingangsvoraussetzung L3 „Eigenschaften von Figuren … Satz des Thales und Satz des Pythagoras“; GK-Ker …)
- punkte-und-strecken-im-koordinatensystem.md Z. 17 (Einheit 4): (Q3, GK-Kern L3 „Beschreibung geometrischer Objekte mittels Vektoren“, „Flächeninhalte von geometrischen Ob …)
- punkte-und-strecken-im-koordinatensystem.md Z. 19 (Einheit 5): (Q3, GK-Kern „Darstellung von … Körpern in … dreidimensionalen kartesischen Koordinatensystemen“; OHiMi 2.3)
- vektoren-und-rechenoperationen.md Z. 11 (Einheit 1): (Q3, GK-Kern „Vektorbegriff (Verschiebung, Pfeilklasse)“, „Koordinatendarstellung“, „Betrag eines Vektors“; …)
- vektoren-und-rechenoperationen.md Z. 13 (Einheit 2): (Q3, GK-Kern „Vektoraddition“, „Multiplikation eines Vektors mit einer reellen Zahl“, „Darstellung von Vekt …)
- vektoren-und-rechenoperationen.md Z. 15 (Einheit 3): (Q3, GK-Kern L1 „Tupel in Form von Punkten und Vektoren angeben“; das Skalarprodukt als Operation aus der L …)
- linearkombination-und-lineare-abhaengigkeit.md Z. 11 (Einheit 1): (Q3, GK-Kern „lineare Abhängigkeit und lineare Unabhängigkeit von Vektoren“; OHiMi 2.3 „Untersuchung von Ve …)
- linearkombination-und-lineare-abhaengigkeit.md Z. 13 (Einheit 2): (Q3, GK-Kern „Darstellung von Vektoren als Linearkombinationen anderer Vektoren“; die Deutung als Strecke i …)
- geraden.md Z. 11 (Einheit 1): (Q3, GK-Kern „Richtungsvektor“, „analytische Beschreibung von Geraden …: Parameterform“; OHiMi 2.3 „Geraden …)
- geraden.md Z. 13 (Einheit 2): (Q3, GK-Kern „Lagebeziehungen zwischen: Punkt und Gerade“; OHiMi 2.3 „Lagebeziehungen …“, „Betrag eines Vek …)
- geraden.md Z. 15 (Einheit 3): (Q3, GK-Kern „Lagebeziehungen zwischen: … Geraden“; OHiMi 2.3)
- geraden.md Z. 17 (Einheit 4): (Q3, GK-Kern L2/L3; die Prüfungsform trägt Teil B mit Maßstab „1 LE = …“)
- lagebeziehungen.md Z. 11 (Einheit 1): (Q3, GK-Kern „Lagebeziehungen zwischen: … Punkt und Ebene“; OHiMi 2.3 „Lagebeziehungen …“)
- lagebeziehungen.md Z. 13 (Einheit 2): (Q3, GK-Kern „Lagebeziehungen …“ rückwärts gelesen; Teil-A-Praxis des Pools)
- lagebeziehungen.md Z. 15 (Einheit 3): (Q3, GK-Kern „Lagebeziehungen zwischen: … Gerade und Ebene“; LK „auch Scharen“)
- lagebeziehungen.md Z. 17 (Einheit 4): (Q3, GK-Kern; die Prüfungsform trägt Teil B mit Maßstab und Bereichsprüfung)
- schnittmengen.md Z. 11 (Einheit 1): (Q3, GK-Kern „Schnittmenge: … einer Geraden und einer Ebene“; IQB-VER 3.2 zu den vorausgesetzten Fällen)
- schnittmengen.md Z. 13 (Einheit 2): (Q3, GK-Kern „Schnittmenge: zweier Geraden“; L1 „Bestimmung von Schnittmengen“)
- schnittmengen.md Z. 15 (Einheit 3): (Q3, GK-Kern „Darstellung …“; LK „Schnittmenge zweier Ebenen“)
- skalarprodukt-und-winkel.md Z. 11 (Einheit 1): (Q3, GK-Kern „das Skalarprodukt geometrisch deuten“; OHiMi 2.3 „Skalarprodukt in Koordinatenform und koordi …)
- skalarprodukt-und-winkel.md Z. 13 (Einheit 2): (Q3, GK-Kern L2 „Winkel zwischen Geraden“, L3 „Winkel zwischen zwei Vektoren“; OHiMi 2.3 „Ansätze zur Winke …)
- skalarprodukt-und-winkel.md Z. 15 (Einheit 3): (Q3, GK-Kern L2 „Winkel zwischen … Ebenen und Ebenen“; OHiMi 2.3 „Ansätze zur Winkelberechnung“)
- skalarprodukt-und-winkel.md Z. 17 (Einheit 4): (Q3, GK-Kern L2 „Winkel zwischen Geraden … und Ebenen“; OHiMi 2.3 „Ansätze zur Winkelberechnung“)
- orthogonalitaet.md Z. 11 (Einheit 1): (Q3, GK-Kern „Orthogonalität von Vektoren“; OHiMi 2.3)
- orthogonalitaet.md Z. 13 (Einheit 2): (Q3, GK-Kern „Orthogonalität von Vektoren“ rückwärts gelesen; OHiMi 2.3)
- orthogonalitaet.md Z. 15 (Einheit 3): (Q3, GK-Kern „Orthogonalität von Geraden, Ebenen, Geraden und Ebenen“; OHiMi 2.3)
- orthogonalitaet.md Z. 17 (Einheit 4): (Q3, GK-Kern; Eingangsvoraussetzung L3 „Ähnlichkeit“ für die Lotfiguren)
- abstaende.md Z. 11 (Einheit 1): (Q3, GK-Kern „Punkt – Punkt“; OHiMi 2.3 „Betrag eines Vektors“)
- abstaende.md Z. 13 (Einheit 2): (Q3, GK-Kern „Punkt – Ebene“; OHiMi 2.3 „Hessesche Normalenform“)
- abstaende.md Z. 15 (Einheit 3): (Q3, LK-Zusatz „Punkt – Gerade“; der Pool prüft auch grundlegend, siehe Befund Niveaustufung)
- abstaende.md Z. 17 (Einheit 4): (Q3, GK-Kern „Gerade – Ebene“, „Ebene – Ebene“; Eingangsvoraussetzung L3 Pythagoras, Thales, Ähnlichkeit)
- spiegelung.md Z. 11 (Einheit 1): (Q3; [IQB-VER 3.2] grundlegend „für Punkte“)
- spiegelung.md Z. 13 (Einheit 2): (Q3; [IQB-VER 3.2] erhöht „uneingeschränkt“)
- spiegelung.md Z. 15 (Einheit 3): (Q3; Eingangsvoraussetzung L3 „Symmetrie“ als Figureigenschaft)
- scharen-von-geraden-und-ebenen.md Z. 11 (Einheit 1): (Q3 LK „Scharen“)
- scharen-von-geraden-und-ebenen.md Z. 13 (Einheit 2): (Q3 LK; Paarregeln aus orthogonalitaet.md mit Parameter)
- scharen-von-geraden-und-ebenen.md Z. 15 (Einheit 3): (Q3 LK; Formeln aus skalarprodukt-und-winkel.md und abstaende.md)
- scharen-von-geraden-und-ebenen.md Z. 17 (Einheit 4): (Q3 LK; Körperarbeit in Teil B)
- flaecheninhalt-und-volumen-im-raum.md Z. 11 (Einheit 1): (Q3, GK-Kern „Flächeninhalte von geometrischen Objekten“; OHiMi 2.3 „Flächenberechnung: Dreieck“)
- flaecheninhalt-und-volumen-im-raum.md Z. 13 (Einheit 2): (Q3, GK-Kern; OHiMi 2.3 „Rechteck“; Trapez- und Rautenformel in FS-IQB 1.1)
- flaecheninhalt-und-volumen-im-raum.md Z. 15 (Einheit 3): (Q3; OHiMi 2.3 „Volumenberechnung: Pyramide, Prisma“; Eingangsvoraussetzung L3)
- flaecheninhalt-und-volumen-im-raum.md Z. 17 (Einheit 4): (Q3; Eingangsvoraussetzung L3 „Cavalieri“, „Ähnlichkeit“; Prüfungshöhe)
- vierfeldertafel.md Z. 11 (Einheit 1): (Q2, GK-Kern „Vierfeldertafel“; OHiMi 2.4)
- vierfeldertafel.md Z. 13 (Einheit 2): (Q2, GK-Kern; OHiMi 2.4 „Additionssatz“)
- bedingte-wahrscheinlichkeit-und-bayes.md Z. 11 (Einheit 1): (Q2, GK-Kern „bedingte Wahrscheinlichkeit“; OHiMi 2.4 Quotient)
- bedingte-wahrscheinlichkeit-und-bayes.md Z. 13 (Einheit 2): (Q2, GK-Kern „Satz von der totalen Wahrscheinlichkeit“, „Satz von Bayes“ – nur Brandenburg nennt die Namen)
- bedingte-wahrscheinlichkeit-und-bayes.md Z. 15 (Einheit 3): (Q2; Prüfungshöhe des Pools)
- unabhaengigkeit.md Z. 11 (Einheit 1): (Q2, GK-Kern; OHiMi 2.4 „stochastische Unabhängigkeit“; FOS Pflichtthema 4)
- unabhaengigkeit.md Z. 13 (Einheit 2): (Q2; Prüfungshöhe)
- unabhaengigkeit.md Z. 15 (Einheit 3): (Q2; BE Kap. 4 „inhaltliches Verständnis“)
- zufallsgroessen-und-verteilungen.md Z. 11 (Einheit 1): (Q2, GK-Kern „Zufallsgrößen als Zuordnung“, „Verteilung in Tabellen“)
- zufallsgroessen-und-verteilungen.md Z. 13 (Einheit 2): (Q2, GK-Kern „Verteilung in … Diagrammen“; OHiMi 2.4 Histogramme)
- hypergeometrische-verteilung.md Z. 11 (Einheit 1): (Q2, GK-Kern „Ziehen ohne Zurücklegen“; OHiMi 2.4 „Ansätze“; IQB-VER 4 vorausgesetzt)
- hypergeometrische-verteilung.md Z. 13 (Einheit 2): (Q2; Prüfungshöhe)
- kenngroessen-von-verteilungen.md Z. 11 (Einheit 1): (Q2 BB, GK-Kern; OHiMi 2.4 „Erwartungswert von Zufallsgrößen“; FOS Pflichtthema 4)
- kenngroessen-von-verteilungen.md Z. 13 (Einheit 2): (Q2 BB; Prüfungshöhe des Pools in Teil A, jährlich)
- kenngroessen-von-verteilungen.md Z. 15 (Einheit 3): (BB Q2 GK-Kern, BE Q4 GK binomial bzw. LK allgemein; [IQB-VER 4] vorausgesetzt)
- normalverteilung-und-sigma-regeln.md Z. 11 (Einheit 1): (Q4 LK; OHiMi-LK „Interpretationen von Darstellungen“; Teil-A-Stoff)
- normalverteilung-und-sigma-regeln.md Z. 13 (Einheit 2): (Q4 LK; FS-IQB Abschnitt „Sigma-Regeln“)
- normalverteilung-und-sigma-regeln.md Z. 15 (Einheit 3): (Q4 LK; Prüfungshöhe des Pools in Teil B)
- hypothesentests.md Z. 11 (Einheit 1): (Q4 LK; Prüfform jedes Testjahrs)
- hypothesentests.md Z. 13 (Einheit 2): (Q4 LK; BE Kap. 4 „kein sicheres Urteil“)
- hypothesentests.md Z. 15 (Einheit 3): (Q4 LK; Prüfungshöhe)
- zufallsexperimente-und-pfadregeln.md Z. 12 (Einheit 1): (Q2, GK-Kern „Grundbegriffe der Mengenlehre“; OHiMi 2.4 Additionssatz; FOS „elementare Begriffe“)
- zufallsexperimente-und-pfadregeln.md Z. 14 (Einheit 2): (Q2; OHiMi 2.4 Laplace-Formel; FOS „Laplace-Experiment“ – die fhr-Zeilen als Zutat ohne Schwerpunktmarkierung)
- zufallsexperimente-und-pfadregeln.md Z. 16 (Einheit 3): (Q2, GK-Kern „zwei- und dreistufige Zufallsexperimente“; OHiMi 2.4 „Baumdiagramm, Pfadregeln“; FOS „mehrstu …)
- zufallsexperimente-und-pfadregeln.md Z. 18 (Einheit 4): (Q2, GK-Kern „Ziehen ohne Zurücklegen“; OHiMi 2.4 Pfadregeln; FOS – die punktreichste fhr-Form)
- zufallsexperimente-und-pfadregeln.md Z. 20 (Einheit 5): (Q2, GK-Kern „kombinatorische Abzählverfahren“; OHiMi 2.4 Kombinatorik; IQB-VER 4 Ziehen ohne Zurücklegen m …)
- zufallsexperimente-und-pfadregeln.md Z. 22 (Einheit 6): (Q2, GK-Kern „Baumdiagramm und Pfadregeln“, „Satz von der totalen Wahrscheinlichkeit“; Vorstufe von Vierfel …)
- zufallsexperimente-und-pfadregeln.md Z. 24 (Einheit 7): (Q2; die Teil-A-Prüfform des Pools – siebzehn der einundzwanzig Zeilen des Haupttyps hilfsmittelfrei)
- zufallsexperimente-und-pfadregeln.md Z. 26 (Einheit 8): (Q2; Prüfungshöhe beider Abiturprofile, jährlich in Teil A und B)
- kombinatorik.md Z. 11 (Einheit 1): (Q2, GK-Kern „kombinatorische Abzählverfahren“; OHiMi 2.4 n! und n^k; FOS „Permutationen, Variationen“)
- kombinatorik.md Z. 13 (Einheit 2): (Q2, GK-Kern; OHiMi 2.4 „Kombinationen ohne Wiederholung“ mit Eigenschaften; FOS „Kombinationen“; FS-IQB 1.4)
- kombinatorik.md Z. 15 (Einheit 3): (Q2; die Prüfform des Pools – sieben der neun Zeilen hilfsmittelfrei, fünf im Anforderungsbereich III)

### Endklammern ohne Klassen- oder Halbjahresangabe, unberührt (20)

- funktionsscharen-und-ortskurven.md Z. 17 (Einheit 4): (LK-Zusatz Integralrechnung „Bestimmung von Scharparametern … bei gegebenem Volumen oder Flächeninhalt“)
- rekonstruktion-von-funktionsgleichungen.md Z. 11 (Einheit 1): (GK-Kern „Rekonstruktion von Funktionsgleichungen“; FOS Pflichtthema 1 und 2; OHiMi 2.2 „aus graphischen Da …)
- rekonstruktion-von-funktionsgleichungen.md Z. 13 (Einheit 2): (GK-Kern; FOS „Symmetrie, Anstieg, Extrem-, Wende- und Sattelstellen“; OHiMi 2.2 „aus Funktionseigenschaften“)
- rekonstruktion-von-funktionsgleichungen.md Z. 15 (Einheit 3): (LK-Funktionsklassen sin/cos und ln als Ansätze; GK-Kern sin/cos-Parameter als Beschreibungsmittel)
- stammfunktion-und-hauptsatz.md Z. 17 (Einheit 4): (im Plan nicht benannt – Poolpraxis auf der Grundlage von Hauptsatz und Graphenzusammenhang, siehe Offene P …)
- integrationsregeln.md Z. 13 (Einheit 2): (kein Planinhalt – Prüfungsform des Pools, die Regel wird vorgegeben; beide Zeilen erhöht)
- flaecheninhalt-durch-integration.md Z. 15 (Einheit 3): (FOS „Grund-, Querschnitts- und Deckflächen von Körpern“, „V = A∙l“; OHiMi „Additivität“)
- flaecheninhalt-durch-integration.md Z. 19 (Einheit 5): (OHiMi „Eigenschaften: Additivität, Monotonie, Linearität“; LS-AA QP III 2 und 9 – der Mittelwert steht nic …)
- rotationsvolumen.md Z. 11 (Einheit 1): (FOS „Rotationsvolumen“ als Pflichtform mit linearen und quadratischen Funktionen; GOST LK „auch zusammenge …)
- rotationsvolumen.md Z. 13 (Einheit 2): (GOST LK; Poolpraxis)
- uneigentliche-integrale.md Z. 13 (Einheit 2): (Prüfungsform des Pools 2022, beide Zeilen erhöht)
- matrizen-und-uebergangsprozesse.md Z. 11 (Einheit 1): (Pool AG/LA 1; kein Planinhalt)
- matrizen-und-uebergangsprozesse.md Z. 13 (Einheit 2): (Pool AG/LA 1)
- matrizen-und-uebergangsprozesse.md Z. 15 (Einheit 3): (Pool AG/LA 1)
- matrizen-und-uebergangsprozesse.md Z. 17 (Einheit 4): (Pool AG/LA 1)
- matrizen-und-uebergangsprozesse.md Z. 19 (Einheit 5): (Pool AG/LA 1)
- kenngroessen-von-verteilungen.md Z. 17 (Einheit 4): (GOST-Inhalt „Eigenschaften auf der Grundlage graphischer Darstellungen“; OHiMi 2.4 „Histogramme“; alle Zei …)
- konfidenzintervalle.md Z. 11 (Einheit 1): (Pool erhöht, Teil B; die Deutung trägt jede Teilaufgabe)
- konfidenzintervalle.md Z. 13 (Einheit 2): (Pool erhöht, Teil B; [FS-IQB] liefert die Gleichung)
- konfidenzintervalle.md Z. 15 (Einheit 3): (Pool erhöht, Teil B; Prüfungshöhe)

### Einführungsklasse anders als in der Zusammenfassung von `_klassen-belege.md` (20)

- prozentrechnung 1 OS: OS Kl. 5–6 → OS Kl. 6
- prozentrechnung 5 OS: OS Kl. 7 → OS Kl. 7–8
- zinsrechnung 2 OS: OS Kl. 8–9 → OS Kl. 8–10
- potenzen-wurzeln 1 OS: OS Kl. 5 → OS Kl. 5–9
- einheiten 4 OS: OS Kl. 7–8 → OS Kl. 8
- flaechen 5 OS: OS Kl. 5–7 → OS Kl. 5–6
- kreis 1 OS: OS Kl. 5–8 → OS Kl. 7–8
- kreis 1 GYM: GYM Kl. 5–6 → GYM Kl. 7–8
- koerper 5 OS: OS Kl. 6–8 → OS Kl. 6–9
- koerper 5 GYM: GYM Kl. 8–9 → GYM Kl. 9
- winkel-dreiecke 2 OS: OS Kl. 5–6 → OS Kl. 6–7
- strahlensaetze 3 GYM: GYM Kl. 8–9 → GYM Kl. 9
- zuordnungen 3 OS: OS Kl. 6–7 → OS Kl. 7
- terme 1 GYM: GYM Kl. 5–6 → GYM Kl. 6–7
- lineare-gleichungen 4 OS: OS Kl. 6–7 → OS Kl. 6–8
- potenz-exponentialfunktionen 1 GYM: GYM Kl. 9 → GYM Kl. 10
- trigonometrische-funktionen 1 GYM: GYM Kl. 9–10 → GYM Kl. 10
- daten 5 GYM: GYM Kl. 6–7 → GYM Kl. 7
- wahrscheinlichkeit 2 OS: OS Kl. 6 → OS Kl. 6–7
- wahrscheinlichkeit 3 OS: OS Kl. 7–10 → OS Kl. 8–10

### Marken nachgetragen (5)

- reelle-zahlen 1, Sekundo Kl. 10: „M LVL: Irrationale Zahlen“ – LVL
- reelle-zahlen 2, Sekundo Kl. 10: „M LVL: Multiplikation und Division von Potenzen“ – LVL
- kreis 1, Sekundo Kl. 9: „Q LVL: Grenzprozesse zur Bestimmung von 7i“ – LVL
- binomische-formeln 1, Sekundo Kl. 8: „O LVL: Produkt von Summen“ – LVL
- potenz-exponentialfunktionen 1, Mathematik heute Kl. 10: „Im Blickpunkt; Vergleich von exponentiellen, linearen und quadratischen Funktionen“ – Im Blickpunkt

### Typzeilen entfallen (7)

- potenz-exponentialfunktionen 1: „Potenzfunktion y = a · xᵏ vom exponentiellen Term unterscheiden (Variable in der Basis gegen Variable im Exponenten; Vorrat)“ – Sekundo Kl. 10 „Potenzenfunktionen“ (Stelle gilt jetzt für Einheit 5)
- potenz-exponentialfunktionen 1: „Potenzfunktion y = a · xᵏ vom exponentiellen Term unterscheiden (Variable in der Basis gegen Variable im Exponenten; Vorrat)“ – Mathematik 2023 Kl. 10 „Potenzfunktionen“ (Stelle gilt jetzt für Einheit 5)
- potenz-exponentialfunktionen 1: „Potenzfunktion y = a · xᵏ vom exponentiellen Term unterscheiden (Variable in der Basis gegen Variable im Exponenten; Vorrat)“ – Schnittpunkt Kl. 10 „2 Potenzfunktionen mit natürlichen Exponenten“ (Stelle gilt jetzt für Einheit 5)
- potenz-exponentialfunktionen 1: „Potenzfunktion y = a · xᵏ vom exponentiellen Term unterscheiden (Variable in der Basis gegen Variable im Exponenten; Vorrat)“ – LS Kl. 9 „7 Potenzfunktionen mit natürlichen Exponenten“ (Stelle gilt jetzt für Einheit 5)
- potenz-exponentialfunktionen 1: „Potenzfunktion y = a · xᵏ vom exponentiellen Term unterscheiden (Variable in der Basis gegen Variable im Exponenten; Vorrat)“ – Fundamente Kl. 9 „6.2 Potenzfunktionen mit natürlichen Exponenten“ (Stelle gilt jetzt für Einheit 5)
- potenz-exponentialfunktionen 1: „Potenzfunktion y = a · xᵏ vom exponentiellen Term unterscheiden (Variable in der Basis gegen Variable im Exponenten; Vorrat)“ – Elemente Kl. 9 (Ausgabe 2016) „5.4.1 Potenzfunktionen mit natürlichen Exponenten“ (Stelle gilt jetzt für Einheit 5)
- potenz-exponentialfunktionen 1: „Potenzfunktion y = a · xᵏ vom exponentiellen Term unterscheiden (Variable in der Basis gegen Variable im Exponenten; Vorrat)“ – mathe.delta Kl. 9 „6.1 Potenzfunktionen mit natürlichem Exponenten“ (Stelle gilt jetzt für Einheit 5)

Push origin drücken
