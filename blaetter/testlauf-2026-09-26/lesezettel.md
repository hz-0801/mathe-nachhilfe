# Lesezettel testlauf-2026-09-26

Je Eingabe: was die Sitzung sagte (wortgleich aus chat.txt), welche PDFs entstanden und worauf beim Gegenlesen zu achten ist – aus der Spalte „prüft“ von werkzeuge/testlauf-eingaben.csv, ergänzt um „Messung:“-Zeilen aus kennzahlen.md und protokoll.txt. Der Lesezettel zeigt, er bewertet nicht. Erzeugt von werkzeuge/testlauf-lesezettel.py.

## 1 quadgl-9-os

Eingabe: „quadratische gleichungen 9 oberschule“ – an die Sitzung: „quadratische gleichungen 9 oberschule – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · mit Wiederholung · mit Ausblick (Register führt das Thema nicht; „nullstellen“ vom 22.09. ist ein anderes Blatt) · 3 Zweige, 1 Ausblick · Zone aus 8 Fertigkeiten
Einheit 1 · Wurzelziehen und Lösbarkeit: Hier lernst du, Gleichungen wie x² = c durch Wurzelziehen zu lösen und zu sagen, ob es zwei, eine oder keine Lösung gibt · neu in diesem Jahr, je nach Buch bis Klasse 10 (am Gymnasium schon in Klasse 8 oder 9) · P10 · baut auf: Quadrieren, Wurzel ziehen, lineare Gleichungen, Scheitelpunktform
Einheit 2 · Normalform und p-q-Formel: Hier lernst du, jede quadratische Gleichung zu ordnen und mit der p-q-Formel zu lösen · neu in diesem Jahr, je nach Buch bis Klasse 10 · P10 oft · baut auf: Wurzelziehen (Einheit 1), Ausmultiplizieren, Terme ordnen
Einheit 3 · Sachaufgaben: Hier lernst du, Zahlenrätsel und Flächenaufgaben mit quadratischen Gleichungen zu lösen · neu in diesem Jahr, je nach Buch bis Klasse 10 · keine P10-Aufgabe · baut auf: Wurzelziehen (Einheit 1), p-q-Formel (Einheit 2)
Ausblick: Einheit 4 · Satz vom Nullprodukt: Hier lernst du, Gleichungen in Produktform mit dem Satz vom Nullprodukt zu lösen · kommt nächstes Jahr (am Gymnasium schon in Klasse 8 oder 9) · P10 · baut auf: Ausklammern, lineare Gleichungen, p-q-Formel (Einheit 2)
```

Ausgabeblock (chat.txt, wortgleich):

```text
Ausblick: Satz vom Nullprodukt (OS erst Kl. 10) steht als Einheit 4 am Ende; die Wahl des Lösungswegs in Einheit 2 (Nr. 24, 36) kommt deshalb ohne Nullprodukt aus.
Geteilt: Nr. 27/28 (p-q-Formel, Grundfall und weiter); Nr. 14, 15 und 27–31 stehen mit Rechenplatz und Raster je allein auf ihrer Seite (etwa zwei Drittel Seite), nicht weiter geteilt.
Im Vorspann definiert: \quadratrand (Quadrat mit Rand, Nr. 44) – Kandidat für die Vorlage.
Zone: Fertigkeit „Ausklammern, Ausmultiplizieren, binomische Formeln“ als zwei Nummern (7, 8); Fehler-Paar 10/11 zur binomischen Formel.
Höhe nach Lehrwerk: Einheit 3 hat kein P10-Original (Prüfungshöhe Nr. 44 b).
Vorlage: Kopfzeile der Zone-Datei doppelt („Kennst du schon · Kennst du schon“); x₁, ≈, ≠, π fehlen im Textfont der Lösungen und stehen dort als Mathematik.
Zeiten gemessen; „weiter“ ist im Testlauf ohne Gegenüber simuliert.
Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen, Sprossen, Typische Fehler, Prüfungsform/Zielmarke; nicht gebraucht Merkkasten, Grundvorstellung, Verortung · Befund: „Was sind p und q?“ und „durch welche Zahl teilen?“ verlangen Zahlen – Vorstufen Nr. 25/26 ohne Ergebnis, Ablesen in Nr. 27 · Befund: die Sperre nennt nur wörtliche Gleichungen, x² + 5x + 6 = 0 ist 2025-OS-B1h in Normalform, x² − 4 = 5 die umgestellte Grundvorstellung · Spannen OS Kl. 9–10 (Einheit 1–3) als „neu in diesem Jahr, je nach Buch bis Klasse 10“ (Eingabeklasse = Untergrenze, „neu oder schon bekannt“ passt nicht); Typklammer p-q-Formel [OS 10] als „(je nach Buch erst in Klasse 10)“ an Nr. 27.
Protokoll-Archiv: QuadratischeGlg_2026-09-26_protokoll.zip
```

PDFs:

- [QuadratischeGlg_Gesamt.pdf](1-quadgl-9-os/QuadratischeGlg_Gesamt.pdf)
- [QuadratischeGlg_KennstDuSchon.pdf](1-quadgl-9-os/QuadratischeGlg_KennstDuSchon.pdf)
- [QuadratischeGlg_Lernblatt.pdf](1-quadgl-9-os/QuadratischeGlg_Lernblatt.pdf)
- [QuadratischeGlg_Loesungen.pdf](1-quadgl-9-os/QuadratischeGlg_Loesungen.pdf)
- Zwischenkompilate der Sitzung: test_e1.pdf, test_e2.pdf, test_e3.pdf, test_e4.pdf

Worauf beim Gegenlesen achten:

- Zeitmarke „kommt nächstes Jahr" an den Zweigen (OS Kl. 10)
- Gleichungsraster
- Prüfungswort je Zweig
- Abhakseite
- Messung: QuadratischeGlg_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 26 von 48 (alle Einheiten); ohne jeden Treffer: E1 x² = c ohne Quadratzahl (Wurzel stehen lassen, Näherungswert mit dem Taschenrechner); E1 x² freistellen bei a·x² + b = 0 und a·x² = b (erst umformen, dann Wurzel); E2 Minus vor dem x-Glied (GYM); E2 Vorzahl vor x² (a·x² + bx = 0: x ausklammern, Klammer lösen) (GYM); E3 Normieren: durch die Vorzahl von x² teilen, auch bei negativer Vorzahl; E3 p ungerade: p halbe als Dezimalzahl.
- v4.4-Prüfpunkte: QuadratischeGlg_Gesamt.pdf – a)–g) erfüllen ihr Soll.
- Messung: 78 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 2 quadgl-9-gym

Eingabe: „quadratische gleichungen 9 gymnasium“ – an die Sitzung: „quadratische gleichungen 9 gymnasium – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · mit Wiederholung, ohne Ausblick (Register führt das Thema; kein Zweig nach Kl. 9) · 4 Zweige · Zone aus 8 Fertigkeiten
Einheit 1 von 4 · Wurzelziehen und Lösbarkeit: Hier lernst du, Gleichungen mit x², aber ohne x-Glied durch Wurzelziehen zu lösen und zu sagen, wie viele Lösungen sie haben · neu oder schon bekannt – je nach Buch (an der Oberschule je nach Buch Kl. 9 oder 10) · P10 · baut auf: Quadrieren, Wurzelziehen, lineare Gleichungen, Scheitelpunktform
Einheit 2 von 4 · Satz vom Nullprodukt: Hier lernst du, Gleichungen der Form Produkt gleich null mit dem Satz vom Nullprodukt zu lösen · neu oder schon bekannt – je nach Buch (an der Oberschule erst Kl. 10) · P10 · baut auf: lineare Gleichungen, Ausmultiplizieren und Ausklammern, Einsetzen
Einheit 3 von 4 · Normalform und p-q-Formel: Hier lernst du, eine quadratische Gleichung in die Normalform zu bringen und mit der p-q-Formel zu lösen · neu in diesem Jahr (an der Oberschule je nach Buch Kl. 9 oder 10) · P10 oft · baut auf: Wurzelziehen (Einheit 1), Ausmultiplizieren und Ordnen (Einheit 2), binomische Formeln
Einheit 4 von 4 · Sachaufgaben: Hier lernst du, zu Zahlenrätseln und Rechtecken eine quadratische Gleichung aufzustellen, sie zu lösen und die passende Lösung auszuwählen · neu in diesem Jahr (an der Oberschule je nach Buch Kl. 9 oder 10) · keine P10-Aufgabe · baut auf: Einheit 1 bis 3, Gleichungen aufstellen
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Abweichungen: ohne Ausblick, weil das Register der Blätter das Thema schon führt (alle Marken liegen ohnehin bei oder vor Kl. 9) · Baustein im Vorspann von Lernblatt und Gesamt: \rechteckrand (Beet mit Weg, Nr. 47 f) · Höhe nach Lehrwerk: Einheit 4 (kein P10-Original, Zielmarke LS-AA Kl. 9 II 6) · Nr. 15, 35, 36 und 40 sind etwa zwei Drittel Seite hoch (unter dem Maß von zwölf Teilaufgaben, daher nicht geteilt), ihre Seiten tragen Restfläche · keine geteilten Hauptnummern, keine Zwischensprossen · Papier der OS-Originale als „FOR“ angenommen · Kopfzeile der Zone zeigt „Kennst du schon“ doppelt (Blattname und Kurzform der Vorlage) · kein Weiter-Stempel (Testlauf ohne Halt)
2. Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (8 Fertigkeiten; 7 Erkennungsschritte als Nr. 12, 13, 24, 32, 33, 34, 45), Sprossen, Typische Fehler, Prüfungsform und Zielmarke; nicht gebraucht Merkkasten, Grundvorstellung, Verortung · Befunde: der Erkennungsschritt „Zwei, eine oder keine?“ braucht den Fall rechts null, x² = 0 ist aber Kastengleichung (ausgewichen auf 5x² = 0); die Prüfungshöhe von Einheit 1 (2021-OS-K7c) enthält „Gleichung ohne Lösung angeben“, das die Kette davor als eigene Sprosse führt (hier verfremdet als „rechte Seite ändern“); der Typ „Quadrat mit Rand (Vorrat)“ hat keine Sprosse in der Kette (in Nr. 47 f als Beet mit Weg gebaut); Einheit 3 führt vier Originale, das Blatt trägt je Hauptnummer eine Prüfungshöhe (2020-OS-K3e in Nr. 29, 2023-OS-K4c in Nr. 41, 2022-OS-K3c in Nr. 44; 2025-OS-K5c und 2017-OS-K5d nicht verwendet); der Eintrag nennt für die OS-Originale kein Papierkürzel · Spannen: Einheit 1 und 2 GYM Kl. 8–9 → „neu oder schon bekannt – je nach Buch“; Oberschul-Zusatz bei Einheit 1, 3, 4 „je nach Buch Kl. 9 oder 10“, bei Einheit 2 „erst Kl. 10“
4. Protokoll-Archiv: QuadratischeGlg_2026-09-26_protokoll.zip
```

