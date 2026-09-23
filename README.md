# mathe-nachhilfe

Prüfungskataloge und Themenkatalog für Mathematik-Nachhilfe, Berlin/Brandenburg.
Vergangene Prüfungen werden Zeile für Zeile in Prüfungskataloge geschrieben, je
Prüfungsart ein Profil. Der Themenkatalog beschreibt den Stoff, aus dem Blätter
gebaut werden. Die Prompts und die LaTeX-Vorlage, die daraus Blätter machen, liegen
im eigenen Repo `blattbau` (siehe unten).

Diese Datei ist die einzige Landkarte. Wer eine Datei anlegt, umbenennt oder
entfernt, trägt das hier ein – sonst nirgends.

Umbau 19.09.2026: Ordner statt Präfixe. Dateinamen sind unverändert geblieben, damit
Querverweise in Texten und Skripten weiter stimmen; nur der Ort hat sich geändert.
Die Bau-Skripte laufen im Ordner ihres Profils (`cd abitur && python abi-bau.py`).

## Wo fange ich an

- `uebergabe.md` – Stand und nächster Arbeitsschritt der Prompt-Werkstatt; ein neuer Chat liest sie zuerst. Wird bei jedem Umzug ersetzt.
- `ziel.md` – das Ziel des Blattbaus: beide Blattsorten, Leiter, gemeinsame Regeln, Offenes. Ein neuer Chat liest sie nach uebergabe.md.
- `CLAUDE.md` – wenn im Repo erfasst wird: Ablauf je Heft, Arbeitsregeln, Commit-Regel.
- `katalog-prompt.md` – der Kern: Zeilenregel, die 37 Felder, Vokabular, Prüfung, Abgleichlauf. Gilt für alle Profile.
- `konzept.md` – warum etwas so ist: Bausteine (§ 2), Themenkatalog (§ 3), Entscheidungen mit Kippbedingung (§ 4), Offenes (§ 6), Jahresroutine (§ 7), neue Prüfung aufnehmen (§ 8), Änderungen (§ 10).
- `blatt-konzept.md` – die Heft-Phase: Sprossen, Decke, Merkmalsfrage (§ 7). Bei Widerspruch zum Prüfungsblatt-Prompt gilt es. Liegt hier, weil beide Repos es brauchen.
- `faellig.md` – am Anfang eines Auftrags: Handlungen mit Termin oder Auslöser und bei wem sie liegen.
- `befund-testlauf-2026-09-22.md` – Befund des ersten Katalog-Testlaufs (Lernblatt Prozentrechnung) mit den Beschlüssen, die den Prompt v4.0 tragen.
- `befund-lauf3-2026-09-22.md` – Befund des dritten Testlaufs (Lernblatt Daten, v4.1): Bereitstellung, Stufenschnitt, Werkzeuggrenze, Bausteinliste für Vorlage Stufe 4.
- `themen.csv` – Themenkonkordanz: kanonisches Thema je Katalogthema, alle vier Profile; nach jeder Katalogänderung `python werkzeuge/themen-pruef.py`.
- `eingang/erledigt/` – verarbeitete Protokoll-Archive der Blatt-Chats (lokal, nicht versioniert).
- `blaetter/` – abgelegte Blätter je Thema und Datum, PDFs und Quelltexte; `blaetter/index.md` ist das Register, abgeleitet.
- `werkzeuge/einsortieren.py` – durchsucht die Quellordner (Downloads, OneDrive/Downloads, OneDrive/blatt-eingang) nach `*protokoll*.zip`, schreibt `blaetter/` und den Index; nach jedem neuen Archiv ausführen.

## msa/ – P10 Mathematik, Brandenburg, Oberschule/Gesamtschule (Niveau FOR) und Gymnasium

- `msa.md` – vor dem Erfassen: Kürzel, Leitideen, Themenliste, Besonderheiten; bei Widerspruch zum Kern gilt es.
- `msa-pruefungen.md` – welches Heft als Nächstes dran ist, wo die Hefte liegen, was je Heft geschah.
- `msa-quellen.md` – Jahresseite, Serverdateien je papier-Kürzel, Heftordner `hefte/msa/` (lokal), Dateien ohne Katalogeintrag.
- `msa-typen.csv` – Typen suchen, vergleichen, anlegen; wächst nur über das Bau-Skript; gilt für OS/EBR/FOR und GYM gemeinsam.
- `msa-katalog-basis.csv`, `msa-katalog-kontext.csv` – der Katalog für OS/EBR/FOR (Basisaufgaben, Kontextaufgaben); nie von Hand ändern.
- `msa-katalog-gym.csv` – der Katalog für Papier GYM (Gymnasium, beide Blöcke in einer Datei, Feld block trennt sie); nie von Hand ändern.
- `msa-bau.py` – Heft erfassen oder Bestand prüfen (leeres ZEILEN = Selbstprüfung); deckt OS/EBR/FOR und GYM ab.
- `msa-vorgaben.md` – jährlicher Vorgabencheck, Formatwechsel 2028.
- `msa-ertrag.md`, `msa-ertrag.csv` – Ertrag je Typ, Sortiergröße, Verteilung für die Schwelle „selten“; abgeleitet von `werkzeuge/ertrag.py`, nie von Hand ändern.
- `gym-stand.md` – Stand der GYM-Erfassung je Jahrgang (2014–2025), Befunde je Heft.
- `gym-vergleich.md` – Vergleich der Typen- und Themenverwendung GYM gegen OS/EBR/FOR; abgeleitet von `werkzeuge/gym-vergleich.py`, nie von Hand ändern.
- `gym-bericht-2026-09.md` – Abschlussbericht des Auftrags Gymnasialhefte (23.09.2026): Punktprüfung, neue Typen und Befunde je Heft, Vergleichszahlen, selbst getroffene Entscheidungen.

