# Auftrag: Testlauf des Unterrichtsblatt-Prompts (wiederkehrend)

## Ausgangslage

`hz-0801/blattbau/unterrichtsblatt.md` liegt in Version v4.3
(Commit 512ae78). Der Prompt ist die Projektanweisung des
Claude-Projekts erzeugeUnterrichtsblatt(); dort baut ein Chat
aus einer Eingabe wie „kreis 8" druckfertige PDFs. Dieser
Auftrag baut dieselben Blätter ohne den Lehrer: je Eingabe aus
`werkzeuge/testlauf-eingaben.csv` eine frische Sitzung, die den
Prompt als Systemanweisung bekommt und die Eingabe als
Nutzerzeile; die Ergebnisse werden abgelegt, gemessen und für
das Gegenlesen aufbereitet. Läuft der Auftrag bei einer späteren
Prompt-Version erneut, entsteht ein zweiter Ordner mit demselben
Aufbau, und die Kennzahlen lassen sich nebeneinanderlegen.

Der Lauf ist unbeaufsichtigt: keine Rückfrage, keine
Wartestelle. Grenzen sind Zählgrenzen, keine Zeitgrenzen.

## Ablageort

`blaetter/testlauf-<JJJJ-MM-TT>/` mit dem heutigen Datum
(Tag des Starts). Darin:
- `stand.md` – Standdatei, nach jeder Eingabe fortgeschrieben
  (siehe Standdatei).
- `<nr>-<kurzname>/` je Eingabe, Kurzname aus der CSV; darin
  alle PDFs, das Protokoll-Archiv entpackt (alle .tex, Logs,
  pruef.py, pruef_out, protokoll.txt, chat.txt, zeiten.txt), die
  Textausgabe der Sitzung als `sitzung.txt`.
- `kennzahlen.md` – Ausgabe von `werkzeuge/blatt-pruef.py` über
  alle Blätter des Laufs (siehe Teil 3).
- `lesezettel.md` – je Eingabe ein Abschnitt für den Lehrer
  (siehe Teil 4).

## Teil 1 – Vorbereitung (ein Commit)

1. `unterrichtsblatt.md` per Raw-URL holen:
   https://raw.githubusercontent.com/hz-0801/blattbau/main/unterrichtsblatt.md
   Zeile 1 muss „v4.3" tragen; sonst abbrechen mit Grund in
   `stand.md` und Bericht.
2. Werkzeuge prüfen: `claude` auf der Befehlszeile (Version
   ausgeben), `xelatex`, `pdftotext` und `pdfinfo` unter
   `%LocalAppData%\Programs\MiKTeX\miktex\bin\x64`, Python unter
   `%LocalAppData%\Programs\Python\Python312\python.exe`, `curl`.
   Den MiKTeX-Pfad in den PATH jeder Sitzung setzen.
3. Bauweise festlegen und in `stand.md` notieren:
   - Regelweg: je Eingabe ein Aufruf
     `claude -p "<Eingabe>" --append-system-prompt-file
     <pfad zu unterrichtsblatt.md> --dangerously-skip-permissions
     --model opus` im Arbeitsordner der Eingabe, Ausgabe nach
     `sitzung.txt`. Kennt die installierte Version die Optionen
     unter anderem Namen, nimm die passenden und notiere sie.
   - Ersatzweg, wenn `claude -p` fehlt oder die Systemanweisung
     nicht annimmt: je Eingabe ein Sub-Agent (Task) mit dem
     vollständigen Prompttext als erstem Teil und der Eingabe als
     zweitem Teil; ein Sub-Agent je Eingabe, nie zwei in einem.
   - Der Prompt verlangt drei Antworten mit „weiter" dazwischen
     (Abschnitt 2.7). In einer Sitzung ohne Gegenüber gilt: Die
     Eingabezeile endet mit „ – Antworten auf Planfrage und Zone:
     <antworten aus der CSV>; baue ohne Halt bis zum Ausgabeblock
     durch". Der Prompt liest das als Freitext-Anweisung (1.1).
4. Ordner `blaetter/testlauf-<datum>/` und `stand.md` anlegen;
   Commit „testlauf <datum>: Vorbereitung".

## Teil 2 – Bau, je Eingabe ein Commit

Für jede Zeile der CSV in Reihenfolge:
1. Arbeitsordner `<nr>-<kurzname>/` anlegen, Sitzung starten
   (Teil 1, Schritt 3), Ausgabe nach `sitzung.txt`.
2. Nach dem Ende: PDFs und Protokoll-Archiv in den Ordner, Archiv
   entpacken. Fehlt das Archiv, bleibt, was da ist.
3. Prüfen: mindestens ein PDF mit „Gesamt" oder „Fokus" im Namen,
   `protokoll.txt` mit Zeile „Prompt: Unterrichtsblatt-Prompt
   v4.3". Fehlt eines, zählt die Eingabe als „offen".
4. Fehlerregel: Bricht die Sitzung ab oder fehlt das Gesamt-PDF,
   ein zweiter Anlauf in frischer Sitzung. Nach zwei Anläufen:
   Eingabe „offen mit Grund" in `stand.md`, nächste Eingabe.
   Nichts wird von Hand nachgebaut, kein Quelltext korrigiert.
5. Zählgrenze: Ein Anlauf, der mehr als 60 Werkzeugaufrufe in
   `protokoll.txt` zeigt, gilt als Befund (Zeile im Lesezettel),
   nicht als Fehler.
6. `stand.md` fortschreiben, Commit „testlauf <datum>: <nr>
   <kurzname>". Bei einem Neustart des Auftrags wird `stand.md`
   gelesen und mit der ersten Eingabe weitergemacht, die dort
   nicht „fertig" oder „offen" ist.

