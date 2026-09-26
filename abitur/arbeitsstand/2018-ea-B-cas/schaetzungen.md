# Blinde Schätzungen 2018-ea-B-cas (vor Erwartungshorizont und Standardbezug)

Erfasst am 29.09.2026 (Auftrag Nacht 2026-09-29, Teil 3) mit dem geprüften Stand dieser Datei und Deutungsliste (f) an
Stochastik CAS 1 1b und CAS 2 1b: 69 von 85, dokumentierte Unterschreitung der Eichschwelle (iqb-bau.py v1.10,
EICHUNG_UNTERSCHRITTEN; iqb-pruefungen.md § 4); Verweise der Landeshefte per abitur-abgleich.py Lauf 27.

## Ergebnis (nach dem Lesen der Standardbezüge; Rechnung eichung.py mit eichung() aus abitur/iqb-bau.py)
Erster vollständiger Stand (alle 85 Zeilen, blind): 57 von 85 (67,1 %) – eigene 55 von 82 (blind 54 von 81, dazu
Stochastik CAS 1 2 c nicht blind), aus der WTR-Zeile übernommene 2 von 3. Nach Prüfung der 28 Abweichungen zehn
Korrekturen mit Regel (Liste in eichung.py): 67 von 85 (78,8 %), eigene 64 von 82, übernommene 3 von 3.
Schwelle 85 % (73 von 85) nicht erreicht → Abbruch, nichts geschrieben. AB-Spalte: I 24, II 39, III 22.
Kein Teilaufgaben-Paar mit Aufgabendublette; geteilt mit StochastikWTR1: 1 d, 2 a, 2 b.

Regel: enge Fassung, Deutungsliste v0.7 (iqb.md § 7). Je Datei zuerst die Aufgabenseiten; EH/SB erst danach.

## AnalysisCAS1 (Seiten 1–2 und Seite 3 oben bis „50“ gelesen; EH 1 a unten auf Seite 3 in Sicht)
1a I – Parabel f6 skizzieren (Zeichnen)
1b II – Term als Flächenstück deuten, Summanden zuordnen, Inhalt angeben (Integralwert deuten, Verkettung)
1c II – Extremum bei x = 2 mit Art nach Vorzeichen von r: die Fallunterscheidung verlangt der Text wörtlich
   („in Abhängigkeit von r angeben“), Vorzeichen eines einzelnen Faktors −2/r – Routinekette, nicht III
1d II – gemeinsame Punkte der Schar über Ausklammern/Gleichsetzen
1e III – Nullstellenzahl in Abhängigkeit von r: Diskriminante 16 + 8r, drei Fälle mit verschiedenem Ausgang
   ausgeführt (Nullfall-Regel: zählt), Verkettung mit Fallunterscheidung
1f III – zwei Aussagen begründen: rechter Winkel bei A_r/B_r nur bei x = 4 (Bedingung erst gefunden, (a)),
   für −2 < r < 0 Skalarprodukt/Thaleskreis – Bedingungen aus der Geometrie erst übersetzen
1g II – zwei vorgegebene Ansätze erläutern (Skalarprodukt null, Steigungsprodukt −1): Deutung vorgegebener Terme
2a I – Nullstelle von f4 als Flugweite nachweisen
2b I – Nullstelle von y(t) als Flugzeit nachweisen
2c II – v(1,22) berechnen, ∫ v dt als zurückgelegten Weg deuten (Bestand aus Rate, Standarddeutung)
3a II – knickfreier Übergang: s(0,5) = f4(0,5), s'(0,5) = f4'(0,5) (Kontrollwerte vorgegeben)
3b II – s'(x) = tan 85° lösen (Winkel ↔ Steigung, kurze Kette)
3c II – Länge aus drei Teilen: zwei Bogenlängen mit vorgegebener Formel plus senkrechter Absturz aus s(1,24);
   Absturz wörtlich vorgegeben, Verkettung von Standardschritten
4 III – Tangente von (17,6 | 0) an f4 (Deutungsliste (a): „ohne Knick“ + Gerade bis zum Boden erst als Tangente
   durch einen äußeren Punkt übersetzen)

