# Prüfung des Vorbehalts in fhr-vorgaben.md

Stand 2026-09-24 (Auftrag Nacht, Teil 3; fhr-vorgaben.md § 4 Schritt 0). Jede
Angabe aus § 1 bis § 3 von fhr-vorgaben.md gegen die Papiere gehalten:
Prüfungsschwerpunkte Mathematik 2026/27 und 2027/28, Rundschreiben
MBJS_RS_07-26, sowie – für die Angaben, die sich auf die Hefte selbst
beziehen – eine Stichprobe von vier der sechzehn Lehrerhefte
(2019-A, 2019-C, 2020-A, 2021-B, 2022-B, 2023-C; sechs von sechzehn, nicht
vier – siehe Methodik). Die reinen Punktsummen und Prüfungstermine aller
sechzehn Hefte wurden zusätzlich vollständig gegen `fhr-katalog.csv` und
`fhr-pruefungen.md` geprüft, die selbst aus dem Lesen der echten Hefte bei
der Erfassung (12.09.2026) stammen.

**Methodik.** Prüfungsschwerpunkte 2026/27 und 2027/28 sowie das
Rundschreiben MBJS_RS_07-26 wurden vollständig gelesen (Text, `pdftotext
-layout`). Von den sechzehn Heften wurden sechs mit curl geholt und im
Textlayer geprüft: 2019-A, 2019-C, 2020-A, 2021-B, 2022-B, 2023-C – je
mindestens ein Heft aus der Vor-Corona-Zeit (2019), den beiden
Corona-Jahrgängen (2021, 2022) und der Zeit danach (2023), dazu 2020 für die
Koordinatenschreibweise. Für die übrigen zehn Hefte (2021-A, 2022-C,
2023-A, 2024-B/C, 2025-A/C, 2026-B/C) gilt nur die Prüfung über
`fhr-katalog.csv`/`fhr-pruefungen.md`, nicht das erneute Lesen des Originals.

## Ergebnis je Angabe

