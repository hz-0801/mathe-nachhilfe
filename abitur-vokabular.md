# VOKABULAR – Sachgebiete, Themen, Gegenstandsklassen, Geltung
Version 1.6 · 17.09.2026 · gilt für die Profile abi und iqb (konzept.md, Entscheidung 25)
Änderungen gegenüber 1.5 (Auftrag F, Punkt 2 und 3): das Abgleichskript heißt abitur-abgleich.py (bis 17.09.2026 abgleich.py), die Messung abi-iqb-typen.md heißt befund-abi-iqb-typen.md; nur Namen, an vier Stellen.
Änderungen gegenüber 1.4 (Auftrag D „Namensschema, Erweiterbarkeit,
Begründungen", Teil 2; Auftrag E Punkt 4: § 4 „Klasse" statt „Unterklasse", „Abgleichlauf 13"): § 3 Geltungstabelle, Rechnerfassung und
Ausschlussliste je Zielprüfung in eigene Dateien abi-<zielprüfung>-geltung.md
ausgelagert, Inhalt unverändert; hier bleiben Regeln und Anmerkungen. Die
Bau-Skripte lesen die Dateien der Zielprüfungen, die das Profil nennt
(abi-bau.py v0.10, iqb-bau.py v1.6).
Änderungen gegenüber 1.3 (Auftrag B „Fünf Hefte erfassen, Heftkorpus,
Katalog gegen Stark prüfen, CAS-Delta", Teil 5): § 3 Ausschlussliste neben
der Geltungstabelle (Aufgabenformen, nicht Themen) mit Befund im Bestand;
Vorschlag einer strukturellen Geltung nach Jahrgangsklassen (nicht gesetzt).
Änderungen gegenüber 1.2 (Auftrag „Eichung korrigieren, Prüfungsgeschichte und
Prüfungsstruktur festhalten, Heftordner ordnen", Teil 3): § 3 Anmerkungen
neben der Geltungstabelle – nicht geforderte Inhalte, landesspezifische
Einschränkung (Berlin LK) und die zwei Rahmenlehrpläne; Tabelle unverändert.
Änderungen gegenüber 1.1 (Auftrag „Geltung klären", Entscheidung des Lehrers
16.09.2026): § 3 Geltung gemeinsamer Hefte Berlin/Brandenburg (bebb) – gegen
beide Spalten, eine Zeile gilt, wenn sie in mindestens einer liegt.

Diese Datei ist die eine Quelle für alles, was abi und iqb an Vokabular
oberhalb des Typs teilen: Sachgebiet (§ 1), Themenliste (§ 2),
Geltungsregeln (§ 3; die Tabellen je Zielprüfung in
abi-<zielprüfung>-geltung.md), Gegenstandsklassen mit der Regel Zeilenthema =
Typthema (§ 4) und die Regeln der gemeinsamen Typenliste abitur-typen.csv
(§ 6); die Handlung je format steht seit Kern v0.4 im Kern § 5 (§ 5 hier
verweist nur). abi-bau.py, iqb-bau.py und abitur-abgleich.py lesen sie; abi.md und
iqb.md verweisen hierher und führen nur, was profilspezifisch ist. Der Kern
(katalog-prompt.md v0.4) sieht die ausgelagerte Vokabulardatei vor: wo er
„im Profil" sagt, ist für abi und iqb diese Datei gemeint. Bis zum
15.09.2026 standen Themenliste und Klassen in abi.md § 5–6 und iqb.md § 5–6
doppelt; die Fassung von iqb.md war die jüngere und ist hier übernommen, die
Abweichungen stehen in § 7.

## 1 Sachgebiete

Feld `leitidee` trägt das Sachgebiet: **Analysis · Analytische Geometrie ·
Stochastik**.

Dieselben drei Werte in beiden Profilen, damit die Typen zusammenführbar
sind. Die Bildungsstandards der KMK kennen für die Oberstufe fünf Leitideen
(Algorithmus und Zahl, Messen, Raum und Form, Funktionaler Zusammenhang,
Daten und Zufall); sie liegen quer zu den Sachgebieten und sind für die
Zuordnung einer Teilaufgabe nicht trennscharf. Prüfung, Kurshalbjahre und
Prüfungsschwerpunkte sind nach Sachgebieten gegliedert. Lineare Algebra ist
kein eigener Wert: Die Alternativen A1 und A2 des IQB-Sachgebiets
„Analytische Geometrie/Lineare Algebra" gehen beide nach Analytische
Geometrie (die Alternative steht im Feld titel, iqb.md § 4).

## 2 Themenliste

Feste Ebene zwischen Sachgebiet und Typ. Abgeleitet aus den
Prüfungsschwerpunkten Brandenburg 2027 (LK und GK) und dem Rahmenlehrplan
GOST Teil C Mathematik (gültig ab 01.08.2022), ergänzt um zwei Themen aus dem
Pool (Matrizen und Übergangsprozesse für die Alternative A1,
Konfidenzintervalle). Ergänzungen nur über den Bericht; jedes Thema braucht
eine Zeile in der Geltungstabelle (§ 3).

**Analysis:** Gleichungen lösen · Lineare Gleichungssysteme · Funktionsklassen und
Eigenschaften · Umkehrfunktion · Grenzwerte und Verhalten im Unendlichen ·
Ableitung und Änderungsrate · Ableitungsregeln · Tangente, Normale, Schnittwinkel ·
Kurvenuntersuchung · Ableitungsgraph und Funktionsgraph · Funktionsscharen und
Ortskurven · Rekonstruktion von Funktionsgleichungen · Extremalprobleme ·
Stammfunktion und Hauptsatz · Integrationsregeln · Flächeninhalt durch Integration ·
Rekonstruktion von Beständen · Uneigentliche Integrale · Rotationsvolumen

**Analytische Geometrie:** Punkte und Strecken im Koordinatensystem · Vektoren und
Rechenoperationen · Linearkombination und lineare Abhängigkeit · Geraden · Ebenen ·
Lagebeziehungen · Schnittmengen · Skalarprodukt und Winkel · Orthogonalität ·
Abstände · Flächeninhalt und Volumen im Raum · Scharen von Geraden und Ebenen ·
Spiegelung · Lineare Gleichungssysteme · Matrizen und Übergangsprozesse

**Stochastik:** Ereignisse und Mengenoperationen · Zufallsexperimente und
Urnenmodelle · Kombinatorik · Baumdiagramm und Pfadregeln · Vierfeldertafel ·
Bedingte Wahrscheinlichkeit und Bayes · Unabhängigkeit · Lage- und Streumaße einer
Stichprobe · Zufallsgrößen und Verteilungen · Binomialverteilung · Kenngrößen von
Verteilungen · Hypergeometrische Verteilung · Normalverteilung und Sigma-Regeln ·
Hypothesentests · Konfidenzintervalle

Anmerkungen zur Liste:

- **Lineare Gleichungssysteme** steht in beiden Listen. Die
  Prüfungsschwerpunkte führen sie unter Analysis; der Pool stellt reine
  LGS-Aufgaben unter AG/LA. Weil leitidee das Sachgebiet der Aufgabenstellung
  trägt und nicht umsortiert wird, brauchen beide Listen das Thema. Typen zu
  LGS werden je Sachgebiet geführt; beim Abgleich ist zu prüfen, ob dieselbe
  Fertigkeit unter beiden steht.
- **Matrizen und Übergangsprozesse** kommt nur in der Alternative A1 des
  Pools vor und ist in Berlin und Brandenburg nicht Prüfungsgegenstand; die
  Aufgaben werden trotzdem erfasst (Typenquelle), gefiltert wird über die
  Geltung.
- **Konfidenzintervalle** stellt der Pool auf erhöhtem Niveau in Teil B
  (2026-ea-B, 2025-ea-B); kein Landesheft bis 2018 stellt sie, kein
  Prüfungsschwerpunkt 2027 nennt sie.
- Nicht erfasst werden Teilaufgaben, deren einzige Leistung das Erläutern
  oder Entwickeln eines Beweises (K1 im engen Sinn) oder eine Simulation ist
  (Prüfungsschwerpunkte 2027: nicht gefordert). Bisher keine Fundstelle.
- Passt kein Thema, wird das nächstliegende gewählt und „ersatzweise" in
  bemerkung vermerkt (Kern § 6); die Bau-Skripte zählen diese Zeilen. Die
  Lücken aus den Landesheften 2017/2018 (Maßstab, Streckenlänge,
  Geschwindigkeit umrechnen, Zeichnen in ein vorgegebenes Koordinatensystem,
  Punkt in vorgegebener Entfernung auf einer Geraden) haben im Pool ein
  Zuhause gefunden: Maßstab und Streckenlänge als Teil des Haupttyps unter
  Flächeninhalt durch Integration bzw. Punkte und Strecken, die
  Geschwindigkeit unter Punkte und Strecken (Körper), das Zeichnen unter
  Kurvenuntersuchung oder Funktionsscharen, der Punkt in Entfernung unter
  Geraden.

## 3 Geltung

Ob ein Thema Prüfungsgegenstand ist, hängt von Land und Niveau ab. Quelle
sind die vier Prüfungsschwerpunkte 2027 (Berlin ps_mathematik_2027_gk/lk,
Brandenburg PS_Mathematik_GK/LK_2027; gelesen am 13.09.2026, Ablage in
abi-vorgaben.md § 1). ja = in den Schwerpunkten genannt, nein = nicht
genannt. **Seit dem 17.09.2026 (Auftrag D, Teil 2) steht die Geltung je
Zielprüfung in einer eigenen Datei:** abi-be-gk-geltung.md,
abi-be-lk-geltung.md, abi-bb-gk-geltung.md, abi-bb-ea-geltung.md – § 1 die
Themen (Tabelle „Thema | gilt", eine Zeile je Thema der Liste in § 2), § 2
die ausgeschlossenen Aufgabenformen, § 3 die Rechnerfassung; erzeugt aus der
Tabelle, die bis v1.4 hier stand, Inhalt unverändert (Benennung nach
namensschema.md § 2). Welche Zielprüfungen ein Profil hat, sagt das Profil
(abi.md § 6, iqb.md § 6, Zeile „Zielprüfungen:"); die Bau-Skripte lesen
diese Zeile und die Dateien und zählen je Heft oder Stapel die Zeilen, deren
Thema für eine Zielprüfung nicht gilt; gefiltert wird über das Thema, ein
Zeilenfeld gibt es dafür nicht (Geltung ist eine Eigenschaft des Themas,
nicht der Zeile). Das Abbruchkriterium der Erfassung (iqb.md § 6) zählt neue
Schnittwerte innerhalb der Geltung. Hier bleiben die Regeln und Anmerkungen,
die alle Zielprüfungen zugleich betreffen.

**Geltung eines Hefts** (Entscheidung des Lehrers, 16.09.2026): Ein
Landesheft wird gegen die Zielprüfung seines Kürzels gemessen (be-gk, be-lk,
bb-ea). Ein gemeinsames Heft Berlin/Brandenburg gilt für zwei Zielprüfungen:
bebb-gk für be-gk und bb-gk, bebb-lk für be-lk und bb-ea. Eine bebb-Zeile
liegt in der Geltung, wenn ihr Thema in mindestens einer der beiden Spalten
gilt; der Bericht nennt daneben beide Spalten einzeln (abi-bau.py v0.7,
Kennzahl „außerhalb der Geltung" je Heft). Für Poolzeilen (iqb) ändert sich
nichts: sie werden weiter gegen alle vier Spalten gezählt. Die beiden
Spalten je Niveau unterscheiden sich derzeit nur bei der hypergeometrischen
Verteilung (Brandenburg ja, Berlin nein); eine bebb-Zeile dazu gilt.

Stand der Tabellen (48 Themenzeilen; Lineare Gleichungssysteme steht in
zwei Sachgebieten, hat aber eine Zeile): be-gk 39 ja, be-lk 45, bb-gk 40,
bb-ea 46.

Anmerkungen zu den Themen (gelten für alle vier Dateien):
Konfidenzintervalle nennt keines der vier Papiere
2027 (Suche in den PDFs nach Konfidenz, Vertrauens, Schätz, 14.09.2026); die
Zeile folgt dem Wortlaut wie bei der hypergeometrischen Verteilung. Abstände
gelten in Berlin nur über Lotfußpunkte, Abstandsformeln und Hessesche
Normalenform sind dort „nicht notwendig"; der Abstand Punkt–Gerade und
windschiefer Geraden steht nur in den LK-Papieren. Bedingte
Wahrscheinlichkeit gilt überall, der Satz von Bayes und das Axiomensystem von
Kolmogorow nur in Brandenburg. Berlin führt statt der hypergeometrischen
Verteilung das „Lotto-Modell" (Ziehen ohne Zurücklegen über Urnenmodelle);
Aufgaben mit Binomialkoeffizienten-Quotienten sind dort also nicht
ausgeschlossen, die Verteilung als Begriff schon – die Tabelle folgt dem
Wortlaut. Berlin verlangt zusätzlich Wurzelgleichungen (GK „grundlegend",
LK) und die Sachkontexte Geschwindigkeit–Weg, Masse–Volumen–Dichte,
Zeit–Uhrzeit, die in der Themenliste keine eigenen Themen haben.
Kettenregel im Berliner GK nur mit linearer innerer Funktion, in Brandenburg
auch quadratisch. Sinus- und Kosinusfunktionen: Ableitung nur bb-gk, bb-ea
und be-lk; be-gk nur die Sek-I-Form. Matrizen sind in keinem der vier
Papiere Prüfungsgegenstand (das Wort fällt nur bei der MMS-Zulassung). Die
Aufgabengruppe AG/LA (A1) des Pools ist überwiegend Matrizen (Verflechtung,
Übergangsprozesse, Matrizenalgebra, daneben lineare Gleichungssysteme und
ebene Vektorrechnung) und liegt für alle vier Zielprüfungen außerhalb der
Geltung. Nur auf erhöhtem Niveau geprüft werden nach den Brandenburger
Schwerpunkten: Uneigentliche Integrale, Rotationsvolumen, Funktionsscharen
und Ortskurven, Scharen von Geraden und Ebenen, Normalverteilung und
Sigma-Regeln, Hypothesentests, goniometrische Gleichungen innerhalb von
„Gleichungen lösen" (abi.md § 6 nannte auch Wurzelgleichungen als nur
erhöht; Berlin verlangt sie im GK, die Tabelle folgt den Schwerpunkten).
Im Pool kann Erhöhtes auch auf grundlegendem Niveau vorkommen, weil der Pool
für alle Länder gilt; die Markierung ist kein Filter beim Erfassen.

**Rechnerfassung je Zielprüfung ab 2027** (Fakt aus den vier
Prüfungsschwerpunkten 2027, Abschnitt 3 „Hilfsmittel", gelesen 15.09.2026;
Dateien wie in abi-vorgaben.md § 1). Alle vier Papiere regeln es gleich:
Regelfall ist der Taschenrechner, der „nicht programmierbar und nicht
grafikfähig" ist und weder numerisch differenziert oder integriert noch
Gleichungen automatisch löst – das ist die WTR-Fassung des Pools. Kurse, für
die als Prüfungsfach „Mathematik mit MMS" (Brandenburg) bzw. „Mathematik mit
MMS (CAS)" (Berlin) angegeben ist, erhalten die MMS-Aufgaben samt
Erwartungshorizont und nutzen außerhalb des Prüfungsteils A das an der Schule
eingeführte MMS-Rechengerät – das ist die MMS-Fassung des Pools. Eine dritte
Fassung gibt es nicht: „CAS" ist im Pool der Name derselben Fassung bis 2021
(iqb-pruefungen.md § 4, Sondierung), Berlin schreibt „MMS (CAS)", Brandenburg
nur „MMS". Die Wahl ist eine des Kurses, nicht der Prüfung; für jede
Zielprüfung sind deshalb beide Fassungen möglich, WTR als Regelfall.

Die Zeile je Zielprüfung (WTR, MMS, CAS, Fundstelle) steht in § 3 der
Geltungsdatei.

Anmerkungen: Berlin verlangt vom Taschenrechner in Fußnote 1 ausdrücklich,
dass „Werte der Binomialverteilungen ermittelt werden können" (GK S. 6, LK
S. 7); Brandenburg lässt „elementare statistische Funktionen" zu (GK S. 5, LK
S. 6). Zugelassene MMS-Funktionen in allen vier Papieren gleich: Gleichungen
und Gleichungssysteme algebraisch lösen, algebraisch differenzieren und
integrieren, Rechnen mit Vektoren und Matrizen, Werte der Binomial- und
Normalverteilung, Tabellenrechnung, Graphen darstellen. Abschnitt 2.2 aller
vier Papiere: die MMS-Aufgaben haben „vergleichbare inhaltliche Schwerpunkte",
können sich aber „u. U. deutlich" von den Aufgaben ohne MMS unterscheiden und
sind auf kein Gerät ausgerichtet. Folge für den Katalog: WTR ist der
Hauptzweig, MMS wird je Niveau als Delta gemessen (iqb.md § 7); eine CAS-Messung
entfällt, weil es keine eigene Fassung ist.

**Neben der Geltungstabelle: nicht geforderte Inhalte, landesspezifische
Einschränkung, Rahmenlehrpläne** (17.09.2026; Quelle STARK-Bände zum Abitur
2027, Vorspann S. I–III, Angabe des Lehrers; abi.md § 11). Nicht gefordert
auf beiden Niveaus: Erläutern und Entwickeln von Beweisen, Simulationen. GK
zusätzlich: Nutzung von Grenzwerten bei der Bestimmung von Ableitung oder
Integral. LK, nur Land Berlin (be-lk): komplexe gebrochen-rationale
Funktionen. Rahmenlehrplan: Berlin Ausgabe 2021, Fachteil C Mathematik in
der Fassung 2014; Brandenburg Ausgabe 2022 – die beiden Spalten je Niveau
beruhen auf verschiedenen Grundlagen. Prüfung gegen die Tabelle und den
Bestand (Auftrag Teil 3, Punkt 11; Änderungen werden nur vorgeschlagen,
nicht gesetzt): Keines der vier Papiere macht ein Thema der Tabelle als
Ganzes ungültig. „Grenzwerte und Verhalten im Unendlichen" bleibt für be-gk
und bb-gk gültig – das Thema meint das Verhalten von Funktionen, nicht die
Grenzwertdefinition von Ableitung oder Integral; im Bestand gibt es keine
Zeile, die eine solche Definition verlangt (Suche in beiden Katalogen nach
h-Methode, Ober-/Untersumme, Streifenmethode: 0; die Zeilen mit
Differenzenquotient sind mittlere Änderungsraten). Gebrochen-rationale
Funktionen haben kein eigenes Thema (sie laufen unter „Funktionsklassen und
Eigenschaften"); der abi-Bestand enthält keine Zeile dazu, der Pool zwei
einfache (Asymptote einer Logarithmusfunktion, transformierte
Potenzfunktion). Vorschlag: Tabelle unverändert lassen; die Einschränkung
be-lk „komplexe gebrochen-rationale Funktionen nicht gefordert" gilt
unterhalb des Themas und wird beim Blattbau als Filter auf die Zeile
angewendet, sobald ein Fall auftritt. Entscheidung beim Lehrer.

**Ausschlussliste neben der Geltungstabelle** (17.09.2026, Auftrag B Teil 5;
Quelle wie oben). Die Einträge sind Aufgabenformen oder Lösungswege, keine
Themen: sie schränken Zeilen innerhalb gültiger Themen ein und ändern keine
Spalte der Tabelle. Befund im Bestand (Auftrag A, Teil 3; nachgeprüft
17.09.2026 mit 794 abi- und 1258 iqb-Zeilen):

Die Einträge stehen je Zielprüfung in § 2 der Geltungsdatei (Beweise
erläutern oder entwickeln und Simulationen in allen vier; Grenzwerte bei der
Bestimmung von Ableitung oder Integral in be-gk und bb-gk; komplexe
gebrochen-rationale Funktionen in be-lk).

Nutzung: der Blattbau filtert nach § 1 der Geltungsdatei über das Thema und
nach § 2 über die Zeile (operator, verfahren, gegeben); die Liste ist kein
Feld und kein Skriptfilter.

**Vorschlag: strukturelle Geltung nach Jahrgangsklassen** (17.09.2026,
Auftrag B Teil 5; Vorschlag, nicht gesetzt – Entscheidung beim Lehrer). Die
Geltungstabelle sagt, ob ein Thema geprüft wird; sie sagt nicht, ob eine
Zeile aus einem Heft stammt, dessen Prüfungsteil es in der Zielprüfung noch
gibt. Für „Prüfung simulieren" (abi.md § 11) braucht der Blattbau eine
zweite, strukturelle Geltung. Sie ist aus den vorhandenen Feldern ableitbar
und braucht kein neues Feld: `papier` liefert den Jahrgang, `block` den
Prüfungsteil (A hilfsmittelfrei, B mit Hilfsmitteln). Vorgeschlagene Klassen:

| Klasse | Jahrgänge (papier) | Teil A | Teil B | Verwendung im Blattbau |
|---|---|---|---|---|
| vor 2019 | 2017-bb-ea, 2018-be-gk, 2018-bb-ea | Berlin keiner; Brandenburg erhöht 15 BE ohne Wahl | drei Wahlpaare | Typenquelle; für die Simulation nur Teil-B-Zeilen als Ersatz gleicher Sachgebiete |
| 2019–2021 | 2019-be-gk, 2020-be-gk, 2021-be-gk | ohne Wahl (2019: 4, 2020: 5 Einheiten), 2021 Corona-Aufbau | 2019/2020 drei Wahlpaare, 2021 Corona | Typenquelle; Teil-A-Zeilen simulationstauglich (Einheiten zu 5 BE), Teil B als Ersatz |
| 2022/2023 (Corona) | 2022-bebb-gk, 2022-bebb-lk, 2023-bebb-gk, 2023-bebb-lk | Einheiten zu 5 BE mit Fachwahl | Analysis beide Pflicht, Geometrie oder Stochastik | Teil-A-Zeilen simulationstauglich, Teil B als Ersatz |
| 2024 (alter Schlüssel) | 2024-bebb-gk, 2024-bebb-lk | Pflicht + Wahl wie ab 2025 (LK: 4 + 2 von 6) | 35/20/20 bzw. 40/25/25 | Teil A voll, Teil B mit abweichender BE-Summe je Aufgabe |
| ab 2025 | 2025-bebb-gk, 2025-bebb-lk, 2026-bb-gk, 2026-bb-ea | Schlüssel 25 bzw. 30 | 25/15/15 bzw. 30/20/20 | vollständig strukturgleich mit 2027 |

Ableitung: Klasse = f(jahr, papier); die BE-Vektoren je Aufgabe stehen in
abi-struktur.json und in abi-pruefungen.md § 2. Der Blattbau nimmt für eine
Simulation zuerst Zeilen der Klasse „ab 2025", dann „2024", dann die
Teil-A-Zeilen der Klassen 2019–2023, und füllt den Rest mit Zeilen gleicher
Sachgebiete aus allen Klassen; die Geltungstabelle bleibt der erste Filter.

## 4 Gegenstandsklassen je Thema

Schnitt für den Blattbau (Entscheidung 24 in konzept.md, 13.09.2026;
Entscheidung 25: auch für abi). Für den Blattbau zählt der Schnitt Thema ×
Gegenstandsklasse × Handlung (Handlung aus dem ersten Wert von format, § 5).
Die Gegenstandsklasse steht als erstes Wort des Typnamens vor einem
Doppelpunkt („Verflechtung: Rohstoffbedarf über die Verflechtungsmatrix
berechnen"); der Typ nach Kern § 6 bleibt als Feinetikett dahinter erhalten.
Klassen bekommen nur Themen, die mehrere Gegenstände bündeln; Themen,
die selbst schon der Gegenstand sind, führen keine (Typname ohne
Doppelpunkt). Die Zuordnung eines Typs richtet sich nach dem Thema in
abitur-typen.csv. Die Bau-Skripte prüfen, dass jeder Typ eines Themas mit
Klassen ein gültiges Präfix trägt und jeder andere keines.

**Zeilenthema = Typthema** (Entscheidung des Lehrers, 16.09.2026): leitidee
und thema einer Zeile sind leitidee und thema ihres Typs (des ersten Typs,
typ). Tragen Zeile und Typ verschiedene Themen, ist eines von beiden falsch –
entweder gehört die Zeile zu einem anderen Typ, oder der Typ ist im falschen
Thema abgelegt; beides wird im Abgleichlauf entschieden, nicht durch ein
abweichendes Zeilenthema. Beide Bau-Skripte erzwingen die Gleichheit (für
neue Zeilen und in der Selbstprüfung für den Bestand), abitur-abgleich.py prüft sie
nach jedem Lauf; der Schnitt wird über das Thema des Typs gemessen. Bis zum
Abgleichlauf 13 (16.09.2026) trugen 21 Zeilen ein anderes Thema als ihr Typ, und der
Schnitt hing davon ab, welche Spalte gezählt wurde (189 gegen 183 Werte);
die Fälle stehen in abi-pruefungen.md § 4. Anders im Profil fhr, das bei
mehrleistigen Zeilen das Thema nach dem Punkt-Schwerpunkt wählt (fhr.md § 6);
für abi und iqb ist der Schwerpunkt die erste Leistung, also der Typ.

| Thema | Gegenstandsklassen |
|---|---|
| Funktionsklassen und Eigenschaften | Symmetrie · Transformation · Extrempunkte · Nullstellen und Werte |
| Flächeninhalt durch Integration | Integralwert · Fläche |
| Punkte und Strecken im Koordinatensystem | Punkt · Ebene Figur · Körper |
| Lagebeziehungen | Punkt und Ebene · Gerade und Ebene |
| Orthogonalität | Dreieck · Geraden und Ebenen |
| Flächeninhalt und Volumen im Raum | Ebene Figur · Körper |
| Matrizen und Übergangsprozesse | Verflechtung · Übergangsprozess · Matrizenalgebra |
| Zufallsexperimente und Urnenmodelle | Term und Ereignis · Laplace-Experiment · Ziehen ohne Zurücklegen |

Lesart: Integralwert heißt deuten, abschätzen, begründen oder ablesen eines
Integrals (auch über Symmetrie), Fläche heißt berechnen eines Flächeninhalts
(auch mit Maßstab); Nullstellen und Werte umfasst Nullstellen,
Funktionswerte, Punktproben und Definitions- wie Wertemengen (Entscheidung
15.09.2026 beim Umstellungslauf: der Definitionsbereich einer
Logarithmusfunktion gehört hierher, keine eigene Klasse); Ebene Figur sind
Dreieck, Viereck und Quadrat auch im Raum, Körper sind Prisma, Pyramide,
Würfel und Quader (auch ihr Einzeichnen ins Schrägbild); Term und Ereignis
ist das Deuten oder Aufstellen eines Wahrscheinlichkeitsterms,
Laplace-Experiment das Abzählen gleich wahrscheinlicher Ergebnisse
(einschließlich Glücksrad). Lagen zweier Geraden zueinander liegen nicht
unter Lagebeziehungen (Klassen Punkt und Ebene, Gerade und Ebene), sondern
unter Geraden; Quadrat- und Vierecksfragen liegen unter Punkte und Strecken
(Ebene Figur), nicht unter Orthogonalität. Die Liste wächst beim
Abgleichlauf, wenn ein Thema einen weiteren Gegenstand bekommt.

## 5 Handlungen

Die Handlung des Schnitts kommt aus dem ersten Wert des Feldes format. Die
Zuordnung format → Handlung (berechnen, begründen, angeben, zeichnen) steht
seit dem 16.09.2026 im Kern § 5 (katalog-prompt.md v0.4), weil format
Kernvokabular ist; die Bau-Skripte lesen die Tabelle dort. Hier steht sie
nicht mehr, damit es keinen Doppelstand gibt.

## 6 Gemeinsame Typenliste abitur-typen.csv

Eine Typenliste für beide Profile (Entscheidung 25), Felder nach Kern § 6:
typ;leitidee;thema;definition;beispiel_id;status. Die beispiel_id zeigt in
einen der beiden Kataloge (abi-katalog.csv oder iqb-katalog.csv); die
Bau-Skripte prüfen sie gegen beide und verlangen, dass jeder Typ in
mindestens einem Katalog verwendet wird. Neue Typen entstehen im Lauf über
NEUE_TYPEN des jeweiligen Bau-Skripts (Präfixregel § 4); Umbenennungen,
Zusammenziehungen, Definitions- und Themenänderungen laufen nur über
abitur-abgleich.py, das beide Kataloge mitzieht (Kern § 9, Liste alt → neu in
abi-pruefungen.md bzw. iqb-pruefungen.md § 5). Entstanden am 15.09.2026 aus
iqb-typen.csv (792 Typen, Leitliste) und abi-typen.csv (146 Typen) durch
den Umstellungslauf 12 (befund-abi-iqb-typen.md, konzept.md Entscheidung 25).

## 7 Änderungen

- 2026-09-15: angelegt aus iqb.md v1.1 § 5–6 (Sachgebiete, Themenliste,
  Geltungstabelle, Gegenstandsklassen) und HANDLUNG aus iqb-bau.py v0.9;
  abi.md v0.7 § 5–6 abgeglichen. Abweichungen der beiden bisherigen
  Fassungen, hier entschieden: (1) abi.md führte 46 Themen, iqb.md 49 –
  Matrizen und Übergangsprozesse, Konfidenzintervalle und Lineare
  Gleichungssysteme auch unter Analytische Geometrie fehlten in abi.md;
  übernommen sind die 49. (2) abi.md nannte Wurzelgleichungen als nur
  erhöht, die Berliner Schwerpunkte 2027 verlangen sie im GK; die
  Geltungstabelle folgt den Schwerpunkten, die Aufzählung „nur erhöht" nennt
  sie nicht mehr. (3) abi.md § 5 begründete die Sachgebiete gegen die
  KMK-Leitideen, iqb.md § 5 gegen die Alternativen A1/A2 – beide
  Begründungen stehen jetzt in § 1. (4) Die „bekannten Lücken" aus abi.md
  § 6 sind durch die Poolpraxis aufgelöst (§ 2, letzte Anmerkung). (5) Die
  Geltungstabelle stand in iqb.md, obwohl sie Zielprüfungen des Profils abi
  beschreibt; hier ist sie beiden Profilen zugänglich. Lesart der Klassen um
  die vier Fälle des Umstellungslaufs ergänzt (§ 4).
- 2026-09-17 (v1.5, Auftrag D Teil 2): Geltungstabelle, Rechnerfassung und
  Ausschlussliste je Zielprüfung nach abi-<zielprüfung>-geltung.md; § 3 heißt
  „Geltung" und behält Regeln und Anmerkungen.
- 2026-09-16 (v1.1, Auftrag „Themenfeld bereinigen"): Regel Zeilenthema =
  Typthema in § 4, Schnitt über das Thema des Typs; Handlungstabelle in den
  Kern § 5 verschoben (§ 5 verweist); Kopf an Kern v0.4 angepasst
  (Vokabulardatei ist im Kern vorgesehen). Der Typ „Term und Ereignis:
  Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen" gehört seit
  Lauf 13 zur Klasse Term und Ereignis (Ergänzen eines Terms ist Aufstellen).
