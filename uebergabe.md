# Übergabe 2026-09-22b – Werkstatt verbessereBlaetter

## 1 Ziel

Der bestmögliche Themenkatalog und die beiden Prompts, die aus
ihm Blätter bauen. Maßgeblich ist ziel.md in der Wurzel; jede
Entscheidung dient dem Blatt, das ein Schüler im ersten Lauf
bearbeiten kann.

## 2 Arbeitsgrundlage

- ziel.md – das Ziel; gilt vor jeder anderen Datei.
- katalog/ (73 Einträge) mit README.md als Landkarte; Stand
  Commit 78363ff. Prüfläufe: werkzeuge/themen-pruef.py,
  verweis-pruef.py, tragfaehigkeit.py, blatt0-belege.py, neu
  ertrag.py (msa/msa-ertrag.md) und einsortieren.py (blaetter/).
- blattbau/unterrichtsblatt.md v4.1 (Commit bd0fee8) – läuft als
  Projektanweisung in erzeugeUnterrichtsblatt(); CHANGELOG.md
  und Testauswertung_2026-09-22.md dort.
- blattbau/pruefungsblatt.md v0.15 – unverändert, noch nicht auf
  ziel.md umgebaut.
- befund-testlauf-2026-09-22.md (Wurzel) – Befunde und
  Beschlüsse der beiden Testläufe.
- blaetter/prozentrechnung/2026-09-22/ – erstes abgelegtes Blatt
  (Lauf 2, v4.0), mit Quelltexten und eigene.sty (Streifen,
  Dreisatz-Schema, Einheitenkopf).

## 3 Arbeitsstand

