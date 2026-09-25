# Lesezettel testlauf-2026-09-25

Je Eingabe: was die Sitzung sagte (wortgleich aus chat.txt), welche PDFs entstanden und worauf beim Gegenlesen zu achten ist – aus der Spalte „prüft“ von werkzeuge/testlauf-eingaben.csv, ergänzt um „Messung:“-Zeilen aus kennzahlen.md und protokoll.txt. Der Lesezettel zeigt, er bewertet nicht. Erzeugt von werkzeuge/testlauf-lesezettel.py.

## 1 quadgl-9-os

Eingabe: „quadratische gleichungen 9 oberschule“ – an die Sitzung: „quadratische gleichungen 9 oberschule – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · mit Wiederholung und Ausblick (das Register der Blätter führt das Thema nicht, nur das Blatt „nullstellen“) · 3 Zweige, 1 Ausblick (Satz vom Nullprodukt: Oberschule erst Kl. 10) · Zone aus 8 Fertigkeiten
Einheit 1 · Wurzelziehen und Lösbarkeit – Hier lernst du, Gleichungen mit x² durch Wurzelziehen zu lösen und zu sagen, wie viele Lösungen sie haben · neu in diesem Jahr, je nach Buch erst Klasse 10 (am Gymnasium je nach Buch schon seit Klasse 8) · P10 · baut auf: Quadrieren, Quadratwurzeln, lineare Gleichungen, Einsetzen, Scheitelpunktform
Einheit 2 · Normalform und p-q-Formel – Hier lernst du, eine quadratische Gleichung zu ordnen, zu normieren und mit der p-q-Formel zu lösen · neu in diesem Jahr, je nach Buch erst Klasse 10 · P10 oft · baut auf: Wurzelziehen und Lösbarkeit (Einheit 1), Terme ordnen, Ausmultiplizieren und binomische Formeln
Einheit 3 · Sachaufgaben – Hier lernst du, zu einer Sachaufgabe eine quadratische Gleichung aufzustellen, sie zu lösen und die passende Lösung auszuwählen · neu in diesem Jahr, je nach Buch erst Klasse 10 · keine P10-Aufgabe · baut auf: Wurzelziehen und Lösbarkeit (Einheit 1), Normalform und p-q-Formel (Einheit 2), Gleichungen aufstellen
Ausblick: Einheit 4 · Satz vom Nullprodukt – Hier lernst du, Gleichungen, bei denen ein Produkt null ist, ohne Formel zu lösen · kommt nächstes Jahr (am Gymnasium je nach Buch schon seit Klasse 8) · P10 · baut auf: Normalform und p-q-Formel (Einheit 2), Ausmultiplizieren und Ausklammern, Einsetzen
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Ausblick-Zweig Satz vom Nullprodukt (Katalog-Einheit 2, Oberschule Kl. 10) steht zuletzt; darum fehlt das Nullprodukt in der Vorstufe „Welche Form?“ (Nr. 11) und in „Lösungsweg wählen“ (Nr. 17), Produkt gleich Zahl läuft in Nr. 17b über die Formel · Zone eigens gezählt (Z1–Z9), Lernblatt ab Nr. 1 · geteilte Hauptnummern: 14/16 (p-q-Formel – weiter), 24/25 (Rechteckaufgabe – weiter) · Zwischensprossen: Nr. 4d Minus vor x², Nr. 8b Gleichung mit genau einer Lösung angeben, Nr. 14e/f „p negativ“ und „q negativ“ getrennt · Höhe nach Lehrwerk: Einheit 3 (keine P10-Aufgabe), Nr. 25b · im Vorspann definiert: \zweigzeile, \abhakkopf/\abhak (Abhakseite), \vzeile (Verzeichniszeile mit Link) · Vorlage: gleichungsraster setzt die letzte Schreibzeile einer Reihe auf die nächste Zeile, \\[3mm] wirkt nicht; im Aufruf mit einer Leerzeile (\rule{0pt}{2mm} & \\) nach jeder Reihe ausgeglichen, die Zone ist danach neu gesetzt · Nullfall x² = 0 aus Kasten 1 nur als 5x² = 0 und 3x² + 5 = 5.
2. Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (Fertigkeiten, Erkennungsschritte), Sprossen, Typische Fehler, Prüfungsform/Zielmarke; Merkkasten nur als Sperrliste, Verortung und Grundvorstellung nicht gebraucht · gefehlt/Konflikt: Typklammer p-q-Formel [OS 10] gegen die Einheitenmarke OS 9–10 (gesetzt als „kommt je nach Buch erst nächstes Jahr“ an Nr. 14); Vorstufe „Welche Form?“ und Typ „Lösungsweg wählen“ der Einheit 3 setzen Einheit 2 voraus, die an der Oberschule erst Kl. 10 kommt; Kasten 1 sperrt x² = 0, das der Nullfall braucht · Spannen: Einheiten 1, 3, 4 „OS Kl. 9–10“ bei Eingabeklasse 9 = frühe Grenze → „neu in diesem Jahr, je nach Buch erst Klasse 10“ (die Formel „neu oder schon bekannt“ passt an der frühen Grenze nicht); GYM 8–9 der Einheiten 1 und 2 → „am Gymnasium je nach Buch schon seit Klasse 8“; „nicht für alle“ ohne Wirkung, weil es keine frühere Klasse nennt.
4. Protokoll-Archiv: QuadratischeGlg_2026-09-25_protokoll.zip
```

PDFs:

- [QuadratischeGlg_Gesamt.pdf](1-quadgl-9-os/QuadratischeGlg_Gesamt.pdf)
- [QuadratischeGlg_KennstDuSchon.pdf](1-quadgl-9-os/QuadratischeGlg_KennstDuSchon.pdf)
- [QuadratischeGlg_Lernblatt.pdf](1-quadgl-9-os/QuadratischeGlg_Lernblatt.pdf)
- [QuadratischeGlg_Loesungen.pdf](1-quadgl-9-os/QuadratischeGlg_Loesungen.pdf)
- Zwischenkompilate der Sitzung: e1_pruef.pdf, e2_pruef.pdf, e3_pruef.pdf, e4_pruef.pdf, test_raster.pdf, zone.pdf

Worauf beim Gegenlesen achten:

- Zeitmarke „kommt nächstes Jahr" an den Zweigen (OS Kl. 10)
- Gleichungsraster
- Prüfungswort je Zweig
- Abhakseite
- Messung: QuadratischeGlg_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 25 von 48 (gebaute Einheiten); ohne jeden Treffer: E1 x² = c ohne Quadratzahl (Wurzel stehen lassen, Näherungswert mit dem Taschenrechner); E2 Minus vor dem x-Glied (GYM); E2 Vorzahl vor x² (a·x² + bx = 0: x ausklammern, Klammer lösen) (GYM); E3 Normieren: durch die Vorzahl von x² teilen, auch bei negativer Vorzahl; E3 p ungerade: p halbe als Dezimalzahl.
- Messung: 113 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 2 quadgl-9-gym

Eingabe: „quadratische gleichungen 9 gymnasium“ – an die Sitzung: „quadratische gleichungen 9 gymnasium – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · mit Wiederholung · 4 Zweige, kein Ausblick-Zweig (keiner liegt nach Kl. 9) · Zone aus 8 Fertigkeiten
Einheit 1 · Wurzelziehen und Lösbarkeit: Hier lernst du, Gleichungen wie x² = c durch Wurzelziehen zu lösen und zu entscheiden, ob sie zwei, eine oder keine Lösung haben · neu oder schon bekannt – je nach Buch (an der Oberschule Klasse 9 oder 10) · P10 · baut auf: Quadrieren, Quadratwurzeln, lineare Gleichungen, Scheitelpunktform
Einheit 2 · Satz vom Nullprodukt: Hier lernst du, Gleichungen wie (x − a)·(x − b) = 0 mit dem Satz vom Nullprodukt zu lösen, auch durch Ausklammern von x · neu oder schon bekannt – je nach Buch (an der Oberschule erst in Klasse 10) · P10 · baut auf: lineare Gleichungen, Ausklammern, Einsetzen prüfen
Einheit 3 · Normalform und p-q-Formel: Hier lernst du, eine quadratische Gleichung in die Normalform zu bringen und mit der p-q-Formel zu lösen · neu in diesem Jahr (an der Oberschule je nach Buch Klasse 9 oder 10) · P10 oft · baut auf: Wurzelziehen und Lösbarkeit (Einheit 1), Satz vom Nullprodukt (Einheit 2), Terme ordnen, binomische Formeln
Einheit 4 · Sachaufgaben: Hier lernst du, zu Zahlenrätseln und Rechtecken eine quadratische Gleichung aufzustellen, zu lösen und die Lösung auszuwählen, die zur Frage passt · neu in diesem Jahr (an der Oberschule je nach Buch Klasse 9 oder 10) · keine P10-Aufgabe · baut auf: Wurzelziehen (Einheit 1), Satz vom Nullprodukt (Einheit 2), p-q-Formel (Einheit 3)
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Abweichungen: geteilte Hauptnummer 28 → 29 und 30 („– weiter“, Teilung nach Grundfall und vor dem Wechsel zu Wurzel-Ergebnissen); Schnittpunkte Parabel–Gerade als eigene Hauptnummer 32 (Typ steht in keiner Kette), oben verfremdet P10 2022; Höhe nach Lehrwerk in Einheit 4 (keine P10-Aufgabe: Rechteck mit Klammer, Ordnen, Formel, Auswahl, ohne Jahr); weggelassen: „grafische Kontrolle an der Parabel“ (Vorrat, Einheit 3) – das grafische Lesen trägt Nr. 15; Einheit 4 hat drei Kontextaufgaben (Beet, Foto, Teich), weil die Kette des Eintrags sie verlangt, Beet und Foto nutzen beide das Rechteckmodell; im Vorspann definiert: \zweigzeile, \verzzeile, \abhakgruppe/\abhakzeile; im Aufruf ergänzt: \noalign{\vspace{6pt}} nach jeder gleichungsraster-Zeile, weil die Schreibzeilen sonst die nächste Gleichung berühren (Befund für die Vorlage); Zeiten gemessen, die Stempel „e 1“, „e 3“, „e 4“ erst zu Beginn des folgenden Aufrufs gesetzt, „weiter“ ohne Wartezeit (Testlauf ohne Gegenüber).
2. Katalogzeile: gebraucht wurden Lerneinheiten, Marken, Typen, Voraussetzungen (acht Fertigkeiten, sieben Erkennungsschritte), Sprossen, Typische Fehler, Prüfungsform und Zielmarke; nicht gebraucht wurden Merkkasten, Grundvorstellung und Verortung. Es fehlt: die Kastenzahlen sperren fast den ganzen kleinen Zahlenraum (0, 2–4, 6–10), deshalb sind nur ganze Gleichungen und Zahlen ab 13 aus Kasten, Beispielen und Originalen gesperrt (Umbaufrage T4 offen); „Gerade und Parabel gleichsetzen“ hat keine Sprosse in der Kette von Einheit 3. Spannen: bei Einheit 1 und 2 steht „GYM Kl. 8–9“ → „neu oder schon bekannt – je nach Buch“; Oberschule als Zusatz: 9–10 → „je nach Buch Klasse 9 oder 10“ (Einheit 1, 3, 4), Kl. 10 → „erst in Klasse 10“ (Einheit 2).
4. Protokoll-Archiv: QuadratischeGlg_2026-09-25_protokoll.zip
```

