Modell: Opus 5.5 (claude-opus-5-5)

# Bericht Auftrag Nacht 2026-09-28

Auftrag und Standdatei: archiv/auftrag-nacht-2026-09-28.md, archiv/nacht-stand-2026-09-28.md. Sechs Teile erledigt, Teil 2 bis auf den 2018-Zweig: der Delta-Stapel 2018-ea-B (CAS) ist zweimal an der Eichschranke gescheitert und nicht erfasst (Fehlerregel), die Vormerkung 2018-bb-ea-cas-B3.1f bleibt als benannter Posten. Hilfsagenten (Opus) für die Stapel und den Abgleichlauf in Teil 2 und für Teil 4 (zwei Hälften), streng nacheinander, wo sie dieselben Dateien berührten; Teile 1, 3, 5, 6 und 7 selbst. Get-Date zeigte den ganzen Lauf den 26.09.2026 (10:09 bis 13:40); Daten in Dateien tragen das Auftragsdatum 28.09.2026, Uhrzeiten in der Standdatei Get-Date.

## Teil 1: Befund ablegen (Commit f6aebd6)

Angelegt: `befund-testlauf-2026-09-25.md` (Datei 2, wortgleich), `auftrag-nacht-2026-09-28.md`, `nacht-stand-2026-09-28.md`; README-Zeilen im Block Wurzel. faellig.md § 2: zwölf Posten – Katalog 1–8 und Werkzeug 1–4, Fundstelle je „befund-testlauf-2026-09-25.md, Katalog n / Werkzeug n“; Prompt, Vorlage und Beschluss ohne Posten.

Gegenprobe: keine im Auftrag.

Eigene Entscheidungen:
- Katalog 9 (Skizzenbeschreibung im Merkkasten) als Zusatz am bestehenden Posten „Anker-Kompositionsregel … Skizzenbedarf“, kein zweiter Posten – die Befundzeile sagt selbst „Posten besteht“, faellig.md duldet keine Doppelposten.
- Drei Vorlagen-Posten nach § 4, weil blattbau sie erledigt hat (Befunddatei Vorlage 8, Repo blattbau): `\streifenfeld` (1809394), Zweigzeile/Abhakseite/Verzeichniszeile (96b25f5, 1809394), `.gitattributes` in blattbau (eaa74fc).

## Teil 2: Stapel 2017-ea-B, Delta-Stapel CAS, Vormerkungen (Commits 42c167a, 990a800, cc451d5, b90e574)

Vorab gemessen: iqb-quellen.csv führt die Spalte `dateidublette_von` für alle Teil-B-Dateien; ein Nachlauf von `scanne_teil_b` (offline, aus dem Cache hefte/iqb/) ergab keine Abweichung zur CSV, also keinen Skriptlauf mit Schreiben. Keine CAS-Datei von 2017-ea-B und 2018-ea-B ist wortgleich mit einer WTR-Datei (Ähnlichkeit höchstens 0,85; das einzige nahe Paar 2018 Stochastik CAS 1 ~ WTR 1, 0,988, hat andere Zahlen und ist nach iqb.md § 7 keine Dateidublette).

| Stapel | Zeilen | neue Typen | Poolquote / Landeshefte | „?“ | ersatzweise | Dateidubletten | Eichung erster Lauf → Ende |
|---|---|---|---|---|---|---|---|
| 2017-ea-B (WTR), 8 Dateien, 275 BE | 82 | 40 | kein erfasstes Landesheft stellt den Zweig; 2017-be-lk 2.1 (nicht erfasst) = AG/LA (A2) WTR 2 | 0 | 0 | 0 | 57 von 82 (70 %) → 71 (87 %), vierzehn Korrekturen |
| 2017-ea-B (CAS), 6 Dateien, 200 BE | 55 | 13 | nach Lauf 25: 4 Poolzeilen wortgleich in 5 Landeszeilen, 2 abgewandelt in 4; AG/LA (A2) CAS 1 teilt sieben Teilaufgaben mit WTR 1 | 0 | 2 (Kurvenlänge) | 0 | 34 von 55 (62 %; eigene 28 von 48) → 47 (85 %), dreizehn Korrekturen |
| 2018-ea-B (CAS), 9 Dateien, 300 BE | – (geplant 85) | – (geplant 18) | Landesheftabgleich im Arbeitsstand | – | – | 0 | 57 von 85 (67 %) → 67 (79 %) nach zehn Korrekturen – **gescheitert** |

