# CHANGELOG – Prompts und Vorlage

Repo hz-0801/mathe-nachhilfe (bis 2026-09-07 pruefungskatalog; Vorlage und Anleitung bis dahin im Repo nachhilfe-arbeitsblatt-vorlage). Masterfassungen: `masterprompt.md` (Themen ohne Katalog) und `pruefungsprompt.md` (Prüfungsprompt, Themen mit Katalog; bis v0.7 `blatt-prompt.md`). Die Projektanweisungen in den Claude-Projekten sind Kopien; Zeile 2 nennt die Version. Änderungen an den gemeinsamen Abschnitten 3–6 werden in beiden Prompts gemacht und hier je einmal genannt.

## masterprompt.md

- 2026-09-07 v3.29 (nach Auswertung LinFkt Teil 1 und 2 mit v3.28, Sonnet): 4.3 Seitenfüllung mit Drittel-Maß, eine Hauptnummer allein ist kein Anlass, nichts kürzen (aus Prüfungsprompt); 5.2 a Maß aus der Textextraktion. 4.4 höchstens vier Graphen je System, Gefragtes in der Fläche. 5.1 a Skript vergleicht Zahlenwerte, null Abweichungen vor der Übergabe. 6.3 Zeile „Modell"; Zeiten gemessen mit t0/t1-Stempeln statt geschätzt. 4.6 PDF ohne Datum, Archiv `[Thema]_[Typ]_[Datum]_protokoll.zip`.
- 2026-09-07 v3.28: Basis-URL auf Repo mathe-nachhilfe (4.6). Reparatur gegen Vorlage 2026-09-06e: Kopfzeile über `\blattkopf`, Sternlegende als drittes Argument von `\blattkopf*` in der Fußzeile, `\sternlegende` und `\blattfuss` entfallen; Anleitungsabschnitt „Noch nicht in Stufe 3". 1.4: Kl.-10-Satz korrigiert (P10 im Niveau FOR, seit 2026 getrennte Hefte EBR/FOR, am Gymnasium seit 2025/26 keine P10); FHR-Fakten gegen die Prüfungsschwerpunkte 2026/27 geprüft und ergänzt (Hilfsmittel ohne CAS, alle Aufgaben Pflicht, Erwartungshorizont in den Lehrerheften). Prüfungsstufe bleibt bei „grundlegend" (1.4, 2.2 c). Kette rückwärts von der Prüfungsstufe, Aufwandsmerkmale nach den Strukturmerkmalen (2.2 b). Hilfe-Seite ohne Ergebnisse und Zwischenwerte aus Teilaufgaben, nie gekürzt (4.2), dazu Prüfschritt 5.1 d. Skriptausgabe mit Sollwerten (5.1 a); Gefragtes in der Fläche, Achsenbereich statt Grafik verkleinern (5.1 c). Protokoll-Archiv mit `.sty` und Anleitung wie verwendet, `pruef_out.txt`, Zählung aus dem Kompilat, Zeilen „Prompt", „Vorlage", „Korrekturrunden" (6.3). Historie aus dem Kopf hierher.
- 2026-09-05 v3.27: Budget mit Zähldefinition; Umgruppieren nur nach 4.3; Achtung-Hinweise nach Aufgabenart; Protokoll-Archiv als zweite Datei.

## pruefungsprompt.md (Prüfungsprompt; bis v0.7 blatt-prompt.md)

