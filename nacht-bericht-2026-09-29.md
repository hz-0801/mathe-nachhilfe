Modell: Opus 5.5 (claude-opus-5-5)

# Bericht Auftrag Nacht 2026-09-29

Auftrag und Standdatei: archiv/auftrag-nacht-2026-09-29.md, archiv/nacht-stand-2026-09-29.md; Wortlaut der Urteile in beschluss-2026-09-26.md. Alle acht Teile sind erledigt. Nichts ist offen nach der Fehlerregel.

Teil 4 ist größer als bestellt: 2017-be-gk-cas 3.1 stammt aus der CAS-Poolfassung 2017MgrundlegendBStochastikCAS. Nach der Regel „Eine Vormerkung überlebt keinen Auftrag“ (CLAUDE.md § 2) ist deshalb vor dem Heft der Reserve-Stapel 2017-ga-B (CAS) erfasst worden, mit eigenem Commit.

Wer was gemacht hat:
- Selbst: Teile 1, 2, 5 und 6.
- Hilfsagenten (Opus): Teil 3; Teil 4 in drei Stufen (Stapel, Hefte, Sek-II-Nachzug), nacheinander; Teil 7 und 8 parallel dazu, beide mit eigenen Dateien.
- Beim Sek-II-Nachzug liefen einmal alte und neue Hilfsagenten zugleich (Teil 4).

Get-Date zeigte den ganzen Lauf den 26.09.2026 (14:07 bis 16:47). Daten in Dateien tragen das Auftragsdatum 29.09.2026, wie in den Nächten zuvor. Uhrzeiten in der Standdatei stammen aus Get-Date.

Kein Push. Nichts gelöscht. Nicht geändert: Prompt, blaetter/, ../blattbau.

## Teil 1: Beschlüsse ablegen (a91af3a)

Angelegt: beschluss-2026-09-26.md und auftrag-nacht-2026-09-29.md, beide wortgleich, UTF-8 ohne BOM, LF, geprüft. Dazu die Standdatei.

- **README.md:** Zeile für den Beschluss im Block Wurzel, hinter befund-testlauf-2026-09-25.md.
- **befund-testlauf-2026-09-25.md:** unter Beschluss 2 und unter Prompt 26 je die Zeile „Nachtrag 26.09.: vertagt, siehe beschluss-2026-09-26.md Punkt 1“. Sonst ist die Datei unverändert.
- **faellig.md:**
  - Der Posten „Übersichtsblatt: Form an den Prüfsteinen entscheiden“ steht in § 4 mit dem Ergebnis „vertagt“.
  - Neuer Posten in § 2: Prüfstein nur mit Abbildung und Tabelle, Auslöser „nach dem Testlauf v4.4“.
  - Der Posten einsortieren.py hat den Zusatz „ruht bis zum neuen Prüfstein“.

Gegenprobe: keine im Auftrag.

## Teil 2: Deutungsliste (f), Eichung 2017 (0d0ac40)

**abitur/iqb.md v1.17, § 7:** Eintrag (f) im Wortlaut des Beschlusses: „Mindestanzahl oder Mindestumfang für eine Mindestwahrscheinlichkeit bestimmen = III“.
- Die fünf Belege stehen dabei:
  - 2017-ga-B Stochastik WTR 1 2 e
  - 2017-ga-B Stochastik WTR 2 1 c
  - 2018-ea-B Stochastik WTR 1 1 b
  - 2019-ga-B Stochastik WTR 1 1 b
  - 2024-ea-B Stochastik WTR 1 1 c
- Abgegrenzt ist die Mindestanzahl aus einer Erwartungswertbedingung n · p > c; sie ist amtlich II.
- Der Kandidat „Fallunterscheidung ist amtlich II“ ist ausdrücklich nicht aufgenommen.
- iqb-pruefungen.md § 4 vermerkt an beiden Kandidaten den Stand.

**Bestandsprüfung:** Gesucht habe ich in Typ, gesucht, verfahren und Stichwörtern aller 1639 Poolzeilen. (f) trifft auf sechs Poolzeilen zu:

