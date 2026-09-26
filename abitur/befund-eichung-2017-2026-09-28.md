# Befund: Eichung Pool 2017 – erste Schätzung, Korrektur, amtlicher Bereich

Stand 28.09.2026 (Auftrag Nacht 2026-09-28, Teil 6; Posten „Eichung Pool 2017 grundlegend prüfen“ in faellig.md § 2). Kein Urteil – das fällt im Chat. Quelle jeder Zeile ist das Feld `bemerkung` der Poolzeile in iqb-katalog.csv („Erste Schätzung …; bei der Prüfung gegen die enge Fassung auf … gesetzt“ bzw. „Schätzung …; der amtliche Bereich ist …“); Regeln nach iqb.md § 7 (enge Fassung, Prinzip, Deutungsliste (a)–(e), Nullfall-Regel). „Treffer“ heißt: Schätzung gleich dem höchsten amtlichen Bereich (Spalte AB bzw. Standardbezug), wie `eichung()` in iqb-bau.py.

Abkürzungen der Regeln:
- **Verkettung → II**: „Reine Verkettungen von Standardschritten bleiben II“ (Grundregel der engen Fassung).
- **Einzeln → I**: „I bleibt die einzelne Beobachtung oder Rechnung, auch wenn sie begründet wird“.
- **(a), (b), (d), (e)**: Einträge der Deutungsliste; „Ausnahme“ = der Nachsatz „nicht, wenn …“ des Eintrags.
- **Prinzip**: „Eine Deutung zählt nur, wenn sie zu finden ist“.

## 2017-ga-B (WTR) – 39 Zeilen, erster Lauf 23 (59 %), heute 34 (87 %)

Sechzehn Abweichungen im ersten Lauf; elf korrigiert, fünf stehen.

| id | erste Schätzung | amtlich (höchster) | jetzt | Grund aus bemerkung | Regel, die griff |
|---|---|---|---|---|---|
| 2017MgrundlegendBAnalysisWTR-1c | II | II\|III (III) | III | Gleichung erst in eine geometrische Bedingung (waagerechte Sehne der Länge 3) übersetzen, dann am Graphen lösen | (a) und (d) |
| 2017MgrundlegendBAnalysisWTR-1e | II | I (I) | I | Extrempunkt über die gegebene faktorisierte Ableitung ist ein einzelnes Standardverfahren; „wie alle Poolzeilen des Typs, I“ | Einzeln → I |
| 2017MgrundlegendBAnalysisWTR-1f | II | I (I) | I | zwei voneinander unabhängige einzelne Rechnungen (Streckenlänge, Steigung) | Einzeln → I |
| 2017MgrundlegendBAnalysisWTR-1g | II | II\|III (III) | III | Sachbedingung (Brücke mit 6 %, Ende auf der Uferzone) erst in eine Gleichung übersetzen | (a) |
| 2017MgrundlegendBAnalysisWTR-2c | II | II\|III (III) | III | Term über zwei verkettete Deutungen (g′ Monotonie, g″ Krümmung) in Aussagen übersetzen | (d) sinngemäß |
| 2017MgrundlegendBAGLAA2WTR1-1e | I | I\|II (II) | II | Normalenvektor wählen und Winkelformel anwenden; „alle Zeilen des Typs im Bestand II“ | Verkettung → II |
| 2017MgrundlegendBAGLAA2WTR2-1d | I | II (II) | II | Parameterform aufstellen und in Koordinatenform überführen; „alle Zeilen des Typs im Bestand II“ | Verkettung → II |
| 2017MgrundlegendBStochastikWTR1-1b | II | I (I) | I | eine einzelne Laplace-Rechnung, B nur Gegenereignis | Einzeln → I |
| 2017MgrundlegendBStochastikWTR1-2c | II | I (I) | I | Vergleich der Nachbarwerte ist das Standardverfahren des Typs; „die Poolzeile des Typs I“ | Einzeln → I |
| 2017MgrundlegendBStochastikWTR1-2d | III | I\|II (II) | II | einfache Deutung einer Binomialsumme; „die Zeilen des Typs im Bestand überwiegend II“ | (d), Ausnahme |
| 2017MgrundlegendBStochastikWTR2-1b | III | I\|II (II) | II | kein Eintrag der Deutungsliste; Urnenmodell mit Pfadprodukt | Verkettung → II |
| 2017MgrundlegendBAnalysisWTR-1d | I | II (II) | I | nicht korrigiert: eine Anwendung der Produktregel (wie 2024-ga-B Analysis WTR 1 1 a, dort amtlich I) | – |
| 2017MgrundlegendBStochastikWTR1-2a | I | I\|II (II) | I | nicht korrigiert: eine Summe von vier Pfadprodukten wie die Poolzeilen des Typs (alle I) | – |
| 2017MgrundlegendBStochastikWTR1-2e | II | II\|III (III) | II | nicht korrigiert: Verkettung von Standardschritten, kein Listeneintrag; erster amtlicher Bereich für den Typ | – |
| 2017MgrundlegendBStochastikWTR2-1c | II | II\|III (III) | II | nicht korrigiert: Verkettung von Standardschritten, kein Listeneintrag | – |
| 2017MgrundlegendBStochastikWTR2-2a | I | II (II) | I | nicht korrigiert: eine Gleichung aus der σ-Formel nach n auflösen | – |

