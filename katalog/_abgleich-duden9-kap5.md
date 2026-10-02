> Lehrerentscheid 02.10.2026: Empfehlungen der Gruppe „Katalog“ übernehmen; zusätzlich aufnehmen (statt „nicht aufnehmen“): Ungleichungen und Ungleichungssysteme, Kathetensatz und Höhensatz, negativer Streckfaktor, Intervallschachtelung, Beweise – mit Marke (Gymnasium/Vorrat) nach ziel.md § 1 („Klasse und Schulform filtern nicht; sie ordnen“). Satz von Vieta offen. Umsetzung in Katalog und Bank steht aus.

# Abgleich: Duden „Wissen – Üben – Testen, Mathematik 9“ (2017), Kapitel 5, gegen katalog/strahlensaetze.md

Messversuch „Lehrbuch als Quelle für Katalog und Aufgabenbank“,
2026-10-02, drittes Kapitel. Gelesen: PDF-Seiten 62–73 (12 Seiten, als
Bild mit 85 dpi, dazu die Textschicht des PDF; keine Seite musste mit
110 dpi nachgerendert werden). Die Klassenarbeiten (S. 74 ff.) sind
bewusst nicht gelesen. Katalogstand: Klon mathe-nachhilfe (flach,
letzter Commit); Bank: Klon aufgabenbank, bank/strahlensaetze (Stand
27.09., Katalog-Commit 7613213). Kein Wortlaut und keine Zahl aus dem
Buch in den Bankzeilen; vom Buch stammen nur Typ und Stufung.

## Kurzfassung

Das Buch bestätigt alle drei Einheiten im Kern, bringt aber fast nur
Rechen- und Sachaufgaben; einem Blatt aus der Bank fehlen danach vor
allem gemischte Tabellen (Maßstab, Strahlensatzfigur mit mehreren
Unbekannten), Streckungen mit negativen Koordinaten und Bruchfaktoren,
der Umfang mal k neben der Fläche mal k² und Sachaufgaben, in denen
eine Angabe überflüssig ist. Neu für den Katalog bringt es vier Dinge:
die Maßstabsleiste einer Karte lesen, Verhältnisgleichungen nur mit
Streckennamen aus der Figur ergänzen (das trifft den häufigsten
Strahlensatzfehler), eine Strecke im Verhältnis m : n teilen und den
Volumenfaktor k³ (die letzten beiden als Vorrat). Negativer
Streckfaktor, Fixgerade und Verkettung von Streckungen sind
Gymnasialstoff und bleiben draußen. Umgekehrt fehlen dem Buch alle
Vorstufen, das ganze maßstabsgerechte Zeichnen der P10, Fehler finden
und fast alles Begründen.

## A „Im Buch, nicht im Katalog“

Gruppe „Bank“: nur zusätzliche Aufgaben an einer Sprosse, die im
Katalog schon steht – geht ohne Einzelbestätigung in die Bank. Gruppe
„Katalog“: ändert den Katalog (neue Sprosse, neuer Typ, Reihenfolge,
Streichung aus „Nicht aufgenommen“) – Entscheidung des Lehrers je Zeile;
die Spalte „Was der Schüler ohne ihn nicht übt“ ist für diese Zeilen
so geschrieben, dass ohne Datei geurteilt werden kann. „Bankzeilen“
nennt die Zahl der Entwürfe in `neu-strahlensaetze-duden9.jsonl`.
Sprossennummern nach der heutigen Bank; das Merkmal einer Zusatzzeile
ist das der Sprosse (das Prüfskript verlangt es einheitlich), das neue
Merkmal der Variante steht nur hier in der Spalte „Typ“.