PDFs:

- [QuadratischeGlg_Gesamt.pdf](2-quadgl-9-gym/QuadratischeGlg_Gesamt.pdf)
- [QuadratischeGlg_KennstDuSchon.pdf](2-quadgl-9-gym/QuadratischeGlg_KennstDuSchon.pdf)
- [QuadratischeGlg_Lernblatt.pdf](2-quadgl-9-gym/QuadratischeGlg_Lernblatt.pdf)
- [QuadratischeGlg_Loesungen.pdf](2-quadgl-9-gym/QuadratischeGlg_Loesungen.pdf)
- Zwischenkompilate der Sitzung: probe_e1_a.pdf, probe_e1_l.pdf, probe_e2_a.pdf, probe_e2_l.pdf, probe_e3_a.pdf, probe_e3_l.pdf, probe_e4_a.pdf, probe_e4_l.pdf, probe_zone_l.pdf

Worauf beim Gegenlesen achten:

- dieselben Zweige wie Nr. 1 mit gekippten Zeitmarken (GYM Kl. 8–9)
- Zusatz „an der Oberschule erst Kl. 10"
- Messung: QuadratischeGlg_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 24 von 48 (alle Einheiten); ohne jeden Treffer: E1 x² = c ohne Quadratzahl (Wurzel stehen lassen, Näherungswert mit dem Taschenrechner); E3 p ungerade: p halbe als Dezimalzahl.
- v4.4-Prüfpunkt: QuadratischeGlg_Gesamt.pdf – g) zeiten.txt: nein (fehlt: weiter) (Soll ja).
- Messung: 76 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 3 prozent-7-schwach

