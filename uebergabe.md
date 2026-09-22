# Übergabe 2026-09-22d – Werkstatt verbessereBlaetter

## 1 Ziel

Der bestmögliche Themenkatalog und die beiden Prompts, die aus
ihm Blätter bauen. Maßgeblich ist ziel.md in der Wurzel; jede
Entscheidung dient dem Blatt, das ein Schüler im ersten Lauf
bearbeiten kann.

## 2 Arbeitsgrundlage

- ziel.md – das Ziel; gilt vor jeder anderen Datei.
- befund-lauf3-2026-09-22.md (Wurzel) – Befunde und Beschlüsse
  des dritten Laufs; § 2.4 (Bauplan Stufe 4) ist abgearbeitet,
  § 2.5 und § 2.6 sind es nicht.
- befund-testlauf-2026-09-22.md (Wurzel) – Läufe 1 und 2 mit
  den Beschlüssen zu v4.0.
- blaetter/ – zwei abgelegte Blätter (prozentrechnung, daten,
  je 2026-09-22); Register blaetter/index.md.
- katalog/ (73 Einträge), README.md als Landkarte.
- blattbau/unterrichtsblatt.md v4.1 – läuft als
  Projektanweisung in erzeugeUnterrichtsblatt(); noch nicht auf
  Stufe 4 nachgezogen.
- blattbau/mathblatt.sty Stand 2026-09-22h (Stufe 4) und
  Anleitung_mathblatt.md – gepusht und live; der Blatt-Prompt
  holt beide bei jedem Lauf.
- blattbau/pruefungsblatt.md v0.15 – unverändert, nicht auf
  ziel.md umgebaut.

## 3 Arbeitsstand

Abgeschlossen: Vorlage Stufe 4 in vier Claude-Code-Aufträgen
(archiv/auftrag-vorlage4a bis 4d in blattbau):
- alle Bausteine aus beiden eigene.sty sind in mathblatt.sty;
  kein Blatt muss sich mehr eine eigene.sty schreiben,
- \einheitskopf bleibt als undokumentierte Weiterleitung auf
  \einheitenkopf*, damit abgelegte Blätter kompilieren,
- vier Layoutfehler behoben: teilezwei fluchtet mit teile,
  neuer Baustein \winkelstrahl, \strichliste zeichnet
  Fünferbündel (nimmt Zahl oder die alte Strich-Schreibweise),
  \saeulenab, \balkenab und \liniendia messen ihre
  Beschriftung selbst.
Gegenprobe nach jedem Auftrag mit xelatex: daten 21 Seiten,
prozentrechnung 16 Seiten, keine Fehlerzeile.

Auf dem Rechner ist MiKTeX 25.12 installiert, [MPM]AutoInstall
steht auf 1; xelatex und pdftoppm sind da, pymupdf nicht.
Claude Code kann die Vorlage damit selbst kompilieren und die
Seiten ansehen.

Läuft nicht: nichts.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Neu am 22.09.:
- Kompiliert und geprüft wird mit xelatex, nicht pdflatex
  (Anleitung_mathblatt.md Zeile 4). pdflatex verfälscht €.
- Dass eine hohe Hauptnummer als Ganzes auf die nächste Seite
  rückt, ist Absicht der Umgebung aufgabe und bleibt. Der
  Befund „halbe Seiten leer“ wird im Prompt gelöst: v4.2 teilt
  zu hohe Nummern in zwei, statt eine Riesenaufgabe zu bauen.
- Gegenprobe der Vorlage: Seitenzahlen 21 (daten) und 16
  (prozentrechnung) bleiben gültig. Die abgelegten PDFs taugen
  als Bildreferenz nur bis zur nächsten Vorlagenänderung – seit
  der teilezwei-Korrektur weichen sie an diesen Stellen
  berechtigt ab.
- Fragen an den Lehrer: eine je Nachricht, als letzte Zeile,
  eingeleitet mit „Frage:“. Ersetzt den Kandidaten „Fragen am
  betroffenen Absatz“.

Beschlüsse vom 22.09. (Läufe 1 bis 3) gelten weiter, siehe
befund-lauf3-2026-09-22.md § 2–3 und
archiv/uebergabe-2026-09-22c.md § 4.

Rahmen:
- Oberfläche: Dateikarten einer Antwort erscheinen erst, wenn
  die Antwort endet; je Antwort etwa 20 Werkzeugaufrufe.
- Claude-Code-Shell: der PATH einer laufenden Sitzung kennt
  MiKTeX, Python und git oft nicht; MiKTeX liegt in
  %LocalAppData%\Programs\MiKTeX\miktex\bin\x64, Python unter
  %LocalAppData%\Programs\Python\Python312\python.exe, git in
  der git.exe von GitHub Desktop. Jeder Auftrag nennt das.
- Die Sitzung startet trotz Vorgabe manchmal auf Sonnet: vor
  einem Opus-Auftrag den Modellwähler prüfen. Zwei der vier
  Stufe-4-Aufträge liefen auf Sonnet, beide Berichte waren
  brauchbar.
- Modellwahl nächste Phase: Fable für den Prompt-Umbau v4.2,
  Opus für Aufträge, Berichte und Auswertung.

## 5 Offene Punkte und verworfene Ansätze

Offen, in dieser Reihenfolge:
1. Prompt-Umbau zu v4.2 (Fable): 2.7 Bereitstellung nach § 4
   der letzten Übergabe und schlank; 1.5 Regel für Einträge
   „Sek I + II“; 4.5 an Stufe 4 – keine eigene.sty mehr, die
   neuen Bausteine stehen in Anleitung_mathblatt.md; neue
   Regel, zu hohe Hauptnummern in zwei zu teilen; Kleines aus
   befund-lauf3 § 2.6; Beispiel je Typ entscheiden (§ 2.5).
   Danach Projektanweisung in erzeugeUnterrichtsblatt()
   ersetzen und Lauf 4.
2. Befunde-Skript: einsortieren.py schreibt zusätzlich
   blaetter/befunde.md. Ab dem fünften Lauf; Sonnet.
3. Sonnet-Vergleichslauf (gleiche Eingabe wie Lauf 2 oder 3).
4. Prompt kürzen um etwa ein Drittel – erst nach v4.2 und
   Lauf 4.
5. Prüfungsblatt-Prompt auf ziel.md umbauen.
6. Katalog: Gegenlese der Sek-II-Einträge, Kategorien je
   Prüfungsart, Boden unter Klasse 8; katalog/_vorlage.md
   Zeile 20; befund-geltung- und
   befund-inkonsistenzen-2026-09-21.md fehlen in README.md.
7. Leerer Kasten zum Selbstausfüllen; Band aller Themen.
8. Kleinigkeit aus 4d: \liniendia lässt in einer halbbreiten
   Spalte eine Overfull-Warnung von 5,7 pt stehen; in voller
   Breite tritt sie nicht auf.

Verworfen:
- Typst oder HTML statt LaTeX – spart Sekunden, kostet die
  Vorlage.
- Umbruch hoher Aufgaben in der Vorlage lockern – zerreißt
  genau das, was die Umgebung schützt.
- Verworfenes der Übergaben 2026-09-22b und c gilt weiter.

## 6 Nächster Arbeitsschritt

Prompt-Umbau zu v4.2 (Fable): unterrichtsblatt.md v4.1 aus
blattbau lesen, die fünf Punkte aus § 5.1 einarbeiten, die
vollständige Fassung als Chat-Block ausgeben, damit der Lehrer
die Projektanweisung in erzeugeUnterrichtsblatt() ersetzt.
Danach Lauf 4 mit einer neuen Eingabe.
