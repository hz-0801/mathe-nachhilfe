Zuerst dieses Zip hochladen.

# Übergabe Werkstatt – Lieferung 2026-09-07g

## 1 Ziel
Der Masterprompt soll Blätter liefern, mit denen ein schwacher Schüler bis Klasse 10 eine Einheit lang allein arbeiten kann: Schwerpunkt jeder Hauptnummer unten, Prüfungsniveau nur als Zielmarke, und das Blatt zeigt die Schreibform, in der gerechnet werden soll. Gleiche Qualität, weniger Korrekturrunden.

## 2 Arbeitsgrundlage
- `masterprompt.md` v3.33 – maßgeblich; Änderungen in 2.2 (Beispiel in Schreibform, Muster Gleichungsraster, Obergrenze je Verfahrens-Hauptnummer), 2.2 Pflichtelemente (Fehler finden mit `\rechnung`), 3.1, 3.2 (Raster-Ausnahme), 4.6 (Inhaltstreue), 5.1 e, 6.3.
- `pruefungsprompt.md` v0.13 – gemeinsame Abschnitte 2.2, 3.2, 4.6, 5.1 e wie v3.33; sonst unverändert.
- `mathblatt.sty` 2026-09-07d – `gleichungsraster`/`\gl`/`\sgl`, `\beispiel`/`\rechnung`, Felder mit Einheit (`\leerfeld[\%]`, `\feld[cm]{l}`), Umbruch vor Feldern mit Strafe statt Verbot. Gegen Glg T1, Terme T1, Prozent-Heft vom 07.09. kompiliert: 0 Fehler, 0 Overfull.
- `Anleitung_mathblatt.md` – zu 2026-09-07d.
- `Testauswertung_Masterprompt_Mathe_2026-09-07.md` – Prüfpunkte Schreibform/Raster, Kasten ohne Fertigkeiten aus Aufgabe 1, Textkürzung für Layout = P, Teile-Zeile wortgleich.
- `CHANGELOG.md` – Einträge v3.33, v0.13, Vorlage 07d.
- `blatt-konzept.md` liegt weiterhin nicht bei.

## 3 Arbeitsstand
Abgeschlossen: Auswertung der Archive Glg T1 und Terme T1 (v3.32) und Prozent-Heft (v0.12), alle Fable 5.1. Alle Prüfpunkte der Lieferung 07f erfüllt (Aufgabe 1 je zwölf, `\weit`, Hilfe-Seite aus, Stern am Ende, 0 Abweichungen, keine Log-Warnungen). Messwerte: Terme T1 0 Korrekturrunden von 3, 211 s (vorher 2 von 4, 238 s); Glg T1 1 von 5, 213 s; Prozent 2 von 12, 565 s.
Befunde P: Beispiele und Fehler-finden-Vorgabe waagerecht mit Pfeilen (Folge der Zwei-Zeilen-Regel); Verfahrens-Hauptnummern mit 14–19 Teilaufgaben; Glg Teile-Zeile weicht von der Teilauswahl ab, Abweichungszeile ohne Anlass; Terme Kasten mit „Punkt vor Strich"; Prozent: vier Aufgabentexte gekürzt, um gedehnte Zeilen zu vermeiden. V: 07c-`\nobreak` dehnt Zeilen, Einheit hinter dem Feld bricht allein um (24 `\mbox`); fehlender Baustein Gleichungsraster. F: `&` im Kasten (Glg). L: Seitentausch (Prozent).
Alle Prompt-Änderungen dieser Lieferung sind ungetestet; die Vorlage ist nur gegen alte .tex und ein Werkstatt-Testblatt kompiliert.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen
- Beispiel in der Schreibform des Verfahrens, so viele Zeilen wie Schritte, keine Nebenrechnung; nur der Grundfall, nie der Sternfall. Zwischenzeile (x + 5 − 5 = 9 − 5) nur im ersten Beispiel des Blatts, auf dem der Strich neu ist. Einsetzen: „(wA)"/„(fA)" und Schluss „x = 3 ist Lösung", kein Pfeil, kein Haken.
- Rechenplatz-Verbot (3.2) bleibt; Ausnahme nur, wo die Schreibform Lerninhalt ist (senkrechte Umformung): Gleichungsraster, zwei Spalten, Zeilenzahl nach Schrittzahl des Grundfalls, graue Linien 9 mm, kein `\feld{x}`. Vorstufe „nur Umformung anschreiben" als eigenes Raster mit Kurzzeile, keine eigene Hauptnummer.
- Verfahrens-Hauptnummer höchstens zwölf Teilaufgaben, im Raster zehn (Vorstufe vier, Grundfall vier, eine mittlere, ein Stern).
- Layoutprobleme werden im Satz gelöst, nie durch Änderung von Aufgabentext oder Zahlen.
- Dreisatz-Schema als Baustein erst, wenn ein Prozent-Lauf zeigt, dass es fehlt.
- Weiterhin aus 07f: Rangfolge Einstieg vor Typenvollständigkeit; genau ein Stern je Hauptnummer; Aufgabe 1 Übung höchstens zwölf mit Hinrichtung; Hilfe-Seite bis Kl. 10 nur auf „mit hilfe"; Kasten höchstens fünf Zeilen; Budget 6/2/4; „start" ist Produkt, nicht Testeingabe; keine neuen Signalwörter.

