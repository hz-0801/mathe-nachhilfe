# VOKABULAR – Sachgebiete, Themen, Gegenstandsklassen, Handlungen, Geltung
Version 1.0 · 15.09.2026 · gilt für die Profile abi und iqb (konzept.md, Entscheidung 25)

Diese Datei ist die eine Quelle für alles, was abi und iqb an Vokabular
oberhalb des Typs teilen: Sachgebiet (§ 1), Themenliste (§ 2),
Geltungstabelle (§ 3), Gegenstandsklassen (§ 4), Handlungen (§ 5) und die
Regeln der gemeinsamen Typenliste abitur-typen.csv (§ 6). abi-bau.py, iqb-bau.py
und abgleich.py lesen sie; abi.md und iqb.md verweisen hierher und führen
nur, was profilspezifisch ist. Der Kern (katalog-prompt.md) bleibt
unverändert: er sagt, dass Leitidee und Thema „im Profil" stehen – für abi
und iqb steht beides hier, das Profil verweist darauf. Bis zum 15.09.2026
standen Themenliste und Klassen in abi.md § 5–6 und iqb.md § 5–6 doppelt;
die Fassung von iqb.md war die jüngere und ist hier übernommen, die
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

## 3 Geltungstabelle

Ob ein Thema Prüfungsgegenstand ist, hängt von Land und Niveau ab. Quelle
sind die vier Prüfungsschwerpunkte 2027 (Berlin ps_mathematik_2027_gk/lk,
Brandenburg PS_Mathematik_GK/LK_2027; gelesen am 13.09.2026, Ablage in
abi-vorgaben.md § 1). ja = in den Schwerpunkten genannt, nein = nicht
genannt. Die Bau-Skripte lesen die Tabelle und zählen je Heft oder Stapel die
Zeilen, deren Thema für eine Zielprüfung nicht gilt; gefiltert wird über das
Thema, ein Zeilenfeld gibt es dafür nicht (Geltung ist eine Eigenschaft des
Themas, nicht der Zeile). Das Abbruchkriterium der Erfassung (iqb.md § 6)
zählt neue Schnittwerte innerhalb der Geltung.

| Thema | be-gk | be-lk | bb-gk | bb-ea |
|---|---|---|---|---|
| Gleichungen lösen | ja | ja | ja | ja |
| Lineare Gleichungssysteme | ja | ja | ja | ja |
| Funktionsklassen und Eigenschaften | ja | ja | ja | ja |
| Umkehrfunktion | ja | ja | ja | ja |
| Grenzwerte und Verhalten im Unendlichen | ja | ja | ja | ja |
| Ableitung und Änderungsrate | ja | ja | ja | ja |
| Ableitungsregeln | ja | ja | ja | ja |
| Tangente, Normale, Schnittwinkel | ja | ja | ja | ja |
| Kurvenuntersuchung | ja | ja | ja | ja |
| Ableitungsgraph und Funktionsgraph | ja | ja | ja | ja |
| Funktionsscharen und Ortskurven | nein | ja | nein | ja |
| Rekonstruktion von Funktionsgleichungen | ja | ja | ja | ja |
| Extremalprobleme | ja | ja | ja | ja |
| Stammfunktion und Hauptsatz | ja | ja | ja | ja |
| Integrationsregeln | ja | ja | ja | ja |
| Flächeninhalt durch Integration | ja | ja | ja | ja |
| Rekonstruktion von Beständen | ja | ja | ja | ja |
| Uneigentliche Integrale | nein | ja | nein | ja |
| Rotationsvolumen | nein | ja | nein | ja |
| Punkte und Strecken im Koordinatensystem | ja | ja | ja | ja |
| Vektoren und Rechenoperationen | ja | ja | ja | ja |
| Linearkombination und lineare Abhängigkeit | ja | ja | ja | ja |
| Geraden | ja | ja | ja | ja |
| Ebenen | ja | ja | ja | ja |
| Lagebeziehungen | ja | ja | ja | ja |
| Schnittmengen | ja | ja | ja | ja |
| Skalarprodukt und Winkel | ja | ja | ja | ja |
| Orthogonalität | ja | ja | ja | ja |
| Abstände | ja | ja | ja | ja |
| Flächeninhalt und Volumen im Raum | ja | ja | ja | ja |
| Scharen von Geraden und Ebenen | nein | ja | nein | ja |
| Spiegelung | ja | ja | ja | ja |
| Matrizen und Übergangsprozesse | nein | nein | nein | nein |
| Ereignisse und Mengenoperationen | ja | ja | ja | ja |
| Zufallsexperimente und Urnenmodelle | ja | ja | ja | ja |
| Kombinatorik | ja | ja | ja | ja |
| Baumdiagramm und Pfadregeln | ja | ja | ja | ja |
| Vierfeldertafel | ja | ja | ja | ja |
| Bedingte Wahrscheinlichkeit und Bayes | ja | ja | ja | ja |
| Unabhängigkeit | ja | ja | ja | ja |
| Lage- und Streumaße einer Stichprobe | ja | ja | ja | ja |
| Zufallsgrößen und Verteilungen | ja | ja | ja | ja |
| Binomialverteilung | ja | ja | ja | ja |
| Kenngrößen von Verteilungen | ja | ja | ja | ja |
| Hypergeometrische Verteilung | nein | nein | ja | ja |
| Normalverteilung und Sigma-Regeln | nein | ja | nein | ja |
| Hypothesentests | nein | ja | nein | ja |
| Konfidenzintervalle | nein | nein | nein | nein |

