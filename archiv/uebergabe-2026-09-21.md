# Übergabe 2026-09-21

## 1 Ziel

Der Themenkatalog in hz-0801/mathe-nachhilfe beschreibt den Stoff so,
dass daraus Unterrichts- und Prüfungsblätter gebaut werden können. Der
Katalog ist vollständig; der nächste Zweck ist der Umbau der beiden
Prompte in hz-0801/blattbau auf den Katalog und der erste Testlauf
eines Blatts aus einem Eintrag.

## 2 Arbeitsgrundlage

- hz-0801/mathe-nachhilfe, Commit dff0d07 (21.09.2026, gepusht).
  Maßgeblich: konzept.md § 4 (Entscheidungen 1–37), README.md als
  Landkarte, faellig.md § 2 für die offenen Handlungen.
- katalog/ – 73 Einträge, Status durchgehend Entwurf, gegengelesen:
  nein. Prüfskripte katalog/_pruef_struktur.py (Kennzahlen 1–7),
  katalog/_pruef_katalog.py <datei>, werkzeuge/themen-pruef.py,
  werkzeuge/tragfaehigkeit.py → katalog/_tragfaehigkeit.md.
- hz-0801/blattbau, Commit 4be34e2 (21.09.2026, gepusht).
  unterrichtsblatt.md v3.35 (326 Z.), pruefungsblatt.md v0.15 (271 Z.),
  mathblatt.sty (1570 Z., TikZ-Makros u. a. \baumzwei, \baumdrei,
  Vierfeldertafel, Kreisdiagramm), Anleitung_mathblatt.md,
  Testauswertung_Masterprompt_Mathe_2026-09-08.md (Testverfahren),
  Bewertung_Masterprompt_v3-34.md, referenz/ (leer, für Referenzblätter).
  Inhaltlich unverändert seit 17.09.2026.
- Der Stand der Prompte vor dem Umbau ist gesichert unter dem Tag
  v3.35-vor-katalogumbau (= 8d15f63, auf GitHub, geprüft byteidentisch):
  https://raw.githubusercontent.com/hz-0801/blattbau/v3.35-vor-katalogumbau/unterrichtsblatt.md
  https://raw.githubusercontent.com/hz-0801/blattbau/v3.35-vor-katalogumbau/pruefungsblatt.md
- hz-0801/anweisungen: global.md, kandidaten.md (Delegationsform),
  projekt-verbessereBlaetter.md ist die Projektanweisung dieses
  Projekts. Das Repo liegt beim Lehrer unter OneDrive, nicht neben den
  beiden anderen.
- Claude Code im Code-Tab, Aufträge als Textblock nach der
  Delegationsform (/clear-Regel, Modell in der Holger-Zeile).
  Katalog- und Prompttexte: Opus; reine Mechanik: Sonnet. Die Ordner
  mathe-nachhilfe, blattbau und anweisungen sind alle verfügbar.

## 3 Arbeitsstand

Abgeschlossen und gepusht: Entscheidung 37 vollständig. Der
Sek-II-Trägereintrag zufallsexperimente-und-pfadregeln.md (237 Zeilen,
acht Einheiten), kombinatorik.md (32 Zeilen, drei Einheiten, Vollform),
die Erweiterung von daten.md (neue Einheit 6),
lineare-gleichungssysteme.md (neue Einheit 5) und einheiten.md (keine
neue Einheit); alle Verweise der Stochastik-Einträge auf die richtige
Stufe gerichtet; themen.csv, index.md, README.md, faellig.md
nachgezogen; themen-pruef.py auf v0.2 (Prüfung 4 kannte E37 nicht).
Kennzahl 5 von 345 auf 23.

Neu gebaut: werkzeuge/tragfaehigkeit.py und katalog/_tragfaehigkeit.md
(Tabelle A: wie oft ein Thema von anderen unter „Voraussetzungen
(Blatt 0)" gebraucht wird; Tabelle B: eigene Voraussetzungen;
Messlücken). Kennzahl 7 in _pruef_struktur.py misst die Messlücke:
„Einträge ohne Verweis in Blatt 0: 22 von 73".

In blattbau: Tag gesetzt und gepusht, README um „Stand vor dem
Katalogumbau" und „Bekannte Abweichungen" ergänzt, referenz/ angelegt.
Kein Zeichen an den Prompten geändert.

In anweisungen (Commit 4e0f498, Push ausstehend): global.md um die
Regel „Ablage der Übergabe" ergänzt, projekt-verbessereBlaetter.md um
die Zeile „Standdatei: uebergabe.md in der Wurzel von
hz-0801/mathe-nachhilfe". Die Arbeitskopien in den Claude-Einstellungen
sind noch nicht nachgezogen.