PDFs:

- [QuadratischeGlg_Gesamt.pdf](2-quadgl-9-gym/QuadratischeGlg_Gesamt.pdf)
- [QuadratischeGlg_KennstDuSchon.pdf](2-quadgl-9-gym/QuadratischeGlg_KennstDuSchon.pdf)
- [QuadratischeGlg_Lernblatt.pdf](2-quadgl-9-gym/QuadratischeGlg_Lernblatt.pdf)
- [QuadratischeGlg_Loesungen.pdf](2-quadgl-9-gym/QuadratischeGlg_Loesungen.pdf)
- Zwischenkompilate der Sitzung: probe_e1.pdf, probe_e2.pdf, probe_e3.pdf, probe_e4.pdf

Worauf beim Gegenlesen achten:

- dieselben Zweige wie Nr. 1 mit gekippten Zeitmarken (GYM Kl. 8–9)
- Zusatz „an der Oberschule erst Kl. 10"
- Messung: QuadratischeGlg_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 24 von 48 (gebaute Einheiten); ohne jeden Treffer: E1 x² = c ohne Quadratzahl (Wurzel stehen lassen, Näherungswert mit dem Taschenrechner); E1 x² freistellen bei a·x² + b = 0 und a·x² = b (erst umformen, dann Wurzel); E3 Normieren: durch die Vorzahl von x² teilen, auch bei negativer Vorzahl; E3 p ungerade: p halbe als Dezimalzahl.
- Messung: 74 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 3 prozent-7-schwach

Eingabe: „prozentrechnung 7 schwach“ – an die Sitzung: „prozentrechnung 7 schwach – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Oberschule als Standpunkt, Gymnasium als Zusatz · mit Wiederholung, ohne Ausblick (Thema steht schon im Register der Blätter) · 4 Zweige; Katalog-Einheit 1 „Prozente als Anteile“ (Kl. 6) als Wiederholung in der Zone · Zone aus 8 Fertigkeiten