## 5 Offene Punkte und verworfene Ansätze
Offen:
- Passt ein Glg-Teil-1 mit drei Raster-Hauptnummern in vier Seiten? Erst der Bau zeigt es; sonst Schnitt in drei Teile oder Obergrenze acht.
- Terme T1: greift das Raster dort (Zusammenfassen ist einzeilig – vermutlich nein; Ausmultiplizieren in Teil 2 vermutlich ja)?
- Terme wurde zweimal ohne „kl. 8" getestet; Deutungszeile bleibt unvergleichbar, bis die Eingabe wortgleich ist.
- Prüfungsprompt: Hilfe-Seite bleibt an; Kl.-10-Regel dort noch nicht entschieden.
- Reproduzierbarkeit des Schnitts (Terme zweimal 2 Teile); Auslöser-Inventar; `\kreuz`-Umbruch bei vielen Kästchen (aus 07f, weiter offen).
Verworfen:
- Vorstufe „Umformung anschreiben" als eigene Hauptnummer: kostet eine von sechs Hauptnummern für einen Vorschritt.
- Linien ganz weglassen (Karopapier-Gewohnheit): keine Orientierung, wo die nächste Gleichung beginnt.
- Zwischenzeile in jedem Beispiel: kostet bei Klammern und x beidseitig zu viele Zeilen; der Strich ist ab dem zweiten Beispiel bekannt.
- Aus 07f weiterhin: Button „alle"; Teil 0; „so viele Übungsaufgaben wie nötig"; zwei Sterne bei „Erhöht".

## 6 Nächster Arbeitsschritt
Teste
* Masterprompt v3.33: „lineare gleichungen kl. 8" → Teil 1 (Raster in Aufgabe 3–5, Beispiele senkrecht, Fehler finden mit `\rechnung`, Seitenzahl)
* Masterprompt v3.33: „terme zusammenfassen kl. 8" → Teil 2 („weiter"; Ausmultiplizieren im Raster?)
* Prüfungsprompt v0.13: „prozent" (Felder mit Einheit ohne `\mbox`, keine Textkürzung, Seitenzahl)
Ergebnis-Zips mit dieser Lieferung in einen neuen Chat. Auswertung nach Testauswertung; Schwerpunkt: Schreibform der Beispiele, Raster-Zeilenzahl je Hauptnummer, Teilaufgaben je Hauptnummer, Seiten vor dem Begleitteil, Korrekturrunden gegen Glg 1/5, Terme 0/3, Prozent 2/12.
