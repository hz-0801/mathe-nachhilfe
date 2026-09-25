Modell: Opus 5.5 (claude-opus-5-5)

# Bericht Auftrag Nacht 2026-09-26

Auftrag: `archiv/auftrag-nacht-2026-09-26.md`; Standdatei: `archiv/nacht-stand-2026-09-26.md`. Commits: Teil 1 c732e7e, Teil 4 19b70c9, Teil 2 f88f137, Teil 3 c6cd85b, Nachzug 8a811fe („werkzeuge: blatt-pruef.py zerlegt Typen wie pruefungswort-belege.py“), Abschluss „archiv: auftrag-nacht-2026-09-26, Bericht“. Nichts gepusht. Kein Katalogeintrag und kein Prompt geändert.

## Teil 1: Prüfskript für Blätter (`werkzeuge/blatt-pruef.py`, `blaetter/kennzahlen.md`)

Vergleichstabelle aus `blaetter/kennzahlen.md`:

| Thema | Datum | Prompt | Datei | Seiten | Hauptnummern | Teilaufgaben | Hauptnummern je Seite | Teilaufgaben je Seite | Titelform | letzte Darstellung | Typen ohne Treffer |
|---|---|---|---|---|---|---|---|---|---|---|---|
| daten | 2026-09-22 | v4.1 | Daten_Blatt0.pdf | 2 | 7 | 39 | 4 · 3 | 24 · 15 | Kurzname – Formwort 2 · Ich kann 0 · anderes 5 | Nr. 4 (Skizze) | – (nur Blatt 0) |
| daten | 2026-09-22 | v4.1 | Daten_E1.pdf | 3 | 6 | 30 | 2 · 3 · 1 | 10 · 16 · 4 | Kurzname – Formwort 6 · Ich kann 0 · anderes 0 | Nr. 10 (Balken) | 3 von 11 (gebaute Einheiten) |
| daten | 2026-09-22 | v4.1 | Daten_Gesamt.pdf | 21 | 40 | 212 | 0 · 4 · 3 · 2 · 3 · 1 · 2 · 1 · 1 · 1 · 2 · 1 · 3 · 2 · 2 · 2 · 2 · 3 · 1 · 1 · 3 | 0 · 24 · 15 · 10 · 16 · 4 · 10 · 12 · 7 · 6 · 7 · 2 · 21 · 8 · 4 · 10 · 20 · 8 · 10 · 6 · 12 | Kurzname – Formwort 35 · Ich kann 0 · anderes 5 | Nr. 38 (sonstige) | 38 von 60 (gebaute Einheiten) |
| daten | 2026-09-22 | v4.1 | Daten_Loesungen.pdf (Ergebnisse) | 3 | – | – | – | – | – | – | – |
| nullstellen | 2026-09-22 | v4.1 | blatt0.pdf | 3 | 11 | 64 | 4 · 5 · 2 | 20 · 31 · 13 | Kurzname – Formwort 11 · Ich kann 0 · anderes 0 | Nr. 10 (Koordinatensystem) | – (nur Blatt 0) |
| nullstellen | 2026-09-22 | v4.1 | e1.pdf | 4 | 9 | 38 | 2 · 1 · 5 · 1 | 10 · 12 · 13 · 3 | Kurzname – Formwort 9 · Ich kann 0 · anderes 0 | Nr. 9 (Tabelle) | 9 von 13 (gebaute Einheiten) |
| nullstellen | 2026-09-22 | v4.1 | e2.pdf | 2 | 7 | 28 | 2 · 5 | 16 · 12 | Kurzname – Formwort 7 · Ich kann 0 · anderes 0 | keine | 8 von 11 (gebaute Einheiten) |
| nullstellen | 2026-09-22 | v4.1 | e3.pdf | 5 | 12 | 47 | 3 · 1 · 2 · 2 · 4 | 16 · 8 · 6 · 5 · 12 | Kurzname – Formwort 12 · Ich kann 0 · anderes 0 | Nr. 17 (Tabelle) | 9 von 16 (gebaute Einheiten) |
| nullstellen | 2026-09-22 | v4.1 | e4.pdf | 5 | 9 | 41 | 1 · 1 · 1 · 4 · 2 | 5 · 9 · 8 · 15 · 4 | Kurzname – Formwort 9 · Ich kann 0 · anderes 0 | Nr. 32 (Koordinatensystem) | 9 von 13 (gebaute Einheiten) |
| nullstellen | 2026-09-22 | v4.1 | e5.pdf | 2 | 5 | 18 | 3 · 2 | 15 · 3 | Kurzname – Formwort 5 · Ich kann 0 · anderes 0 | Nr. 40 (Skizze) | 4 von 8 (gebaute Einheiten) |
| nullstellen | 2026-09-22 | v4.1 | gesamt.pdf | 22 | 53 | 236 | 0 · 4 · 5 · 2 · 2 · 1 · 5 · 1 · 2 · 5 · 3 · 1 · 2 · 2 · 4 · 1 · 1 · 1 · 4 · 2 · 3 · 2 | 0 · 20 · 31 · 13 · 10 · 12 · 13 · 3 · 16 · 12 · 16 · 8 · 6 · 5 · 12 · 5 · 9 · 8 · 15 · 4 · 15 · 3 | Kurzname – Formwort 53 · Ich kann 0 · anderes 0 | Nr. 40 (Skizze) | 33 von 61 (gebaute Einheiten) |
| nullstellen | 2026-09-22 | v4.1 | loesungen.pdf (Ergebnisse) | 3 | – | – | – | – | – | – | – |
| prozentrechnung | 2026-09-22 | v4.0 | blatt0.pdf | 4 | 7 | 34 | 4 · 2 · 1 | 23 · 9 · 2 | Kurzname – Formwort 0 · Ich kann 0 · anderes 7 | Nr. 5 (Tabelle) | – (nur Blatt 0) |
| prozentrechnung | 2026-09-22 | v4.0 | e1.pdf | 3 | 7 | 31 | 3 · 4 | 19 · 12 | Kurzname – Formwort 5 · Ich kann 0 · anderes 2 | Nr. 7 (Tabelle) | 3 von 9 (gebaute Einheiten) |
| prozentrechnung | 2026-09-22 | v4.0 | e2.pdf | 3 | 8 | 30 | 4 · 4 | 19 · 11 | Kurzname – Formwort 8 · Ich kann 0 · anderes 0 | Nr. 9 (Streifen) | 3 von 8 (gebaute Einheiten) |
| prozentrechnung | 2026-09-22 | v4.0 | e3.pdf | 3 | 7 | 28 | 3 · 4 | 17 · 11 | Kurzname – Formwort 7 · Ich kann 0 · anderes 0 | Nr. 17 (Streifen) | 3 von 10 (gebaute Einheiten) |
| prozentrechnung | 2026-09-22 | v4.0 | e4.pdf | 3 | 7 | 26 | 4 · 3 | 17 · 9 | Kurzname – Formwort 6 · Ich kann 0 · anderes 1 | Nr. 24 (Streifen) | 2 von 7 (gebaute Einheiten) |
| prozentrechnung | 2026-09-22 | v4.0 | e5.pdf | 3 | 9 | 36 | 4 · 5 | 22 · 14 | Kurzname – Formwort 8 · Ich kann 0 · anderes 1 | keine | 3 von 10 (gebaute Einheiten) |
| prozentrechnung | 2026-09-22 | v4.0 | gesamt.pdf | 16 | 45 | 185 | 0 · 4 · 2 · 1 · 3 · 4 · 4 · 4 · 3 · 4 · 4 · 3 · 4 · 5 | 0 · 23 · 9 · 2 · 19 · 12 · 19 · 11 · 17 · 11 · 17 · 9 · 22 · 14 | Kurzname – Formwort 34 · Ich kann 0 · anderes 11 | Nr. 24 (Streifen) | 14 von 44 (gebaute Einheiten) |
| prozentrechnung | 2026-09-22 | v4.0 | lernblatt.pdf | 13 | 38 | 151 | 0 · 3 · 4 · 4 · 4 · 3 · 4 · 4 · 3 · 4 · 5 | 0 · 19 · 12 · 19 · 11 · 17 · 11 · 17 · 9 · 22 · 14 | Kurzname – Formwort 34 · Ich kann 0 · anderes 4 | Nr. 24 (Streifen) | 14 von 44 (gebaute Einheiten) |
| prozentrechnung | 2026-09-24 | v4.2 | fokus_a.pdf | 4 | 16 | 54 | 4 · 4 · 5 · 3 | 12 · 15 · 21 · 6 | Kurzname – Formwort 12 · Ich kann 0 · anderes 4 | Nr. 9 (Streifen) | 3 von 8 (gebaute Einheiten) |
| prozentrechnung | 2026-09-24 | v4.2 | fokus_l.pdf (Ergebnisse) | 1 | – | – | – | – | – | – | – |