| Nr. | Gruppe | Typ | Buchstelle | Was der Schüler ohne ihn nicht übt | Vorschlag | Bankzeilen |
|---|---|---|---|---|---|---|
| A1 | Bank | Streckenverhältnis mit Dezimalzahlen und Strecken in verschiedenen Einheiten | S. 63 Nr. 1, 2 | Die Bank gibt Original- und Bildstrecke immer in derselben Einheit und mit glattem k. | e2 Kette 1, Sprosse 4, Variante 4. | 1 |
| A2 | Bank | Maßstabstabelle, in der jede Zeile eine andere Richtung verlangt; sehr große Maßstäbe mit Dezimalzahl auf der Karte | S. 63 Nr. 3, 5 | Er rechnet die Landkarte nur in einer Richtung (Kartenzentimeter in Kilometer). | e1 Kette 2, Sprosse 8, Varianten 4–5. | 2 |
| A3 | Bank | Strahlensatzfigur als Tabelle: zwei Unbekannte, Teil- und Gesamtstrecken gemischt, beide Sätze | S. 65 Nr. 7 | Er löst immer nur eine Gleichung je Figur. | e3 Kette 1, Sprosse 5, Variante 4. | 1 |
| A4 | Bank | Steigung als Strahlensatz (Seilbahn), mit einer überflüssigen Angabe | S. 65 Nr. 8; S. 73 Nr. 30 | Er bekommt nie eine Sachaufgabe, in der er eine Angabe weglassen muss. | e3 Kette 1, Sprosse 7, Variante 4. | 1 |
| A5 | Bank | Peilung: ein kleiner Gegenstand am ausgestreckten Arm verdeckt ein großes Objekt; Messkeil | S. 65 Nr. 10, 11 | Die Bank kennt nur Baum, Fluss, Förster, Lochkamera; den Messkeil als Werkstück trägt kein Blatt (ohne Zeile). | e3 Kette 1, Sprosse 7, Variante 5. | 1 |
| A6 | Bank | Flussbreite in der X-Figur mit fertiger Skizze | S. 65 Nr. 9a | Die X-Figur kommt in der Bank nur ohne Sachkontext vor. | e3 Kette 1, Sprosse 6, Variante 4 (`\strahlensatz[x]`). | 1 |
| A7 | Bank | Ein Verhältnis, mehrere Gesuchte (Schatten mehrerer Bäume) | S. 66 Nr. 14 | Er rechnet das Verhältnis jedes Mal neu, statt es einmal als Faktor zu bestimmen. | e3 Kette 1, Sprosse 6, Variante 5. | 1 |
| A8 | Bank | Messanordnung begründen (warum ein ganzzahliges Verhältnis abstecken; Monddurchmesser mit Murmel erläutern) | S. 65 Nr. 9b; S. 66 Nr. 12 | Das Begründen der Bank fragt nur nach Gründen der Sätze, nie nach der Planung einer Messung. | e3 Kette 4 (Pflicht begründen), Sprosse 2, Variante 4. | 1 |
| A9 | Bank | Umkehrung mit Teilstrecken in dm und cm, Ergebnis „nicht parallel“ | S. 67 Nr. 16 | In der Bank sind die Gesamtstrecken gegeben und die Einheiten gleich. | e3 Kette 1, Sprosse 8, Variante 4. | 1 |
| A10 | Bank | Streckung im Koordinatensystem: Zentrum im Ursprung innerhalb der Figur, negative und halbe Koordinaten; Zentrum mit negativen Koordinaten und k als Bruch | S. 69 Nr. 17, 18; S. 70 Nr. 24 (nur k > 0) | Die Bank streckt nur im ersten Quadranten mit ganzem k. | e2 Kette 1, Sprosse 2, Varianten 4–5. | 2 |
| A11 | Bank | Streckfaktor aus Zentrum und einem Bildpunkt ablesen, dann weitere Bildpunkte | S. 69 Nr. 19, 22 | Er bekommt k immer genannt oder als zwei Längen, nie aus der Lage. | e2 Kette 1, Sprosse 4, Variante 6. | 1 |
| A12 | Bank | Kreis vom Mittelpunkt aus strecken: k aus den Radien, Bilddurchmesser | S. 69 Nr. 20 | Er streckt nur Vielecke. | e2 Kette 1, Sprosse 4, Variante 5. | 1 |
| A13 | Bank | Flächenfaktor zu k als Maßstab 1 : n und als Dezimalzahl; Umfang mal k und Fläche mal k² in einer Aufgabe | S. 69 Nr. 21; S. 72 Nr. 27; S. 73 Nr. 31 | Die Bank fragt nur die Fläche mit ganzem k; den Unterschied Umfang–Fläche sieht er nie nebeneinander. | e2 Kette 1, Sprosse 10, Varianten 4–5. | 2 |
| A14 | Bank | Zentrum und k aus zwei Punktpaaren im Gitter | S. 70 Nr. 25 | – (Vorrat-Kette hat nur Figuren mit drei Paaren) | e2 Kette 2, Sprosse 1, Variante 4. | 1 |
| A15 | Bank | Rahmen gleicher Breite: Außen- und Innenfigur ähnlich? | S. 72 Nr. 26 | Er verwechselt „gleich breiter Rand“ mit „ähnlich“. | e2 Kette 3 (Pflicht begründen), Sprosse 2, Variante 4. | 1 |
| A16 | Bank | Ähnlichkeit über Seitenverhältnisse mit Einheitenwechsel und Nein-Fall; zweite Rechteckseite erst aus dem Flächeninhalt | S. 73 Nr. 29, 32 | Die Bank gibt alle Seiten in cm und meist den Ja-Fall. | e2 Kette 1, Sprosse 7, Varianten 4–5. | 2 |
| A17 | Bank | Ähnliches Dreieck zu einer vorgegebenen Bildseite: k als Bruch, zwei Seiten berechnen, zeichnen | S. 72 Nr. 28 | Er berechnet nie ein ganzes Bilddreieck mit unglattem k. | e2 Kette 1, Sprosse 8, Variante 4. | 1 |
| A18 | Katalog | Maßstabsleiste lesen: Leistenabschnitt und Beschriftung in 1 : n, dann Strecken umrechnen | S. 63 Nr. 6; Wissen S. 62 | Er kann eine Karte nur benutzen, wenn „1 : 25 000“ daraufsteht; auf Wander- und Stadtkarten steht oft nur die Leiste. | Aufnehmen, für alle: Einheit 1, Kette „Maßstab umrechnen“, neue Sprosse nach „Landkarte mit großer Zahl hinten“, vor der Prüfungshöhe (NEU-massstabsleiste). | 2 |
| A19 | Katalog | Verhältnisgleichung nur mit Streckennamen aus der Figur ergänzen, auch bei drei Parallelen | S. 66 Nr. 13; Wissen S. 66 (Erweiterung) | Er rechnet, bevor er weiß, welche Strecken zusammengehören – genau daher kommt der Fehler „Parallele mit Strahlabschnitt gemischt“. | Aufnehmen, für alle: Einheit 3, Kette 1, neue Sprosse nach „zweiter Strahlensatz“, vor der X-Figur (NEU-gleichung-ergaenzen); drei Parallelen nur als zweite Variante. | 2 |
| A20 | Katalog | Strecke im Verhältnis m : n teilen (Hilfsstrahl mit m + n Teilen) | S. 67 Nr. 15; Wissen S. 67 | Er teilt nur in gleiche Teile und sieht nicht, dass „7 : 3“ dieselbe Konstruktion mit zehn Teilen ist. | Aufnehmen als Vorrat, Kette „Strecke in n gleiche Teile“, zweite Sprosse (NEU-teilung-mn). Berührt „Streckenteilung als Hauptleistung“ nicht – es bleibt eine Vorrat-Sprosse. | 1 |
| A21 | Katalog | Volumen mal k³, k aus dem Volumenfaktor zurück; Oberfläche mal k² | S. 73 Nr. 33 | Er überträgt k² auf Körper und glaubt, die achtfache Schachtel habe achtfach lange Kanten. | Aufnehmen als Vorrat nach „Modellbau“ (NEU-volumen-k3), nur ganze k durch Probieren; „k³ als Hauptleistung“ bleibt unter „Nicht aufgenommen“. | 1 |
| A22 | Katalog | Negativer Streckfaktor (Bild auf der Gegenseite des Zentrums) | S. 70 Nr. 24; Wissen S. 68 (\|k\|) | Er kennt Streckungen nur als Vergrößern und Verkleinern auf derselben Seite. | Nicht aufnehmen: steht unter „Nicht aufgenommen“; die X-Figur deckt den Gedanken ab. GYM. | 0 |
| A23 | Katalog | Zentrum und k aus einer Geraden, die auf sich selbst abgebildet wird, und einem Punktpaar | S. 69 Nr. 23 | Er weiß nicht, dass eine Gerade durch das Zentrum auf sich selbst fällt. | Nicht aufnehmen: eine Aufgabe, kein Lehrwerk des Katalogs nennt sie; die Vorrat-Kette „Zentrum finden“ reicht. GYM. | 0 |
| A24 | Katalog | Verkettung zentrischer Streckungen (k = k₁ · k₂) | Wissen S. 70, keine Übung | Er streckt nie zweimal hintereinander. | Nicht aufnehmen: ohne Übung im Buch, kein Prüfungsbezug. GYM. | 0 |
| A25 | Katalog | Streckenpaare zu einem Verhältnis zeichnen, das als Bruch oder Dezimalzahl gegeben ist | S. 63 Nr. 4 | Er übersetzt 0,6 oder 4/9 nicht in zwei Längen. | Nicht aufnehmen: Blatt 0 „Verhältnis lesen und als Division schreiben“ deckt es. | 0 |
| A26 | Katalog | Zentrische Streckung mit Hilfsstrahl konstruieren statt Längen messen und malnehmen | Wissen S. 68 | Er braucht für k = 3/2 das Lineal und eine Rechnung. | Nicht aufnehmen: der Katalog streckt auf Karo und mit Strahlen; die Hilfsstrahl-Konstruktion ist Streckenteilung (A20). GYM. | 0 |

