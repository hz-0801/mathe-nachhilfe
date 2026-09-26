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

- `uebergabe.md` – Stand und nächster Arbeitsschritt der Prompt-Werkstatt; ein neuer Chat liest sie zuerst. Stand 2026-09-26. Wird bei jedem Umzug ersetzt; die vorige liegt dann in `archiv/`.
- `ziel.md` – das Ziel des Blattbaus: beide Blattsorten, Leiter, gemeinsame Regeln, Offenes. Ein neuer Chat liest sie nach uebergabe.md.
- `CLAUDE.md` – wenn im Repo erfasst wird: Ablauf je Heft, Arbeitsregeln, Commit-Regel.
- `katalog-prompt.md` – der Kern: Zeilenregel, die 37 Felder, Vokabular, Prüfung, Abgleichlauf. Gilt für alle Profile.
- `konzept.md` – warum etwas so ist: Bausteine (§ 2), Themenkatalog (§ 3), Entscheidungen mit Kippbedingung (§ 4), Offenes (§ 6), Jahresroutine (§ 7), neue Prüfung aufnehmen (§ 8), Änderungen (§ 10).
- `blatt-konzept.md` – die Heft-Phase: Sprossen, Decke, Merkmalsfrage (§ 7). Bei Widerspruch zum Prüfungsblatt-Prompt gilt es. Liegt hier, weil beide Repos es brauchen.
- `faellig.md` – am Anfang eines Auftrags: Handlungen mit Termin oder Auslöser und bei wem sie liegen.
- `befund-testlauf-2026-09-22.md` – Befund des ersten Katalog-Testlaufs (Lernblatt Prozentrechnung) mit den Beschlüssen, die den Prompt v4.0 tragen.
- `befund-lauf3-2026-09-22.md` – Befund des dritten Testlaufs (Lernblatt Daten, v4.1): Bereitstellung, Stufenschnitt, Werkzeuggrenze, Bausteinliste für Vorlage Stufe 4.
- `befund-foerderhefte-2026-09-24.md` – Befund der Förderheft-Formen (Klick!, Kohl) gegen unterrichtsblatt.md v4.2 und ziel.md § 2 „Option schwach“, mit Revisionsvorschlag für die Option „schwach“; Befund, kein Beschluss.
- `befund-schwach-blatt-2026-09-24.md` – Befund des Prüfstein-Blatts „prozentsatz 7 schwach“ (v4.2, Opus) gegen den MSK-Baustein P A: was stimmt, fünf Abweichungen nach Wirkung geordnet, Folgerung für die Revision der Option „schwach“ in v4.3.
- `nacht-bericht-2026-09-25.md` – Bericht des Auftrags Nacht 2026-09-25: Teil 1 Inhaltsverzeichnisse (LS BE/BB, Klasse 5/6, weitere Reihen), Teil 2 Klassenbelege je Lerneinheit (Zahlenblock, Gegenproben, Verlagsmarken), Teil 3 fremde Aufgabensammlungen und Fundstellen, je Teil offene Punkte und eigene Entscheidungen.
- `nacht-bericht-2026-09-26.md` – Bericht des Auftrags Nacht 2026-09-26: Teil 1 Kennzahlen je Blatt (Vergleichstabelle, Gegenprobe mit vier Abweichungen), Teil 2 Prüfungswort-Belege (Verteilung für die Schwelle „oft“, Themenregel, Befunde zu Einträgen), Teil 3 Sek-II-Ordnung nach Halbjahr und Kursart (Stochastik bei Bigalke/Köhler meist Band 11), Teil 4 Ermessensfälle nach Sorten; je Teil offene Punkte und eigene Entscheidungen.
- `nacht-bericht-2026-09-27.md` – Bericht des Auftrags Nacht 2026-09-27: zehn Teile (Belegskripte und Marken, FHR-Wort, potenz-exponentialfunktionen, Kleinposten, Vorrat-Verweise mit Zuordnungstabelle, Quellen und Pfade, Vorschläge, Prüfskript Stufe 5, CAS-Nachtrag 2017/2018, 2017-be-gk mit den Stapeln 2017 und Abgleichlauf 24); je Teil Gegenprobe, eigene Entscheidungen, offene Punkte.
- `nacht-bericht-2026-09-28.md` – Bericht des Auftrags Nacht 2026-09-28: sieben Teile (Befund Testlauf abgelegt, Stapel 2017-ea-B WTR und CAS mit Abgleichlauf 25, der gescheiterte Delta-Stapel 2018-ea-B CAS, Berliner CAS-Hefte gemessen, Sek-II-Einträge nachgezogen, blatt-pruef.py v0.4 und marken-bau-Gegenprobe, Eichung Pool 2017, Prüfstein Übersichtsblatt); je Teil Gegenprobe, eigene Entscheidungen, offene Punkte.
- `bericht-marken.md` – Bericht des Auftrags Marken (26.09.2026): Zahlen der Marken-Zeilen und Typklammern, Gegenproben mit Ist-Wert, Regel A und B (Stellen außerhalb von Datei 2 mit Grund), Einheiten ohne Stelle einer Schulform, eigene Entscheidungen, Befunde der Prüfskripte. Öffnen, wenn eine Marken-Zeile nicht einleuchtet.
- `themen.csv` – Themenkonkordanz: kanonisches Thema je Katalogthema, alle vier Profile; nach jeder Katalogänderung `python werkzeuge/themen-pruef.py`.
- `eingang/erledigt/` – verarbeitete Protokoll-Archive der Blatt-Chats (lokal, nicht versioniert).
- `blaetter/` – abgelegte Blätter je Thema und Datum, PDFs und Quelltexte; `blaetter/index.md` ist das Register, abgeleitet. Testläufe des Unterrichtsblatt-Prompts liegen dort datiert als `blaetter/testlauf-<datum>/` und stehen nicht im Register `blaetter/index.md`.
- `blaetter/testlauf-2026-09-25/` – erster Testlauf (Prompt v4.3, zehn Eingaben aus `werkzeuge/testlauf-eingaben.csv`, je Eingabe eine Sub-Agent-Sitzung): `stand.md`, je Eingabe ein Ordner mit PDFs, entpacktem Protokoll-Archiv und `sitzung.txt`, `kennzahlen.md`, `lesezettel.md`, die Promptkopie `unterrichtsblatt-v4.3.md`. Öffnen zum Gegenlesen (erst `lesezettel.md`) oder um einen späteren Testlauf danebenzulegen.
- `blaetter/uebersicht/` – Übersichtsblätter für den Lehrer, je Thema eine Seite aus den Merkkästen des Katalogeintrags (Beschluss 26.09.2026, befund-testlauf-2026-09-25.md): `<thema>/<datum>/` mit `src/uebersicht.tex`, `pdf/uebersicht.pdf`, Seitenbild `pdf/uebersicht.png` und `protokoll.txt` (Quelle je Block). Seit 28.09.2026 die Prüfsteine quadratische-funktionen (Objektthema) und prozentrechnung (Verfahrensthema), an denen der Chat die Form entscheidet; nicht im Register `blaetter/index.md`, `einsortieren.py` und `blatt-pruef.py` kennen die Sorte nicht.
- `bericht-testlauf-2026-09-25.md` – Bericht des Testlaufs: Bauweise (Ersatzweg), Tabelle je Eingabe (Anläufe, Aufrufe, Seiten, Zeit), die drei Gegenproben mit Ist-Wert, eigene Entscheidungen, Abweichungen der Sitzungen vom Prompt.
- `befund-testlauf-2026-09-25.md` – Lesebefunde des Lehrers (26.09.2026) am Fokus (Eingabe 7) und am Schwach-Blatt (Eingabe 3) des Testlaufs, je Befund mit Ziel: Prompt v4.4, Vorlage Stufe 6, Katalog, Werkzeug, Beschluss (Übersichtsblatt, Beispiel nur auf Zuruf). Öffnen vor v4.4 und vor dem nächsten Testlauf.
- `beschluss-2026-09-26.md` – die fünf Urteile des Chats vom 26.09.2026 nachmittags auf den Nachtbericht 2026-09-28 (Übersichtsblatt vertagt, Eichung Abitur-Pool mit Deutungslisteneintrag (f), Abgrenzung der Berliner CAS-Hefte, Sollwert kreis 1, Katalogbefunde als Vorschläge); umgesetzt durch den Auftrag Nacht 2026-09-29. Öffnen, wenn eine dieser Regeln begründet werden muss.
- `blaetter/kennzahlen.md` – Kennzahlen je Blatt (seit 26.09.2026): je PDF Seiten, Hauptnummern und Teilaufgaben (gesamt und je Seite), Titel wortgleich mit Titelform, Darstellungen, Antwortform, Merkkästen, erstes Auftreten der Fachwörter des Merkkastens und Sprossenabgleich gegen „Typen je Lerneinheit“, oben eine Vergleichstabelle über alle Blätter; abgeleitet von `werkzeuge/blatt-pruef.py`, nie von Hand ändern. Öffnen, wenn zwei Läufe desselben Themas verglichen werden.
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
- `gym-abgleich.csv` – entschiedene Abgleichliste (alt;neu;thema_neu;art) des Auftrags Abgleichlauf GYM (24.09.2026); Eingabe für `werkzeuge/typen-abgleich.py`.
- `gym-abgleich-log.md` – Log des Abgleichlaufs: geänderte Zeilen je id, Themenwechsel durch Zeilenthema = Typthema, Themenumbenennung, Statusänderung; abgeleitet, nie von Hand ändern.
- `ebr-vergleich.md` – Vergleich der Typen- und Themenverwendung EBR gegen FOR/OS (Auftrag Nacht, Teil 1, 24.09.2026); abgeleitet von `werkzeuge/gym-vergleich.py --gruppen`, nie von Hand ändern.
- `nacht-stand.md` – Standdatei des Auftrags Nacht (24.09.2026): Stand je Teil (offen/erledigt) für einen unbeaufsichtigten Lauf.
- `nacht-bericht-2026-09-24.md` – Bericht des Auftrags Nacht (24.09.2026): Teil 1 EBR-Erfassung und -Vergleich, Teil 2 Fundliste Stoffverteilungspläne, Teil 3 Vorgabenprüfung fhr.