Gegenprobe im Wortlaut von `kennzahlen.md` (Abschnitt „prozentrechnung · 2026-09-24 · fokus_a.pdf“): „1. Seiten: 4 (Aufgabenseiten 4; Aufgaben).“ – „2. Hauptnummern: 16; Teilaufgaben: 54.“ – „3. Hauptnummern je Seite: 4 · 4 · 5 · 3; Teilaufgaben je Seite: 12 · 15 · 21 · 6.“ – Titelform „Kurzname – Formwort 12 · Ich kann 0 · anderes 4“ – „5. Letzte Hauptnummer mit Darstellung: Nr. 9; je Kategorie: Streifen Nr. 9, Tabelle Nr. 4.“ – „7. Merkkästen: 0.“

Abgleich mit der Erwartung: 4 Seiten und 16 Hauptnummern stimmen. Vier Abweichungen (Befund, das Skript ist nicht angepasst):
- Teilaufgaben 54 statt 52. Quelltext und PDF zeigen je Seite 12 + 15 + 21 + 6; die 52 stammen aus der Textextraktion im Protokoll des Blatts (`src/protokoll.txt`, Zeile „Zählung“), die an den Streifen Buchstaben verliert.
- Form „Kurzname – Formwort“ bei 12, nicht 16 Hauptnummern. Nr. 2–5 sind Blatt-0-Titel in Fertigkeitsform („Brüche kürzen und erweitern“), wie v4.2 2.3 e für Blatt 0 vorschreibt; Nr. 1 „Anteile am Balken – ablesen und färben“ hat die Strichform.
- Der Streifen reicht bis Nr. 9, nicht bis Nr. 8: Nr. 9 „Prozentsatz – am Streifen, Fortsetzung“ trägt drei `\streifenfeld`. Der Befund vom 24.09. sagt selbst „Ablesen … (Nr. 8–9)“ und „verschwindet ab Nr. 10“.
- Kein Merkkasten, weder oben noch unten: `fokus_a.tex` hat kein `\uebersichtskasten` (so auch kein anderes Blatt; `ziel.md` § 2 „Kein Kasten auf dem Blatt“).

