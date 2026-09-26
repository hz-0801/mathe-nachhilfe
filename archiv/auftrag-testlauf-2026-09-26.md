# Auftrag: Testlauf des Unterrichtsblatt-Prompts v4.4

Modell der Auftragssitzung: Opus. Ordner: mathe-nachhilfe.
Unbeaufsichtigt: keine Rückfrage, keine Wartestelle, Standdatei,
Commit je Teil bzw. je Eingabe, Fehlerregel je Schritt. Grenzen
sind Zählgrenzen, keine Zeitgrenzen. In ../blattbau läuft keine
Sitzung; du liest dort, schreibst dort nichts.

Datum des Laufs: aus `Get-Date -Format yyyy-MM-dd` beim Start;
überall, wo unten `<datum>` steht, dieses Datum – nie ein Datum
aus einem Text, einer Übergabe oder dem Gedächtnis.

## Ausgangslage

`hz-0801/blattbau/unterrichtsblatt.md` liegt in Version v4.4
(Commit 36b7b12) und ist die Projektanweisung des Projekts
erzeugeUnterrichtsblatt(). Dieser Auftrag baut die zehn Eingaben
aus `werkzeuge/testlauf-eingaben.csv` mit v4.4, legt sie neben
den Lauf vom 25.09. (v4.3, `blaetter/testlauf-2026-09-25/`,
eingefroren), misst beide gleich und bereitet einen Lesezettel
vor. Grundlage ist die Vorlage `werkzeuge/testlauf-auftrag.md`;
wo dieser Auftrag abweicht, gilt dieser Auftrag.

## Regeln

- Shell PowerShell 5.1: kein Heredoc, kein sed. Dateien schreiben
  mit [System.IO.File]::WriteAllText(pfad, text,
  (New-Object System.Text.UTF8Encoding($false))); nach dem
  Schreiben prüfen (keine BOM, kein CR).
- Python nur %LocalAppData%\Programs\Python\Python312\python.exe;
  xelatex, pdftotext, pdfinfo unter
  %LocalAppData%\Programs\MiKTeX\miktex\bin\x64 (in den PATH jeder
  Blattsitzung setzen).
- git über die git.exe von GitHub Desktop, mit -c core.pager=cat;
  Commit-Nachrichten über commit -F aus einer UTF-8-Datei; kein
  Push.
- Nichts löschen; verschieben nur mit git mv. hefte/ und
  blaetter/testlauf-2026-09-25/ nicht anfassen.
- Am Prompt und an den Katalogeinträgen wird nichts geändert; ein
  schlechtes Blatt ist ein Befund. Nichts wird von Hand nachgebaut,
  kein Quelltext einer Blattsitzung korrigiert.
- Gegenproben: Weicht eine ab, steht die Abweichung mit Erklärung
  im Bericht; kein Skript wird deshalb geändert.
- Uhrzeiten nur aus Get-Date, im Augenblick des Schritts.
- Skripte und Daten, die der Lauf braucht, kommen ins Repo.

## Teil 0: Vorbereitung der Werkzeuge (ein Commit)

1. werkzeuge/testlauf-eingaben.csv, Spalte „prueft" (Posten aus
   befund-testlauf-2026-09-25.md, Werkzeug 3):
   - Eingabe 5: „Ausblick-Zweig Kreisteile am Ende mit Ausblick"
     ersetzen durch „kein Ausblick-Zweig (alle Marken bei Kl. 7–8);
     die Deutungszeile nennt ‚mit Ausblick' ohne Zweig".
   - Eingabe 6: „Stufenfrage beantwortet (Sek I)" ersetzen durch
     „keine Stufenfrage, weil die Klasse 7 genannt ist".
   Sonst nichts an der CSV; Eingaben und Antworten bleiben gleich,
   damit die Läufe vergleichbar sind.
