# Übergabe 2026-09-21b

## 1 Ziel

Der Prüfungsblatt-Prompt soll über msa hinaus auf fhr und abi
erweitert werden; zugleich sollen die Katalogdaten auch den
Unterrichtsblatt-Prompt speisen, statt nur Prüfungsblätter zu
tragen. Dafür wurden zuerst die Prüfungskataloge, dann der
Themenkatalog fertiggestellt. Jetzt folgt der Umbau der beiden
Prompte im Repo blattbau.

## 2 Arbeitsgrundlage

- GitHub hz-0801/mathe-nachhilfe, Commit a1a7d07 (21.09.2026).
- befund-inkonsistenzen-2026-09-21.md – die sieben Befunde, die
  vor dem Umbau zu besprechen sind. Zentraler Text dieses Chats.
- blatt-konzept.md v0.8 (12.09.2026) – trägt den Satz „Für die
  Heft-Phase gilt bei Widerspruch diese Datei", ist aber in Teilen
  überholt (Befund § 2, 3, 5, 6, 7, 8).
- konzept.md § 4 – Entscheidungen 1–37, maßgeblich für den Katalog.
- katalog/ – 73 Einträge, Status Entwurf, gegengelesen: nein.
- katalog/_tragfaehigkeit.md (Kennzahl 7), katalog/_verweise.md
  (Kennzahl 8), katalog/_blatt0-belege.md (Kennzahl 9) – abgeleitet,
  nie von Hand ändern.
- befund-geltung-2026-09-21.md – Geltung der beiden Vorratsthemen,
  Lage der Vorgaben, P10-Strukturänderung ab 2026.
- themen.csv; faellig.md § 2 und § 3.
- hz-0801/blattbau, Commit 0e1ec2d: unterrichtsblatt.md v3.35,
  pruefungsblatt.md v0.15, mathblatt.sty, Anleitung, zwei
  Testauswertungen. Gegenstand des Umbaus, bisher unangetastet.
- hz-0801/anweisungen: global.md und projekt-verbessereBlaetter.md,
  beide Stand 2026-09-21; kandidaten.md mit der Delegationsform.

## 3 Arbeitsstand

Fünf Läufe an einem Tag, alle gepusht: cfa4723 (112 Dateiverweise
in 21 Einträgen), 9722afb (Werkzeugpflege, beide Messwerkzeuge auf
v0.2), f6e5fc5 (50 Dateiverweise in acht weiteren Einträgen),
795ca0a (20 Zuordnungen, Geltungsbefund abgelegt, blatt0-belege.py
v0.2), a1a7d07 (Geltungsvermerke geschlossen).

Damit ist die Mechanik am Katalog erledigt. Kennzahl 9 fiel von 93
auf 24 von 463 Fertigkeitszeilen, Kennzahl 7 von 22 auf 0 von 73.
Alle Blatt-0-Voraussetzungen, die auf ein Katalogthema zeigen,
nennen es jetzt als Dateiverweis – ein Prompt kann Blatt 0
maschinell auflösen.

Nicht begonnen: der Umbau der blattbau-Prompte. Kein Blatt ist
bisher aus einem Katalogeintrag gebaut worden.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Entscheidungen 1–37: konzept.md § 4; nicht neu aufrollen.
- Die vier blattbau-Konzepte vom 19.09. (Blatt 0 als
  Standardbestandteil, Überspringbarkeit, Kurztest, Stundenanker
  samt Zuruf-Deutung) sind **nicht** entschieden, sondern
  Diskussionsstand. Die Übergabe 2026-09-20 führte sie
  fälschlich unter „Verbindliche Entscheidungen".
- Die Prompte funktionieren in ihrem bisherigen Zuschnitt. Der
  Umbau erweitert sie, er repariert sie nicht.