Eingabe: „prozentrechnung 7 schwach“ – an die Sitzung: „prozentrechnung 7 schwach – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Kl. 7, Standpunkt Oberschule (Gymnasium als Zusatz) · mit Wiederholung, ohne Ausblick (Thema im Register der Blätter) · Einheit 1 „Prozente als Anteile“ (OS Kl. 6) liegt in der Zone · 4 Zweige · Zone aus 7 Fertigkeiten und dem Fehler-Paar (Nr. 1–11)
1 · Prozentsatz berechnen: Hier lernst du auszurechnen, wie viel Prozent ein Teil vom Ganzen ist · neu in diesem Jahr · P10 oft · baut auf: Prozent am Streifen (Nr. 1–3), Bruch auf den Nenner 100 (Nr. 4), Runden (Nr. 6), Dreisatz (Nr. 8)
2 · Prozentwert berechnen: Hier lernst du auszurechnen, wie viel ein Anteil in Prozent von einer Größe ist · neu in diesem Jahr · P10 · baut auf: Streifen einteilen (Nr. 13), Bruch als Dezimalzahl (Nr. 5), durch 100 teilen (Nr. 7), Dreisatz (Nr. 8), Bruchteil einer Größe (Nr. 9)
3 · Grundwert berechnen: Hier lernst du, aus einem Teil und seinem Anteil in Prozent das Ganze auszurechnen · neu in diesem Jahr · P10 oft · baut auf: Prozentwert (Einheit 2), Streifen einteilen (Nr. 13), Dreisatz (Nr. 8)
4 · Prozentuale Veränderung: Hier lernst du auszurechnen, wie sich ein Wert ändert, wenn er um einige Prozent steigt oder fällt · neu in diesem Jahr oder erst in Klasse 8 – je nach Buch (am Gymnasium in Klasse 7) · P10 oft · baut auf: Prozentsatz (Einheit 1), Prozentwert (Einheit 2), Grundwert (Einheit 3), Runden (Nr. 6)
```

Ausgabeblock (chat.txt, wortgleich):

```text
Zone: Einheit 1 des Eintrags (Prozente als Anteile, Marke OS Kl. 6) steht als Fertigkeit in der Zone (Nr. 1–3 mit der Grundvorstellung), nicht als Zweig; kein Ausblick-Zweig, weil das Register der Blätter das Thema führt.
Zone: Grundvorstellung auf drei Hauptnummern verteilt (Nr. 1 ablesen, Nr. 2 einzeichnen, Nr. 3 von 10 % auf das Ganze), weil es drei Antwortformen sind.
Geteilte Hauptnummern: 15/16, 18/19, 24/25, 44/45.
Zwischensprossen: Nr. 16 d (erst kürzen, dann erweitern), Nr. 17 b (Teil als Dezimalzahl), Nr. 26 b (Ganzes unter 100, 1 % als Dezimalzahl), Nr. 37 b (Rest zu 100 % zuerst bilden).
Prüfungshöhe nicht in der letzten Verfahrens-Hauptnummer: Einheit 2 in Nr. 29 (P10 2021 OS), weil Nr. 30 (über 100 %) eine eigene Fertigkeit ist; Einheit 4 in Nr. 47 (P10 2026 FOR) und Nr. 51 (P10 2025 OS), weil die Kette dort nach Form zerfällt.
Typ „Mehrwertsteuer in Euro“ (Einheit 2) steht in keiner Kette und ist die Anwendung Nr. 33.
Im Quelltext definiert: \abhakverf (kursive Verfahrenszeile auf der Abhakseite über \abhakgruppe), weil die Vorlage nur eine Gruppenebene kennt.
Vorlage: Kopfzeile der Zone doppelt („Prozentrechnung · Kennst du schon · Kennst du schon“); \dreieckrw setzt immer die Eckpunktnamen A, B, C (Nr. 51, gegen 3.6); Streifen in \swz ragen 2–12 pt über den Satzspiegel (Overfull hbox).
Stempel „e 2“ in eigenem Aufruf direkt nach der Durchsicht gesetzt, nicht im Prüfaufruf.
Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (Fertigkeiten und Erkennungsschritte), Für schwache Schüler (Sprossen, Grundvorstellung), Typische Fehler, Prüfungsform/Zielmarke, Merkkasten (bei schwach am Zweigende); nicht gebraucht Verortung. Befunde: Einheit 1 trägt OS Kl. 6, zwei ihrer Typen aber [OS 7] – bei Kl. 7 Oberschule fällt sie in die Zone, obwohl Typen neu sind; die Ketten „Prozentsatz“ und „Grundwert“ nennen als Vorstufe Streifenaufgaben mit Zahlergebnis (als Verfahrens-Hauptnummern Nr. 14 und 35 gesetzt); Kettenlücken Kürzen vor dem Erweitern (Einheit 2) und Rest zu 100 % (Einheit 4). Spannen: Einheit 5 „OS Kl. 7–8“ bei Eingabeklasse 7 als „neu in diesem Jahr oder erst in Klasse 8 – je nach Buch“ aufgelöst (die Regel „neu oder schon bekannt“ passt an der unteren Grenze nicht); Typ „Prozentsatz über 100 %“ [OS 7–8] als „je nach Buch erst in Klasse 8“; Typklammern [OS 9] Faktor, [OS 10] Steigung, [OS 7] Brutto/Netto am Titel.
Protokoll-Archiv: Prozentrechnung_2026-09-26_protokoll.zip
```

PDFs:

- [Prozentrechnung_Gesamt.pdf](3-prozent-7-schwach/Prozentrechnung_Gesamt.pdf)
- [Prozentrechnung_KennstDuSchon.pdf](3-prozent-7-schwach/Prozentrechnung_KennstDuSchon.pdf)
- [Prozentrechnung_Lernblatt.pdf](3-prozent-7-schwach/Prozentrechnung_Lernblatt.pdf)
- [Prozentrechnung_Loesungen.pdf](3-prozent-7-schwach/Prozentrechnung_Loesungen.pdf)

Worauf beim Gegenlesen achten:

- Form nach 2.8: Darstellung neben jeder Teilaufgabe
- Raster je Schritt
- Päckchen mit Erklärzeile
- Kasten am Zweigende
- Zone mit Grundvorstellung
- Messung: Prozentrechnung_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 17 von 44 (alle Einheiten); ohne jeden Treffer: E1 Anteilsaussage prüfen und korrigieren (Tabellenwerte); E2 Umkehrung: zu einem Prozentsatz ein Zahlenpaar angeben; E4 glatte Sätze (50 %, 25 %, 20 %, 10 %: mal 2, 4, 5, 10).
- v4.4-Prüfpunkte: Prozentrechnung_Gesamt.pdf – a)–g) erfüllen ihr Soll.
- Messung: 107 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 4 linfkt-8-neu

Eingabe: „lineare funktionen 8 nur das neue“ – an die Sitzung: „lineare funktionen 8 nur das neue – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Oberschule als Standpunkt (Gymnasium gleich, alle Zweige Kl. 8) · 5 Zweige, alle neu in Kl. 8 · ohne Zone
Einheit 1 von 5 · Proportionale Funktion – Hier lernst du, Funktionen y = m · x zu zeichnen, abzulesen und aufzustellen · neu in diesem Jahr · P10 oft · baut auf: Dreisatz, proportionale Zuordnung, Koordinatensystem
Einheit 2 von 5 · Lineare Funktion f(x) = m · x + n – Hier lernst du, Geraden mit f(x) = m · x + n zu zeichnen und m und n abzulesen und zu deuten · neu in diesem Jahr · P10 oft · baut auf: proportionale Funktion (Einheit 1), Brüche, negative Zahlen
Einheit 3 von 5 · Punkte und Werte – Hier lernst du, Funktionswerte zu berechnen, Punkte zu prüfen und Nullstellen und Achsenschnittpunkte zu bestimmen · neu in diesem Jahr · P10 oft · baut auf: lineare Funktion (Einheit 2), Gleichungen lösen, negative Zahlen
Einheit 4 von 5 · Gleichung bestimmen – Hier lernst du, die Gleichung einer Geraden aus dem Graphen, aus Steigung und Punkt oder aus zwei Punkten zu bestimmen und Schnittpunkte zu berechnen · neu in diesem Jahr · P10 · baut auf: m und n ablesen (Einheit 2), Punktprobe (Einheit 3), Gleichungen lösen, Terme zusammenfassen
Einheit 5 von 5 · Anwendungen – Hier lernst du, Sachsituationen mit linearen Funktionen zu beschreiben und Tarife zu berechnen und zu vergleichen · neu in diesem Jahr · P10 oft · baut auf: Gleichung bestimmen und Schnittpunkt (Einheit 4), Funktionswerte (Einheit 3), Dreisatz
```

Ausgabeblock (chat.txt, wortgleich):

