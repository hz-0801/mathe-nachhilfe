# Rohdatei vierfeldertafel

Stufe: II

- abi: Vierfeldertafel (8 Zeilen)
- iqb: Vierfeldertafel (21 Zeilen)

Stand: 2026-09-19, Commit 16e5c1f

## A Typenprofil

**Vierfeldertafel aus Anteilen vervollständigen** · 19 Zeilen · abi 6 iqb 13 · Jahre 2017–2026
abitur/abitur-typen.csv (neu): Aus zwei Randanteilen und einem Schnittanteil – oder einem Randanteil und einem bedingten Anteil, aus dem der Schnittanteil folgt – alle Felder einer Vierfeldertafel ergänzen.

**Aussage über ein Entweder-oder-Ereignis aus der Vierfeldertafel beurteilen** · 2 Zeilen · iqb 2 · Jahre 2025
abitur/abitur-typen.csv (neu): Ein ausschließendes Oder als Summe zweier Felder der Vierfeldertafel berechnen und eine Aussage darüber beurteilen.

**Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen** · 2 Zeilen · abi 1 iqb 1 · Jahre 2019
abitur/abitur-typen.csv (neu): Aus Gesamtzahl, Randsummen und einem Feld einer Vierfeldertafel mit absoluten Häufigkeiten ein fehlendes Feld durch Subtraktion berechnen.

**Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen** · 2 Zeilen · abi 1 iqb 1 · Jahre 2023
abitur/abitur-typen.csv (neu): P(A ∪ B) aus der Vierfeldertafel als 1 − P(¬A ∩ ¬B) berechnen.

**Anteil aus Anteilen und bedingten Anteilen über die Vierfeldertafel berechnen** · 1 Zeile · iqb 1 · Jahre 2020
abitur/abitur-typen.csv (neu): Einen Anteil an der Gesamtheit aus gegebenen absoluten und bedingten Anteilen berechnen (Vierfeldertafel oder Baum).

**Tabelle mit drei Spalten analog zur Vierfeldertafel aus Anteilen vervollständigen** · 1 Zeile · iqb 1 · Jahre 2022
abitur/abitur-typen.csv (neu): Eine Tafel mit zwei Zeilen und drei Spalten aus Rand-, Schnitt- und bedingten Anteilen vollständig ausfüllen.

**Vierfeldertafel mit Parameter vervollständigen und einen Parameterwert ausschließen** · 1 Zeile · iqb 1 · Jahre 2021
abitur/abitur-typen.csv (neu): Eine Vierfeldertafel mit Einträgen in einem Parameter vervollständigen und einen Parameterwert über eine negative Wahrscheinlichkeit ausschließen.

**Vierfeldertafel mit absoluten Häufigkeiten aus Gruppengrößen und bedingten Anteilen vervollständigen** · 1 Zeile · iqb 1 · Jahre 2019
abitur/abitur-typen.csv (neu): Aus den Größen zweier Gruppen und je einem bedingten Anteil die Vierfeldertafel mit absoluten Häufigkeiten und Randsummen ausfüllen.

**Nebentypen:** Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen (1)

## B Zeilenliste

## abi