Weitere Befunde:
- `blaetter/index.md` führt für nullstellen nur „quadratische-gleichungen.md (…) und“ – `einsortieren.py` übernimmt nur die erste Zeile des Protokollfelds „Katalog:“. Das Skript liest die Fortsetzung aus `src/protokoll.txt` nach (quadratische-funktionen.md).
- Kein Blatt trägt einen Titel „Ich kann …“ (`ziel.md` § 2 verlangt ihn für die Schülersprache); v4.0–v4.2 bauen „Kurzname – Formwort“.
- Kein Merkkasten eines Katalogeintrags hat fett gesetzte Begriffe; überall greift die Ersatzregel „Begriffe vor einem Doppelpunkt“. Sie liefert auch Satzanfänge („Prozent heißt Hundertstel“, „Lesen“, „Zeichnen“) – mechanisch, wie verlangt.

Offen: keine Schritte nach Fehlerregel. Der Sprossenabgleich (Kennzahl 9) ist eine Wortstamm-Heuristik: „ohne Treffer“ heißt, dass kein Titel und kein Aufgabentext die Kernwörter des Typs nennt, nicht, dass die Sprosse fehlt.

Eigene Entscheidungen:
- `../blattbau/` liegt vor; Makronamen und Kategorien aus `mathblatt.sty` (Version 2026-09-22h) und der Anleitung, im Skript als Tabelle (kein Laufzeitzugriff auf das Nachbarrepo). Kategorien: Streifen (jedes Makro `\streifen…`, auch das blatteigene `\streifenfeld`), Tabelle, Skizze (mit freiem TikZ), Koordinatensystem, Balken (Säulen, Balken, Histogramm), dazu „sonstige“ (Kreis-, Liniendiagramm, Boxplot, Baum, Zahlenstrahl …), damit keine Grafik verloren geht.
- Ein Blatt = eine PDF-Datei mit gleichnamiger tex-Datei (`\input` aufgelöst). Ergebnisdateien (ohne `aufgabe`) nur mit Seitenzahl, Kennzeichen „(Ergebnisse)“; bei Dateien mit Begleitteil zählen nur die Aufgabenseiten.
- Titel = erster Satz des `aufgabe`-Arguments (Schlusspunkt weggelassen); Form strukturell (Gedankenstrich zwischen zwei Teilen).
- Antwortform zählt auch Felder in blatteigenen Makros (`\streifenfeld` trägt ein `\leerfeld`); Kasten = Ankreuzkästchen.
- Seite einer Hauptnummer aus pdftotext über „N. <Titelanfang>“; Teilaufgaben zählen auf der Seite, auf der ihre Nummer beginnt.
- Sprossenabgleich nur für die Einheiten, die das Blatt baut (Einheitenkopf gegen Lerneinheitstitel, zwei Drittel der Kernwörter); reine Blatt-0-Dateien „entfällt“; Sek-II-Zusätze von Sek-I-Einträgen zählen nicht mit. In der Tabelle steht die Zahl, die Liste im Abschnitt des Blatts.
- Katalogeintrag = heutiger Stand in `katalog/`, nicht die Kopie im Blattordner.
- Aufruf mit Pfad gibt ein Blatt auf der Konsole aus und schreibt `kennzahlen.md` nicht (kein Teilstand der abgeleiteten Datei).
- Nachzug 8a811fe: die Typzerlegung übernimmt `blatt-pruef.py` aus `pruefungswort-belege.py` (Malpunkt-Regel, engerer Platzhalterfilter, siehe Teil 2); `kennzahlen.md` ist dabei byteidentisch geblieben.

