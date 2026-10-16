# Gliederung Dreiecke (P10)

Prüfung: msa
Kapitel: dreiecke
Gebiet: Geometrie
Kurzwort: geo | geometrie
Name: Dreiecke
Folge: 1
Gruppen: Rechtwinklige Dreiecke = pythagoras, trigonometrie | Alle Dreiecke und Vierecke = winkel-dreiecke, symmetrie-abbildungen
Bank: pythagoras | trigonometrie | winkel-dreiecke | symmetrie-abbildungen
Katalog: katalog/pythagoras.md | katalog/trigonometrie.md | katalog/winkel-dreiecke.md | katalog/symmetrie-abbildungen.md
Anzeigenamen: Länge mit Pythagoras = Pythagoras
Kennung alt: Länge mit Pythagoras = P4Z
Anzeigenamen: Seite oder Winkel mit sin, cos, tan = sin, cos, tan
Kennung alt: Seite oder Winkel mit sin, cos, tan = GYW
Anzeigenamen: Seite im allgemeinen Dreieck (Sinussatz) = Sinussatz
Kennung alt: Seite im allgemeinen Dreieck (Sinussatz) = LXA
Kennung alt: Vierecke: Symmetrie und Eigenschaften = 22A
Anzeigenamen: Winkel ohne Rechnung bestimmen oder begründen = Winkel aus Winkeln
Kennung alt: Winkel ohne Rechnung bestimmen oder begründen = T2U
Anzeigenamen: Vierecke: Symmetrie und Eigenschaften = Figuren
Kennung alt: Symmetrie = NUB
Figuren (plan.md § 10, 15.10. p, 16.10. f): Symmetrie (bis 16.10. PG20, Ordner symmetrie) und
Vierecke (bis 16.10. PG30, Ordner vierecke) sind ein Blatt mit zwei Abschnitten, A Symmetrieachsen
gesucht · B Eigenschaft gesucht; die älteren Originale stehen mit auf dem Blatt (auf_blatt = ja,
rang am Ende der Stufe), kein eigenes Mehr.
Kennung: Winkel ohne Rechnung bestimmen oder begründen = PG10
Kennung: Vierecke: Symmetrie und Eigenschaften = PG20
Kennung: Länge mit Pythagoras = PG50
Kennung: Seite oder Winkel mit sin, cos, tan = PG60
Kennung: Seite im allgemeinen Dreieck (Sinussatz) = PG70
Ordner: Winkel ohne Rechnung bestimmen oder begründen = winkel
Ordner: Vierecke: Symmetrie und Eigenschaften = figuren
Ordner: Länge mit Pythagoras = pythagoras
Ordner: Seite oder Winkel mit sin, cos, tan = sin-cos-tan
Ordner: Seite im allgemeinen Dreieck (Sinussatz) = sinussatz
Formelkasten: Länge mit Pythagoras = duden-s21-rechtwinkliges-dreieck
Formelkasten: Seite oder Winkel mit sin, cos, tan = duden-s27-trigonometrische-beziehungen
Formelkasten: Seite im allgemeinen Dreieck (Sinussatz) = duden-s27-sinussatz
Kern am Ende: Länge mit Pythagoras = Die Hypotenuse liegt dem rechten Winkel gegenüber; sie ist die längste Seite, die beiden anderen sind die Katheten. | a² + b² = c²: Die Quadrate über den Katheten sind zusammen so groß wie das Quadrat über der Hypotenuse c. | Hypotenuse gesucht: c = √(a² + b²); Kathete gesucht: a = √(c² − b²). | In Figur oder Körper: Such den rechten Winkel (eine Höhe steht senkrecht); die Strecken daran sind die Katheten (Höhe, Radius oder Durchmesser), gegenüber liegt die Hypotenuse.

Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026): Kapitel → Stufe → Bankaufgaben, Originale,
didaktische Felder. Erzeugt daraus: zuordnung-<kapitel>.csv (werkzeuge/zuordnung.py), die
Zuschnitt-CSV und handgriffe-p10.csv (werkzeuge/gliederung-sichten.py). Stand der Daten: zuordnung.py
und Zuschnitt vom 08.10.2026, Steckbriefe vom 07.10.2026.

## Stufen

### Gleichung aufstellen
- **Anzeigename:** Pythagoras aufstellen
- **Regine:** S. 24
- **Schülerfrage:** Markiere die Hypotenuse. Schreib dann die Gleichung des Satzes des Pythagoras auf.
- **Schülerfrage-Fälle:** Dreieck mit den Seiten p, q und r → r² = p² + q²
- **Schülerfrage-Form:** linie
- **Schülerfrage-Skizze:** \begin{tikzpicture}[line width=0.7pt,scale=0.8]\coordinate (P1) at (0,0);\coordinate (P2) at (2.5,0);\coordinate (P3) at (0.9,1.2);\draw (P1) -- (P2) -- (P3) -- cycle;\pfrw[0.35]{(P3)}{-126.9}\node[font=\small,anchor=north] at (1.25,-0.08) {$r$};\node[font=\small,anchor=south east] at (0.40,0.62) {$p$};\node[font=\small,anchor=south west] at (1.75,0.62) {$q$};\end{tikzpicture}
- **Heranführung:** P4Z 10.10. Nr. 1 (abgenommen), ein Dreieck in schiefer Lage statt drei (aufgabenbank bau/heranfuehrungen-p10.md).
- **Kern:** ja – 5 echte, Basisteil 2017, 2021, 2022, 2024, 2026 (Niveau I), Bank-Kette Hypotenuse mit Grundfall
- **Originale:** 2022-OS-B1g 2024-OS-B1f 2026-FOR-B1j 2021-OS-B1h 2017-OS-B1d
- **Bank:** pythagoras-e1-k2-s6(i) pythagoras-e1-k2-s7(i) pythagoras-e1-k2-s8(i) pythagoras-e1-k5-s4(i) pythagoras-e2-k3-s5(i) pythagoras-e2-k6-s4(i)
- **Zuschnitt:** Länge mit Pythagoras
  - Gleichung aufstellen [2026-FOR-B1j 2024-OS-B1f 2022-OS-B1g]

### Hypotenuse gesucht
- **Anzeigename:** Hypotenuse gesucht
- **Regine:** S. 24
- **Schülerfrage:** Bei welcher Seite ist die Hypotenuse gesucht?
- **Schülerfrage-Fälle:** x → ja | y → nein | z → ja
- **Schülerfrage-Form:** kreuz:
- **Schülerfrage-Skizze:** \begin{tikzpicture}[line width=0.7pt,scale=0.7,font=\footnotesize]\draw (0,0)--(2.4,0)--(2.4,1.6)--cycle;\pfrw[0.25]{(2.4,0)}{90}\node[anchor=north] at (1.2,-0.05) {$6$ cm};\node[anchor=west] at (2.45,0.8) {$4$ cm};\node[anchor=south east] at (1.2,0.85) {$x$};\begin{scope}[xshift=4.8cm]\draw (0,0)--(2.4,0)--(0,1.6)--cycle;\pfrw[0.25]{(0,0)}{0}\node[anchor=north] at (1.2,-0.05) {$y$};\node[anchor=east] at (-0.05,0.8) {$4$ cm};\node[anchor=south west] at (1.25,0.85) {$7$ cm};\end{scope}\begin{scope}[xshift=9.6cm]\draw (0,0.3)--(0.99,1.34)--(2.4,0)--cycle;\pfrw[0.25]{(0.99,1.34)}{-133.6}\node[anchor=south east] at (0.45,0.85) {$5$ cm};\node[anchor=south west] at (1.75,0.75) {$6$ cm};\node[anchor=north] at (1.2,0.1) {$z$};\end{scope}\end{tikzpicture}
- **Heranführung:** P4Z 10.10. Nr. 4 (abgenommen; Lehrer 13.10. „wo ist die Hypotenuse gesucht“).
- **Durchsicht 16.10.:** Erkennen-Aufgabe knapp (15.10. u): gesuchte Seiten x, y, z, kurze Frage; Skizzen größer, ohne Überlappung, jede Zahl mit Einheit.
- **Trennung 13.10.:** wieder eigene Stufe wie im abgenommenen Blatt P4Z vom 10.10. und pruefung.md § 2 (Lehrer 13.10.: P4Z2 hatte Hypotenuse und Kathete zusammengelegt); vorher „Kathete oder Hypotenuse direkt“.
- **Kern:** ja – 2 echte (2020, 2025), Bank-Kette Hypotenuse mit Grundfall
- **Originale:** 2025-OS-K4a 2020-OS-K7a
- **Bank:** pythagoras-e1-k2-s1(i) pythagoras-e1-k2-s2(i) pythagoras-e1-k2-s3(i) pythagoras-e1-k2-s4(i) pythagoras-e1-k2-s5(i) pythagoras-e1-k2-s10 pythagoras-e1-k5-s3 pythagoras-e1-k2-s15[2020-OS-K7a,2025-OS-K4a]
- **Verwechselbar:** Kathete gesucht | Winkel berechnen | Seite berechnen | Seite berechnen (Sinussatz)
- **Zuschnitt:** Länge mit Pythagoras