- 2026-09-07 v0.9 (nach Auswertung Prozent 6 („start") mit v0.8, Sonnet): 2.1/2.2 b Grundfall-Originale gleicher Merkmale sind eine Sternsprosse. 5.1 a Skript vergleicht Zahlenwerte, null Abweichungen vor der Übergabe. 6.3 Zeile „Modell"; Zeiten gemessen mit t0/t1-Stempeln statt geschätzt.
- 2026-09-07 v0.8: Basis-URL auf Repo mathe-nachhilfe (2.1, 4.6). Umbenannt in Prüfungsprompt (Profil msa), Datei `pruefungsprompt.md`; Regel „Änderungen zuerst im Masterprompt" aufgehoben, 3–6 werden in beiden Prompts gepflegt (blatt-konzept §5). 4.6: Anleitungsabschnitt „Noch nicht in Stufe 3", fehlende Bausteine auch ins Protokoll. 6.3: Protokoll-Archiv mit `mathblatt.sty` und Anleitung wie verwendet, Zeilen „Prompt", „Vorlage", „Korrekturrunden", geplante Zahlen neben der Zählung. Historie aus dem Kopf hierher. Bauregeln unverändert.
- 2026-09-06 v0.7: nach Auswertung Prozent 5 („start") und Lineare Funktionen 3 mit v0.6: gefragte Punkte in der Fläche als Prüfpunkt, Hilfe-Seite ohne Ergebniswerte als Prüfpunkt, Zählung nach Hauptnummern präzisiert, Überschrift „Voraussetzungen.".
- 2026-09-06 v0.6: nach Auswertung Prozent 4 („start") und Lineare Funktionen 2 mit v0.5: ein PDF statt zwei, Grundfall-Originale keine Zusatzsprosse, Hilfe-Seite ungekürzt, höchstens vier Graphen je System, Gefragtes sichtbar in der Fläche, Zählung aus dem Kompilat.
- 2026-09-06 v0.5: nach Auswertung Themenheft Prozent 3 („start") und Lineare Funktionen 1: Stern = Prüfungsaufgabe, Hilfe ohne Ergebnisse, Dateirollen, Skriptausgabe mit Soll, Umbruch und Seitenfüllung.
- 2026-09-06 v0.4: nach Auswertung Themenheft 2 und Probeprüfung 2025: Originale gleicher Merkmale eine Sprosse, Rundung nach glatten Fällen, „original" mit Jahr, Vorablauf auf „start", Prüfskript-Ausgabe im Archiv, `\weit`, Sternlegende neu.
- 2026-09-06 v0.3: Kopfzeile, zwei PDFs.
- 2026-09-06 v0.2: Herkunft nur im Protokoll.
- 2026-09-06 v0.1: angelegt; Abschnitte 0–2 eigen, 3–6 aus Masterprompt v3.27 mit den Abweichungen aus blatt-konzept §5.

## mathblatt.sty und Anleitung_mathblatt.md

Die Versionszeile steht in Zeile 2 der `.sty`; die Anleitung nennt in Zeile 2, zu welcher Vorlagenversion sie gehört. Ältere Einträge stehen im Kopf der `.sty`.

- 2026-09-07a (nach Auswertung LinFkt Teil 1 und Prozent 6): `\gerade` – das Label bleibt in der Zeichenfläche (Kante nach Austrittsseite, sonst Suche wie bei `\funktion`); vorher konnte der Ausweichpunkt außerhalb liegen und wurde stumm weggeclippt. Anleitung: Kasten ohne `\sternlegende`; `\janein` ohne Argument, sonst `\kreuz`; Prozentzeichen im Text als `\%`; Einheit im Mathemodus mit `\,`; alle Grafiken im eigenen Absatz; Hinweis zum Geradenlabel. Geprüft gegen die .tex von LinFkt T1/T2 und Prozent 6: gleiche Seitenzahlen, keine Warnungen.
- 2026-09-07: in dieses Repo übernommen, unverändert (2026-09-06e, Anleitung Stufe 3).
- 2026-09-06e: `\wertetabelle` – leere Einträge in der Werteliste ergeben leere Felder.
- 2026-09-06d: `\blattkopf*` – Legendentext als drittes Argument, kein Text mehr in der Vorlage.
- 2026-09-06c: neu `\blattkopf` mit Sternlegende, `\weit`/`\eng`, `\kreissektor`, `\leerfeld`; Reparaturen kreisdiagramm-Überlauf, schritte-Zähler, geruest-Umbruch.

## archiv/

Fassungen von vor der Ablage im Repo: `masterprompt-v3.27.md` (05.09.2026), `blatt-prompt-v0.7.md` (06.09.2026). Ab v3.28/v0.8 hält die Git-Historie jede Fassung.