Plan:
Einheit 1 von 4 · Prozentsatz berechnen – Hier lernst du auszurechnen, wie viel Prozent ein Teil vom Ganzen ist · neu in diesem Jahr · P10 oft · baut auf: Prozente als Anteile, Brüche erweitern, Runden (Kennst du schon)
Einheit 2 von 4 · Prozentwert berechnen – Hier lernst du auszurechnen, wie viel ein Prozentanteil von einer Größe ist – in Euro, kg oder Stück · neu in diesem Jahr · P10 · baut auf: Prozente als Anteile, Bruchteil einer Größe, Kommazahlen malnehmen, Dreisatz (Kennst du schon)
Einheit 3 von 4 · Grundwert berechnen – Hier lernst du, aus einem Teil und seiner Prozentzahl auszurechnen, wie groß das Ganze ist · neu in diesem Jahr · P10 oft · baut auf: Einheit 1 und 2 (für die gemischten Aufgaben), Dreisatz (Kennst du schon)
Einheit 4 von 4 · Prozentuale Veränderung – Hier lernst du, Preise nach einer Erhöhung oder Senkung auszurechnen und eine Veränderung in Prozent anzugeben · neu oder schon bekannt – je nach Buch · P10 oft · baut auf: Einheit 1 bis 3, Rest zu 100 % und Runden (Kennst du schon)
```

Ausgabeblock (chat.txt, wortgleich):

```text
Abweichungen: Katalog-Einheit 1 „Prozente als Anteile“ (OS Kl. 6) steht als Wiederholung in der Zone (Nr. 5), das Blatt zählt Einheit 1–4 = Katalog-Einheit 2–5 · kein Ausblick, weil das Register der Blätter das Thema schon führt · geteilte Hauptnummern 2/3, 14/15, 18/19, 25/26, 27/28, 33/34, 41/42, 44/49 · Päckchen-Nummern 14, 22, 33, 41 etwa eine halbe Seite hoch statt einer Drittelseite (Grundfall wird nicht geteilt) · Prüfungshöhe der Einheit 4 als eigene Nr. 49 mit einer Teilaufgabe, weil die Kette mit der Steigung endet · Vorstufen 11, 31, 39, 40 mit einem gemeinsamen Streifen statt Darstellung je Teilaufgabe und ohne Raster (kein Rechenschritt); Nr. 7 ohne Darstellung (keine Stellenwerttafel in der Vorlage) · Darstellungen über 100 % (Faktor, Brutto/Netto, 150 %) als Zahlenstrahl, weil der Streifen bei 100 % endet; Steigung als Skizze mit \dreieckrw (Punktnamen A, B, C setzt das Makro) · im Vorspann definierte Bausteine: \swz, \swa, \swb, \swfrage (Teilaufgabe mit Raster und Darstellung daneben, Option schwach), \anw, \rasterende, \zweigzeile (zweite Zeile des Einheitenkopfs), \verzeile (Verzeichniszeile), needspace im Lösungsrahmen · Vorlage: gleichungsraster endet ohne Tiefe unter der letzten Schreibzeile (Folgetext lief hinein, 3 mm Abstand gesetzt); \zahlenstrahl mit xstep 0.01 ab xmin 7.6 zeichnet nichts, letzter Teilstrich fehlt, wenn xmax genau auf dem Raster liegt; \streifenwertreihe zeigt bei leerem Ganzwert kein Feld; \setcounter{aufgabe}{n} ergibt Nr. n+1
Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (Fertigkeiten und alle fünf Erkennungsschritte), Für schwache Schüler (Sprossen, Grundvorstellung), Typische Fehler, Prüfungsform/Zielmarke (2018-OS-K7a, 2021-OS-B1c, 2025-OS-B1a, 2026-FOR-K3c verfremdet), Merkkasten (bei schwach am Zweigende); nicht gebraucht Verortung · Spanne Einheit 5 „OS Kl. 7–8“ bei Eingabeklasse 7 → „neu oder schon bekannt – je nach Buch“; Typklammern [OS 9] Faktor → „kommt in Klasse 9“, [OS 10] Steigung → „kommt in Klasse 10“, [OS 7] Brutto/Netto → „neu in diesem Jahr“; [OS 7–8, GYM 7] „Prozentsatz über 100 %“ steht als Sprosse in Nr. 25 ohne eigene Marke · gefehlt: „Für schwache Schüler“ nennt keine Darstellung für Faktor, Brutto/Netto, Prozentpunkte und Steigung; die Kette der Einheit 5 endet mit der Steigung vor einer Prüfungshöhe anderer Art; der Kasten der Einheit 5 hat mehr als fünf Zeilen (auf vier Zeilen gesetzt)
Protokoll-Archiv: Prozentrechnung_2026-09-25_protokoll.zip
```

PDFs:

- [Prozentrechnung_Gesamt.pdf](3-prozent-7-schwach/Prozentrechnung_Gesamt.pdf)
- [Prozentrechnung_KennstDuSchon.pdf](3-prozent-7-schwach/Prozentrechnung_KennstDuSchon.pdf)
- [Prozentrechnung_Lernblatt.pdf](3-prozent-7-schwach/Prozentrechnung_Lernblatt.pdf)
- [Prozentrechnung_Loesungen.pdf](3-prozent-7-schwach/Prozentrechnung_Loesungen.pdf)
- Zwischenkompilate der Sitzung: check_e1.pdf, check_e2.pdf, check_e3.pdf, check_e4.pdf, check_zone.pdf, test.pdf

Worauf beim Gegenlesen achten:

- Form nach 2.8: Darstellung neben jeder Teilaufgabe
- Raster je Schritt
- Päckchen mit Erklärzeile
- Kasten am Zweigende
- Zone mit Grundvorstellung
- Messung: Prozentrechnung_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 15 von 35 (gebaute Einheiten); ohne jeden Treffer: E2 Umkehrung: zu einem Prozentsatz ein Zahlenpaar angeben; E4 glatte Sätze (50 %, 25 %, 20 %, 10 %: mal 2, 4, 5, 10); E4 Sachtext („das sind 60 % der Klasse“).
- Messung: 124 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 4 linfkt-8-neu

Eingabe: „lineare funktionen 8 nur das neue“ – an die Sitzung: „lineare funktionen 8 nur das neue – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Standpunkt Oberschule (Gymnasium ebenfalls Kl. 8) · 5 Zweige, alle neu in Kl. 8 · ohne Zone, ohne Ausblick

Einheit 1 von 5 · Proportionale Funktion: Hier lernst du, Funktionen mit y = m · x zu berechnen, zu zeichnen und zu erkennen · neu in diesem Jahr · P10 oft · baut auf: Koordinatensystem, proportionale Zuordnungen (Dreisatz)
Einheit 2 von 5 · Lineare Funktion f(x) = m · x + n: Hier lernst du, Geraden mit f(x) = m · x + n zu zeichnen, m und n abzulesen und zu deuten · neu in diesem Jahr · P10 oft · baut auf: proportionale Funktion (Einheit 1), Brüche, negative Zahlen
Einheit 3 von 5 · Punkte und Werte: Hier lernst du, Funktionswerte zu berechnen, Punkte zu prüfen und Nullstellen und Achsenschnittpunkte zu bestimmen · neu in diesem Jahr · P10 oft · baut auf: lineare Funktion (Einheit 2), lineare Gleichungen lösen, negative Zahlen
Einheit 4 von 5 · Gleichung bestimmen: Hier lernst du, die Gleichung einer Geraden aus dem Graphen, aus Steigung und Punkt oder aus zwei Punkten zu bestimmen und den Schnittpunkt zweier Geraden zu berechnen · neu in diesem Jahr · P10 · baut auf: m und n ablesen (Einheit 2), Punktprobe und Nullstelle (Einheit 3), lineare Gleichungen, Terme zusammenfassen
Einheit 5 von 5 · Anwendungen: Hier lernst du, Tarife und andere Sachsituationen mit linearen Funktionen zu beschreiben, zu berechnen und zu vergleichen · neu in diesem Jahr · P10 oft · baut auf: Gleichung, Graph und Schnittpunkt (Einheit 2 bis 4), Dreisatz
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Abweichungen: keine Zone (Bestellung „nur das Neue“), das Gesamt hat daher denselben Inhalt wie das Lernblatt, nur mit der Kopfzeile „Gesamt“ · geteilte Hauptnummern 1/2, 12/13, 23/24, 36/37 · im Vorspann bzw. mit Standard-LaTeX ergänzt: \zweigzeile (zweite Zeile des Einheitenkopfs), Abhakseite (minipage/tabular), Buchstaben der geteilten Nummern per \setcounter{teil}{4}, unbeschriftete Steigungsdreiecke in Nr. 10 per TikZ-\draw im ksys (\steigungsdreieck beschriftet die Höhe und verriete die Antwort) · Vorstufe Nr. 20 ohne Ausrechnen (der Katalog sagt „rechne aus“, 2.3 a verbietet ein Ergebnis) · Einheit 1 ohne P10-Original: Decke nach der Zielmarke des Eintrags (Nr. 7, ohne Jahr) · Ketten nach Lehrwerk für Typen ohne Sprossen im Eintrag: Argument zum Funktionswert (Nr. 22), Parameter deuten (Nr. 16), Gerade durch zwei Punkte zeichnen (Nr. 35), Schnittpunkt rechnerisch (Nr. 36/37) · Nullstelle (Nr. 23/24) steht vor der Punktprobe (Nr. 25), damit die letzte Verfahrensnummer der Einheit 3 die Prüfungshöhe trägt · Einheit 5 besteht nur aus Anwendungen, die Grenze von zwei Kontextaufgaben je Zweig gilt dort nicht · Prüfumfang reduziert
2. Katalog: gebraucht – Lerneinheiten, Marken, Typen je Lerneinheit, Erkennungsschritte und Einheitenangaben der Voraussetzungen, Sprossen je Verfahrenstyp, Typische Fehler, Prüfungsform mit Zielmarke und Zuordnung · nicht gebraucht – Fertigkeiten der Voraussetzungen (ohne Zone), Grundvorstellung, Merkkasten, Verortung · gefehlt – Sprossen für Argument zum Funktionswert, Parameter deuten, Gerade durch zwei Punkte zeichnen und Schnittpunkt rechnerisch; der Erkennungsschritt „Punkt einsetzen … rechne aus“ widerspricht der Vorstufe ohne Ergebnis; die Kette der Einheit 1 beginnt mit einer Blatt-0-Vorstufe (bei „nur das Neue“ entfallen); in der Kette der Einheit 3 liegt die Nullstelle zwischen der Punktprobe und der Prüfungshöhe (Punktprobe mit Bruch-m); getrennt nach Form ergibt das zwei Punktprobe-Stellen, gebaut ist daher die Nullstelle vor der Punktprobe · Spannen: keine – alle fünf Marken OS Kl. 8 · GYM Kl. 8 → „neu in diesem Jahr“; „nicht für alle“ nennt nur spätere Klassen oder Zusatzstoff (z. B. Sekundo 9), daher kein „in manchen Büchern schon“
3. Protokoll-Archiv: LinFkt_2026-09-25_protokoll.zip
```

