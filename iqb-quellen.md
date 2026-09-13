# QUELLEN IQB – Gemeinsame Abituraufgabenpools der Länder, Mathematik

Version 0.1 · 13.09.2026 · gehört zum Profil iqb

Diese Datei beschreibt die Quelle; die vollständige Dateiliste mit Zerlegung der
Kennungen, papier-Kürzel und Stapelzuordnung steht in iqb-quellen.csv (624
Zeilen, erzeugt aus der Übersichtsseite des IQB, nicht von Hand gepflegt).
iqb-bau.py liest sie.

## 1 Amtliche Quelle

Übersicht mit Paginierung, zwölf Einträge je Seite, 52 Seiten (Stand 13.09.2026):
https://www.iqb.hu-berlin.de/de/schule/aufgaben/sekii/abiturpruefungsaufgaben-mathematik/?page=N

Dateien: https://www.iqb.hu-berlin.de/media/exercise_files/Abituraufgaben_Mathematik/<Kennung>_Aufgabe.pdf

Jede Datei enthält Aufgabe, Erwartungshorizont, Standardbezug und
Bewertungshinweise (iqb.md § 3). Die Domain ist mit curl erreichbar.

## 2 Bestand

Geprüft am 13.09.2026: 624 Dateien, alle nach dem Muster <Kennung>_Aufgabe.pdf,
Zerlegung der Kennungen eindeutig, keine Kollisionen.

| | erhöht | grundlegend | gesamt |
|---|---|---|---|
| Prüfungsteil A | 175 | 153 | 328 |
| Prüfungsteil B | 158 | 138 | 296 |
| gesamt | 333 | 291 | 624 |

Nach Sachgebiet: Analysis 178, AG/LA (A1) 103, AG/LA (A2) 165, Stochastik 178.
Nach Jahr: 2017 45 · 2018 53 · 2019 52 · 2020 53 · 2021 54 · 2022 60 · 2023 62 ·
2024 62 · 2025 66 · 2026 70 · Beispielaufgaben ohne Jahr 47.

Teil A je Stapel (Jahr-Niveau-A), zugleich die Erfassungsreihenfolge:

| Stapel | Dateien | Stapel | Dateien |
|---|---|---|---|
| 2026-ga-A | 19 | 2026-ea-A | 20 |
| 2025-ga-A | 17 | 2025-ea-A | 20 |
| 2024-ga-A | 17 | 2024-ea-A | 19 |
| 2023-ga-A | 14 | 2023-ea-A | 18 |
| 2022-ga-A | 14 | 2022-ea-A | 17 |
| 2021-ga-A | 13 | 2021-ea-A | 19 |
| 2020-ga-A | 10 | 2020-ea-A | 15 |
| 2019-ga-A | 11 | 2019-ea-A | 10 |
| 2018-ga-A | 12 | 2018-ea-A | 12 |
| 2017-ga-A | 10 | 2017-ea-A | 11 |
| bsp-ga-A | 16 | bsp-ea-A | 14 |

Teil B: je Jahr und Niveau eine Datei je Sachgebiet und Rechnerfassung, mit
Nummer, wenn es mehrere gibt (WTR1, WTR2, MMS1 …). Das Rechnerkürzel heißt
2017–2021 CAS, ab 2022 MMS.

## 3 Kennungsmuster

    <Jahr|Beispielaufgaben> M <erhoeht|grundlegend> <A|B> <Analysis|AGLAA1|AGLAA2|Stochastik> <Rest>
    Rest in Teil A: Aufgabengruppe (1|2) und Nummer, wenn die Gruppe mehrere Aufgaben hat
    Rest in Teil B: WTR|CAS|MMS und Nummer, wenn es mehrere Dateien gibt

Beispiele: 2026MgrundlegendAAnalysis11 (Gruppe 1, Nr. 1), 2017MerhoehtAAnalysis2
(Gruppe 2, einzige Aufgabe), BeispielaufgabenMgrundlegendAAGLAA213 (A2, Gruppe 1,
Nr. 3), 2026MgrundlegendBAnalysisWTR1. Die Fußzeile der Datei trägt dieselbe
Kennung mit Unterstrichen.

## 4 Holen und Prüfen

    curl -s -o <Kennung>.pdf "https://www.iqb.hu-berlin.de/media/exercise_files/Abituraufgaben_Mathematik/<Kennung>_Aufgabe.pdf"

Seitenzahl prüfen (Teil A zwei Seiten, Teil B vier bis sechs), Text je Seite
extrahieren, jede Aufgabenseite rendern und ansehen – die Formeln liegen als
Bilder im PDF und fehlen in der Textextraktion.

Liste erneuern: Übersichtsseiten 1–N holen, alle Treffer auf
`Abituraufgaben_Mathematik/<Kennung>_Aufgabe.pdf` sammeln, zerlegen, sortieren
(Jahr absteigend, Beispielaufgaben zuletzt; grundlegend vor erhöht; A vor B;
Analysis, AG/LA (A1), AG/LA (A2), Stochastik; Gruppe bzw. Hilfsmittel; Nummer)
und als iqb-quellen.csv schreiben. Neue Jahrgänge werden dann als neue Stapel
sichtbar; Zeilen dürfen nur hinzukommen, nie verschwinden.