| id | Schätzung vorher | amtlich (AB) |
|---|---|---|
| 2017MgrundlegendBStochastikWTR1-2e | II | III |
| 2017MgrundlegendBStochastikWTR2-1c | II | III |
| 2017MerhoehtBStochastikCAS1-4 | II | III |
| 2018MerhoehtBStochastikWTR1-1b | II | III |
| 2019MgrundlegendBStochastikWTR1-1b | III | III |
| 2024MerhoehtBStochastikWTR1-1c | II | III |

- **Korrektur über Abgleichlauf 26** (abitur-abgleich.py v0.27, Feldkorrektur mit Grund in bemerkung): Die fünf Schätzungen II stehen jetzt auf III.
- **Landeszeile 2024-bebb-lk-B4c:** Sie ist die wortgleiche Dublette von 2024MerhoehtBStochastikWTR1-1c und trug deren Schätzung; sie zieht auf III nach.
- **Nicht (f):**
  - 2023MerhoehtBStochastikWTR3-1b (n · p > c, amtlich II)
  - 2023MerhoehtBStochastikWTR1-4b (Unverträglichkeit, III)
  - 2018MerhoehtBStochastikWTR2-1e (Mindestwert einer Wahrscheinlichkeit)
- **Eichung Bestand:** vorher 1526 von 1638 (enge Fassung 1527), nachher 1531 von 1638 (1532); abi 334 → 335 von 355.
- **Selbstprüfung:** beide Skripte bestanden; der Lauf aus einer frischen HEAD-Kopie ist byteidentisch.

**faellig.md:** Der Posten „Eichung Pool 2017 grundlegend prüfen“ steht in § 4 als „geschlossen, keine Jahrgangsregel“.

**Gegenprobe im Wortlaut** (abitur/befund-eichung-2017-2026-09-28.md, Abschnitt „Eichung je Pooljahr“): „Bestand vorher 1526 von 1638 gewerteten Zeilen; iqb-pruefungen.md § 4: (f) hat fünf Poolfälle, alle amtlich III“.
- 1526 von 1638: erfüllt.
- Poolfälle: **Abweichung, sechs statt fünf.** Erklärung: Die Zählung „fünf von fünf“ stammt vom Stapel 2017-ga-B. Der danach erfasste Stapel 2017-ea-B (CAS) brachte mit Stochastik CAS 1 Aufgabe 4 einen sechsten Fall, ebenfalls amtlich III. Die Regel ist dadurch gestützt, nicht geschwächt.

**Eigene Entscheidungen:**
- In bemerkung steht „Beschluss vom 26.09.2026“ statt des Dateinamens. Der Dateiname „beschluss-2026-…“ löste in der Selbstprüfung die ASCII-Minus-Prüfung aus. Der erste Lauf 26 ist deshalb zurückgesetzt und neu gefahren worden.
- Landeszeilen ohne Maßstab mit einer (f)-Leistung bleiben II: 2017-bb-ea-B4.2b, 2019-be-gk-B4.1b, 2020-be-gk-B4.1c, 2021-be-gk-B4e, 2022-bebb-gk-B4d, 2023-bebb-gk-B4.1f. Der Auftrag begrenzt auf Poolzeilen, und die Eichschranke gilt für Landeshefte nicht. Vermerkt in abi-pruefungen.md § 5.
- In iqb-pruefungen.md § 2 bleiben die Stapelwerte beim Stapellauf stehen. Die Änderung je Stapel steht in § 5 (2017-ga-B-wtr 34 → 36).

## Teil 3: Delta-Stapel 2018-ea-B (CAS) (e368eed)

**Stapel:**
- 9 CAS-Dateien, 300 BE, 85 Zeilen, 18 neue Typen.
- 1 Zeile ersatzweise (Kurvenlänge), 0 Zeilen mit „?“.
- Katalog 1639 → 1724 Zeilen, 42 Stapel.

**Eichung:**
- Schritte: blind 57 → nach Prüfung 67 → **nach (f) 69 von 85 (81,2 %)**.
- (f) greift nur bei Stochastik CAS 1 1 b (n = 108) und CAS 2 1 b (333), beide II → III.
- Keine andere Schätzung ist geändert.