## fhr/ – Fachhochschulreife Mathematik, Brandenburg

- `fhr.md` – vor dem Erfassen: Kürzel, Themenliste mit Schwerpunktmarkierung, Regel Punkt-Schwerpunkt.
- `fhr-pruefungen.md` – Heftliste, Quelle, Umfang, Änderungslog; alle sechzehn Hefte 2019–2026 erfasst.
- `fhr-quellen.md` – Übersichtsseite, Serverdateien, Heftordner `hefte/fhr/` (lokal).
- `fhr-typen.csv` – Typen suchen oder anlegen.
- `fhr-katalog.csv` – der Katalog; nie von Hand ändern.
- `fhr-bau.py` – Heft erfassen oder Bestand prüfen.
- `fhr-vorgaben.md` – jährlicher Vorgabencheck.
- `fhr-vorgaben-pruefung-2026-09.md` – Prüfung des Vorbehalts (Schritt 0, Auftrag Nacht Teil 3, 24.09.2026): jede Angabe aus § 1–3 gegen die Papiere gehalten, Ergebnis je Angabe.
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
- `befund-eichung-2017-2026-09-28.md` – die abweichenden Zeilen der Poolstapel 2017 (ga-A, ga-B WTR; zum Vergleich ea-B WTR und CAS, der gescheiterte 2018-ea-B CAS) mit erster Schätzung, amtlichem Bereich, Grund der Korrektur und Regel der engen Fassung, dazu die Eichung je Pooljahr und Niveau (erster Lauf, heute); kein Urteil. Öffnen, wenn im Chat über die Eichung des Pools 2017 oder die Deutungsliste entschieden wird.
- `befund-cas-berlin-2026-09-28.md` – Messung der vier Berliner CAS-Hefte 2017/2018 gegen die WTR-Fassung je Teilaufgabe (wortgleich/abweichend, Art der Abweichung, schon vorhandene Zeilen der BB-CAS-Hefte); kein Urteil. Öffnen, wenn im Chat die Abgrenzung nach abi.md § 9 entschieden wird.

Profil iqb:
- `iqb.md` – vor dem Erfassen eines Stapels: Kennung und id, Stapel als Laufeinheit, Schätzung vor dem Erwartungshorizont, Schwellen, Abbruchkriterium.
- `iqb-quellen.md`, `iqb-quellen.csv`, `iqb-quellen.py` – Pooljahrgänge, Kennungen deuten, Dateiliste erneuern (Cache `hefte/iqb/`, lokal; seit 27.09.2026 Standard des Skripts, vorher `iqb-pdf/`).
- `iqb-pruefungen.md` – nächster Stapel, Reserven, Kennzahlen, Befunde, Änderungslog.
- `iqb-katalog.csv` – der Katalog; nie von Hand ändern.
- `iqb-bau.py` – Stapel erfassen oder Bestand prüfen.
- `arbeitsstand/2018-ea-B-cas/` – Arbeitsstand des nicht erfassten Delta-Stapels 2018-ea-B (CAS) (Auftrag Nacht 2026-09-28: Eichschranke gerissen, iqb-pruefungen.md § 4): blinde und geprüfte Schätzungen, Typwahl je Zeile, Landesheftabgleich, `eichung.py` (aus `abitur/` starten, schreibt nichts). Öffnen für einen Wiederanlauf nach der Entscheidung des Lehrers.

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

