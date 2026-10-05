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


def main():
    w = csv.writer(sys.stdout, delimiter=";", lineterminator="\n")
    w.writerow(["id", "kurz", "zwischen", "stich", "neben", "abh", "sympy"])
    for r in Z:
        w.writerow(r)


if __name__ == "__main__":
    main()
