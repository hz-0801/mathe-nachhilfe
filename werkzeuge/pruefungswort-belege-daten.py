"""Zuordnungsdaten für werkzeuge/pruefungswort-belege.py – je Sek-I-Eintrag ein Abschnitt.

U(eintrag, einheit, [P10-Typen]) – die P10-Typen der Einheit laut Zuordnungszeile im Abschnitt
  „Prüfungsform (P10)“ des Eintrags (Namen wie in msa/msa-typen.csv; jeder muss in der Prüfungsform stehen).
V(eintrag, einheit, [P10-Typen]) – Verfahrensgeber: die Zuordnungszeile nennt die Einheit „Verfahren für“ diese
  P10-Typen einer anderen Datei (Stelle im Kommentar); sie zählen für die Einheit wie eigene.
T(eintrag, nr, text, [P10-Typen], grund) – die P10-Typen, die einen Katalogtyp prüfen; nr und text wie in
  werkzeuge/pruefungswort-belege-typen.txt (Einheit.Lfd, Wortlaut als Kontrolle). Grund Pflicht, außer der
  Typ (ohne Klammerzusatz) heißt wie der eine P10-Typ. Ohne T-Zeile: „kein P10-Typ“.
S(eintrag, nr, text, abi=[…], fhr=[…], grund) – Sek II: Prüfungstyp eines Katalogtyps, den das Skript nicht
  wortgleich findet (bisher keiner nötig).

Lesart „prüft“: die Fertigkeit des Katalogtyps ist Teil der Leistung, die der P10-Typ verlangt – nach seiner
Definition in msa-typen.csv oder nach einem Original (Haupt- oder Nebentyp); Vorstufen desselben Verfahrens
zählen mit; Fehler-finden-, Begründungs- und Darstellungstypen nur, wenn ein P10-Typ genau diese Leistung
verlangt. Stand 2026-09-26 (Auftrag Nacht, Teil 2).
"""

# ==== prozentrechnung ====
U('prozentrechnung', 1, ['Prozent und Anteil umwandeln', 'Fehlenden Prozentanteil ergänzen', 'Anteilsaussage prüfen und korrigieren'])
U('prozentrechnung', 2, ['Prozentsatz berechnen'])
U('prozentrechnung', 3, ['Prozentwert berechnen'])
U('prozentrechnung', 4, ['Grundwert berechnen'])
U('prozentrechnung', 5, ['Wert nach prozentualer Erhöhung berechnen', 'Prozentuale Veränderung berechnen', 'Steigung in Prozent deuten', 'Steigung in Prozent berechnen'])
T('prozentrechnung', '1.1', 'Bruch → Prozent (Nenner 100; Nenner, der in 100 aufgeht)', ['Prozent und Anteil umwandeln'],
  'Definition „Anteil als Prozentsatz angeben“; Nebenleistung in 2014-OS-B1i (9 von 15 Feldern als Prozentsatz) und 2014-OS-K6a (3/8 in Prozent).')
T('prozentrechnung', '1.2', 'Dezimalzahl ↔ Prozent', ['Prozent und Anteil umwandeln'],
  'Vorstufe desselben Umwandelns: die Dezimalzahl ist die Anteilsform, über die der Anteil in Prozent geschrieben wird (Definition „Anteil als Prozentsatz angeben“).')
T('prozentrechnung', '1.3', 'Anteil am Streifen oder an einer Figur ablesen und einzeichnen', ['Prozent und Anteil umwandeln', 'Prozentanteil einer Rasterfläche markieren'],
  'Ablesen an einer Figur: 2014-OS-B1i (graue Felder eines Rechtecks als Prozentsatz, Nebentyp); Einzeichnen: Definition „zum Prozentsatz gehörende Kästchen markieren“ (2014-GYM-B1g).')
T('prozentrechnung', '1.4', 'Anteilsformulierung ↔ Prozent („jeder fünfte“, „ein Viertel“, „4 von 100“)', ['Prozent und Anteil umwandeln'],
  'Definition nennt „jeder fünfte“, „ein Viertel“ und „4 von 100“; Originale 2022-OS-B1f und 2020-OS-B1a.')
T('prozentrechnung', '1.5', 'Prozentangaben ordnen', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  'Definition „Zahlen in Dezimal-, Prozent-, Bruch- … schreibweise in dieselbe Form bringen und ordnen“; Typ bei brueche-dezimalzahlen.md.')
T('prozentrechnung', '1.6', 'fehlenden Anteil zu 100 % ergänzen', ['Fehlenden Prozentanteil ergänzen'],
  'Definition „fehlenden Prozentsatz als Rest zu 100 %“; Original 2021-OS-K5b.')
T('prozentrechnung', '1.7', 'Anteilsaussage prüfen und korrigieren (Tabellenwerte)', ['Anteilsaussage prüfen und korrigieren'])
T('prozentrechnung', '2.1', 'Teil von 100', ['Prozentsatz berechnen'],
  'Vorstufe des Verfahrens Teil durch Ganzes mit dem Ganzen 100 (Definition „aus Teil und Ganzem den Anteil in Prozent“).')
T('prozentrechnung', '2.2', 'Teil von 50, 25, 20, 10 (erweitern)', ['Prozentsatz berechnen'],
  'Vorstufe desselben Verfahrens: Anteil auf Hundertstel erweitern (Definition „aus Teil und Ganzem den Anteil in Prozent“).')
T('prozentrechnung', '2.3', 'beliebiges Ganzes: W : G mit Taschenrechner, runden', ['Prozentsatz berechnen'],
  'Prüfungsform: 2023-OS-K6a (Anteil an 7,8 Mrd., gerundet) und 2015-OS-K7c (12 : 83 ≈ 14,5 %).')
T('prozentrechnung', '2.4', 'Anteil aus Sachtext (Ganzes zuerst finden)', ['Prozentsatz berechnen'],
  '2018-OS-K7a: das Ganze aus 14 und 2 Pfannkuchen erst bilden; ebenso 2015-OS-K7c (verwandelt und nicht verwandelt).')
T('prozentrechnung', '2.5', 'Rabatt in Prozent aus altem und neuem Preis (erst Rabatt in Euro)', ['Prozentsatz berechnen', 'Prozentuale Veränderung berechnen'],
  'Rabatt in Euro durch alten Preis ist der Prozentsatz (Definition); aus altem und neuem Preis ist es die Abnahme in Prozent des Ausgangswerts (Definition „Prozentuale Veränderung berechnen“, 2022-OS-K4b).')
T('prozentrechnung', '3.1', '50 %, 25 %, 10 % vom Ganzen', ['Prozentwert berechnen'],
  'Vorstufe mit bequemen Sätzen; die Originale rechnen 20 % (2017-OS-B1b, 2021-OS-B1c) und 30 % (2026-FOR-B1a) vom Grundwert.')
T('prozentrechnung', '3.2', '1 %-Weg (G : 100, mal p)', ['Prozentwert berechnen'],
  'Rechenweg des Prozentwerts (Definition „aus Grundwert und Prozentsatz den Prozentwert“), etwa 13 % von 50 € (2014-OS-B1a).')
T('prozentrechnung', '3.3', '10 %-Schritte (30 %, 15 %, 5 %)', ['Prozentwert berechnen'],
  'Rechenweg für 30 % von 70 € (2026-FOR-B1a) und 20 % von 550 € (2021-OS-B1c).')
T('prozentrechnung', '3.4', 'Dezimalzahl mal Grundwert (0,3 · G)', ['Prozentwert berechnen'],
  'Lösungswege der Originale „0,3 · 70“ (2026-FOR-B1a) und „550 · 0,2“ (2021-OS-B1c).')
T('prozentrechnung', '3.5', 'Grundwert mit Komma (3,50 €)', ['Prozentwert berechnen'],
  '20 % von 7,50 € in 2015-OS-K2a (Nebentyp) und 20 % von 3,50 € als Schritt in 2024-OS-B1e.')
T('prozentrechnung', '3.6', 'Ersparnis und neuer Preis unterscheiden', ['Prozentwert berechnen'],
  '2021-OS-B1c (Ersparnis, Restpreis 440 € als Distraktor) und 2017-OS-B1b (Rabatt in Euro, Fehlerquelle Restpreis).')
T('prozentrechnung', '3.7', 'Prozentsatz über 100 %', ['Prozentwert berechnen'],
  'Definition „aus Grundwert und Prozentsatz den Prozentwert“ ohne Grenze für p; kein Original mit p über 100 %.')
T('prozentrechnung', '3.8', 'Mehrwertsteuer in Euro', ['Prozentwert berechnen'],
  'Prozentwert (19 % vom Nettopreis) im Kontext Mehrwertsteuer (Definition); kein Original mit diesem Kontext.')
T('prozentrechnung', '4.1', 'glatte Sätze (50 %, 25 %, 20 %, 10 %: mal 2, 4, 5, 10)', ['Grundwert berechnen'],
  '2023-OS-B1b (25 % sind 200 €, mal 4) und 2025-OS-B1a (20 % sind 6 €, mal 5).')
T('prozentrechnung', '4.2', '1 %-Weg (W : p, mal 100)', ['Grundwert berechnen'],
  'Lösungsweg von 2025-OS-B1a: „1 % = 0,30 €, 100 % = 30 €“.')
T('prozentrechnung', '4.3', 'beliebiger Satz mit Taschenrechner', ['Grundwert berechnen'],
  'Definition „aus Prozentwert und Prozentsatz den Grundwert“ ohne Einschränkung des Satzes.')
T('prozentrechnung', '4.4', 'Sachtext („das sind 60 % der Klasse“)', ['Grundwert berechnen'],
  'Beide Originale sind Sachtexte der Form „… das sind p %“: 2023-OS-B1b (Gewinn), 2025-OS-B1a (Rabatt).')
T('prozentrechnung', '4.5', 'gemischte Aufgaben: erst zuordnen (Prozentwert, Prozentsatz oder Grundwert gesucht), dann rechnen', ['Grundwert berechnen', 'Prozentwert berechnen', 'Prozentsatz berechnen'],
  'Die P10 stellt die drei Grundaufgaben einzeln, das Zuordnen ist ihre Hürde (Fehlerquelle „p % von W statt Grundwert“ in 2023-OS-B1b und 2025-OS-B1a).')
T('prozentrechnung', '5.1', '„um“ und „auf“ unterscheiden', ['Wert nach prozentualer Erhöhung berechnen'],
  'Vorstufe des Verfahrens: „um 20 % erhöht“ (2024-OS-B1e) und „20 % Rabatt“ (2015-OS-K2b) richtig lesen.')
T('prozentrechnung', '5.2', 'neuer Wert über Prozentwert (dazu, weg)', ['Wert nach prozentualer Erhöhung berechnen'],
  '2024-OS-B1e (3,50 € plus 0,70 €) und 2015-OS-K2b (Rabattbetrag abziehen).')
T('prozentrechnung', '5.3', 'neuer Wert über Faktor (1,2; 0,8)', ['Wert nach prozentualer Erhöhung berechnen'],
  'Definition nennt den Wachstumsfaktor; 2015-OS-K2b über den Faktor 0,8.')
T('prozentrechnung', '5.4', 'Veränderung in Prozent aus zwei Werten (Differenz : Ausgangswert)', ['Prozentuale Veränderung berechnen'],
  'Definition „Zu- oder Abnahme zwischen zwei Werten in Prozent des Ausgangswerts“; 2016-OS-K2c, 2022-OS-K4b, 2026-FOR-K3c.')
T('prozentrechnung', '5.5', 'alter Wert aus neuem Wert und Prozentsatz', ['Grundwert berechnen'],
  'Der neue Wert ist der Prozentwert zum Satz 80 % bzw. 120 % (Definition „aus Prozentwert und Prozentsatz den Grundwert“); kein Original mit verändertem Grundwert.')
T('prozentrechnung', '5.6', 'Brutto/Netto (19 %, 7 %)', ['Wert nach prozentualer Erhöhung berechnen'],
  'Brutto aus Netto ist die Erhöhung um 19 % (Definition, Wachstumsfaktor); kein Original im Kontext Mehrwertsteuer.')
T('prozentrechnung', '5.7', 'Prozentpunkte gegen Prozent', ['Prozentwert berechnen'],
  '2019-OS-K5a: Zunahme von 72 % auf 95 % als 23 % von 1 200, Fehlerquelle „Prozentpunkte als Anzahl“ (Typ bei Einheit 3).')
T('prozentrechnung', '5.8', 'Steigung in Prozent deuten und berechnen', ['Steigung in Prozent deuten', 'Steigung in Prozent berechnen'],
  'Beide Steigungs-Typen; einziges Original 2025-OS-K4b (deuten als Haupt-, berechnen als Nebentyp).')


# ==== brueche-dezimalzahlen ====
U('brueche-dezimalzahlen', 1, ['Bruchteil einer Fläche bestimmen', 'Bruchteil einer Größe berechnen'])
U('brueche-dezimalzahlen', 5, ['Mitte zweier Zahlen bestimmen', 'Zahlen in verschiedenen Darstellungen vergleichen'])
T('brueche-dezimalzahlen', '1.1', 'Anteil an einer gleich geteilten Figur ablesen', ['Bruchteil einer Fläche bestimmen'],
  'Definition „Bruchteil einer markierten Teilfläche an einer Figur angeben“; 2014-OS-B1i (9 von 15 gleichen Feldern) und 2024-OS-B1b (8 von 16 Kästchen).')
T('brueche-dezimalzahlen', '1.2', 'Anteil einzeichnen (Kästchen, Streifen, Kreis)', ['Bruchteil einer Fläche bestimmen', 'Prozentanteil einer Rasterfläche markieren'],
  'Definition „einen Bruchteil einer Figur durch Zerlegen markieren“ (2017-OS-B1a 6/7 schraffieren, 2021-OS-B1b 3/8 kennzeichnen, 2025-OS-B1c ein Viertel eines Quadrats); als Prozentanteil in 2014-GYM-B1g (8 % von 25 Kästchen).')
T('brueche-dezimalzahlen', '1.3', 'Anteil bei ungleichen Teilen (erst gleich groß machen: halbe Kästchen, Sektoren verschiedener Größe)', ['Bruchteil einer Fläche bestimmen'],
  '2019-OS-B1c (Sektoren zu 60° und 30° erst auf das Maß 30° bringen, 3/12) und 2024-OS-B1b (graue Fläche mit halben Kästchen).')
T('brueche-dezimalzahlen', '1.4', 'unter mehreren Figuren die mit dem gegebenen Anteil auswählen (Ankreuzen)', ['Bruchteil einer Fläche bestimmen'],
  'Definition „unter mehreren Figuren die mit einem vorgegebenen Anteil auswählen“; 2026-FOR-B1b (Figur mit dem Anteil 1/3).')
T('brueche-dezimalzahlen', '1.5', 'Anteil an einer Menge (Kinder, Plättchen) angeben', ['Wahrscheinlichkeit einstufig', 'Relative Häufigkeit angeben'],
  'Anteil an einer Menge als Bruch im Kontext Zufall und Daten: 2015-OS-B1a (Anteil weißer Kugeln je Topf 4/6, 2/6, 3/6), 2019-OS-K6a (3 von 20 Stiften) und 2015-OS-K7b (22 von 34 Spielen als relative Häufigkeit).')
T('brueche-dezimalzahlen', '1.6', 'Bruchteil einer Menge oder Größe berechnen (Ganzes : Nenner · Zähler; auch mit Komma und Einheit)', ['Bruchteil einer Größe berechnen', 'Bruchteil einer Fläche bestimmen', 'Aussage über Bruchteile einer Größe prüfen', 'Gesamtmenge aus Pro-Kopf-Angabe berechnen'],
  'Definition „Bruchteil einer Größe mit Einheit berechnen“ (2018-OS-B1a, 3/4 von 1,2 kg); dasselbe Verfahren in 2017-OS-B1a (28 : 7 · 6 = 24 Kästchen), 2021-GYM-B1b (ein Drittel von 60 km) und 2023-GYM-K4c (zwei Drittel von 128 kg je Einwohner).')
T('brueche-dezimalzahlen', '1.7', 'Rest zum Ganzen (Tonne zu 2/3 voll – wie viel fehlt)', ['Bruchteil einer Größe berechnen', 'Aussage über Bruchteile einer Größe prüfen'],
  '2015-OS-B1h (Tonne zu 2/3 gefüllt, Rest 200 l statt der Füllmenge) und 2021-GYM-B1b (Rest der Strecke nach einem Drittel, davon ein Viertel).')
T('brueche-dezimalzahlen', '1.8', 'Ganzes aus Bruchteil (Vorrat: ein Viertel sind 6 – wie viel ist alles)', ['Grundwert berechnen'],
  'Ganzes aus einem Bruchteil ist das Verfahren des Grundwerts mit glattem Satz: 2023-OS-B1b (25 %, also ein Viertel, sind 200 €, mal 4).')
T('brueche-dezimalzahlen', '2.2', 'Erweitern mit gegebener Zahl', ['Prozent und Anteil umwandeln', 'Wahrscheinlichkeit mehrstufig unabhängig'],
  'Vorstufe des Erweiterns auf einen gegebenen Nenner: 1/5 = 20/100 in 2022-OS-B1f und 1/4 = 16/64 in 2014-OS-K6c.')
T('brueche-dezimalzahlen', '2.3', 'Kürzen mit gegebener Zahl', ['Bruchteil einer Fläche bestimmen', 'Wahrscheinlichkeit einstufig'],
  'Vorstufe des vollständigen Kürzens mit einer Zahl: 9/15 = 3/5 in 2014-OS-B1i, 20/100 = 1/5 in 2014-OS-B1b.')
T('brueche-dezimalzahlen', '2.4', 'vollständig kürzen', ['Bruchteil einer Fläche bestimmen', 'Wahrscheinlichkeit einstufig', 'Relative Häufigkeit angeben', 'Wahrscheinlichkeit mehrstufig unabhängig', 'Wahrscheinlichkeit mehrstufig ohne Zurücklegen', 'Baumdiagramm ergänzen', 'Wahrscheinlichkeit über Gegenereignis berechnen'],
  'Das Ergebnis gilt erst vollständig gekürzt als fertig: 2014-OS-B1i (9/15 = 3/5, Voraussetzung „Bruch kürzen“), 2014-OS-B1d (4/6 = 2/3), 2015-OS-K7b (22/34 = 11/17), 2014-OS-K6c (26/64 = 13/32), 2019-OS-K6c (120/6840 = 1/57), 2026-FOR-K6b (15/36 = 5/12) und 2026-FOR-K6c (33/36 = 11/12).')
T('brueche-dezimalzahlen', '2.5', 'auf gegebenen Nenner erweitern (Zwölftel, Hundertstel)', ['Prozent und Anteil umwandeln', 'Wahrscheinlichkeit mehrstufig unabhängig'],
  'Auf Hundertstel erweitern in 2022-OS-B1f (1/5 = 20/100 = 20 %), auf Vierundsechzigstel in 2014-OS-K6c (1/4 = 16/64 vor dem Addieren).')
T('brueche-dezimalzahlen', '2.6', 'zwei Brüche gleichnamig machen (ein Nenner Vielfaches des anderen; beide erweitern; Nenner multiplizieren)', ['Wahrscheinlichkeit mehrstufig unabhängig'],
  'Summenregel mit einem Nenner als Vielfachem des anderen: 2014-OS-K6c (16/64 + 9/64 + 1/64) und 2025-OS-K3c (1/4 + 1/16 = 5/16).')
T('brueche-dezimalzahlen', '2.8', 'Bruch als Geteilt-Aufgabe (3 : 4 = 3/4, 5 : 2 = 2 1/2)', ['Wahrscheinlichkeit einstufig', 'Relative Häufigkeit angeben', 'Termwert berechnen'],
  'Quotient als Bruch: 20 : (80 + 20) = 20/100 in 2014-OS-B1b und 22 : 34 = 22/34 in 2015-OS-K7b; umgekehrt der Bruchterm (a + b)/c als 7 : (−2) in 2021-OS-B1g.')
T('brueche-dezimalzahlen', '3.6', 'drei bis vier Brüche ordnen', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  'Definition „Zahlen in … Bruchschreibweise in dieselbe Form bringen und ordnen“; Vorstufe mit Brüchen allein, kein Original ordnet nur Brüche.')
T('brueche-dezimalzahlen', '3.7', 'Zahl zwischen zwei Brüchen angeben (erweitern, dann dazwischen wählen)', ['Zahl zu Bedingung angeben'],
  'Definition nennt „zwischen 1/2 und 4/5“; Original 2014-OS-B1c wird hier geführt, der Typ liegt in rationale-zahlen.md Einheit 1.')
T('brueche-dezimalzahlen', '4.2', 'Zehnerbruch ↔ Dezimalzahl (auch mit Nullen: 3/100, 3/1000)', ['Zahlen in verschiedenen Darstellungen vergleichen', 'Wahrscheinlichkeit einstufig'],
  'Hundertstel mit Null: 5 % = 5/100 = 0,05 in 2018-OS-B1d (Fehlerquelle 0,5) und P = 5/100 = 0,05 in 2016-GYM-B1f.')
T('brueche-dezimalzahlen', '4.3', 'Dezimalzahl am Zahlenstrahl (Zehntel-, Hundertstelskala) eintragen und ablesen', ['Mitte zweier Zahlen bestimmen'],
  'Definition „als Mittelwert oder am Zahlenstrahl“; 2020-OS-B1f (Zahlenstrahl mit Hundertsteln zwischen −0,6 und −0,5).')
T('brueche-dezimalzahlen', '4.5', 'Bruch → Dezimalzahl durch Erweitern auf 10, 100, 1000 (Halbe, Viertel, Fünftel, Zwanzigstel, Fünfundzwanzigstel)', ['Zahlen in verschiedenen Darstellungen vergleichen', 'Zahl zu Bedingung angeben'],
  'Halbe und Fünftel als Dezimalzahlen: 3/2 = 1,5 und 8/5 = 1,6 in 2015-OS-B1c, 1/2 = 0,5 und 4/5 = 0,8 in 2014-OS-B1c.')
T('brueche-dezimalzahlen', '4.6', 'Dezimalzahl → Bruch und kürzen (auch größer als 1)', ['Anteilsaussage prüfen und korrigieren'],
  '2023-OS-K6b: der Quotient 0,25 ist als „ein Viertel“ zu lesen, um die Aussage „ein Drittel“ zu widerlegen.')
T('brueche-dezimalzahlen', '4.7', 'Bruch → Dezimalzahl durch Division (Achtel; Taschenrechner)', ['Prozent und Anteil umwandeln', 'Relative Häufigkeit angeben'],
  'Division mit Taschenrechner: 3 : 8 = 0,375 = 37,5 % in 2014-OS-K6a (Nebentyp) und 22 : 34 ≈ 0,65 in 2015-OS-K7b.')
T('brueche-dezimalzahlen', '5.1', 'zwei Dezimalzahlen mit gleich vielen Stellen vergleichen', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  'Vorstufe des Ordnens: in 2023-OS-B1f sind 0,44 und 0,16 zu vergleichen, nachdem alle Zahlen Dezimalzahlen sind.')
T('brueche-dezimalzahlen', '5.2', 'verschieden viele Stellen (Nullen anhängen)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2014-OS-B1h (1,4 gegen 1,414; −0,5 gegen −0,512) und 2018-OS-B1d (0,05 gegen 0,5).')
T('brueche-dezimalzahlen', '5.3', 'Dezimalzahlen ordnen', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  'Definition „… in dieselbe Form bringen und ordnen“; aufsteigende Reihe in 2014-OS-B1h.')
T('brueche-dezimalzahlen', '5.4', 'runden auf Zehntel und Hundertstel (auch Größen mit Einheit)', ['Prozentsatz berechnen', 'Relative Häufigkeit angeben', 'Pythagoras Kathete'],
  'Runden auf Zehntel oder Hundertstel verlangen die Ergebnisse von 2023-OS-K6a (≈ 16,0 %), 2015-OS-K7b (≈ 0,65) und als Größe mit Einheit 2026-FOR-K4a (h ≈ 29,2 cm).')
T('brueche-dezimalzahlen', '5.5', 'Mitte zweier Zahlen (Mittelwert oder Zahlenstrahl eine Stelle feiner)', ['Mitte zweier Zahlen bestimmen', 'Median bestimmen'],
  'Definition „Zahl genau in der Mitte zweier Dezimalzahlen … als Mittelwert“ (2020-OS-B1f); dieselbe Mitte beim Median gerader Anzahl in 2024-OS-B1h (Mitte zwischen 18 und 20).')
T('brueche-dezimalzahlen', '5.6', 'Zahl zwischen zwei Zahlen angeben (auch zwischen zwei Brüchen über Dezimalzahlen)', ['Zahl zu Bedingung angeben'],
  'Definition „zwischen 1/2 und 4/5“; 2014-OS-B1c über die Dezimalzahlen 0,5 und 0,8.')
T('brueche-dezimalzahlen', '5.7', 'Bruch gegen Dezimalzahl (Vergleichszeichen)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2015-OS-B1c: 1,5 < 3/2 und 8/5 > 3/2 prüfen.')
T('brueche-dezimalzahlen', '5.8', 'Prozent gegen Dezimalzahl', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2018-OS-B1d: Vergleichszeichen zwischen 5 % und 0,5.')
T('brueche-dezimalzahlen', '5.9', 'gemischte Liste ordnen (Bruch, Dezimalzahl, Prozent, Potenz einer Dezimalzahl)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2023-OS-B1f (4,4; 0,44; 0,4²; 44 %) und 2014-OS-B1h (−1/2; 1,4; −0,512; √2).')
T('brueche-dezimalzahlen', '5.10', 'Aussagen prüfen und die wahre ankreuzen', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2015-OS-B1c verlangt genau diese Leistung: die wahre von drei Ungleichungen ankreuzen.')
T('brueche-dezimalzahlen', '5.11', 'mit negativen Zahlen (Vorrat, rationale-zahlen.md Einheit 1)', ['Zahlen in verschiedenen Darstellungen vergleichen', 'Mitte zweier Zahlen bestimmen'],
  'Negative Zahlen in 2014-OS-B1h (−1/2 gegen −0,512), 2017-OS-B1e (−10³ als kleinste) und 2020-OS-B1f (Mitte von −0,6 und −0,5).')
T('brueche-dezimalzahlen', '5.12', 'mit Wurzeln über Näherungswert (Vorrat, potenzen-wurzeln.md)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2015-OS-B1c und 2014-OS-B1h vergleichen √2 über den Näherungswert 1,41 (Voraussetzung „Wurzel abschätzen“).')

# ==== bruchrechnung ====
T('bruchrechnung', '1.1', 'gleichnamig addieren und subtrahieren', ['Wahrscheinlichkeit mehrstufig unabhängig', 'Wahrscheinlichkeit mehrstufig ohne Zurücklegen', 'Baumdiagramm ergänzen'],
  'Summenregel mit gleichnamigen Brüchen: 2014-OS-K6c (16/64 + 9/64 + 1/64), 2017-OS-K6b (1/6 + 1/6, Nebentyp) und 2020-OS-K6c (15/216 + 1/216).')
T('bruchrechnung', '1.2', 'Ergebnis kürzen', ['Wahrscheinlichkeit mehrstufig unabhängig', 'Wahrscheinlichkeit mehrstufig ohne Zurücklegen', 'Baumdiagramm ergänzen', 'Wahrscheinlichkeit über Gegenereignis berechnen'],
  'Summe oder Differenz wird gekürzt: 26/64 = 13/32 (2014-OS-K6c), 2/6 = 1/3 (2017-OS-K6b), 16/216 = 2/27 (2020-OS-K6c) und 33/36 = 11/12 (2026-FOR-K6c).')
T('bruchrechnung', '1.4', 'gleichnamig machen mit einem Nenner als Vielfachem des anderen', ['Wahrscheinlichkeit mehrstufig unabhängig'],
  '2014-OS-K6c (1/4 = 16/64 neben 9/64 und 1/64) und 2025-OS-K3c (1/4 + 1/16 = 5/16).')
T('bruchrechnung', '1.6', 'ganze Zahl plus Bruch', ['Wahrscheinlichkeit über Gegenereignis berechnen', 'Baumdiagramm ergänzen', 'Wahrscheinlichkeit einstufig'],
  'Eins minus Bruch: Definition „über 1 − P(Gegenereignis)“ (2026-FOR-K6c, 1 − 3/36), Knotensumme 1 im Baum (2015-OS-K7d, 1 − 1/11 = 10/11) und 2014-OS-B1d (1 − 2/6 als Rechenweg).')
T('bruchrechnung', '2.1', 'gleich viele Stellen', ['Spannweite berechnen', 'Guthabentabelle mit Zinsen ergänzen'],
  'Dezimalzahlen mit gleich vielen Stellen: 1,85 − 1,77 in 2026-FOR-K3a, 9,9 − 9,5 in 2019-OS-B1i und 612,08 + 12,24 in 2014-OS-K3b.')
T('bruchrechnung', '2.3', 'mit Übertrag', ['Spannweite berechnen', 'Guthabentabelle mit Zinsen ergänzen', 'Wert nach prozentualer Erhöhung berechnen'],
  'Übertrag: 85,1 − 19,2 in 2024-OS-K2a, 612,08 + 12,24 (Hundertstel) in 2014-OS-K3b und 3,50 € + 0,70 € in 2024-OS-B1e.')
T('bruchrechnung', '2.4', 'ganze Zahl plus Dezimalzahl', ['Guthabentabelle mit Zinsen ergänzen', 'Wert nach prozentualer Erhöhung berechnen'],
  '612,08 + 12,24 + 200 = 824,32 in 2014-OS-K3b und 36 € + 7,50 € in 2015-OS-K2b.')
T('bruchrechnung', '2.5', 'Größen mit Komma (2,50 € + 0,75 €; 1,2 m − 0,45 m)', ['Spannweite berechnen', 'Guthabentabelle mit Zinsen ergänzen', 'Wert nach prozentualer Erhöhung berechnen'],
  'Größen mit Komma: 1,85 € − 1,77 € (2026-FOR-K3a), 9,9 m − 9,5 m (2019-OS-B1i), die Euro-Beträge der Guthabentabelle (2014-OS-K3b) und 3,50 € + 0,70 € (2024-OS-B1e).')
T('bruchrechnung', '3.1', 'Bruch mal natürliche Zahl (vervielfachen)', ['Wahrscheinlichkeit mehrstufig unabhängig', 'Baumdiagramm ergänzen'],
  '2020-OS-K6c: drei gleich wahrscheinliche Pfade, 3 · 5/216 = 15/216.')
T('bruchrechnung', '3.3', 'Bruch von Bruch (Zähler mal Zähler, Nenner mal Nenner; Bruchteil einer Zahl oder Größe → brueche-dezimalzahlen.md Einheit 1)', ['Wahrscheinlichkeit mehrstufig unabhängig', 'Wahrscheinlichkeit mehrstufig ohne Zurücklegen', 'Baumdiagramm ergänzen', 'Wahrscheinlichkeit über Gegenereignis berechnen', 'Zufallsgerät zu Wahrscheinlichkeit entwerfen'],
  'Pfadregel als Bruch mal Bruch: 2025-OS-K3b (1/4 · 2/4), 2019-OS-K6c (6/20 · 5/19 · 4/18), 2026-FOR-K6b (3/6 · 5/6), 2026-FOR-K6c (3/6 · 1/6) und 2025-OS-K3d (2/4 · 2/4 = 1/4).')
T('bruchrechnung', '4.1', 'Komma verschieben (mal 10, 100, 1000; geteilt durch 10, 100)', ['Zehnerpotenzschreibweise umwandeln', 'Große Zahl mit Zehnerpotenz multiplizieren', 'Kosten aus Menge und Preis berechnen'],
  'Komma verschieben mit Zehnerpotenzen: 8,5 · 10⁵ = 850 000 (2016-OS-B1h), 2,1 · 10⁻⁴ = 0,00021 (2019-OS-B1j), mal 100 durch Nullen anhängen (2015-OS-K3a) und 145,5 ct = 1,455 € (2014-OS-K4c).')
T('bruchrechnung', '4.2', 'Dezimalzahl mal natürliche Zahl', ['Kosten aus Menge und Preis berechnen', 'Prozentwert berechnen'],
  '16 · 0,14 ct (2024-OS-K2d), 9 000 · 1,455 € (2014-OS-K4c), 400 · 0,02 (2015-OS-B1e) und 550 · 0,2 (2021-OS-B1c).')
T('bruchrechnung', '4.3', 'Dezimalzahl mal Dezimalzahl (Kommastellen zählen)', ['Zahlen in verschiedenen Darstellungen vergleichen', 'Guthabentabelle mit Zinsen ergänzen', 'Wert nach prozentualer Erhöhung berechnen'],
  'Kommastellen zählen: 0,4² = 0,16 (2023-OS-B1f, Fehlerquelle 0,8), 824,32 · 0,02 (2014-OS-K3b) und 43,50 · 0,8 (2015-OS-K2b).')
T('bruchrechnung', '4.4', 'Dezimalzahl geteilt durch natürliche Zahl', ['Bruchteil einer Größe berechnen', 'Mitte zweier Zahlen bestimmen', 'Arithmetisches Mittel berechnen'],
  '1,2 : 4 (2018-OS-B1a), −1,1 : 2 (2020-OS-B1f) und 78,3 : 9 (2021-OS-K5a, Nebentyp).')
T('bruchrechnung', '4.5', 'geteilt durch Dezimalzahl (beide Kommas verschieben)', ['Rechteckseite aus Fläche berechnen'],
  '2014-OS-K5d: Plattenlänge 1,8 : 1,2 = 1,5 m.')
T('bruchrechnung', '4.7', 'Größen (Preis mal Anzahl, Cent und Euro)', ['Kosten aus Menge und Preis berechnen'],
  'Definition „Gesamtpreis aus einer berechneten Menge und einem Einheitspreis“; 2024-OS-K2d (Cent bleibt Cent) und 2014-OS-K4c (Cent in Euro).')
T('bruchrechnung', '5.1', 'Punkt vor Strich mit Brüchen', ['Wahrscheinlichkeit mehrstufig unabhängig', 'Wahrscheinlichkeit mehrstufig ohne Zurücklegen', 'Baumdiagramm ergänzen'],
  'Pfad- und Summenregel als Punkt vor Strich: (1/2)² + (3/8)² + (1/8)² (2014-OS-K6c), 1/6 + 5/6 · 1/5 (2017-OS-K6b) und 1/11 + 10/11 · 1/10 + 10/11 · 9/10 · 1/9 (2015-OS-K7d).')
T('bruchrechnung', '5.2', 'mit Dezimalzahlen', ['Wert nach prozentualer Erhöhung berechnen', 'Term zu Sachtext angeben', 'Termwert berechnen'],
  '3 · 12 + 7,50 (2015-OS-K2b), 2 · 12 € + 2 · 7,50 € (2015-OS-K2a) und (−5)² − 2 · 2,5 − (−2) (2022-GYM-B2a).')
T('bruchrechnung', '5.3', 'Klammern', ['Termwert berechnen', 'Term zu Sachtext angeben'],
  'Klammer zuerst: (8 + (−1)) : (−2) (2021-OS-B1g), 5 · (−2 − 3) (2026-FOR-B1g) und 1/5 · (36 € + 7,50 €) (2015-OS-K2a).')

# ==== rationale-zahlen ====
U('rationale-zahlen', 1, ['Zahl zu Bedingung angeben'])
U('rationale-zahlen', 3, ['Vorzeichenregel anwenden', 'Termwert berechnen'])
U('rationale-zahlen', 4, ['Ausgangswert aus Differenz berechnen', 'Günstigste Preiskombination bestimmen'])
T('rationale-zahlen', '1.2', 'Zahlen an der Zahlengeraden eintragen und ablesen (ganze, Dezimalzahlen, Brüche)', ['Mitte zweier Zahlen bestimmen', 'Zahl zu Bedingung angeben', 'Zahlen in verschiedenen Darstellungen vergleichen'],
  'Zahlengerade mit negativen Zahlen: Definition „am Zahlenstrahl“ (2020-OS-B1f), „jede Zahl rechts von −150“ (2015-OS-B1b) und „am weitesten links auf dem Zahlenstrahl“ (2017-OS-B1e).')
T('rationale-zahlen', '1.4', 'zwei Zahlen vergleichen (< >)', ['Zahl zu Bedingung angeben', 'Zahlen in verschiedenen Darstellungen vergleichen'],
  '2015-OS-B1b (größer als −150, Fehlerquelle −200) und 2014-OS-B1h (−1/2 = −0,5 > −0,512).')
T('rationale-zahlen', '1.5', 'Zahlen ordnen (gemischt: Bruch, Dezimalzahl, negativ)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  'Definition „… in dieselbe Form bringen und ordnen“; 2014-OS-B1h (−1/2; 1,4; −0,512; √2) und 2017-OS-B1e (−0,01; −10³; −10²; −0,1).')
T('rationale-zahlen', '1.6', 'Zahl zu Bedingung angeben („größer als −150“, „zwischen zwei Zahlen“)', ['Zahl zu Bedingung angeben'])
T('rationale-zahlen', '1.7', 'Mitte zweier Zahlen', ['Mitte zweier Zahlen bestimmen'],
  '2020-OS-B1f: Mitte von −0,6 und −0,5 (Fehlerquelle −0,65 in die falsche Richtung); Typ bei brueche-dezimalzahlen.md.')
T('rationale-zahlen', '1.8', 'runden', ['Nullstellen quadratische Funktion berechnen'],
  '2017-OS-K5d rundet die negativen Nullstellen −3 ± √2 auf −1,59 und −4,41 (Nebentyp).')
T('rationale-zahlen', '1.9', 'Punkte in vier Quadranten (Verfahren und Kette in symmetrie-abbildungen.md Einheit 1; hier nur als Anwendung der negativen Zahlen)', ['Gerade durch zwei Punkte zeichnen', 'Streckenlänge aus Koordinaten berechnen'],
  'Punkte mit negativen Koordinaten eintragen und ablesen: K(−4|−1) in 2017-OS-K5a, B(3|−1,5) in 2025-OS-K5a, A(0|−2) und B(2|−2) aus dem Bild in 2019-OS-K2d.')
T('rationale-zahlen', '2.1', 'positive Zahl dazu oder weg von negativer Zahl (Zahlengerade)', ['Termwert berechnen'],
  '2026-FOR-B1g: −2 − 3 = −5 in der Klammer (Fehlerquelle −1).')
T('rationale-zahlen', '2.2', 'negative Zahl addieren (Klammer)', ['Termwert berechnen', 'Mitte zweier Zahlen bestimmen'],
  '8 + (−1) in 2021-OS-B1g, 2 + (−4) in 2016-OS-B1i und −0,6 + (−0,5) in 2020-OS-B1f.')
T('rationale-zahlen', '2.3', 'negative Zahl subtrahieren (zwei Minus)', ['Termwert berechnen', 'Geradengleichung aus zwei Punkten'],
  '4 − (−3) in 2019-GYM-B1d, − (−2) in 2022-GYM-B2a und die Koordinatendifferenzen 3 − (−2) in 2025-OS-K5a und 2 − (−4) in 2017-OS-K5a (Nebentyp).')
T('rationale-zahlen', '2.4', 'Zeichen zusammenfassen und rechnen', ['Termwert berechnen'],
  'Erster Schritt der Termwert-Originale: 8 + (−1) = 8 − 1 (2021-OS-B1g) und 2 + (−4) = 2 − 4 (2016-OS-B1i).')
T('rationale-zahlen', '2.5', 'Beträge: gleiche Vorzeichen addieren, verschiedene subtrahieren', ['Termwert berechnen', 'Mitte zweier Zahlen bestimmen'],
  '2 + (−4) = −2 (2016-OS-B1i), −2 − 3 = −5 (2026-FOR-B1g) und −0,6 + (−0,5) = −1,1 (2020-OS-B1f).')
T('rationale-zahlen', '2.6', 'Unterschied zweier Zahlen (Abstand)', ['Geradengleichung aus zwei Punkten'],
  'Die Steigung aus zwei Punkten verlangt den Unterschied der Koordinaten über null hinweg: 3 − (−2) = 5 und −1,5 − 6 = −7,5 in 2025-OS-K5a, 2 − (−4) = 6 in 2017-OS-K5a.')
T('rationale-zahlen', '2.7', 'mehrere Summanden', ['Termwert berechnen'],
  '2022-GYM-B2a: 25 − 5 + 2 nach dem Einsetzen von a = −2.')
T('rationale-zahlen', '2.8', 'Dezimalzahlen und Brüche', ['Mitte zweier Zahlen bestimmen', 'Termwert berechnen'],
  'Dezimalzahlen mit Vorzeichen: −0,6 + (−0,5) in 2020-OS-B1f und −2 + 4,5 in 2022-GYM-B2a.')
T('rationale-zahlen', '3.1', 'plus mal minus, minus mal minus', ['Vorzeichenregel anwenden', 'Termwert berechnen', 'Punktprobe durchführen'],
  'Definition „Vorzeichen des Ergebnisses beim Multiplizieren“ (2015-OS-B1g); 5 · (−5) in 2026-FOR-B1g und −2 · (−4) in 2026-FOR-K5b.')
T('rationale-zahlen', '3.2', 'dividieren mit Vorzeichen', ['Termwert berechnen', 'Vorzeichenregel anwenden'],
  '7 : (−2) = −3,5 (2021-OS-B1g) und (−2) : (−2) = 1 (2016-OS-B1i); die Definition der Vorzeichenregel nennt das Dividieren.')
T('rationale-zahlen', '3.3', 'mehrere Faktoren (Anzahl der Minuszeichen)', ['Vorzeichenregel anwenden'],
  'Definition „Vorzeichen des Ergebnisses beim Multiplizieren … positiver und negativer Zahlen“ ohne Beschränkung auf zwei Faktoren; kein Original mit drei Faktoren.')
T('rationale-zahlen', '3.4', 'Potenzen: (−2)² gegen −2²', ['Punktprobe durchführen', 'Termwert berechnen', 'Wurzel eines Quadrats berechnen'],
  'p(−3) = −(−3)² = −9 in 2014-OS-K7a (Fehlerquelle +9), (−5)² = 25 in 2022-GYM-B2a und (−4)² = 16 in 2015-OS-B1j.')
T('rationale-zahlen', '3.5', 'Punkt vor Strich mit negativen Zahlen', ['Termwert berechnen', 'Punktprobe durchführen', 'Funktionswert berechnen'],
  '(−5)² − 2 · 2,5 − (−2) (2022-GYM-B2a), −2 · (−4) + 2 (2026-FOR-K5b) und ½ · (−10) + 1 (2017-OS-K5b).')
T('rationale-zahlen', '3.6', 'Termwert mit Klammer (5 · (x − 3) für x = −2)', ['Termwert berechnen'],
  'Definition „Wert eines Terms für einen gegebenen Variablenwert … auch mit negativen Zahlen“; 2026-FOR-B1g ist genau 5 · (x − 3) für x = −2.')
T('rationale-zahlen', '3.7', 'Vorzeichenregel als Aussage prüfen', ['Vorzeichenregel anwenden'],
  'Definition „oder eine Regel dazu auswählen“; 2015-OS-B1g lässt die wahre Aussage zu plus mal minus ankreuzen.')
T('rationale-zahlen', '4.2', 'Plus- und Minusklammer auflösen', ['Term mit Klammern und Potenzen vereinfachen'],
  '2022-GYM-B2b: −2 · (a + 4,5) = −2a − 9 beim Vereinfachen.')
T('rationale-zahlen', '4.3', 'Termwert für gegebene Werte, auch Bruchterm (a + b) : c', ['Termwert berechnen'],
  'Bruchterme (a + b)/c in 2021-OS-B1g und 2016-OS-B1i, (a − b) : (2a + b) in 2019-GYM-B1d.')
T('rationale-zahlen', '4.4', 'Kontostand nach mehreren Buchungen', ['Endwert linearer Veränderung berechnen'],
  'Kontostand aus Anfangsguthaben und gleichen Buchungen: 1 472 € + 12 · 22 € in 2022-OS-K6a (Definition nennt Sparen).')
T('rationale-zahlen', '4.6', 'Ausgangswert aus Differenz („8 512 mehr als“)', ['Ausgangswert aus Differenz berechnen'],
  'Definition „x mehr/weniger als“ mit Umkehroperation; 2017-OS-K2a (682 069 − 8 512).')
T('rationale-zahlen', '4.7', 'günstigste Preiskombination (Vorrat, Niveau III)', ['Günstigste Preiskombination bestimmen'],
  '2016-OS-K2d: Eintrittspreise mit Familienkarte, Großeltern-Enkel-Ticket und Altersgrenzen, Niveau III.')

# ==== zinsrechnung ====
U('zinsrechnung', 2, ['Guthabentabelle mit Zinsen ergänzen', 'Zinseszins Endkapital berechnen'])
T('zinsrechnung', '1.1', 'Kapital, Zinssatz und Zinsen im Text finden und den Prozentbegriffen zuordnen (Kapital = Grundwert, Zinssatz = Prozentsatz, Zinsen = Prozentwert)', ['Prozentwert berechnen', 'Prozentsatz berechnen'],
  'Vorstufe der Zins-Originale: vor der Rechnung ist das Kapital als Grundwert und der Zinssatz als Prozentsatz zu erkennen (2015-OS-B1e, Fehlerquelle 408 €; 2014-OS-B1e).')
T('zinsrechnung', '1.2', 'Jahreszinsen aus Kapital und Zinssatz: Prozentsatz als Dezimalzahl mal Kapital (400 € zu 2 %: 400 · 0,02 = 8 €; P10-Form) oder 1 %-Weg (ein Prozent von 400 € sind 4 €, zwei Prozent 8 €)', ['Prozentwert berechnen'],
  'Definition „auch Jahreszinsen aus Kapital und Zinssatz“; 2015-OS-B1e (400 € · 0,02 = 8 €).')
T('zinsrechnung', '1.3', 'Guthaben nach einem Jahr: Kapital plus Zinsen (408 € – nicht mit den Zinsen verwechseln)', ['Wert nach prozentualer Erhöhung berechnen', 'Guthabentabelle mit Zinsen ergänzen'],
  'Kapital plus Zinsen ist der erhöhte Wert (Definition „neuen Wert nach Erhöhung um einen Prozentsatz“) und der Rechenschritt „altes Guthaben + Zinsen“ der Tabelle in 2014-OS-K3b.')
T('zinsrechnung', '1.4', 'Zinssatz aus Zinsen und Kapital: Zinsen geteilt durch Kapital, als Prozent schreiben (230 € von 10 000 €: 230 : 10 000 = 0,023 = 2,3 %; P10-Form)', ['Prozentsatz berechnen'],
  'Definition „auch Zinssatz aus Kapital und Jahreszinsen“; 2014-OS-B1e (230 : 10 000 = 2,3 %).')
T('zinsrechnung', '1.5', 'Kapital aus Zinsen und Zinssatz (1 %-Weg rückwärts: 45 € sind 3 % → 1 % = 15 € → 1500 €)', ['Grundwert berechnen'],
  'Das Kapital ist der Grundwert (Definition „aus Prozentwert und Prozentsatz den Grundwert“); kein Original im Kontext Zinsen.')
T('zinsrechnung', '1.6', 'Nachweis „stimmt der Zinssatz?“ in einer Tabelle (4,00 € Zinsen bei 200 € Guthaben sind 2 %; P10-Form 2014-OS-K3a)', ['Prozentwert berechnen', 'Prozentsatz berechnen'],
  '2014-OS-K3a: Haupttyp Prozentwert (200 · 0,02 = 4,00 €), alternativ 4 : 200 = 2 %.')
T('zinsrechnung', '1.7', 'Zinsen für mehrere Jahre ohne Zinseszins: Jahreszins mal Jahre (Kredit, Vergleich mit Einheit 2)', ['Prozentwert berechnen', 'Endwert linearer Veränderung berechnen'],
  'Jahreszins als Prozentwert, jedes Jahr gleich: Definition „Anfangswert plus … n-fache konstante Änderung (Sparen …)“ wie in 2022-OS-K6a; kein Original mit einfacher Verzinsung über Jahre.')
T('zinsrechnung', '1.8', 'Kredit: Zinsen als Kosten, Rückzahlung = Kreditsumme plus Zinsen', ['Prozentwert berechnen', 'Wert nach prozentualer Erhöhung berechnen'],
  'Kontextvariante: Zinsen als Prozentwert, Rückzahlung als um den Zinssatz erhöhter Betrag; kein Original im Kontext Kredit.')
T('zinsrechnung', '2.1', 'Zinsen ans Guthaben anhängen, neues Guthaben nach einem Jahr (200 € → 204 €)', ['Guthabentabelle mit Zinsen ergänzen', 'Zinseszins Endkapital berechnen', 'Wert nach prozentualer Erhöhung berechnen'],
  'Erster Schritt der Tabelle in 2014-OS-K3b und des Rechenwegs „Jahr für Jahr“ in 2014-OS-K3c; Definition „neuen Wert nach Erhöhung um einen Prozentsatz“.')
T('zinsrechnung', '2.2', 'Zinsen im zweiten Jahr vom neuen Guthaben (204 · 0,02 = 4,08 €), Guthaben nach zwei Jahren Schritt für Schritt', ['Guthabentabelle mit Zinsen ergänzen', 'Zinseszins Endkapital berechnen'],
  'Zinsen vom neuen Guthaben: 824,32 · 0,02 in 2014-OS-K3b (Fehlerquelle vom alten Guthaben); Definition Zinseszins „oder schrittweise“.')
T('zinsrechnung', '2.3', 'Guthabentabelle mit den Spalten Zinsen, Einzahlung und Guthaben um eine Zeile fortschreiben (Zinsen = Zinssatz vom Guthaben der Vorzeile; Guthaben = altes Guthaben + Zinsen + Einzahlung)', ['Guthabentabelle mit Zinsen ergänzen'],
  'Definition „Guthaben = altes Guthaben + Zinsen + Einzahlung, Zinsen = Zinssatz vom Guthaben“; 2014-OS-K3b.')
T('zinsrechnung', '2.4', 'zwei fehlende Felder in einer gegebenen Tabelle ergänzen, Kontrolle über die nächste gegebene Zeile (P10-Form 2014-OS-K3b)', ['Guthabentabelle mit Zinsen ergänzen'],
  '2014-OS-K3b: zwei Felder ergänzen, Kontrolle an 1040,81 € in der nächsten Zeile.')
T('zinsrechnung', '2.5', 'Wachstumsfaktor: „plus 2 %“ ist „mal 1,02“, q = 1 + p/100', ['Zinseszins Endkapital berechnen', 'Wert nach prozentualer Erhöhung berechnen', 'Wachstumstabelle ergänzen', 'Exponentialfunktion aufstellen'],
  'q = 1,03 in 2014-OS-K3c, Definition „(Wachstumsfaktor)“ mit 3,50 · 1,2 in 2024-OS-B1e, Voraussetzung „Prozentsatz in Wachstumsfaktor umrechnen“ in 2026-FOR-K7a und 13 % Abnahme als 0,87 in 2017-OS-K7c.')
T('zinsrechnung', '2.6', 'Endkapital nach n Jahren: Startkapital mal q hoch n mit dem Taschenrechner (1 000 € zu 3 % über 5 Jahre: 1000 · 1,03⁵ ≈ 1 159,27 €; P10-Form 2014-OS-K3c) oder Jahr für Jahr', ['Zinseszins Endkapital berechnen'],
  'Definition „als K · q^n (oder schrittweise)“; 2014-OS-K3c (1000 · 1,03⁵).')
T('zinsrechnung', '2.7', 'einfache Verzinsung und Zinseszins nebeneinander (1 150 € gegen 1 159,27 €)', ['Zinseszins Endkapital berechnen'],
  '2014-OS-K3c: 1 159,27 € statt der einfachen Verzinsung 1 150 € (Fehlerquelle und Bemerkung des Originals).')
T('zinsrechnung', '2.9', 'Guthaben nach n Jahren mit jährlicher Einzahlung (Tabelle statt Formel)', ['Guthabentabelle mit Zinsen ergänzen'],
  'Definition „mit jährlichen Zinsen, Einzahlungen und Guthaben … fortschreiben“; 2014-OS-K3b (Einzahlung je 200 €).')
T('zinsrechnung', '2.11', 'Laufzeit für eine Verdopplung durch Probieren mit der Tabelle oder 72er-Regel (Vorrat)', ['Verdopplungs- oder Halbwertszeit bestimmen', 'Zeitpunkt für Schwellenwert bei Wachstum bestimmen'],
  'Kontextvariante: Verdopplung bei 3 % im Jahr in 2020-OS-K4b, schrittweise mal 1,08 bis zur Schwelle in 2018-OS-K2c.')
T('zinsrechnung', '2.12', 'Ratenkauf und Kredit mit Zinseszins (Vorrat, Verbrauchersicht)', ['Zinseszins Endkapital berechnen'],
  'Kontextvariante von K · qⁿ: 2017-GYM-K5a (Miete mit jährlich 1,1 % Steigerung, 310 € · 1,011⁵); kein Original zu Ratenkauf.')

# ==== potenzen-wurzeln ====
U('potenzen-wurzeln', 1, ['Exponent einer Potenz bestimmen'])
U('potenzen-wurzeln', 2, ['Zehnerpotenzschreibweise umwandeln', 'Große Zahl mit Zehnerpotenz multiplizieren'])
U('potenzen-wurzeln', 3, ['Wurzel eines Quadrats berechnen'])
T('potenzen-wurzeln', '1.1', 'Potenz als Malkette schreiben (3⁴ = 3 · 3 · 3 · 3) und Malkette als Potenz (2 · 2 · 2 · 2 · 2 = 2⁵)', ['Exponent einer Potenz bestimmen'],
  '2020-OS-B1h: 16 als Malkette 2 · 2 · 2 · 2, also x = 4.')
T('potenzen-wurzeln', '1.3', 'Potenz von Produkt unterscheiden und beide ausrechnen (4³ = 64, 4 · 3 = 12)', ['Exponent einer Potenz bestimmen', 'Zahlen in verschiedenen Darstellungen vergleichen'],
  'Die Fehlerquellen „16 : 2 = 8“ (2020-OS-B1h) und „256 : 4 = 64“ (2024-OS-B1g) verwechseln Potenz und Produkt; 2019-OS-B1d verlangt 4³ = 64 ausgerechnet.')
T('potenzen-wurzeln', '1.4', 'Quadratzahlen bis 20² aus dem Kopf, Kubikzahlen bis 10³', ['Wurzel eines Quadrats berechnen', 'Quadratseite aus Fläche berechnen', 'Zahlen in verschiedenen Darstellungen vergleichen'],
  '(−4)² = 16 in 2015-OS-B1j, √36 = 6 in 2020-OS-B1d und die Kubikzahl 4³ = 64 in 2019-OS-B1d.')
T('potenzen-wurzeln', '1.5', 'Potenzwert mit dem Taschenrechner (Tasten x² und ^, Klammern bei negativer Basis)', ['Zinseszins Endkapital berechnen', 'Funktionswert berechnen', 'Wahrscheinlichkeit mehrstufig unabhängig'],
  'Voraussetzung „Potenz mit Taschenrechner“: 1,03⁵ in 2014-OS-K3c, 1,03¹⁴ in 2020-OS-K4c, 1,019¹⁴ in 2026-FOR-K7c (Nebentyp) und 0,985⁵ in 2025-GYM-K6a.')
T('potenzen-wurzeln', '1.6', 'Potenz mit negativer Basis: Vorzeichen aus gerader oder ungerader Hochzahl ((−3)⁴ = 81, (−3)³ = −27), Klammer gegen kein Klammer (−3⁴ = −81)', ['Wurzel eines Quadrats berechnen', 'Punktprobe durchführen', 'Termwert berechnen', 'Zahlen in verschiedenen Darstellungen vergleichen'],
  '(−4)² in 2015-OS-B1j, −(−3)² in 2014-OS-K7a (Voraussetzung „Potenz mit negativer Basis“), (−5)² in 2022-GYM-B2a und −10³ ohne Klammer in 2017-OS-B1e.')
T('potenzen-wurzeln', '1.7', 'Potenz einer Dezimalzahl (0,4² = 0,16, 1,5³ = 3,375) und eines Bruchs ((2/3)² = 4/9)', ['Zahlen in verschiedenen Darstellungen vergleichen', 'Wahrscheinlichkeit mehrstufig unabhängig'],
  '0,4² = 0,16 in 2023-OS-B1f und die Brüche (1/2)², (3/8)², (1/8)² in 2014-OS-K6c.')
T('potenzen-wurzeln', '1.8', 'zwei Potenzen vergleichen, indem beide ausgerechnet werden (2⁸ gegen 3⁵)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  'Definition „… Potenzschreibweise in dieselbe Form bringen und ordnen“; 2019-OS-B1d (4³, 8⁴, 2⁸ ausrechnen).')
T('potenzen-wurzeln', '1.9', 'Potenzen ordnen, größte oder kleinste unterstreichen (P10-Form)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2019-OS-B1d: die größte von drei Potenzen unterstreichen.')
T('potenzen-wurzeln', '1.10', 'Potenz gegen Dezimalzahl und Prozent vergleichen (Vergleichszeichen eintragen)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '0,4² gegen 44 % in 2023-OS-B1f und 2⁻⁵ gegen 0,25 in 2022-OS-B1j.')
T('potenzen-wurzeln', '1.11', 'Exponent bestimmen durch wiederholtes Malnehmen (2^x = 16: 2, 4, 8, 16 → x = 4; P10-Form)', ['Exponent einer Potenz bestimmen', 'Parameter einer Wurzelfunktion aus einem Punkt bestimmen'],
  'Definition „durch Probieren“ (2020-OS-B1h, 2024-OS-B1g); 2^n = 8 in 2020-GYM-K3a.')
T('potenzen-wurzeln', '1.12', 'Exponent bestimmen durch Zerlegen (256 = 4 · 4 · 4 · 4)', ['Exponent einer Potenz bestimmen'],
  'Definition „durch Probieren oder Zerlegen“; 2024-OS-B1g (256 als Viererpotenz).')
T('potenzen-wurzeln', '1.13', 'Exponent mit Basis 10 (10^x = 100 000; Brücke zu Einheit 2)', ['Exponent einer Potenz bestimmen', 'Zehnerpotenzschreibweise umwandeln'],
  'Definition „a^x = b“ mit a = 10; 100 000 = 10⁵ in 2017-OS-B1g.')
T('potenzen-wurzeln', '1.14', 'Potenz mit negativem Exponenten als Bruch und als Dezimalzahl (2⁻³ = 1/8 = 0,125), hoch null', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2022-OS-B1j: 2⁻⁵ = 1/32 = 0,03125 (Fehlerquelle −32).')
T('potenzen-wurzeln', '1.15', 'negative Potenz gegen Dezimalzahl vergleichen (P10-Form)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2022-OS-B1j: Vergleichszeichen zwischen 2⁻⁵ und 0,25.')
T('potenzen-wurzeln', '2.1', 'Zehnerpotenz ausschreiben (10⁶ = 1 000 000) und Zahl als Zehnerpotenz schreiben (100 000 = 10⁵; P10-Form)', ['Zehnerpotenzschreibweise umwandeln'],
  '2017-OS-B1g: 100 000 als 10⁵.')
T('potenzen-wurzeln', '2.3', 'große Zahl mit 10, 100, 1000 vervielfachen: Nullen anhängen, Ergebnis ausgeschrieben (P10-Form)', ['Große Zahl mit Zehnerpotenz multiplizieren'],
  'Definition „mit 10, 100 oder 1000 vervielfachen (Nullen anhängen)“; 2015-OS-K3a.')
T('potenzen-wurzeln', '2.4', 'Zahl in Zehnerpotenzschreibweise a · 10ⁿ mit a zwischen 1 und 10 schreiben (Komma setzen, Stellen zählen)', ['Zehnerpotenzschreibweise umwandeln'],
  'Definition „Eine Zahl in der Form a · 10^n schreiben“; 2025-OS-B1d (850 000 = 8,5 · 10⁵). 2025-OS-B1d: Komma in 8,5 um fünf Stellen, Fehlerquelle Nullen gezählt.')
T('potenzen-wurzeln', '2.5', 'fehlenden Exponenten in „a · 10^□“ eintragen (P10-Form)', ['Zehnerpotenzschreibweise umwandeln'],
  'Definition „den fehlenden Exponenten angeben“; 2025-OS-B1d. Zweite Hälfte desselben Typs „fehlenden Exponenten in a · 10^□ eintragen“, die die Liste am Malpunkt trennt; 2025-OS-B1d.')
T('potenzen-wurzeln', '2.6', 'Zehnerpotenzschreibweise ausschreiben: Komma nach rechts, Nullen auffüllen (P10-Form)', ['Zehnerpotenzschreibweise umwandeln'],
  'Definition „als Dezimalzahl ausschreiben“; 2016-OS-B1h (8,5 · 10⁵ = 850 000).')
T('potenzen-wurzeln', '2.7', 'passende ausgeschriebene Zahl unter drei Angeboten ankreuzen (P10-Form)', ['Zehnerpotenzschreibweise umwandeln'],
  '2015-OS-K3b: zu 9,46 · 10¹² die passende von drei ausgeschriebenen Zahlen ankreuzen.')
T('potenzen-wurzeln', '2.8', 'kleine Zahl mit negativem Exponenten: Komma nach links, Nullen vorn (2,1 · 10⁻⁴ = 0,00021; P10-Form)', ['Zehnerpotenzschreibweise umwandeln'],
  '2019-OS-B1j: 2,1 · 10⁻⁴ = 0,00021.')
T('potenzen-wurzeln', '2.9', 'Zahl kleiner als eins in Zehnerpotenzschreibweise schreiben (0,00035 = 3,5 · 10⁻⁴)', ['Zehnerpotenzschreibweise umwandeln'],
  'Definition „Eine Zahl in der Form a · 10^n schreiben“ ohne Beschränkung des Exponenten; kein Original mit negativem Exponenten in dieser Richtung.')
T('potenzen-wurzeln', '2.10', 'Zahlen in Zehnerpotenzschreibweise vergleichen und ordnen (erst Exponent, dann Faktor)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  'Definition „… Potenzschreibweise in dieselbe Form bringen und ordnen“; 2017-OS-B1e (−10³ und −10² unter Dezimalzahlen).')
T('potenzen-wurzeln', '2.11', 'negative Zehnerpotenzen auf der Zahlengerade ordnen (−10³ gegen −0,01; P10-Form)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2017-OS-B1e: die kleinste von −0,01; −10³; −10²; −0,1.')
T('potenzen-wurzeln', '2.13', 'gerundeter Wert in Zehnerpotenzschreibweise (9 460 730 472 581 km ≈ 9,46 · 10¹² km)', ['Dauer aus Menge und Rate berechnen'],
  '2015-OS-K3c: Ergebnis ≈ 1,34 · 10¹⁰ s als gerundeter Wert in Zehnerpotenzschreibweise.')
T('potenzen-wurzeln', '2.14', 'Sachaufgabe aus Astronomie oder Mikrowelt (Lichtjahr, Atommasse; Einheit mitführen)', ['Große Zahl mit Zehnerpotenz multiplizieren', 'Zehnerpotenzschreibweise umwandeln', 'Dauer aus Menge und Rate berechnen'],
  'Stamm „Sterne“ 2015: Lichtjahre in km (2015-OS-K3a), 9,46 · 10¹² ausgeschrieben (2015-OS-K3b) und Lichtlaufzeit (2015-OS-K3c).')
T('potenzen-wurzeln', '2.15', 'Zehnerpotenzen multiplizieren und dividieren (Exponenten addieren, subtrahieren; Vorrat, Nebenleistung 2015-OS-K3c)', ['Dauer aus Menge und Rate berechnen'],
  '2015-OS-K3c: 4,03 · 10¹⁵ : (3 · 10⁵), Voraussetzung „Zehnerpotenzen dividieren“.')
T('potenzen-wurzeln', '3.1', 'Quadratzahl erkennen und Wurzel im Kopf (√169 = 13; Quadratzahlen bis 20²)', ['Wurzel eines Quadrats berechnen', 'Quadratseite aus Fläche berechnen', 'Argument zu Funktionswert berechnen', 'Schnittpunkte Gerade und Parabel berechnen'],
  'Wurzel aus einer Quadratzahl: √16 in 2015-OS-B1j und in der p-q-Formel von 2023-OS-K4c, √36 in 2020-OS-B1d und √9 in 2024-OS-K3d.')
T('potenzen-wurzeln', '3.2', 'Wurzel als Umkehrung: „welche Zahl mal sich selbst gibt …“', ['Wurzel eines Quadrats berechnen', 'Quadratseite aus Fläche berechnen'],
  'Vorstufe: Definition „Quadrat zuerst, Wurzel ist nie negativ“ (2015-OS-B1j) und „Seitenlänge eines Quadrats als Wurzel aus dem Flächeninhalt“ (2020-OS-B1d, 6 · 6 = 36).')
T('potenzen-wurzeln', '3.3', 'Wurzel mit dem Taschenrechner, Anzeige ablesen, auf zwei Dezimalen runden (√7 ≈ 2,65)', ['Pythagoras Kathete', 'Pythagoras Hypotenuse', 'Radius eines Zylinders aus Volumen berechnen', 'Nullstellen quadratische Funktion berechnen'],
  'Voraussetzung „Wurzel ziehen“ mit gerundetem Ergebnis: √855 ≈ 29,2 (2026-FOR-K4a), √29 156 ≈ 170,8 (2025-OS-K4a), r ≈ 4,40 (2022-OS-K2d) und 3 ± √2 ≈ 1,59 und 4,41 (2025-OS-K5c).')
T('potenzen-wurzeln', '3.4', 'Wurzel zwischen zwei Nachbar-Quadratzahlen abschätzen (√50 liegt zwischen 7 und 8)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  'Voraussetzung „Wurzel abschätzen“ in 2015-OS-B1c und 2014-OS-B1h.')
T('potenzen-wurzeln', '3.5', 'Wurzel mit Dezimalzahl und Bruch vergleichen (√2 gegen 1,4; P10-Form)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '√2 gegen 3/2 in 2015-OS-B1c und gegen 1,4 in 2014-OS-B1h.')
T('potenzen-wurzeln', '3.6', 'Zahlen mit Wurzel aufsteigend ordnen (P10-Form)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2014-OS-B1h: −1/2; 1,4; −0,512; √2 aufsteigend ordnen.')
T('potenzen-wurzeln', '3.7', 'Wurzel eines Quadrats: erst das Quadrat, dann die Wurzel (√((−4)²) = √16 = 4; die richtige von drei Aussagen ankreuzen; P10-Form)', ['Wurzel eines Quadrats berechnen'],
  'Definition „Wert eines Terms wie √((−4)²) bestimmen oder die richtige Aussage dazu auswählen“; 2015-OS-B1j.')
T('potenzen-wurzeln', '3.9', 'Wurzel aus einer negativen Zahl: kein Wert (√(−9) gegen −√9)', ['Lösbarkeit quadratischer Gleichung beurteilen', 'Wurzel eines Quadrats berechnen'],
  'Gleichung ohne Lösung wie x² = −1 in 2021-OS-K7c; in 2015-OS-B1j ist „nicht definiert“ zu verwerfen, weil (−4)² nicht negativ ist.')
T('potenzen-wurzeln', '3.10', 'Wurzel aus Dezimalzahl und Bruch (√0,25 = 0,5, √(1/4) = 1/2; nicht „halbieren“)', ['Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen'],
  '2025-GYM-K6c: √0,9801 = 0,99, Fehlerquelle „0,9801 durch 2 teilen statt die Quadratwurzel zu ziehen“.')
T('potenzen-wurzeln', '3.11', 'Quadratseite aus dem Flächeninhalt (a = √A; Typ in flaechen.md Einheit 1)', ['Quadratseite aus Fläche berechnen', 'Grundkante aus Volumen berechnen'],
  'Definition „Seitenlänge eines Quadrats als Wurzel aus dem Flächeninhalt“ (2020-OS-B1d); a = √62,5 für die quadratische Grundfläche in 2017-GYM-K4c.')
T('potenzen-wurzeln', '3.12', 'Wurzel als letzter Schritt einer Formel: erst den Term unter der Wurzel ausrechnen, dann die Wurzel (Hypotenuse, Zylinderradius r = √(V : (π · h)), p-q-Formel)', ['Pythagoras Hypotenuse', 'Pythagoras Kathete', 'Radius eines Zylinders aus Volumen berechnen', 'Nullstellen quadratische Funktion berechnen'],
  'Die drei Beispiele des Typs: √(170² + 16²) in 2025-OS-K4a, √(384² − 255²) in 2024-OS-K6a, r = √(425 : (π · 7)) in 2022-OS-K2d und x = 3 ± √(9 − 7) in 2025-OS-K5c.')
T('potenzen-wurzeln', '3.13', 'Kubikwurzel (³√27 = 3; Vorrat)', ['Parameter einer Wurzelfunktion aus einem Punkt bestimmen', 'Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen'],
  '³√8 = 2 in 2020-GYM-K3a und ³√x als Umkehrung von x³ in 2020-GYM-K3b.')

# ==== reelle-zahlen ====
T('reelle-zahlen', '1.3', 'Wurzel rational oder irrational: Radikand Quadratzahl (√49 = 7) oder nicht (√50 ≈ 7,07 – kein Bruch)', ['Nullstellen quadratische Funktion berechnen', 'Argument zu Funktionswert berechnen', 'Schnittpunkte Gerade und Parabel berechnen'],
  'Ob die Wurzel der p-q-Formel aufgeht, entscheidet über exakte oder genäherte Lösungen: √16 in 2023-OS-K4c und √9 in 2024-OS-K3d gegen √2 in 2025-OS-K5c.')
T('reelle-zahlen', '1.4', 'irrationale Zahlen nennen (√2, √3, √5, π) und mit dem Taschenrechner den Näherungswert ablesen', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  'Näherungswert √2 ≈ 1,41 in 2015-OS-B1c und ≈ 1,414 in 2014-OS-B1h.')
T('reelle-zahlen', '1.7', 'irrationale Zahl auf der Zahlengeraden zwischen zwei Zehntel einordnen', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2014-OS-B1h: √2 ≈ 1,414 liegt zwischen 1,4 und 1,5 und steht darum hinter 1,4.')
T('reelle-zahlen', '1.8', 'reelle Zahlen vergleichen und ordnen über Näherungswerte (√10, 3,2, 3 1/5)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2015-OS-B1c und 2014-OS-B1h ordnen √2 über den Näherungswert zwischen Brüche und Dezimalzahlen.')
T('reelle-zahlen', '1.9', 'exakt und gerundet: Wurzel als exaktes Ergebnis stehen lassen, dann Näherungswert mit ≈ (P10-Form 2025-OS-K5c „x = 3 ± √2“)', ['Nullstellen quadratische Funktion berechnen', 'Streckenlänge aus Koordinaten berechnen'],
  'P10-Form 2025-OS-K5c (x = 3 ± √2 und N1(1,59|0)), ebenso 2017-OS-K5d (Nebentyp) und BC = √20 ≈ 4,47 in 2019-OS-K2d.')
T('reelle-zahlen', '2.2', 'Quotient gleicher Basen: Exponenten subtrahieren (5⁶ : 5² = 5⁴; 3² : 3² = 3⁰ = 1; 2³ : 2⁵ = 2⁻²)', ['Dauer aus Menge und Rate berechnen'],
  '2015-OS-K3c: 10¹⁵ : 10⁵ = 10¹⁰, Fehlerquelle 10³.')
T('reelle-zahlen', '2.9', 'Potenzen mit negativem Exponenten in Brüche und zurück (Blatt 0 aus potenzen-wurzeln.md; LISUM-PH)', ['Zahlen in verschiedenen Darstellungen vergleichen'],
  '2022-OS-B1j: 2⁻⁵ = 1 : 2⁵ = 1/32.')
T('reelle-zahlen', '3.5', 'Summe unter der Wurzel erst ausrechnen (√(9 + 16) = 5, nicht 3 + 4; Pythagoras-Form)', ['Pythagoras Hypotenuse', 'Pythagoras Kathete', 'Streckenlänge aus Koordinaten berechnen', 'Mantellinie Kegel bestimmen'],
  'Summe oder Differenz unter der Wurzel zuerst: √(170² + 16²) (2025-OS-K4a), √(32² − 13²) = √855 (2026-FOR-K4a), BC² = 2² + 4² = 20 (2019-OS-K2d) und s = √(r² + h²) (2018-OS-K6d).')
T('reelle-zahlen', '3.7', 'Wurzel als Potenz mit Exponent 1/2 (√a = a^(1/2)), Taschenrechner mit Klammer (8^(1/3))', ['Parameter einer Wurzelfunktion aus einem Punkt bestimmen'],
  '2020-GYM-K3a rechnet ⁿ√8 als 8^(1/n) = 2.')
T('reelle-zahlen', '3.8', 'n-te Wurzel als a^(1/n), Kubikwurzel (³√8 = 2, ³√27 = 3)', ['Parameter einer Wurzelfunktion aus einem Punkt bestimmen', 'Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen'],
  '2020-GYM-K3a (8^(1/n) = 2, also ³√8 = 2) und 2020-GYM-K3b (³√x mit der Umkehrung x³).')

# ==== einheiten ====
U('einheiten', 1, ['Größen vergleichen', 'Längeneinheit mit Faktor umrechnen'])
U('einheiten', 2, ['Zeiteinheiten umrechnen', 'Uhrzeit aus Startzeit und Dauer berechnen'])
U('einheiten', 3, ['Portionen aus Gesamtmenge berechnen'])
U('einheiten', 4, ['Volumen aus Masse und Dichte berechnen', 'Masse aus Volumen und Dichte berechnen', 'Materialbedarf aus Fläche berechnen', 'Fehler in Rechnung erklären und korrigieren'])
T('einheiten', '1.1', 'Einheiten der Länge, der Masse und des Geldes der Größe nach ordnen', ['Größen vergleichen'],
  'Vorstufe des Vergleichens: welche Einheit die größere ist, legt in 2019-OS-B1b (0,06 m □ 60 cm) und 2026-FOR-B1d (3,5 m □ 35 cm) die Richtung der Umrechnung fest.')
T('einheiten', '1.3', 'in die Nachbareinheit umrechnen, größer nach kleiner (mal)', ['Größen vergleichen', 'Strecke aus Teilstrecken berechnen', 'Fehler in Rechnung erklären und korrigieren'],
  'Grundschritt der Umrechnungen Meter in Zentimeter in 2019-OS-B1b, 2026-FOR-B1d und 2018-OS-B1b (Definition „nach Umrechnung in eine gemeinsame Einheit“); als einzelner Schritt Euro in Cent in 2014-OS-K4e (585 € = 58 500 ct).')
T('einheiten', '1.4', 'in die Nachbareinheit umrechnen, kleiner nach größer (geteilt)', ['Strecke aus Teilstrecken berechnen', 'Dauer aus Menge und Rate berechnen'],
  '2014-OS-K2a rechnet 2800 m in 2,8 km um (Definition „nach Umrechnung in eine gemeinsame Einheit (cm, m, km)“), 2014-OS-K2c 2500 m in 2,5 km vor der Division durch 5 km/h.')
T('einheiten', '1.5', 'über zwei Stufen umrechnen (Millimeter in Meter)', ['Größen vergleichen', 'Strecke aus Teilstrecken berechnen', 'Materialbedarf aus Längen berechnen'],
  'Meter in Zentimeter über zwei Stufen in 2019-OS-B1b (0,06 m = 6 cm), 2026-FOR-B1d (3,5 m = 350 cm) und 2018-OS-B1b (5 m = 500 cm); Millimeter in Meter in 2016-GYM-K3a (180 mm = 0,18 m).')
T('einheiten', '1.6', 'Kilometer und Meter (Umrechnungszahl tausend)', ['Strecke aus Teilstrecken berechnen', 'Dauer aus Menge und Rate berechnen'],
  '2014-OS-K2a (2800 m + 1,5 km = 4,3 km, Fehlerquelle 2801,5) und 2014-OS-K2c (2500 m = 2,5 km bei 5 km/h).')
T('einheiten', '1.8', 'Komma setzen: Größe in der Stellenwerttafel lesen', ['Größen vergleichen'],
  'Die Hürde beider Originale ist die Kommastelle: 2019-OS-B1b (Fehlerquelle 0,06 m als 60 cm) und 2026-FOR-B1d (Fehlerquelle 3,5 m als 35 cm).')
T('einheiten', '1.9', 'zwei Größen mit verschiedenen Einheiten vergleichen und das Zeichen setzen (P10-Form)', ['Größen vergleichen'],
  'Definition „Zwei Größen mit verschiedenen Einheiten vergleichen und <, = oder > setzen“; 2019-OS-B1b, 2026-FOR-B1d.')
T('einheiten', '1.11', 'Umrechnen mit gegebenem Faktor bei nichtmetrischen Einheiten (Fuß, Meile, Zoll; P10-Form)', ['Längeneinheit mit Faktor umrechnen'],
  'Definition „mit gegebenem Umrechnungsfaktor (Fuß, Meile, Zoll) in Meter oder Zentimeter umrechnen“; 2016-OS-K3a (7 · 0,305 m).')
T('einheiten', '1.12', 'Nachweis einer vorgegebenen Länge mit dem Faktor (P10-Form)', ['Längeneinheit mit Faktor umrechnen', 'Behauptung prüfen'],
  '2016-OS-K3a: die vorgegebene Angabe d ≈ 2,14 m mit 7 · 0,305 m = 2,135 m nachweisen (Nebentyp „Behauptung prüfen“).')
T('einheiten', '1.13', 'Größen mit gleicher Einheit addieren und subtrahieren', ['Strecke aus Teilstrecken berechnen', 'Materialbedarf aus Längen berechnen'],
  'Definition „als Summe oder Differenz gegebener Teilstrecken“: 2018-OS-B1b (500 cm − 5 · 30 cm) und 2014-OS-K2a (2,8 km + 1,5 km); 2016-GYM-K3a addiert 60 + 100 + 20 mm.')
T('einheiten', '2.1', 'Zeiteinheiten nennen und ordnen', ['Zeiteinheiten umrechnen'],
  'Vorstufe: die Zeiteinheiten mit ihren Umrechnungszahlen trägt jede Umrechnung der Definition „Zeitangaben zwischen h, min und s umrechnen“.')
T('einheiten', '2.2', 'Minuten in Stunden und Stunden in Minuten', ['Zeiteinheiten umrechnen'],
  'Definition „Zeitangaben zwischen h, min und s umrechnen“; Grundfall der Originale 2018-OS-B1e, 2025-OS-B1b und 2024-OS-B1a.')
T('einheiten', '2.3', 'Sekunden in Minuten', ['Zeiteinheiten umrechnen', 'Dauer aus Menge und Rate berechnen'],
  '2024-OS-K6c: 120 s = 2 min als Nebentyp „Zeiteinheiten umrechnen“ im Haupttyp „Dauer aus Menge und Rate berechnen“ (Definition „in die verlangte Zeiteinheit umrechnen“).')
T('einheiten', '2.4', 'Dezimalstunden in Minuten (P10-Form: eineinhalb Stunden, drei Komma zwei fünf Stunden)', ['Zeiteinheiten umrechnen', 'Dauer aus Menge und Rate berechnen'],
  'Definition „auch aus Dezimalstunden“: 2018-OS-B1e (3,5 h), 2025-OS-B1b (1,5 h), 2024-OS-B1a (3,25 h); dazu 2014-OS-K2c (0,5 h = 30 min).')
T('einheiten', '2.5', 'Minuten als Dezimalstunde schreiben', ['Zeiteinheiten umrechnen'],
  'Andere Richtung derselben Definition „Zeitangaben zwischen h, min und s umrechnen“; kein Original in dieser Richtung.')
T('einheiten', '2.7', 'Endzeit aus Startzeit und Dauer mit Übertrag bei sechzig Minuten (P10-Form)', ['Uhrzeit aus Startzeit und Dauer berechnen'],
  'Definition „die End- oder Startzeit bestimmen, mit Übertrag bei 60 Minuten“; 2021-OS-B1a (11:38 Uhr + 2 h 35 min = 14:13 Uhr).')
T('einheiten', '2.8', 'Startzeit aus Endzeit und Dauer', ['Uhrzeit aus Startzeit und Dauer berechnen'],
  'Definition „die End- oder Startzeit bestimmen“; kein Original in dieser Richtung.')
T('einheiten', '2.9', 'Dauer mit Pause (zwei Abschnitte addieren)', ['Uhrzeit aus Startzeit und Dauer berechnen'],
  '2014-OS-K2c: 11:30 Uhr + 45 min Pause + 30 min Weg = 12:45 Uhr (Nebentyp, Fehlerquelle Pause vergessen).')
T('einheiten', '2.11', 'Dauer in eine sinnvolle Einheit bringen (Sekunden in Minuten, Stunden in Tage)', ['Zeiteinheiten umrechnen', 'Dauer aus Menge und Rate berechnen'],
  '2024-OS-K6c (120 s als 2 min) und 2015-OS-K3c (1,34 · 10¹⁰ s in Jahren), beide mit „Zeiteinheiten umrechnen“ als Nebentyp.')
T('einheiten', '3.1', 'Flächeneinheiten ordnen (mm² bis km², a und ha einordnen)', ['Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen'],
  'Vorstufe von 3.2 und 3.3: das einzige Original mit Flächenumrechnung, 2016-GYM-K5b, verlangt Hektar (546 409 m² ≈ 54,6 ha).')
T('einheiten', '3.2', 'Flächeneinheit in die Nachbareinheit umrechnen', ['Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen'],
  'Teilschritt von 2016-GYM-K5b: Quadratmeter über Ar in Hektar (Fehlerquelle „ha und m² bei der Volumenrechnung nicht umrechnen“).')
T('einheiten', '3.3', 'über zwei Stufen (mm² in dm²)', ['Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen'],
  '2016-GYM-K5b rechnet 546 409 m² in 54,64 ha um, zwei Stufen mit der Umrechnungszahl hundert.')
T('einheiten', '3.4', 'Volumeneinheiten ordnen (mm³ bis m³)', ['Volumen Zylinder berechnen', 'Höhe eines Zylinders aus Volumen berechnen', 'Dauer aus Menge und Rate berechnen'],
  'Vorstufe von 3.5: die Richtung der Umrechnung in 2021-OS-K4a (cm³ in dm³), 2023-OS-K5d (1 l = 1000 cm³) und 2017-OS-K3d (m³ in l).')
T('einheiten', '3.5', 'Volumeneinheit in die Nachbareinheit umrechnen', ['Volumen Zylinder berechnen', 'Höhe eines Zylinders aus Volumen berechnen', 'Dauer aus Menge und Rate berechnen'],
  'Umrechnungszahl tausend in 2021-OS-K4a (250 998 cm³ ≈ 251 dm³, Fehlerquelle Faktor 100), 2023-OS-K5d (1 l als 1000 cm³, Fehlerquelle 100 cm³) und 2017-OS-K3d (140 m³ = 140 000 l, Fehlerquelle 1 m³ = 100 l).')
T('einheiten', '3.6', 'Liter und Kubikdezimeter, Milliliter und Kubikzentimeter gleichsetzen', ['Volumen Zylinder berechnen', 'Höhe eines Zylinders aus Volumen berechnen', 'Radius eines Zylinders aus Volumen berechnen'],
  '2021-OS-K4a („1 l = 1 dm³“), 2022-OS-K2b und 2023-OS-K5b („1 cm³ = 1 ml“), 2023-OS-K5d (1 l = 1000 cm³) und 2022-OS-K2d (425 ml als 425 cm³).')
T('einheiten', '3.7', 'Liter in Milliliter und zurück (P10-Form)', ['Portionen aus Gesamtmenge berechnen', 'Materialbedarf aus Fläche berechnen'],
  '2022-OS-B1h (1,5 l = 1500 ml, Fehlerquelle 150 ml) und 2015-OS-K6d (0,256 l = 256 ml gegen Dosen zu 375 ml).')
T('einheiten', '3.8', 'Kubikmeter in Liter (P10-Form)', ['Dauer aus Menge und Rate berechnen'],
  '2017-OS-K3d: 140 m³ = 140 000 l vor der Division durch 17 500 l je Stunde (Original hier geführt, Typ bei zuordnungen.md).')
T('einheiten', '3.9', 'Portionen aus einer Gesamtmenge nach Umrechnung (P10-Form)', ['Portionen aus Gesamtmenge berechnen'],
  'Definition „Anzahl gleicher Portionen aus Gesamtmenge und Portionsgröße berechnen, nach Umrechnung der Einheiten“; 2022-OS-B1h.')
T('einheiten', '3.13', 'Fehler finden (Flächeneinheit mit zehn statt hundert umgerechnet; Kubikmeter mit hundert statt tausend in Liter)', ['Fehler in Rechnung erklären und korrigieren'],
  'Definition „den Fehler (z. B. falscher Umrechnungsfaktor zwischen Einheiten) benennen“ – dieselbe Leistung wie in 2014-OS-K4e (Faktor 1000 statt 100), hier mit Flächen- und Volumeneinheiten.')
T('einheiten', '4.1', 'gegebene Größen vor dem Rechnen auf eine Einheit bringen', ['Portionen aus Gesamtmenge berechnen', 'Strecke aus Teilstrecken berechnen', 'Dauer aus Menge und Rate berechnen'],
  'Definitionen „nach Umrechnung der Einheiten“ (2022-OS-B1h) und „nach Umrechnung in eine gemeinsame Einheit“ (2014-OS-K2a, Fehlerquelle 2800 + 1,5); 2017-OS-K3d rechnet 140 m³ vor der Division in Liter um.')
T('einheiten', '4.2', 'Ergebnis in eine sinnvolle Einheit umrechnen (0,6 m als 60 cm angeben)', ['Länge im Maßstab umrechnen', 'Materialbedarf aus Fläche berechnen', 'Dauer aus Menge und Rate berechnen'],
  '2018-OS-K6c (0,6 m = 60 cm, Definition „mit passender Einheit“), 2015-OS-K6d (0,256 l = 256 ml) und 2024-OS-K6c (120 s = 2 min, Definition „in die verlangte Zeiteinheit umrechnen“).')
T('einheiten', '4.3', 'Masse aus Volumen und Dichte (P10-Form)', ['Masse aus Volumen und Dichte berechnen', 'Volumen zusammengesetzter Körper berechnen'],
  'Definition „Masse aus Volumen und Masse je Volumeneinheit (Dichte) berechnen“, einziges Original 2019-OS-K4c (Nebentyp); GYM-Definition „und daraus über die Dichte die Masse bestimmen“ (2016-GYM-K3b).')
T('einheiten', '4.4', 'Volumen aus Masse und Dichte durch Umstellen (P10-Form)', ['Volumen aus Masse und Dichte berechnen'],
  'Definition „durch Umstellen von ϱ = m : V“; 2016-OS-K3d (4000 : 7,8 ≈ 512,8 cm³).')
T('einheiten', '4.6', 'Masse eines Anteils (Füllgrad in Prozent) und Leermasse addieren (P10-Form)', ['Masse aus Volumen und Dichte berechnen'],
  'Definition „ggf. mit Füllgrad in Prozent und Leermasse“; 2019-OS-K4c (10 % von 1,2 m³ Wasser ≙ 120 kg, plus 200 kg).')
T('einheiten', '4.7', 'Materialbedarf aus Fläche und Ergiebigkeit, mehrere Flächen, zweiter Anstrich (P10-Form)', ['Materialbedarf aus Fläche berechnen'],
  'Definition „aus zu bearbeitender Fläche (mehrere Flächen, mehrere Anstriche) und Ergiebigkeit (m² je Liter)“; 2015-OS-K6d (4 · 0,32 m² · 2 bei 10 m² je Liter).')
T('einheiten', '4.8', 'Bedarf mit Gebindegrößen vergleichen und entscheiden (P10-Form)', ['Materialbedarf aus Fläche berechnen', 'Behauptung prüfen', 'Materialbedarf aus Längen berechnen'],
  'Definition „und mit Gebindegrößen vergleichen“; 2015-OS-K6d entscheidet mit Nebentyp „Behauptung prüfen“, ob Dose S (375 ml) reicht; 2016-GYM-K3a teilt durch die Stranglänge 6 m.')
T('einheiten', '4.9', 'Euro und Cent in einer Rechnung', ['Fehler in Rechnung erklären und korrigieren', 'Kosten aus Menge und Preis berechnen'],
  '2014-OS-K4e (585 € = 58 500 ct, dann 58 500 ct : 100 000) und 2024-OS-K2d (16 · 0,14 ct, Fehlerquelle 0,14 ct als 0,14 €).')
T('einheiten', '4.10', 'eine fremde Rechnung nachrechnen und den Einheitenfehler benennen (P10-Form)', ['Fehler in Rechnung erklären und korrigieren'],
  'Definition „In einer vorgegebenen Schülerrechnung den Fehler (z. B. falscher Umrechnungsfaktor zwischen Einheiten) benennen“; 2014-OS-K4e.')
T('einheiten', '4.11', 'die Rechnung berichtigen und die Behauptung korrigieren (P10-Form)', ['Fehler in Rechnung erklären und korrigieren', 'Behauptung prüfen'],
  'Definition „die Rechnung berichtigen und die daraus abgeleitete Behauptung korrigieren“; 2014-OS-K4e korrigiert „ca. 6 ct“ auf ca. 0,6 ct je Kilometer (Nebentyp „Behauptung prüfen“).')
T('einheiten', '4.12', 'Fehler finden (Faktor tausend statt hundert bei Euro und Cent; nur eine der beiden Größen umgerechnet)', ['Fehler in Rechnung erklären und korrigieren'],
  '2014-OS-K4e verlangt genau diesen Fehler zu benennen: 585 € als 585 000 ct, Faktor 1000 statt 100.')

# ==== flaechen ====
U('flaechen', 1, ['Umfang Rechteck berechnen', 'Rechteckseite aus Fläche berechnen', 'Rechteckseite aus Umfang berechnen', 'Quadratseite aus Fläche berechnen', 'Flächeninhalt Rechteck berechnen', 'Term zu Figur angeben'])
U('flaechen', 3, ['Flächeninhalt Dreieck berechnen', 'Grundseite aus Dreiecksfläche berechnen', 'Term zu Figur angeben'])
U('flaechen', 4, ['Flächeninhalt Trapez berechnen', 'Trapezhöhe aus Fläche berechnen', 'Umfang Trapez berechnen', 'Flächeninhalt Drachenviereck berechnen'])
U('flaechen', 5, ['Figur in Teilflächen zerlegen', 'Flächeninhalt zusammengesetzter Figur berechnen', 'Restfläche berechnen', 'Verschnitt in Prozent berechnen'])
T('flaechen', '1.1', 'Rechteck A und u aus a und b', ['Flächeninhalt Rechteck berechnen', 'Umfang Rechteck berechnen'],
  'Definitionen „Flächeninhalt eines Rechtecks aus Länge und Breite“ und „Umfang eines Rechtecks aus Länge und Breite“; 2026-FOR-B1h (u = 10 cm), A als Nebenleistung in 2017-OS-K3b und 2018-OS-K6a.')
T('flaechen', '1.2', 'Quadrat A und u aus a', ['Flächeninhalt Rechteck berechnen', 'Umfang Rechteck berechnen'],
  'Das Quadrat ist der Grundfall a = b derselben Rechteckformeln (Definitionen „aus Länge und Breite“); kein eigenes Original.')
T('flaechen', '1.3', 'Umfang eines Vielecks aus allen Seiten', ['Umfang Rechteck berechnen', 'Umfang Trapez berechnen'],
  'Der Umfang als Summe aller Seiten ist Teilschritt von 2026-FOR-B1h (u = 2 · (3,5 + 1,5)) und Schlussschritt von 2023-OS-K2c (U = 15 + 25,8 + 2s).')
T('flaechen', '1.4', 'Seite aus A und anderer Seite (A : b)', ['Rechteckseite aus Fläche berechnen'],
  'Definition „Länge oder Breite eines Rechtecks aus Flächeninhalt und der anderen Seite“; 2023-OS-B1c (42 000 : 400) und 2014-OS-K5d.')
T('flaechen', '1.5', 'Seite aus u und anderer Seite', ['Rechteckseite aus Umfang berechnen'],
  'Definition „aus Umfang und der anderen Seite durch Umstellen von u = 2a + 2b“; 2018-OS-B1f.')
T('flaechen', '1.6', 'Quadratseite als Wurzel aus A', ['Quadratseite aus Fläche berechnen'],
  'Definition „als Wurzel aus dem Flächeninhalt“; 2020-OS-B1d (√36 = 6 cm).')
T('flaechen', '1.7', 'aus Rechtecken zusammengesetzte Fläche (Summe)', ['Flächeninhalt Rechteck berechnen', 'Mantelfläche Prisma berechnen'],
  'Definition „auch als Summe mehrerer Rechtecke“; 2019-OS-K4b addiert drei gleiche Rechtecke (3 · 1,5 · 1,2), Original hier in Einheit 1, Typ bei koerper.md.')
T('flaechen', '1.8', 'Term zu Figur (Fläche oder Umfang mit Variablen)', ['Term zu Figur angeben'],
  'Definition „den Term für Flächeninhalt oder Umfang angeben“; 2019-OS-B1e und 2025-OS-B1i (Rechtecke), 2014-OS-B1g (Kreuz aus Quadraten, u = 16a).')
T('flaechen', '1.9', 'Einheit wechseln vor dem Rechnen (cm und m gemischt)', ['Rechteckseite aus Fläche berechnen'],
  '2014-OS-K5d: Rückwand in cm, Platte in m² und m (Voraussetzung „m² und cm umrechnen“, 1,65 m gegen 1,5 m).')
T('flaechen', '3.1', 'A aus g und h', ['Flächeninhalt Dreieck berechnen'],
  'Definition „Flächeninhalt eines Dreiecks aus Grundseite und Höhe“; 2015-OS-K6c, 2022-OS-K5e, 2019-OS-K4c.')
T('flaechen', '3.2', 'rechtwinklig: Katheten als g und h', ['Flächeninhalt Dreieck berechnen', 'Term zu Figur angeben', 'Grundseite aus Dreiecksfläche berechnen'],
  'Katheten als Grundseite und Höhe in 2015-OS-K5d (A = ½ · AE · DE), 2022-OS-B1e (A = d · e : 2) und 2020-OS-K7b (A = ½ · QC · BC).')
T('flaechen', '3.3', 'Höhe zur passenden Grundseite wählen (drei Höhen)', ['Flächeninhalt Dreieck berechnen', 'Grundseite aus Dreiecksfläche berechnen'],
  '2022-OS-K5e (h_c zur Seite c, Fehlerquelle „a als Höhe verwenden“) und 2020-OS-K7b (Fehlerquelle „AC statt BC als Höhe“).')
T('flaechen', '3.4', 'stumpfwinklig, Höhe außerhalb', ['Flächeninhalt Dreieck berechnen'],
  'Definition „aus Grundseite und Höhe“ ohne Einschränkung der Dreiecksform; kein Original mit Höhe außerhalb.')
T('flaechen', '3.5', 'g oder h aus A (umstellen)', ['Grundseite aus Dreiecksfläche berechnen'],
  'Definition „Grundseite oder Höhe eines Dreiecks aus Flächeninhalt und der anderen Größe durch Umstellen“; 2020-OS-K7b (QC = 2 · 90 : 12).')
T('flaechen', '3.6', 'Umfang', ['Umfang eines Dreiecks aus Koordinaten berechnen'],
  'GYM-Definition „indem die drei Seitenlängen … bestimmt und addiert werden“ (2015-GYM-K2c); der Umfang als Summe der Seiten ist deren Schlussschritt.')
T('flaechen', '3.7', 'Term zu Figur (Umfang gleichseitig 3 · a; Fläche rechtwinklig)', ['Term zu Figur angeben'],
  'Definition „den Term für Flächeninhalt oder Umfang angeben“; 2024-OS-B1c (u = 3 · a) und 2022-OS-B1e (A = d · e : 2).')
T('flaechen', '4.1', 'Trapez A aus a, c, h', ['Flächeninhalt Trapez berechnen'],
  'Definition „aus den parallelen Seiten und der Höhe“; 2023-OS-K2b.')
T('flaechen', '4.2', 'Höhe aus A und den parallelen Seiten', ['Trapezhöhe aus Fläche berechnen'],
  'Definition „aus Flächeninhalt und den parallelen Seiten durch Umstellen der Trapezformel“; 2014-OS-K5c (h = 2 · 5 225 : 190).')
T('flaechen', '4.3', 'Umfang mit gegebenen Schenkeln', ['Umfang Trapez berechnen'],
  'Vorstufe: der Schlussschritt von 2023-OS-K2c (U = 15 + 25,8 + 2s) ohne die Schenkelberechnung.')
T('flaechen', '4.4', 'Umfang mit Schenkel aus Pythagoras oder Sinus (Vorrat)', ['Umfang Trapez berechnen'],
  'Definition „dessen Schenkel erst über Trigonometrie oder Pythagoras bestimmt werden müssen“; 2023-OS-K2c.')
T('flaechen', '4.5', 'Drachen und Raute A aus e und f', ['Flächeninhalt Drachenviereck berechnen'],
  'Definition „eines Drachenvierecks oder einer Raute aus den Diagonalen“; 2025-OS-K2b.')
T('flaechen', '5.1', 'Teilflächen erkennen und benennen (Rechteck, Dreieck, Halbkreis)', ['Figur in Teilflächen zerlegen'],
  'Definition „in bekannte Teilflächen (Rechteck, Halbkreise, Dreiecke) zerlegen und diese benennen“; 2017-OS-K3a.')
T('flaechen', '5.2', 'Fläche als Summe', ['Flächeninhalt zusammengesetzter Figur berechnen'],
  'Definition „als Summe der Teilflächen“; 2017-OS-K3b (10 · 5 + π · 2,5²).')
T('flaechen', '5.3', 'Fläche durch Ergänzen (Rechteck minus Ecke)', ['Restfläche berechnen', 'Term zu Figur angeben'],
  'Ergänzen ist die Differenz zweier Flächen (Definition „Differenz der Flächeninhalte zweier Figuren“); 2023-GYM-B2a berechnet das Fünfeck als Rechteck minus Dreieck.')
T('flaechen', '5.4', 'Restfläche (Rechteck minus Kreis oder Quadrat)', ['Restfläche berechnen'],
  'Definition „Differenz der Flächeninhalte zweier Figuren (Rechteck minus Kreis)“; 2018-OS-K6a.')
T('flaechen', '5.5', 'Umfang einer zusammengesetzten Figur', ['Term zu Figur angeben'],
  '2014-OS-B1g: Umfang des Kreuzes aus Quadraten als Term (u = 16a, Fehlerquelle Kanten falsch gezählt).')
T('flaechen', '5.6', 'Sachaufgabe mit Entscheidung (reicht die Platte?)', ['Rechteckseite aus Fläche berechnen', 'Behauptung prüfen', 'Restfläche berechnen'],
  '2014-OS-K5d fragt genau, ob die Platte reicht (Nebentyp „Behauptung prüfen“); 2019-GYM-K4c entscheidet, ob die Farbe für Wand minus Fenster reicht.')
T('flaechen', '5.7', 'Verschnitt in Prozent (Vorrat, Niveau III)', ['Verschnitt in Prozent berechnen'],
  'Definition „den Abfall als Prozentsatz der Ausgangsfläche berechnen“; 2023-OS-K5c.')

# ==== kreis ====
U('kreis', 2, ['Kreisfläche berechnen'])
U('kreis', 3, ['Kreissektor Anteil berechnen'])
T('kreis', '1.2', 'Kreis mit gegebenem Radius oder Durchmesser zeichnen', ['Draufsicht maßstabsgerecht zeichnen'],
  '2021-OS-K4c: die Tonne als Kreis mit d = 5,8 cm (Maßstab 1 : 10) in die Draufsicht zeichnen.')
T('kreis', '1.3', 'd = 2 · r und r = d : 2', ['Kreisfläche berechnen', 'Volumen Kugel berechnen', 'Mantellinie Kegel bestimmen', 'Verpackungsmaße aus Körpermaßen bestimmen', 'Draufsicht maßstabsgerecht zeichnen'],
  'r = d : 2 in 2016-OS-K3b, 2016-OS-K3c und 2018-OS-K6d (Voraussetzung „Radius aus Durchmesser“), d = 2 · r in 2024-OS-K4b (Voraussetzung „Durchmesser = 2r“) und 2021-OS-K4c (Kreis d = 58 cm aus r = 29 cm), jeweils mit der Fehlerquelle Radius und Durchmesser vertauscht.')
T('kreis', '1.5', 'u aus r', ['Mantelfläche Zylinder als Netz skizzieren', 'Netz eines Zylinders erkennen', 'Kreisumfang berechnen'],
  'Länge des Mantelrechtecks als 2 · π · r in 2023-OS-K5a (r = 4 cm) und 2022-OS-K2a (r = 3,2 cm); GYM-Definition „aus dem Durchmesser oder Radius“ (2014-GYM-B1a).')
T('kreis', '1.6', 'u aus d', ['Kreisumfang berechnen', 'Mantelfläche Zylinder berechnen'],
  '2014-GYM-B1a (U = π · 15) und 2018-OS-K6b (M = π · d · h, Definition „als Umfang mal Höhe“).')
T('kreis', '1.8', 'Umfang mit Dezimalzahlen, auf eine Stelle runden', ['Mantelfläche Zylinder als Netz skizzieren', 'Netz eines Zylinders erkennen'],
  '2023-OS-K5a (a ≈ 25,1 cm) und 2022-OS-K2a (Länge ≈ 20,1 cm) runden den Umfang auf eine Stelle.')
T('kreis', '1.10', 'Sachaufgabe (Rad: Weg bei mehreren Umdrehungen; Baumstamm; Reifen)', ['Kreisumfang berechnen'],
  'Kontextvariante des Umfangs aus d: 2014-GYM-B1a (Umfang einer Uhr mit d = 15 cm).')
T('kreis', '2.1', 'A aus r', ['Kreisfläche berechnen'],
  'Definition „Flächeninhalt eines Kreises aus dem Radius“; 2024-OS-K4a (r = 30 cm).')
T('kreis', '2.2', 'A aus d (erst halbieren)', ['Kreisfläche berechnen'],
  '2016-OS-K3b (d = 2,14 m, π · 1,07²); als Nebentyp in 2018-OS-K6a (d = 6,4 m) und 2017-OS-K3b (d = 5 m), jeweils Fehlerquelle Durchmesser als Radius.')
T('kreis', '2.3', 'A mit Dezimalzahlen, runden', ['Kreisfläche berechnen'],
  '2016-OS-K3b (≈ 3,60 m²) und 2024-OS-K4a (≈ 2827,4 cm²).')
T('kreis', '2.5', 'r aus A (Wurzel)', ['Radius eines Zylinders aus Volumen berechnen', 'Kreisringmaß aus Fläche berechnen'],
  'Teilschritt: den Radius aus π · r² über die Wurzel in 2022-OS-K2d (r = √(425 : (π · 7))) und 2023-GYM-K4b (r = √(R² − A : π)).')
T('kreis', '2.6', 'Halbkreis- und Viertelkreisfläche', ['Flächeninhalt zusammengesetzter Figur berechnen', 'Kreisfläche berechnen'],
  'Zwei Halbkreise in 2017-OS-K3b (Fehlerquelle nur einen addiert); Halbkreisfläche 0,5 · π · 154² in 2014-GYM-K5a (Haupttyp „Kreisfläche berechnen“).')
T('kreis', '2.7', 'Term zu Figur (Viertelkreis: 1/4 · π · r²)', ['Term zu Figur angeben'],
  'Definition „Zu einer beschrifteten Figur … den Term für Flächeninhalt oder Umfang angeben“ ohne Einschränkung der Figur; kein Original mit Kreisteil.')
T('kreis', '2.8', 'Sachaufgabe (Abwurfring, Pizza, Deckel, Grundfläche eines Kegels oder Zylinders)', ['Kreisfläche berechnen'],
  '2016-OS-K3b (Abwurfring) und 2024-OS-K4a (Grundfläche eines Kegels); Deckel als Nebenleistung in 2023-OS-K5c.')
T('kreis', '2.9', 'Fläche oder Umfang: die passende Formel wählen', ['Kreisfläche berechnen', 'Mantelfläche Zylinder als Netz skizzieren', 'Netz eines Zylinders erkennen'],
  'Die Verwechslung ist Fehlerquelle in 2024-OS-K4a (2πr statt πr²), 2023-OS-K5a (a = πr²) und 2022-OS-K2a (Länge = πr²).')
T('kreis', '3.1', 'Anteil aus dem Mittelpunktswinkel als Bruch (90° → 1/4) und als Prozent', ['Kreissektor Anteil berechnen', 'Bruchteil einer Fläche bestimmen', 'Prozentsatz berechnen'],
  'Definition „Anteil eines Kreissektors an der Kreisfläche aus dem Mittelpunktswinkel“ (2025-OS-B1e, 145 : 360, Nebentyp „Prozentsatz berechnen“); als Bruch an Sektoren in 2019-OS-B1c (3/12) und 2026-FOR-B1b (120° = 1/3).')
T('kreis', '3.2', 'Winkel aus dem Anteil (1/3 → 120°)', ['Mittelpunktswinkel berechnen', 'Kreisdiagramm zeichnen'],
  'Definitionen „Mittelpunktswinkel eines Anteils … aus Teil und Ganzem“ (2022-OS-K4d: 0,16 · 360° = 57,6°) und „Anteil in Prozent in den Mittelpunktswinkel umrechnen“ (2017-OS-K2c).')
T('kreis', '3.6', 'Kreisring (großer Kreis minus kleiner Kreis)', ['Kreisringmaß aus Fläche berechnen', 'Restfläche berechnen'],
  'GYM-Typ mit der Ringformel A = π · (R² − r²) (2023-GYM-K4b); die Differenz zweier Kreisflächen ist ein Fall der Definition „Differenz der Flächeninhalte zweier Figuren“.')
T('kreis', '3.7', 'Sachaufgabe (Rasensprenger, Tortenstück, Sektor im Kreisdiagramm)', ['Mittelpunktswinkel berechnen', 'Kreisdiagramm zeichnen', 'Sektor im Kreisdiagramm zuordnen'],
  'Kontext „Sektor im Kreisdiagramm“: 2015-OS-K7c (≈ 52°), 2017-OS-K2c (Sektor mit 40° einzeichnen), 2022-OS-K4d und 2024-OS-K2c (Sektoren nach Größe zuordnen).')

# ==== koerper ====
U('koerper', 1, ['Körper aus Netz oder Schrägbild benennen', 'Kantenzahl eines Körpers angeben', 'Gegenfläche im Würfelnetz bestimmen', 'Körperskizze beschriften', 'Körper in Schrägbild skizzieren'])
U('koerper', 2, ['Volumen Würfel berechnen'])
U('koerper', 3, ['Volumen Prisma berechnen', 'Mantelfläche Prisma berechnen', 'Netz eines Prismas vervollständigen'])
U('koerper', 4, ['Volumen Zylinder berechnen', 'Mantelfläche Zylinder berechnen', 'Mantelfläche Zylinder als Netz skizzieren', 'Netz eines Zylinders erkennen', 'Höhe eines Zylinders aus Volumen berechnen', 'Radius eines Zylinders aus Volumen berechnen', 'Volumenänderung bei doppeltem Radius begründen'])
U('koerper', 5, ['Term zu Körper angeben', 'Restvolumen berechnen', 'Verpackungsmaße aus Körpermaßen bestimmen', 'Packungsanzahl in Quader bestimmen'])
T('koerper', '1.1', 'Körper in der Umwelt, aus Schrägbild oder Netz benennen (Prisma, Pyramide, Quader – Ankreuzen)', ['Körper aus Netz oder Schrägbild benennen'],
  'Definition „Zu einem gezeichneten Netz oder Schrägbild den Körper (Prisma, Pyramide, Quader) benennen oder auswählen“; 2017-OS-B1c, 2018-OS-B1i.')
T('koerper', '1.2', 'Grund- und Deckfläche, Seitenflächen benennen (auch beim liegenden Prisma)', ['Körper aus Netz oder Schrägbild benennen', 'Grundfläche im Netz kennzeichnen'],
  '2017-OS-B1c erkennt das liegende Prisma an zwei kongruenten Dreiecken als Grund- und Deckfläche (Fehlerquelle Dreiecke als Seitenflächen); GYM-Definition „eine Fläche markieren, die als Grundfläche des Prismas dienen kann“ (2020-GYM-K5a).')
T('koerper', '1.3', 'Ecken, Kanten, Flächen zählen (Quader, Dreiecksprisma, quadratische Pyramide)', ['Kantenzahl eines Körpers angeben'],
  'Definition „Anzahl der Kanten, Ecken oder Flächen eines benannten Körpers“; 2019-OS-B1f (quadratische Pyramide, 8 Kanten).')
T('koerper', '1.5', 'Gegenfläche im Würfelnetz markieren', ['Gegenfläche im Würfelnetz bestimmen'],
  'Definition „In einem Würfelnetz die Fläche markieren, die beim Falten einer markierten Fläche gegenüberliegt“; 2016-OS-B1j.')
T('koerper', '1.6', 'Netz von Quader oder Würfel mit Maßen zeichnen', ['Netz eines Prismas vervollständigen'],
  'Grundfall: der Quader ist das Prisma mit Rechteckgrundfläche; 2014-OS-K5b ergänzt Rechtecke mit Maßen (57 × 165, 110 × 165).')
T('koerper', '1.7', 'Schrägbild lesen: verdeckte Kanten, Maße entnehmen', ['Körper aus Netz oder Schrägbild benennen'],
  '2017-OS-B1c: den Körper aus einem Schrägbild mit gestrichelten verdeckten Kanten erkennen.')
T('koerper', '1.8', 'Schrägbild eines Quaders auf Rasterpapier zeichnen (Tiefe halb, schräg)', ['Körper im Schrägbild darstellen'],
  'GYM-Typ: 2019-GYM-K4a (Quader mit Pyramide) und 2025-GYM-K5b (Tiefenachse unter 45° mit q = 0,5).')
T('koerper', '1.9', 'Schrägbild beschriften, Körperhöhe einzeichnen', ['Körperskizze beschriften'],
  'Definition „eine Strecke (Körperhöhe) einzeichnen und die Skizze mit gegebenen Maßen beschriften“; 2015-OS-K6b.')
T('koerper', '1.10', 'Körper in ein Schrägbild einzeichnen (Kegel im Quader)', ['Körper in Schrägbild skizzieren'],
  'Definition „Einen Körper in ein vorgegebenes Schrägbild (z. B. in einen Quader) einzeichnen“; 2024-OS-K4b.')
T('koerper', '2.1', 'V = a · b · c mit ganzen Zahlen', ['Volumen Würfel berechnen', 'Volumen Prisma berechnen'],
  'Der Würfel ist der Fall a = b = c (2026-FOR-B1f, Fehlerquelle 3 · 3 = 9), der Quader das Prisma mit Rechteckgrundfläche (Definition „Volumen eines geraden Prismas als Grundfläche mal Höhe“).')
T('koerper', '2.2', 'Würfel a³', ['Volumen Würfel berechnen'],
  'Definition „Volumen eines Würfels aus der Kantenlänge“; 2026-FOR-B1f (3 · 3 · 3 = 27 cm³).')
T('koerper', '2.3', 'Einheiten cm³, dm³ = l, m³ (1 l = 1000 cm³)', ['Volumen Zylinder berechnen', 'Höhe eines Zylinders aus Volumen berechnen'],
  '2021-OS-K4a (cm³ in Liter, Fehlerquelle Faktor 100) und 2023-OS-K5d (1 l als 1000 cm³, Fehlerquelle 100 cm³).')
T('koerper', '2.6', 'Kante aus V und zwei Kanten', ['Grundkante aus Volumen berechnen'],
  'GYM-Typ: 2017-GYM-K4c stellt die Quaderformel nach der Kante um (a² = 500 : 8, dann Wurzel).')
T('koerper', '2.8', 'aus zwei Quadern zusammengesetzt (Treppe, L-Form)', ['Volumen zusammengesetzter Körper berechnen'],
  'Grundfall der GYM-Definition „Volumen eines aus mehreren Körpern … zusammengesetzten Werkstücks“ (2016-GYM-K3b).')
T('koerper', '3.1', 'Grundfläche erkennen und markieren (auch liegend)', ['Volumen Prisma berechnen', 'Grundfläche im Netz kennzeichnen'],
  'Teilschritt von „Grundfläche mal Höhe“ (2019-OS-K4c: die dreieckige Deckfläche als G); GYM-Definition „eine Fläche markieren, die als Grundfläche des Prismas dienen kann“ (2020-GYM-K5a).')
T('koerper', '3.2', 'V = G · h mit gegebener Grundfläche', ['Volumen Prisma berechnen'],
  'Definition „Volumen eines geraden Prismas als Grundfläche mal Höhe“; 2014-OS-K5a (gegebene Trapezfläche 5 225 cm² · 165 cm).')
T('koerper', '3.3', 'Rechteckgrundfläche (Quader als Prisma)', ['Volumen Prisma berechnen'],
  'Grundfall der Definition „Volumen eines geraden Prismas als Grundfläche mal Höhe“ mit rechteckiger Grundfläche.')
T('koerper', '3.4', 'Dreiecksgrundfläche (G = g · h_g : 2)', ['Volumen Prisma berechnen', 'Flächeninhalt Dreieck berechnen'],
  '2019-OS-K4c: Deckfläche ½ · 1,5 · 1,3 (Haupttyp „Flächeninhalt Dreieck berechnen“), dann V = A · 1,2 (Nebentyp „Volumen Prisma berechnen“).')
T('koerper', '3.5', 'Trapezgrundfläche', ['Volumen Prisma berechnen', 'Flächeninhalt Trapez berechnen'],
  '2014-OS-K5a (gegebene Trapezfläche mal Prismenhöhe); 2018-GYM-K3c sowie 2025-GYM-K5a und 2025-GYM-K5c berechnen die Trapezfläche und daraus das Volumen.')
T('koerper', '3.6', 'Mantel als Rechtecke (Umfang der Grundfläche · h)', ['Mantelfläche Prisma berechnen'],
  'Definition „Gesamtfläche der rechteckigen Seitenflächen eines geraden Prismas“; 2019-OS-K4b (3 · 1,5 · 1,2).')
T('koerper', '3.8', 'Netz eines Prismas vervollständigen (fehlende Rechtecke, Maße)', ['Netz eines Prismas vervollständigen'])
T('koerper', '3.10', 'Sachaufgabe (Dach, Vitrine, Werbeprisma, Zelt, Schokoladenverpackung)', ['Volumen Prisma berechnen', 'Mantelfläche Prisma berechnen'],
  'Werbeprisma in 2019-OS-K4c (Volumen) und 2019-OS-K4b (Werbefläche), Kühlvitrine in 2014-OS-K5a.')
T('koerper', '4.1', 'V = π · r² · h', ['Volumen Zylinder berechnen'],
  'Definition „Volumen eines Zylinders aus Radius und Höhe“; 2026-FOR-K2a (Fehlerquelle r² als 2r), 2021-OS-K4a, 2022-OS-K2b, 2023-OS-K5b.')
T('koerper', '4.2', 'r aus d', ['Volumen Zylinder berechnen', 'Höhe eines Zylinders aus Volumen berechnen'],
  'Radius aus dem Durchmesser in 2023-GYM-K4a (d = 57 cm), 2017-GYM-K4a und 2019-GYM-K3c; Fehlerquelle Durchmesser statt Radius in 2026-FOR-K2a und 2021-OS-K4a.')
T('koerper', '4.3', 'Liter (cm³ → dm³)', ['Volumen Zylinder berechnen'],
  '2021-OS-K4a: 250 998 cm³ ≈ 251 dm³ = 251 l (Fehlerquelle Faktor 100 statt 1000).')
T('koerper', '4.4', 'Mantel M = 2 · π · r · h (Umfang mal Höhe)', ['Mantelfläche Zylinder berechnen'],
  'Definition „Mantelfläche eines Zylinders als Umfang mal Höhe (M = π · d · h)“; 2018-OS-K6b (Fehlerquelle Grund- und Deckfläche mitgerechnet).')
T('koerper', '4.5', 'Netz: Rechtecklänge gleich Umfang', ['Netz eines Zylinders erkennen', 'Mantelfläche Zylinder als Netz skizzieren'],
  '2022-OS-K2a (die Rechtecklänge muss dem Umfang 2πr entsprechen) und 2023-OS-K5a (a = 2πr, b = h).')
T('koerper', '4.7', 'h aus V', ['Höhe eines Zylinders aus Volumen berechnen'],
  'Definition „Höhe eines Zylinders aus Volumen und Radius durch Umstellen der Volumenformel“; 2023-OS-K5d.')
T('koerper', '4.8', 'r aus V (Wurzel)', ['Radius eines Zylinders aus Volumen berechnen'],
  'Definition „durch Umstellen der Volumenformel und Wurzelziehen“; 2022-OS-K2d.')
T('koerper', '4.9', 'Behauptung prüfen (Herstellerangabe „ca. 400 ml“)', ['Volumen Zylinder berechnen', 'Behauptung prüfen'],
  '2023-OS-K5b weist die Herstellerangabe „ca. 400 ml“ nach, 2022-OS-K2b die Angabe „200 ml passen hinein“ (beide Nebentyp „Behauptung prüfen“).')
T('koerper', '4.10', 'Volumen bei doppeltem Radius (vierfach)', ['Volumenänderung bei doppeltem Radius begründen', 'Volumen Kegel und Zylinder vergleichen'],
  '2021-OS-K4b (doppelter Radius, rechnerisch π · 58² · 95 ≈ 1004 l); dieselbe Wirkung des vervielfachten Radius in 2026-FOR-K2d (Definition „Volumenformeln von Körpern mit Variablen vergleichen“).')
T('koerper', '4.11', 'Sachaufgabe (Dose, Regentonne, Turm, Becher, Rohr)', ['Volumen Zylinder berechnen', 'Mantelfläche Zylinder berechnen'],
  'Dose 2023-OS-K5b, Regentonne 2021-OS-K4a, Becher 2022-OS-K2b, Turm 2026-FOR-K2a und Außenmauer des Turms 2018-OS-K6b.')
T('koerper', '4.13', 'Begründen (warum vierfach)', ['Volumenänderung bei doppeltem Radius begründen'],
  'Der P10-Typ verlangt genau diese Begründung: Definition „Begründen, wie sich das Volumen eines Zylinders (Kegels) ändert, wenn der Radius vervielfacht wird“; 2021-OS-K4b.')
T('koerper', '5.1', 'Körper in Teilkörper zerlegen und benennen (Haus = Quader + Dreiecksprisma; Pool = Quader + Halbzylinder)', ['Term zu Körper angeben', 'Volumen zusammengesetzter Körper berechnen'],
  'Teilschritt: 2017-OS-K3c (Pool, Grundfläche a · b + π · (a/2)²) und 2016-GYM-K3b (Werkstück aus Zylinder, Kegel und Halbkugel).')
T('koerper', '5.2', 'Term zum Volumen aufstellen oder vorgegebene Terme prüfen (Klammer)', ['Term zu Körper angeben'],
  'Definition „den Term für das Volumen angeben … oder vorgegebene Terme daraufhin prüfen, ob sie das Volumen richtig beschreiben (Grundfläche mal Höhe, Klammerung)“; 2017-OS-K3c.')
T('koerper', '5.3', 'Volumen zusammengesetzter Körper', ['Volumen zusammengesetzter Körper berechnen', 'Term zu Körper angeben'],
  'GYM-Definition „Volumen eines aus mehreren Körpern … zusammengesetzten Werkstücks berechnen“ (2016-GYM-K3b); 2017-OS-K3c verlangt das Volumen des Pools als Term.')
T('koerper', '5.4', 'Restvolumen (Verpackung minus Inhalt)', ['Restvolumen berechnen'],
  'Definition „Differenz der Volumen zweier Körper (Verpackung minus Inhalt)“; 2024-OS-K4c.')
T('koerper', '5.5', 'kleinste Quaderverpackung aus Körpermaßen (Durchmesser, nicht Radius)', ['Verpackungsmaße aus Körpermaßen bestimmen'],
  'Definition „Kleinste Quaderverpackung aus Durchmesser und Höhe eines Körpers auswählen und begründen“; 2024-OS-K4b (Nebentyp).')
T('koerper', '5.6', 'Packungsanzahl in einer Kiste durch Anordnen', ['Packungsanzahl in Quader bestimmen'],
  'Definition „Größtmögliche Anzahl gleicher Körper in einer quaderförmigen Kiste durch Anordnen“; 2020-OS-K5c.')
T('koerper', '5.7', 'Masse aus Volumen und Dichte (1 m³ Wasser = 1000 kg)', ['Masse aus Volumen und Dichte berechnen', 'Volumen zusammengesetzter Körper berechnen'],
  '2019-OS-K4c (1 m³ Wasser = 1 000 kg, Nebentyp) und GYM-Definition „daraus über die Dichte die Masse bestimmen“ (2016-GYM-K3b).')
T('koerper', '5.8', 'Füllstand in Prozent', ['Masse aus Volumen und Dichte berechnen'],
  'Definition „ggf. mit Füllgrad in Prozent“; 2019-OS-K4c (zu 10 % gefüllt).')
T('koerper', '5.10', 'Fehler finden (Klammer fehlt, h wirkt nur auf einen Teil; Radius als Mindestbreite)', ['Term zu Körper angeben', 'Verpackungsmaße aus Körpermaßen bestimmen'],
  'Beide Fehler sind die verlangte Leistung: 2017-OS-K3c lässt vorgegebene Terme prüfen (zweite Formel ohne Klammer), 2024-OS-K4b begründen, warum 31 cm schmaler als der Durchmesser 60 cm sind.')
T('koerper', '5.11', 'Begründen (Zerlegung erklären; warum Volumen teilen nicht reicht)', ['Packungsanzahl in Quader bestimmen'],
  'Definition „durch Anordnen (nicht nur Volumendivision) bestimmen und erläutern“; 2020-OS-K5c (Fehlerquelle nur Volumen teilen, 8,4).')

# ==== pyramide-kegel-kugel ====
U('pyramide-kegel-kugel', 2, ['Volumen Kegel berechnen', 'Mantelfläche Kegel berechnen', 'Volumen Kegel und Zylinder vergleichen'])
U('pyramide-kegel-kugel', 3, ['Volumen Kugel berechnen'])
T('pyramide-kegel-kugel', '1.1', 'Teile der Pyramide im Schrägbild benennen (Grundfläche, Seitenflächen, Höhe h, Seitenhöhe h_s, Seitenkante; Kantenzahl → koerper.md Einheit 1)', ['Körperskizze beschriften'],
  '2015-OS-K6b: die Höhe der Pyramide von der Spitze zum Diagonalenschnittpunkt einzeichnen (Fehlerquelle Seitenkante oder Höhe einer Seitenfläche).')
T('pyramide-kegel-kugel', '1.5', 'Seitenhöhe aus h und a/2 (Stützdreieck, Pythagoras)', ['Pythagoras Hypotenuse', 'Mantelfläche einer Pyramide berechnen'],
  '2015-OS-K6c: h_s = √(0,68² + 0,40²) als Nebentyp „Pythagoras Hypotenuse“ (Voraussetzung „Höhe der Seitenfläche über rechtwinkliges Dreieck aus h und a/2“); GYM-Definition „über den Satz des Pythagoras ermittelten Seitenhöhe“ (2019-GYM-K4b).')
T('pyramide-kegel-kugel', '1.6', 'Flächeninhalt einer Seitenfläche (Dreieck mit h_s)', ['Flächeninhalt Dreieck berechnen', 'Mantelfläche einer Pyramide berechnen'],
  '2015-OS-K6c: A = ½ · 0,80 · 0,789 ≈ 0,32 m² (Fehlerquelle Pyramidenhöhe als Dreieckshöhe); Teilschritt der Mantelfläche in 2019-GYM-K4b.')
T('pyramide-kegel-kugel', '1.7', 'Mantel M = 4 · a · h_s : 2', ['Mantelfläche einer Pyramide berechnen'],
  'GYM-Definition „Mantelfläche einer quadratischen Pyramide aus der Grundkante und der über den Satz des Pythagoras ermittelten Seitenhöhe“; 2019-GYM-K4b (4 · 0,5 · 4 · h_s).')
T('pyramide-kegel-kugel', '1.10', 'Schrägbild zeichnen, Höhe einzeichnen und beschriften', ['Körperskizze beschriften', 'Körper im Schrägbild darstellen'],
  '2015-OS-K6b (Höhe einzeichnen und beschriften) und 2019-GYM-K4a (Turm aus Quader und Pyramide als Schrägbild zeichnen).')
T('pyramide-kegel-kugel', '1.13', 'Sachaufgabe (Zeltdach: Stoff; Glaspyramide: Volumen und Glasfläche; Kirchturmspitze; Modell im Maßstab)', ['Flächeninhalt Dreieck berechnen', 'Länge im Maßstab umrechnen', 'Mantelfläche einer Pyramide berechnen'],
  'Modellpyramide in 2015-OS-K6c (Sperrholz für eine Seitenfläche) und 2015-OS-K6a (Maßstab 1 : 10); Turmdach in 2019-GYM-K4b (Mantelfläche).')
T('pyramide-kegel-kugel', '2.1', 'Radius, Höhe, Mantellinie im Bild benennen (welche Strecke steht senkrecht)', ['Mantellinie Kegel bestimmen', 'Pythagoras Kathete'],
  'Voraussetzung „rechtwinkliges Dreieck im Kegel erkennen“ in 2018-OS-K6d und 2026-FOR-K2c (Fehlerquelle s als Kegelhöhe).')
T('pyramide-kegel-kugel', '2.2', 'V = 1/3 · π · r² · h', ['Volumen Kegel berechnen'],
  'Definition „Volumen eines Kegels aus Radius und Höhe berechnen“; 2024-OS-K4c (Nebentyp, Fehlerquelle Faktor 1/3 vergessen).')
T('pyramide-kegel-kugel', '2.3', 'r aus d', ['Volumen Kegel berechnen', 'Mantellinie Kegel bestimmen'],
  '2021-GYM-K5a (V = 1/3 · π · (d/2)² · t, Nebentyp „Volumen Kegel berechnen“) und 2018-OS-K6d (Radius 3,2 m aus d = 6,4 m als Kathete).')
T('pyramide-kegel-kugel', '2.4', 'Liter (cm³ → dm³)', ['Volumen Kegel berechnen'],
  '2021-GYM-K5a: 393,5 cm³ ≈ 0,39 l (Nebentyp „Volumen Kegel berechnen“).')
T('pyramide-kegel-kugel', '2.5', 's aus r und h (Stützdreieck)', ['Mantellinie Kegel bestimmen'],
  'Definition „Mantellinie eines Kegels aus Radius und Höhe über den Satz des Pythagoras berechnen“; 2018-OS-K6d.')
T('pyramide-kegel-kugel', '2.6', 'h aus s und r', ['Pythagoras Kathete', 'Kegelhöhe aus Mantellinie und Radius berechnen'],
  '2026-FOR-K2c (Kegelhöhe √(8,6² − 4,7²), Haupttyp „Pythagoras Kathete“); GYM-Definition „Höhe eines Kegels aus der Mantellinie und dem Radius“ (2022-GYM-K4b).')
T('pyramide-kegel-kugel', '2.7', 'Mantel M = π · r · s', ['Mantelfläche Kegel berechnen'],
  'Definition „Mantelfläche eines Kegels aus Radius und Mantellinie berechnen“; 2026-FOR-K2b (Fehlerquelle Grundfläche mitgerechnet, s als Höhe).')
T('pyramide-kegel-kugel', '2.9', 'Schrägbild eines Kegels skizzieren (Ellipse, Spitze, Höhe gestrichelt)', ['Körper in Schrägbild skizzieren'],
  '2024-OS-K4b: den Kegel in den Quader skizzieren (Ellipse auf der Bodenfläche, Spitze mittig oben).')
T('pyramide-kegel-kugel', '2.12', 'Kegeldach auf einem Zylinder: Dachfläche, Materialkosten, Gesamthöhe', ['Mantelfläche Kegel berechnen', 'Kosten aus Menge und Preis berechnen', 'Pythagoras Kathete', 'Strecke aus Teilstrecken berechnen'],
  'Turm 2026: Dachfläche und Ziegelkosten in 2026-FOR-K2b (Nebentyp „Kosten aus Menge und Preis berechnen“), Gesamthöhe 25,0 m plus Kegelhöhe in 2026-FOR-K2c (Nebentyp „Strecke aus Teilstrecken berechnen“).')
T('pyramide-kegel-kugel', '2.13', 'Kegel in Zylinderverpackung (Restvolumen → koerper.md Einheit 5)', ['Restvolumen berechnen', 'Volumen Kegel berechnen'],
  '2024-OS-K4c: Zylinderverpackung minus Kegel (Haupttyp „Restvolumen berechnen“, Nebentyp „Volumen Kegel berechnen“).')
T('pyramide-kegel-kugel', '2.14', 'Volumen des Kegels gegen den Zylinder mit gleichem r und h (ein Drittel)', ['Volumen Kegel und Zylinder vergleichen'],
  'Definition „Volumenformeln von Körpern mit Variablen vergleichen“; 2026-FOR-K2d rechnet mit V_Kegel = 1/3 · π · r² · h gegen V_Zylinder.')
T('pyramide-kegel-kugel', '2.15', 'Aussage über den dreifachen Radius rechnerisch prüfen (Niveau III)', ['Volumen Kegel und Zylinder vergleichen', 'Behauptung prüfen'],
  '2026-FOR-K2d prüft genau diese Aussage (Nebentyp „Behauptung prüfen“, Ergebnis dreifaches Volumen).')
T('pyramide-kegel-kugel', '2.16', 'Sachaufgabe (Trichter, Eistüte, Verkehrshütchen, Sandhaufen, Sektglas, Zelt)', ['Volumen Kegel berechnen', 'Mantelfläche Kegel berechnen'],
  'Kontextvarianten: kegelförmiger Messbecher 2021-GYM-K5a und Halde 2014-GYM-K5c (Volumen), Boje 2022-GYM-K4c (Mantelfläche als Nebentyp).')
T('pyramide-kegel-kugel', '2.18', 'Begründen (drei Kegel füllen den Zylinder; warum das Volumen beim dreifachen Radius neunfach wird)', ['Volumen Kegel und Zylinder vergleichen', 'Volumenänderung bei doppeltem Radius begründen'],
  '2026-FOR-K2d verlangt die Begründung über (3r)² = 9r² als Antworttext; Definition „Begründen, wie sich das Volumen eines Zylinders (Kegels) ändert, wenn der Radius vervielfacht wird“.')
T('pyramide-kegel-kugel', '3.2', 'V = 4/3 · π · r³ mit r', ['Volumen Kugel berechnen'],
  'Definition „Volumen einer Kugel aus Radius oder Durchmesser mit V = 4/3 · π · r³ berechnen“; 2016-OS-K3c (Fehlerquelle 4/3 vergessen).')
T('pyramide-kegel-kugel', '3.3', 'aus d', ['Volumen Kugel berechnen'],
  'Definition „aus Radius oder Durchmesser“; 2016-OS-K3c (d = 12 cm, Fehlerquelle 12 statt 6).')
T('pyramide-kegel-kugel', '3.4', 'Oberfläche O = 4 · π · r²', ['Kugeloberfläche berechnen'],
  'GYM-Definition „Oberfläche einer Kugel aus Radius oder Durchmesser mit O = 4 · π · r² berechnen“; 2015-GYM-K4c.')
T('pyramide-kegel-kugel', '3.6', 'Halbkugel: Volumen halb, Oberfläche halb plus Schnittkreis', ['Volumen zusammengesetzter Körper berechnen', 'Kugelmaß aus Oberfläche berechnen'],
  'GYM: Halbkugelvolumen 2/3 · π · r³ in 2016-GYM-K3b und 2022-GYM-K4d, gewölbte Halbkugelfläche 2 · π · r² in 2022-GYM-K4a.')
T('pyramide-kegel-kugel', '3.7', 'Masse aus Volumen und Dichte (Stoßkugel, Stahlkugel)', ['Masse aus Volumen und Dichte berechnen', 'Volumen zusammengesetzter Körper berechnen'],
  'Definition „Masse aus Volumen und Masse je Volumeneinheit (Dichte) berechnen“ (2019-OS-K4c); Stahlwerkstück mit Halbkugel über 7,8 g je cm³ in 2016-GYM-K3b.')
T('pyramide-kegel-kugel', '3.8', 'r aus O (Wurzel)', ['Kugelmaß aus Oberfläche berechnen'],
  'GYM-Definition „Durchmesser oder Radius einer Halbkugel durch Umstellen der Oberflächenformel“; 2022-GYM-K4a (r = √(O : (2π))).')
T('pyramide-kegel-kugel', '3.9', 'r aus V (Kubikwurzel, Vorrat)', ['Volumen zusammengesetzter Körper berechnen'],
  '2022-GYM-K4d löst π · r³ = 10,6 nach r auf (r = 1,5 m).')
T('pyramide-kegel-kugel', '3.11', 'Kugel in der Würfelschachtel: Kante gleich Durchmesser, Restvolumen', ['Verpackungsmaße aus Körpermaßen bestimmen', 'Restvolumen berechnen', 'Kugeldurchmesser aus Anordnung bestimmen'],
  'Mindestmaß gleich Durchmesser in 2024-OS-K4b (Definition „aus Durchmesser und Höhe eines Körpers“), Restvolumen nach Definition „Verpackung minus Inhalt“ (2024-OS-K4c), Kante gleich vier Durchmesser in 2020-GYM-K5d.')
T('pyramide-kegel-kugel', '3.12', 'Sachaufgabe (Silo oder Turm mit Halbkugeldach, Eiskugel in der Tüte – Kegel plus Halbkugel)', ['Volumen zusammengesetzter Körper berechnen'],
  'GYM-Definition „aus mehreren Körpern (z. B. Zylinder, Kegel, Halbkugel) zusammengesetzt“; Boje aus Halbkugel und Kegel in 2022-GYM-K4d.')

# ==== pythagoras ====
U('pythagoras', 1, ['Satz des Pythagoras formulieren', 'Pythagoras Gleichung zuordnen', 'Pythagoras Hypotenuse'])
U('pythagoras', 2, ['Pythagoras Kathete', 'Pythagoras Gleichung zuordnen'])
U('pythagoras', 3, ['Streckenlänge aus Koordinaten berechnen', 'Mantellinie Kegel bestimmen', 'Pythagoras Kathete', 'Pythagoras Hypotenuse'])
T('pythagoras', '1.1', 'rechten Winkel im Dreieck finden, Hypotenuse und Katheten benennen (Dreieck in verschiedener Lage: rechter Winkel unten links, unten rechts, oben; Hypotenuse waagerecht)', ['Pythagoras Gleichung zuordnen', 'Satz des Pythagoras formulieren', 'Pythagoras Hypotenuse', 'Pythagoras Kathete'],
  'Teilschritt jeder Pythagoras-Aufgabe: 2017-OS-B1d erkennt die Hypotenuse gegenüber dem rechten Winkel, 2022-OS-B1g hat den Distraktor „Dem rechten Winkel liegt eine Kathete gegenüber“, die falsche Hypotenuse ist Fehlerquelle in 2020-OS-K7a und 2016-OS-K7b.')
T('pythagoras', '1.2', 'Satz in Worten: die richtige von drei Aussagen ankreuzen (Kathetenquadrate und Hypotenusenquadrat; P10-Form)', ['Satz des Pythagoras formulieren'],
  'Definition „unter mehreren Aussagen die korrekte sprachliche Fassung … auswählen“; Original 2022-OS-B1g mit drei Aussagen.')
T('pythagoras', '1.3', 'Gleichung zum beschrifteten Dreieck aufstellen (a² + b² = c², mit x, y, z oder u, v, w nach der Beschriftung)', ['Pythagoras Gleichung zuordnen', 'Pythagoras Hypotenuse'],
  'Vorstufe des Auswählens (2017-OS-B1d z² = x² + y², 2026-FOR-B1j mit u, v, w) und erster Schritt der Hypotenusenrechnung (2020-OS-K7a AB² = 12² + 34²).')
T('pythagoras', '1.4', 'Gleichung aus vier Optionen ankreuzen (Summe, Differenz, mit und ohne Wurzel; P10-Form)', ['Pythagoras Gleichung zuordnen'],
  'Definition „die richtige Pythagoras-Gleichung auswählen“; 2021-OS-B1h und 2017-OS-B1d mit vier Optionen aus Summe, Differenz, mit und ohne Wurzel.')
T('pythagoras', '1.6', 'Hypotenuse aus zwei Katheten mit aufgehender Wurzel', ['Pythagoras Hypotenuse'],
  'Grundfall der Definition „Hypotenuse … aus beiden Katheten“; 2020-GYM-B1a rechnet √(6² + 8²) = 10.')
T('pythagoras', '1.7', 'mit nicht aufgehender Wurzel: Zwischenergebnis c², Näherungswert gerundet', ['Pythagoras Hypotenuse'],
  '2020-OS-K7a: AB² = 1300 als Zwischenergebnis, AB ≈ 36,1 m.')
T('pythagoras', '1.8', 'Katheten als Dezimalzahlen', ['Pythagoras Hypotenuse'],
  'Dezimalkatheten in 2022-OS-K2c (7 cm und 6,4 cm) und 2015-OS-K6c (0,68 m und 0,40 m, Nebentyp).')
T('pythagoras', '1.9', 'Einheit beim Ergebnis, gemischte Einheiten vorher angleichen', ['Pythagoras Hypotenuse'],
  '2019-GYM-K3b rechnet mit Längen in Meter und dem Zuschlag 25 cm; alle Originale verlangen die Einheit im Ergebnis (2020-OS-K7a ≈ 36,1 m).')
T('pythagoras', '1.10', 'Diagonale im Rechteck und Quadrat', ['Pythagoras Hypotenuse'],
  '2022-OS-K2c: Diagonale im Rechteck 7 cm × 6,4 cm des Becherquerschnitts.')
T('pythagoras', '1.11', 'Sachaufgabe mit gegebener Skizze (Rampe, Leiter an der Wand, Abkürzung über die Wiese, Stab in der Kiste)', ['Pythagoras Hypotenuse'],
  'Rampe 2025-OS-K4a, Stab im Becher 2022-OS-K2c, Seil am Pfeiler 2019-GYM-K3b, jeweils mit Skizze.')
T('pythagoras', '1.12', 'Überstand oder Zuschlag zum Ergebnis addieren', ['Pythagoras Hypotenuse', 'Strecke aus Teilstrecken berechnen'],
  '2022-OS-K2c (plus 2 cm Überstand) und 2019-GYM-K3b (plus 2 · 25 cm Zuschlag); das Addieren ist „Strecke aus Teilstrecken berechnen“ (Definition, Nebentyp in 2026-FOR-K2c).')
T('pythagoras', '1.13', 'Ergebnis mit sinnvoller Genauigkeit angeben', ['Pythagoras Hypotenuse', 'Pythagoras Kathete'],
  'Die Wurzel geht in der P10 nie auf, verlangt ist ein gerundeter Näherungswert (2020-OS-K7a ≈ 36,1 m, 2019-OS-K3a ≈ 8,1 m).')
T('pythagoras', '2.1', 'Gleichung nach einer Kathete umstellen (a² = c² − b², b² = c² − a²)', ['Pythagoras Kathete', 'Pythagoras Gleichung zuordnen'],
  'Erster Schritt der Kathetenrechnung (2019-OS-K3a BC² = 9² − 4²) und Kathetenform des Auswählens (2024-OS-B1f z = √(x² − y²)).')
T('pythagoras', '2.2', 'Kathetengleichung aus Optionen ankreuzen (P10-Form)', ['Pythagoras Gleichung zuordnen'],
  'Original 2024-OS-B1f: Kathete z gesucht, vier Gleichungen zur Auswahl.')
T('pythagoras', '2.3', 'Kathete aus Hypotenuse und Kathete mit aufgehender Wurzel', ['Pythagoras Kathete'],
  'Grundfall der Definition „Kathete … aus Hypotenuse und anderer Kathete“ mit leichteren Zahlen; die Originale haben nie eine aufgehende Wurzel.')
T('pythagoras', '2.4', 'mit nicht aufgehender Wurzel: Zwischenergebnis a², Näherungswert', ['Pythagoras Kathete'],
  '2019-OS-K3a (BC² = 65, ≈ 8,06 m) und 2026-FOR-K4a (h = √855 ≈ 29,2 cm).')
T('pythagoras', '2.5', 'Dezimalzahlen', ['Pythagoras Kathete'],
  'Dezimalzahlen in 2022-OS-K5a (√(14,1² − 7,4²)) und 2026-FOR-K2c (√(8,6² − 4,7²)).')
T('pythagoras', '2.6', 'Ergebnis prüfen: die Kathete ist kürzer als die Hypotenuse', ['Pythagoras Kathete'],
  'Kontrollschritt gegen die Fehlerquelle aller sechs Kathete-Originale „Quadrate addiert“, die eine Kathete länger als die Hypotenuse liefert (2024-OS-K6a 461 m bei AB = 384 m).')
T('pythagoras', '2.7', 'Nachweis mit vorgegebenem Ergebnis („Weisen Sie nach, dass … ≈ …“; P10-Form)', ['Pythagoras Kathete', 'Behauptung prüfen'],
  '2022-OS-K5a: Nachweis AD ≈ 12,0 m, Nebentyp „Behauptung prüfen“ zu genau dieser Behauptung.')
T('pythagoras', '2.8', 'Kathete im Sachzusammenhang (Höhenunterschied der Seilbahn, Abstand auf dem Platz, Höhe des Parallelogramms mit Fußpunkt außerhalb)', ['Pythagoras Kathete'],
  'Seilbahn 2024-OS-K6a, Abstand 2019-OS-K3a, Parallelogrammhöhe mit Fußpunkt auf der Verlängerung 2026-FOR-K4a.')
T('pythagoras', '2.9', 'Umkehrung: drei Seiten gegeben, längste Seite als c, a² + b² mit c² vergleichen, rechtwinklig oder nicht (Antwort mit Rechnung)', ['Rechten Winkel begründen'],
  'Definition „Begründen, dass ein Winkel 90° misst (… Umkehrung des Pythagoras)“; 2025-OS-K2c lässt AD² + DC² = 2500 = AC² als Weg zu (Typ in winkel-dreiecke.md).')
T('pythagoras', '2.10', 'rechten Winkel mit der Umkehrung begründen (Verfahren; Typ in winkel-dreiecke.md Einheit 3)', ['Rechten Winkel begründen'],
  'Definition nennt die Umkehrung des Pythagoras als Begründungsweg; 2025-OS-K2c, dritter Weg.')
T('pythagoras', '2.13', 'Begründen (warum bei gesuchter Kathete subtrahiert wird; warum die Zwölfknotenschnur mit den Abschnitten drei, vier, fünf einen rechten Winkel liefert)', ['Rechten Winkel begründen'],
  'Die zweite Begründung ist genau die Leistung der Definition „Begründen, dass ein Winkel 90° misst (… Umkehrung des Pythagoras)“, vgl. 2025-OS-K2c; die erste hat keinen P10-Typ.')
T('pythagoras', '3.1', 'rechtwinkliges Teildreieck in der Figur markieren und seine drei Seiten benennen (Hypotenuse gegenüber dem rechten Winkel)', ['Pythagoras Kathete', 'Pythagoras Hypotenuse', 'Mantellinie Kegel bestimmen', 'Streckenlänge aus Koordinaten berechnen', 'Gleichung zu Figur erläutern'],
  'Teilschritt der Figurenaufgaben: Teildreieck ADC in 2022-OS-K5a, Rechteck im Becherquerschnitt 2022-OS-K2c, Stützdreieck aus Radius, Dachhöhe und Mantellinie 2018-OS-K6d, rechter Winkel bei A in 2019-OS-K2d, Teildreieck XCE in 2021-GYM-K4d.')
T('pythagoras', '3.2', 'Höhe im gleichschenkligen Dreieck aus Schenkel und halber Grundseite', ['Pythagoras Kathete'],
  'Definition „Kathete … aus Hypotenuse und anderer Kathete“ mit dem Schenkel als Hypotenuse; kein Original mit dieser Figur.')
T('pythagoras', '3.3', 'Schenkel aus Höhe und halber Grundseite', ['Pythagoras Hypotenuse'],
  '2023-GYM-K6a: Schenkel = √(40² + 100²) im halben gleichschenkligen Dreieck, Fehlerquelle volle Basis.')
T('pythagoras', '3.4', 'gleichschenkliges Trapez: Überstand als halbe Differenz der parallelen Seiten, Schenkel oder Höhe', ['Pythagoras Hypotenuse', 'Pythagoras Kathete', 'Umfang Trapez berechnen', 'Trapezhöhe aus Fläche berechnen'],
  'Definitionen von „Umfang Trapez berechnen“ (Schenkel über Pythagoras, 2023-OS-K2c mit Überstand 5,4 m) und „Trapezhöhe aus Fläche berechnen“ (aus Schenkel und halber Seitendifferenz, 2014-OS-K5c √(57² − 15²)); der Schenkel ist Hypotenuse, die Höhe Kathete.')
T('pythagoras', '3.5', 'Parallelogramm: Höhe mit Fußpunkt auf der Verlängerung der Grundseite', ['Pythagoras Kathete'],
  '2026-FOR-K4a: h = √(32² − 13²) mit F auf der Verlängerung von AB.')
T('pythagoras', '3.6', 'stumpfwinkliges Dreieck mit Höhe: Teilstrecke der Grundseite', ['Pythagoras Kathete'],
  '2022-OS-K5a: Teilstrecke AD = √(14,1² − 7,4²) im Teildreieck mit der Höhe hc.')
T('pythagoras', '3.7', 'Drachen und Raute: Seite aus den halben Diagonalen', ['Pythagoras Hypotenuse', 'Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen'],
  '2025-OS-K2a: AB = √(25² + 55²) aus den Diagonalenabschnitten (Nebentyp); Definition des GYM-Typs, Seiten aus den Diagonalenabschnitten über den Satz des Pythagoras (2017-GYM-K3b).')
T('pythagoras', '3.8', 'Diagonale im Rechteck, Raumdiagonale im Quader in zwei Schritten', ['Pythagoras Hypotenuse'],
  'Diagonale im Rechteck in 2022-OS-K2c; die Raumdiagonale ist dieselbe Hypotenusenrechnung zweimal, ohne Original.')
T('pythagoras', '3.9', 'Streckenlänge aus Koordinaten: Differenzen der x- und y-Werte als Katheten, auch negative Koordinaten (P10-Form)', ['Streckenlänge aus Koordinaten berechnen', 'Umfang eines Dreiecks aus Koordinaten berechnen', 'Dreiecksart aus Koordinaten nachweisen'],
  'Definition „über die Koordinatendifferenzen mit dem Satz des Pythagoras“, 2019-OS-K2d mit A(0|−2); dieselbe Rechnung in 2015-GYM-K2c (RO = √29) und 2024-GYM-K3c (AC = BC = √2).')
T('pythagoras', '3.10', 'Seitenhöhe der Pyramide aus Höhe und halber Grundkante', ['Pythagoras Hypotenuse', 'Mantelfläche einer Pyramide berechnen'],
  '2015-OS-K6c: h_s = √(0,68² + 0,40²) als Nebentyp „Pythagoras Hypotenuse“; Definition „… über den Satz des Pythagoras ermittelten Seitenhöhe“ (2019-GYM-K4b).')
T('pythagoras', '3.11', 'Mantellinie des Kegels aus Radius und Höhe, Radius zuerst aus dem Durchmesser', ['Mantellinie Kegel bestimmen'],
  'Definition „Mantellinie eines Kegels aus Radius und Höhe“; 2018-OS-K6d mit r = 3,2 m aus d = 6,4 m.')
T('pythagoras', '3.12', 'Kegelhöhe aus Mantellinie und Radius', ['Kegelhöhe aus Mantellinie und Radius berechnen', 'Pythagoras Kathete'],
  'GYM-Typ gleichen Inhalts (2022-GYM-K4b); 2026-FOR-K2c rechnet die Kegelhöhe √(8,6² − 4,7²) als „Pythagoras Kathete“.')
T('pythagoras', '3.13', 'Rechenweg ohne Zahlen beschreiben (P10-Form)', ['Mantellinie Kegel bestimmen'],
  'Definition „… oder den Rechenweg beschreiben“; 2018-OS-K6d verlangt den Rechenweg für den Dachbalken ohne Zahlenergebnis.')
T('pythagoras', '3.14', 'Gesamthöhe eines Turms aus Zylinderhöhe und Kegelhöhe', ['Pythagoras Kathete', 'Strecke aus Teilstrecken berechnen', 'Kegelhöhe aus Mantellinie und Radius berechnen'],
  '2026-FOR-K2c (Kegelhöhe, dann 25,0 m + 7,2 m, Nebentyp „Strecke aus Teilstrecken berechnen“) und 2022-GYM-K4b (Gesamthöhe der Boje aus Halbkugelradius und Kegelhöhe).')
T('pythagoras', '3.15', 'Stab oder Stange schräg im Zylinder oder Quader mit Überstand', ['Pythagoras Hypotenuse'],
  '2022-OS-K2c: Stab diagonal im Becher, 2 cm Überstand.')
T('pythagoras', '3.16', 'Rampe, Leiter, Seil an der Wand mit Skizze', ['Pythagoras Hypotenuse', 'Pythagoras Kathete'],
  'Rampe 2025-OS-K4a und Seil 2019-GYM-K3b mit gesuchter Hypotenuse, Höhenunterschied an der Seilbahn 2024-OS-K6a mit gesuchter Kathete.')

# ==== trigonometrie ====
U('trigonometrie', 1, ['Winkelfunktion Seitenverhältnis angeben', 'Trigonometrische Gleichung nach Seite umstellen', 'Seite im rechtwinkligen Dreieck berechnen'])
U('trigonometrie', 2, ['Winkel im rechtwinkligen Dreieck berechnen'])
U('trigonometrie', 3, ['Seite im rechtwinkligen Dreieck berechnen', 'Winkel im rechtwinkligen Dreieck berechnen'])
U('trigonometrie', 4, ['Sinussatz Seite berechnen'])
T('trigonometrie', '1.1', 'rechten Winkel und markierten Winkel finden, Hypotenuse, Gegenkathete und Ankathete beschriften (Dreieck in verschiedener Lage: rechter Winkel unten links, unten rechts, oben; Hypotenuse unten oder oben)', ['Winkelfunktion Seitenverhältnis angeben', 'Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen', 'Seite im rechtwinkligen Dreieck berechnen', 'Winkel im rechtwinkligen Dreieck berechnen'],
  'Teilschritt aller Aufgaben des Themas: 2025-OS-B1g („Gegenkathete von γ ist u“), GYM-Definition „typische Verwechslung von Ankathete und Gegenkathete“, Fehlerquellen in 2016-GYM-K4d (Seite) und 2024-OS-K6b (Winkel, 255 als Gegenkathete).')
T('trigonometrie', '1.2', 'Seiten vom zweiten spitzen Winkel aus neu benennen (Gegen- und Ankathete tauschen)', ['Winkelfunktion Seitenverhältnis angeben', 'Winkel im rechtwinkligen Dreieck berechnen'],
  '2017-OS-B1j und 2018-OS-B1g fragen nach β statt α; Fehlerquelle „Winkel am anderen Ende“ in 2020-OS-K5b und 2019-OS-K2d (tan β = 2/4).')
T('trigonometrie', '1.3', 'sin, cos oder tan zum beschrifteten Dreieck als Bruch eintragen (P10-Form, Buchstaben r, s, t; a, b; u, v, w)', ['Winkelfunktion Seitenverhältnis angeben'],
  'Definition „sin, cos oder tan eines Winkels als Verhältnis der beschrifteten Seiten angeben“; 2025-OS-B1g (Eintragen), 2017-OS-B1j, 2019-OS-B1h, 2020-OS-B1c.')
T('trigonometrie', '1.4', 'die richtige von drei Gleichungen ankreuzen (P10-Form)', ['Winkelfunktion Seitenverhältnis angeben', 'Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen'],
  '2018-OS-B1g (sin β = b/a unter drei Gleichungen); je Option dieselbe Prüfung wie im GYM-Typ „eine behauptete Gleichung für sin, cos oder tan … als wahr oder falsch prüfen“ (2024-GYM-B2a).')
T('trigonometrie', '1.5', 'sin-, cos- und tan-Werte mit dem Taschenrechner, Grad-Modus prüfen', ['Seite im rechtwinkligen Dreieck berechnen', 'Trigonometrische Gleichung nach Seite umstellen'],
  'Rechenschritt jeder Seitenrechnung; Fehlerquelle „Taschenrechner in Bogenmaß“ in 2021-OS-K3a, sin 30° = 0,5 in 2020-OS-B1j.')
T('trigonometrie', '1.7', 'Gegenkathete aus Hypotenuse und Winkel (Sinus, mal)', ['Seite im rechtwinkligen Dreieck berechnen'],
  '2021-OS-K3a (AB = 1500 · sin 55°) und 2018-OS-K4d (CB = 112,8 · sin 30°).')
T('trigonometrie', '1.8', 'Ankathete aus Hypotenuse und Winkel (Kosinus, mal)', ['Seite im rechtwinkligen Dreieck berechnen'],
  '2021-OS-K3b (AD = 1500 · cos 55°) und 2023-OS-K7b (AF = 131,5 · cos 45°).')
T('trigonometrie', '1.9', 'Hypotenuse aus Gegenkathete und Winkel (geteilt durch den Sinus)', ['Seite im rechtwinkligen Dreieck berechnen', 'Trigonometrische Gleichung nach Seite umstellen'],
  '2022-OS-K5d (a = 7,4 : sin 52°) und 2026-FOR-K4c (AC = 29,24 : sin 22°); ohne Figur dieselbe Umstellung in 2020-OS-B1j (x = 7 : sin 30°).')
T('trigonometrie', '1.10', 'Hypotenuse aus Ankathete und Winkel (geteilt durch den Kosinus)', ['Seite im rechtwinkligen Dreieck berechnen'],
  '2023-OS-K7b (BC = BF : cos 65°) und 2025-GYM-K4a (SQ = PQ : cos 20°).')
T('trigonometrie', '1.11', 'Gegenkathete aus Ankathete und Winkel (Tangens, mal)', ['Seite im rechtwinkligen Dreieck berechnen'],
  '2016-OS-K7c: BD = AD · tan 34°.')
T('trigonometrie', '1.12', 'Ankathete aus Gegenkathete und Winkel (geteilt durch den Tangens)', ['Seite im rechtwinkligen Dreieck berechnen'],
  '2017-OS-K4b (PB = 1,20 : tan 34,9°) und 2022-OS-K5e (DB = 7,4 : tan 52°, Nebentyp).')
T('trigonometrie', '1.13', 'Funktion selbst wählen: welche zwei Seiten sind beteiligt', ['Seite im rechtwinkligen Dreieck berechnen'],
  'Definition „über sin, cos oder tan“ ohne Vorgabe der Funktion; Fehlerquellen „Sinus verwenden“ (2017-OS-K4b) und „cos statt sin“ (2018-OS-K4d).')
T('trigonometrie', '1.14', 'Gleichung ohne Figur nach der Seite umstellen, Seite im Nenner (P10-Form)', ['Trigonometrische Gleichung nach Seite umstellen'],
  'Definition „sin α = a/x ohne Figur nach x umstellen“; Original 2020-OS-B1j.')
T('trigonometrie', '1.15', 'Winkel als Dezimalgrad, Seiten als Dezimalzahlen', ['Seite im rechtwinkligen Dreieck berechnen'],
  '2017-OS-K4b (tan 34,9°, 1,20 m) und 2018-OS-K4d (112,8 m).')
T('trigonometrie', '1.16', 'Einheit beim Ergebnis, Runden auf eine Dezimale', ['Seite im rechtwinkligen Dreieck berechnen'],
  'Muster der Kontextaufgaben: Ergebnis auf eine Dezimale mit Einheit, etwa 2022-OS-K5d (a ≈ 9,4 m) und 2026-FOR-K4c (≈ 78,1 cm).')
T('trigonometrie', '1.17', 'Ergebnis prüfen: Kathete kürzer als Hypotenuse', ['Seite im rechtwinkligen Dreieck berechnen'],
  'Kontrollschritt gegen die Fehlerquelle „a = 7,4 · sin 52°“ in 2022-OS-K5d, die eine Hypotenuse kürzer als die Kathete liefert.')
T('trigonometrie', '1.18', 'Nachweis mit vorgegebenem Ergebnis (P10-Form)', ['Seite im rechtwinkligen Dreieck berechnen', 'Behauptung prüfen'],
  '2021-OS-K3a (zu zeigen AB ≈ 1229 m) und 2023-OS-K7b (Nachweis BF ≈ AF ≈ 93,0 cm, Nebentyp „Behauptung prüfen“ zu genau dieser Behauptung).')
T('trigonometrie', '1.19', 'Sachaufgabe mit gegebener Skizze (Leiter an der Wand, Dachschräge mit Wand, Rampe, Diagonale eines Vierecks mit rechtem Winkel)', ['Seite im rechtwinkligen Dreieck berechnen'],
  'Dachwand 2017-OS-K4b, Viereck mit rechtem Winkel und Diagonale 2021-OS-K3a und 2021-OS-K3b.')
T('trigonometrie', '2.1', '„Seite oder Winkel gesucht“ erkennen', ['Winkel im rechtwinkligen Dreieck berechnen', 'Seite im rechtwinkligen Dreieck berechnen'],
  'Die Stämme mischen beide Fragen (2022-OS-K5b Winkel, 2022-OS-K5d Seite; 2026-FOR-K4b und 2026-FOR-K4c), das Zuordnen gehört zu jeder Teilaufgabe.')
T('trigonometrie', '2.2', 'zwei gegebene Seiten vom gesuchten Winkel aus benennen und die Funktion wählen', ['Winkel im rechtwinkligen Dreieck berechnen'],
  '2024-OS-K6b (cos β1 = 255 : 384, Fehlerquelle sin statt cos) und 2019-OS-K3b (cos α = 4/9).')
T('trigonometrie', '2.3', 'Verhältnis als Bruch und als Dezimalzahl', ['Winkel im rechtwinkligen Dreieck berechnen'],
  '2026-FOR-K4b: cos ε = 13 : 32 = 0,406, dann ε.')
T('trigonometrie', '2.4', 'Umkehrtaste am Taschenrechner (SHIFT sin, cos, tan; Anzeige sin⁻¹)', ['Winkel im rechtwinkligen Dreieck berechnen'],
  'Definition „über tan, sin oder cos und die Umkehrfunktion“; 2019-OS-K3b α = cos⁻¹(4/9).')
T('trigonometrie', '2.5', 'Winkel aus Gegenkathete und Hypotenuse (sin⁻¹)', ['Winkel im rechtwinkligen Dreieck berechnen'],
  '2022-OS-K5b: sin α = 7,4 : 14,1.')
T('trigonometrie', '2.6', 'aus Ankathete und Hypotenuse (cos⁻¹)', ['Winkel im rechtwinkligen Dreieck berechnen'],
  '2019-OS-K3b, 2024-OS-K6b und 2026-FOR-K4b rechnen den Winkel mit cos⁻¹.')
T('trigonometrie', '2.7', 'aus beiden Katheten (tan⁻¹)', ['Winkel im rechtwinkligen Dreieck berechnen'],
  '2020-OS-K5b (tan α = 14/9), als Nebentyp 2025-OS-K4a (tan α = 16 : 170) und 2019-OS-K2d (tan β = 4/2).')
T('trigonometrie', '2.8', 'Runden auf eine Dezimale, Gradzeichen', ['Winkel im rechtwinkligen Dreieck berechnen'],
  'Ergebnisse der Originale auf eine Dezimale, etwa 2022-OS-K5b (α ≈ 31,7°) und 2024-OS-K6b (β1 ≈ 48,4°).')
T('trigonometrie', '2.9', 'zweiter spitzer Winkel als Ergänzung zum rechten Winkel, Kontrolle mit der zweiten Funktion', ['Winkelsumme im Dreieck anwenden', 'Winkel im rechtwinkligen Dreieck berechnen'],
  '2022-OS-K5c: γ₁ = 180° − 90° − α (Definition „Dritten Winkel … aus der Winkelsumme“); die zweite Funktion ist der Alternativweg in 2022-OS-K5b (cos α = 12 : 14,1) und 2024-OS-K6b.')
T('trigonometrie', '2.10', 'Steigungswinkel einer Rampe oder Seilbahn aus Höhe und Länge', ['Winkel im rechtwinkligen Dreieck berechnen', 'Neigungswinkel einer Geraden berechnen'],
  'Rampe 2025-OS-K4a (Nebentyp), Seilbahn 2024-OS-K6b; Steigungswinkel der Seilbahn über den Tangens in 2020-GYM-K4b.')
T('trigonometrie', '2.11', 'Winkel eines Dreiecks im Koordinatensystem aus abgelesenen Katheten (P10-Form)', ['Winkel im rechtwinkligen Dreieck berechnen', 'Neigungswinkel einer Geraden berechnen'],
  '2019-OS-K2d: tan β = 4/2 im Koordinatendreieck (Nebentyp); Definition des GYM-Typs, Winkel einer Geraden zur x-Achse über den Tangens (2018-GYM-K2d).')
T('trigonometrie', '2.12', 'Winkel im Teildreieck mit gezeichneter Höhe', ['Winkel im rechtwinkligen Dreieck berechnen'],
  '2022-OS-K5b: α im Teildreieck ADC mit der Höhe hc.')
T('trigonometrie', '2.13', 'Nachweis mit vorgegebenem Winkel („Zeigen Sie rechnerisch, dass α ≈ …“; P10-Form)', ['Winkel im rechtwinkligen Dreieck berechnen'],
  '2019-OS-K3b („also rund 64°“) und 2026-FOR-K4b (Nachweis ε ≈ 66°).')
T('trigonometrie', '2.14', 'Winkel prüfen: die längere Kathete liegt dem größeren Winkel gegenüber', ['Winkel im rechtwinkligen Dreieck berechnen'],
  'Kontrollschritt gegen die Fehlerquelle „Katheten vertauscht“, die den anderen spitzen Winkel liefert (2020-OS-K5b 32,7° statt 57,3°, 2019-OS-K2d 26,6°).')
T('trigonometrie', '3.1', 'rechtwinkliges Teildreieck in der Figur markieren, rechten Winkel und gegebenen Winkel finden, Seiten vom Winkel aus benennen', ['Seite im rechtwinkligen Dreieck berechnen', 'Winkel im rechtwinkligen Dreieck berechnen'],
  'Teilschritt der Figurenaufgaben: Dreieck AFC in 2026-FOR-K4c, Teildreiecke ABF und CBF in 2023-OS-K7b, Hilfsdreieck im Trapez 2020-OS-K5b.')
T('trigonometrie', '3.2', 'Höhe im gleichschenkligen Dreieck aus Schenkel und Basiswinkel', ['Seite im rechtwinkligen Dreieck berechnen'],
  'Definition „Seite aus einer Seite und einem Winkel“ im halben gleichschenkligen Dreieck; kein Original mit dieser Figur, verwandt die Kegelhöhe im gleichschenkligen Achsenschnitt 2015-GYM-K4a.')
T('trigonometrie', '3.3', 'Höhe im beliebigen Dreieck aus Seite und Winkel, dann Fläche (Typ in flaechen.md)', ['Flächeninhalt Dreieck berechnen', 'Seite im rechtwinkligen Dreieck berechnen'],
  '2022-OS-K5e und 2015-OS-K5d: Teilstrecken über Sinus oder Tangens (Nebentyp „Seite im rechtwinkligen Dreieck berechnen“), dann die Fläche (Definition „Flächeninhalt Dreieck berechnen“).')
T('trigonometrie', '3.4', 'Trapez: Schenkel aus Höhe und Basiswinkel, Höhe aus Schenkel und Winkel, Überstand mit dem Tangens', ['Umfang Trapez berechnen', 'Seite im rechtwinkligen Dreieck berechnen'],
  'Definition „Umfang eines Trapezes …, dessen Schenkel erst über Trigonometrie … bestimmt werden müssen“, 2023-OS-K2c (s = 8 : sin 56°, Nebentyp „Seite …“); Höhe aus Schenkel und Winkel in 2023-GYM-K6d (x = b · sin β).')
T('trigonometrie', '3.5', 'rechtwinkliges Trapez: Hilfsdreieck mit der Differenz der beiden Höhen als Kathete, Winkel darin (P10-Form)', ['Winkel im rechtwinkligen Dreieck berechnen', 'Strecke aus Teilstrecken berechnen'],
  '2020-OS-K5b: Kathete 15 − 6 = 9 (Nebentyp „Strecke aus Teilstrecken berechnen“), dann tan α = 14/9.')
T('trigonometrie', '3.6', 'Parallelogramm: Höhe mit Fußpunkt auf der Verlängerung, Winkel dort, Diagonale aus Höhe und Winkel', ['Seite im rechtwinkligen Dreieck berechnen', 'Winkel im rechtwinkligen Dreieck berechnen'],
  '2026-FOR-K4b (Winkel ε an der Verlängerung) und 2026-FOR-K4c (Diagonale AC = 29,24 : sin 22°).')
T('trigonometrie', '3.7', 'Drachen und Raute: halbe Diagonale aus Seite und Winkel', ['Diagonale eines Drachenvierecks über Winkelfunktion berechnen', 'Seite im rechtwinkligen Dreieck berechnen'],
  'Definition des GYM-Typs (2018-GYM-K4a, TM = 51 · sin β₁); 2018-GYM-K4b (LM = 51 · cos β₁) und der zweite Weg in 2015-OS-K5c (AE = 4,1 · sin 21°) als „Seite im rechtwinkligen Dreieck berechnen“.')
T('trigonometrie', '3.8', 'Vermessung: Höhe eines Turms oder Bergs aus Abstand und Höhenwinkel, Gerätehöhe oder Sockel addieren (P10-Form)', ['Seite im rechtwinkligen Dreieck berechnen', 'Strecke aus Teilstrecken berechnen'],
  '2018-OS-K4d: CB = 112,8 · sin 30° plus Gerätehöhe 1,5 m (Nebentyp „Strecke aus Teilstrecken berechnen“); ebenso 2016-GYM-K4d (8 m plus 37,6 · sin 30°).')
T('trigonometrie', '3.9', 'Plattform oder Aufbau zur Höhe addieren', ['Strecke aus Teilstrecken berechnen', 'Seite im rechtwinkligen Dreieck berechnen'],
  '2018-OS-K4d: Höhe von D mit der Plattform 12,0 m (69,9 m), Nebentyp „Strecke aus Teilstrecken berechnen“.')
T('trigonometrie', '3.10', 'Teilwinkel: den Winkel des Teildreiecks als Differenz zweier gegebener Winkel bilden (P10-Form)', ['Winkel aus Teilwinkeln berechnen', 'Seite im rechtwinkligen Dreieck berechnen'],
  '2016-OS-K7c: Winkel DAB = 70° − 36° als Nebentyp „Winkel aus Teilwinkeln berechnen“, dann BD = AD · tan 34°.')
T('trigonometrie', '3.11', 'zwei Teildreiecke nacheinander an derselben Höhe (P10-Form)', ['Seite im rechtwinkligen Dreieck berechnen', 'Diagonale eines Drachenvierecks über Winkelfunktion berechnen'],
  '2023-OS-K7b: BF im Dreieck ABF, dann BC im Dreieck CBF; Definition des GYM-Typs „zwei rechtwinklige Teildreiecke mit gemeinsamer Kathete“ (2018-GYM-K4a).')
T('trigonometrie', '3.12', 'Strecke aus Teilstrecken nach der Trigonometrie', ['Strecke aus Teilstrecken berechnen', 'Seite im rechtwinkligen Dreieck berechnen'],
  'Nebentyp „Strecke aus Teilstrecken berechnen“ in 2018-OS-K4d und 2020-OS-K5b; BD = DE + EB aus zwei Teildreiecken im zweiten Weg von 2015-OS-K5c.')
T('trigonometrie', '3.13', 'Rechenweg als Lösungsplan ohne Zahlen (P10-Form)', ['Flächeninhalt Dreieck berechnen', 'Seite im rechtwinkligen Dreieck berechnen', 'Formel über Winkelfunktion herleiten'],
  'Definition „Flächeninhalt Dreieck berechnen … auch als Beschreibung des Rechenwegs ohne Zahlen“, 2015-OS-K5d mit Nebentyp „Seite …“ (AE = AD · sin δ); die allgemeine Formel über ein Teildreieck in 2021-GYM-K5a.')
T('trigonometrie', '3.14', 'zweiter Weg mit dem Satz des Pythagoras, Vergleich der Ergebnisse', ['Pythagoras Kathete', 'Seite im rechtwinkligen Dreieck berechnen'],
  '2016-OS-K7b führt beide Wege („Pythagoras Kathete“, Nebentyp 920 · sin 54°), 2021-OS-K3b lässt den Pythagoras neben dem Kosinus zu.')
T('trigonometrie', '3.15', 'Seitenhöhe oder Mantellinie aus Grundkante oder Radius und Neigungswinkel im Stützdreieck (kein P10-Original, RLP G, LISUM-PH „Körper“)', ['Seite im rechtwinkligen Dreieck berechnen', 'Formel über Winkelfunktion herleiten'],
  'Stützdreieck im Kegel aus Radius und halbem Öffnungswinkel in 2015-GYM-K4a (h = r : tan 30°) und 2021-GYM-K5a (Tiefe über tan(α/2)); dort ist die Höhe gesucht, nicht die Mantellinie.')
T('trigonometrie', '4.1', 'rechtwinklig oder nicht: sin, cos, tan oder Sinussatz (Vorstufe)', ['Sinussatz Seite berechnen', 'Kosinussatz Seite berechnen'],
  'Fehlerquelle „Dreieck ACD als rechtwinklig behandeln“ in 2018-OS-K4c und „Satz des Pythagoras statt Kosinussatz“ in 2015-GYM-K5a.')
T('trigonometrie', '4.2', 'Seite und Gegenwinkel als Paar markieren, das vollständige Paar finden', ['Sinussatz Seite berechnen', 'Sinussatz Winkel berechnen'],
  'Fehlerquelle „falsche Paarung Seite–Gegenwinkel“ in 2025-OS-K4c und 2024-OS-K6d, ebenso in 2025-GYM-K4b beim Winkel.')
T('trigonometrie', '4.3', 'dritter Winkel aus der Winkelsumme', ['Winkelsumme im Dreieck anwenden', 'Sinussatz Seite berechnen'],
  'Nebentyp „Winkelsumme im Dreieck anwenden“ in 2019-OS-K3c, 2020-OS-K7c und 2021-OS-K3c; Schritt im Verfahren von 2024-OS-K6d (γ = 34°) und 2025-OS-K4c.')
T('trigonometrie', '4.4', 'Sinussatz aufstellen (Seite durch Sinus des Gegenwinkels gleich Seite durch Sinus des Gegenwinkels)', ['Sinussatz Seite berechnen', 'Sinussatz Winkel berechnen'],
  'Erster Schritt beider Sinussatz-Typen (2024-OS-K6d, 2015-GYM-K5b).')
T('trigonometrie', '4.5', 'nach der Seite umstellen und mit dem Taschenrechner berechnen', ['Sinussatz Seite berechnen'],
  '2024-OS-K6d: BC = 384 · sin 38° : sin 34°.')
T('trigonometrie', '4.6', 'stumpfer Winkel im Sinussatz (Taschenrechner rechnet direkt; der stumpfe Winkel gehört in die Winkelsumme)', ['Sinussatz Seite berechnen'],
  'Stumpfe Winkel in vier Originalen: 2015-OS-K5c (123°), 2020-OS-K7c (115°), 2024-OS-K6d (108°), 2025-OS-K4c (141°).')
T('trigonometrie', '4.7', 'Nachweis mit vorgegebenem Ergebnis (P10-Form)', ['Sinussatz Seite berechnen', 'Behauptung prüfen'],
  '2018-OS-K4c: Nachweis AC ≈ 112,8 m, Nebentyp „Behauptung prüfen“ zu genau dieser Behauptung.')
T('trigonometrie', '4.8', 'Aussage über zwei Seiten prüfen (P10-Form)', ['Sinussatz Seite berechnen', 'Behauptung prüfen'],
  '2021-OS-K3c: Aussage „BC ist genauso lang wie DC“ mit Nebentyp „Behauptung prüfen“.')
T('trigonometrie', '4.9', 'Sinussatz im Viereck mit Diagonale: Teilwinkel zuerst, dann das Dreieck mit dem vollständigen Paar wählen (P10-Form)', ['Sinussatz Seite berechnen'],
  '2019-OS-K3c (Teilwinkel 26° und 60°) und 2021-OS-K3c (35°, 74°, 46°) im Viereck mit Diagonale.')
T('trigonometrie', '4.10', 'Seite als Teil einer Weglänge oder Differenz zu einer Teilstrecke (P10-Form)', ['Sinussatz Seite berechnen', 'Strecke aus Teilstrecken berechnen'],
  '2014-OS-K2b (plus 2500 m) und 2020-OS-K7c (DP = DE − 10), beide mit Nebentyp „Strecke aus Teilstrecken berechnen“.')
T('trigonometrie', '4.11', 'zweiter Weg über zwei rechtwinklige Teildreiecke mit der Höhe (Vergleich)', ['Seite im rechtwinkligen Dreieck berechnen'],
  'Nebentyp „Seite im rechtwinkligen Dreieck berechnen“ als zweiter Weg über die Höhe in 2014-OS-K2b und 2015-OS-K5c.')
T('trigonometrie', '4.12', 'Winkel mit dem Sinussatz (kein P10-Original, RLP G)', ['Sinussatz Winkel berechnen'],
  'GYM-Typ mit Definition „einen Winkel mit dem Sinussatz … berechnen“; 2015-GYM-K5b und 2025-GYM-K4b.')
T('trigonometrie', '4.13', 'Kosinussatz für die dritte Seite aus zwei Seiten und dem eingeschlossenen Winkel (kein P10-Original, RLP G)', ['Kosinussatz Seite berechnen'],
  'GYM-Typ mit Definition „eine Seite aus den zwei anliegenden Seiten und dem eingeschlossenen Winkel“; 2015-GYM-K5a, 2021-GYM-K4c, 2025-GYM-K4c.')
T('trigonometrie', '4.14', 'Kosinussatz nach dem Winkel umgestellt (Vorrat, RLP H, LISUM-PH „nur GYM“)', ['Kosinussatz Winkel berechnen'],
  'GYM-Typ mit Definition „einen Winkel aus den drei gegebenen Seiten mit dem Kosinussatz“; 2014-GYM-K5b und 2020-GYM-K4c.')

# ==== winkel-dreiecke ====
U('winkel-dreiecke', 1, ['Winkel aus Teilwinkeln berechnen', 'Strecke aus Teilstrecken berechnen'])
U('winkel-dreiecke', 2, ['Winkel über Scheitel- oder Nebenwinkel bestimmen', 'Winkel an geschnittenen Parallelen bestimmen', 'Winkel im Viereck berechnen'])
U('winkel-dreiecke', 3, ['Winkelsumme im Dreieck anwenden', 'Gleichschenkliges Dreieck erkennen', 'Eigenschaft einer Figur zuordnen', 'Rechten Winkel begründen'])
U('winkel-dreiecke', 4, ['Dreiecksungleichung anwenden'])
T('winkel-dreiecke', '1.5', 'Winkel mit gegebener Größe an einen Schenkel zeichnen', ['Kreisdiagramm zeichnen', 'Vieleck aus Seiten und Winkeln im Maßstab konstruieren'],
  'Der Sektor wird mit dem berechneten Winkel an einen Radius angetragen (2015-OS-K7c „Sektor mit 52° am Radius abtragen“, 2017-OS-K2c mit 40°); im GYM-Typ werden 155° und 63° angetragen (2021-GYM-K4a).')
T('winkel-dreiecke', '1.6', 'Winkel benennen, Scheitel und Schenkel markieren', ['Winkel in zusammengesetzter Figur kennzeichnen'],
  'Definition „einen … Winkel markieren“; 2025-GYM-B1a kennzeichnet γ und δ in der Figur.')
T('winkel-dreiecke', '1.7', 'Winkel aus Teilwinkeln (nebeneinander: Summe; ineinander: Differenz; Rest zum gestreckten oder vollen Winkel)', ['Winkel aus Teilwinkeln berechnen', 'Winkel in zusammengesetzter Figur kennzeichnen'],
  'Definition „Winkel als Differenz oder Summe gegebener Winkel“, 2018-OS-K4a (35° − 30°); den doppelt so großen Winkel als Summe zweier β kennzeichnet 2025-GYM-B1a.')
T('winkel-dreiecke', '1.8', 'Strecke aus Teilstrecken (Summe, Differenz, Einheiten m/km)', ['Strecke aus Teilstrecken berechnen'],
  'Definition „als Summe oder Differenz gegebener Teilstrecken, ggf. nach Umrechnung“; 2016-OS-K7a und 2014-OS-K2a (Meter und Kilometer).')
T('winkel-dreiecke', '2.1', 'Scheitel- und Nebenwinkel benennen', ['Winkel über Scheitel- oder Nebenwinkel bestimmen'],
  'Teilschritt: 2019-OS-B1a erkennt β und 35° als Scheitelwinkel, 2014-OS-B1f hat die Fehlerquelle „Nebenwinkel statt Scheitelwinkel“.')
T('winkel-dreiecke', '2.2', 'aus einem Winkel die drei anderen an der Kreuzung', ['Winkel über Scheitel- oder Nebenwinkel bestimmen'],
  'Definition „über Scheitel- oder Nebenwinkel …, ohne Parallelen“; 2014-OS-B1f an der Kreuzung zweier Geraden.')
T('winkel-dreiecke', '2.3', 'drei Geraden durch einen Punkt (Teilwinkel, Scheitelwinkel minus Teil)', ['Winkel über Scheitel- oder Nebenwinkel bestimmen', 'Winkel aus Teilwinkeln berechnen'],
  '2014-OS-B1f: β = 50° − 30° am Scheitelwinkel, Nebentyp „Winkel aus Teilwinkeln berechnen“.')
T('winkel-dreiecke', '2.4', 'Stufenwinkel an Parallelen', ['Winkel an geschnittenen Parallelen bestimmen'],
  'Definition „über Stufen-, Wechsel-, Scheitel- oder Nebenwinkel“; Stufenwinkel in 2020-OS-B1g und 2020-GYM-B1b.')
T('winkel-dreiecke', '2.5', 'Wechselwinkel', ['Winkel an geschnittenen Parallelen bestimmen'],
  '2020-OS-B1g: α = 74° als Wechselwinkel an Parallelen.')
T('winkel-dreiecke', '2.6', 'Nebenwinkel des Stufenwinkels (180° − …)', ['Winkel an geschnittenen Parallelen bestimmen'],
  '2015-OS-B1d: α = 180° − 53°.')
T('winkel-dreiecke', '2.7', 'Winkel an einer Figur mit verlängerten Seiten (Scheitelwinkel des Innenwinkels; überflüssige Angabe)', ['Winkel über Scheitel- oder Nebenwinkel bestimmen', 'Winkelsumme im Dreieck anwenden'],
  'Definition „in einer Figur mit verlängerten Seiten … überflüssige Angaben erkennen“, 2019-OS-B1a; Nebenwinkel 120° an der verlängerten Seite in 2018-OS-K4b („Winkelsumme im Dreieck anwenden“).')
T('winkel-dreiecke', '2.8', 'Winkel im Parallelogramm und Trapez an den parallelen Seiten', ['Winkel im Viereck berechnen', 'Eigenschaft einer Figur zuordnen'],
  'Definition „in Trapez oder Parallelogramm über Neben- oder Gegenwinkel an den parallelen Seiten“ (2026-FOR-B1i, 2023-OS-K2a); 2016-OS-B1e fragt „gegenüberliegende Winkel gleich groß“.')
T('winkel-dreiecke', '3.1', 'dritter Winkel im Dreieck (ganze Grade, Dezimalgrade)', ['Winkelsumme im Dreieck anwenden'],
  'Definition „Dritten Winkel eines Dreiecks aus der Winkelsumme 180°“; 2015-OS-K5b (ganze Grade) und 2017-OS-K4a (Dezimalgrade).')
T('winkel-dreiecke', '3.2', 'fehlender Winkel im Viereck (360°)', ['Winkel im Viereck berechnen'],
  '2021-OS-B1i: α = 360° − 50° − 140° − 130°.')
T('winkel-dreiecke', '3.3', 'Dreieck nach Winkeln und Seiten einteilen (Ankreuzen)', ['Dreiecksart aus Koordinaten nachweisen'],
  'Der GYM-Typ verlangt den Nachweis „gleichschenklig und rechtwinklig“ und setzt die Einteilung nach Seiten und Winkeln voraus (2024-GYM-K3c).')
T('winkel-dreiecke', '3.4', 'gleichschenklig: Basiswinkel gleich, dritter Winkel', ['Winkelsumme im Dreieck anwenden'],
  '2023-OS-B1g: γ = 180° − 2 · 70° bei gleichen Basiswinkeln (Nebentyp).')
T('winkel-dreiecke', '3.5', 'aus gleichen Winkeln auf gleiche Schenkel schließen (Seite angeben)', ['Gleichschenkliges Dreieck erkennen'],
  'Definition „aus gleichen Basiswinkeln auf gleiche Schenkel schließen, als Angabe der Seite“; 2023-OS-B1g (BC = 6 cm).')
T('winkel-dreiecke', '3.6', 'gleichseitig 60°', ['Winkelsumme im Dreieck anwenden'],
  'Drei gleiche Winkel aus der Winkelsumme 180° (Definition); kein Original mit gleichseitigem Dreieck.')
T('winkel-dreiecke', '3.7', 'rechtwinklig: die zwei spitzen Winkel ergeben 90°', ['Winkelsumme im Dreieck anwenden'],
  '2022-OS-K5c (γ₁ = 180° − 90° − α) und der zweite Weg in 2018-OS-K4b (δ und der Winkel bei A ergänzen sich zu 90°).')
T('winkel-dreiecke', '3.8', 'Winkel im Teildreieck (Höhe, Diagonale, Drachen mit rechtem Winkel der Diagonalen)', ['Winkelsumme im Dreieck anwenden', 'Rechten Winkel begründen', 'Gleichschenkliges Dreieck erkennen'],
  'Teildreieck mit Höhe 2022-OS-K5c, Drachen-Teildreieck 2015-OS-K5b; 45° im Teildreieck AFD mit rechtem Winkel der Diagonalen in 2025-OS-K2c, 45° im Teildreieck ABF an der Höhe in 2023-OS-K7a.')
T('winkel-dreiecke', '3.9', 'rechten Winkel begründen (gleichschenklig-rechtwinklig 45° + 45°; Winkelsumme)', ['Rechten Winkel begründen'])
T('winkel-dreiecke', '3.11', 'Vierecksart-Eigenschaft ankreuzen („In jedem Trapez …“, „In jedem Parallelogramm …“)', ['Eigenschaft einer Figur zuordnen', 'Streckenlänge im Vieleck begründen'],
  'Originale 2026-FOR-B1c („In jedem Trapez …“) und 2016-OS-B1e („In jedem Parallelogramm …“); die Parallelogramm-Eigenschaft „Gegenseiten gleich lang“ trägt den GYM-Typ in 2022-GYM-K5b.')
T('winkel-dreiecke', '4.4', 'SWS', ['Vieleck aus Seiten und Winkeln im Maßstab konstruieren'],
  'Definition „aus einer Folge gegebener Seitenlängen und eingeschlossener Winkel … konstruieren“, Schritt für Schritt Seite, eingeschlossener Winkel, Seite (2021-GYM-K4a).')
T('winkel-dreiecke', '4.9', 'Dreiecksungleichung: konstruierbar oder nicht (b + c > a)', ['Dreiecksungleichung anwenden'],
  'Definition „Summe zweier Dreiecksseiten zur dritten (b + c > a)“; 2020-OS-B1i mit der Fehlerquelle entartetes Dreieck.')
T('winkel-dreiecke', '4.10', 'kongruente Figuren erkennen und Ecken zuordnen', ['Winkel in zusammengesetzter Figur kennzeichnen'],
  'Definition „unter Nutzung der Kongruenz der Teildreiecke“: 2025-GYM-B1a kennzeichnet den gleich großen Winkel am entsprechenden Punkt des kongruenten Dreiecks.')
T('winkel-dreiecke', '5.8', 'rechten Winkel mit Thales begründen', ['Rechten Winkel begründen', 'Dreiecksart aus Koordinaten nachweisen'],
  'Definition „Rechten Winkel begründen“ nennt Thales als Weg (2025-OS-K2c, Alternative); 2024-GYM-K3c weist den rechten Winkel bei C über CM = AB : 2 mit dem Satz des Thales nach.')

# ==== symmetrie-abbildungen ====
U('symmetrie-abbildungen', 1, ['Lage eines Punktes zu den Achsen erkennen'])
U('symmetrie-abbildungen', 2, ['Symmetrieachsen bestimmen', 'Figur nach Spiegelung benennen'])
T('symmetrie-abbildungen', '1.1', 'Achsen und Ursprung benennen, Einteilung ablesen', ['Lage eines Punktes zu den Achsen erkennen'],
  'Definition unterscheidet x-Achse, y-Achse und Ursprung; Vorstufe von 2020-OS-B1b.')
T('symmetrie-abbildungen', '1.2', 'Punkt im ersten Quadranten eintragen', ['Wertetabelle als Punkte darstellen'],
  'Definition „Wertepaare einer Tabelle in ein vorgegebenes Koordinatensystem eintragen“; 2025-OS-K7a mit Punkten im ersten Quadranten.')
T('symmetrie-abbildungen', '1.3', 'Koordinaten eines eingezeichneten Punktes ablesen', ['Scheitelpunkt ablesen', 'Schnittpunkt am Graphen ablesen', 'Streckenlänge aus Koordinaten berechnen'],
  'Scheitel am Graphen ablesen (2021-OS-B1d), Schnittpunkt am Bild ablesen (2023-OS-K4a), Punkte nur im Bild gegeben in 2019-OS-K2d (Fehlerquelle „Koordinaten falsch ablesen“).')
T('symmetrie-abbildungen', '1.4', 'Schreibweise P(x | y) lesen und schreiben (erste Zahl nach rechts, zweite nach oben)', ['Lage eines Punktes zu den Achsen erkennen', 'Scheitelpunkt ablesen'],
  '2020-OS-B1b liest D(3|0) gegen B(0|2); Fehlerquelle „Koordinaten vertauschen“ beim Scheitelpunkt in 2021-OS-B1d (S(−1|−2)) und 2018-OS-K5b.')
T('symmetrie-abbildungen', '1.5', 'Punkte mit negativen Koordinaten eintragen (vier Quadranten)', ['Gerade durch zwei Punkte zeichnen', 'Wertetabelle als Punkte darstellen'],
  'A(−2|6) und B(3|−1,5) eintragen in 2025-OS-K5a, K(−4|−1) in 2017-OS-K5a; Punkte mit negativem x in 2021-GYM-K3a.')
T('symmetrie-abbildungen', '1.7', 'Lage zu den Achsen erkennen: Punkt auf der Rechtsachse, auf der Hochachse, im Ursprung (P10-Form)', ['Lage eines Punktes zu den Achsen erkennen'],
  'Definition „auf der x-Achse (y = 0), der y-Achse (x = 0) oder im Ursprung“; Original 2020-OS-B1b.')
T('symmetrie-abbildungen', '1.10', 'Streckenlänge parallel zu einer Achse abzählen', ['Streckenlänge aus Koordinaten berechnen', 'Flächeninhalt eines Dreiecks aus Koordinaten berechnen', 'Umfang eines Dreiecks aus Koordinaten berechnen'],
  'Achsenparallele Katheten AB = 2 und AC = 4 in 2019-OS-K2d; Grundseite und Höhe parallel zu den Achsen in 2016-GYM-K2e und 2024-GYM-B1a, Seiten OP = 2 und PR = 5 in 2015-GYM-K2c.')
T('symmetrie-abbildungen', '2.1', 'Symmetrieachse einer Figur einzeichnen', ['Symmetrieachsen bestimmen'],
  'Definition „Anzahl oder Lage der Symmetrieachsen einer Figur angeben“.')
T('symmetrie-abbildungen', '2.2', 'prüfen, ob eine eingezeichnete Gerade Symmetrieachse ist (falten oder messen)', ['Symmetrieachsen bestimmen'],
  'Beim Zählen wird jede mögliche Achse geprüft; Fehlerquelle „waagerechte Achse wie beim Rechteck“ in 2022-OS-B1i.')
T('symmetrie-abbildungen', '2.3', 'Anzahl der Symmetrieachsen einer Figur angeben (P10-Form: Quadrat, Rechteck, Raute, gleichschenkliges Trapez, Drachenviereck, gleichseitiges und gleichschenkliges Dreieck, Kreis, Buchstaben, Verkehrszeichen)', ['Symmetrieachsen bestimmen'],
  'Definition „Anzahl … der Symmetrieachsen“; 2022-OS-B1i (Trapez), 2021-OS-B1j (Quadrat), 2025-OS-K2a (Drachenviereck).')
T('symmetrie-abbildungen', '2.4', 'Figuren ohne Symmetrieachse erkennen (Parallelogramm)', ['Symmetrieachsen bestimmen'],
  'Die Anzahl null ist eine der Ankreuzoptionen 0 bis 5 in 2021-OS-B1j und 2022-OS-B1i (Definition „Anzahl … angeben“).')
T('symmetrie-abbildungen', '2.5', 'Punkt an einer Geraden spiegeln (Kästchen abzählen)', ['Parabel an der y-Achse spiegeln'],
  '2020-OS-K3d: der Scheitel (−2|−4) wird an der y-Achse zu (2|−4) gespiegelt.')
T('symmetrie-abbildungen', '2.6', 'Figur an einer senkrechten oder waagerechten Geraden spiegeln', ['Parabel an der y-Achse spiegeln'],
  'Definition „Spiegelbild einer Parabel … an der y-Achse skizzieren“; 2020-OS-K3d verlangt die Skizze.')
T('symmetrie-abbildungen', '2.7', 'Figur an einer schrägen Achse spiegeln (Vorrat)', ['Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen'],
  'Definition „durch Spiegelung an der Geraden y=x skizzieren“; 2020-GYM-K3b.')
T('symmetrie-abbildungen', '2.8', 'Figur an einer Koordinatenachse spiegeln und die Koordinaten des Bildpunkts angeben', ['Parabel an der y-Achse spiegeln', 'Parabel an der x-Achse spiegeln', 'Gerade an der x-Achse spiegeln', 'Graph einer Exponentialfunktion an der y-Achse spiegeln'],
  'Spiegelbild an einer Koordinatenachse mit Bildpunkt: 2020-OS-K3d (Scheitel (2|−4)), Definition „Parabel an der x-Achse spiegeln“ (Scheitel-y-Wert wechselt, Graph in 2023-GYM-K3c), Spiegelbild zeichnen in 2014-GYM-K2b und 2018-GYM-K2c.')
T('symmetrie-abbildungen', '2.10', 'die Figur aus Dreieck und Spiegelbild benennen (P10-Form: Drachenviereck, bei gleichschenkligem Dreieck Raute)', ['Figur nach Spiegelung benennen'],
  'Definition „welche Figur beim Spiegeln … zusammen mit dem Urbild entsteht“; Original 2018-OS-B1h.')
T('symmetrie-abbildungen', '2.11', 'Symmetrie der Vierecksarten im Haus der Vierecke zuordnen', ['Symmetrieachsen bestimmen'],
  'Achsenzahl von Vierecksarten: gleichschenkliges Trapez 2022-OS-B1i, Quadrat 2021-OS-B1j, Drachenviereck 2025-OS-K2a.')
T('symmetrie-abbildungen', '2.12', 'Symmetrieachse als Diagonale nutzen (Drachenviereck: die Achse halbiert die andere Diagonale senkrecht; Voraussetzung in pythagoras.md)', ['Symmetrieachsen bestimmen', 'Pythagoras Hypotenuse', 'Figur nach Spiegelung benennen', 'Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen'],
  '2025-OS-K2a: Achse BD, AF = AC : 2 für die Hypotenuse AB (Fehlerquelle AF = 50 cm); 2018-OS-B1h begründet das Drachenviereck mit der halbierten Diagonale; 2017-GYM-K3b halbiert die 15-m-Diagonale.')
T('symmetrie-abbildungen', '3.7', 'Figur mit einem Pfeil verschieben (Länge und Richtung)', ['Parabel verschieben'],
  '2015-OS-B1i: Scheitel der Normalparabel um 2 nach rechts, S(2|0) (Definition „oder nur den neuen Scheitelpunkt nennen“); ebenso 2017-GYM-K2b.')
T('symmetrie-abbildungen', '3.8', 'Verschiebung im Koordinatensystem beschreiben (so viele Kästchen nach rechts, so viele nach oben)', ['Parabeltransformation gegenüber der Normalparabel beschreiben'],
  'Definition „beschreiben, durch welche Verschiebung … eine Parabel aus der Normalparabel entstanden ist“; 2022-GYM-K3a (2,5 nach rechts, 1 nach unten).')
T('symmetrie-abbildungen', '3.12', 'Abbildung benennen, die zwei gegebene Figuren ineinander überführt', ['Graph einer Exponentialfunktion an der y-Achse spiegeln', 'Parabeltransformation gegenüber der Normalparabel beschreiben'],
  '2025-GYM-K3f benennt die Spiegelung an der y-Achse, die f in g überführt; 2022-GYM-K3a die Verschiebung der Normalparabel.')

# ==== strahlensaetze ====
U('strahlensaetze', 1, ['Länge im Maßstab umrechnen', 'Draufsicht maßstabsgerecht zeichnen'])
T('strahlensaetze', '1.1', 'Maßstab lesen und in Worten sagen (1 : 200 – ein Zentimeter auf dem Plan sind 200 cm = 2 m)', ['Länge im Maßstab umrechnen'],
  'Vorstufe des Umrechnens (Definition „mit einem gegebenen Maßstab“); 2018-OS-K6c mit 1 : 50.')
T('strahlensaetze', '1.3', 'Länge von der Wirklichkeit in die Zeichnung umrechnen: durch n teilen, vorher in cm umrechnen (Zaun 4 m bei 1 : 200 → 2 cm)', ['Länge im Maßstab umrechnen', 'Draufsicht maßstabsgerecht zeichnen', 'Vieleck aus Seiten und Winkeln im Maßstab konstruieren'],
  '2018-OS-K6c (30 m : 50 = 60 cm) und 2017-GYM-K3a (850 cm : 250); in der Draufsicht 2021-OS-K4c 55 cm → 5,5 cm, im GYM-Typ 30 m → 6 cm bei 1 : 500 (2021-GYM-K4a).')
T('strahlensaetze', '1.4', 'Länge von der Zeichnung in die Wirklichkeit: mal n, Ergebnis in eine sinnvolle Einheit (3 cm bei 1 : 200 → 600 cm = 6 m)', ['Länge im Maßstab umrechnen', 'Maße aus Netz im Maßstab ablesen'],
  '2015-OS-K6a (0,68 m · 10 = 6,8 m); Definition des GYM-Typs „durch Ausmessen der Zeichnung und Umrechnen über den Maßstab“ (2020-GYM-K5b, mal 3).')
T('strahlensaetze', '1.5', 'Modellmaße aus Originalmaßen (h = 30 m, 1 : 50 → 60 cm; P10-Form) und Originalmaße aus Modellmaßen (0,68 m bei 1 : 10 → 6,8 m; P10-Form)', ['Länge im Maßstab umrechnen'],
  'Definition „Originalmaße … in Modellmaße umrechnen (oder umgekehrt)“; 2018-OS-K6c und 2015-OS-K6a.')
T('strahlensaetze', '1.6', 'zwei Größen in einer Aufgabe umrechnen (Höhe und Durchmesser)', ['Länge im Maßstab umrechnen'],
  '2018-OS-K6c (Höhe und Durchmesser) und 2015-OS-K6a (Höhe und Grundkante; Fehlerquelle „nur eine der beiden Größen“).')
T('strahlensaetze', '1.8', 'Kästchenmaßstab eines Rasters lesen (ein Kästchen ≙ 2 cm; Voraussetzung in koerper.md)', ['Netz eines Prismas vervollständigen'],
  '2020-OS-K5a (15 cm als 7,5 Kästchen, ein Kästchen ≙ 2 cm) und 2019-OS-K4a (1,50 m als 5 Kästchen, ein Kästchen ≙ 0,3 m).')
T('strahlensaetze', '1.10', 'Rechteck und Kreis im gegebenen Maßstab zeichnen (Durchmesser umrechnen, Radius halbieren, Zirkel)', ['Draufsicht maßstabsgerecht zeichnen', 'Länge im Maßstab umrechnen'],
  '2021-OS-K4c: Rechteck 5,5 cm × 8 cm und Kreis d = 5,8 cm; 2017-GYM-K3a zeichnet eine Figur im gegebenen Maßstab 1 : 250.')
T('strahlensaetze', '1.11', 'Draufsicht eines Körpers als Figur erkennen (Zylinder → Kreis, Quader → Rechteck, Turm auf Platte → Kreis im Rechteck)', ['Draufsicht maßstabsgerecht zeichnen'],
  '2021-OS-K4c: Draufsicht der Regentonne auf der Platte als Kreis im Rechteck.')
T('strahlensaetze', '1.12', 'Maßstab für ein Zeichenfeld wählen (passt 1 : 5, 1 : 10 oder 1 : 20 ins Feld?), angeben und die Zeichnung beschriften (P10-Form)', ['Draufsicht maßstabsgerecht zeichnen', 'Körper im Schrägbild darstellen'],
  'Definition „passenden Maßstab wählen und angeben, Zeichnung beschriften“ (2021-OS-K4c, Fehlerquelle 1 : 5 passt nicht ins Feld); Schrägbild im selbst gewählten Maßstab in 2019-GYM-K4a.')
T('strahlensaetze', '1.13', 'an der Zeichnung entscheiden (bedeckt die Platte die Tonne? Überstand ablesen; P10-Form)', ['Draufsicht maßstabsgerecht zeichnen', 'Behauptung prüfen'],
  '2021-OS-K4c: Entscheidung, ob die Platte die Tonne bedeckt, mit Nebentyp „Behauptung prüfen“.')
T('strahlensaetze', '1.14', 'Landkarte: Strecke aus Kartenzentimetern (1 : 25 000 → 1 cm ≙ 250 m)', ['Länge im Maßstab umrechnen'],
  'Kontextvariante der Definition „mit einem gegebenen Maßstab … umrechnen (oder umgekehrt)“; kein Original mit Landkarte.')
T('strahlensaetze', '2.5', 'Streckfaktor aus einer Original- und Bildstrecke berechnen (k = Bildstrecke : Originalstrecke)', ['Streckenlänge über Ähnlichkeit berechnen'],
  '2021-GYM-K5b: Streckfaktor 13,7 : t aus Füllhöhe und Kegelhöhe.')
T('strahlensaetze', '2.10', 'fehlende Seite in ähnlichen Dreiecken über die Verhältnisgleichung', ['Streckenlänge über Ähnlichkeit berechnen'],
  'Definition „über die Ähnlichkeit von großem und kleinem Kegel bestimmen“; 2021-GYM-K5b und 2023-GYM-K6c.')
T('strahlensaetze', '3.1', 'Strahlensatzfigur erkennen: Zentrum, zwei Geraden, zwei Parallelen (V-Figur und X-Figur)', ['Streckenlänge über Ähnlichkeit berechnen'],
  'Teilschritt: 2023-GYM-K6c nutzt die V-Figur aus Dreieck und paralleler Bereichsgrenze, 2021-GYM-K5b den Achsenschnitt des Kegels.')
T('strahlensaetze', '3.3', 'erster Strahlensatz in der V-Figur: Abschnitte vom Zentrum aus im selben Verhältnis (ZA : ZA′ = ZB : ZB′)', ['Streckenlänge über Ähnlichkeit berechnen'],
  '2021-GYM-K5b: Abschnitt auf der Mantellinie s · 13,7 : t im Verhältnis der Abschnitte auf der Achse.')
T('strahlensaetze', '3.4', 'zweiter Strahlensatz: Parallelen wie die Abschnitte vom Zentrum (AB : A′B′ = ZA : ZA′)', ['Streckenlänge über Ähnlichkeit berechnen'],
  '2023-GYM-K6c: Breite 80 · (1 − 30 : 100) = 56 m an der parallelen Bereichsgrenze.')
T('strahlensaetze', '3.6', 'Verhältnisgleichung aufstellen, gesuchte Strecke allein auf eine Seite, ausrechnen (auch Dezimalzahlen)', ['Streckenlänge über Ähnlichkeit berechnen'],
  'Rechenweg beider Originale 2021-GYM-K5b (13,7 cm und 15,03 cm) und 2023-GYM-K6c.')
T('strahlensaetze', '3.7', 'Abschnitt gesucht, wenn die Gesamtstrecke gegeben ist (ZA′ = ZA + AA′; Teilstrecke berechnen)', ['Streckenlänge über Ähnlichkeit berechnen'],
  '2021-GYM-K5b: Abstand der Markierung vom oberen Rand als s − s · 13,7 : t; 2023-GYM-K6c mit 100 m − 30 m vom Zentrum.')
T('strahlensaetze', '3.8', 'Sachaufgabe mit Skizze: Höhe eines Baums aus Schatten und Stab, Breite eines Flusses aus Peilung, Försterdreieck, Lochkamera, Leiter an der Wand', ['Streckenlänge über Ähnlichkeit berechnen'],
  'Sachkontexte Messbecher (2021-GYM-K5b) und Wohngebiet (2023-GYM-K6c) mit Skizze.')

# ==== zuordnungen ====
U('zuordnungen', 1, ['Wertetabelle als Punkte darstellen', 'Achseneinteilung wählen'])
U('zuordnungen', 2, ['Proportionale Zuordnung Dreisatz'])
U('zuordnungen', 4, ['Kosten aus Menge und Preis berechnen', 'Geschwindigkeit aus Weg und Zeit berechnen', 'Dauer aus Menge und Rate berechnen'])
T('zuordnungen', '1.1', 'Wertetabelle aus Text anlegen', ['Endwert linearer Veränderung berechnen', 'Graph eines exponentiellen Vorgangs zeichnen'],
  'In 2021-OS-K6a sind leere Tabellenfelder aus dem Text zu füllen (Anfangshöhe 40 cm, Höhe nach 80 min), in 2014-GYM-K4b entstehen die Wertepaare aus der Vorschrift „Halbierung je Stunde“ (Definition „aus einer Wertetabelle oder Rekursionsvorschrift“).')
T('zuordnungen', '1.2', 'Punkte ins Koordinatensystem eintragen', ['Wertetabelle als Punkte darstellen', 'Graph eines exponentiellen Vorgangs zeichnen'],
  'Definition „Wertepaare einer Tabelle in ein vorgegebenes Koordinatensystem eintragen“ (2025-OS-K7a, 2021-OS-K6b); Kontextvariante Zerfall in 2014-GYM-K4b.')
T('zuordnungen', '1.3', 'Werte aus Graph ablesen', ['Wert aus Diagramm ablesen', 'Nullstelle am Graphen ablesen'],
  'Definition „Einzelwert … aus einem Funktionsgraphen im Sachzusammenhang (z. B. Startwert bei t = 0) … ablesen“; 2015-OS-K4a liest am Höhe-Zeit-Graphen die Absprunghöhe und als Nullstelle die Zeit bis zur Landung ab.')
T('zuordnungen', '1.4', 'Achseneinteilung für gegebene Werte wählen', ['Achseneinteilung wählen'],
  'Definition „für ein Kästchenraster ohne Skala eine Achseneinteilung wählen, mit der alle Werte einer Tabelle darstellbar sind“; Originale 2021-OS-K6b, 2016-OS-K4b, 2017-OS-K7b.')
T('zuordnungen', '1.6', 'Graph zu Situation qualitativ zuordnen (Füllgraph, Weg-Zeit)', ['Graph zu Tarif zuordnen', 'Graph zu Wachstumsprozess zuordnen'],
  'Beide verlangen zu einer beschriebenen Situation den qualitativ passenden Graphen (Definitionen; 2016-OS-K6a und 2023-OS-K3a für Tarife, 2019-OS-K7c und 2026-FOR-K7b für Wachstum).')
T('zuordnungen', '2.1', 'Tabelle ergänzen durch Verdoppeln und Halbieren', ['Proportionale Zuordnung Dreisatz'],
  'Vorstufe des Dreisatzes mit den Faktoren 2 und ½ (Definition „aus einem Wertepaar den fehlenden vierten Wert“).')
T('zuordnungen', '2.2', 'Hochrechnen (mal 3, mal 10)', ['Proportionale Zuordnung Dreisatz'],
  'Vorstufe des Dreisatzes mit ganzzahligem Faktor (Definition „aus einem Wertepaar den fehlenden vierten Wert“).')
T('zuordnungen', '2.3', 'Runterrechnen', ['Proportionale Zuordnung Dreisatz'],
  '2016-OS-B1d: Fett in 20 g aus 30 g in 100 g durch Runterrechnen (30 : 5).')
T('zuordnungen', '2.4', 'auf eine Portion runterrechnen, dann hochrechnen (Dreisatz, Minitabelle)', ['Proportionale Zuordnung Dreisatz'],
  'Lösungsweg der Originale 2023-OS-B1a (25 : 4 = 6,25 min je km, mal 6) und 2022-OS-B1b (4,80 : 3 = 1,60 € je kg, mal 5).')
T('zuordnungen', '2.5', 'fester Faktor angeben (Preis je Einheit), Gleichung y = k · x', ['Proportionale Zuordnung Dreisatz', 'Lineare Funktion aus Sachverhalt aufstellen'],
  'Fester Faktor als Lösungsweg des Dreisatzes in 2016-OS-B1d („0,3 · 20“); die Gleichung y = k · x ist der Grundfall ohne Anfangswert von „Lineare Funktion aus Sachverhalt aufstellen“ (Definition „Anfangswert und konstante Änderung je Einheit“).')
T('zuordnungen', '2.6', 'Preisvergleich über gleiche Portion', ['Tarife vergleichen'],
  'Definition „Gesamtkosten zweier Tarife … für eine konkrete Nutzung berechnen und den günstigeren wählen“: der Vergleich läuft über dieselbe Menge (2023-OS-K3b: 5 Tage und 470 km; 2017-GYM-K5b: 1000 kWh).')
T('zuordnungen', '2.7', 'Graph zeichnen (Ursprungsgerade) und Werte ablesen', ['Wertetabelle als Punkte darstellen', 'Wert aus Diagramm ablesen'],
  'Zeichnen über eingetragene Wertepaare (Definition „Wertepaare einer Tabelle … eintragen“, in 2021-OS-K6b zur Strecke verbunden) und Ablesen am Funktionsgraphen im Sachzusammenhang (Definition „Wert aus Diagramm ablesen“, 2015-OS-K4a).')
T('zuordnungen', '3.1', 'Tabelle ergänzen: doppelt → halb, dreifach → Drittel', ['Antiproportionale Zuordnung Dreisatz'],
  '2014-GYM-B1c: doppelt so viele Pferde, halb so viele Tage (Vorrat für 4 Pferde 8 Tage, für 8 Pferde 4 Tage).')
T('zuordnungen', '3.2', 'Produkt prüfen (x · y gleich)', ['Antiproportionale Zuordnung Dreisatz'],
  'Definition „über das konstante Produkt“; 2014-GYM-B1c rechnet 4 · 8 = 32 Pferdetage.')
T('zuordnungen', '3.3', 'Dreisatz umgekehrt (auf eine Einheit hochrechnen, dann runter)', ['Antiproportionale Zuordnung Dreisatz'],
  '2014-GYM-B1c: auf ein Pferd hochrechnen (32 Tage), dann durch 8 teilen.')
T('zuordnungen', '3.4', 'Sachtext (Arbeiter und Tage, Pumpen und Stunden, Geschwindigkeit und Fahrzeit bei fester Strecke)', ['Antiproportionale Zuordnung Dreisatz'],
  'Definition „Vorrat für mehr oder weniger Personen oder Tiere“; Sachtext Futtervorrat in 2014-GYM-B1c.')
T('zuordnungen', '3.5', 'Graph als fallende Kurve, Werte ablesen', ['Wertetabelle als Punkte darstellen', 'Wert aus Diagramm ablesen'],
  'Punkte einer Tabelle eintragen und zur fallenden Kurve verbinden verlangen 2016-OS-K4b und 2017-OS-K7b (Nebentyp „Wertetabelle als Punkte darstellen“); Ablesen nach Definition „Wert aus Diagramm ablesen“ (Funktionsgraph im Sachzusammenhang).')
T('zuordnungen', '4.2', 'aus Text (je mehr, desto mehr – reicht nicht: Nullwert prüfen)', ['Graph zu Tarif zuordnen'],
  '2016-OS-K6a: aus dem Text „ohne Grundpreis“ auf die Ursprungsgerade schließen, der Tarif mit 200 € Grundpreis beginnt nicht bei null (Definition „mit oder ohne Grundpreis“).')
T('zuordnungen', '4.3', 'aus Graph (Ursprungsgerade, fallende Kurve, andere)', ['Graph zu Tarif zuordnen', 'Graph einer linearen Funktion erkennen'],
  'Ursprungsgerade gegen Gerade mit Achsenabschnitt in 2016-OS-K6a; unter Gerade, Hyperbelast, Parabel und Streckenzug die Gerade wählen in 2025-OS-B1f.')
T('zuordnungen', '4.4', 'Gegenbeispiele (Alter und Größe, Tarif mit Grundgebühr)', ['Graph zu Tarif zuordnen'],
  'Definition „auch bei rein linearen Tarifen (mit oder ohne Grundpreis)“: der Tarif mit Grundgebühr ist das Gegenbeispiel zur proportionalen Zuordnung (2016-OS-K6a, 2023-OS-K3a).')
T('zuordnungen', '4.5', 'Kosten aus Menge und Preis je Einheit', ['Kosten aus Menge und Preis berechnen'],
  'Definition „Gesamtpreis aus einer … Menge und einem Einheitspreis“; 2014-OS-K4c, 2024-OS-K2d.')
T('zuordnungen', '4.6', 'Geschwindigkeit aus Weg und Zeit mit Einheitenwechsel', ['Geschwindigkeit aus Weg und Zeit berechnen'],
  'Definition „… in die verlangte Einheit (m/s, km/h) umrechnen“; 2015-OS-K4c (5 m/s = 18 km/h).')
T('zuordnungen', '4.7', 'Dauer aus Menge und Rate, Zeiteinheit umrechnen', ['Dauer aus Menge und Rate berechnen', 'Zeiteinheiten umrechnen'],
  'Definition „in die verlangte Zeiteinheit umrechnen“; 2024-OS-K6c und 2015-OS-K3c tragen „Zeiteinheiten umrechnen“ als Nebentyp (120 s = 2 min).')
T('zuordnungen', '4.8', 'Fehler finden (antiproportional gerechnet; Einheit)', ['Fehler in Rechnung erklären und korrigieren'],
  '2014-OS-K4e: im Aufgabenstamm der Kraftstoffkosten den Einheitenfehler (585 € als 585 000 ct) in der Rechnung „Mehrkosten je Kilometer“ finden und berichtigen.')

# ==== terme ====
U('terme', 1, ['Term zu Sachtext angeben'])
T('terme', '1.1', 'Termwert berechnen (auch negative Einsetzung)', ['Termwert berechnen', 'Funktionswert berechnen', 'Term durch Zusammenfassen gleichartiger Glieder vereinfachen'],
  'Definition „auch mit negativen Zahlen“ (2026-FOR-B1g, 2021-OS-B1g); derselbe Schritt als Funktionswert, etwa ½ · (−10) + 1 in 2017-OS-K5b, und nach dem Zusammenfassen in 2025-GYM-B2a (Wert für x = 2).')
T('terme', '1.2', 'Term zu Sachtext angeben (Doppeltes, vermindert um)', ['Term zu Sachtext angeben', 'Lineare Gleichung aus Sachverhalt aufstellen'],
  'Definition „Differenz, Doppeltes, verdreifachen, vermindert um“ (2023-OS-B1h, 2017-OS-B1i); dieselbe Übersetzung als Gleichung in 2016-GYM-B1b („das Achtfache einer Zahl vermindert um zwölf“).')
T('terme', '1.3', 'Term zu Figur angeben (Umfang, Fläche aus Rechtecken)', ['Term zu Figur angeben', 'Term zu Körper angeben'],
  'Definition „Term für Flächeninhalt oder Umfang“ (2025-OS-B1i, 2014-OS-B1g); Kontextvariante am Körper in 2017-OS-K3c und 2022-GYM-B1a (Kantensumme 4 · (3 + 6 + 5)).')
T('terme', '1.4', 'Situation zu Term angeben', ['Gleichung im Sachzusammenhang deuten', 'Gleichung zu Figur erläutern'],
  'Definition „eine gegebene Gleichung als Satz im Sachzusammenhang formulieren“ (2024-OS-K7b: „r + t = 13“); zu einer gegebenen Flächengleichung die Zerlegung der Figur erläutern in 2021-GYM-K4d.')
T('terme', '2.1', 'gleichartige Glieder zusammenfassen', ['Term durch Zusammenfassen gleichartiger Glieder vereinfachen', 'Term mit Klammern und Potenzen vereinfachen', 'Lineare Gleichung lösen', 'Lineares Gleichungssystem lösen'],
  'Definitionen der beiden Termtypen (2025-GYM-B2a: 6x − 4x = 2x; 2022-GYM-B2b); beim Gleichungslösen in 2018-OS-K3b (x + 3x = 400, Nebentyp), 2021-GYM-B1a und nach dem Einsetzen in 2022-OS-K7b (9x − 3x = 6x).')
T('terme', '2.2', 'Zusammenfassen mit Potenzen (x, x²)', ['Term durch Zusammenfassen gleichartiger Glieder vereinfachen', 'Term mit Klammern und Potenzen vereinfachen'],
  '2025-GYM-B2a: 6x − 3x² − 4x = 2x − 3x² (x² bleibt getrennt); 2022-GYM-B2b: Ergebnis a² − 9a.')
T('terme', '2.3', 'Zahl mal Term', ['Binomische Formel anwenden'],
  '2019-GYM-B1f: das Mittelglied 2 · 2a · b = 4ab bilden.')
T('terme', '2.4', 'Term mal Term (x · x = x²)', ['Binomische Formel anwenden', 'Scheitelpunktform in Normalform umformen', 'Term mit Klammern und Potenzen vereinfachen'],
  'Teilschritt der binomischen Formel: (2a)² = 4a² in 2019-GYM-B1f, x · x = x² in (x + 3)² (2017-OS-K5d) und a · a in (a − 3)² (2022-GYM-B2b).')
T('terme', '2.7', 'Term aus Situation aufstellen und zusammenfassen', ['Term zu Figur angeben', 'Lineare Gleichung aus Sachverhalt aufstellen'],
  '2014-OS-B1g: Umfangsterm des Kreuzes aufstellen und zu 16a zusammenfassen; 2018-OS-K3b: aus „Pasta = 3 · Salat“ den Term x + 3x bilden und zusammenfassen.')
T('terme', '3.2', 'Minusklammer (alle Vorzeichen drehen)', ['Lineare Gleichung lösen'],
  '2021-GYM-B1a: die rechte Seite −(x + 2) zu −x − 2 auflösen.')
T('terme', '3.3', 'Zahl mal Klammer', ['Lineare Gleichung lösen', 'Lineares Gleichungssystem lösen'],
  'Lösungsweg „2x − 8 = 6“ zu 2(x − 4) = 6 in 2020-OS-B1e; nach dem Einsetzen 3 · (63 − x) = 189 − 3x in 2022-OS-K7b und 2,30 · (13 − t) in 2024-OS-K7b.')
T('terme', '3.4', 'negative Zahl mal Klammer', ['Term mit Klammern und Potenzen vereinfachen'],
  '2022-GYM-B2b: −2 · (a + 4,5) = −2a − 9.')
T('terme', '3.5', 'Klammer auflösen und zusammenfassen', ['Term mit Klammern und Potenzen vereinfachen', 'Lineare Gleichung lösen', 'Lineares Gleichungssystem lösen', 'Scheitelpunktform in Normalform umformen'],
  'Definition „mehrere Klammern … ausmultiplizieren und so weit wie möglich zusammenfassen“ (2022-GYM-B2b); ebenso 2021-GYM-B1a, 2022-OS-K7b (9x + 189 − 3x) und 2017-OS-K5d (x² + 6x + 9 − 2).')

# ==== lineare-gleichungen ====
U('lineare-gleichungen', 1, ['Lösung durch Einsetzen prüfen'])
U('lineare-gleichungen', 2, ['Lineare Gleichung lösen'])
U('lineare-gleichungen', 4, ['Lineare Gleichung aus Sachverhalt aufstellen'])
T('lineare-gleichungen', '1.1', 'Lösung durch Einsetzen prüfen (wA/fA)', ['Lösung durch Einsetzen prüfen'])
T('lineare-gleichungen', '1.2', 'Lösung durch Probieren finden', ['Lösung durch Einsetzen prüfen'],
  'Probieren mit vorgegebenen Kandidaten: 2022-OS-B1c (x = 2, 4, 6, 8 einsetzen), Definition „Vorgegebene Werte … einsetzen und die Lösung auswählen“.')
T('lineare-gleichungen', '1.3', 'Gleichung mit Umkehroperation lösen', ['Ausgangswert aus Differenz berechnen', 'Lineare Gleichung lösen'],
  'Definition „den Ausgangswert durch Umkehroperation berechnen“ (2017-OS-K2a: 682 069 − 8 512); als Vorstufe des Lösens geht 2(x − 4) = 6 in 2020-OS-B1e rückwärts (6 : 2 = 3, 3 + 4 = 7, Lösungsweg „x − 4 = 3“).')
T('lineare-gleichungen', '2.1', 'einschrittig (+, −, ·, :)', ['Lineare Gleichung lösen'],
  'Grundfall des Verfahrens (Definition „Eine lineare Gleichung mit einer Unbekannten lösen“), letzter Schritt jedes Originals, etwa 2x = 14 in 2020-OS-B1e.')
T('lineare-gleichungen', '2.2', 'zweischrittig (erst Strich, dann Punkt)', ['Lineare Gleichung lösen', 'Nullstelle lineare Funktion berechnen'],
  '2020-OS-B1e (2x − 8 = 6); die Nullstelle führt auf eine zweischrittige Gleichung 0 = −2x + 3 (2022-OS-K3a) bzw. 0 = −0,2x + 40 (2021-OS-K6d).')
T('lineare-gleichungen', '2.3', 'negative Lösung', ['Lineare Gleichung lösen'],
  '2021-GYM-B1a: Lösung x = −2.')
T('lineare-gleichungen', '2.4', 'negative Vorzahl (−4x = 20)', ['Lineare Gleichung lösen', 'Nullstelle lineare Funktion berechnen'],
  '2021-GYM-B1a (−9x = 18 nach dem Zusammenfassen); 0 = −2x + 3 in 2022-OS-K3a und 0 = −0,2x + 40 in 2021-OS-K6d.')
T('lineare-gleichungen', '2.6', 'Umformung anschreiben (Vorstufe, s. Voraussetzungen)', ['Lineare Gleichung lösen'],
  'Vorstufe des Verfahrens (Katalog: Blatt 0): die Umformung hinter dem Strich notieren, Teil jeder Lösung mit Äquivalenzumformungen (2020-OS-B1e, 2023-OS-B1e).')
T('lineare-gleichungen', '3.1', 'x beidseitig', ['Lineare Gleichung lösen', 'Lage zweier Geraden bestimmen'],
  '2021-GYM-B1a (−10x − 20 = −x − 2); Schnittpunkt aus −0,5x + 2 = 0,5x in 2023-GYM-B1b.')
T('lineare-gleichungen', '3.2', 'erst zusammenfassen', ['Lineare Gleichung lösen', 'Lineares Gleichungssystem lösen'],
  'Vor dem Umformen zusammenfassen: x + 3x = 400 in 2018-OS-K3b (Nebentyp „Lineare Gleichung lösen“), −10x − 20 in 2021-GYM-B1a, 9x + 189 − 3x in 2022-OS-K7b.')
T('lineare-gleichungen', '3.3', 'Klammer auflösen (Plus, Minus, Zahl mal Klammer)', ['Lineare Gleichung lösen', 'Lineares Gleichungssystem lösen'],
  '2020-OS-B1e (2(x − 4) = 6), 2021-GYM-B1a (4 · (−5 − 3x) und −(x + 2)); nach dem Einsetzen 3 · (63 − x) in 2022-OS-K7b.')
T('lineare-gleichungen', '3.5', 'Dezimalzahlen', ['Lineare Gleichung lösen', 'Lineares Gleichungssystem lösen', 'Nullstelle lineare Funktion berechnen'],
  '2024-OS-B1d (2 · (x − 6,5) = 0), 2022-OS-K7b (6x = 163,20), 2024-OS-K7b (29,9 − 0,6t = 26,90) und 2021-OS-K6d (0 = −0,2x + 40).')
T('lineare-gleichungen', '4.1', 'Zahlenrätsel', ['Term zu Sachtext angeben', 'Lineare Gleichung aus Sachverhalt aufstellen'],
  'Zahlenrätsel als Gleichung: 2016-OS-B1b, 2021-OS-B1e („das Fünffache einer Zahl vermindert um 4 ist gleich 36“) und 2016-GYM-B1b.')
T('lineare-gleichungen', '4.2', 'Alter, Geld, Verteilung', ['Lineare Gleichung aus Sachverhalt aufstellen'],
  'Geld in 2020-OS-K2e (12 · (520 + x) = 7920 € Einnahmen), Verteilung in 2018-OS-K3b (1000 Befragte, Pasta = 3 · Salat).')
T('lineare-gleichungen', '4.3', 'Geometrie (Umfang, Winkel)', ['Rechteckseite aus Umfang berechnen'],
  'Definition „durch Umstellen von u = 2a + 2b“; 2018-OS-B1f (b aus u = 26 cm und a = 8 cm).')
T('lineare-gleichungen', '4.4', 'Formel umstellen', ['Rechteckseite aus Umfang berechnen', 'Grundseite aus Dreiecksfläche berechnen', 'Trapezhöhe aus Fläche berechnen', 'Höhe eines Zylinders aus Volumen berechnen', 'Radius eines Zylinders aus Volumen berechnen', 'Volumen aus Masse und Dichte berechnen', 'Trigonometrische Gleichung nach Seite umstellen', 'Kreisringmaß aus Fläche berechnen', 'Kugelmaß aus Oberfläche berechnen'],
  'Die Definitionen verlangen das Umstellen einer Formel: u = 2a + 2b (2018-OS-B1f), A = ½ · g · h (2020-OS-K7b), Trapezformel (2014-OS-K5c), Zylindervolumen (2023-OS-K5d, 2022-OS-K2d), ϱ = m : V (2016-OS-K3d), sin α = a/x (2020-OS-B1j), Ringfläche (2023-GYM-K4b) und Halbkugeloberfläche (2022-GYM-K4a).')
T('lineare-gleichungen', '4.5', 'Gleichung aus Sachverhalt aufstellen und lösen (P10-Form)', ['Lineare Gleichung aus Sachverhalt aufstellen', 'Lineare Gleichung lösen'],
  'Definition „… aufstellen, die anschließend gelöst wird“; 2020-OS-K2e und 2018-OS-K3b mit Nebentyp „Lineare Gleichung lösen“.')
T('lineare-gleichungen', '4.6', 'Deutung der Lösung im Kontext', ['Lineare Gleichung aus Sachverhalt aufstellen', 'Lineare Funktion aus Sachverhalt aufstellen'],
  'Aus der Lösung die gefragten Größen ableiten (2018-OS-K3b: Salat 100, Pasta 300; 2020-OS-K2e: 140 Besucher) und im Kontext runden (2022-OS-K6b: x ≥ 18,4 heißt 19 Monate).')

# ==== lineare-funktionen ====
U('lineare-funktionen', 2, ['Gerade aus Gleichung zeichnen', 'Geradengleichung zu Graph zuordnen', 'Graph einer linearen Funktion erkennen', 'Graph nach Eigenschaft auswählen', 'y-Achsenabschnitt ablesen'])
U('lineare-funktionen', 3, ['Nullstelle lineare Funktion berechnen', 'Nullstelle am Graphen ablesen', 'Schnittpunkt am Graphen ablesen', 'Funktionswert berechnen', 'Punktprobe durchführen', 'Wertetabelle einer Funktion zuordnen'])
U('lineare-funktionen', 4, ['Gerade durch zwei Punkte zeichnen', 'Geradengleichung aus zwei Punkten'])
U('lineare-funktionen', 5, ['Lineare Funktion aus Sachverhalt aufstellen', 'Gleichung zu Tarif zuordnen', 'Endwert linearer Veränderung berechnen', 'Tarife vergleichen', 'Graph zu Tarif zuordnen', 'Eigenschaften eines Graphen beurteilen'])
T('lineare-funktionen', '1.1', 'Proportionalität erkennen (Tabelle, Text)', ['Graph zu Tarif zuordnen'],
  '2016-OS-K6a: aus dem Text erkennen, dass der Tarif ohne Grundpreis proportional ist und zur Ursprungsgeraden gehört (Definition „mit oder ohne Grundpreis“).')
T('lineare-funktionen', '1.2', 'Proportionalitätsfaktor bestimmen', ['Proportionale Zuordnung Dreisatz'],
  'Fester Faktor als Lösungsweg des Dreisatzes: 0,3 g Fett je Gramm in 2016-OS-B1d („0,3 · 20“).')
T('lineare-funktionen', '1.3', 'Graph zeichnen', ['Gerade aus Gleichung zeichnen'],
  'Die Ursprungsgerade ist der Grundfall n = 0 der Definition „Graph einer linearen Funktion aus der Gleichung mit y-Achsenabschnitt und Steigungsdreieck zeichnen“ (2021-OS-K2a).')
T('lineare-funktionen', '1.4', 'Wert ablesen und berechnen', ['Funktionswert berechnen', 'Wert aus Diagramm ablesen'],
  'Berechnen nach Definition „Wert einer Funktion für ein gegebenes Argument“ (2017-OS-K5b), Ablesen nach Definition „aus einem Funktionsgraphen im Sachzusammenhang“ (2015-OS-K4a).')
T('lineare-funktionen', '1.5', 'Dreisatz als Kontrolle', ['Proportionale Zuordnung Dreisatz'],
  'Definition „aus einem Wertepaar den fehlenden vierten Wert per Dreisatz“ (2023-OS-B1a, 2022-OS-B1b).')
T('lineare-funktionen', '2.1', 'n am Graphen ablesen', ['y-Achsenabschnitt ablesen', 'Geradengleichung zu Graph zuordnen', 'Eigenschaften eines Graphen beurteilen', 'Wert aus Diagramm ablesen'],
  'Definition „Schnittpunkt einer Geraden mit der y-Achse … ablesen und markieren“ (2024-OS-B1i); n am Graphen lesen in 2019-OS-K2c (Auswahl über den y-Achsenabschnitt) und 2025-OS-K5a (Aussage „schneidet die y-Achse in (0|3)“); Startwert bei t = 0 in 2015-OS-K4a.')
T('lineare-funktionen', '2.2', 'm mit Steigungsdreieck ablesen (auch negativ, auch Bruch)', ['Geradengleichung zu Graph zuordnen', 'Graph nach Eigenschaft auswählen'],
  '2019-OS-K2b und 2019-OS-K2c: am Steigungsdreieck von f den Anstieg −2 ablesen (Auswahl mit y = −½x + 2 als Ablenker).')
T('lineare-funktionen', '2.3', 'Gerade aus Gleichung zeichnen', ['Gerade aus Gleichung zeichnen'])
T('lineare-funktionen', '2.4', 'Gleichung zu Graph zuordnen', ['Geradengleichung zu Graph zuordnen'],
  'Definition „zu gezeichneten Geraden aus einer Auswahl die passende Gleichung“; 2019-OS-K2c.')
T('lineare-funktionen', '2.5', 'Parameter deuten (steigend, fallend, parallel, Sonderfall m = 0)', ['Graph nach Eigenschaft auswählen', 'Eigenschaften eines Graphen beurteilen', 'Lage zweier Geraden bestimmen'],
  'Fallend und parallel zur x-Achse (m = 0) in 2016-OS-B1c und 2019-OS-K2b, Monotonie aus m in 2021-OS-K2b, parallel bei gleicher Steigung in 2014-GYM-B1i.')
T('lineare-funktionen', '2.7', 'Begründen (ohne Rechnung: welche Gerade steiler)', ['Graph zu Tarif zuordnen'],
  '2016-OS-K6a verlangt die Begründung der Zuordnung; der Graph des Tarifs mit Grundpreis steigt flacher (1,50 € je km gegen 2,00 €).')
T('lineare-funktionen', '3.1', 'Funktionswert berechnen', ['Funktionswert berechnen'])
T('lineare-funktionen', '3.2', 'Argument zum Funktionswert', ['Nullstelle lineare Funktion berechnen', 'Lineare Gleichung lösen'],
  'Die Nullstelle ist das Argument zum Funktionswert null (Definition); 2022-OS-K6b: aus 55x + 990 = 2 000 die Monatszahl bestimmen (Nebentyp „Lineare Gleichung lösen“).')
T('lineare-funktionen', '3.3', 'Wertetabelle', ['Wertetabelle einer Funktion zuordnen', 'Funktionswert berechnen'],
  'Definition „zu einer Funktionsgleichung die passende Wertetabelle auswählen oder prüfen“ (2026-FOR-B1e); fehlende Tabellenwerte berechnen in 2016-GYM-K4c.')
T('lineare-funktionen', '3.4', 'Punktprobe', ['Punktprobe durchführen'],
  'Definition „Rechnerisch prüfen, ob ein Punkt auf dem Graphen einer Funktion liegt“; 2026-FOR-K5b, 2023-OS-B1i.')
T('lineare-funktionen', '3.5', 'Nullstelle berechnen', ['Nullstelle lineare Funktion berechnen'],
  'Definition „Nullstelle einer linearen Funktion aus der Gleichung berechnen“; 2022-OS-K3a, 2021-OS-K6d.')
T('lineare-funktionen', '3.6', 'Schnittpunkt mit y-Achse', ['y-Achsenabschnitt ablesen', 'Eigenschaften eines Graphen beurteilen'],
  'Definition „Schnittpunkt einer Geraden mit der y-Achse aus der Gleichung ablesen“ (2024-OS-B1i); Aussage „schneidet die y-Achse in P(0|1)“ in 2021-OS-K2b.')
T('lineare-funktionen', '4.1', 'Gleichung aus Graph', ['Geradengleichung aus zwei Punkten'],
  '2015-OS-K4d: die Gleichung h(t) = −5t + 1300 aus zwei Punkten des gezeichneten Graphen bestimmen.')
T('lineare-funktionen', '4.2', 'aus m und Punkt', ['Geradengleichung aus Punkt und einem Parameter bestimmen', 'Geradengleichung aus zwei Punkten', 'Gleichung einer Senkrechten aufstellen', 'Geradengleichung einer Parallelen durch einen Punkt bestimmen'],
  'Definition „aus einer gegebenen Steigung und einem Punkt … durch Einsetzen“ (2021-GYM-B2a); derselbe Schritt für n in 2025-OS-K5a („6 = −1,5 · (−2) + n“), mit der Steigung der Senkrechten in 2015-GYM-K2d und der Parallelen in 2024-GYM-B1b.')
T('lineare-funktionen', '4.3', 'aus zwei Punkten', ['Geradengleichung aus zwei Punkten', 'Geradengleichung einer Parallelen durch einen Punkt bestimmen'],
  'Definition „Steigung und y-Achsenabschnitt aus zwei Punkten“ (2025-OS-K5a, 2017-OS-K5a); in 2024-GYM-B1b die Steigung von g aus A und B.')
T('lineare-funktionen', '4.4', 'Gerade durch zwei Punkte zeichnen', ['Gerade durch zwei Punkte zeichnen'])
T('lineare-funktionen', '4.5', 'Schnittpunkt zweier Geraden rechnerisch', ['Lage zweier Geraden bestimmen'],
  '2023-GYM-B1b: den Schnittpunkt S(2|1) von f und g durch Gleichsetzen −0,5x + 2 = 0,5x berechnen.')
T('lineare-funktionen', '4.7', 'Begründen (Lage zweier Geraden)', ['Lage zweier Geraden bestimmen'],
  '2021-GYM-B2b: mit den verschiedenen Anstiegen begründen, dass sich g und h in genau einem Punkt schneiden (Definition „schneiden, parallel oder identisch“).')
T('lineare-funktionen', '5.1', 'Lineare Funktion aus Sachverhalt aufstellen', ['Lineare Funktion aus Sachverhalt aufstellen'])
T('lineare-funktionen', '5.2', 'Gleichung zu Tarif zuordnen', ['Gleichung zu Tarif zuordnen'])
T('lineare-funktionen', '5.3', 'Graph zu Tarif zuordnen', ['Graph zu Tarif zuordnen'])
T('lineare-funktionen', '5.4', 'Endwert berechnen', ['Endwert linearer Veränderung berechnen'],
  'Definition „Anfangswert plus oder minus n-fache konstante Änderung“; 2022-OS-K6a, 2021-OS-K6a.')
T('lineare-funktionen', '5.5', 'Tarife vergleichen mit Entscheidung', ['Tarife vergleichen'],
  'Definition „… berechnen und den günstigeren wählen“; 2023-OS-K3b, 2016-OS-K6b.')
T('lineare-funktionen', '5.6', 'Situation zu Gleichung beschreiben', ['Gleichung im Sachzusammenhang deuten'],
  'Definition „auch bei linearen … Funktionen“; 2021-OS-K6c: Bedeutung von y, x und 40 in y = −0,2x + 40.')

# ==== lineare-gleichungssysteme ====
U('lineare-gleichungssysteme', 2, ['Lineares Gleichungssystem lösen'])
U('lineare-gleichungssysteme', 4, ['Lineares Gleichungssystem aufstellen', 'Gleichung im Sachzusammenhang deuten'])
T('lineare-gleichungssysteme', '1.1', 'Zahlenpaar als Lösung einer Gleichung prüfen (wA/fA)', ['Punktprobe durchführen', 'Lösung durch Einsetzen prüfen'],
  'Die Punktprobe prüft ein Zahlenpaar an y = f(x) (Definition; 2026-FOR-K5b), in 2014-OS-K7a an zwei Gleichungen; Kontextvariante der Definition „Vorgegebene Werte in eine Gleichung … einsetzen“.')
T('lineare-gleichungssysteme', '1.3', 'Gleichung nach y umstellen', ['Lineares Gleichungssystem lösen'],
  'Teilschritt des Einsetzens: x + y = 63 zu y = 63 − x in 2022-OS-K7b, r + t = 13 zu r = 13 − t in 2024-OS-K7b.')
T('lineare-gleichungssysteme', '1.4', 'Gerade zu einer Gleichung zeichnen', ['Gerade aus Gleichung zeichnen'],
  'Definition „aus der Gleichung mit y-Achsenabschnitt und Steigungsdreieck zeichnen“, nach dem Umstellen nach y (2026-FOR-K5a).')
T('lineare-gleichungssysteme', '1.5', 'zwei Geraden zeichnen, Schnittpunkt ablesen, Probe', ['Gerade aus Gleichung zeichnen', 'Schnittpunkt am Graphen ablesen'],
  '2023-OS-K4a: die Gerade f zeichnen und den Schnittpunkt S(1|2) mit dem gegebenen Graphen ablesen.')
T('lineare-gleichungssysteme', '1.6', 'Lösung eines Systems am gegebenen Bild ablesen', ['Schnittpunkt am Graphen ablesen'],
  'Definition „Koordinaten eines Schnittpunkts zweier Graphen aus dem Koordinatensystem ablesen“; 2023-OS-K4a.')
T('lineare-gleichungssysteme', '1.7', 'Sonderfälle erkennen (parallel: keine Lösung; identisch: unendlich viele) am Bild und an der Gleichung (gleiche Steigung)', ['Lage zweier Geraden bestimmen'],
  'Definition „aus den Gleichungen … entscheiden, ob sich die Geraden schneiden, parallel oder identisch sind“; 2014-GYM-B1i.')
T('lineare-gleichungssysteme', '1.8', 'systematisches Probieren mit Tabelle bei ganzzahliger Lösung', ['Lineares Gleichungssystem lösen'],
  '2016-OS-K6d (Nebentyp): Zimmer und Betten mit ganzzahliger Lösung, laut Katalogzeile „auch durch systematisches Probieren lösbar“.')
T('lineare-gleichungssysteme', '1.10', 'Begründen (warum der Schnittpunkt beide Gleichungen erfüllt; warum Parallelen keine Lösung haben)', ['Lage zweier Geraden bestimmen'],
  '2021-GYM-B2b (format Begründung): die Zahl der gemeinsamen Punkte zweier Geraden über ihre Anstiege begründen.')
T('lineare-gleichungssysteme', '2.1', 'eine Gleichung ist nach y aufgelöst, in die andere einsetzen', ['Lineares Gleichungssystem lösen'],
  'Kern des Einsetzungsverfahrens (Definition „rechnerisch lösen“): y = 63 − x in II einsetzen (2022-OS-K7b).')
T('lineare-gleichungssysteme', '2.2', 'I nach y umstellen (Vorzahl 1)', ['Lineares Gleichungssystem lösen'],
  '2022-OS-K7b: I x + y = 63 nach y = 63 − x umstellen; ebenso 2024-OS-K7b.')
T('lineare-gleichungssysteme', '2.3', 'nach x umstellen', ['Lineares Gleichungssystem lösen'],
  '2015-GYM-K3b: x = 16 − y; 2021-OS-K7b: e = 64,90 − 3k.')
T('lineare-gleichungssysteme', '2.4', 'Klammer mit Zahl davor auflösen', ['Lineares Gleichungssystem lösen'],
  'Nach dem Einsetzen 3 · (63 − x) in 2022-OS-K7b, 2,30 · (13 − t) in 2024-OS-K7b, 3 · (16 − y) in 2016-OS-K6d.')
T('lineare-gleichungssysteme', '2.6', 'Dezimalzahlen (Geld)', ['Lineares Gleichungssystem lösen'],
  'Preise mit Dezimalzahlen in 2022-OS-K7b (352,20 €), 2024-OS-K7b (26,90 €) und 2021-OS-K7b (77,80 €).')
T('lineare-gleichungssysteme', '2.9', 'Gleichsetzen bei zwei Gleichungen der Form y = … (→ lineare-funktionen.md Einheit 4 für Schnittpunkte)', ['Lage zweier Geraden bestimmen', 'Schnittpunkte Gerade und Parabel berechnen'],
  '2023-GYM-B1b: −0,5x + 2 = 0,5x; Definition „durch Gleichsetzen der Funktionsterme“ für Gerade und Parabel (2024-OS-K3d, 2021-OS-K2c).')
T('lineare-gleichungssysteme', '2.10', 'zweite Variable berechnen und Probe in beiden Gleichungen', ['Lineares Gleichungssystem lösen'],
  'Aus x = 27,20 die zweite Variable y = 35,80 (2022-OS-K7b), aus t = 5 die Zahl r = 8 (2024-OS-K7b).')
T('lineare-gleichungssysteme', '4.1', 'Unbekannte benennen und mit Einheit beschriften', ['Gleichung im Sachzusammenhang deuten', 'Lineares Gleichungssystem aufstellen'],
  '2022-OS-K7a: x und y als Preis eines Baums in € benennen (Definition „ihre Variablen … benennen“); beim Aufstellen in 2021-OS-K7b und 2016-OS-K6d die Unbekannten selbst festlegen.')
T('lineare-gleichungssysteme', '4.2', 'aus zwei Angaben „zusammen …“ zwei Gleichungen aufstellen (nur aufstellen)', ['Lineares Gleichungssystem aufstellen'],
  '2024-OS-K7a: aus „Rose und Tulpe zusammen 3,80 €“ und „6 Rosen und 5 Tulpen 21,20 €“ nur die Gleichungen aufstellen.')
T('lineare-gleichungssysteme', '4.3', 'Anzahl-und-Preis mit Dezimalzahlen (Eintritt, Blumen, Bäume)', ['Lineares Gleichungssystem aufstellen', 'Lineares Gleichungssystem lösen'],
  'Blumen in 2024-OS-K7a und 2024-OS-K7b, Eintritt in 2021-OS-K7b, Bäume in 2022-OS-K7b.')
T('lineare-gleichungssysteme', '4.4', 'Anzahl-und-Bestand (Zimmer und Betten, Räder von Autos und Rädern)', ['Lineares Gleichungssystem aufstellen', 'Lineares Gleichungssystem lösen'],
  'Zimmer und Betten in 2016-OS-K6d (aufstellen, lösen als Nebentyp) und 2015-GYM-K3b.')
T('lineare-gleichungssysteme', '4.7', 'System aufstellen, lösen, Lösung zuordnen, Antwortsatz', ['Lineares Gleichungssystem aufstellen', 'Lineares Gleichungssystem lösen'],
  '2021-OS-K7b und 2016-OS-K6d: aufstellen und lösen in einer Teilaufgabe, Fehlerquelle „Ergebnisse den Personen falsch zuordnen“.')
T('lineare-gleichungssysteme', '4.9', 'Gleichung im Sachzusammenhang deuten: Variablen benennen (Preis oder Anzahl?)', ['Gleichung im Sachzusammenhang deuten'],
  'Definition „ihre Variablen … benennen“; 2022-OS-K7a (x und y sind Preise, nicht Anzahlen).')
T('lineare-gleichungssysteme', '4.10', 'Gleichung als Satz formulieren („x + y = 20“: zusammen zwanzig Stück)', ['Gleichung im Sachzusammenhang deuten'],
  'Definition „als Satz im Sachzusammenhang formulieren“; 2024-OS-K7b („r + t = 13“).')
T('lineare-gleichungssysteme', '4.11', 'Bestandteile einer Gleichung deuten (Vorzahl, Absolutglied; bei linearen Funktionen → lineare-funktionen.md Einheit 5, bei Wachstum → potenz-exponentialfunktionen.md)', ['Gleichung im Sachzusammenhang deuten'],
  'Definition „Bestandteile (Koeffizient, Absolutglied, Wachstumsfaktor) benennen“; 2021-OS-K6c, 2019-OS-K7b.')

# ==== binomische-formeln ====
T('binomische-formeln', '1.1', 'Termwert mit zwei Variablen berechnen (auch negativ)', ['Termwert berechnen'],
  'Definition „auch mit negativen Zahlen“; 2021-OS-B1g und 2016-OS-B1i ((a + b) : c mit negativen Werten), 2019-GYM-B1d ((a − b) : (2a + b) mit b = −3).')
T('binomische-formeln', '1.3', 'zusammenfassen mit Potenzen und Produkten (x², xy, x getrennt)', ['Term mit Klammern und Potenzen vereinfachen', 'Term durch Zusammenfassen gleichartiger Glieder vereinfachen'],
  '2022-GYM-B2b (a² − 6a + 9 − 2a − 9 − a = a² − 9a) und 2025-GYM-B2a (2x − 3x²): Potenz und lineares Glied getrennt halten.')
T('binomische-formeln', '1.5', 'Klammer mal Klammer mit lauter Plus: vier Produkte hinschreiben', ['Parabelgleichung aus Nullstellen aufstellen', 'Parameter einer Parabel aus Graph bestimmen'],
  'Grundfall des Ausmultiplizierens, das 2024-GYM-K3d ((x + 2)(x − 1)) und 2017-GYM-K2c (0,5(x + 3)(x − 1)) verlangen.')
T('binomische-formeln', '1.6', 'zusammenfassen zum dreigliedrigen Term', ['Parabelgleichung aus Nullstellen aufstellen', 'Parameter einer Parabel aus Graph bestimmen'],
  '2024-GYM-K3d: (x + 2)(x − 1) = x² + x − 2; 2022-GYM-K3b: x² − 5x + 5,25; 2017-GYM-K2c: 0,5x² + x − 1,5.')
T('binomische-formeln', '1.7', 'ein Minus in einer Klammer', ['Parabelgleichung aus Nullstellen aufstellen', 'Parameter einer Parabel aus Graph bestimmen'],
  '(x + 2)(x − 1) in 2024-GYM-K3d, 0,5(x + 3)(x − 1) in 2017-GYM-K2c.')
T('binomische-formeln', '1.8', 'Minus in beiden Klammern', ['Parabelgleichung aus Nullstellen aufstellen'],
  '2022-GYM-K3b: (x − 1,5)(x − 3,5) ausmultiplizieren.')
T('binomische-formeln', '2.1', 'gleiche Klammer zweimal erkennen ((a + b)² ist (a + b)·(a + b))', ['Scheitelpunktform in Normalform umformen', 'Binomische Formel anwenden'],
  'Vorstufe gegen die Fehlerquelle „Mittelglied fehlt“ in 2017-OS-K5d ((x + 3)² = x² + 9) und 2019-GYM-B1f (Mittelglied nicht verdoppelt).')
T('binomische-formeln', '2.2', 'erste binomische Formel mit x und Zahl', ['Scheitelpunktform in Normalform umformen', 'Binomische Formel anwenden'],
  '2017-OS-K5d: (x + 3)² = x² + 6x + 9; Definition „(a±b)² … mithilfe einer binomischen Formel ausmultiplizieren“.')
T('binomische-formeln', '2.3', 'zweite Formel (Minus im Mittelglied)', ['Binomische Formel anwenden', 'Schnittpunkte Gerade und Parabel berechnen', 'Term mit Klammern und Potenzen vereinfachen', 'Parabelgleichung aus Scheitel und Punkt bestimmen'],
  '(2a − b)² in 2019-GYM-B1f, (x − 2)² vor dem Gleichsetzen in 2022-OS-K3c, (a − 3)² in 2022-GYM-B2b, (x − 1,5)² in 2014-GYM-K2c.')
T('binomische-formeln', '2.4', 'dritte Formel (Mittelglied fällt weg)', ['Binomische Formel anwenden'],
  'Definition nennt (a + b)(a − b); kein Original mit der dritten Formel.')
T('binomische-formeln', '2.5', 'Formel zuordnen (welche der drei, oder keine)', ['Binomische Formel anwenden'],
  '2019-GYM-B1f: die zweite Formel erkennen und das Ergebnis unter vier Termen auswählen.')
T('binomische-formeln', '2.6', 'mit Vorzahl vor x (a ist die ganze Vorzahl mit x)', ['Binomische Formel anwenden'],
  '2019-GYM-B1f: (2a)² = 4a², unter den Ablenkern Terme mit 2a².')
T('binomische-formeln', '2.7', 'mit zwei Variablen', ['Binomische Formel anwenden'],
  '2019-GYM-B1f: (2a − b)² mit den Variablen a und b.')
T('binomische-formeln', '2.8', 'Vorfaktor vor der Klammer', ['Parabelgleichung aus Scheitel und Punkt bestimmen'],
  '2014-GYM-K2c: 4/3 · (x − 1,5)² zu 4/3 x² − 4x + 3 ausmultiplizieren.')
T('binomische-formeln', '2.10', 'Klammer mit Formel auflösen und mit dem Rest zusammenfassen (Scheitelpunktform → Normalform)', ['Scheitelpunktform in Normalform umformen', 'Schnittpunkte Gerade und Parabel berechnen', 'Term mit Klammern und Potenzen vereinfachen'],
  'Definition „Scheitelpunktform durch Ausmultiplizieren der binomischen Formel in die Normalform“ (2017-OS-K5d); ebenso (x − 2)² − 4 in 2022-OS-K3c und 2022-GYM-B2b.')
T('binomische-formeln', '2.11', 'Nachweis „Normalform stimmt“ (P10-Form)', ['Scheitelpunktform in Normalform umformen'],
  'Definition „ggf. als Nachweis“; 2017-OS-K5d: die vorgegebene Normalform y = x² + 6x + 7 aus (x + 3)² − 2 nachweisen.')
T('binomische-formeln', '3.9', 'Anwendung: Produktform gleich null (Verfahren in quadratische-gleichungen.md Einheit 2)', ['Lineare Gleichung lösen'],
  'Verfahren der Originale 2024-OS-B1d („Produkt ist null, wenn die Klammer null ist“: 2 · (x − 6,5) = 0) und 2023-OS-B1e (3 · (x − 8) = 0, also x − 8 = 0).')

# ==== quadratische-funktionen ====
U('quadratische-funktionen', 1, ['Parabelgleichung zu Graph zuordnen'])
U('quadratische-funktionen', 2, ['Scheitelpunkt ablesen', 'Scheitelpunktform aufstellen', 'Parabel aus Gleichung skizzieren', 'Parabel verschieben', 'Parabel an der x-Achse spiegeln', 'Parabel an der y-Achse spiegeln', 'Parabel zu Eigenschaften angeben', 'Lage zweier Parabeln begründen'])
U('quadratische-funktionen', 3, ['Scheitelpunktform in Normalform umformen'])
U('quadratische-funktionen', 4, ['Nullstellen quadratische Funktion berechnen', 'Argument zu Funktionswert berechnen', 'Schnittpunkte Gerade und Parabel berechnen', 'Gerade ohne gemeinsamen Punkt mit Parabel angeben'])
T('quadratische-funktionen', '1.1', 'Wertetabelle zu p(x) = x² ausfüllen (auch negative x)', ['Funktionswert berechnen', 'Wertetabelle einer Funktion zuordnen'],
  'Jeder Tabelleneintrag ist ein Funktionswert (Definition „Wert einer Funktion für ein gegebenes Argument berechnen“); Grundfall a = 1 zu 2026-FOR-B1e (Tabellen für x = −2 bis 2 zu y = 3x² prüfen).')
T('quadratische-funktionen', '1.2', 'Punkte eintragen und Normalparabel zeichnen (Bogen, kein Lineal)', ['Wertetabelle als Punkte darstellen', 'Parabel aus Gleichung skizzieren'],
  'Definition „Wertepaare einer Tabelle in ein vorgegebenes Koordinatensystem eintragen“ (an einer Parabel 2024-GYM-K3b, Nebentyp); die Normalparabel ist der Grundfall von „Verschobene Normalparabel aus der Gleichung … skizzieren“ (2024-OS-K3b).')
T('quadratische-funktionen', '1.3', 'Eigenschaften nennen (Scheitel, Symmetrieachse, Öffnung, kleinster Wert)', ['Scheitelpunkt ablesen', 'Funktionswert über Symmetrie bestimmen'],
  'Der Scheitel S(0 | 0) ist der Grundfall von „Scheitelpunkt … am Graphen ablesen oder aus der Gleichung bestimmen“ (Definition); die Symmetrie zur y-Achse nutzt 2023-GYM-K3a (f(−1/3) = f(1/3) ohne Rechnung).')
T('quadratische-funktionen', '1.4', 'Funktionswert berechnen (auch negatives x)', ['Funktionswert berechnen'])
T('quadratische-funktionen', '1.5', 'Punktprobe rechnerisch', ['Punktprobe durchführen'],
  'Definition „Rechnerisch prüfen, ob ein Punkt auf dem Graphen einer Funktion liegt“; an Parabeln 2020-OS-K3b und 2024-OS-K3c.')
T('quadratische-funktionen', '1.6', 'Wertetabelle zu p(x) = a·x² ausfüllen und zuordnen', ['Wertetabelle einer Funktion zuordnen', 'Funktionswert berechnen'],
  '2026-FOR-B1e: zu y = 3x² unter drei Wertetabellen die passende wählen, Kontrolle 3 · 2² = 12; Ausfüllen heißt Funktionswerte berechnen (Definition).')
T('quadratische-funktionen', '1.7', 'Öffnung und Breite an a erkennen (a < 0 nach unten; a größer als 1 schmaler; a zwischen 0 und 1 breiter)', ['Parabelgleichung zu Graph zuordnen', 'Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen', 'Parabeltransformation gegenüber der Normalparabel beschreiben'],
  'Definition „über Öffnung, Streckung …“ (2015-OS-K4b: −3t² für den fallenden Bogen); falsche Öffnung am Koeffizienten −40 in 2018-GYM-K5a; Breite im Vergleich zur Normalparabel in 2022-GYM-K3a (Definition „und ggf. Streckung“).')
T('quadratische-funktionen', '1.8', 'Parabel zu a·x² zeichnen (Schablone reicht nicht; LISUM G, kein P10-Original)', ['Parabelgleichung aus Scheitel und Punkt bestimmen', 'Parabel aus Gleichung skizzieren'],
  'GYM-Originale: Definition „… und den Graphen zeichnen“ mit gestreckten Parabeln in 2014-GYM-K2c (a = 4/3, Nebentyp „Parabel aus Gleichung skizzieren“) und 2022-GYM-K3c (h(x) = 2x² − 4,5 zeichnen).')
T('quadratische-funktionen', '1.9', 'Parabelgleichung zu Graph zuordnen über Öffnung, Streckung und Startwert, mit Begründung', ['Parabelgleichung zu Graph zuordnen'],
  '2015-OS-K4b: h(t) = −3t² + 2400 über Startwert und Öffnung wählen und begründen; ebenso 2014-GYM-B1d (y = x² + c).')
T('quadratische-funktionen', '2.1', 'Scheitel aus der Scheitelpunktform ablesen (Vorzeichen von d)', ['Scheitelpunkt ablesen'],
  'Definition „… oder aus der Gleichung bestimmen“; 2022-OS-K3b ((x − 2)² − 4) und 2017-OS-K5c ((x + 3)² − 2).')
T('quadratische-funktionen', '2.2', 'Scheitel am Graphen ablesen und als S(d | e) schreiben', ['Scheitelpunkt ablesen'],
  'Definition „am Graphen ablesen“; 2021-OS-B1d (S(−2 | −1) unter vier Angaben) und 2020-OS-K3a.')
T('quadratische-funktionen', '2.3', 'Parabel aus der Gleichung skizzieren (Scheitel setzen, Normalparabel-Punkte vom Scheitel aus)', ['Parabel aus Gleichung skizzieren'],
  '2024-OS-K3b (p(x) = x² − 4); Nebentyp in 2016-GYM-K2d und 2019-GYM-K2a.')
T('quadratische-funktionen', '2.4', 'Scheitelpunktform aus dem Scheitel aufstellen', ['Scheitelpunktform aufstellen'],
  'Definition „in der Form p(x) = (x − d)² + e angeben“; 2016-OS-B1g (zu S(1 | 3) die Gleichung ankreuzen).')
T('quadratische-funktionen', '2.5', 'Scheitelpunktform aus dem Graphen aufstellen (Scheitel ablesen, Öffnung prüfen, nach unten: Minus vor der Klammer)', ['Scheitelpunktform aufstellen', 'Scheitelpunkt ablesen'],
  '2023-OS-K4b: Scheitel (−1 | 6) ablesen (Haupttyp) und p(x) = −(x + 1)² + 6 mit Minus vor der Klammer aufstellen (Nebentyp).')
T('quadratische-funktionen', '2.6', 'Parabel verschieben (nach oben/unten über e, nach rechts/links über d) und neue Gleichung oder neuen Scheitel angeben', ['Parabel verschieben', 'Parabeltransformation gegenüber der Normalparabel beschreiben'],
  'Definition „Gleichung … nach Verschiebung … angeben oder nur den neuen Scheitelpunkt nennen“ (2015-OS-B1i, 2017-OS-K5e); die Verschiebung aus der Lage des Scheitels beschreiben verlangt 2022-GYM-K3a.')
T('quadratische-funktionen', '2.7', 'an der x-Achse spiegeln (Minus vor den ganzen Term)', ['Parabel an der x-Achse spiegeln'],
  'Definition „Vorzeichen des gesamten Funktionsterms wechselt“; 2017-OS-K5e und 2018-OS-K5d (Nebentyp), 2023-GYM-K3c.')
T('quadratische-funktionen', '2.8', 'an der y-Achse spiegeln (d wechselt das Vorzeichen)', ['Parabel an der y-Achse spiegeln'],
  '2020-OS-K3d: Scheitel (−2 | −4) wird (2 | −4), Gleichung (x − 2)² − 4.')
T('quadratische-funktionen', '2.9', 'Parabel zu Eigenschaften angeben (Scheitel auf einer Achse, keine Nullstellen, Öffnung; mehrere Lösungen)', ['Parabel zu Eigenschaften angeben'])
T('quadratische-funktionen', '2.10', 'Lage zweier Parabeln begründen (gleicher Scheitel, entgegengesetzte Öffnung; Scheitel über- oder untereinander)', ['Lage zweier Parabeln begründen', 'Anzahl gemeinsamer Punkte zweier Graphen begründen'],
  '2026-FOR-K5d (gleicher Scheitel, entgegengesetzte Öffnung); Scheitel übereinander mit entgegengesetzter Öffnung in 2020-GYM-B2b (x² − 2 und −x² − 3 ohne gemeinsamen Punkt).')
T('quadratische-funktionen', '2.11', 'Aussagen zur Parabel als wahr/falsch beurteilen', ['Eigenschaften eines Graphen beurteilen'],
  'Definition „Aussagen zu … Verlauf eines Graphen als wahr oder falsch bewerten“; an der Parabel 2018-OS-K5a (Typ bei lineare-funktionen.md).')
T('quadratische-funktionen', '2.12', 'Streckfaktor vor der Klammer erkennen und Merkmale der gestreckten Parabel bestimmen (LISUM G, kein P10-Original)', ['Parabelgleichung aus Scheitel und Punkt bestimmen', 'Parabeltransformation gegenüber der Normalparabel beschreiben'],
  'GYM-Originale: Ansatz a · (x − 1,5)² mit a = 4/3 in 2014-GYM-K2c; Definition „durch welche Verschiebung (und ggf. Streckung)“ (2022-GYM-K3a).')
T('quadratische-funktionen', '2.14', 'Begründen (warum (x − d)² bei x = d am kleinsten ist; warum e der kleinste Funktionswert ist)', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  '2017-GYM-K2a begründet genau das: (x − 3)² ≥ 0, also f(x) ≥ 1,5, darum keine Nullstelle (Typ bei quadratische-gleichungen.md).')
T('quadratische-funktionen', '3.1', 'y-Achsenabschnitt q aus der Normalform ablesen', ['Funktionswert berechnen', 'Eigenschaften eines Graphen beurteilen'],
  'q ist p(0): Schnittpunkt mit der y-Achse über f(0) in 2024-GYM-K3b und 2017-GYM-K2a (Nebentyp); Aussage zum y-Achsenschnittpunkt (0 | 2) in 2018-OS-K5a.')
T('quadratische-funktionen', '3.2', 'Funktionswert und Punktprobe in der Normalform mit negativem x', ['Funktionswert berechnen', 'Punktprobe durchführen', 'Scheitelpunkt einer Parabel rechnerisch nachweisen'],
  '2018-OS-K5a: p(−1) = 1 + 4 + 2 = 7 (Nebentyp Punktprobe); 2021-GYM-K6a (h(2) = 4,7); 2019-GYM-K2a setzt den Scheitel in die Normalform ein (f(3,5) = 5).')
T('quadratische-funktionen', '3.3', 'Scheitelpunktform ausmultiplizieren (binomische Formel) und zusammenfassen', ['Scheitelpunktform in Normalform umformen', 'Binomische Formel anwenden'],
  'Definition „durch Ausmultiplizieren der binomischen Formel in die Normalform überführen“ (2017-OS-K5d); der Teilschritt (x + 3)² ist „Binomische Formel anwenden“ (Definition, Thema Terme umformen).')
T('quadratische-funktionen', '3.4', 'Nachweis „Normalform stimmt“ (Behauptung prüfen)', ['Scheitelpunktform in Normalform umformen', 'Behauptung prüfen'],
  'Definition „ggf. als Nachweis“; 2017-OS-K5d lässt genau die Behauptung y = x² + 6x + 7 prüfen (Nebentyp Behauptung prüfen).')
T('quadratische-funktionen', '3.5', 'Scheitel einer Normalform-Parabel am Graphen ablesen', ['Scheitelpunkt ablesen'],
  '2018-OS-K5b (x² − 4x + 2) und 2025-OS-K5b (x² − 6x + 7), Scheitel jeweils am Graphen.')
T('quadratische-funktionen', '3.6', 'Scheitelpunktform aus Normalform und abgelesenem Scheitel aufstellen, Probe mit q', ['Scheitelpunktform aufstellen'],
  '2018-OS-K5c (p(x) = (x − 2)² − 2 aus x² − 4x + 2) und 2025-OS-K5b (Nebentyp).')
T('quadratische-funktionen', '3.7', 'Aussagen zur Parabel als wahr/falsch beurteilen (Punktprobe, Verschiebung, y-Achsenabschnitt)', ['Eigenschaften eines Graphen beurteilen', 'Punktprobe durchführen'],
  '2018-OS-K5a mit genau diesen drei Aussagen (Punktprobe als Nebentyp).')
T('quadratische-funktionen', '3.9', 'allgemeine Form a·x² + bx + c erkennen und Öffnung an a ablesen (Vorrat, H)', ['Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen'],
  'Definition „falsche Öffnungsrichtung bzw. falscher Koeffizient“: 2018-GYM-K5a liest an y = −40x² + 12,5 die Öffnung am Koeffizienten vor x² ab.')
T('quadratische-funktionen', '4.1', 'Nullstellen aus der Scheitelpunktform durch Wurzelziehen', ['Nullstellen quadratische Funktion berechnen'],
  'Lösungsweg „(x + 3)² = 2, x = −3 ± √2“ in 2017-OS-K5d (Nebentyp); 0,0085x² = 12 durch Wurzelziehen in 2016-GYM-K4c (Nebentyp).')
T('quadratische-funktionen', '4.2', 'Zahl der Nullstellen am Scheitel begründen', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  '2017-GYM-K2a (nachweisen, dass (x − 3)² + 1,5 keine Nullstellen hat) und 2021-OS-K7c ((x + 7)² = 0 hat genau eine Lösung); Typ bei quadratische-gleichungen.md.')
T('quadratische-funktionen', '4.3', 'Nullstellen aus der Normalform mit der p-q-Formel', ['Nullstellen quadratische Funktion berechnen'],
  '2025-OS-K5c (x² − 6x + 7 = 0 mit der p-q-Formel) und 2024-GYM-K3a.')
T('quadratische-funktionen', '4.4', 'vorher durch den Streckfaktor teilen', ['Nullstellen quadratische Funktion berechnen', 'Argument zu Funktionswert berechnen'],
  '2020-OS-K3e (2x² + 8x + 6 = 0 durch 2 teilen); 2023-OS-K4c (Minus vor x², zu x² + 2x − 15 = 0 normiert).')
T('quadratische-funktionen', '4.5', 'Nullstellen mit Wurzel als Ergebnis (Näherungswert)', ['Nullstellen quadratische Funktion berechnen'],
  '2025-OS-K5c (3 ± √2 ≈ 1,59 und 4,41) und 2017-OS-K5d (−3 ± √2, Nebentyp).')
T('quadratische-funktionen', '4.6', 'Argument zu gegebenem Funktionswert (Gleichung aufstellen, ordnen, lösen)', ['Argument zu Funktionswert berechnen'],
  '2023-OS-K4c (−x² − 2x + 5 = −10) und 2020-GYM-B2a (x² − 2 = 23).')
T('quadratische-funktionen', '4.7', 'Schnittpunkte Gerade und Parabel (gleichsetzen, alles auf eine Seite, lösen, y-Werte über die Gerade)', ['Schnittpunkte Gerade und Parabel berechnen'],
  'Definition „durch Gleichsetzen der Funktionsterme“; 2021-OS-K2c und 2024-OS-K3d (y-Werte über die Gerade).')
T('quadratische-funktionen', '4.8', 'Parabel in Scheitelpunktform gleichsetzen (Klammer auflösen)', ['Schnittpunkte Gerade und Parabel berechnen'],
  '2022-OS-K3c: (x − 2)² − 4 = −2x + 3, Klammer auflösen zu x² − 2x − 3 = 0.')
T('quadratische-funktionen', '4.9', 'Punktprobe als Schnittpunkt-Nachweis (in beide Funktionen einsetzen)', ['Punktprobe durchführen'],
  '2014-OS-K7a: S(−3 | −9) in p(x) = −x² und g(x) = 2x − 3 einsetzen (Typ bei lineare-funktionen.md).')
T('quadratische-funktionen', '4.10', 'Gerade ohne gemeinsamen Punkt mit der Parabel angeben (waagerecht jenseits des Scheitels)', ['Gerade ohne gemeinsamen Punkt mit Parabel angeben'],
  '2014-OS-K7b: waagerechte Gerade f(x) = 1 über dem Scheitel von p(x) = −x².')
T('quadratische-funktionen', '4.11', 'Schnittpunkte zweier Parabeln berechnen (LISUM G, kein P10-Original)', ['Schnittpunkte zweier Parabeln berechnen'],
  'GYM-Typ mit dem Original 2019-GYM-K2b (Gleichsetzen führt auf x² − 5x + 2,25 = 0).')

# ==== quadratische-gleichungen ====
U('quadratische-gleichungen', 1, ['Lösbarkeit quadratischer Gleichung beurteilen'])
T('quadratische-gleichungen', '1.1', 'x² = c mit Quadratzahl lösen, beide Lösungen (x₁ = √c, x₂ = −√c)', ['Argument zu Funktionswert berechnen', 'Quadratseite aus Fläche berechnen'],
  '2020-GYM-B2a endet mit x² = 25, x = ±5; im Sachzusammenhang 2020-OS-B1d (a² = 36 cm², nur die positive Lösung; Typ bei flaechen.md).')
T('quadratische-gleichungen', '1.2', 'x² = c ohne Quadratzahl (Wurzel stehen lassen, Näherungswert mit dem Taschenrechner)', ['Nullstellen quadratische Funktion berechnen', 'Radius eines Zylinders aus Volumen berechnen'],
  '2016-GYM-K4c: x = √(12 : 0,0085) ≈ 37,57 (Nebentyp Nullstellen); 2022-OS-K2d: r = √(425 : (π · 7)) ≈ 4,40 cm (Typ bei koerper.md).')
T('quadratische-gleichungen', '1.3', 'x² = c mit negativem c: keine Lösung', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  'Definition „eine Gleichung ohne Lösung angeben“ (2021-OS-K7c, etwa x² + 1 = 0); 2017-GYM-K2a (keine Nullstelle von (x − 3)² + 1,5).')
T('quadratische-gleichungen', '1.4', 'x² freistellen bei a·x² + b = 0 und a·x² = b (erst umformen, dann Wurzel)', ['Radius eines Zylinders aus Volumen berechnen', 'Nullstellen quadratische Funktion berechnen'],
  '2022-OS-K2d: r² aus V = π · r² · h freistellen, dann Wurzel (Nebenbestand, Typ bei koerper.md); 2016-GYM-K4c: −0,0085x² + 12 = 0 zu 0,0085x² = 12 (Nebentyp Nullstellen).')
T('quadratische-gleichungen', '1.5', 'a·x² + b = c mit beliebiger rechter Seite und Fallbetrachtung (GYM)', ['Argument zu Funktionswert berechnen'],
  '2020-GYM-B2a: x² − 2 = 23 zu x² = 25 umformen, x = ±5.')
T('quadratische-gleichungen', '1.6', '(x − d)² = c rückwärts rechnen (zwei Fälle x − d = √c und x − d = −√c, dann d hinüberbringen)', ['Lösbarkeit quadratischer Gleichung beurteilen', 'Nullstellen quadratische Funktion berechnen'],
  '2021-OS-K7c: (x + 8)² = 16, x + 8 = ±4, x = −4 oder −12; Lösungsweg „(x + 3)² = 2, x = −3 ± √2“ in 2017-OS-K5d (Nebentyp Nullstellen).')
T('quadratische-gleichungen', '1.7', '(x − d)² = 0: genau eine Lösung', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  '2021-OS-K7c: Aussage „(x + 7)² = 0 hat genau eine Lösung“ beurteilen.')
T('quadratische-gleichungen', '1.8', 'Lösung durch Einsetzen prüfen, auch negativ, (wA)/(fA)', ['Lösung durch Einsetzen prüfen', 'Lösbarkeit quadratischer Gleichung beurteilen'],
  'Definition „Vorgegebene Werte in eine Gleichung (linear oder quadratisch) einsetzen“ (2025-OS-B1h, Typ bei lineare-gleichungen.md); die Aussage „4 und 12 sind Lösungen von (x + 8)² = 16“ in 2021-OS-K7c widerlegt man durch Einsetzen.')
T('quadratische-gleichungen', '1.9', 'Zahl der Lösungen an c begründen (positiv, null, negativ)', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  'Definition „Aussagen zur Anzahl … der Lösungen … prüfen“; 2021-OS-K7c (rechte Seite null: eine Lösung) und 2017-GYM-K2a (keine Nullstelle begründen).')
T('quadratische-gleichungen', '1.10', 'Zahl der Lösungen am Graphen ablesen (Parabel und waagerechte Gerade y = c; Nullstellen als Sonderfall c = 0)', ['Gerade ohne gemeinsamen Punkt mit Parabel angeben'],
  '2014-OS-K7b: eine waagerechte Gerade ohne Schnittpunkt mit p(x) = −x² wählen heißt, am Graphen ein c mit null Lösungen zu finden (Typ bei quadratische-funktionen.md).')
T('quadratische-gleichungen', '1.11', 'Gleichung ohne Lösung angeben', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  'Definition „und eine Gleichung ohne Lösung angeben“; 2021-OS-K7c (etwa x² + 1 = 0).')
T('quadratische-gleichungen', '1.12', 'Aussagen zu Lösungen als wahr oder falsch beurteilen (P10-Form)', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  '2021-OS-K7c: zwei Aussagen zu (x + 7)² = 0 und (x + 8)² = 16 als wahr oder falsch ankreuzen.')
T('quadratische-gleichungen', '1.13', 'Fehler finden (nur die positive Wurzel; Vorzeichen von d beim Rückwärtsrechnen; Wurzel aus einer negativen Zahl „gezogen“)', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  '2021-OS-K7c: die Aussage „4 und 12 sind Lösungen von (x + 8)² = 16“ ist genau das Ergebnis des Vorzeichenfehlers bei d; sie als falsch zu erkennen heißt, diesen Fehler zu finden.')
T('quadratische-gleichungen', '1.14', 'Begründen (warum x² = c mit positivem c zwei Lösungen hat; warum x² = c mit negativem c keine hat)', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  '2017-GYM-K2a verlangt die Begründung, dass ein Quadrat nie negativ ist: (x − 3)² = −1,5 hat keine Lösung, also hat f keine Nullstelle.')
T('quadratische-gleichungen', '2.1', 'Produktform (x − a)·(x − b) = 0, jeden Faktor null setzen', ['Nullstellen quadratische Funktion berechnen'],
  'Lösungsweg „Faktorisieren (x + 1)(x + 3)“ in 2020-OS-K3e, ebenso 2024-GYM-K3a und 2025-GYM-B2b ((x + 4)(x − 2) = 0): jeden Faktor null setzen.')
T('quadratische-gleichungen', '2.2', 'Vorzeichen in den Klammern (x + a)', ['Nullstellen quadratische Funktion berechnen'],
  'Die Faktorisierungen der Lösungswege tragen Plus in der Klammer: (x + 1)(x + 3) in 2020-OS-K3e, (x + 4)(x − 2) in 2025-GYM-B2b.')
T('quadratische-gleichungen', '2.3', 'gleiche Faktoren (x − a)² = 0: eine Lösung', ['Lösbarkeit quadratischer Gleichung beurteilen'],
  '2021-OS-K7c: Aussage „(x + 7)² = 0 hat genau eine Lösung“.')
T('quadratische-gleichungen', '2.8', 'Lösung durch Einsetzen prüfen bei Produktform, negativ (Klammer zuerst, Punkt vor Strich)', ['Lösung durch Einsetzen prüfen', 'Parabelgleichung aus Nullstellen aufstellen'],
  '2025-OS-B1h: x·(x + 5) = −6 mit x = −2 prüfen (Typ bei lineare-gleichungen.md); 2022-GYM-K3b bestätigt die Nullstellen durch Einsetzen in die Produktform (Definition „… durch Einsetzen bestätigen“).')
T('quadratische-gleichungen', '2.10', 'Nullstellen einer Normalform durch Faktorisieren als Alternative zur Formel (Vorrat)', ['Nullstellen quadratische Funktion berechnen'],
  'Lösungsweg „p-q-Formel oder Faktorisieren“ in 2020-OS-K3e, 2024-GYM-K3a und 2025-GYM-B2b.')
T('quadratische-gleichungen', '3.1', 'Normalform erkennen und p, q mit Vorzeichen ablesen', ['Nullstellen quadratische Funktion berechnen', 'Argument zu Funktionswert berechnen', 'Schnittpunkte Gerade und Parabel berechnen', 'Schnittpunkte zweier Parabeln berechnen'],
  'Erster Schritt der p-q-Formel in den Verfahrensgebern 2025-OS-K5c, 2023-OS-K4c und 2024-OS-K3d; 2019-GYM-K2b nennt p = −5, q = 2,25 ausdrücklich.')
T('quadratische-gleichungen', '3.2', 'Gleichung ordnen: alles auf eine Seite, Reihenfolge x², x, Zahl', ['Argument zu Funktionswert berechnen', 'Schnittpunkte Gerade und Parabel berechnen', 'Schnittpunkte zweier Parabeln berechnen'],
  '2023-OS-K4c (−x² − 2x + 5 = −10), 2024-OS-K3d (4x + 1 = x² − 4 zu x² − 4x − 5 = 0), 2019-GYM-K2b (h − f).')
T('quadratische-gleichungen', '3.3', 'Normieren: durch die Vorzahl von x² teilen, auch bei negativer Vorzahl', ['Nullstellen quadratische Funktion berechnen', 'Argument zu Funktionswert berechnen', 'Schnittpunkte zweier Parabeln berechnen'],
  '2020-OS-K3e (durch 2), 2023-OS-K4c (durch −1), 2019-GYM-K2b (2x² − 10x + 4,5 durch 2).')
T('quadratische-gleichungen', '3.4', 'p-q-Formel mit ganzzahligen Lösungen (Diskriminante Quadratzahl)', ['Nullstellen quadratische Funktion berechnen', 'Argument zu Funktionswert berechnen', 'Schnittpunkte Gerade und Parabel berechnen'],
  '2020-OS-K3e (−1 und −3), 2023-OS-K4c (−5 und 3), 2022-OS-K3c und 2024-OS-K3d (Wert unter der Wurzel 4 bzw. 9).')
T('quadratische-gleichungen', '3.5', 'p ungerade: p halbe als Dezimalzahl', ['Schnittpunkte Gerade und Parabel berechnen', 'Schnittpunkte zweier Parabeln berechnen'],
  '2021-OS-K2c (x² − x − 2 = 0, p halbe = 0,5) und 2019-GYM-K2b (p = −5, p halbe = 2,5).')
T('quadratische-gleichungen', '3.6', 'Lösungen mit Wurzel, Näherungswert runden', ['Nullstellen quadratische Funktion berechnen'],
  '2025-OS-K5c (3 ± √2 ≈ 1,59 und 4,41) und 2017-OS-K5d (−3 ± √2, Nebentyp).')
T('quadratische-gleichungen', '3.10', 'Probe mit einer Lösung', ['Lösung durch Einsetzen prüfen', 'Nullstellen quadratische Funktion berechnen'],
  'Definition „Vorgegebene Werte in eine Gleichung (linear oder quadratisch) einsetzen“ (Typ bei lineare-gleichungen.md); 2023-GYM-K3b weist Nullstellen durch Einsetzen nach (f(−2) = 0, f(2) = 0).')
T('quadratische-gleichungen', '3.11', 'Klammer oder Produkt zuerst auflösen (binomische Formel, x·(x + a)), dann ordnen', ['Schnittpunkte Gerade und Parabel berechnen', 'Scheitelpunktform in Normalform umformen'],
  '2022-OS-K3c: (x − 2)² − 4 = −2x + 3, Klammer auflösen; 2017-OS-K5d: (x + 3)² − 2 zu x² + 6x + 7 ausmultiplizieren, dann null setzen.')
T('quadratische-gleichungen', '3.12', 'Gerade und Parabel gleichsetzen als Anwendung (Verfahren hier, Typ in quadratische-funktionen.md Einheit 4)', ['Schnittpunkte Gerade und Parabel berechnen'],
  'Die drei Verfahrensgeber 2021-OS-K2c, 2022-OS-K3c und 2024-OS-K3d (Typ bei quadratische-funktionen.md Einheit 4).')
T('quadratische-gleichungen', '3.13', 'Lösungsweg wählen: Wurzelziehen, Nullprodukt oder Formel', ['Schnittpunkte zweier Parabeln berechnen'],
  'Definition „eine geeignete Lösungsmethode (z. B. pq-Formel) … erläutern“ (2019-GYM-K2b).')
T('quadratische-gleichungen', '3.15', 'Fehler finden (ohne Normieren; Vorzeichen von −p/2; Diskriminante mit Plus; nur eine Lösung; Wurzel aufgeteilt)', ['Fehler in Rechnung erklären und korrigieren'],
  '2021-GYM-K6c: in einer vorgegebenen p-q-Rechnung den Vorzeichenfehler unter der Wurzel (9 − 3,75 statt 9 + 3,75) benennen und berichtigen.')
T('quadratische-gleichungen', '4.5', 'Lösungen im Kontext prüfen: negative Länge ausschließen, beim Zahlenrätsel beide Zahlen zulassen', ['Quadratseite aus Fläche berechnen', 'Fehler in Rechnung erklären und korrigieren'],
  '2020-OS-B1d: als Seitenlänge gilt nur die positive Lösung von a² = 36 (Nebenbestand, Typ bei flaechen.md); 2021-GYM-K6c: der negative Wert x₂ ≈ −0,57 ist als Stoßweite auszuschließen.')

# ==== potenz-exponentialfunktionen ====
U('potenz-exponentialfunktionen', 1, ['Wachstumsart begründen', 'Graph zu Wachstumsprozess zuordnen'])
U('potenz-exponentialfunktionen', 2, ['Wachstumstabelle ergänzen', 'Wachstumsfaktor aus Tabelle bestimmen'])
U('potenz-exponentialfunktionen', 3, ['Exponentialfunktion aufstellen', 'Zeitpunkt für Schwellenwert bei Wachstum bestimmen'])
U('potenz-exponentialfunktionen', 4, ['Verdopplungs- oder Halbwertszeit bestimmen'])
T('potenz-exponentialfunktionen', '1.1', 'an einer Tabelle entscheiden, ob die Zunahme immer gleich groß ist (Differenzen) oder immer derselbe Faktor wirkt (Quotienten)', ['Wachstumsart begründen', 'Wachstumsfaktor aus Tabelle bestimmen'],
  '2016-OS-K4d (Differenzen 0,55; 0,49 … werden kleiner, Faktor 0,89 bleibt); 2016-GYM-K2b (ungleiche Quotienten, also keine Exponentialfunktion).')
T('potenz-exponentialfunktionen', '1.2', 'Wachstumsart begründen: gleicher Prozentsatz vom jeweils vorigen Wert bedeutet gleicher Faktor, die Zuwächse in Euro oder Kilogramm werden größer (bei Abnahme kleiner)', ['Wachstumsart begründen'],
  '2018-OS-K2b (gleicher Faktor 1,08, Zuwächse werden größer) und 2016-OS-K4d (Abnahme, Differenzen werden kleiner).')
T('potenz-exponentialfunktionen', '1.3', 'dieselbe Entscheidung aus einem Text ohne Tabelle', ['Wachstumsart begründen'],
  'Definition „ob ein beschriebener Vorgang linear … oder exponentiell … wächst“; 2018-OS-K2b nur aus dem Text „jährlich um 8 %“.')
T('potenz-exponentialfunktionen', '1.4', 'Zunahme und Abnahme unterscheiden (Faktor größer oder kleiner als eins)', ['Exponentialfunktion aufstellen', 'Wachstumstabelle ergänzen'],
  '2017-OS-K7c: bei 13 % Abnahme 1000 · 0,87^x statt 1000 · 1,13^x wählen; Definition „Faktor > 1 oder < 1“ bei der Wachstumstabelle.')
T('potenz-exponentialfunktionen', '1.5', 'Wertepaare aus einer Tabelle als Punkte eintragen, Skala mit größeren Schritten lesen', ['Wertetabelle als Punkte darstellen', 'Graph eines exponentiellen Vorgangs zeichnen'],
  '2025-OS-K7a (Bakterien, Skala in größeren Schritten); GYM-Typ mit 2014-GYM-K4b (Punkte eines Zerfalls eintragen).')
T('potenz-exponentialfunktionen', '1.6', 'Achseneinteilung für gegebene Werte wählen und die Punkte zur Kurve verbinden', ['Achseneinteilung wählen', 'Wertetabelle als Punkte darstellen'],
  '2017-OS-K7b und 2016-OS-K4b: Achsen einteilen, Punkte eintragen und zur fallenden Kurve verbinden (Nebentyp Wertetabelle als Punkte darstellen).')
T('potenz-exponentialfunktionen', '1.7', 'Graph zu einem Wachstumsprozess auswählen: Startwert auf der y-Achse gegen Beginn im Ursprung, Gerade gegen gekrümmte Kurve', ['Graph zu Wachstumsprozess zuordnen'],
  'Definition „den passenden auswählen und die anderen ausschließen“; 2019-OS-K7c und 2026-FOR-K7b (Startwert größer null, gekrümmt statt gerade).')
T('potenz-exponentialfunktionen', '1.8', 'begründen, warum die beiden anderen Graphen nicht passen', ['Graph zu Wachstumsprozess zuordnen', 'Eigenschaften eines Graphen beurteilen'],
  'Definition „… und die anderen ausschließen“; die Begründung je Graph tragen 2019-OS-K7c und 2026-FOR-K7b als Nebentyp „Eigenschaften eines Graphen beurteilen“.')
T('potenz-exponentialfunktionen', '1.9', 'Graph einer Abnahme (fallend, flacher werdend) erkennen', ['Graph zu Wachstumsprozess zuordnen'],
  'Definition „zu einem linearen oder exponentiellen Sachverhalt“ schließt die Abnahme ein; beide Originale (2019-OS-K7c, 2026-FOR-K7b) zeigen Zunahmen.')
T('potenz-exponentialfunktionen', '1.11', 'Potenzfunktion y = a · xᵏ vom exponentiellen Term unterscheiden (Variable in der Basis gegen Variable im Exponenten; Vorrat)', ['Exponentialfunktion aufstellen'],
  'Erste Hälfte von „Potenzfunktion y = a · xᵏ vom exponentiellen Term unterscheiden“; 2017-OS-K7c verlangt, den Vorschlag y = x^1,13 als Potenzfunktion auszuschließen. 2017-OS-K7c: unter vier Gleichungen steht y = x^1,13 neben y = 1000 · 0,87^x; die richtige Wahl setzt die Unterscheidung Basis gegen Exponent voraus.')
T('potenz-exponentialfunktionen', '1.13', 'Begründen (warum „jedes Jahr gleich viel Prozent“ nicht „jedes Jahr gleich viel Euro“ heißt)', ['Wachstumsart begründen'],
  '2018-OS-K2b verlangt genau diese Begründung: gleicher Prozentsatz vom jeweils vorigen Wert, die absoluten Zuwächse werden größer.')
T('potenz-exponentialfunktionen', '2.1', 'Prozentsatz in den Faktor umrechnen, Zunahme und Abnahme', ['Wachstumstabelle ergänzen', 'Exponentialfunktion aufstellen', 'Wert nach prozentualer Erhöhung berechnen'],
  'Teilschritt aller Originale: 3 % zu 1,03 (2020-OS-K4a), 11 % Abnahme zu 0,89 (2016-OS-K4a), 1,9 % zu 1,019 (2026-FOR-K7c); Definition „Erhöhung oder Senkung … (Wachstumsfaktor)“ bei prozentrechnung.md.')
T('potenz-exponentialfunktionen', '2.2', 'Faktor in den Prozentsatz zurück', ['Wachstumsfaktor aus Tabelle bestimmen', 'Gleichung im Sachzusammenhang deuten'],
  '2018-OS-K2a (Nachweis der 8 % über 1,08); 2019-OS-K7b (1,04 als Zunahme um 4 % deuten, Typ bei lineare-gleichungssysteme.md).')
T('potenz-exponentialfunktionen', '2.3', 'Faktor als Quotient zweier aufeinanderfolgender Tabellenwerte nachweisen, mehrere Quotienten prüfen', ['Wachstumsfaktor aus Tabelle bestimmen'],
  'Definition „als Quotient aufeinanderfolgender Tabellenwerte nachweisen“; 2025-OS-K7b (112 : 80 = 1,4, weitere Quotienten ≈ 1,40).')
T('potenz-exponentialfunktionen', '2.4', 'nächsten Tabellenwert berechnen (Wert mal Faktor)', ['Wachstumstabelle ergänzen'],
  '2026-FOR-K7a (674,93 · 1,019) und 2020-OS-K4a (57,3 · 1,03).')
T('potenz-exponentialfunktionen', '2.5', 'Lücke mitten in der Tabelle füllen', ['Wachstumstabelle ergänzen'],
  '2016-OS-K4a (Wert bei 1 h: 5,00 · 0,89) und 2017-OS-K7a (Wert bei 2 km).')
T('potenz-exponentialfunktionen', '2.6', 'Anfangsbestand als Wert im Schritt null eintragen (nicht rückwärts rechnen, wenn der Startwert im Text steht)', ['Wachstumstabelle ergänzen'],
  '2026-FOR-K7a (2026: 650 €), 2020-OS-K4a (2019: 54) und 2019-OS-K7a (Woche 0: 10 kg).')
T('potenz-exponentialfunktionen', '2.7', 'einen Schritt zurückrechnen (geteilt durch den Faktor)', ['Wachstumstabelle ergänzen'],
  'Definition „Fehlende Werte … über den Wachstumsfaktor ergänzen“ schließt den Wert vor einem bekannten ein; in den Originalen steht der Anfangswert im Text (2020-OS-K4a: 55,6 : 1,03 ≈ 54 als Kontrolle).')
T('potenz-exponentialfunktionen', '2.8', 'Wert über mehrere Schritte mit der Potenz des Faktors', ['Wachstumstabelle ergänzen'],
  '2019-OS-K7a (10 · 1,04⁵) und 2017-OS-K7a (498 · 0,87³).')
T('potenz-exponentialfunktionen', '2.9', 'fehlende Zeitangabe im Tabellenkopf über die Zahl der Schritte bestimmen und prüfen', ['Wachstumstabelle ergänzen'],
  'Definition „auch eine fehlende Zeitangabe“; 2016-OS-K4a (3,14 mg gehört zu 4 h, Kontrolle 5,00 · 0,89⁴).')
T('potenz-exponentialfunktionen', '2.10', 'Wachstumsrate aus zwei Werten bestimmen', ['Wachstumsfaktor aus Tabelle bestimmen', 'Prozentuale Veränderung berechnen', 'Parameter einer Exponentialfunktion bestimmen'],
  '2018-OS-K2a (48 000 : 600 000 = 8 %); Definition „Zu- oder Abnahme zwischen zwei Werten in Prozent des Ausgangswerts“ (prozentrechnung.md); Faktor aus nicht benachbarten Werten in 2016-GYM-K2a (a² = 2,25) und 2024-GYM-K4d (b⁶ = 25 875 : 550).')
T('potenz-exponentialfunktionen', '2.11', 'Tabelle für einen Zerfall mit Faktor kleiner eins fortschreiben', ['Wachstumstabelle ergänzen'],
  'Definition „Faktor > 1 oder < 1“; 2016-OS-K4a (0,89) und 2017-OS-K7a (0,87).')
T('potenz-exponentialfunktionen', '3.1', 'Anfangswert und Faktor im Text finden', ['Exponentialfunktion aufstellen'],
  'Teilschritt der Definition „aus Anfangswert und Wachstumsfaktor angeben“; 2026-FOR-K7c (650 € und 1,9 % im Text).')
T('potenz-exponentialfunktionen', '3.2', 'Gleichung y = a · qˣ aufstellen (Zunahme und Abnahme)', ['Exponentialfunktion aufstellen'],
  'Erste Hälfte von „Gleichung y = a · qˣ aufstellen“; Definition „Gleichung N(t) = a · q^t … angeben“ (2026-FOR-K7c). 2026-FOR-K7c (Zunahme, M(t) = 650 · 1,019^t) und 2017-OS-K7c (Abnahme, y = 1000 · 0,87^x).')
T('potenz-exponentialfunktionen', '3.3', 'passende Gleichung unter vier Vorschlägen ankreuzen', ['Exponentialfunktion aufstellen'],
  '2017-OS-K7c: y = 1000 · 0,87^x unter vier Gleichungen ankreuzen.')
T('potenz-exponentialfunktionen', '3.4', 'Bestandteile einer gegebenen Gleichung deuten: Anfangswert, Faktor als „hundert Prozent plus Zuwachs“, Variable als Zeit', ['Gleichung im Sachzusammenhang deuten', 'Gleichungskette im Sachzusammenhang erläutern'],
  '2019-OS-K7b (10, 1,04 und x in f(x) = 10 · 1,04^x; Typ bei lineare-gleichungssysteme.md); 2024-GYM-K4c erläutert 500 000 = 200 · 2,5^x im Sachzusammenhang.')
T('potenz-exponentialfunktionen', '3.5', 'Wert nach einer gegebenen Zahl von Schritten berechnen (Potenz mit dem Taschenrechner, Ergebnis mit ≈ und Einheit)', ['Funktionswert berechnen', 'Zinseszins Endkapital berechnen'],
  '2016-OS-K4e (5 · 0,89²⁴ ≈ 0,31 mg), 2026-FOR-K7c (Nebentyp; Typ bei lineare-funktionen.md); dieselbe Rechnung im Zinskontext 2014-OS-K3c (1000 · 1,03⁵, Typ bei zinsrechnung.md).')
T('potenz-exponentialfunktionen', '3.6', 'Zeitschritte zählen, wenn Jahreszahlen gegeben sind (Startjahr ist der Schritt null)', ['Funktionswert berechnen', 'Zeitpunkt für Schwellenwert bei Wachstum bestimmen'],
  '2026-FOR-K7c (2040 heißt t = 14) und 2020-OS-K4c (2033 heißt x = 14, Fehlerquelle „x = 2033 einsetzen“); 2018-OS-K2c zählt die Jahre ab 2017 bis 2020.')
T('potenz-exponentialfunktionen', '3.7', 'Behauptung prüfen: Wert berechnen und mit dem genannten vergleichen, Entscheidung mit Begründung', ['Funktionswert berechnen', 'Behauptung prüfen'],
  'Definition „ggf. mit einer Vorgabe vergleichen“; genau diese Behauptungen prüfen 2017-OS-K7d (etwa 4 km Höhe bei 573 hPa) und 2025-OS-K7b (mehr als 250 000 Bakterien nach 24 Stunden), beide mit Nebentyp Behauptung prüfen.')
T('potenz-exponentialfunktionen', '3.8', 'zwei Vorhersagen vergleichen (exponentiell gegen einen festen Gesamtprozentsatz)', ['Funktionswert berechnen', 'Wert nach prozentualer Erhöhung berechnen', 'Behauptung prüfen'],
  '2020-OS-K4c: 54 · 1,03¹⁴ ≈ 81,7 gegen 54 · 1,4 = 75,6 (Nebentypen Wert nach prozentualer Erhöhung berechnen und Behauptung prüfen).')
T('potenz-exponentialfunktionen', '3.9', 'Zeitpunkt für einen Schwellenwert durch schrittweises Multiplizieren finden, Schritte zählen und den erreichten Wert angeben', ['Zeitpunkt für Schwellenwert bei Wachstum bestimmen'],
  'Definition „durch schrittweises Multiplizieren … und den Wert angeben“; 2018-OS-K2c (2020, ≈ 1 028 294 €).')
T('potenz-exponentialfunktionen', '3.10', 'Zerfall bis unter eine Schwelle', ['Zeitpunkt für Schwellenwert bei Wachstum bestimmen'],
  'Dasselbe Verfahren mit Faktor kleiner eins (Definition „schrittweises Multiplizieren mit dem Wachstumsfaktor“); kein Original mit Zerfall.')
T('potenz-exponentialfunktionen', '4.1', 'Startwert verdoppeln oder halbieren und den Zielwert notieren', ['Verdopplungs- oder Halbwertszeit bestimmen'],
  'Teilschritt: 2020-OS-K4b (108 = 2 · 54) und 2016-OS-K4c (2,50 mg als Hälfte von 5,00 mg).')
T('potenz-exponentialfunktionen', '4.2', 'Zielwert in einer Tabelle suchen und die Zeit ablesen', ['Verdopplungs- oder Halbwertszeit bestimmen'],
  'Definition „aus … der Wertetabelle“; 2016-OS-K4c.')
T('potenz-exponentialfunktionen', '4.3', 'Zielwert am Graphen suchen: Wert an der y-Achse, waagerecht zum Graphen, senkrecht zur x-Achse, Zeit ablesen', ['Verdopplungs- oder Halbwertszeit bestimmen'],
  'Definition „aus dem Graphen“; 2020-OS-K4b (y = 108 suchen, zugehöriges x ablesen).')
T('potenz-exponentialfunktionen', '4.4', 'das eigene Vorgehen in Worten beschreiben', ['Verdopplungs- oder Halbwertszeit bestimmen'],
  'Definition „ggf. das Vorgehen beschreiben“; 2020-OS-K4b.')
T('potenz-exponentialfunktionen', '4.5', 'zwischen zwei Tabellenwerten die nächstliegende Zeit angeben (der Zielwert liegt selten genau auf einem Tabellenwert)', ['Verdopplungs- oder Halbwertszeit bestimmen'],
  '2016-OS-K4c: 2,50 mg liegt zwischen 2,79 (5 h) und 2,48 (6 h), Antwort etwa 6 h.')
T('potenz-exponentialfunktionen', '4.6', 'durch Probieren mit dem Faktor rechnen, bis der Zielwert erreicht ist', ['Zeitpunkt für Schwellenwert bei Wachstum bestimmen', 'Exponent einer Potenz bestimmen'],
  'Abgrenzung in der Definition von „Verdopplungs- oder Halbwertszeit bestimmen“: schrittweises Multiplizieren bis zur Schwelle ist der Schwellenwert-Typ (2018-OS-K2c); Probieren über die Potenzen in 2024-OS-B1g (4^x = 256, Typ bei potenzen-wurzeln.md).')
T('potenz-exponentialfunktionen', '4.7', 'Halbwertszeit beim Zerfall, Verdopplungszeit beim Wachstum benennen', ['Verdopplungs- oder Halbwertszeit bestimmen'],
  'Definition „verdoppelt oder halbiert“: Halbierung in 2016-OS-K4c, Verdopplung in 2020-OS-K4b.')
T('potenz-exponentialfunktionen', '4.9', 'Logarithmus für den genauen Zeitpunkt (Vorrat)', ['Zeit aus Exponentialgleichung berechnen', 'Aussage zu Logarithmusterm prüfen', 'Gleichungskette im Sachzusammenhang erläutern'],
  'GYM-Typen: Definition „den Exponenten t durch Logarithmieren berechnen“ (2014-GYM-K4c, 2018-GYM-K2b); derselbe Schritt in 2025-GYM-K3c (x = log₂ 10) und 2024-GYM-K4c (x = log₂,₅ 2500 erläutern).')

# ==== trigonometrische-funktionen ====
T('trigonometrische-funktionen', '1.5', 'abgelesenen Wert mit dem Taschenrechner prüfen (Grad-Modus)', ['Sinussatz Seite berechnen'],
  'Nebenleistungsbestand: sin 123°, sin 115° und sin 141° mit dem Taschenrechner im Grad-Modus bilden (2015-OS-K5c, 2020-OS-K7c, 2025-OS-K4c; Typ bei trigonometrie.md).')
T('trigonometrische-funktionen', '1.11', 'Taschenrechner-Modus erkennen und wechseln (DEG, RAD)', ['Seite im rechtwinkligen Dreieck berechnen'],
  '2021-OS-K3a nennt als Fehlerquelle „Taschenrechner in Bogenmaß“; das richtige Ergebnis setzt den Grad-Modus voraus (Typ bei trigonometrie.md).')
T('trigonometrische-funktionen', '2.1', 'Wertetabelle in gleichmäßigen Winkelschritten ausfüllen (am Einheitskreis oder mit dem Taschenrechner)', ['Funktionswert berechnen'],
  'Definition „Wert einer Funktion für ein gegebenes Argument berechnen“ gilt für jede Funktion (Typ bei lineare-funktionen.md); kein Original an der Sinusfunktion.')
T('trigonometrische-funktionen', '2.2', 'Punkte eintragen und den Graphen zeichnen', ['Wertetabelle als Punkte darstellen'],
  'Definition „Wertepaare einer Tabelle in ein vorgegebenes Koordinatensystem eintragen“ ohne Einschränkung des Funktionstyps; kein Original an der Sinusfunktion.')
T('trigonometrische-funktionen', '2.3', 'Achseneinteilung wählen und beschriften', ['Achseneinteilung wählen'],
  'Definition „eine Achseneinteilung wählen, mit der alle Werte einer Tabelle darstellbar sind, und sie beschriften“; kein Original an der Sinusfunktion.')
T('trigonometrische-funktionen', '2.6', 'Funktionswert berechnen und Punktprobe durchführen', ['Funktionswert berechnen', 'Punktprobe durchführen'],
  'Beide Definitionen gelten für jede Funktion (Typen bei lineare-funktionen.md); kein Original an der Sinusfunktion.')
T('trigonometrische-funktionen', '2.7', 'Wertebereich angeben', ['Eigenschaften trigonometrischer Funktionen vergleichen'],
  'Grundfall a = 1 zu 2015-GYM-K2b (Wertebereich [−2; 2] gegen [−2; 6] als unterscheidende Eigenschaft).')
T('trigonometrische-funktionen', '2.10', 'kleinste Periode angeben', ['Trigonometrische Funktionsgleichung zu Graph zuordnen'],
  '2019-GYM-B1i: zwei volle Perioden auf [−2π; 2π], also Periode 2π ablesen.')
T('trigonometrische-funktionen', '2.13', 'Sinus- und Kosinusgraph vergleichen und die Verschiebung angeben', ['Eigenschaften trigonometrischer Funktionen vergleichen'],
  'Definition „Zwei trigonometrische Funktionen anhand einer unterscheidenden Eigenschaft (z. B. … Achsenschnittpunkt) vergleichen“ (2015-GYM-K2b).')
T('trigonometrische-funktionen', '2.14', 'Graph einer Gleichung zuordnen', ['Trigonometrische Funktionsgleichung zu Graph zuordnen'],
  'Grundfall zu 2019-GYM-B1i (Gleichung unter vier Vorschlägen dem Graphen zuordnen).')
T('trigonometrische-funktionen', '3.1', 'Amplitude aus einer Gleichung ablesen', ['Eigenschaften trigonometrischer Funktionen vergleichen', 'Trigonometrische Funktionsgleichung zu Graph zuordnen'],
  '2015-GYM-K2b (f(x) = 2 · sin(0,5π · x) hat Amplitude 2); 2019-GYM-B1i (Amplituden der vier Vorschläge vergleichen).')
T('trigonometrische-funktionen', '3.2', 'Amplitude an einem Graphen ablesen (halber Abstand zwischen Hoch- und Tiefpunkt)', ['Eigenschaften trigonometrischer Funktionen vergleichen', 'Transformation einer trigonometrischen Funktion beschreiben', 'Trigonometrische Funktionsgleichung zu Graph zuordnen'],
  '2015-GYM-K2b und 2015-GYM-K2a (g mit Maximum 6 und Minimum −2, Amplitude 4); 2019-GYM-B1i (Wertebereich [−3; 1], Amplitude 2).')
T('trigonometrische-funktionen', '3.3', 'Wertebereich zu gegebenem a angeben', ['Eigenschaften trigonometrischer Funktionen vergleichen'],
  '2015-GYM-K2b: Wertebereich [−2; 2] zu a = 2 als unterscheidende Eigenschaft (Definition „z. B. Amplitude, Wertebereich“).')
T('trigonometrische-funktionen', '3.5', 'Periode aus dem Parameter b berechnen (Vollkreis geteilt durch b)', ['Trigonometrische Funktionsgleichung zu Graph zuordnen'],
  '2019-GYM-B1i: die Vorschläge mit sin(2x) haben Periode π und scheiden aus.')
T('trigonometrische-funktionen', '3.6', 'Parameter b aus der abgelesenen Periode berechnen', ['Trigonometrische Funktionsgleichung zu Graph zuordnen'],
  '2019-GYM-B1i: Periode 2π abgelesen, also Faktor 1 vor x.')
T('trigonometrische-funktionen', '3.8', 'Gleichung aus einem gegebenen Graphen aufstellen (erst Amplitude, dann Periode, dann b)', ['Trigonometrische Funktionsgleichung zu Graph zuordnen', 'Transformation einer trigonometrischen Funktion beschreiben'],
  '2019-GYM-B1i (Amplitude, Periode und Verschiebung am Graphen, Gleichung wählen); 2015-GYM-K2a (zum Graphen von g eine passende Gleichung notieren).')
T('trigonometrische-funktionen', '3.9', 'Graphen und Gleichungen einander zuordnen', ['Trigonometrische Funktionsgleichung zu Graph zuordnen'],
  'Definition „aus mehreren Gleichungen (unterschiedliche Amplitude, Streckung oder Verschiebung) die passende auswählen“ (2019-GYM-B1i).')
T('trigonometrische-funktionen', '3.10', 'Wirkung eines Parameters in Worten beschreiben (höher, flacher, schneller, langsamer)', ['Transformation einer trigonometrischen Funktion beschreiben'],
  'Definition „Beschreiben, wie der Graph … durch Streckung in y-Richtung und Verschiebung … hervorgeht“ (2015-GYM-K2a).')
T('trigonometrische-funktionen', '3.11', 'zwei Graphen mit verschiedenen Parametern vergleichen', ['Eigenschaften trigonometrischer Funktionen vergleichen', 'Transformation einer trigonometrischen Funktion beschreiben'],
  '2015-GYM-K2b (Amplitude 2 gegen 4) und 2015-GYM-K2a (g aus f durch Streckung und Verschiebung).')
T('trigonometrische-funktionen', '3.12', 'Verschiebung nach oben und unten mit d, Verschiebung zur Seite mit c (Vorrat, H, GYM)', ['Transformation einer trigonometrischen Funktion beschreiben', 'Trigonometrische Funktionsgleichung zu Graph zuordnen'],
  '2015-GYM-K2a (Verschiebung um 2 nach oben) und 2019-GYM-B1i (Verschiebung um −1, Vorschlag 2 · sin(2x − 1) zur Seite).')
T('trigonometrische-funktionen', '4.3', 'Größtwert und Kleinstwert einer Tabelle entnehmen', ['Minimum und Maximum ablesen'],
  'Definition „Kleinsten und größten Wert einer Datenreihe oder eines Diagramms angeben“ (Typ bei daten.md).')
T('trigonometrische-funktionen', '4.4', 'Mittellinie und Amplitude daraus bestimmen', ['Trigonometrische Funktionsgleichung zu Graph zuordnen', 'Transformation einer trigonometrischen Funktion beschreiben'],
  'Aus Größt- und Kleinstwert Mittellinie und Amplitude: 2019-GYM-B1i ([−3; 1] ergibt Amplitude 2, Verschiebung −1), 2015-GYM-K2a (6 und −2 ergeben Amplitude 4, Verschiebung 2).')
T('trigonometrische-funktionen', '4.6', 'Sachkontext, Gleichung und Graph einander zuordnen', ['Trigonometrische Funktionsgleichung zu Graph zuordnen'],
  'Kontextvariante des Zuordnens von Gleichung und Graph in 2019-GYM-B1i; kein Original mit Sachkontext.')
T('trigonometrische-funktionen', '4.9', 'eine Frage am Graphen beantworten (Ablesen mit Hilfslinien)', ['Wert aus Diagramm ablesen'],
  'Definition „aus einem Funktionsgraphen im Sachzusammenhang … an der Skala ablesen“ (Typ bei daten.md).')
T('trigonometrische-funktionen', '4.12', 'zu einem Sachverhalt den passenden Funktionstyp auswählen und die übrigen ausschließen', ['Graph zu Wachstumsprozess zuordnen'],
  'Nebenleistungsbestand des Eintrags: 2019-OS-K7c und 2026-FOR-K7b (linear gegen exponentiell, die anderen Graphen ausschließen; Typ bei potenz-exponentialfunktionen.md).')

# ==== daten ====
U('daten', 1, ['Relative Häufigkeit angeben'])
U('daten', 2, ['Wert aus Diagramm ablesen', 'Werte im Diagramm nach Bedingung auswählen', 'Achsenskalierung aus Säule bestimmen', 'Säulen- oder Balkendiagramm ergänzen'])
U('daten', 3, ['Streifendiagramm zeichnen', 'Kreisdiagramm zeichnen', 'Mittelpunktswinkel berechnen', 'Sektor im Kreisdiagramm zuordnen'])
U('daten', 4, ['Arithmetisches Mittel berechnen', 'Median bestimmen', 'Spannweite berechnen', 'Minimum und Maximum ablesen', 'Fehlenden Wert aus Mittelwert bestimmen', 'Kenngrößen einer Liste prüfen', 'Veränderung des Mittelwerts begründen'])
U('daten', 5, ['Aussage zu Diagramm prüfen', 'Verzerrung eines Diagramms erklären'])
T('daten', '1.2', 'Häufigkeitstabelle aus einer Urliste', ['Kreisdiagramm zeichnen'],
  '2020-GYM-K6c zeichnet das Kreisdiagramm aus einer Urliste von zehn Trefferzahlen und muss dafür erst die Häufigkeit je Trefferzahl auszählen (Fehlerquelle „die Trefferzahlen selbst statt der Häufigkeiten“).')
T('daten', '1.3', 'relative Häufigkeit als Bruch (22 von 34)', ['Relative Häufigkeit angeben'],
  'Definition „Quotient aus absoluter Häufigkeit und Gesamtzahl (Bruch, Dezimalzahl oder Prozent)“; einziges Original 2015-OS-K7b mit 22 von 34 Spielen als 22/34.')
T('daten', '1.4', 'als Dezimalzahl und in Prozent (Taschenrechner, runden)', ['Relative Häufigkeit angeben', 'Prozentsatz berechnen'],
  'Die Definition nennt Dezimalzahl und Prozent (2015-OS-K7b ≈ 0,65 ≈ 64,7 %); in 2025-OS-K6b (hier geführt, Typ bei prozentrechnung.md) ist der Anteil 5 von 11 in Prozent der Haupttyp „Prozentsatz berechnen“.')
T('daten', '1.5', 'Summe der relativen Häufigkeiten prüfen', ['Fehlenden Prozentanteil ergänzen'],
  'Vorstufe desselben Verfahrens: die Anteile ergänzen sich zu 100 % (Definition „fehlenden Prozentsatz als Rest zu 100 %“, 2021-OS-K5b, hier geführt, Typ bei prozentrechnung.md).')
T('daten', '1.6', 'häufigster und seltenster Wert', ['Modalwert bestimmen', 'Kenngrößen einer Liste prüfen'],
  'Definition „Modalwert (häufigster Wert)“ (2016-GYM-K3c, 2023-GYM-K5c); in 2025-OS-K6a ist der häufigste Wert 2 (fünfmal) zu bestimmen, um die falsche Modalwert-Aussage zu berichtigen.')
T('daten', '1.7', 'relative Häufigkeit aus einem Diagramm (Anzahl und Gesamtzahl ablesen)', ['Relative Häufigkeit angeben', 'Wert aus Diagramm ablesen'],
  'Kontextvariante des Quotienten aus Anzahl und Gesamtzahl (Definition „Relative Häufigkeit angeben“), die Anzahlen liefert das Ablesen an der Skala (Definition „Wert aus Diagramm ablesen“); kein Original verbindet beides.')
T('daten', '1.8', 'Anzahl aus relativer Häufigkeit und Gesamtzahl (Umkehrung)', ['Prozentwert berechnen'],
  'Anzahl gleich Anteil mal Gesamtzahl ist der Prozentwert (Definition „aus Grundwert und Prozentsatz den Prozentwert“); 2019-OS-K5a rechnet 23 % von 1 200 Befragten (Typ bei prozentrechnung.md).')
T('daten', '2.1', 'Wert einer Säule an der Skala ablesen (Hilfslinien zählen)', ['Wert aus Diagramm ablesen'],
  'Definition „Einzelwert einer Kategorie … an der Skala ablesen“; 2016-OS-K2b (Säule 2015 auf Höhe 250).')
T('daten', '2.2', 'Achsenbeschriftung „in Tausend“, „in Mio.“, „in %“ anwenden', ['Wert aus Diagramm ablesen', 'Werte im Diagramm nach Bedingung auswählen'],
  'Definition „ggf. mit Einheit ‚in Tausend‘ umrechnen“ (2016-OS-K2b: 250 Tausend sind 250 000 Besucher); 2016-OS-K2a vergleicht Säulen „in Tausend“ mit der Schwelle 300 000.')
T('daten', '2.3', 'Werte über oder unter einer Schwelle auswählen (Grenzwert zählt nicht mit)', ['Werte im Diagramm nach Bedingung auswählen'],
  '2020-OS-K2b (mehr als 190 Besucher, der Freitag mit genau 190 zählt nicht) und 2016-OS-K2a (weniger als 300 000).')
T('daten', '2.4', 'größte und kleinste Säule, Differenz zweier Säulen', ['Minimum und Maximum ablesen', 'Spannweite berechnen'],
  '2022-OS-K4a liest kleinste und größte Säule ab; die Differenz der größten und der kleinsten Säule ist die Spannweite am Besucherdiagramm in 2020-OS-K2d (280 − 130).')
T('daten', '2.5', 'Achseneinteilung aus einer Säule mit bekanntem Wert bestimmen', ['Achsenskalierung aus Säule bestimmen'],
  'Definition „aus einer Säule mit bekanntem Wert die fehlende Einteilung der Achse ermitteln“; 2023-OS-K6d (50 Mio. je Kästchen), 2018-OS-K3a (20 je Gitterlinie).')
T('daten', '2.6', 'unbeschriftete Säule anhand der Höhe zuordnen', ['Achsenskalierung aus Säule bestimmen'],
  'Definition „… und weitere Säulen zuordnen“; 2023-OS-K6d (unbeschriftete Säule ist Hindi), 2018-OS-K3a (Balken den Gerichten zuordnen).')
T('daten', '2.7', 'Säule oder Balken mit gegebenem Wert ergänzen', ['Säulen- oder Balkendiagramm ergänzen'],
  '2020-OS-K2a (Balken 180), 2026-FOR-K3d (Säule 1,85), Nebenleistung in 2023-OS-K6d (Säule Arabisch).')
T('daten', '2.8', 'Diagramm aus einer Tabelle zeichnen (Skala wählen)', ['Säulen- oder Balkendiagramm ergänzen', 'Achseneinteilung wählen'],
  'Die Säulen trägt „Säulen- oder Balkendiagramm ergänzen“ ab (2026-FOR-K3d), die Skala zu einer Tabelle wählt „Achseneinteilung wählen“ (Definition, 2021-OS-K6b, Typ bei zuordnungen.md); 2023-OS-K6d verlangt Achsenbeschriftung und Säule zusammen.')
T('daten', '2.9', 'Liniendiagramm lesen (Verlauf, Anstieg, Rückgang)', ['Wert aus Diagramm ablesen', 'Aussage zu Diagramm prüfen'],
  'Die Definition von „Wert aus Diagramm ablesen“ nennt das Liniendiagramm (2018-GYM-K3d: Maximum der Hoch-Kurve); Verlauf, Anstieg und Rückgang beurteilt „Aussage zu Diagramm prüfen“ (Definition „Behauptung über Verlauf oder Veränderung“, 2022-OS-K4c).')
T('daten', '3.1', 'Anteil in Prozent → Streifenabschnitt (1 mm je 1 % bei 10 cm)', ['Streifendiagramm zeichnen'],
  'Definition „Prozentanteile als Abschnitte eines vorgegebenen Streifens (Gesamtlänge = 100 %) abtragen“; 2018-OS-K3c (Streifen 10 cm).')
T('daten', '3.2', 'Streifen mit vier Abschnitten zeichnen und beschriften', ['Streifendiagramm zeichnen'],
  '2018-OS-K3c trägt vier Abschnitte (10 %, 15 %, 55 %, 20 %) ab und beschriftet sie; 2023-GYM-K5a mit drei Abschnitten.')
T('daten', '3.3', 'Prozent → Mittelpunktswinkel (Anteil mal 360°)', ['Mittelpunktswinkel berechnen', 'Kreisdiagramm zeichnen'],
  'Definition „Kreisdiagramm zeichnen“: Anteil in Prozent in den Mittelpunktswinkel umrechnen; 2022-OS-K4d (0,16 · 360°) und 2017-OS-K2c (0,112 · 360°).')
T('daten', '3.4', 'Bruchteil oder Anzahl → Winkel (12 von 508)', ['Mittelpunktswinkel berechnen', 'Kreisdiagramm zeichnen'],
  'Definition „Mittelpunktswinkel … aus Teil und Ganzem“ (2024-OS-K2c: 12 : 508 · 360°); 2025-OS-K6b und 2015-OS-K7c zeichnen den Sektor aus Anzahlen (5 von 11, 12 von 83).')
T('daten', '3.5', 'Sektor mit dem Geodreieck ab dem Radius zeichnen', ['Kreisdiagramm zeichnen'],
  'Definition „als Sektor in einen Kreis eintragen“; 2015-OS-K7c (Sektor mit 52° am vorgegebenen Radius), 2017-OS-K2c (Sektor mit 40°).')
T('daten', '3.6', 'Kreisdiagramm mit drei bis vier Sektoren aus Prozentangaben', ['Kreisdiagramm zeichnen'],
  'Definition „Anteil in Prozent … als Sektor eintragen“; die OS-Originale tragen je einen Sektor ein (2017-OS-K2c, 2025-OS-K6b), vollständige Kreisdiagramme mit drei bis fünf Sektoren verlangen 2019-GYM-K5a, 2022-GYM-K6a und 2020-GYM-K6c.')
T('daten', '3.7', 'fehlenden Anteil zu 100 % ergänzen', ['Fehlenden Prozentanteil ergänzen'],
  'Definition „fehlenden Prozentsatz als Rest zu 100 %“; 2021-OS-K5b (hier geführt, Typ bei prozentrechnung.md).')
T('daten', '3.8', 'Sektoren nach Größe den Angaben zuordnen', ['Sektor im Kreisdiagramm zuordnen'],
  'Definition „unbeschrifteten Sektor anhand der Anteile einer Tabelle identifizieren“; 2024-OS-K2c, 2022-OS-K4d, Nebenleistung in 2021-OS-K5b und 2017-OS-K2c.')
T('daten', '3.9', 'Anteil aus einem Sektor schätzen (Viertel, Drittel, Hälfte)', ['Sektor im Kreisdiagramm zuordnen', 'Kreissektor Anteil berechnen'],
  'Die Größe eines Sektors als Anteil einschätzen ist der Schritt beim Zuordnen (2022-OS-K4d: 18 %, 27 %, 39 % nach Größe); rechnerisch ist es der „Anteil eines Kreissektors an der Kreisfläche aus dem Mittelpunktswinkel“ (2025-OS-B1e, Typ bei kreis.md).')
T('daten', '4.1', 'Minimum und Maximum aus Liste, Tabelle, Diagramm', ['Minimum und Maximum ablesen', 'Spannweite berechnen'],
  '2014-OS-K4a (Tabelle), 2022-OS-K4a (Säulendiagramm); 2023-OS-K6c fragt Minimum und Maximum als eigene Angaben vor der Spannweite.')
T('daten', '4.2', 'Spannweite (auch Dezimalzahlen und große Zahlen)', ['Spannweite berechnen'],
  'Definition „Differenz von Maximum und Minimum“; Dezimalzahlen in 2019-OS-B1i (0,4 m) und 2026-FOR-K3a (0,08 €), große Zahlen in 2023-OS-K6c (1010 Mio.).')
T('daten', '4.3', 'Modalwert', ['Modalwert bestimmen', 'Kenngrößen einer Liste prüfen'],
  'Definition „Modalwert (häufigster Wert)“ (2016-GYM-K3c, 2020-GYM-K6c, 2023-GYM-K5c); in 2025-OS-K6a ist der angegebene Modalwert 4 auf 2 zu berichtigen.')
T('daten', '4.4', 'Median bei ungerader Anzahl (sortieren)', ['Median bestimmen'],
  'Definition „nach dem Sortieren bestimmen“; 2015-OS-B1f (sieben Werte, der vierte ist 5 °C).')
T('daten', '4.5', 'Median bei gerader Anzahl', ['Median bestimmen'],
  'Definition „bei gerader Anzahl als Mitte der beiden mittleren Werte“; 2024-OS-B1h (sechs Werte, 19 °C).')
T('daten', '4.6', 'arithmetisches Mittel aus einer Liste', ['Arithmetisches Mittel berechnen'],
  'Definition „Durchschnitt einer Datenliste“; 2021-OS-B1f, 2017-OS-B1h, 2016-OS-B1a.')
T('daten', '4.7', 'aus Tabelle oder Diagramm', ['Arithmetisches Mittel berechnen'],
  'Werte aus einem Diagramm in 2020-OS-K2c (Besucher), 2022-OS-K4a (Bücher-Säulen, Nebentyp) und 2024-OS-K2b (Niederschläge).')
T('daten', '4.8', 'sinnvoll runden (Zuschauer je Spiel)', ['Arithmetisches Mittel berechnen'],
  '2015-OS-K7a: 680 353 : 17 = 40 020,76 …, auf ganze Zuschauer oder Tausender sinnvoll gerundet.')
T('daten', '4.9', 'Mittel aus Gesamtsumme und Anzahl', ['Arithmetisches Mittel berechnen'],
  'Aus der Summe durch die Anzahl in 2015-OS-K7a (680 353 Zuschauer auf 17 Heimspiele) und 2024-OS-K2b (Jahressumme 581,7 mm durch 12).')
T('daten', '4.10', 'fehlender Wert aus Mittelwert und den übrigen Werten', ['Fehlenden Wert aus Mittelwert bestimmen'],
  'Definition „aus dem Mittelwert und den übrigen Werten einer Liste den fehlenden Wert“; 2022-OS-B1d (7 · 20 − 122 = 18 °C), 2023-GYM-K5d.')
T('daten', '4.11', 'Mittelwert nach Hinzufügen oder Entfernen begründen', ['Veränderung des Mittelwerts begründen'],
  'Der P10-Typ verlangt genau diese Begründung (Definition „Erklären, wie sich Hinzufügen oder Entfernen einzelner Werte auf den Mittelwert auswirkt“); 2025-OS-K6c (Nebentyp).')
T('daten', '4.12', 'Aussagen zu Kenngrößen prüfen und korrigieren', ['Kenngrößen einer Liste prüfen', 'Behauptung prüfen'],
  'Definition „Aussagen zu Spannweite, Modalwert, Median oder Mittelwert … prüfen und korrigieren“ (2025-OS-K6a); Behauptungen zu Kenngrößen prüfen 2020-OS-K2d (Spannweite 150) und 2026-FOR-K3b (Durchschnitt unter 1,80 €), beide mit Nebentyp „Behauptung prüfen“.')
T('daten', '5.1', 'Aussage zum Verlauf prüfen („immer weniger“ – gibt es einen Anstieg dazwischen?)', ['Aussage zu Diagramm prüfen', 'Behauptung prüfen'],
  '2022-OS-K4c prüft „Von Jahr zu Jahr lesen immer weniger“ trotz Anstieg 2018 → 2019, mit Nebentyp „Behauptung prüfen“; ebenso 2019-OS-K5c („nimmt von Jahr zu Jahr extrem ab“).')
T('daten', '5.2', 'Aussage zur Veränderung prüfen („mehr als die Hälfte“, „um ein Drittel mehr“)', ['Aussage zu Diagramm prüfen', 'Prozentuale Veränderung berechnen', 'Behauptung prüfen'],
  '„Um mehr als die Hälfte reduziert“ prüft 2022-OS-K4c, „Abnahme um 75 %“ 2022-GYM-K6c; „ein Drittel mehr“ weist 2020-OS-K2d mit den Nebentypen „Prozentuale Veränderung berechnen“ und „Behauptung prüfen“ nach.')
T('daten', '5.3', '„jede 15.“ gegen 15 %', ['Aussage zu Diagramm prüfen', 'Prozent und Anteil umwandeln', 'Behauptung prüfen'],
  '2018-OS-K3d: „jede 15. Frau“ als 1/15 ≈ 6,7 % gegen 15 % im Diagramm, mit den Nebentypen „Prozent und Anteil umwandeln“ (Typ bei prozentrechnung.md) und „Behauptung prüfen“.')
T('daten', '5.4', 'zwei Teilaussagen getrennt prüfen', ['Aussage zu Diagramm prüfen', 'Behauptung prüfen'],
  'Zwei Teilbehauptungen getrennt prüfen 2022-OS-K4c (Fehlerquelle „nur den ersten Teil prüfen“) und 2018-OS-K3d, zwei Aussagen nachweisen 2020-OS-K2d, alle mit Nebentyp „Behauptung prüfen“.')
T('daten', '5.5', 'abgeschnittene Achse erklären (Säulenhöhe zeigt nur den Teil über dem Achsenanfang)', ['Verzerrung eines Diagramms erklären'],
  'Definition „abgeschnittene Achse“; 2014-OS-K3d (ab 1060 €), 2026-FOR-K3e (ab 1,75 €), Nebentyp in 2019-OS-K5c (ab 30 %).')
T('daten', '5.6', 'gedehnte Achse', ['Verzerrung eines Diagramms erklären'],
  'Definition „abgeschnittene Achse, Skalierung“; 2014-OS-K3d: die y-Achse ist abgeschnitten und stark gedehnt.')
T('daten', '5.7', 'Fortschreibung eines Trends prüfen', ['Aussage zu Diagramm prüfen'],
  '2019-OS-K5c: „in wenigen Jahren liest kein Jugendlicher mehr ein Buch“ – bei zwei Prozentpunkten je Jahr erst nach rund 18 Jahren, die Fortschreibung ist unzulässig.')
T('daten', '5.12', 'Fehler finden (Verdopplung der Säulenhöhe als Verdopplung des Werts; nur „die Säulen sind verschieden hoch“ ohne die Achse)', ['Verzerrung eines Diagramms erklären'],
  'Der P10-Typ verlangt genau diese Fehleranalyse: 2026-FOR-K3e erklärt Fabios Schluss von der verdoppelten Säulenhöhe auf den verdoppelten Preis, und die Fehlerquelle von 2014-OS-K3d ist die Antwort „die Säulen sind unterschiedlich hoch“ ohne Bezug zur Achse.')
T('daten', '5.13', 'Begründen (warum die Achse bei 0 beginnen sollte)', ['Verzerrung eines Diagramms erklären'],
  'Definition „Erklären, warum ein Diagramm (abgeschnittene Achse, Skalierung) einen falschen Eindruck erzeugt“ ist dieselbe Begründung am konkreten Diagramm (2014-OS-K3d, 2026-FOR-K3e).')

# ==== wahrscheinlichkeit ====
U('wahrscheinlichkeit', 1, ['Ergebnismenge aufzählen', 'Anzahl der Anordnungen bestimmen', 'Größte Zahl aus Ziffern bilden', 'Anzahl der Dreiecke aus Punkten bestimmen'])
U('wahrscheinlichkeit', 2, ['Wahrscheinlichkeit einstufig', 'Zufallsgerät zu Wahrscheinlichkeit entwerfen'])
U('wahrscheinlichkeit', 3, ['Baumdiagramm ergänzen', 'Wahrscheinlichkeit mehrstufig unabhängig', 'Wahrscheinlichkeit über Gegenereignis berechnen'])
U('wahrscheinlichkeit', 4, ['Wahrscheinlichkeit mehrstufig ohne Zurücklegen', 'Baumdiagramm ergänzen'])
T('wahrscheinlichkeit', '1.1', 'Möglichkeiten aufzählen (Kleidung, Menü, Wege) und zählen', ['Ergebnismenge aufzählen', 'Anzahl Kombinationen nach dem Zählprinzip bestimmen'],
  'Systematisches Auflisten wie in 2017-OS-B1f und 2025-OS-K3a, hier als Kontextvariante außerhalb eines Zufallsversuchs; das Zählen von Menü-Kombinationen verlangt 2017-GYM-K5d (belegte Brötchen, 2 · 6 · 2 = 24).')
T('wahrscheinlichkeit', '1.2', 'Zählprinzip: Anzahl der Kombinationen als Produkt', ['Anzahl Kombinationen nach dem Zählprinzip bestimmen', 'Anzahl der Anordnungen bestimmen'],
  'Definition „durch Multiplikation der jeweiligen Möglichkeiten“ (2017-GYM-K5d, 2018-GYM-K5c: 4 · 4); „Anzahl der Anordnungen bestimmen“ zählt nach Definition auch über das Zählprinzip (2017-OS-K6b: 3 · 2 · 1).')
T('wahrscheinlichkeit', '1.3', 'alle zweistelligen Zahlen aus zwei Ziffernscheiben (doppelte Ziffern nur einmal)', ['Ergebnismenge aufzählen'],
  '2025-OS-K3a: neun zweistellige Zahlen aus den Scheiben 1, 2, 1, 3 und 2, 3, 2, 1.')
T('wahrscheinlichkeit', '1.4', 'Anordnungen von drei Ziffern oder drei Personen (auflisten, dann 3 · 2 · 1)', ['Anzahl der Anordnungen bestimmen'],
  'Definition „durch Auflisten oder Zählprinzip“; 2016-OS-K5b (sechs Zahlen aus 2, 3, 6 auflisten), 2017-OS-K6b (3 · 2 · 1 = 6).')
T('wahrscheinlichkeit', '1.5', 'größte und kleinste Zahl aus Ziffern', ['Größte Zahl aus Ziffern bilden'],
  'Definition „die größte (oder kleinste) Zahl bilden“; 2016-OS-K5a (632).')
T('wahrscheinlichkeit', '1.6', 'Ergebnismenge zweier Münzen (ZZ, ZW, WZ, WW)', ['Ergebnismenge aufzählen'],
  '2017-OS-B1f: zwei Münzen, vier Ergebnisse ZZ, ZW, WZ, WW (ebenso 2017-GYM-B1f).')
T('wahrscheinlichkeit', '1.7', 'Paare beim zweifachen Würfeln mit Bedingung (zweiter Wurf 2)', ['Ergebnismenge aufzählen'],
  '2020-OS-K6a: alle Augenpaare mit zweiter Augenzahl 2 aufzählen.')
T('wahrscheinlichkeit', '1.8', 'Ergebnisse zu „mindestens einmal …“ aufzählen', ['Ergebnismenge aufzählen'],
  'Nebenleistung in 2018-OS-K7c: alle Ergebnisse mit mindestens einem Senf-Pfannkuchen aufzählen.')
T('wahrscheinlichkeit', '1.9', 'Dreiecke aus fünf Punkten (Punkte auf einer Geraden ausschließen)', ['Anzahl der Dreiecke aus Punkten bestimmen', 'Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen'],
  '2015-OS-K5a (8 Dreiecke, Punkte auf einer Geraden ausgeschlossen); sein Rechenweg „10 Dreierauswahlen aus 5 Punkten“ ist die Auswahl ohne Reihenfolge der Definition „Kombination ohne Wiederholung“ (2019-GYM-K5b: fünf über drei gleich 10).')
T('wahrscheinlichkeit', '2.1', 'P eines Ergebnisses beim Würfel, Glücksrad mit gleich großen Feldern, Urne', ['Wahrscheinlichkeit einstufig'],
  'Definition „günstige durch mögliche Fälle“; Würfel 2026-FOR-K6a, Glücksrad 2014-OS-K6a, Stiftekiste 2019-OS-K6a.')
T('wahrscheinlichkeit', '2.2', 'P als Bruch, gekürzt, als Dezimalzahl und Prozent', ['Wahrscheinlichkeit einstufig', 'Prozent und Anteil umwandeln'],
  'P als Bruch und in Prozent in 2014-OS-K6a (3/8 = 37,5 %) und 2017-OS-K6a (1/10 = 10 %), beide mit Nebentyp „Prozent und Anteil umwandeln“ (Typ bei prozentrechnung.md).')
T('wahrscheinlichkeit', '2.3', 'Ereignis aus mehreren Ergebnissen (Summenregel: „gerade Zahl“, „weder 1 noch 6“)', ['Wahrscheinlichkeit einstufig'],
  '2014-OS-B1d („weder 1 noch 6“: 4/6) und Nebenleistung in 2016-OS-K5b (P(gerade) = 4/6).')
T('wahrscheinlichkeit', '2.4', 'Gesamtzahl aus dem Text finden (Nieten plus Gewinne; Lose 101 bis 900 sind 800)', ['Wahrscheinlichkeit einstufig'],
  '2014-OS-B1b (80 Nieten und 20 Gewinne), 2016-OS-B1f (100 Lampen, 5 kaputt), 2016-OS-K5c (Lose 101 bis 900 sind 800).')
T('wahrscheinlichkeit', '2.5', 'Gegenereignis einstufig (1 − P)', ['Wahrscheinlichkeit über Gegenereignis berechnen', 'Wahrscheinlichkeit einstufig'],
  'Definition „über 1 − P(Gegenereignis)“, der einstufige Fall ist der Grundfall desselben Verfahrens; 2014-OS-B1d löst „weder 1 noch 6“ auch als 1 − 2/6.')
T('wahrscheinlichkeit', '2.6', 'Zufallsgerät entwerfen: Anzahl der Felder oder Kugeln zu gegebener Wahrscheinlichkeit; Kugeln einzeichnen; Topf mit P = 50 % auswählen', ['Zufallsgerät zu Wahrscheinlichkeit entwerfen', 'Wahrscheinlichkeit einstufig'],
  'Felder und Kugeln zu einer Wahrscheinlichkeit in 2018-OS-B1j (40 % sind 2 von 5 Feldern) und 2019-OS-B1g (Kugeln einzeichnen); den Topf mit P = 50 % wählt 2015-OS-B1a mit Haupttyp „Wahrscheinlichkeit einstufig“.')
T('wahrscheinlichkeit', '2.7', 'veränderte Grundmenge (zwei Pfannkuchen sind schon weg)', ['Wahrscheinlichkeit einstufig', 'Wahrscheinlichkeit mehrstufig ohne Zurücklegen'],
  '2018-OS-K7b (nach zwei entnommenen Pfannkuchen 2/14 statt 2/16); die nach einer Entnahme verkleinerte Grundmenge ist die Stufe der Definition „ohne Zurücklegen“ (2015-GYM-K3c: nach Lisas Zug bleiben 5 Plätze).')
T('wahrscheinlichkeit', '2.8', 'Grundmenge einschränken (nur die Lose mit Endziffer 6)', ['Wahrscheinlichkeit einstufig'],
  '2016-OS-K5d: nur die 80 Lose mit Endziffer 6 bilden die Grundmenge, P = 7/80.')
T('wahrscheinlichkeit', '2.9', 'relative Häufigkeit einer Versuchsreihe mit P vergleichen; erwartete Anzahl bei n Versuchen', ['Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen'],
  'Die erwartete Anzahl ist das „Produkt aus Wahrscheinlichkeit und Anzahl“ der Definition (2025-GYM-K6b: 1000 · 0,015 = 15); den Vergleich einer Versuchsreihe mit P verlangt kein P10-Typ.')
T('wahrscheinlichkeit', '2.10', 'Behauptung prüfen', ['Behauptung prüfen', 'Wahrscheinlichkeit einstufig'],
  'Einstufige Behauptungen mit Nebentyp „Behauptung prüfen“ in 2016-OS-K5c (P = 1/800), 2016-OS-K5d (P = 7/80) und 2018-OS-K7b (Pias 2/16).')
T('wahrscheinlichkeit', '3.1', 'Baum zu zwei Drehungen oder zwei Würfeln zeichnen', ['Baumdiagramm ergänzen'],
  'Die P10 gibt das Astgerüst vor und verlangt alle Wahrscheinlichkeiten: 2014-OS-K6b (zwei Drehungen, nur P(C) = 1/8 eingetragen), 2026-FOR-K6b (zwei Würfel).')
T('wahrscheinlichkeit', '3.2', 'Astwahrscheinlichkeiten ergänzen (Summe an jedem Punkt 1)', ['Baumdiagramm ergänzen'],
  'Definition „Fehlende Wahrscheinlichkeiten in einem Baumdiagramm eintragen (Knotensumme 1)“; 2014-OS-K6b, 2024-OS-K5b.')
T('wahrscheinlichkeit', '3.3', 'P eines Pfades (Pfadregel)', ['Wahrscheinlichkeit mehrstufig unabhängig'],
  'Definition „mit Pfad- und Summenregel“; ein Pfad in 2025-OS-K3b (P(33) = 1/4 · 1/4) und 2026-FOR-K6b (3/6 · 5/6).')
T('wahrscheinlichkeit', '3.4', 'P eines Ereignisses aus mehreren Pfaden (Summenregel: „12 oder 21“)', ['Wahrscheinlichkeit mehrstufig unabhängig'],
  '2025-OS-K3c: P(12 oder 21) = 4/16 + 1/16 = 5/16.')
T('wahrscheinlichkeit', '3.5', '„zweimal derselbe Buchstabe“ (drei Pfade)', ['Wahrscheinlichkeit mehrstufig unabhängig'],
  '2014-OS-K6c: zweimal derselbe Buchstabe als Summe der Pfade AA, BB und CC.')
T('wahrscheinlichkeit', '3.6', '„mindestens einmal“ über 1 − P(nie)', ['Wahrscheinlichkeit über Gegenereignis berechnen', 'Wahrscheinlichkeit mehrstufig unabhängig'],
  'Definition „mit ‚mindestens‘ formuliertes Ereignis über 1 − P(Gegenereignis)“; P(nie) ist ein Pfad mit unabhängigen Stufen (2024-GYM-K6b: in keiner der drei Nächte 0,8³).')
T('wahrscheinlichkeit', '3.7', '„nicht zweimal gerade“', ['Wahrscheinlichkeit über Gegenereignis berechnen'],
  '2026-FOR-K6c: P(nicht zweimal gerade) = 1 − 3/36 = 11/12.')
T('wahrscheinlichkeit', '3.8', 'dreistufig („mindestens zwei Sechsen“)', ['Wahrscheinlichkeit mehrstufig unabhängig', 'Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen'],
  '2020-OS-K6c berechnet P(mindestens zwei Sechsen) über drei Stufen (Nebentyp „mehrstufig unabhängig“); die Pfade zu „mindestens zwei von drei“ zählt 2019-GYM-K5c.')
T('wahrscheinlichkeit', '3.9', 'Behauptung prüfen (P(22) = P(33)? P(gleich) gegen P(erst 6))', ['Wahrscheinlichkeit mehrstufig unabhängig', 'Behauptung prüfen'],
  'Genau diese Behauptungen prüfen 2025-OS-K3b (P(33) gegen P(22)) und 2020-OS-K6b (zwei gleiche Augenzahlen gegen zuerst eine 6), beide mit Nebentyp „Behauptung prüfen“.')
T('wahrscheinlichkeit', '3.10', 'Zufallsgerät mehrstufig belegen (Produkt 1/4; Würfelnetz für P(Summe 2))', ['Zufallsgerät zu Wahrscheinlichkeit entwerfen', 'Wahrscheinlichkeit mehrstufig unabhängig', 'Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen'],
  'Definition „ein- oder mehrstufig“: 2025-OS-K3d (P(13) = 2/4 · 2/4) und 2026-FOR-K6d (Würfel B für P(Summe 2) = 1/6), beide mit Nebentyp „mehrstufig unabhängig“; die Einzelwahrscheinlichkeit aus dem Produkt zurückrechnen verlangt auch 2025-GYM-K6c.')
T('wahrscheinlichkeit', '4.1', 'Baum für zweimal Ziehen ohne Zurücklegen (Nenner minus 1)', ['Baumdiagramm ergänzen', 'Wahrscheinlichkeit mehrstufig ohne Zurücklegen'],
  'Baum mit verkleinertem Nenner in 2019-OS-K6b (16/20, 3/18) und 2015-OS-K7d (10/11, 1/10), beide mit Nebentyp „ohne Zurücklegen“ (Definition „verkleinerte Grundmenge“).')
T('wahrscheinlichkeit', '4.2', 'P zweier gleicher Farben', ['Wahrscheinlichkeit mehrstufig ohne Zurücklegen'],
  '2018-OS-K7c (P(beide Marmelade) = 14/16 · 13/15, Ereignis E „beide gleich“) und 2015-GYM-K3c (beide im gleichen Zimmer).')
T('wahrscheinlichkeit', '4.3', 'zweite Person zieht (erste Stufe mitrechnen: erst kein Joker, dann Joker)', ['Wahrscheinlichkeit mehrstufig ohne Zurücklegen'],
  '2024-OS-K5c: Klara zieht als Zweite den Joker, 4/5 · 1/4; ebenso 2017-GYM-K5c (zweiter Schlüssel, 6/7 · 1/6).')
T('wahrscheinlichkeit', '4.4', 'dreistufig, ein Pfad (drei rote Stifte)', ['Wahrscheinlichkeit mehrstufig ohne Zurücklegen'],
  'Dreistufig ein Pfad in 2019-OS-K6c (drei blaue, drei gelbe Stifte) und als Nebenleistung in 2019-OS-K6b (dreimal rot, 4/20 · 3/19 · 2/18).')
T('wahrscheinlichkeit', '4.5', 'Baum mit leeren Feldern nach verschiedenen Vorgeschichten ergänzen', ['Baumdiagramm ergänzen', 'Wahrscheinlichkeit mehrstufig ohne Zurücklegen'],
  '2019-OS-K6b (zwei leere Felder nach verschiedenen Vorgeschichten) und 2015-OS-K7d (vier leere Felder), beide Haupttyp „Baumdiagramm ergänzen“ mit Nebentyp „ohne Zurücklegen“.')
T('wahrscheinlichkeit', '4.6', '„unter den ersten drei“ (Summe dreier Pfade oder Gegenereignis)', ['Wahrscheinlichkeit mehrstufig ohne Zurücklegen', 'Wahrscheinlichkeit über Gegenereignis berechnen'],
  '2015-OS-K7d: P(Ronny unter den ersten drei) als Summe dreier Pfade oder als 1 − 10/11 · 9/10 · 8/9 (Gegenereignis als Rechenweg laut Prüfungsform); 2018-GYM-K5d summiert zwei Pfade.')
T('wahrscheinlichkeit', '4.7', 'Vergleich mit Zurücklegen (Behauptung „doppelt so hoch“)', ['Wahrscheinlichkeit mehrstufig ohne Zurücklegen', 'Wahrscheinlichkeit mehrstufig unabhängig', 'Behauptung prüfen'],
  '2019-OS-K6c widerlegt „doppelt so hoch“ ohne Zurücklegen (Nebentyp „Behauptung prüfen“, Fehlerquelle „mit Zurücklegen rechnen“); den Vergleichswert mit Zurücklegen rechnet die Definition von „Wahrscheinlichkeit mehrstufig unabhängig“.')
T('wahrscheinlichkeit', '4.8', 'Ereignis zu einer gegebenen Rechnung in Worten', ['Ereignis zu Wahrscheinlichkeitsterm beschreiben', 'Gleichung im Sachzusammenhang deuten'],
  'Definition „zu einem gegebenen Wahrscheinlichkeitsterm das Ereignis in Worten beschreiben“ (2018-GYM-K4c, Nebentyp in 2019-GYM-K5c); in 2018-OS-K7c trägt dieselbe Leistung den Nebentyp „Gleichung im Sachzusammenhang deuten“ (Typ bei lineare-gleichungssysteme.md).')

# ==== Verfahrensgeber laut Zuordnungszeile (Daten V) ====
# potenzen-wurzeln: „Einheit 3 – … dazu das Verfahren … für … „Quadratseite aus Fläche berechnen“ (2020-OS-B1d, flaechen.md)“
V('potenzen-wurzeln', 3, ['Quadratseite aus Fläche berechnen'])
# pythagoras: „Einheit 2 – … Umkehrung als Verfahren für Rechten Winkel begründen (Typ in winkel-dreiecke.md Einheit 3)“
V('pythagoras', 2, ['Rechten Winkel begründen'])
# terme: „Die Typen „Termwert berechnen“ …, „Term zu Figur angeben“ … und „Term zu Körper angeben“ … hier sind sie Verfahren der Einheit 1“
V('terme', 1, ['Termwert berechnen', 'Term zu Figur angeben', 'Term zu Körper angeben'])
# lineare-gleichungen: „Einheit 3 – kein Typ (Verfahren der Einheit 2 in schwererer Form)“
V('lineare-gleichungen', 3, ['Lineare Gleichung lösen'])
# binomische-formeln: „Einheit 2 – Verfahren für „Scheitelpunktform in Normalform umformen“ (… quadratische-funktionen.md Einheit 3)“;
# „Voraussetzung für Schnittpunkte Gerade und Parabel berechnen“ ist Nebenleistung und zählt nicht
V('binomische-formeln', 2, ['Scheitelpunktform in Normalform umformen'])
# quadratische-gleichungen: „Einheit 3 – kein eigener Typ: Verfahren für Nullstellen quadratische Funktion berechnen,
# Argument zu Funktionswert berechnen, Schnittpunkte Gerade und Parabel berechnen (… quadratische-funktionen.md Einheit 4)“
V('quadratische-gleichungen', 3, ['Nullstellen quadratische Funktion berechnen', 'Argument zu Funktionswert berechnen',
                                   'Schnittpunkte Gerade und Parabel berechnen'])