**Mit dokumentierter Unterschreitung erfasst** (iqb-bau.py v1.10):
- Die Liste `EICHUNG_UNTERSCHRITTEN = {"2018-ea-B-cas": (69, 85, "beschluss-2026-09-26.md Punkt 2")}` steht neben SCHWELLEN.
- Der Stapellauf macht aus der gerissenen Schwelle nur dann eine Warnung, wenn die Messung genau diesen Wert ergibt. Gegenprobe: Mit Listenwert 68 oder ohne Eintrag bricht der Lauf ab.
- Die Selbstprüfung meldet „Warnung: Stapel 2018-ea-B-cas mit dokumentierter Unterschreitung der Eichschwelle … 69 von 85 (81.2 %), Schwelle 85 % unverändert“.
- SCHWELLEN bleibt 0.85.
- Begründung in iqb.md v1.18 § 7 und in iqb-pruefungen.md § 5. Der Absatz sagt ausdrücklich, dass das keine Wiedereinführung der Überschreibung je Stapel aus v1.4 ist: kein anderer Grenzwert, kein KONFIG-Feld, nur dieser Stapel.

**Abgleichlauf 27** (abitur-abgleich.py v0.28), sieben Zeilen, alle auf 2018MerhoehtBAGLAA2CAS1:
- 2018-bb-ea-B3.1 a, b, d, e: „Dublette von:“. Bei b und e zieht die Schätzung II → I auf den amtlichen Bereich nach.
- 2018-bb-ea-B3.1 c: „Dublette von:“ mit BE-Vermerk (5 statt 4 BE; die Kontrollangabe h_EF ≈ 21,21 m steht nur im Heft).
- 2018-bb-ea-B3.1 f: „Abgewandelt von:“ (Ebenengleichung vorgegeben, 6 statt 7 BE).
- 2018-bb-ea-cas-B3.1 f: „Abgewandelt von:“ (umformuliert, 6 statt 7 BE). Damit ist die Vormerkung geschlossen.

Dazu im selben Lauf:
- eine Zusammenziehung: „Mindestanzahl von Versuchen für mindestens drei Treffer … durch Probieren ermitteln“ → „Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln“
- neun Umbenennungen, vier erweiterte Definitionen; Liste in iqb-pruefungen.md und abi-pruefungen.md § 5
- Selbstprüfung beider Skripte bestanden; der Lauf aus einer frischen Kopie ist byteidentisch

**faellig.md:** Der Posten „Pool-Vormerkung 2018 schließen“ steht in § 4.

**Gegenprobe im Wortlaut** (nacht-bericht-2026-09-28.md Teil 2, befund-eichung-2017 Abschnitt 2018-ea-B): „85 Zeilen, erster Stand 57, nach Prüfung 67 von 85; danach grep „Poolaufgabe (nicht erfasst)" über abitur/abi-katalog.csv: 0 Treffer; Typenzahl vorher 1393 (Abgleichlauf 25)“. Erfüllt: 85 Zeilen, 57, 67, dazu 69 nach (f), grep 0, vorher 1393. **Typen vorher/nachher:** 1393 → 1411 (Stapel) → 1410 (Lauf 27).

**Eigene Entscheidungen (Hilfsagent):**
- 2018-bb-ea-B3.1c ist wie vorgegeben „Dublette von:“, obwohl das Heft eine zusätzliche Kontrollangabe trägt. Der Vermerk nennt sie.
- 2018-bb-ea-cas-B3.1f ist „Abgewandelt von:“.
- Die Zusammenziehung ist nach Kern § 6 geboten; sie betrifft eine Zeile.

**Quellbefunde** (iqb-pruefungen.md § 4):
- Analysis CAS 1 3 c: amtlich 7,56 m, ungerundet etwa 7,65 m.
- Zwei Druckfehler im Erwartungshorizont.
- AG/LA (A1) CAS 2 2 b: amtliche Begründung falsch, das Urteil stimmt.

## Teil 4: Nachtrag Berliner CAS-Hefte 2017/2018

### Vorstufe: Delta-Stapel 2017-ga-B (CAS) (708c4b2)