PDFs:

- [LinFkt_Gesamt.pdf](4-linfkt-8-neu/LinFkt_Gesamt.pdf)
- [LinFkt_Lernblatt.pdf](4-linfkt-8-neu/LinFkt_Lernblatt.pdf)
- [LinFkt_Loesungen.pdf](4-linfkt-8-neu/LinFkt_Loesungen.pdf)
- Zwischenkompilate der Sitzung: gesamt.pdf, lernblatt.pdf, loesungen.pdf, makrotest.pdf, probe_e1.pdf, probe_e2.pdf, probe_e3.pdf, probe_e4.pdf, probe_e5.pdf

Worauf beim Gegenlesen achten:

- keine Zone, kein PDF KennstDuSchon
- Zweigzeilen „neu in diesem Jahr"
- Grafiken auf Gitter
- Wertetabellen
- Halbseitenmaß
- Messung: LinFkt_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 10 von 26 (gebaute Einheiten); ohne jeden Treffer: E3 Punktprobe.
- Messung: 93 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 5 kreis-8-ausblick

Eingabe: „kreis 8 mit ausblick“ – an die Sitzung: „kreis 8 mit ausblick – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Kl. 8, Oberschule als Standpunkt (Gymnasium mit denselben Marken) · mit Wiederholung · 3 Zweige, kein Ausblick-Zweig (jede Marke reicht bis Kl. 8) · Zone aus 6 Fertigkeiten
Einheit 1 · Kreisumfang: Hier lernst du, den Umfang eines Kreises aus Radius oder Durchmesser zu berechnen und umgekehrt · neu oder schon bekannt – je nach Buch · P10 · baut auf: Rechnen mit Kommazahlen und Runden, Umfang und Fläche unterscheiden, Formeln umstellen
Einheit 2 · Kreisfläche: Hier lernst du, den Flächeninhalt eines Kreises zu berechnen und aus der Fläche den Radius zu bestimmen · neu oder schon bekannt – je nach Buch · P10 oft · baut auf: Kreisumfang (Einheit 1), Quadrieren und Wurzelziehen, Formeln umstellen
Einheit 3 · Kreisteile: Hier lernst du, mit Kreisausschnitten zu rechnen: Anteil aus dem Winkel, Bogenlänge, Fläche des Ausschnitts und Kreisring · neu oder schon bekannt – je nach Buch · P10 · baut auf: Kreisumfang (Einheit 1), Kreisfläche (Einheit 2), mit dem Vollwinkel rechnen, Anteile als Bruch und Prozent
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Abweichungen: „mit Ausblick“ bestellt, aber kein Ausblick-Zweig – alle drei Einheiten tragen OS und GYM Kl. 7–8 bzw. 7–9, Kl. 8 liegt in jeder Spanne, also stehen alle drei als „neu oder schon bekannt – je nach Buch“ auf dem Blatt · Zone mit eigenen Nummern 1–7, das Lernblatt zählt ab 1 · Zwischensprossen: E2 Nr. 15c Durchmesser aus der Fläche, E3 Nr. 21e glatter Prozentanteil (36° → 10 %) vor dem gerundeten · Ketten nach Form geteilt: Umfang Nr. 6–7, Fläche Nr. 12–15, Kreisteile Nr. 21–24 (Original jeweils in der letzten) · im Vorspann definierte Bausteine: \zweigzeile, \abhak/\abhakgruppe, \vzeile, \zeichenflaeche, \tortenkreis, \tortenrechteck · vereinfachte Grafiken: Halbkreis als grauer Sektor im Vollkreis (die kreis-Umgebung zeichnet immer den ganzen Kreis), Kreisring mit freiem TikZ in der kreis-Umgebung · Vorstufe „Radius oder Durchmesser?“ nur als Ankreuzen, das Umrechnen steht als eigene Nr. 4 (2.3 a verbietet ein Zahlenergebnis in der Vorstufe).
2. Katalogzeile: Gebraucht wurden Lerneinheiten, Marken, Typen je Lerneinheit, Voraussetzungen (Fertigkeiten und alle vier Erkennungsschritte), Sprossen je Verfahrenstyp, Typische Fehler, Prüfungsform/Zielmarke; nicht gebraucht wurden Verortung, Grundvorstellung und Mindeststoff (nur bei „schwach“), der Merkkasten nur zum Sperren von Zahlen. Befunde: Der Erkennungsschritt „Radius oder Durchmesser?“ verlangt „die andere angeben (d = 6,4 → r = 3,2)“, also eine Zahl – das widerspricht der Vorstufe. Von der Fertigkeit „Winkel messen und zeichnen, Vollwinkel“ braucht das Blatt nur den Vollwinkel. Die Kastenzahlen (r = 2, 3, 4, 5, 10) sperren viele Grundfallzahlen. „nicht für alle“ bei Einheit 1 nennt nur spätere Bücher (Sekundo 9) und passt nicht zur Form „in manchen Büchern schon Kl. n“. Spannen: E1 und E2 OS/GYM 7–8, E3 7–9 → bei Kl. 8 „neu oder schon bekannt – je nach Buch“. Typklammer [OS 5, GYM 5–6] → „kennst du seit Klasse 5“ an Nr. 3; [OS 5–8], [OS 7–8] und [OS 7–9] decken sich mit der Einheitsmarke → keine Klammer.
4. Protokoll-Archiv: Kreis_2026-09-25_protokoll.zip
```

PDFs:

- [Kreis_Gesamt.pdf](5-kreis-8-ausblick/Kreis_Gesamt.pdf)
- [Kreis_KennstDuSchon.pdf](5-kreis-8-ausblick/Kreis_KennstDuSchon.pdf)
- [Kreis_Lernblatt.pdf](5-kreis-8-ausblick/Kreis_Lernblatt.pdf)
- [Kreis_Loesungen.pdf](5-kreis-8-ausblick/Kreis_Loesungen.pdf)
- Zwischenkompilate der Sitzung: pruef_e1.pdf, pruef_e2.pdf, pruef_e3.pdf, test_grafik.pdf

Worauf beim Gegenlesen achten:

- Typklammer „kennst du seit Klasse 5" am Zeichnen-Typ
- Zeichenflächen mit 8-mm-Karo
- Ausblick-Zweig Kreisteile am Ende mit „Ausblick"
- Messung: Kreis_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 12 von 25 (gebaute Einheiten); ohne jeden Treffer: E1 Halbkreisbogen (mit und ohne Durchmesser); E1 Sachaufgabe (Rad: Weg bei mehreren Umdrehungen; Baumstamm; Reifen); E2 Sachaufgabe (Abwurfring, Pizza, Deckel, Grundfläche eines Kegels oder Zylinders); E3 Ausschnittsfläche A = α/360° · π · r²; E3 Sachaufgabe (Rasensprenger, Tortenstück, Sektor im Kreisdiagramm).
- Messung: 98 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 6 daten-7

Eingabe: „daten 7“ – an die Sitzung: „daten 7 – Antworten auf Planfrage und Zone: sek i, alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Kl. 7 · Standpunkt Oberschule, Gymnasium als Zusatz · mit Wiederholung, ohne Ausblick (Thema im Register der Blätter) · 2 Zweige · Einheiten 1, 2 und 4 (Marke vor Kl. 7) als Fertigkeiten in der Zone · Einheit 6 (Sek II) und Einheit 7 (Vierfeldertafel, Kl. 9) weggelassen · Zone aus 9 Fertigkeiten
Einheit 1 von 2 · Streifen- und Kreisdiagramm – Hier lernst du, Anteile als Streifen und als Kreisdiagramm darzustellen · neu oder schon bekannt – je nach Buch (am Gymnasium schon seit Klasse 6) · P10 oft · baut auf: Häufigkeiten und Anteile (Kennst du schon), Prozentsatz, Längen in cm und mm, Winkel zeichnen
Einheit 2 von 2 · Diagramme beurteilen und Boxplot – Hier lernst du, Aussagen zu Diagrammen zu prüfen, täuschende Diagramme zu erkennen und Boxplots zu lesen · neu oder schon bekannt – je nach Buch, bis Klasse 9 (am Gymnasium neu in diesem Jahr) · P10 · baut auf: Säulendiagramme lesen und Kenngrößen (Kennst du schon), Prozentsatz, Bruchteil und Vielfaches
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Abweichungen: Katalog-Einheiten 1, 2 und 4 (Marke OS Kl. 5–6 bzw. 6, also vor Kl. 7) stehen nur als Fertigkeiten in der Zone, damit fallen ihre Typen über den Grundfall hinaus und die Vorstufen „Welche Kenngröße?“ und „Sortiert?“ weg · Einheit 6 (Sek II) und Einheit 7 (Vierfeldertafel, Kl. 9) weggelassen, kein Ausblick, weil das Register der Blätter „daten“ schon führt · geteilte Hauptnummern 6/7, 14/15, 17/18, 25/26 · Boxplot lesen und zeichnen (30, 31) als eigene Hauptnummern hinter der Prüfungshöhe 29, weil sie eigene Form und Zeitmarke haben; Decke dort nach Lehrwerk (kein P10-Original), Quartilregel in der Anweisung, Daten so gewählt, dass beide Schulbuchregeln dasselbe Quartil ergeben · Zwischensprosse „ein Sechstel“ beim Schätzen von Sektoren (19) · Vorstufe 24 mit vier kleinen Diagrammen, weil jede Achse ihre eigene Grafik braucht · im Vorspann definiert: \zweigkopf (Zweigzeile als zweite Zeile), \zonekopf, \loesungskopf, die Abhakseite (aus den Titeln erzeugt) · Vorlage: Bei \bp sind die Endstriche der Antennen im Raster nicht immer zu sehen (liegen auf Gitterlinien), die Werte lassen sich trotzdem ablesen.
2. Katalog: gebraucht wurden Lerneinheiten, Marken, Typen je Lerneinheit, Voraussetzungen (Fertigkeiten und Erkennungsschritte), Sprossen, Typische Fehler und Prüfungsform/Zielmarke (P10); nicht gebraucht: Merkkasten, Verortung, alle Sek-II-Teile · Befunde: „Boxplot zeichnen [GYM 7]“ hat keine OS-Marke, und „Boxplot zeichnen/vergleichen“ haben keine Sprossenkette; „Spannweite [OS 9]“ passt nicht zur Einheitsmarke OS Kl. 6 · Spannen: Einheit 3 (OS 6–7) und Einheit 5 (OS 6–9) enthalten Kl. 7 → „neu oder schon bekannt – je nach Buch“; Einheit 1 und 2 (OS 5–6) liegen vor Kl. 7 → Zone; die Typklammer „Liniendiagramm lesen [OS 6–8]“ enthält Kl. 7, gehört aber zu einem Zweig der Zone und ist deshalb nur dort als Grundfall vertreten.
4. Protokoll-Archiv: Daten_2026-09-25_protokoll.zip
```