### Kathete gesucht
- **Anzeigename:** Kathete gesucht
- **Regine:** S. 24
- **Schülerfrage:** Kreuze an, mit welcher Gleichung du die Länge der Seite k berechnest.
- **Schülerfrage-Fälle:** $k = \sqrt{m^2 + g^2}$ → nein | $k = \sqrt{m^2 - g^2}$ → ja | $k = \sqrt{g^2 - m^2}$ → nein
- **Schülerfrage-Form:** kreuz:
- **Schülerfrage-Weg:** m² = k² + g²
- **Schülerfrage-Skizze:** \begin{tikzpicture}[line width=0.7pt,scale=0.85]\coordinate (P1) at (0,0);\coordinate (P2) at (2.8,0);\coordinate (P3) at (0,1.7);\draw (P1) -- (P2) -- (P3) -- cycle;\pfrw[0.35]{(P1)}{0}\node[font=\small,anchor=north] at (1.4,-0.08) {$g$};\node[font=\small,anchor=east] at (-0.08,0.85) {$k$};\node[font=\small,anchor=south west] at (1.44,0.9) {$m$};\end{tikzpicture}
- **Heranführung:** P4Z 10.10. Nr. 7 (abgenommen).
- **Trennung 13.10.:** wie bei „Hypotenuse gesucht“.
- **Kern:** ja – 5 echte 2016–2026 (Niveau I/II), Bank-Kette Kathete mit Grundfall
- **Originale:** 2022-OS-K5a 2024-OS-K6a 2026-FOR-K4a 2019-OS-K3a 2016-OS-K7b
- **Bank:** pythagoras-e2-k3-s1(i) pythagoras-e2-k3-s2(i) pythagoras-e2-k3-s3(i) pythagoras-e2-k3-s6(i) pythagoras-e2-k3-s7 pythagoras-e2-k6-s3 pythagoras-e2-k3-s12[2022-OS-K5a,2024-OS-K6a]
- **Verwechselbar:** Hypotenuse gesucht | Winkel berechnen | Seite berechnen | Seite berechnen (Sinussatz)
- **Zuschnitt:** Länge mit Pythagoras
  - Kathete gesucht [2024-OS-K6a 2026-FOR-K4a 2022-OS-K5a]

### Dreieck erst in Figur oder Körper finden
- **Anzeigename:** Pythagoras versteckt
- **Regine:** S. 24
- **Schülerfrage:** Welche Strecken bilden das rechtwinklige Dreieck? Nenne die beiden Katheten und die Hypotenuse.
- **Schülerfrage-Fälle:** Kegel mit Radius r, Höhe h, Mantellinie s = Katheten r und h, Hypotenuse s | Zylinder mit Radius r, Höhe h; Stab vom Rand des Bodens schräg zum gegenüberliegenden oberen Rand = Katheten 2 · r und h, Hypotenuse der Stab
- **Schülerfrage-Form:** linie
- **Durchsicht 13.10.:** Schritt B (Daten): ’26 · 2c (Turm, Kegelhöhe) und ’22 · 2c (Becher) hier; ’25 · 2a (Drachen, AB) nur auf Symmetrie (Hauptplatz, ungekürzt): eine Zeile je Original trägt nur eine Einheitsfassung, die Symmetrie-Frage ließe sich hier nicht ausblenden (Wunsch an den Setzer im Bericht).
- **Kern:** ja – 5 echte (2018, 2019, 2025 zweimal, 2026), Bank-Kette Figuren und Körper mit Grundfall
- **Originale:** 2026-FOR-K2c 2022-OS-K2c 2018-OS-K6d 2019-OS-K2d
- **Bank:** pythagoras-e3-k2-s1(i) pythagoras-e3-k2-s2(i) pythagoras-e3-k2-s3(i) pythagoras-e3-k2-s4(i) pythagoras-e3-k2-s5(i) pythagoras-e3-k2-s6(i) pythagoras-e3-k2-s7(i) pythagoras-e3-k2-s8(i) pythagoras-e3-k2-s9(i) pythagoras-e3-k2-s10(i) pythagoras-e3-k2-s11(i) pythagoras-e3-k2-s12(i) pythagoras-e3-k2-s16(i) pythagoras-e3-k2-s17(i) pythagoras-e3-k2-s13 pythagoras-e3-k2-s14 pythagoras-e3-k2-s15 pythagoras-e3-k4-s3 pythagoras-e3-k2-s19[2026-FOR-K2c,2018-OS-K6d,2019-OS-K2d,2022-OS-K2c]
- **Zuschnitt:** Länge mit Pythagoras
  - Dreieck versteckt [2026-FOR-K2c 2022-OS-K2c] neben [2025-OS-K2a]

### Seitenverhältnis benennen
- **Anzeigename:** sin, cos, tan aufstellen
- **Regine:** S. 34
- **Schülerfrage:** Benenne die Seiten des Dreiecks aus Sicht des Winkels α.
- **Schülerfrage-Fälle:** Dreieck ABC mit dem rechten Winkel bei C = Gegenkathete a, Ankathete b, Hypotenuse c
- **Schülerfrage-Form:** antwort:Gegenkathete|;Ankathete|;Hypotenuse|
- **Schülerfrage-Skizze:** \begin{tikzpicture}[line width=0.7pt,font=\small,scale=0.8]\coordinate (C) at (0,0);\coordinate (B) at (3,0);\coordinate (A) at (0,2);\draw (A) -- (B) -- (C) -- cycle;\pfrw[0.35]{(C)}{0}\pfwinkel[0.7][0.62]{(A)}{-90}{-56.3}{\alpha}\node[anchor=south] at (A) {$A$};\node[anchor=west] at (B) {$B$};\node[anchor=north east] at (C) {$C$};\node[anchor=north] at (1.5,0) {$a$};\node[anchor=east] at (0,1) {$b$};\node[anchor=south west] at (1.5,1) {$c$};\end{tikzpicture}
- **Durchsicht 13.10.:** Schritt B (Daten): erst die Seiten aus Sicht des Winkels benennen (Lehrer 11.10. „benennen“), dann ’25 · 1g mit fremden Buchstaben.
- **Kern:** ja – 6 echte, Basisteil 2017–2020 und 2025 (Niveau I), Grundfall der Bank-Kette Seite berechnen
- **Originale:** 2025-OS-B1g 2020-OS-B1c 2020-OS-B1j 2019-OS-B1h 2018-OS-B1g 2017-OS-B1j
- **Bank:** trigonometrie-e1-k3-s1(i) trigonometrie-e1-k3-s2(i) trigonometrie-e1-k4-s1(i) trigonometrie-e1-k3-s12(i) trigonometrie-e1-k3-s17[2020-OS-B1c,2020-OS-B1j,2025-OS-B1g]
- **Zuschnitt:** Seite oder Winkel mit sin, cos, tan

### Winkel berechnen
- **Anzeigename:** Winkel gesucht
- **Regine:** S. 34
- **Schülerfrage:** Welche zwei Seiten kennst du aus Sicht des Winkels am Boden? Schreib sin oder cos dazu; rechne nicht.
- **Schülerfrage-Fälle:** Leiter 5 m lang, sie reicht 4,8 m hoch an der Wand = Gegenkathete und Hypotenuse: sin | Leiter 5 m lang, ihr Fuß steht 1,4 m vor der Wand = Ankathete und Hypotenuse: cos
- **Schülerfrage-Form:** linie
- **Durchsicht 13.10.:** Schritt B (Daten): ’22 · 5b (sin) und ’24 · 6b, ’26 · 4b (cos) – der Anstoß übt nur, welche Funktion die beiden gegebenen Seiten verbindet.
- **Kern:** ja – 5 echte (2019, 2020, 2022, 2024, 2026), Bank-Kette Winkel berechnen mit Grundfall
- **Originale:** 2022-OS-K5b 2024-OS-K6b 2026-FOR-K4b 2020-OS-K5b 2019-OS-K3b
- **Bank:** trigonometrie-e2-k1-s1(i) trigonometrie-e2-k1-s2(i) trigonometrie-e2-k1-s3(i) trigonometrie-e2-k1-s4(i) trigonometrie-e2-k1-s5(i) trigonometrie-e2-k1-s6(i) trigonometrie-e2-k1-s8(i) trigonometrie-e2-k1-s9(i) trigonometrie-e2-k1-s10(i) trigonometrie-e2-k1-s7 trigonometrie-e2-k4-s3 trigonometrie-e2-k1-s12[2022-OS-K5b,2024-OS-K6b,2026-FOR-K4b,2019-OS-K3b]
- **Verwechselbar:** Hypotenuse gesucht | Kathete gesucht | Seite berechnen | Seite berechnen (Sinussatz)
- **Zuschnitt:** Seite oder Winkel mit sin, cos, tan
  - Winkel berechnen [2022-OS-K5b 2024-OS-K6b 2026-FOR-K4b] neben [2025-OS-K4a]