**Anlass und Voraussetzung:** Den Stapel verlangt die Vormerkungsregel (siehe oben). Geprüft am Text und am Seitenbild: 2017-be-gk-cas 3.1 a–g ist wortgleich mit Pool 1 a, 1 b, 2 a–e, bei gleichen BE.

**Umfang:**
- 5 Dateien, 115 BE, 38 Zeilen, 7 neue Typen.
- Keine Dateidublette.
- Stochastik CAS Aufgabe 1 ist eine Aufgabendublette zu WTR 1; sie bekommt keine Zeile, das Soll ist 15.
- AG/LA (A2) CAS 1 druckt die BE-Summe 25; die Teilaufgaben ergeben 20. Das Soll ist 20.

**Eichung:** erster Lauf 28 von 38 (73,7 %). Fünf Korrekturen mit Regel ergeben 33 von 38 (86,8 %); die Schwelle ist ohne Sonderliste erreicht.

**Bestand danach:**
- Typen 1410 → 1417, Katalog 1724 → 1762, 43 Stapel.
- iqb.md ist jetzt v1.19.

### Die vier Hefte (a46b6d1, 5df108b, 0ee9749, 999a88a)

**abi-bau.py v0.15:** neue Landes-Dublette.
- Form: „Dublette von: <id der WTR-Zeile>.“ mit dem Vermerk „nur BE: …“, „nur Zahl: …“ oder „nur BE und Zahl: …“.
- Das Skript prüft: dieselbe Aufgabe, gleicher typ, gleiches afb_amtlich, Vermerk passend zu den BE.
- Für den alten Bestand ist die Selbstprüfung byteidentisch zu v0.14.
- iqb-bau.py übergeht den Verweis, weil er keine Pool-Kennung trägt.

| Heft | neue Zeilen | eigene | Landes-Dubletten | Pool-Dubletten | Verweise auf BB-CAS-Zeilen | nicht erfasst (eigene LK-Aufgaben) | neue Typen |
|---|---|---|---|---|---|---|---|
| 2017-be-gk-cas | 16 | 9 (1.1 a, e, f; 1.2 a, b, d, f; 2.2 c; 3.2 d) | 5, nur BE (1.1 b, c; 1.2 e; 2.2 d; 3.2 c) | 2 (3.1 e → 2017MgrundlegendBStochastikCAS-2c, 3.1 g → -2e) | 0 | – | 2 |
| 2017-be-lk-cas | 0 | – | – | – | 9 (1.2 b, d, g → 2017-bb-ea-cas-B2.2b, d, g; 2.2 c, e, f → B3.1c, e, f; 3.2 a, b, d → B4.2a, b, d) | 10 (1.1 a, b, c, e, f, g; 2.1 b, c; 3.1 b, c) | 0 |
| 2018-be-gk-cas | 16 | 12 (1.1 c, e, f, g; 1.2 a–h) | 3 (1.1 b, d nur BE; 3.1 b nur Zahl) | 1 (3.2 a → 2018MgrundlegendBStochastikWTR2-1a) | 0 | – | 2 |
| 2018-be-lk-cas | 0 | – | – | – | 13 (1.1 c–h → 2018-bb-ea-cas-B2.1c–h; 1.2 b, d, e, f, g, i → B2.2…; 2.1 f → B3.1f) | 3 (2.2 c, g; 3.1 a) | 0 |

Die Verweislisten der LK-Hefte stehen wie bei einem Zwilling des anderen Landes in abi-pruefungen.md § 4.

**abi.md v0.31:**
- § 7 trägt die Abgrenzung als entschieden, mit Regel aus Punkt 1–3, Landes-Dublette und Verweis auf den Beschluss.
- § 9 führt den Punkt als beantwortet.

**Abgleichlauf 28** (abitur-abgleich.py v0.29):
- 11 neue Typen abgeglichen, keine Zusammenziehung.
- Vier Umbenennungen:
  - vertikaler Abstand „bestimmen“
  - Zeitraum mit Mindest- oder Höchständerungsrate
  - Winkel zwischen Seitenflächen „eines Körpers“
  - „Wahrscheinlichkeit für eine Einheit …“