## Teil 2: Prüfungswort-Belege (`werkzeuge/pruefungswort-belege.py`, `katalog/_pruefungswort-belege.md`)

Zahlen: 29 Sek-I-Einträge, 114 Lerneinheiten (ohne die Sek-II-Einheiten), 1 308 Typen; 847 Typzuordnungen mit Grund (T), 71 Einheitenzuordnungen aus den Zuordnungszeilen (U), 6 Verfahrensgeber (V). Typen mit P10-Typ 651, ohne 657 (davon 196 nur mit P10-Typen fremder Themen, zählen nicht). Sek II: 47 Einträge (44 und die Sek-II-Teile von daten, lineare-gleichungssysteme, einheiten), 162 Einheiten, alle Haupttypen wortgleich den Prüfungstypen zugeordnet (1 360; 324 didaktische Typen ohne Prüfungstyp).

Verteilung der Sek-I-Einheiten nach P10-Jahrgängen (von 13):

| P10-Jahrgänge | Einheiten (Haupt oder Neben) | Einheiten (nur Haupt) |
|---|---|---|
| 13 | 5 | 1 |
| 12 | 2 | 1 |
| 11 | 7 | 7 |
| 10 | 5 | 4 |
| 9 | 7 | 8 |
| 8 | 9 | 10 |
| 7 | 9 | 7 |
| 6 | 8 | 5 |
| 5 | 11 | 10 |
| 4 | 9 | 10 |
| 3 | 9 | 14 |
| 2 | 4 | 6 |
| 1 | 6 | 8 |
| 0 | 23 | 23 |

Einheiten ohne P10-Typ („keine P10-Aufgabe“): 21 (bruchrechnung 1–5, reelle-zahlen 1–3, trigonometrische-funktionen 1–4, binomische-formeln 1 und 3, strahlensaetze 2 und 3, flaechen 2, symmetrie-abbildungen 3, terme 4, lineare-gleichungssysteme 3, quadratische-gleichungen 4). Die Zeile 0 der Tabelle zählt 23, weil zwei Einheiten nur einen GYM-Typ tragen, der in den Jahrgängen der msa-Kataloge nicht vorkommt (pyramide-kegel-kugel 1, terme 3; gezählt wie `ertrag.py`, ohne GYM). Die Verteilung je Typ und die sortierten Tabellen stehen in der Datei.

Gegenprobe im Wortlaut der Datei:
- prozentrechnung, „**Einheit 2 · Prozentsatz berechnen** – P10-Jahrgänge 11 von 13 (davon Haupt 8); P10-Typen 2; Summe ertrag 19.“ mit „Prozentsatz berechnen“ und „Prozentuale Veränderung berechnen“, beide Thema „Prozentrechnung“ in `msa-typen.csv`. Erfüllt.
- trigonometrie, Einheit 4 „Sinussatz“: „| Sinussatz Seite berechnen | 29 | 9 | 9 | 2014 | 2025 | 0 | 9 |  |“ – jahre_haupt 9, erster 2014, letzter 2025 wortgleich wie in `msa-ertrag.csv`. Erfüllt.