Nicht begonnen: der Promptumbau selbst.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Entscheidungen 1–37: konzept.md § 4; nicht neu aufrollen.
  E37 (21.09.2026): Sek-II-Zeilen an Sek-I-Themen werden getrennt,
  wenn die Oberstufe eigene Kompetenzen prüft, sonst wird der Eintrag
  erweitert; die Zeilenzahl ist Indiz, kein Maß; kein Stufensuffix in
  Dateinamen.
- Der Themenkatalog baut keine Blätter. Was Blattform ist, wird in
  blattbau entschieden.
- Schutz der Prompte beim Umbau (beschlossen 21.09.2026): abschnitts-
  weise ändern mit einem Commit je Abschnitt; Abschnitte 3–6 (Inhalt,
  Layout, Prüfung vor Übergabe, Ausgabe) bleiben unangetastet, sie
  sind erprobt; der Umbau betrifft 0–2 (Rolle/Blatttypen, Eingabe
  deuten, Blätter und Katalog-Abruf); neue Version heißt v4.0 und
  nennt den Vorgänger in der Versionszeile.
- Referenzblätter: Der Lehrer hat bestehende Blätter mit protokoll.txt
  und legt zwei davon (ein Unterrichtsblatt, ein Prüfungsheft) nach
  blattbau/referenz/. Sie sind der Vergleichsmaßstab nach jedem
  Umbauschritt. Prüfraster ist das vorhandene Testverfahren
  (Testauswertung_Masterprompt_Mathe_2026-09-08.md), Vergleichseingabe
  für den Prüfungsprompt ist „prozent" ohne Zusatz.
- Git: Claude Code committet, pusht nicht. Der Lehrer pusht über
  GitHub Desktop; Tags gehen dort nicht mit und brauchen die Konsole:
  "%LOCALAPPDATA%\GitHubDesktop\app-3.6.5\resources\app\git\cmd\git.exe"
  push origin <tag>. Der Git Credential Manager ist autorisiert.

## 5 Offene Punkte und verworfene Ansätze

Befunde für den Promptumbau (am 21.09.2026 an den Prompten erhoben):
- Die Arbeitsteilung der beiden Prompte ist überholt.
  unterrichtsblatt.md definiert sich als Werkzeug „für alle Themen ohne
  Prüfungskatalog", pruefungsblatt.md für Themen mit Katalog. Seit alle
  Themen einen Eintrag haben, hat der Unterrichtsblatt-Prompt keinen
  Bereich mehr. Die Grenze muss nach Zweck neu gezogen werden
  (laufender Unterricht gegen Prüfungsvorbereitung). Erste Entscheidung
  des Umbaus.
- Die Prompte holen den Katalog nicht. pruefungsblatt.md zieht per
  curl msa-typen.csv, msa-katalog-basis.csv, msa-katalog-kontext.csv
  (existieren alle); unterrichtsblatt.md holt nur mathblatt.sty. Kein
  Prompt kennt Merkkästen, Sprossen, Auswendig-Zeilen, Voraussetzungen.