| § | Angabe | Fundstelle im Papier | Ergebnis |
|---|---|---|---|
| 1 | Rechtsgrundlage FOSFHRV; Aufgaben nach § 31 Abs. 1 zentral festgelegt | MBJS_RS_07-26.pdf, S. 1 (Ziff. 1.1.2): „Gemäß § 31 Absatz 1 FOSFHRV werden die Aufgaben für die zentralen schriftlichen Prüfungsfächer Deutsch, Englisch und Mathematik durch das für Schule zuständige Ministerium verbindlich festgelegt …“ | bestätigt |
| 1 | Rundschreiben MBJS_RS_07-26 vom 25.06.2026, nennt die Ersatzaufgabe nach § 31 Abs. 1 FOSFHRV | MBJS_RS_07-26.pdf, S. 1: „Vom 25. Juni 2026“; Ziff. 1.1.2: „Für einen zentralen Nachprüfungstermin wird eine Ersatzaufgabe zur Verfügung gestellt.“ | bestätigt |
| 1 | Prüfungsschwerpunkte je Schuljahr im Ordner `Pruefungsschwerpunkte/`; dort liegen nur die Fassungen 2026/27 und 2027/28, für 2019–2026 fehlen sie | Beide Dateien unter den in fhr-quellen.md § 1 genannten Adressen abrufbar (je 2 Seiten, wie in fhr-quellen.md § 5 vermerkt); keine weiteren Jahrgänge im Verzeichnis gefunden | bestätigt |
| 1 | Rahmenlehrplan Mathematik FOS seit 01.08.2019, konkretisiert durch die jährlichen Prüfungsschwerpunkte | Pruefungsschwerpunkte_Mathematik_2026-2027.pdf, S. 1: „Die angegebenen Schwerpunkte basieren auf dem am 01. August 2019 in Kraft getretenen Rahmenlehrplan …“; deckungsgleich mit `quellen/quelle-rlp-fos-bb-2019-mathematik.txt` [RLP-FOS] („gültig ab 1. August 2019“) | bestätigt |
| 1 | Kein IQB-Pool: die Aufgabenpools des IQB gelten nur für die Allgemeine Hochschulreife | nicht erneut geprüft – bereits mit eigenem Beleg versehen (fhr.md § 9, IQB-Pool-Seite, Stand 19.09.2026); außerhalb der heute geholten Papiere | nicht erneut geprüft |
| 2 | Aufbau: drei voneinander unabhängige Aufgaben mit Überschrift; laut Prüfungsschwerpunkten sind auch vier möglich, im Bestand kommen nur drei vor | Pruefungsschwerpunkte_Mathematik_2026-2027.pdf, S. 2 (Ziff. 2.1): „In einem Aufgabenvorschlag werden drei oder vier voneinander unabhängige, komplexe Aufgaben gestellt“; 2019-A/2019-C/2020-A/2021-B/2022-B/2023-C je genau drei Aufgaben mit Überschrift „1./2./3. Aufgabe: …“ | bestätigt |
| 2 | Zweimal Differential- und Integralrechnung, einmal Stochastik | 2019-A: „Differentialrechnung“ / „Integralrechnung“ / „Stochastik“; 2021-B: „Differential- und Integralrechnung“ / „Anwendung der Differential- und Integralrechnung“ / „Stochastik“; 2022-B: „Differentialrechnung“ / „Differential- und Integralrechnung“ / „Stochastik“ – Wortlaut der Aufgaben-Überschrift wechselt von Jahr zu Jahr, das Themenverhältnis (zwei Analysis, eine Stochastik) ist in allen drei geprüften Jahrgängen gleich | bestätigt (Wortlaut der Überschrift variiert, Sache stimmt) |
| 2 | 70 Bewertungseinheiten, 180 Minuten, ein Niveau, keine Anforderungsbereiche im Heft | Pruefungsschwerpunkte_Mathematik_2026-2027.pdf, S. 2 (Ziff. 5): „Die Arbeitszeit beträgt 180 Minuten“; Punktsumme aller 16 Hefte laut `fhr-katalog.csv` durchgehend 70; kein Heft der Stichprobe nennt einen Anforderungsbereich | bestätigt |
| 2 | Zwei gleichwertige Aufgabenvorschläge (A/B/C) zur Wahl der Lehrkraft, ein weiterer unveröffentlichter Vorschlag für den Nachschreibetermin | Pruefungsschwerpunkte_Mathematik_2026-2027.pdf, S. 2 (Ziff. 2.1): „Den Schulen werden zum Prüfungstermin zwei gleichwertige Aufgabensätze zur Verfügung gestellt … Für den Nachschreibetermin wird nur ein Aufgabenvorschlag bereitgestellt“; fhr-quellen.md § 1 bestätigt, dass nur zwei der drei Vorschläge je Jahrgang veröffentlicht sind | bestätigt |
| 2 | 2019: Prüfung 10.05.2019, vor dem Rahmenlehrplan vom 01.08.2019; Hefte nennen keine Hilfsmittel; Koordinaten als P(–1\|–5) mit ASCII-Bindestrich als Minus | 2019-A.pdf, S. 1: „10. Mai 2019 – 09:00 Uhr“ (Datum bestätigt); 2019-A und 2019-C enthalten an keiner Stelle die Wörter „Hilfsmittel“, „Taschenrechner“ oder „Formelsammlung“ (Hilfsmittel-Angabe bestätigt); Koordinatenschreibweise: 2019-A, 2019-C und 2020-A verwenden im PDF-Textlayer durchgehend das Minuszeichen U+2212 (z. B. 2020-A: „Sx1(−1\|0)“), an keiner Stelle einen ASCII-Bindestrich vor einer Ziffer | Datum und Hilfsmittel-Angabe bestätigt; **Koordinatenschreibweise abweichend: die geprüften Hefte 2019/2020 benutzen das echte Minuszeichen (U+2212), nicht den ASCII-Bindestrich** |
| 2 | 2020: Prüfung 03.06.2020, erster Jahrgang unter dem heutigen Rahmenlehrplan, vor den Kürzungen; Hilfsmittel im Heft nicht genannt; Punkte 28+21+21 (A) und 29+21+20 (C) | fhr-pruefungen.md: „03.06.2020“ für 2020-A/C; 2020-A.pdf enthält keinen Hilfsmittel-Abschnitt; `fhr-katalog.csv`: 2020-A = 28+21+21 = 70, 2020-C = 29+21+20 = 70 | bestätigt |
| 2 | 2021: Coronabedingt gekürzte Vorgaben; ab 2021 stehen die Hilfsmittel im Heft (Formelsammlung, Nachschlagewerk Rechtschreibung, Taschenrechner ohne Programmierbarkeit/Grafik/numerisches Differenzieren oder Integrieren/automatisches Gleichungslösen; Rundung zwei Dezimalstellen); ab 2021 meist Gutachtenbogen (fehlt 2021 B und 2023 C); Punkte 2021 B 32+18+20 | 2021-B.pdf (8 Seiten) enthält an keiner Stelle die Wörter „Hilfsmittel“, „Taschenrechner“, „Formelsammlung“, „Nachschlagewerk“ oder „Dezimalstelle“ – ebenso wenig 2022-B.pdf und 2023-C.pdf; der zitierte Wortlaut ist dagegen deckungsgleich mit Abschnitt 3 der Prüfungsschwerpunkte 2026/27 und 2027/28 („Nachschlagewerk zur Rechtschreibung … Formelsammlung … Taschenrechner, die nicht programmierbar und nicht graphikfähig sind …“); für 2019–2026 liegen aber keine Prüfungsschwerpunkte vor (§ 1). Gutachtenbogen-Befund: deckt sich mit fhr-pruefungen.md Kopf. Punktsumme: `fhr-katalog.csv` 2021-B = 32+18+20 = 70 | Punkte und Gutachtenbogen bestätigt; **Corona-Kürzung nicht belegbar** (keine Prüfungsschwerpunkte 2021 archiviert); **Hilfsmittel-Wortlaut „im Heft" nicht belegbar** (Wortlaut steht in keinem der vier geprüften Lehrerhefte 2019-A/2021-B/2022-B/2023-C; er entspricht wörtlich den Prüfungsschwerpunkten, deren Fassung für 2021 aber nicht vorliegt) |
| 2 | 2022: Coronabedingt gekürzte Vorgaben; Prüfung 06.05.2022; Aufbau sonst unverändert | fhr-pruefungen.md: „06.05.2022“; 2022-B.pdf: drei Aufgaben mit Überschrift, 70 BE (Aufbau bestätigt) | Datum und Aufbau bestätigt; **Corona-Kürzung nicht belegbar** (wie 2021, keine Prüfungsschwerpunkte archiviert) |
| 2 | 2023–2026: Aufbau unverändert; Prüfungen 05.05.2023, 08.05.2024, 28.05.2025, 05.06.2026; 2026 C mit 27+23+20; Prüfungsschwerpunkte dieser Jahrgänge liegen nicht auf dem Server | fhr-pruefungen.md nennt exakt diese vier Daten; `fhr-katalog.csv`: 2026-C = 27+23+20 = 70 (einzige Abweichung vom 30+20+20-Muster in diesem Zeitraum, wie behauptet); 2023-C.pdf: drei Aufgaben, 70 BE; im Verzeichnis `Pruefungsschwerpunkte/` liegen weiterhin nur die Fassungen 2026/27 und 2027/28 | bestätigt |
| 2 | 2027 (Prüfungsschwerpunkte 2026/27): zwei gleichwertige Aufgabensätze plus Nachschreibvorschlag; Hilfsmittel ohne CAS; Kompetenzen ausdrücklich nicht auf Themengebiete beschränkt; neue Inhalte 2027: Extremwertaufgaben, Rotationsvolumen um die x-Achse, Kombinatorische Abzählverfahren, Funktionsgleichung bis 2. Grad | Pruefungsschwerpunkte_Mathematik_2026-2027.pdf, S. 1–2 durchgehend – alle vier Inhalte wörtlich enthalten („Extremwertaufgaben (Umfang/Fläche von Drei- und Vierecken …)“, „Rotationsvolumen um die x-Achse (lineare und quadratische Funktionen)“, „kombinatorische Abzählverfahren …“, „Bestimmung von ganzrationalen Funktionsgleichungen bis zweiten Grades“); Hilfsmittelliste ohne CAS (S. 2, Abschnitt 3); „Der Erwerb von Kompetenzen ist grundsätzlich nicht auf einzelne Themengebiete beschränkt“ (S. 1) | bestätigt |
| 2 | 2028 (Prüfungsschwerpunkte 2027/28): neu gegenüber 2027 – Normale, Körpervolumen aus Grundfläche und Länge, Unabhängigkeit von Ereignissen, Funktionsgleichung bis 4. Grad (3./4. Grad nur über Symmetrie); die Inhalte mit Markierung 27 entfallen | Pruefungsschwerpunkte_Mathematik_2027-2028.pdf, S. 1: „Anstieg und Tangentengleichung, Normalengleichung“, „Berechnung von Körpervolumen aus Grundflächeninhalt und Länge“, „Unabhängigkeit von Ereignissen bei mehrstufigen Zufallsversuchen“, „Bestimmung von ganzrationalen Funktionsgleichungen bis vierten Grades (dritten und vierten Grades nur unter Ausnutzung von Symmetrie)“; Extremwertaufgaben, Rotationsvolumen und kombinatorische Abzählverfahren kommen im Dokument 2027/28 nicht mehr vor | bestätigt |
| 3 | Geometrie, Trigonometrie und Gleichungslehre kommen in den Prüfungsschwerpunkten nur als Werkzeug vor (kein eigener Abschnitt) | Pruefungsschwerpunkte_Mathematik_2026-2027.pdf und …2027-2028.pdf: die einzigen Abschnitte sind „Differentialrechnung“, „Integralrechnung“, „Stochastik“; kein Abschnitt „Geometrie“, „Trigonometrie“ oder „Gleichungslehre“ | bestätigt |
| 3 | Einstufige Laplace-Versuche stehen nicht in den Schwerpunkten, die Hefte verlangen sie aber (2023-C-3b) | Pruefungsschwerpunkte_Mathematik_2026-2027.pdf, Abschnitt Stochastik nennt nur „Mehrstufige Zufallsexperimente“; 2023-C.pdf, Aufgabe 3b (Poolbillard-Kugeln, eine Ziehung): „Da alle Kugeln gleich groß und gleich schwer sind, ist beim Ziehen … die Wahrscheinlichkeit für jedes Ergebnis gleich. Deshalb handelt es sich um ein Laplace-Experiment.“ – ein einstufiger Versuch | bestätigt |