- je Thema eine Datei (`bruchrechnung.md`, `prozentrechnung.md` …): Lerneinheiten, Voraussetzungen, Grundvorstellung, Sprossen, Merkkasten, Fehlerquellen, Zielmarke; Sek-II-Einträge mit Prüfungsform je Profil (fhr / abi / iqb) aus der Rohdatei `rohdaten/<kanonisch>.md`, Zahl der Lerneinheiten frei (zufallsexperimente-und-pfadregeln acht, funktionsklassen-und-eigenschaften sechs, kurvenuntersuchung, binomialverteilung, tangente-normale-schnittwinkel, funktionsscharen-und-ortskurven, flaecheninhalt-durch-integration, punkte-und-strecken-im-koordinatensystem und matrizen-und-uebergangsprozesse fünf, ebenen, ableitung-und-aenderungsrate, gleichungen-loesen, stammfunktion-und-hauptsatz, geraden, lagebeziehungen, skalarprodukt-und-winkel, orthogonalitaet, abstaende, scharen-von-geraden-und-ebenen, flaecheninhalt-und-volumen-im-raum und kenngroessen-von-verteilungen vier, ableitungsregeln, grenzwerte-und-verhalten-im-unendlichen, extremalprobleme, rekonstruktion-von-funktionsgleichungen, rekonstruktion-von-bestaenden, vektoren-und-rechenoperationen, schnittmengen, spiegelung, bedingte-wahrscheinlichkeit-und-bayes, unabhaengigkeit, normalverteilung-und-sigma-regeln, hypothesentests, konfidenzintervalle und kombinatorik drei, umkehrfunktion, integrationsregeln, rotationsvolumen, uneigentliche-integrale, linearkombination-und-lineare-abhaengigkeit, vierfeldertafel, zufallsgroessen-und-verteilungen und hypergeometrische-verteilung zwei; der Verweiseintrag ableitungsgraph-und-funktionsgraph ohne eigene Einheiten; die erweiterten Sek-I-Einträge nach Entscheidung 37: daten sieben – Einheit 7 Vierfeldertafel (Sek I) seit 26.09.2026 –, lineare-gleichungssysteme fünf, einheiten vier Einheiten; potenz-exponentialfunktionen seit 26.09.2026 fünf). Unter jeder Nummernzeile steht seit dem 26.09.2026 eine erzeugte Zeile „Marken:“ – Sek I Einführungsklasse Oberschule und Gymnasium aus den Lehrwerken, Prüfungswort („P10 oft“, „P10“, „keine P10-Aufgabe“) und „nicht für alle“ (Verlagsmarken), Sek II Halbjahr Berlin und Brandenburg, Kursart, „Abitur GK“, „Abitur LK“, „FHR“ –, und Typen, die ein Lehrwerksverzeichnis einzeln nennt, tragen ihre Klasse in eckigen Klammern („[OS 5, GYM 6]“); gebaut von `werkzeuge/marken-bau.py` aus den drei Belegdateien, nie von Hand ändern. Jeder Merkkasten eines Sek-II-Eintrags trägt seit dem 19.09.2026 eine Zeile „Auswendig (Teil A):" (Entscheidung 36, Kastenform), die nennt, welche Kastenteile laut Anlage ohne Hilfsmittel ohne Rechner und Formelsammlung sitzen müssen; in den erweiterten Sek-I-Einträgen tragen sie die Kästen, die Sek-II-Zeilen betreffen.
- `index.md` – Tabelle je Sek-I-Thema (Leitidee, Stufe, Klasse, P10, Status) mit Gegenlese-Verlauf und CSV-Themen-Zuordnung für Kennzahl 6 (`_pruef_struktur.py`); seit dem Sek-II-Piloten auch eine Sek-II-Tabelle (Profile, Zeilen/Typen aus `themen.csv`).
- `_quellen.md` – Zweck, Aufbau, Notation je Thema, Quellenregister mit Kürzeln (seit 19.09.2026 auch [GOST], [FOS], [BASICS], [COSH], [FS-IQB], [IQB-VER], [IQB-STR]; seit 20.09.2026 die Fachdidaktik-Quelle [FD-BAUM], Bartz 2008, Baumtypen als Gliederungsraster).
- `_quellenprotokoll.md` – was aus welcher Quelle gelesen wurde.
- `_formelsammlung.md` – Prüfliste [FS]; steht zur Streichung (Abschnittsverweis nicht haltbar, Adresse der Formelsammlung nicht feststellbar).
- `_tragfaehigkeit.md` – Tragfähigkeit der Themen (seit 21.09.2026): wie oft ein Thema in den Blatt-0-Abschnitten der anderen Einträge vorausgesetzt wird (Tabelle A, mit eigenen Katalogzeilen und Nachfragern), wie viele Themen ein Eintrag voraussetzt (Tabelle B), Messlücken; abgeleitet von `werkzeuge/tragfaehigkeit.py`, nie von Hand ändern. Öffnen, wenn die Reihenfolge der Blätter geplant wird – als Rangliste, nicht als Absolutwert.
- `_verweise.md` – Verweis- und Namensprüfung (seit 21.09.2026): jeder Verweis `<name>.md` aller Abschnitte nach Ziel (in `katalog/`, anderswo im Repo, fehlt), Einheitsnummern hinter Verweisen gegen die Lerneinheiten der Zieldatei, Namensgleichheit von Dateinamen, H1, `themen.csv`, Vokabular, Geltungstabellen und Typenkatalogen, Gegenrichtung der Blatt-0-Verweise, Formlücke mit jeder Wortform-Nennung als Zitat; abgeleitet von `werkzeuge/verweis-pruef.py`, nie von Hand ändern. Öffnen, bevor Verweise oder Namen im Katalog geändert werden, und vor dem Umbau der Blatt-Prompte.
- `_blatt0-belege.md` – Belege der Blatt-0-Fertigkeiten ohne Ziel (seit 21.09.2026): je Eintrag die Fertigkeitszeilen unter „Voraussetzungen (Blatt 0)“, die keinen Verweis `<name>.md` auf einen anderen Eintrag tragen, mit Wortlaut, Quellenklammer in Bestandteilen (sechs Sorten: P10-Typ, LS-AA-Kapitel, RLP mit Zitat, RLP ohne Zitat, MSK-Code, sonstiges) und dem, was die Register des Repos dazu hergeben (Typ und Thema aus `msa/msa-typen.csv` und den msa-Katalogen, Kapitel- und Lerneinheitstitel aus dem LS-AA-Fahrplan, Fundstelle mit Niveaustufe im RLP-Text, Bausteintitel aus `_quellen.md`), dazu die wörtlichen `themen.csv`-Treffer; Teil 1 die 22 Sek-I-Einträge des Auftrags Blatt-0-Dateiverweise, Teil 2 die übrigen; abgeleitet von `werkzeuge/blatt0-belege.py`, nie von Hand ändern. Öffnen, wenn entschieden wird, ob eine Fertigkeit ohne Ziel ein Katalogthema bekommt oder einen Verweis – die Datei schlägt vor, sie entscheidet nicht.
- `_niveaustufen-belege.md` – Belege der Niveaustufe je Lerneinheit und Sprosse der Sek-I-Einträge aus RLP und LISUM (seit 24.09.2026): je Eintrag die [RLP]-Klammern der Verortung, die eine Stufe nennen, je Lerneinheit und je Sprosse die Stufe mit Fundstelle im Rahmenlehrplantext (Zeilen, Block, Buchstabe am Block, Seitenkopf) und wortgleichem Standard oder „keine Stelle“, die Reihenlage in den LISUM-Planungshilfen (getrennte Reihen EBR/FOR und GYM oder Differenzierungshinweis) und die Zeile „Spanne: ja/nein“; abgeleitet aus den Einträgen und den beiden Quellentexten, nie von Hand ändern. Öffnen, wenn entschieden wird, welche Marke eine Einheit oder Sprosse für die Schulformfrage des Unterrichtsblatt-Prompts ab v4.3 bekommt – die Datei schlägt vor, sie entscheidet nicht.
- `_kursart-belege.md` – Belege der Kursart je Einheit und Typ der Sek-II-Einträge aus Geltungstabellen, GOST und Prüfungsform (seit 24.09.2026): je Eintrag die Geltung der vier Zielprüfungen wortgleich mit Zeilennummer, je Lerneinheit die Kursartmarke des Eintrags und die Stelle im Berliner und im Brandenburger GOST-Text mit ihrem Block (Grund- und Leistungskursfach oder Leistungskurszusatz) oder „keine Stelle“, je Haupttyp der Prüfungsform die Zählung Zeilen GK / Zeilen LK und die Zeile „Spanne: ja/nur LK/nur GK/kein Planinhalt“; abgeleitet aus Einträgen, Geltungstabellen, GOST-Texten und Katalogen, nie von Hand ändern. Öffnen, wenn entschieden wird, welche LK-Marke eine Einheit oder ein Typ bekommt – die Datei schlägt vor, sie entscheidet nicht.
- `_klassen-belege.md` – Klassenbelege je Lerneinheit der Sek-I-Einträge aus den Inhaltsverzeichnissen der Lehrwerke (seit 25.09.2026): je Lerneinheit und Regelreihe (Oberschule: Sekundo, Mathematik 2023, Schnittpunkt, Mathematik heute; Gymnasium: Lambacher Schweizer, Fundamente, Elemente, mathe.delta) die Verzeichniszeile wortgleich mit Klasse, Seite und Zeilennummer oder „keine Stelle“ mit Grund, die Typzeilen, die Verlagsmarken, die Förderheftstellen, die Zusammenfassung „OS: Kl. n“ / „GYM: Kl. n“ und je Eintrag „Spanne OS/GYM“, „Boden“ und die Ermessensfälle; abgeleitet aus den Einträgen und den Verzeichnisdateien unter `quellen/`, nie von Hand ändern. Öffnen, wenn entschieden wird, in welcher Klasse eine Einheit auf der Zeitachse (`ziel.md` § 1) steht und was „nicht für alle“ ist – die Datei schlägt vor, sie entscheidet nicht.
- `_pruefungswort-belege.md` – Belege für das Prüfungswort der Zweigzeile (seit 26.09.2026): Sek I je Lerneinheit und Typ die P10-Typen, die ihn prüfen (Zuordnung mit Grund, Themenregel nach `themen.csv`), je P10-Typ die Kennzahlen aus `msa/msa-ertrag.csv`, je Einheit P10-Jahrgänge (von 13), Zahl der P10-Typen und Summe ertrag, „keine P10-Aufgabe“ mit dem Vermerk aus `themen.csv`, die Verteilung für die Schwelle „oft“ je Einheit und je Typ; Sek II je Einheit und Typ die Abitur-Jahrgänge GK und LK und die FHR-Jahrgänge; abgeleitet von `werkzeuge/pruefungswort-belege.py`, nie von Hand ändern. Öffnen, wenn die Schwelle „oft“ gesetzt oder das Prüfungswort eines Zweigs bestimmt wird – die Datei schlägt vor, sie entscheidet nicht.
- `_sek2-ordnung-belege.md` – Ordnung der Sek-II-Lerneinheiten nach Halbjahr und Kursart (seit 26.09.2026, Vorschlagsliste): je Sek-II-Eintrag und Lerneinheit (dazu die Sek-II-Einheiten von daten und lineare-gleichungssysteme) die Stellen im GOST-Plan Berlin und Brandenburg mit Kurshalbjahr und Block, die FOS-Stelle mit Themenfeld, die Kapitelzeilen in Bigalke/Köhler (GK/LK 11 und 12, Reihenfolge-Quelle), Fundamente (Einführungsphase), Elemente NRW und Neue Wege Berlin 2011 (Gegenproben), die Zusammenfassung „Halbjahr: … · GK/LK: …“, „nur LK: ja/nein“ und Ermessen; oben eine Übersicht je Eintrag; abgeleitet von `werkzeuge/sek2-ordnung-belege.py`, nie von Hand ändern. Öffnen, wenn entschieden wird, in welchem Halbjahr und für welche Kursart ein Sek-II-Blatt eine Einheit einordnet – die Datei schlägt vor, sie entscheidet nicht.
- `_klassen-ermessen.md` – die 250 Ermessensfälle aus `_klassen-belege.md` mit Eintrag, Einheit, Reihe, Zitat und Grund, gruppiert nach der Sorte des Grundes (neun Sorten aus dem Wortlaut, oben mit Zahl; seit 26.09.2026); abgeleitet von `werkzeuge/klassen-ermessen.py`, nie von Hand ändern. Öffnen, wenn das Urteil über die Klassenbelege im Chat gebündelt fallen soll – die Datei ordnet, sie bewertet nicht.
- `_marken-entscheidungen.md` – die Urteile des Chats vom 26.09.2026 über die 38 Ermessensfälle mit Urteilsbedarf aus `_klassen-ermessen.md`, dazu Regel A (Vorstufe setzt keine Klasse), Regel B (Verlagsmarke setzt keine Klasse) und die Schwelle „P10 oft“ (7 von 13); von Hand geschrieben, `werkzeuge/marken-bau.py` liest Regel B, die Schwelle und die Fälle. Öffnen, wenn eine Marken-Zeile erklärt oder eine Klassenzuordnung neu entschieden werden soll.
- `_marken-neue-einheiten.md` – die drei Ergänzungen des Chats vom 26.09.2026, die vor dem ersten Markenlauf eingearbeitet wurden: potenz-exponentialfunktionen Einheit 5 (Potenzfunktionen), daten Einheit 7 (Vierfeldertafel, Sek I) und daten Einheit 1 um Klassen erweitert; Wortlaut und Stelle. Öffnen, wenn nachvollzogen werden soll, woher diese Einheiten kommen.
- `_vorschlaege-2026-09-27.md` – Vorschläge für das Urteil im Chat (Auftrag Nacht 2026-09-27, Teil 7), „Vorschlag, nicht entschieden“: (1) Ausbau von potenz-exponentialfunktionen Einheit 5 und daten Einheit 7 in der Form des Eintrags (Merkkasten, Sprossen, Zielmarke, Typische Fehler, Blatt 0, Verortung), (2) Sinussatz und Lösbarkeit quadratischer Gleichungen auf Niveaustufe G, (3) Nebentyp von 2025-GYM-K5d, (4) die 28 Namensabweichungen H1/thema; von Hand geschrieben. Öffnen, wenn einer dieser Posten im Chat entschieden wird.
- `_vorschlaege-sprossen-2026-09-29.md` – Vorschläge zur Sprossenregel (befund-testlauf-2026-09-25.md, Katalog 2; Auftrag Nacht 2026-09-29, Teil 7): alle 29 Sek-I-Einträge nach _klassen-belege.md, je Lerneinheit die Kette unter „Sprossen je Verfahrenstyp“ gegen die Regel „Vorformen vor dem Universalverfahren, Abkürzungen danach“; sechs Vorschläge (darunter die Einheitenfolge von quadratische-gleichungen), eine Bestätigung. Vorschlag, nicht entschieden; öffnen, wenn der Chat über die Sprossenfolge urteilt.
- `_vorschlaege-2026-09-29.md` – Vorschläge für das Urteil im Chat (Auftrag Nacht 2026-09-29): je Katalogbefund 3–8 aus befund-testlauf-2026-09-25.md ein Abschnitt (Teil 8; was fehlt im Wortlaut des Eintrags, fertige Katalogzeilen, Beleg je Zeile – Prüfungs-id, Lehrwerksstelle aus _klassen-belege.md oder RLP; 22 Zeilen, eine ohne Beleg) und der Abschnitt Sek-II-Nachzug (Teil 4 Punkt 7: neue Einheiten nur als Vorschlag). Vorschlag, nicht entschieden; öffnen, wenn einer dieser Posten im Chat entschieden wird.
- `_fremdoriginale-belege.md` – Fundstellen fremder Originalaufgaben für die 22 Sprossen mit „kein P10-Original“ (seit 25.09.2026): je Typ Eintrag, Einheit, Typname und Sprossenzeile wortgleich, dazu höchstens fünf Aufgaben aus den gesicherten Sammlungen anderer Länder (`quellen/fremdsammlungen-fundliste.md`, Texte lokal unter `hefte/fremd/`) mit Sammlung, Jahr, Aufgabennummer, Zeilen, einem Satz zur Aufgabe und Punktzahl, „Teil:“ bei Teilleistung, oder „keine Fundstelle“; abgeleitet, nie von Hand ändern. Öffnen, wenn für eine Prüfungshöhe ohne P10-Original eine Originalaufgabe als Decke gesucht wird – die Datei nennt Fundstellen, sie bewertet nicht.
- `_pruef_katalog.py`, `_pruef_struktur.py` – Prüfskripte (Sek-II-Modus: Zählzeile und Profillisten gegen `themen.csv`, Einheitsnummern E1–E9; `_pruef_struktur.py` gibt die Kennzahlen 1–9 aus, Kennzahl 7 „Einträge ohne Verweis in Blatt 0“ seit 21.09.2026 mit der Zählregel aus `werkzeuge/tragfaehigkeit.py`, Kennzahl 8 „Verweisbefunde“ – Verweise auf fehlende Dateien, Einheitsnummern größer als vorhanden – seit 21.09.2026 mit der Zählregel aus `werkzeuge/verweis-pruef.py`, Kennzahl 9 „Fertigkeitszeilen ohne Ziel in Blatt 0“ seit 21.09.2026 mit der Zählregel aus `werkzeuge/blatt0-belege.py`); `_suche_quelle.py` – Suche in den zweispaltigen Quellentexten.