Abgleichlauf 25 (abitur-abgleich.py v0.26): neun Feldkorrekturen – 2017-bb-ea-cas-B3.1c „Dublette von:“, e, f „Abgewandelt von:“ (Satz zur Ebene F im Aufgabenstamm); die WTR-Zeilen 2017-bb-ea-B3.1 a, b, c, d „Dublette von:“ (c mit 5 statt 4 BE), e, f „Abgewandelt von:“, jeweils auf 2017MerhoehtBAGLAA2CAS2; Typ von B3.1b auf den Pooltyp. Dazu vier Zusammenziehungen und neun Umbenennungen, Typenliste 1398 → 1393, Liste alt → neu in abi-pruefungen.md und iqb-pruefungen.md § 5; alte Namen in sieben Sek-II-Einträgen mitgezogen. Poolquote 2017-bb-ea danach 10 von 36 Zeilen, 32 von 185 BE (17 %) wortgleich, 2 Zeilen 8 BE abgewandelt; 2017-bb-ea-cas 1 von 14 Zeilen, 4 von 87 BE, aufs Heft 31 von 185. Selbstprüfung beider Bau-Skripte bestanden, jeder Lauf aus frischer Repo-Kopie byteidentisch.

Gegenprobe im Wortlaut (iqb-pruefungen.md § 2, abi-pruefungen.md § 2): „2017-ea-B (WTR) 14 Dateien“ – erfüllt (Zeile „| 2017-ea-B (WTR) | 8 von 14 | …“: 8 WTR- und 6 CAS-Dateien). „nach Punkt 4 steht in keinem abi-Katalogeintrag mehr „Poolaufgabe (nicht erfasst)“ (grep über abitur/abi-katalog.csv: 0 Treffer)“ – **Abweichung: 1 Treffer, 2018-bb-ea-cas-B3.1f**. Erklärung: Punkt 3 (2018-ea-B-cas) ist gescheitert, damit entfällt der 2018-Teil von Punkt 4; die drei 2017-Vormerkungen sind geschlossen.

Eigene Entscheidungen:
- Punkt 3 als „offen“ nach der Fehlerregel: erster vollständiger Stand 57 von 85, nach Prüfung und Wiederholung 67 von 85 – zweimal unter 85 %. Die Schwelle wurde nicht geändert (iqb.md § 7: gilt für jeden Stapel gleich; die Überschreibung je Stapel hat der Lehrer am 17.09. zurückgebaut) und keine weiteren Korrekturen erzwungen – genau die Frage, ob Korrekturen die Quote verfälschen, liegt in Teil 6 beim Chat. Befund in iqb-pruefungen.md § 4, Änderungslog § 5; Arbeitsstand (blinde und geprüfte Schätzungen, Typwahl, Landesheftabgleich, `eichung.py`) unter abitur/arbeitsstand/2018-ea-B-cas/ (README), damit ein Wiederanlauf nach der Entscheidung nicht neu anfangen muss.
- 2017-bb-ea-cas-B3.1 e, f als „Abgewandelt von:“, weil der Aufgabenstamm im Heft einen zusätzlichen Satz trägt (streng wortgleich heißt Dublette).
- 2017-bb-ea-B3.1c: meine erste Vorgabe „Abgewandelt von:“ (nur andere BE) widersprach abi.md § 7 („bei anderer Punktzahl nennt bemerkung die BE“); vor dem Commit berichtigt, Lauf 25 aus dem HEAD-Stand neu gefahren – jetzt „Dublette von:“ mit „5 statt 4 BE“.
- Korrekturen der Schätzungen in beiden 2017-Stapeln nur, wo der Erfasser eine Regel der engen Fassung oder der Deutungsliste als falsch angewandt benennt; der erste Lauf ist je Stapel festgehalten.

