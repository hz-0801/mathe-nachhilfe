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
