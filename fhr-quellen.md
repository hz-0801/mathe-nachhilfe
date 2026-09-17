# QUELLEN FACHHOCHSCHULREIFE – Mathematik Brandenburg

Version 0.1 · 18.09.2026 · gehört zum Profil fhr
Angelegt in Auftrag O, Punkt 2, nach dem Muster von abi-quellen.md (ohne die
Teile, die es dort nur wegen der Verlagsbände gibt). Die Zahlen zum lokalen
Bestand (§ 5) sind aus befund-quellenbestand-2026-09-18.md § 5 übernommen und
nicht neu erhoben.

Diese Datei ersetzt eine Ablage der Prüfungshefte im Repo. Die Hefte werden bei
Bedarf über die hier genannten URLs mit curl geholt; lokal liegen sie unter
hefte/fhr/ (nicht im Repo, § 5). Die Spalte `papier` liefert die Kürzel, die im
Katalog und in den ids verwendet werden (fhr.md § 4).

## 1 Amtliche Quelle

Bildungsserver Berlin-Brandenburg, Übersichtsseite für alle veröffentlichten
Jahrgänge:
https://bildungsserver.berlin-brandenburg.de/pruefungen-fos-bb

Verzeichnis der Hefte:
https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/pruefungen/Fachoberschule_BB/Pruefungsaufgaben/

Nachbarordner derselben Ablage: Pruefungsschwerpunkte/ (Prüfungsschwerpunkte
je Schuljahr und Fach) und Pruefungstermine/ (Rundschreiben des MBJS); beide
sind in fhr-vorgaben.md § 1 verzeichnet, nicht im Katalog.

Veröffentlicht sind die Jahrgänge 2019–2026, je Jahrgang zwei Lehrerhefte
(„Unterlagen für die Lehrkraft" mit Aufgabentext und Erwartungshorizont, ab
2021 meist mit Gutachtenbogen). Der dritte Vorschlag je Jahrgang
(Nachschreibetermin) liegt nicht auf dem Server (fhr.md § 4, fhr-pruefungen.md).

## 2 Bestand

Bestand des Profils sind die sechzehn Hefte 2019–2026, seit dem 12.09.2026 alle
erfasst (fhr.md § 1); Status je Heft in fhr-pruefungen.md.

| papier | Jahr | Serverdatei | PDF-S. | Katalog |
|---|---|---|---|---|
| A | 2019 | 19_Mathematik_FOS_Lehrer_A.pdf | 10 | erfasst |
| C | 2019 | 19_Mathematik_FOS_Lehrer_C.pdf | 9 | erfasst |
| A | 2020 | 20_FOS_Ma_EH_A.pdf | 9 | erfasst |
| C | 2020 | 20_FOS_Ma_EH_C.pdf | 9 | erfasst |
| A | 2021 | 21_FOS_Ma_LH_A.pdf | 9 | erfasst |
| B | 2021 | 21_FOS_Ma_LH_B.pdf | 8 | erfasst |
| B | 2022 | 22_FOS_Ma_B_LH.pdf | 10 | erfasst |
| C | 2022 | 22_FOS_Ma_C_LH.pdf | 10 | erfasst |
| A | 2023 | 23_FOS_Ma_A_LH.pdf | 10 | erfasst |
| C | 2023 | 23_FOS_Ma_C_LH.pdf | 8 | erfasst |
| B | 2024 | 24_FOS_Ma_B_LH.pdf | 10 | erfasst |
| C | 2024 | 24_FOS_Ma_C_LH.pdf | 10 | erfasst |
| A | 2025 | 25_FOS_Ma_LH_A.pdf | 9 | erfasst |
| C | 2025 | 25_FOS_Ma_LH_C.pdf | 10 | erfasst |
| B | 2026 | 26_FOS_Ma_LH_B.pdf | 10 | erfasst |
| C | 2026 | 26_FOS_Ma_LH_C.pdf | 10 | erfasst |

Vollständige URL = Verzeichnis aus § 1 + Serverdatei. Die Namensschemata des
Servers schwanken (Lehrer_A, EH_A, LH_A, A_LH); der Buchstabe des Vorschlags
ist das papier-Kürzel, seine Stellung im Namen wechselt.

## 3 Vorhanden, aber nicht im Bestand

Im Verzeichnis und in den Nachbarordnern liegen außerdem die
Prüfungsschwerpunkte Mathematik 2026/27 und 2027/28 und das Rundschreiben
MBJS_RS_07-26 (Vorgaben, fhr-vorgaben.md § 1; lokal gesichert, § 5
sonstiges/) sowie Dokumente zu Deutsch und Englisch (acht, nicht Mathematik,
nicht geholt). Kein IQB-Pool: die Aufgabenpools des IQB gelten nur für die
Allgemeine Hochschulreife (fhr.md § 9).

## 4 Lösungen

Amtliche Lösungen liegen für jedes Heft vor: die Hefte enthalten den
Erwartungshorizont mit verbindlicher Punkteverteilung, ab 2021 meist auch den
Gutachtenbogen. Für dieses Profil gilt Kern § 3 d in der Fassung „amtliche
Lösung vorhanden": sie ist maßgeblich, eigene Rechnung ist Kontrolle, ergebnis
trägt den Zusatz „amtlich" (fhr.md § 2, § 7).

## 5 Lokaler Heftordner hefte/fhr/

