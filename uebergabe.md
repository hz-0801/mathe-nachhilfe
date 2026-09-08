Zuerst dieses Zip hochladen.

# Übergabe Werkstatt – Lieferung 2026-09-08h

## 1 Ziel
Der Masterprompt soll Blätter liefern, mit denen ein schwacher Schüler bis Klasse 10 eine Einheit lang allein arbeiten kann: Schwerpunkt jeder Hauptnummer unten, Prüfungsniveau nur als Zielmarke, Schreibform des Verfahrens auf dem Blatt. Gleiche Qualität, weniger Korrekturrunden. Der Prüfungsprompt baut dasselbe für Themen mit Katalog.

## 2 Arbeitsgrundlage
- `masterprompt.md` v3.34 – maßgeblich; Änderungen in 2.1 (Erkennungsschritte keine Typen), 2.2 (Budget 6/2/5, Rasterdeckel gestrichen, Beispiel- und Kastenzahlen in keiner Teilaufgabe, ungebrauchte Fertigkeit nicht in Aufgabe 1), 3.1 (Zahlenbeispiele statt Buchstabenformel, Muster und Gegenmuster), 3.2 (Zeilenzahlen), 5.1 b, 6.3 (Teile-Zeilen-Muster, t0 in eigenem Aufruf).
- `pruefungsprompt.md` v0.14 – gemeinsame Abschnitte 3.2, 5.1 b, 6.3 wie v3.34; 2.2 Beispielzahlen; sonst unverändert.
- `mathblatt.sty` 2026-09-07d – unverändert.
- `Anleitung_mathblatt.md` – zu 07d, fünf Ergänzungen (Kasten ohne `&`, `teilezwei`-Zeichenzahl, `\\` gegen gedehnte Zeile, `\kreuz` untereinander, Raster in der Buchstabenzählung).
- `Testauswertung_Masterprompt_Mathe_2026-09-08.md` – Budget 6/2/5, Prüfpunkte Beispielzahlen, Vorstufe in der Hauptnummer, Buttons kurz/lang, t0, Feld allein erlaubt.
- `CHANGELOG.md` – Einträge v3.34, v0.14, Anleitung 08.09.
- `blatt-konzept.md` liegt weiterhin nicht bei.

## 3 Arbeitsstand
Abgeschlossen: Auswertung Glg T1, Terme T1, Terme T2 (v3.33) und Prozent-Heft (v0.13), alle Fable 5.1, Vorlage 07d. Alle Archive korrekt versioniert, Zählungen stimmig, 0 Abweichungen, keine Log-Warnungen. Messwerte: Glg 2/9, 316 s (vorher 1/5, 213 s); Terme T1 0/3, 160 s (0/3, 211 s); Terme T2 1/3, 37 s (Messfehler, t0 im Aufruf mit dem Quelltext); Prozent 1/6, 512 s (2/12, 565 s).
Befunde P: Beispiel als erste Teilaufgabe kopiert (alle drei Masterprompt-Blätter); Teile-Zeile aus dem Prompt-Muster „Grundlagen · Verfahren · Anwendung" übernommen; Rasterdeckel 10 gerissen (Glg 3: 12, Terme T2 2: 11); Vorstufe als eigene Hauptnummer (Terme T1); Kasten mit Beispielen (Terme T1) und Sätzen (Glg); Punkt vor Strich in Aufgabe 1 ohne Stelle auf dem Blatt (Terme T1, aus dem Prompt-Beispiel); Umgruppierung gegen 4.3 zur Budgetrettung (Glg); Textkürzung 6c (Terme T2); Glg-Teilauswahl ohne „lang"-Button. A: `&` im Kasten (zweiter Lauf), zwei greps ins .sty, `teilezwei`-Überläufe (Terme T2 5i, Prozent 7a–e). L: halb leere Seiten Glg 1/2/4, Prozent 2. Offen V: Felder allein in der nächsten Zeile (Prozent achtmal, Folge von 07d), `\kreuz`-Umbruch (Prozent 2h).
Alle Änderungen dieser Lieferung sind ungetestet.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen
- Kein Rasterdeckel; es gelten zwölf je Verfahrens-Hauptnummer und das Budget. Reicht der Platz nicht, wandert ein Typ, nie eine Sprosse.
- Budget 6 Hauptnummern, 2 Grafiken, 5 Seiten – Maßstab ist Erzeugungszeit, das Raster kostet Papier, keine Zeit. 4.3 (Umgruppieren nur unter einem Drittel, nie nach den Ergebnissen) bleibt.
- Kasten: Formel, wo sie ohne Buchstaben als Vorzahlen geht; sonst ein bis drei Zahlenbeispiele je Regel; nie beides. Terme-Kasten aus T1 ist das Muster.
- Beispiel- und Kastenzahlen kommen in keiner Teilaufgabe vor.
- Erkennungsschritte sind Vorstufe innerhalb der Hauptnummer, nie ein Typ.
- Feld allein in der nächsten Zeile ist erlaubt (07d); Befund ist nur die gedehnte Zeile und jede Textkürzung.
- Layout-Fahrplan beschlossen, noch nicht gebaut: 07i Vorlage 07e mit Flattersatz im Aufgabenteil und `teilezwei` als Spaltensatz statt Tabelle; 07j Feld füllt Restzeile, Kästchen-Makro, nur wenn nach 07i noch nötig; 07k Seitenumbruch innerhalb einer Hauptnummer an sicheren Stellen (Beispiel + erste Zeile zusammen, Grafik mit Text), eigenes Testblatt vorab, danach Budget ggf. zurück auf vier.
- Weiterhin aus 07g: Beispiel in Schreibform, Zwischenzeile nur im ersten Beispiel, Einsetzen mit „(wA)"; Rechenplatz-Verbot mit Raster-Ausnahme; Layout nie durch Textänderung; Rangfolge Einstieg vor Typenvollständigkeit; genau ein Stern je Hauptnummer; Hilfe-Seite bis Kl. 10 nur auf „mit hilfe"; keine neuen Signalwörter.

