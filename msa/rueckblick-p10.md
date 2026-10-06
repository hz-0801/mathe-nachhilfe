# Rückblick je Stufe P10

Stand 2026-10-06 (Auftrag K Schritt 4). Datei: `msa/rueckblick-p10.csv`
(kapitel;stufe;voraussetzung;aufgabe;form;loesung;gebraucht_ab). Regel:
Beschluss N2.10 (ersetzt Punkt 18), Muster Grundwert.

- 46 Zeilen für die 45 Kern-Stufen der Zuordnungsdateien (`kern` = ja):
  das sind die Stufen, die eine Portion oder ein Fokusblatt eröffnen.
  Nicht-Kern-Stufen hängen an einer Kern-Stufe und bekommen deren
  Rückblick.
- Eine Zeile je Voraussetzung, die die Leiter gleich braucht; meist eine
  zusammenhängende Aufgabe (Tabelle) statt verstreuter. Prozentwert und
  Grundwert haben zwei Zeilen (Tabelle Prozent | Bruch | Dezimalzahl
  und eine Kopfrechenaufgabe).
- Die Voraussetzungen kommen aus dem Feld `voraussetzungen` der echten
  Aufgaben der Stufe und aus deren `verfahren`; wo das Feld leer ist
  (Prozentwert, Grundwert, Scheitelpunkt), aus dem ersten Rechenschritt
  der Aufgaben.
- `gebraucht_ab`: die echten Aufgaben, in denen die Rückblick-Aufgabe
  wiederkommt (Prüfstein N2.10). Eine laufende Nummer gibt es erst im
  gebauten Heft; das Bauprogramm setzt dort die Nummer der ersten
  genannten Aufgabe ein. Bei Grundwert zuerst die Leiter-Sprosse
  (1 %-Schritt, N2.11).
- Keine Taschenrechner-Übung (N2.10).
- Jeder Zahlenwert der Lösungen mit sympy nachgerechnet (0 Abweichungen).
