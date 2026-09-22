# Übergabe 2026-09-22c – Werkstatt verbessereBlaetter

## 1 Ziel

Der bestmögliche Themenkatalog und die beiden Prompts, die aus
ihm Blätter bauen. Maßgeblich ist ziel.md in der Wurzel; jede
Entscheidung dient dem Blatt, das ein Schüler im ersten Lauf
bearbeiten kann.

## 2 Arbeitsgrundlage

- ziel.md – das Ziel; gilt vor jeder anderen Datei.
- befund-lauf3-2026-09-22.md (Wurzel) – Befunde und Beschlüsse
  des dritten Laufs; Bauplan für Vorlage Stufe 4 in § 2.4.
- befund-testlauf-2026-09-22.md (Wurzel) – Befunde der Läufe 1
  und 2 mit den Beschlüssen zu v4.0.
- blaetter/ – zwei abgelegte Blätter (prozentrechnung und daten,
  je 2026-09-22) mit PDFs, Quelltexten und je einer eigene.sty;
  Register blaetter/index.md.
- katalog/ (73 Einträge), README.md als Landkarte; Stand
  Commit 1e811b5.
- blattbau/unterrichtsblatt.md v4.1 (Commit bd0fee8) – läuft als
  Projektanweisung in erzeugeUnterrichtsblatt() (am 22.09. dort
  eingesetzt; vorher lag versehentlich die Werkstatt-Anweisung).
- blattbau/mathblatt.sty Stand 2026-09-07d, Anleitung_mathblatt.md.
- blattbau/pruefungsblatt.md v0.15 – unverändert, nicht auf
  ziel.md umgebaut.

## 3 Arbeitsstand