- Zwei Definitionen erweitert.
- Eine Feldkorrektur (typ_neben von 2018-be-gk-cas-B1.2e).
- Typen 1417 → 1421, nach Lauf 28 weiter 1421.
- Selbstprüfung abi: 887 Zeilen aus 21 Heften, 8 Landes-Dubletten, 0 offene Posten.
- Selbstprüfung iqb: 1762 Zeilen, 43 Stapel vollständig.
- Alle Läufe aus einer frischen Kopie sind byteidentisch.

### Punkt 7: Sek-II-Nachzug (95b0f8b)

**Umfang:**
- 155 neue Zeilen (Teil 3: 85, Stapel 2017-ga-B-cas: 38, Hefte: 32) in 29 Sek-II-Einträgen.
- 27 neue Typen in vorhandenen Einheiten; keine neue Einheit, deshalb kein Vorschlag. Der Abschnitt „Sek-II-Nachzug“ in katalog/_vorschlaege-2026-09-29.md sagt das und passt den Vorschlag zu Katalogbefund 8.3 an.

**Alte Typnamen mitgezogen:**
- 13 Umbenennungen und die Zusammenziehung aus den Läufen 27 und 28.
- Niveauangaben aus den Läufen 26 und 27 in binomialverteilung, orthogonalitaet und schnittmengen.

**Neu gebaut:**
- themen.csv (Zählung, 41 Profilzeilen) und alle 68 Rohdateien.
- _pruefungswort-belege.md mit pruefungswort-belege-typen.txt.
- zwei Sek-II-Marken-Zeilen („Abitur LK“ an kurvenuntersuchung 5 und gleichungen-loesen 1).
- _verweise.md und die Sek-II-Tabelle in index.md.

**Prüfläufe:**
- `_pruef_katalog.py` über alle Einträge: ERGEBNIS „Befunde“ nur bei lineare-gleichungen und terme, wie vorher.
- `_pruef_struktur.py`: ok.
- `themen-pruef.py`: bestanden.
- `verweis-pruef.py`: kein neuer Befund.
- `marken-bau.py --probe`: „nichts zu ändern“.

**Nachprüfung durch den Hauptlauf:** Jede der 155 ids steht in einem Eintrag. 19 ids stehen mehrfach in einem Eintrag; nachgesehen: das sind Musterzeilen und Ermessensvermerke, keine doppelt eingefügten Zeilen.

**Gegenprobe im Wortlaut** (abitur/befund-cas-berlin-2026-09-28.md, Übersicht): „abweichende Teilaufgaben je Heft 16, 19, 16, 16; davon nur BE 5, 9, 2, 7; schon Zeile eines BB-CAS-Hefts 0, 9, 0, 13“. Erfüllt: Ist 16, 19, 16, 16; 5, 9, 2, 7; 0, 9, 0, 13.

**Gegenprobe Kennzahl 5:** „Kennzahl 5 vor dem Teil 28 (nacht-stand-2026-09-28.md, Teil 4); „Zeilensumme ≠ themen.csv" danach 0 Einträge“.
- **Abweichung vorher: 183 statt 28 von 3320.** Erklärung: Zwischen dem Stand vom 28.09. und dem Beginn von Punkt 7 sind 155 Originale neu dazugekommen, alle aus Teil 3 und Teil 4. Die übrigen 28 sind dieselben msa/fhr-Originale wie am 28.09. (25 × 2026-EBR, 2020-A-1a, 2023-A-2c, 2026-C-3b).
- **Nachher: 28 von 3320**, und „Zeilensumme ≠ themen.csv“ in **0 Einträgen**. Beide Werte erfüllt.

**Eigene Entscheidungen:**
- Die Vormerkungsregel hat Vorrang vor dem wörtlichen Umfang des Auftrags. Deshalb ist der Stapel 2017-ga-B (CAS) mit erfasst.
- 2018-be-gk-cas 3.2 a trägt den Poolverweis statt der Landes-Dublette, weil er wortgleich mit der WTR-Pooldatei ist (abi.md § 7). Die Schätzung folgt dem amtlichen Bereich I.
- Bei einem Zuschnitt zeigt der Vermerk „CAS-Nachtrag zu …“ auf genau eine WTR-Zeile.
- 2017-be-gk-cas 3.2 c bleibt „nur BE“, obwohl die Binomialtafel fehlt; bemerkung sagt es.
- Mehrdeutige Aufgaben mit beiden Lesarten in der Zeile: 2017 2.2 c, 1.1 f; 2018 1.2 g.

