# IQB-Aufgabenpool Mathematik – Stapel und Erfassungsstatus
Stand 13.09.2026 · Profil iqb · gepflegt vom Katalog-Prompt

## 1 Quelle

Gemeinsame Abituraufgabenpools der Länder, Fach Mathematik, IQB. Dateien und
Kennungen in iqb-quellen.md und iqb-quellen.csv; Aufbau, Kürzel und Regeln in
iqb.md. Amtliche Lösungen liegen für jede Aufgabe vor (Erwartungshorizont);
der Standardbezug liefert afb_amtlich. Amtliche Vorgaben stehen gesondert in
abi-vorgaben.md.

## 2 Stapel Prüfungsteil A

Ein Stapel ist ein Prüfungsteil eines Pooljahrs auf einem Niveau (iqb.md § 7);
Reihenfolge von oben nach unten. „weiter" ist der nächste Stapel mit Status
„nicht erfasst".

| Stapel | Dateien | Status |
|---|---|---|
| 2026-ga-A | 19 (18 + 1 Dublette) | **erfasst 2026-09-13, 33 Zeilen** · 34 Typen neu · Eichung 30 von 33 |
| 2026-ea-A | 20 | nicht erfasst |
| 2025-ga-A | 17 (16 + 1 Dublette) | nicht erfasst |
| 2025-ea-A | 20 (19 + 1 Dublette) | nicht erfasst |
| 2024-ga-A | 17 (16 + 1 Dublette) | nicht erfasst |
| 2024-ea-A | 19 | nicht erfasst |
| 2023-ga-A | 14 (13 + 1 Dublette) | nicht erfasst |
| 2023-ea-A | 18 | nicht erfasst |
| 2022-ga-A | 14 | nicht erfasst |
| 2022-ea-A | 17 | nicht erfasst |
| 2021-ga-A | 13 (11 + 2 Dubletten) | nicht erfasst |
| 2021-ea-A | 19 (17 + 2 Dubletten) | nicht erfasst |
| 2020-ga-A | 10 | nicht erfasst |
| 2020-ea-A | 15 | nicht erfasst |
| 2019-ga-A | 11 | nicht erfasst |
| 2019-ea-A | 10 | nicht erfasst |
| 2018-ga-A | 12 | nicht erfasst |
| 2018-ea-A | 12 | nicht erfasst |
| 2017-ga-A | 10 | nicht erfasst |
| 2017-ea-A | 11 | nicht erfasst |
| bsp-ga-A | 16 (12 + 4 Dubletten) | nicht erfasst |
| bsp-ea-A | 14 (12 + 2 Dubletten) | nicht erfasst |

Dubletten: wortgleiche Dateien unter beiden AG/LA-Alternativen (iqb.md § 7,
Spalte dublette_von in iqb-quellen.csv); sie bekommen keine Zeile. Teil A hat
damit 313 zu erfassende Aufgaben.

Kennzahlen je Stapel (Zeile „Kennzahlen:" aus iqb-bau.py; Grundlage für die
Schwellenwerte nach drei Stapeln, iqb.md § 7):

| Stapel | Zeilen | Typen verwendet | davon neu | Eichung | „?" | ersatzweise |
|---|---|---|---|---|---|---|
| 2026-ga-A | 33 | 34 | 34 (100 %) | 30 von 33 (91 %) | 0 | 0 |

## 3 Zurückgestellt

Prüfungsteil B (296 Dateien, 20 Stapel Jahr-Niveau-B plus zwei mit
Beispielaufgaben) liegt, bis Teil A durch ist und die Kennzahlen stehen. Die
Kürzel für Teil B sind in iqb.md § 4 vorläufig festgelegt.

## 4 Befunde

**Sondierung 13.09.2026.** 624 Dateien, Kennungen eindeutig zerlegbar. Der
Standardbezug ist eine Matrix Teilaufgabe × K1–K6 mit I, II, III in den Zellen –
bis zu sechs Bereiche je Teilaufgabe, nicht einer. Das Rechnerkürzel in Teil B
heißt 2017–2021 CAS, ab 2022 MMS. AG/LA hat zwei Alternativen: A1
Vektorgeometrie ohne Ebenen mit Matrizen, A2 mit Geraden, Ebenen, Abständen
(die Berlin-Brandenburger Fassung).

**Probelauf 2026MgrundlegendAAnalysis11.** Zwei Teilaufgaben, 5 BE, beide
Zeilen ohne „?", Eichung 2 von 2 (a: geschätzt I, amtlich I; b: geschätzt II,
amtlich I|II). Der 37-Feld-Satz trägt den Pool ohne Änderung: afb_amtlich ist
gefüllt, titel hält die Alternative A1/A2, aufgabe die Aufgabengruppe, bemerkung
die Standardbezug-Zeile. Nichts geschrieben; die zwei Zeilen gingen mit dem
Stapel 2026-ga-A in den Katalog.

**Stapel 2026-ga-A.** 19 Dateien, davon eine Dublette; 18 Aufgaben, 33 Zeilen,
alle 5 BE je Datei bestätigt, kein „?", kein „ersatzweise". Lauf aus frischer
Kopie byteidentisch, Selbstprüfung über den Bestand bestanden.