Befunde (nicht geändert, der Auftrag ändert keinen Eintrag):
- `flaechen.md`, Prüfungsform: die Originale zu „Term zu Figur angeben“ sind vertauscht; laut CSV ist 2014-OS-B1g das Kreuz aus Quadraten, 2022-OS-B1e das rechtwinklige Dreieck, 2025-OS-B1i das geteilte Rechteck.
- `zuordnungen.md` sagt, die antiproportionale Zuordnung habe keinen eigenen Typ; `msa-typen.csv` führt inzwischen „Antiproportionale Zuordnung Dreisatz“ (GYM). `terme.md` sagt, das Thema habe einen Typ; es sind drei weitere GYM-Typen dazugekommen. Die Zuordnungszeilen der Sek-I-Einträge kennen die GYM-Typen allgemein noch nicht (sie sind älter als die GYM-Erfassung); die Datei nennt je Eintrag die P10-Typen der Themen ohne Einheit.
- `themen.csv` weist „Maßstab“ noch zuordnungen zu, `katalog/index.md` seit 09b strahlensaetze.
- `msa-katalog-gym.csv`: 2025-GYM-K5d führt den Trapezschenkel über den Pythagoras mit dem Nebentyp „Mantellinie Kegel bestimmen“ – wohl ein falsches Etikett.

Offen: keine Schritte nach Fehlerregel. Die Schwelle „oft“ setzt der Lehrer.

Eigene Entscheidungen:
- Lesart „prüft“: die Fertigkeit des Katalogtyps ist Teil der Leistung des P10-Typs (Definition oder Original, Haupt- oder Nebentyp); Vorstufen und Kontextvarianten desselben Verfahrens zählen; Fehler finden, Begründen, Umkehrung nur, wenn ein P10-Typ genau das verlangt.
- Themenregel („themen.csv gibt die Thema-Ebene vor“): gezählt werden nur P10-Typen der Themen des Eintrags laut `themen.csv` und der Themen, aus denen seine Zuordnungszeile Typen führt (so zählen bei kreis und pyramide-kegel-kugel auch neuere GYM-Typen ihres Themas). Zuordnungen zu fremden Themen stehen als Hinweis „zählt nicht“ da. Ohne diese Regel bekämen bruchrechnung oder reelle-zahlen über Nebenleistungen in Wahrscheinlichkeits- oder Pythagorasaufgaben P10-Jahrgänge, und der Vermerk aus `themen.csv` liefe ins Leere.
- Verfahrensgeber (V): wo die Zuordnungszeile eine Einheit „Verfahren für“ einen namentlich genannten P10-Typ einer anderen Datei nennt, zählt dieser Typ (quadratische-gleichungen 3 für die Nullstellen, binomische-formeln 2, potenzen-wurzeln 3, pythagoras 2, terme 1, lineare-gleichungen 3); „liefert … für“ und „Voraussetzung für“ bleiben Nebenleistung. Ohne diese Regel stünde „Normalform und p-q-Formel“ bei „keine P10-Aufgabe“.
- „Behauptung prüfen“ (themenübergreifender Nebentyp) zählt nie; er hätte bei jedem Eintrag bis zu 12 Jahrgänge eingetragen.
- P10-Jahrgänge = Haupt oder Neben („kam vor“), daneben „nur Haupt“; Zeilen aus `msa-katalog-basis.csv` und `-kontext.csv` wie `ertrag.py`, ohne GYM (13 Jahrgänge 2014–2026, 2026 FOR und EBR). GYM-Typen tragen den Vermerk „nur GYM“.
- Die sortierte Typentabelle führt nur die 651 Typen mit P10-Typ; die Zählung je Wert umfasst alle 1 308.
- Sek II ohne Urteil: Haupttypen wortgleich (mit oder ohne Gegenstandsklasse) aus `abitur-typen.csv`/`fhr-typen.csv`; GK = `…-gk`, LK = `…-lk` und `bb-ea`; erfasst GK 2018–2026 (9), LK 2017, 2018, 2022–2026 (7), FHR 2019–2026 (8); der IQB-Pool zählt nicht (Auftrag: Abitur und FHR), Typen nur im Pool tragen „nur Pool“.
- Arbeitsteilung: prozentrechnung habe ich selbst als Muster zugeordnet; die übrigen 28 Einträge haben sechs Hilfsagenten (Opus) nach derselben Lesart zugeordnet, jede Teildatei an der Prüfung des Skripts (`--probe`); zusammengeführt, 18 Zuordnungen stichprobenweise nachgelesen, formelhafte Gründe gesucht (keine).
- Zerlegung der Typenzeilen: Malpunkte in Formeln trennen nicht („V = π · r² · h“, „a · 10ⁿ“), Platzhalter nur „kein …typ“ (vorher fiel „kein Binom erkennen“ weg); die Teildaten sind über den Wortlaut umnummeriert.