```text
Ohne Zone (Bestellung „nur das Neue“): keine Datei KennstDuSchon, das Gesamt ist inhaltsgleich mit dem Lernblatt (nur Kopfzeile „Gesamt“).
Geteilte Hauptnummern nach 2.3 g: 4/5, 14/15, 26/27, 36/37, 39/40.
Höhe nach Lehrwerk: Einheit 1 hat kein P10-Original, Zielmarke Nr. 9 nach RLP F und LISUM-PH Jg. 8; Nr. 18 (Parameter deuten), Nr. 28 (Achsenschnittpunkte) und Nr. 39/40 (Schnittpunkt rechnerisch) haben im Eintrag keine Sprossenkette, die Kette ist nach Lehrwerk gebildet und endet ohne Original.
Über die Pflichtelemente jedes Zweigs (Fehler finden, Begründen, Anwendung) ist die Zwischenzeile „Prüfen, begründen, anwenden“ gesetzt, damit jede Hauptnummer unter einer Überschrift steht; sie ist keine Verfahrensüberschrift im Sinn von 2.3 b.
Zeiten gemessen; Stempel „zone“ und „weiter“ fehlen, weil es ohne Zone keinen Halt gab; „e 1“ steht vor der Sichtprüfung, die Layoutkorrektur von Einheit 1 lag danach.
Katalogzeile: gebraucht Lerneinheiten, Marken, Typen je Lerneinheit, Voraussetzungen (Erkennungsschritte → Vorstufen Nr. 10–12, 22, 45; Fertigkeiten nur für „baut auf“), Sprossen je Verfahrenstyp, Typische Fehler, Prüfungsform und Zielmarke; nicht gebraucht Merkkasten, Verortung, Grundvorstellung. Befund: Die Erkennungsschritte „Steigungsdreieck lesen“ (wie viel nach oben) und „Punkt einsetzen … rechne aus“ verlangen eine Zahl – umgesetzt als Einzeichnen (Nr. 12) und Einsetzen ohne Ausrechnen (Nr. 22), das Ausrechnen steht in Nr. 16 und Nr. 23. Für Einheit 4 fehlt eine Kette zum Schnittpunkt rechnerisch. Keine Marke trägt eine Spanne; alle Zweige sind OS Kl. 8 · GYM Kl. 8, Zeitmarke durchgehend „neu in diesem Jahr“.
Protokoll-Archiv: LinFkt_2026-09-26_protokoll.zip
```

PDFs:

- [LinFkt_Gesamt.pdf](4-linfkt-8-neu/LinFkt_Gesamt.pdf)
- [LinFkt_Lernblatt.pdf](4-linfkt-8-neu/LinFkt_Lernblatt.pdf)
- [LinFkt_Loesungen.pdf](4-linfkt-8-neu/LinFkt_Loesungen.pdf)
- Zwischenkompilate der Sitzung: e1_test.pdf, e1l_test.pdf, e2_test.pdf, e2l_test.pdf, e3_test.pdf, e3l_test.pdf, e4_test.pdf, e4l_test.pdf, e5_test.pdf, e5l_test.pdf

Worauf beim Gegenlesen achten:

- keine Zone, kein PDF KennstDuSchon
- Zweigzeilen „neu in diesem Jahr"
- Grafiken auf Gitter
- Wertetabellen
- Halbseitenmaß
- Messung: LinFkt_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 8 von 33 (alle Einheiten).
- v4.4-Prüfpunkte: LinFkt_Gesamt.pdf – a)–g) erfüllen ihr Soll.
- Messung: 119 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 5 kreis-8-ausblick

Eingabe: „kreis 8 mit ausblick“ – an die Sitzung: „kreis 8 mit ausblick – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Kl. 8, Oberschule als Standpunkt (Gymnasium mit gleichen Marken) · mit Wiederholung · mit Ausblick: kein Zweig nach Kl. 8 · 3 Zweige · Zone aus 6 Fertigkeiten
Einheit 1 · Kreisumfang: Hier lernst du, den Umfang eines Kreises aus Radius oder Durchmesser zu berechnen und umgekehrt · neu oder schon bekannt – je nach Buch · P10 · baut auf: Kommazahlen und Runden, Umfang und Fläche, Formeln umstellen
Einheit 2 · Kreisfläche: Hier lernst du, die Fläche eines Kreises zu berechnen und aus der Fläche den Radius · neu oder schon bekannt – je nach Buch · P10 oft · baut auf: Kreisumfang (Einheit 1), Quadrieren und Wurzelziehen, Formeln umstellen
Einheit 3 · Kreisteile: Hier lernst du, Anteil, Bogen und Fläche eines Kreisausschnitts aus dem Mittelpunktswinkel zu berechnen · neu oder schon bekannt – je nach Buch, manche Bücher erst Kl. 9 · P10 · baut auf: Kreisumfang (Einheit 1), Kreisfläche (Einheit 2), Winkel, Anteile als Bruch und Prozent
```

Ausgabeblock (chat.txt, wortgleich):

```text
Abweichung: kein Rechenplatz auf dem ganzen Blatt – alle Verfahren sind Geometrie (2.3 b); Umkehrungen als eigene Hauptnummer (Nr. 17, 28, 35).
Abweichung: Original von Einheit 3 (Glücksrad, P10 2025 OS) am Ende von Nr. 34 (Anteil in Prozent), nicht in der letzten Verfahrensnummer – Bogen, Ausschnitt und Ring (Nr. 36–39) enden auf ihrer höchsten Sprosse; in Einheit 1 und 2 trägt die letzte Verfahrensnummer das Original (Nr. 18 Dosenetikett, P10 2022 OS; Nr. 28 Brunnen, P10 2016 OS).
Abweichung: Zwischensprossen Nr. 18 c (Halbkreis mit Durchmesser), Nr. 28 c (Durchmesser aus der Fläche), Nr. 39 c (Ring aus der Breite); Höhe nach Lehrwerk bei Bogenlänge, Ausschnittsfläche, Ausschnittsumfang und Kreisring (Nr. 36–39), weil der Eintrag dort kein Original führt.
Abweichung: im Vorspann definiert \zeichenplatz (Zeichenfläche mit vorgegebenem M, Nr. 14) und für das Zonen-PDF \zonekopf – \einheitenkopf verdoppelt dort die Kopfzeile („Kreis · Kennst du schon · Kennst du schon“) oder setzt bei leerer Kurzform einen leeren Punkt.
Abweichung: Zeiten gemessen; Stempel zone vor zwei Kopfzeilen-Korrekturen gesetzt, Stempel e 1 im Aufruf nach der Sichtprüfung.
Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen mit Erkennungsschritten, Typische Fehler, Sprossen, Prüfungsform und Zielmarke; Merkkasten nur als Sperrliste, Verortung und Grundvorstellung nicht.
Katalog-Befund: Erkennungsschritt „Radius oder Durchmesser?“ verlangt eine Zahl (d → r) – Vorstufe Nr. 10 als Ankreuzen, Umrechnen als erste Verfahrensnummer Nr. 12; „Welcher Teil vom Kreis?“ verlangt einen Bruch – Vorstufe Nr. 33 mit Wortnamen (Halbkreis …), Bruch erst in Nr. 34; Marken-Zeile Einheit 1 sagt „P10“, Prüfungsform nur Nebenleistung; kein Original zu Bogen, Ausschnitt, Ring.
Katalog-Spannen: Einheit 1 und 2 OS/GYM Kl. 7–8, Einheit 3 Kl. 7–9 – Kl. 8 liegt jeweils in der Spanne → „neu oder schon bekannt – je nach Buch“ (Einheit 3 mit „manche Bücher erst Kl. 9“); Typklammer [OS 5, GYM 5–6] → „kennst du seit Klasse 5“ (Nr. 13); [OS 5–8] Kreis zeichnen wie die Einheit, ohne Klammer.
Protokoll-Archiv: Kreis_2026-09-26_protokoll.zip
```

PDFs:

- [Kreis_Gesamt.pdf](5-kreis-8-ausblick/Kreis_Gesamt.pdf)
- [Kreis_KennstDuSchon.pdf](5-kreis-8-ausblick/Kreis_KennstDuSchon.pdf)
- [Kreis_Lernblatt.pdf](5-kreis-8-ausblick/Kreis_Lernblatt.pdf)
- [Kreis_Loesungen.pdf](5-kreis-8-ausblick/Kreis_Loesungen.pdf)
- Zwischenkompilate der Sitzung: e1_pruef.pdf, e2_pruef.pdf, e3_pruef.pdf, probe.pdf

Worauf beim Gegenlesen achten:

- Typklammer „kennst du seit Klasse 5" am Zeichnen-Typ
- Zeichenflächen mit 8-mm-Karo
- kein Ausblick-Zweig (alle Marken bei Kl. 7–8)
- die Deutungszeile nennt ‚mit Ausblick' ohne Zweig
- Messung: Kreis_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 12 von 25 (alle Einheiten); ohne jeden Treffer: E1 Halbkreisbogen (mit und ohne Durchmesser); E1 Sachaufgabe (Rad: Weg bei mehreren Umdrehungen; Baumstamm; Reifen); E2 Sachaufgabe (Abwurfring, Pizza, Deckel, Grundfläche eines Kegels oder Zylinders); E3 Bogenlänge b = α/360° · 2 · π · r; E3 Ausschnittsfläche A = α/360° · π · r²; E3 Sachaufgabe (Rasensprenger, Tortenstück, Sektor im Kreisdiagramm).
- v4.4-Prüfpunkte: Kreis_Gesamt.pdf – a)–g) erfüllen ihr Soll.
- Messung: 95 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 6 daten-7

Eingabe: „daten 7“ – an die Sitzung: „daten 7 – Antworten auf Planfrage und Zone: sek i, alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Kl. 7, Standpunkt Oberschule (Gymnasium als Zusatz) · Sek I: Einheit 6 und die Sek-II-Zeilen weggelassen · mit Wiederholung, ohne Ausblick (das Register führt daten seit 22.09.): Einheit 7 Vierfeldertafel (Kl. 9) nicht gebaut · Einheit 1, 2 und 4 (Marke vor Kl. 7) als Fertigkeiten in der Zone · 2 Zweige · Zone aus 9 Fertigkeiten und dem Fehler-finden-Paar (Nr. 1–11)
Einheit 1 von 2 · Streifen- und Kreisdiagramm: Hier lernst du, Anteile als Streifen und als Kreisdiagramm darzustellen · neu oder schon bekannt – je nach Buch (am Gymnasium schon seit Klasse 6) · P10 oft · baut auf: Prozentsatz (Nr. 1–2), relative Häufigkeit (Nr. 3), Winkel (Nr. 5–6), Längen (Nr. 7)
Einheit 2 von 2 · Diagramme beurteilen und Boxplot: Hier lernst du, Aussagen zu Diagrammen zu prüfen, Täuschungen zu erkennen und Boxplots zu lesen · neu oder schon bekannt – je nach Buch (am Gymnasium neu in diesem Jahr) · P10 · baut auf: Säulendiagramme lesen (Nr. 4), Kenngrößen (Nr. 8), Bruchteile (Nr. 9), Prozentsatz (Nr. 1)
```