2. werkzeuge/testlauf-auftrag.md: die feste Versionsnummer „v4.3"
   (Ausgangslage, Teil 1 Schritt 1, Teil 2 Schritt 3) ersetzen
   durch „die Version aus Zeile 1 von unterrichtsblatt.md, die der
   Auftrag nennt"; den Pfad der Befehlszeile ersetzen durch
   %LocalAppData%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\
   Roaming\Claude\claude-code\<version>\claude.exe; in Teil 4 die
   Tabellenspalte „Aufrufe (Umgebung)" neben „Werkzeugaufrufe laut
   protokoll.txt" verlangen (Posten Werkzeug 1).
3. faellig.md: Posten Werkzeug 1 und 3 erledigt (§ 4).

Commit „testlauf: Vorlage und Eingabeliste nachgezogen".

## Teil 1: Vorbereitung des Laufs (ein Commit)

1. unterrichtsblatt.md per Raw-URL holen
   (https://raw.githubusercontent.com/hz-0801/blattbau/main/
   unterrichtsblatt.md); Zeile 1 muss „v4.4" tragen, sonst Abbruch
   mit Grund in stand.md und Bericht.
2. Werkzeuge prüfen wie in der Vorlage, Teil 1 Schritt 2.
3. Bauweise nach der Vorlage, Teil 1 Schritt 3: zuerst der
   Regelweg `claude -p` mit `--append-system-prompt-file` und
   `--model opus` (Pfad aus Teil 0 Punkt 2), Probeaufruf vorher;
   erst wenn er nicht verfügbar ist, der Ersatzweg mit einem
   Sub-Agenten je Eingabe (werkzeuge/testlauf-umgebung.md). Die
   Blätter laufen nacheinander, nie gleichzeitig. Die Eingabezeile
   endet mit „ – Antworten auf Planfrage und Zone: <antworten aus
   der CSV>; baue ohne Halt bis zum Ausgabeblock durch".
4. Ordner blaetter/testlauf-<datum>/ (bei Namensgleichheit „b"
   anhängen) und stand.md (Form wie in der Vorlage) anlegen.

Commit „testlauf <datum>: Vorbereitung".

## Teil 2: Bau, je Eingabe ein Commit

Wie die Vorlage, Teil 2, mit zwei Änderungen: In Schritt 3 muss
protokoll.txt „Prompt: Unterrichtsblatt-Prompt v4.4" tragen.
Zusätzlich zur Aufrufzahl aus protokoll.txt zählst du die
tatsächlichen Werkzeugaufrufe der Sitzung aus ihrer Ausgabe oder
dem Sitzungsprotokoll (Spalte „Aufrufe (Umgebung)"); geht das im
gewählten Weg nicht, steht „nicht messbar" mit Grund.
Fehlerregel: nach zwei Anläufen „offen mit Grund", nächste
Eingabe.

## Teil 3: Messen (ein Commit)

1. werkzeuge/blatt-pruef.py --testlauf blaetter/testlauf-<datum>
   --ausgabe blaetter/testlauf-<datum>/kennzahlen.md;
   blaetter/kennzahlen.md bleibt unberührt.
2. Zusätzlich je Blatt, aus Quelltext und Textextraktion, in eine
   Tabelle v44-pruefung in kennzahlen.md (eine Zeile je Eingabe,
   eine Spalte je Punkt, Wert oder „ja/nein"):
   a) Zahl `\rechenplatz`; Zahl Umgebung `beispiel` (Soll 0 –
      keine Eingabe bestellt „mit beispiel");
   b) Seite „Inhalt" vorhanden (Soll nein); `\verzeichniszeile`
      vorhanden (Soll ja bei Lernblatt und Gesamt);
   c) Nummern: beginnt die Zone bei 1 und läuft das Lernblatt
      danach weiter (Soll ja); kommt „Z1" vor (Soll nein);
   d) Zahl `\verfahren`; Zahl `\anweisung`;
   e) Bausteine der Vorlage im Vorspann nachgebaut: Zahl der
      `\newcommand`, `\def`, `\newenvironment` in den Rahmen- und
      Einheitsdateien, deren Name in ../blattbau/
      Anleitung_mathblatt.md steht (Soll 0), mit Namen;
   f) Deutungszeile in chat.txt beginnt mit „→" (Soll ja);
   g) zeiten.txt: jeder Stempel genau einmal, „e n" mit
      Leerzeichen (Soll ja);
   h) Prüfungsmarken: Zahl der Klammern „(P10 JJJJ …)" und davon
      mit Papier (FOR, EBR, OS, GYM) dahinter.