### Seite berechnen
- **Anzeigename:** Seite gesucht
- **Regine:** S. 34
- **Schülerfrage:** Stelle die Formel $\sin\alpha = \frac{a}{c}$ um.
- **Schülerfrage-Fälle:** nach a → $a = c \cdot \sin\alpha$ | nach c → $c = \frac{a}{\sin\alpha}$
- **Schülerfrage-Form:** linie
- **Durchsicht 13.10.:** Schritt B (Daten): Umstellen an der einfachen Formel ohne Zahlen (befunde-M3 AZL2), die beiden Lagen kommen in ’23 · 7b (BF oben, BC unten) und ’22 · 5d, ’26 · 4c (unten) vor; ’23 · 7b als schwerste echte am Ende.
- **Kern:** ja – 8 echte 2016–2026, Bank-Ketten Seite berechnen und Teildreiecke mit Grundfall
- **Originale:** 2022-OS-K5d 2026-FOR-K4c 2023-OS-K7b 2021-OS-K3a 2021-OS-K3b 2018-OS-K4d 2017-OS-K4b 2016-OS-K7c
- **Bank:** trigonometrie-e1-k3-s4(i) trigonometrie-e1-k3-s5(i) trigonometrie-e1-k3-s6(i) trigonometrie-e1-k3-s7(i) trigonometrie-e1-k3-s8(i) trigonometrie-e1-k3-s9(i) trigonometrie-e1-k3-s10(i) trigonometrie-e1-k3-s11(i) trigonometrie-e1-k3-s13(i) trigonometrie-e1-k3-s14(i) trigonometrie-e3-k1-s1(i) trigonometrie-e3-k1-s2(i) trigonometrie-e3-k1-s3(i) trigonometrie-e1-k3-s15 trigonometrie-e1-k7-s3 trigonometrie-e3-k1-s8 trigonometrie-e1-k3-s17[2022-OS-K5d,2021-OS-K3a,2021-OS-K3b,2017-OS-K4b] trigonometrie-e3-k1-s19[2026-FOR-K4c,2023-OS-K7b,2018-OS-K4d,2016-OS-K7c]
- **Verwechselbar:** Hypotenuse gesucht | Kathete gesucht | Winkel berechnen | Seite berechnen (Sinussatz)
- **Zuschnitt:** Seite oder Winkel mit sin, cos, tan
  - Seite berechnen [2022-OS-K5d 2026-FOR-K4c 2023-OS-K7b] neben [2022-OS-K5e 2023-OS-K2c]

### erst entscheiden, dann rechnen
- **Anzeigename:** Pythagoras oder sin, cos, tan?
- **Regine:** S. 24 · 34
- **Schülerfrage:** Womit rechnest du – Pythagoras oder sin, cos, tan? Rechne nicht.
- **Schülerfrage-Fälle:** Du kennst zwei Seiten; gesucht ist die dritte Seite = Pythagoras | Du kennst zwei Seiten; gesucht ist ein Winkel = sin, cos, tan | Du kennst eine Seite und einen Winkel; gesucht ist eine Seite = sin, cos, tan
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** Kommt ein Winkel vor (gegeben oder gesucht), dann sin, cos, tan; nur Seiten, dann Pythagoras.
- **Durchsicht 13.10.:** Schritt B (Daten): Schlussstufe nur mit dem Anstoß, ohne eigene echte (Lehrer 11.10.: darf das Ende des Blatts sein). Echte am Ende: ’19 · 2d (Strecke BC mit Pythagoras, Winkel β mit tan, ungekürzt; älteres Original, Setzer v0.11). Die Rampe ’25 · 4a (x und α in einem Teil) wäre die junge Wahl, steht aber gekürzt auf Pythagoras; eine Zeile trägt nur eine Einheitsfassung – Wunsch im Bericht.
- **Kern:** nein – Schlussstufe (Lehrer 10.10., Befund Geometrie § 3): Winkel gegeben oder gesucht → sin, cos, tan, nur Seiten → Pythagoras; die echten sind dieselben wie bei Pythagoras und Winkel (2025-OS-K4a hat beides in einem Teil), kein eigenes Blatt; Mischsprossen der Bank
- **Originale:** 
- **Bank:** pythagoras-e2-k3-s11(i) trigonometrie-e2-k1-s11(i) trigonometrie-e4-k1-s16(i) trigonometrie-e3-k1-s14(i) pythagoras-e3-k2-s18
- **Zuschnitt:** Seite oder Winkel mit sin, cos, tan

### Seite berechnen (Sinussatz)
- **Anzeigename:** Seite gesucht
- **Regine:** S. 36
- **Schülerfrage:** Im Sinussatz steht jede Seite mit dem Winkel, der ihr gegenüberliegt. Im Dreieck ABC kennst du die Seite c und die Winkel α und β; gesucht ist die Seite a.
- **Schülerfrage-Fälle:** Welchen Winkel rechnest du zuerst aus? → γ = 180° − α − β | Welche Gleichung stellst du dann auf? → a : sin α = c : sin γ
- **Schülerfrage-Form:** linie
- **Schülerfrage-Skizze:** \begin{tikzpicture}[line width=0.7pt,font=\small,scale=0.9]\coordinate (A) at (0,0);\coordinate (B) at (3.4,0);\coordinate (C) at (1.1,1.9);\draw (A)--(B)--(C)--cycle;\pfwinkel[0.55][0.62]{(A)}{0}{59.9}{\alpha}\pfwinkel[0.55][0.62]{(B)}{140.4}{180}{\beta}\pfwinkel[0.45][0.62]{(C)}{-120.1}{-39.6}{\gamma}\node[anchor=north east] at (A) {$A$};\node[anchor=north west] at (B) {$B$};\node[anchor=south] at (C) {$C$};\node[anchor=north] at (1.7,0) {$c$};\node[anchor=south west] at (2.25,0.95) {$a$};\node[anchor=south east] at (0.55,0.95) {$b$};\end{tikzpicture}
- **Durchsicht 13.10.:** Schritt B (Daten): beide jungen Originale brauchen zuerst den dritten Winkel (’24 · 6d: 35°, ’25 · 4c: 35°); der Anstoß übt genau das und das Paar Seite–Gegenwinkel, ohne Zahlen. ’25 · 4c (stumpfer Winkel, Stern) am Ende.
- **Kern:** ja – 9 echte 2014–2025, fast jedes Jahr (Niveau II), Bank-Kette Sinussatz mit Grundfall
- **Originale:** 2024-OS-K6d 2025-OS-K4c 2021-OS-K3c 2020-OS-K7c 2019-OS-K3c 2018-OS-K4c 2017-OS-K4c 2015-OS-K5c 2014-OS-K2b
- **Bank:** trigonometrie-e4-k1-s1(i) trigonometrie-e4-k1-s2(i) trigonometrie-e4-k1-s3(i) trigonometrie-e4-k1-s4(i) trigonometrie-e4-k1-s5(i) trigonometrie-e4-k1-s6(i) trigonometrie-e4-k1-s7(i) trigonometrie-e4-k1-s9(i) trigonometrie-e4-k2-s3(i) trigonometrie-e4-k1-s10 trigonometrie-e4-k1-s17
- **Verwechselbar:** Hypotenuse gesucht | Kathete gesucht | Winkel berechnen | Seite berechnen
- **Zuschnitt:** Seite im allgemeinen Dreieck (Sinussatz)
  - Seite berechnen [2024-OS-K6d 2025-OS-K4c]