2019-be-gk-B4.1c | 2 | ja | Rechnung · Bestimmen Sie | Fahrprüfungen einer Region: 13 879 Prüflinge, davon 2 482 mindestens 30 Jahre alt; 11 104 haben bestanden, davon 8 870 jünger als 30; Ereignisse A: mindestens 30 Jahre alt, B: Prüfung bestanden → Anzahl der Prüflinge, die jünger als 30 waren und nicht bestanden haben | Gesamtzahl minus mindestens 30-Jährige minus jüngere Bestandene
2017-bb-ea-B4.1a | 2 | ja | Rechnung · Ermitteln Sie | Zu einer Autogrammstunde haben 30 Frauen und 50 Männer je eine Frage eingereicht. 75 Prozent aller eingereichten Fragen beziehen sich auf den Fußball, die übrigen sind eher allgemeiner Natur. Die Fragen der Frauen verteilen sich zu gleichen Teilen auf rein fußballerische und allgemeine. → Anzahl der von Männern gestellten Fragen, die eher allgemeine Dinge betreffen | Insgesamt sind es 80 Fragen, davon 25 % allgemeine, also 20. Von den Frauen stammen 15 allgemeine Fragen; die Differenz entfällt auf die Männer.
2018-bb-ea-B4.2a | 5 | ja | Tabelle¦Rechnung · Stellen Sie dar¦Berechnen Sie | In einer großen Gemeinde tragen 62,5 % der Bevölkerung eine Brille. Bei den Frauen beträgt der Anteil 64,8 %. Bekannt ist außerdem, dass 52,1 % der Bevölkerung Frauen sind. Eine aus der Bevölkerung zufällig ausgewählte Person ist ein Mann. → Darstellung des Sachverhalts in einer Vierfeldertafel¦Wahrscheinlichkeit dafür, dass dieser Mann eine Brille trägt | Die Randwerte 0,625 für Brille und 0,521 für Frauen eintragen. Die 64,8 % sind ein Anteil innerhalb der Frauen, also eine bedingte Wahrscheinlichkeit; daraus folgt das Feld Frau und Brille als 0,521 · 0,648. Die übrigen Felder über die Randsummen ergänzen. Die gesuchte Wahrscheinlichkeit ist das Feld Mann und Brille geteilt durch den Randwert der Männer.
2018-be-gk-B3.2e | 3 | ja | Tabelle · Stellen Sie dar | Für einen zufällig ausgewählten Bildschirm gilt: das Display ist mit der Wahrscheinlichkeit 10,7 Prozent defekt, das Netzteil mit 3,0 Prozent, und mit 87,3 Prozent ist weder das Display noch das Netzteil defekt. → vollständig ausgefüllte Vierfeldertafel | Aus dem Rand für das Display folgt der Gegenwert 89,3 Prozent; das Feld Display heil und Netzteil defekt ergibt sich als 89,3 − 87,3 = 2,0 Prozent. Damit ist das Feld Display defekt und Netzteil defekt 3,0 − 2,0 = 1,0 Prozent und das Feld Display defekt und Netzteil heil 10,7 − 1,0 = 9,7 Prozent.
2022-bebb-gk-B4h | 3 | ja | Tabelle · Stellen Sie dar | P(S) = 5 %, P(Z) = 10 %, P_Z(S) = 8 % → vollständige Vierfeldertafel | S∩Z = 0,008, Rest aus den Rändern
2023-bebb-gk-B4.1a | 3 | ja | Tabelle · Stellen Sie dar | Von den Lehrkräften eines Landes arbeiten 25 % an einem Gymnasium; 15 % der Lehrkräfte sind weiblich und arbeiten an einem Gymnasium; insgesamt sind 72 % der Lehrkräfte weiblich. → vollständig ausgefüllte Vierfeldertafel | Fehlende Felder als Differenzen der Ränder.
2024-bebb-gk-B4.1b | 3 | ja | Tabelle · Stellen Sie dar | 60 % Treuekunden, 20 % Morgenkunden, P(¬T ∩ M) = 0,05 → vollständige Vierfeldertafel | Differenzen der Ränder
2023-bebb-gk-B4.1b | 2 | ja | Rechnung · Ermitteln Sie | Von den Lehrkräften eines Landes arbeiten 25 % an einem Gymnasium; 15 % der Lehrkräfte sind weiblich und arbeiten an einem Gymnasium; insgesamt sind 72 % der Lehrkräfte weiblich. Vierfeldertafel aus a. → Wahrscheinlichkeit, dass eine zufällig ausgewählte Lehrkraft weiblich ist oder an einem Gymnasium arbeitet | Eins minus Feld ¬W∩¬G, alternativ 72 % + 25 % − 15 %.
## iqb