Offen: Vormerkung 2018-bb-ea-cas-B3.1f und die Poolverweise der WTR-Zeilen 2018-bb-ea-B3.1 a–f (Posten in faellig.md § 2, Entscheidung beim Lehrer: Stapel mit dokumentierter Unterschreitung erfassen, Schwelle begründet ändern, Deutungsliste um die zwei Kandidaten erweitern oder Vormerkung stehen lassen). Hinweise der Erfasser: 2017-be-lk 2.1 = Pooldatei 2017MerhoehtBAGLAA2WTR2, 2018-be-lk 2.2 = 2018MerhoehtBAGLAA2WTR1 (Verweise fällig, wenn die Hefte erfasst werden; Zusatz am Posten in faellig.md); „Kurvenlänge“ als dritte Themenlücke (ersatzweise).

## Teil 3: Berliner CAS-Hefte 2017/2018 (Commit a1d8012)

Neu: `abitur/befund-cas-berlin-2026-09-28.md` (je Heft Tabelle Teilaufgabe · WTR-Gegenstück · BE · wortgleich/abweichend · Art · Unterschied) und das Messwerkzeug `werkzeuge/cas-vergleich.py` (README). Arten: Zahl, Werkzeug, Auftrag, Zuschnitt, ganze Aufgabe, nur BE; „wortgleich“ heißt Text gleich (redaktionell vermerkt) und gleiche BE, wie „uebernommen“ im Nachtragsmodus.

Abweichende Teilaufgaben je Heft: **2017-be-gk-cas 16 von 34, 2017-be-lk-cas 19 von 36, 2018-be-gk-cas 16 von 37, 2018-be-lk-cas 16 von 43**; davon nur BE 5, 9, 2, 7. In den LK-Heften sind 22 der 35 abweichenden Teilaufgaben schon Zeilen der Brandenburger CAS-Hefte (2017-be-lk-cas 1.2, 2.2, 3.2 = 2017-bb-ea-cas 2.2, 3.1, 4.2; 2018-be-lk-cas 1.1, 1.2, 2.1 = 2018-bb-ea-cas 2.1, 2.2, 3.1); ohne vorhandene Zeile bleiben 16 + 10 + 16 + 3 = 45.

Gegenprobe im Wortlaut (abi-pruefungen.md § 2): „Seiten je Heft 8, 9, 10, 9“ – erfüllt (pdfinfo: 8, 9, 10, 9).

Eigene Entscheidungen: Zwischenstämme gehören zur folgenden Teilaufgabe (2017-be-lk 3.2 d: 6 % statt 5 % Stornierungen); bei Formelsatz entschied das Seitenbild (2018-be-lk 1.1, 2.1). Poolbezug als Befund: 2017-be-gk-cas 3.1 ist die CAS-Poolfassung 2017MgrundlegendBStochastikCAS (Reserve); 2018-be-lk-cas 3.2 Brillenträger ist die WTR-Fassung, nicht die Brandenburger CAS-Fassung. Kein Katalogeintrag, Urteil im Chat (Zusatz am Posten CAS-Nachtrag).

## Teil 4: Sek-II-Einträge nachgezogen (Commit 3e956a5)