### Symmetrieachsen zählen
- **Anzeigename:** Symmetrieachsen gesucht
- **Begriff:** Symmetrieachse: Faltest du die Figur an ihr, liegen beide Hälften genau aufeinander.
- **Schülerfrage:** Wie viele Symmetrieachsen hat die Figur?
- **Schülerfrage-Fälle:** Rechteck, das kein Quadrat ist = 2 | Parallelogramm, das weder Rechteck noch Raute ist = 0
- **Schülerfrage-Form:** linie
- **Schülerfrage-Skizze:** \begin{tikzpicture}[line width=0.7pt,font=\small]\draw (0,0) rectangle (2,1.1);\node at (1,-0.35) {a)};\draw (2.8,0)--(4.6,0)--(5.2,1.1)--(3.4,1.1)--cycle;\node at (4,-0.35) {b)};\end{tikzpicture}
- **Durchsicht 13.10.:** Schritt B (Daten): ’22 · 1i (gleichschenkliges Trapez) und ’25 · 2a (Drachen, ungekürzt mit BF und AB über Pythagoras) aufs Blatt; ’21 · 1j in den Mehr-Block. Der Anstoß übt die Falle Diagonale als Achse.
- **Kern:** ja – 3 echte, Basisteil 2021 und 2022, Kontext 2025 (Niveau I), Bank-Kette Symmetrieachsen bestimmen mit Grundfall
- **Originale:** 2022-OS-B1i 2025-OS-K2a 2021-OS-B1j
- **Bank:** symmetrie-abbildungen-e2-k2-s2(i) symmetrie-abbildungen-e2-k2-s3(i) symmetrie-abbildungen-e2-k2-s4(i) symmetrie-abbildungen-e2-k2-s5(i) symmetrie-abbildungen-e2-k2-s6(i) symmetrie-abbildungen-e2-k2-s7(i) symmetrie-abbildungen-e2-k2-s8(i) symmetrie-abbildungen-e2-k2-s11 symmetrie-abbildungen-e2-k2-s12
- **Zuschnitt:** Vierecke: Symmetrie und Eigenschaften

### Eigenschaft erkennen
- **Anzeigename:** Eigenschaft gesucht
- **Schülerfrage:** Ein Trapez ist ein Viereck mit mindestens zwei parallelen Seiten. Ist das Viereck ein Trapez?
- **Schülerfrage-Fälle:** Rechteck = ja | Parallelogramm = ja | Drachenviereck, das keine Raute ist = nein
- **Schülerfrage-Form:** kreuz:Trapez
- **Schülerfrage-Skizze:** \begin{tikzpicture}[line width=0.7pt,font=\small]\draw (0,0) rectangle (1.6,1);\node at (0.8,-0.45) {a)};\draw (2.2,0)--(3.8,0)--(4.3,1)--(2.7,1)--cycle;\node at (3.25,-0.45) {b)};\draw (5.6,1.2)--(6.1,0.6)--(5.6,-0.3)--(5.1,0.6)--cycle;\node at (5.6,-0.6) {c)};\end{tikzpicture}
- **Durchsicht 13.10.:** Schritt B (Daten): ’26 · 1c fragt, was für jedes Trapez gilt; der Anstoß zeigt, dass „mindestens zwei parallel“ auch Rechteck und Parallelogramm einschließt.
- **Kern:** nein – 2 echte (Basisteil 2016, 2026), Ankreuzen als Sprosse der Kette Winkelsumme
- **Originale:** 2026-FOR-B1c 2016-OS-B1e
- **Bank:** winkel-dreiecke-e3-k2-s10(i) symmetrie-abbildungen-e2-k5-s1(i)
- **Zuschnitt:** Vierecke: Symmetrie und Eigenschaften
- **Hinweis:** Lehrer 11.10.: nach Vierecke verschoben

### Winkelsumme
- **Anzeigename:** Winkel gesucht
- **Regine:** S. 23
- **Schülerfrage:** Nenne die Innenwinkelsumme im Dreieck. Gib dann den Winkel mit dem Fragezeichen an.
- **Schülerfrage-Fälle:** Innenwinkelsumme im Dreieck → 180 | Winkel mit dem Fragezeichen → 112
- **Schülerfrage-Form:** linie:°
- **Schülerfrage-Weg:** ? + 68° = 180°
- **Schülerfrage-Skizze:** \begin{tikzpicture}[line width=0.7pt,font=\small]\draw (-1.4,0)--(1.8,0);\draw (0,0)--(68:1.6);\pfwinkel[0.6][0.62]{(0,0)}{0}{68}{68^\circ}\pfwinkel[0.45][0.62]{(0,0)}{68}{180}{?}\end{tikzpicture}
- **Heranführung:** Lehrer 13.10. (T2U2 Nr. 1b unverständlich, besser „Viereck 360°, Dreieck?“).
- **Durchsicht 16.10.:** Nr. 1 neu (Durchsicht PG10 S. 10): Innenwinkelsumme und Nebenwinkel an einer Geraden – genau die Rechnung von ’26 · 1i und ’23 · 2a; „Viereck 360°“ verriet mehr, als es fragte.
- **Durchsicht 13.10.:** Schritt B (Daten): ’26 · 1i und ’23 · 2a brauchen die Parallelen, ’22 · 5c die Winkelsumme im Teildreieck; 2018-OS-K4b (älter als fünf Jahre) in den Mehr-Block.
- **Kern:** ja – 7 echte 2015–2026 (Niveau I), Bank-Kette Winkelsumme mit Grundfall
- **Originale:** 2022-OS-K5c 2023-OS-K2a 2026-FOR-B1i 2021-OS-B1i 2018-OS-K4b 2017-OS-K4a 2015-OS-K5b
- **Bank:** winkel-dreiecke-e3-k2-s1(i) winkel-dreiecke-e3-k2-s2(i) winkel-dreiecke-e3-k2-s4(i) winkel-dreiecke-e3-k2-s5(i) winkel-dreiecke-e3-k2-s6(i) winkel-dreiecke-e3-k2-s7(i) winkel-dreiecke-e3-k2-s11(i) winkel-dreiecke-e3-k4-s3(i) winkel-dreiecke-e2-k2-s9
- **Zuschnitt:** Winkel ohne Rechnung bestimmen oder begründen

### gleichschenkliges Dreieck
- **Anzeigename:** Basiswinkel gesucht
- **Begriff:** Basiswinkel: die zwei gleichen Winkel an der Grundseite des gleichschenkligen Dreiecks.
- **Heranführung:** Nr. 5 fällt weg (plan.md § 10, 15.10. l: das Prinzip steckt im Original); der Begriff steht über der ersten Aufgabe (16.10. e).
- **Durchsicht 13.10.:** Schritt B (Daten): ’23 · 1g (Seite ablesen, γ ausrechnen; je eine Antwortzeile) und ’23 · 7a (begründen).
- **Kern:** nein – 2 echte, nur 2023
- **Originale:** 2023-OS-B1g 2023-OS-K7a
- **Bank:** winkel-dreiecke-e3-k2-s3(i) winkel-dreiecke-e3-k2-s8(i) winkel-dreiecke-e3-k2-s13[2023-OS-B1g]
- **Zuschnitt:** Winkel ohne Rechnung bestimmen oder begründen

### rechten Winkel begründen
- **Anzeigename:** rechten Winkel begründen
- **Schülerfrage:** CD steht senkrecht auf AB. Trage die Winkel in den Dreiecken ADC und DBC ein. Warum ist γ = 90°?
- **Schülerfrage-Fälle:** Begründung → in beiden Dreiecken je 45° bei C: 45° + 45° = 90°
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** AD = DC = DB = 3 cm ⇒ je 45°
- **Schülerfrage-Skizze:** \begin{tikzpicture}[line width=0.7pt,scale=0.9]\draw (0,0)--(3,0)--(1.5,1.5)--cycle;\draw (1.5,1.5)--(1.5,0);\pfrw[0.28]{(1.5,0)}{0}\pfwinkel*[0.7]{(1.5,1.5)}{-135}{-45}{}\node[inner sep=0pt,font=\footnotesize] at ($(1.5,1.5)+(-108:0.45)$) {$\gamma$};\node[font=\small,anchor=north east] at (0,0) {$A$};\node[font=\small,anchor=north west] at (3,0) {$B$};\node[font=\small,anchor=south] at (1.5,1.5) {$C$};\node[font=\small,anchor=north] at (1.5,-0.02) {$D$};\node[font=\footnotesize,anchor=north] at (0.75,-0.02) {$3$ cm};\node[font=\footnotesize,anchor=north] at (2.25,-0.02) {$3$ cm};\node[font=\footnotesize,anchor=east] at (1.47,0.3) {$3$ cm};\end{tikzpicture}
- **Heranführung:** T2U 11.10. Nr. 8 (abgenommen; Kritiker B 13.10.: macht den Gedanken für den Drachen ’25 · 2c vor).
- **Durchsicht 13.10.:** Schritt B (Daten): der Anstoß trägt den Gedanken von ’25 · 2c (AF = DF, also 45° bei D, zweimal) ohne die Figur vorwegzunehmen.
- **Kern:** nein – 1 echte (2025), Begründen auf mehreren Wegen (Winkelsumme, Umkehrung, Thales)
- **Originale:** 2025-OS-K2c
- **Bank:** winkel-dreiecke-e3-k2-s9(i) winkel-dreiecke-e5-k1-s8(i) pythagoras-e2-k3-s9(i) winkel-dreiecke-e5-k1-s11 winkel-dreiecke-e3-k2-s13[2025-OS-K2c] pythagoras-e2-k3-s12[2025-OS-K2c]
- **Zuschnitt:** Winkel ohne Rechnung bestimmen oder begründen