2020MgrundlegendAStochastik12-a | 3 | nein | Rechnung · Bestimmen Sie | Anteil verkleideter Erwachsener unter allen Gästen 12 %, Anteil aller Erwachsenen 60 %; 75 % der Jugendlichen verkleidet → Anteil der nicht Verkleideten unter allen Gästen | 0,48 + 0,25 · 0,4
2025MerhoehtBStochastikWTR1-1b | 4 | ja | Begründung · Beurteilen Sie | Vierfeldertafel aus a; Aussage: P(G und nicht J) ist etwa halb so groß wie P(entweder G oder nicht J) → Beurteilung | beide Wahrscheinlichkeiten aus der Tafel, Verhältnis
2025MgrundlegendBStochastikWTR3-1b | 3 | ja | Begründung · Beurteilen Sie | Vierfeldertafel aus a; Aussage: P(entweder in Großstadt oder nicht jünger als 50) < 60 % → Beurteilung | die beiden passenden Felder addieren
2019MgrundlegendBStochastikWTR1-1c | 2 | ja | Rechnung · Bestimmen Sie | Fahrprüfungen einer Region: 13 879 Prüflinge, 2 482 davon mindestens 30 Jahre alt; 11 104 haben bestanden, davon 8 870 jünger als 30; A: Prüfling mindestens 30, B: Prüfung bestanden → Anzahl der Prüflinge unter 30, die nicht bestanden haben | Randsumme der Jüngeren minus Bestandene der Jüngeren
2022MerhoehtBStochastikWTR2-1a | 3 | ja | Tabelle · Stellen Sie dar | 20 % Tarif S, 25 % L; 47 % haben angerufen, darunter die Hälfte der M-Kunden; 11 % haben S und nicht angerufen → vollständige Tabelle | M-Anteil als Rest, dann Zeilen und Spalten ergänzen
2018MerhoehtBStochastikWTR2-1b | 4 | ja | Tabelle · Stellen Sie dar | Für einen zufällig ausgewählten Bildschirm: Display defekt 10,7 %, weder Display noch Netzteil defekt 87,3 %, entweder Display oder Netzteil defekt 11,7 % → vollständig ausgefüllte Vierfeldertafel | D∩N aus 100 − 87,3 − 11,7; Rest als Differenzen
2018MgrundlegendBStochastikWTR1-1a | 3 | ja | Tabelle · Stellen Sie dar | Jugendliche eines Landes: 49,20 % weiblich (W), 47,10 % erledigen Finanzangelegenheiten regelmäßig mit Smartphone oder Tablet (S), 19,68 % sind weiblich und tun das → vollständig ausgefüllte Vierfeldertafel | Differenzen der Ränder
2018MgrundlegendBStochastikWTR2-1e | 3 | ja | Tabelle · Stellen Sie dar | Für einen zufällig ausgewählten Bildschirm: Display defekt 10,7 %, weder Display noch Netzteil defekt 87,3 %, Netzteil defekt 3,0 % → vollständig ausgefüllte Vierfeldertafel | ¬D∩¬N = 87,3 %, Ränder 10,7/89,3 und 3,0/97,0, Rest als Differenzen
2021MgrundlegendBStochastikWTR3-1a | 3 | ja | Tabelle · Stellen Sie dar | Großes Unternehmen: 77 % aller Beschäftigten sind mit ihrem Gehalt zufrieden; 5 % aller Beschäftigten sind in der Werbeabteilung und nicht zufrieden; 12 % aller Beschäftigten gehören zur Werbeabteilung → vollständig ausgefüllte Vierfeldertafel | Randwerte eintragen, Felder durch Differenzen ergänzen
2022MgrundlegendBStochastikWTR1-1e | 3 | ja | Tabelle · Stellen Sie dar | P(S) = 5 %, P(Z) = 10 %, P_Z(S) = 8 % → vollständige Vierfeldertafel | S∩Z = 0,008, Rest aus den Rändern
2023MgrundlegendBStochastikWTR3-1a | 3 | ja | Tabelle · Stellen Sie dar | 25 % der Lehrkräfte am Gymnasium; 15 % weiblich und am Gymnasium; 72 % weiblich → vollständige Vierfeldertafel | Fehlende Felder als Differenzen
2024MerhoehtBStochastikWTR2-1a | 4 | ja | Tabelle · Stellen Sie dar | 60 % mit Pkw, 8 % mit Lastenrad, 14 % der Haushalte ohne Pkw mit Lastenrad → vollständige Vierfeldertafel | 0,4 · 0,14 als Schnitt, Rest über Differenzen
2024MgrundlegendBStochastikWTR1-1b | 3 | ja | Tabelle · Stellen Sie dar | 60 % Treuekunden, 20 % Morgenkunden, P(nicht T ∩ M) = 0,05 → vollständige Vierfeldertafel | Ränder eintragen, Felder als Differenzen
2024MgrundlegendBStochastikWTR2-1b | 4 | ja | Tabelle¦Kurzantwort · Stellen Sie dar¦Geben Sie an | P(L) = 0,56, P(D) = 0,33, P(nicht L ∩ nicht D) = 0,28 → vollständige Vierfeldertafel und P(Laptop, aber kein Desktop-PC) | Felder aus Rändern und 0,28, Feld ablesen
2025MerhoehtBStochastikWTR1-1a | 3 | ja | Tabelle · Stellen Sie dar | 72 % jünger als 50 Jahre; 18 % jünger als 50 und nicht in einer Großstadt; 75 % in einer Großstadt → vollständige Vierfeldertafel | Ränder eintragen, Felder als Differenzen
2025MgrundlegendBStochastikWTR3-1a | 3 | ja | Tabelle · Stellen Sie dar | 72 % jünger als 50 Jahre; 18 % jünger als 50 und nicht in einer Großstadt; 75 % in einer Großstadt → vollständige Vierfeldertafel | Ränder eintragen, Felder als Differenzen
2026MerhoehtBStochastikWTR2-1b | 2 | ja | Tabelle · Vervollständigen Sie | A: mindestens fünf Jahre alt (70,8 %); B: Pkw (80 %); P(nicht A und nicht B) = 0,044 → alle Felder der Vierfeldertafel | Ränder eintragen, Felder als Differenzen
2026MgrundlegendBStochastikWTR2-1a | 2 | ja | Tabelle · Ergänzen Sie | 32 % Hip-Hop-Songs (H), 40 % mindestens 4 Minuten lang (L), P(H und L) = 0,14 → fehlende Wahrscheinlichkeiten der Vierfeldertafel | Ränder eintragen, Innenfelder als Differenzen
2021MerhoehtAStochastik11-a | 3 | nein | Tabelle¦Begründung · Vervollständigen Sie¦Zeigen Sie | Vierfeldertafel mit P(A∩B) = p, P(A) = 3p, P(Ā) = 1 − 3p, P(B) = 4p; p ≠ 0 → vollständige Tafel; Nachweis, dass p nicht 1/5 sein kann | fehlende Felder als Differenzen, Vorzeichen von 1 − 6p prüfen
2019MgrundlegendBStochastikWTR3-1a | 3 | ja | Tabelle · Stellen Sie dar | Befragung von 2 360 Männern und 2 200 Frauen (Glücksspielteilnahme): 2,5 % der Männer und 0,5 % der Frauen mit Anzeichen spielsüchtigen Verhaltens; M: Person ist ein Mann, S: Anzeichen spielsüchtigen Verhaltens → vollständig ausgefüllte Vierfeldertafel | Anzahlen je Feld berechnen, Randsummen bilden
2023MgrundlegendBStochastikWTR3-1b | 2 | ja | Rechnung · Ermitteln Sie | Vierfeldertafel aus a → Wahrscheinlichkeit, dass eine Lehrkraft weiblich ist oder am Gymnasium arbeitet | Eins minus Feld ¬W∩¬G