## fhr/ – Fachhochschulreife Mathematik, Brandenburg

- `fhr.md` – vor dem Erfassen: Kürzel, Themenliste mit Schwerpunktmarkierung, Regel Punkt-Schwerpunkt.
- `fhr-pruefungen.md` – Heftliste, Quelle, Umfang, Änderungslog; alle sechzehn Hefte 2019–2026 erfasst.
- `fhr-quellen.md` – Übersichtsseite, Serverdateien, Heftordner `hefte/fhr/` (lokal).
- `fhr-typen.csv` – Typen suchen oder anlegen.
- `fhr-katalog.csv` – der Katalog; nie von Hand ändern.
- `fhr-bau.py` – Heft erfassen oder Bestand prüfen.
- `fhr-vorgaben.md` – jährlicher Vorgabencheck.
- `fhr-typenbibliothek.py`, `fhr-typenbibliothek.md` – Skript nach jeder Katalogänderung ausführen; die Bibliothek öffnen, wenn ein Blatt zu einem fhr-Typ geplant wird.

## abitur/ – Zentralabitur Berlin/Brandenburg (abi) und IQB-Aufgabenpool (iqb)

Beide Profile in einem Ordner, weil sie sich gegenseitig lesen (Dubletten, gemeinsame
Typenliste, Abgleich).

Profil abi:
- `abi.md` – vor dem Erfassen: Kürzel je Jahrgang, Zielprüfungen, Dubletten und Vormerkungen, Prüfungsgeschichte (§ 10–11); bei Widerspruch zum Kern gilt es.
- `abi-quellen.md` – amtliche Dateien 2011–2018 (44 Dateien, Serverpfade je Jahrgang), Verlagsbände ab 2019, Heftordner `hefte/abi/` (lokal), Markdown-Korpus `hefte-md/` (lokal).
- `abi-pruefungen.md` – nächstes Heft, Kennzahlen, Befunde je Heft und Lauf, Änderungslog.
- `abi-katalog.csv` – der Katalog (Feld block trennt die Teile); nie von Hand ändern.
- `abi-bau.py` – Heft erfassen oder Bestand prüfen; enthält die Zeilen des zuletzt erfassten Hefts.
- `abi-vorgaben.md` – jährlicher Vorgabencheck (Prüfungsschwerpunkte beider Länder; gilt auch für iqb).
- `abi-aufbau.md`, `abi-struktur.json` – nur für 2017/2018: Wahlstruktur, BE-Vektoren, Zwillingsnachweis.
- `abi-be-gk-geltung.md`, `abi-be-lk-geltung.md`, `abi-bb-gk-geltung.md`, `abi-bb-ea-geltung.md` – je Zielprüfung Thema ja/nein, ausgeschlossene Aufgabenformen, Rechnerfassung.

Profil iqb:
- `iqb.md` – vor dem Erfassen eines Stapels: Kennung und id, Stapel als Laufeinheit, Schätzung vor dem Erwartungshorizont, Schwellen, Abbruchkriterium.
- `iqb-quellen.md`, `iqb-quellen.csv`, `iqb-quellen.py` – Pooljahrgänge, Kennungen deuten, Dateiliste erneuern (Cache `iqb-pdf/`, lokal).
- `iqb-pruefungen.md` – nächster Stapel, Reserven, Kennzahlen, Befunde, Änderungslog.
- `iqb-katalog.csv` – der Katalog; nie von Hand ändern.
- `iqb-bau.py` – Stapel erfassen oder Bestand prüfen.

Gemeinsam:
- `abitur-vokabular.md` – Themen, Gegenstandsklassen, Regel Zeilenthema = Typthema; Änderungen an Themen und Klassen nur hier.
- `abitur-typen.csv` – gemeinsame Typenliste; Umbenennen und Zusammenziehen nur über das Abgleich-Skript.
- `abitur-abgleich.py` – nach jedem Heft und Stapel (`python abitur-abgleich.py N`); jeder Lauf bleibt als Code stehen.

## katalog/ – Themenkatalog

