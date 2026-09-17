# QUELLEN ABITUR – Mathematik Berlin/Brandenburg

Version 0.3 · 17.09.2026 · gehört zum Profil abi (in Arbeit)
Änderungen gegenüber 0.2 (Auftrag „Eichung korrigieren, Prüfungsgeschichte und
Prüfungsstruktur festhalten, Heftordner ordnen", Teil 4): § 8 lokaler
Heftordner hefte/ – alle dreizehn Dateien mit Jahr, Land, Niveau,
Rechnerfassung, Seiten, Textebene und Erfassungsstand; 2026-Dateien nach dem
Kürzel umbenannt.
Änderungen gegenüber 0.1: § 2 Brandenburg auf grundlegendem Niveau beantwortet,
BLiQ/LIBRA ab 2026; § 4 und § 6 IQB-Pool auf das Profil iqb verwiesen.

Diese Datei ersetzt eine Ablage der Prüfungshefte. Der Container wird zwischen
Sitzungen zurückgesetzt; die Hefte werden bei Bedarf über die hier genannten
URLs mit curl geholt. Die Spalte `papier` liefert die Kürzel, die im Katalog
und in den ids verwendet werden.

## 1 Amtliche Quelle

Bildungsserver Berlin-Brandenburg, Jahresseite für alle veröffentlichten
Jahrgänge:
https://bildungsserver.berlin-brandenburg.de/abituraufgaben-2011
(eigene Seiten je Jahr existieren nicht; `abituraufgaben-2017` liefert 404)

Verzeichnis der Dateien:
https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/pruefungen/abitur_bb/Zabi_Mathematik/

Veröffentlicht sind nur die Jahrgänge 2011–2018, aus urheberrechtlichen Gründen
nichts danach. Lösungen und Erwartungshorizonte sind nicht enthalten.

## 2 Bestand (Schnitt ab 2017)

Geprüft am 12.09.2026, alle zwölf Dateien mit HTTP 200 geholt.

| papier | Jahr | Land | Niveau | Rechner | Serverdatei | PDF-S. |
|---|---|---|---|---|---|---|
| 2017-be-gk | 2017 | BE | grundlegend | WTR | 17_Ma_GK_Aufgaben.pdf | 8 |
| 2017-be-gk-cas | 2017 | BE | grundlegend | CAS | 17_Ma_GK_CAS_Aufgaben.pdf | 8 |
| 2017-be-lk | 2017 | BE | erhöht | WTR | 17_Ma_LK_Aufgaben_neu.pdf | 10 |
| 2017-be-lk-cas | 2017 | BE | erhöht | CAS | 17_Ma_LK_CAS_Aufgaben_neu.pdf | 9 |
| 2017-bb-ea | 2017 | BB | erhöht | WTR | BB_17_Ma_Aufgaben.pdf | 10 |
| 2017-bb-ea-cas | 2017 | BB | erhöht | CAS | BB_17_Ma_CAS_Aufgaben.pdf | 10 |
| 2018-be-gk | 2018 | BE | grundlegend | WTR | 18_Ma_GK_Aufgaben.pdf | 11 |
| 2018-be-gk-cas | 2018 | BE | grundlegend | CAS | 18_Ma_GK_CAS_Aufgaben.pdf | 10 |
| 2018-be-lk | 2018 | BE | erhöht | WTR | 18_Ma_LK_Aufgaben.pdf | 11 |
| 2018-be-lk-cas | 2018 | BE | erhöht | CAS | 18_Ma_LK_CAS_Aufgaben.pdf | 9 |
| 2018-bb-ea | 2018 | BB | erhöht | WTR | BB_18_Ma_Aufgaben.pdf | 13 |
| 2018-bb-ea-cas | 2018 | BB | erhöht | CAS | BB_18_Ma_CAS_Aufgaben.pdf | 12 |

Vollständige URL = Verzeichnis aus § 1 + Serverdatei.

Auf grundlegendem Niveau gibt es keine Brandenburger Datei. Brandenburg hat eine
eigene zentrale Prüfung auf grundlegendem Niveau, veröffentlicht aber die
Aufgabenhefte nicht (abi.md § 9, abi-pruefungen.md § 4).

Ab dem Abitur 2026 entstehen die Aufgaben getrennt: Berlin über das BLiQ,
Brandenburg über das LIBRA (LISUM Ende 2024 aufgelöst; abi.md § 1). Für die
Quellenlage ändert das nichts – veröffentlicht bleibt 2011–2018.

## 3 Vorhanden, aber nicht im Bestand

Auf dem Server liegen außerdem 2014–2016 (14_Ma_GK, 14_Ma_GK_CAS,
16_Ma_GK, 16_Ma_GK_CAS, 16_Ma_LK, 16_Ma_LK_CAS, BB_14_Ma_L,
BB_14_Ma_L_CAS, BB_15_Ma, BB_15_Ma_CAS, BB_16_Ma_Aufgaben_1 und _2,
BB_16_Ma_CAS_Aufgaben_1 und _2, BE_14_Ma_LK, BE_14_CMa_LK, BE_15_Ma_GK,
BE_15_Ma_GK_CAS, BE_15_Ma_LK, BE_15_Ma_LK_CAS) sowie 2011–2013.

Nicht aufgenommen: alter Rahmenlehrplan 2006, noch keine Poolaufgaben des IQB.
Die Namensschemata schwanken dort (14_Ma_GK gegen BE_15_Ma_GK, zweiteilige
BB-Dateien 2016); bei einer späteren Erweiterung ist die Zuordnung einzeln zu
prüfen.

## 4 Zweite Quelle: IQB

https://www.iqb.hu-berlin.de/ , Bereich Abituraufgabenpools. Poolaufgaben seit
Prüfungsjahr 2017, nach der Prüfung veröffentlicht, einschließlich
Erwartungshorizonten und Bewertungshinweisen. Grenze: Es ist nicht erkennbar,
welches Land welche Poolaufgabe entnommen hat, und die Landesaufgaben stehen
dort nicht. Der Pool wird seit dem 13.09.2026 im eigenen Profil iqb erfasst
(iqb.md, iqb-quellen.md); er ist keine Quelle dieses Profils.

## 5 Verlagsbände (Upload durch den Lehrer)

Sieben Bände, 2016–2022, alle Berlin Grundkurs. Quelle nur für 2019–2022;
2016–2018 amtlich vorhanden. Aus ihnen liegen 2019, 2020 und 2021 als PDF
mit Textebene unter hefte/ (§ 8); dazu kommen die Scans 2022–2025
(Berlin/Brandenburg, GK und LK) und die PDFs 2026 (Brandenburg) aus den
Bänden zum Abitur 2026/2027. Aufgabeninhalt ist das Original der geschriebenen
Prüfung. Nicht amtlich sind Lösungen und Tipps; das Deckblatt mit
Bearbeitungszeit, Hilfsmitteln und Gesamtpunktzahl fehlt. Die mit „(CAS)"
markierten Aufgaben der Bände 2016 und 2017 sind Verlagsauswahl, keine
Differenzmenge.

## 6 Lösungen

Für die Landesaufgaben 2017/2018 gibt es keine amtlichen Lösungen; dort gilt
Kern § 3 d in der Fassung „eigene Rechnung". Amtliche Lösungen zu Poolaufgaben
gehören zum Profil iqb (iqb.md § 2).

## 7 Holen und Prüfen

    curl -s -o 2018-bb-ea.pdf "<Verzeichnis>/BB_18_Ma_Aufgaben.pdf"

Die Domain ist aus der Sandbox erreichbar. Beim Holen über „main" im Repo
Cache-Buster anhängen; für die Hefte nicht nötig. Seitenzahl mit `pdfinfo`
gegen die Spalte PDF-S. prüfen.

## 8 Lokaler Heftordner hefte/

Stand 17.09.2026 (Auftrag „Eichung korrigieren, Prüfungsgeschichte und
Prüfungsstruktur festhalten, Heftordner ordnen", Teil 4). Der Ordner liegt
neben dem Repo, per .gitignore ausgeschlossen (Verlagsausgaben,
urheberrechtlich geschützt). Dateiname = <jahr>-<land>-<niveau>.pdf, gleich
dem papier-Kürzel (abi.md § 4); bei abweichender Rechnerfassung käme -cas
bzw. -mms dazu (bisher keine solche Datei). Land und Niveau aus der Kopfzeile
der ersten Aufgabenseite (Befund in abi-pruefungen.md § 4, 17.09.2026),
Seiten und Textebene mit pypdf ermittelt. Umbenannt am 17.09.2026:
2026-bebb-gk.pdf → 2026-bb-gk.pdf, 2026-bebb-lk.pdf → 2026-bb-ea.pdf
(Kopfzeile „Brandenburg – Mathematik Leistungskurs", Kürzel für das erhöhte
Niveau in Brandenburg ist ea, § 2). Kollisionen und unklare Fälle: keine.
Rechnerfassung: keine Datei nennt CAS oder MMS, alle sind die Fassung ohne
MMS (WTR). Die Verlagsausgaben enthalten kein Deckblatt des Originals
(Bearbeitungszeit, Hilfsmittel, Gesamt-BE fehlen).

| Datei | Jahr | Land | Niveau | Rechnerfassung | Seiten | Textebene | Größe | Erfassungsstand |
|---|---|---|---|---|---|---|---|---|
| 2019-be-gk.pdf | 2019 | BE | grundlegend | WTR | 46 | ja (Aufgaben, Tipps, Lösungen) | 1,4 MB | nicht erfasst |
| 2020-be-gk.pdf | 2020 | BE | grundlegend | WTR | 49 | ja (Aufgaben, Tipps, Lösungen) | 1,2 MB | nicht erfasst |
| 2021-be-gk.pdf | 2021 | BE | grundlegend | WTR | 45 | ja (Aufgaben, Tipps, Lösungen) | 1,0 MB | nicht erfasst |
| 2022-bebb-gk.pdf | 2022 | BE/BB | grundlegend | WTR | 12 | nein (Bildscan, nur Aufgabenseiten) | 78,0 MB | erfasst 2026-09-16, 57 Zeilen |
| 2022-bebb-lk.pdf | 2022 | BE/BB | erhöht | WTR | 15 | nein (Bildscan, nur Aufgabenseiten) | 99,4 MB | erfasst 2026-09-16, 68 Zeilen |
| 2023-bebb-gk.pdf | 2023 | BE/BB | grundlegend | WTR | 14 | nein (Bildscan, nur Aufgabenseiten) | 90,1 MB | erfasst 2026-09-16, 58 Zeilen |
| 2023-bebb-lk.pdf | 2023 | BE/BB | erhöht | WTR | 14 | nein (Bildscan, nur Aufgabenseiten) | 93,1 MB | erfasst 2026-09-16, 66 Zeilen |
| 2024-bebb-gk.pdf | 2024 | BE/BB | grundlegend | WTR | 10 | nein (Bildscan, nur Aufgabenseiten) | 80,5 MB | erfasst 2026-09-16, 47 Zeilen |
| 2024-bebb-lk.pdf | 2024 | BE/BB | erhöht | WTR | 13 | nein (Bildscan, nur Aufgabenseiten) | 85,6 MB | nicht erfasst |
| 2025-bebb-gk.pdf | 2025 | BE/BB | grundlegend | WTR | 8 | nein (Bildscan, nur Aufgabenseiten) | 68,2 MB | erfasst 2026-09-16, 39 Zeilen |
| 2025-bebb-lk.pdf | 2025 | BE/BB | erhöht | WTR | 11 | nein (Bildscan, nur Aufgabenseiten) | 69,6 MB | nicht erfasst |
| 2026-bb-gk.pdf | 2026 | BB | grundlegend | WTR | 36 | ja (Aufgaben, Tipps, Lösungen; A5) | 0,9 MB | erfasst 2026-09-17, 45 Zeilen |
| 2026-bb-ea.pdf | 2026 | BB | erhöht | WTR | 47 | ja (Aufgaben, Tipps, Lösungen; A5) | 1,1 MB | erfasst 2026-09-17, 50 Zeilen |

Nicht erfasst sind fünf Dateien: 2019-be-gk, 2020-be-gk, 2021-be-gk (Berlin
Grundkurs, Format mit Teil A und drei Wahlpaaren; 2021 mit je einer
Geometrie- und Stochastikaufgabe), 2024-bebb-lk und 2025-bebb-lk (erhöhtes
Niveau, Kopfzeile „… Leistungskurs … Pflichtaufgaben"). Die Heftliste
abi-pruefungen.md § 2 führt sie mit Status „nicht erfasst".
