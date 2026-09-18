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

| Datei | Ergebnis | Seiten | Zeichen | Abbildungen | Dauer/Grund |
|---|---|---|---|---|---|

## 5 korpus/ Etappe 4 – iqb (624 Dateien)

| Datei | Ergebnis | Seiten | Zeichen | Abbildungen | Dauer/Grund |
|---|---|---|---|---|---|

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