Richtung der elf Korrekturen: fünf nach oben (II → III dreimal, I → II zweimal), sechs nach unten (II → I viermal, III → II zweimal); alle elf treffen danach. Die fünf stehenden Abweichungen liegen alle unter dem amtlichen Bereich. Fünf der elf Korrekturen nennen als Stütze die amtlichen Bereiche anderer Zeilen desselben Typs im Bestand (1e, AG/LA WTR 1 1e, WTR 2 1d, Stochastik WTR 1 2c, 2d).

## 2017-ga-A – 20 Zeilen, erster Lauf 15 (75 %), heute 17 (85 %)

Fünf Abweichungen im ersten Lauf; zwei korrigiert, drei stehen. (Der Auftrag nennt „drei Abweichungen, zwei korrigiert“: das sind die drei heute stehenden und die zwei korrigierten.)

| id | erste Schätzung | amtlich (höchster) | jetzt | Grund aus bemerkung | Regel, die griff |
|---|---|---|---|---|---|
| 2017MgrundlegendAAGLAA211-a | I | I\|II (II) | II | Nachweis der Nichtkollinearität und Ebenengleichung aus denselben Spannvektoren | Verkettung → II |
| 2017MgrundlegendAStochastik12-b | I | I\|II (II) | II | gerade Zahlen je Würfel abzählen und Pfadregeln über zwei Zweige | Verkettung → II |
| 2017MgrundlegendAAnalysis2-b | II | II\|III (III) | II | nicht korrigiert: Routineverkettung Stammfunktion und lineare Gleichung, kein Listeneintrag | – |
| 2017MgrundlegendAAGLAA11-a | I | I\|II (II) | I | nicht korrigiert: je Term eine einzelne begründete Beobachtung | – |
| 2017MgrundlegendAStochastik11-a | I | I\|II (II) | I | nicht korrigiert: einzelne Ablesung mit Summe | – |

Beide Korrekturen nach oben; die drei stehenden Abweichungen liegen unter dem amtlichen Bereich.

## Zum Vergleich: 2017-ea-B (WTR) – 82 Zeilen, erster Lauf 57 (70 %), heute 71 (87 %)

Im selben Auftrag erfasst (Teil 2, Punkt 1; iqb-pruefungen.md § 4). 25 Abweichungen im ersten Lauf; vierzehn korrigiert, elf stehen.