**Dubletten im Pool.** Aufgaben, die für beide AG/LA-Alternativen taugen,
nennen in der Kurzbeschreibung nur „AG/LA" und liegen wortgleich unter A1 und
A2 (2026MgrundlegendAAGLAA112 = …212). Der erste Textvergleich des Abschnitts
„1 Aufgabe" über alle 328 Teil-A-Dateien fand 13 Paare; die Absicherung vom
selben Tag (Auftrag des Lehrers) verglich alle drei Abschnitte – Aufgabe,
Erwartungshorizont, Standardbezug – und zusätzlich die Bildobjekte: bei allen
Paaren gleich, ein Paar nur in der Bildkodierung verschieden
(BeispielaufgabenMerhoehtAAGLAA111/211), eines nur im Leerraum („1: 3" gegen
„1:3", 2024MgrundlegendAAGLAA112/212). Der Scan vergleicht seitdem alle drei
Abschnitte ohne Leerraum und findet 15 Paare, alle AG/LA; sie stehen in
iqb-quellen.csv (dublette_von). Eine Fassung mit gleicher Aufgabe, aber
anderem Erwartungshorizont oder Standardbezug gibt es in Teil A nicht; die
Regel dafür (eigene Zeile, geteilter Typ) steht in iqb.md § 7. Sechzehn
Teil-A-Dateien haben drei Seiten (Bewertungshinweise rutschen auf Seite 3),
die Seitenzahl steht in iqb-quellen.csv.

**Ungegliederte Aufgaben.** Vier der 18 Aufgaben haben keine
Teilaufgabenbuchstaben, alle in Gruppe 2 (AGLAA12, AGLAA221, Stochastik21,
Stochastik22 mit je 5 BE); die beiden Analysis-Aufgaben der Gruppe 2 sind
gegliedert. Nach Kern § 4 eine Zeile;
teilaufgabe leer, id gleich Kennung. Auch der Standardbezug lässt die
Teilaufgabenspalte leer.

**Lineare Gleichungssysteme unter AG/LA.** 2026MgrundlegendAAGLAA12 ist ein
reines LGS; der Pool führt es unter AG/LA (A1), abi.md § 5 führt LGS unter
Analysis. Das Thema steht jetzt in beiden Listen von iqb.md § 6.

**Eichung 2026-ga-A: 30 von 33.** Drei Abweichungen: Analysis 1.4 a (Graph der
Funktion vom Ableitungsgraphen unterscheiden) geschätzt II, amtlich I;
Analysis 2.1 b (Produktregel mit Werten aus dem Graphen) geschätzt II, amtlich
III; Stochastik 2.2 (n und p aus μ und σ) geschätzt II, amtlich III. Muster:
die eigene Schätzung hält Ablesen plus Regelanwendung für II, der
Standardbezug setzt Kombinieren mehrerer Regeln (K2, K4) auf III. Zu wenig
Zeilen für eine Regeländerung; nach drei Stapeln prüfen.

**Typen.** 34 neue Typen bei 34 verwendeten, einer nur als typ_neben
(Orthogonalität von Gerade und Ebene über Normalen- und Richtungsvektor
begründen). Ein Etikett aus abi-typen.csv übernommen: Punktprobe an einer
Ebenengleichung durchführen. Kurzaufgaben des Teils A tragen je Teilaufgabe
fast immer nur eine Leistung; typ_neben ist in 2 von 33 Zeilen belegt, in den
abi-Kontextaufgaben war es ein Drittel.

**Kurzbeschreibung gegen Kennung.** Bei den Dubletten nennt die Kurzbeschreibung
das Sachgebiet als „AG/LA" ohne Alternative, die Fußzeile aber AGLA(A1) bzw.
AGLA(A2). titel folgt der Kennung (iqb.md § 4).

## 5 Änderungslog

| Datum | Änderung |
|---|---|
| 2026-09-13 | 2026-ga-A vollständig erfasst: 33 Zeilen aus 18 Dateien (eine Dublette ohne Zeile), Katalog 33 Zeilen, Typenliste 34. Alle 18 Punktsummen gegen die BE-Spalte geprüft (je 5), Lauf aus frischer Kopie byteidentisch, Selbstprüfung bestanden, Eichung 30 von 33. iqb.md v0.2: § 4 ungegliederte Aufgaben und titel bei „AG/LA", § 6 Lineare Gleichungssysteme auch unter Analytische Geometrie, § 7 Dubletten, § 8 aus dem Katalog. iqb-quellen.csv um seiten und dublette_von ergänzt (Scan aller 328 Teil-A-Dateien: 13 Dublettenpaare, 16 Dateien mit drei Seiten); iqb-quellen.py angelegt. iqb-bau.py v0.2: Dubletten, ungegliederte Aufgaben, Seitenzahl aus der Quelle. Befunde in § 4. |
| 2026-09-13 | Profil iqb angelegt (iqb.md v0.1, iqb-quellen.md, iqb-quellen.csv, iqb-bau.py v0.1, diese Datei). Probelauf an 2026MgrundlegendAAnalysis11 bestanden. Schwellenwerte nach iqb.md § 7 als Vorschlag. |