## Plätze der Originale

Jede Teilaufgabe 2014–2026 (OS, EBR, FOR, GYM) mit ihrem Hauptplatz (Stufe, deren Handgriff die
ganze Teilaufgabe ist), „ganz auch“ (die ganze Aufgabe ist dieser Handgriff, obwohl anders
etikettiert) und Zwischenschritt; Stufen anderer Kapitel mit „kapitel:“. Erzeugt daraus:
msa/handgriffe-p10.csv (werkzeuge/gliederung-sichten.py).

| id | Hauptplatz | Ganz auch | Zwischenschritt | Begründung |
|---|---|---|---|---|
| 2014-GYM-B1f | Eigenschaft erkennen |  |  | Hauptplatz nach typ „Eigenschaft einer Figur zuordnen“ |
| 2014-OS-K2b | Seite berechnen (Sinussatz) |  | Winkelsumme | Hauptplatz nach typ „Sinussatz Seite berechnen“. Winkel bei J über Winkelsumme, rechtwinkliger Weg nur Alternative |
| 2015-GYM-K2c |  |  | Dreieck erst in Figur oder Körper finden | Hauptplatz außerhalb der P10-Stufen. RO über Pythagoras aus Koordinaten |
| 2015-GYM-K4a | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2015-GYM-K5b |  |  | Seite berechnen (Sinussatz) | Hauptplatz außerhalb der P10-Stufen. Sinussatz (nach einem Winkel umgestellt) |
| 2015-OS-K5b | Winkelsumme |  |  | Hauptplatz nach typ „Winkelsumme im Dreieck anwenden“ |
| 2015-OS-K5c | Seite berechnen (Sinussatz) |  |  | Hauptplatz nach typ „Sinussatz Seite berechnen“. rechtwinkliger Weg nur Alternative |
| 2016-GYM-B1e | Eigenschaft erkennen |  |  | GYM-Zwilling von 2016-OS-B1e |
| 2016-GYM-K4d | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2016-OS-B1e | Eigenschaft erkennen |  |  | Hauptplatz nach typ „Eigenschaft einer Figur zuordnen“ |
| 2016-OS-K7b | Kathete gesucht |  |  | Hauptplatz nach typ „Pythagoras Kathete“. Weg über sin 54° nur Alternative |
| 2016-OS-K7c | Seite berechnen |  | Winkelsumme | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“. Zwischenschritt aus typ_neben |
| 2017-GYM-B1d | Gleichung aufstellen |  |  | GYM-Zwilling von 2017-OS-B1d |
| 2017-GYM-B1j | Seitenverhältnis benennen |  |  | GYM-Zwilling von 2017-OS-B1j |
| 2017-GYM-K2d | Dreieck erst in Figur oder Körper finden |  |  | Hauptplatz nach typ „Streckenlänge aus Koordinaten berechnen“ |
| 2017-GYM-K3b |  |  | Dreieck erst in Figur oder Körper finden | Hauptplatz außerhalb der P10-Stufen. Drachenseiten über Pythagoras |
| 2017-GYM-K3d | Winkel berechnen |  |  | Hauptplatz nach typ „Winkel im rechtwinkligen Dreieck berechnen“ |
| 2017-OS-B1d | Gleichung aufstellen |  |  | Hauptplatz nach typ „Pythagoras Gleichung zuordnen“ |
| 2017-OS-B1j | Seitenverhältnis benennen |  |  | Hauptplatz nach typ „Winkelfunktion Seitenverhältnis angeben“ |
| 2017-OS-K4a | Winkelsumme |  |  | Hauptplatz nach typ „Winkelsumme im Dreieck anwenden“ |
| 2017-OS-K4b | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2017-OS-K4c | Seite berechnen (Sinussatz) |  | flaechen:Fläche gesucht | Hauptplatz nach typ „Sinussatz Seite berechnen“. Zwischenschritt aus typ_neben |
| 2018-GYM-B1g | Seitenverhältnis benennen |  |  | GYM-Zwilling von 2018-OS-B1g |
| 2018-GYM-K2e | Dreieck erst in Figur oder Körper finden |  |  | Hauptplatz nach typ „Streckenlänge aus Koordinaten berechnen“ |
| 2018-GYM-K3b | Winkel berechnen |  |  | Hauptplatz nach typ „Winkel im rechtwinkligen Dreieck berechnen“ |
| 2018-GYM-K4a |  |  | Seite berechnen | Hauptplatz außerhalb der P10-Stufen. Teilstrecken über sin und cos |
| 2018-GYM-K4b | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2018-OS-B1g | Seitenverhältnis benennen |  |  | Hauptplatz nach typ „Winkelfunktion Seitenverhältnis angeben“ |
| 2018-OS-K4b | Winkelsumme |  |  | Hauptplatz nach typ „Winkelsumme im Dreieck anwenden“ |
| 2018-OS-K4c | Seite berechnen (Sinussatz) |  |  | Hauptplatz nach typ „Sinussatz Seite berechnen“ |
| 2018-OS-K4d | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2018-OS-K6d | Dreieck erst in Figur oder Körper finden |  |  | Hauptplatz nach typ „Mantellinie Kegel bestimmen“ |
| 2019-GYM-B1h | Seitenverhältnis benennen |  |  | GYM-Zwilling von 2019-OS-B1h |
| 2019-GYM-K3b | Hypotenuse gesucht |  |  | Hauptplatz nach typ „Pythagoras Hypotenuse“ |
| 2019-OS-B1h | Seitenverhältnis benennen |  |  | Hauptplatz nach typ „Winkelfunktion Seitenverhältnis angeben“ |
| 2019-OS-K2d | Dreieck erst in Figur oder Körper finden |  | Winkel berechnen | Hauptplatz nach typ „Streckenlänge aus Koordinaten berechnen“. Zwischenschritt aus typ_neben |
| 2019-OS-K3a | Kathete gesucht |  |  | Hauptplatz nach typ „Pythagoras Kathete“ |
| 2019-OS-K3b | Winkel berechnen |  |  | Hauptplatz nach typ „Winkel im rechtwinkligen Dreieck berechnen“ |
| 2019-OS-K3c | Seite berechnen (Sinussatz) |  | Winkelsumme | Hauptplatz nach typ „Sinussatz Seite berechnen“. Zwischenschritt aus typ_neben |
| 2020-GYM-B1a | Hypotenuse gesucht |  |  | Hauptplatz nach typ „Pythagoras Hypotenuse“ |
| 2020-OS-B1c | Seitenverhältnis benennen |  |  | Hauptplatz nach typ „Winkelfunktion Seitenverhältnis angeben“ |
| 2020-OS-B1j | Seitenverhältnis benennen |  |  | Hauptplatz nach typ „Trigonometrische Gleichung nach Seite umstellen“ |
| 2020-OS-K5b | Winkel berechnen |  |  | Hauptplatz nach typ „Winkel im rechtwinkligen Dreieck berechnen“ |
| 2020-OS-K7a | Hypotenuse gesucht |  |  | Hauptplatz nach typ „Pythagoras Hypotenuse“ |
| 2020-OS-K7c | Seite berechnen (Sinussatz) |  | Winkelsumme | Hauptplatz nach typ „Sinussatz Seite berechnen“. Zwischenschritt aus typ_neben |
| 2021-GYM-K5b |  |  | Dreieck erst in Figur oder Körper finden | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2021-OS-B1h | Gleichung aufstellen |  |  | Hauptplatz nach typ „Pythagoras Gleichung zuordnen“ |
| 2021-OS-B1i | Winkelsumme |  |  | Hauptplatz nach typ „Winkel im Viereck berechnen“ |
| 2021-OS-B1j | Symmetrieachsen zählen |  |  | Hauptplatz nach typ „Symmetrieachsen bestimmen“ |
| 2021-OS-K3a | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2021-OS-K3b | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2021-OS-K3c | Seite berechnen (Sinussatz) |  | Winkelsumme | Hauptplatz nach typ „Sinussatz Seite berechnen“. Zwischenschritt aus typ_neben |
| 2022-GYM-K4b | Dreieck erst in Figur oder Körper finden |  |  | Hauptplatz nach typ „Kegelhöhe aus Mantellinie und Radius berechnen“ |
| 2022-GYM-K5a | Hypotenuse gesucht |  |  | Hauptplatz nach typ „Pythagoras Hypotenuse“ |
| 2022-OS-B1g | Gleichung aufstellen |  |  | Hauptplatz nach typ „Satz des Pythagoras formulieren“ |
| 2022-OS-B1i | Symmetrieachsen zählen |  |  | Hauptplatz nach typ „Symmetrieachsen bestimmen“ |
| 2022-OS-K2c | Dreieck erst in Figur oder Körper finden |  |  | Hauptplatz nach Zuschnitt „Dreieck versteckt“ (Befund Geometrie 10.10.): der Stab steckt im Zylinder, Pythagoras Hypotenuse |
| 2022-OS-K5a | Kathete gesucht | erst entscheiden, dann rechnen |  | Hauptplatz nach typ „Pythagoras Kathete“ |
| 2022-OS-K5b | Winkel berechnen | erst entscheiden, dann rechnen |  | Hauptplatz nach typ „Winkel im rechtwinkligen Dreieck berechnen“ |
| 2022-OS-K5c | Winkelsumme |  |  | Hauptplatz nach typ „Winkelsumme im Dreieck anwenden“ |
| 2022-OS-K5d | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2023-GYM-B2b | Dreieck erst in Figur oder Körper finden |  |  | Hauptplatz nach typ „Streckenlänge aus Koordinaten berechnen“. AE als Hypotenuse eines Teildreiecks |
| 2023-GYM-K6a | Hypotenuse gesucht |  |  | Hauptplatz nach typ „Pythagoras Hypotenuse“ |
| 2023-GYM-K6d | Seite berechnen |  | Winkelsumme | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“. Basiswinkel (180° − 43,6°) : 2 |
| 2023-OS-B1g | gleichschenkliges Dreieck |  | Winkelsumme | Hauptplatz nach typ „Gleichschenkliges Dreieck erkennen“. Zwischenschritt aus typ_neben |
| 2023-OS-K2a | Winkelsumme |  |  | Hauptplatz nach typ „Winkel im Viereck berechnen“ |
| 2023-OS-K7a | gleichschenkliges Dreieck |  | Winkelsumme | Hauptplatz nach typ „Gleichschenkliges Dreieck erkennen“. dritter Winkel im Dreieck ABF |
| 2023-OS-K7b | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2024-GYM-K6a |  |  | Winkel berechnen; Winkelsumme | Hauptplatz außerhalb der P10-Stufen. Winkel ADC über Winkelsumme |
| 2024-OS-B1f | Gleichung aufstellen |  |  | Hauptplatz nach typ „Pythagoras Gleichung zuordnen“ |
| 2024-OS-K6a | Kathete gesucht | erst entscheiden, dann rechnen |  | Hauptplatz nach typ „Pythagoras Kathete“ |
| 2024-OS-K6b | Winkel berechnen | erst entscheiden, dann rechnen |  | Hauptplatz nach typ „Winkel im rechtwinkligen Dreieck berechnen“ |
| 2024-OS-K6d | Seite berechnen (Sinussatz) |  | Winkelsumme | Hauptplatz nach typ „Sinussatz Seite berechnen“. γ = 180° − 38° − 108° |
| 2025-GYM-K4a | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |
| 2025-GYM-K4b |  |  | Seite berechnen (Sinussatz) | Hauptplatz außerhalb der P10-Stufen. Sinussatz (nach einem Winkel umgestellt) |
| 2025-OS-B1g | Seitenverhältnis benennen |  |  | Hauptplatz nach typ „Winkelfunktion Seitenverhältnis angeben“ |
| 2025-OS-K2a | Symmetrieachsen zählen | Dreieck erst in Figur oder Körper finden |  | Hauptplatz nach typ „Symmetrieachsen bestimmen“. Symmetrieachse nach typ Hauptplatz, Pythagoras gehört zu D3 |
| 2025-OS-K2c | rechten Winkel begründen |  | gleichschenkliges Dreieck | Hauptplatz nach typ „Rechten Winkel begründen“. Dreieck AFD gleichschenklig-rechtwinklig, Basiswinkel 45° |
| 2025-OS-K4a | Hypotenuse gesucht | erst entscheiden, dann rechnen | Winkel berechnen | Hauptplatz nach Zuschnitt „Hypotenuse gesucht“ (Befund Geometrie 10.10.): die Rampe ist ein nacktes Dreieck; Winkel im selben Teil mit tan |
| 2025-OS-K4c | Seite berechnen (Sinussatz) |  | Winkelsumme | Hauptplatz nach typ „Sinussatz Seite berechnen“. dritter Winkel 180° − 5° − 141° |
| 2026-EBR-B1c | Eigenschaft erkennen |  |  | EBR-Zwilling von 2026-FOR-B1c |
| 2026-EBR-B1i | Winkelsumme |  |  | EBR-Zwilling von 2026-FOR-B1i |
| 2026-EBR-B1j | Gleichung aufstellen |  |  | EBR-Zwilling von 2026-FOR-B1j |
| 2026-EBR-K3a | Kathete gesucht | erst entscheiden, dann rechnen |  | EBR-Zwilling von 2026-FOR-K4a |
| 2026-EBR-K3b | Winkel berechnen | erst entscheiden, dann rechnen |  | EBR-Zwilling von 2026-FOR-K4b |
| 2026-FOR-B1c | Eigenschaft erkennen |  |  | Hauptplatz nach typ „Eigenschaft einer Figur zuordnen“ |
| 2026-FOR-B1i | Winkelsumme |  |  | Hauptplatz nach typ „Winkel im Viereck berechnen“ |
| 2026-FOR-B1j | Gleichung aufstellen |  |  | Hauptplatz nach typ „Pythagoras Gleichung zuordnen“ |
| 2026-FOR-K2c | Dreieck erst in Figur oder Körper finden |  |  | Hauptplatz nach Zuordnung |
| 2026-FOR-K4a | Kathete gesucht | erst entscheiden, dann rechnen |  | Hauptplatz nach typ „Pythagoras Kathete“ |
| 2026-FOR-K4b | Winkel berechnen | erst entscheiden, dann rechnen |  | Hauptplatz nach typ „Winkel im rechtwinkligen Dreieck berechnen“ |
| 2026-FOR-K4c | Seite berechnen |  |  | Hauptplatz nach typ „Seite im rechtwinkligen Dreieck berechnen“ |