**Zwischenfall:** Beim Sek-II-Nachzug liefen die zwei ersten Hilfsagenten noch, als der Koordinator sechs neue startete. Drei Agenten meldeten die Kollision. Der Hauptlauf hat den älteren Agenten die bereits nachgezogenen Dateien gesperrt; der Koordinator hat jedem Eintrag genau einen Schreiber zugeordnet und alle 29 Einträge auf Doppelungen geprüft. Ergebnis: keine Doppelung, alle Prüfskripte ohne neuen Befund. Folgerung für künftige Aufträge: Hilfsagenten, die Unteragenten starten, erst fortsetzen, wenn keine Kinder mehr laufen (ListAgents).

**Offen, als Posten in faellig.md:**
- Eigene Aufgaben der Berliner LK-Hefte: Der bestehende Posten 2017-be-lk/2018-be-lk ist um die CAS-Fassungen und die 13 Teilaufgaben erweitert, statt einen zweiten Posten anzulegen.
- Nebenteile der Sek-II-Einträge: Zusatz mit den Stellen, die der Nachzug gemeldet hat, und dem veralteten _kursart-belege.md.
- Drei Etikettenbefunde für den nächsten Abgleichlauf.

**faellig.md:** Der Posten CAS-Nachtrag steht in § 4.

## Teil 5: marken-bau.py Sollwert kreis 1 (3e64629)

- **Umstellung:** Die GEGENPROBE-Zeile kreis 1 für den Typ „Kreis mit gegebenem Radius oder Durchmesser zeichnen“ steht auf „[OS 5–8, GYM 5–6]“.
- **Quelle im Skriptkopf:** bericht-marken.md Gegenprobe 4, mit den Typzeilen:
  - Mathematik 2023 Kl. 5
  - Mathematik heute Kl. 8
  - Elemente Kl. 5
  - LS 6
  - Fundamente 6 und 7
- **Läufe:** `--probe` meldet „nichts zu ändern“. Auch der schreibende Lauf ändert keine Datei.
- **faellig.md:** Posten in § 4.

**Gegenprobe im Wortlaut:** „alle GEGENPROBE-Zeilen melden „stimmt"“. Erfüllt: alle 8.

## Teil 6: Merkkasten Nullstellengleichung (c8c16ef)

**Befund:** Die Schreibweise „… (x) = 0 setzen“ stand nicht im Merkkasten von quadratische-gleichungen.md. Dort gibt es nur Gleichungen in Normalform und keine Nullstellengleichung einer Funktion. Sie stand in quadratische-funktionen.md, Einheit 4: „Nullstellen: p(x) = 0 setzen“ mit dem Beispiel „(x − 2)² − 16 = 0 → …“. Von dort übernahm das Blatt der Eingabe 7 „Setze f(x) = 0“.

**Umgestellt:**
- „Nullstellen: 0 = p(x) setzen – die Null tritt an die Stelle von p(x), der Term bleibt, wo er stand.“
- „0 = (x − 2)² − 16 → 16 = (x − 2)² → …“
- Änderungszeile im Kopf des Eintrags.
- quadratische-gleichungen.md bleibt unverändert.
- faellig.md: Posten in § 4.

**Gegenprobe im Wortlaut:** „grep „f(x) = 0" in beiden Merkkästen vorher und nachher, Zahlen in den Bericht; katalog/_pruef_katalog.py ohne neuen Fehler“.
- „f(x) = 0“: vorher 0 und 0, nachher 0 und 0. Der wörtliche grep trifft die Stelle nicht, weil die Funktion im Kasten p heißt.
- Schreibweise „p(x) = 0“: quadratische-funktionen vorher 1, nachher 0.
- `_pruef_katalog.py` und `_pruef_struktur.py`: Ausgabe gleich wie vorher.

## Teil 7: Vorschläge Sprossenregel (e439302)

