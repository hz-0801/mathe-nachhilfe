# Rohdatei trigonometrie

Stufe: I

- msa: Trigonometrie im rechtwinkligen Dreieck (19 Zeilen)
- msa: Sinussatz (9 Zeilen)

Stand: 2026-09-19, Commit 16e5c1f

## A Typenprofil

**Sinussatz Seite berechnen** · 9 Zeilen · msa 9 · Jahre 2014–2025
msa/msa-typen.csv (gültig): Im allgemeinen Dreieck eine Seite mit dem Sinussatz aus einer Seite und zwei Winkeln berechnen.

**Seite im rechtwinkligen Dreieck berechnen** · 8 Zeilen · msa 8 · Jahre 2016–2026
msa/msa-typen.csv (gültig): Seite aus einer Seite und einem Winkel über sin, cos oder tan berechnen.

**Winkel im rechtwinkligen Dreieck berechnen** · 5 Zeilen · msa 5 · Jahre 2019–2026
msa/msa-typen.csv (gültig): Winkel aus zwei Seiten über tan, sin oder cos und die Umkehrfunktion berechnen.

**Winkelfunktion Seitenverhältnis angeben** · 5 Zeilen · msa 5 · Jahre 2017–2025
msa/msa-typen.csv (gültig): Im rechtwinkligen Dreieck sin, cos oder tan eines Winkels als Verhältnis der beschrifteten Seiten angeben.

**Trigonometrische Gleichung nach Seite umstellen** · 1 Zeile · msa 1 · Jahre 2020
msa/msa-typen.csv (gültig): Eine Gleichung der Form sin α = a/x ohne Figur nach x umstellen und den Wert berechnen.

**Nebentypen:** Strecke aus Teilstrecken berechnen (4) · Winkelsumme im Dreieck anwenden (4) · Behauptung prüfen (3) · Seite im rechtwinkligen Dreieck berechnen (2) · Flächeninhalt Rechteck berechnen (1) · Winkel aus Teilwinkeln berechnen (1)

## B Zeilenliste

## msa