| id | erste Schätzung | amtlich (höchster) | jetzt | Grund aus bemerkung | Regel, die griff |
|---|---|---|---|---|---|
| 2017MerhoehtBAnalysisWTR1-1b | II | I | I | Tangente anlegen und Steigung ablesen ist ein einzelnes Standardverfahren | Einzeln → I |
| 2017MerhoehtBAnalysisWTR1-3a | II | I | I | Amplitude und Periode stehen im Term, jede Skizze ein einzelnes Verfahren | Einzeln → I |
| 2017MerhoehtBAnalysisWTR2-1b | II | I | I | Nullstellen durch Ausklammern und Faktorisieren | Einzeln → I |
| 2017MerhoehtBAnalysisWTR2-1i | III | II | II | der Tiefpunkt ist vorgegeben, (e) greift nicht | Prinzip |
| 2017MerhoehtBAnalysisWTR2-2a | II | I | I | eine einzelne Deutung zweier Funktionswerte | Einzeln → I |
| 2017MerhoehtBAnalysisWTR2-2e | II | II\|III (III) | III | Vollkörper minus Hohlraum erst erkennen und in zwei Integrale übersetzen; bei WTR 3 2 d angewandt, hier nicht | (a) |
| 2017MerhoehtBAnalysisWTR3-1b | II | I | I | zwei unabhängige Einzelbeobachtungen | Einzeln → I |
| 2017MerhoehtBAnalysisWTR3-1f | III | II | II | die Höhe des Hochpunkts ist in c gezeigt | (b), Ausnahme |
| 2017MerhoehtBAnalysisWTR3-2b | II | I | I | Eigenschaften über eine Beobachtung übertragen | Einzeln → I |
| 2017MerhoehtBAnalysisWTR3-2c | II | I | I | ein Funktionswert mit Umrechnung und Addition | Einzeln → I |
| 2017MerhoehtBAGLAA2WTR3-1e | II | III | III | mehrere verkettete Deutungen je Ansatz | (d) |
| 2017MerhoehtBAGLAA2WTR3-1g | III | II | II | Richtung des Weiterflugs wörtlich vorgegeben | (a), Ausnahme |
| 2017MerhoehtBStochastikWTR-1c | II | I | I | zwei unabhängige Rechnerwerte | Einzeln → I |
| 2017MerhoehtBStochastikWTR-1d | II | III | III | zwei Binomialsummen deuten und Gegenereignis bilden | (d) |

Stehende Abweichungen (nicht korrigiert, „keine Regel als falsch angewandt erkannt“): über dem amtlichen Bereich sechs – Analysis WTR 1 1c (III gegen II, (a)), WTR 3 1a (III gegen II, Nullfall-Regel mit zwei ausgeführten Fällen), AG/LA (A2) WTR 1 1b, WTR 2 1b, WTR 3 1d (je II gegen I, Verkettung), WTR 2 1f (III gegen II, (a)); unter dem amtlichen Bereich fünf – Analysis WTR 1 2c, WTR 3 2h, AG/LA (A1) 2b, AG/LA (A2) WTR 3 1f (je II gegen III), Analysis WTR 2 1d (I gegen II). Richtung der vierzehn Korrekturen: elf nach unten (II → I achtmal, III → II dreimal), drei nach oben (II → III). Der Hilfsagent, der den Stapel erfasst hat, nennt drei Korrekturen grenzwertig (WTR 1 3a, WTR 2 2a, WTR 3 2c); ohne die vierzehnte (AG/LA WTR 3 1e) hätte der Lauf 70 von 82 erreicht, die Schwelle also auch gehalten.

## Zum Vergleich: 2017-ea-B (CAS) – 55 Zeilen, erster Lauf 34 (62 %), heute 47 (85 %)

Delta-Stapel, im selben Auftrag erfasst (Teil 2, Punkt 2; Einzelheiten in iqb-pruefungen.md § 4). Im ersten Lauf trafen die eigenen blinden Schätzungen 28 von 48 (58 %), die aus WTR-Zeilen übernommenen 6 von 7. 21 Abweichungen; dreizehn korrigiert (zwölf eigene: fünf nach oben – (c), (a), Verkettung → II dreimal –, sieben nach unten – Einzeln → I zweimal, Ausnahme zu (a) zweimal, Ausnahme zu (b) einmal, (b) greift nicht (Punkte genannt) einmal, kein Listeneintrag einmal; dazu eine übernommene Schätzung nach dem Vorrang des Amtlichen), acht stehen. Die Schwelle hält mit 47 von 55 genau.

## Zum Vergleich: 2018-ea-B (CAS) – nicht erfasst, erster Stand 57 von 85 (67 %), nach Prüfung 67 (79 %)

Im selben Auftrag versucht (Teil 2, Punkt 3; iqb-pruefungen.md § 4, Arbeitsstand unter abitur/arbeitsstand/2018-ea-B-cas/): alle 85 Schätzungen blind, eigene 55 von 82, übernommene 2 von 3. Nach Prüfung der 28 Abweichungen zehn Korrekturen (fünf nach oben, fünf nach unten), dann 67 von 85 – unter der Schwelle; die Schwelle wurde nicht geändert, der Stapel nicht erfasst. Die zwei Kandidaten für die Deutungsliste aus diesem Stapel („Mindestumfang durch Probieren = III“; „vom Text verlangte Fallunterscheidung ist amtlich II“) hätten 71 von 85 ergeben.