Zählung: Gruppe Bank 17 Zeilen (A1–A17) mit 21 Bankzeilen; Gruppe
Katalog 9 Zeilen (A18–A26), davon 4 mit Empfehlung „aufnehmen“ (A18–A21;
6 Bankzeilen) und 5 mit „nicht aufnehmen“ (4 davon GYM).

### Platzhalter in der jsonl

| Platzhalter | Bedeutung | Ziel-Bankdatei | vorgeschlagene Stelle |
|---|---|---|---|
| NEU-massstabsleiste | A18 | e1.jsonl, Kette 2 | nach Sprosse 8 „Landkarte …“; alte 9 rückt um eins |
| NEU-gleichung-ergaenzen | A19 | e3.jsonl, Kette 1 | nach Sprosse 2 „zweiter Strahlensatz“; alte 3–9 rücken um eins |
| NEU-teilung-mn | A20 | e3.jsonl, Kette 3 | nach Sprosse 1 „Strecke in n gleiche Teile“ |
| NEU-volumen-k3 | A21 | e2.jsonl, Kette 1 | nach Sprosse 11 „Modellbau“, vor der Prüfungshöhe; alte 12 rückt um eins |

## B „Reihenfolge weicht ab“

| Nr. | Gruppe | Buch | Katalog | Urteil |
|---|---|---|---|---|
| B1 | Katalog | Strahlensätze (5.2) vor zentrischer Streckung (5.3) und Ähnlichkeit (5.4); die Streckung wird mit dem Hilfsstrahl aus den Strahlensätzen konstruiert. | Einheit 2 Streckung und Ähnlichkeit vor Einheit 3 Strahlensätze; die Strahlensätze werden aus der Streckung begründet. | Zwei Wege: (a) bleibt – folgt dem Lehrwerk (Kl. 9 IV 1–3), die Begründen-Sprosse „Strahlensätze folgen aus der Streckung“ und die Prüfungshöhe von Einheit 3 brauchen Einheit 2 vorher; (b) tauschen – folgt dem Duden, der Schüler rechnet zuerst an der festen Figur und lernt die Streckung als deren Anwendung, aber die Begründen-Sprosse kippt und beide Bankdateien tauschen die Einheitennummer. Empfehlung (a); Grundlage ein Lehrwerk gegen ein Übungsbuch, also dünn. |
| B2 | Bank | Fläche mal k² gleich bei der Streckung (S. 69 Nr. 21), Umfang mal k und Fläche mal k² bei der Ähnlichkeit vor den ähnlichen Dreiecken. | Fläche mal k² als Vorrat spät in Einheit 2 (Sprosse 10), Umfang mal k ohne eigene Sprosse. | Reihenfolge bleibt; die Lücke „Umfang mal k“ schließt A13 als Merkmal der Sprosse 10. |