Ausgabeblock (chat.txt, wortgleich):

```text
Zeitachse Kl. 7 (Standpunkt Oberschule): Einheit 1, 2 und 4 liegen mit ihrer Marke vor Kl. 7 und stehen nur mit ihrem Grundfall in der Zone (Nr. 3, 4, 8); ihre übrigen Typen (u. a. Klassen bilden und auszählen [OS 8–9], Achseneinteilung aus einer Säule, arithmetisches Mittel, fehlender Wert aus dem Mittel) stehen nicht auf dem Blatt.
Weggelassen: Einheit 6 und die Sek-II-Zeilen der Einheiten 1 und 4 (Sek I); Einheit 7 Vierfeldertafel (Kl. 9) nicht gebaut, weil das Register daten schon führt und damit kein Ausblick bestellt ist.
Keine Planfrage: Kl. 7 löst die Stufe, der Plan hat zwei Zweige; die Antwort „sek i, alle“ deckt sich damit.
Zwischensprossen: Streifen ohne Teilstriche (Nr. 14 e–f), Anteil als Bruch zum Winkel (Nr. 16 g), fast gleich große Sektoren (Nr. 21 a).
Höhe nach Lehrwerk: Boxplot (Nr. 32–34) hat kein P10-Original; Decke ist „zwei Boxplots vergleichen und beurteilen“. Nr. 14, 16–19 enden auf ihrer höchsten Sprosse, die Originale tragen Nr. 15 d, 21 b, 26 f, 27 f und 31 a.
Reihenfolge: Boxplot steht als eigenes Verfahren nach dem Original 2019-OS-K5c (Nr. 31), nicht wie in der Kette davor.
Geteilte Hauptnummern: 20/21 (Sektoren zuordnen), 30/31 (Trend und Zeitungsdiagramm).
Keine im Vorspann definierten Bausteine, keine vereinfachten Grafiken; Zeiten gemessen.
Katalog: gebraucht wurden Lerneinheiten, Marken, Typen je Einheit, Voraussetzungen (Fertigkeiten und Erkennungsschritte), Sprossen, Typische Fehler und Prüfungsform (P10) mit Zielmarke; der Merkkasten nur als Sperre; Verortung, Prüfungsform fhr/abi/iqb und die Sek-II-Teile nicht.
Befund Katalog: Der Erkennungsschritt „Wo fängt die Achse an?“ verlangt mit „sonst den Startwert notieren“ eine Zahl; umgesetzt als „umkreise den Startwert“ (Nr. 25).
Befund Katalog: Die Kette der Einheit 5 stellt „Boxplot lesen (Vorrat)“ vor die Prüfungshöhe 2019-OS-K5c, die aber Verlauf und Achse prüft; Boxplot braucht eine eigene Kette mit eigener Decke. „Gedehnte Achse“ steht in keiner Kette und hat kein Original.
Befund Katalog: „Addieren und Dividieren mit Dezimalzahlen und Runden“ trägt nur „– Einheit 4“, „Zahlen ordnen, Skalen ablesen“ nur „– Einheit 2 und 4“; gebraucht werden beide auch in Einheit 3 (Winkel runden) und 5 (Skala, Boxplot). Hier sind sie in Nr. 1 e und Nr. 4 und 8 aufgefangen.
Spannen: Einheit 3 (OS Kl. 6–7) und Einheit 5 (OS Kl. 6–9) enthalten Kl. 7, deshalb „neu oder schon bekannt – je nach Buch“; beide stehen auf dem Blatt. Einheit 4 (GYM Kl. 6–7) wäre am Gymnasium ebenfalls ein Zweig, am Standpunkt Oberschule (OS Kl. 6) liegt sie in der Zone.
Typklammern: Kreisdiagramm [OS 6] → „kennst du wahrscheinlich seit Klasse 6“, Trend [OS 9] → „kommt in Klasse 9“, Boxplot lesen [OS 8–9] → „kommt in Klasse 8, je nach Buch bis Kl. 9“.
Protokoll-Archiv: Daten_2026-09-26_protokoll.zip
```

PDFs:

- [Daten_Gesamt.pdf](6-daten-7/Daten_Gesamt.pdf)
- [Daten_KennstDuSchon.pdf](6-daten-7/Daten_KennstDuSchon.pdf)
- [Daten_Lernblatt.pdf](6-daten-7/Daten_Lernblatt.pdf)
- [Daten_Loesungen.pdf](6-daten-7/Daten_Loesungen.pdf)
- Zwischenkompilate der Sitzung: pruef_e1.pdf, pruef_e2.pdf

Worauf beim Gegenlesen achten:

