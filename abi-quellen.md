# QUELLEN ABITUR – Mathematik Berlin/Brandenburg

Version 0.5 · 17.09.2026 · gehört zum Profil abi (in Arbeit)
Änderungen gegenüber 0.4 (Auftrag C, Teil 4): § 5 CAS-Fassungen bestanden
als Prüfungsform weiter, STARK druckt sie ab 2018 nicht mehr ab; § 8 die
fünf abgeschriebenen Quelldateien (Stichwortverzeichnisse, Hinweise) im
Ordner hefte/.
Änderungen gegenüber 0.3 (Auftrag B „Fünf Hefte erfassen, Heftkorpus,
Katalog gegen Stark prüfen, CAS-Delta", Teile 1, 4 und 6): § 5 Verlagsbände
nach den Angaben des Lehrers mit Beschaffungstabelle je Jahrgang und Land;
§ 8 alle fünf Restdateien erfasst, dazu die amtlichen Dateien 2016/2017
(WTR und CAS, Berlin GK) für das CAS-Delta; § 9 Markdown-Korpus hefte-md/.
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

## 5 Verlagsbände (STARK; Angaben des Lehrers, Stand 17.09.2026)

Aufgabeninhalt der Bände ist das Original der geschriebenen Prüfung; nicht
amtlich sind Lösungen und Tipps, das Deckblatt mit Bearbeitungszeit,
Hilfsmitteln und Gesamtpunktzahl fehlt. Aus den Bänden stammen alle Dateien
unter hefte/ ab 2019 (§ 8).

**Vorhandene Bände.** Sieben Bände Berlin Grundkurs zu den Abiturjahrgängen
2016 bis 2022. Der Band zum Abitur 2021 („Berlin", Autorenliste „Berlin")
enthält die Jahrgänge 2016–2020; CAS-Fassungen führt er nur für 2016
Aufgabe 1.1 und 2017 Aufgabe 1.2 (Analysis) – Verlagsauswahl, keine
Differenzmenge (CAS-Delta: abi-pruefungen.md § 4, Auftrag B Teil 4). Die
CAS-Variante bestand als Prüfungsform weiter (Hilfsmittelteil desselben
Bands mit Geräteliste, abi.md § 11); STARK druckt sie ab dem Jahrgang 2018
nicht mehr ab. CAS-Fassungen der Landeshefte 2018–2021 sind daher über
keine bekannte Quelle zu beschaffen (Bildungsserver nur bis 2018, Bände
ohne CAS; ob der Brandenburger Band 2022 sie enthält, ist unbekannt). Ab dem
Band zum Abitur 2023 heißen die Bände „Berlin/Brandenburg" (gemeinsame
Hefte, Kürzel bebb). Die Bände zum Abitur 2027 (Grundkurs und Leistungskurs)
enthalten 2022–2025 gedruckt und 2026 Brandenburg als Online-Ergänzung
(MyStark); ein Berliner Heft 2026 enthalten sie nicht. Nicht vorhanden: der
Band zum Abitur 2022 „Brandenburg" Leistungskurs mit den Jahrgängen
2017–2021 (antiquarisch über rebuy). Er würde entscheiden, ob Brandenburg
2019–2021 dieselben Aufgaben stellte wie Berlin (abi.md § 9); der Lehrer
beschafft ihn vorerst nicht.

**Beschaffung je Jahrgang und Land** (vorhanden = amtlich oder als Band bzw.
Scan unter hefte/; STARK = über einen Verlagsband beschaffbar, meist
antiquarisch; – = nicht beschaffbar, weil weder veröffentlicht noch
verlegt):

| Jahrgang | Berlin GK | Berlin LK | Brandenburg GK | Brandenburg LK/EA |
|---|---|---|---|---|
| 2016–2018 | vorhanden (Bildungsserver, dazu Bände) | vorhanden (Bildungsserver) | – (nicht veröffentlicht, kein Band bekannt) | vorhanden (Bildungsserver, 2017/2018 erfasst) |
| 2019–2021 | vorhanden (Bände, erfasst) | STARK (Bände Berlin LK, nicht geprüft) | unklar (kein Band bekannt; Berlin GK „weitgehend gemeinsam", abi.md § 9) | STARK (Band 2022 „Brandenburg" LK, rebuy) |
| 2022–2025 | vorhanden (Bände 2027, gemeinsame Hefte bebb, erfasst) | vorhanden (Bände 2027, erfasst) | vorhanden (= bebb) | vorhanden (= bebb) |
| 2026 | – (kein Band, keine Veröffentlichung) | – | vorhanden (Band 2027 online, erfasst) | vorhanden (Band 2027 online, erfasst) |