**Neue Datei:** katalog/_vorschlaege-sprossen-2026-09-29.md, mit README-Zeile.

**Zählzeile:** „Einträge geprüft: 29 · Einheiten geprüft: 118 · Vorschläge: 6 (davon Einheitenfolge: 1) · Bestätigungen: 1“.

**Die sechs Vorschläge:**
- brueche-dezimalzahlen Einheit 3: Abkürzung vor dem Gleichnamigmachen.
- zinsrechnung Einheit 1: 1 %-Weg hinter dem Faktor.
- koerper Einheit 3: Rechteckgrundfläche hinter V = G · h.
- quadratische-gleichungen, Einheitenfolge: 1 Wurzelziehen → p-q-Formel → Nullprodukt → Sachaufgaben. Gründe dafür und dagegen stehen mit Lehrwerksstellen in der Zeile.
- quadratische-gleichungen Einheiten 2 und 3: Folgezeilen dazu.

**Bestätigung:** quadratische-funktionen Einheit 4.

**Kette:** abgelesen an „Für schwache Schüler › Sprossen je Verfahrenstyp“, so wie der Prompt sie liest (../blattbau/unterrichtsblatt.md § 2.1, 2.3 b). Die Typenzeile ist mitgelesen.

**Gegenprobe:** „quadratische-gleichungen muss einen Vorschlag oder eine Bestätigung zu Wurzelziehen, p-q-Formel und Satz vom Nullprodukt tragen“. Erfüllt: Zeile „Einheitenfolge“ und zwei Kettenzeilen.

## Teil 8: Vorschläge Katalogbefund 3–8 (008f79e)

**Neue Datei:** katalog/_vorschlaege-2026-09-29.md, mit README-Zeile.

**Zählzeile:** „Zählung: 6 Punkte · 22 vorgeschlagene Zeilen · 1 Zeile „kein Beleg gefunden““. Die Zeile ohne Beleg ist die Quartilregel in daten.

**Je Punkt:**
- Punkt 3: 2 Zeilen.
- Punkt 4: 5 Zeilen.
- Punkt 5: 3 Zeilen; Marken nur als Fundstellen mit Entscheidungsweg.
- Punkt 6: 5 Zeilen.
- Punkt 7: 2 Zeilen.
- Punkt 8: 5 Zeilen, LK-Vermerk.

Alle 22 Zeilen sind probeweise in einer Kopie eingesetzt worden. Die Prüfskripte meldeten dort keinen neuen Befund.

**Gegenprobe im Wortlaut:** „die Abweichung „Spannweite [OS 9]" gegen Einheitsmarke OS 6 muss mit beiden Fundstellen aus _klassen-belege.md im Abschnitt stehen“. Erfüllt.
- Typklammer: Z. 4276, „Spannweite … – Mathematik 2023 Kl. 9, S. 112: „Streumaße““.
- Einheitsmarke: Z. 4290, „OS: Kl. 6 (…)“.
- Ursache: Die Kl.-6-Stelle Z. 4246 nennt die Spannweite, ist aber nur als Typzeile von „Minimum und Maximum“ zugeordnet.

faellig.md: Die Posten Katalog 2 bis 8 tragen „Vorschlag liegt vor, Urteil im Chat“ mit Verweis auf die Vorschlagsdatei.

## Abschluss

**faellig.md** ist in jedem Teil im selben Commit nachgeführt.

Nach § 4 gegangen:
- Übersichtsblatt-Form (vertagt)
- Eichung 2017
- kreis 1
- Merkkasten
- Pool-Vormerkung 2018
- CAS-Nachtrag

Neu oder erweitert in § 2:
- Prüfstein nach v4.4
- eigene Aufgaben der Berliner LK-Hefte, WTR und CAS
- Etikettenbefunde
- Zusatz an den Nebenteilen der Sek-II-Einträge
- „Urteil im Chat“ an den Posten Katalog 2–8

Offen außerhalb dieses Auftrags (Beschluss Punkt 5): Auch die vier Abschnitte von katalog/_vorschlaege-2026-09-27.md warten auf das Urteil im Chat.

Standdatei und Auftrag liegen per git mv in archiv/; es gab keine Namensgleichheit.

Push origin drücken
