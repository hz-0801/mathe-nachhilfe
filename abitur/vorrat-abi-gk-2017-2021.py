#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""vorrat-abi-gk-2017-2021.py – Beitabelle Vorrat Abitur GK 2017–2021 (Berlin).

Quelle der Zeilen: nur die Katalogzeilen in abi-katalog.csv (gegeben, gesucht,
verfahren, ergebnis, zwischenergebnis, stichwoerter), Agent 05.10.2026.
Je Teilaufgabe: kurz (Kurzlösung ohne Sätze, mit Einheit), zwischen (Werte, mit
denen weitergerechnet wird, als „Ansatz ⇒ Wert“, höchstens BE − 1), stich
(Begriffe), neben (mitbenutzte Themen aus abitur-vokabular.md, nie das
Hauptthema), abh (id derselben Prüfung). Vektoren als (a | b | c); die
Übernahme (vorrat-uebernahme.py) setzt ⟨a | b | c⟩, Punkte bleiben P(a | b | c).

Aufruf: python3 vorrat-abi-gk-2017-2021.py > vorrat-abi-gk-2017-2021.csv
Die Spalte sympy füllt vorrat-sympy-abi-gk-2017-2021.py --eintragen.
"""
import csv
import sys

Z = []


def z(id_, kurz, zwischen="", stich="", neben="", abh=""):
    Z.append([id_, kurz, zwischen, stich, neben, abh, ""])


# ------------------------------------------------------------- 2017-be-gk
z("2017-be-gk-B1.1a",
  "T(0 | 1) = A, H(20 | 9) = B; knickfrei in waagerechte Schienen ⇒ waagerechte Tangente in A und B ⇒ f′ = 0 genau bei x = 0 und x = 20",
  "f′(x) = 0 ⇒ x · (−3/500 x + 3/25) = 0 ⇒ x = 0, x = 20|f″(x) = −3/250 x + 3/25|f″(0) = 0,12 > 0, f″(20) = −0,12 < 0|f(20) = 9",
  "Extrempunkte|notwendige und hinreichende Bedingung|zweite Ableitung|waagerechte Tangente|knickfreier Übergang",
  "Ableitungsregeln|Gleichungen lösen")
z("2017-be-gk-B1.1b",
  "m = 0,4; x₁ = 10 − 10/√3 ≈ 4,23, x₂ = 10 + 10/√3 ≈ 15,77",
  "m = (f(20) − f(0))/20 = 8/20 = 0,4|f′(x) = 0,4 ⇒ x² − 20x + 200/3 = 0 ⇒ x = 10 ± 10/√3",
  "mittlere Änderungsrate|Differenzenquotient|lokale Änderungsrate|quadratische Gleichung",
  "Gleichungen lösen", "2017-be-gk-B1.1a")
z("2017-be-gk-B1.1c",
  "W(10 | 5); f′(10) = 0,6 ⇒ α ≈ 31,0° < 32° ⇒ Kriterium erfüllt",
  "f″(x) = 0 ⇒ x = 10|f(10) = 5, f′(10) = 0,6|tan α = 0,6 ⇒ α ≈ 30,96°",
  "Wendepunkt|größter Anstieg|Steigungswinkel|Arkustangens",
  "Ableitungsregeln|Tangente, Normale, Schnittwinkel")
z("2017-be-gk-B1.1d",
  "A = 100 cm²; V = 400 cm³",
  "F(x) = −1/2000 x⁴ + 1/50 x³ + x|∫₀²⁰ f(x) dx = F(20) − F(0) = 100|V = 4 · 100",
  "bestimmtes Integral|Stammfunktion|Querschnittsfläche|Prisma|Volumen",
  "Stammfunktion und Hauptsatz")
z("2017-be-gk-B1.1e",
  "Schnittwinkel α ≈ 20,9° < 25° ⇒ Neigungswinkel nicht zu groß",
  "f′(1,5) = 0,1665 ⇒ α₁ ≈ 9,45°|f′(8,5) = 0,5865 ⇒ α₂ ≈ 30,39°|α = α₂ − α₁",
  "Tangente|Steigungswinkel|Schnittwinkel zweier Geraden|Arkustangens",
  "Ableitung und Änderungsrate")
z("2017-be-gk-B1.1f",
  "g(x) = −0,00128x³ + 0,048x² + 1,5",
  "g(0) = 1,5 ⇒ c = 1,5|g′(25) = 0 ⇒ 1875a + 50b = 0 ⇒ b = −37,5a|g(25) = 11,5 ⇒ 15 625a + 625b = 10 ⇒ a = −0,00128, b = 0,048",
  "Steckbriefaufgabe|Bedingungen aufstellen|lineares Gleichungssystem|Extrempunkte als Bedingung",
  "Gleichungen lösen|Ableitungsregeln|Kurvenuntersuchung")
z("2017-be-gk-B1.2a",
  "S_y(0 | 1), N(1 | 0); T(1 | 0), H(3 | 4e⁻³) ≈ H(3 | 0,20)",
  "f(0) = 1|f(x) = 0 ⇒ (x − 1)² = 0 ⇒ x = 1|f′(x) = 0 ⇒ −x² + 4x − 3 = 0 ⇒ x = 1, x = 3|f″(x) = (x² − 6x + 7) · e^(−x)|f″(1) = 2/e > 0, f″(3) = −2e⁻³ < 0",
  "Achsenschnittpunkte|doppelte Nullstelle|Extrempunkte|hinreichende Bedingung|Produktregel|e-Funktion",
  "Kurvenuntersuchung|Ableitungsregeln|Gleichungen lösen")
z("2017-be-gk-B1.2b",
  "Graph über [0; 2] durch (0 | 1), T(1 | 0), (2 | 0,14); berührt die x-Achse in T",
  "f(0,5) ≈ 0,15|f(2) = e⁻² ≈ 0,14",
  "Graph zeichnen|Wertetabelle|Berührpunkt mit der x-Achse",
  "", "2017-be-gk-B1.2a")
z("2017-be-gk-B1.2c",
  "x_P = 3 − √2 ≈ 1,59; f′(x_P) ≈ 0,170",
  "f″(x) = 0 ⇒ x² − 6x + 7 = 0 ⇒ x = 3 ± √2|3 + √2 ≈ 4,41 ∉ [0; 2]",
  "maximale Steigung|Wendestelle|notwendige Bedingung|zweite Ableitung",
  "Ableitungsregeln|Gleichungen lösen|Kurvenuntersuchung")
z("2017-be-gk-B1.2d",
  "F′ = f; A = 1 − 2/e ≈ 0,264 FE ≈ 26,4 m²",
  "F′(x) = −2x · e^(−x) + (x² + 1) · e^(−x) = f(x)|∫₀¹ f(x) dx = F(1) − F(0) = −2/e + 1|1 FE = 100 m²",
  "Stammfunktion nachweisen|Produktregel|bestimmtes Integral|Flächenmaßstab",
  "Ableitungsregeln|Flächeninhalt durch Integration")
z("2017-be-gk-B1.2e",
  "t(x) = −3x + 1; Einsparung 100 · (5/6 − 2/e) ≈ 9,8 m²",
  "f′(0) = −3 ⇒ t(x) = −3x + 1|t(x) = 0 ⇒ x = 1/3|A = 1/2 · 1 · 1/3 = 1/6 FE ≈ 16,7 m²|Einsparung (1 − 2/e) − 1/6 FE",
  "Tangentengleichung|Achsendreieck|Flächeninhalt eines Dreiecks|Flächenmaßstab",
  "Flächeninhalt durch Integration|Ableitung und Änderungsrate", "2017-be-gk-B1.2d")
z("2017-be-gk-B1.2f",
  "p(0) = 1, p′(0) = −3, p(1) = 0, p′(1) = 0; aus drei Bedingungen p(x) = 2x² − 3x + 1, dann p′(1) = 1 ≠ 0 ⇒ kein solches p",
  "p(x) = ax² + bx + c|p(0) = 1 ⇒ c = 1|p′(0) = −3 ⇒ b = −3|p(1) = 0 ⇒ a = 2|p′(1) = 2a + b = 1 ≠ 0",
  "Steckbriefaufgabe|Berührbedingung|überbestimmtes Gleichungssystem|Widerspruch",
  "Gleichungen lösen|Tangente, Normale, Schnittwinkel", "2017-be-gk-B1.2a")
z("2017-be-gk-B2.1a",
  "r = (60 | 11 | 30); g: x = (1140 | 240 | 0) + t · (60 | 11 | 30); |r| = √4621 ≈ 68,0 m; v ≈ 244,7 km/h; α ≈ 26,2°",
  "|r| = √(60² + 11² + 30²) = √4621 ≈ 67,98|67,98 m/s · 3,6 ≈ 244,7 km/h|sin α = 30/√4621 ⇒ α ≈ 26,2°",
  "Richtungsvektor|Geradengleichung|Betrag eines Vektors|Geschwindigkeit|Winkel zwischen Gerade und Ebene",
  "Vektoren und Rechenoperationen|Skalarprodukt und Winkel|Punkte und Strecken im Koordinatensystem")
z("2017-be-gk-B2.1b",
  "R(8040 | 1505 | 0)",
  "Richtung der Startbahn (60 | 11 | 0), Betrag 61|7000/61 ≈ 114,75 ≈ 115|R = P0 + 115 · (60 | 11 | 0)",
  "Verlängerung einer Strecke|Vielfaches eines Vektors|Betrag eines Vektors|Runden",
  "Vektoren und Rechenoperationen|Punkte und Strecken im Koordinatensystem", "2017-be-gk-B2.1a")
z("2017-be-gk-B2.1c",
  "s = 70 ⇒ Punkt (8040 | 1505 | 615) ∈ h senkrecht über R ⇒ Überflug in 615 m Höhe",
  "1740 + 90s = 8040 ⇒ s = 70|y = 350 + 70 · 16,5 = 1505 stimmt|z = 300 + 70 · 4,5 = 615",
  "Punktprobe|Parameter bestimmen|Flughöhe|Geradengleichung",
  "Gleichungen lösen|Punkte und Strecken im Koordinatensystem", "2017-be-gk-B2.1b")
z("2017-be-gk-B2.1d",
  "r_neu · n = 0 ⇒ h ∥ E (echt parallel); Wolkenuntergrenze über R in 480 m, Jet in 615 m ⇒ nur die Wolkendecke sichtbar",
  "n = (1 | 0 | −20)|(90 | 16,5 | 4,5) · (1 | 0 | −20) = 90 − 90 = 0|P10 ∉ E: 1740 − 6000 = −4260 ≠ −1560|8040 − 20z = −1560 ⇒ z = 480",
  "Lage Gerade–Ebene|Normalenvektor|Skalarprodukt|echt parallel|Punktprobe",
  "Orthogonalität|Skalarprodukt und Winkel|Ebenen|Gleichungen lösen", "2017-be-gk-B2.1c")
z("2017-be-gk-B2.2a",
  "A(10 | 0 | 0), E(9 | 1 | 6), H(1 | 1 | 6)",
  "Mittelachse x = 5, y = 5",
  "Pyramidenstumpf|Koordinaten ablesen|Symmetrie|Deckfläche")
z("2017-be-gk-B2.2b",
  "E1: 6x + z = 60",
  "AB = (0 | 10 | 0), AF = (−1 | 9 | 6)|n = AB × AF = (60 | 0 | 10) ⇒ (6 | 0 | 1)|A einsetzen ⇒ 60",
  "Koordinatenform|Normalenvektor|Kreuzprodukt|Spannvektoren",
  "Vektoren und Rechenoperationen|Orthogonalität", "2017-be-gk-B2.2a")
z("2017-be-gk-B2.2c",
  "γ ≈ 80,5°; größter Abstand |AC| = 10√2 ≈ 14,14 cm",
  "cos γ = |n1 · n2|/(|n1| · |n2|) = 1/√37 ⇒ γ ≈ 80,54°|AC = (−10 | 10 | 0) ⇒ |AC| = √200|DF = (9 | 9 | 6) ⇒ |DF| = √198 ≈ 14,07|AS = (−5 | 5 | 9) ⇒ |AS| = √131 ≈ 11,45",
  "Winkel zwischen Ebenen|Normalenvektor|Betrag eines Vektors|Raumdiagonale",
  "Ebenen|Punkte und Strecken im Koordinatensystem|Vektoren und Rechenoperationen", "2017-be-gk-B2.2b")
z("2017-be-gk-B2.2d",
  "80 cm²",
  "Pyramidenhöhe 9 − 6 = 3 cm|Seitenhöhe √(3² + 4²) = 5 cm|4 · 1/2 · 8 · 5",
  "Pyramide|Mantelfläche|Seitenhöhe|Satz des Pythagoras")
z("2017-be-gk-B2.2e",
  "P1(9,5 | 0,5 | 3); |P1D| = |P1B| = √99,5 ≈ 9,97 cm; 8 · √99,5 ≈ 79,8 cm < 80 cm ⇒ Draht reicht",
  "Mitte von AE ⇒ P1(9,5 | 0,5 | 3)|P1D = (−9,5 | −0,5 | −3) ⇒ |P1D| = √99,5|P1B = (0,5 | 9,5 | −3) ⇒ |P1B| = √99,5|8 · 9,975 ≈ 79,8",
  "Mittelpunkt einer Strecke|Betrag eines Vektors|Streckenlänge|Symmetrie",
  "Vektoren und Rechenoperationen", "2017-be-gk-B2.2a")
z("2017-be-gk-B3.1a",
  "(6 über 4) = 15", "",
  "Binomialkoeffizient|Auswahl ohne Reihenfolge|Kombination")
z("2017-be-gk-B3.1b",
  "P(A) = 247/490 ≈ 0,504; P(B) = 1 − P(A) ≈ 0,496",
  "P(A) = (47 über 10)/(50 über 10) = 247/490|P(B) = 1 − P(A)",
  "Ziehen ohne Zurücklegen|hypergeometrische Verteilung|Gegenereignis|Binomialkoeffizient",
  "Hypergeometrische Verteilung|Kombinatorik|Ereignisse und Mengenoperationen")
z("2017-be-gk-B3.1c",
  "0,1 · 0,05 + 0,3 · 0,03 + 0,2 · 0,04 + 0,4 · 0,02 = 0,03 = 3 %",
  "0,005 + 0,009 + 0,008 + 0,008",
  "totale Wahrscheinlichkeit|Pfadregeln|Baumdiagramm")
z("2017-be-gk-B3.1d",
  "P(A | fehlerhaft) = 0,005/0,03 = 1/6 ≈ 16,7 %",
  "P(A ∩ F) = 0,1 · 0,05 = 0,005|P(F) = 0,03",
  "bedingte Wahrscheinlichkeit|Satz von Bayes|Umkehrung des Baumdiagramms",
  "Baumdiagramm und Pfadregeln", "2017-be-gk-B3.1c")
z("2017-be-gk-B3.1e",
  "P(X = 0) = 0,95²⁰ ≈ 0,358",
  "X ~ B(20; 0,05)",
  "Bernoulli-Kette|Binomialverteilung|kein Treffer")
z("2017-be-gk-B3.1f",
  "s = 199; Ereignis: unter 200 Geräten aus Werk D ist höchstens eines fehlerhaft; P(X ≤ 1) ≈ 0,089",
  "0,98²⁰⁰ = P(X = 0) für n = 200, p = 0,02|200 · 0,02 · 0,98¹⁹⁹ = P(X = 1)",
  "Bernoulli-Formel|Term deuten|höchstens ein Treffer|Binomialverteilung")
z("2017-be-gk-B3.1g",
  "n ≥ 74",
  "1 − 0,96ⁿ ≥ 0,95 ⇒ 0,96ⁿ ≤ 0,05 ⇒ n ≥ ln 0,05/ln 0,96 ≈ 73,4|1 − 0,96⁷³ ≈ 0,9492, 1 − 0,96⁷⁴ ≈ 0,9512",
  "Mindestanzahl|Gegenereignis|Exponentialgleichung|Logarithmus|Dreimal-mindestens-Aufgabe",
  "Gleichungen lösen")
z("2017-be-gk-B3.2a",
  "P(A1) = 1/3; P(A2) = 8/15 ≈ 0,533",
  "P(2) = 2/3, P(Rot | G2) = 1/2 ⇒ P(A1) = 2/3 · 1/2|P(A2) = 1/3 · 6/10 + 2/3 · 1/2",
  "zweistufiges Zufallsexperiment|Pfadmultiplikationsregel|Pfadadditionsregel|Glücksrad",
  "Zufallsexperimente und Urnenmodelle")
z("2017-be-gk-B3.2b",
  "(1; Rot), (2; Blau), (2; Schwarz) mit je 1/6",
  "P(1) = 1/3, P(2) = 2/3; P(Rot) = 1/2, P(Blau) = P(Schwarz) = 1/4|1/3 · 1/2 = 2/3 · 1/4 = 1/6",
  "unabhängige Experimente|Pfadmultiplikationsregel|Ergebnismenge",
  "Unabhängigkeit")
z("2017-be-gk-B3.2c",
  "P(C1) ≈ 0,2508; P(C2) = 0,3669",
  "X ~ B(10; 0,4)|P(C1) = (10 über 4) · 0,4⁴ · 0,6⁶|P(C2) = 1 − P(X ≤ 4) = 1 − 0,6331",
  "Binomialverteilung|Bernoulli-Formel|kumulierte Wahrscheinlichkeit|Gegenereignis|Tabelle")
z("2017-be-gk-B3.2d",
  "P(Y = 15) ≈ 0,048 < 0,05 ⇒ Behauptung richtig",
  "Y ~ B(30; 0,3669)|P(Y = 15) = (30 über 15) · 0,3669¹⁵ · 0,6331¹⁵",
  "Binomialverteilung|Bernoulli-Formel|Behauptung prüfen",
  "", "2017-be-gk-B3.2c")
z("2017-be-gk-B3.2e",
  "P ≈ 0,2007 · 0,6331 ≈ 0,127",
  "erste zehn: P(X = 5) = P(X ≤ 5) − P(X ≤ 4) = 0,8338 − 0,6331 = 0,2007|letzte zehn: höchstens 4 Treffer ⇒ P(X ≤ 4) = 0,6331|Produkt unabhängiger Abschnitte",
  "Binomialverteilung|unabhängige Teilketten|kumulierte Wahrscheinlichkeit|Multiplikationsregel",
  "Unabhängigkeit", "2017-be-gk-B3.2c")


# ------------------------------------------------------------- 2018-be-gk
z("2018-be-gk-B1.1a",
  "S liegt 4 m höher als C; |AB| = 24 m",
  "h(0) = 54, g(0) = 50 ⇒ Differenz 4|B(−20 | 50), h(−20) = 74 ⇒ A(−20 | 74)",
  "Funktionswert|Schnittpunkt mit der y-Achse|Höhenunterschied|Punkte ablesen")
z("2018-be-gk-B1.1b",
  "A = 640/3 m² ≈ 213,3 m²",
  "Integrand h(x) − 50 = 0,05x² + 4|∫ von −20 bis 0 (0,05x² + 4) dx = [x³/60 + 4x] = 640/3",
  "Querschnittsfläche|bestimmtes Integral|Differenzfunktion|Stammfunktion",
  "Stammfunktion und Hauptsatz|Gleichungen lösen", "2018-be-gk-B1.1a")
z("2018-be-gk-B1.1c",
  "H(0 | 50), T₁(−100 | 0), T₂(100 | 0); U = T₂(100 | 0)",
  "g′(x) = 0 ⇒ x · (x² − 10 000) = 0 ⇒ x = −100, 0, 100|g″(x) = 1/1000 · (3/500 x² − 20)|g″(0) = −0,02 < 0, g″(±100) = 0,04 > 0|g(±100) = 0, g(0) = 50",
  "Extrempunkte|notwendige und hinreichende Bedingung|zweite Ableitung|Sachzusammenhang",
  "Ableitungsregeln|Gleichungen lösen")
z("2018-be-gk-B1.1d",
  "K(100/√3 | 200/9) ≈ K(57,7 | 22,2); g′(x_K) ≈ −0,77",
  "g″(x) = 0 ⇒ 3/500 x² = 20 ⇒ x² = 10 000/3 ⇒ x = 100/√3 ≈ 57,74|g(57,74) ≈ 22,22",
  "stärkstes Gefälle|Wendestelle|notwendige Bedingung|zweite Ableitung",
  "Ableitungsregeln|Gleichungen lösen", "2018-be-gk-B1.1c")
z("2018-be-gk-B1.1e",
  "f(x) = −0,008x² + 54",
  "f(x) = ax² + bx + c|f(0) = h(0) = 54 ⇒ c = 54|f′(0) = h′(0) = 0 ⇒ b = 0|g(60) = 20,48 ⇒ f(60) = 25,2 ⇒ 3600a + 54 = 25,2 ⇒ a = −0,008",
  "Steckbriefaufgabe|knickfreier Übergang|Berührbedingung|quadratische Funktion",
  "Gleichungen lösen|Ableitung und Änderungsrate")
z("2018-be-gk-B1.1f",
  "L(73,9 | 10,3); Flugbahn: nach unten geöffnete Parabel mit Scheitel S(0 | 54) durch (40 | 41,2), (60 | 25,2) bis L",
  "f(x) = g(x) ⇒ x⁴ − 4000x² − 8 000 000 = 0|u = x² ⇒ u² − 4000u − 8 000 000 = 0 ⇒ u = 2000 + 2000√3 ≈ 5464,1|x = √u ≈ 73,92|g(73,92) ≈ 10,29",
  "Schnittpunkt zweier Graphen|biquadratische Gleichung|Substitution|Parabel skizzieren",
  "Funktionsklassen und Eigenschaften|Kurvenuntersuchung", "2018-be-gk-B1.1e")
z("2018-be-gk-B1.1g",
  "d(x) = f(x) − g(x) maximal bei x = 20√5 ≈ 44,7 m mit d = 38 − 32 = 6 m ⇒ Abstand höchstens 6 m",
  "d(x) = 0,002x² + 4 − x⁴/2 000 000|d′(x) = 0,004x − x³/500 000 = 0 ⇒ x² = 2000 ⇒ x = 20√5 ≈ 44,72|f(44,72) = 38, g(44,72) = 32",
  "Differenzfunktion|Extremwertaufgabe|notwendige Bedingung|vertikaler Abstand",
  "Ableitungsregeln|Gleichungen lösen|Kurvenuntersuchung", "2018-be-gk-B1.1e")
z("2018-be-gk-B1.2a",
  "f(x) → 0 für x → +∞ (e-Funktion dominiert); x-Achse waagerechte Asymptote, Annäherung von oben",
  "",
  "Grenzwert|Verhalten im Unendlichen|Asymptote|Exponentialfunktion dominiert")
z("2018-be-gk-B1.2b",
  "φ ≈ 18,4°",
  "f′(x) = (0,5 − 0,5x) · e^(−0,5x) ⇒ f′(0) = 0,5|m_g = 1|tan φ = |(1 − 0,5)/(1 + 0,5 · 1)| = 1/3 ⇒ φ ≈ 18,43°|oder arctan 1 − arctan 0,5 = 45° − 26,57°",
  "Schnittwinkel|Tangentensteigung|Produktregel|Kettenregel|Steigungswinkel",
  "Ableitungsregeln|Ableitung und Änderungsrate")
z("2018-be-gk-B1.2c",
  "F′ = f; einzige Nullstelle x = −1 (e^(−0,5x) > 0); A = 4√e − 6,5 ≈ 0,09 FE",
  "F′(x) = −2e^(−0,5x) + (−2x − 6) · (−0,5) · e^(−0,5x) = (x + 1) · e^(−0,5x)|f(x) = 0 ⇒ x + 1 = 0 ⇒ x = −1; g(x) = 0 ⇒ x = −1|A = ∫ von −1 bis 0 (f(x) − g(x)) dx = F(0) − F(−1) − 1/2|F(0) = −6, F(−1) = −4√e ≈ −6,595",
  "Stammfunktion nachweisen|Produktregel|Kettenregel|Nullstelle|Fläche zwischen zwei Graphen",
  "Ableitungsregeln|Flächeninhalt durch Integration|Gleichungen lösen")
z("2018-be-gk-B1.2d",
  "H(1 | 2e^(−0,5)) ≈ H(1 | 1,21): 1 km nach dem Start, Höhe ≈ 1,21 km",
  "f′(x) = 0 ⇒ 0,5 − 0,5x = 0 ⇒ x = 1|f(1) = 2e^(−0,5) ≈ 1,213",
  "Hochpunkt|notwendige Bedingung|Ableitung null setzen|Sachzusammenhang",
  "Gleichungen lösen", "2018-be-gk-B1.2b")
z("2018-be-gk-B1.2e",
  "y ≈ −0,189x + 1,481",
  "f(2) = 3e^(−1) ≈ 1,1036, f(6) = 7e^(−3) ≈ 0,3485|m = (f(6) − f(2))/4 ≈ −0,1888|y = m · (x − 2) + f(2)",
  "Sekante|Gerade durch zwei Punkte|Punkt-Steigungs-Form|Näherung",
  "Funktionsklassen und Eigenschaften")
z("2018-be-gk-B1.2f",
  "f′(3) = −e^(−1,5) ≈ −0,223 < −0,222 ⇒ Stelle existiert (x = 3)",
  "f″(x) = 0,25 · (x − 3) · e^(−0,5x) = 0 ⇒ x = 3|f′(3) = −e^(−1,5)",
  "Steigung|Minimum der Ableitung|Wendestelle|Schranke|Existenznachweis",
  "Ableitungsregeln|Kurvenuntersuchung")
z("2018-be-gk-B1.2g",
  "mittlere Steigung f: (7e^(−3) − 1)/6 ≈ −0,109, h_W: −0,15 ⇒ Betrag bei h_W größer; a = 1,2, b = −ln 24/6 ≈ −0,53",
  "f(0) = 1, f(6) = 7e^(−3) ≈ 0,3485 ⇒ m_f ≈ −0,109|m_h = (0,3 − 1,2)/6 = −0,15|h_W(0) = 1,2 ⇒ a = 1,2|h_W(6) = 0,3 ⇒ 7,2 · e^(6b) = 0,3 ⇒ e^(6b) = 1/24 ⇒ b = ln(1/24)/6",
  "mittlere Änderungsrate|Differenzenquotient|Parameter bestimmen|Exponentialgleichung|Logarithmus",
  "Gleichungen lösen|Funktionsklassen und Eigenschaften")
z("2018-be-gk-B2.1a",
  "n = (10 | −1 | 0); E: −10x + y = 0",
  "AB = (4,4 | 44 | 0), AC = (0,2 | 2 | 2)|AB × AC = (88 | −8,8 | 0) ⇒ n = (10 | −1 | 0)|A einsetzen ⇒ d = 0",
  "Ebene durch drei Punkte|Normalenvektor|Kreuzprodukt|Koordinatenform",
  "Vektoren und Rechenoperationen|Orthogonalität")
z("2018-be-gk-B2.1b",
  "−10 · 4,8 + 48 = 0 ⇒ D ∈ E; n_E · n_xy = (−10 | 1 | 0) · (0 | 0 | 1) = 0 ⇒ E ⊥ x-y-Ebene",
  "",
  "Punktprobe|Orthogonalität zweier Ebenen|Normalenvektor|Koordinatenebene",
  "Orthogonalität|Ebenen", "2018-be-gk-B2.1a")
z("2018-be-gk-B2.1c",
  "g, h ⊂ E und nicht parallel ⇒ Schnittpunkt; φ ≈ 2,5°",
  "u = (4,4 | 44 | 0), v = (4,6 | 46 | 2) nicht kollinear|cos φ = |u · v|/(|u| · |v|) = 2044,24/(44,22 · 46,27) ≈ 0,9991 ⇒ φ ≈ 2,5°|Schnittpunkt (−4,4 | −44 | 5)",
  "Lage zweier Geraden|gemeinsame Ebene|lineare Abhängigkeit|Schnittwinkel|Skalarprodukt",
  "Lagebeziehungen|Skalarprodukt und Winkel|Linearkombination und lineare Abhängigkeit", "2018-be-gk-B2.1b")
z("2018-be-gk-B2.1d",
  "|PQ| = √1616 = 4√101 ≈ 40,2 m; v ≈ 26,8 m/s ≈ 96,5 km/h",
  "PQ = (−40 | −4 | 0) ⇒ |PQ| = √1616|40,2/1,5 ≈ 26,8 m/s|· 3,6",
  "Betrag eines Vektors|Streckenlänge|Geschwindigkeit|Einheiten umrechnen",
  "Vektoren und Rechenoperationen|Punkte und Strecken im Koordinatensystem")
z("2018-be-gk-B2.1e",
  "r = 32/33 ⇒ t = 1,5 s · 32/33 = 16/11 s ≈ 1,45 s",
  "Bahn x = (42 | 36 | 0) + r · (−40 | −4 | 0)|in E: −10 · (42 − 40r) + (36 − 4r) = 0 ⇒ 396r = 384 ⇒ r = 32/33|Punkt (3,2 | 32,1 | 0)",
  "Schnittpunkt Gerade–Ebene|Geradengleichung|Parameter deuten|Sachzusammenhang",
  "Geraden|Gleichungen lösen", "2018-be-gk-B2.1d")
z("2018-be-gk-B2.2a",
  "M₁(1,5 | 1,5 | 2), M₂(3 | 3 | 0); |M₁M₂| = √8,5 ≈ 2,92 m; Seil ≈ 3,50 m",
  "M₁M₂ = (1,5 | 1,5 | −2) ⇒ |M₁M₂| = √8,5|1,2 · 2,915",
  "Mittelpunkt einer Strecke|Betrag eines Vektors|Abstand zweier Punkte|prozentualer Zuschlag",
  "Punkte und Strecken im Koordinatensystem|Vektoren und Rechenoperationen")
z("2018-be-gk-B2.2b",
  "EF = (−6 | 6 | 0) = 2 · AB ⇒ AB ∥ EF ⇒ Trapez; |AE| = |BF| = √13 ≈ 3,61 m",
  "AB = (−3 | 3 | 0), EF = (−6 | 6 | 0)|AE = (3 | 0 | −2), BF = (0 | 3 | −2)",
  "Trapez|Parallelität|kollineare Vektoren|Betrag eines Vektors",
  "Vektoren und Rechenoperationen|Linearkombination und lineare Abhängigkeit")
z("2018-be-gk-B2.2c",
  "φ ≈ 43,3°",
  "n_L = (2 | 2 | 3), n_xy = (0 | 0 | 1)|cos φ = 3/√17 ≈ 0,7276",
  "Winkel zwischen Ebenen|Normalenvektor|Skalarprodukt|Koordinatenebene",
  "Ebenen")
z("2018-be-gk-B2.2d",
  "T′ = E + 5/6 · EF, 0 < 5/6 < 1 ⇒ T′ auf EF; S′(7 | 8 | 0); Schatten = Dreieck R′S′T′",
  "E + t · (F − E) = T′ ⇒ 6 − 6t = 1 ⇒ t = 5/6|Lichtrichtung RR′ = (−1 | −5 | −3)|S + k · (−1 | −5 | −3), z = 0 ⇒ k = 1 ⇒ S′(7 | 8 | 0)",
  "Parallelprojektion|Schattenpunkt|Punkt auf einer Strecke|Teilverhältnis|Lichtrichtung",
  "Punkte und Strecken im Koordinatensystem|Vektoren und Rechenoperationen|Gleichungen lösen")
z("2018-be-gk-B2.2e",
  "Weg: Berührpunkt X auf RT aus dem Teilverhältnis; Gerade durch (0 | 0 | 2) und X; Schnitt mit der Senkrechten x = 5, y = 10 durch P₂; z-Koordinate minus 3",
  "",
  "Lösungsweg beschreiben|Teilverhältnis|Gerade durch zwei Punkte|Schnittpunkt zweier Geraden",
  "Punkte und Strecken im Koordinatensystem|Schnittmengen")
z("2018-be-gk-B3.1a",
  "p = 4/6 · 3/5 = 2/5 = 0,4",
  "",
  "Ziehen ohne Zurücklegen|Pfadmultiplikationsregel|Urnenmodell|Binomialkoeffizient",
  "Baumdiagramm und Pfadregeln|Kombinatorik")
z("2018-be-gk-B3.1b",
  "P(A) ≈ 0,2508; P(B) ≈ 0,0282",
  "X ~ B(10; 0,4) ⇒ P(A) = (10 über 4) · 0,4⁴ · 0,6⁶|P(B) = 0,4 · P(höchstens 1 von 9)|0,6⁹ + 9 · 0,4 · 0,6⁸ ≈ 0,0705",
  "Bernoulli-Formel|Binomialverteilung|unabhängige Teilketten|höchstens ein Treffer",
  "Unabhängigkeit", "2018-be-gk-B3.1a")
z("2018-be-gk-B3.1c",
  "P(C) = 1 − 0,6ⁿ wächst mit n (n = 1: 0,4; n = 10: ≈ 0,994) ⇒ Behauptung falsch",
  "Gegenereignis: kein Gewinn ⇒ 0,6ⁿ|0,6¹⁰ ≈ 0,0060",
  "Gegenereignis|wenigstens ein Treffer|Monotonie|Behauptung prüfen",
  "Ereignisse und Mengenoperationen", "2018-be-gk-B3.1a")
z("2018-be-gk-B3.1d",
  "E(Auszahlung) = 0,4 · 2 € = 0,80 € < 1 € Einsatz ⇒ Anbieter gewinnt im Mittel 0,20 € je Spiel",
  "",
  "Erwartungswert|faires Spiel|Einsatz und Auszahlung",
  "", "2018-be-gk-B3.1a")
z("2018-be-gk-B3.1e",
  "q(2) = 35/57 ≈ 0,614 ≠ 0,5; x = 4 (15 weiße, 6 schwarze ⇒ q = 0,5)",
  "q(x) = 15/(17 + x) · 14/(16 + x)|q(x) = 0,5 ⇒ (17 + x) · (16 + x) = 420 ⇒ x² + 33x − 148 = 0 ⇒ x = 4 (x = −37 entfällt)|Probe: 15/21 · 14/20 = 1/2",
  "Ziehen ohne Zurücklegen|faires Spiel|quadratische Gleichung|Probe",
  "Zufallsexperimente und Urnenmodelle|Gleichungen lösen", "2018-be-gk-B3.1a")
z("2018-be-gk-B3.2a",
  "P(A) = P(X ≤ 8) ≈ 0,3073; P(B) = P(11 ≤ X ≤ 14) ≈ 0,3557",
  "X ~ B(50; 0,2)|P(B) = P(X ≤ 14) − P(X ≤ 10) ≈ 0,9393 − 0,5836",
  "Binomialverteilung|kumulierte Wahrscheinlichkeit|Tabelle|Intervallwahrscheinlichkeit")
z("2018-be-gk-B3.2b",
  "50 fehlerhafte Bildschirme (P(X = 50) ≈ 0,0630)",
  "μ = 250 · 0,2 = 50",
  "wahrscheinlichste Trefferzahl|Erwartungswert|Binomialverteilung",
  "Kenngrößen von Verteilungen")
z("2018-be-gk-B3.2c",
  "richtig: 0,8^(n+1) = 0,8 · 0,8ⁿ < 0,8ⁿ",
  "",
  "kein Treffer|Potenz|Aussage beurteilen|Stichprobenumfang")
z("2018-be-gk-B3.2d",
  "p ≤ 1 − 0,1^(1/25) ≈ 0,088 ⇒ höchstens etwa 8,8 %",
  "(1 − p)²⁵ ≥ 0,1 ⇒ 1 − p ≥ 0,1^(1/25) ≈ 0,9120",
  "kein Treffer|Ungleichung|Wurzel ziehen|Mindestwahrscheinlichkeit",
  "Gleichungen lösen")
z("2018-be-gk-B3.2e",
  "beide defekt 1,0 %; nur Display 9,7 %; nur Netzteil 2,0 %; keines 87,3 %; Ränder Display 10,7/89,3 %, Netzteil 3,0/97,0 %",
  "Display heil: 100 − 10,7 = 89,3 %|nur Netzteil defekt: 89,3 − 87,3 = 2,0 %",
  "Vierfeldertafel|Randwahrscheinlichkeit|Gegenereignis|Schnittmenge",
  "Ereignisse und Mengenoperationen")
z("2018-be-gk-B3.2f",
  "P(N | D) = 0,010/0,107 ≈ 0,0935 ≈ 9,3 %",
  "",
  "bedingte Wahrscheinlichkeit|Vierfeldertafel",
  "Vierfeldertafel", "2018-be-gk-B3.2e")
z("2018-be-gk-B3.2g",
  "nein: ohne Zurücklegen, p ändert sich (6/40 nur beim ersten Zug) ⇒ hypergeometrisch; 10 von 40 zu groß für die Näherung",
  "",
  "Bernoulli-Kette|Voraussetzungen der Binomialverteilung|ohne Zurücklegen|hypergeometrische Verteilung",
  "Hypergeometrische Verteilung|Zufallsexperimente und Urnenmodelle")


# ------------------------------------------------------------- 2019-be-gk
z("2019-be-gk-A1.1a",
  "f′(x) = −20x³ − 6x + 1; F(x) = −x⁵ − x³ + 1/2 x²",
  "",
  "Potenzregel|Summenregel|Stammfunktion",
  "Stammfunktion und Hauptsatz")
z("2019-be-gk-A1.1b",
  "x_Max ∈ [0; 1]: f′(0) = 1 > 0, f′(1) = −25 < 0 ⇒ Vorzeichenwechsel von + nach −",
  "f′(0) = 1, f′(1) = −25",
  "Vorzeichenwechselkriterium|Maximumstelle|Intervall eingrenzen|Monotonie",
  "Ableitung und Änderungsrate", "2019-be-gk-A1.1a")
z("2019-be-gk-A1.2a",
  "g(x) = h(x) ⇒ x² − x − 2 = 0 ⇒ x = −1, x = 2 (quadratische Gleichung, höchstens zwei Lösungen)",
  "2x² − 2x − 4 = 0|g(−1) = h(−1) = −2, g(2) = h(2) = 1",
  "Schnittstellen zweier Graphen|quadratische Gleichung|Anzahl der Lösungen",
  "Schnittmengen|Funktionsklassen und Eigenschaften")
z("2019-be-gk-A1.2b",
  "A = 9",
  "h ≥ g auf [−1; 2]|∫ von −1 bis 2 (−2x² + 2x + 4) dx = [−2/3 x³ + x² + 4x] = 20/3 − (−7/3)",
  "Fläche zwischen zwei Graphen|Differenzfunktion|bestimmtes Integral",
  "Stammfunktion und Hauptsatz", "2019-be-gk-A1.2a")
z("2019-be-gk-A1.3a",
  "z. B. p: x = (5 | 4 | 6) + k · (2 | −5 | −1); s: x = (5 | 3 | 6) + t · (1 | 0 | 2)",
  "Punktprobe: Stützpunkt (5 | 4 | 6) ∉ g|(2 | −5 | −1) · (1 | 0 | 2) = 2 + 0 − 2 = 0",
  "echt parallele Gerade|Punktprobe|senkrecht schneidende Gerade|Skalarprodukt null",
  "Orthogonalität|Lagebeziehungen")
z("2019-be-gk-A1.3b",
  "nein: g und p legen eine Ebene fest; s kann g senkrecht schneiden und aus der Ebene herausführen ⇒ s windschief zu p",
  "",
  "Lage zweier Geraden|windschief|Ebene durch zwei parallele Geraden",
  "Lagebeziehungen|Ebenen", "2019-be-gk-A1.3a")
z("2019-be-gk-A1.4a",
  "11/20",
  "",
  "Laplace-Wahrscheinlichkeit|Anteil")
z("2019-be-gk-A1.4b",
  "11 Frauen > 9 Männer ⇒ mehr Frauenpaare als Männerpaare ⇒ P(zwei Frauen) > P(zwei Männer)",
  "",
  "Begründen ohne Rechnung|Vergleich von Anzahlen|Ziehen ohne Zurücklegen")
z("2019-be-gk-A1.4c",
  "P = 11/20 · 9/19 + 9/20 · 11/19 = 99/190 ≈ 0,52 (oder (11 über 1) · (9 über 1)/(20 über 2))",
  "",
  "Ziehen ohne Zurücklegen|Pfadregeln|zwei Pfade|Binomialkoeffizient",
  "Baumdiagramm und Pfadregeln|Kombinatorik")
z("2019-be-gk-B2.1a",
  "h(2) = 78,4 cm, h(8) = 870,4 cm; maximale Höhe 1000 cm nach 10 Jahren; Wachstumsdauer 10 Jahre",
  "h′(t) = −0,4t³ + 40t = 0 ⇒ t · (−0,4t² + 40) = 0 ⇒ t = 0, t = 10|h″(t) = −1,2t² + 40 ⇒ h″(10) = −80 < 0|h(10) = 1000",
  "Funktionswert|Extrempunkt|hinreichende Bedingung|Sachzusammenhang|Definitionsbereich",
  "Kurvenuntersuchung|Ableitungsregeln|Gleichungen lösen")
z("2019-be-gk-B2.1b",
  "t_m = 10/√3 ≈ 5,77 Jahre; h′(t_m) = 800√3/9 ≈ 154 cm/Jahr",
  "h″(t) = −1,2t² + 40 = 0 ⇒ t² = 100/3 ⇒ t = 10/√3|h′(5,77) ≈ 154",
  "maximale Änderungsrate|Wendestelle|notwendige Bedingung|zweite Ableitung",
  "Kurvenuntersuchung|Gleichungen lösen", "2019-be-gk-B2.1a")
z("2019-be-gk-B2.1c",
  "g(t) = −2t³ + 30t²",
  "g′(t) = 3at² + 2bt|g(5) = 500 ⇒ 125a + 25b = 500|g′(5) = 150 ⇒ 75a + 10b = 150 ⇒ a = −2, b = 30",
  "Steckbriefaufgabe|Bedingungen aufstellen|lineares Gleichungssystem",
  "Gleichungen lösen|Ableitungsregeln")
z("2019-be-gk-B2.1d",
  "h(0) = g(0) = 0 cm; gleiche Wachstumsgeschwindigkeit bei t = 0, t = 5 und t = 10 Jahren",
  "g′(t) = −6t² + 60t|h′(t) = g′(t) ⇒ t · (0,4t² − 6t + 20) = 0 ⇒ t² − 15t + 50 = 0 ⇒ t = 5, t = 10",
  "Funktionswert|Ableitungen gleichsetzen|quadratische Gleichung|Ausklammern",
  "Ableitung und Änderungsrate|Gleichungen lösen", "2019-be-gk-B2.1c")
z("2019-be-gk-B2.1e",
  "t = 5 − 5/√3 ≈ 2,1 Jahre (B schneller) und t = 5 + 5/√3 ≈ 7,9 Jahre (A schneller)",
  "d(t) = g′(t) − h′(t) = 0,4t³ − 6t² + 20t|d′(t) = 1,2t² − 12t + 20 = 0 ⇒ t² − 10t + 50/3 = 0 ⇒ t = 5 ± 5/√3",
  "Differenzfunktion|Extremstellen|notwendige Bedingung|quadratische Gleichung",
  "Kurvenuntersuchung|Gleichungen lösen", "2019-be-gk-B2.1c")
z("2019-be-gk-B2.1f",
  "g′(0) = 0, g′(4) = 144, g′(6) = 144, g′(10) = 0; Parabel mit Scheitel (5 | 150), Nullstellen 0 und 10",
  "g′(2) = g′(8) = 96, g′(5) = 150",
  "Wertetabelle|Graph zeichnen|Parabel|Scheitelpunkt",
  "Funktionsklassen und Eigenschaften", "2019-be-gk-B2.1c")
z("2019-be-gk-B2.1g",
  "A = 62,5 FE; Baum B ist nach 5 Jahren 62,5 cm höher als A (gleiche Starthöhe 0, g′ ≥ h′ auf [0; 5])",
  "∫ von 0 bis 5 (g′(t) − h′(t)) dt = [0,1t⁴ − 2t³ + 10t²] von 0 bis 5 = 62,5",
  "Integral der Änderungsrate|Bestandsdifferenz|Fläche zwischen zwei Graphen|Interpretation",
  "Flächeninhalt durch Integration|Stammfunktion und Hauptsatz", "2019-be-gk-B2.1d|2019-be-gk-B2.1f")
z("2019-be-gk-B2.2a",
  "h(t) → 50 für t → +∞ (8t · e^(−0,04t) → 0); Hormonspiegel fällt auf den Ausgangswert 50 % zurück",
  "",
  "Grenzwert|Verhalten im Unendlichen|Exponentialfunktion dominiert|Asymptote")
z("2019-be-gk-B2.2b",
  "t = 25 Tage; h(25) = 200/e + 50 ≈ 123,6 %",
  "h′(t) = (8 − 0,32t) · e^(−0,04t)|h′(t) = 0 ⇒ 8 − 0,32t = 0 ⇒ t = 25",
  "Maximum|notwendige Bedingung|Produktregel|Kettenregel|Sachzusammenhang",
  "Ableitungsregeln|Gleichungen lösen")
z("2019-be-gk-B2.2c",
  "t = 50 Tage; h(50) = 400e⁻² + 50 ≈ 104,1 %; h′(50) = −8e⁻² ≈ −1,08 % pro Tag",
  "h″(t) = 0 ⇒ −0,64 + 0,0128t = 0 ⇒ t = 50|h(50) = 400e⁻² + 50|h′(50) = (8 − 16) · e⁻²",
  "stärkste Abnahme|Wendestelle|notwendige Bedingung|lokale Änderungsrate",
  "Ableitung und Änderungsrate|Gleichungen lösen", "2019-be-gk-B2.2b")
z("2019-be-gk-B2.2d",
  "(h(7) − h(0))/7 ≈ (92,3 − 50)/7 ≈ 6,0 Prozentpunkte pro Tag",
  "h(7) = 56e^(−0,28) + 50 ≈ 92,32|h(0) = 50",
  "mittlere Änderungsrate|Differenzenquotient|Sachzusammenhang")
z("2019-be-gk-B2.2e",
  "1/70 · (H(70) − H(0)) = 1/70 · (8500 − 19 000e^(−2,8)) ≈ 104,9 > 100",
  "H(70) = −19 000e^(−2,8) + 3500 ≈ 2344,6|H(0) = −5000",
  "Mittelwert einer Funktion|bestimmtes Integral|Stammfunktion|Ungleichung nachweisen",
  "Stammfunktion und Hauptsatz")
z("2019-be-gk-B2.2f",
  "g(t) ≈ −0,88t + 145,7 (exakt m = −14,4e^(−2,8) ≈ −0,876, n ≈ 145,3); g(t) ≤ 50 ab t ≈ 108,75 Tagen (exakt ≈ 108,9)",
  "m = h′(70) = −14,4e^(−2,8) ≈ −0,876|h(70) = 560e^(−2,8) + 50 ≈ 84,05 ⇒ n = 84,05 + 70 · 0,876|−0,88t + 145,7 ≤ 50 ⇒ t ≥ 108,75",
  "Tangentengleichung|Steigung aus der Ableitung|lineare Ungleichung|Sachzusammenhang",
  "Ableitung und Änderungsrate|Gleichungen lösen", "2019-be-gk-B2.2b")
z("2019-be-gk-B2.2g",
  "k ≥ 50e^(2,8)/70 ≈ 11,75",
  "h_k(70) ≥ 100 ⇒ 70k · e^(−2,8) ≥ 50",
  "Parameter bestimmen|Ungleichung|Exponentialfunktion|Funktionenschar",
  "Funktionsscharen und Ortskurven")
z("2019-be-gk-B2.2h",
  "gemeinsam: Startwert 50, Grenzwert 50, Maximumstelle t = 25; Unterschiede: h_k für t > 0 oberhalb von h, größeres Maximum (h_10(25) ≈ 142 gegen 123,6)",
  "h_k′(t) = k · (1 − 0,04t) · e^(−0,04t) = 0 ⇒ t = 25 für jedes k",
  "Funktionenschar|Parameter als Streckfaktor|Grenzwert|Maximum|Graphen vergleichen",
  "Kurvenuntersuchung|Grenzwerte und Verhalten im Unendlichen")
z("2019-be-gk-B3.1a",
  "g: x = (0 | 40 | 6) + r · (30 | 25 | 1); Länge √1526 ≈ 39,06 LE ≈ 3906 m; α ≈ 1,5°",
  "SN = (30 | 25 | 1)|30² + 25² + 1² = 1526|sin α = |SN · (0 | 0 | 1)|/|SN| = 1/√1526",
  "Geradengleichung|Betrag eines Vektors|Winkel zwischen Gerade und Ebene|Maßstab",
  "Vektoren und Rechenoperationen|Skalarprodukt und Winkel|Punkte und Strecken im Koordinatensystem")
z("2019-be-gk-B3.1b",
  "D(15 | 52,5 | 9); Rohr 2,5 LE = 250 m im Berg, insgesamt 252 m",
  "Lot h: x = (15 | 52,5 | 6,5) + t · (0 | 0 | 1)|in F: 150 + 262,5 + 7 · (6,5 + t) = 475,5 ⇒ t = 2,5",
  "Schnittpunkt Gerade–Ebene|Lotgerade|Koordinatenform|Maßstab",
  "Geraden|Gleichungen lösen")
z("2019-be-gk-B3.1c",
  "nicht parallel (AB = (40 | 5 | −0,5) nicht kollinear zu (30 | 25 | 1)); P(28 | 61 | 6,4)",
  "40/30 ≠ 5/25|z = 6,4 ⇒ 6,5 − 0,5t = 6,4 ⇒ t = 0,2 ⇒ P = A + 0,2 · AB",
  "Lage zweier Geraden|kollineare Vektoren|Punkt mit vorgegebener Koordinate|Parameter bestimmen",
  "Lagebeziehungen|Linearkombination und lineare Abhängigkeit|Gleichungen lösen", "2019-be-gk-B3.1a")
z("2019-be-gk-B3.1d",
  "L = |AB| · 100 m ≈ 4031 m; s = 5/9 · L ≈ 2240 m ≈ 2,24 km",
  "AB = (40 | 5 | −0,5) ⇒ |AB| = √1625,25 ≈ 40,31 LE|gleiche Zeit: s/100 = (L − s)/80 ⇒ s = 100/180 · L",
  "Streckenlänge|Betrag eines Vektors|Geschwindigkeit und Zeit|Gleichung aufstellen",
  "Vektoren und Rechenoperationen|Gleichungen lösen")
z("2019-be-gk-B3.2a",
  "Viereck IJKL: I auf BF, J auf CD, K auf DH, L auf EF",
  "",
  "Würfel im Koordinatensystem|Punkte einzeichnen|Schrägbild")
z("2019-be-gk-B3.2b",
  "IL = (−4 | 0 | 4) = 2 · JK ⇒ IL ∥ JK (Trapez), |IL| = 2 · |JK|; |IJ| = |KL| = √35 ⇒ zwei gleich lange Schenkel",
  "JK = (−2 | 0 | 2)|IJ = (−3 | 5 | −1), KL = (1 | −5 | 3)|√32 = 2 · √8",
  "Trapez|kollineare Vektoren|Betrag eines Vektors|Längenverhältnis",
  "Vektoren und Rechenoperationen|Linearkombination und lineare Abhängigkeit")
z("2019-be-gk-B3.2c",
  "φ ≈ 76,2° bei I (und L); bei J und K ≈ 103,8°",
  "IL · IJ = 12 + 0 − 4 = 8|cos φ = 8/(√32 · √35) ≈ 0,239",
  "Winkel zwischen Vektoren|Skalarprodukt|Innenwinkel",
  "Vektoren und Rechenoperationen", "2019-be-gk-B3.2b")
z("2019-be-gk-B3.2d",
  "A = 1/2 · (√32 + √8) · √33 = 3√66 ≈ 24,37 FE",
  "M₁(3 | 0 | 3) Mitte von IL, M₂(1 | 5 | 1) Mitte von JK|h = |M₁M₂| = √33",
  "Trapezformel|Höhe eines symmetrischen Trapezes|Mittelpunkt einer Strecke|Betrag eines Vektors",
  "Punkte und Strecken im Koordinatensystem|Vektoren und Rechenoperationen", "2019-be-gk-B3.2b")
z("2019-be-gk-B3.2e",
  "T: 5x + 4y + 5z = 30; L: 5 + 0 + 25 = 30 ⇒ L ∈ T",
  "K einsetzen ⇒ d = 0 + 20 + 10 = 30",
  "parallele Ebene|gleicher Normalenvektor|Punktprobe|Koordinatenform",
  "Lagebeziehungen")
z("2019-be-gk-B3.2f",
  "r = −2, S(2 | 5 | 5), w = 3/5 ⇒ S teilt GH im Verhältnis 3 : 2",
  "GH: x = (5 | 5 | 5) + w · (−5 | 0 | 0), 0 ≤ w ≤ 1|y: −5u = 5 ⇒ u = −1|z: r² + 1 = 5 ⇒ r = ±2|x: −r = 5 − 5w ⇒ w = 3/5 (r = −2) oder 7/5 (r = 2, außerhalb)",
  "Schnittpunkt zweier Geraden|Gleichungssystem|Parameter|Teilverhältnis|Kante als Strecke",
  "Geraden|Gleichungen lösen|Punkte und Strecken im Koordinatensystem")
z("2019-be-gk-B4.1a",
  "P(E1) = P(X = 80) ≈ 0,099; P(E2) = P(X ≤ 75) ≈ 0,131",
  "X ~ B(100; 0,8)|P(X = 80) = (100 über 80) · 0,8⁸⁰ · 0,2²⁰|P(X ≤ 75) = P(Y ≥ 25) = 1 − 0,8686 mit Y ~ B(100; 0,2)",
  "Binomialverteilung|Bernoulli-Formel|kumulierte Wahrscheinlichkeit|Tabelle|Gegenereignis")
z("2019-be-gk-B4.1b",
  "n ≥ 20,6 ⇒ mindestens 21 Erwachsene",
  "1 − 0,8ⁿ ≥ 0,99 ⇒ 0,8ⁿ ≤ 0,01 ⇒ n ≥ ln 0,01/ln 0,8 ≈ 20,6",
  "Mindestanzahl|Gegenereignis|Exponentialgleichung|Logarithmus|Dreimal-mindestens-Aufgabe",
  "Gleichungen lösen")
z("2019-be-gk-B4.1c",
  "2 527 Prüflinge",
  "jünger als 30: 13 879 − 2 482 = 11 397|11 397 − 8 870",
  "Vierfeldertafel|absolute Häufigkeiten|Gegenereignis")
z("2019-be-gk-B4.1d",
  "P_A(B) = 2 234/2 482 ≈ 0,900 ≠ P(B) = 11 104/13 879 ≈ 0,800 ⇒ A, B abhängig; Ältere bestehen häufiger",
  "Bestandene ab 30: 11 104 − 8 870 = 2 234",
  "bedingte Wahrscheinlichkeit|stochastische Unabhängigkeit|Vierfeldertafel|Interpretation",
  "Bedingte Wahrscheinlichkeit und Bayes|Vierfeldertafel")
z("2019-be-gk-B4.1e",
  "q = (3 − √1,8)/2 ≈ 0,829 (82,9 %); zweite Lösung ≈ 2,17 entfällt",
  "q + (1 − q) · q/2 = 0,9 ⇒ q² − 3q + 1,8 = 0",
  "zweistufiges Experiment|Pfadregeln|quadratische Gleichung|Lösung im Sachzusammenhang",
  "Gleichungen lösen")
z("2019-be-gk-B4.2a",
  "1/6 · 2/6 = 1/18",
  "",
  "Pfadmultiplikationsregel|Laplace-Würfel|zweistufiges Experiment")
z("2019-be-gk-B4.2b",
  "15 günstige von 36 Ergebnissen ⇒ p = 15/36 = 5/12; Tabelle: Sven 1: Tom 2–6, Sven 2: 3–6, 3: 4–6, 4: 5–6, 5: 6",
  "5 + 4 + 3 + 2 + 1 = 15",
  "Laplace-Experiment|Ergebnismenge|günstige Ergebnisse|Tabelle",
  "Kombinatorik")
z("2019-be-gk-B4.2c",
  "E(X) = 30 · 5/12 = 12,5",
  "",
  "Erwartungswert der Binomialverteilung",
  "Binomialverteilung", "2019-be-gk-B4.2b")
z("2019-be-gk-B4.2d",
  "P(A) = P(X = 12) ≈ 0,145; P(B) = 1 − (5/12)³⁰ ≈ 1",
  "X ~ B(30; 5/12)|P(X = 12) = (30 über 12) · (5/12)¹² · (7/12)¹⁸|B: nicht Sven an allen 30 Tagen",
  "Bernoulli-Formel|Gegenereignis|mindestens einmal|Term angeben",
  "Ereignisse und Mengenoperationen", "2019-be-gk-B4.2b")
z("2019-be-gk-B4.2e",
  "P(10 ≤ X ≤ 12): Sven bringt in 30 Tagen mindestens 10-mal und höchstens 12-mal den Müll hinunter (≈ 0,372)",
  "",
  "Term deuten|Bernoulli-Formel|Intervallwahrscheinlichkeit|Sachzusammenhang")
z("2019-be-gk-B4.2f",
  "P(Y ≤ 3) = [(5 über 2) · (5 über 5) + (5 über 3) · (5 über 4)]/(10 über 7) = 60/120 = 1/2; weniger als 2 schwarze unmöglich (nur 5 weiße)",
  "(10 über 7) = 120|(5 über 2) · (5 über 5) = 10, (5 über 3) · (5 über 4) = 50",
  "Ziehen ohne Zurücklegen|hypergeometrische Verteilung|Binomialkoeffizient|günstige Fälle|Ansatz begründen",
  "Hypergeometrische Verteilung|Kombinatorik")


# ------------------------------------------------------------- 2020-be-gk
z("2020-be-gk-A1.1a",
  "f(x) = 8x³ − 1", "",
  "Ableitung der Stammfunktion|Potenzregel",
  "Ableitungsregeln")
z("2020-be-gk-A1.1b",
  "alle Stammfunktionen 2x⁴ − x + C; F₁(x) = 2x⁴ − x + 4, F₂(x) = 2x⁴ − x − 2",
  "Verschiebung um ±3 in y-Richtung ⇒ C = 1 ± 3",
  "Integrationskonstante|Schar der Stammfunktionen|Verschiebung in y-Richtung",
  "", "2020-be-gk-A1.1a")
z("2020-be-gk-A1.2a",
  "f(x) = 1/2 x² + 2x",
  "f(x) = ax² + bx + c|f(0) = 0 ⇒ c = 0|f(2) = 4 · 2 − 2 = 6 ⇒ 4a + 2b = 6|f′(2) = 4 ⇒ 4a + b = 4 ⇒ b = 2, a = 1/2",
  "Steckbriefaufgabe|Tangentenbedingung|lineares Gleichungssystem|quadratische Funktion",
  "Gleichungen lösen|Tangente, Normale, Schnittwinkel")
z("2020-be-gk-A1.3a",
  "AB = (1 | 2 | 1), AC = (−2 | −4 | −2) = −2 · AB ⇒ A, B, C auf g: x = (3 | 4 | −1) + r · (1 | 2 | 1) (C für r = −2)",
  "",
  "kollineare Punkte|Geradengleichung|Punktprobe|Vielfaches eines Vektors",
  "Vektoren und Rechenoperationen|Linearkombination und lineare Abhängigkeit")
z("2020-be-gk-A1.3b",
  "D(2 | 2 | −2)",
  "D = A − AB (r = −1)",
  "Punkt auf einer Geraden|gleicher Abstand|Vektor abtragen",
  "Geraden|Vektoren und Rechenoperationen", "2020-be-gk-A1.3a")
z("2020-be-gk-A1.4a",
  "|AB| = 5 LE",
  "AB = (−3 | 4 | 0) ⇒ √(9 + 16 + 0)",
  "Abstand zweier Punkte|Betrag eines Vektors",
  "Vektoren und Rechenoperationen")
z("2020-be-gk-A1.4b",
  "C(5,5 | −1 | 9) (oder C(5,5 | −1 | 1))",
  "A = 1/2 · 5 · h = 10 ⇒ h = 4|M(5,5 | −1 | 5) Mitte von AB|AB in der Ebene z = 5 ⇒ Höhe in z-Richtung",
  "gleichschenkliges Dreieck|Höhe aus dem Flächeninhalt|Mittelpunkt einer Strecke|senkrecht zur x-y-Ebene",
  "Punkte und Strecken im Koordinatensystem|Gleichungen lösen", "2020-be-gk-A1.4a")
z("2020-be-gk-A1.5a",
  "3/5 · 2/4 + 2/5 · 3/4 = 3/5",
  "",
  "Ziehen ohne Zurücklegen|Pfadregeln|zwei Pfade",
  "Baumdiagramm und Pfadregeln")
z("2020-be-gk-A1.5b",
  "P(erste gewinnt) = 2/5 + 3/5 · 2/4 · 2/3 = 3/5 > 1/2",
  "Gewinnpfade: r | b b r (spätestens im 4. Zug fällt rot)",
  "Ziehen ohne Zurücklegen|Pfadregeln|Gewinnwahrscheinlichkeit|Abbruchbedingung",
  "Zufallsexperimente und Urnenmodelle")
z("2020-be-gk-B2.1a",
  "S_x(0,5 | 0), S_y(0 | −3)",
  "6x − 3 = 0 ⇒ x = 0,5 (e^(−x) ≠ 0)|f(0) = −3",
  "Achsenschnittpunkte|Nullstelle eines Produkts|Exponentialfunktion",
  "Gleichungen lösen")
z("2020-be-gk-B2.1b",
  "f(x) → 0 für x → +∞; f(x) → −∞ für x → −∞",
  "",
  "Verhalten im Unendlichen|Exponentialfunktion dominiert|Grenzwert")
z("2020-be-gk-B2.1c",
  "f′(x) = (−6x + 9) · e^(−x); Extrempunkt P(1,5 | 6e^(−1,5)) ≈ P(1,5 | 1,34)",
  "Produktregel: 6 · e^(−x) + (6x − 3) · (−e^(−x))|f′(x) = 0 ⇒ −6x + 9 = 0 ⇒ x = 1,5|f(1,5) = 6e^(−1,5)",
  "Produktregel|Kettenregel|Extrempunkt|notwendige Bedingung",
  "Kurvenuntersuchung|Gleichungen lösen")
z("2020-be-gk-B2.1d",
  "f′ > 0 für x < 1,5 und f′ < 0 für x > 1,5 (Skizze) ⇒ Vorzeichenwechsel + nach − ⇒ Hochpunkt",
  "",
  "Vorzeichenwechselkriterium|Ableitungsgraph lesen|Hochpunkt",
  "", "2020-be-gk-B2.1c")
z("2020-be-gk-B2.1e",
  "Graph von f für x ≥ 0: von (0 | −3) steigend durch (0,5 | 0) zum Hochpunkt (1,5 | 1,34), dann fallend gegen die x-Achse",
  "",
  "Graph skizzieren|markante Punkte|Asymptote",
  "", "2020-be-gk-B2.1c")
z("2020-be-gk-B2.1f",
  "t(x) = 3/e · x ≈ 1,10x (Ursprungsgerade); α = arctan(3/e) ≈ 47,8°",
  "f(1) = 3/e ≈ 1,104, f′(1) = 3/e|t(x) = 3/e · (x − 1) + 3/e",
  "Tangentengleichung|Steigungswinkel|Arkustangens|Ursprungsgerade",
  "Ableitung und Änderungsrate")
z("2020-be-gk-B2.1g",
  "x_M = 2; Abstand d(2) = 12e⁻² ≈ 1,62",
  "d(x) = f(x) − f′(x) = (12x − 12) · e^(−x)|d′(x) = (24 − 12x) · e^(−x) = 0 ⇒ x = 2",
  "Differenzfunktion|Extremwertaufgabe|notwendige Bedingung|Produktregel",
  "Ableitungsregeln|Gleichungen lösen", "2020-be-gk-B2.1c")
z("2020-be-gk-B2.1h",
  "Nachweis: F mit der Produktregel ableiten, F′ = f zeigen; H(x) = (−6x − 3) · e^(−x) + 20",
  "H = F + C|H(0) = −3 + C = 17 ⇒ C = 20",
  "Stammfunktion nachweisen|Produktregel|Integrationskonstante|Wertebedingung",
  "Ableitungsregeln|Gleichungen lösen")
z("2020-be-gk-B2.1i",
  "A = F(5) − F(1) = −33e⁻⁵ + 9e⁻¹ ≈ 3,09 FE",
  "f > 0 auf [1; 5]|F(5) = −33e⁻⁵ ≈ −0,222, F(1) = −9e⁻¹ ≈ −3,311",
  "bestimmtes Integral|Stammfunktion|Vorzeichen des Integranden",
  "Stammfunktion und Hauptsatz", "2020-be-gk-B2.1h")
z("2020-be-gk-B2.1j",
  "ja, x_T = 2",
  "f″(x) = (6x − 15) · e^(−x)|f′(x) = f″(x) ⇒ −6x + 9 = 6x − 15 ⇒ x = 2",
  "parallele Tangenten|gleiche Steigung|zweite Ableitung|Produktregel",
  "Ableitungsregeln|Gleichungen lösen", "2020-be-gk-B2.1c")
z("2020-be-gk-B2.2a",
  "x₁ = 8, x₂ = −1 (doppelt)",
  "",
  "Nullstellen|Produktform|doppelte Nullstelle")
z("2020-be-gk-B2.2b",
  "f(x) = −1/100 · (x³ − 6x² − 15x − 8) = −1/100 x³ + 3/50 x² + 3/20 x + 2/25; f(x) → −∞ für x → +∞, f(x) → +∞ für x → −∞",
  "(x + 1)² = x² + 2x + 1|(x − 8) · (x² + 2x + 1) = x³ − 6x² − 15x − 8",
  "Ausmultiplizieren|binomische Formel|Grenzverhalten|Leitkoeffizient",
  "Grenzwerte und Verhalten im Unendlichen|Funktionsklassen und Eigenschaften")
z("2020-be-gk-B2.2c",
  "T(−1 | 0), H(5 | 27/25) = H(5 | 1,08)",
  "f′(x) = −3/100 x² + 3/25 x + 3/20 = 0 ⇒ x² − 4x − 5 = 0 ⇒ x = −1, x = 5|f″(x) = −3/50 x + 3/25|f″(−1) = 9/50 > 0, f″(5) = −9/50 < 0|f(−1) = 0, f(5) = 1,08",
  "Extrempunkte|notwendige und hinreichende Bedingung|quadratische Gleichung|zweite Ableitung",
  "Ableitungsregeln|Gleichungen lösen", "2020-be-gk-B2.2b")
z("2020-be-gk-B2.2d",
  "f: (−2 | 0,1), T(−1 | 0), H(5 | 1,08), Nullstelle 8; f′: Parabel mit Nullstellen −1 und 5, Scheitel (2 | 0,27)",
  "f(−2) = 0,1|f′(2) = 0,27",
  "Graphen skizzieren|Zusammenhang f und f′|Parabel",
  "Ableitungsgraph und Funktionsgraph", "2020-be-gk-B2.2c")
z("2020-be-gk-B2.2e",
  "Hochpunkt von f′ bei x = 2 ⇒ Wendepunkt von f bei x = 2 mit größter Steigung",
  "",
  "Wendepunkt|Extremstelle der Ableitung|Krümmungswechsel|größte Steigung",
  "Kurvenuntersuchung")
z("2020-be-gk-B2.2f",
  "t(x) = −0,21x + 2,24; Nullstelle x = 32/3 ≈ 10,67",
  "f′(6) = −21/100 = −0,21|f(6) = 49/50 = 0,98 ⇒ n = 0,98 + 6 · 0,21 = 2,24",
  "Tangentengleichung|Steigung aus der Ableitung|Nullstelle einer Geraden|Gerade einzeichnen",
  "Ableitung und Änderungsrate|Gleichungen lösen", "2020-be-gk-B2.2c")
z("2020-be-gk-B2.2g",
  "Querschnitt ≈ 2,29 − 1,18 = 1,11 m²; Volumen ≈ 1,11 · 5 ≈ 5,5 m³",
  "Dreieck unter t von 6 bis 32/3: 1/2 · 4,67 · 0,98 ≈ 2,29|∫ von 6 bis 8 f(x) dx = [−x⁴/400 + x³/50 + 3x²/40 + 2x/25] = 1,18|Breite 5 m",
  "Fläche zwischen Gerade und Graph|bestimmtes Integral|Dreiecksfläche|Prismenvolumen",
  "Stammfunktion und Hauptsatz|Flächeninhalt und Volumen im Raum", "2020-be-gk-B2.2f")
z("2020-be-gk-B2.2h",
  "x = 2 + √18 ≈ 6,24 (2 − √18 ≈ −2,24 entfällt)",
  "f′(2) = 0,27|f′(x) = −0,27 ⇒ x² − 4x − 14 = 0 ⇒ x = 2 ± √18",
  "Tangentensteigung|quadratische Gleichung|Lösung im Definitionsbereich",
  "Gleichungen lösen|Ableitung und Änderungsrate", "2020-be-gk-B2.2c")
z("2020-be-gk-B3.1a",
  "E₁: 12x + 4y + 9z = 36",
  "(−3 | 9 | 0) × (−3 | 0 | 4) = (36 | 12 | 27) ⇒ n = (12 | 4 | 9)|(3 | 0 | 0) einsetzen ⇒ 36",
  "Parameterform in Koordinatenform|Kreuzprodukt|Normalenvektor",
  "Vektoren und Rechenoperationen|Orthogonalität")
z("2020-be-gk-B3.1b",
  "S_x(3 | 0 | 0), S_y(0 | 9 | 0), S_z(0 | 0 | 4)",
  "36/12 = 3, 36/4 = 9, 36/9 = 4",
  "Spurpunkte|Achsenabschnitte|Koordinatenform",
  "", "2020-be-gk-B3.1a")
z("2020-be-gk-B3.1c",
  "d = 36/√241 ≈ 2,32 LE",
  "|n| = √(144 + 16 + 81) = √241|d = |12 · 0 + 4 · 0 + 9 · 0 − 36|/√241",
  "Hessesche Normalform|Abstand Punkt–Ebene|Betrag des Normalenvektors",
  "", "2020-be-gk-B3.1a")
z("2020-be-gk-B3.1d",
  "nicht parallel ((12 | 4 | 9) kein Vielfaches von (6 | 2 | 9)); g: x = (3 | 0 | 0) + r · (−3 | 9 | 0)",
  "Parameterform von E₁ in E₂: 6 · (3 − 3r − 3s) + 2 · 9r + 9 · 4s = 18 ⇒ 18s = 0 ⇒ s = 0|s = 0 in E₁ einsetzen",
  "Lage zweier Ebenen|Normalenvektoren vergleichen|Schnittgerade|Parameterform einsetzen",
  "Lagebeziehungen|Gleichungen lösen", "2020-be-gk-B3.1a")
z("2020-be-gk-B3.1e",
  "V = 18 VE",
  "A_G = 1/2 · 3 · 9 = 13,5 (rechtwinkliges Dreieck OAB)|h = 4|V = 1/3 · 13,5 · 4",
  "Pyramidenvolumen|Grundfläche|Höhe")
z("2020-be-gk-B3.1f",
  "P(2,7 | 0,9 | 0) (r = 1/10)",
  "g_AB: x = (3 | 0 | 0) + r · (−3 | 9 | 0)|PC = (3r − 3 | −9r | 4)|PC · (−3 | 9 | 0) = 0 ⇒ 9 − 90r = 0 ⇒ r = 0,1",
  "Lotfußpunkt|Orthogonalität|Skalarprodukt null|laufender Punkt",
  "Orthogonalität|Geraden|Gleichungen lösen")
z("2020-be-gk-B3.2a",
  "H(0 | 10 | 6), G(10 | 10 | 6); |EK| = |EL| = √104 ≈ 10,2 m, |KL| = √168 ≈ 13,0 m ⇒ gleichschenklig mit Basis KL",
  "EK = (2 | 10 | 0), EL = (10 | 0 | −2), KL = (8 | −10 | −2)",
  "Koordinaten ablesen|gleichschenkliges Dreieck|Betrag eines Vektors|Seitenlängen vergleichen",
  "Vektoren und Rechenoperationen")
z("2020-be-gk-B3.2b",
  "E_P: x = (10 | 0 | 4) + r · (−10 | 0 | 2) + s · (−8 | 10 | 2); 5x − y + 25z = 150",
  "LE = (−10 | 0 | 2), LK = (−8 | 10 | 2)|LE × LK = (−20 | 4 | −100) ⇒ n = (5 | −1 | 25)|L einsetzen ⇒ 50 − 0 + 100 = 150",
  "Parameterform|Koordinatenform|Kreuzprodukt|Normalenvektor",
  "Vektoren und Rechenoperationen|Orthogonalität")
z("2020-be-gk-B3.2c",
  "E_B: 5x − y + 25z = 50 (gleicher Normalenvektor, B: 50 = 50); maximale Höhe 2,4 m in D′(0 | 10 | 2,4)",
  "B(10 | 0 | 0) einsetzen ⇒ d = 50|höchster Punkt über D (x = 0, y = 10): −10 + 25z = 50 ⇒ z = 2,4",
  "parallele Ebene|Normalenvektor übernehmen|Punktprobe|Schnitt mit einer Kante",
  "Lagebeziehungen|Schnittmengen|Gleichungen lösen", "2020-be-gk-B3.2b")
z("2020-be-gk-B3.2d",
  "Abstand < 4 m: |LB| = 4 m verbindet beide Ebenen, steht aber nicht senkrecht auf ihnen (rechnerisch 100/√651 ≈ 3,92 m)",
  "LB = (0 | 0 | −4) kein Vielfaches von n = (5 | −1 | 25)|d = |150 − 50|/√651",
  "Abstand paralleler Ebenen|kürzeste Verbindung|Lot|Hessesche Normalform",
  "Lagebeziehungen|Orthogonalität", "2020-be-gk-B3.2c")
z("2020-be-gk-B3.2e",
  "A = (4 + 2)/2 · 10 = 30 m²",
  "z = 0,8 in E_B ⇒ 5x − y = 30|y = 0 ⇒ x = 6: S₁(6 | 0 | 0,8); y = 10 ⇒ x = 8: S₂(8 | 10 | 0,8)|parallele Seiten 10 − 6 = 4 und 10 − 8 = 2, Höhe 10",
  "Schnittgerade zweier Ebenen|Trapezfläche|Spurpunkte|Sachzusammenhang",
  "Schnittmengen|Gleichungen lösen", "2020-be-gk-B3.2c")
z("2020-be-gk-B4.1a",
  "P(A) ≈ 0,228; P(B) = (2/3)¹⁰ ≈ 0,017",
  "X ~ B(10; 1/3)|P(X = 4) = (10 über 4) · (1/3)⁴ · (2/3)⁶",
  "Bernoulli-Formel|Binomialverteilung|kein Treffer")
z("2020-be-gk-B4.1b",
  "P(Luisa fängt an) = 1/3 + 2/3 · 1/3 + (2/3)² · 1/3 = 19/27 ≈ 0,704 (oder 1 − (2/3)³)",
  "Baum: je Stufe 6 mit 1/3, keine 6 mit 2/3, Abbruch nach der 6|(2/3)³ = 8/27",
  "mehrstufiges Zufallsexperiment|Baumdiagramm mit Abbruch|Pfadadditionsregel|Gegenereignis",
  "Ereignisse und Mengenoperationen")
z("2020-be-gk-B4.1c",
  "n ≥ 7,39 ⇒ mindestens 8 Würfe",
  "1 − (2/3)ⁿ ≥ 0,95 ⇒ (2/3)ⁿ ≤ 0,05 ⇒ n ≥ ln 0,05/ln(2/3) ≈ 7,39",
  "Mindestanzahl|Gegenereignis|Exponentialgleichung|Logarithmus|Dreimal-mindestens-Aufgabe",
  "Gleichungen lösen")
z("2020-be-gk-B4.1d",
  "P(C) = 1/3 · 1/3 + 1/6 · 1/6 = 5/36 ≈ 0,139",
  "Summe 11 nur als 5 + 6 oder 6 + 5",
  "Pfadregeln|Augensumme|günstige Kombinationen",
  "Zufallsexperimente und Urnenmodelle")
z("2020-be-gk-B4.1e",
  "P = 6 · (1/6 · 1/3 · 1/6) + (1/3)³ = 1/18 + 1/27 = 5/54",
  "Tripel: 4, 5, 6 in sechs Reihenfolgen; 5, 5, 5",
  "Pfadregeln|Anordnungen|Augensumme|dreistufiges Experiment",
  "Kombinatorik")
z("2020-be-gk-B4.1f",
  "falsch: 4, 5, 6 bei beiden 1/18; 5, 5, 5 beim 5er-Würfel 1/27, beim 6er-Würfel 1/216 ⇒ 20/216 > 13/216",
  "6er-Würfel: 6 · (1/6 · 1/6 · 1/3) = 1/18, (1/6)³ = 1/216",
  "Vergleich von Wahrscheinlichkeiten|Pfadregeln|Begründen",
  "Zufallsexperimente und Urnenmodelle", "2020-be-gk-B4.1e")
z("2020-be-gk-B4.2a",
  "P(X ≥ 17) = 1 − P(X ≤ 16) = 1 − 0,4868 ≈ 0,513",
  "",
  "kumulierte Binomialverteilung|Gegenereignis|Tabelle")
z("2020-be-gk-B4.2b",
  "P(X = 13) + P(X = 14) ≈ 0,158: unter den 50 ausgewählten Beschäftigten sind genau 13 oder genau 14 weiblich",
  "",
  "Term deuten|Bernoulli-Formel|Sachzusammenhang")
z("2020-be-gk-B4.2c",
  "P(X = 10) ≈ 0,016",
  "a + 4a = 50 ⇒ a = 10|P(X = 10) = (50 über 10) · (1/3)¹⁰ · (2/3)⁴⁰",
  "Bernoulli-Formel|Bedingung in eine Trefferzahl übersetzen",
  "Gleichungen lösen")
z("2020-be-gk-B4.2d",
  "E(X) = 50/3 ≈ 16,67 ⇒ Maximum der Verteilung bei den Nachbarn 16 oder 17",
  "",
  "Erwartungswert|wahrscheinlichste Trefferzahl|Begründen ohne Rechnung",
  "Kenngrößen von Verteilungen")
z("2020-be-gk-B4.2e",
  "x = 0,895; y = 1/3 · 0,035 ≈ 0,0117",
  "x = 1 − 0,105",
  "Baumdiagramm|Gegenwahrscheinlichkeit am Knoten|Pfadmultiplikationsregel")
z("2020-be-gk-B4.2f",
  "P_u(nicht w) = 0,07/0,0817 ≈ 0,857",
  "P(nicht w ∩ u) = 2/3 · 0,105 = 0,07|P(u) = 1/3 · 0,035 + 2/3 · 0,105 ≈ 0,0817",
  "bedingte Wahrscheinlichkeit|Satz von Bayes|Vierfeldertafel|totale Wahrscheinlichkeit",
  "Vierfeldertafel|Baumdiagramm und Pfadregeln")
z("2020-be-gk-B4.2g",
  "a = 1/3 ≈ 33,3 %",
  "Anteil a weiblich|5 · a · 0,04 = (1 − a) · 0,1 ⇒ 0,3a = 0,1",
  "Anteil als Unbekannte|Pfadprodukte|lineare Gleichung",
  "Gleichungen lösen")


def main():
    # Reihenfolge wie im Katalog (werkzeuge/vorrat-pruef.py verlangt sie)
    with open("abi-katalog.csv", encoding="utf-8", newline="") as fh:
        rang = {r[0]: i for i, r in enumerate(csv.reader(fh, delimiter=";"))}
    w = csv.writer(sys.stdout, delimiter=";", lineterminator="\n")
    w.writerow(["id", "kurz", "zwischen", "stich", "neben", "abh", "sympy"])
    for r in sorted(Z, key=lambda r: rang[r[0]]):
        w.writerow(r)


if __name__ == "__main__":
    main()