- keine Stufenfrage, weil die Klasse 7 genannt ist
- Einheit 6 weggelassen und in der Deutungszeile genannt
- neue Klassen-Typen in Einheit 1 als Sprosse oder Hauptnummer
- Säulendiagramme mit Bausteinen
- Messung: Daten_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 46 von 73 (alle Einheiten); ohne jeden Treffer: E1 Häufigkeitstabelle aus einer Urliste; E4 Modalwert; E7 Tafel aus einem Text aufstellen (Merkmale benennen, Zahlen einordnen).
- v4.4-Prüfpunkte: Daten_Gesamt.pdf – a)–g) erfüllen ihr Soll.

## 7 nullstellen-fokus

Eingabe: „nullstellen“ – an die Sitzung: „nullstellen – Antworten auf Planfrage und Zone: quadratische-funktionen; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Fokus Nullstellen · ohne Klasse, Marken absolut
```

Ausgabeblock (chat.txt, wortgleich):

```text
Abweichung: Zwischensprossen ergänzt – Scheitelpunktform: Plus in der Klammer, nach unten geöffnet; p-q-Formel: q negativ, p ungerade, eine Nullstelle (berührt), keine Nullstelle · geteilte Hauptnummern 7/8 und 13/14 · Streckfaktor vor den nicht ganzzahligen Nullstellen (Aufwand nach Struktur, 2.4 b) · Prüfungshöhe 2017-OS-K5d ohne den Nachweis durch Ausmultiplizieren (Stoff von Einheit 3), Scheitelpunktform vorgegeben · Funktionsname f statt p (p ist in der p-q-Formel belegt) · keine Abhakseite im Fokus
Katalog: gebraucht Lerneinheiten (Einheit 4), Marken, Typen Einheit 4, Voraussetzungen (Quadrieren, Wurzel, quadratische Gleichung, Nullstelle der Geraden; Erkennungsschritt „Was wird gleichgesetzt?“ als Vorstufe Nr. 6), Sprossen Einheit 4, Typische Fehler (nur eine Lösung, Vorzeichen in der Klammer, p-q-Formel), Prüfungsform (2017-OS-K5d, 2020-OS-K3e, 2025-OS-K5c); nicht gebraucht Merkkasten, Verortung, Grundvorstellung, Fertigkeiten Koordinaten, binomische Formel, lineare Gleichung, Schnittpunkt zweier Geraden · gefehlt: Kette Einheit 4 ohne Sprossen für Vorzeichen in der Klammer, Öffnung nach unten, q negativ, p ungerade, Diskriminante null oder negativ; Stichwort „nullstellen“ allein führt auf zwei Einträge, geführt ist nur „nullstellen parabel“ · Marke Einheit 4 ohne Spanne (OS Kl. 10 · GYM Kl. 9), Zeitmarke „ab Kl. 10 (am Gymnasium ab Kl. 9)“
Protokoll-Archiv: QuadratischeFkt_2026-09-26_protokoll.zip
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
- Messung: QuadratischeFkt_Fokus_Nullstellen.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 41 von 49 (alle Einheiten); ohne jeden Treffer: E1 Wertetabelle zu p(x) = x² ausfüllen (auch negative x); E1 Punkte eintragen und Normalparabel zeichnen (Bogen, kein Lineal); E1 Eigenschaften nennen (Scheitel, Symmetrieachse, Öffnung, kleinster Wert); E1 Punktprobe rechnerisch; E1 Wertetabelle zu p(x) = a·x² ausfüllen und zuordnen; E1 Parabelgleichung zu Graph zuordnen über Öffnung, Streckung und Startwert, mit Begründung; E3 y-Achsenabschnitt q aus der Normalform ablesen; E3 Nachweis „Normalform stimmt“ (Behauptung prüfen); E4 vorher durch den Streckfaktor teilen; E4 Punktprobe als Schnittpunkt-Nachweis (in beide Funktionen einsetzen).
- v4.4-Prüfpunkte: QuadratischeFkt_Fokus_Nullstellen.pdf – a)–g) erfüllen ihr Soll.

## 8 potenz-10