## Fokus pythagoras-seite

Titel: Steckbrief Pythagoras: Seite berechnen (P10-Stufen „Gleichung aufstellen“, „Hypotenuse gesucht“, „Kathete gesucht“, „Dreieck erst in Figur oder Körper finden“)

Kapitel: dreiecke
Stufen: Gleichung aufstellen | Hypotenuse gesucht | Kathete gesucht | Dreieck erst in Figur oder Körper finden
Bank: pythagoras


Stand 06.10.2026, Entwurf zur Bestätigung durch den Lehrer (je Zeile).
Teil 1 aus `katalog/pythagoras.md` (Grundvorstellung, Erkennungsschritte,
Merkkasten, Typische Fehler, Sprossen; Quellen Serlo, LS-AA, RLP, P10),
Teil 2 und 3 aus 91 echten und herausgelösten Aufgaben (BB/BE, andere
Länder, VERA). Übertragen vom Steckbrief Grundwert: Begriffsfrage vorn,
Schätzfrage als Kontrolle, Kopfzahlen unten, Darstellung nur wo sie trägt.

### 1 Verständnis

- **Begriff:** Die Hypotenuse liegt dem rechten Winkel gegenüber und ist die
  längste Seite; die beiden anderen sind Katheten. Der Satz spricht über
  Flächen (Quadrate über den Seiten), nicht über Längen.
- **Erste Frage:** „Wo ist der rechte Winkel? Welche Seite liegt ihm
  gegenüber?“ – Rechtwinkelmarke einkreisen, Hypotenuse mit H beschriften,
  in Dreiecken verschiedener Lage; nicht rechnen. Dazu „Gilt der Satz
  hier?“ (Dreiecke mit und ohne rechten Winkel).
- **Schätzfrage:** „Ist die gesuchte Seite länger oder kürzer als die
  längste gegebene?“ – Hypotenuse gesucht: länger; Kathete gesucht: kürzer
  als die Hypotenuse. Dient später als Kontrolle des eigenen Ergebnisses.
- **Typische Fehler:** → katalog/pythagoras.md, Typische Fehler: Quadrate addiert | Falsche Seite als Hypotenuse | Wurzel vergessen | Satz als Längenformel | Wurzel aus jedem Summanden | Ganze statt halbe Seite | Radius und Durchmesser | Schräge als Höhe | Buchstabenfixierung
- **Darstellung:** Skizze mit Rechtwinkelmarke; in Figuren und Körpern das
  rechtwinklige Teildreieck farbig nachfahren und neu beschriften. Quadrate
  über den Seiten (Kästchen zählen) nur als Grundvorstellung am Anfang.
- **Formel:** Gleichung in Rollen aufstellen (H² = K² + K²), dann mit den
  Buchstaben der Aufgabe (der Buchstabe der Hypotenuse steht allein); bei
  gesuchter Kathete ergibt das Umstellen das Minus. Eher nicht die Merkregel „plus/
  minus“ als Ersatz (Lehrer 07.10., Beschluss A6). Rechnung in drei Zeilen:
  Gleichung, Zwischenergebnis, Wurzel.