- Zuordnungen werden additiv geschrieben: der lesbare Titel bleibt,
  der Dateiname kommt in Klammern dazu („Thema Terme (terme.md),
  Einheit 2."). Die Angleichung an die knappere Sek-II-Form gehört
  in die Zielform-Diskussion.
- Eine Fertigkeit ohne Ziel wird nicht gebogen, bis eine passt.
  „Punkt vor Strich mit natürlichen Zahlen" auf bruchrechnung E5 zu
  legen wäre mehr Papier, aber nicht mehr Hilfe.
- Claude Code im Code-Tab, Aufträge als Textblock nach der
  Delegationsform, /clear als eigene Eingabe voraus. Die
  Modellangabe im Block ist Dokumentation, keine Umschaltung: das
  Modell setzt die Sitzung. Sie steht deshalb in der ersten Zeile
  des Blocks, nicht am Ende.

## 5 Offene Punkte und verworfene Ansätze

**Vor dem Umbau zu besprechen** – die sieben Befunde und die vier
Konzepte. Tragend ist Befund § 1: Der Themenkatalog hat bis heute
keinen Abnehmer, und blatt-konzept.md § 5 schließt aus, dass der
Unterrichtsblatt-Prompt einen Katalog liest.

**Dazu die Frage, die an diesem Tag entstand:** Blatt 0 soll nicht
nur Voraussetzungen prüfen, sondern Stoff in Erinnerung rufen, den
der Schüler seit Jahren nicht hatte, und zwar an den Stellen, die
nach langer Pause Probleme machen. Das Material dafür liegt
bereits im Katalog – jeder Eintrag hat Merkkästen je Lerneinheit
und einen Abschnitt „Typische Fehler". Zu klären ist dreierlei: ob
der Prompt sie über die Blatt-0-Verweise holt (Anker-
Kompositionsregel, Posten in faellig.md § 2); dass die Körnung
nicht passt (Kasten gehört zur Lerneinheit, Verweis zur
Fertigkeit); und dass „Typische Fehler" Prüfungsfehler sammelt,
nicht Vergessensfehler.

**24 Fertigkeitszeilen ohne Ziel** (Kennzahl 9), in drei Sorten:
20 zeigen unter den Katalog (Einmaleins und schriftliches Rechnen,
Teilbarkeit, Stellenwerte und Zahlenstrahl, Punkt vor Strich,
Zeichnen mit dem Geodreieck, Vierecksarten); 3 sind
Rechnerbedienung in Sek-II-Einträgen, ausdrücklich als
Werkzeugwissen gekennzeichnet; 1 ist der Grenzfall daten 37
(„Längen abtragen"). Fünf der 20 tragen bereits die selbst
erfundene Marke „Kein eigenes Thema", die die Messung nicht kennt.
Zu entscheiden: ob der Katalog einen Boden bekommt, in welcher
Form (eine schlanke Eintragsart wäre der Präzedenzfall
Verweiseintrag aus E36), und ob Werkzeugwissen eine eigene Marke
braucht. Quellen dafür wären RLP Teil C Niveaustufen C/D und die
MSK-Bausteine; für den Schnitt der Bodenthemen bräuchte es zwei
bis drei weitere Lehrwerks-Gliederungen für Klasse 5/6 zum
Übereinanderlegen – im Repo liegt nur der Klett-Fahrplan.

**Werkstatt, Posten in faellig.md § 2:** fhr-typen.csv führt das
Thema „Gleichungen lösen", themen.csv hat keine fhr-Zeile dazu
(wird dringend bei der fhr-Erweiterung); 27 Namensabweichungen
H1 gegen thema; 237 Verweise aus Katalogeinträgen in
Werkstattdateien; 270 Paare ohne Gegenrichtung (hängt daran, ob
Blatt 0 auch vorwärts aufgelöst wird); sechs RLP-Zitate nicht
wörtlich; MSK-Bausteinliste lückenhaft (Online-Check über das
Brandenburger Schulportal verfügbar); P10-Struktur ab 2026;
zwei neue Inhalte auf Niveaustufe G (Sinussatz, Lösbarkeit
quadratischer Gleichungen); index.md Zeile 232 veraltet – die
fehlende Zahl ist 316/308/8.

**Zwei Werkzeuge tragen fest eingebaute Zahlen**, die bei jeder
gewollten Änderung reißen: die Gegenprobe in blatt0-belege.py und
die Prosazeile index.md 232. Dieselbe Schwäche; die saubere Lösung
ist, auf die abgeleiteten Dateien zu verweisen statt Zahlen zu
wiederholen.

**Verworfen:** Quellenklammern maschinell gegen Register auflösen,
um fehlende Themenzuordnungen zu finden – die Klammern sagen, wo
eine Fertigkeit gebraucht wird, nicht wo sie gelehrt wird; 55 von
145 Bestandteilen ließen sich auflösen, keine einzige Auflösung
nannte ein Katalogthema. Ebenso: Formerweiterung „typischer Fehler
→ verletzte Voraussetzung"; Zurufparameter „reduziert"/
„Spickzeile"; Stundenanker als Katalogobjekt; gemeinsamer Kern 3–6
der Prompte als geholte Datei.

**Lehrer:** fachliche Gegenlese der Sek-II-Einträge; Posten in
faellig.md § 3; global.md und projekt-verbessereBlaetter.md aus
dem Repo in die Einstellungen kopieren (Stand 2026-09-21 gegen
19c bzw. 19).

## 6 Nächster Arbeitsschritt

Die sieben Befunde aus befund-inkonsistenzen-2026-09-21.md
durchgehen, beginnend mit § 1 und § 2: Wird die Architekturregel
„Trennung nach Quelle" aufgehoben oder neu gezogen, und liest der
Unterrichtsblatt-Prompt künftig themen.csv und katalog/*.md? An
dieser Antwort hängen die vier Konzepte vom 19.09. und die
Erinnerungsfrage. Erst danach wird an den Prompten gebaut.