Eingabe: „potenz-exponentialfunktionen 10“ – an die Sitzung: „potenz-exponentialfunktionen 10 – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Kl. 10 Oberschule, Gymnasium als Zusatz · mit Wiederholung · mit Ausblick: kein Zweig nach Kl. 10 · 5 Zweige · Zone aus 8 Fertigkeiten
Einheit 1 von 5 · Lineares und exponentielles Wachstum unterscheiden — Hier lernst du, lineares und exponentielles Wachstum an Tabelle, Text und Graph zu unterscheiden · neu in diesem Jahr · P10 oft · baut auf: Punkte eintragen, gleicher Betrag je Schritt, Erhöhen um p %
Einheit 2 von 5 · Wachstumsfaktor und Wachstumstabelle — Hier lernst du, aus einem Prozentsatz den Wachstumsfaktor zu bilden und Wachstumstabellen zu ergänzen · neu in diesem Jahr · P10 oft · baut auf: Differenz oder Quotient (Einheit 1), Erhöhen um p %, Quotient zweier Werte
Einheit 3 von 5 · Exponentialfunktion aufstellen und auswerten — Hier lernst du, eine Wachstumsgleichung N(t) = N₀ · qᵗ aufzustellen, zu deuten und damit Werte und Schwellen zu berechnen · neu in diesem Jahr · P10 · baut auf: Wachstumsfaktor und Tabelle (Einheit 2), Potenz mit dem Taschenrechner
Einheit 4 von 5 · Verdopplungs- und Halbwertszeit — Hier lernst du, die Zeit zu bestimmen, nach der sich ein Wert verdoppelt oder halbiert hat · neu in diesem Jahr · P10 · baut auf: Wachstumstabelle (Einheit 2), Wachstumsgleichung (Einheit 3), Werte am Graphen ablesen
Einheit 5 von 5 · Potenzfunktionen mit natürlichem Exponenten — Hier lernst du Potenzfunktionen wie y = x³ und y = x⁴ kennen: Wertetabelle, Graph, Symmetrie und Funktionswerte · neu in diesem Jahr (am Gymnasium schon seit Klasse 9) · keine P10-Aufgabe · baut auf: Potenz mit dem Taschenrechner, Punkte eintragen, Normalparabel
```

Ausgabeblock (chat.txt, wortgleich):

```text
Abweichungen: kein Ausblick-Zweig (alle Marken bei Kl. 10 oder davor) · geteilte Hauptnummern: 23/24, 34/35/36, 58/59 · im Vorspann definiert: \leeresgitter (leeres Karo ohne Bezifferung für Nr. 25 „Achseneinteilung wählen“) · Einheit 5: Kette, Fehler finden und Decke nach Lehrwerk-Konvention (Eintrag ohne Sprossen, Fehler und Zielmarke, keine P10-Aufgabe) · Zwischensprosse 33 f (Wachstumsrate aus zwei nicht benachbarten Werten über q²) · Logarithmus (Vorrat) als oberste Sprosse 54 h · Kopfzeile der Zonen-Datei trägt „Kennst du schon“ doppelt (Kurzform der Vorlage zusätzlich zur Blattbezeichnung) · Zeiten: Stempel „e 1“ fehlt (nicht im Prüfaufruf gesetzt), „weiter“ ohne Klick
Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (Fertigkeiten und Erkennungsschritte), Sprossen, Typische Fehler, Prüfungsform/Zielmarke; nicht gebraucht Merkkasten, Verortung, Grundvorstellung; gefehlt: Einheit 5 ohne Sprossen, Typische Fehler, Zielmarke und Blatt-0-Fertigkeit · Befund: Erkennungsschritte „Differenz oder Quotient?“ und „Welcher Schritt ist null?“ verlangen Zahlen – als Vorstufe ohne Ergebnis gesetzt (Nr. 14 mit vorgedruckten Differenzen und Quotienten, Nr. 40 nur Startjahr und Zieljahr markieren), das Rechnen steht in Nr. 16/17 und 44 f · keine Marke mit Spanne; Einheit 5 (OS 10 · GYM 9) als „neu in diesem Jahr (am Gymnasium schon seit Klasse 9)“; „nicht für alle“-Zusätze ohne Klassenzahl (Sekundo LVL/Zusatzstoff) nicht auf dem Blatt
Protokoll-Archiv: PotenzUndExponentialFkt_2026-09-26_protokoll.zip
```

PDFs:

- [PotenzUndExponentialFkt_Gesamt.pdf](8-potenz-10/PotenzUndExponentialFkt_Gesamt.pdf)
- [PotenzUndExponentialFkt_KennstDuSchon.pdf](8-potenz-10/PotenzUndExponentialFkt_KennstDuSchon.pdf)
- [PotenzUndExponentialFkt_Lernblatt.pdf](8-potenz-10/PotenzUndExponentialFkt_Lernblatt.pdf)
- [PotenzUndExponentialFkt_Loesungen.pdf](8-potenz-10/PotenzUndExponentialFkt_Loesungen.pdf)
- Zwischenkompilate der Sitzung: probe_e1_a.pdf, probe_e1_l.pdf, probe_e2_a.pdf, probe_e2_l.pdf, probe_e3_a.pdf, probe_e3_l.pdf, probe_e4_a.pdf, probe_e4_l.pdf, probe_e5_a.pdf, probe_e5_l.pdf, probe_zone_l.pdf

Worauf beim Gegenlesen achten:

- neue Einheit 5 Potenzfunktionen als Zweig mit „keine P10-Aufgabe"
- Decke nach Lehrwerk im Ausgabeblock genannt
- Graphen von x³ und x⁴
- Messung: PotenzUndExponentialFkt_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 44 von 62 (alle Einheiten); ohne jeden Treffer: E3 Zeitschritte zählen, wenn Jahreszahlen gegeben sind (Startjahr ist der Schritt null).
- v4.4-Prüfpunkt: PotenzUndExponentialFkt_Gesamt.pdf – g) zeiten.txt: nein (fehlt: e 1) (Soll ja).
- Messung: 87 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 9 kurven-12-be

Eingabe: „kurvenuntersuchung 12 berlin“ – an die Sitzung: „kurvenuntersuchung 12 berlin – Antworten auf Planfrage und Zone: gymnasium, gk; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Q3/Q4 in Berlin, Zeitmarken ab Q1 · mit Wiederholung · mit Ausblick: kein Zweig nach Kl. 12 · 5 Zweige · Zone aus 6 Fertigkeiten
Einheit 1 · Monotonie und erste Ableitung: Hier lernst du, am Vorzeichen der Ableitung abzulesen und am Term nachzuweisen, wo ein Graph steigt oder fällt · kennst du seit Q1 · Abitur GK · baut auf: Gleichungen lösen, Ableitungen bilden
Einheit 2 · Extrempunkte: Hier lernst du, Hoch-, Tief- und Sattelpunkte zu berechnen und an einer gegebenen Stelle nachzuweisen, auch den größten Wert am Rand · kennst du seit Q1 · Abitur GK · baut auf: Monotonie (Einheit 1), Gleichungen lösen, Ableitungen bilden, Funktionswerte
Einheit 3 · Krümmung und Wendepunkte: Hier lernst du, mit der zweiten Ableitung Krümmung und Wendepunkte zu bestimmen und an einer gegebenen Stelle nachzuweisen · kennst du seit Q1 · Abitur GK · baut auf: Extrempunkte (Einheit 2), Gleichungen lösen, Ableitungen bilden
Einheit 4 · Graph und Ableitungsgraph: Hier lernst du, vom Graphen von f auf den Graphen von f' zu schließen und umgekehrt und Graphen aus Eigenschaften zu skizzieren · kennst du seit Q1 oder Q2 – je nach Buch · Abitur GK · baut auf: Einheit 1 bis 3, Ableitung als Steigung
Einheit 5 · Kurvenuntersuchung im Sachzusammenhang: Hier lernst du, Sachfragen in Hoch-, Tief- und Wendepunkte zu übersetzen und die Ergebnisse mit Einheit zu deuten · kennst du seit Q1 · Abitur GK · baut auf: Einheit 1 bis 4, Ableitung als Änderungsrate
```

Ausgabeblock (chat.txt, wortgleich):

```text
Abweichung: kein Zweig abgewählt, kein Ausblick-Zweig (alle Marken Q1 bzw. Q1/2); LK-Stoff weggelassen – Sprossen „genau einen Tiefpunkt über die streng monotone Ableitung“, „Extremstelle einer Logarithmusfunktion“, „zweiten Wendepunkt über die Punktsymmetrie“, „Wendepunkt über den Vorzeichenwechsel von f'' aus der Kettenregel“ und die Typen an Sinus-, Logarithmus- und Scharfunktionen, deshalb Prüfungshöhe Nr. 19 aus IQB 2026 grundlegend statt der LK-Zielmarke; kein Rechenplatz (Sek II); geteilte Hauptnummer Nr. 17/18; Einheit 1 bis 3 mit je zwei, Einheit 5 mit vier Verfahrensüberschriften; Zwischensprosse Nr. 40 b (stärkste Abnahme an einer e-Funktion); keine Bausteine im Vorspann, keine vereinfachten Grafiken; Zeitstempel „weiter“, „e 3“ und „e 4“ verspätet gesetzt (protokoll.txt).
Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (6 Fertigkeiten → Zone Nr. 1–8, 3 Erkennungsschritte → Vorstufen Nr. 15, 16, 37), Sprossen, Typische Fehler, Prüfungsform und Zielmarke; nicht gebraucht Merkkasten, Grundvorstellung, Verortung; Befunde: die Ketten von Einheit 1 und 4 beginnen mit einer „Vorstufe“, die Erkennungsschritte nennen aber keine vor Einheit 1 und 4 (nicht gebaut, die Grundvorstellung trägt Zone Nr. 8); 26 von 76 Haupttypen (Einzeltypen, 8 davon erhöht oder LK) haben keine eigene Sprosse – „jeder Typ eine Sprosse“ ist bei 76 Typen nicht einlösbar, die Ketten tragen die häufigen; die eine Kette von Einheit 5 läuft über vier Formen; die Stand-Zeile trägt Nachzüge vom 28. und 29.09.2026, nach dem Bautag; Spanne nur in Einheit 4 („BE Q1/2“ → „kennst du seit Q1 oder Q2 – je nach Buch“); Prüfungswort aus „GK · Abitur GK · Abitur LK“ als „Abitur GK“.
Vorlage: Kopfzeile der Zonen-Datei doppelt („Kurvenuntersuchung · Kennst du schon · Kennst du schon“), eine leere Kurzform lässt ein „·“ am Ende stehen.
Protokoll-Archiv: Kurvenuntersuchung_2026-09-26_protokoll.zip
```

PDFs:

