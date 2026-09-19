# QUELLEN P10 – Mathematik Brandenburg, Oberschule/Gesamtschule

Version 0.1 · 18.09.2026 · gehört zum Profil msa
Angelegt in Auftrag O, Punkt 2, nach dem Muster von abi-quellen.md (ohne die
Teile, die es dort nur wegen der Verlagsbände gibt). Die Zahlen zum lokalen
Bestand (§ 5) sind aus befund-quellenbestand-2026-09-18.md § 4 übernommen und
nicht neu erhoben.

Diese Datei ersetzt eine Ablage der Prüfungshefte im Repo. Die Hefte werden bei
Bedarf über die hier genannten URLs mit curl geholt; lokal liegen sie unter
hefte/msa/ (nicht im Repo, § 5). Die Spalte `papier` liefert die Kürzel, die im
Katalog und in den ids verwendet werden (msa.md § 4).

## 1 Amtliche Quelle

Bildungsserver Berlin-Brandenburg, Jahresseite für alle veröffentlichten
Jahrgänge:
https://bildungsserver.berlin-brandenburg.de/unterricht/pruefungen/pruefungen-10/pruefungsaufgaben-mathematik

Verzeichnis der Dateien:
https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/pruefungen/pruefungen_am_ende_der_jahrgangsstufe_10/Pruefungsaufgaben_P10_Mathematik/

Veröffentlicht sind die Jahrgänge 2014–2026: je Jahrgang das Heft der
Oberschulen und Gesamtschulen (bis 2025 integriert EBR/FOR, ab 2026 getrennt)
und bis 2025 die Gymnasialhefte. Lösungen, Erwartungshorizonte und
Vorgabendokumente liegen nicht auf der Seite; die amtlichen Vorgaben
(Fachbriefe, Rundschreiben) stehen in msa-vorgaben.md § 1.

## 2 Bestand

Bestand des Profils sind die Oberschulhefte 2014–2026 und die Musteraufgaben
2028 (msa.md § 1, konzept.md Entscheidung 18). Status je Heft in
msa-pruefungen.md § 2.

| papier | Jahr | Serverdatei | PDF-S. | Katalog |
|---|---|---|---|---|
| OS | 2014 | 14_P10_Ma_Set2_A.pdf | 9 | erfasst |
| OS | 2015 | 15_P10_Ma_A.pdf | 9 | erfasst |
| OS | 2016 | 16_P10_Ma_A.pdf | 9 | erfasst |
| OS | 2017 | 17_P10_Ma_A.pdf | 15 | erfasst |
| OS | 2018 | 18_P10_Ma_A.pdf | 15 | erfasst |
| OS | 2019 | 19_P10_Ma_A.pdf | 15 | erfasst |
| OS | 2020 | 20_P10_Ma_A.pdf | 15 | erfasst |
| OS | 2021 | 21_P10_Ma_A.pdf | 15 | erfasst |
| OS | 2022 | 22_P10_Ma_EBR_FOR.pdf | 13 | erfasst |
| OS | 2023 | 23_P10_Ma_A.pdf | 12 | erfasst |
| OS | 2024 | 24_P10_Ma_A.pdf | 14 | erfasst |
| OS | 2025 | 25_P10_Ma_A.pdf | 15 | erfasst |
| EBR | 2026 | 26_P10_Ma_EBR_A.pdf | 10 | **ohne Katalogeintrag** (zurückgestellt, kein EBR-Schüler) |
| FOR | 2026 | 26_P10_Ma_FOR_A.pdf | 15 | erfasst |
| MUSTER-EBR, MUSTER-FOR | 2028 | Fachbrief Mathematik Nr. 10, S. 20–31 (msa-vorgaben.md § 1) | – | ohne Katalogeintrag (FOR nicht erfasst, EBR zurückgestellt) |

Vollständige URL = Verzeichnis aus § 1 + Serverdatei. Die Musteraufgaben 2028
liegen nicht auf der Jahresseite, sondern im Fachbrief 10; sie sind lokal nicht
gesichert (befund-quellenbestand-2026-09-18.md § 4).

