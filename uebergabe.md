Zuerst dieses Zip hochladen.

# Übergabe Werkstatt – Lieferung 2026-09-07f

## 1 Ziel
Der Masterprompt soll Blätter liefern, mit denen ein schwacher Schüler bis Klasse 10 eine Einheit lang allein arbeiten kann: Schwerpunkt jeder Hauptnummer unten (Übung der Fertigkeiten, Vorstufe, Grundfall), Prüfungsniveau nur als Zielmarke. Gleiche Qualität, weniger Korrekturrunden.

## 2 Arbeitsgrundlage
- `masterprompt.md` v3.32 – maßgeblich; Änderungen in 0, 1.1, 1.2, 1.4, 2.1, 2.2, 2.4, 3.1, 4.1, 4.2, 4.6, 5.1 b, 6.3, 6.4.
- `pruefungsprompt.md` v0.12 – nur 4.1 Muster (`\quad`) und 6.3 Versionszeile.
- `mathblatt.sty` 2026-09-07c – `\weit` 1,6 / 6 pt; `\leerfeld` 3 cm, `\feld` 2 cm, `\feldl` 3 cm; Felder brechen nicht mehr allein um. Gegen T1, T2 und Prozent-Heft vom 07.09. kompiliert, ohne Warnungen.
- `Anleitung_mathblatt.md` – zu 2026-09-07c; `teilezwei`-Regel, Feldbreiten, `\weit`.
- `Testauswertung_Masterprompt_Mathe_2026-09-07.md` – Prüfpunkte Übung/Hinrichtung, „erste sechs", Kasten, `\weit`, `teilezwei`, Feld-Umbruch; Testauftrag ohne „start", zwei Themen beim Masterprompt.
- `CHANGELOG.md` – Einträge v3.32, v0.12, Vorlage 07c.
- `blatt-konzept.md` lag nicht in Lieferung 07e und liegt auch hier nicht bei.