73 Einträge, Stand 2026-09-20: 29 Sek-I-Einträge (Stand 2026-09-11j, gegengelesen
bis auf den Punkt [FS]; drei davon seit dem 20.09.2026 mit einem Sek-II-Teil nach
Entscheidung 37, siehe unten) und vierundvierzig Sek-II-Einträge in der Eintragsform nach `konzept.md`
§ 4 Entscheidung 36 (alle Entwurf, nicht gegengelesen): die drei Formproben
`kurvenuntersuchung.md` (Pilot, Analysis, fhr/abi/iqb), `binomialverteilung.md`
(Stochastik, abi/iqb) und `ebenen.md` (Analytische Geometrie, abi/iqb), die fünf
Einträge des Serienbaus Bündel 1 „Ableitung Grundlagen“ (149 Katalogzeilen):
`ableitung-und-aenderungsrate.md`, `ableitungsregeln.md`,
`grenzwerte-und-verhalten-im-unendlichen.md`, `gleichungen-loesen.md` und
`umkehrfunktion.md` (Kurzform), sowie die drei Einträge des Bündels 2 „Ableitung
Anwendung“ (171 Katalogzeilen): `tangente-normale-schnittwinkel.md`,
`extremalprobleme.md` und `ableitungsgraph-und-funktionsgraph.md` – Letzterer der
erste Verweiseintrag (Eintragsart nach dem E36-Zusatz vom 19.09.2026: eigener Kopf,
eigene Verortung und Prüfungsform, die didaktischen Abschnitte je eine Verweiszeile
auf den tragenden Eintrag, hier `kurvenuntersuchung.md` Einheit 4), der eine
Eintrag des Bündels 3 (200 Katalogzeilen, das größte Einzelthema der Serie):
`funktionsklassen-und-eigenschaften.md`, die zwei Einträge des Bündels 4
„Scharen“ (177 Katalogzeilen): `funktionsscharen-und-ortskurven.md` (142 Zeilen,
nach GOST-Plan Leistungskursstoff, der Pool prüft grundlegend in Teil B) und
`rekonstruktion-von-funktionsgleichungen.md` (Steckbriefaufgaben, fhr/abi/iqb), sowie
die sechs Einträge des Bündels 5 „Integral“ (220 Katalogzeilen – die Integralrechnung
damit vollständig): `stammfunktion-und-hauptsatz.md`, `integrationsregeln.md` (Kurzform),
`flaecheninhalt-durch-integration.md` (124 Zeilen, das größte Integralthema, fhr/abi/iqb),
`rekonstruktion-von-bestaenden.md`, `rotationsvolumen.md` (fhr-Pflichtform eines
GOST-LK-Themas) und `uneigentliche-integrale.md` (Kurzform), sowie die vier Einträge
des Bündels 6 „Vektoren/Geraden“ (140 Katalogzeilen, Auftakt der Analytischen
Geometrie neben der Formprobe `ebenen.md`):
`punkte-und-strecken-im-koordinatensystem.md` (83 Zeilen, das größte Thema des
Bündels, mit den Gegenstandsklassen Punkt/Ebene Figur/Körper),
`vektoren-und-rechenoperationen.md` (das Werkzeugthema des Sachgebiets, abi nur
eine Zeile), `linearkombination-und-lineare-abhaengigkeit.md` (Kurzform; erster
Eintrag mit einem Profil ganz ohne Katalogzeile – iqb prüft die Begriffe nur
eingebettet) und `geraden.md` (die Lagebeziehungs- und Schnittthemen folgen in
Bündel 7), sowie die vier Einträge des Bündels 7 „Lage/Winkel“ (154 Katalogzeilen):
`lagebeziehungen.md` (der Lagebefund; Klassen Punkt und Ebene, Gerade und Ebene),
`schnittmengen.md` (die Schnittobjekte samt Spuren und Schnittfiguren; die Anlage
ohne Hilfsmittel nennt die Schnittmenge nicht – Auswendig-Zeilen dort als
begründetes Ermessen mit [IQB-VER]-Beleg), `skalarprodukt-und-winkel.md` (das
Winkelmaß; der Neigungswinkel gegen die Koordinatenebene ist mit 17 Zeilen das
häufigste Einzelverfahren des Sachgebiets, abi stellt das Thema nur in Teil B) und
`orthogonalitaet.md` (Nachweis und Konstruktion senkrechter Objekte; größter
Teil-A-Posten des Sachgebiets mit der höchsten Dublettenquote des Bündels –
elf der vierzehn abi-Zeilen wortgleich aus dem Pool), sowie die vier Einträge
des Bündels 8 „Abstände/Raum“ (212 Katalogzeilen – die Analytische Geometrie
damit vollständig): `abstaende.md` (58 Zeilen; der Plan führt den Abstand
Punkt–Gerade erst im LK-Zusatz, der Pool prüft den Lotfußpunkt auch
grundlegend – als Niveaustufungs-Befund im Eintrag; Abstände paralleler und
windschiefer Geraden sind Planinhalt ohne eine einzige Katalogzeile),
`spiegelung.md` (der GOST nennt die Raumspiegelung in keiner Inhaltszeile –
amtliche Stütze ist allein [IQB-VER 3.2] mit der Stufung „erhöht
uneingeschränkt, grundlegend für Punkte“), `scharen-von-geraden-und-ebenen.md`
(LK-Zusatz beider Länder, Geltung nur be-lk und bb-ea; das Lehrwerk führt kein
Scharen-Kapitel – die Sprossen stützen sich allein auf die Rohdatei) und
`flaecheninhalt-und-volumen-im-raum.md` (78 Zeilen, Klassen Ebene Figur und
Körper; Vektorgeometrie plus Elementarformeln – die Namensvettern
`flaecheninhalt-durch-integration.md` und `rotationsvolumen.md` tragen das
Integral; der Q3-Plan nennt kein Volumen, die Anlage ohne Hilfsmittel führt
Pyramide und Prisma trotzdem als Teil-A-Stoff). Vor Bündel 8 wurde der Befund
aus `punkte-und-strecken-im-koordinatensystem.md` erledigt:
`flaecheninhalt-durch-integration.md` behauptete, die Flächenformeln ebener
Figuren stünden nicht in der Formelsammlung – [FS-IQB 1.1] führt „Maße von
Figuren“ und „Maße von Körpern“, beide Einträge sind berichtigt
(Befundkorrektur 2026-09-20). Bündel 9 ist der eine Eintrag
`matrizen-und-uebergangsprozesse.md` (154 Katalogzeilen, 115 Typen – das größte
Einzelthema des Sek-II-Katalogs; nur iqb, Alternative A1 „Lineare Algebra“ des
Pools, Geltung aller vier Zielprüfungen „nein“, kein Planinhalt, kein
Lehrwerkskapitel, keine Formelsammlungszeile – der Eintrag ruht ganz auf der
Poolpraxis; die Prüfungsrelevanz ab Abitur 2030 ist ungeklärt und wird nach der
Serie gebündelt recherchiert, für den Unterrichtszweck gilt der Eintrag
unabhängig davon; fünf Lerneinheiten entlang der Gegenstandsklassen
Matrizenalgebra, Verflechtung, Übergangsprozess). Dazu die fünf Einträge des
Bündels 10 „Bedingte Wahrscheinlichkeit/Verteilungen“ (108 Katalogzeilen,
Auftakt der Stochastik-Serie neben der Formprobe `binomialverteilung.md`):
`vierfeldertafel.md` (das Darstellungsmittel – der Begriff bedingte
Wahrscheinlichkeit liegt beim Nachbareintrag),
`bedingte-wahrscheinlichkeit-und-bayes.md` (39 Zeilen; Befund: der Satz von
Bayes steht namentlich nur im Brandenburger Plan, Berlin und der Pool prüfen
den Quotienten und die Baumumkehr ohne den Namen), `unabhaengigkeit.md`
(erstes Stochastik-Thema mit eigenem fhr-Bestand – die FHR-Kette
Vierfeldertafel → Produktregel jährlich seit 2023),
`zufallsgroessen-und-verteilungen.md` (Kurzform; die nackte Verteilung ohne
Modellkontext, alle Zeilen Teil A) und `hypergeometrische-verteilung.md`
(Kurzform; einziges Thema des Bündels mit einem Geltungs-Länderunterschied:
Brandenburg ja, Berlin nein – die Landeshefte prüfen es häufiger als der
Pool). Den Abschluss bilden die vier Einträge des Bündels 11
„Kenngrößen/Beurteilende Statistik“ (127 Katalogzeilen – damit ist die
Sek-II-Serie der Entscheidung 36 abgeschlossen, alle Sek-II-Themen der
`themen.csv` haben einen Eintrag): `kenngroessen-von-verteilungen.md`
(73 Zeilen, nach Zeilen das größte Stochastik-Thema neben der Formprobe;
Länderbefund: der allgemeine diskrete Erwartungswert ist in Berlin formal
LK-Stoff, in Brandenburg GK-Kern Q2 – der Pool prüft ihn grundlegend und die
IQB-Vereinbarungen setzen Varianz und Standardabweichung voraus; die Anlage
ohne Hilfsmittel nennt keine Streumaße, der Pool prüft die σ-Formeln
trotzdem hilfsmittelfrei), `normalverteilung-und-sigma-regeln.md` (LK-Zusatz
beider Länder, Geltung nur be-lk und bb-ea, im Pool erst seit 2022 – die
vier Teil-A-Zeilen sind sämtlich Darstellungsdeutungen),
`hypothesentests.md` (LK-Zusatz, alle Zeilen Teil B; zweiseitige Tests,
Alternativtests und normalverteilte Testgrößen sind Planinhalt ohne
Katalogzeile; mit 2022-bebb-lk-B4g die erste abgewandelte Poolzeile der
Stochastik-Serie; Befundkorrektur im selben Lauf: die Formelsammlung führt
einen Abschnitt „Signifikanztest“ mit beiden Fehlerarten) und
`konfidenzintervalle.md` (reines Poolthema wie die Matrizen: kein
Planinhalt, kein Lehrwerkskapitel, keine Landeszeile, Geltung viermal
„nein“ – die Formelsammlung führt die Grenzgleichung trotzdem wörtlich; die
Relevanz künftiger Jahrgänge klärt die gebündelte Geltungsrecherche nach
der Serie; die ersten MMS-Zeilen des Stochastik-Serienbaus). Nach der Serie der
erste Eintrag nach Entscheidung 37 (Sek-II-Zeilen an Sek-I-Themen):
`zufallsexperimente-und-pfadregeln.md` (237 Katalogzeilen aus fhr, abi und iqb – das
größte Einzelthema des Katalogs und Trägerthema von neun Stochastik-Einträgen; acht
Lerneinheiten entlang der Baumtypen der Fachdidaktik-Quelle [FD-BAUM] – Ereignisse als
Mengen, Laplace, unabhängige Stufen, ohne Zurücklegen, Mammutbäume, Situationsbäume,
Term und Ereignis, Rückwärts; der Sek-I-Eintrag `wahrscheinlichkeit.md` bleibt
unverändert und wird als Blatt 0 verwiesen; Befund: neun Einträge verweisen als Blatt 0 auf den
Sek-I-Eintrag, vier davon müssten auf den neuen zeigen – nur geprüft, nicht geändert; am 21.09.2026
gerichtet, samt den sechs Verortungssätzen der Stochastik-Abnehmer).
Am selben Tag der zweite und letzte Neubau nach Entscheidung 37: `kombinatorik.md`
(32 Katalogzeilen aus fhr, abi und iqb; drei Lerneinheiten – Zählprinzip und
Anordnungen, Auswahlen und Binomialkoeffizient, Zählen mit Bedingungen und
Wahrscheinlichkeitsterme; Vollform, die Kurzform trägt 32 Zeilen in 18 Typen nicht;
Voraussetzung von `zufallsexperimente-und-pfadregeln.md` und `binomialverteilung.md`,
deren Verweise seitdem auf seine Einheiten 1 und 2 zeigen; der Sek-I-Anteil des Zählens
bleibt in `wahrscheinlichkeit.md` Einheit 1; Befund: alle vier abi-Zeilen sind
Pooldubletten, das fhr-Thema ist Prüfungsschwerpunkt nur 2026/27 und trotzdem seit 2019
jährlich geprüft), dazu die drei nach Entscheidung 37 erweiterten Sek-I-Einträge –
`daten.md` (Einheit 6 neu: Kenngrößen aus Häufigkeitstabellen und Klassen, 30
Sek-II-Zeilen, fast alle fhr), `lineare-gleichungssysteme.md` (Einheit 5 neu: drei
Variablen, Lösbarkeit mit Parameter, Lösungsscharen; 14 Poolzeilen, alle Teil A) und
`einheiten.md` (keine neue Einheit: der Maßstab des Koordinatensystems in den Einheiten
1, 3 und 4; 9 fhr-Zeilen) – je mit einem Abschnitt „Prüfungsform (fhr / abi / iqb)“,
Auswendig-Zeilen in den betroffenen Kästen, Stufe „Sek I + II“ und unveränderter
P10-Prüfungsform (einzige Ausnahme: die Zuordnungszeile nennt die neue Einheit als
„kein P10-Typ“, weil `_pruef_struktur.py` das verlangt). Damit ist Entscheidung 37
abgeschlossen: Kennzahl 5 steht auf 23 von 2883 (von 345 vor der Entscheidung); die 23
liegen in fertigen Einträgen (18 in kurvenuntersuchung, fünf Einzelzeilen in terme,
prozentrechnung, extrem-und-sattelpunkte und wendepunkte) und werden getrennt geklärt.
Zweck und Arbeitsteilung mit den
Prüfungskatalogen: `konzept.md` § 3. Bis zum Umbau lag der Themenkatalog nur in Lieferzips
der Prompt-Werkstatt, nicht im Repo.