## AnalysisCAS2 (Seiten 1–3 oben bis „50“; EH 1 a–c unten auf Seite 3 in Sicht, Standardbezug nicht)
1a II – Extrempunkte und Art (Ableitung, Gleichung, zweite Ableitung: Verkettung nach der Liste)
1b II – y-Achsenabschnitt angeben, genau zwei Nullstellen ohne Rechnung aus Verhalten im Unendlichen und Tiefpunkt
1c II – f(x) = f(x + 60) mit dem Rechner; Bedingung wörtlich vorgegeben („um 60 unterscheiden … übereinstimmen“)
1d III – aus gleichen Funktionswerten im Abstand 60 auf eine Extremstelle dazwischen schließen (Beziehung hergeleitet, Prinzip; Satz von Rolle)
1e II – senkrechte Gerade x = c mit ∫0..c f = ½ ∫0..240 f; „halbiert“ wörtlich, Gleichung mit dem Rechner
1f III – Aussage ½ · u · f(u) + ∫u..240 f = 2/3 ∫0..240 f veranschaulichen: Gerade durch Ursprung und (u | f(u)) erst finden (Dreieck + Restfläche), (d)
2a II – f(x) = 170 lösen, Dauer als Differenz (erster Hochpunkt unter 170)
2b II – stärkster Anstieg: Maximum von f' mit Randvergleich
2c I – Sekantensteigung als mittlere, Grenzwert als momentane Änderungsrate veranschaulichen (Reproduktion)
2d II – |f'(x)| <= 0,3: Gleichungen f'(x) = ±0,3, Teilintervalle addieren
2e II – Integralmittelwert und diskreter Mittelwert (9 Werte), prozentuale Abweichung
2f II – h_k'(0) = f'(240) (zwei Ableitungen, eine Gleichung)
2g II – Verschiebung von h_k um 240 nach rechts und f(240) nach oben; Bedingung der Steigung in f vorbereitet, Wert wörtlich

## AnalysisCAS3 (Seiten 1–3 oben bis „50“; EH 1 a unten auf Seite 3 in Sicht)
1a I – f5 skizzieren, Achsensymmetrie, f_k(−x) = f_k(x) (Identität mit Parameter, Reproduktion)
1b I – Radikand >= 400 > 0 (einzelne Beobachtung)
1c II – Extrempunkt mit Parameter: Kettenregel, f_k' = 0, Art (Verkettung)
1d II – y-Achsenabschnitt der Tangente 400/√(5c^2 + 400) > 10, Ungleichung
1e III – für alle k und alle Stellen: Achsenabschnitt der Tangente 400/√(…) > 0, Beziehung hergeleitet ((c), wie „Tangente an der Stelle u schneidet bei …“)
1f III – x^2 · (k − 4 − x^2/100) = 0: Bedingung k > 4 erst gefunden, zwei Fälle mit verschiedenem Ausgang (Nullfall-Regel zählt)
1g I – mittlere Abweichung mit dem Rechner (eine Rechnung)
1h III – Gedankengang zum Term: Vorzeichen von f5 − g auf [0; 10] und [10; 15], gewichtetes Mittel der Teilmittel (zwei Deutungen verkettet, (d))
2a I – Punktprobe mit (250 | 72,8) aus der Abbildung (Kontrolle vorgegeben)
2b III – Fläche zwischen Fahrbahn und Seil, oben durch y = 37 begrenzt: Grenze erst übersetzen, stückweise Fläche ((a))
2c II – Graphen nach s ordnen (Öffnung nach Vorzeichen, Weite nach Betrag), begründen
2d II – Krümmung/Öffnung nach oben ⇔ s > 0, begründen
2e II – Längenformel mit v = 250 gleich 514,5 nach s lösen, t aus dem Befestigungspunkt (Formel vorgegeben)
2f III – Steigungen an den Befestigungspunkten vergleichen und daraus auf einen Schnitt der Seile schließen (Beziehung hergeleitet, Symmetrie)

## AGLAA1CAS1 (Seiten 1–3 oben; EH a–f auf Seite 3 in Sicht, Standardbezug nicht)
a II – Matrix aus dem Diagramm, Vormonat über Gleichungssystem/Inverse
b III – fünf Monate zurück ergibt negative Anzahlen: Bedingung (Nichtnegativität) erst gefunden, Verkettung mit Deutung
c II – Vormonat mit M^(−1), prozentuale Anteile
d II – Grenzmatrix bzw. stationäre Verteilung, Anteile
e I – Diagonale ablesen: B, 28 %
f II – erste Komponente mit N gleich 3022 setzen, p = 1,1 außerhalb [0; 1]
g II – Anteil C linear in p, Randwerte p = 0 und p = 1
h III – für alle p nichtnegativer Fixvektor mit Summe 10000 (allgemeiner Nachweis mit Parameter, (c)), ganzzahliges Beispiel, Deutung