## 3 Arbeitsstand
Abgeschlossen: Auswertung der Archive Terme T1/T2 (v3.31) und Prozent Heft (v0.11), alle mit Fable 5.1. Befunde: Prüfskripte 0 Abweichungen, Zählungen stimmen, keine Log-Warnungen; Vorstufe, `\quad`-Regel und Symbolregel umgesetzt. P: Termwert ohne eigene Hauptnummer ohne Abweichungszeile; Erklärsatz vor dem Bau nach Off-Menu-Antwort „1 bis 4"; T2 Aufgabe 2 a) und c) derselbe Term. V (über drei Archive wiederholt): Feld allein in der nächsten Zeile → Vorlage 07c. A: `teilezwei` nie genutzt → Anleitung. Nicht beurteilbar: ob der Schnitt in zwei Teile reproduzierbar ist (früheres Terme-Protokoll fehlte). Testeingabe war „terme zusammenfassen" ohne „kl. 8" – Deutungszeile daher nicht vergleichbar.
Alle Prompt-Änderungen dieser Lieferung sind ungetestet.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen
- Rangfolge gedreht: Einstieg jeder Hauptnummer vor Typenvollständigkeit vor Rest der Kette. Reicht das Budget nicht, wandert ein Typ in den nächsten Teil, nie eine Einstiegssprosse. Budget 6/2/4 bleibt.
- Prüfungsniveau genau eine Teilaufgabe je Hauptnummer, markiert, am Ende; „Erhöht" macht sie anspruchsvoller, nicht zahlreicher. Begründung: Prüfungsniveau wird in einer Einheit nicht erreicht; die Aufgabe ist Vorrat für spätere Einheiten.
- Aufgabe 1 ist Übung, nicht Diagnose: je Fertigkeit zwei leichte, eine mittlere, je Fallstrick des Blatts eine; rückwärts vom Blatt geplant; höchstens zwölf; keine Fokus-Zeile. Prüfregel (Hinrichtung): jeder Fallstrick aus Aufgabe 1 kommt auf dem Blatt wieder.
- Vorstufe vier bis fünf, Grundfall in Teil 1 vier- bis fünfmal; Kriterium: die ersten sechs Teilaufgaben jeder Verfahrens-Hauptnummer ohne die Sprossen ab der Mitte lösbar.
- Teil 0 und „vorbereiten" gestrichen; Fertigkeiten liegen auf jedem Blatt in Aufgabe 1, mehr davon ist ein Fokus.
- Hilfe-Seite bis Kl. 10 nur auf „mit hilfe"; ab Kl. 11 und im Erarbeitungsmodus wie bisher. Gilt nur für den Masterprompt.
- Kasten (3.1): je Zeile eine Regel, Varianten derselben Regel zusammen, höchstens fünf Zeilen, nichts aus der Vorstufe.
- Antwort außerhalb der Buttons wird als Freitext gedeutet, Ergebnis in der Deutungszeile, kein Erklärsatz, kein Zusatzbutton. Ein Blatt je Antwort bleibt („weiter").
- `\weit` Standard bis Kl. 10 (Masterprompt 4.6); Prüfungsprompt setzt es ohnehin.
- „start" ist Produkt (Start-PDF für den Schüler), nicht Testeingabe; Messbasis Prüfungsprompt neu ab v0.12.
- Weiterhin: keine neuen Signalwörter; bis Kl. 10 keine Schulform-Filterung; 3.2 „kein Rechenplatz".

## 5 Offene Punkte und verworfene Ansätze
Offen:
- Hält „erste sechs allein lösbar" im Bau? Das Modell beurteilt „lösbar" selbst; erst das PDF zeigt es. Deshalb zwei Themen im Test.
- Prüfungsprompt: Hilfe-Seite bleibt dort an, weil 3.1 über sie auf die Formelsammlung verweist. Ob die Kl.-10-Regel dort gelten soll, nach dem Test entscheiden.
- Reproduzierbarkeit des Schnitts (Terme: früher ein Blatt, jetzt zwei Teile, mit v3.32 vermutlich drei). Frühere Protokolle desselben Themas in der Werkstatt sammeln.
- T2 Aufgabe 2 a) und c) derselbe Term (Vorstufe und Grundfall): gewollt oder Verstoß gegen 3.6 – nicht entschieden.
- Abweichungszeile im Ausgabeblock, wenn ein Typ keine eigene Hauptnummer bekommt (T1 Termwert): Prompt verlangt sie, das Modell hat sie nicht geschrieben; beim nächsten Lauf prüfen.
- Auslöser-Inventar aufschreiben und Ungenutztes streichen (aus 07e, weiter offen).
- `\kreuz`-Zeilen brechen bei vielen Kästchen um (T1 4 m, Klasse F); erst bei Wiederholung ein Vorlagen-Befund.
Verworfen:
- Button „alle": verspricht mehr als ein Tap liefert (baut trotzdem nur Teil 1) und ist ein Signalwort.
- Teil 0 als Warm-up-Blatt: zweiter Mechanismus für dasselbe Bedürfnis, nie gebaut.
- „So viele Übungsaufgaben wie nötig" ohne Form: nicht prüfbar, führte in T1 zu 13–14 Teilaufgaben je Hauptnummer.
- Zwei Sternaufgaben je Hauptnummer bei „Erhöht": Mengenhebel gegen das Ziel „Schwerpunkt unten".

## 6 Nächster Arbeitsschritt
Teste
* Masterprompt v3.32: „terme zusammenfassen kl. 8"
* Masterprompt v3.32: „lineare gleichungen kl. 8"
* Prüfungsprompt v0.12: „prozent"
Ergebnis-Zips mit dieser Lieferung in einen neuen Chat. Auswertung nach Testauswertung; Schwerpunkt: Aufgabe 1 als Übung mit Hinrichtung, Vorstufe vier bis fünf, erste sechs allein lösbar, Kasten fünf Zeilen, Hilfe-Seite aus, `\weit` gesetzt, Felder nicht allein umgebrochen, Teilzahl je Thema; Terme gegen die Archive vom 07.09. (T1: 2 Korrekturrunden von 4 Schritten, 238 s).