- je Thema eine Datei (`bruchrechnung.md`, `prozentrechnung.md` …): Lerneinheiten, Voraussetzungen, Grundvorstellung, Sprossen, Merkkasten, Fehlerquellen, Zielmarke; Sek-II-Einträge mit Prüfungsform je Profil (fhr / abi / iqb) aus der Rohdatei `rohdaten/<kanonisch>.md`, Zahl der Lerneinheiten frei (zufallsexperimente-und-pfadregeln acht, funktionsklassen-und-eigenschaften sechs, kurvenuntersuchung, binomialverteilung, tangente-normale-schnittwinkel, funktionsscharen-und-ortskurven, flaecheninhalt-durch-integration, punkte-und-strecken-im-koordinatensystem und matrizen-und-uebergangsprozesse fünf, ebenen, ableitung-und-aenderungsrate, gleichungen-loesen, stammfunktion-und-hauptsatz, geraden, lagebeziehungen, skalarprodukt-und-winkel, orthogonalitaet, abstaende, scharen-von-geraden-und-ebenen, flaecheninhalt-und-volumen-im-raum und kenngroessen-von-verteilungen vier, ableitungsregeln, grenzwerte-und-verhalten-im-unendlichen, extremalprobleme, rekonstruktion-von-funktionsgleichungen, rekonstruktion-von-bestaenden, vektoren-und-rechenoperationen, schnittmengen, spiegelung, bedingte-wahrscheinlichkeit-und-bayes, unabhaengigkeit, normalverteilung-und-sigma-regeln, hypothesentests, konfidenzintervalle und kombinatorik drei, umkehrfunktion, integrationsregeln, rotationsvolumen, uneigentliche-integrale, linearkombination-und-lineare-abhaengigkeit, vierfeldertafel, zufallsgroessen-und-verteilungen und hypergeometrische-verteilung zwei; der Verweiseintrag ableitungsgraph-und-funktionsgraph ohne eigene Einheiten; die erweiterten Sek-I-Einträge nach Entscheidung 37: daten sechs, lineare-gleichungssysteme fünf, einheiten vier Einheiten). Jeder Merkkasten eines Sek-II-Eintrags trägt seit dem 19.09.2026 eine Zeile „Auswendig (Teil A):" (Entscheidung 36, Kastenform), die nennt, welche Kastenteile laut Anlage ohne Hilfsmittel ohne Rechner und Formelsammlung sitzen müssen; in den erweiterten Sek-I-Einträgen tragen sie die Kästen, die Sek-II-Zeilen betreffen.
- `index.md` – Tabelle je Sek-I-Thema (Leitidee, Stufe, Klasse, P10, Status) mit Gegenlese-Verlauf und CSV-Themen-Zuordnung für Kennzahl 6 (`_pruef_struktur.py`); seit dem Sek-II-Piloten auch eine Sek-II-Tabelle (Profile, Zeilen/Typen aus `themen.csv`).
- `_quellen.md` – Zweck, Aufbau, Notation je Thema, Quellenregister mit Kürzeln (seit 19.09.2026 auch [GOST], [FOS], [BASICS], [COSH], [FS-IQB], [IQB-VER], [IQB-STR]; seit 20.09.2026 die Fachdidaktik-Quelle [FD-BAUM], Bartz 2008, Baumtypen als Gliederungsraster).
- `_quellenprotokoll.md` – was aus welcher Quelle gelesen wurde.
- `_formelsammlung.md` – Prüfliste [FS]; steht zur Streichung (Abschnittsverweis nicht haltbar, Adresse der Formelsammlung nicht feststellbar).
- `_tragfaehigkeit.md` – Tragfähigkeit der Themen (seit 21.09.2026): wie oft ein Thema in den Blatt-0-Abschnitten der anderen Einträge vorausgesetzt wird (Tabelle A, mit eigenen Katalogzeilen und Nachfragern), wie viele Themen ein Eintrag voraussetzt (Tabelle B), Messlücken; abgeleitet von `werkzeuge/tragfaehigkeit.py`, nie von Hand ändern. Öffnen, wenn die Reihenfolge der Blätter geplant wird – als Rangliste, nicht als Absolutwert.
- `_verweise.md` – Verweis- und Namensprüfung (seit 21.09.2026): jeder Verweis `<name>.md` aller Abschnitte nach Ziel (in `katalog/`, anderswo im Repo, fehlt), Einheitsnummern hinter Verweisen gegen die Lerneinheiten der Zieldatei, Namensgleichheit von Dateinamen, H1, `themen.csv`, Vokabular, Geltungstabellen und Typenkatalogen, Gegenrichtung der Blatt-0-Verweise, Formlücke mit jeder Wortform-Nennung als Zitat; abgeleitet von `werkzeuge/verweis-pruef.py`, nie von Hand ändern. Öffnen, bevor Verweise oder Namen im Katalog geändert werden, und vor dem Umbau der Blatt-Prompte.
- `_blatt0-belege.md` – Belege der Blatt-0-Fertigkeiten ohne Ziel (seit 21.09.2026): je Eintrag die Fertigkeitszeilen unter „Voraussetzungen (Blatt 0)“, die keinen Verweis `<name>.md` auf einen anderen Eintrag tragen, mit Wortlaut, Quellenklammer in Bestandteilen (sechs Sorten: P10-Typ, LS-AA-Kapitel, RLP mit Zitat, RLP ohne Zitat, MSK-Code, sonstiges) und dem, was die Register des Repos dazu hergeben (Typ und Thema aus `msa/msa-typen.csv` und den msa-Katalogen, Kapitel- und Lerneinheitstitel aus dem LS-AA-Fahrplan, Fundstelle mit Niveaustufe im RLP-Text, Bausteintitel aus `_quellen.md`), dazu die wörtlichen `themen.csv`-Treffer; Teil 1 die 22 Sek-I-Einträge des Auftrags Blatt-0-Dateiverweise, Teil 2 die übrigen; abgeleitet von `werkzeuge/blatt0-belege.py`, nie von Hand ändern. Öffnen, wenn entschieden wird, ob eine Fertigkeit ohne Ziel ein Katalogthema bekommt oder einen Verweis – die Datei schlägt vor, sie entscheidet nicht.
- `_niveaustufen-belege.md` – Belege der Niveaustufe je Lerneinheit und Sprosse der Sek-I-Einträge aus RLP und LISUM (seit 24.09.2026): je Eintrag die [RLP]-Klammern der Verortung, die eine Stufe nennen, je Lerneinheit und je Sprosse die Stufe mit Fundstelle im Rahmenlehrplantext (Zeilen, Block, Buchstabe am Block, Seitenkopf) und wortgleichem Standard oder „keine Stelle“, die Reihenlage in den LISUM-Planungshilfen (getrennte Reihen EBR/FOR und GYM oder Differenzierungshinweis) und die Zeile „Spanne: ja/nein“; abgeleitet aus den Einträgen und den beiden Quellentexten, nie von Hand ändern. Öffnen, wenn entschieden wird, welche Marke eine Einheit oder Sprosse für die Schulformfrage des Unterrichtsblatt-Prompts ab v4.3 bekommt – die Datei schlägt vor, sie entscheidet nicht.
- `_kursart-belege.md` – Belege der Kursart je Einheit und Typ der Sek-II-Einträge aus Geltungstabellen, GOST und Prüfungsform (seit 24.09.2026): je Eintrag die Geltung der vier Zielprüfungen wortgleich mit Zeilennummer, je Lerneinheit die Kursartmarke des Eintrags und die Stelle im Berliner und im Brandenburger GOST-Text mit ihrem Block (Grund- und Leistungskursfach oder Leistungskurszusatz) oder „keine Stelle“, je Haupttyp der Prüfungsform die Zählung Zeilen GK / Zeilen LK und die Zeile „Spanne: ja/nur LK/nur GK/kein Planinhalt“; abgeleitet aus Einträgen, Geltungstabellen, GOST-Texten und Katalogen, nie von Hand ändern. Öffnen, wenn entschieden wird, welche LK-Marke eine Einheit oder ein Typ bekommt – die Datei schlägt vor, sie entscheidet nicht.
- `_pruef_katalog.py`, `_pruef_struktur.py` – Prüfskripte (Sek-II-Modus: Zählzeile und Profillisten gegen `themen.csv`, Einheitsnummern E1–E9; `_pruef_struktur.py` gibt die Kennzahlen 1–9 aus, Kennzahl 7 „Einträge ohne Verweis in Blatt 0“ seit 21.09.2026 mit der Zählregel aus `werkzeuge/tragfaehigkeit.py`, Kennzahl 8 „Verweisbefunde“ – Verweise auf fehlende Dateien, Einheitsnummern größer als vorhanden – seit 21.09.2026 mit der Zählregel aus `werkzeuge/verweis-pruef.py`, Kennzahl 9 „Fertigkeitszeilen ohne Ziel in Blatt 0“ seit 21.09.2026 mit der Zählregel aus `werkzeuge/blatt0-belege.py`); `_suche_quelle.py` – Suche in den zweispaltigen Quellentexten.