Stand 18.09.2026 (Auftrag N „Originale sichern und ordnen";
befund-quellenbestand-2026-09-18.md § 5: 19 Dateien, 12,8 MB, alle vom
Bildungsserver geholt, 0 nicht holbar). Der Ordner hefte/ liegt neben dem Repo,
per .gitignore ausgeschlossen, und ist je Profil unterteilt (abi-quellen.md
§ 8); hefte/fhr/ hält die Aufgabenhefte dieses Profils, hefte/fhr/sonstiges/
alles, was kein Heft ist.

Dateiname in hefte/fhr/ = <jahr>-<papier>.pdf in Kleinbuchstaben (2026-c.pdf);
Seiten und Textebene mit pypdf ermittelt.

| Datei | papier | Jahrgang | Serverdatei | Seiten | Textebene | Größe | Erfassungsstand |
|---|---|---|---|---|---|---|---|
| 2019-a.pdf | A | 2019 | 19_Mathematik_FOS_Lehrer_A.pdf | 10 | ja | 0,8 MB | erfasst 2026-09-12, 16 Zeilen |
| 2019-c.pdf | C | 2019 | 19_Mathematik_FOS_Lehrer_C.pdf | 9 | ja | 0,8 MB | erfasst 2026-09-12, 14 Zeilen |
| 2020-a.pdf | A | 2020 | 20_FOS_Ma_EH_A.pdf | 9 | ja | 0,7 MB | erfasst 2026-09-12, 15 Zeilen |
| 2020-c.pdf | C | 2020 | 20_FOS_Ma_EH_C.pdf | 9 | ja | 0,8 MB | erfasst 2026-09-12, 15 Zeilen |
| 2021-a.pdf | A | 2021 | 21_FOS_Ma_LH_A.pdf | 9 | ja | 0,8 MB | erfasst 2026-09-12, 16 Zeilen |
| 2021-b.pdf | B | 2021 | 21_FOS_Ma_LH_B.pdf | 8 | ja | 1,4 MB | erfasst 2026-09-12, 15 Zeilen |
| 2022-b.pdf | B | 2022 | 22_FOS_Ma_B_LH.pdf | 10 | ja | 0,5 MB | erfasst 2026-09-12, 16 Zeilen |
| 2022-c.pdf | C | 2022 | 22_FOS_Ma_C_LH.pdf | 10 | ja | 0,6 MB | erfasst 2026-09-12, 15 Zeilen |
| 2023-a.pdf | A | 2023 | 23_FOS_Ma_A_LH.pdf | 10 | ja | 0,3 MB | erfasst 2026-09-12, 17 Zeilen |
| 2023-c.pdf | C | 2023 | 23_FOS_Ma_C_LH.pdf | 8 | ja | 0,4 MB | erfasst 2026-09-12, 14 Zeilen |
| 2024-b.pdf | B | 2024 | 24_FOS_Ma_B_LH.pdf | 10 | ja | 1,0 MB | erfasst 2026-09-12, 16 Zeilen |
| 2024-c.pdf | C | 2024 | 24_FOS_Ma_C_LH.pdf | 10 | ja | 1,0 MB | erfasst 2026-09-12, 17 Zeilen |
| 2025-a.pdf | A | 2025 | 25_FOS_Ma_LH_A.pdf | 9 | ja | 0,8 MB | erfasst 2026-09-12, 19 Zeilen |
| 2025-c.pdf | C | 2025 | 25_FOS_Ma_LH_C.pdf | 10 | ja | 1,0 MB | erfasst 2026-09-12, 15 Zeilen |
| 2026-b.pdf | B | 2026 | 26_FOS_Ma_LH_B.pdf | 10 | ja | 0,8 MB | erfasst 2026-09-12, 17 Zeilen |
| 2026-c.pdf | C | 2026 | 26_FOS_Ma_LH_C.pdf | 10 | ja | 0,6 MB | erfasst 2026-09-12, 16 Zeilen |

Abgleich (Befund § 5): Katalog 16 Hefte, alle mit Datei; kein Heft ohne
Katalogeintrag.

**sonstiges/** – kein Aufgabenheft, alle ohne Katalogeintrag (Vorgaben, in
fhr-vorgaben.md § 1 verzeichnet):

| Datei | Herkunft | Seiten | Textebene | Größe |
|---|---|---|---|---|
| sonstiges/MBJS_RS_07-26.pdf | Pruefungstermine/ (Rundschreiben vom 25.06.2026) | 7 | ja | 0,2 MB |
| sonstiges/Pruefungsschwerpunkte_Mathematik_2026-2027.pdf | Pruefungsschwerpunkte/ (Prüfung 2027) | 2 | ja | 0,1 MB |
| sonstiges/Pruefungsschwerpunkte_Mathematik_2027-2028.pdf | Pruefungsschwerpunkte/ (Prüfung 2028) | 2 | ja | 92,4 KB |

## 6 Holen und Prüfen

    curl -s -o 2026-c.pdf "<Verzeichnis>/26_FOS_Ma_LH_C.pdf"

Vollständige URL = Verzeichnis aus § 1 + Serverdatei. Seitenzahl mit pypdf gegen
die Spalte Seiten prüfen (kein pdfinfo auf dem Rechner, CLAUDE.md). Liegt die
Datei schon unter hefte/fhr/, wird sie nicht neu geholt.
