# QUELLEN IQB – Gemeinsame Abituraufgabenpools der Länder, Mathematik

Version 0.4 · 15.09.2026 · gehört zum Profil iqb

Diese Datei beschreibt die Quelle; die vollständige Dateiliste mit Zerlegung der
Kennungen, papier-Kürzel, Stapelzuordnung, Seitenzahl und Dublettenverweis
steht in iqb-quellen.csv (624 Zeilen, erzeugt von iqb-quellen.py aus der
Übersichtsseite des IQB und dem Scan aller Dateien, nicht von Hand
gepflegt). iqb-bau.py liest sie.

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

Dubletten in Teil A (Scan 13.09.2026, alle drei Abschnitte verglichen, nur
Buchstaben und Ziffern – iqb-quellen.py v0.2, weil zwei PDF-Erzeuger Glyphen
wie ≠ und − verschieden ausgeben): 16 Paare wortgleicher Dateien, alle AG/LA,
je einmal unter A1 und A2 abgelegt; die zweite Datei zeigt in dublette_von auf
die erste und wird nicht erfasst. Zu erfassen sind damit 312 Aufgaben.
Seitenzahl: 312 Dateien mit zwei Seiten, 16 mit drei. Der 16. Fall
(2023MerhoehtAAGLAA211 = AGLAA111) kam beim Erfassen des Stapels 2023-ea-A ans
Licht; der Scan v0.1 hatte ihn wegen der Glyphen übersehen.

Teil B: je Jahr und Niveau eine Datei je Sachgebiet und Rechnerfassung, mit
Nummer, wenn es mehrere gibt (WTR1, WTR2, MMS1 …). Das Rechnerkürzel heißt
2017–2021 CAS, ab 2022 MMS. Scan 15.09.2026 (iqb-quellen.py v0.3, Abschnitt
„1 Aufgabe" ohne Seitenkopfzeilen und Hilfsmittelwort, Schwelle Gleichheit,
iqb.md § 7): 296 Dateien, 157 WTR, 139 MMS/CAS; 18 Dubletten, alle MMS/CAS →
WTR (eine von Hand bestätigt, DUBLETTEN_HAND im Skript), 121 MMS/CAS-Dateien
ohne WTR-Zwilling. v0.4 (Stapel 2026-ea-B-mms): 19 Dubletten, zwei von Hand
bestätigt – DUBLETTEN_HAND auch für rein redaktionelle Abweichungen ohne
Änderung an Zahlen, Aufträgen und BE (2026-ea-B Stochastik MMS 1 = WTR 1, ein
Artikel; iqb.md § 7), 120 MMS/CAS-Dateien ohne WTR-Zwilling. Seitenzahl: 83 Dateien mit drei, 164 mit vier, 46 mit
fünf, 3 mit sechs Seiten.

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

Liste erneuern: `python iqb-quellen.py [Cache-Ordner]` holt die
Übersichtsseiten, sammelt alle Treffer auf
`Abituraufgaben_Mathematik/<Kennung>_Aufgabe.pdf`, zerlegt und sortiert sie
(Jahr absteigend, Beispielaufgaben zuletzt; grundlegend vor erhöht; A vor B;
Analysis, AG/LA (A1), AG/LA (A2), Stochastik; Gruppe bzw. Hilfsmittel; Nummer),
lädt fehlende Dateien beider Teile in den Cache (Teil B seit v0.3), liest
Seitenzahl und Dubletten und schreibt iqb-quellen.csv. Neue Jahrgänge werden dann als neue Stapel sichtbar;
Kennungen dürfen nur hinzukommen, nie verschwinden – sonst bricht das Skript ab.