PDFs:

- [Daten_Gesamt.pdf](6-daten-7/Daten_Gesamt.pdf)
- [Daten_KennstDuSchon.pdf](6-daten-7/Daten_KennstDuSchon.pdf)
- [Daten_Lernblatt.pdf](6-daten-7/Daten_Lernblatt.pdf)
- [Daten_Loesungen.pdf](6-daten-7/Daten_Loesungen.pdf)
- Zwischenkompilate der Sitzung: check_e1.pdf, check_e2.pdf

Worauf beim Gegenlesen achten:

- Stufenfrage beantwortet (Sek I)
- Einheit 6 weggelassen und in der Deutungszeile genannt
- neue Klassen-Typen in Einheit 1 als Sprosse oder Hauptnummer
- Säulendiagramme mit Bausteinen
- Messung: Daten_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 49 von 73 (alle Einheiten); ohne jeden Treffer: E1 Häufigkeitstabelle aus einer Urliste; E4 Modalwert; E7 Tafel aus einem Text aufstellen (Merkmale benennen, Zahlen einordnen).

## 7 nullstellen-fokus

Eingabe: „nullstellen“ – an die Sitzung: „nullstellen – Antworten auf Planfrage und Zone: quadratische-funktionen; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Fokus Nullstellen · Eintrag quadratische-funktionen, Einheit 4 · ohne Klasse, Marken absolut (ab Kl. 10, am Gymnasium ab Kl. 9) · Zone aus 5 Fertigkeiten