## Teil 3: Sek-II-Ordnung (`werkzeuge/sek2-ordnung-belege.py`, `katalog/_sek2-ordnung-belege.md`)

Je Sek-II-Eintrag eine Zeile (BE = Berlin Khj, BB = Brandenburg Q, B/K = Bigalke/Köhler-Band):

| Eintrag | Halbjahr | GK/LK | nur LK |
|---|---|---|---|
| kurvenuntersuchung | BE Q1/Q2 · BB Q1 · B/K 11 | BE GK und LK, Teile nur LK · BB GK und LK | nein |
| binomialverteilung | BE Q4 · BB Q2 · B/K 11 | GK und LK | nein |
| ebenen | Q3 · B/K 12 | GK und LK | nein |
| ableitung-und-aenderungsrate | BE Q1/Q2 · BB Q1 · B/K 11 | GK und LK | nein |
| ableitungsregeln | Q1 · B/K 11 | GK und LK | nein |
| grenzwerte-und-verhalten-im-unendlichen | BE Q1/Q2 · BB Q1 · B/K 11 | BE GK und LK, Teile nur LK · BB GK und LK | nein |
| gleichungen-loesen | BE Q1/Q3 · BB Q1 · B/K 11 | GK und LK | nein |
| umkehrfunktion | Q2 · B/K 11 | nur LK | Einheit 1, 2 |
| ableitungsgraph-und-funktionsgraph | keine Lerneinheiten (Verweiseintrag) | – | – |
| tangente-normale-schnittwinkel | Q1 · B/K 11 | GK und LK | nein |
| extremalprobleme | Q1 · B/K 11 | GK und LK | nein |
| funktionsklassen-und-eigenschaften | BE Q1/Q2 · BB Q1 · B/K 11 | BE GK und LK, Teile nur LK · BB GK und LK | nein |
| funktionsscharen-und-ortskurven | Q1 · B/K 11 | nur LK | Einheit 1, 2, 3, 4, 5 |
| rekonstruktion-von-funktionsgleichungen | Q1 · B/K 11 | GK und LK | nein |
| stammfunktion-und-hauptsatz | Q2 · B/K 11 | GK und LK | nein |
| integrationsregeln | Q2 · B/K 11 | GK und LK | nein |
| flaecheninhalt-durch-integration | BE Q2 · BB Q2/Q4 · B/K 11/12 | BE GK und LK · BB GK und LK, Teile nur LK | nein |
| rekonstruktion-von-bestaenden | Q2 · B/K 11 | GK und LK | nein |
| rotationsvolumen | BE Q2/Q4 · BB Q4 · B/K 12 | nur LK | Einheit 1, 2 |
| uneigentliche-integrale | BE Q2/Q4 · BB Q2 · B/K 11 | nur LK | Einheit 1, 2 |
| punkte-und-strecken-im-koordinatensystem | Q3 · B/K 12 | GK und LK | nein |
| vektoren-und-rechenoperationen | Q3 · B/K 12 | GK und LK | nein |
| linearkombination-und-lineare-abhaengigkeit | Q3 · B/K 12 | GK und LK | nein |
| geraden | Q3 · B/K 12 | GK und LK | nein |
| lagebeziehungen | Q3 · B/K 12 | GK und LK, Teile nur LK | nein |
| schnittmengen | Q3 · B/K 12 | BE GK und LK · BB GK und LK, Teile nur LK | nein |
| skalarprodukt-und-winkel | Q3 · B/K 12 | GK und LK | nein |
| orthogonalitaet | Q3 · B/K 12 | GK und LK | nein |
| abstaende | Q3 · B/K 12 | GK und LK, Teile nur LK | Einheit 3 |
| spiegelung | Q3 · B/K 12 | GK und LK | nein |
| scharen-von-geraden-und-ebenen | Q3 · B/K 12 | nur LK | Einheit 1, 2, 3, 4 |
| flaecheninhalt-und-volumen-im-raum | Q3 · B/K 12 | GK und LK | nein |
| matrizen-und-uebergangsprozesse | BE Q3 · B/K – | BE GK und LK · BB – | nein |
| vierfeldertafel | Q2 · B/K 11 | GK und LK | nein |
| bedingte-wahrscheinlichkeit-und-bayes | Q2 · B/K 11 | GK und LK | nein |
| unabhaengigkeit | Q2 · B/K 11 | GK und LK | nein |
| zufallsgroessen-und-verteilungen | BE Q2/Q4 · BB Q2 · B/K 11 | BE nur LK · BB GK und LK | nein |
| hypergeometrische-verteilung | Q2 · B/K 11 | GK und LK | nein |
| kenngroessen-von-verteilungen | BE Q2/Q4 · BB Q2 · B/K 11 | BE GK und LK, Teile nur LK · BB GK und LK | nein |
| normalverteilung-und-sigma-regeln | Q4 · B/K 12 | nur LK | Einheit 1, 2, 3 |
| hypothesentests | Q4 · B/K 12 | nur LK | Einheit 1, 2, 3 |
| konfidenzintervalle | Q4 · B/K 12 | GK und LK | nein |
| zufallsexperimente-und-pfadregeln | Q2 · B/K 11 | GK und LK | nein |
| kombinatorik | Q2 · B/K 11 | GK und LK | nein |
| lineare-gleichungssysteme (Einheit 5, Sek II) | BE Q3 · BB Q1/Q3 · B/K 11 | GK und LK | nein |
| daten (Einheit 6, Sek II) | Q2 · B/K 11 | GK und LK | nein |