## Eichung je Pooljahr über den Bestand

Gerechnet mit `eichung()` aus iqb-bau.py über iqb-katalog.csv am Stand b90e574 (nach Teil 2 dieses Auftrags); Summe über den Bestand wie in der Selbstprüfung von iqb-bau.py: 1526 von 1638 gewerteten Zeilen (93 %), eine Zeile ohne Standardbezug. „Erster Lauf“ nur, wo iqb-pruefungen.md (§ 2, § 4, § 5) ihn nennt; alle übrigen Stapel nennen nur den Wert nach dem Stapellauf.

| Jahr | Niveau | Zeilen | Eichung erster Lauf (Stapel, laut Änderungslog und Befunden) | Eichung heute |
|---|---|---|---|---|
| 2017 | erhöht | 160 | 2017-ea-B WTR 57 von 82 (70 %); 2017-ea-B CAS 34 von 55 (62 %); 2017-ea-A nicht genannt (Stapellauf 22 von 23) – zusammen für B 91 von 137 (66 %) | 140 von 160 (87 %) |
| 2017 | grundlegend | 59 | 2017-ga-A 15 von 20 (75 %); 2017-ga-B WTR 23 von 39 (59 %) – zusammen 38 von 59 (64 %) | 51 von 59 (86 %) |
| 2018 | erhöht | 95 | nicht genannt (Stapelläufe 2018-ea-A 25 von 26, 2018-ea-B WTR 59 von 69); 2018-ea-B CAS nicht erfasst, erster Stand 57 von 85 (67 %) | 84 von 95 (88 %) |
| 2018 | grundlegend | 78 | 2018-ga-B WTR 44 von 53 (83 %); 2018-ga-A nicht genannt | 69 von 78 (88 %) |
| 2019 | erhöht | 20 | nicht genannt | 20 von 20 (100 %) |
| 2019 | grundlegend | 89 | nicht genannt | 81 von 88 gewerteten (92 %) |
| 2020 | erhöht | 28 | nicht genannt | 28 von 28 (100 %) |
| 2020 | grundlegend | 66 | nicht genannt | 65 von 66 (98 %) |
| 2021 | erhöht | 33 | nicht genannt | 33 von 33 (100 %) |
| 2021 | grundlegend | 70 | nicht genannt | 68 von 70 (97 %) |
| 2022 | erhöht | 101 | nicht genannt | 92 von 101 (91 %) |
| 2022 | grundlegend | 76 | 2022-ga-B WTR 35 von 52 (67 %; im Stapellauf nach sechs Korrekturen 41, seit Abgleichlauf 20 mit übernommenen Schätzungen auf dem amtlichen Bereich 50) | 73 von 76 (96 %) |
| 2023 | erhöht | 96 | nicht genannt | 84 von 96 (87 %) |
| 2023 | grundlegend | 85 | nicht genannt | 80 von 85 (94 %) |
| 2024 | erhöht | 93 | nicht genannt | 91 von 93 (97 %) |
| 2024 | grundlegend | 79 | nicht genannt | 72 von 79 (91 %) |
| 2025 | erhöht | 106 | nicht genannt | 101 von 106 (95 %) |
| 2025 | grundlegend | 73 | nicht genannt (2025-ga-A: weit 29, eng 30 von 31) | 71 von 73 (97 %), enge Fassung 72 |
| 2026 | erhöht | 129 | nicht genannt (2026-ea-A: 34 von 37, eng 36) | 125 von 129 (96 %) |
| 2026 | grundlegend | 103 | nicht genannt | 98 von 103 (95 %) |

Die Stapel ab 2019-ga-B (Teil B, Reserve) tragen in § 2 den Vermerk „Schätzung mit Standardbezug in Sicht, keine unabhängige Kennzahl“ (2019-ga-B, 2020-ga-B, 2021-ga-B, 2025-ea-B MMS); auch dort ist ein erster Lauf nicht genannt.