3. Vergleichstabelle v4.3 gegen v4.4 in kennzahlen.md: je Eingabe
   Seiten Gesamt/Fokus, Hauptnummern, Teilaufgaben, Werkzeug-
   aufrufe laut protokoll.txt, Zeit aus zeiten.txt – links die
   Werte aus blaetter/testlauf-2026-09-25/kennzahlen.md und
   bericht-testlauf-2026-09-25.md, rechts die neuen.
4. Gegenproben (Belegquelle dabei):
   - Eingabe 1 und 2: dieselben Zweige, verschiedene Zeitmarken
     (katalog/quadratische-gleichungen.md, Marken Einheit 2:
     OS Kl. 10, GYM Kl. 8–9).
   - Eingabe 4: kein PDF „KennstDuSchon".
   - Eingabe 5: Deutungszeile nennt „mit Ausblick" ohne Zweig
     (CSV nach Teil 0).
   - Eingabe 8: ein Zweig mit „Potenzfunktion" und „keine
     P10-Aufgabe".
   - Eingabe 9: kein Zweig liegt in der Zone; die Zweige tragen
     eine Zeitmarke mit „Q1" (unterrichtsblatt.md v4.4, 1.5).
   - Eingabe 7: Zweigkopf ohne „von" (v4.4, 2.5).

Commit „testlauf <datum>: Kennzahlen".

## Teil 4: Lesezettel, Bericht, Abschluss (ein Commit)

1. lesezettel.md wie in der Vorlage, Teil 4 Schritt 1; unter
   „Worauf beim Gegenlesen achten" je Blatt zusätzlich die Punkte
   aus Teil 3 Schritt 2, die ihr Soll verfehlen.
2. Bericht bericht-testlauf-<datum>.md in der Wurzel wie in der
   Vorlage, Teil 4 Schritt 2, mit der Spalte „Aufrufe
   (Umgebung)" und einem Abschnitt „v4.3 gegen v4.4" (drei bis
   sechs Sätze aus der Vergleichstabelle, ohne Urteil).
3. README.md: Ordner, Bericht, Auftrag im Archiv.
4. faellig.md § 2, zwei neue Posten:
   - „Unterrichtsblatt v4.5 straffen: nach dem Lesen dieses
     Testlaufs; Kandidaten 4.4 und 4.6 in die Anleitung der
     Vorlage, Muster in 2.3 zusammenfassen, 6.3 kürzen; danach
     derselbe Testlauf als Kontrolle (gleiche Kennzahlen bei
     kürzerem Prompt) · Chat (Fable), dann Claude Code".
   - „Aufträge datieren mit Get-Date: Dateinamen von Nacht- und
     Standdateien tragen das Datum des Starts aus Get-Date, bei
     zwei Aufträgen am selben Tag ‚b'; die fortlaufende Zählung
     (nacht-2026-09-29 am 26.09.) endet · Chat".
5. Diesen Auftrag nach archiv/auftrag-testlauf-<datum>.md
   verschieben (git mv; bei Namensgleichheit „b").

Commit „testlauf <datum>: Lesezettel, Bericht".

## Bericht

bericht-testlauf-<datum>.md und im Chat. Erste Zeile: Modell der
Auftragssitzung und der Blattsitzungen. Je Teil, was geändert
ist; die Tabelle je Eingabe; alle Gegenproben im Wortlaut mit
Ist-Wert; die Tabelle v44-pruefung; was der Auftrag nicht regelte
und wie entschieden; Abweichungen des Sitzungsverhaltens vom
Prompt. Letzte Zeile: „Push origin drücken".