Kastenform entschieden (19.09.2026, Entscheidung 36 „Kastenform"): Arbeitskästen je Lerneinheit mit Auswendig-Zeile; der themenweite Stundenanker ist Kompositionsregel des Unterrichtsblatt-Prompts (Posten in `faellig.md` § 2). Offen: [FS]-Abschnittsverweis am PDF, Mechanik-Punkte (A4 breit/eng, Prüflisten, Prüflistenzeilen 10 und 11). Kein Blatt ist bisher aus einem Eintrag gebaut worden.

## rohdaten/ – Rohdateien je Thema

Lesestoff für Katalogeinträge: je kanonischem Thema aus `themen.csv` eine Datei
`<kanonisch>.md` mit Teil A Typenprofil (jeder Haupttyp mit Zeilenzahl, Profilen, Jahren
und Definition aus der Typenliste, dazu die Nebentypen) und Teil B Zeilenliste (eine Zeile
je Katalogzeile, nach Profil, Typ, Jahr, id). Abgeleitet aus `themen.csv` und den fünf
Katalogen, nie von Hand ändern; neu bauen mit `python werkzeuge/rohdatei-bau.py [thema ...]`.
68 Dateien – alle kanonischen Themen mit Katalogzeilen; die 6 ohne Zeilen haben keine Datei (seit 27.09.2026 hat strahlensaetze eine, weil themen.csv den Maßstab dort führt).

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
- `quelle-westermann-elemente-der-mathematik-bb-2016.txt` – Stoffverteilungspläne Elemente der Mathematik SI, Ausgabe 2016 für Berlin/Brandenburg, Klasse 5–9.
- `quelle-westermann-sekundo-bb-2017.txt` – Stoffverteilungspläne Sekundo, Ausgabe 2017 für Berlin und Brandenburg, Klasse 7–10.
- `lehrwerke-fundliste.md` – Fundliste der Stoffverteilungspläne/Synopsen (Teil 2) und der Inhaltsverzeichnisse (Teil 3) für Landesausgaben BE/BB: je Lehrwerk gefunden/nicht gefunden/nicht frei verfügbar.
- `quelle-cornelsen-fundamente-bb-ausgabeb2024-inhalt.txt` – Inhaltsverzeichnisse Fundamente der Mathematik, Ausgabe B ab 2024, Klasse 7–10, aus der DNB.
- `quelle-cornelsen-fundamente-bb-ausgabeb2017-inhalt.txt` – dieselbe Reihe, Vorgängerausgabe B ab 2017, nur Klasse 9 gesichert.
- `quelle-westermann-mathematik2023-bebbstth-inhalt.txt` – Inhaltsverzeichnisse Mathematik, Ausgabe 2023 für BE/BB/Sachsen-Anhalt/Thüringen, Klasse 7–10, aus der DNB.
- `quelle-westermann-mathematikheute-bebb-inhalt.txt` – Inhaltsverzeichnisse Mathematik heute (Ausgabe für Berlin/Brandenburg), Klasse 7–10, aus der DNB.
- `quelle-westermann-elemente-der-mathematik-bb-2016u2025-inhalt.txt` – Inhaltsverzeichnisse Elemente der Mathematik SI, Ausgabe 2016 (Kl. 7–10) und Ausgabe 2025 (Kl. 5–7, soweit erschienen), aus der DNB.
- `quelle-westermann-sekundo-bb-2017-inhalt.txt` – Inhaltsverzeichnisse Sekundo, Klasse 7–10, aus der DNB (Gegenprobe zu den Stoffverteilungsplänen).
- `quelle-klett-schnittpunkt-mathematik-diff2017-inhalt.txt` – Inhaltsverzeichnisse Schnittpunkt Mathematik, Differenzierende Ausgabe ab 2017, Klasse 7–10, aus der DNB.
- `lehrwerke-inhalt-bericht-2026-09.md` – Bericht des Auftrags Inhaltsverzeichnisse (24.09.2026).
- `quelle-cornelsen-fundamente-sek2-ausgabeb-inhalt.txt` – Inhaltsverzeichnis der Einführungsphase, Fundamente der Mathematik Ausgabe B (Berlin/Brandenburg/Mecklenburg-Vorpommern); Qualifikationsphase noch nicht gefunden.
- `quelle-westermann-elemente-der-mathematik-sek2-nrw-inhalt.txt` – Elemente der Mathematik SII, keine BE/BB-Ausgabe gefunden, Gegenprobe Ausgabe Nordrhein-Westfalen.
- `quelle-westermann-mathematikneuewege-sek2-berlin2011-inhalt.txt` – Mathematik Neue Wege SII, Ausgabe 2011 für Berlin (mit Rheinland-Pfalz, Saarland, Schleswig-Holstein).
- `foerderhefte-fundliste.md` – Fundliste der Förderhefte (Auftrag Lehrwerke Sek II und Förderhefte, 24.09.2026), drei Sorten (Regelreihen, eigenständige Grundwissenreihen, Förderschwerpunkt Lernen).
- `quelle-westermann-sekundo-foerder-be_bb2017-inhalt.txt` – Sekundo-Förderhefte zur Ausgabe 2017 für Berlin und Brandenburg, Klasse 5, 7, 9.
- `quelle-klett-schnittpunkt-foerder-diff2017-inhalt.txt` – Schnittpunkt-Mathematik-Förderhefte zur Differenzierenden Ausgabe ab 2017, Klasse 7 und 9.
- `quelle-westermann-mathematik2023-foerder-bebbstth-inhalt.txt` – Förderhefte zur Ausgabe 2023 für Berlin/Brandenburg/Sachsen-Anhalt/Thüringen, Klasse 7–9.
- `quelle-kohlverlag-grundwissenmathematik-foerder-freiarbeit-inhalt.txt` – eigenständige Übungsheftreihe „Grundwissen Mathematik Freiarbeit“ (Kohl Verlag), Klasse 5–7, ohne Schulbuchbindung.
- `quelle-cornelsen-klick-foerder-ab2024-inhalt.txt` – Klick! – Mathematik, Ausgabe ab 2024, für den Förderschwerpunkt Lernen, Klasse 5–7.
- `foerderhefte-formen.md` – Formenliste der Förderhefte: Teil C (24.09.2026) fand keine downloadbare Probe, nur Betrachter; der Nachauftrag (24.09.2026) hat die Betrachter angesehen und die Formenliste gefüllt (Cornelsen Klick! Kl. 5–7, Kohl Verlag Kl. 5 und 8).
- `lehrwerke-stand-2026-09-24.md` – Standdatei des Auftrags Lehrwerke Sek II und Förderhefte, nach Abschluss als Beleg liegen geblieben.
- `lehrwerke-sek2-foerder-bericht-2026-09.md` – Bericht des Auftrags Lehrwerke Sek II und Förderhefte (24.09.2026).
- `quelle-cornelsen-bigalkekoehler-sek2-bebb-inhalt.txt` – Inhaltsverzeichnisse Bigalke/Köhler Mathematik, Ausgabe Brandenburg 2019 (Qualifikationsphase GK/LK, Abiturvorbereitung); keine Berlin-Ausgabe gefunden.
- `quelle-westermann-mathematikheute-diagnoseundfoerdern-inhalt.txt` – Förderheft „Diagnose und Fördern“ zur Regelreihe Mathematik heute, Klasse 7–10.
- `quelle-cornelsen-klick-foerder-vorgaenger-inhalt.txt` – Klick! – Mathematik, Vorgängerausgabe 2008–2018, nur Klasse 10 mit Inhaltsverzeichnis auffindbar.
- `lehrwerke-stand-2026-09-24b.md` – Standdatei des Nachauftrags Lehrwerke (Formenliste, Bigalke/Köhler, Sorte 1 und 3, 24.09.2026).
- `lehrwerke-nach-bericht-2026-09.md` – Bericht des Nachauftrags Lehrwerke (24.09.2026).
- `foerderformen-fundliste.md` – Fundliste des Auftrags Förderformen (24.09.2026): freie Quellen für Klasse 7–10 und Sek II (DZLM, Stark, Persen, Auer, Grundwissen Bayern, Brückenkurse, Händlervorschauen, Rechenschwäche), Formenzeile je Titel.
- `quelle-dzlm-mathe-sicher-koennen-inhalt.txt` – DZLM „Mathe sicher können“, Diagnose-/Förderbausteine Natürliche Zahlen/Brüche-Prozente-Dezimalzahlen/Sachrechnen, CC BY-NC-SA 4.0.
- `quelle-dzlm-difsek-stellenwert-steckbrief.txt` – DZLM-Fortbildungssteckbrief Stellenwertverständnis Sek I, CC BY-SA 4.0.
- `quelle-freiburg-vorkurs-mathematik-inhalt.txt` – Vorkurs-Skript Universität Freiburg, CC BY-SA 4.0, einziges frei lizenziertes von fünf geprüften Brückenkurs-Skripten.
- `quelle-lisum-diagnose-foerderung-zahlen-operationen.txt` – LISUM-Diagnose-/Fördermaterial Leitidee Zahlen und Operationen, CC BY-SA 4.0; löst die Fundlücke [MzDuF] in `quellen.md`.
- `foerderformen-stand-2026-09-24.md` – Standdatei des Auftrags Förderformen, nach Abschluss als Beleg liegen geblieben.
- `foerderformen-bericht-2026-09.md` – Bericht des Auftrags Förderformen (24.09.2026).
- `quelle-westermann-mathematik2022-bebbstth-kl5-6-inhalt.txt` – Inhaltsverzeichnisse Mathematik, Ausgabe 2022 für BE/BB/Sachsen-Anhalt/Thüringen, Klasse 5–6 (Vorstufe zur Ausgabe 2023), aus der DNB; öffnen für die Klassenlage eines Stoffs vor Klasse 7 an der Oberschulreihe.
- `quelle-klett-schnittpunkt-mathematik-diff2017-kl5-6-inhalt.txt` – Inhaltsverzeichnisse Schnittpunkt Mathematik, Differenzierende Ausgabe ab 2017, Klasse 5–6, aus der DNB.
- `quelle-westermann-mathematikheute-bebb-kl5-6-inhalt.txt` – Inhaltsverzeichnisse Mathematik heute, Ausgabe 2014 für Grundschulen in Berlin und Brandenburg, Klasse 5–6 (Klasse 5 über den Lösungsband), aus der DNB.
- `quelle-cornelsen-fundamente-bb-ausgabeb2024-kl5-6-inhalt.txt` – Inhaltsverzeichnisse Fundamente der Mathematik, Ausgabe B ab 2024, Klasse 5–6 (grundständiges Gymnasium), aus der DNB.
- `quelle-buchner-mathedelta-bb-2016-inhalt.txt` – Inhaltsverzeichnisse mathe.delta Berlin/Brandenburg (Gymnasium), Klasse 7–10, aus der DNB; Klasse 8 ab Kapitel 5 aus dem Stoffverteilungsplan des Verlags.
- `quelle-cosh-mindestanforderungskatalog-v3.1.pdf`, `quelle-cosh-mindestanforderungskatalog-v3.1.txt` – cosh-Mindestanforderungskatalog Mathematik Schule–Hochschule, Version 3.1 (2025), CC BY-SA 4.0, PDF und Textfassung (seit 27.09.2026); öffnen, wenn der Mindeststoff eines fhr-Eintrags (Entscheidung 36) gegen den Katalog gehalten wird.
- `fremdsammlungen-fundliste.md` – Fundliste freier amtlicher Aufgabensammlungen anderer Länder (Auftrag Nacht 2026-09-25, Teil 3): Bayern (Jahrgangsstufentests Gymnasium 8/10, Realschule 6/8, Realschulabschluss Mathematik I/II, je 2021–2025) und IQB VERA-8 (2022–2026) mit Adresse, Vermerk, Umfang und Lösungen, dazu die nicht frei erreichbaren (Quali Mittelschule, Kompetenztests Sachsen); die PDFs und Textfassungen liegen lokal unter `hefte/fremd/`. Öffnen, wenn für eine Prüfungshöhe ohne P10-Original eine fremde Originalaufgabe gesucht wird.

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
- `gym-vergleich.py` – vergleicht Typenverwendung (getrennt Haupt und Haupt+Neben) und Themenverwendung (Haupttyp) zwischen `msa-katalog-gym.csv` und den Papieren OS/EBR/FOR und schreibt `msa/gym-vergleich.md` (je drei Zahlen/Listen: nur GYM, nur OS/EBR/FOR, in beiden); nach jeder Änderung an `msa-katalog-gym.csv` oder den OS/EBR/FOR-Katalogen ausführen. Option `--gruppen` (seit 24.09.2026) vergleicht stattdessen Gruppe A (papier EBR) gegen Gruppe B (papier FOR und OS) innerhalb von `msa-katalog-basis.csv`/`msa-katalog-kontext.csv` und schreibt `msa/ebr-vergleich.md`.
- `typen-abgleich.py` – Abgleichlauf nach Kern § 9: benennt Typen um oder zieht sie zu einem vorhandenen Typ zusammen, in `msa-typen.csv` und allen Katalogen eines Profils zugleich (Eingabe eine Liste alt;neu;thema_neu;art, z. B. `msa/gym-abgleich.csv`); Optionen `--thema ALT NEU` (Themenumbenennung, zieht `themen.csv` mit) und `--status-neu-gueltig`; idempotent, prüft vor dem Schreiben.
- `dnb-sru.py` – Suche in der Deutschen Nationalbibliothek über die SRU-Schnittstelle (CQL-Abfrage als Argument), listet Treffer mit IDN, Jahr, ISBN, Titel und ob ein Inhaltsverzeichnis-PDF verlinkt ist (`https://d-nb.info/<IDN>/04`); Grundlage der Lehrwerk-Inhaltsverzeichnisse in `quellen/`.
- `klassen-belege.py` – baut `katalog/_klassen-belege.md` aus den 29 Sek-I-Einträgen, den Verzeichnisdateien unter `quellen/` und den Zuordnungsdaten, prüft jedes Zitat an der Quelldatei und jeden Typnamen am Eintrag (die Klassenklammer „[OS …]“ von `marken-bau.py` wird dabei abgestreift) und schreibt nichts bei einem Fehler; `--probe` vergleicht nur mit der vorhandenen Datei; nach einer Änderung an den Einträgen, an einer Verzeichnisdatei oder an den Daten ausführen.
- `klassen-belege-daten.py` – die Zuordnungsdaten dazu, je Reihe und für die Förderhefte ein Abschnitt (Lerneinheit, Verzeichniszeile, Seite, Zeilenhinweis, Typ, Marke, Ermessen); hier wird eine Zuordnung ergänzt oder berichtigt, nie in der Ausgabedatei.
- `klassen-belege-typen.txt` – Typenliste zum Nachschlagen der Typnamen beim Zuordnen (je Einheit die Zeile aus „Typen je Lerneinheit“ mit Zeilennummer); abgeleitet von `klassen-belege.py`, nie von Hand ändern.
- `pruefungswort-belege.py` – baut `katalog/_pruefungswort-belege.md` aus den Einträgen, `themen.csv`, den msa-, abi- und fhr-Katalogen und den Zuordnungsdaten und schreibt die Typenliste `pruefungswort-belege-typen.txt`; prüft jede Zuordnung (Nummer, Wortlaut, Typname, Grund) und schreibt nichts bei einem Fehler; die Typnamen liest es ohne die Klassenklammer „[OS …]“ von `marken-bau.py` (`typen_des_eintrags`, auch für `blatt-pruef.py`); `--typen` nur die Typenliste, `--probe` nur vergleichen; Sek II ordnet es die Katalogtypen wortgleich (auch mit Gegenstandsklasse) den Prüfungstypen zu; nach einer Änderung an den Einträgen, den Prüfungskatalogen oder den Daten ausführen.
- `pruefungswort-belege-daten.py` – die Zuordnungsdaten dazu: je Sek-I-Eintrag U (P10-Typen der Einheit laut Zuordnungszeile), T (P10-Typen je Katalogtyp mit Grund) und V (Verfahrensgeber laut Zuordnungszeile); hier wird eine Zuordnung ergänzt oder berichtigt, nie in der Ausgabedatei.
- `pruefungswort-belege-typen.txt` – Typenliste zum Zuordnen (je Eintrag und Einheit die Typen mit Nummer, Sek II mit Marke wortgleich/didaktisch); abgeleitet von `pruefungswort-belege.py`, nie von Hand ändern.
- `sek2-ordnung-belege.py` – baut `katalog/_sek2-ordnung-belege.md`: übernimmt die Planstellen je Einheit aus `katalog/_kursart-belege.md`, liest Kurshalbjahr (Berlin: Spalte „Khj“, Brandenburg: Abschnitt Q1–Q4) und Block am Plantext nach, sucht die FOS-Zitate der Lerneinheitszeilen im FOS-Plan (spaltengenau) und prüft jede Lehrwerkszeile der Daten an der Verzeichnisdatei; schreibt nichts bei einem Fehler; `--probe` vergleicht nur; nach einer Änderung an den Sek-II-Einträgen, an `_kursart-belege.md`, an einer Verzeichnisdatei oder an den Daten ausführen.
- `sek2-ordnung-belege-daten.py` – die Zuordnungsdaten dazu (L = Lehrwerkszeile je Einheit, K = keine Stelle mit Grund, R = zusätzliche Planstelle mit Zitat, E = Ermessen); hier wird eine Zuordnung ergänzt oder berichtigt, nie in der Ausgabedatei.
- `klassen-ermessen.py` – liest die Ermessenslisten aus `katalog/_klassen-belege.md`, holt je Fall das Zitat von der Einzelstelle und ordnet ihn nach der ersten zutreffenden Wortlautregel einer Sorte zu; schreibt `katalog/_klassen-ermessen.md` mit Gegenprobe gegen den Zahlenblock; `--probe` vergleicht nur; nach jedem Neubau von `_klassen-belege.md` ausführen.
- `blatt-pruef.py` – misst je Blatt unter `blaetter/` (jede PDF-Datei mit der gleichnamigen tex-Datei unter `src/`, pdfinfo und pdftotext aus MiKTeX) die Kennzahlen 1–9 des Auftrags Nacht 2026-09-26 und schreibt `blaetter/kennzahlen.md`; Lesarten (Titel, Darstellungskategorien nach den Makros von `mathblatt.sty`, Antwortform, Fachwörter, Wortstamm im Sprossenabgleich) im Skriptkopf; mit Pfad nur ein Blatt auf die Konsole, ohne zu schreiben; nach jedem neuen Blatt (nach `einsortieren.py`) ausführen. Seit v0.2 (Testlauf 25.09.2026): `--ausgabe <datei>` schreibt woandershin, `--testlauf <ordner>` misst die Gesamt- und Fokus-PDFs eines Testlaufordners (flache Ordner, Katalog aus `protokoll.txt`). Seit v0.3 (27.09.2026): Bausteine der Vorlage Stufe 5 – `\swfrage` als Teilaufgabe, Kennzahlen 10–12 (Zweigzeilen je Einheitenkopf, Abhakseite, Verzeichniszeile) und die Zuordnung Einheitenkopf → Lerneinheit über den Titel, nur für Blätter mit diesen Bausteinen; ältere Blätter messen sich byteidentisch wie in v0.2. Seit v0.4 (28.09.2026): `\swz` und `\swa` zählen als Teilaufgaben, Teilaufgaben im Beispielblock nicht; Kennzahlen 13–17 für die Bausteine der Vorlage Stufe 6 (`\verfahren`, `\anweisung`, `\rechenplatz`, Umgebung `beispiel`, `\streifenleer[0]`), je Blatt und als Tabelle, nur für Blätter mit diesen Bausteinen.
- `testlauf-eingaben.csv` – die Eingaben des Testlaufs (nr;kurzname;eingabe;antworten;prueft); bleibt für jeden Testlauf gleich, damit die Kennzahlen vergleichbar sind.
- `testlauf-auftrag.md` – Vorlage des Auftrags Testlauf des Unterrichtsblatt-Prompts (seit 27.09.2026; aus `archiv/auftrag-testlauf-2026-09-25.md` mit drei Änderungen: Blätter nacheinander, Regelweg `claude -p` vor dem Ersatzweg, Uhrzeiten nur aus `Get-Date`, Ordner- und Berichtsname mit dem Datum des Laufs); für einen Lauf in die Wurzel als `auftrag-testlauf.md` kopieren und das Datum eintragen.
- `testlauf-umgebung.md` – Vorlage der Nachricht an eine Blattsitzung im Ersatzweg (Prompt, Umgebung Windows/PowerShell, Eingabe); Platzhalter setzt die Auftragssitzung.
- `testlauf-ablage.py` – legt das Ergebnis einer Blattsitzung im Testlaufordner ab (PDFs, entpacktes Protokoll-Archiv), prüft Gesamt/Fokus-PDF und Prompt-Zeile und zählt die Werkzeugaufrufe laut `protokoll.txt`.
- `testlauf-messen.py` – schreibt `blaetter/testlauf-<datum>/kennzahlen.md`: `blatt-pruef.py --testlauf` plus Zusatzzählung aus der Textextraktion (Einheitenköpfe, Zweigzeilen, Ich-Titel, Abhakseite, „Blatt 0“) und die Gegenproben des Auftrags; `--probe` nur auf die Konsole.
- `testlauf-lesezettel.py` – schreibt `blaetter/testlauf-<datum>/lesezettel.md` (je Eingabe Deutungszeile, Plan und Ausgabeblock wortgleich aus `chat.txt`, PDFs, Hinweise aus der Spalte „prueft“ und Messungen).
- `marken-bau.py` – schreibt in jeden Katalogeintrag unter jede Nummernzeile die Zeile „Marken:“ (Sek I: „OS Kl. n“ bzw. Spanne mit Reihenliste, „GYM Kl. n“, Prüfungswort, seit 27.09.2026 „FHR“ bei Sek-I-Einheiten mit Sek-II-Zeilen und mindestens einem FHR-Jahrgang, „nicht für alle: <Reihe> <Klasse> <Marke>“; Sek II: „BE Q…“, „BB Q…“, Kursart, „Abitur GK“, „Abitur LK“, „FHR“), setzt hinter Typen mit eigener Verzeichnisstelle die Klasse in eckigen Klammern und entfernt am Ende einer Nummernzeile die reine Klassenklammer „(Kl. n)“; liest `katalog/_klassen-belege.md`, `_pruefungswort-belege.md`, `_sek2-ordnung-belege.md`, `_marken-entscheidungen.md` und `marken-bau-stellen.txt`; wiederholbar (ersetzt vorhandene Marken-Zeilen und Klammern), schreibt nichts bei einem Fehler, `--probe` baut und vergleicht nur; Gegenprobe des Auftrags im Skript (Abweichung wird gemeldet; seit 28.09.2026 lineare-funktionen 4 und quadratische-gleichungen 2 auf den Belegwerten, Quelle im Skriptkopf); nach jedem Neubau einer der drei Belegdateien oder einer Änderung an der Stellenliste ausführen.
- `marken-bau-stellen.txt` – die Stellenliste dazu: je Stelle aus `_klassen-belege.md` die Lesart (gilt, ohne Klasse, gilt für eine andere Einheit, Typzeile an einem Typ) mit Quelle (Datei 2 oder im Lauf entschieden) und Grund; hier wird eine Lesart ergänzt oder berichtigt, nie in den Einträgen.
- `cas-vergleich.py` – hält die CAS-Fassung eines Landeshefts je Teilaufgabe gegen die WTR-Fassung (pdftotext aus MiKTeX, Hefte unter `hefte/abi/`, Normierung wie beim Pool-Abgleich) und gibt Zuordnung, Urteil, BE und Diff auf die Konsole; mit einem dritten Heft (z. B. `2017-bb-ea-cas`) auch dagegen; Messwerkzeug zu `abitur/befund-cas-berlin-2026-09-28.md`, schreibt nichts.

## archiv/ – eingefroren

Datierte Befunde und Werkstattzettel. Beschreiben den Stand ihres Datums, werden nicht
fortgeschrieben, kein Chat muss sie lesen. `namensschema.md` liegt hier, weil der Umbau
auf Ordner es überholt hat. `auftrag-testlauf-2026-09-25.md` ist der Auftrag des ersten Testlaufs
des Unterrichtsblatt-Prompts; für einen neuen Lauf gilt seit 27.09.2026 die Vorlage
`werkzeuge/testlauf-auftrag.md` (Posten in `faellig.md` § 2). Abgelöste Übergaben liegen als
`uebergabe-<Kopfzeilendatum>.md`; zuletzt abgelegt `uebergabe-2026-09-25-abends.md` (abgelöst
durch die Übergabe vom 26.09.2026; das Kopfzeilendatum folgt nicht der Ablagefolge).

## Nicht im Repo (lokal, `.gitignore`)

`hefte/` gescannte Prüfungshefte (urheberrechtlich geschützt), `hefte-md/` Markdown-Korpus
der Verlagsbände, `korpus/` maschineller Korpus, `baende/` Sammelbände; der Cache der Pool-PDFs von `abitur/iqb-quellen.py` liegt unter `hefte/iqb/`.
`hefte/fremd/` freie Tests und Prüfungen anderer Länder als PDF mit Textfassung (Verzeichnis:
`quellen/fremdsammlungen-fundliste.md`).

## Repo blattbau – anderes Projekt

`unterrichtsblatt.md`, `pruefungsblatt.md`, `mathblatt.sty`, `Anleitung_mathblatt.md`,
`CHANGELOG.md` und die Testauswertungen liegen seit dem Umbau im eigenen Repo. Der
Prüfungsblatt-Prompt lädt die Kataloge per Abruf aus diesem Repo; nach dem Umbau müssen die
Pfade dort auf die Profilordner zeigen (`msa/msa-typen.csv` statt `msa-typen.csv`).
