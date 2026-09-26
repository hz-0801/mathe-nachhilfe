# PROFIL IQB – Gemeinsame Abituraufgabenpools der Länder, Mathematik
Version 1.17 · 29.09.2026 · Kennung iqb · gilt mit Kern v0.9 (Schema-Version 2)
Änderungen gegenüber 1.16 (Auftrag Nacht 2026-09-29, Teil 2; beschluss-2026-09-26.md Punkt 2): § 7 Deutungsliste um Eintrag (f) erweitert – „Mindestanzahl oder Mindestumfang für eine Mindestwahrscheinlichkeit bestimmen = III" (Belege: die fünf Poolfälle aus iqb-pruefungen.md § 4, alle amtlich III; die Bestandsprüfung fand einen sechsten, 2017-ea-B CAS Stochastik 1 Aufgabe 4, ebenfalls III). Der Kandidat „vom Text verlangte Fallunterscheidung ist amtlich II" ist nicht aufgenommen, bis er Belegzahlen hat. Fünf Poolschätzungen und eine wortgleiche Landeszeile per abitur-abgleich.py Lauf 26 auf III gesetzt (Grund in bemerkung); Eichung über den Bestand 1526 → 1531 von 1638. Keine Schwelle geändert; die Bindung iqb.md v1.13 im Kopf von iqb-bau.py v1.9 bleibt sachlich gültig.
Änderungen gegenüber 1.15 (Auftrag Nacht 2026-09-28, Teil 2 Punkt 2): § 1 Bestand nachgezogen – Delta-Stapel 2017-ea-B (CAS, 55 Zeilen) wegen der Landesheftverweise aus 2017-bb-ea-cas B3.1 geöffnet (keine Dateidublette, alle sechs CAS-Dateien, Abbruchkriterium unberührt); Stand 1639 Zeilen in 41 Stapeln, 1398 Typen. Keine Regel geändert; die Bindung iqb.md v1.13 im Kopf von iqb-bau.py v1.9 bleibt sachlich gültig.
Änderungen gegenüber 1.14 (Auftrag Nacht 2026-09-28, Teil 2 Punkt 1): § 1 Bestand nachgezogen – Reserve-Stapel 2017-ea-B (WTR, 82 Zeilen) wegen der Landesheftverweise aus 2017-bb-ea-cas B3.1 geöffnet (WTR-Zweig vor dem CAS-Delta, Abbruchkriterium unberührt); Stand 1584 Zeilen in 40 Stapeln, 1385 Typen. Keine Regel geändert; die Bindung iqb.md v1.13 im Kopf von iqb-bau.py v1.9 bleibt sachlich gültig.
Änderungen gegenüber 1.13 (Auftrag Nacht 2026-09-27, Teil 10): § 1 Bestand nachgezogen – Reserve-Stapel 2017-ga-A (20 Zeilen) und 2017-ga-B (WTR, 39 Zeilen) wegen Landesheftverweisen des Hefts 2017-be-gk geöffnet (Abbruchkriterium unberührt); Stand 1502 Zeilen in 39 Stapeln, 1344 Typen. Keine Regel geändert; die Bindung iqb.md v1.13 im Kopf von iqb-bau.py v1.9 bleibt sachlich gültig.
Änderungen gegenüber 1.12 (Auftrag F, Punkt 1 und 2): Kernbindung v0.9 – der Kern nennt in § 1 die msa-Dateien mit Präfix; für dieses Profil ohne Folge. Punkt 2: das Abgleichskript heißt abitur-abgleich.py (bis 17.09.2026 abgleich.py, bis Abgleichlauf 11 iqb-abgleich.py; Familienname wie abitur-typen.csv), Verweise in § 2, § 7, § 9 nachgezogen. Punkt 5: Kern § 6 setzt Zeilenthema = Typthema als Regel (bisher Verweis auf das Profil) und § 5 die Eichung als Kennzahl nur bei amtlichen Anforderungsbereichen – für dieses Profil ohne Änderung (abitur-vokabular.md § 4, § 7). Punkt 6: Kern § 7 Selbstprüfung als Bedingung eines vollständigen Profils – iqb-bau.py hat sie.
Änderungen gegenüber 1.11 (Auftrag E, Punkt 1, 3 und 4; Punkt 4: Begriffe – Dateidublette und Aufgabendublette statt Dublette für Datei und Aufgabe, Spalte dateidublette_von, Vormerkung statt Vermerk/Vorstufe, WTR-Fassung statt WTR-Zwilling, Schnitt statt Typenschnitt, Abgleichlauf bei erster Nennung; Punkt 3: unsichtbares Zeichen U+FEFF vor der ersten Beispielzeile in § 8 entfernt): überholte Aussagen auf den Stand vom 17.09.2026 – § 1 Bestand nach Abgleichlauf 23 und Zusammenführung mit abi als vollzogen; § 4 „vorläufig" bei den Kürzeln für Teil B gestrichen (seit dem Probestapel geltend); § 7 Schwellenwerte als gesetzt, Schranke neue Typen; Messgeschichte der Deutungsliste als eigener Befund vom Regelteil getrennt; § 9 erledigte Punkte gestrichen, Eichungsfrage beantwortet.
Änderungen gegenüber 1.10 (Auftrag D, Teil 7): § 7 Regel „Eine Vormerkung
überlebt keinen Auftrag" – ein Reserve-Stapel mit Landesheftverweisen wird
im selben Auftrag erfasst.
Änderungen gegenüber 1.9 (Auftrag D „Namensschema, Erweiterbarkeit,
Begründungen", Teil 2): § 6 Geltung je Zielprüfung in eigenen Dateien
abi-<zielprüfung>-geltung.md, das Profil nennt die Zielprüfungen, gegen die
Poolzeilen gezählt werden; iqb-bau.py v1.6 liest sie dort.
Änderungen gegenüber 1.8 (Auftrag C, Teil 0, Entscheidung des Lehrers): § 7
Eichschwelle für Poolstapel unverändert 85 %, für Landeshefte (abi)
ausgesetzt; Maßstab der Schätzung nach Kern § 5 v0.7 (afb_amtlich leer =
Schätzung ohne Maßstab). iqb-bau.py unverändert (v1.5).
Änderungen gegenüber 1.7 (Auftrag „Eichung korrigieren, Prüfungsgeschichte und
Prüfungsstruktur festhalten, Heftordner ordnen", Entscheidung des Lehrers): § 7
Überschreibung der Eichschwelle je Stapel zurückgebaut, Vorrang des Amtlichen
für übernommene Schätzungen (Kern § 5, iqb-bau.py v1.5, Lauf 20).
Änderungen gegenüber 1.6 (Stapel 2022-ga-B): § 7 Eichschwelle je Stapel in KONFIG
überschreibbar (iqb-bau.py v1.4; in 1.8 zurückgebaut).
Änderungen gegenüber 1.5 (Auftrag „Geltung klären"): § 6 Poolzeilen weiter
gegen alle vier Spalten, die bebb-Regel gilt nur für abi
(abitur-vokabular.md v1.2).
Änderungen gegenüber 1.4 (Auftrag „Reserve öffnen, Verweise schließen, Heft
2024 erfassen"): § 7 Vormerkung als Übergangszustand (offener Posten), Verweis
„Abgewandelt von:" in der Kennzahl „in Landesheften"; § 2 Reserve-Stapel
2017-ea-A, 2018-ga-B, 2018-ea-B wegen Landesheftverweisen erfasst
(Abbruchkriterium unberührt; iqb-bau.py v1.3, Lauf 15).
Änderungen gegenüber 1.3 (Auftrag „abi-Bestand gegen den Pool abgleichen"):
§ 7 Vormerkung „Poolaufgabe (nicht erfasst)" aus abi und Kennzahl „in
Landesheften" je Stapel (iqb-bau.py v1.2).
Änderungen gegenüber 1.2 (Auftrag „Themenfeld bereinigen, dann Stark-Heft 2023
erfassen"): § 6 Regel Zeilenthema = Typthema (iqb-bau.py v1.1, Lauf 13),
Handlungen im Kern § 5; § 2 Lesequellen des Skripts; § 7 dublette_von
klargestellt (Spalte von iqb-quellen.csv, kein Katalogfeld).
Änderungen gegenüber 1.1 (Entscheidung 25, Auftrag „Weg A umsetzen"): § 5–6
Sachgebiete, Themenliste, Geltungstabelle, Gegenstandsklassen, Handlungen und
Rechnerfassung nach abitur-vokabular.md verschoben, hier nur noch Verweis und
Profilspezifisches; § 2 gemeinsame Typenliste abitur-typen.csv und abitur-abgleich.py
(vorher iqb-typen.csv, iqb-abgleich.py); § 7 Pool-Teilaufgaben in
Landesheften (Regel des Profils abi, hier festgehalten); § 9 Zusammenführung
mit abi entschieden.
Änderungen gegenüber 1.0 (Auftrag „Teil B schließen, Rechnerfassung der
Zielprüfungen klären"): § 1 Bestand fortgeschrieben, Teil B abgeschlossen; § 6
Rechnerfassung je Zielprüfung aus den vier Prüfungsschwerpunkten 2027 mit
Fundstellen, neben der Geltungstabelle; § 6 Abbruchkriterium Teil B: Stand
abgeschlossen, Reserve benannt; § 9 Teil B geschlossen; § 7 Dubletten:
DUBLETTEN_HAND auch für rein redaktionelle Abweichungen, wortgleiche
Teilaufgaben und Aufgaben in nicht wortgleichen MMS-Dateien (nach dem
Delta-Stapel 2026-ea-B-mms, iqb-quellen.py v0.4).
Änderungen gegenüber 0.9 (Auftrag „Erhöhtes Niveau absichern, MMS-Dubletten
bereinigen", Entscheidungen des Lehrers nach der Delta-Messung 2026-ga-B-mms):
§ 7 MMS/CAS als Delta zum WTR-Zweig – wortgleiche Dateien sind Dubletten der
WTR-Datei (iqb-quellen.py v0.3 scannt Teil B, Verfahren und Schwelle in § 7),
Erfassungseinheit für mms-/cas-Stapel sind die nicht wortgleichen Dateien
(iqb-bau.py v0.9); § 9 offener Punkt MMS geschlossen; § 6 Abbruchkriterium
erhöht: Reihe wird fortgesetzt (nicht ausgereizt nach 2024-ea-B).
Änderungen gegenüber 0.8 (Auftrag „Teil B absichern", Entscheidungen des
Lehrers nach fünf Teil-B-Stapeln): § 6 Abbruchkriterium für Teil B gesetzt
(getrennt je Niveau, Zielprüfung des Niveaus); § 6 Thema Konfidenzintervalle
in der Stochastik-Liste und in der Geltungstabelle (bisher ersatzweise unter
Hypothesentests); § 7 Dubletten unterhalb der Dateiebene in Teil B (nach
2026-ea-B und 2025-ea-B).
Änderungen gegenüber 0.7 (Vorarbeit Teil B, Auftrag des Lehrers nach dem
Probestapel 2026-ga-B): § 7 Stapelschnitt in Teil B mit Rechnerfassung als
vierter Achse; § 7 Trägerbindung mit fester Markierung „Traegerbindung:
Kontext" in bemerkung; § 4 Eichregel Teil B nach der Spalte Anforderungsbereich
des Standardbezugs (Teil A bleibt beim Maximum).
Änderungen gegenüber 0.6 (nach 2022-ea-A und Abgleichlauf 2): § 7 Deutungsliste –
Nullfall-Regel zur Fallunterscheidung (ein einzelner Nullfall eines Koeffizienten
zählt nicht; Vermerk nach Abgleichlauf 3: beruht auf einem einzigen Fall, der
zweite Beleg war falsch); § 7 Befund zum Anteil amtlich-III je Pooljahr (Stufe
zwischen 2023 und 2024, ohne Deutung; nach 2018-ea-A bis Pool 2018
fortgeschrieben); § 4 afb_amtlich leer bei leerer Matrixzeile im
Standardbezug (nach 2019-ga-A, iqb-bau.py v0.5); § 7 Messung der Eichung bis
2018-ea-A; § 6 Abbruchkriterium für Teil A (neue Schnittwerte innerhalb der
Geltung, nach Abgleichlauf 4).
Änderungen gegenüber 0.5 (nach 2024-ea-A): § 6 Gegenstandsklassen je Thema als
Schnitt für Teil A, Präfix im Typnamen (Entscheidung 24, Abgleichlauf über
alle Typen); § 7 Deutungsliste mit Prinzip am Kopf und Eintrag (e).
Änderungen gegenüber 0.4 (nach 2024-ga-A): § 7 Deutungsliste (a)–(d) neu
gefasst – „faires Spiel" und „Aussage beurteilen" gestrichen, „allgemeiner
Nachweis mit Parameter" und „Term in Sachaussage übersetzen" aufgenommen; § 6
Anmerkung zur Aufgabengruppe A1 (überwiegend Matrizen, außerhalb der Geltung).
Änderungen gegenüber 0.3: § 6 Geltungstabelle Thema × (be-gk, be-lk, bb-gk,
bb-ea) aus den Prüfungsschwerpunkten 2027; § 7 Schranke für neue Typen
deaktiviert, Eichschranke 85 % nach der engen Fassung.
Änderungen gegenüber 0.2 (nach den Stapeln 2026-ea-A und 2025-ga-A): § 7
Erfassungshinweis auf die enge Fassung „Kombinieren mit Deutung heißt III"
umgestellt, mit der Messung; § 7 Dubletten-Fassungsregel, Kennzahlen je Stapel.
Änderungen gegenüber 0.1 (nach dem Stapel 2026-ga-A): § 4 ungegliederte Aufgaben
(teilaufgabe leer, id gleich Kennung) und titel bei Kurzbeschreibung „AG/LA";
§ 6 Lineare Gleichungssysteme auch unter Analytische Geometrie; § 7 Dubletten;
§ 8 Beispielzeilen aus dem Katalog; § 2 iqb-quellen.py.

## 1 Prüfung

Der Aufgabenpool des IQB (Institut zur Qualitätsentwicklung im Bildungswesen)
für die schriftliche Abiturprüfung im Fach Mathematik. Die Länder entnehmen dem
Pool Aufgaben für ihre Prüfungen; welches Land welche Aufgabe genommen hat, ist
nicht erkennbar. Der Pool ist länderneutral, gliedert sich nach Anforderungsniveau
(grundlegend, erhöht), Prüfungsteil (A hilfsmittelfrei, B mit Hilfsmitteln) und
Sachgebiet (Analysis, Analytische Geometrie/Lineare Algebra in den Alternativen A1
und A2, Stochastik). Jede Aufgabe wird mit Erwartungshorizont, Standardbezug
(Zuordnung der Teilaufgaben zu den Kompetenzen K1–K6 und den
Anforderungsbereichen I–III) und Bewertungshinweisen veröffentlicht.

Rolle im Katalog: Der Pool ist Typenquelle und Eichmaß. Er liefert 624 gelöste
Aufgaben mit amtlichem Erwartungshorizont, wo die Landeshefte des Profils abi
keine Lösungen haben, und er eicht über den Standardbezug die Schätzung in
`niveau_geschaetzt`. Die Landeshefte bleiben das Formatmodell der Prüfung; der
Pool sagt nichts darüber, wie eine Prüfung zusammengestellt wird. abi und iqb
sind seit dem 15.09.2026 über die Typen zusammengeführt – gemeinsame Typenliste
abitur-typen.csv und gemeinsames Vokabular abitur-vokabular.md –, nicht über
die Dateien (konzept.md, Entscheidungen 23 und 25).

Sagt der Lehrer IQB, Pool oder Poolaufgabe, ist dieses Profil gemeint. Abi, GK, LK
meinen weiterhin das Profil abi.

Bestand: 624 Dateien, Sondierung 13.09.2026 (iqb-quellen.md). Erfasst wurde
zuerst Prüfungsteil A (328 Dateien, 22 Stapel; 18 Stapel erfasst, nach dem
Abbruchkriterium ausgereizt am 14.09.2026, Pool 2017 und Beispielaufgaben
Reserve), dann Prüfungsteil B (296 Dateien, 44 Stapel je Rechnerfassung; der
WTR-Zweig beider Niveaus ist mit neun Stapeln 2026 bis 2022 ausgereizt,
15.09.2026, MMS/CAS sind Delta nach § 7 und werden je Niveau an einem Stapel
gemessen; alles Übrige Reserve, davon zwölf Stapel wegen Landesheftverweisen
geöffnet: 2017-ea-A, 2018-ga-B, 2018-ea-B, 2022-ga-B, 2020-ga-B, 2021-ga-B,
2025-ea-B-mms, 2019-ga-B, 2017-ga-A, 2017-ga-B (WTR), 2017-ea-B (WTR),
2017-ea-B (CAS); § 7).
Stand 28.09.2026 nach dem Stapel 2017-ea-B (CAS): 1639 Zeilen in 41 Stapeln
(20 Teil A, 17 Teil B WTR, 4 Teil B MMS/CAS), 1398 Typen in der gemeinsamen Liste
(769 nur im Pool, 370 in beiden Katalogen), 192 Schnittwerte im Poolbestand
(iqb-pruefungen.md § 2 und § 4).

## 2 Ablage und Quellen

Basis-URL der Katalogdateien: https://raw.githubusercontent.com/hz-0801/mathe-nachhilfe/main/
(alle Dateien flach in der Wurzel; bei anderer Ablage nur diese Zeile ändern).
Katalogdateien dieses Profils: iqb-quellen.md, iqb-quellen.csv,
iqb-pruefungen.md, iqb-katalog.csv; die Typenliste abitur-typen.csv und das
Vokabular abitur-vokabular.md sind mit dem Profil abi geteilt (Entscheidung
25, 15.09.2026; vorher iqb-typen.csv). Eine Katalogdatei wie bei abi; das
Feld `block` trennt Teil A und Teil B.

Aufgaben: https://www.iqb.hu-berlin.de/media/exercise_files/Abituraufgaben_Mathematik/<Kennung>_Aufgabe.pdf
Die Kennungen stehen vollständig in iqb-quellen.csv; geholt wird mit curl. Ein
zweiter Download je Aufgabe ist nicht nötig, die Datei enthält alles.

Gerüst für Erfassung und Prüfung: iqb-bau.py. Es liest Kopfzeile,
Formvokabular und Handlung je format aus katalog-prompt.md § 5, Sachgebiete,
Themen, Geltung und Klassen aus abitur-vokabular.md, die Stapelzuordnung,
Seitenzahlen und Dubletten aus iqb-quellen.csv, und schreibt die beiden
CSV-Dateien nur, wenn alle Prüfungen bestehen – einschließlich der
Schwellenwerte aus § 7. Umbenennungen und Zusammenziehungen von Typen laufen
über abitur-abgleich.py, das beide Kataloge mitzieht. iqb-quellen.py erzeugt
iqb-quellen.csv aus der Übersichtsseite des IQB und dem Scan aller Dateien
(Teil A seit v0.2, Teil B seit v0.3: Seitenzahl und Dubletten, § 7).

Amtliche Lösungen liegen für jede Aufgabe vor. Es gilt Kern § 3 d in der Fassung
„amtliche Lösung vorhanden" wie im Profil fhr: der Erwartungshorizont ist
maßgeblich, eigene Rechnung ist Kontrolle, `ergebnis` trägt den Zusatz
„amtlich". Der Erwartungshorizont „stellt für jede Teilaufgabe eine mögliche
Lösung dar"; er ist ein Lösungsweg, keine Punkteaufteilung – die BE stehen nur je
Teilaufgabe.

Amtliche Vorgaben: die Prüfungsschwerpunkte der Länder (abi-vorgaben.md) und die
„Beschreibung der Struktur" des IQB. Dieses Profil liest sie nicht; die
Themenliste (abitur-vokabular.md § 2) ist die des Profils abi.

## 3 Aufbau der Dateien

Jede Datei ist eine Aufgabe mit vier Abschnitten: **1 Aufgabe** (Aufgabentext,
BE am rechten Rand je Teilaufgabe, Summe am Ende), **2 Erwartungshorizont** (je
Teilaufgabe ein Lösungsweg, BE wiederholt), **3 Standardbezug** (Tabelle
Teilaufgabe × BE × K1–K6, in den Zellen I, II oder III), **4 Bewertungshinweise**
(Standardtext). Vorweg eine Kurzbeschreibung mit Anforderungsniveau,
Prüfungsteil, Sachgebiet und – in Teil A – Aufgabengruppe, in Teil B dem digitalen
Hilfsmittel. Die Fußzeile trägt die Dokumentkennung mit Unterstrichen
(2026_M_grundlegend_A_Analysis_1_1); der Dateiname ist dieselbe Kennung ohne
Unterstriche.

**Teil A** (hilfsmittelfrei): zwei Seiten, zwei bis drei Teilaufgaben a, b, c,
meist 5 BE je Aufgabe. Aufgabengruppe 1 in den Anforderungsbereichen I und II,
Gruppe 2 mit mindestens einer Teilaufgabe im Bereich III (abi.md § 3). Je Jahr,
Niveau, Sachgebiet und Gruppe gibt es eine bis vier Aufgaben; bei genau einer
trägt der Dateiname keine Nummer (2017MerhoehtAAnalysis2).

**Teil B** (mit Hilfsmitteln): vier bis sechs Seiten, eine Datei je Sachgebiet
und Rechnerfassung (WTR, ab 2022 MMS, davor CAS), darin mehrere durchnummerierte
Aufgaben 1, 2, … mit je bis zu acht Teilaufgaben; sechs bis sechzehn
Teilaufgaben je Datei. Formeln liegen im PDF als Bilder, die Textextraktion
verschluckt sie – Rendern ist Pflicht (Kern § 3 b).

**Beispielaufgaben.** 47 Dateien ohne Jahr (Kennung beginnt mit
„Beispielaufgaben"), vom IQB vor dem ersten Pool 2017 veröffentlicht; gleicher
Aufbau. Sie werden nach den Jahrgängen erfasst.

**Rechnerfassungen** gibt es nur in Teil B. Teil A ist hilfsmittelfrei und
deshalb ohne CAS-Delta; das ist einer der Gründe, mit Teil A zu beginnen.

## 4 Kürzel und Werte

    Kennung: der Dateiname ohne „_Aufgabe.pdf", z. B. 2026MgrundlegendAAnalysis11.
            Aufbau: Jahr (oder „Beispielaufgaben"), M, Niveau (grundlegend |
            erhoeht), Prüfungsteil (A | B), Sachgebiet (Analysis | AGLAA1 |
            AGLAA2 | Stochastik), dann in Teil A Aufgabengruppe und, wenn die
            Gruppe mehrere Aufgaben hat, die Nummer (11, 12, 2); in Teil B das
            Hilfsmittel (WTR | CAS | MMS) und, wenn es mehrere Dateien gibt, die
            Nummer (WTR1, MMS2, WTR). Die Zerlegung ist eindeutig (iqb-quellen.csv).
    id:     Kennung-Teilaufgabe · 2026MgrundlegendAAnalysis11-a
            Aufgaben ohne Teilaufgabenbuchstaben (in Gruppe 2 häufig: eine
            Aufgabe, 5 BE) sind nach Kern § 4 eine Zeile; teilaufgabe bleibt
            leer und die id ist die Kennung allein: 2026MgrundlegendAAGLAA12.
            In Teil B zusätzlich die Aufgabennummer innerhalb der Datei:
            2026MgrundlegendBAnalysisWTR1-2a (seit dem Probestapel 2026-ga-B,
            14.09.2026). Die Kennung ist der Rückweg ins Original: Kennung plus
            „_Aufgabe.pdf" ist die Datei. Die id ist umlautfrei („erhoeht" ist
            Schreibweise des IQB, keine Umschrift).
    jahr:   Pooljahr aus der Kennung; „bsp" für die Beispielaufgaben ohne Jahr.
            Auswertungen über das Jahr lassen „bsp" aus.
    papier: Jahr-iqb-Niveau · 2026-iqb-ga · 2026-iqb-ea · bsp-iqb-ga
            Niveau: ga grundlegend, ea erhöht (wie bb-ea im Profil abi).
            Teil B in der Rechnerfassung CAS/MMS: Zusatz -mms (2026-iqb-ga-mms),
            analog zu -cas im Profil abi.
    block:  A | B, der Prüfungsteil.
    aufgabe: Teil A: Aufgabengruppe, bei mehreren Aufgaben der Gruppe
            Gruppe.Nummer wie in der Kennung – 1.1, 1.2, 2. Nicht umnummerieren.
            Teil B: Dateinummer.Aufgabennummer, ohne Dateinummer nur die
            Aufgabennummer (Datei mit einer unnummerierten Aufgabe: 1).
    titel:  das Sachgebiet nach der Kennung, in der Schreibweise der
            Kurzbeschreibung: Analysis · AG/LA (A1) · AG/LA (A2) · Stochastik.
            Die Aufgaben haben keine Überschrift; über titel bleibt die
            Alternative A1/A2 erkennbar, die leitidee nicht trägt. Aufgaben, die
            für beide Alternativen taugen, nennen in der Kurzbeschreibung nur
            „AG/LA"; titel folgt dann der Kennung (Ablage unter A1 oder A2),
            der Befund steht in bemerkung.
    teilaufgabe: ein Kleinbuchstabe; leer bei Aufgaben ohne Gliederung.
    seite:  Seite des Aufgabentexts im PDF (Teil A: 1, selten 1|2), nicht die
            Seite des Erwartungshorizonts. Die Seitenzahl der Datei steht in
            iqb-quellen.csv (Teil A meist 2, 16 Dateien haben 3).
    punkte: BE am rechten Rand der Teilaufgabe.
    stern:  leer. Das Niveau steht in papier.
    hilfsmittel: nein in block A, ja in block B.
    afb_amtlich: aus dem Standardbezug, Pflichtfeld in diesem Profil. Der
            Standardbezug ist eine Matrix Teilaufgabe × K1–K6; in den Zellen
            stehen I, II oder III, leere Zellen bedeuten „Kompetenz nicht
            angesprochen". Das Feld trägt alle vorkommenden Bereiche der
            Teilaufgabe, aufsteigend, ohne Wiederholung, mit „|" getrennt:
            I · I|II · II|III · I|II|III. Nicht nur den höchsten – das Feld hält
            fest, was amtlich ausgewiesen ist, eine Auswahl wäre Deutung. Die
            Matrixzeile mit der Zuordnung zu K1–K6 steht wörtlich in bemerkung
            („Standardbezug: K1 I, K2 II, K5 II"). Ist die Matrixzeile einer
            Teilaufgabe leer (Lücke in der Quelle, erstmals 2019-ga-A AGLAA22 a),
            bleibt das Feld leer und bemerkung nennt „Standardbezug: keine
            Eintragung"; die Zeile zählt in der Eichung nicht mit (iqb-bau.py
            v0.5). Nichts wird ergänzt – das Feld hält nur fest, was amtlich
            ausgewiesen ist.
    niveau_geschaetzt: eigene Schätzung nach Kern § 5, aus dem Aufgabentext
            gebildet, nicht aus dem Standardbezug abgeschrieben – sonst eicht
            das Feld nichts. Erfassungshinweis aus der Eichung siehe § 7
            („Kombinieren mit Deutung heißt III"). Eichung (Auswertungsregel, keine
            Erfassungsregel): in Teil A verglichen mit dem höchsten Bereich in
            afb_amtlich, weil das Feld einwertig ist und die Teilaufgabe
            insgesamt meint. In Teil B hat der Standardbezug eine eigene Spalte
            „Anforderungsbereich" mit Kreuz; sie ist maßgeblich (Entscheidung
            des Lehrers, 14.09.2026) und steht in bemerkung als „AB amtlich:
            III." (Pflicht in Teil B). Weicht sie vom höchsten Kompetenzeintrag
            ab, gilt die Spalte und bemerkung trägt „Anforderungsbereich
            weicht vom höchsten Kompetenzeintrag ab" (iqb-bau.py v0.7 prüft
            beides). iqb-bau.py gibt die Trefferquote je Lauf aus.
            Die Beispielaufgaben erklären die Matrix in einer Fußnote: „Für jede
            Kompetenz, die bei der Bearbeitung der Teilaufgabe eine wesentliche
            Rolle spielt, ist der Anforderungsbereich eingetragen, in dem die
            Kompetenz benötigt wird."
    ergebnis: amtliches Ergebnis aus dem Erwartungshorizont mit Zusatz
            „(amtlich)"; weicht die eigene Rechnung ab, bleibt das amtliche in
            ergebnis und die Abweichung geht nach bemerkung. Ergebnisse zu
            Zeigen, Begründen, Angeben als erwartete Antwort in eigenen Worten.
    bemerkung: enthält immer den Standardbezug (siehe afb_amtlich). Passt kein
            Thema der Liste, trägt bemerkung das Wort „ersatzweise" mit dem
            gewählten Thema – iqb-bau.py zählt diese Zeilen (§ 7).

Schreibweisen wie im Profil fhr: Potenzen mit ^, Ableitungen f'(x), f''(x),
Koordinaten P(x; y) und P(x; y; z) mit Semikolon, Vektoren als (1; 0; 0), „|"
trennt nur Mehrfachwerte. Intervalle als −3 <= x <= 3. Unicode-Minus „−",
Malpunkt „·", Wurzel als √. Dezimalkomma wie in der Aufgabe; der Pool schreibt
Brüche und Wurzeln exakt (2√5), der Katalog übernimmt das.

## 5 Sachgebiete

Feld `leitidee` trägt das Sachgebiet: Analysis · Analytische Geometrie ·
Stochastik – die Liste steht in abitur-vokabular.md § 1 (gemeinsam mit dem
Profil abi, Entscheidung 25). Profilspezifisch: Die Alternativen A1 und A2
des IQB-Sachgebiets „Analytische Geometrie/Lineare Algebra" gehen beide nach
Analytische Geometrie; die Alternative steht in titel (§ 4).

## 6 Themenliste, Geltung, Schnitt

Themenliste und Gegenstandsklassen stehen in abitur-vokabular.md § 2 und
§ 4, die Handlung je format im Kern § 5; iqb-bau.py liest sie dort. Bis
v1.1 standen sie hier. Die Geltung steht je Zielprüfung in einer eigenen
Datei (seit 17.09.2026, Auftrag D Teil 2; vorher Tabelle in
abitur-vokabular.md § 3, dorthin war sie mit v1.1 gewandert); Poolzeilen
haben kein eigenes Zielheft und werden gegen alle Zielprüfungen des
Profils abi gezählt:

Zielprüfungen: be-gk · be-lk · bb-gk · bb-ea (Geltung je Zielprüfung in
abi-<zielprüfung>-geltung.md; iqb-bau.py liest diese Zeile und die Dateien)

Die Rechnerfassung je Zielprüfung steht in § 3 derselben Dateien.
**Zeilenthema = Typthema** (16.09.2026, abitur-vokabular.md § 4): leitidee
und thema einer Zeile sind die ihres Typs, iqb-bau.py erzwingt das, der
Schnitt wird über das Thema des Typs gezählt; die acht iqb-Zeilen, die davon
abwichen, hat Abgleichlauf 13 (abitur-abgleich.py) nachgezogen (iqb-pruefungen.md § 5). Die Regel für
gemeinsame Landeshefte bebb (Zeile gilt, wenn sie in
einer der beiden Spalten des Niveaus liegt; Entscheidung des Lehrers,
16.09.2026) betrifft nur das Profil abi (abitur-vokabular.md § 3, abi.md § 6).
Profilspezifisch bleiben:

- **Aufgabengruppe A1** ist überwiegend Matrizen (Verflechtung,
  Übergangsprozesse, Matrizenalgebra) und liegt für alle vier Zielprüfungen
  außerhalb der Geltung; die Aufgaben werden trotzdem erfasst (Typenquelle).
- **Konfidenzintervalle** (v0.9, Entscheidung des Lehrers nach fünf
  Teil-B-Stapeln): eigene Zeile, weil der Pool sie auf erhöhtem Niveau in
  Teil B stellt; bis dahin ersatzweise unter Hypothesentests, mit
  Abgleichlauf 7 umgestellt.
- **Schnitt für den Blattbau** (Entscheidung 24, hier entstanden, seit
  Entscheidung 25 für beide Profile): Thema × Gegenstandsklasse × Handlung;
  die Kennzahl „Schnitt" in iqb-pruefungen.md § 2 zählt die Werte je Stapel.

**Abbruchkriterium für Teil A (Entscheidung des Lehrers, 14.09.2026, nach
Abgleichlauf 4).** Maßstab ist je Stapel die Zahl der neuen Schnittwerte
innerhalb der Geltung (Tabelle oben) – gezählt gegen den Gesamtbestand beider
Niveaus, getrennt für be-gk und bb-ea; die Zahl im selben Niveau wird
daneben ausgewiesen. Ein Rohzuwachs außerhalb der Geltung (Matrizen,
Aufgabengruppe A1) zählt nicht. Unter fünf neue Werte je Stapel heißt
ausgereizt. Messung in iqb-pruefungen.md § 4 (Skript: neue Werte je Stapel in
der Erfassungsreihenfolge, Geltung nach dem Thema des Werts).

**Abbruchkriterium für Teil B (Entscheidung des Lehrers, 14.09.2026, nach
fünf Teil-B-Stapeln).** Derselbe Maßstab, getrennt je Niveau: je Stapel die
Zahl der neuen Schnittwerte innerhalb der Geltung, gezählt gegen den
Gesamtbestand beider Niveaus und beider Prüfungsteile, mit der Zielprüfung des
Niveaus (be-gk für grundlegend, bb-ea für erhöht). Unter fünf neue Werte je
Stapel heißt der Zweig des Niveaus ausgereizt. Der Teil-A-Maßstab bleibt
daneben unberührt. Verlauf und Reihe je Niveau in iqb-pruefungen.md § 4.
Stand 15.09.2026: grundlegend ausgereizt (7 → 3 → 2 → 2, WTR-Zweig bis
2023-ga-B); erhöht nach 2024-ea-B nicht ausgereizt (9 → 0 → 7), auf
Entscheidung des Lehrers mit 2023-ea-B (4) und 2022-ea-B (3) fortgesetzt –
zwei Stapel in Folge unter fünf, erhöht ausgereizt (9 → 0 → 7 → 4 → 3).
Beide Niveaus des WTR-Zweigs in Teil B sind damit ausgereizt. Ein
mms-Stapel zählt nicht in die Reihe (Delta, § 7). **Teil B abgeschlossen**
(Entscheidung des Lehrers, 15.09.2026): die nicht erfassten WTR-Stapel (2022-ga-B,
2021 bis 2017, Beispielaufgaben) sind Reserve wie 2017 und die
Beispielaufgaben in Teil A; die MMS/CAS-Stapel sind Delta (§ 7) und werden je
Niveau an einem Stapel gemessen (2026-ga-B-mms: 1 neuer Schnittwert in
Geltung, 2026-ea-B-mms: 0), die übrigen sind Reserve. Verzeichnis in
iqb-pruefungen.md § 2.

**Bekannte Lücken** werden wie im Profil abi gesammelt: nächstliegendes
Thema wählen, „ersatzweise" in bemerkung, Entscheidung nach mehreren Stapeln
(abitur-vokabular.md § 2). Stand v1.2: keine.

## 7 Besonderheiten beim Erfassen

- **Ein Stapel je Lauf.** Die Regel „ein Heft je Lauf" aus CLAUDE.md § 3 gilt
  für Hefte; eine Poolaufgabe ist kein Heft. Die Einheit ist der Stapel: alle
  Aufgaben eines Prüfungsteils, eines Pooljahrs und eines Niveaus (Spalte
  `stapel` in iqb-quellen.csv, z. B. 2026-ga-A mit 19 Dateien). Teil A hat 22
  Stapel zu 10 bis 20 Dateien, also 25 bis 50 Zeilen – der Umfang eines
  Landeshefts. Ein Lauf erfasst genau einen Stapel vollständig; iqb-bau.py
  prüft gegen iqb-quellen.csv, dass keine Datei des Stapels fehlt. Kein halber
  Stapel, keine Zwischenstände, ein Commit je Stapel. Reihenfolge: vom jüngsten
  Pooljahr zum ältesten, je Jahr grundlegend vor erhöht, die Beispielaufgaben
  zuletzt; innerhalb des Stapels Analysis, AG/LA (A1), AG/LA (A2), Stochastik.
  **Teil B** (Entscheidung des Lehrers, 14.09.2026, nach dem Probestapel): Der
  Stapelschnitt bekommt die Rechnerfassung als vierte Achse – Prüfungsteil ×
  Pooljahr × Niveau × Rechnerfassung (WTR | MMS | CAS), Kennung in KONFIG
  `2026-ga-B-wtr`; iqb-bau.py v0.6 prüft die Vollständigkeit je Rechnerfassung.
  Erfasst wird zuerst der WTR-Zweig. Teil A ist von der vierten Achse
  unberührt. **MMS/CAS als Delta** (Entscheidung des Lehrers, 15.09.2026, nach
  der Delta-Messung 2026-ga-B-mms in iqb-pruefungen.md § 4: 69 % der Zeilen auf
  Schnittwerten der WTR-Fassung, 3 von 7 Dateien wortgleich, 2 von 25
  eigenen Zeilen reine Rechnerbedienung): Die Einheit „Stapel je
  Rechnerfassung" gilt weiter für WTR. Für einen mms- oder cas-Stapel tritt
  an ihre Stelle: vollständig sind die nicht wortgleichen Dateien, das Soll
  rechnet gegen deren BE; wortgleiche Dateien (Dateidubletten) stehen in
  iqb-quellen.csv mit dateidublette_von auf die WTR-Datei und bekommen keine
  Zeile (Dateidubletten unten). Der WTR-Zweig ist vor dem MMS-Zweig zu
  erfassen; iqb-bau.py v0.9 prüft, dass die erste Datei jeder Dateidublette im
  Katalog steht. Der Rechner ist Lösungsweg
  unterhalb des Typs, kein eigenes Etikett (Kern § 6).
- **Trägerbindung in Teil B** (Entscheidung des Lehrers, 14.09.2026): Eine
  Zeile, die ohne den Sachkontext ihrer Trägeraufgabe nicht beschreibbar ist
  (Deutung, Abbildung oder Sachlage, die nur der Aufgabenstamm liefert), trägt
  in bemerkung am Feldanfang die feste Markierung „Traegerbindung: Kontext"
  (bewusst umlautfrei, exakter Wortlaut, iqb-bau.py prüft ihn), gefolgt von
  Punkt oder einer Klammer mit dem Grund. Kein eigenes Feld; keine Markierung
  heißt frei. Beim Blattbau werden markierte Zeilen nur mit der ganzen Trägeraufgabe
  (Kennung als Rückweg) verwendet. Die Markierung ist unabhängig von
  abhaengig_von: im Probestapel 2026-ga-B fielen von sechs kontextgebundenen
  Zeilen nur zwei mit den sechs Zeilen mit belegtem abhaengig_von zusammen, deshalb keine
  Kopplung an abhaengig_von.
- **Qualitätsschranke im Skript, nicht im Urteil des Lehrers.** Der Lehrer liest
  keine Berichte und entscheidet nicht im Lauf. iqb-bau.py bricht deshalb ab,
  wenn ein Schwellenwert gerissen wird; die Werte stehen in SCHWELLEN im Skript
  und sind revidierbar:
  · Zeilen mit „?": höchstens 10 % der Zeilen des Stapels, mindestens 2 erlaubt.
  · Neue Typen: Schranke deaktiviert (13.09.2026). Nach drei Stapeln lag der
    Anteil neuer Typen bei 100, 82 und 94 % – die geplanten 60 % hätten jeden
    weiteren Stapel abgebrochen, ohne dass etwas faul ist. Gemessen wird der
    Anteil weiter (Kennzahlen). Der Schnitt ist entschieden (Entscheidung
    24, 13.09.2026); eine Schranke für neue Typen wurde danach nicht gesetzt,
    der Anteil bleibt Kennzahl (zuletzt 40–76 % je Stapel, iqb-pruefungen.md
    § 2).
  · Eichung: mindestens 85 % der Zeilen treffen nach der engen Fassung den
    höchsten amtlichen Bereich (ab 10 Zeilen im Stapel scharf). Die Schwelle
    gilt für jeden Stapel gleich: die Überschreibung je Stapel aus iqb-bau.py
    v1.4 (2022-ga-B, 19 Zeilen mit der Schätzung der wortgleichen Landeszeilen,
    Schwelle 75 %) ist mit v1.5 zurückgebaut (Entscheidung des Lehrers,
    17.09.2026). Stattdessen gilt der Vorrang des Amtlichen (Kern § 5): weicht
    eine aus einer Landeszeile übernommene Schätzung vom Standardbezug ab, wird
    die Schätzung korrigiert, nicht die Schwelle, und die Landeszeile zieht
    nach; iqb-bau.py v1.5 prüft übernommene Schätzungen gegen den amtlichen
    Bereich (Lauf 20: neun Zeilen von 2022-ga-B, iqb-pruefungen.md § 4).
    **Die Schranke gilt nur für Poolstapel** (Entscheidung des Lehrers,
    17.09.2026, Auftrag C Teil 0): hier liegt der Maßstab für praktisch jede
    Zeile vor (1 von 1258 Zeilen ohne Standardbezug), die Quote misst die
    Erfassungsarbeit. Für Landeshefte (abi.md § 7) ist sie ausgesetzt – dort
    fehlt der Maßstab für die meisten Zeilen, und wo er vorliegt (41
    Landesschätzungen mit amtlichem Bereich: 11 über, 22 gleich, 8 unter;
    Teil A eher zu niedrig, Teil B eher zu hoch), liegt die Trefferquote bei
    54 % gegen 94 % im Pool, sie misst dort die Schwierigkeit der Aufgabe,
    nicht die Arbeit; die Quote wird dort weiter als Kennzahl ausgewiesen.
    Zurückgenommen wird die Aussetzung, falls die Erfassungsqualität sichtbar
    leidet. Maßstab der Schätzung (Kern § 5 v0.7): niveau_geschaetzt ist
    genau dort messbar, wo afb_amtlich gefüllt ist; die eine Zeile ohne
    Standardbezug (2019 AG/LA A2 2 a) trägt eine Schätzung ohne Maßstab, die
    Selbstprüfung zählt solche Zeilen („Zeilen ohne Standardbezug").
  · Zeilen mit „ersatzweise" (kein passendes Thema): höchstens 10 % der Zeilen,
    mindestens 2 erlaubt.
  Reißt eine Schranke, ist der Stapel nicht schlecht, sondern die Etiketten sind
  zu prüfen: Typen gegen den Bestand abgleichen, Themen erneut zuordnen,
  Unsicheres nachrechnen – und dann erneut laufen lassen. Erst wenn das nicht
  hilft, wird der Schwellenwert im Skript geändert und die Änderung in
  iqb-pruefungen.md § 5 begründet. Die Werte stehen seit dem 13.09.2026 fest
  und wurden seither zweimal geändert (Schranke neue Typen deaktiviert, Eichung
  85 % nach der engen Fassung; Änderungen in iqb-pruefungen.md § 5). Der
  Bericht jedes Stapels nennt als **Kennzahlen** die Quote neuer Typen an den
  verwendeten und die Eichtrefferquote (Zeile „Kennzahlen:" von iqb-bau.py, in
  iqb-pruefungen.md § 4 gesammelt).
- **Dateidubletten** (wortgleiche Pooldateien; zu unterscheiden von der
  Dublette als Landeszeile mit „Dublette von:", unten, und von der
  Aufgabendublette innerhalb eines Stapels, unten). Aufgaben, die für beide
  AG/LA-Alternativen taugen, liegen im Pool zweimal, wortgleich unter A1 und
  unter A2 (Teil A: 16 Paare, alle AG/LA, Scan vom 13.09.2026). Dateidublette
  heißt: Aufgabe, Erwartungshorizont **und**
  Standardbezug sind gleich – iqb-quellen.py vergleicht alle drei Abschnitte
  ohne Leerraum (ein Paar unterschied sich nur in „1: 3" gegen „1:3"); bei
  allen 15 Paaren des ersten Scans sind auch die Formelbilder gleich, geprüft über die
  Bildobjekte, bei einem Paar nur anders kodiert. Stimmt bei gleicher Aufgabe
  Erwartungshorizont oder Standardbezug nicht überein, ist das keine Dublette,
  sondern eine eigene Fassung: sie bekommt eine eigene Zeile und teilt nur den
  Typ; das Skript meldet solche Fälle und markiert sie nicht (bisher keiner).
  Die Spalte dateidublette_von in iqb-quellen.csv (bis 17.09.2026
  dublette_von) nennt für die zweite Datei die erste (Ordnung nach § 7);
  Dateidubletten bekommen keine Zeile und kein Soll, iqb-bau.py verlangt sie
  nicht und weist sie ab. Der Befund steht in bemerkung der ersten Datei. Ein
  Stapel zählt deshalb nach Dateien ohne Dateidubletten (2026-ga-A: 19
  Dateien, 18 erfasst). **Aufgabendubletten in Teil B** (nach 2026-ea-B-wtr):
  unterhalb der Dateiebene kann eine ganze nummerierte Aufgabe in zwei Dateien
  desselben Stapels wortgleich stehen (2026-ea-B Stochastik WTR 2 und WTR 3,
  Aufgabe 1 mit fünf Teilaufgaben). Die Regel gilt sinngemäß: die zweite
  Aufgabe bekommt keine Zeile, das Soll der
  Datei sinkt um ihre BE, der Befund steht in bemerkung der gekürzten Datei
  (letzte Zeile) und in iqb-pruefungen.md § 4. Einzelne wortgleiche Teilaufgaben
  über Niveaus hinweg (2026 Stochastik WTR 1 grundlegend und erhöht teilen vier
  Teilaufgaben) sind keine Aufgabendublette: andere Trägeraufgabe, andere Zeile,
  geteilter Typ. Dasselbe gilt innerhalb eines Stapels für geteilte
  Teilaufgaben einer Aufgabe, die als Ganzes nicht wortgleich ist (2025-ea-B
  Stochastik WTR 2 und WTR 3, Aufgabe 2: a und b gleich, c und d verschieden):
  die Regel stellt auf die ganze nummerierte Aufgabe ab, beide Dateien tragen
  die Zeilen. **Teil B über die Rechnerfassung hinweg** (15.09.2026,
  iqb-quellen.py v0.3): Der Pool führt viele Aufgaben wortgleich unter WTR und
  MMS/CAS (Scan: 18 Dateipaare in Teil B, 17 MMS/CAS → WTR, darunter drei im
  Stapel 2026-ga-B). Verfahren: iqb-quellen.py lädt alle Teil-B-Dateien,
  normiert den Abschnitt „1 Aufgabe" (ohne Leerraum, ohne Kennung, ohne
  Hilfsmittelwort, ohne die Seitenkopfzeilen, die ab Seite 2 den laufenden
  Abschnitt nennen) und vergleicht ihn innerhalb desselben Stapels und
  Sachgebiets. **Schwelle: Gleichheit.** Gleicher Aufgabentext heißt
  Dateidublette, die spätere Datei (Ordnung § 7: WTR vor CAS/MMS) zeigt in
  dateidublette_von auf die frühere; Erwartungshorizont und Standardbezug dürfen
  abweichen (anderer Rechnerweg), das Skript meldet es. Paare mit Ähnlichkeit
  ≥ 0,95 (difflib), aber ohne Gleichheit, meldet das Skript als „nahe" – sie
  sind beim Erfassen des mms-Stapels von Hand anzusehen; ist der Unterschied
  nur ein Artefakt der Textextraktion (2023-ga-B Stochastik MMS 2 = WTR 2,
  Kurzbeschreibung „MMS/WTR", die BE-Summe wandert), wird das Paar in
  DUBLETTEN_HAND im Skript mit Grund eingetragen – ebenso, wenn die Abweichung
  rein redaktionell ist und Zahlen, Aufträge und BE aller Aufgaben gleich
  bleiben (2026-ea-B Stochastik MMS 1 = WTR 1: „Die normalverteilte
  Zufallsgröße" statt „Eine …", Ähnlichkeit 0,999; iqb-quellen.py v0.4, nach
  dem Delta-Stapel 2026-ea-B-mms); unterscheiden sich Zahlen oder Aufträge im
  Aufgabentext (2024-ea-B Stochastik MMS 1: „mehr als 20" statt „mehr als
  fünf", Ähnlichkeit 0,999), ist es keine Dateidublette. Wortgleiche Teilaufgaben
  in einer nicht wortgleichen MMS-Datei teilen den Typ, die Felder werden aus
  der WTR-Zeile übernommen (Vermerk in bemerkung); eine ganze wortgleiche
  nummerierte Aufgabe (Aufgabendublette) bekommt wie innerhalb des WTR-Zweigs
  keine Zeile, das
  Soll sinkt (2026-ea-B Stochastik MMS 3, Aufgabe 1 = WTR 2, Aufgabe 1). Die
  17 im Stapel 2026-ga-B-mms zunächst aus dem WTR-Zweig übernommenen Zeilen
  wurden mit Abgleichlauf 9 gestrichen (iqb-pruefungen.md § 5).
- **Abgleichlauf nach jedem Stapel** (Kern § 9, „abgleich"): die Etiketten des
  Stapels gegen abitur-typen.csv vereinheitlichen, anhand von gegeben, gesucht,
  verfahren, stichwoerter; abitur-abgleich.py zieht beide Kataloge mit. Ergebnis als
  Liste alt → neu in iqb-pruefungen.md § 5.
- **Pool-Teilaufgaben in Landesheften** (Entscheidung des Lehrers, 15.09.2026,
  Regel des Profils abi, hier festgehalten): Nimmt ein Landesheft eine
  Poolaufgabe (2018-bb-ea Teil 1 aus dem Pool 2018 erhöht, das Stark-Heft 2023
  zu 30 von 185 BE), bekommt jede solche Teilaufgabe eine eigene abi-Zeile mit
  demselben typ wie die iqb-Zeile und dem Verweis „Dublette von: <iqb-id>" am
  Anfang von bemerkung; abi-bau.py prüft den Verweis gegen iqb-katalog.csv.
  Die iqb-Zeile bleibt unverändert; der Pool ist die Erstfassung. Ein
  Katalogfeld für Dubletten gibt es nicht (Kern § 5); die Spalte
  dateidublette_von in iqb-quellen.csv meint etwas anderes – eine
  Dateidublette, die keine Zeile bekommt (§ 4, § 7).
  Landeshefte, die eine Poolaufgabe aus einem nicht erfassten Stapel
  (Reserve) stellen, merken sie als „Poolaufgabe (nicht erfasst): <iqb-id>"
  vor (abi.md § 7) – ein Übergangszustand, der als offener Posten geführt
  wird, bis der Stapel erfasst ist (Entscheidung des Lehrers, 16.09.2026);
  iqb-bau.py meldet beim Stapellauf die vorgemerkten Zeilen und in der
  Selbstprüfung die offenen Posten mit erfasster Poolzeile, danach stellt
  abitur-abgleich.py die Vormerkung auf „Dublette von:" (wortgleich) oder „Abgewandelt
  von: <iqb-id>; <Unterschied>." (abgewandelte Fassung) um (Abgleichlauf 15). Die
  Kennzahl „in Landesheften" je Stapel (v1.2, v1.3) zählt die Zeilen mit
  Verweis, abgewandelte getrennt ausgewiesen. Reserve-Stapel, auf die
  Landeshefte verweisen, dürfen dafür erfasst werden, ohne dass das
  Abbruchkriterium fällt (2017-ea-A, 2018-ga-B, 2018-ea-B; § 2, § 4).
  **Eine Vormerkung überlebt keinen Auftrag** (Regel, gesetzt 17.09.2026, Auftrag D Teil 7; Vorschlag aus Auftrag C Teil 2, abi-pruefungen.md § 4): Wird ein Landesheft erfasst, dessen Poolaufgaben in einem Reserve-Stapel liegen, wird dieser Stapel im selben Auftrag erfasst und die Vormerkung im anschließenden Abgleichlauf auf „Dublette von:" oder „Abgewandelt von:" umgestellt. Das Abbruchkriterium bleibt dabei unberührt (iqb.md § 6, konzept.md Entscheidung 29). Kann der Stapel nicht erfasst werden, ist das im Bericht zu melden und im Änderungslog festzuhalten; die Vormerkung bleibt dann als benannter offener Posten stehen, nicht stillschweigend.
- **Standardbezug vor Erwartungshorizont lesen? Nein.** Reihenfolge beim
  Erfassen: Aufgabe lesen, niveau_geschaetzt festlegen, dann Erwartungshorizont
  und Standardbezug. Die eigene Schätzung wird nicht nachträglich an den
  Standardbezug angepasst; eine Abweichung ist ein Messwert, kein Fehler. Anders
  eine übernommene Schätzung (aus einer wortgleichen Landeszeile): sie ist kein
  Messwert dieses Stapels und folgt dem amtlichen Bereich (Vorrang des
  Amtlichen, Kern § 5, v1.8).
- **Kombinieren mit Deutung heißt III** (Erfassungshinweis aus der Eichung,
  enge Fassung; Entscheidung nach dem Stapel 2025-ga-A, 13.09.2026). Der
  amtliche Standardbezug setzt III, wo eine Teilaufgabe mehrere Regeln oder
  Verfahren verkettet **und** dabei eine Deutung oder Fallunterscheidung
  verlangt. **Nullfall-Regel** (v0.7, nach 2022-ea-A): Eine Fallunterscheidung
  zählt erst, wenn mindestens zwei Fälle mit verschiedenem Ausgang ausgeführt
  werden (a = 0 oder t = 2 in M · v = t · v; a = 2 ohne Lösung, a = −2 unendlich
  viele). Ein einzelner Nullfall eines Koeffizienten – ein Parameterwert, für
  den eine Gleichung unlösbar wird, sonst eindeutige Lösung (b = −4 in
  (4 + b) · z = 1) – ist keine Fallunterscheidung und bleibt II (2023-ea-A
  AGLAA111 amtlich II). Die Regel beruht auf diesem einen Fall: der zweite
  Beleg, mit dem sie ursprünglich begründet wurde (2025-ea-A AGLAA121 b), hat
  sich als falsch erwiesen – dort werden zwei Fälle a = ±2 mit verschiedenem
  Ausgang ausgeführt, die Zeile ist ein Treffer der Grundregel. Ein weiterer
  Nullfall im Bestand würde die Regel erst absichern (Stand 14.09.2026, nach
  2020-ea-A). **Prinzip** (an den Kopf gestellt nach 2024-ea-A, v0.6): Eine
  Deutung zählt nur, wenn sie zu finden ist – eine Beziehung wird hergeleitet,
  eine Bedingung erst gefunden, eine Symmetrie erst erkannt. Was der Text
  wörtlich vorgibt oder was sich als Identität mit mitgeführtem Parameter
  nachrechnen lässt, ist Routine und bleibt II. Deutungsliste (Stand v0.6,
  13.09.2026; (f) seit v1.17, 29.09.2026): (a) eine Bedingung aus dem Sachverhalt oder der Geometrie
  erst in eine Gleichung übersetzen (Flächenhalbierung als Integral gleich
  null, Abstand zum Spiegelbild als doppelter Abstand zur Ebene, mittlere
  Änderungsrate als Steigung der Sekante, Diagonalenschnittpunkt als
  Spurpunkt) – nicht, wenn die Übersetzung wörtlich vorgegeben ist („doppelt
  so viel", „viermal so groß"); (b) eine Symmetrie oder einen Sonderfall
  erkennen und ausnutzen (Spiegelung an y = x, gemeinsamer Lotfußpunkt, zwei
  Behälter mit gleichem Anteil) – nicht, wenn die Symmetrie schon in einer
  vorigen Teilaufgabe gezeigt oder in einer vorgegebenen Rechnung benutzt ist;
  (c) einen allgemeinen Nachweis mit Parameter führen, bei dem eine Beziehung
  hergeleitet wird (Tangente an der Stelle u schneidet bei −f(u); g'(a) = 0
  zieht f'(a) = −f(a) nach sich; zwei Scharebenen mit a ≠ b sind nie
  parallel) – nicht das Nachrechnen einer Identität mit mitgeführtem
  Parameter (Skalarprodukt mit t gleich null, f_a'(0) = 1, f_a(−x) = −f_a(x),
  amtlich I bis II); (d) einen Term oder eine Ungleichung in eine Sachaussage
  übersetzen, wenn dazu zwei Deutungen verkettet werden (Gleichung als totale
  Wahrscheinlichkeit und Binomialsumme als kumulierte Wahrscheinlichkeit) –
  nicht die einfache Deutung eines Terms als Ereignis; (e) die Beziehung
  zwischen Funktion und Stammfunktion oder Integralfunktion am Graphen deuten
  (Extrempunkte von F aus dem Vorzeichen von f, Nullstellen einer
  Integralfunktion als Flächenbilanz; ergänzt nach 2024-ea-A) – nicht das
  Zuordnen von Graph und Ableitungsgraph über Nullstellen und Extremstellen,
  das ist II; (f) Mindestanzahl oder Mindestumfang für eine
  Mindestwahrscheinlichkeit bestimmen = III (kleinstes n, für das mindestens
  ein Treffer oder mehr als k Treffer mit mindestens p eintreten – über das
  Gegenereignis mit Ungleichung für n oder durch Probieren an kumulierten
  Werten; gesetzt 29.09.2026, Beschluss vom 26.09.2026: im Pool fünf von fünf
  Fällen amtlich III – 2017-ga-B Stochastik WTR 1 2 e und WTR 2 1 c,
  2018-ea-B Stochastik WTR 1 1 b, 2019-ga-B Stochastik WTR 1 1 b, 2024-ea-B
  Stochastik WTR 1 1 c, iqb-pruefungen.md § 4; die Bestandsprüfung dazu fand
  als sechsten 2017-ea-B Stochastik CAS 1 Aufgabe 4, ebenfalls III; nicht
  gemeint ist eine Mindestanzahl aus einer Erwartungswertbedingung n · p > c,
  amtlich II). Nicht aufgenommen, bis er Belegzahlen hat: „vom Text verlangte
  Fallunterscheidung ist amtlich II" (Kandidat aus 2018-ea-B CAS). Das Prinzip
  schärft (a), (b) und (d) um die jeweils genannte
  Ausnahme; (c) trug es schon. Gestrichen nach
  2024-ga-A: „faires Spiel als Erwartungswert gleich Einsatz" (in drei
  Fällen zweimal amtlich II) und „eine Aussage beurteilen" (feuert auch bei
  einem einfachen Vergleich; eine Beurteilung ist nur III, wenn (a) bis (d)
  greifen). Offen: „Lösungsmenge mit freien Parametern beschreiben" (AGLAA12 b
  2024 amtlich III, AGLAA11 2025-ga amtlich II). Wörtlich vorgegebene
  Übersetzungen (doppelt so viel, viermal so groß) sind keine Deutung. Reine
  Verkettungen von Standardschritten bleiben II: Ableitung bilden und eine
  Bruchgleichung lösen, Schnittstelle und Steigungen und Winkelbedingung, μ
  und σ berechnen und im Diagramm ablesen, Mittelpunkt und Höhe und Fläche,
  Erwartungswert berechnen und mit dem Einsatz vergleichen. I bleibt die
  einzelne Beobachtung oder Rechnung, auch wenn sie begründet wird (Graph der
  Funktion vom Ableitungsgraphen unterscheiden: geschätzt II, amtlich I).
- **Messgeschichte der Deutungsliste** (Befund, keine Regel – die Regel steht
  im Punkt davor; Treffer der Schätzung gegen den höchsten amtlichen Bereich
  je Stapel und Listenfassung). Messung, die zur engen Fassung geführt hat:
  2026-ga-A 30 von 33 in beiden Fassungen;
  2026-ea-A weit 34, eng 36 von 37 (Analysis 1.1 b und Stochastik 1.1 b sind
  Routineverkettungen mit amtlich II); 2025-ga-A weit 29, eng 30 von 31 (die
  weite Fassung überschätzt AGLAA11 und AGLAA212-b, die enge unterschätzt nur
  Analysis 2.2 a, wo der Standardbezug die Bruchgleichung mit K5 III belegt).
  Erster Stapel nach der engen Fassung als Regel: 2025-ea-A 30 von 34; die
  Fairnessdeutung (Stochastik 1.1 b) ist dort amtlich nur II, die algebraische
  Verkettung mit Ersatz n · p = E (Stochastik 2.1) amtlich III. 2024-ga-A 26
  von 30; je Abweichung der gefeuerte Eintrag in iqb-pruefungen.md § 4
  („faires Spiel" und „Aussage beurteilen" feuern dort über dem
  Standardbezug, „allgemeiner Nachweis mit Parameter" und „Term in
  Sachaussage übersetzen" fehlen der Liste – daraufhin die Liste (a)–(d)
  oben, v0.5). Rückwirkend mit der Liste v0.5: 2026-ga-A 29, 2026-ea-A 35,
  2025-ga-A 29, 2025-ea-A 31, 2024-ga-A 28 – zusammen 152 von 165 wie zuvor,
  Einzelheiten in iqb-pruefungen.md § 4. Erster Stapel mit der Liste v0.5:
  2024-ea-A 32 von 32. Mit der Liste v0.6 (Prinzip, (e)) rückwirkend 186 von
  197 – (e) holt 2026-ga-A Analysis 2.2 b und 2026-ea-A Analysis 2.3 zurück,
  das Prinzip ändert keine Schätzung; erster Stapel mit v0.6: 2023-ga-A 23
  von 24 (Wertemenge von e^(x²) amtlich III, kein Eintrag). Mit v0.6 weiter:
  2023-ea-A 29 von 32, 2022-ga-A 23 von 24, 2022-ea-A 30 von 32. Mit der
  Nullfall-Regel (v0.7) rückwirkend: nur 2023-ea-A AGLAA111 ändert sich (III
  → II, amtlich II), 287 von 309 über zehn Stapel. Mit v0.7 weiter: 2021-ga-A
  23 von 23, 2021-ea-A 33 von 33, 2020-ga-A 18 von 19, 2020-ea-A 28 von 28,
  2019-ga-A 22 von 22 (eine Zeile ohne Standardbezug), 2019-ea-A 20 von 20,
  2018-ga-A 23 von 25, 2018-ea-A 25 von 26 – über den Bestand von 505
  gewerteten Zeilen 478 (94 %). Die vier Abweichungen seit 2020-ga-A sind
  Einzelurteile ohne Listeneintrag (Volumenverhältnis, binomische Formel für
  Matrizen, rechter Winkel mit Parameter amtlich II statt I, Fallunterscheidung
  am Graphen amtlich II statt III).
  Die weite Fassung „Kombinieren heißt III" (Stand nach 2026-ga-A) hatte die
  Verkettung allein zum Maß gemacht; sie trifft die amtlich mit III belegten
  Zeilen ebenso, überschätzt aber Routineverkettungen. Im Katalog tragen die
  Zeilen von 2026-ea-A und 2025-ga-A die Schätzung der jeweils geltenden
  Fassung; wo die enge Fassung abweicht, steht sie in bemerkung („Schätzung enge
  Fassung: II").
- **Anteil amtlich-III je Pooljahr** (Befund aus dem Bestand von 506 Zeilen,
  Teil A, Stand 14.09.2026 nach 2018-ea-A; Anteil der gewerteten Zeilen, deren
  höchster amtlicher Bereich III ist): Pool 2018 11 von 51 (22 %), 2019 8 von
  42 (19 %), 2020 8 von 47 (17 %), 2021 9 von 56 (16 %), 2022 11 von 56
  (20 %), 2023 12 von 56 (21 %), 2024 18 von 62 (29 %), 2025 19 von 65 (29 %),
  2026 19 von 70 (27 %). Nach Niveau: grundlegend 2018 24 %, 2019 18 %, 2020
  11 %, 2021 13 %, 2022 17 %, 2023 21 %, 2024 23 %, 2025 23 %, 2026 21 %;
  erhöht 2018 19 %, 2019 20 %, 2020 21 %, 2021 18 %, 2022 22 %, 2023 22 %,
  2024 34 %, 2025 35 %, 2026 32 %. Die Stufe liegt zwischen den Pooljahren
  2023 und 2024 und stammt aus dem erhöhten Niveau, das von 2018 bis 2023 bei
  18–22 % liegt; im grundlegenden Niveau fällt der Anteil von 2018 (24 %, das
  einzige Jahr mit grundlegend über erhöht) auf 2020 (11 %) und steigt dann
  bis 2024 gleichmäßig. Eine Ursache wird nicht gedeutet. 2019 und 2018 haben
  keine ungegliederten Aufgaben, 2018 keine Teilaufgabe über 3 BE.
- **Kein Aufgabenstamm im engen Sinn**, aber Text vor a) ist der Normalfall
  („Der Graph der in IR definierten Funktion f mit … wird mit G bezeichnet").
  Jede Zeile wiederholt in gegeben, was sie davon braucht (Kern § 4).
  Voraussetzungen wie „G ist symmetrisch zum Koordinatenursprung" aus der
  Teilaufgabe selbst gehören ebenfalls nach gegeben.
- **Mehrere Leistungen** in einer Teilaufgabe bleiben eine Zeile: typ die erste,
  typ_neben die weiteren, format und operator alle (Kern § 4).
- **Angeben ohne Rechnung** („Geben Sie … an") ist in Teil A häufig: format
  Kurzantwort, antwort Zahl oder Term, schritte 0 oder 1. Nachweise („Weisen
  Sie nach", „Zeigen Sie", „Begründen Sie") sind format Begründung mit antwort
  Text, auch wenn gerechnet wird; die Rechnung steht in verfahren.
- **Abbildungen** (Würfelnetze, Graphen, Schrägbilder) gehören nach material
  und skizze so genau, dass sie nachgezeichnet werden können; Werte, die nur
  im Bild stehen, nach gegeben. Formeln im Aufgabentext sind ebenfalls Bilder
  und nur im gerenderten PDF lesbar.
- **Amtliche Ergebnisse** übernehmen, eigene Rechnung mit sympy als Kontrolle;
  Rundungen und Näherungen wie im Erwartungshorizont („≈", exakte Werte mit
  Wurzeln). Der Erwartungshorizont ist nur ein möglicher Weg; verfahren darf
  einen anderen, für Schüler üblichen Weg beschreiben, das Ergebnis bleibt.
- **Kontext:** in Teil A überwiegend „ohne"; Sachkontexte (Atmung, Würfelspiel)
  kurz wie im Kern.

## 8 Beispielzeilen

Vier Zeilen aus dem Stapel 2026-ga-A, zur Lesbarkeit als Feld = Wert; in
iqb-katalog.csv stehen dieselben Werte als eine Zeile in der Reihenfolge der
Kopfzeile. Gewählt sind die beiden Zeilen der Probeaufgabe, eine ungegliederte
Aufgabe (5 BE, teilaufgabe leer, id gleich Kennung) und eine Stochastik-Zeile
mit Baumdiagramm. Dieser Abschnitt wird aus dem Katalog erzeugt und weicht
deshalb nicht von ihm ab.

    id = 2026MgrundlegendAAnalysis11-a · jahr = 2026 · papier = 2026-iqb-ga · block = A · aufgabe = 1.1 · titel = Analysis · teilaufgabe = a · seite = 1
    punkte = 2 · stern =  · hilfsmittel = nein · afb_amtlich = I
    leitidee = Analysis · thema = Kurvenuntersuchung · typ = Extrempunkt an vorgegebener Stelle nachweisen · typ_neben =  · stichwoerter = ganzrationale Funktion dritten Grades|notwendige Bedingung|hinreichende Bedingung|zweite Ableitung · voraussetzungen = Potenzregel anwenden|Vorzeichen der zweiten Ableitung deuten
    format = Begründung · operator = Weisen Sie nach · antwort = Text
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = f(x) = x^3 − 3x, definiert in IR; Graph G · gesucht = Nachweis, dass G einen Hochpunkt mit der x-Koordinate −1 hat · verfahren = erste und zweite Ableitung bilden, f'(−1) = 0 und f''(−1) < 0 zeigen · schritte = 3 · zahlenraum = ganz|negativ|Potenz · einheiten =  · abhaengig_von = 
    ergebnis = f'(x) = 3x^2 − 3, f''(x) = 6x; f'(−1) = 0 und f''(−1) = −6 < 0, also Hochpunkt bei x = −1 (amtlich) · zwischenergebnis = f'(x) = 3x^2 − 3|f''(x) = 6x
    niveau_geschaetzt = I · fehlerquelle = nur f'(−1) = 0 zeigen und die hinreichende Bedingung weglassen · bemerkung = Standardbezug: K1 I, K2 I, K5 I. Amtlich, eigene Rechnung bestätigt.

    id = 2026MgrundlegendAAnalysis11-b · jahr = 2026 · papier = 2026-iqb-ga · block = A · aufgabe = 1.1 · titel = Analysis · teilaufgabe = b · seite = 1
    punkte = 3 · stern =  · hilfsmittel = nein · afb_amtlich = I|II
    leitidee = Analysis · thema = Kurvenuntersuchung · typ = Abstand zweier Extrempunkte über die Punktsymmetrie berechnen · typ_neben =  · stichwoerter = Punktsymmetrie zum Ursprung|Hochpunkt|Tiefpunkt|Abstand zweier Punkte · voraussetzungen = Funktionswert berechnen|Abstand zweier Punkte mit dem Satz des Pythagoras|Punktsymmetrie nutzen
    format = Rechnung · operator = Berechnen Sie · antwort = Zahl
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = f(x) = x^3 − 3x, definiert in IR; Graph G; G ist symmetrisch zum Koordinatenursprung; G hat einen Hochpunkt mit der x-Koordinate −1 · gesucht = Abstand zwischen Hoch- und Tiefpunkt von G · verfahren = f(−1) = 2 berechnen, Hochpunkt H(−1; 2); wegen der Punktsymmetrie ist der Tiefpunkt T(1; −2); Abstand als Länge der Strecke HT, gleich dem Doppelten des Abstands von H zum Ursprung · schritte = 3 · zahlenraum = ganz|negativ|Wurzel · einheiten =  · abhaengig_von = 2026MgrundlegendAAnalysis11-a
    ergebnis = 2 · √((−1)^2 + 2^2) = 2√5 (amtlich) · zwischenergebnis = f(−1) = 2|H(−1; 2)|T(1; −2)
    niveau_geschaetzt = II · fehlerquelle = den Tiefpunkt neu über die Ableitung berechnen statt die Symmetrie zu nutzen, oder nur den Abstand von H zum Ursprung angeben · bemerkung = Standardbezug: K2 II, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt: 2√5 ≈ 4,47.

    id = 2026MgrundlegendAAGLAA12 · jahr = 2026 · papier = 2026-iqb-ga · block = A · aufgabe = 2 · titel = AG/LA (A1) · teilaufgabe =  · seite = 1
    punkte = 5 · stern =  · hilfsmittel = nein · afb_amtlich = II|III
    leitidee = Analytische Geometrie · thema = Lineare Gleichungssysteme · typ = Lösung eines unterbestimmten Gleichungssystems unter Zusatzbedingungen auswählen · typ_neben =  · stichwoerter = LGS mit drei Unbekannten|Gleichungen II und III Vielfache|Lösungsschar mit Parameter|negativ und ganzzahlig|größtes y · voraussetzungen = abhängige Gleichungen erkennen|Lösungsmenge mit Parameter angeben|Bedingungen an den Parameter übersetzen
    format = Rechnung · operator = Bestimmen Sie · antwort = Zahl
    material = keins · skizze = keine · kontext = ohne · textumfang = mittel
    gegeben = lineares Gleichungssystem I: −4x + z = 4, II: 2y − z = 4, III: 4y − 2z = 8; betrachtet werden nur Lösungen (x; y; z), bei denen x, y und z negativ und ganzzahlig sind · gesucht = die Lösung mit dem größten Wert für y · verfahren = II und III sind Vielfache, das System hat unendlich viele Lösungen; mit z = t folgt x = t/4 − 1 und y = t/2 + 2; alle drei negativ heißt t < −4, ganzzahlig heißt t Vielfaches von 4; größtes y bei t = −8 · schritte = 4 · zahlenraum = ganz|negativ|Bruch · einheiten =  · abhaengig_von = 
    ergebnis = (−3; −2; −8) (amtlich) · zwischenergebnis = allgemeine Lösung (t/4 − 1; t/2 + 2; t) mit t aus IR|Bedingung t < −4 und t Vielfaches von 4
    niveau_geschaetzt = III · fehlerquelle = das System für eindeutig lösbar halten oder die Ganzzahligkeit von x übersehen und t = −6 nehmen · bemerkung = Standardbezug: K1 III, K2 II, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE. Lineare Gleichungssysteme stehen im Pool unter AG/LA, in der Themenliste deshalb auch unter Analytische Geometrie (iqb.md § 6).

    id = 2026MgrundlegendAStochastik13-b · jahr = 2026 · papier = 2026-iqb-ga · block = A · aufgabe = 1.3 · titel = Stochastik · teilaufgabe = b · seite = 1
    punkte = 2 · stern =  · hilfsmittel = nein · afb_amtlich = I|II
    leitidee = Stochastik · thema = Bedingte Wahrscheinlichkeit und Bayes · typ = Bedingte Wahrscheinlichkeit aus dem Baumdiagramm mit einer Schranke vergleichen · typ_neben =  · stichwoerter = bedingte Wahrscheinlichkeit|Bedingung verspätet|0,18/(0,08 + 0,18)|größer als 50 % · voraussetzungen = Bedingung als Nenner aus zwei Pfaden zusammensetzen
    format = Rechnung · operator = Untersuchen Sie · antwort = Zahl|Text
    material = Diagramm · skizze = zweistufiges Baumdiagramm: erste Stufe A (40 %) und A quer, zweite Stufe je V und V quer; am Ast A–V steht x, am Ende 8 %; am Ast A quer–V steht 30 %, am Ende y; die übrigen Äste ohne Angabe · kontext = Onlinehandel/Versand · textumfang = mittel
    gegeben = Baumdiagramm: P(A) = 0,4, P(A und verspätet) = 0,08, P(nicht A und verspätet) = 0,18; eine zufällig ausgewählte Sendung wird verspätet zugestellt · gesucht = Untersuchung, ob die Wahrscheinlichkeit, dass diese Sendung nicht mit A verschickt wurde, größer als 50 % ist · verfahren = P(nicht A | verspätet) = 0,18/(0,08 + 0,18) berechnen und mit 0,5 vergleichen · schritte = 2 · zahlenraum = dezimal|Prozent · einheiten =  · abhaengig_von = 2026MgrundlegendAStochastik13-a
    ergebnis = 0,18/(0,08 + 0,18) = 0,18/0,26 > 0,5, also ja (amtlich) · zwischenergebnis = 0,18/0,26 ≈ 0,69
    niveau_geschaetzt = II · fehlerquelle = mit 0,3 (Anteil unter den nicht mit A verschickten) statt mit der bedingten Wahrscheinlichkeit unter der Bedingung verspätet antworten · bemerkung = Standardbezug: K1 I, K3 II, K4 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt.

Ein „?" hinter einem Wert bedeutet: plausibel, aber nicht am Bild geprüft; der
Grund steht dann in bemerkung. In diesem Stapel kommt es nicht vor.

## 9 Offene Punkte

- Beispielaufgaben: Veröffentlichungsjahr nicht ermittelt; jahr = „bsp".
- Aufgabengruppe (1 oder 2) steht nur in aufgabe; ob sie als Merkmal für den
  Blattbau reicht, zeigt die Heft-Phase.
- Beantwortet (17.09.2026): Die Trefferquote niveau_geschaetzt gegen den
  höchsten amtlichen Bereich liegt über 37 Stapel bei 94 % (1357 von 1442
  gewerteten Zeilen); die Schätzregel des Kerns § 5 (I reproduzieren, II
  Zusammenhänge herstellen, III verallgemeinern und reflektieren) wird für das
  Abitur nicht nachjustiert – die enge Fassung (§ 7) präzisiert sie, der Kern
  bleibt unverändert.

Erledigt (Beleg): Kürzel für Teil B (papier-Zusatz -mms, aufgabe
Dateinummer.Aufgabennummer, id mit Aufgabennummer) seit dem Probestapel
2026-ga-B (14.09.2026) geltend, § 4; MMS-Fassung als Delta (15.09.2026), § 7;
Teil B abgeschlossen (15.09.2026), § 6; Schwellenwerte gesetzt (§ 7);
Zusammenführung mit abi über die Typen (Entscheidung 25, 15.09.2026), § 1.