Anmerkungen zur Tabelle: Konfidenzintervalle nennt keines der vier Papiere
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

| Zielprüfung | WTR | MMS | CAS | Fundstelle |
|---|---|---|---|---|
| be-gk | zugelassen, Regelfall (Taschenrechner nach Abschnitt 3) | zugelassen für Kurse mit Prüfungsfach „Mathematik mit MMS (CAS)", dann MMS-Aufgaben | keine eigene Fassung, in Berlin „MMS (CAS)" | ps_mathematik_2027_gk.pdf, Abschnitt 3 (S. 6 mit Fußnote 1, S. 7), Abschnitt 2.2 (S. 2) |
| be-lk | zugelassen, Regelfall | zugelassen für Kurse mit „Mathematik mit MMS (CAS)" | keine eigene Fassung, „MMS (CAS)" | ps_mathematik_2027_lk.pdf, Abschnitt 3 (S. 7 mit Fußnote 1), Abschnitt 2.2 (S. 2) |
| bb-gk | zugelassen, Regelfall („Mathematik ohne MMS") | zugelassen für Schulen mit Prüfungsfach „Mathematik mit MMS", dann MMS-Aufgaben | nicht genannt (nur MMS) | PS_Mathematik_GK_2027.pdf, Abschnitt 3 (S. 5 mit Fußnote 1, S. 6), Abschnitt 2.2 (S. 2) |
| bb-ea | zugelassen, Regelfall („Mathematik ohne MMS") | zugelassen für Schulen mit „Mathematik mit MMS" | nicht genannt (nur MMS) | PS_Mathematik_LK_2027.pdf, Abschnitt 3 (S. 6 mit Fußnote 1), Abschnitt 2.2 (S. 2) |

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

## 4 Gegenstandsklassen je Thema

Schnitt für den Blattbau (Entscheidung 24 in konzept.md, 13.09.2026;
Entscheidung 25: auch für abi). Für den Blattbau zählt der Schnitt Thema ×
Gegenstandsklasse × Handlung (Handlung aus dem ersten Wert von format, § 5).
Die Gegenstandsklasse steht als erstes Wort des Typnamens vor einem
Doppelpunkt („Verflechtung: Rohstoffbedarf über die Verflechtungsmatrix
berechnen"); der Typ nach Kern § 6 bleibt als Feinetikett dahinter erhalten.
Unterklassen bekommen nur Themen, die mehrere Gegenstände bündeln; Themen,
die selbst schon der Gegenstand sind, führen keine (Typname ohne
Doppelpunkt). Die Zuordnung eines Typs richtet sich nach dem Thema in
abitur-typen.csv, nicht nach dem Thema der einzelnen Zeile. Die Bau-Skripte prüfen,
dass jeder Typ eines Themas mit Klassen ein gültiges Präfix trägt und jeder
andere keines.

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

Die Handlung des Schnitts kommt aus dem ersten Wert des Feldes format (Kern
§ 5). Die Bau-Skripte lesen diese Tabelle.

| format | Handlung |
|---|---|
| Rechnung | berechnen |
| Begründung | begründen |
| Kurzantwort | angeben |
| Ankreuzen | angeben |
| Tabelle | angeben |
| Zeichnen | zeichnen |
| Eintragen | zeichnen |
| Konstruieren | zeichnen |

## 6 Gemeinsame Typenliste abitur-typen.csv

Eine Typenliste für beide Profile (Entscheidung 25), Felder nach Kern § 6:
typ;leitidee;thema;definition;beispiel_id;status. Die beispiel_id zeigt in
einen der beiden Kataloge (abi-katalog.csv oder iqb-katalog.csv); die
Bau-Skripte prüfen sie gegen beide und verlangen, dass jeder Typ in
mindestens einem Katalog verwendet wird. Neue Typen entstehen im Lauf über
NEUE_TYPEN des jeweiligen Bau-Skripts (Präfixregel § 4); Umbenennungen,
Zusammenziehungen, Definitions- und Themenänderungen laufen nur über
abgleich.py, das beide Kataloge mitzieht (Kern § 9, Liste alt → neu in
abi-pruefungen.md bzw. iqb-pruefungen.md § 5). Entstanden am 15.09.2026 aus
iqb-typen.csv (792 Typen, Leitliste) und abi-typen.csv (146 Typen) durch
den Umstellungslauf 12 (abi-iqb-typen.md, konzept.md Entscheidung 25).

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