Einheiten „nur LK: ja“: 22 von 157 (umkehrfunktion 1–2, funktionsscharen-und-ortskurven 1–5, rotationsvolumen 1–2, uneigentliche-integrale 1–2, abstaende 3, scharen-von-geraden-und-ebenen 1–4, normalverteilung-und-sigma-regeln 1–3, hypothesentests 1–3). Länderunterschied in der Kursart bei 6 Einheiten; Einheiten je Kurshalbjahr (BE oder BB): Q1 41, Q2 58, Q3 56, Q4 25.

Gegenprobe im Wortlaut der Datei:
- ableitung-und-aenderungsrate, Einheit 2 „Ableitung an einer Stelle“: „Bigalke/Köhler GK 11, S. 88: „III. Einführung des Ableitungsbegriffs“ (Z. 56) › „3. Die lokale Steigung einer Funktion“ (Z. 59)“, „Bigalke/Köhler LK 11, S. 98: … (Z. 149)“; „Rahmenlehrplan Berlin, Z. 1179: … – Q1 (Khj, Z. 1179)“, „Rahmenlehrplan Brandenburg, Z. 950–951: … – Q1“. Erfüllt.
- Stochastik in Band 12: nur teilweise erfüllt (Befund). Bigalke/Köhler führt die Stochastik zum größten Teil in Band 11 (GK 11 Kap. X–XIII, LK 11 Kap. XI–XIV: Beschreibende Statistik, Grundbegriffe, Kombinatorik, bedingte Wahrscheinlichkeit, Vierfeldertafel, Binomialverteilung) – damit liegen binomialverteilung, vierfeldertafel, bedingte-wahrscheinlichkeit-und-bayes, unabhaengigkeit, zufallsgroessen-und-verteilungen, hypergeometrische-verteilung, kenngroessen-von-verteilungen, zufallsexperimente-und-pfadregeln, kombinatorik und daten 6 in Band 11. In Band 12 stehen nur Prognose- und Konfidenzintervalle, Normalverteilung und Hypothesentests (konfidenzintervalle, normalverteilung-und-sigma-regeln, hypothesentests). Das passt zum Brandenburger Plan: Q2 „Analysis; Stochastik“.

Weitere Befunde:
- Berlin setzt die Binomialverteilung ins Kurshalbjahr Q4, Brandenburg in Q2.
- Keine Planstelle: gleichungen-loesen 4 (Ungleichungen) und matrizen-und-uebergangsprozesse 5 (so schon `_kursart-belege.md`).
- Matrizen stehen bei Bigalke/Köhler nur im Band Abiturvorbereitung (Kap. II.7, II.8), in keinem Kursband.
- Elemente NRW führt „Funktionen mit einem Parameter“ auch im GK-Band; Bigalke/Köhler Scharen nur im LK.
- Hypothesentests fehlen in Elemente NRW ganz.
- Zwei FOS-Zitate der Einträge stehen so nicht im Plantext: ableitungsregeln 1 „Konstanten-, Potenz-, Faktor-, Summenregel“ (Plan: „Konstanten-, Faktor-, Summen- und Potenzregel“), kombinatorik 1 „Permutationen, Variationen“ (Plan: „Permutationen, Kombinationen, Variationen“); die Stelle ist als Daten mit Ermessen nachgetragen.