- **Vorher können (Rückblick):** Quadratzahlen bis 20² im Kopf; Wurzel mit
  dem Taschenrechner (erst Summe/Differenz, dann Wurzel, dann runden);
  Rechtwinkelmarke erkennen; cm und m angleichen.
- **Leiter:** → katalog/pythagoras.md, Lerneinheiten und Merkkasten Einheiten 1–3 (Sprossen in der Bank)
- **Verständnis-Bank:** pythagoras-e1-k2-s0 → pythagoras-e1-k1-s0 (Vorschlag
  Lauf 06.10. abends, zur Bestätigung)
- **Leiter-Bank:** pythagoras-e1-k2-s1 → pythagoras-e1-k2-s2 →
  pythagoras-e1-k2-s3 → pythagoras-e1-k2-s5 → pythagoras-e2-k3-s0 →
  pythagoras-e2-k3-s1 → pythagoras-e3-k2-s0 (unterer Teil der Leiter bis
  vor die echten Aufgaben; Vorschlag Lauf 06.10. abends, zur Bestätigung)

### 2 Raster (91 echte und herausgelöste Aufgaben)

- **Sachen:** Leiter an der Wand · Rampe, Treppe, Skate-Hindernis ·
  Diagonale (Tisch, Kinoleinwand, Zaunelement, Platte im Transporter) ·
  Drachenschnur, Turm, Entfernung im Gelände · Kanalufer, Flugzeug-Gleitweg
  · ebene Figuren (gleichschenkliges Dreieck, Trapez, Quadrat im Kreis,
  Drachenviereck) · Körper (Pyramide, Kegel, Quader-Raumdiagonale,
  Trinkhalm im Becher) · Koordinaten.
- **Darstellung:** Bild/Skizze 63, nur Text 26, Graph 2. Ohne Skizze heißt:
  selbst skizzieren (NRW „Skizziere“) – das fehlt bisher als eigene Sprosse.
- **Fragerichtung:** Seite berechnen 70 · Aussage prüfen / Nachweis 16
  („Zeige, dass …“, „Ragt er mehr als 13 cm heraus?“) · rückwärts 3.
- **Zahlen:** krumm 74, im Kopf 11, glatt 5. **Lücke:** unten fehlen
  aufgehende Tripel in Sachaufgaben – hier sind eigene Aufgaben sinnvoll.

### 3 Formulierungen

kurz:
- Berechne die Länge der Diagonale. (NRW, NI)
- Wie lang ist die Seite c? (HH)
- Ermittle den Abstand zwischen Ben und Chris. (P10)
- Berechne die Höhe h. (P10)
- Bestimme die Entfernung der Punkte A und B. (HH)

lang:
- Im abgebildeten Dreieck sind x und y die Katheten, z ist die
  Hypotenuse. Kreuze die Gleichung an, mit der … berechnet werden kann. (P10,
  jedes Jahr mit anderen Buchstaben)
- Weise nach, dass die Strecke AD etwa 12,0 m lang ist. (P10)
- Zeige, dass seine Mantellinie s 5 cm lang ist. (SH, HH)
- Eine 6,50 m lange Leiter lehnt an einer Hauswand … Berechne, wie hoch
  sie reicht. (SH)
- Ragt der Trinkhalm mehr als 13 cm über den Becher hinaus? (NI)

### 4 Befunde

- Wie beim Grundwert steht Teil 1 seit September im Katalog; das
  Bauprogramm liest ihn nicht.
- Die Stufe „Dreieck erst in Figur oder Körper finden“ enthält viele
  Körperaufgaben anderer Länder, die schwerer sind als BB/BE (Pyramide mit
  Raute, Streckenzug im Prisma) – der Filter „nicht schwerer“ muss sie
  aussortieren.

### 5 Arten

Stand 07.10.2026 (Beschlüsse 06./07.10., aufgabenbank
bau/pruefheft/beschluesse-2026-10-07.md A1–A4, F3, F7, F8, G1). Arten nach
der gesuchten Größe (A3): Hypotenuse und Kathete getrennt wie in den
Lehrwerken („Berechnung der Hypotenuse … 39 · Berechnung einer Kathete …
40“), den P10-Typen und Katalog Einheit 1/2. Grenze direkt/versteckt nach
F8: Dreieck mit Marke und nötigen Längen eingezeichnet = direkt (auch als
Teil einer Figur); selbst finden, Linie denken oder Länge erst ableiten =
versteckt. Gezählt sind BB/BE-Aufgaben ohne GYM, EBR-Zwillinge einmal. Gruppen
leicht → schwer, in der Gruppe die Aufgaben leicht → schwer (Katalog:
Niveau I vor II); versteckte Dreiecke nach der Vorarbeit (nur hinsehen /
Länge halbieren oder verdoppeln / Längen aus Koordinaten), Lauf 07.10.

- **Kurzname:** Satz des Pythagoras
- **Vorher:** Quadrat und Wurzel
- **Weiter:** Seiten und Winkel mit sin, cos, tan · Körper: Mantellinie und Höhe
- **Nicht geprüft:** Umkehrung, Höhensatz und Kathetensatz [Fundamente
  2024 „8.3 Umkehrung des Satzes des Pythagoras 229“,
  quellen/quelle-cornelsen-fundamente-bb-ausgabeb2024-inhalt.txt;
  Schnittpunkt 2017 „4 Höhensatz 92 · 5 Kathetensatz 94“,
  quellen/quelle-klett-schnittpunkt-mathematik-diff2017-inhalt.txt; die
  Umkehrung nur als ein möglicher Weg in 2025-OS-K2c (Typ „Rechten Winkel
  begründen“)]
- **Formel:** a² + b² = c² (vorläufig: Schreibweise aus dem Katalog,
  Merkkasten Einheit 1 „Formelsammlung: Geometrie – rechtwinkliges Dreieck,
  Satz des Pythagoras“; Formelsammlung noch nicht gesichtet)
- **Rückblick:** keiner (A1: Quadrieren, Wurzel und Einheiten übt die
  Leiter selbst; „Quadratzahlen bis 20²“ ist keine belegte Stolperstelle)
- **Abruf-Frage:** „Notiere den Satz des Pythagoras.“
- **Abruf-Lösung:** c² = a² + b² (c: Hypotenuse)
- **Formel-Frage:** „Suche zuerst die Hypotenuse – sie steht in der Gleichung allein auf einer Seite. Schreibe die Gleichung mit den Buchstaben des Dreiecks.“
- **Formel-Fälle:** (Erkennen und Aufstellen in einer Aufgabe, Bauregeln 3.3/3.4; verschiedene Lagen, wechselnde Buchstaben; kein Einkreisen, Lehrer 07.10.)
  - (0|0) (4|0) (4|3); Seiten a b c; rechter Winkel 2
  - (0|0) (5|0) (1,8|2,4); Seiten y z x; rechter Winkel 3
  - (0|0) (0|3) (2,4|3); Seiten p q s; rechter Winkel 2
  - (0|2,5) (3,6|0) (5,6|2,88); Seiten u v w; rechter Winkel 2

#### Gleichung aufstellen
- **Kurzname:** Welche Gleichung passt?
- **Stufe:** Gleichung aufstellen
- **Zuschnitt:** Gleichung aufstellen
- **Beleg:** „Bezeichnungen im rechtwinkligen Dreieck 37 · Der Satz des
  Pythagoras 38“ (Mathematik 2023 Förder,
  quellen/quelle-westermann-mathematik2023-foerder-bebbstth-inhalt.txt)
- **P10-Typ:** Pythagoras Gleichung zuordnen; Satz des Pythagoras formulieren
- **Typischer Fehler:** Wurzel vergessen: z = y² + x² angekreuzt; „c ist
  immer die Hypotenuse“ [Katalog pythagoras.md, Typische Fehler; P10
  2021-OS-B1h, 2024-OS-B1f]
- **Geprüft:** 2× (EBR und FOR)
- **Aufgaben:** 2017-OS-B1d 2022-OS-B1g
- **Gruppen:** Gleichung ankreuzen: 2017-OS-B1d | Satz in Worten: 2022-OS-B1g
- **Umgezogen:** 2021-OS-B1h, 2026-FOR-B1j → Hypotenuse gesucht; 2024-OS-B1f →
  Kathete gesucht (Formel mit Wurzel ankreuzen gehört zur Art ihres
  Rechenwegs, Bauregeln 3.5, Lehrer 07.10.)