39 Einträge, 257 neue Zeilen (27.09.: 120; 28.09.: 137 aus Teil 2), 74 neue Typen – alle in vorhandenen Einheiten, deshalb kein katalog/_vorschlaege-2026-09-28.md. Dazu themen.csv-Zählung (36 Profilzeilen; neue Zeile iqb „Linearkombination und lineare Abhängigkeit“ 1/1), alle 68 Rohdateien, `_pruefungswort-belege.md` (163 Sek-II-Einheiten), Marken (drei Zeilen: extremalprobleme „Abitur LK“, rekonstruktion-von-funktionsgleichungen und kombinatorik „Abitur GK“), `_verweise.md`, index.md Sek-II-Tabelle.

Neue Typen je Eintrag – Analysis: kurvenuntersuchung 1, funktionsscharen-und-ortskurven 8, funktionsklassen-und-eigenschaften 6, tangente-normale-schnittwinkel 4, flaecheninhalt-durch-integration 2, gleichungen-loesen 2, ableitung-und-aenderungsrate 2, rekonstruktion-von-funktionsgleichungen 2, stammfunktion-und-hauptsatz 3, ableitungsregeln 1, rekonstruktion-von-bestaenden 2, extremalprobleme 1, ableitungsgraph-und-funktionsgraph 1, rotationsvolumen 3, uneigentliche-integrale 1, umkehrfunktion 1, grenzwerte-und-verhalten-im-unendlichen 0. Geometrie und Stochastik: spiegelung 1, orthogonalitaet 1, konfidenzintervalle 1, normalverteilung-und-sigma-regeln 1, kombinatorik 1, hypothesentests 2, kenngroessen-von-verteilungen 2, zufallsexperimente-und-pfadregeln 2, ebenen 1, lagebeziehungen 2, flaecheninhalt-und-volumen-im-raum 2, skalarprodukt-und-winkel 1, geraden 3, punkte-und-strecken-im-koordinatensystem 5, abstaende 4, matrizen-und-uebergangsprozesse 5; ohne neuen Typ: schnittmengen, vektoren-und-rechenoperationen, scharen-von-geraden-und-ebenen, linearkombination-und-lineare-abhaengigkeit, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung. Vorschläge neue Einheiten: keine.

Gegenprobe im Wortlaut (nacht-bericht-2026-09-27.md Teil 10): „Kennzahl 5 vor diesem Teil 168; 31 Einträge mit Zeilensumme-Abweichung“ – erfüllt am Stand vor Teil 2 (168 von 3028, 31 Einträge, beide nachgemessen); zu Beginn von Teil 4 stand Kennzahl 5 bei 305 von 3165, weil Teil 2 137 Zeilen hinzugefügt hatte. **Kennzahl 5 vorher 168 (bzw. 305) → nachher 28 von 3165** (Ziel ≤ 48 erfüllt; der Rest sind msa- und fhr-Originale: 25 × 2026-EBR, 2020-A-1a, 2023-A-2c, 2026-C-3b); „Zeilensumme der Profilliste ≠ themen.csv“ in **0 Einträgen** (vorher 31). `themen-pruef.py` bestanden, `_pruef_struktur.py` ok, `_pruef_katalog.py` für alle Einträge ohne Zeilensummen-Meldung (ERGEBNIS „Befunde“ nur bei lineare-gleichungen und terme, schon bei HEAD so), `verweis-pruef.py` ohne neuen Befund, `marken-bau.py --probe` danach „nichts zu ändern“.

Eigene Entscheidungen: Teil 4 erst nach Teil 2, damit die neuen Stapelzeilen und die Umbenennungen von Lauf 25 in einem Nachzug stehen; zwei Hälften nacheinander (Analysis, dann Geometrie/Stochastik mit den Schlussbauten). Jede Ermessenszuordnung steht in den „Offenen Punkten“ des Eintrags.

Offen (neuer Posten in faellig.md § 2): Sprossen mit altem Niveau oder altem Typ (linearkombination Einheit 2, skalarprodukt Einheit 2 und 3), Nebentypen-Zeilen, alte Zeilenzahlen in [FD]-Zeilen, index.md-Zeile matrizen („ungeklärt“ gegen „geklärt“).

