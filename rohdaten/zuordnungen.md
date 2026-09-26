# Rohdatei zuordnungen

Stufe: I

- msa: Zuordnungen proportional und antiproportional (10 Zeilen)

Stand: 2026-09-26, Commit ca3237b

## A Typenprofil

**Dauer aus Menge und Rate berechnen** · 3 Zeilen · msa 3 · Jahre 2014–2024
msa/msa-typen.csv (gültig): Dauer aus einer Gesamtmenge und einer Rate je Zeiteinheit berechnen (Strecke : Geschwindigkeit, Volumen : Durchsatz) und in die verlangte Zeiteinheit umrechnen. Gegenrichtung: „Geschwindigkeit aus Weg und Zeit berechnen“.

**Kosten aus Menge und Preis berechnen** · 3 Zeilen · msa 3 · Jahre 2014–2024
msa/msa-typen.csv (gültig): Gesamtpreis aus einer berechneten Menge und einem Einheitspreis bestimmen.

**Proportionale Zuordnung Dreisatz** · 3 Zeilen · msa 3 · Jahre 2016–2023
msa/msa-typen.csv (gültig): Zu einer proportionalen Zuordnung aus einem Wertepaar den fehlenden vierten Wert per Dreisatz bestimmen. Abgrenzung: ist eine Rate (Geschwindigkeit, Durchsatz) gegeben und die Dauer gesucht, gilt „Dauer aus Menge und Rate berechnen“.

**Geschwindigkeit aus Weg und Zeit berechnen** · 1 Zeile · msa 1 · Jahre 2015
msa/msa-typen.csv (gültig): Konstante Geschwindigkeit aus zurückgelegter Strecke (auch Höhendifferenz) und Dauer berechnen und in die verlangte Einheit (m/s, km/h) umrechnen. Gegenrichtung zu „Dauer aus Menge und Rate berechnen“.

**Nebentypen:** Zeiteinheiten umrechnen (2) · Uhrzeit aus Startzeit und Dauer berechnen (1)

## B Zeilenliste

## msa

2014-OS-K2c | 3 | ja | Rechnung · Berechnen Sie | Durchschnittsgeschwindigkeit 5 km/h; um 11:30 Uhr am Restaurant; 45 Minuten Pause; Restaurant–Badestelle 2500 m → Ankunftszeit an der Badestelle | 2,5 km : 5 km/h = 0,5 h = 30 min; 11:30 + 45 min + 30 min
2015-OS-K3c | 4 | ja | Rechnung¦Rechnung · Berechnen Sie¦Ermitteln Sie | Lichtgeschwindigkeit ca. 3 · 10⁵ km/s; Entfernung Sonne – Proxima Centauri ca. 4,03 · 10¹⁵ km; 1 Jahr = 365 Tage → Lichtlaufzeit in Sekunden¦Lichtlaufzeit in Jahren | t = s : v = 4,03 · 10¹⁵ : (3 · 10⁵) ≈ 1,34 · 10¹⁰ s; ein Jahr = 365 · 24 · 60 · 60 = 31 536 000 s; Sekunden durch Jahressekunden
2024-OS-K6c | 2 | ja | Rechnung · Ermitteln Sie¦Geben Sie an | Strecke AB = 384 m; Durchschnittsgeschwindigkeit 3,2 m/s → Fahrtdauer in Minuten | t = 384 : 3,2 = 120 s = 2 min
2015-OS-K4c | 2 | ja | Rechnung · Berechnen Sie | Fallschirm öffnet bei t = 20 s in 1200 m Höhe; nach weiteren 100 s Höhe 700 m; konstante Geschwindigkeit → Sinkgeschwindigkeit in km/h | Höhendifferenz 500 m in 100 s = 5 m/s; · 3,6 = 18 km/h (oder 0,5 km in 1/36 h)
2014-OS-K4c | 1 | ja | Rechnung · Berechnen Sie | Verbrauch 9 l je 100 km; 100 000 km im Jahr 2011; Dieselpreis 145,5 ct je Liter → Kraftstoffkosten 2011 | 100 000 : 100 · 9 = 9 000 l; 9 000 · 1,455 €
2014-OS-K4d | 2 | ja | Rechnung · Weisen Sie nach | gleiche Fahrleistung 100 000 km, Verbrauch 9 l je 100 km (9 000 l); Preis 2012 152,0 ct; Kosten 2011 13 095 €; Behauptung: 585 € mehr → Nachweis der Mehrkosten 585 € | 9 000 · 1,52 = 13 680 €; 13 680 − 13 095 = 585 € (oder 9 000 · 0,065 €)
2024-OS-K2d | 1 | ja | Rechnung · Berechnen Sie | Gartenpflege 16 l pro Tag; 1 l Leitungswasser kostet 0,14 ct → Ersparnis pro Tag | 16 · 0,14 ct
2016-OS-B1d | 1 | ja | Kurzantwort · Geben Sie an | 100 g enthalten 30 g Fett → Fett in 20 g | 30 : 5 oder 0,3 · 20
2022-OS-B1b | 1 | ja | Kurzantwort · Geben Sie an | 3 kg Äpfel kosten 4,80 € → Preis für 5 kg | 4,80 : 3 = 1,60 € je kg, mal 5
2023-OS-B1a | 1 | ja | Kurzantwort · Geben Sie an | 4 km in 25 min bei gleichbleibender Geschwindigkeit → Zeit für 6 km in Minuten | 25 : 4 = 6,25 min je km, mal 6