## Teil 3 – Messen (ein Commit)

1. `werkzeuge/blatt-pruef.py` über alle Gesamt- und Fokus-PDFs
   des Laufs laufen lassen; Ergebnis nach
   `blaetter/testlauf-<datum>/kennzahlen.md`. `blaetter/
   kennzahlen.md` bleibt unberührt (das Skript schreibt sie
   ungefragt – vorher sichern, danach zurücksetzen).
   Kennt das Skript einen Parameter für den Ausgabeort nicht,
   ergänze ihn und lege die Änderung mit ab.
2. Zusätzlich je Blatt aus der Textextraktion zählen und in
   `kennzahlen.md` eintragen: Zahl der Zweigzeilen (Zeilen mit
   „Hier lernst du" oder zwei „·"-Trennern nach einem
   Einheitenkopf), Zahl der Titel, die mit „Ich kann", „Ich
   erkenne" oder „Ich finde" beginnen, gegen die Zahl der
   Hauptnummern; ob eine Seite „Das kann ich" existiert; ob das
   Wort „Blatt 0" irgendwo im PDF vorkommt (darf nicht).
3. Gegenprobe mit bekannten Werten – Abweichung ist ein Befund,
   kein Grund, das Skript zu ändern:
   - Eingabe 1 und 2 haben dieselben Zweige, aber verschiedene
     Zeitmarken (die Marken-Zeile von quadratische-gleichungen
     Einheit 2 lautet OS Kl. 10, GYM Kl. 8–9).
   - Eingabe 8 enthält einen Zweig mit „Potenzfunktion" und dem
     Prüfungswort „keine P10-Aufgabe".
   - Eingabe 4 hat kein PDF „KennstDuSchon".
4. Commit „testlauf <datum>: Kennzahlen".

## Teil 4 – Lesezettel und Bericht (ein Commit)

1. `lesezettel.md`: je Eingabe ein Abschnitt mit: der Eingabe,
   der Deutungszeile und dem Plan wortgleich aus `chat.txt`, dem
   Ausgabeblock wortgleich, den Dateinamen der PDFs mit relativem
   Pfad, drei bis fünf Zeilen „Worauf beim Gegenlesen achten" aus
   der Spalte „prüft" der CSV, ergänzt um das, was in diesem
   Blatt auffällt (fehlende Zweigzeile, Titel ohne „Ich kann",
   Typen ohne Treffer aus den Kennzahlen, Aufrufe über 60). Der
   Lesezettel bewertet nicht; er zeigt.
2. Bericht `bericht-testlauf-<datum>.md` in der Wurzel: erste
   Zeile das Modell der Auftragssitzung und das Modell der
   Blattsitzungen; Bauweise (Regel- oder Ersatzweg, Optionen);
   Tabelle je Eingabe: Anläufe, Ergebnis (fertig/offen),
   Werkzeugaufrufe laut protokoll.txt, Seiten Gesamt, Zeit aus
   zeiten.txt; die drei Gegenproben mit Ist-Wert; was der
   Auftrag nicht regelte und wie entschieden; Abweichungen des
   Sitzungsverhaltens vom Prompt, die dir auffallen (Planfrage
   trotz Antwort gestellt, Bau angehalten, Rückfall ohne
   Katalog); letzte Zeile „Push origin drücken".
3. README.md: den Ordner `blaetter/testlauf-<datum>/`, die CSV,
   diesen Auftrag (Archiv) und den Bericht eintragen; im Absatz
   zu `blaetter/` einen Satz, dass Testläufe dort datiert liegen
   und nicht im Register `blaetter/index.md` stehen.
4. `faellig.md` § 2: Posten „Testlauf wiederholen · Auslöser:
   neue Version von unterrichtsblatt.md · bei wem: Claude Code
   (Nacht)".
5. Diesen Auftrag nach `archiv/auftrag-testlauf-<datum>.md`
   verschieben (nicht löschen). Commit „testlauf <datum>:
   Lesezettel, Bericht".

## Standdatei (`stand.md`)

Je Zeile: „<nr> <kurzname> · <fertig|offen|läuft> · Anläufe n ·
<Grund bei offen>". Kopf: Datum, Prompt-Version, Bauweise, Modell.
Wird nach jedem Schritt geschrieben, nie nur am Ende.

## Regeln

- Shell ist PowerShell 5.1: kein Heredoc, kein sed. Dateien
  schreiben mit `[System.IO.File]::WriteAllText(pfad, text,
  (New-Object System.Text.UTF8Encoding($false)))`; nach dem
  Schreiben prüfen, dass keine BOM und kein CR entstanden sind.
- Python nur über `%LocalAppData%\Programs\Python\Python312\
  python.exe`; MiKTeX, `pdftotext`, `pdfinfo` unter
  `%LocalAppData%\Programs\MiKTeX\miktex\bin\x64`.
- git über die git.exe von GitHub Desktop mit `-c
  core.pager=cat`; Commit-Nachrichten über `commit -F` aus einer
  UTF-8-Datei.
- Nichts löschen; verschieben nach `archiv/`. `hefte/` nicht
  anfassen.
- Am Prompt und an den Katalogeinträgen wird nichts geändert;
  ein Blatt, das schlecht ist, ist ein Befund.
- Skripte und Daten, die der Lauf braucht, kommen ins Repo.
- Nichts wartet auf den Lehrer. Ein Zuruf von ihm (etwa
  „Stand?") wird mit dem Inhalt von `stand.md` beantwortet, der
  Lauf geht weiter.