Plan: entfällt (Fokus)
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Zwischensprosse in Nr. 11: p-q-Formel mit Radikand null (eine Nullstelle) und negativ (keine Nullstelle) – die Kette der Einheit 4 führt den Sonderfall nur über den Scheitel · geteilte Hauptnummern 7/8, 10/11, 16/17; 13/14 nach Form getrennt (Normalform, Scheitelpunktform) · Nr. 18 (Wurfparabel) ohne Original, Höhe nach Lehrwerk · Fokus mit 27 Rechenteilaufgaben einschließlich zweier Lückenbeispiele (Richtwert 15–25), Kette nicht gekürzt · nicht im Fokus: die übrigen Typen der Einheit 4 (Argument zu Funktionswert, Schnittpunkte Gerade–Parabel, Punktprobe als Schnittpunkt-Nachweis, Gerade ohne gemeinsamen Punkt, Schnittpunkte zweier Parabeln), nur in der Vorstufe d–e angelegt · im Vorspann definiert: \zweigzeile · gleichungsraster: letzte Schreibzeile lief in die Folgezeile, im Aufruf mit Zusatzabstand ausgeglichen
2. Katalog: gebraucht Lerneinheiten, Marken, Typen Einheit 4, Voraussetzungen (5 der 8 Fertigkeiten; Koordinaten, lineare Gleichung und Schnittpunkt zweier Geraden braucht der Fokus nicht), Erkennungsschritt „Was wird gleichgesetzt?“, Sprossen Einheit 4, Typische Fehler (nur eine Lösung; ohne Normieren), Prüfungsform und Zielmarke (2020-OS-K3e, 2025-OS-K5c, 2017-OS-K5d); nicht gebraucht Merkkasten, Verortung, Grundvorstellung · gefehlt: „nullstellen“ allein trifft zwei Einträge (Eintragsfrage nötig); p-q-Sonderfälle fehlen in der Kette; die Kastensperre (0–6, 8–10, 16) ist wörtlich nicht einzuhalten – angewandt auf Terme und Ergebnispaare aus Kästen und Originalen, nicht auf Einzelziffern · Spanne: Einheit 4 trägt keine (OS Kl. 10 · GYM Kl. 9) → „ab Kl. 10 (am Gymnasium ab Kl. 9)“
4. Protokoll-Archiv: QuadratischeFkt_2026-09-25_protokoll.zip
```

PDFs:

- [QuadratischeFkt_Fokus_Nullstellen.pdf](7-nullstellen-fokus/QuadratischeFkt_Fokus_Nullstellen.pdf)
- [QuadratischeFkt_Fokus_Nullstellen_Loesungen.pdf](7-nullstellen-fokus/QuadratischeFkt_Fokus_Nullstellen_Loesungen.pdf)

Worauf beim Gegenlesen achten:

- Eintragsfrage gestellt und mit dem Eintrag beantwortet
- dann Fokus: kurze Zone
- Zweigzeile
- Grundfall dreimal
- Prüfungshöhe mehrfach
- Messung: QuadratischeFkt_Fokus_Nullstellen.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 8 von 13 (gebaute Einheiten); ohne jeden Treffer: E4 Argument zu gegebenem Funktionswert (Gleichung aufstellen, ordnen, lösen).

## 8 potenz-10

Eingabe: „potenz-exponentialfunktionen 10“ – an die Sitzung: „potenz-exponentialfunktionen 10 – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
Lernblatt · Oberschule als Standpunkt, Gymnasium als Zusatz · mit Wiederholung · mit Ausblick (Thema noch nicht gebaut), kein Zweig liegt hinter Kl. 10 · 5 Zweige · Zone aus 8 Fertigkeiten

Plan:
1. Lineares und exponentielles Wachstum unterscheiden: Hier lernst du, an Tabellen, Texten und Graphen zu erkennen, ob ein Wert linear oder exponentiell wächst · neu in diesem Jahr · P10 oft · baut auf: Zunahme um denselben Betrag, Erhöhen um Prozent mit einer Dezimalzahl, Punkte im Koordinatensystem
2. Wachstumsfaktor und Wachstumstabelle: Hier lernst du, aus dem Prozentsatz den Wachstumsfaktor zu bilden und eine Wachstumstabelle mit ihm fortzuschreiben · neu in diesem Jahr · P10 oft · baut auf: Einheit 1, Prozentwert und Prozentsatz, Zinseszins, Quotient zweier Werte
3. Exponentialfunktion aufstellen und auswerten: Hier lernst du, eine Gleichung für ein Wachstum aufzustellen und damit Werte und Zeitpunkte zu berechnen · neu in diesem Jahr · P10 · baut auf: Einheit 2, Potenz mit dem Taschenrechner, Zinseszins
4. Verdopplungs- und Halbwertszeit: Hier lernst du, die Zeit zu bestimmen, nach der sich ein Wert verdoppelt oder halbiert hat · neu in diesem Jahr · P10 · baut auf: Einheit 3, Wertetabelle und Graph lesen, Potenz mit dem Taschenrechner
5. Potenzfunktionen mit natürlichem Exponenten: Hier lernst du Funktionen wie y = x³ und y = x⁴ kennen: Wertetabelle, Graph und Eigenschaften · neu in diesem Jahr (am Gymnasium schon seit Klasse 9) · keine P10-Aufgabe · baut auf: Einheit 3, Normalparabel, Punkte im Koordinatensystem
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Abweichungen: kein Ausblick-Zweig – alle Marken liegen bei Kl. 10 (Einheit 5 am Gymnasium Kl. 9), „mit Ausblick“ hatte nichts zu tragen · Einheit 5 hat im Eintrag keine Sprossenkette: Ketten und Höhe nach Lehrwerk-Konvention (keine P10-Aufgabe) · die Vorrats-Kette „Potenzfunktion einordnen“ aus Einheit 1 ist in Einheit 5 gebaut (Nr. 43–48), nicht doppelt · Logarithmus (Vorrat) als Sprosse Nr. 39 c · geteilte Hauptnummern 14/15, 16/17, 23/24, 29/30, 31/32, 37/38/39 · Nr. 16: Zeichenfläche neben sechs kurzen Teilaufgaben statt Teilung (Grundfall ist eine Sprosse) · im Vorspann definierte Bausteine: \zweigzeile, \punktfeldn, \leeresgitter, \langzelle, \abhak · Abhakseite läuft über zwei Seiten · Zeiten gemessen; zwei Stempel „zone“ (der erste aus einem fehlgeschlagenen Aufruf), die Stempel „e n“ je einen Aufruf nach der Prüfung · unbeaufsichtigter Lauf: Planfrage und „weiter“ aus der Eingabe beantwortet
2. Katalog: gebraucht Lerneinheiten, Marken, Typen je Lerneinheit, Voraussetzungen (Fertigkeiten und Erkennungsschritte), Sprossen je Verfahrenstyp, Typische Fehler, Prüfungsform und Zielmarke; nicht gebraucht Merkkasten (nur als Sperrliste), Verortung, Grundvorstellung (nur bei schwach) · gefehlt: Einheit 5 hat weder Sprossen noch Erkennungsschritte noch eine Fertigkeitszeile „– Einheit 5“; Einheit 1 führt die Potenzfunktion noch als Vorrat-Kette neben der eigenen Einheit 5; die Erkennungsschritte „Differenz oder Quotient?“ und „Welcher Schritt ist null?“ verlangen Aufschreiben bzw. Abzählen und widersprechen der Vorstufenregel (auf dem Blatt ohne Zahl umgesetzt); die Kastenzahlen-Sperre (0, 1, 4, 5, 20, 100) ist in Tabellenköpfen nicht einhaltbar, 20 und 80 stehen in Nr. 16 bewusst in einer Verdopplungsreihe · Spannen: keine Marke trug eine Spanne; „nicht für alle“ nennt nur Bücher ohne frühere Klasse und steht deshalb nicht in der Zweigzeile
3. Protokoll: PotenzExponentialFkt_2026-09-25_protokoll.zip
```