- Die Kopfzeilen beider Prompte nennen als Masterfassung noch
  hz-0801/mathe-nachhilfe statt blattbau (im blattbau-README unter
  „Bekannte Abweichungen" vermerkt).
- Ungeprüft: ob mathblatt.sty in Claude Code durchkompiliert. Einzige
  technische Vorbedingung für den Testlauf.
- referenz/ fehlt in der Dateiliste des blattbau-README-Kopfs.

Diskussionsgrundlage für den Umbau, nichts davon entschieden (Stand
19.09., ergänzt 21.09.; Kurzposten in faellig.md § 2): Blatt 0 als
Hinführung zum Stundenthema; Bauprinzip Überspringbarkeit; Kurzkästen
der Herkunftsthemen und Kurzergebnisse am Blattende; Scheiternsregel
(Herkunftsthema wird Stundenthema); Kurztest als fester
Schlussabschnitt (10 Minuten, 3 Aufgaben, Etikett je Aufgabe,
Ankreuzfußzeile, Befund per Foto); Stundenanker als Kompositionsregel;
Zuruf-Deutung über die Konkordanz; Betriebsmodell eigenes Projekt
„Unterricht", ein Chat je Schüler, Pseudonyme.
Dazu neu vom 21.09.:
- Geltungszeile im Kasten: statt einer Rubrik „Definitionen und Sätze"
  eine Zeile „gilt nur, wenn …" je Kasten – die Voraussetzung zählt,
  nicht der Satzname (Beleg: 1073 von 2883 Katalogzeilen verlangen
  Begründen oder Nachweisen, aber „Strahlensatz" steht in 4 Zeilen,
  „Thales" in 5, „Bayes" in 2). Auf dem Prüfungsblatt darf die Zeile
  nicht mitgeliefert werden, weil sie die verlangte Leistung vorwegnimmt.
  Achtung: Das ist der am 19.09. verworfene Ansatz „typischer Fehler →
  verletzte Voraussetzung" an anderer Stelle; als Revision vorgelegt,
  nicht entschieden.
- Tragfähigkeit als zweite Achse neben der Prüfungslast: Stunden-
  reihenfolge bei knapper Zeit nach dem Trägerwerkzeug, nicht nach
  Prüfungshäufigkeit. Belastbar ist die Frage, welche Sek-I-Themen die
  Oberstufe braucht: lineare-gleichungen 16 Nachfrager, gleichungen-
  loesen 15, potenzen-wurzeln 15, prozentrechnung 15, lineare-
  funktionen 14, quadratische-gleichungen 14 (bei 2 eigenen Zeilen),
  strahlensaetze 9 (bei 0 eigenen Zeilen). Die Rangliste bildet
  derzeit die Sek-II-Perspektive ab, weil 22 Sek-I-Einträge ihre
  Voraussetzungen in Wortform statt als Dateiverweis nennen.
- Baumdiagramm als dauerhaft mitlaufender Kurzkasten in der Stochastik,
  in der Form des Dreischritts (Ereignis formulieren, im Baum zerlegen,
  Pfade bestimmen; [FD-BAUM] in katalog/_quellen.md).

Werkstatt, mit Posten in faellig.md § 2: gebündelte Geltungsrecherche
zu Matrizen, Konfidenzintervallen und Abitur 2030 (offen seit dem
Serienende, liegt beim Chat, nicht bei Claude Code); Quellenausbau
Erwartungshorizonte; Vorrat-Verweise auf nicht existierende gost-*.md
und fos-*.md in sieben Sek-I-Einträgen. Ohne Posten: [FS]-Abgleich am
PDF der Formelsammlung, COSH-Beschaffung, MaCo-Lizenz; funktionen-
allgemein ohne Katalogdatei; 3 fhr-Zeilen in terme und prozentrechnung
ohne Typ (unter jeder Schwelle, Sammelauftrag abwarten).

Regelwerk: In global.md steht seit 4e0f498 „bestehende Datei
überschreiben", in projekt-verbessereBlaetter.md dagegen, die alte
Übergabe wandere nach archiv/. Der Widerspruch ist bekannt und nicht
bereinigt; maßgeblich ist die Projektanweisung. Zu ändern, wenn
ohnehin jemand an global.md arbeitet. Regeländerungen künftig sammeln
statt einzeln durchs Verfahren schicken – jede kostet sonst Auftrag,
Push und Kopierschritt.

Entschieden nicht zu tun, bis der Blattbau es verlangt: die 22 Sek-I-
Einträge auf Dateiverweise umstellen (Gewinn wäre eine vollständigere
Rangliste, kein besseres Blatt).

Verworfen: Formerweiterung „typischer Fehler → verletzte Voraussetzung"
(19.09., kommt als Geltungszeile zurück, s. o.); Zurufparameter
„reduziert"/„Spickzeile"; Stundenanker als Katalogobjekt; Bartz'
Baumtypen als Gliederungsraster für Katalogeinträge (gliedert einen
ganzen Kurs, sieben seiner neun Kapitel liegen in anderen Einträgen);
eine Archivkopie der Prompte im Repo (Git bewahrt sie ohnehin, eine
zweite Datei schafft zwei Wahrheiten – stattdessen das Tag).

Kennzahl 5 ist als Serienzähler verbraucht: Die 23 Reste sind gewollte
Straffungsreste (18 in kurvenuntersuchung, deren Typen im Eintrag
stehen, nur ohne id-Nennung) plus 5 Einzelzeilen; sie sinkt nie auf
null.

## 6 Nächster Arbeitsschritt

Promptumbau, ab 18 Uhr mit Fable, in dieser Reihenfolge:

1. Zwei Referenzblätter nach blattbau/referenz/ legen (Lehrer), damit
   der Vergleichsmaßstab vor dem ersten Umbauschritt steht.
2. Feldabgleich als Papierarbeit: Welches Feld eines Katalogeintrags
   braucht das Unterrichtsblatt, welches das Prüfungsblatt, welches
   keiner? Ein Feld, das kein Blatt liest, war in Entscheidung 36 zu
   großzügig.
3. Die Zuständigkeitsgrenze der beiden Prompte neu ziehen (§ 5, erster
   Befund), dann Abschnitte 0–2 abschnittsweise umbauen, ein Commit je
   Abschnitt, gegen die Referenzblätter prüfen.
4. Danach der Testlauf: ein Unterrichtsblatt aus einem fertigen
   Sek-II-Eintrag bauen und am Ergebnis prüfen, ob der Eintrag trägt.
   Erster Belastungstest des Katalogs.