Offen: keine Schritte nach Fehlerregel. Die Qualifikationsphase von Fundamente B liegt nicht im Repo (`quellen/lehrwerke-fundliste.md`); „keine Stelle“ heißt dort „nicht in der Einführungsphase“.

Eigene Entscheidungen:
- Die Planstellen je Einheit übernimmt das Skript aus `katalog/_kursart-belege.md` (Auftrag vom 24.09., dort am Quelltext geprüft, mit Ermessen); das Kurshalbjahr liest es selbst am Quelltext nach: Berlin in der Spalte „Khj“ am Ende des Standards (Q1/2 = Q1 oder Q2), Brandenburg aus dem Abschnitt Q1–Q4, dazu der Block.
- FOS: die Zitate der Lerneinheitszeile, spaltengenau im FOS-Plan gesucht (Spalten „Thema“ und „Inhaltliche Präzisierung“, Trennstriche am Zeilenende verbunden); Ort = Themenfeld, kein Halbjahr, keine Kursart (die FOS ist einjährig).
- Die Lehrwerkszuordnung habe ich selbst gemacht (157 Einheiten, vier Verzeichnisse): Daten nennen nur Quelle und Zeilennummer, Band, Kapitel und Seite liest das Skript; Kapitelzeilen, die den Inhalt nur mittelbar nennen, tragen Ermessen. Band Abiturvorbereitung und „Grundstrategien“ zählen nicht in die Zusammenfassung; das Abiturband ist nur bei den Matrizen zitiert (einzige Stelle).
- Aufgenommen sind auch die Sek-II-Einheiten der Sek-I-Einträge (daten 6, lineare-gleichungssysteme 5); ihre Planstellen habe ich zugeordnet (in `_kursart-belege.md` fehlen sie).
- „nur LK: ja“, wenn jede Planstelle im LK-Zusatz steht oder Bigalke/Köhler die Einheit nur in LK-Bänden führt.

## Teil 4: Ermessensfälle gruppiert (`werkzeuge/klassen-ermessen.py`, `katalog/_klassen-ermessen.md`)

| Sorte | Fälle |
|---|---|
| Wortlaut weicht ab | 112 |
| Zeile deckt mehrere Einheiten oder Typen | 32 |
| Förderheft nach Blocktitel | 31 |
| Katalog verortet den Stoff anders | 23 |
| Zeile unlesbar oder abgeschnitten | 19 |
| Frühe Stelle als Grundstufe gelesen | 15 |
| Kapitel in zwei Bänden | 7 |
| Ersatzverzeichnis | 6 |
| Verzeichnis zu grob | 5 |
| zusammen | 250 |

Gegenprobe: 250 Fälle, Zahlenblock von `_klassen-belege.md` 250 – stimmt.

Offen: keine.

Eigene Entscheidungen:
- Ein Fall = ein Punkt der Liste „Ermessen (n)“ am Schluss eines Eintrags; das Zitat kommt von der Verzeichniszeile, unter der derselbe Grund steht (bei Förderheft-Blöcken die Förderheftzeile mit dem Blocktitel); 8 Fälle betreffen die ganze Einheit und haben kein Zitat.
- Jeder Fall genau einer Sorte: die erste zutreffende Wortlautregel in fester Reihenfolge (Muster im Skript); „Wortlaut weicht ab“ nimmt die übrigen Lesarten „… als … gelesen“.

## Abschluss und allgemeine Entscheidungen

- Die Auftragsdatei ist wortgleich angelegt, auch mit der doppelten ersten Überschriftszeile.
- Teil 4 ist vor Teil 2 und 3 committet, weil er unabhängig war und Teil 2 auf die Hilfsagenten wartete.
- Commit-Nachrichten mit Umlaut über `git commit -F` mit UTF-8-Datei statt `-m` (PowerShell 5.1 verfälscht sonst Umlaute im Argument); ohne Umlaut `-m`.
- Neue Dateien teils mit dem Schreibwerkzeug der Sitzung statt `WriteAllText`; jede Datei danach auf BOM und CR geprüft (keine).
- Auftrag und Standdatei mit `git mv` nach `archiv/` (keine Namensgleichheit); ihre README-Zeilen sind entfernt, dieser Bericht hat eine.

Push origin drücken