PDFs:

- [PotenzExponentialFkt_Gesamt.pdf](8-potenz-10/PotenzExponentialFkt_Gesamt.pdf)
- [PotenzExponentialFkt_KennstDuSchon.pdf](8-potenz-10/PotenzExponentialFkt_KennstDuSchon.pdf)
- [PotenzExponentialFkt_Lernblatt.pdf](8-potenz-10/PotenzExponentialFkt_Lernblatt.pdf)
- [PotenzExponentialFkt_Loesungen.pdf](8-potenz-10/PotenzExponentialFkt_Loesungen.pdf)
- Zwischenkompilate der Sitzung: check_e1.pdf, check_e2.pdf, check_e3.pdf, check_e4.pdf, check_e5.pdf

Worauf beim Gegenlesen achten:

- neue Einheit 5 Potenzfunktionen als Zweig mit „keine P10-Aufgabe"
- Decke nach Lehrwerk im Ausgabeblock genannt
- Graphen von x³ und x⁴
- Messung: PotenzExponentialFkt_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 43 von 62 (gebaute Einheiten); ohne jeden Treffer: E1 Grenzen des Modells nennen (ein Bestand wächst nicht ewig); E5 Punktprobe.

## 9 kurven-12-be

Eingabe: „kurvenuntersuchung 12 berlin“ – an die Sitzung: „kurvenuntersuchung 12 berlin – Antworten auf Planfrage und Zone: gymnasium, gk; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Sek II, Standpunkt Q1 = Klasse 11: alle Zweige liegen vor der Eingabeklasse und stehen als Wiederholung zum Abitur auf dem Blatt · mit Wiederholung · 5 Zweige, kein Ausblick · Zone aus 6 Fertigkeiten
Einheit 1 · Monotonie und erste Ableitung – Hier lernst du, am Vorzeichen der Ableitung abzulesen, wo ein Graph steigt und wo er fällt · kennst du seit Q1 (Klasse 11) · Abitur GK · baut auf: Ableitungen bilden, Gleichungen lösen
Einheit 2 · Extrempunkte – Hier lernst du, Hoch-, Tief- und Sattelpunkte zu berechnen und nachzuweisen · kennst du seit Q1 (Klasse 11) · Abitur GK · baut auf: Monotonie (Einheit 1), Ableitungen bilden, Gleichungen lösen, Funktionswerte berechnen, Graphen grob skizzieren
Einheit 3 · Krümmung und Wendepunkte – Hier lernst du, mit der zweiten Ableitung die Krümmung eines Graphen und seine Wendepunkte zu bestimmen · kennst du seit Q1 (Klasse 11) · Abitur GK · baut auf: Monotonie (Einheit 1), Extrempunkte (Einheit 2), Ableitungen bilden, Gleichungen lösen, Funktionswerte berechnen
Einheit 4 · Graph und Ableitungsgraph – Hier lernst du, aus dem Graphen einer Funktion den Graphen ihrer Ableitung zu entwickeln und umgekehrt · kennst du seit Q1 (Klasse 11), je nach Kursplan bis Q2 · Abitur GK · baut auf: Monotonie (Einheit 1), Extrempunkte (Einheit 2), Krümmung und Wendepunkte (Einheit 3), Ableitung als Steigung deuten, Graphen grob skizzieren
Einheit 5 · Kurvenuntersuchung im Sachzusammenhang – Hier lernst du, Sachfragen in Hoch-, Tief- und Wendepunkte zu übersetzen und die Ergebnisse im Sachzusammenhang zu deuten · kennst du seit Q1 (Klasse 11) · Abitur GK · baut auf: Extrempunkte (Einheit 2), Krümmung und Wendepunkte (Einheit 3), Graph und Ableitungsgraph (Einheit 4), Ableitung als Änderungsrate deuten, Gleichungen lösen, Funktionswerte berechnen
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Kl. 12 Berlin: alle fünf Zweige tragen Q1 (Klasse 11) und lägen nach 1.5 vor der Eingabeklasse, also ganz in der Zone – sie stehen als Wiederholung zum Abitur auf dem Blatt, Zeitmarke „kennst du seit Q1 (Klasse 11)“ · Umfang alle Zweige (Rückfall) · weggelassen wegen GK: „Einzigen Tiefpunkt über die streng monotone Ableitung nachweisen und berechnen“ und „Extremstelle einer Logarithmusfunktion über die Ableitung oder die Symmetrie begründen“ (E2), „Wendepunkt mit vorgegebenen Koordinaten über die zweite Ableitung nachweisen und den symmetrischen Wendepunkt angeben“, „Wendepunkt über den Vorzeichenwechsel der zweiten Ableitung aus der Kettenregel am Graphen nachweisen“ und „Wendestellen einer Sinusfunktion als ganzzahlig nachweisen …“ (E3), „Logarithmus einer Exponentialfunktion als lineare Funktion nachweisen …“ (E4) · geteilte Hauptnummern 25/26 (Zeichenfläche) und 41/42 (vor dem Formwechsel Maßstab) · im Vorspann definiert: \zweigzeile (zweite Zeile des Einheitenkopfs), \abhakgruppe und \abhak (Abhakseite), \verzeile (Verzeichniszeile) · keine Zwischensprossen, keine vereinfachten Grafiken
2. Katalog: gebraucht Lerneinheiten, Marken, Typen je Lerneinheit, Voraussetzungen (6 Fertigkeiten → Zone, 3 Erkennungsschritte → Vorstufen 14, 15, 39), Sprossen je Verfahrenstyp, Typische Fehler, Prüfungsform und Zielmarke; nicht gebraucht Merkkasten, Grundvorstellung, Verortung · Befund: Sek-II-Marken nennen keine Klasse, für Kl. 12 Berlin liegt jeder Zweig vor der Eingabeklasse – 1.5 regelt den Fall nicht; die Kastenzahlen-Sperre der Offenen Punkte (0 bis 4, 6) ist in Sek II nicht einhaltbar, gemieden wurden Kastenfunktionen und -ergebnisse; Mindestgrad und Skizze aus Eigenschaften (E4) stammen nur aus LK-Heft und erhöhtem Pool, ohne LK-Vermerk im Eintrag, hier als GK geführt; der iqb-Typ „Gerade durch die beiden Wendepunkte … parallele Gerade mit genau einem gemeinsamen Punkt“ ist bei Funktionen vierten Grades auf ℝ unmöglich (f minus Wendepunktgerade ist symmetrisch), gebaut auf eingeschränktem Bereich · Spanne: Einheit 4 „BE Q1/2“ → „kennst du seit Q1 (Klasse 11), je nach Kursplan bis Q2“
4. Protokoll-Archiv: Kurvenuntersuchung_2026-09-25_protokoll.zip
```

PDFs:

- [Kurvenuntersuchung_Gesamt.pdf](9-kurven-12-be/Kurvenuntersuchung_Gesamt.pdf)
- [Kurvenuntersuchung_KennstDuSchon.pdf](9-kurven-12-be/Kurvenuntersuchung_KennstDuSchon.pdf)
- [Kurvenuntersuchung_Lernblatt.pdf](9-kurven-12-be/Kurvenuntersuchung_Lernblatt.pdf)
- [Kurvenuntersuchung_Loesungen.pdf](9-kurven-12-be/Kurvenuntersuchung_Loesungen.pdf)
- Zwischenkompilate der Sitzung: check_e1.pdf, check_e2.pdf, check_e3.pdf, check_e4.pdf, check_e5.pdf, check_zone.pdf

Worauf beim Gegenlesen achten:

- Sek II: Zeitmarke mit Halbjahr Q1 Berlin
- Kursart GK
- Prüfungswort „Abitur GK"
- Decke Abitur Teil A/B
- kein `\weit`
- Messung: Kurvenuntersuchung_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 68 von 83 (gebaute Einheiten).
- Messung: 111 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 10 ka-terme-8-gym

Eingabe: „klassenarbeit terme binomische formeln 8 gymnasium“ – an die Sitzung: „klassenarbeit terme binomische formeln 8 gymnasium – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
Lernblatt · Klassenarbeit aus zwei Einträgen: terme.md (Einheit 3–4) und binomische-formeln.md (Einheit 1–3) · mit Wiederholung, Ausblick leer (kein Zweig nach Kl. 8) · 5 Zweige · Zone aus 6 Fertigkeiten, darin terme.md Einheit 1–2

Plan:
Einheit 1 · Klammern auflösen: Hier lernst du, Klammern mit Plus, Minus oder einer Zahl davor aufzulösen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Terme zusammenfassen, Malnehmen mit Vorzeichen
Einheit 2 · Ausklammern: Hier lernst du, einen gemeinsamen Faktor vor die Klammer zu ziehen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Zahl mal Klammer (Einheit 1)
Einheit 3 · Summe mal Summe: Hier lernst du, Terme mit zwei Variablen zusammenzufassen und zwei Klammern miteinander malzunehmen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Klammern auflösen (Einheit 1), Terme zusammenfassen, Terme malnehmen
Einheit 4 · Binomische Formeln: Hier lernst du, Quadrate von Klammern mit den drei binomischen Formeln auszumultiplizieren · neu in diesem Jahr · P10 · baut auf: Summe mal Summe (Einheit 3), Minusklammer (Einheit 1), Quadratzahlen
Einheit 5 · Faktorisieren: Hier lernst du, eine Summe mit einer binomischen Formel in ein Produkt zu verwandeln · neu in diesem Jahr (an der Oberschule je nach Buch bis Klasse 10) · keine P10-Aufgabe · baut auf: binomische Formeln (Einheit 4), Ausklammern (Einheit 2)
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Abweichungen:
- Die Klassenarbeit stützt sich auf zwei Einträge: terme.md Einheit 1–2 liegen als Wiederholung in der Zone (am Gymnasium Kl. 6–7 und 7), terme.md Einheit 3–4 und binomische-formeln.md Einheit 1–3 sind die fünf Zweige. Kein Ausblick-Zweig, weil keine Marke nach Kl. 8 liegt.
- Die Zone ist ohne „Scheitelpunktform lesen“ (am Gymnasium erst Kl. 9; der P10-Nachweis Nr. 33 d ist reine Termumformung) und ohne „Dezimalzahlen als Vorzahlen“, weil das Blatt beides nicht braucht.
- Zwischensprosse: Nr. 11 g „Variable mal Klammer“ als Brücke zu Ausklammern und Klammer mal Klammer.
- Ergänzte Pflichtelemente ohne passenden Typ im Eintrag: Entscheiden Nr. 18, Anwendungen Nr. 19, 38 und 46.
- Die Höhe ist die Zielmarke des Eintrags ohne Original in den Einheiten 1, 2, 3 und 5. Einheit 4 schließt mit dem verfremdeten Original (P10 2017), Nr. 33 d.
- Geteilte Hauptnummern: 23/24, 31/32/33, 35/36, 41/42/43.
- Im Vorspann definierte Bausteine: \zweigkopf (Zweigzeile unter \einheitenkopf*), \flaechenbild (Rechteck in vier Teilflächen, Nr. 26 und 37), \abhak/\abhakgruppe (Abhakseite), \verzzeile (Verzeichniszeile mit Link).
- Befund zur Vorlage 2026-09-22h: Im gleichungsraster liegt die letzte Schreiblinie einer Zeile auf dem Text der nächsten Zeile. Ich habe je Rasterzeile \noalign{\vspace{5mm}} gesetzt; die Vorlage bleibt unverändert.
- Die „Tabelle als Bild“ der Klammer-Kette steht nur im Beispiel von Nr. 11, als Sachtabelle.
- Auf dem ganzen Blatt stehen a und b nur für die Glieder der Formel. Aufgabenvariablen sind x, y, z, m, n, u, v; Sachvariablen p, k, s, q, w.
2. Katalogzeile:
- Gebraucht: Lerneinheiten, Marken, Typen, Voraussetzungen (Fertigkeiten und Erkennungsschritte), Sprossen, Typische Fehler, Prüfungsform/Zielmarke. Nicht gebraucht: Merkkasten, Grundvorstellung. Die Verortung diente nur zur Wahl der beiden Einträge.
- Lücken im Katalog: Die Vorstufen „Ist das ein Quadrat?“ (Wurzel dazuschreiben) und „Passt das Mittelglied?“ (doppeltes Produkt bilden) in binomische-formeln.md verlangen eine Rechnung, was 2.3 a widerspricht. Auf dem Blatt stehen sie als „Quadrat von“ (Nr. 39) und als reines Ankreuzen (Nr. 40).
- Weitere Lücken: terme.md Einheit 4 hat keinen Begründen- oder Kontexttyp. Die Voraussetzung „Scheitelpunktform lesen“ liegt am Gymnasium hinter dem Thema.
- Spannen: terme.md Einheit 3–4 und binomische-formeln.md Einheit 1 (GYM Kl. 7–8) wurden zu „neu oder schon bekannt – je nach Buch“. binomische-formeln.md Einheit 3 (OS Kl. 8–10) steht als Zusatz „an der Oberschule je nach Buch bis Klasse 10“. terme.md Einheit 1 (GYM 6–7) und 2 (GYM 7) liegen in der Zone.
3. Protokoll-Archiv: TermeBinomischeFormeln_2026-09-25_protokoll.zip
```

