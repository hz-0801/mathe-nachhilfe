Zuerst dieses Zip hochladen.

# Übergabe Werkstatt – Lieferung 2026-09-07e

## 1 Ziel
Der Masterprompt soll Blätter liefern, die schwache Schüler bis Klasse 10 bei der ersten Teilaufgabe nicht verlieren: Erkennungsschritte unter dem Verfahren werden zu Aufgaben, nicht nur zu Kastentext und Hilfe-Seite. Gleiche Qualität, weniger Korrekturrunden.

## 2 Arbeitsgrundlage
- `masterprompt.md` v3.31 – maßgeblich, Änderungen 2.2 b Vorstufe, 3.4, 3.6.
- `pruefungsprompt.md` v0.11 – nur 3.4 und 3.6 nachgezogen.
- `mathblatt.sty` 2026-09-07b – unverändert.
- `Anleitung_mathblatt.md` – Syntaxzeile `teilezwei`, `\erg`-Beispiel mit `\quad`.
- `Testauswertung_Masterprompt_Mathe_2026-09-07.md` – Prüfpunkte Vorstufe, Senkrechtstrich, Symbolregel ergänzt; doppelter Testauftrag-Absatz entfernt.
- `CHANGELOG.md` – Einträge v3.31, v0.11, Anleitung.
- `masterprompt_aenderungsvorschlaege_2026-09-07.md` (im Werkstatt-Chat hochgeladen, nicht im Repo) – Diskussionsgrundlage; Punkt 3 und 5 umgesetzt, Punkt 2 in der Vorstufe aufgegangen, Punkt 1 und 4 zurückgestellt.

## 3 Arbeitsstand
Abgeschlossen: Diagnose – alle früheren Anläufe (Anspruchsachse v3.7, 30/30/30/10, „jede Sprosse zweimal") drehten am Mengenhebel; das Problem ist, dass die Kette beim leichtesten Fall des Verfahrens beginnt statt bei der Fertigkeit darunter. Antwort: Vorstufe in 2.2 b, Standard bis Kl. 10, Auslöser ist ein Merkmal des Verfahrens, kein Eingabewort. Alle Änderungen additiv, ungetestet.
Läuft: Testbau mit v3.31.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen
- Vorstufe ist Standard für Lernblatt und Teile bis Kl. 10; nicht bei Fokus, kurz, Test; abschaltbar nur über Freitext („ohne vorstufe"), kein eigenes Auslöserwort.
- Keine neuen Signalwörter; jedes Bedürfnis wird zuerst als Verbesserung des Standards gelöst. Drei Achsen: was (Thema, Klasse), wie viel (Blatttyp), wie tief (Anspruch).
- Bis Kl. 10 keine Filterung nach Schulform (1.4 bleibt).
- Abschnitt 0 unverändert: übersprungen wird auf dem Blatt, nicht beim Bau. Unvollständige Blätter sind Fokus und Teil; kein neuer Mechanismus.
- Budget 6/2/4 bleibt; Änderung nur aus Messreihe (mehrere Läufe je Thema). Sprengt die Vorstufe das Budget, wird weiter geschnitten, nicht das Budget angehoben.
- 3.2 „Kein Rechenplatz" bleibt; Vorstufe bekommt `\leerfeld`. `\weit` als Standard für Kl. ≤ 10 erst nach dem Test entscheiden.
- Teillösungen im Begleitteil durch `\quad`, kein `|` (Annahme: Abstand ist das Gewünschte).

## 5 Offene Punkte und verworfene Ansätze
Offen:
- Findet das Modell den Erkennungsschritt bei anderen Themen (Brüche, Gleichungen) so sauber wie bei Termen? Erst nach dem Testbau, dann zweites Thema.
- Hilfe-Seite unter Kl. 11: Lehrer bezweifelt, dass sie genutzt wird. Nach dem Test prüfen, ob sie neben der Vorstufe noch trägt; ggf. nur auf „mit hilfe".
- Budgetdruck durch die Vorstufe → Vollständigkeitsfrage kommt aus dem Test zurück.
- Auslöser-Inventar (Zusätze „schnell", „mit hilfe", „mit tipps" …) beim nächsten ruhigen Umzug aufschreiben und Ungenutztes streichen.
- Aus den Vorschlägen: Pflichtelement Begründen in Fehler-finden mittragen („Erkläre, warum das falsch ist") – braucht Praxis.
Verworfen:
- Förderfassung als Anspruchslage mit Auslöserwörtern (Punkt 1, 4) – Mengenhebel, löst nicht, dass a) schon nicht klappt; Signalwörter wuchern.
- Schulform als Filter bis Kl. 10 – Streuung innerhalb der Schulform größer als zwischen; weiteres Signalwort.
- Weiches Budget („etwa sechs") – zerstört die Reproduzierbarkeit des Schnitts.
- Teilaufgaben-Obergrenze als zweites Budget – zwei Budgets widersprechen sich.
- Äpfel-und-Birnen-Bild – bricht bei 3a · 5a.

## 6 Nächster Arbeitsschritt
Testauftrag Masterprompt v3.31: Eingabe wortgleich „terme zusammenfassen kl. 8" (Annahme: Eingabe des Vergleichs-PDFs vom 07.09.; sonst dieselbe wie damals). Ein Bau. Auswertung gegen das PDF `TermeZusammenfassen_Lern.pdf`: Aufgabe 2 und 3 beginnen mit Erkennungsschritt und Antwortfeld; kein T ohne Erklärung, keine doppelt belegten Labels; Ergebnisse ohne Strich; Seitenzahl gegen 4; Korrekturrunden gegen den vorigen Lauf. Prüfungsprompt v0.11: Prozentrechnung „start" wie bisher, nur 3.4/3.6 sichtbar.