Abgeschlossen: Lauf 3 (Eingabe „daten", v4.1, Opus) gebaut,
ausgewertet und abgelegt. Das Blatt trägt gegen ziel.md § 1–3;
Befunde und Beschlüsse in befund-lauf3-2026-09-22.md. Erste
Bauzeitmessung: Blatt 0 nach 284 s, Gesamt nach 1127 s, 24
Werkzeugschritte, 7 Korrekturen, Werkzeuggrenze der Oberfläche
einmal erreicht.

Seit der letzten Übergabe geändert: Beschlüsse zu Bereitstellung
und Reihenfolge (§ 4); Vorlage Stufe 4 rückt vor die
Prompt-Kürzung.

Läuft nicht: nichts.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Beschlüsse 22.09.2026 (Lauf 3, Details befund-lauf3 § 2–3):
- Blatt 0 beendet die erste Antwort des Blatt-Chats (Karte plus
  Zeile „Weiter baut Einheit 1 bis 5, Gesamt und Lösungen"); der
  Rest läuft nach „Weiter" ohne Rückfrage und liefert Lernblatt
  ohne Blatt 0, Gesamt mit Blatt 0, Lösungen, Archiv. Einheit 1
  als eigenes frühes PDF entfällt. Ersetzt den Beschluss „Bau in
  Reihe, Blatt 0 und Einheit 1 früh als PDF".
- Ziel für den Rest nach Blatt 0: ein Durchgang unter der
  Werkzeuggrenze. Mittel: Vorlage Stufe 4 (keine eigene.sty mehr)
  und 2.7 schlank – Aufrufe derselben Einheit bündeln, ein
  Prüfskript für alle Einheiten; Prüfung je Einheit direkt nach
  dem Schreiben bleibt, keine Prüfung entfällt. Bedingung des
  Lehrers: Druckqualität und Inhalt unverändert.
- Vorlage Stufe 4 vor der Prompt-Kürzung.
- LaTeX bleibt das Format (Typst, HTML geprüft und verworfen: die
  Bauzeit ist Schreibzeit des Modells, nicht Kompilat).
- Fehlerlisten aus abgelegten Blättern sind Werkzeug der
  Werkstatt, nicht Eingabe des Blatt-Prompts: Was zweimal
  auftritt, wandert in Vorlage oder Prompt.

Beschlüsse vom 22.09. (Läufe 1 und 2) gelten weiter, siehe
befund-testlauf-2026-09-22.md und archiv/uebergabe-2026-09-22b.md
§ 4.

Rahmen:
- Oberfläche: Dateikarten einer Antwort erscheinen erst, wenn die
  Antwort endet (Annahme, hohe Sicherheit). Je Antwort etwa 20
  Werkzeugaufrufe, dann „Weiter"-Knopf; nicht einstellbar.
- Claude-Code-Shell: py -3 gibt es nicht, nur der volle Pfad
  %LocalAppData%\Programs\Python\Python312\python.exe; git über
  die git.exe von GitHub Desktop.
- Der Blatt-Prompt holt mathblatt.sty und Anleitung bei jedem Lauf
  aus dem Repo: Stufe 4 wirkt mit dem Push sofort auf jedes neue
  Blatt – Test vor dem Commit ist Pflicht.
- Modellwahl: Opus Regelfall; Fable für den Prompt-Umbau 2.7/1.5
  und Katalogentscheidungen; Claude Code Opus für die Vorlage,
  Sonnet für Mechanik.

## 5 Offene Punkte und verworfene Ansätze

Offen, in dieser Reihenfolge:
1. TeX auf dem Rechner klären (MiKTeX oder anderes): Claude Code
   muss die Vorlage vor dem Commit kompilieren und rendern können.
   Ohne TeX: Probekompilat über einen Blatt-Chat.
2. Vorlage Stufe 4 in blattbau (Claude Code, Opus): Bausteine aus
   beiden eigene.sty (blaetter/*/2026-09-22/src/), Layoutfehler
   und Verzeichnis mit hyperref nach befund-lauf3 § 2.4;
   Anleitung_mathblatt.md nachziehen; Test mit einem abgelegten
   Quelltext.
3. Prompt-Umbau zu v4.2 (Fable): 2.7 Bereitstellung nach § 4 und
   schlank; 1.5 Regel für Einträge „Sek I + II" (ohne
   Klassenangabe Sek-I-Stoff, Deutungszeile nennt den Schnitt;
   Sek-II-Teil nur mit „fos", „gymnasium" oder Klasse ab 11);
   4.5 an Stufe 4; Kleines aus befund-lauf3 § 2.6; Beispiel je
   Typ entscheiden (§ 2.5). Danach Projektanweisung in
   erzeugeUnterrichtsblatt() ersetzen und Lauf 4.
4. Befunde-Skript: einsortieren.py schreibt zusätzlich
   blaetter/befunde.md (Tabelle je Lauf aus protokoll.txt:
   Version, Vorlage, Zeiten, Schritte, Korrekturen mit Anlass,
   fehlende Bausteine, Warnungen; Zählung über alle Läufe). Ab
   dem fünften Lauf; Sonnet.
5. Sonnet-Vergleichslauf (gleiche Eingabe wie Lauf 2 oder 3).
6. Prompt kürzen um etwa ein Drittel – erst nach v4.2 und Lauf 4.
7. Prüfungsblatt-Prompt auf ziel.md umbauen (Prüfungsheft,
   Lösungsdatei getrennt, Lösungstiefe § 4, Schwelle „selten").
8. Katalog: Gegenlese der Sek-II-Einträge, Kategorien je
   Prüfungsart, Boden unter Klasse 8; katalog/_vorlage.md Zeile 20
   („eigene Aufgabe auf Blatt 0"); befund-geltung- und
   befund-inkonsistenzen-2026-09-21.md fehlen in README.md.
9. Leerer Kasten zum Selbstausfüllen; Band aller Themen – wie in
   der letzten Übergabe.

Verworfen:
- Typst oder HTML statt LaTeX – spart Sekunden, kostet die
  Vorlage (97 KB geprüfte Bausteine).
- Einheit 1 als eigenes frühes PDF – wird ohnehin erst mit dem
  Gesamt sichtbar.
- Browser-Erweiterungen, die „Weiter" drücken – nur im Browser,
  Drittanbieter.
- Prüfung über alle Einheiten erst am Ende bündeln – Fehler in
  Einheit 1 zeigt sich sonst erst nach Einheit 5.
- Fehlerliste als Eingabe des Blatt-Prompts – Umgehen je Lauf
  kostet die Schritte, die gespart werden sollen.
- Verworfenes der Übergabe 2026-09-22b gilt weiter.

## 6 Nächster Arbeitsschritt

TeX klären: Auftrag an Claude Code (blattbau, Sonnet), der
prüft, ob pdflatex oder latexmk in der Shell erreichbar sind und
ob mathblatt.sty mit einem abgelegten Quelltext (etwa
blaetter/daten/2026-09-22/src/) kompiliert; Bericht hierher.
Danach den Stufe-4-Auftrag schreiben (Opus).
