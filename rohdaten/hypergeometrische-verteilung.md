# Rohdatei hypergeometrische-verteilung

Stufe: II

- abi: Hypergeometrische Verteilung (5 Zeilen)
- iqb: Hypergeometrische Verteilung (2 Zeilen)

Stand: 2026-09-25, Commit 25322c5

## A Typenprofil

**Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen** · 3 Zeilen · abi 1 iqb 2 · Jahre 2023–2024
abitur/abitur-typen.csv (neu): Die Wahrscheinlichkeit für genau k Treffer beim Ziehen ohne Zurücklegen als Quotient von Binomialkoeffizienten berechnen.

**Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das Gegenereignis berechnen** · 3 Zeilen · abi 3 · Jahre 2017–2022
abitur/abitur-typen.csv (neu): Eine Auswahl ohne Zurücklegen als hypergeometrische Situation erkennen und die Wahrscheinlichkeit für höchstens oder mindestens eine Trefferzahl über das Gegenereignis bestimmen.

**Größte Trefferzahl, bis zu der die kumulierte hypergeometrische Wahrscheinlichkeit unter einer Schranke bleibt, ermitteln** · 1 Zeile · abi 1 · Jahre 2023
abitur/abitur-typen.csv (neu): Hypergeometrische Einzelwahrscheinlichkeiten aufsummieren und die größte Trefferzahl bestimmen, für die die kumulierte Wahrscheinlichkeit eine Schranke unterschreitet.

**Nebentypen:** Ungeeignetheit des Binomialmodells begründen (1)

## B Zeilenliste

## abi

2023-bebb-lk-B4l | 4 | ja | Rechnung · Ermitteln Sie | 30 Personen, 12 weiblich, 5 ausgewählt; P(höchstens n weiblich) < 35 % → größtmögliches n | Kumulierte hypergeometrische Wahrscheinlichkeiten aufsummieren, bis 0,35 überschritten wird
2023-bebb-lk-B4k | 2 | ja | Rechnung · Ermitteln Sie | 30 Personen buchen, 12 davon weiblich; 5 werden zufällig ausgewählt → P(alle 5 weiblich) | Quotient der Binomialkoeffizienten (oder Produkt 12/30 · 11/29 · … · 8/26)
2017-bb-ea-B4.2e | 4 | ja | Rechnung¦Begründung · Berechnen Sie¦Begründen Sie | An der Lesung nehmen 174 Besucher teil, darunter ein Deutschkurs und dessen Lehrerin. Aus den Teilnehmern werden fünf Personen ausgelost, die je eine Freikarte für die nächste Veranstaltung erhalten. → Wahrscheinlichkeit dafür, dass die Lehrerin unter den fünf Gewinnern ist; Begründung, dass das Modell der Binomialverteilung dafür ungeeignet ist | Ziehen ohne Zurücklegen: über das Gegenereignis P = 1 − C(173; 5)/C(174; 5) = 1 − 169/174, gleichwertig zur Überlegung, dass jede der 174 Personen dieselbe Chance hat, unter den fünf Gezogenen zu sein. Die Binomialverteilung setzt unabhängige Wiederholungen mit gleichbleibender Trefferwahrscheinlichkeit voraus.
2018-bb-ea-B4.1d | 3 | ja | Rechnung · Berechnen Sie | Eine Umfrage ergab, dass zu medizinischen Fragen 73 % der Bevölkerung das Internet nutzen. 55 % der Internetnutzer nutzen Medinet, einen Ratgeber bei medizinischen Fragen, der nur im Internet verfügbar ist. In einer Arztpraxis sitzen 12 Personen, die das Internet zu medizinischen Fragen nutzen. Von diesen recherchieren 7 bei Medinet. 3 Personen werden aufgerufen. → Wahrscheinlichkeit dafür, dass unter den aufgerufenen Personen höchstens zwei sind, die bei Medinet recherchieren | Aus einer festen Gruppe wird ohne Zurücklegen gezogen, die Verteilung ist also hypergeometrisch. Statt drei Fälle zu addieren, das Gegenereignis nehmen: alle drei Aufgerufenen recherchieren bei Medinet, mit der Wahrscheinlichkeit (7 über 3) geteilt durch (12 über 3).
2022-bebb-gk-A1.6a | 2 | nein | Rechnung · Ermitteln Sie | Urne mit vier roten und zwei grünen Kugeln; drei Kugeln werden ohne Zurücklegen gezogen → Wahrscheinlichkeit, dass mindestens eine gezogene Kugel grün ist | 1 − P(alle rot)
## iqb

2023MgrundlegendBStochastikWTR1-1b | 3 | ja | Rechnung · Berechnen Sie | 200 Probepackungen, 10 davon mit Gutschein; 180 zufällig ausgewählte werden verschenkt → Wahrscheinlichkeit, dass alle Gutscheinpackungen verschenkt werden | Anzahl günstiger Auswahlen (alle 10 Gutscheine und 170 der 190 anderen) durch Anzahl aller Auswahlen
2024MerhoehtBStochastikWTR2-1e | 3 | ja | Rechnung · Weisen Sie nach | 80 Kinder, 12 davon mit Lastenrad gebracht; 10 zufällig ausgewählt → Nachweis P(genau zwei mit Lastenrad) ≈ 29,6 % | günstige durch mögliche Teilmengen