## Teil 5: Prüfskript und Marken-Gegenprobe (Commit 0062451)

1. `werkzeuge/blatt-pruef.py` v0.4: `\swz` und `\swa` in TEILZAEHLER; Teilaufgaben im Beispielblock (`\begin{beispiel}`) zählen nicht (die Vorlage setzt den Buchstaben zurück); Kennzahlen 13–17 je Blatt für `\verfahren`, `\anweisung`, `\rechenplatz` (mit Zeilensumme), Umgebung `beispiel`, `\streifenleer[0]` – im Abschnitt des Blatts und als Tabelle „Bausteine Stufe 6“, beides nur für Blätter mit diesen Bausteinen. Alte Blätter byteidentisch (alle 22 PDFs unter blaetter/; Testlauf außer Eingabe 3); am Probeblatt der Vorlage gezählt: `\verfahren` 2, `\anweisung` 1, `\rechenplatz` 1 (2 Zeilen), beispiel 1, `\streifenleer[0]` 1 – gleich der Rohzählung im Quelltext.
2. `werkzeuge/marken-bau.py`: GEGENPROBE lineare-funktionen 4 „P10“ und quadratische-gleichungen 2 „GYM Kl. 8–9“ (Quellen im Skriptkopf: _pruefungswort-belege.md 3 von 13, _klassen-belege.md Elemente Kl. 8); beide melden „stimmt“, `--probe` „nichts zu ändern“.
3. blaetter/kennzahlen.md und die Testlaufdatei nicht neu gebaut; Nachweislauf nach scratch.

Gegenprobe im Wortlaut (bericht-testlauf-2026-09-25.md): „Eingabe 3 Teilaufgaben bisher 34; Quelltext zählen (\teil, \swz, \swa, \swfrage, \gl) und beide Zahlen in den Bericht“ – bisher 34 (Bericht 25.09.; v0.3 zählte 38 mit `\swfrage`), **jetzt 173**; Quelltext in den Hauptnummern: 28 `\teil` + 126 `\swz` + 9 `\swa` + 4 `\swfrage` + 6 `\gl` = 173 (im ganzen Quelltext mit Vorspann und Begleitteil 179).

Eigene Entscheidungen: Die Prüfung der Marken-Zeile verlangt Schulformangabe und Prüfungswort als ganzen Teil („P10“ trifft nicht „P10 oft“; eine Spanne darf ihre Reihenliste tragen) – sonst wäre der neue Sollwert „P10“ auch bei „P10 oft“ erfüllt. kreis 1 (Typ) weicht weiter ab (Soll aus der Übergabe vom 26.09., nicht Gegenstand der Chat-Entscheidung) – neuer Posten in faellig.md.

## Teil 6: Eichungsfrage Pool 2017 (Commit ca3237b)

Neu: `abitur/befund-eichung-2017-2026-09-28.md` – die sechzehn Abweichungen von 2017-ga-B (WTR) mit erster Schätzung, amtlichem Bereich, jetzt, Grund aus bemerkung und Regel (elf korrigiert: fünf nach oben, sechs nach unten; fünf stehen, alle unter dem amtlichen Bereich; fünf Korrekturen stützen sich auf die amtlichen Bereiche anderer Zeilen desselben Typs), die fünf von 2017-ga-A (zwei korrigiert, drei stehen), zum Vergleich 2017-ea-B WTR (vierzehn Korrekturen, davon elf nach unten), 2017-ea-B CAS (dreizehn) und der gescheiterte 2018-ea-B CAS; darunter die Eichung je Pooljahr und Niveau (erster Lauf, wo die Logs ihn nennen: 2017-ga-A 15, 2017-ga-B 23, 2018-ga-B 44 von 53, 2022-ga-B 35 von 52, dazu die drei Stapel dieses Auftrags; heute: 2017 grundlegend 51 von 59, 2017 erhöht 140 von 160, Bestand 1526 von 1638). Kein Urteil.

