# KORPUS-PROTOKOLL – Markdown-Korpus und OCR der Prüfungshefte

Angelegt 18.09.2026 (Auftrag Korpus und OCR). Läuft mitlaufend während der vier
Etappen (§ 2–5); § 0 hält Entscheidungen, die beim Arbeiten fehlten und ohne
Rückfrage getroffen wurden (Laufregeln des Auftrags), § 1 hält den
eingestellten ersten Anlauf fest. Nach einem Abbruch zeigt
`python korpus-bau.py <profil> --status`, welche Dateien noch offen sind;
`korpus-bau.py --bauen` trägt jede fertige oder fehlgeschlagene Datei selbst
hier ein (append_protokoll_zeile) – die Tabellen unter § 2–5 sind die
Handakte.

## 0 Entscheidungen ohne Rückfrage

- **Korrektur 18.09.2026 (zweiter Anlauf).** Der erste Anlauf las jede Seite
  mit dem Modell und übertrug sie von Hand in das reiche hefte-md-Format
  (Zweck: Katalogprüfung). Der Auftrag wurde korrigiert: Zweck dieses Laufs
  ist Durchsuchbarkeit, nicht Katalogprüfung – dafür genügt maschinelle
  Extraktion ohne Modell-Lesen. Ablage jetzt unter `korpus/<profil>/` statt
  `hefte-md/<profil>/`; das Muster hefte-md/ ist nicht mehr maßgeblich für
  dieses Format. Die sechs im ersten Anlauf erfassten msa-Dateien bleiben
  unter hefte-md/ liegen (§ 1) und werden nicht nachgearbeitet; sie zählen
  nicht zum Fortschritt von Etappe 1 unten, die bei null neu beginnt (52 von
  52 Dateien offen für `korpus/`).
- **Jede Seite wird gerendert, ausnahmslos.** Der Auftrag verlangt ein
  Ganzseitenrender „je Seite, die [Bilder oder Vektorgrafiken] enthält" –
  ohne Ansehen der Seite lässt sich das nicht zuverlässig automatisch
  entscheiden (eingebettete Rasterbilder sind über pypdf erkennbar,
  Vektorgrafik im Inhaltsstrom nicht robust genug, siehe Versuch unten).
  Nächstliegende Entscheidung: jede Seite wird gerendert (150 DPI, PNG, kein
  Zuschnitt); das trifft die geforderte Menge als Obermenge, kostet nur
  zusätzlichen – lokalen, nicht committeten – Plattenplatz.
- **Text unverändert.** `pypdf.extract_text()` je Seite, roh übernommen;
  Formeln, mehrspaltige Tabellen und Sonderzeichen kommen erwartbar
  verunstaltet heraus (Zehnerpotenzen, Brüche, Wurzelzeichen). Das ist keine
  Abweichung, sondern die Grenze der Extraktion – Einschätzung je Profil im
  Schlussbericht (§ 6).
- **Etappe 2 „abi amtlich 2011–2018" = alle hefte/abi/*.pdf außer** den
  dreizehn Verlagsheften ab 2019 (2019-be-gk … 2026-bb-gk, elektronisch schon
  über hefte-md/ durchsuchbar) und den drei STARK-Alternativfassungen
  2016–2018 (`*-stark.pdf`, Dubletten der amtlichen Fassung) – macht die
  genannten 44 Dateien (60 Dateien im Ordner, 60 − 13 − 3 = 44), geprüft mit
  `korpus-bau.py abi --status --etappe 2`.