Berlin 2026 ist die einzige Lücke, die Geld nicht schließt (abi-pruefungen.md
§ 3).

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
| 2019-be-gk.pdf | 2019 | BE | grundlegend | WTR | 46 | ja (Aufgaben, Tipps, Lösungen) | 1,4 MB | erfasst 2026-09-17, 45 Zeilen |
| 2020-be-gk.pdf | 2020 | BE | grundlegend | WTR | 49 | ja (Aufgaben, Tipps, Lösungen) | 1,2 MB | erfasst 2026-09-17, 51 Zeilen |
| 2021-be-gk.pdf | 2021 | BE | grundlegend | WTR | 45 | ja (Aufgaben, Tipps, Lösungen) | 1,0 MB | erfasst 2026-09-17, 56 Zeilen |
| 2022-bebb-gk.pdf | 2022 | BE/BB | grundlegend | WTR | 12 | nein (Bildscan, nur Aufgabenseiten) | 78,0 MB | erfasst 2026-09-16, 57 Zeilen |
| 2022-bebb-lk.pdf | 2022 | BE/BB | erhöht | WTR | 15 | nein (Bildscan, nur Aufgabenseiten) | 99,4 MB | erfasst 2026-09-16, 68 Zeilen |
| 2023-bebb-gk.pdf | 2023 | BE/BB | grundlegend | WTR | 14 | nein (Bildscan, nur Aufgabenseiten) | 90,1 MB | erfasst 2026-09-16, 58 Zeilen |
| 2023-bebb-lk.pdf | 2023 | BE/BB | erhöht | WTR | 14 | nein (Bildscan, nur Aufgabenseiten) | 93,1 MB | erfasst 2026-09-16, 66 Zeilen |
| 2024-bebb-gk.pdf | 2024 | BE/BB | grundlegend | WTR | 10 | nein (Bildscan, nur Aufgabenseiten) | 80,5 MB | erfasst 2026-09-16, 47 Zeilen |
| 2024-bebb-lk.pdf | 2024 | BE/BB | erhöht | WTR | 13 | nein (Bildscan, nur Aufgabenseiten) | 85,6 MB | erfasst 2026-09-17, 53 Zeilen |
| 2025-bebb-gk.pdf | 2025 | BE/BB | grundlegend | WTR | 8 | nein (Bildscan, nur Aufgabenseiten) | 68,2 MB | erfasst 2026-09-16, 39 Zeilen |
| 2025-bebb-lk.pdf | 2025 | BE/BB | erhöht | WTR | 11 | nein (Bildscan, nur Aufgabenseiten) | 69,6 MB | erfasst 2026-09-17, 46 Zeilen |
| 2026-bb-gk.pdf | 2026 | BB | grundlegend | WTR | 36 | ja (Aufgaben, Tipps, Lösungen; A5) | 0,9 MB | erfasst 2026-09-17, 45 Zeilen |
| 2026-bb-ea.pdf | 2026 | BB | erhöht | WTR | 47 | ja (Aufgaben, Tipps, Lösungen; A5) | 1,1 MB | erfasst 2026-09-17, 50 Zeilen |

Seit dem 17.09.2026 (Auftrag B, Teil 1) sind alle dreizehn Verlagsdateien
erfasst; die Heftliste abi-pruefungen.md § 2 führt Status und Kennzahlen.

**Amtliche Dateien im Ordner (Auftrag B, Teil 4, CAS-Delta).** Für den
Vergleich WTR gegen CAS liegen zusätzlich die Berliner Grundkurshefte 2016
und 2017 in beiden Rechnerfassungen unter hefte/, geholt vom Bildungsserver
(§ 1, § 3); sie sind keine Verlagsausgaben, bleiben aber der Einheitlichkeit
halber im selben Ordner. Erfasst wird daraus nichts (2017-be-gk ist nicht
Leitfassung, 2016 liegt vor dem Schnitt).

| Datei | Serverdatei | Seiten | Zweck |
|---|---|---|---|
| 2016-be-gk.pdf, 2016-be-gk-cas.pdf | 16_Ma_GK_Aufgaben.pdf, 16_Ma_GK_CAS_Aufgaben.pdf (§ 3 nennt sie ohne „_Aufgaben") | siehe abi-pruefungen.md § 4 | CAS-Delta Aufgabe 1.1 |
| 2017-be-gk.pdf, 2017-be-gk-cas.pdf | 17_Ma_GK_Aufgaben.pdf, 17_Ma_GK_CAS_Aufgaben.pdf | 8, 8 | CAS-Delta Aufgabe 1.2 |

**Abgeschriebene Quelldateien im Ordner (Auftrag C, 17.09.2026).** Fünf
Markdown-Dateien aus den STARK-Bänden, vom Lehrer angelegt; die beiden
Stichwortverzeichnisse 2027 verlustfrei aus Text-PDFs, die drei übrigen aus
Scans abgeschrieben (einzelne Ziffern können fehlerhaft sein). Verlagstext,
bleiben wie die Hefte außerhalb des Repos.

| Datei | Inhalt | Verwendung |
|---|---|---|
| stichwort-2027-bebb-gk.md | Stichwortverzeichnis Band 2027 GK (Jahrgänge 2022–2026), Seitenverweise <jahr>-<seite> | Katalog gegen Stark (abi-pruefungen.md § 4, Auftrag C Teil 3) |
| stichwort-2027-bebb-lk.md | Stichwortverzeichnis Band 2027 LK (2022–2026) | ebenso |
| stichwort-2021-be-gk.md | Stichwortverzeichnis Band 2021 Berlin GK (2016–2019) | ebenso |
| hinweise-2027-bebb.md | Vorspann der Bände 2027: Struktur, Bewertung, Hilfsmittel, beide Niveaus | abi.md § 11 (Beleg im Wortlaut) |
| hinweise-2021-be-gk.md | Vorspann des Bands 2021: Struktur, Bewertung, Hilfsmittel bis 2021 | abi.md § 11 (Reihe der Bewertungsschlüssel, CAS) |

## 9 Markdown-Korpus hefte-md/

Seit dem 17.09.2026 (Auftrag B, Teil 2) entsteht neben hefte/ der Ordner
hefte-md/ mit je einer Markdown-Datei je Prüfung (Wortlaut der Aufgaben,
Formeln als LaTeX, Abbildungen als ausgeschnittene JPEG-Dateien im
Unterordner <kürzel>/ mit Verweis und Bildbeschreibung im Text). Er enthält
Verlags- und Prüfungsmaterial und bleibt wie hefte/ außerhalb des Repos
(.gitignore). Erstes Heft: 2025-bebb-gk.md (Bericht in abi-pruefungen.md
§ 4); die übrigen Hefte 2022–2026 folgen nach Rückmeldung des Lehrers.