## 5 Offene Punkte und verworfene Ansätze
Offen:
- Reißt eine Raster-Hauptnummer die Zwölf (Vorstufe fünf plus Kette acht), sagt der Prompt nicht, was fällt; einzige Stelle mit Spiel wäre die Vorstufe auf vier. Erst regeln, wenn es vorkommt.
- Prüfungsprompt: Hauptnummer 6 im Prozent-Heft hat 13 Teilaufgaben (sechs Originale); kein Deckel im Prüfungsprompt, offen, ob einer sinnvoll ist.
- Prüfungsprompt: Hilfe-Seite bleibt an; Kl.-10-Regel dort nicht entschieden. Grenzfall „die Oma zahlt keinen Kinderpreis" (halber Rechenweg in 4.2) stehen gelassen.
- Reproduzierbarkeit des Schnitts, Auslöser-Inventar (aus 07f).
Verworfen:
- Rasterdeckel 12 oder Deckel als Teilaufgaben × Zeilen ≤ 26: jede Zahl gilt nur für das Thema, an dem sie gemessen wurde; das Budget regelt es schon.
- 4.3-Ausnahme „Umgruppieren bei einer Seite über Budget": unnötig, wenn das Budget fünf ist.
- Kasten bei Terme entfallen lassen: der Schüler schlägt beim Rechnen genau das nach.
- Kasten mit Buchstabenformeln: für Kl. 8 unlesbar, gegen 3.6.
- Aus 07g weiterhin: Vorstufe als eigene Hauptnummer, Linien im Raster weglassen, Zwischenzeile in jedem Beispiel, Button „alle", Teil 0.

## 6 Nächster Arbeitsschritt
Bau im Aufgaben-Projekt mit dieser Lieferung, Archive dann in einen neuen Werkstatt-Chat mit diesem Zip:
* Masterprompt v3.34: „lineare gleichungen kl.8", Antwort 1 → Teile-Zeile wortgleich, Kasten ohne Sätze, 2a nicht das Beispiel, Buttons kurz und lang, Seiten gegen fünf, keine Umgruppierung.
* Masterprompt v3.34: „terme zusammenfasssen kl.8" (Schreibweise wie am 08.09.), Antwort 1 → Vorstufe in Aufgabe 3 statt eigener Hauptnummer, Kasten nach Muster, Aufgabe 1 ohne Punkt vor Strich, 3a/5a nicht das Beispiel.
* Prüfungsprompt v0.14: „prozent" → t0 in eigenem Aufruf, Sekundenzahl plausibel, Beispielzahlen.
Auswertung nach Testauswertung 2026-09-08; Vergleichswerte Glg 2/9, 316 s; Terme T1 0/3, 160 s; Prozent 1/6, 512 s. Danach Lieferung 07i (Vorlage 07e) nach dem Fahrplan in Abschnitt 4.