Gegenprobe im Wortlaut (iqb-pruefungen.md § 2): „2017-ga-B 34 von 39, erster Lauf 23 von 39; 2017-ga-A 17 von 20, erster Lauf 15“ – erfüllt.

Eigene Entscheidung: Der Auftrag nennt für 2017-ga-A „drei Abweichungen, zwei korrigiert“; der erste Lauf hatte fünf (15 von 20) – die Tabelle zeigt alle fünf und sagt es.

## Teil 7: Prüfstein Übersichtsblatt (Commit 3474faa)

Neu unter `blaetter/uebersicht/`: `quadratische-funktionen/2026-09-28/` und `prozentrechnung/2026-09-28/` je mit `src/uebersicht.tex`, `pdf/uebersicht.pdf`, Seitenbild `pdf/uebersicht.png` (pdftoppm, 100 dpi) und `protokoll.txt` (Quelle je Block und je Tabellenzeile). quadratische-funktionen: vier Kastenblöcke (Einheit 1–4), Koordinatensystem mit p(x) = x² und q(x) = (x + 3)² − 1 (Beispiel aus Kasten 2), Tabelle „Form · Verfahren zur Nullstelle · wann“ mit Normalparabel, Scheitelpunktform, Normalform, Normalform ohne q (Nullprodukt), allgemeine Form; drei Kompilierläufe. prozentrechnung (Verfahrensthema): fünf Kastenblöcke, Streifen (45 % ≙ 36 €, Kasten 4), Tabelle „Gesucht · Rechnung · wann“; zwei Kompilierläufe. `.gitattributes`: `*.png binary` (sonst hätte `* text eol=lf` die PNG verändert). index.md unberührt; Posten „einsortieren.py um Sorte uebersicht erweitern“ und „Form an den Prüfsteinen entscheiden“ in faellig.md.

Gegenprobe im Wortlaut (katalog/quadratische-funktionen.md): „die Zahl der Kästen im Eintrag und die Zahl der Blöcke auf der Seite müssen gleich sein; pdfinfo: 1 Seite“ – erfüllt: 4 Kästen, 4 Blöcke, 1 Seite; prozentrechnung ebenso 5 = 5, 1 Seite.

Eigene Entscheidungen: Die Zeilen „Formelsammlung: …“ und „Quelle: …“ der Kästen sind keine Regelzeilen und fehlen; in der Prozentrechnung stehen die Formeln der Formelsammlungszeilen in der Tabelle. Der Name „allgemeine Form a·x² + bx + c“ steht in keinem Kasten (Auftrag und Typenzeile Einheit 3), das Verfahren (normieren) im Kasten 3 von quadratische-gleichungen.md. Der Satz vom Nullprodukt als eigene Tabellenzeile „Normalform ohne q“. Der Kasten zum Lösen aus quadratische-gleichungen.md ist in die Tabelle gegangen, nicht als fünfter Block – die Gegenprobe zählt die Kästen des Eintrags quadratische-funktionen.md.

## Abschluss

faellig.md: Teil 1 zwölf Posten; nach § 4: Pool-Vormerkungen 2017, Sek-II-Nachzug, blatt-pruef.py, drei Vorlagen-Posten; Zusatz „Befund liegt vor, Urteil im Chat“ an den Posten CAS-Nachtrag (Teil 3) und Eichung Pool 2017 (Teil 6); neue Posten: Pool-Vormerkung 2018 (Rest), marken-bau-Gegenprobe kreis 1, einsortieren.py Sorte uebersicht, Formentscheidung Übersichtsblatt, Nebenteile der Sek-II-Einträge. Standdatei und Auftrag nach archiv/ (git mv, keine Namensgleichheit). Nichts gelöscht, kein Push, kein Prompt und nichts unter blaetter/testlauf-*/ oder ../blattbau geändert.

Push origin drücken