Kastenform entschieden (19.09.2026, Entscheidung 36 „Kastenform"): Arbeitskästen je Lerneinheit mit Auswendig-Zeile; der themenweite Stundenanker ist Kompositionsregel des Unterrichtsblatt-Prompts (Posten in `faellig.md` § 2). Offen: [FS]-Abschnittsverweis am PDF, Mechanik-Punkte (A4 breit/eng, Prüflisten, Prüflistenzeilen 10 und 11). Kein Blatt ist bisher aus einem Eintrag gebaut worden.

## rohdaten/ – Rohdateien je Thema

Lesestoff für Katalogeinträge: je kanonischem Thema aus `themen.csv` eine Datei
`<kanonisch>.md` mit Teil A Typenprofil (jeder Haupttyp mit Zeilenzahl, Profilen, Jahren
und Definition aus der Typenliste, dazu die Nebentypen) und Teil B Zeilenliste (eine Zeile
je Katalogzeile, nach Profil, Typ, Jahr, id). Abgeleitet aus `themen.csv` und den fünf
Katalogen, nie von Hand ändern; neu bauen mit `python werkzeuge/rohdatei-bau.py [thema ...]`.
66 Dateien – alle kanonischen Themen mit Katalogzeilen; die 7 ohne Zeilen haben keine Datei.

## quellen/ – Quellentexte

Textfassungen der Quellen, die alle Katalogeinträge brauchen, damit sie nicht in jedem
Chat neu geholt werden. Herkunft, Stand, Lizenz und Suchfallstricke in `quellen/quellen.md`.

- `quelle-rlp-teil-c-mathematik-2023.txt` – Rahmenlehrplan 1–10, Teil C Mathematik, gültig ab 2025/26.
- `quelle-lisum-planungshilfen-7bis10.txt` – LISUM-Planungshilfen 7–10, Gesamtdatei 2024, CC BY-SA 4.0.
- `quelle-klett-fahrplan-ls-aa-berlin-2024.txt` – Lambacher Schweizer, Fahrplan Berlin 2024.
- `quelle-rlp-gost-bb-2022-mathematik.txt` – Rahmenlehrplan GOST Brandenburg, Teil C Mathematik, gültig ab 2022/23.
- `quelle-rlp-gost-be-2022-mathematik.txt` – Rahmenlehrplan GOST Berlin, Teil C Mathematik, gültig ab 2014.
- `quelle-rlp-gost-2022-mathematik-anlage-ohimi.txt` – Anlage zum RLP GOST: Inhalte ohne Hilfsmittel, Grundlage für Prüfungsteil A.
- `quelle-rlp-fos-bb-2019-mathematik.txt` – Rahmenlehrplan Fachoberschule Mathematik, Brandenburg, gültig ab 2019.
- `quelle-iqb-formelsammlung-2024-mathematik.txt` – IQB-Formelsammlung, nur Teil 1 Mathematik, Stand 2024, © IQB.
- `quelle-iqb-operatoren-2019.txt` – IQB, Grundstock von Operatoren, Stand 2019, © IQB.
- `quelle-iqb-vereinbarungen-2022.txt` – IQB, Inhaltliche Vereinbarungen zur Gestaltung der Aufgaben, Stand 2022, © IQB.
- `quelle-iqb-struktur-2024.txt` – IQB, Beschreibung der Struktur der Aufgaben, Stand 2024, © IQB.

Das LISUM wurde zum 31.12.2024 aufgelöst; die Texte werden nicht mehr fortgeschrieben
und ihre Adressen sind nicht gesichert. Deshalb liegen sie hier.

## werkzeuge/ – Bände und Korpus

Lesen die Kataloge, ändern nichts. Ausgabeordner `baende/` und `korpus/` sind lokal (`.gitignore`).

- `band-anleitung.md`, `band-bau.py`, `fhr-band-struktur.py`, `fhr-band.csv` – Sammelbände aus den Originalseiten.
- `korpus-bau.py`, `korpus-protokoll.md` – Markdown-Korpus und OCR der Prüfungshefte.
- `themen-inventar.py`, `themen-inventar.md` – Themennamen aller vier Prüfungskataloge gezählt; Vorstufe der Themenkonkordanz.
- `themen-pruef.py` – prüft `themen.csv` gegen Kataloge, `katalog/` und Vokabular; nach jeder Katalogänderung ausführen, Rückgabewert 0 nur bei bestandener Prüfung (v0.2 seit 20.09.2026: Prüfung 4 lässt einen kanonischen Sek-II-Namen mit eigener Katalogdatei zu – Namensregel der Entscheidung 37).
- `rohdatei-bau.py` – schreibt je kanonischem Thema `rohdaten/<kanonisch>.md` aus `themen.csv` und den Katalogen; ohne Argument alle Themen mit Katalogzeilen.
- `tragfaehigkeit.py` – zählt je Eintrag von `katalog/` die Verweise `<name>.md` im Abschnitt „Voraussetzungen (Blatt 0)“ und schreibt `katalog/_tragfaehigkeit.md` (Nachfrage je Thema, Einstiegshürde je Eintrag, Messlücken); nach jeder Änderung an einem Blatt-0-Abschnitt ausführen; `katalog/_pruef_struktur.py` importiert die Zählregel für Kennzahl 7.
- `verweis-pruef.py` – prüft die Einträge von `katalog/` auf Dateiverweise, Einheitsnummern, Namensgleichheit (mit `themen.csv`, `abitur/abitur-vokabular.md`, den vier `abitur/abi-*-geltung.md`, `msa/msa-typen.csv` und `fhr/fhr-typen.csv`), Gegenrichtung und Formlücke und schreibt `katalog/_verweise.md`; Lesarten für Blatt 0, Verweisform und Wortform aus `tragfaehigkeit.py` importiert, die Themenliste aus `themen-pruef.py`; nach jeder Katalogänderung ausführen; `katalog/_pruef_struktur.py` importiert die Zählregel für Kennzahl 8.
- `blatt0-belege.py` – sammelt je Eintrag von `katalog/` die Fertigkeitszeilen des Abschnitts „Voraussetzungen (Blatt 0)“ (vor der Zwischenzeile „Erkennungsschritte…“) ohne Verweis `<name>.md` auf einen anderen Eintrag, zerlegt ihre Quellenklammer in Bestandteile (sechs Sorten) und löst sie gegen `msa/msa-typen.csv`, die msa-Kataloge, `themen.csv`, den LS-AA-Fahrplan und den RLP-Text in `quellen/` sowie die Registerzeile [MSK] in `katalog/_quellen.md` auf; schreibt `katalog/_blatt0-belege.md`; Lesarten für Blatt 0 und Verweisform aus `tragfaehigkeit.py` importiert; Gegenprobe im Skript (22 Einträge des Auftrags: 147/131/16 seit v0.2, sonst wird nichts geschrieben – ändert ein Auftrag die Aufteilung, wird sie nachgezogen); nach jeder Änderung an einem Blatt-0-Abschnitt ausführen; `katalog/_pruef_struktur.py` importiert die Zählregel für Kennzahl 9.
- `ertrag.py` – zählt je Typ aus `msa/msa-typen.csv` Haupt- und Nebenzeilen, Jahrgänge, Punkte, block und niveau_geschaetzt sowie das Mittel von schritte aus den msa-Katalogen und schreibt `msa/msa-ertrag.csv` und `msa/msa-ertrag.md` (Ertrag als Sortiergröße, Verteilung als Hilfe für die Schwelle „selten“); Gegenprobe im Skript; nach jeder Änderung an den msa-Katalogen oder an `msa-typen.csv` ausführen; liest nur `msa-katalog-basis.csv`/`msa-katalog-kontext.csv`, nicht `msa-katalog-gym.csv`.
- `gym-vergleich.py` – vergleicht Typen- und Themenverwendung (Haupttyp) zwischen `msa-katalog-gym.csv` und den Papieren OS/EBR/FOR und schreibt `msa/gym-vergleich.md` (je drei Zahlen/Listen: nur GYM, nur OS/EBR/FOR, in beiden); nach jeder Änderung an `msa-katalog-gym.csv` oder den OS/EBR/FOR-Katalogen ausführen.

## archiv/ – eingefroren

Datierte Befunde und Werkstattzettel. Beschreiben den Stand ihres Datums, werden nicht
fortgeschrieben, kein Chat muss sie lesen. `namensschema.md` liegt hier, weil der Umbau
auf Ordner es überholt hat.

## Nicht im Repo (lokal, `.gitignore`)

`hefte/` gescannte Prüfungshefte (urheberrechtlich geschützt), `hefte-md/` Markdown-Korpus
der Verlagsbände, `korpus/` maschineller Korpus, `baende/` Sammelbände, `iqb-pdf/` Cache.

## Repo blattbau – anderes Projekt

`unterrichtsblatt.md`, `pruefungsblatt.md`, `mathblatt.sty`, `Anleitung_mathblatt.md`,
`CHANGELOG.md` und die Testauswertungen liegen seit dem Umbau im eigenen Repo. Der
Prüfungsblatt-Prompt lädt die Kataloge per Abruf aus diesem Repo; nach dem Umbau müssen die
Pfade dort auf die Profilordner zeigen (`msa/msa-typen.csv` statt `msa-typen.csv`).