## C „Im Katalog, im Buch nicht“

- Alle Vorstufen (Gleiche Einheit?, kleiner oder größer, passt es ins
  Feld?, gleiche Form?, V oder X?) und beide Grundvorstellungsaufgaben.
- Einheit 1: Maßstab in Worten sagen; Vergrößerungsmaßstab n : 1 rechnen
  (nur im Wissen-Kasten); Modell- und Originalmaße nach P10-Form; ganze
  Kette „Maßstabsgerecht zeichnen“ (Kästchenmaßstab, Karo vergrößern,
  Rechteck und Kreis im Maßstab, Draufsicht, Maßstab wählen, an der
  Zeichnung entscheiden).
- Einheit 2: Figur auf Karo strecken; Eigenschaften ankreuzen; ähnliche
  Dreiecke an zwei Winkeln (nur Wissen-Kasten, keine Übung);
  Gegenkathete zu Hypotenuse vergleichen; Modellbau mit Kanten.
- Einheit 3: Voraussetzung „wirklich parallel?“ vor dem Rechnen;
  X-Figur ohne Sachkontext; Försterdreieck, Lochkamera; Strecke in n
  gleiche Teile (nur Wissen-Kasten).
- Alle drei Einheiten: Fehler finden; Begründen außer A8 und A15;
  Prüfungshöhe.