- **Etappe 3** läuft über die acht Bildscan-Verlagshefte 2022–2025
  (befund-quellenbestand-2026-09-18.md: Textebene „nein", 68–99 MB je Scan);
  `korpus-bau.py abi --ocr` erzeugt `<datei>-ocr.pdf` daneben, danach baut
  `--bauen --etappe 3` den Korpus aus diesen -ocr.pdf (Filter: Dateiname
  endet auf `-ocr.pdf`).

## 1 hefte-md/ – eingestellter erster Anlauf (Modell-gelesen)

Sechs Dateien im reichen, katalognahen Format erfasst, bevor der Auftrag auf
rein maschinelle Extraktion korrigiert wurde (§ 0). Bleiben liegen, werden
nicht fortgeführt und nicht in `korpus/` dupliziert.

| Datei | Ergebnis | Seiten | Abbildungen | Dauer/Grund |
|---|---|---|---|---|
| msa/2014-os.pdf | erfasst (hefte-md/, eingestellt) | 9 | 7 (Ganzseite) | – |
| msa/2015-os.pdf | erfasst (hefte-md/, eingestellt) | 9 | 7 (Ganzseite) | – |
| msa/2016-os.pdf | erfasst (hefte-md/, eingestellt) | 9 | 8 (Ganzseite) | – |
| msa/2017-os.pdf | erfasst (hefte-md/, eingestellt) | 15 | 8 (Ganzseite) | – |
| msa/2018-os.pdf | erfasst (hefte-md/, eingestellt) | 15 | 8 (Ganzseite) | – |
| msa/2019-os.pdf | erfasst (hefte-md/, eingestellt) | 15 | 10 (Ganzseite) | – |

## 2 korpus/ Etappe 1 – msa und fhr (52 Dateien)

| Datei | Ergebnis | Seiten | Zeichen | Abbildungen | Dauer/Grund |
|---|---|---|---|---|---|
| msa/2014-os.pdf | erfasst | 9 | 10371 | 9 | 2.5 s |
| msa/2015-os.pdf | erfasst | 9 | 10962 | 9 | 1.9 s |
| msa/2016-os.pdf | erfasst | 9 | 12399 | 9 | 2.2 s |
| msa/2017-os.pdf | erfasst | 15 | 22850 | 15 | 4.1 s |
| msa/2018-os.pdf | erfasst | 15 | 20180 | 15 | 3.2 s |
| msa/2019-os.pdf | erfasst | 15 | 19448 | 15 | 3.4 s |
| msa/2020-os.pdf | erfasst | 15 | 20685 | 15 | 3.8 s |
| msa/2021-os.pdf | erfasst | 15 | 19419 | 15 | 3.5 s |
| msa/2022-os.pdf | erfasst | 13 | 17999 | 13 | 3.2 s |
| msa/2023-os.pdf | erfasst | 12 | 17016 | 12 | 3.1 s |
| msa/2024-os.pdf | erfasst | 14 | 18661 | 14 | 3.2 s |
| msa/2025-os.pdf | erfasst | 15 | 19137 | 15 | 3.4 s |
| msa/2026-ebr.pdf | erfasst | 10 | 11734 | 10 | 2.3 s |
| msa/2026-for.pdf | erfasst | 15 | 18278 | 15 | 3.2 s |
| msa/sonstiges/14_P10_Gym_Ma_A_Set1.pdf | erfasst | 7 | 8702 | 7 | 1.7 s |
| msa/sonstiges/15_P10_Ma_Gym_A.pdf | erfasst | 7 | 9407 | 7 | 1.9 s |
| msa/sonstiges/16_P10_Gym_Ma_A.pdf | erfasst | 11 | 18653 | 11 | 3.2 s |
| msa/sonstiges/17_P10_Ma_Gym_A.pdf | erfasst | 11 | 15965 | 11 | 3.2 s |
| msa/sonstiges/18_P10_Ma_Gym_A.pdf | erfasst | 11 | 15642 | 11 | 3.0 s |
| msa/sonstiges/19_P10_Ma_Gym_A_1.pdf | erfasst | 3 | 3858 | 3 | 1.2 s |
| msa/sonstiges/19_P10_Ma_Gym_A_2.pdf | erfasst | 9 | 12374 | 9 | 2.4 s |
| msa/sonstiges/20_P10_Ma_Gym_A_1.pdf | erfasst | 3 | 4436 | 3 | 1.5 s |
| msa/sonstiges/20_P10_Ma_Gym_A_2.pdf | erfasst | 9 | 11684 | 9 | 2.3 s |
| msa/sonstiges/21_P10_Ma_Gym_A1.pdf | erfasst | 3 | 4272 | 3 | 1.8 s |
| msa/sonstiges/21_P10_Ma_Gym_A2.pdf | erfasst | 9 | 11798 | 9 | 4.3 s |
| msa/sonstiges/22_P10_Ma_Gym_Aufgaben_1_und_2.pdf | erfasst | 3 | 3577 | 3 | 1.4 s |
| msa/sonstiges/22_P10_Ma_Gym_Aufgaben_3_bis_6.pdf | erfasst | 9 | 12615 | 9 | 2.7 s |
| msa/sonstiges/23_P10_Ma_Gym_A1.pdf | erfasst | 3 | 4083 | 3 | 1.5 s |
| msa/sonstiges/23_P10_Ma_Gym_A2.pdf | erfasst | 9 | 13445 | 9 | 2.7 s |
| msa/sonstiges/24_P10_Ma_Gym_A1.pdf | erfasst | 3 | 4256 | 3 | 1.5 s |
| msa/sonstiges/24_P10_Ma_Gym_A2.pdf | erfasst | 9 | 13470 | 9 | 2.6 s |
| msa/sonstiges/25_P10_Ma_Gym_A1.pdf | erfasst | 3 | 4007 | 3 | 1.6 s |
| msa/sonstiges/25_P10_Ma_Gym_A2.pdf | erfasst | 8 | 11290 | 8 | 2.5 s |
| fhr/2019-a.pdf | erfasst | 10 | 12549 | 10 | 1.5 s |
| fhr/2019-c.pdf | erfasst | 9 | 10838 | 9 | 0.8 s |
| fhr/2020-a.pdf | erfasst | 9 | 10725 | 9 | 0.9 s |
| fhr/2020-c.pdf | erfasst | 9 | 13129 | 9 | 1.0 s |
| fhr/2021-a.pdf | erfasst | 9 | 11868 | 9 | 0.9 s |
| fhr/2021-b.pdf | erfasst | 8 | 11371 | 8 | 0.9 s |
| fhr/2022-b.pdf | erfasst | 10 | 11534 | 10 | 0.9 s |
| fhr/2022-c.pdf | erfasst | 10 | 11931 | 10 | 0.9 s |
| fhr/2023-a.pdf | erfasst | 10 | 11945 | 10 | 0.8 s |
| fhr/2023-c.pdf | erfasst | 8 | 10012 | 8 | 0.7 s |
| fhr/2024-b.pdf | erfasst | 10 | 13396 | 10 | 0.9 s |
| fhr/2024-c.pdf | erfasst | 10 | 13182 | 10 | 0.9 s |
| fhr/2025-a.pdf | erfasst | 9 | 13412 | 9 | 1.0 s |
| fhr/2025-c.pdf | erfasst | 10 | 12614 | 10 | 1.0 s |
| fhr/2026-b.pdf | erfasst | 10 | 12810 | 10 | 1.0 s |
| fhr/2026-c.pdf | erfasst | 10 | 13569 | 10 | 1.0 s |
| fhr/sonstiges/MBJS_RS_07-26.pdf | erfasst | 7 | 14613 | 7 | 0.6 s |
| fhr/sonstiges/Pruefungsschwerpunkte_Mathematik_2026-2027.pdf | erfasst | 2 | 4599 | 2 | 0.2 s |
| fhr/sonstiges/Pruefungsschwerpunkte_Mathematik_2027-2028.pdf | erfasst | 2 | 4548 | 2 | 0.2 s |

## 3 korpus/ Etappe 2 – abi amtlich 2011–2018 (44 Dateien)

| Datei | Ergebnis | Seiten | Zeichen | Abbildungen | Dauer/Grund |
|---|---|---|---|---|---|
| abi/2011-bebb-gk-cas.pdf | erfasst | 9 | 16772 | 9 | 1.4 s |
| abi/2011-bebb-gk.pdf | erfasst | 10 | 16904 | 10 | 1.0 s |
| abi/2011-bebb-lk-cas.pdf | erfasst | 9 | 17907 | 9 | 0.9 s |
| abi/2011-bebb-lk.pdf | erfasst | 12 | 24043 | 12 | 1.2 s |
| abi/2012-bebb-gk-cas.pdf | erfasst | 8 | 14088 | 8 | 0.7 s |
| abi/2012-bebb-gk.pdf | erfasst | 8 | 12519 | 8 | 0.7 s |
| abi/2012-bebb-lk-cas.pdf | erfasst | 8 | 16665 | 8 | 0.9 s |
| abi/2012-bebb-lk.pdf | erfasst | 11 | 23477 | 11 | 1.2 s |
| abi/2013-bebb-gk-cas.pdf | erfasst | 8 | 15051 | 8 | 1.7 s |
| abi/2013-bebb-gk.pdf | erfasst | 8 | 13018 | 8 | 1.7 s |
| abi/2013-bebb-lk-cas.pdf | erfasst | 7 | 16563 | 7 | 1.7 s |
| abi/2013-bebb-lk.pdf | erfasst | 10 | 21256 | 10 | 2.1 s |
| abi/2014-bb-ea-cas.pdf | erfasst | 8 | 16710 | 8 | 1.7 s |
| abi/2014-bb-ea.pdf | erfasst | 9 | 18909 | 9 | 1.9 s |
| abi/2014-be-gk-cas.pdf | erfasst | 8 | 13935 | 8 | 0.9 s |
| abi/2014-be-gk.pdf | erfasst | 10 | 19359 | 10 | 1.2 s |
| abi/2014-be-lk-cas.pdf | erfasst | 8 | 16589 | 8 | 1.7 s |
| abi/2014-be-lk.pdf | erfasst | 9 | 18908 | 9 | 1.9 s |
| abi/2015-bb-ea-cas.pdf | erfasst | 9 | 16447 | 9 | 2.4 s |
| abi/2015-bb-ea.pdf | erfasst | 9 | 17421 | 9 | 2.7 s |
| abi/2015-be-gk-cas.pdf | erfasst | 11 | 14846 | 11 | 1.0 s |
| abi/2015-be-gk.pdf | erfasst | 12 | 19890 | 12 | 1.3 s |
| abi/2015-be-lk-cas.pdf | erfasst | 8 | 16404 | 8 | 2.5 s |
| abi/2015-be-lk.pdf | erfasst | 11 | 20247 | 11 | 2.7 s |
| abi/2016-bb-ea-cas-teil1.pdf | erfasst | 3 | 4913 | 3 | 1.4 s |
| abi/2016-bb-ea-cas-teil2.pdf | erfasst | 5 | 10408 | 5 | 1.8 s |
| abi/2016-bb-ea-teil1.pdf | erfasst | 3 | 5025 | 3 | 1.3 s |
| abi/2016-bb-ea-teil2.pdf | erfasst | 6 | 12484 | 6 | 2.0 s |
| abi/2016-be-gk-cas.pdf | erfasst | 8 | 16361 | 8 | 1.2 s |
| abi/2016-be-gk.pdf | erfasst | 9 | 18764 | 9 | 1.5 s |
| abi/2016-be-lk-cas.pdf | erfasst | 7 | 15571 | 7 | 2.4 s |
| abi/2016-be-lk.pdf | erfasst | 8 | 17109 | 8 | 2.6 s |
| abi/2017-bb-ea-cas.pdf | erfasst | 10 | 20869 | 10 | 3.4 s |
| abi/2017-bb-ea.pdf | erfasst | 10 | 20359 | 10 | 3.2 s |
| abi/2017-be-gk-cas.pdf | erfasst | 8 | 15581 | 8 | 1.1 s |
| abi/2017-be-gk.pdf | erfasst | 8 | 17911 | 8 | 1.4 s |
| abi/2017-be-lk-cas.pdf | erfasst | 9 | 19199 | 9 | 2.4 s |
| abi/2017-be-lk.pdf | erfasst | 10 | 21327 | 10 | 2.6 s |
| abi/2018-bb-ea-cas.pdf | erfasst | 12 | 19730 | 12 | 4.2 s |
| abi/2018-bb-ea.pdf | erfasst | 13 | 22261 | 13 | 4.2 s |
| abi/2018-be-gk-cas.pdf | erfasst | 10 | 17145 | 10 | 1.5 s |
| abi/2018-be-gk.pdf | erfasst | 11 | 18888 | 11 | 2.1 s |
| abi/2018-be-lk-cas.pdf | erfasst | 9 | 17906 | 9 | 2.7 s |
| abi/2018-be-lk.pdf | erfasst | 11 | 23087 | 11 | 3.2 s |

## 4 korpus/ Etappe 3 – OCR der acht Bildscans + Korpus (8 Dateien)

**Blockiert am 18.09.2026: kein Tesseract auf dem Rechner installierbar.**
`ocrmypdf` braucht das Tesseract-Programm (kein reines Python-Paket); pip
--target hilft hier nicht. Winget kennt `UB-Mannheim.TesseractOCR`
(Installer-URL und SHA-256 geprüft, Hash stimmt), aber:
- `winget install --scope user` bricht mit „No applicable installer found"
  ab – der NSIS-Installer ist nicht für Benutzer-Scope deklariert.
- Direkter Aufruf des heruntergeladenen, hashgeprüften Installers mit
  `/S /D=<Benutzerordner ohne Programme>` bricht mit „Der Vorgang wurde
  durch den Benutzer abgebrochen" ab – der Installer verlangt in seinem
  Manifest Administratorrechte (UAC), unabhängig vom Zielordner; die
  Sitzung läuft ohne Administratorkonto und ohne interaktive
  UAC-Bestätigung.
- Kein 7-Zip installiert, um den Installer ohne Ausführung zu entpacken.

Dieselbe Hürde träfe `ocrmypdf` selbst (braucht zusätzlich Ghostscript).
Eintrag dazu in `faellig.md` § 3 (liegt beim Lehrer: Tesseract/Ghostscript
installieren oder Administratorrechte für diese Sitzung). Etappe 3 bleibt
offen, bis das geklärt ist; Etappe 4 läuft unabhängig weiter.

| Datei | Ergebnis | Seiten | Zeichen | Abbildungen | Dauer/Grund |
|---|---|---|---|---|---|

## 5 korpus/ Etappe 4 – iqb (624 Dateien)

| Datei | Ergebnis | Seiten | Zeichen | Abbildungen | Dauer/Grund |
|---|---|---|---|---|---|
| iqb/2017MerhoehtAAGLAA111.pdf | erfasst | 2 | 2525 | 2 | 0.7 s |
| iqb/2017MerhoehtAAGLAA112.pdf | erfasst | 3 | 2781 | 3 | 0.2 s |
| iqb/2017MerhoehtAAGLAA211.pdf | erfasst | 2 | 2100 | 2 | 0.2 s |
| iqb/2017MerhoehtAAGLAA212.pdf | erfasst | 2 | 2183 | 2 | 0.2 s |
| iqb/2017MerhoehtAAGLAA22.pdf | erfasst | 2 | 2404 | 2 | 0.2 s |
| iqb/2017MerhoehtAAnalysis11.pdf | erfasst | 2 | 2145 | 2 | 0.2 s |
| iqb/2017MerhoehtAAnalysis12.pdf | erfasst | 2 | 2289 | 2 | 0.2 s |
| iqb/2017MerhoehtAAnalysis2.pdf | erfasst | 2 | 2465 | 2 | 0.2 s |
| iqb/2017MerhoehtAStochastik11.pdf | erfasst | 2 | 2822 | 2 | 0.2 s |
| iqb/2017MerhoehtAStochastik12.pdf | erfasst | 2 | 2505 | 2 | 0.2 s |
| iqb/2017MerhoehtAStochastik2.pdf | erfasst | 2 | 2574 | 2 | 0.2 s |
| iqb/2017MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 6739 | 4 | 0.5 s |
| iqb/2017MerhoehtBAGLAA2CAS1.pdf | erfasst | 4 | 6112 | 4 | 0.6 s |
| iqb/2017MerhoehtBAGLAA2CAS2.pdf | erfasst | 4 | 5943 | 4 | 0.6 s |
| iqb/2017MerhoehtBAGLAA2WTR1.pdf | erfasst | 3 | 5730 | 3 | 0.5 s |
| iqb/2017MerhoehtBAGLAA2WTR2.pdf | erfasst | 3 | 5417 | 3 | 0.5 s |
| iqb/2017MerhoehtBAGLAA2WTR3.pdf | erfasst | 4 | 5826 | 4 | 0.5 s |
| iqb/2017MerhoehtBAnalysisCAS1.pdf | erfasst | 5 | 8085 | 5 | 0.8 s |
| iqb/2017MerhoehtBAnalysisCAS2.pdf | erfasst | 5 | 8195 | 5 | 0.9 s |
| iqb/2017MerhoehtBAnalysisWTR1.pdf | erfasst | 5 | 6904 | 5 | 0.7 s |
| iqb/2017MerhoehtBAnalysisWTR2.pdf | erfasst | 5 | 6984 | 5 | 0.8 s |
| iqb/2017MerhoehtBAnalysisWTR3.pdf | erfasst | 5 | 7603 | 5 | 0.8 s |
| iqb/2017MerhoehtBStochastikCAS1.pdf | erfasst | 3 | 4725 | 3 | 0.6 s |
| iqb/2017MerhoehtBStochastikCAS2.pdf | erfasst | 4 | 6257 | 4 | 0.7 s |
| iqb/2017MerhoehtBStochastikWTR.pdf | erfasst | 3 | 5994 | 3 | 0.7 s |
| iqb/2017MgrundlegendAAGLAA11.pdf | erfasst | 2 | 2360 | 2 | 0.3 s |
| iqb/2017MgrundlegendAAGLAA211.pdf | erfasst | 2 | 2344 | 2 | 0.3 s |
| iqb/2017MgrundlegendAAGLAA212.pdf | erfasst | 2 | 2182 | 2 | 0.3 s |
| iqb/2017MgrundlegendAAGLAA22.pdf | erfasst | 2 | 2637 | 2 | 0.3 s |
| iqb/2017MgrundlegendAAnalysis11.pdf | erfasst | 2 | 2213 | 2 | 0.2 s |
| iqb/2017MgrundlegendAAnalysis12.pdf | erfasst | 2 | 1870 | 2 | 0.2 s |
| iqb/2017MgrundlegendAAnalysis2.pdf | erfasst | 2 | 2313 | 2 | 0.3 s |
| iqb/2017MgrundlegendAStochastik11.pdf | erfasst | 2 | 1981 | 2 | 0.2 s |
| iqb/2017MgrundlegendAStochastik12.pdf | erfasst | 2 | 2180 | 2 | 0.2 s |
| iqb/2017MgrundlegendAStochastik2.pdf | erfasst | 2 | 2267 | 2 | 0.2 s |
| iqb/2017MgrundlegendBAGLAA1CAS.pdf | erfasst | 4 | 6214 | 4 | 0.6 s |
| iqb/2017MgrundlegendBAGLAA2CAS1.pdf | erfasst | 3 | 4977 | 3 | 0.5 s |
| iqb/2017MgrundlegendBAGLAA2CAS2.pdf | erfasst | 3 | 4348 | 3 | 0.4 s |
| iqb/2017MgrundlegendBAGLAA2WTR1.pdf | erfasst | 4 | 5298 | 4 | 0.5 s |
| iqb/2017MgrundlegendBAGLAA2WTR2.pdf | erfasst | 3 | 4643 | 3 | 0.4 s |
| iqb/2017MgrundlegendBAnalysisCAS.pdf | erfasst | 5 | 7063 | 5 | 0.7 s |
| iqb/2017MgrundlegendBAnalysisWTR.pdf | erfasst | 4 | 6298 | 4 | 0.7 s |
| iqb/2017MgrundlegendBStochastikCAS.pdf | erfasst | 3 | 4436 | 3 | 0.5 s |
| iqb/2017MgrundlegendBStochastikWTR1.pdf | erfasst | 3 | 4307 | 3 | 0.4 s |
| iqb/2017MgrundlegendBStochastikWTR2.pdf | erfasst | 3 | 3826 | 3 | 0.4 s |
| iqb/2018MerhoehtAAGLAA111.pdf | erfasst | 2 | 2859 | 2 | 0.2 s |
| iqb/2018MerhoehtAAGLAA112.pdf | erfasst | 2 | 2694 | 2 | 0.3 s |
| iqb/2018MerhoehtAAGLAA12.pdf | erfasst | 2 | 2790 | 2 | 0.3 s |
| iqb/2018MerhoehtAAGLAA211.pdf | erfasst | 2 | 2436 | 2 | 0.3 s |
| iqb/2018MerhoehtAAGLAA212.pdf | erfasst | 2 | 2419 | 2 | 0.3 s |
| iqb/2018MerhoehtAAGLAA22.pdf | erfasst | 2 | 2485 | 2 | 0.3 s |
| iqb/2018MerhoehtAAnalysis11.pdf | erfasst | 2 | 2277 | 2 | 0.2 s |
| iqb/2018MerhoehtAAnalysis12.pdf | erfasst | 2 | 2027 | 2 | 0.2 s |
| iqb/2018MerhoehtAAnalysis2.pdf | erfasst | 2 | 2113 | 2 | 0.3 s |
| iqb/2018MerhoehtAStochastik11.pdf | erfasst | 2 | 2308 | 2 | 0.3 s |
| iqb/2018MerhoehtAStochastik12.pdf | erfasst | 2 | 2196 | 2 | 0.3 s |
| iqb/2018MerhoehtAStochastik2.pdf | erfasst | 2 | 1983 | 2 | 0.3 s |
| iqb/2018MerhoehtBAGLAA1CAS1.pdf | erfasst | 5 | 7182 | 5 | 0.6 s |
| iqb/2018MerhoehtBAGLAA1CAS2.pdf | erfasst | 4 | 7537 | 4 | 0.6 s |
| iqb/2018MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 5545 | 4 | 0.6 s |
| iqb/2018MerhoehtBAGLAA2CAS1.pdf | erfasst | 3 | 5258 | 3 | 0.4 s |
| iqb/2018MerhoehtBAGLAA2CAS2.pdf | erfasst | 3 | 5146 | 3 | 0.5 s |
| iqb/2018MerhoehtBAGLAA2WTR1.pdf | erfasst | 3 | 4735 | 3 | 0.4 s |
| iqb/2018MerhoehtBAGLAA2WTR2.pdf | erfasst | 4 | 5713 | 4 | 0.5 s |
| iqb/2018MerhoehtBAGLAA2WTR3.pdf | erfasst | 4 | 5638 | 4 | 0.6 s |
| iqb/2018MerhoehtBAnalysisCAS1.pdf | erfasst | 5 | 8864 | 5 | 0.8 s |
| iqb/2018MerhoehtBAnalysisCAS2.pdf | erfasst | 5 | 8569 | 5 | 0.9 s |
| iqb/2018MerhoehtBAnalysisCAS3.pdf | erfasst | 5 | 8659 | 5 | 0.9 s |
| iqb/2018MerhoehtBAnalysisWTR1.pdf | erfasst | 5 | 7489 | 5 | 0.8 s |
| iqb/2018MerhoehtBAnalysisWTR2.pdf | erfasst | 5 | 7687 | 5 | 0.8 s |
| iqb/2018MerhoehtBStochastikCAS1.pdf | erfasst | 3 | 5347 | 3 | 0.4 s |
| iqb/2018MerhoehtBStochastikCAS2.pdf | erfasst | 4 | 6344 | 4 | 0.6 s |
| iqb/2018MerhoehtBStochastikWTR1.pdf | erfasst | 3 | 5396 | 3 | 0.4 s |
| iqb/2018MerhoehtBStochastikWTR2.pdf | erfasst | 4 | 5930 | 4 | 0.6 s |
| iqb/2018MgrundlegendAAGLAA111.pdf | erfasst | 2 | 2305 | 2 | 0.3 s |
| iqb/2018MgrundlegendAAGLAA112.pdf | erfasst | 3 | 3048 | 3 | 0.4 s |
| iqb/2018MgrundlegendAAGLAA12.pdf | erfasst | 2 | 2338 | 2 | 0.3 s |
| iqb/2018MgrundlegendAAGLAA211.pdf | erfasst | 2 | 2238 | 2 | 0.2 s |
| iqb/2018MgrundlegendAAGLAA212.pdf | erfasst | 2 | 2499 | 2 | 0.3 s |
| iqb/2018MgrundlegendAAGLAA22.pdf | erfasst | 2 | 2198 | 2 | 0.2 s |
| iqb/2018MgrundlegendAAnalysis11.pdf | erfasst | 2 | 1881 | 2 | 0.2 s |
| iqb/2018MgrundlegendAAnalysis12.pdf | erfasst | 2 | 1807 | 2 | 0.3 s |
| iqb/2018MgrundlegendAAnalysis2.pdf | erfasst | 2 | 2329 | 2 | 0.2 s |
| iqb/2018MgrundlegendAStochastik11.pdf | erfasst | 2 | 2037 | 2 | 0.2 s |
| iqb/2018MgrundlegendAStochastik12.pdf | erfasst | 2 | 2752 | 2 | 0.3 s |
| iqb/2018MgrundlegendAStochastik2.pdf | erfasst | 2 | 2450 | 2 | 0.2 s |
| iqb/2018MgrundlegendBAGLAA1WTR.pdf | erfasst | 4 | 6149 | 4 | 0.5 s |
| iqb/2018MgrundlegendBAGLAA2CAS1.pdf | erfasst | 4 | 5737 | 4 | 0.4 s |
| iqb/2018MgrundlegendBAGLAA2CAS2.pdf | erfasst | 4 | 5166 | 4 | 0.5 s |
| iqb/2018MgrundlegendBAGLAA2WTR1.pdf | erfasst | 3 | 4489 | 3 | 0.4 s |
| iqb/2018MgrundlegendBAGLAA2WTR2.pdf | erfasst | 3 | 5393 | 3 | 0.4 s |
| iqb/2018MgrundlegendBAnalysisCAS1.pdf | erfasst | 5 | 7232 | 5 | 0.7 s |
| iqb/2018MgrundlegendBAnalysisCAS2.pdf | erfasst | 4 | 6711 | 4 | 0.6 s |
| iqb/2018MgrundlegendBAnalysisWTR.pdf | erfasst | 5 | 6515 | 5 | 0.8 s |
| iqb/2018MgrundlegendBStochastikCAS.pdf | erfasst | 3 | 4675 | 3 | 0.4 s |
| iqb/2018MgrundlegendBStochastikWTR1.pdf | erfasst | 3 | 5058 | 3 | 0.4 s |
| iqb/2018MgrundlegendBStochastikWTR2.pdf | erfasst | 3 | 4717 | 3 | 0.4 s |
| iqb/2018MgrundlegendBStochastikWTR3.pdf | erfasst | 4 | 5346 | 4 | 0.5 s |
| iqb/2019MerhoehtAAGLAA11.pdf | erfasst | 2 | 2805 | 2 | 0.3 s |
| iqb/2019MerhoehtAAGLAA12.pdf | erfasst | 2 | 2212 | 2 | 0.2 s |
| iqb/2019MerhoehtAAGLAA21.pdf | erfasst | 2 | 2036 | 2 | 0.2 s |
| iqb/2019MerhoehtAAGLAA22.pdf | erfasst | 2 | 2049 | 2 | 0.2 s |
| iqb/2019MerhoehtAAnalysis11.pdf | erfasst | 2 | 2032 | 2 | 0.2 s |
| iqb/2019MerhoehtAAnalysis12.pdf | erfasst | 2 | 2193 | 2 | 0.2 s |
| iqb/2019MerhoehtAAnalysis2.pdf | erfasst | 2 | 2130 | 2 | 0.2 s |
| iqb/2019MerhoehtAStochastik11.pdf | erfasst | 2 | 2018 | 2 | 0.2 s |
| iqb/2019MerhoehtAStochastik12.pdf | erfasst | 2 | 2007 | 2 | 0.2 s |
| iqb/2019MerhoehtAStochastik2.pdf | erfasst | 2 | 2221 | 2 | 0.2 s |
| iqb/2019MerhoehtBAGLAA1CAS.pdf | erfasst | 5 | 6839 | 5 | 0.6 s |
| iqb/2019MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 6633 | 4 | 0.5 s |
| iqb/2019MerhoehtBAGLAA2CAS1.pdf | erfasst | 4 | 6325 | 4 | 0.5 s |
| iqb/2019MerhoehtBAGLAA2CAS2.pdf | erfasst | 4 | 4605 | 4 | 0.5 s |
| iqb/2019MerhoehtBAGLAA2WTR1.pdf | erfasst | 4 | 4429 | 4 | 0.5 s |
| iqb/2019MerhoehtBAGLAA2WTR2.pdf | erfasst | 4 | 5570 | 4 | 0.5 s |
| iqb/2019MerhoehtBAGLAA2WTR3.pdf | erfasst | 4 | 5086 | 4 | 0.5 s |
| iqb/2019MerhoehtBAnalysisCAS1.pdf | erfasst | 6 | 10458 | 6 | 0.9 s |
| iqb/2019MerhoehtBAnalysisCAS2.pdf | erfasst | 5 | 8077 | 5 | 0.8 s |
| iqb/2019MerhoehtBAnalysisWTR1.pdf | erfasst | 5 | 7223 | 5 | 0.7 s |
| iqb/2019MerhoehtBAnalysisWTR2.pdf | erfasst | 5 | 6668 | 5 | 0.7 s |
| iqb/2019MerhoehtBAnalysisWTR3.pdf | erfasst | 5 | 7361 | 5 | 0.7 s |
| iqb/2019MerhoehtBStochastikCAS1.pdf | erfasst | 4 | 5514 | 4 | 0.5 s |
| iqb/2019MerhoehtBStochastikCAS2.pdf | erfasst | 4 | 6831 | 4 | 0.5 s |
| iqb/2019MerhoehtBStochastikWTR1.pdf | erfasst | 4 | 5475 | 4 | 0.5 s |
| iqb/2019MerhoehtBStochastikWTR2.pdf | erfasst | 4 | 6853 | 4 | 0.6 s |
| iqb/2019MerhoehtBStochastikWTR3.pdf | erfasst | 4 | 5049 | 4 | 0.6 s |
| iqb/2019MgrundlegendAAGLAA11.pdf | erfasst | 2 | 2266 | 2 | 0.2 s |
| iqb/2019MgrundlegendAAGLAA12.pdf | erfasst | 2 | 2502 | 2 | 0.2 s |
| iqb/2019MgrundlegendAAGLAA211.pdf | erfasst | 2 | 1935 | 2 | 0.2 s |
| iqb/2019MgrundlegendAAGLAA212.pdf | erfasst | 2 | 1995 | 2 | 0.2 s |
| iqb/2019MgrundlegendAAGLAA22.pdf | erfasst | 2 | 2297 | 2 | 0.2 s |
| iqb/2019MgrundlegendAAnalysis11.pdf | erfasst | 2 | 1956 | 2 | 0.2 s |
| iqb/2019MgrundlegendAAnalysis12.pdf | erfasst | 2 | 1951 | 2 | 0.2 s |
| iqb/2019MgrundlegendAAnalysis2.pdf | erfasst | 2 | 2144 | 2 | 0.2 s |
| iqb/2019MgrundlegendAStochastik11.pdf | erfasst | 2 | 2454 | 2 | 0.3 s |
| iqb/2019MgrundlegendAStochastik12.pdf | erfasst | 2 | 2304 | 2 | 0.2 s |
| iqb/2019MgrundlegendAStochastik2.pdf | erfasst | 2 | 2307 | 2 | 0.3 s |
| iqb/2019MgrundlegendBAGLAA1CAS.pdf | erfasst | 5 | 6376 | 5 | 0.6 s |
| iqb/2019MgrundlegendBAGLAA1WTR.pdf | erfasst | 4 | 5204 | 4 | 0.4 s |
| iqb/2019MgrundlegendBAGLAA2CAS1.pdf | erfasst | 4 | 5675 | 4 | 0.5 s |
| iqb/2019MgrundlegendBAGLAA2CAS2.pdf | erfasst | 4 | 5265 | 4 | 0.6 s |
| iqb/2019MgrundlegendBAGLAA2WTR1.pdf | erfasst | 3 | 3906 | 3 | 0.6 s |
| iqb/2019MgrundlegendBAGLAA2WTR2.pdf | erfasst | 4 | 4908 | 4 | 0.5 s |
| iqb/2019MgrundlegendBAnalysisCAS.pdf | erfasst | 6 | 8571 | 6 | 0.9 s |
| iqb/2019MgrundlegendBAnalysisWTR1.pdf | erfasst | 5 | 7187 | 5 | 0.8 s |
| iqb/2019MgrundlegendBAnalysisWTR2.pdf | erfasst | 4 | 6442 | 4 | 0.7 s |
| iqb/2019MgrundlegendBStochastikCAS1.pdf | erfasst | 3 | 4691 | 3 | 0.4 s |
| iqb/2019MgrundlegendBStochastikCAS2.pdf | erfasst | 3 | 4436 | 3 | 0.4 s |
| iqb/2019MgrundlegendBStochastikWTR1.pdf | erfasst | 3 | 4393 | 3 | 0.4 s |
| iqb/2019MgrundlegendBStochastikWTR2.pdf | erfasst | 3 | 4134 | 3 | 0.5 s |
| iqb/2019MgrundlegendBStochastikWTR3.pdf | erfasst | 3 | 4934 | 3 | 0.4 s |
| iqb/2020MerhoehtAAGLAA11.pdf | erfasst | 2 | 2755 | 2 | 0.3 s |
| iqb/2020MerhoehtAAGLAA12.pdf | erfasst | 2 | 2078 | 2 | 0.2 s |
| iqb/2020MerhoehtAAGLAA211.pdf | erfasst | 2 | 2243 | 2 | 0.3 s |
| iqb/2020MerhoehtAAGLAA212.pdf | erfasst | 2 | 2195 | 2 | 0.2 s |
| iqb/2020MerhoehtAAGLAA22.pdf | erfasst | 2 | 2354 | 2 | 0.2 s |
| iqb/2020MerhoehtAAnalysis11.pdf | erfasst | 2 | 2074 | 2 | 0.2 s |
| iqb/2020MerhoehtAAnalysis12.pdf | erfasst | 2 | 2070 | 2 | 0.3 s |
| iqb/2020MerhoehtAAnalysis13.pdf | erfasst | 2 | 2321 | 2 | 0.2 s |
| iqb/2020MerhoehtAAnalysis21.pdf | erfasst | 2 | 2189 | 2 | 0.2 s |
| iqb/2020MerhoehtAAnalysis22.pdf | erfasst | 2 | 1802 | 2 | 0.3 s |
| iqb/2020MerhoehtAStochastik11.pdf | erfasst | 2 | 2359 | 2 | 0.3 s |
| iqb/2020MerhoehtAStochastik12.pdf | erfasst | 2 | 2461 | 2 | 0.2 s |
| iqb/2020MerhoehtAStochastik13.pdf | erfasst | 2 | 2053 | 2 | 0.2 s |
| iqb/2020MerhoehtAStochastik21.pdf | erfasst | 2 | 2478 | 2 | 0.4 s |
| iqb/2020MerhoehtAStochastik22.pdf | erfasst | 2 | 2533 | 2 | 0.3 s |
| iqb/2020MerhoehtBAGLAA1CAS.pdf | erfasst | 4 | 5325 | 4 | 0.5 s |
| iqb/2020MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 6140 | 4 | 0.6 s |
| iqb/2020MerhoehtBAGLAA2CAS1.pdf | erfasst | 4 | 5412 | 4 | 0.5 s |
| iqb/2020MerhoehtBAGLAA2CAS2.pdf | erfasst | 3 | 3949 | 3 | 0.5 s |
| iqb/2020MerhoehtBAGLAA2WTR1.pdf | erfasst | 4 | 5315 | 4 | 0.5 s |
| iqb/2020MerhoehtBAGLAA2WTR2.pdf | erfasst | 4 | 5070 | 4 | 0.7 s |
| iqb/2020MerhoehtBAnalysisCAS1.pdf | erfasst | 4 | 7359 | 4 | 0.7 s |
| iqb/2020MerhoehtBAnalysisCAS2.pdf | erfasst | 5 | 8197 | 5 | 0.7 s |
| iqb/2020MerhoehtBAnalysisWTR1.pdf | erfasst | 4 | 7188 | 4 | 0.6 s |
| iqb/2020MerhoehtBAnalysisWTR2.pdf | erfasst | 5 | 7410 | 5 | 0.7 s |
| iqb/2020MerhoehtBAnalysisWTR3.pdf | erfasst | 5 | 6782 | 5 | 1.0 s |
| iqb/2020MerhoehtBStochastikCAS1.pdf | erfasst | 3 | 5273 | 3 | 0.5 s |
| iqb/2020MerhoehtBStochastikCAS2.pdf | erfasst | 4 | 6700 | 4 | 0.5 s |
| iqb/2020MerhoehtBStochastikWTR1.pdf | erfasst | 3 | 5300 | 3 | 0.5 s |
| iqb/2020MerhoehtBStochastikWTR2.pdf | erfasst | 4 | 5646 | 4 | 0.6 s |
| iqb/2020MgrundlegendAAGLAA111.pdf | erfasst | 2 | 2470 | 2 | 0.2 s |
| iqb/2020MgrundlegendAAGLAA112.pdf | erfasst | 2 | 1962 | 2 | 0.2 s |
| iqb/2020MgrundlegendAAGLAA12.pdf | erfasst | 2 | 1974 | 2 | 0.2 s |
| iqb/2020MgrundlegendAAGLAA211.pdf | erfasst | 2 | 2206 | 2 | 0.2 s |
| iqb/2020MgrundlegendAAGLAA212.pdf | erfasst | 2 | 2052 | 2 | 0.2 s |
| iqb/2020MgrundlegendAAnalysis11.pdf | erfasst | 2 | 1928 | 2 | 0.2 s |
| iqb/2020MgrundlegendAAnalysis12.pdf | erfasst | 2 | 1850 | 2 | 0.2 s |
| iqb/2020MgrundlegendAStochastik11.pdf | erfasst | 2 | 2154 | 2 | 0.3 s |
| iqb/2020MgrundlegendAStochastik12.pdf | erfasst | 2 | 1995 | 2 | 0.3 s |
| iqb/2020MgrundlegendAStochastik2.pdf | erfasst | 2 | 2027 | 2 | 0.2 s |
| iqb/2020MgrundlegendBAGLAA1CAS.pdf | erfasst | 4 | 5477 | 4 | 0.5 s |
| iqb/2020MgrundlegendBAGLAA1WTR.pdf | erfasst | 4 | 5199 | 4 | 0.5 s |
| iqb/2020MgrundlegendBAGLAA2CAS1.pdf | erfasst | 3 | 4540 | 3 | 0.5 s |
| iqb/2020MgrundlegendBAGLAA2CAS2.pdf | erfasst | 3 | 3853 | 3 | 0.4 s |
| iqb/2020MgrundlegendBAGLAA2WTR.pdf | erfasst | 3 | 4454 | 3 | 0.4 s |
| iqb/2020MgrundlegendBAnalysisCAS1.pdf | erfasst | 4 | 5394 | 4 | 0.5 s |
| iqb/2020MgrundlegendBAnalysisCAS2.pdf | erfasst | 4 | 5255 | 4 | 0.6 s |
| iqb/2020MgrundlegendBAnalysisWTR1.pdf | erfasst | 4 | 5841 | 4 | 0.6 s |
| iqb/2020MgrundlegendBAnalysisWTR2.pdf | erfasst | 4 | 5427 | 4 | 0.6 s |
| iqb/2020MgrundlegendBStochastikCAS1.pdf | erfasst | 3 | 4099 | 3 | 0.4 s |
| iqb/2020MgrundlegendBStochastikCAS2.pdf | erfasst | 3 | 4650 | 3 | 0.4 s |
| iqb/2020MgrundlegendBStochastikWTR1.pdf | erfasst | 3 | 4134 | 3 | 0.3 s |
| iqb/2020MgrundlegendBStochastikWTR2.pdf | erfasst | 4 | 5976 | 4 | 0.5 s |
| iqb/2021MerhoehtAAGLAA111.pdf | erfasst | 2 | 1972 | 2 | 0.2 s |
| iqb/2021MerhoehtAAGLAA112.pdf | erfasst | 2 | 2065 | 2 | 0.2 s |
| iqb/2021MerhoehtAAGLAA113.pdf | erfasst | 2 | 2508 | 2 | 0.3 s |
| iqb/2021MerhoehtAAGLAA121.pdf | erfasst | 2 | 2084 | 2 | 0.2 s |
| iqb/2021MerhoehtAAGLAA122.pdf | erfasst | 2 | 2004 | 2 | 0.2 s |
| iqb/2021MerhoehtAAGLAA211.pdf | erfasst | 2 | 2027 | 2 | 0.2 s |
| iqb/2021MerhoehtAAGLAA212.pdf | erfasst | 2 | 2065 | 2 | 0.2 s |
| iqb/2021MerhoehtAAGLAA213.pdf | erfasst | 2 | 2139 | 2 | 0.2 s |
| iqb/2021MerhoehtAAGLAA22.pdf | erfasst | 2 | 2082 | 2 | 0.2 s |
| iqb/2021MerhoehtAAnalysis11.pdf | erfasst | 2 | 2019 | 2 | 0.3 s |
| iqb/2021MerhoehtAAnalysis12.pdf | erfasst | 2 | 2029 | 2 | 0.2 s |
| iqb/2021MerhoehtAAnalysis13.pdf | erfasst | 2 | 2475 | 2 | 0.2 s |
| iqb/2021MerhoehtAAnalysis21.pdf | erfasst | 2 | 2263 | 2 | 0.2 s |
| iqb/2021MerhoehtAAnalysis22.pdf | erfasst | 2 | 2166 | 2 | 0.3 s |
| iqb/2021MerhoehtAStochastik11.pdf | erfasst | 2 | 2049 | 2 | 0.2 s |
| iqb/2021MerhoehtAStochastik12.pdf | erfasst | 2 | 1964 | 2 | 0.2 s |
| iqb/2021MerhoehtAStochastik13.pdf | erfasst | 2 | 2379 | 2 | 0.2 s |
| iqb/2021MerhoehtAStochastik21.pdf | erfasst | 2 | 2418 | 2 | 0.3 s |
| iqb/2021MerhoehtAStochastik22.pdf | erfasst | 2 | 2833 | 2 | 0.3 s |
| iqb/2021MerhoehtBAGLAA1CAS.pdf | erfasst | 5 | 7202 | 5 | 0.6 s |
| iqb/2021MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 6861 | 4 | 0.6 s |
| iqb/2021MerhoehtBAGLAA2CAS.pdf | erfasst | 3 | 4569 | 3 | 0.4 s |
| iqb/2021MerhoehtBAGLAA2WTR.pdf | erfasst | 3 | 4147 | 3 | 0.4 s |
| iqb/2021MerhoehtBAnalysisCAS.pdf | erfasst | 5 | 7339 | 5 | 0.6 s |
| iqb/2021MerhoehtBAnalysisWTR1.pdf | erfasst | 4 | 7157 | 4 | 0.6 s |
| iqb/2021MerhoehtBAnalysisWTR2.pdf | erfasst | 4 | 5431 | 4 | 0.5 s |
| iqb/2021MerhoehtBStochastikCAS1.pdf | erfasst | 4 | 5604 | 4 | 0.5 s |
| iqb/2021MerhoehtBStochastikCAS2.pdf | erfasst | 3 | 4809 | 3 | 0.5 s |
| iqb/2021MerhoehtBStochastikWTR.pdf | erfasst | 4 | 5635 | 4 | 0.4 s |
| iqb/2021MgrundlegendAAGLAA111.pdf | erfasst | 3 | 2709 | 3 | 0.3 s |
| iqb/2021MgrundlegendAAGLAA112.pdf | erfasst | 2 | 1939 | 2 | 0.2 s |
| iqb/2021MgrundlegendAAGLAA12.pdf | erfasst | 2 | 2176 | 2 | 0.2 s |
| iqb/2021MgrundlegendAAGLAA211.pdf | erfasst | 2 | 2080 | 2 | 0.2 s |
| iqb/2021MgrundlegendAAGLAA212.pdf | erfasst | 2 | 1939 | 2 | 0.2 s |
| iqb/2021MgrundlegendAAGLAA22.pdf | erfasst | 2 | 2176 | 2 | 0.2 s |
| iqb/2021MgrundlegendAAnalysis11.pdf | erfasst | 2 | 2136 | 2 | 0.2 s |
| iqb/2021MgrundlegendAAnalysis12.pdf | erfasst | 2 | 2076 | 2 | 0.2 s |
| iqb/2021MgrundlegendAAnalysis13.pdf | erfasst | 2 | 1923 | 2 | 0.2 s |
| iqb/2021MgrundlegendAAnalysis2.pdf | erfasst | 2 | 1935 | 2 | 0.2 s |
| iqb/2021MgrundlegendAStochastik11.pdf | erfasst | 2 | 2340 | 2 | 0.2 s |
| iqb/2021MgrundlegendAStochastik12.pdf | erfasst | 2 | 2481 | 2 | 0.2 s |
| iqb/2021MgrundlegendAStochastik2.pdf | erfasst | 2 | 2251 | 2 | 0.2 s |
| iqb/2021MgrundlegendBAGLAA1WTR.pdf | erfasst | 3 | 5384 | 3 | 0.5 s |
| iqb/2021MgrundlegendBAGLAA2CAS1.pdf | erfasst | 3 | 3762 | 3 | 0.4 s |
| iqb/2021MgrundlegendBAGLAA2CAS2.pdf | erfasst | 3 | 3662 | 3 | 0.4 s |
| iqb/2021MgrundlegendBAGLAA2WTR1.pdf | erfasst | 3 | 3824 | 3 | 0.4 s |
| iqb/2021MgrundlegendBAGLAA2WTR2.pdf | erfasst | 3 | 4467 | 3 | 0.4 s |
| iqb/2021MgrundlegendBAnalysisCAS.pdf | erfasst | 4 | 5855 | 4 | 0.6 s |
| iqb/2021MgrundlegendBAnalysisWTR.pdf | erfasst | 4 | 5173 | 4 | 0.6 s |
| iqb/2021MgrundlegendBStochastikCAS1.pdf | erfasst | 3 | 4263 | 3 | 0.3 s |
| iqb/2021MgrundlegendBStochastikCAS2.pdf | erfasst | 3 | 4443 | 3 | 0.3 s |
| iqb/2021MgrundlegendBStochastikWTR1.pdf | erfasst | 3 | 4604 | 3 | 0.4 s |
| iqb/2021MgrundlegendBStochastikWTR2.pdf | erfasst | 3 | 4444 | 3 | 0.4 s |
| iqb/2021MgrundlegendBStochastikWTR3.pdf | erfasst | 3 | 4968 | 3 | 0.4 s |
| iqb/2022MerhoehtAAGLAA111.pdf | erfasst | 3 | 2939 | 3 | 0.3 s |
| iqb/2022MerhoehtAAGLAA112.pdf | erfasst | 2 | 2105 | 2 | 0.2 s |
| iqb/2022MerhoehtAAGLAA12.pdf | erfasst | 2 | 2453 | 2 | 0.2 s |
| iqb/2022MerhoehtAAGLAA211.pdf | erfasst | 2 | 2288 | 2 | 0.2 s |
| iqb/2022MerhoehtAAGLAA212.pdf | erfasst | 2 | 2293 | 2 | 0.2 s |
| iqb/2022MerhoehtAAGLAA213.pdf | erfasst | 2 | 2059 | 2 | 0.2 s |
| iqb/2022MerhoehtAAGLAA221.pdf | erfasst | 2 | 2250 | 2 | 0.2 s |
| iqb/2022MerhoehtAAGLAA222.pdf | erfasst | 2 | 2453 | 2 | 0.3 s |
| iqb/2022MerhoehtAAnalysis11.pdf | erfasst | 2 | 1997 | 2 | 0.2 s |
| iqb/2022MerhoehtAAnalysis12.pdf | erfasst | 2 | 2096 | 2 | 0.2 s |
| iqb/2022MerhoehtAAnalysis13.pdf | erfasst | 2 | 2240 | 2 | 0.2 s |
| iqb/2022MerhoehtAAnalysis2.pdf | erfasst | 2 | 2050 | 2 | 0.2 s |
| iqb/2022MerhoehtAStochastik11.pdf | erfasst | 2 | 2816 | 2 | 0.2 s |
| iqb/2022MerhoehtAStochastik12.pdf | erfasst | 3 | 3259 | 3 | 0.3 s |
| iqb/2022MerhoehtAStochastik13.pdf | erfasst | 2 | 2212 | 2 | 0.3 s |
| iqb/2022MerhoehtAStochastik21.pdf | erfasst | 2 | 2518 | 2 | 0.2 s |
| iqb/2022MerhoehtAStochastik22.pdf | erfasst | 2 | 2391 | 2 | 0.2 s |
| iqb/2022MerhoehtBAGLAA1MMS.pdf | erfasst | 4 | 5852 | 4 | 0.5 s |
| iqb/2022MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 5673 | 4 | 0.5 s |
| iqb/2022MerhoehtBAGLAA2MMS1.pdf | erfasst | 4 | 6366 | 4 | 0.5 s |
| iqb/2022MerhoehtBAGLAA2MMS2.pdf | erfasst | 4 | 4970 | 4 | 0.5 s |
| iqb/2022MerhoehtBAGLAA2WTR1.pdf | erfasst | 4 | 4735 | 4 | 0.5 s |
| iqb/2022MerhoehtBAGLAA2WTR2.pdf | erfasst | 4 | 5141 | 4 | 0.5 s |
| iqb/2022MerhoehtBAnalysisMMS1.pdf | erfasst | 5 | 7915 | 5 | 0.7 s |
| iqb/2022MerhoehtBAnalysisMMS2.pdf | erfasst | 5 | 6762 | 5 | 0.8 s |
| iqb/2022MerhoehtBAnalysisWTR1.pdf | erfasst | 5 | 8086 | 5 | 0.6 s |
| iqb/2022MerhoehtBAnalysisWTR2.pdf | erfasst | 5 | 6531 | 5 | 0.6 s |
| iqb/2022MerhoehtBAnalysisWTR3.pdf | erfasst | 4 | 6720 | 4 | 0.6 s |
| iqb/2022MerhoehtBStochastikMMS1.pdf | erfasst | 4 | 5783 | 4 | 0.6 s |
| iqb/2022MerhoehtBStochastikMMS2.pdf | erfasst | 4 | 5266 | 4 | 0.4 s |
| iqb/2022MerhoehtBStochastikMMS3.pdf | erfasst | 4 | 5796 | 4 | 0.5 s |
| iqb/2022MerhoehtBStochastikWTR1.pdf | erfasst | 4 | 5783 | 4 | 0.5 s |
| iqb/2022MerhoehtBStochastikWTR2.pdf | erfasst | 4 | 5266 | 4 | 0.5 s |
| iqb/2022MgrundlegendAAGLAA11.pdf | erfasst | 2 | 2809 | 2 | 0.2 s |
| iqb/2022MgrundlegendAAGLAA12.pdf | erfasst | 2 | 2042 | 2 | 0.2 s |
| iqb/2022MgrundlegendAAGLAA211.pdf | erfasst | 2 | 2031 | 2 | 0.2 s |
| iqb/2022MgrundlegendAAGLAA212.pdf | erfasst | 2 | 2075 | 2 | 0.2 s |
| iqb/2022MgrundlegendAAGLAA213.pdf | erfasst | 2 | 2207 | 2 | 0.2 s |
| iqb/2022MgrundlegendAAGLAA22.pdf | erfasst | 2 | 2128 | 2 | 0.2 s |
| iqb/2022MgrundlegendAAnalysis11.pdf | erfasst | 2 | 2210 | 2 | 0.2 s |
| iqb/2022MgrundlegendAAnalysis12.pdf | erfasst | 2 | 2064 | 2 | 0.2 s |
| iqb/2022MgrundlegendAAnalysis13.pdf | erfasst | 2 | 2130 | 2 | 0.2 s |
| iqb/2022MgrundlegendAAnalysis2.pdf | erfasst | 2 | 1915 | 2 | 0.2 s |
| iqb/2022MgrundlegendAStochastik11.pdf | erfasst | 2 | 2677 | 2 | 0.2 s |
| iqb/2022MgrundlegendAStochastik12.pdf | erfasst | 2 | 2098 | 2 | 0.2 s |
| iqb/2022MgrundlegendAStochastik13.pdf | erfasst | 2 | 2263 | 2 | 0.2 s |
| iqb/2022MgrundlegendAStochastik2.pdf | erfasst | 2 | 2421 | 2 | 0.2 s |
| iqb/2022MgrundlegendBAGLAA1WTR.pdf | erfasst | 4 | 5232 | 4 | 0.4 s |
| iqb/2022MgrundlegendBAGLAA2MMS1.pdf | erfasst | 3 | 3984 | 3 | 0.4 s |
| iqb/2022MgrundlegendBAGLAA2MMS2.pdf | erfasst | 3 | 4397 | 3 | 0.4 s |
| iqb/2022MgrundlegendBAGLAA2WTR1.pdf | erfasst | 3 | 4799 | 3 | 0.4 s |
| iqb/2022MgrundlegendBAGLAA2WTR2.pdf | erfasst | 3 | 4700 | 3 | 0.4 s |
| iqb/2022MgrundlegendBAnalysisMMS1.pdf | erfasst | 4 | 6168 | 4 | 0.5 s |
| iqb/2022MgrundlegendBAnalysisMMS2.pdf | erfasst | 4 | 6614 | 4 | 0.5 s |
| iqb/2022MgrundlegendBAnalysisWTR1.pdf | erfasst | 4 | 5912 | 4 | 0.5 s |
| iqb/2022MgrundlegendBAnalysisWTR2.pdf | erfasst | 4 | 5801 | 4 | 0.5 s |
| iqb/2022MgrundlegendBStochastikMMS1.pdf | erfasst | 3 | 4799 | 3 | 0.4 s |
| iqb/2022MgrundlegendBStochastikMMS2.pdf | erfasst | 3 | 4885 | 3 | 0.4 s |
| iqb/2022MgrundlegendBStochastikWTR1.pdf | erfasst | 3 | 4802 | 3 | 0.4 s |
| iqb/2022MgrundlegendBStochastikWTR2.pdf | erfasst | 4 | 5321 | 4 | 0.4 s |
| iqb/2023MerhoehtAAGLAA111.pdf | erfasst | 2 | 1967 | 2 | 0.2 s |
| iqb/2023MerhoehtAAGLAA112.pdf | erfasst | 3 | 2992 | 3 | 0.3 s |
| iqb/2023MerhoehtAAGLAA12.pdf | erfasst | 2 | 2639 | 2 | 0.2 s |
| iqb/2023MerhoehtAAGLAA211.pdf | erfasst | 2 | 1885 | 2 | 0.2 s |
| iqb/2023MerhoehtAAGLAA212.pdf | erfasst | 2 | 2119 | 2 | 0.2 s |
| iqb/2023MerhoehtAAGLAA213.pdf | erfasst | 2 | 2166 | 2 | 0.2 s |
| iqb/2023MerhoehtAAGLAA221.pdf | erfasst | 2 | 2186 | 2 | 0.2 s |
| iqb/2023MerhoehtAAGLAA222.pdf | erfasst | 2 | 2222 | 2 | 0.2 s |
| iqb/2023MerhoehtAAnalysis11.pdf | erfasst | 2 | 2019 | 2 | 0.2 s |
| iqb/2023MerhoehtAAnalysis12.pdf | erfasst | 2 | 2217 | 2 | 0.2 s |
| iqb/2023MerhoehtAAnalysis13.pdf | erfasst | 2 | 2448 | 2 | 0.2 s |
| iqb/2023MerhoehtAAnalysis21.pdf | erfasst | 2 | 1906 | 2 | 0.2 s |
| iqb/2023MerhoehtAAnalysis22.pdf | erfasst | 2 | 1782 | 2 | 0.2 s |
| iqb/2023MerhoehtAStochastik11.pdf | erfasst | 2 | 2240 | 2 | 0.2 s |
| iqb/2023MerhoehtAStochastik12.pdf | erfasst | 2 | 2279 | 2 | 0.2 s |
| iqb/2023MerhoehtAStochastik13.pdf | erfasst | 2 | 2596 | 2 | 0.2 s |
| iqb/2023MerhoehtAStochastik21.pdf | erfasst | 2 | 2156 | 2 | 0.2 s |
| iqb/2023MerhoehtAStochastik22.pdf | erfasst | 2 | 2197 | 2 | 0.2 s |
| iqb/2023MerhoehtBAGLAA1MMS.pdf | erfasst | 4 | 5763 | 4 | 0.7 s |
| iqb/2023MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 6009 | 4 | 0.6 s |
| iqb/2023MerhoehtBAGLAA2MMS1.pdf | erfasst | 4 | 5552 | 4 | 0.5 s |
| iqb/2023MerhoehtBAGLAA2MMS2.pdf | erfasst | 4 | 4715 | 4 | 0.4 s |
| iqb/2023MerhoehtBAGLAA2WTR1.pdf | erfasst | 4 | 5632 | 4 | 0.5 s |
| iqb/2023MerhoehtBAGLAA2WTR2.pdf | erfasst | 4 | 4505 | 4 | 0.5 s |
| iqb/2023MerhoehtBAnalysisMMS1.pdf | erfasst | 5 | 7539 | 5 | 0.7 s |
| iqb/2023MerhoehtBAnalysisMMS2.pdf | erfasst | 4 | 6595 | 4 | 0.6 s |
| iqb/2023MerhoehtBAnalysisWTR1.pdf | erfasst | 5 | 7390 | 5 | 0.6 s |
| iqb/2023MerhoehtBAnalysisWTR2.pdf | erfasst | 4 | 6167 | 4 | 0.5 s |
| iqb/2023MerhoehtBStochastikMMS1.pdf | erfasst | 4 | 6220 | 4 | 0.5 s |
| iqb/2023MerhoehtBStochastikMMS2.pdf | erfasst | 4 | 7394 | 4 | 0.5 s |
| iqb/2023MerhoehtBStochastikWTR1.pdf | erfasst | 4 | 6237 | 4 | 0.5 s |
| iqb/2023MerhoehtBStochastikWTR2.pdf | erfasst | 4 | 7394 | 4 | 0.5 s |
| iqb/2023MerhoehtBStochastikWTR3.pdf | erfasst | 4 | 5939 | 4 | 0.5 s |
| iqb/2023MgrundlegendAAGLAA111.pdf | erfasst | 2 | 2222 | 2 | 0.2 s |
| iqb/2023MgrundlegendAAGLAA112.pdf | erfasst | 2 | 2224 | 2 | 0.2 s |
| iqb/2023MgrundlegendAAGLAA12.pdf | erfasst | 2 | 2157 | 2 | 0.2 s |
| iqb/2023MgrundlegendAAGLAA211.pdf | erfasst | 2 | 2222 | 2 | 0.2 s |
| iqb/2023MgrundlegendAAGLAA212.pdf | erfasst | 2 | 2060 | 2 | 0.2 s |
| iqb/2023MgrundlegendAAGLAA213.pdf | erfasst | 2 | 2399 | 2 | 0.2 s |
| iqb/2023MgrundlegendAAGLAA22.pdf | erfasst | 2 | 2338 | 2 | 0.2 s |
| iqb/2023MgrundlegendAAnalysis11.pdf | erfasst | 2 | 1989 | 2 | 0.2 s |
| iqb/2023MgrundlegendAAnalysis12.pdf | erfasst | 2 | 2207 | 2 | 0.2 s |
| iqb/2023MgrundlegendAAnalysis13.pdf | erfasst | 2 | 2094 | 2 | 0.3 s |
| iqb/2023MgrundlegendAAnalysis2.pdf | erfasst | 2 | 1894 | 2 | 0.2 s |
| iqb/2023MgrundlegendAStochastik11.pdf | erfasst | 2 | 2037 | 2 | 0.2 s |
| iqb/2023MgrundlegendAStochastik12.pdf | erfasst | 2 | 2545 | 2 | 0.2 s |
| iqb/2023MgrundlegendAStochastik2.pdf | erfasst | 2 | 2215 | 2 | 0.2 s |
| iqb/2023MgrundlegendBAGLAA1MMS.pdf | erfasst | 3 | 4872 | 3 | 0.4 s |
| iqb/2023MgrundlegendBAGLAA1WTR.pdf | erfasst | 4 | 5412 | 4 | 0.6 s |
| iqb/2023MgrundlegendBAGLAA2MMS1.pdf | erfasst | 3 | 4603 | 3 | 0.4 s |
| iqb/2023MgrundlegendBAGLAA2MMS2.pdf | erfasst | 3 | 3830 | 3 | 0.4 s |
| iqb/2023MgrundlegendBAGLAA2WTR1.pdf | erfasst | 4 | 4596 | 4 | 0.4 s |
| iqb/2023MgrundlegendBAGLAA2WTR2.pdf | erfasst | 4 | 4372 | 4 | 0.6 s |
| iqb/2023MgrundlegendBAnalysisMMS1.pdf | erfasst | 4 | 6199 | 4 | 0.6 s |
| iqb/2023MgrundlegendBAnalysisMMS2.pdf | erfasst | 5 | 7264 | 5 | 0.6 s |
| iqb/2023MgrundlegendBAnalysisWTR1.pdf | erfasst | 4 | 5614 | 4 | 0.6 s |
| iqb/2023MgrundlegendBAnalysisWTR2.pdf | erfasst | 4 | 6206 | 4 | 0.5 s |
| iqb/2023MgrundlegendBStochastikMMS1.pdf | erfasst | 3 | 5044 | 3 | 0.4 s |
| iqb/2023MgrundlegendBStochastikMMS2.pdf | erfasst | 3 | 4162 | 3 | 0.4 s |
| iqb/2023MgrundlegendBStochastikWTR1.pdf | erfasst | 3 | 5044 | 3 | 0.4 s |
| iqb/2023MgrundlegendBStochastikWTR2.pdf | erfasst | 3 | 4164 | 3 | 0.4 s |
| iqb/2023MgrundlegendBStochastikWTR3.pdf | erfasst | 3 | 4697 | 3 | 0.4 s |
| iqb/2024MerhoehtAAGLAA11.pdf | erfasst | 3 | 2713 | 3 | 0.3 s |
| iqb/2024MerhoehtAAGLAA121.pdf | erfasst | 2 | 2223 | 2 | 0.2 s |
| iqb/2024MerhoehtAAGLAA122.pdf | erfasst | 2 | 2540 | 2 | 0.2 s |
| iqb/2024MerhoehtAAGLAA211.pdf | erfasst | 3 | 2263 | 3 | 0.3 s |
| iqb/2024MerhoehtAAGLAA212.pdf | erfasst | 2 | 2029 | 2 | 0.2 s |
| iqb/2024MerhoehtAAGLAA221.pdf | erfasst | 2 | 2147 | 2 | 0.2 s |
| iqb/2024MerhoehtAAGLAA222.pdf | erfasst | 2 | 1976 | 2 | 0.2 s |
| iqb/2024MerhoehtAAGLAA223.pdf | erfasst | 2 | 2292 | 2 | 0.2 s |
| iqb/2024MerhoehtAAnalysis11.pdf | erfasst | 2 | 2251 | 2 | 0.3 s |
| iqb/2024MerhoehtAAnalysis12.pdf | erfasst | 2 | 1842 | 2 | 0.2 s |
| iqb/2024MerhoehtAAnalysis13.pdf | erfasst | 2 | 2107 | 2 | 0.2 s |
| iqb/2024MerhoehtAAnalysis21.pdf | erfasst | 2 | 2022 | 2 | 0.3 s |
| iqb/2024MerhoehtAAnalysis22.pdf | erfasst | 2 | 2242 | 2 | 0.2 s |
| iqb/2024MerhoehtAAnalysis23.pdf | erfasst | 2 | 2129 | 2 | 0.2 s |
| iqb/2024MerhoehtAStochastik11.pdf | erfasst | 2 | 2368 | 2 | 0.2 s |
| iqb/2024MerhoehtAStochastik12.pdf | erfasst | 2 | 2312 | 2 | 0.2 s |
| iqb/2024MerhoehtAStochastik21.pdf | erfasst | 2 | 2453 | 2 | 0.2 s |
| iqb/2024MerhoehtAStochastik22.pdf | erfasst | 2 | 2444 | 2 | 0.2 s |
| iqb/2024MerhoehtAStochastik23.pdf | erfasst | 3 | 2952 | 3 | 0.3 s |
| iqb/2024MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 5398 | 4 | 0.5 s |
| iqb/2024MerhoehtBAGLAA2MMS1.pdf | erfasst | 4 | 5567 | 4 | 0.5 s |
| iqb/2024MerhoehtBAGLAA2MMS2.pdf | erfasst | 4 | 7082 | 4 | 0.5 s |
| iqb/2024MerhoehtBAGLAA2WTR1.pdf | erfasst | 4 | 5603 | 4 | 0.5 s |
| iqb/2024MerhoehtBAnalysisMMS1.pdf | erfasst | 5 | 8861 | 5 | 0.7 s |
| iqb/2024MerhoehtBAnalysisMMS2.pdf | erfasst | 5 | 7397 | 5 | 0.6 s |
| iqb/2024MerhoehtBAnalysisWTR1.pdf | erfasst | 5 | 7259 | 5 | 0.7 s |
| iqb/2024MerhoehtBAnalysisWTR2.pdf | erfasst | 5 | 7476 | 5 | 0.7 s |
| iqb/2024MerhoehtBAnalysisWTR3.pdf | erfasst | 5 | 7784 | 5 | 0.7 s |
| iqb/2024MerhoehtBStochastikMMS1.pdf | erfasst | 4 | 6631 | 4 | 0.6 s |
| iqb/2024MerhoehtBStochastikMMS2.pdf | erfasst | 4 | 6678 | 4 | 0.6 s |
| iqb/2024MerhoehtBStochastikWTR1.pdf | erfasst | 4 | 6631 | 4 | 0.5 s |
| iqb/2024MerhoehtBStochastikWTR2.pdf | erfasst | 4 | 6414 | 4 | 0.6 s |
| iqb/2024MgrundlegendAAGLAA111.pdf | erfasst | 2 | 2218 | 2 | 0.2 s |
| iqb/2024MgrundlegendAAGLAA112.pdf | erfasst | 2 | 1937 | 2 | 0.2 s |
| iqb/2024MgrundlegendAAGLAA12.pdf | erfasst | 2 | 2114 | 2 | 0.2 s |
| iqb/2024MgrundlegendAAGLAA211.pdf | erfasst | 2 | 2138 | 2 | 0.3 s |
| iqb/2024MgrundlegendAAGLAA212.pdf | erfasst | 2 | 1936 | 2 | 0.3 s |
| iqb/2024MgrundlegendAAGLAA213.pdf | erfasst | 2 | 2027 | 2 | 0.2 s |
| iqb/2024MgrundlegendAAGLAA221.pdf | erfasst | 2 | 2010 | 2 | 0.2 s |
| iqb/2024MgrundlegendAAnalysis11.pdf | erfasst | 2 | 2010 | 2 | 0.2 s |
| iqb/2024MgrundlegendAAnalysis12.pdf | erfasst | 2 | 1939 | 2 | 0.2 s |
| iqb/2024MgrundlegendAAnalysis13.pdf | erfasst | 2 | 2039 | 2 | 0.2 s |
| iqb/2024MgrundlegendAAnalysis21.pdf | erfasst | 2 | 1954 | 2 | 0.2 s |
| iqb/2024MgrundlegendAAnalysis22.pdf | erfasst | 2 | 1950 | 2 | 0.2 s |
| iqb/2024MgrundlegendAStochastik11.pdf | erfasst | 2 | 2154 | 2 | 0.2 s |
| iqb/2024MgrundlegendAStochastik12.pdf | erfasst | 2 | 2149 | 2 | 0.2 s |
| iqb/2024MgrundlegendAStochastik13.pdf | erfasst | 2 | 2003 | 2 | 0.2 s |
| iqb/2024MgrundlegendAStochastik21.pdf | erfasst | 2 | 2351 | 2 | 0.2 s |
| iqb/2024MgrundlegendAStochastik22.pdf | erfasst | 3 | 2729 | 3 | 0.3 s |
| iqb/2024MgrundlegendBAGLAA1MMS.pdf | erfasst | 4 | 6197 | 4 | 0.5 s |
| iqb/2024MgrundlegendBAGLAA1WTR.pdf | erfasst | 4 | 6526 | 4 | 0.5 s |
| iqb/2024MgrundlegendBAGLAA2MMS1.pdf | erfasst | 4 | 5927 | 4 | 0.5 s |
| iqb/2024MgrundlegendBAGLAA2MMS2.pdf | erfasst | 4 | 4529 | 4 | 0.6 s |
| iqb/2024MgrundlegendBAGLAA2WTR1.pdf | erfasst | 4 | 5953 | 4 | 0.5 s |
| iqb/2024MgrundlegendBAGLAA2WTR2.pdf | erfasst | 4 | 4301 | 4 | 0.5 s |
| iqb/2024MgrundlegendBAnalysisMMS1.pdf | erfasst | 4 | 6532 | 4 | 0.6 s |
| iqb/2024MgrundlegendBAnalysisMMS2.pdf | erfasst | 5 | 7409 | 5 | 0.7 s |
| iqb/2024MgrundlegendBAnalysisWTR1.pdf | erfasst | 5 | 7003 | 5 | 0.6 s |
| iqb/2024MgrundlegendBAnalysisWTR2.pdf | erfasst | 5 | 6797 | 5 | 0.7 s |
| iqb/2024MgrundlegendBStochastikMMS1.pdf | erfasst | 4 | 5486 | 4 | 0.5 s |
| iqb/2024MgrundlegendBStochastikWTR1.pdf | erfasst | 4 | 5571 | 4 | 0.5 s |
| iqb/2024MgrundlegendBStochastikWTR2.pdf | erfasst | 4 | 5052 | 4 | 0.5 s |
| iqb/2025MerhoehtAAGLAA11.pdf | erfasst | 2 | 1737 | 2 | 0.3 s |
| iqb/2025MerhoehtAAGLAA121.pdf | erfasst | 2 | 2197 | 2 | 0.3 s |
| iqb/2025MerhoehtAAGLAA122.pdf | erfasst | 2 | 1975 | 2 | 0.3 s |
| iqb/2025MerhoehtAAGLAA211.pdf | erfasst | 2 | 2323 | 2 | 0.4 s |
| iqb/2025MerhoehtAAGLAA212.pdf | erfasst | 3 | 2163 | 3 | 0.4 s |
| iqb/2025MerhoehtAAGLAA221.pdf | erfasst | 2 | 2120 | 2 | 0.2 s |
| iqb/2025MerhoehtAAGLAA222.pdf | erfasst | 2 | 1903 | 2 | 0.2 s |
| iqb/2025MerhoehtAAGLAA223.pdf | erfasst | 2 | 2381 | 2 | 0.3 s |
| iqb/2025MerhoehtAAGLAA224.pdf | erfasst | 2 | 2197 | 2 | 0.3 s |
| iqb/2025MerhoehtAAnalysis11.pdf | erfasst | 2 | 1933 | 2 | 0.2 s |
| iqb/2025MerhoehtAAnalysis12.pdf | erfasst | 2 | 1831 | 2 | 0.3 s |
| iqb/2025MerhoehtAAnalysis13.pdf | erfasst | 2 | 1874 | 2 | 0.3 s |
| iqb/2025MerhoehtAAnalysis21.pdf | erfasst | 2 | 2132 | 2 | 0.2 s |
| iqb/2025MerhoehtAAnalysis22.pdf | erfasst | 2 | 2239 | 2 | 0.2 s |
| iqb/2025MerhoehtAAnalysis23.pdf | erfasst | 2 | 1993 | 2 | 0.3 s |
| iqb/2025MerhoehtAStochastik11.pdf | erfasst | 2 | 2202 | 2 | 0.3 s |
| iqb/2025MerhoehtAStochastik12.pdf | erfasst | 2 | 2352 | 2 | 0.3 s |
| iqb/2025MerhoehtAStochastik21.pdf | erfasst | 2 | 1742 | 2 | 0.2 s |
| iqb/2025MerhoehtAStochastik22.pdf | erfasst | 2 | 2328 | 2 | 0.3 s |
| iqb/2025MerhoehtAStochastik23.pdf | erfasst | 2 | 1628 | 2 | 0.2 s |
| iqb/2025MerhoehtBAGLAA1MMS.pdf | erfasst | 4 | 5528 | 4 | 0.7 s |
| iqb/2025MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 5129 | 4 | 0.5 s |
| iqb/2025MerhoehtBAGLAA2MMS.pdf | erfasst | 3 | 3812 | 3 | 0.4 s |
| iqb/2025MerhoehtBAGLAA2WTR.pdf | erfasst | 4 | 3896 | 4 | 0.5 s |
| iqb/2025MerhoehtBAnalysisMMS1.pdf | erfasst | 4 | 5990 | 4 | 0.6 s |
| iqb/2025MerhoehtBAnalysisMMS2.pdf | erfasst | 4 | 5898 | 4 | 0.7 s |
| iqb/2025MerhoehtBAnalysisWTR1.pdf | erfasst | 4 | 6092 | 4 | 0.6 s |
| iqb/2025MerhoehtBAnalysisWTR2.pdf | erfasst | 4 | 5400 | 4 | 0.7 s |
| iqb/2025MerhoehtBAnalysisWTR3.pdf | erfasst | 4 | 6153 | 4 | 0.6 s |
| iqb/2025MerhoehtBStochastikMMS1.pdf | erfasst | 4 | 5714 | 4 | 0.5 s |
| iqb/2025MerhoehtBStochastikMMS2.pdf | erfasst | 3 | 5253 | 3 | 0.4 s |
| iqb/2025MerhoehtBStochastikMMS3.pdf | erfasst | 4 | 5598 | 4 | 0.6 s |
| iqb/2025MerhoehtBStochastikWTR1.pdf | erfasst | 4 | 5714 | 4 | 0.6 s |
| iqb/2025MerhoehtBStochastikWTR2.pdf | erfasst | 3 | 5253 | 3 | 0.5 s |
| iqb/2025MerhoehtBStochastikWTR3.pdf | erfasst | 4 | 5598 | 4 | 0.5 s |
| iqb/2025MgrundlegendAAGLAA11.pdf | erfasst | 2 | 1907 | 2 | 0.2 s |
| iqb/2025MgrundlegendAAGLAA12.pdf | erfasst | 2 | 2209 | 2 | 0.3 s |
| iqb/2025MgrundlegendAAGLAA211.pdf | erfasst | 2 | 2201 | 2 | 0.2 s |
| iqb/2025MgrundlegendAAGLAA212.pdf | erfasst | 2 | 1925 | 2 | 0.2 s |
| iqb/2025MgrundlegendAAGLAA213.pdf | erfasst | 2 | 1892 | 2 | 0.2 s |
| iqb/2025MgrundlegendAAGLAA221.pdf | erfasst | 2 | 2092 | 2 | 0.2 s |
| iqb/2025MgrundlegendAAGLAA222.pdf | erfasst | 2 | 2211 | 2 | 0.3 s |
| iqb/2025MgrundlegendAAnalysis11.pdf | erfasst | 3 | 1896 | 3 | 0.3 s |
| iqb/2025MgrundlegendAAnalysis12.pdf | erfasst | 2 | 1918 | 2 | 0.3 s |
| iqb/2025MgrundlegendAAnalysis13.pdf | erfasst | 2 | 1767 | 2 | 0.2 s |
| iqb/2025MgrundlegendAAnalysis21.pdf | erfasst | 2 | 1984 | 2 | 0.2 s |
| iqb/2025MgrundlegendAAnalysis22.pdf | erfasst | 2 | 2053 | 2 | 0.2 s |
| iqb/2025MgrundlegendAStochastik11.pdf | erfasst | 2 | 2331 | 2 | 0.2 s |
| iqb/2025MgrundlegendAStochastik12.pdf | erfasst | 2 | 1849 | 2 | 0.2 s |
| iqb/2025MgrundlegendAStochastik13.pdf | erfasst | 2 | 1988 | 2 | 0.2 s |
| iqb/2025MgrundlegendAStochastik21.pdf | erfasst | 2 | 2171 | 2 | 0.3 s |
| iqb/2025MgrundlegendAStochastik22.pdf | erfasst | 2 | 2279 | 2 | 0.2 s |
| iqb/2025MgrundlegendBAGLAA1WTR.pdf | erfasst | 3 | 4164 | 3 | 0.4 s |
| iqb/2025MgrundlegendBAGLAA2MMS1.pdf | erfasst | 4 | 4861 | 4 | 0.5 s |
| iqb/2025MgrundlegendBAGLAA2MMS2.pdf | erfasst | 3 | 3485 | 3 | 0.5 s |
| iqb/2025MgrundlegendBAGLAA2WTR1.pdf | erfasst | 4 | 4909 | 4 | 0.5 s |
| iqb/2025MgrundlegendBAGLAA2WTR2.pdf | erfasst | 3 | 3525 | 3 | 0.4 s |
| iqb/2025MgrundlegendBAnalysisMMS1.pdf | erfasst | 4 | 5241 | 4 | 0.6 s |
| iqb/2025MgrundlegendBAnalysisMMS2.pdf | erfasst | 4 | 4861 | 4 | 0.7 s |
| iqb/2025MgrundlegendBAnalysisWTR1.pdf | erfasst | 4 | 4897 | 4 | 0.5 s |
| iqb/2025MgrundlegendBAnalysisWTR2.pdf | erfasst | 4 | 4152 | 4 | 0.5 s |
| iqb/2025MgrundlegendBStochastikMMS1.pdf | erfasst | 3 | 3787 | 3 | 0.4 s |
| iqb/2025MgrundlegendBStochastikMMS2.pdf | erfasst | 3 | 3565 | 3 | 0.4 s |
| iqb/2025MgrundlegendBStochastikWTR1.pdf | erfasst | 3 | 3832 | 3 | 0.4 s |
| iqb/2025MgrundlegendBStochastikWTR2.pdf | erfasst | 3 | 3565 | 3 | 0.4 s |
| iqb/2025MgrundlegendBStochastikWTR3.pdf | erfasst | 3 | 5001 | 3 | 0.4 s |
| iqb/2026MerhoehtAAGLAA11.pdf | erfasst | 3 | 2762 | 3 | 0.3 s |
| iqb/2026MerhoehtAAGLAA121.pdf | erfasst | 2 | 2078 | 2 | 0.2 s |
| iqb/2026MerhoehtAAGLAA122.pdf | erfasst | 2 | 2047 | 2 | 0.2 s |
| iqb/2026MerhoehtAAGLAA211.pdf | erfasst | 2 | 2009 | 2 | 0.2 s |
| iqb/2026MerhoehtAAGLAA212.pdf | erfasst | 2 | 1853 | 2 | 0.2 s |
| iqb/2026MerhoehtAAGLAA221.pdf | erfasst | 2 | 2143 | 2 | 0.2 s |
| iqb/2026MerhoehtAAGLAA222.pdf | erfasst | 2 | 2023 | 2 | 0.2 s |
| iqb/2026MerhoehtAAGLAA223.pdf | erfasst | 2 | 2200 | 2 | 0.2 s |
| iqb/2026MerhoehtAAnalysis11.pdf | erfasst | 2 | 1864 | 2 | 0.2 s |
| iqb/2026MerhoehtAAnalysis12.pdf | erfasst | 3 | 2021 | 3 | 0.4 s |
| iqb/2026MerhoehtAAnalysis13.pdf | erfasst | 2 | 1996 | 2 | 0.3 s |
| iqb/2026MerhoehtAAnalysis14.pdf | erfasst | 2 | 1933 | 2 | 0.2 s |
| iqb/2026MerhoehtAAnalysis21.pdf | erfasst | 2 | 2214 | 2 | 0.2 s |
| iqb/2026MerhoehtAAnalysis22.pdf | erfasst | 2 | 2041 | 2 | 0.3 s |
| iqb/2026MerhoehtAAnalysis23.pdf | erfasst | 2 | 2153 | 2 | 0.2 s |
| iqb/2026MerhoehtAStochastik11.pdf | erfasst | 2 | 1967 | 2 | 0.2 s |
| iqb/2026MerhoehtAStochastik12.pdf | erfasst | 2 | 2350 | 2 | 0.2 s |
| iqb/2026MerhoehtAStochastik21.pdf | erfasst | 2 | 2369 | 2 | 0.3 s |
| iqb/2026MerhoehtAStochastik22.pdf | erfasst | 2 | 2182 | 2 | 0.2 s |
| iqb/2026MerhoehtAStochastik23.pdf | erfasst | 2 | 2127 | 2 | 0.2 s |
| iqb/2026MerhoehtBAGLAA1MMS.pdf | erfasst | 4 | 5813 | 4 | 0.6 s |
| iqb/2026MerhoehtBAGLAA1WTR.pdf | erfasst | 4 | 5851 | 4 | 0.6 s |
| iqb/2026MerhoehtBAGLAA2MMS1.pdf | erfasst | 4 | 5348 | 4 | 0.5 s |
| iqb/2026MerhoehtBAGLAA2MMS2.pdf | erfasst | 4 | 5102 | 4 | 0.6 s |
| iqb/2026MerhoehtBAGLAA2WTR1.pdf | erfasst | 4 | 5464 | 4 | 0.5 s |
| iqb/2026MerhoehtBAGLAA2WTR2.pdf | erfasst | 3 | 3583 | 3 | 0.4 s |
| iqb/2026MerhoehtBAnalysisMMS1.pdf | erfasst | 4 | 7009 | 4 | 0.7 s |
| iqb/2026MerhoehtBAnalysisMMS2.pdf | erfasst | 4 | 5916 | 4 | 0.6 s |
| iqb/2026MerhoehtBAnalysisWTR1.pdf | erfasst | 4 | 5597 | 4 | 0.6 s |
| iqb/2026MerhoehtBAnalysisWTR2.pdf | erfasst | 4 | 5661 | 4 | 0.6 s |
| iqb/2026MerhoehtBAnalysisWTR3.pdf | erfasst | 4 | 5053 | 4 | 0.7 s |
| iqb/2026MerhoehtBStochastikMMS1.pdf | erfasst | 4 | 5925 | 4 | 0.5 s |
| iqb/2026MerhoehtBStochastikMMS2.pdf | erfasst | 4 | 5697 | 4 | 0.6 s |
| iqb/2026MerhoehtBStochastikMMS3.pdf | erfasst | 4 | 6629 | 4 | 0.6 s |
| iqb/2026MerhoehtBStochastikWTR1.pdf | erfasst | 4 | 5950 | 4 | 0.5 s |
| iqb/2026MerhoehtBStochastikWTR2.pdf | erfasst | 4 | 5700 | 4 | 0.5 s |
| iqb/2026MerhoehtBStochastikWTR3.pdf | erfasst | 4 | 6644 | 4 | 0.6 s |
| iqb/2026MgrundlegendAAGLAA111.pdf | erfasst | 2 | 2053 | 2 | 0.3 s |
| iqb/2026MgrundlegendAAGLAA112.pdf | erfasst | 2 | 1829 | 2 | 0.3 s |
| iqb/2026MgrundlegendAAGLAA12.pdf | erfasst | 2 | 2067 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAGLAA211.pdf | erfasst | 2 | 1916 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAGLAA212.pdf | erfasst | 2 | 1829 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAGLAA213.pdf | erfasst | 3 | 2035 | 3 | 0.3 s |
| iqb/2026MgrundlegendAAGLAA221.pdf | erfasst | 2 | 1947 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAGLAA222.pdf | erfasst | 2 | 2112 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAnalysis11.pdf | erfasst | 2 | 1806 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAnalysis12.pdf | erfasst | 2 | 2241 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAnalysis13.pdf | erfasst | 2 | 2228 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAnalysis14.pdf | erfasst | 2 | 1914 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAnalysis21.pdf | erfasst | 2 | 1948 | 2 | 0.2 s |
| iqb/2026MgrundlegendAAnalysis22.pdf | erfasst | 2 | 2125 | 2 | 0.3 s |
| iqb/2026MgrundlegendAStochastik11.pdf | erfasst | 2 | 1781 | 2 | 0.2 s |
| iqb/2026MgrundlegendAStochastik12.pdf | erfasst | 2 | 2076 | 2 | 0.2 s |
| iqb/2026MgrundlegendAStochastik13.pdf | erfasst | 2 | 2243 | 2 | 0.2 s |
| iqb/2026MgrundlegendAStochastik21.pdf | erfasst | 2 | 1855 | 2 | 0.2 s |
| iqb/2026MgrundlegendAStochastik22.pdf | erfasst | 2 | 1752 | 2 | 0.2 s |
| iqb/2026MgrundlegendBAGLAA1MMS.pdf | erfasst | 3 | 4646 | 3 | 0.4 s |
| iqb/2026MgrundlegendBAGLAA1WTR.pdf | erfasst | 4 | 4263 | 4 | 0.5 s |
| iqb/2026MgrundlegendBAGLAA2MMS1.pdf | erfasst | 4 | 4316 | 4 | 0.5 s |
| iqb/2026MgrundlegendBAGLAA2MMS2.pdf | erfasst | 3 | 3372 | 3 | 0.4 s |
| iqb/2026MgrundlegendBAGLAA2WTR1.pdf | erfasst | 4 | 4322 | 4 | 0.5 s |
| iqb/2026MgrundlegendBAGLAA2WTR2.pdf | erfasst | 3 | 3491 | 3 | 0.4 s |
| iqb/2026MgrundlegendBAnalysisMMS1.pdf | erfasst | 4 | 5155 | 4 | 0.6 s |
| iqb/2026MgrundlegendBAnalysisMMS2.pdf | erfasst | 4 | 5082 | 4 | 0.5 s |
| iqb/2026MgrundlegendBAnalysisWTR1.pdf | erfasst | 4 | 5102 | 4 | 0.6 s |
| iqb/2026MgrundlegendBAnalysisWTR2.pdf | erfasst | 4 | 5181 | 4 | 0.5 s |
| iqb/2026MgrundlegendBStochastikMMS1.pdf | erfasst | 4 | 4689 | 4 | 0.5 s |
| iqb/2026MgrundlegendBStochastikMMS2.pdf | erfasst | 3 | 4121 | 3 | 0.4 s |
| iqb/2026MgrundlegendBStochastikWTR1.pdf | erfasst | 4 | 4709 | 4 | 0.5 s |
| iqb/2026MgrundlegendBStochastikWTR2.pdf | erfasst | 3 | 4120 | 3 | 0.4 s |
| iqb/BeispielaufgabenMerhoehtAAGLAA111.pdf | erfasst | 2 | 2308 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAGLAA112.pdf | erfasst | 2 | 2308 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAGLAA113.pdf | erfasst | 2 | 2938 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAGLAA121.pdf | erfasst | 2 | 2191 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAGLAA122.pdf | erfasst | 2 | 2929 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAGLAA211.pdf | erfasst | 2 | 2308 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAGLAA212.pdf | erfasst | 2 | 2247 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAGLAA22.pdf | erfasst | 2 | 2189 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAnalysis11.pdf | erfasst | 2 | 2269 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAnalysis12.pdf | erfasst | 2 | 2198 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAAnalysis2.pdf | erfasst | 3 | 2471 | 3 | 0.3 s |
| iqb/BeispielaufgabenMerhoehtAStochastik11.pdf | erfasst | 2 | 2253 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAStochastik12.pdf | erfasst | 2 | 2473 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtAStochastik2.pdf | erfasst | 2 | 2658 | 2 | 0.2 s |
| iqb/BeispielaufgabenMerhoehtBAGLAA1CAS.pdf | erfasst | 5 | 7629 | 5 | 0.6 s |
| iqb/BeispielaufgabenMerhoehtBAGLAA1WTR.pdf | erfasst | 5 | 7734 | 5 | 0.6 s |
| iqb/BeispielaufgabenMerhoehtBAGLAA2CAS.pdf | erfasst | 4 | 6551 | 4 | 0.5 s |
| iqb/BeispielaufgabenMerhoehtBAGLAA2WTR.pdf | erfasst | 3 | 5539 | 3 | 0.4 s |
| iqb/BeispielaufgabenMerhoehtBAnalysisCAS1.pdf | erfasst | 5 | 8780 | 5 | 0.7 s |
| iqb/BeispielaufgabenMerhoehtBAnalysisCAS2.pdf | erfasst | 6 | 9336 | 6 | 0.8 s |
| iqb/BeispielaufgabenMerhoehtBAnalysisWTR.pdf | erfasst | 5 | 7739 | 5 | 0.6 s |
| iqb/BeispielaufgabenMerhoehtBStochastikCAS.pdf | erfasst | 4 | 6134 | 4 | 0.5 s |
| iqb/BeispielaufgabenMerhoehtBStochastikWTR.pdf | erfasst | 4 | 7156 | 4 | 0.5 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA111.pdf | erfasst | 2 | 2628 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA112.pdf | erfasst | 2 | 2510 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA113.pdf | erfasst | 2 | 2428 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA114.pdf | erfasst | 2 | 2574 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA121.pdf | erfasst | 2 | 2339 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA122.pdf | erfasst | 2 | 3015 | 2 | 0.3 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA211.pdf | erfasst | 2 | 2629 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA212.pdf | erfasst | 2 | 2510 | 2 | 0.3 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA213.pdf | erfasst | 2 | 2427 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAGLAA22.pdf | erfasst | 2 | 2337 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAnalysis11.pdf | erfasst | 2 | 2256 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAnalysis12.pdf | erfasst | 2 | 2610 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAAnalysis2.pdf | erfasst | 2 | 2558 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAStochastik11.pdf | erfasst | 2 | 2461 | 2 | 0.3 s |
| iqb/BeispielaufgabenMgrundlegendAStochastik12.pdf | erfasst | 2 | 2899 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendAStochastik2.pdf | erfasst | 2 | 2625 | 2 | 0.2 s |
| iqb/BeispielaufgabenMgrundlegendBAGLAA1CAS.pdf | erfasst | 4 | 6562 | 4 | 0.5 s |
| iqb/BeispielaufgabenMgrundlegendBAGLAA1WTR.pdf | erfasst | 4 | 5595 | 4 | 0.5 s |
| iqb/BeispielaufgabenMgrundlegendBAGLAA2CAS.pdf | erfasst | 4 | 5192 | 4 | 0.4 s |
| iqb/BeispielaufgabenMgrundlegendBAGLAA2WTR.pdf | erfasst | 3 | 4775 | 3 | 0.4 s |
| iqb/BeispielaufgabenMgrundlegendBAnalysisCAS.pdf | erfasst | 5 | 7505 | 5 | 0.6 s |
| iqb/BeispielaufgabenMgrundlegendBAnalysisWTR.pdf | erfasst | 4 | 6258 | 4 | 0.6 s |
| iqb/BeispielaufgabenMgrundlegendBStochastikCAS.pdf | erfasst | 4 | 5521 | 4 | 0.4 s |
| iqb/BeispielaufgabenMgrundlegendBStochastikWTR.pdf | erfasst | 3 | 4712 | 3 | 0.4 s |
| iqb/sonstiges/2025MerhoehtBAnalysisMMS3.pdf | fehlgeschlagen | – | – | – | keine echte PDF-Datei (153 Byte, beginnt mit `<html`, kein `%PDF-`-Header); die Kennung steht nicht in iqb-quellen.csv (624 Zeilen, nur MMS1/MMS2 für 2025-ea-B) – also keine der 624 echten Kennungen, sondern eine Altlast unter sonstiges/ ohne verlässliche Quelle zum Neuholen (faellig.md § 3). Etappe 4 zählt trotzdem 624 von 624 echten Dateien vollständig |

## 6 Zusammenfassung je Etappe

Wird am Ende jeder Etappe nachgetragen: verarbeitet, übersprungen,
fehlgeschlagen, Gesamtdauer.

## 7 Unterschied korpus/ und hefte-md/

`hefte-md/` (zehn abi-Verlagshefte plus sechs msa-Hefte aus § 1) ist
Modell-gelesen: Gliederung, Aufgabenmarken und Abbildungsausschnitte folgen
dem Katalog, gedacht für den Abgleich Katalogzeile ↔ Heft. `korpus/` ist rein
maschinell: Rohtext je Seite plus Ganzseitenrender, ohne Gliederung nach
Aufgaben, gedacht für Volltextsuche über den ganzen Heftbestand. Beide
Formate schließen sich nicht aus; wo beide existieren (die zehn abi-Hefte,
die sechs msa-Hefte aus § 1), ist `hefte-md/` die genauere Quelle für den
Wortlaut, `korpus/` die einzige mit durchgängiger Abdeckung.