#### Hypotenuse gesucht
- **Kurzname:** Die lange Seite gesucht
- **Stufe:** Hypotenuse gesucht
- **Zuschnitt:** Hypotenuse gesucht
- **Beleg:** „Berechnung der Hypotenuse in einem rechtwinkligen Dreieck 39“
  (Mathematik 2023 Förder,
  quellen/quelle-westermann-mathematik2023-foerder-bebbstth-inhalt.txt);
  „Berechnen der Hypotenuse 29“ (Sekundo Förder 2017,
  quellen/quelle-westermann-sekundo-foerder-be_bb2017-inhalt.txt)
- **P10-Typ:** Pythagoras Hypotenuse
- **Typischer Fehler:** falsche Seite als Hypotenuse: die längere Kathete
  für die Hypotenuse gehalten, die Stufenhöhe der Rampe als Hypotenuse
  [Katalog pythagoras.md, Typische Fehler; P10 2020-OS-K7a, 2025-OS-K4a];
  Wurzel vergessen: z = y² + x² angekreuzt [P10 2021-OS-B1h]
- **Geprüft:** 4× (EBR und FOR)
- **Einstieg:** 2021-OS-B1h 2026-FOR-B1j
- **Erkennen-Platz:** vor der Überschrift   (Brücke zwischen Formel und den Arten, Lehrer 07.10.)
- **Erkennen-Frage:** „Hypotenuse oder Kathete gesucht? Schreibe die Gleichung auf.“
- **Erkennen-Vorgabe:** a   (der erste Fall steht vorgedruckt, grau, ohne „Beispiel“; Lehrer 07.10.)
- **Erkennen-Fälle:** (Bauregeln 3.3: beide Arten gemischt; kurze Lagen statt Fragen, damit nichts zum Rechnen einlädt)
  - Leiter 5 m lang, Fuß 1,4 m von der Wand – Höhe an der Wand? → Kathete; 5² = h² + 1,4²
  - Rampe 3 m lang, 0,4 m hoch – schräge Fläche? → Hypotenuse; s² = 3² + 0,4²
  - Bildschirm 48 cm breit, 27 cm hoch – Diagonale? → Hypotenuse; d² = 48² + 27²
  - Drachenschnur 25 m lang, Lena 7 m neben dem Punkt unter dem Drachen – Höhe? → Kathete; 25² = h² + 7²
- **Aufgaben:** 2020-OS-K7a 2025-OS-K4a
- **Nur gekürzt:** 2025-OS-K4a (die Teilaufgabe fragt auch den Winkel α)
- **Gruppen:** Hypotenuse aus zwei Katheten: 2020-OS-K7a 2025-OS-K4a
- **Fremd-Merkmal:** \+
- **Leiter-Bank:** pythagoras-e1-k2-s1   (s3 nur mit Rundung: gleiche Sorte, Lehrer 07.10.)
- **Schritte:**
  - Welche Seite liegt dem rechten Winkel gegenüber – ist sie gegeben oder
    gesucht? → naheliegend falsch: die längste gegebene Zahl [falsche Seite
    als Hypotenuse; P10 2020-OS-K7a]
  - Wird die gesuchte Seite länger oder kürzer als die längste gegebene? →
    naheliegend falsch: kürzer oder „dazwischen“ [Stufenhöhe als Hypotenuse;
    P10 2025-OS-K4a]
  - Gleichung so hinschreiben, dass die gesuchte Seite allein steht; dann:
    Ist c² schon die Länge? → naheliegend falsch: ja [Wurzel vergessen; P10
    2021-OS-B1h]

#### Kathete gesucht
- **Kurzname:** Eine kurze Seite gesucht
- **Stufe:** Kathete gesucht
- **Zuschnitt:** Kathete gesucht
- **Beleg:** „Berechnung einer Kathete in einem rechtwinkligen Dreieck 40“
  (Mathematik 2023 Förder,
  quellen/quelle-westermann-mathematik2023-foerder-bebbstth-inhalt.txt);
  „Berechnen einer Kathete 30“ (Sekundo Förder 2017,
  quellen/quelle-westermann-sekundo-foerder-be_bb2017-inhalt.txt)
- **P10-Typ:** Pythagoras Kathete
- **Typischer Fehler:** Quadrate addiert, obwohl eine Kathete gesucht ist
  (Fehlerquelle aller Kathete-Originale) [Katalog pythagoras.md, Typische
  Fehler; P10 2019-OS-K3a, 2024-OS-K6a]; „c ist immer die Hypotenuse“ [P10
  2024-OS-B1f]
- **Geprüft:** 6× (EBR und FOR)
- **Einstieg:** –   (2024-OS-B1f gleiche Sorte wie der Einstieg der Hypotenuse, Bauregeln 2.1; kommt mit „mehr“)
- **Rechnen-Fall:** „Rechne die Höhe der Leiter aus {nr} a) aus.“ → h² = 5² − 1,4² = 23,04; h = 4,8 m   (ersetzt die Leiter-Bank, Lehrer 07.10.)
- **Aufgaben:** 2019-OS-K3a 2024-OS-K6a 2026-FOR-K4a 2022-OS-K5a 2016-OS-K7b
- **Gruppen:** Kathete aus Hypotenuse und Kathete: 2019-OS-K3a 2024-OS-K6a 2026-FOR-K4a 2022-OS-K5a 2016-OS-K7b
- **Fremd-Merkmal:** −|-
- **Leiter-Bank:** –   (s1 ersetzt durch den Rechnen-Fall, s2 nur mit Rundung: gleiche Sorte, Lehrer 07.10.; s0 „Plus oder minus?“ ersetzt durch Erkennen-Fälle, A6)
- **Schritte:**
  - Kann die gesuchte Seite länger sein als die Seite gegenüber dem rechten
    Winkel (die Leiter, der Weg, die Seilbahn)? → naheliegend falsch: ja oder
    „weiß nicht“ [Quadrate addiert; P10 2019-OS-K3a, 2024-OS-K6a]
  - Gleichung so hinschreiben, dass die längste Seite allein steht → naheliegend
    falsch: die gesuchte Seite allein (a² = b² + c²) [dieselbe Fehlerquelle]
  - Passt dein Ergebnis zu deiner ersten Antwort? → naheliegend falsch: nicht
    vergleichen, 5,8 m stehen lassen [Quadrate addiert; Kontrolle laut
    Begriff „Schätzfrage“]

#### Dreieck versteckt
- **Kurzname:** Das Dreieck erst finden
- **Stufe:** Dreieck erst in Figur oder Körper finden
- **Zuschnitt:** Dreieck versteckt
- **Beleg:** „3 Der Satz des Pythagoras in Figuren und Körpern 88“
  (Schnittpunkt 2017,
  quellen/quelle-klett-schnittpunkt-mathematik-diff2017-inhalt.txt);
  „3.2 Längen berechnen in Figuren und Körpern“ (Fundamente 2017,
  quellen/quelle-cornelsen-fundamente-bb-ausgabeb2017-inhalt.txt)
- **P10-Typ:** Mantellinie Kegel bestimmen; Streckenlänge aus Koordinaten
  berechnen; Pythagoras Hypotenuse/Kathete als Teil einer Figur
- **Typischer Fehler:** ganze statt halbe Seite, Durchmesser statt Radius,
  Schräge als Höhe [Katalog pythagoras.md, Typische Fehler; P10
  2015-OS-K6c, 2025-OS-K2a, 2022-OS-K2c, 2026-FOR-K2c]
- **Geprüft:** 6× (EBR und FOR)
- **Aufgaben:** 2026-FOR-K2c 2019-OS-K2d 2015-OS-K6c 2025-OS-K2a 2018-OS-K6d 2022-OS-K2c
- **Nur gekürzt:** 2025-OS-K2a (Symmetrieachsen) · 2015-OS-K6c (Flächeninhalt der Seitenfläche) · 2019-OS-K2d (Winkel β)
- **Gruppen:** Nur hinsehen: 2026-FOR-K2c | Längen aus Koordinaten: 2019-OS-K2d | Länge halbieren oder verdoppeln: 2015-OS-K6c 2025-OS-K2a 2018-OS-K6d 2022-OS-K2c
- **Leiter-Bank:** pythagoras-e3-k2-s0 → pythagoras-e3-k2-s1
- **Schritte:**
  - Wo steckt ein rechter Winkel? Fahre das Dreieck nach. → naheliegend
    falsch: ein Dreieck ohne rechten Winkel, die Schräge als Höhe [P10
    2022-OS-K2c, 2026-FOR-K2c]
  - Reicht die Seite deines Dreiecks über die ganze Kante (den ganzen
    Durchmesser)? → naheliegend falsch: ja [ganze statt halbe Seite,
    Durchmesser statt Radius; P10 2015-OS-K6c, 2025-OS-K2a]
  - danach die Schritte der Art „Hypotenuse gesucht“ oder „Kathete gesucht“
  - (Längen aus Koordinaten: kein Schritt, kein belegter Fehler)
