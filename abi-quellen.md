# QUELLEN ABITUR – Mathematik Berlin/Brandenburg

Version 0.1 · 12.09.2026 · gehört zum Profil abi (in Arbeit)

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

Auf grundlegendem Niveau gibt es keine Brandenburger Datei. Ob Brandenburg
dieselbe Prüfung schrieb oder seine gA-Prüfung nicht veröffentlicht, ist offen.

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
Erwartungshorizonten und Bewertungshinweisen. Damit ist die Lösungslücke ab
2019 geschlossen. Grenze: Es ist nicht erkennbar, welches Land welche
Poolaufgabe entnommen hat, und die Landesaufgaben stehen dort nicht.

## 5 Verlagsbände (Upload durch den Lehrer)

Sieben Bände, 2016–2022, alle Berlin Grundkurs. Quelle nur für 2019–2022;
2016–2018 amtlich vorhanden. Aufgabeninhalt ist das Original der geschriebenen
Prüfung. Nicht amtlich sind Lösungen und Tipps; das Deckblatt mit
Bearbeitungszeit, Hilfsmitteln und Gesamtpunktzahl fehlt. Die mit „(CAS)"
markierten Aufgaben der Bände 2016 und 2017 sind Verlagsauswahl, keine
Differenzmenge.

## 6 Lösungen

Für die Landesaufgaben 2017/2018 gibt es keine amtlichen Lösungen; dort gilt
Kern § 3 d in der Fassung „eigene Rechnung". Für Poolaufgaben ab 2019 liegt der
Erwartungshorizont vor; dort gilt die Fassung „amtliche Lösung vorhanden" wie
im Profil fhr, `ergebnis` mit dem Zusatz „amtlich".

## 7 Holen und Prüfen

    curl -s -o 2018-bb-ea.pdf "<Verzeichnis>/BB_18_Ma_Aufgaben.pdf"

Die Domain ist aus der Sandbox erreichbar. Beim Holen über „main" im Repo
Cache-Buster anhängen; für die Hefte nicht nötig. Seitenzahl mit `pdfinfo`
gegen die Spalte PDF-S. prüfen.