PDFs:

- [TermeBinomischeFormeln_Gesamt.pdf](10-ka-terme-8-gym/TermeBinomischeFormeln_Gesamt.pdf)
- [TermeBinomischeFormeln_KennstDuSchon.pdf](10-ka-terme-8-gym/TermeBinomischeFormeln_KennstDuSchon.pdf)
- [TermeBinomischeFormeln_Lernblatt.pdf](10-ka-terme-8-gym/TermeBinomischeFormeln_Lernblatt.pdf)
- [TermeBinomischeFormeln_Loesungen.pdf](10-ka-terme-8-gym/TermeBinomischeFormeln_Loesungen.pdf)
- Zwischenkompilate der Sitzung: check_e1.pdf, check_e2.pdf, check_e3.pdf, check_e4.pdf, check_e5.pdf, check_zone.pdf

Worauf beim Gegenlesen achten:

- zwei Einträge
- Zweige in Lehrplanfolge
- eine Zone aus beiden
- Nachbarzweige aus „Querbezüge" genannt
- Leiter eine Stufe über der Richtung
- Messung: TermeBinomischeFormeln_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 31 von 61 (alle Einheiten); ohne jeden Treffer: E3 Minusklammer (alle Vorzeichen drehen); E3 Anwendung: Produktform gleich null (Verfahren in quadratische-gleichungen.md Einheit 2).
- Messung: 113 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).