## Befunde außerhalb der Tabellen

1. `leere_sprossen.json` meldet für strahlensaetze vier leere
   Vorstufen. Die Bank hat dort je vier Zeilen; ihr `sprosse_text` ist
   die Kurzform („„kleiner oder größer“ und „mal oder geteilt“
   ankreuzen (Vorstufe)“), der Katalog trägt seit dem Bankstand die
   Langform. Die Liste meldet eine Textabweichung, keine Lücke. Das Buch
   hat ohnehin keine Vorstufe; keine Zeile dafür.
2. Prüfskript mit `--katalog` auf dem heutigen Katalog: schon der
   unveränderte Bestand hat 145 Abweichungen, alle „sprosse_text nicht
   wortgleich in Zeile N“ – die `quelle`-Zeilen der Bank (87–90) liegen
   heute auf 81–84, der Katalog ist um sechs Zeilen gewachsen. Ohne
   `--katalog` 0 Abweichungen. Die neuen Zeilen tragen die alten
   Zeilennummern wie ihre Nachbarn.
3. Mengen: Die Bank-Gruppe schiebt zwölf Stellen über die Sollmenge
   (Sprosse 3, Pflicht begründen 3; bis sechs Zeilen an e2 Sprosse 4) –
   dieselbe Frage wie in
   Kapitel 3: Zusatzvariante oder Ersatz einer älteren?
4. Bausteine: Eine Maßstabsleiste und eine Figur mit drei Parallelen
   hat `_bausteine.md` nicht; die Zeilen zu A18 und die zweite zu A19
   stehen deshalb ohne Grafik. Ein Baustein `\massstabsleiste` wäre für
   A18 der nächste Handgriff in der Vorlage.
5. Schreibweise: Das Buch nennt das Zentrum S, schreibt SA : SA′ ohne
   Überstrich in den Sätzen und ~ für „ähnlich“; der Katalog bleibt bei
   Z und Überstrich.
6. S. 69 Nr. 23: Die Koordinaten von P und P′ sind bei 85 dpi nicht
   sicher zu lesen; für das Urteil (A23, nicht aufnehmen) ohne Belang.

## Anhang: Aufgabenliste des Kapitels

Schwierigkeit nach Läufersymbol und Inhalt (Einschätzung; die
Graustufen sind bei 85 dpi nicht sicher zu trennen): l leicht, m
mittel, s schwer.

### 5.1 Streckenverhältnisse (S. 62–63), 6 Übungen

| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 63 | 1 | Streckenverhältnis zweier Strecken als Zahl | l | Rechnung |
| 63 | 2 | Tabelle: Strecke oder Verhältnis (auch Bruch, verschiedene Einheiten) ergänzen | m | Tabelle |
| 63 | 3 | Atlas-Tabelle: Maßstab, Original- oder Bildstrecke ergänzen | m | Tabelle |
| 63 | 4 | Streckenpaare zu Verhältnissen (a : b, Bruch, Dezimalzahl) zeichnen | l | Zeichnen |
| 63 | 5 | Karte 1 : 15 Mio.: Karte und Wirklichkeit in beide Richtungen | m | Tabelle |
| 63 | 6 | Maßstab aus Maßstabsleiste, Strecken auf drei Karten umrechnen | s | Grafik lesen, Rechnung |

### 5.2 Strahlensätze (S. 64–67), 10 Übungen

| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 65 | 7 | Skizze zeichnen, Tabelle mit Abschnitten und Parallelen ergänzen | m | Tabelle, Skizze |
| 65 | 8 | Drahtseilbahn: Höhe aus Fahrstrecke (Steigung) | m | Sachaufgabe |
| 65 | 9 | Flussbreite in X-Figur; Begründen der Messanordnung | m–s | Skizze gegeben, Begründen |
| 65 | 10 | Messkeil: Formel deuten, Flaschenhals messen | s | Handlung |
| 65 | 11 | Münze verdeckt Gasbehälter: Entfernung | m | Sachaufgabe |
| 66 | 12 | Monddurchmesser mit Murmel erläutern | s | Erläutern |
| 66 | 13 | Verhältnisgleichungen mit drei Parallelen ergänzen | m | Lückengleichung |
| 66 | 14 | Drei Baumhöhen aus Schatten, Skizze selbst | m | Sachaufgabe |
| 67 | 15 | Strecke im Verhältnis 5 : 2 konstruktiv teilen | m | Konstruktion |
| 67 | 16 | Umkehrung: Parallelität prüfen, gemischte Einheiten | m | Rechnung |

### 5.3 Zentrische Streckung (S. 68–70), 9 Übungen

| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 69 | 17 | Figuren im KS vom Ursprung aus mit k = 2 strecken | l | Zeichnen, Koordinaten |
| 69 | 18 | Dreieck mit Zentrum außerhalb und k = 1,5 strecken | m | Zeichnen, Koordinaten |
| 69 | 19 | k aus Zeichnung, weitere Bildpunkte, Bildviereck | m | Zeichnen |
| 69 | 20 | Kreis vom Mittelpunkt aus strecken | l | Zeichnen |
| 69 | 21 | Flächenfaktor zu k (ganz, dezimal, Bruch, Maßstab) | m | Rechnung |
| 69 | 22 | k aus Zentrum und A′, Bildpunkte, Flächen vergleichen | m | Zeichnen, Rechnung |
| 69 | 23 | Zentrum und k aus Fixgerade und Punktpaar | s | Grafik |
| 70 | 24 | Strecken mit k = 2,5 und k = −1,5 | s | Zeichnen |
| 70 | 25 | Punktgitter: Bild, Zentrum, Faktor in Tabellen ergänzen | m | Tabelle, Gitter |

### 5.4 Ähnlichkeit (S. 71–73), 8 Übungen

| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 72 | 26 | Außen- und Innenfigur ähnlich? entscheiden und begründen | l | Begründen |
| 72 | 27 | Umfang und Fläche bei Maßstab 3,5 : 1 und 1 : 2 | m | Rechnung |
| 72 | 28 | Ähnliches Dreieck zu gegebener Bildseite konstruieren | m | Konstruktion |
| 73 | 29 | Welches Dreieck ist ähnlich? (Seitenverhältnisse, dm) | m | Rechnung |
| 73 | 30 | Seilbahn: Strecke je 10 m Höhe, Höhe je 100 m (überflüssige Angabe) | m | Sachaufgabe |
| 73 | 31 | Umfang und Fläche der Bildfiguren bei k = 1,8 | m | Rechnung |
| 73 | 32 | Rechtecke ähnlich? Seite aus Fläche | m | Begründen |
| 73 | 33 | Streichholzschachtel: Kanten aus k³ = 27, Kartonfläche | s | Sachaufgabe |