## AGLAA1CAS2 (Seiten 1–3 oben; EH 1 a–2 c auf Seite 3 in Sicht)
1a I – Bedeutung zweier Matrixeinträge
1b I – L^6 · v0, L^10 · v0 mit dem Rechner
1c II – Quotienten nach je vier Wochen, vierte Wurzel für die wöchentliche Zunahme
2a I – zwei Schritte mit Entnahme
2b II – Aussage beurteilen: entnommene Tiere vermehren sich nicht mehr (kein Listeneintrag)
2c II – stationärer Zustand mit Entnahme: L · v − (0; 0; a) = v
3a II – Eigenschaften in (b · V; 4V; V) und M · v = c · v übersetzen; Verhältnisse wörtlich
3b III – Matrix mit 0 statt 0,9 aufstellen, M'^3 = 1,35 · E erkennen (Sonderfall (b)), exponentielles Wachstum im Dreiwochenrhythmus

## AGLAA2CAS1 (Museum; Seiten 1–2 oben; EH a–d auf Seite 2 in Sicht)
a II – vorgegebene Rechnung erläutern: S als Schnitt der Geraden AD und BE (Pyramide DEFS)
b I – drei Skalarprodukte ungleich null
c II – Innenwinkel bei E und Höhe zur Seite EF (zwei Standardrechnungen)
d II – Pyramidenvolumen DEFG (Grundfläche in z = 15, Höhe 20), Leistung 20 kW <= 25 kW
e I – Gerade AG mit z = 15 schneiden
f II – Punkt auf RG im Abstand 5 von der Ebene EFG: Ebene, Parameter, Abstand = 5, Lösung auf der Strecke wählen (Abstand wörtlich)

## AGLAA2CAS2 (Obelisk; Seiten 1–2 oben; EH a–e auf Seite 2 in Sicht)
a II – A aus B und Mittelpunkt, Gerade AE mit der z-Achse schneiden
b II – Neigungswinkel der Seitenkanten (Verkettung wie im Vorbild korrigiert)
c II – Trapezfläche mit Höhe der Seitenfläche
d II – Stumpfvolumen als Differenz zweier Pyramiden, Masse
e II – vier Ebenengleichungen auf Symmetrie prüfen, eine widerlegen
f II – Schatten der Spitze fällt auf den unteren Teilkörper, wenn die Pyramide zu flach ist (qualitativ)
g II – Schattenpunkt (h/2; h/2; 0), Abstand zu B gleich 5,1, h bestimmen (Abstand wörtlich, Verkettung)

## StochastikCAS1 (Seiten 1–2 oben; EH 1 a, b auf Seite 2 in Sicht)
(Erste Annahme „Aufgabe 2 ganz wortgleich“ war ein Artefakt des Textschnitts an der Seitenkopfzeile
„2 Erwartungshorizont“; nach Korrektur des Schnitts und am Bild von WTR1 S. 2: 2 c ist abgewandelt – CAS: blauer Sektor
vergrößert, drei Drehungen, Pfad R–R–B 0,036; WTR: grüner Sektor verkleinert, zwei Drehungen, 0,14. Also keine
Aufgabendublette, Soll bleibt 25.)
Geteilt (wortgleich mit WTR1): 1d (Stamm: Stichprobe 500 statt 200, für d ohne Belang), 2a, 2b → Schätzung übernommen.
2c: beim Ansehen von CAS1 S. 3 lag der Standardbezug offen, bevor 2 c geschätzt war → Schätzung II nicht blind
(Pfadgleichung 2p · 2p · (1 − 3p) = 0,036 aufstellen, lösen, Lösung mit vergrößertem Blau wählen: Verkettung, II).
1a I – zwei Binomialwerte mit dem Rechner
1b II – Mindestumfang für P(Y >= 100) >= 0,95 mit p = 0,96 durch Probieren (kein Listeneintrag; Kandidat aus 2017-ga-B)
1c II – Entscheidungsregel linksseitig, n = 500
1d (übernommen aus 2018MerhoehtBStochastikWTR1-1d: II)

## StochastikCAS2 (Seiten 1–3 oben; EH 1 a–3 b auf Seite 3 in Sicht)
1a I – zwei Binomialwerte
1b II – Mindestanzahl durch Probieren (wie CAS 1 1 b)
2a II – Laplace: Scheine unter 50 € und umlauffähig (176 − 4)/380
2b II – Zufallsexperiment und Ereignis zu einem hypergeometrischen Term (nicht nur Deutung eines Terms als Ereignis, Experiment beschreiben)
3a I – Erwartungswert aus dem Säulendiagramm
3b II – Aussage beurteilen: Diagramm gibt Anzahlen, nicht Anteile (kein Listeneintrag)
4a II – Entscheidungsregel rechtsseitig, n = 10
4b III – Güte aus Abbildung 2 für p > 0,5 ablesen, Fehler zweiter Art als Gegenwahrscheinlichkeit ((d): zwei Deutungen verkettet)