- [Kurvenuntersuchung_Gesamt.pdf](9-kurven-12-be/Kurvenuntersuchung_Gesamt.pdf)
- [Kurvenuntersuchung_KennstDuSchon.pdf](9-kurven-12-be/Kurvenuntersuchung_KennstDuSchon.pdf)
- [Kurvenuntersuchung_Lernblatt.pdf](9-kurven-12-be/Kurvenuntersuchung_Lernblatt.pdf)
- [Kurvenuntersuchung_Loesungen.pdf](9-kurven-12-be/Kurvenuntersuchung_Loesungen.pdf)
- Zwischenkompilate der Sitzung: _pruef_e1.pdf, _pruef_e2.pdf, _pruef_e3.pdf, _pruef_e4.pdf, _pruef_e5.pdf, _pruef_zone_l.pdf

Worauf beim Gegenlesen achten:

- Sek II: Zeitmarke mit Halbjahr Q1 Berlin
- Kursart GK
- Prüfungswort „Abitur GK"
- Decke Abitur Teil A/B
- kein `\weit`
- Messung: Kurvenuntersuchung_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 71 von 86 (alle Einheiten).
- v4.4-Prüfpunkte: Kurvenuntersuchung_Gesamt.pdf – a)–g) erfüllen ihr Soll.
- Messung: 80 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).

## 10 ka-terme-8-gym

Eingabe: „klassenarbeit terme binomische formeln 8 gymnasium“ – an die Sitzung: „klassenarbeit terme binomische formeln 8 gymnasium – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch“

Deutungszeile und Plan (chat.txt, wortgleich):

```text
→ Lernblatt · Einträge terme.md und binomische-formeln.md · mit Wiederholung · mit Ausblick: kein Zweig nach Kl. 8 · 5 Zweige · Terme Einheit 1 und 2 (GYM Kl. 6–7) in der Zone · Zone aus 7 Fertigkeiten und dem Fehler-finden-Paar
Einheit 1 von 5 · Klammern auflösen: Hier lernst du, Klammern in Termen aufzulösen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Glieder zusammenfassen, Rechnen mit Vorzeichen
Einheit 2 von 5 · Ausklammern: Hier lernst du, einen gemeinsamen Faktor auszuklammern · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Klammern auflösen (Einheit 1)
Einheit 3 von 5 · Summe mal Summe: Hier lernst du, Terme mit zwei Variablen umzuformen und zwei Klammern miteinander malzunehmen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Klammern auflösen (Einheit 1), Terme malnehmen
Einheit 4 von 5 · Binomische Formeln: Hier lernst du, Quadrate von Klammern mit den binomischen Formeln auszumultiplizieren · neu in diesem Jahr · P10 · baut auf: Klammer mal Klammer (Einheit 3), Quadratzahlen
Einheit 5 von 5 · Faktorisieren: Hier lernst du, eine Summe mit den binomischen Formeln in ein Produkt zu verwandeln · neu in diesem Jahr · keine P10-Aufgabe · baut auf: Ausklammern (Einheit 2), binomische Formeln (Einheit 4), Quadratwurzeln
```

Ausgabeblock (chat.txt, wortgleich):

```text
1. Abweichungen: keine Planfrage (Klassenarbeit, 1.3) – das „alle“ der Eingabe ist gegenstandslos · Zone und Rest in einem Durchgang (unbeaufsichtigt, „weiter“ aus der Eingabe) · Zwischensprossen: Nr. 12 k Variable mal Klammer (gebraucht für die Probe in Einheit 2), Nr. 24 Klammer mit zwei Variablen als eigene Hauptnummer mit Grundfall · Höhe ohne Original nach der Zielmarke des Eintrags: Nr. 13 g, 17 j, 25 j, 42 j · geteilte Hauptnummer: 32/33 · Original 2022-OS-K3c (Scheitelpunktform mit Gerade gleichsetzen) nicht verwendet, es braucht quadratische Gleichungen (Kl. 9); Nr. 33 f trägt 2022-GYM-B2b, Nr. 34 d 2017-OS-K5d, Nr. 37 c 2019-GYM-B1f · im Vorspann definierter Baustein: \flaechenbild (Rechteck mit geteilten Seiten und vier Teilflächen, Nr. 27, 38, 39) · Vorlage: Kopfzeile des Zone-PDFs trägt „Kennst du schon“ doppelt
2. Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen, Erkennungsschritte, Sprossen, Typische Fehler, Prüfungsform und Zielmarke beider Einträge; nicht gebraucht Merkkasten (kein „mit kasten“), Grundvorstellung (nicht schwach), Verortung (die Nachbarthemen – Scheitelpunktform, Produktform – stehen schon als Sprossen in der Kette) · Befunde: die Erkennungsschritte „Ist das ein Quadrat? … Wurzel daneben schreiben“ und „Passt das Mittelglied? … doppeltes Produkt bilden“ (binomische-formeln.md, vor Einheit 3) verlangen ein Ergebnis – auf dem Blatt ohne Ergebnis umgesetzt (Nr. 40 ankreuzen, Nr. 41 unterstreichen), das Ausrechnen liegt in Nr. 42 · Voraussetzung „Scheitelpunktform lesen“ (Kl. 9) für Kl. 8 am Gymnasium nicht vorhanden; entfällt, weil der Nachweis 2017-OS-K5d rein algebraisch gestellt ist · Produktform gleich null und quadratische Ergänzung (RLP H) stehen in Einheit 3 ohne GYM-Typklammer, obwohl sie am Gymnasium nach Kl. 8 liegen · Spannen: terme.md Einheit 3 und 4 und binomische-formeln.md Einheit 1 (GYM Kl. 7–8) → „neu oder schon bekannt – je nach Buch“; terme.md Einheit 1 (GYM 6–7) und 2 (GYM 7) → Zone; Typklammern [GYM 8] (Minusklammer, Zahl mal Klammer, Zusammenfassen mit zwei Variablen) → „(neu in diesem Jahr)“ am Titel von Nr. 12 und 23
3. Protokoll-Archiv: TermeBinomischeFormeln_2026-09-26_protokoll.zip
```

PDFs:

- [TermeBinomischeFormeln_Gesamt.pdf](10-ka-terme-8-gym/TermeBinomischeFormeln_Gesamt.pdf)
- [TermeBinomischeFormeln_KennstDuSchon.pdf](10-ka-terme-8-gym/TermeBinomischeFormeln_KennstDuSchon.pdf)
- [TermeBinomischeFormeln_Lernblatt.pdf](10-ka-terme-8-gym/TermeBinomischeFormeln_Lernblatt.pdf)
- [TermeBinomischeFormeln_Loesungen.pdf](10-ka-terme-8-gym/TermeBinomischeFormeln_Loesungen.pdf)
- Zwischenkompilate der Sitzung: e1_probe.pdf, e2_probe.pdf, e3_probe.pdf, e4_probe.pdf, e5_probe.pdf, test_bausteine.pdf, zone_probe.pdf

Worauf beim Gegenlesen achten:

- zwei Einträge
- Zweige in Lehrplanfolge
- eine Zone aus beiden
- Nachbarzweige aus „Querbezüge" genannt
- Leiter eine Stufe über der Richtung
- Messung: TermeBinomischeFormeln_Gesamt.pdf – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 34 von 61 (alle Einheiten); ohne jeden Treffer: E3 Plusklammer weglassen; E3 Minusklammer (alle Vorzeichen drehen); E1 mit Vorzahl vor x; E2 mit Vorzahl vor x (a ist die ganze Vorzahl mit x); E3 mit Vorzahl (Quadrat von 2x); E3 Anwendung: Produktform gleich null (Verfahren in quadratische-gleichungen.md Einheit 2).
- v4.4-Prüfpunkte: TermeBinomischeFormeln_Gesamt.pdf – a)–g) erfüllen ihr Soll.
- Messung: 80 Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).