2016-OS-K7c | 4 | ja | Rechnung · Ermitteln Sie | AD ≈ 744 m; Winkel CAB = 70°; Winkel CAD = 180° − 90° − 54° = 36°; rechter Winkel bei D → BD | Winkel DAB = 70° − 36° = 34°; BD = AD · tan 34°
2017-OS-K4b | 2 | ja | Rechnung · Berechnen Sie | Wand 1,20 m senkrecht auf AB, Winkel bei B 34,9° → Abstand PB | tan 34,9° = 1,20 : PB; PB = 1,20 : tan 34,9°
2018-OS-K4d | 4 | ja | Rechnung¦Kurzantwort · Ermitteln Sie¦Geben Sie an | AC = 112,8 m (im Text), Winkel 30° bei A, rechter Winkel bei B; A liegt 1,5 m über dem Boden; Plattform 12,0 m → Höhe des Berges¦Höhe von D über dem Boden | CB = 112,8 · sin 30° = 56,4 m; plus 1,5 m; D: plus 12,0 m
2021-OS-K3a | 2 | ja | Rechnung · Zeigen Sie | Viereck ABCD: rechter Winkel bei A; Diagonale BD = 1500 m; Winkel ADB = 55°, Winkel BDC = 60°; Winkel ABC = 109°; DC = 2004 m; zu zeigen: AB ≈ 1229 m → Länge AB | im rechtwinkligen Dreieck ABD: sin 55° = AB/1500, AB = 1500 · sin 55°
2021-OS-K3b | 2 | ja | Rechnung · Berechnen Sie | Viereck ABCD: rechter Winkel bei A; Diagonale BD = 1500 m; Winkel ADB = 55°, Winkel BDC = 60°; Winkel ABC = 109°; DC = 2004 m; aus a): AB ≈ 1229 m → Länge AD | cos 55° = AD/1500, AD = 1500 · cos 55°; alternativ Pythagoras AD = √(1500² − 1229²)
2022-OS-K5d | 2 | ja | Rechnung · Berechnen Sie | Dreieck ABC, nicht rechtwinklig; Höhe hc ≈ 7,4 m mit Fußpunkt D auf AB; b = 14,1 m; β = 52° → Seite a | sin 52° = 7,4 : a, also a = 7,4 : sin 52°
2023-OS-K7b | 4 | ja | Rechnung¦Rechnung · Weisen Sie nach¦Berechnen Sie | Dreieck ABC mit F auf AC und BF ⊥ AC; AB = 131,5 cm; Winkel bei B: CBF = 65°, FBA = 45°; Winkel bei A 45°; Behauptung: BF und AF sind je ca. 93,0 cm lang → Nachweis BF ≈ AF ≈ 93,0 cm¦Länge BC | in ABF: BF = 131,5 · sin 45°, AF = 131,5 · cos 45°; in CBF: BC = BF : cos 65° (oder Winkel bei C = 25°, BC = BF : sin 25°)
2026-FOR-K4c | 3 | ja | Rechnung · Bestimmen Sie | Parallelogramm ABCD; BC = 32 cm; F auf der Verlängerung von AB mit BF = 13 cm; CF = h steht senkrecht auf AF; ε = Winkel CBF; Winkel CAB = 22°; h ≈ 29,24 cm aus a) → Länge der Diagonale AC | im rechtwinkligen Dreieck AFC: sin 22° = h : AC, AC = 29,24 : sin 22°; alternativ Sinussatz im Dreieck ABC
2014-OS-K2b | 4 | ja | Rechnung · Berechnen Sie | Dreieck Forsthaus (F) – Jugendherberge (J) – Restaurant (R): FJ = 2800 m, Winkel bei F 60°, bei R 50°; Badestelle–Restaurant 2500 m auf FR → Gesamtlänge Jugendherberge–Restaurant–Badestelle | Winkel bei J = 70°; Sinussatz JR = 2800 · sin 60° : sin 50° ≈ 3165 m (alternativ Höhe von J auf FR: 2800 · sin 60° ≈ 2425 m, JR = 2425 : sin 50°); plus 2500 m
2015-OS-K5c | 2 | ja | Rechnung · Berechnen Sie | Dreieck ABD: AD = 4,1 cm, ∠A = 123°, ∠B = 36°, δ = 21°; E Fußpunkt von A auf BD mit rechtem Winkel → Länge der Diagonalen BD | Sinussatz: BD = 4,1 · sin 123° : sin 36°; alternativ DE = 4,1 · cos 21°, AE = 4,1 · sin 21°, EB = AE : tan 36°, BD = DE + EB
2017-OS-K4c | 4 | ja | Rechnung¦Rechnung · Berechnen Sie¦Berechnen Sie | AC = 4,50 m, α = 62,8°, β = 34,9°; Dachlänge 8,00 m; Dachflächen über AC und BC → Länge BC¦Dachfläche in m² | BC : sin α = AC : sin β, BC = 4,5 · sin 62,8° : sin 34,9°; Fläche = (4,5 + 7,0) · 8
2018-OS-K4c | 2 | ja | Rechnung · Bestätigen Sie | Dreieck ACD mit CD = 12,0 m, γ = 5°, δ = 55°; Behauptung AC = 112,8 m → Nachweis für AC | AC : sin δ = CD : sin γ; AC = 12 · sin 55° : sin 5°
2019-OS-K3c | 4 | ja | Rechnung · Berechnen Sie | Viereck ABCD mit rechtem Winkel bei B; AC = 9 m; Winkel BAC = 64°; Winkel BCD = 86° (zwischen CB und CD); Winkel ADC = 80° → Abstand AD | Winkel ACB = 90° − 64° = 26°; Winkel ACD = 86° − 26° = 60°; Sinussatz im Dreieck ACD: AD/sin 60° = 9/sin 80°
2020-OS-K7c | 3 | ja | Rechnung · Berechnen Sie | Dreieck DEF mit DF = 4 m, FE = 11 m, Winkel F = 115°, Winkel E = 16°; P auf DE mit PE = 10 m → Länge DP | Winkel D = 180° − 115° − 16° = 49°; DE/sin 115° = 11/sin 49° → DE ≈ 13,2 m; DP = DE − 10
2021-OS-K3c | 3 | ja | Rechnung¦Begründung · Prüfen Sie¦Entscheiden Sie | Viereck ABCD: rechter Winkel bei A; Diagonale BD = 1500 m; Winkel ADB = 55°, Winkel BDC = 60°; Winkel ABC = 109°; DC = 2004 m; Aussage: BC ist genauso lang wie DC → Länge BC¦Entscheidung über die Aussage | Winkel ABD = 180° − 90° − 55° = 35°, Winkel DBC = 109° − 35° = 74°, Winkel BCD = 180° − 60° − 74° = 46°; Sinussatz BC/sin 60° = DC/sin 74°
2024-OS-K6d | 4 | ja | Rechnung · Berechnen Sie | Dreieck ABC mit AB = 384 m, α = 38° bei A, β2 = 108° bei B → Strecke BC | γ = 180° − 38° − 108° = 34°; BC : sin α = AB : sin γ, BC = 384 · sin 38° : sin 34°
2025-OS-K4c | 3 | ja | Rechnung · Berechnen Sie | Dreieck aus Rampe y, waagerechter Strecke 160 cm und der Verbindung Treppenfuß–obere Stufenkante; Winkel 5° am Rampenfuß (gegenüber dieser Verbindung), Winkel 141° am Treppenfuß (gegenüber y) → y | dritter Winkel 180° − 5° − 141° = 34° gegenüber 160 cm; Sinussatz y : sin 141° = 160 : sin 34°
2020-OS-B1j | 1 | ja | Kurzantwort · Geben Sie an | Gleichung sin 30° = 7/x → x | x = 7 : sin 30° = 7 : 0,5
2019-OS-K3b | 2 | ja | Rechnung · Zeigen Sie rechnerisch | rechtwinkliges Dreieck ABC mit rechtem Winkel bei B, AB = 4 m, AC = 9 m (oder BC ≈ 8,06 m aus a); α bei A → Nachweis α ≈ 64° | cos α = 4/9 → α = cos⁻¹(4/9)
2020-OS-K5b | 3 | ja | Rechnung · Berechnen Sie | rechtwinkliges Trapez mit Grundseite 14 cm, Höhen 6 cm und 15 cm; α an der oberen Ecke der 15-cm-Seite → α | Hilfsdreieck mit Katheten 14 (waagerecht) und 15 − 6 = 9 (senkrecht); tan α = 14/9
2022-OS-K5b | 2 | ja | Rechnung · Berechnen Sie | Dreieck ABC, nicht rechtwinklig; Höhe hc ≈ 7,4 m mit Fußpunkt D auf AB; b = 14,1 m; β = 52° → Winkel α | sin α = 7,4 : 14,1 (oder cos α = 12 : 14,1)
2024-OS-K6b | 2 | ja | Rechnung · Bestimmen Sie | rechtwinkliges Dreieck AFB mit rechtem Winkel in F, FB = 255 m, AB = 384 m; β1 bei B zwischen FB und BA → β1 | cos β1 = 255 : 384; alternativ sin β1 = FA : 384 mit FA aus a)
2026-FOR-K4b | 2 | ja | Rechnung · Weisen Sie nach | Parallelogramm ABCD; BC = 32 cm; F auf der Verlängerung von AB mit BF = 13 cm; CF = h steht senkrecht auf AF; ε = Winkel CBF → Nachweis ε ≈ 66° | cos ε = 13 : 32 = 0,406; ε = cos⁻¹(0,406); alternativ tan ε = h : 13 mit h aus a)
2017-OS-B1j | 1 | ja | Kurzantwort · Geben Sie an | Katheten r (gegenüber β) und s, Hypotenuse t → Gleichung für sin β | Gegenkathete durch Hypotenuse
2018-OS-B1g | 1 | ja | Ankreuzen · Kreuzen Sie an | rechtwinkliges Dreieck mit Kathete b (gegenüber β), Hypotenuse a; Auswahl sin β = a/b, cos β = a/b, sin β = b/a → die zu β passende Gleichung | Gegenkathete b durch Hypotenuse a
2019-OS-B1h | 1 | ja | Kurzantwort · Geben Sie an | rechtwinkliges Dreieck mit rechtem Winkel gegenüber der Seite t; α liegt zwischen s und t; r liegt α gegenüber → Gleichung für sin α | Gegenkathete r durch Hypotenuse t
2020-OS-B1c | 1 | ja | Kurzantwort · Geben Sie an | rechtwinkliges Dreieck mit Katheten s (an α) und r (gegenüber α), Hypotenuse t → Gleichung für tan α | tan = Gegenkathete durch Ankathete
2025-OS-B1g | 1 | ja | Eintragen · Ergänzen Sie | rechtwinkliges Dreieck mit Katheten u (waagerecht) und v (senkrecht), Hypotenuse w, Winkel γ gegenüber u → Bruch für sin γ | Gegenkathete von γ ist u, Hypotenuse ist w
