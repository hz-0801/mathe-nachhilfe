# PROFIL ABI – Zentrale schriftliche Abiturprüfung, Mathematik, Berlin/Brandenburg
Version 0.9 · 16.09.2026 · Kennung abi · gilt mit Kern v0.4 (Schema-Version 2)
Änderungen gegenüber 0.8 (Auftrag „Themenfeld bereinigen, dann Stark-Heft 2023
erfassen"): § 6 Regel Zeilenthema = Typthema (abi-bau.py v0.4 erzwingt sie,
Lauf 13), Handlungen im Kern § 5; § 7 dublette_von klargestellt (Spalte von
iqb-quellen.csv, kein Katalogfeld; Zeilenverweis „Dublette von:" in
bemerkung); § 2 Stark-Scans ohne Lösungen, Pool-Teilaufgaben mit afb_amtlich
aus der Poolzeile (erstes Stark-Heft 2023-bebb-gk erfasst, abi-bau.py v0.4).
Änderungen gegenüber 0.7 (Entscheidung 25, Auftrag „Weg A umsetzen"): § 5–6
Sachgebiete und Themenliste nach abitur-vokabular.md, hier nur Verweis und
Lücken; Typenschnitt nach Entscheidung 24 auch für abi; § 2 gemeinsame
Typenliste abitur-typen.csv und abgleich.py; § 4 typ mit Präfix; § 7
Pool-Teilaufgaben in Landesheften (eigene Zeile, geteilter Typ, „Dublette
von:"), Trägerbindung, Qualitätsschranke im Skript (abi-bau.py v0.3).
Änderungen gegenüber 0.6 (Auftrag „Stark-Heft 2023 Berlin/Brandenburg GK –
Pool-Abgleich vor Erfassung"): § 4 papier-Kürzel `bebb` für die gemeinsamen
Hefte Berlin/Brandenburg 2019–2025 aus Verlagsbänden; § 2 Ablage der
gescannten Hefte unter hefte/ (lokal, nicht im Repo).
Änderungen gegenüber 0.5 (Nacharbeiten nach der Sondierung des IQB-Pools): § 4
afb_amtlich berichtigt – der Standardbezug ist eine Matrix Teilaufgabe × K1–K6,
keine angekreuzte Spalte je Bereich; § 9 Land und Niveau des Schülers beantwortet,
Annahme „Brandenburg, erhöhtes Niveau" gestrichen; § 2 Verweis auf abi-vorgaben.md.
Poolaufgaben des IQB werden nicht in diesem Profil erfasst, sondern im Profil iqb
(iqb.md); die Hinweise in § 2 sind entsprechend gefasst.
Änderungen gegenüber 0.4 (nach dem Heft 2018-be-gk, erstes Heft auf grundlegendem
Niveau): § 3 Aufbau am Heft bestätigt, § 6 Lückenstand und eine neue Themenlücke, § 7
neuer Punkt zum grundlegenden Niveau.

## 1 Prüfung

Zentrale schriftliche Abiturprüfung im Fach Mathematik. Berlin und Brandenburg
prüfen beide zentral, auf grundlegendem Anforderungsniveau (Grundkurs) und auf
erhöhtem Anforderungsniveau (Leistungskurs; in Brandenburg „Kurs auf erhöhtem
Anforderungsniveau"). In Brandenburg ist Mathematik nur dann Pflichtprüfungsfach,
wenn es als Leistungskurs belegt wird.

Die Aufgaben entstehen gemeinsam: Die Hefte für das erhöhte Niveau tragen im Kopf
sowohl das Ministerium für Bildung, Jugend und Sport als auch die Senatsverwaltung
für Bildung, Jugend und Familie, und ein erheblicher Teil der Aufgaben ist in
beiden Ländern wortgleich (Nachweis in abi-aufbau.md § 4). Die Länder stellen aus
diesem Werk verschieden zusammen. Auf grundlegendem Niveau tragen die
veröffentlichten Hefte nur die Berliner Behörde.

**Zeitleiste der Zusammenarbeit.** Berlin führte das Zentralabitur im Schuljahr
2006/2007 ein; seit dem Schuljahr 2009/2010 entwickeln Berlin und Brandenburg die
Aufgaben für Deutsch, Englisch, Französisch und Mathematik gemeinsam, koordiniert
vom LISUM. Bis 2013 erschien je Niveau ein Heft ohne Länderkennzeichnung, ab 2014
drei Hefte je Jahrgang (be-gk, be-lk, bb-ea) aus einem gemeinsamen Werk mit
landeseigener Auswahl. Das LISUM wurde Ende 2024 aufgelöst; seit dem Abitur 2026
erstellt Berlin seine Aufgaben über das BLiQ, Brandenburg über das LIBRA. Belegt
ist der Bruch an den Prüfungsschwerpunkten 2027, die für beide Länder getrennt
erscheinen und sich inhaltlich unterscheiden (§ 3). Für den Katalog heißt das: der
Bestand 2017/2018 bildet eine Kooperation ab, die für den Prüfungsjahrgang 2027
nicht mehr besteht. Er bleibt Typenquelle, ist aber kein Beleg dafür, dass beide
Länder dasselbe schreiben.

Bestand: Die Hefte laut abi-quellen.md § 2, zunächst 2017 und 2018.
Sagt der Lehrer Abi, Abitur, GK oder LK, ist dieses Profil gemeint.

## 2 Ablage und Quellen

Basis-URL der Katalogdateien: https://raw.githubusercontent.com/hz-0801/mathe-nachhilfe/main/
(alle Dateien flach in der Wurzel; bei anderer Ablage nur diese Zeile ändern).
Katalogdateien dieses Profils: abi-quellen.md, abi-pruefungen.md,
abi-katalog.csv; die Typenliste abitur-typen.csv und das Vokabular
abitur-vokabular.md sind mit dem Profil iqb geteilt (Entscheidung 25,
15.09.2026; vorher abi-typen.csv). Umbenennungen und Zusammenziehungen von
Typen laufen über abgleich.py, das beide Kataloge mitzieht. Eine
Katalogdatei, kein zweiter Block wie beim Profil msa: Das Feld `block` trägt
die Unterscheidung zwischen hilfsmittelfreiem Teil und Teil mit Hilfsmitteln
bereits. Eine zweite Datei würde dieselbe Information ein zweites Mal ablegen und
die Auswertung über beide Teile hinweg erschweren.

Hefte: abi-quellen.md nennt Verzeichnis, Dateinamen und papier-Kürzel; geholt wird
mit curl. Veröffentlicht sind nur 2011–2018. Hefte ab 2019 liegen nur in
Verlagsbänden (Stark) vor; ihre Scans stehen lokal unter hefte/<papier>.pdf
(reine Bildscans ohne Textebene, jede Seite wird gerendert gelesen) und sind
über .gitignore vom Repo ausgeschlossen, weil sie urheberrechtlich geschützt
sind. Bestand und Abgleich je Heft in abi-pruefungen.md.

Amtliche Lösungen: für die Landesaufgaben 2017/2018 keine, für die Stark-Scans
ab 2019 ebenfalls nicht (nur die Aufgabenseiten sind gescannt, die Lösungen des
Bands nicht). Der Erwartungshorizont mit verbindlicher Verteilung der
Bewertungseinheiten geht nur an die Schulen. Für diese Hefte gilt Kern § 3 d in
der Fassung „eigene Rechnung"; Unsicherheiten nach `bemerkung`; Ablesewerte aus
Abbildungen tragen „?". Die Poolaufgaben des IQB (seit Prüfungsjahr 2017, mit
Erwartungshorizont und Standardbezug) werden nicht in diesem Profil erfasst,
sondern im eigenen Profil iqb (iqb.md, iqb-katalog.csv, gemeinsame Typenliste
abitur-typen.csv); dort gilt die Fassung „amtliche Lösung vorhanden" wie im
Profil fhr. Nimmt ein Landesheft eine Poolaufgabe auf, bekommt sie hier eine
eigene Zeile mit Verweis (§ 7), afb_amtlich aus der Poolzeile. Zusammengeführt
wird über die Typen, nicht über die Dateien.

Amtliche Vorgaben: die Prüfungsschwerpunkte des jeweiligen Prüfungsjahrs,
getrennt nach Land und Niveau. Brandenburg unter
.../fileadmin/bbb/unterricht/pruefungen/abitur_bb/RS_ZA_JJJJ/PS_Mathematik_LK_JJJJ.pdf
(entsprechend _GK_), Berlin unter berlin.de, ps_mathematik_JJJJ_lk.pdf bzw. _gk.pdf.
Sie gehören nach abi-vorgaben.md und werden jährlich geprüft.

## 3 Aufbau der Hefte

**Zwei Formate.** Die erfassten Hefte 2017/2018 und die heutige Prüfung sind
verschieden gebaut. Der Katalog nimmt 2017/2018 als Typenquelle; die Blattstruktur
richtet sich nach dem heutigen Format.

**Format bis 2018 (papier be-gk, be-lk, bb-ea).** Drei Aufgabenstellungen, je eine
von zwei Aufgaben zur Wahl: 1 Analysis, 2 Analytische Geometrie, 3 Stochastik.
Berlin GK 210 Minuten, 40 + 20 + 20 = 80 BE; Berlin LK 270 Minuten,
50 + 25 + 25 = 100 BE. Brandenburg auf erhöhtem Niveau hat zusätzlich
Aufgabenstellung 1 als hilfsmittelfreien Teil ohne Wahl (drei Aufgaben zu je zwei
Teilaufgaben, 15 BE, Abgabe spätestens nach 40 Minuten); die Sachgebiete
verschieben sich dadurch auf 2, 3 und 4, und die Wahl in 3 und 4 ist gekoppelt –
wer 3.1 nimmt, muss 4.1 nehmen. 270 Minuten, 15 + 50 + 35 = 100 BE. Berlin hat in
diesen Jahren keinen hilfsmittelfreien Teil. Hilfsmittel: Nachschlagewerk zur
Rechtschreibung, an der Schule eingeführte Formelsammlung, nicht programmierbarer
und nicht grafikfähiger Taschenrechner.

**Format ab Prüfungsjahr 2019 (Berlin) bzw. bereits vorher (Brandenburg).** Jeder
Aufgabenvorschlag besteht aus Prüfungsteil A (hilfsmittelfrei) und Prüfungsteil B
(mit Hilfsmitteln). Teil A enthält mehrere kurze, nicht zusammenhängende Aufgaben
in zwei Gruppen: Gruppe 1 in den Anforderungsbereichen I und II, Gruppe 2 mit
mindestens einer Teilaufgabe im Anforderungsbereich III. Brandenburg LK 2027: vier
Pflichtaufgaben aus Gruppe 1, dazu zwei aus sechs angebotenen der Gruppe 2; GK:
je drei Aufgaben beider Gruppen zur Auswahl, aus jeder Gruppe eine. Teil B enthält
komplexe Aufgaben, mindestens eine aus der Analysis, dazu Analytische Geometrie
und Stochastik, teils Pflicht, teils Wahl. Arbeitszeit Brandenburg LK 2027
330 Minuten inklusive Auswahlzeit, Abgabe von Teil A innerhalb der ersten
110 Minuten; auf grundlegendem Niveau 285 Minuten und 100 Minuten, in Berlin und
Brandenburg gleich. Die 255 Minuten aus den Berliner Fachbriefen 21 und 22 sind
ein historischer Wert und gelten nicht mehr. **Getrennte Kataloge ab 2027:**
Brandenburg verlangt im Grundkurs hypergeometrische Verteilung, Satz von Bayes,
Axiomensystem von Kolmogorow, Hessesche Normalenform und die Ableitung von Sinus-
und Kosinusfunktionen; Berlin nichts davon, schließt Abstandsformeln und Hessesche
Normalenform ausdrücklich aus, verlangt dafür Wurzelgleichungen, das Lotto-Modell
und Sachkontexte wie Masse, Volumen, Dichte und begnügt sich bei Extrempunkten mit
der notwendigen Bedingung. Struktur und Zeit sind identisch, die Inhalte nicht. Hilfsmittel: Nachschlagewerk zur
Rechtschreibung, Formelsammlung des IQB (nicht in Teil A), Taschenrechner (nicht
in Teil A), Standard-Zeichenwerkzeuge.

**WTR, CAS und MMS.** Zu jedem Heft gibt es eine vollständige Parallelfassung für
Rechner mit Computeralgebra. Brandenburg nennt sie ab 2027 „modulares
Mathematiksystem" (MMS); Berlin schreibt „MMS (CAS)". Die Fassungen tragen
dieselben Kontexte; der Eingriff sitzt in einzelnen Teilaufgaben. In den
Brandenburger CAS-Heften trägt jede geänderte Aufgabe das Präfix „CAS:" im Titel;
fehlt es, ist die Aufgabe unverändert aus dem WTR-Heft übernommen. Die Berliner
CAS-Hefte sind durchgehend eigene Fassungen.

## 4 Kürzel und Werte

    papier: Jahr-Land-Niveau[-cas], klein und ohne Umlaute
            2017-be-gk · 2017-be-gk-cas · 2017-be-lk · 2017-be-lk-cas
            2017-bb-ea · 2017-bb-ea-cas · entsprechend 2018
            Land „bebb" für die gemeinsamen Hefte Berlin/Brandenburg der
            Jahre 2019 bis 2025 (Verlagsbände, Kopf „Berlin/Brandenburg –
            Mathematik Grundkurs"): 2023-bebb-gk, mit Rechnerfassung
            2023-bebb-gk-cas bzw. -mms wie der Band sie nennt. Entscheidung
            15.09.2026 (Vorschlag des Lehrers): das Muster Jahr-Land-Niveau
            trägt die gemeinsame Prüfung nicht, „bebb" nennt beide Länder in
            der Reihenfolge der amtlichen Kopfzeile; be und bb bleiben für
            die landeseigenen Hefte bis 2018 und ab 2026.
            Die Werte stehen in abi-quellen.md § 2 und sind zugleich die
            Dateinamen des Korpus.
    block:  A (hilfsmittelfreier Teil; bis 2018 Aufgabenstellung 1 der
            bb-ea-Hefte) · B (Sachgebietsaufgaben)
    id:     Jahr-papier-BlockkürzelAufgabeTeilaufgabe, Aufgabe zweistufig
            2018-bb-ea-B2.1c · 2018-bb-ea-A1.2a · 2018-be-gk-B3.2e
    aufgabe: die Nummer wie im Heft, mit Punkt (2.1). Nicht umnummerieren –
            die Nummer ist der Rückweg ins Original.
    titel:  der Aufgabentitel des Hefts ohne das CAS-Präfix (Vase, Museum,
            Gartenteich); im hilfsmittelfreien Teil das Sachgebiet.
    stern:  leer. Es gibt keine Sternaufgaben; Niveauunterschiede stehen im
            papier-Kürzel.
    hilfsmittel: nein in block A, sonst ja.
    typ:    Etikett aus abitur-typen.csv; in Themen mit Gegenstandsklassen
            (abitur-vokabular.md § 4) beginnt der Name mit der Klasse und
            Doppelpunkt („Körper: Pyramidenvolumen aus Grundfläche und Höhe
            berechnen"), sonst ohne Präfix; abi-bau.py prüft das.
    afb_amtlich: leer für 2017/2018 – diese Hefte weisen keine
            Anforderungsbereiche aus, und die zugehörigen Erwartungshorizonte
            sind nicht veröffentlicht. Eine Schätzung gehört nicht in dieses
            Feld; sie steht in niveau_geschaetzt. Gefüllt wird nur bei
            Poolaufgaben des IQB, die im Profil iqb erfasst werden: deren
            Abschnitt „Standardbezug" ist eine Matrix Teilaufgabe × K1–K6, in
            den Zellen stehen I, II oder III (Sondierung 13.09.2026). Eine
            Teilaufgabe trägt also bis zu sechs Bereiche, nicht einen; die
            frühere Beschreibung „eine angekreuzte Spalte je
            Anforderungsbereich" war falsch. Schreibweise: alle vorkommenden
            Werte I, II, III, aufsteigend, ohne Wiederholung, mit „|" getrennt
            (I|II). Die Matrix mit der Zuordnung zu K1–K6 kommt wörtlich nach
            bemerkung, nicht ins Feld. Einzelheiten in iqb.md § 4.
    seite:  Seite im PDF. Die Brandenburger Dateien sind Zusammenschnitte mit
            eigener Seitenzählung je Teil; die gedruckte Angabe weicht ab.
            Liegt die zugehörige Abbildung in einer Anlage auf einer anderen
            Seite, werden beide genannt (5|6).
    punkte: Bewertungseinheiten (BE) laut der Tabelle am Ende jeder Aufgabe.
            Im hilfsmittelfreien Teil steht keine Tabelle an den einzelnen
            Aufgaben; die BE aller drei Sachgebiete stehen gesammelt auf der
            letzten Seite von Teil 1, nach Teilgebiet und Buchstabe gegliedert
            (2018: Analysis 2 + 3, Geometrie 2 + 3, Stochastik 3 + 2 = 15).
            Die Herkunft der BE gehört in diesen Fällen nach bemerkung.

## 5 Sachgebiete

Feld `leitidee` trägt das Sachgebiet: Analysis · Analytische Geometrie ·
Stochastik. Die Liste und ihre Begründung gegen die KMK-Leitideen stehen in
abitur-vokabular.md § 1 (gemeinsam mit dem Profil iqb, Entscheidung 25).

## 6 Themenliste, Geltung, Schnitt

Themenliste, Geltungstabelle (be-gk, be-lk, bb-gk, bb-ea) und
Gegenstandsklassen stehen in abitur-vokabular.md § 2–4, die Handlung je
format im Kern § 5; abi-bau.py liest sie dort.
Bis v0.7 stand die Themenliste hier (46 Themen); die gemeinsame Liste hat 49
(dazu Matrizen und Übergangsprozesse, Konfidenzintervalle, Lineare
Gleichungssysteme auch unter Analytische Geometrie), die Abweichungen der
beiden Fassungen sind in abitur-vokabular.md § 7 festgehalten. Seit dem
Umstellungslauf 12 (15.09.2026) gilt für abi der Typenschnitt nach
Entscheidung 24: Typen in Themen mit Gegenstandsklassen tragen die Klasse als
Präfix („Ebene Figur: …"), der Schnitt Thema × Gegenstandsklasse × Handlung
ist die Einheit für den Blattbau, der Typ das Feinetikett. **Zeilenthema =
Typthema** (16.09.2026, abitur-vokabular.md § 4): leitidee und thema einer
Zeile sind die ihres Typs, abi-bau.py erzwingt das; wer bei einer Zeile ein
anderes Thema für richtig hält, wechselt den Typ oder meldet den Typ für den
Abgleichlauf. Der Schnitt wird über das Thema des Typs gezählt.

**Bekannte Lücken** (Feldprobe 2018-bb-ea und die Hefte 2017/2018): relative
Abweichung in Prozent, elementargeometrische Nebenrechnungen (Sechseck),
Maßstab, Geschwindigkeit umrechnen, Zeichnen ins vorgegebene
Koordinatensystem, Punkt in vorgegebener Entfernung auf einer Geraden – im
Pool haben diese Fertigkeiten ein Thema gefunden (abitur-vokabular.md § 2,
letzte Anmerkung); die betroffenen Zeilen behalten ihr Thema, „ersatzweise"
in bemerkung bleibt als Vermerk. Stand nach 2018-be-gk: 33 der 46 damaligen
Themen belegt.

## 7 Besonderheiten beim Erfassen

- **Pool-Teilaufgaben in Landesheften** (Entscheidung des Lehrers,
  15.09.2026): Nimmt ein Landesheft eine Poolaufgabe des IQB (2018-bb-ea
  Teil 1 Analysis und Geometrie aus dem Pool 2018 erhöht; das Stark-Heft
  2023 zu 30 von 185 BE), bekommt jede solche Teilaufgabe eine eigene
  abi-Zeile mit demselben typ wie die iqb-Zeile (geteilter Typ; typ_neben
  darf Nebenleistungen nennen) und dem Verweis „Dublette von: <iqb-id>." am
  Anfang von bemerkung. Kein bloßer Verweis ohne Zeile. abi-bau.py prüft,
  dass die id in iqb-katalog.csv steht und typ übereinstimmt; bei anderer
  Punktzahl nennt bemerkung die BE. Die Zeile trägt die Fakten des
  Landeshefts (Seite, BE, Wortlaut der Aufgabe), afb_amtlich darf aus der
  Poolzeile übernommen werden. Ein Katalogfeld dublette_von gibt es nicht
  (Kern § 5, 37 Felder); die Markierung in bemerkung ist der Verweis.
  dublette_von ist allein eine Spalte von iqb-quellen.csv und sagt, dass eine
  Pooldatei wortgleich mit einer anderen ist (Datei → Datei, keine Zeile) –
  ein anderer Sachverhalt als die Pool-Teilaufgabe im Landesheft, die eine
  eigene Zeile bekommt.
- **Trägerbindung** wie im Profil iqb (iqb.md § 7): feste Markierung
  „Traegerbindung: Kontext" am Anfang von bemerkung, kein eigenes Feld.
- **Qualitätsschranke im Skript** (abi-bau.py v0.3, SCHWELLEN wie iqb-bau.py):
  Zeilen mit „?" höchstens 10 % (mindestens 2), Zeilen mit „ersatzweise"
  höchstens 10 % (mindestens 2), Eichung mindestens 85 % der Zeilen mit
  amtlichem Bereich, scharf ab 10 gewerteten Zeilen; die Hefte bis 2018 haben
  keinen amtlichen Bereich. Ein Heft ist vollständig, wenn jede Aufgabe aus
  KONFIG["soll"] Zeilen hat und jede Punktsumme stimmt; probe = True prüft,
  ohne zu schreiben.

- **Eine Leitfassung je Jahr und Niveau.** Auf erhöhtem Niveau bb-ea, weil sie den
  hilfsmittelfreien Teil enthält; auf grundlegendem be-gk, weil Brandenburg dort
  nichts veröffentlicht. Wortgleiche Zwillinge des anderen Landes werden nicht als
  Zeile erfasst, sondern in abi-pruefungen.md notiert. Eigene Zeile nur bei
  abweichender Teilung; Erkennungsregel ist der Vergleich der BE-Vektoren
  (abi-aufbau.md § 4). **Grenze der Regel** (Befund an 2017, abi-pruefungen.md
  § 4): Die Berliner LK-Hefte sind keine Zwillinge, sondern Überschneidungen. 2017
  stehen drei der sechs Wahlaufgaben wortgleich in beiden Heften, drei weitere gibt
  es nur in Berlin (Verbindungsbrücke, Solarmodule, Autopanne, zusammen 100 BE) und
  drei nur in Brandenburg; 2018 ist es dasselbe Bild mit je zwei eigenen Aufgaben.
  Die Leitfassungsregel deckt also nicht das ganze Aufgabenwerk ab. Ob die eigenen
  Berliner Aufgaben nachträglich erfasst werden, ist offen (§ 9).
- **Grundlegendes Niveau.** Die be-gk-Hefte bis 2018 haben keinen
  hilfsmittelfreien Teil; alle Zeilen tragen block B, `soll_teil1` entfällt in
  KONFIG. Beide Wahlwege sind gleich gewichtet (40/40, 20/20, 20/20), eine
  Kopplung wie in bb-ea gibt es nicht. Die Typenliste trägt über die
  Niveaugrenze, aber ungleichmäßig: 16 der 50 Typen von 2018-be-gk waren
  bekannt, in der Stochastik 7 von 14, in der Analysis nur 4 von 20.
- **CAS als Nachtrag**, und nur für Aufgaben mit „CAS:"-Präfix. Der Eingriff ist
  punktuell und sitzt in `gegeben`, `gesucht`, `punkte` und teils `verfahren`;
  typisch wird ein im WTR-Heft vorgegebener Kontrollwert in der CAS-Fassung selbst
  bestimmt.
- **Wahl ist keine Eigenschaft der Teilaufgabe.** Dass 2.1 und 2.2 zur Wahl stehen
  und dass 3.x und 4.x in bb-ea gekoppelt sind, steht in diesem Profil und in
  abi-pruefungen.md, nicht im Katalog.
- **Aufbauende Teilaufgaben.** Manche Aufgaben sind Ketten: Teilaufgabe d) nutzt das
  Ergebnis aus b). Das ist eine Eigenschaft der einzelnen Aufgabe, nicht des Formats –
  in 2.1 ist `abhaengig_von` in 6 von 11 Zeilen belegt, in 2.2 in keiner von 8, im
  ganzen Heft in 8 von 41. Kontrollangaben in eckigen Klammern („Zur Kontrolle: …") gehören nach
  `gegeben` der folgenden Teilaufgabe.
- **Umfang.** Eine Analysisaufgabe hat bis zu zehn Teilaufgaben und 50 BE. Ob
  `verfahren` und `schritte` diesen Umfang tragen, ist in der Feldprobe zu prüfen,
  bevor ein ganzes Heft erfasst wird.
- **Mehrere Leistungen je Einheit sind der Normalfall.** Kern § 4 hält sie in
  einer Zeile: typ trägt die erste Leistung, typ_neben die weiteren. In der
  Feldprobe entfielen zehn von 21 Typen allein auf typ_neben. Das Feld thema ist
  dabei einwertig, obwohl die Einheit oft zwei Themen berührt (2.1 a: Nullstellen
  einer Schar und Grenzverhalten); ein zweites Thema ist nur mittelbar über
  typ_neben sichtbar. In 2018-bb-ea entfielen 22 von 60 Typen allein auf `typ_neben`,
  fast alle in den Analysis-Kontextaufgaben; Geometrie und Stochastik haben meist
  eine Leistung je Teilaufgabe. Folge für die Heft-Phase: ein Typ, der nur als
  Nebenleistung vorkommt, hat keine Ankeraufgabe, die als Decke taugt. Entschieden:
  `typen.csv` markiert das nicht. Ob ein Typ je als Haupttyp auftritt, ist aus dem
  Katalog jederzeit berechenbar; ein eigenes Feld wäre dieselbe Information ein
  zweites Mal, veraltet mit dem ersten Heft, das den Typ als Haupttyp verwendet, und
  müsste über msa und fhr mitgepflegt werden. Stattdessen wird beim Bau die
  Ankeraufgabe auf die Teilleistung zugeschnitten.
- **schritte trägt hier wenig.** Bei Deutungsaufgaben ohne Rechnung steht 0
  (2.1 h), bei langen Ketten ist der Wert eine Schätzung, weil Ableiten,
  Gleichsetzen, Fallunterscheidung und Randvergleich keine natürliche
  Schrittzahl haben. Das Feld wird gefüllt, aber nicht ausgewertet.
- **skizze meint Material, nicht Lösung.** Verlangt die Aufgabe selbst eine
  Darstellung, beschreibt das Feld ausnahmsweise die zu erstellende Darstellung
  statt vorhandenen Materials; der Fall wird in `bemerkung` kenntlich gemacht. Das
  gilt für jede zu erstellende Darstellung, nicht nur für Skizzen im engeren Sinn –
  belegt an 2.1 i (Skizze zur Sechseckfläche) und 4.1 a (Baumdiagramm).
- **Kontrollangaben** in eckigen Klammern stehen in gegeben der Teilaufgabe, in
  der sie abgedruckt sind, und werden durch eigene Rechnung bestätigt; die
  Bestätigung wird in bemerkung vermerkt.
- **Kein Volltext.** Beschreibung statt Wortlaut, auch bei den langen
  Aufgabenstämmen. Das Original wird nur für Wortlaut und Bild der Ankeraufgabe
  herangezogen.

## 8 Beispielzeilen

Drei Zeilen aus der Feldprobe an 2018-bb-ea, zur Lesbarkeit als Feld = Wert; in
abi-katalog.csv stehen dieselben Werte als eine Zeile in der Reihenfolge der
Kopfzeile. Gewählt sind eine Zeile aus dem hilfsmittelfreien Teil und zwei aus
der Analysisaufgabe, darunter die mit der zu erstellenden Skizze.

    id = 2018-bb-ea-A1.2b · jahr = 2018 · papier = 2018-bb-ea · block = A · aufgabe = 1.2 ·
      titel = Analytische Geometrie · teilaufgabe = b · seite = 2
    punkte = 3 · stern =  · hilfsmittel = nein · afb_amtlich =
    leitidee = Analytische Geometrie · thema = Orthogonalität · typ = Eckpunkt eines Quadrates
      nachweisen · typ_neben = Durchstoßpunkt einer Geraden durch eine Ebene bestimmen|
      Streckenlänge im Raum berechnen · stichwoerter =
      Quadrat|Diagonalenschnittpunkt|Halbdiagonalen|Skalarprodukt · voraussetzungen =
      Vektorlänge berechnen|Skalarprodukt bilden|Eigenschaften der Quadratdiagonalen kennen
    format = Begründung · operator = Zeigen Sie · antwort = Text
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = Quadrat mit Eckpunkt P(0 | 1 | 5) in der y-z-Ebene; die Gerade g mit x = (5 | 4 |
      1) + t · (1 | 0 | 0) verläuft orthogonal zur Trägerebene. Der Schnittpunkt der beiden
      Diagonalen des Quadrates liegt auf g. Der Punkt Q(0 | 8 | 4) liegt in der y-z-Ebene. ·
      gesucht = Nachweis, dass Q einer der beiden zu P benachbarten Eckpunkte des Quadrates ist
      · verfahren = Diagonalenschnittpunkt M als Schnittpunkt von g mit der y-z-Ebene bestimmen
      (x-Koordinate 0 setzen). Dann die Halbdiagonalen MP und MQ vergleichen: gleiche Länge
      zeigt, dass Q Eckpunkt ist, Skalarprodukt 0 zeigt, dass Q nicht der zu P
      gegenüberliegende, sondern ein benachbarter Eckpunkt ist. · schritte = 4 · zahlenraum =
      ganz · einheiten =  · abhaengig_von = 2018-bb-ea-A1.2a
    ergebnis = M(0 | 4 | 1). Mit MP = (0 | −3 | 4) und MQ = (0 | 4 | 3) ist |MP| = |MQ| = 5 und
      MP · MQ = −12 + 12 = 0. Im Quadrat sind die vier Halbdiagonalen gleich lang und die
      Diagonalen orthogonal, also ist Q ein zu P benachbarter Eckpunkt. · zwischenergebnis = M(0
      | 4 | 1)|MP = (0 | −3 | 4)|MQ = (0 | 4 | 3)|Seitenlänge |PQ| = 5·√2
    niveau_geschaetzt = II · fehlerquelle = gleiche Länge der Halbdiagonalen allein als Nachweis
      nehmen und den gegenüberliegenden Eckpunkt nicht ausschließen · bemerkung = BE aus der
      gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Geometrie, b) 3 BE). Eigene Rechnung.

    id = 2018-bb-ea-B2.1a · jahr = 2018 · papier = 2018-bb-ea · block = B · aufgabe = 2.1 ·
      titel = Vase · teilaufgabe = a · seite = 5
    punkte = 8 · stern =  · hilfsmittel = ja · afb_amtlich =
    leitidee = Analysis · thema = Funktionsscharen und Ortskurven · typ = Nullstellen einer
      Funktionenschar mit Fallunterscheidung ermitteln · typ_neben = Grenzverhalten einer
      Exponentialfunktion untersuchen · stichwoerter =
      Funktionenschar|Nullstellen|Fallunterscheidung|Grenzwert · voraussetzungen = Satz vom
      Nullprodukt|quadratische Gleichung lösen|Vorzeichen der Exponentialfunktion kennen
    format = Rechnung|Begründung · operator = Ermitteln Sie|Untersuchen Sie · antwort =
      Term|Text
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = Funktionenschar f_a mit f_a(x) = (x² + a) · e^(0,5 − x), a ∈ IR; die Graphen der
      Schar sind G_a. · gesucht = Anzahl der Nullstellen von f_a in Abhängigkeit von a;
      Verhalten der Funktionswerte für x → ∞ und für x → −∞ · verfahren = Der Faktor e^(0,5 − x)
      ist stets positiv, also nur x² + a = 0 lösen: x² = −a mit Fallunterscheidung a < 0, a = 0,
      a > 0. Für x → ∞ dominiert der fallende Exponentialfaktor, für x → −∞ wachsen beide
      Faktoren unbeschränkt. · schritte = 5 · zahlenraum = ganz|Wurzel|Potenz · einheiten =  ·
      abhaengig_von =
    ergebnis = a < 0: zwei Nullstellen x = ±√(−a); a = 0: eine Nullstelle x = 0; a > 0: keine
      Nullstelle. Für x → ∞ gilt f_a(x) → 0, für x → −∞ gilt f_a(x) → +∞. · zwischenergebnis =
    niveau_geschaetzt = II · fehlerquelle = den Exponentialfaktor als möglichen Nullfaktor
      behandeln oder die Fallunterscheidung auf a < 0 und a > 0 verkürzen · bemerkung = Zwei
      Themen in einer Einheit: Nullstellen der Schar und Grenzverhalten. Das Feld thema ist
      einwertig, das zweite Thema (Grenzwerte und Verhalten im Unendlichen) erscheint nur über
      typ_neben. Eigene Rechnung.

    id = 2018-bb-ea-B2.1i · jahr = 2018 · papier = 2018-bb-ea · block = B · aufgabe = 2.1 ·
      titel = Vase · teilaufgabe = i · seite = 6
    punkte = 7 · stern =  · hilfsmittel = ja · afb_amtlich =
    leitidee = Analysis · thema = Rotationsvolumen · typ = Umbeschriebenes Prisma zu einem
      Rotationskörper bestimmen · typ_neben = Flächeninhalt eines regelmäßigen Sechsecks aus dem
      Inkreisradius berechnen|Sachzusammenhang durch Skizze und Gleichung darstellen ·
      stichwoerter = regelmäßiges Sechseck|Inkreisradius|Prisma|Mindestvolumen · voraussetzungen
      = regelmäßiges Sechseck in Dreiecke zerlegen|Inkreisradius und Seitenlänge
      umrechnen|Einheiten dm³ in cm³ umrechnen
    format = Zeichnen|Rechnung · operator = Stellen Sie dar|Ermitteln Sie · antwort =
      Grafik|Zahl
    material = keins · skizze = Im Heft ist keine Abbildung vorgegeben; die Skizze ist Teil der
      Lösung. Gefordert ist eine Draufsicht auf das regelmäßige Sechseck der Grundfläche mit
      eingezeichnetem Inkreis vom Radius r (maximaler Vasenradius), dem Inkreisradius als
      Abstand vom Mittelpunkt zur Seitenmitte und der Seitenlänge s. · kontext = Verpackung /
      Vase · textumfang = mittel
    gegeben = Die Vase hat die Länge 3 dm und einen maximalen Radius von ca. 1,07 dm. Sie soll
      stehend in einem Karton verpackt werden, der die Form eines regelmäßigen sechsseitigen
      Prismas besitzt. · gesucht = Zusammenhang zwischen dem maximalen Radius der Vase und der
      Grundfläche des Kartons als Skizze und Gleichung; Mindestvolumen des Kartons in cm³ ·
      verfahren = Der maximale Radius ist der Inkreisradius r des regelmäßigen Sechsecks. Aus s
      = 2r / √3 folgt für die Grundfläche A = 6 · (s · r / 2) = 2√3 · r². Die Prismenhöhe ist
      die Vasenlänge 3 dm, also V = 2√3 · r² · 3; Ergebnis in cm³ umrechnen. · schritte = 5 ·
      zahlenraum = dezimal|Wurzel · einheiten = dm|cm³ · abhaengig_von = 2018-bb-ea-B2.1g
    ergebnis = A = 2√3 · r² ≈ 3,98 dm² und V = 6√3 · r² ≈ 11,9 dm³, also muss der Karton
      mindestens etwa 11 900 cm³ Volumen haben. · zwischenergebnis = s = 2r / √3 ≈ 1,237 dm|A ≈
      3,98 dm²|V ≈ 11,94 dm³
    niveau_geschaetzt = III · fehlerquelle = den Umkreisradius statt des Inkreisradius mit dem
      Vasenradius gleichsetzen, oder dm³ nicht in cm³ umrechnen · bemerkung = Mit r = 0,65 · √e
      ≈ 1,0717 dm ergibt sich V ≈ 11 935 cm³, mit dem gerundeten r = 1,07 dm ≈ 11 898 cm³;
      beides rundet auf 11 900 cm³. Das Feld skizze beschreibt hier eine vom Prüfling zu
      erstellende Skizze, nicht vorhandenes Aufgabenmaterial. Die Teilaufgabe ist
      elementargeometrisch; die Themenliste Analysis führt dafür kein passendes Thema,
      ersatzweise Rotationsvolumen. Eigene Rechnung.

## 9 Offen

- Beantwortet (13.09.2026): Land und Niveau des Schülers sind nicht auf eines
  festgelegt – der Schüler kann beides schreiben. Die frühere Annahme
  „Brandenburg, erhöhtes Niveau" ist gestrichen; die Leitfassungsregel in § 7
  bleibt als Erfassungsordnung bestehen, ist aber keine Aussage über den
  Schüler. Folge: die nur in den Berliner LK-Heften stehenden Aufgaben sind eine
  Lücke, keine Dublette (nächster Punkt).
- Werden die Themenlücken aus § 6 durch neue Themen geschlossen oder durch eine
  Lockerung der Regel, dass leitidee das Sachgebiet der Aufgabenstellung trägt?
- Beantwortet: Brandenburg hat eine eigene zentrale Prüfung auf grundlegendem
  Niveau. Die Prüfungsschwerpunkte PS_Mathematik_GK_2027.pdf liegen auf dem
  Bildungsserver; nur die Aufgabenhefte werden nicht veröffentlicht. Damit ist
  offen, woher Material auf grundlegendem Niveau für einen Brandenburger
  Prüfling kommt – die Berliner GK-Hefte sind seit 2026 nicht mehr dieselbe
  Prüfung.
- Werden die Aufgaben nacherfasst, die nur in den Berliner LK-Heften stehen? Sie
  gehören zum selben Aufgabenwerk und brächten je Jahrgang rund 100 BE zusätzliche
  Typenquelle; erfasst würden nur die dort eigenen Aufgaben.
- Auf welcher Vereinbarung beruht das gemeinsame Aufgabenwerk, und welche Länder
  gehören dazu?
- Ab wann genau gilt in Berlin Teil A/Teil B? Belegt ist: Brandenburg hatte den
  hilfsmittelfreien Teil bereits 2017, Berlin nach den Fachbriefen ab 2019.
- Trägt das CAS-Delta über alle Sachgebiete? Geprüft ist nur Analysis (2016,
  Aufgabe 1.1).