## 3 Vorhanden, aber nicht im Bestand

Auf der Jahresseite liegen außerdem 19 Gymnasialhefte 2014–2025 (ab 2019 in zwei
Dateien je Jahrgang). Sie gehören nach konzept.md Entscheidung 18 nicht zum
Bestand (seit 2025/26 keine P10 am Gymnasium; ein Gymnasialschüler mit
zentraler Klassenarbeit wäre eine neue Prüfungsart, konzept.md § 8) und haben
keinen papier-Wert im Profil. Sie sind in Auftrag N nur gesichert worden (§ 5,
sonstiges/) und nicht erfasst.

## 4 Lösungen

Für die Hefte gibt es keine amtlichen Lösungen; alle Ergebnisse im Katalog sind
eigene Rechnung (Kern § 3 d in der Fassung „eigene Rechnung"). Die einzigen
amtlichen Lösungen sind der Erwartungshorizont der Musteraufgaben 2028 im
Fachbrief 10 (Bewertungseinheiten, Anforderungsbereich, Standardbezug; msa.md
§ 2 und § 7).

## 5 Lokaler Heftordner hefte/msa/

Stand 18.09.2026 (Auftrag N „Originale sichern und ordnen";
befund-quellenbestand-2026-09-18.md § 4: 33 Dateien, 39,7 MB, alle vom
Bildungsserver geholt, 0 nicht holbar). Der Ordner hefte/ liegt neben dem Repo,
per .gitignore ausgeschlossen, und ist je Profil unterteilt (abi-quellen.md
§ 8); hefte/msa/ hält die Aufgabenhefte dieses Profils, hefte/msa/sonstiges/
alles, was kein Heft des Bestands ist.

Dateiname in hefte/msa/ = <jahr>-<papier>.pdf in Kleinbuchstaben (2025-os.pdf,
2026-for.pdf); Seiten und Textebene mit pypdf ermittelt.

| Datei | papier | Jahrgang | Serverdatei | Seiten | Textebene | Größe | Erfassungsstand |
|---|---|---|---|---|---|---|---|
| 2014-os.pdf | OS | 2014 | 14_P10_Ma_Set2_A.pdf | 9 | ja | 0,5 MB | erfasst 2026-09-05, 30 Zeilen |
| 2015-os.pdf | OS | 2015 | 15_P10_Ma_A.pdf | 9 | ja | 0,9 MB | erfasst 2026-09-05, 31 Zeilen |
| 2016-os.pdf | OS | 2016 | 16_P10_Ma_A.pdf | 9 | ja | 0,9 MB | erfasst 2026-09-05, 34 Zeilen |
| 2017-os.pdf | OS | 2017 | 17_P10_Ma_A.pdf | 15 | ja | 1,4 MB | erfasst 2026-09-05, 31 Zeilen |
| 2018-os.pdf | OS | 2018 | 18_P10_Ma_A.pdf | 15 | ja | 2,8 MB | erfasst 2026-09-05, 32 Zeilen |
| 2019-os.pdf | OS | 2019 | 19_P10_Ma_A.pdf | 15 | ja | 1,4 MB | erfasst 2026-09-05, 29 Zeilen |
| 2020-os.pdf | OS | 2020 | 20_P10_Ma_A.pdf | 15 | ja | 1,3 MB | erfasst 2026-09-05, 32 Zeilen |
| 2021-os.pdf | OS | 2021 | 21_P10_Ma_A.pdf | 15 | ja | 1,3 MB | erfasst 2026-09-05, 28 Zeilen |
| 2022-os.pdf | OS | 2022 | 22_P10_Ma_EBR_FOR.pdf | 13 | ja | 1,2 MB | erfasst 2026-09-05, 30 Zeilen |
| 2023-os.pdf | OS | 2023 | 23_P10_Ma_A.pdf | 12 | ja | 1,3 MB | erfasst 2026-09-05, 27 Zeilen |
| 2024-os.pdf | OS | 2024 | 24_P10_Ma_A.pdf | 14 | ja | 1,5 MB | erfasst 2026-09-05, 29 Zeilen |
| 2025-os.pdf | OS | 2025 | 25_P10_Ma_A.pdf | 15 | ja | 1,4 MB | erfasst 2026-09-05, 27 Zeilen |
| 2026-ebr.pdf | EBR | 2026 | 26_P10_Ma_EBR_A.pdf | 10 | ja | 1,3 MB | **ohne Katalogeintrag** (zurückgestellt, msa-pruefungen.md § 2) |
| 2026-for.pdf | FOR | 2026 | 26_P10_Ma_FOR_A.pdf | 15 | ja | 1,6 MB | erfasst 2026-09-05, 33 Zeilen |

Abgleich (Befund § 4): Katalog 13 Hefte, alle mit Datei; eine Datei ohne
Katalogeintrag (2026-ebr.pdf).

**sonstiges/** – die 19 Gymnasialhefte 2014–2025, alle ohne Katalogeintrag;
nach Entscheidung 18 nicht Bestand, nur gesichert (§ 3). Kein papier-Wert,
deshalb Servername als Dateiname:

| Datei | Jahrgang | Seiten | Textebene | Größe |
|---|---|---|---|---|
| sonstiges/14_P10_Gym_Ma_A_Set1.pdf | 2014 | 7 | ja | 0,5 MB |
| sonstiges/15_P10_Ma_Gym_A.pdf | 2015 | 7 | ja | 1,0 MB |
| sonstiges/16_P10_Gym_Ma_A.pdf | 2016 | 11 | ja | 1,3 MB |
| sonstiges/17_P10_Ma_Gym_A.pdf | 2017 | 11 | ja | 1,4 MB |
| sonstiges/18_P10_Ma_Gym_A.pdf | 2018 | 11 | ja | 2,4 MB |
| sonstiges/19_P10_Ma_Gym_A_1.pdf | 2019 | 3 | ja | 0,8 MB |
| sonstiges/19_P10_Ma_Gym_A_2.pdf | 2019 | 9 | ja | 1,1 MB |
| sonstiges/20_P10_Ma_Gym_A_1.pdf | 2020 | 3 | ja | 0,8 MB |
| sonstiges/20_P10_Ma_Gym_A_2.pdf | 2020 | 9 | ja | 1,2 MB |
| sonstiges/21_P10_Ma_Gym_A1.pdf | 2021 | 3 | ja | 0,7 MB |
| sonstiges/21_P10_Ma_Gym_A2.pdf | 2021 | 9 | ja | 1,1 MB |
| sonstiges/22_P10_Ma_Gym_Aufgaben_1_und_2.pdf | 2022 | 3 | ja | 0,8 MB |
| sonstiges/22_P10_Ma_Gym_Aufgaben_3_bis_6.pdf | 2022 | 9 | ja | 1,2 MB |
| sonstiges/23_P10_Ma_Gym_A1.pdf | 2023 | 3 | ja | 1,0 MB |
| sonstiges/23_P10_Ma_Gym_A2.pdf | 2023 | 9 | ja | 1,4 MB |
| sonstiges/24_P10_Ma_Gym_A1.pdf | 2024 | 3 | ja | 0,8 MB |
| sonstiges/24_P10_Ma_Gym_A2.pdf | 2024 | 9 | ja | 1,4 MB |
| sonstiges/25_P10_Ma_Gym_A1.pdf | 2025 | 3 | ja | 0,9 MB |
| sonstiges/25_P10_Ma_Gym_A2.pdf | 2025 | 8 | ja | 1,2 MB |

## 6 Holen und Prüfen

    curl -s -o 2025-os.pdf "<Verzeichnis>/25_P10_Ma_A.pdf"

Vollständige URL = Verzeichnis aus § 1 + Serverdatei. Seitenzahl mit pypdf gegen
die Spalte Seiten prüfen (kein pdfinfo auf dem Rechner, CLAUDE.md). Liegt die
Datei schon unter hefte/msa/, wird sie nicht neu geholt.