Abgeschlossen: Katalogumbau des Unterrichtsblatt-Prompts. Lauf 1
(v3.34, Eintrag als Zuruf-Quelle) und Lauf 2 (v4.0, Eingabe
„prozentrechnung") sind ausgewertet; v4.0 baute alle fünf
Einheiten aus dem Eintrag, fachlich fehlerfrei, die Kette folgte
den Sprossen des Eintrags, Vorstufen und Verfremdung mit Jahr
saßen. v4.1 zieht Bereitstellung, Lösungsdatei, Vorstufenregel,
Titelregel und Protokoll nach. Katalog: 71 tote „→ Dialog"-Zeilen
entfernt, Erkennungsschritt-Kopfzeile auf den neuen Beschluss
umgestellt. Ertrag je Typ (msa) liegt vor. Blattablage steht:
einsortieren.py holt *protokoll*.zip aus Downloads,
OneDrive/Downloads und OneDrive/blatt-eingang.

Seit der letzten Übergabe geändert: alles oben; dazu Python 3.12
auf dem Rechner (voller Pfad, nicht im PATH der Claude-Code-
Shell), git nur über die git.exe von GitHub Desktop.

Läuft nicht: nichts.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Beschlüsse 22.09.2026 (Details in befund-testlauf-2026-09-22.md):
- Ein Lernblatt, alle Einheiten des Eintrags, kein Budget, kein
  Schnitt; Bau in Reihe, Blatt 0 und Einheit 1 früh als PDF,
  am Ende Gesamt (klickbares Verzeichnis, Seitenbereiche je
  Einheit) und Lösungen als eigene Datei mit Lösungstiefe nach
  ziel.md § 4. Grund: Lehrer baut am Stundenanfang, druckt nach
  Seitenbereichen, entscheidet am Drucker über Lösungen.
- Blatt 0 nur Fertigkeiten, Reihenfolge nach erster Verwendung
  („– Einheit n"); Erkennungsschritte als Vorstufe der Einheit,
  einmal bei der ersten Einheit ihres Bereichs.
- Jede Hauptnummer „Kurzname – Formwort"; keine Typnamen des
  Katalogs auf dem Blatt; gemischte Aufgaben „Gemischt".
- Verfremdung mit Jahr; keine Zahl aus Kasten, Beispiel oder
  Original in einer Teilaufgabe.
- Kein Kasten (nur „mit kasten"), keine Sterne, keine Hilfe-
  Seite, kein „Lernblatt kurz", kein Testformat.
- Dreisatz als gerahmtes Schema; Blatt-0-Zahlen im Kopf
  rechenbar; Doppelpunkt als Geteiltzeichen bleibt.
- Blätter werden abgelegt (blaetter/, PDFs und Quelltexte);
  ein Thema wird einmal gebaut. Aktualisieren aus Quelltext erst,
  wenn der Prompt zwischen zwei Versionen nur in Abschnitt 3–6
  ändert.
- Der Erkennungsschritt-Bereich („vor Einheit 2 bis 5") bleibt
  im Katalog; die Zuordnung ist Prompt-Regel.
- Titelprüfung auf Schülersprache (271 Einheitstitel) nicht
  nötig, solange kein Lauf sie erzwingt.

Rahmen:
- Modellwahl im Werkstattchat: Opus als Regelfall; Fable nur für
  Laufauswertung gegen ziel.md, Prompt-Umbau in Abschnitt 0–2
  und Katalogentscheidungen. Sonnet hier nicht. Claude Code:
  Sonnet für Mechanik, Opus für die Vorlage. Blatt-Chats Opus.
- Aufträge kommen als .txt-Datei in Blockform (Kopieren, nicht
  gerenderte md-Vorschau); Material steht direkt am Handgriff.
- Ein Sprachmodell trägt nie Dateiinhalte (Drive-Upload teuer);
  Dateien wandern per Download und Shell.
- Bauzeit je Einheit bisher nie gemessen; v4.1 misst in
  zeiten.txt.
- Tabelle C in msa-ertrag.md: Median 3 Punkte je Typ in 13
  Jahren, 111 von 175 Typen in höchstens zwei Jahrgängen –
  „selten" braucht zwei Bedingungen (Punkte und Jahre); Schwelle
  offen, gehört zum Prüfungsheft.

## 5 Offene Punkte und verworfene Ansätze

Offen, in dieser Reihenfolge:
1. Lauf 3 mit v4.1 an einem Thema, das dem Prompt wehtut:
   daten.md (sechs Einheiten, unsortierte Fertigkeiten) oder ein
   Sek-II-Eintrag mit Profilen. Danach Archiv aus Downloads
   einsortieren; Auswertung gegen ziel.md, Bauzeiten je Einheit.
2. Vorlage Stufe 4 in blattbau (Opus): Streifen, gerahmter
   Dreisatz, Einheitenkopf, Verzeichnis mit hyperref aus
   eigene.sty; Anleitung nachziehen. Braucht TeX auf dem Rechner
   (MiKTeX) – vorher klären.
3. Prompt kürzen um etwa ein Drittel (1.5 FOS-Block in die
   Prüfungsform der Sek-II-Einträge, 4.4 in die Anleitung, zwei
   Muster) – erst, wenn v4.1 an einem zweiten Thema steht.
4. Sonnet-Vergleichslauf (gleiche Eingabe, Blatt gegen Lauf 2).
5. Prüfungsblatt-Prompt auf ziel.md umbauen (Prüfungsheft,
   Lösungsdatei getrennt, Lösungstiefe § 4, Schwelle „selten").
6. Gegenlese der Sek-II-Einträge, Kategorien je Prüfungsart,
   Boden unter Klasse 8 – unverändert aus der letzten Übergabe.
7. Katalog: katalog/_vorlage.md nennt noch „eigene Aufgabe auf
   Blatt 0" (Zeile 20); befund-geltung- und befund-
   inkonsistenzen-2026-09-21.md stehen nicht in README.md.
8. Leerer Kasten zum Selbstausfüllen: einmal auf Zuruf bauen,
   dann entscheiden.
9. Band aller Themen: erst, wenn zwei Läufe ohne Prompt-Umbau
   durchgehen; die Ablage ist die Vorstufe.

Verworfen:
- Einzel-PDFs je Einheit als Standard – nicht gebraucht, Lehrer
  druckt aus dem Gesamt; nur Einheit 1 früh, weitere auf Zuruf.
- Blatt 0 mit Erkennungsschritten – führte Themenbegriffe ein,
  bevor das Blatt sie lehrt.
- Beschlüsse als Zuruf gegen den alten Prompt testen – misst
  nichts, weil der Prompt das Gegenteil sagt.
- Katalogfeld „Blattname je Typ" – der Katalog kennt die
  Hauptnummern nicht; der Schnitt ist Prompt-Sache.
- Ablage per Drive-Konnektor – Modell trägt Bytes, teuer.

## 6 Nächster Arbeitsschritt

Lauf 3 vorbereiten: Thema wählen (Vorschlag daten.md), Eingabe
ist nur das Thema; nach dem Lauf Archiv einsortieren (Claude
Code, mathe-nachhilfe: py -3 werkzeuge/einsortieren.py, Commit,
Push) und die PDFs samt protokoll.txt hier auswerten – zuerst die
Zeiten je Einheit, dann Blatt 0, Vorstufen, Titel, Verzeichnis
und Lösungsdatei gegen ziel.md.