## Zusammenfassung

- **Bestätigt:** 16 Angaben (davon 2 mit kleiner Wortlaut-Nuance ohne
  sachlichen Widerspruch: Aufgaben-Überschrift „Differentialrechnung“ vs.
  „Differential- und Integralrechnung“; Hilfsmittelliste „ohne CAS“ als
  Kurzform der vollständigen Taschenrechner-Beschreibung).
- **Abweichend:** 1 Angabe – die Koordinatenschreibweise 2019/2020 („ASCII-
  Bindestrich als Minus“, fhr.md § 4): die geprüften Originale verwenden das
  echte Minuszeichen U+2212, keinen ASCII-Bindestrich.
- **Nicht belegbar:** 3 Angaben – die „Coronabedingt gekürzte Vorgaben“ für
  2021 und 2022 (keine Prüfungsschwerpunkte dieser Jahrgänge archiviert) und
  der Hilfsmittel-Wortlaut „ab 2021 stehen die Hilfsmittel im Heft“ (steht in
  keinem der vier geprüften Lehrerhefte, sondern nur – wortgleich – in den
  für frühere Jahre nicht vorliegenden Prüfungsschwerpunkten).
- **Nicht erneut geprüft:** 1 Angabe (IQB-Pool gilt nicht für FHR) –
  außerhalb der heute geholten Papiere, bereits mit eigenem Beleg vom
  19.09.2026 versehen.

Der Vorbehalt im Kopf von fhr-vorgaben.md bleibt bestehen, da drei Angaben
offen sind. Nach fhr-vorgaben.md § 4 Schritt 0 bekommen nur die bestätigten
Zeilen die Fundstelle nachgetragen; die abweichende und die nicht
belegbaren Angaben werden nicht geändert – Entscheidung beim Lehrer.
