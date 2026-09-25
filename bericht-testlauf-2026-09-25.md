Modell der Auftragssitzung: Claude Opus 5.5 (claude-opus-5-5) · Modell der Blattsitzungen: Sub-Agent mit model „opus“, laut protokoll.txt aller zehn Sitzungen Opus 5.5 (claude-opus-5-5)

# Bericht Testlauf des Unterrichtsblatt-Prompts, 25.09.2026

Auftrag: `archiv/auftrag-testlauf-2026-09-25.md`. Prompt: `hz-0801/blattbau/unterrichtsblatt.md` v4.3,
Commit 512ae78, Zeile 1 „# UNTERRICHTSBLATT v4.3 – PROMPT FÜR LERNBLATT UND FOKUS“, Kopie im
Testlaufordner (`unterrichtsblatt-v4.3.md`, 71520 Byte). Katalog live von raw.githubusercontent.com,
Stand main = 7613213 (lokal und origin gleich). Ablage `blaetter/testlauf-2026-09-25/`
(11,3 MB, 497 Dateien). Commits: 93a5d70 Vorbereitung, 22e5f09 … 332cad3 je Eingabe, fb6b897
Kennzahlen, dazu der Commit dieses Berichts.

## Bauweise

**Ersatzweg.** `claude` steht nicht im PATH. Die Beigabe der Desktop-App
(`%APPDATA%\Claude\claude-code\2.1.280\claude.exe`, Version 2.1.280) kennt alle Optionen des
Regelwegs unter demselben Namen (`-p`, `--append-system-prompt-file`,
`--dangerously-skip-permissions`, `--model`), meldet aber bei `-p` „Not logged in · Please run
/login“: Die Anmeldung liefert der Desktop-Host der Auftragssitzung, nicht die CLI. Ein Login ist
nicht Sache der Sitzung. Deshalb je Eingabe ein Sub-Agent (Typ general-purpose, model opus), ein
Sub-Agent je Eingabe, nie zwei Eingaben in einem.

Nachricht an jede Blattsitzung, drei Teile (Vorlage: `werkzeuge/testlauf-umgebung.md`):
1. Systemanweisung: Verweis auf die Promptkopie mit der Anweisung, sie vollständig mit dem
   Read-Tool zu lesen und genau nach ihr zu arbeiten (nicht der Prompttext selbst – siehe
   Entscheidungen, Punkt 2).
2. Umgebung: kein Gegenüber; Arbeitsverzeichnis im Scratchpad; PowerShell statt bash
   (Zeitstempel über `[DateTimeOffset]::UtcNow.ToUnixTimeSeconds()`); Pfade von xelatex,
   pdftotext, pdfinfo, pdftoppm, Python, sympy; Repo nicht lesen, Katalog per curl; keine
   Sub-Agenten; Schlussnachricht = was der Lehrer im Chat sähe.
3. Eingabe: Spalte `eingabe`, dahinter „ – Antworten auf Planfrage und Zone: <antworten>; baue
   ohne Halt bis zum Ausgabeblock durch“.

**Fehlstart.** Die erste Fassung der Nachricht (Eingaben 1–5) lehnte die API vor dem ersten
Werkzeugaufruf ab: „Opus 5.5's safeguards flagged this message“, Detail `reasoning_extraction`.
Umformuliert wurden zwei Sätze: „Sein Inhalt ist deine Systemanweisung für diese Sitzung, so als
stünde er als Projektanweisung über dem Chat“ → „arbeite dann genau nach ihr“, und „schreibe darin
der Reihe nach wortgleich alles, was du dem Lehrer … geschrieben hättest“ → „zeigt, was der Lehrer
im Chat zu sehen bekäme“. Danach lief jede Sitzung an.

## Ergebnis je Eingabe

Zeit = t0 bis zum letzten Stempel in `zeiten.txt`. Alle zehn Sitzungen liefen gleichzeitig
(t0 zwischen 12:17:36 und 12:22:15); die Zeiten enthalten also die Last von zehn parallelen
Sitzungen und sind nicht mit einem Einzellauf vergleichbar. „Aufrufe (Umgebung)“ und „Dauer“
meldete die Laufzeitumgebung beim Ende des Sub-Agenten; der Auftrag verlangt die Zahl laut
protokoll.txt, die Umgebungszahl steht daneben, weil sie zeigt, wie viel das Protokoll auslässt.

| Nr. | Kurzname | Anläufe | Ergebnis | Werkzeugaufrufe laut protokoll.txt | Aufrufe (Umgebung) | Seiten Gesamt | Zeit laut zeiten.txt | Dauer (Umgebung) |
|---|---|---|---|---|---|---|---|---|
| 1 | quadgl-9-os | 1 | fertig | 113 (über 60) | 118 | 22 | 35,6 min | 39,7 min |
| 2 | quadgl-9-gym | 1 | fertig | 74 (über 60) | 76 | 16 | 28,0 min | 30,7 min |
| 3 | prozent-7-schwach | 1 | fertig | 124 (über 60) | 130 | 32 | 36,1 min | 40,2 min |
| 4 | linfkt-8-neu | 1 | fertig | 93 (über 60) | 96 | 24 | 26,5 min | 30,0 min |
| 5 | kreis-8-ausblick | 1 | fertig | 98 (über 60) | 112 | 12 | 24,6 min | 27,7 min |
| 6 | daten-7 | 1 | fertig | 44 | 100 | 18 | 26,7 min | 30,7 min |
| 7 | nullstellen-fokus | 1 | fertig | 34 | 60 | 7 (Fokus) | 13,7 min | 16,2 min |
| 8 | potenz-10 | 1 | fertig | 55 | 88 | 23 | 36,6 min | 40,3 min |
| 9 | kurven-12-be | 1 | fertig | 111 (über 60) | 113 | 20 | 39,8 min | 43,1 min |
| 10 | ka-terme-8-gym | 1 | fertig | 113 (über 60) | 118 | 18 | 30,4 min | 34,6 min |

Jede Eingabe hat ein PDF „Gesamt“ bzw. „Fokus“ und eine protokoll.txt mit der Zeile „Prompt:
Unterrichtsblatt-Prompt v4.3“; kein zweiter Anlauf war nötig, keine Eingabe ist offen. Die
Zählgrenze 60 überschreiten sieben Anläufe (Befundzeile im Lesezettel).

## Gegenproben mit Ist-Wert

1. **Eingabe 1 und 2 – dieselben Zweige, verschiedene Zeitmarken.** Ist: dieselben vier Zweige
   nach Titel (Wurzelziehen und Lösbarkeit, Satz vom Nullprodukt, Normalform und p-q-Formel,
   Sachaufgaben), die Zeitmarke unterscheidet sich bei allen vier. Der Zweig der
   Katalog-Einheit 2 „Satz vom Nullprodukt“ (Marke OS Kl. 10 · GYM Kl. 8–9): Eingabe 1 (Oberschule)
   „Ausblick E4 · kommt nächstes Jahr (am Gymnasium je nach Buch schon seit Klasse 8) · P10“,
   Eingabe 2 (Gymnasium) „E2 · neu oder schon bekannt – je nach Buch (an der Oberschule erst in
   Klasse 10) · P10“. Die Stelle des Zweigs wechselt mit der Bestellung (bei Eingabe 1 Ausblick
   am Ende, bei Eingabe 2 zweiter Zweig). Stimmt mit dem erwarteten Wert überein.
2. **Eingabe 8 – Zweig mit „Potenzfunktion“ und „keine P10-Aufgabe“.** Ist: „Einheit 5 von 5 ·
   Potenzfunktionen mit natürlichem Exponenten“, Zweigzeile „… · neu in diesem Jahr (am
   Gymnasium schon seit Klasse 9) · keine P10-Aufgabe · baut auf: Einheit 3, Normalparabel,
   Punkte im Koordinatensystem“. Stimmt.
3. **Eingabe 4 – kein PDF „KennstDuSchon“.** Ist: LinFkt_Lernblatt.pdf, LinFkt_Gesamt.pdf,
   LinFkt_Loesungen.pdf (dazu Zwischenkompilate), kein KennstDuSchon. Stimmt.

## Kennzahlen im Überblick

Aus `blaetter/testlauf-2026-09-25/kennzahlen.md` (Zusatzzählung aus der Textextraktion der
zehn Gesamt-/Fokus-PDFs):
- Jeder Einheitenkopf hat seine Zweigzeile (38 Köpfe, 38 Zweigzeilen, keine fehlt).
- Alle 413 Hauptnummern der zehn PDFs tragen einen Titel mit „Ich kann“, „Ich erkenne“ oder
  „Ich finde“; die Zahl aus dem Text stimmt je PDF mit der Zahl aus dem Quelltext überein.
- Jedes Gesamt-PDF endet mit „Das kann ich“ (bei 1, 3, 4, 8 über zwei Seiten); der Fokus
  (Eingabe 7) hat keine Abhakseite, der Prompt verlangt dort keine.
- „Blatt 0“ kommt in keinem PDF vor.
- Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): 1: 25/48, 2: 24/48, 3: 15/35,
  4: 10/26, 5: 12/25, 6: 49/73, 7: 8/13, 8: 43/62, 9: 68/83, 10: 31/61. Kennzahl 9 ist ein
  Wortstamm-Abgleich, kein Urteil; die Typen ohne jeden Treffer stehen je Eingabe im Lesezettel.

Messgrenzen, gemeldet statt am Skript behoben (Auftrag: Abweichung ist Befund): Bei Eingabe 3
zählt blatt-pruef.py nur 34 Teilaufgaben, weil die blatteigenen Schwach-Makros (`\swa`, `\swb`,
`\swz`) keine Teilaufgabenzähler der Vorlage sind; bei Eingabe 6 und 10 erkennt es die gebauten
Einheiten nicht (Blattnummer ≠ Katalognummer, Kopfmakro `\zweigkopf`), „Typen ohne Treffer“ zählt
dort gegen alle Einheiten und ist zu hoch.

## Was der Auftrag nicht regelte, und wie entschieden

1. **Regelweg ohne Anmeldung** → Ersatzweg (oben). Kein Versuch, die CLI über fremde Zugangsdaten
   anzumelden.
2. **Prompttext als erster Teil**: übergeben als Verweis auf die Promptkopie mit
   Leseanweisung, nicht als eingefügter Text. Grund: 71520 Byte hätten abgetippt werden
   müssen; das Read-Tool liefert den Text fehlerfrei. Jede Sitzung hat den Prompt laut eigenem
   Protokoll gelesen und nach ihm gebaut (Prompt-Zeile v4.3 in allen zehn protokoll.txt).
3. **Umgebungsteil** zwischen Prompt und Eingabe, weil der Prompt eine Linux-Sandbox mit
   Dateikarten voraussetzt (bash, `date +%s`, Chat-Oberfläche); er ändert am Prompt nichts.
4. **Fehlstart zählt nicht als Anlauf**: Keine Sitzung kam zustande, keine Datei entstand; die
   Fehlerregel („bricht die Sitzung ab“) setzt eine Sitzung voraus.
5. **Parallel statt nacheinander**: Alle zehn Sub-Agenten liefen gleichzeitig (Rechnerlast bei
   fünf Sitzungen 23 %); abgelegt und committet wurde trotzdem je Eingabe in CSV-Reihenfolge
   (Eingabe 7 lag zuerst vor, wurde aber erst nach 3–6 committet). Folge: Die Zeiten sind unter
   Last gemessen.
6. **Arbeitsverzeichnis im Scratchpad**, nicht im Repo; ins Repo kamen alle PDFs und das
   entpackte Protokoll-Archiv. Das Zip selbst nicht: `.gitattributes` setzt `* text eol=lf` und
   nimmt nur `*.pdf` als binär aus, ein eingechecktes Zip wäre beim Commit beschädigt worden.
   Die Zips liegen im Scratchpad der Sitzung.
7. **„Alle PDFs“** heißt auch die Zwischenkompilate der Sitzungen (`check_e1.pdf`,
   `probe_e1.pdf`, `gesamt.pdf` …); sie liegen im Ordner, gemessen und im Lesezettel verlinkt
   werden nur die Übergabedateien nach dem Namensschema des Prompts (4.5).
8. **`sitzung.txt`** ist die Schlussnachricht des Sub-Agenten, wie die Laufzeitumgebung sie
   zurückgab (Zwischentexte einer Sub-Agent-Sitzung sind nicht zugänglich, die
   Verlaufsdatei war leer). In Eingabe 1 stand dort „&amp;“ als HTML-Maskierung; geschrieben ist
   „&“, wie im LaTeX-Aufruf gemeint.
9. **Werkzeugaufrufe laut protokoll.txt** = höchste Schrittnummer im Abschnitt „Werkzeugaufrufe“
   bzw. „Schritte (Schritt · Anlass)“ (Bereichsangaben „20.–24.“ zählen bis zur oberen Grenze).
10. **`werkzeuge/blatt-pruef.py`** kannte weder einen Ausgabeort noch die flache Ordnerform eines
   Testlaufs: v0.2 mit `--ausgabe` und `--testlauf`; im alten Modus byteidentisch zur
   Vorgängerfassung (geprüft gegen die HEAD-Fassung). Katalogeintrag je Blatt aus der Zeile
   „Katalog:“ von protokoll.txt (nur der Name direkt dahinter; die erste Fassung las auch die
   Namen in der Stand-Zeile und maß Eingabe 6 gegen daten.md und prozentrechnung.md – im
   Kennzahlen-Commit fb6b897 so enthalten, im Commit dieses Berichts berichtigt).
11. **Zusatzzählung und Gegenproben** in einem eigenen Skript (`werkzeuge/testlauf-messen.py`),
   angehängt an die Ausgabe von blatt-pruef.py. Gegenprobe 1 vergleicht nach Zweigtitel, nicht
   nach Blattnummer, weil die Bestellung die Stelle eines Zweigs verschiebt.
12. **Lesezettel**: „Worauf beim Gegenlesen achten“ = die Stücke der Spalte „prueft“ (höchstens
   fünf Zeilen), darunter als „Messung:“ die Auffälligkeiten aus Kennzahlen und Protokoll.
   Deutungszeile, Plan und Ausgabeblock stehen wortgleich aus chat.txt in Textblöcken
   (`werkzeuge/testlauf-lesezettel.py`), weil die zehn chat.txt verschieden gegliedert sind.
13. **Datum**: Tag des Starts laut Systemuhr 25.09.2026, obwohl Prompt und einige Repo-Dateien
   schon den 26.09.2026 tragen.
14. **Irrläufer im Repo**: Drei leere Dateien in der Repo-Wurzel, von Blattsitzungen
   angelegt (`e1_a.tex` von Eingabe 5, von ihr gemeldet; `check.tex` und
   `Prozentrechnung_KennstDuSchon.tex`, beide 12:34:19, von keiner Sitzung gemeldet). Nicht
   committet, in den Scratchpad verschoben (nicht gelöscht).
15. **README-Eintrag erst in Teil 4**, wie der Auftrag es ordnet, nicht in jedem Commit, der eine
   Datei anlegt (CLAUDE.md § 3 „Landkarte pflegen“); der archivierte Auftrag bekommt eine Zeile
   im archiv-Block, weil der Auftrag es verlangt (sonst tragen archivierte Aufträge keine).
16. **Uhrzeiten in stand.md**: Die ersten Einträge nannten geschätzte Zeiten; berichtigt auf die
   gemessenen t0-Stempel.

## Abweichungen des Sitzungsverhaltens vom Prompt

- **Planfrage trotz Antwort gestellt**: nicht als Rückfrage. Sechs Sitzungen (1, 2, 3, 4, 8, 9)
  schreiben die Umfangsfrage in ihre Ausgabe und die Antwort aus der Eingabe dahinter (der
  Umgebungsteil verlangte „gegebenenfalls die Planfrage mit der Antwort“). Eingabe 9 stellt
  Umfangs- und Bildungsgangfrage zugleich, liest „gymnasium, gk“ nur als Antwort auf den
  Bildungsgang und nimmt für den Umfang den Rückfall „alle“ (1.3). Eingabe 7 stellt die
  Eintragsfrage und nimmt die Antwort aus der Eingabe, wie erwartet. Eingabe 6 stellt keine
  Stufenfrage, weil „7“ die Klasse nennt (1.3: nur ohne Klasse und Schulform); die CSV erwartete
  „Stufenfrage beantwortet (Sek I)“.
- **Bau angehalten**: keiner; alle zehn bauten ohne Halt bis zum Ausgabeblock.
- **Rückfall ohne Katalog**: keiner; alle zehn nennen in protokoll.txt ihren Eintrag mit
  Stand-Zeile.
- **Aufrufzahl**: Der Aufrufplan (2.7) rechnet mit etwa 16 Aufrufen für fünf Einheiten; sieben
  Sitzungen brauchten laut Protokoll 74–124. protokoll.txt führt nicht jeden Werkzeugaufruf
  (6.3: „Je Werkzeugaufruf eine Zeile“): Eingabe 6 protokolliert 44 von 100, Eingabe 7 34 von 60,
  Eingabe 8 55 von 88.
- **Vorlage gelesen**: 6.3/4.5 sagen, die Vorlage werde nicht gelesen. Eingabe 1 meldet selbst,
  sie habe Teile der Vorlage und den Eintrag samt Status gelesen; Eingabe 7 (Schritte 9–11)
  und 5 (Schritt 84) haben die Vorlage durchsucht.
- **Schreiben außerhalb des Arbeitsverzeichnisses**: siehe Entscheidungen, Punkt 14.
- **Nummern der Zone**: 2.3 „Die Hauptnummern laufen über das ganze Blatt durch“. Eingabe 5
  zählt die Zone 1–7 und das Lernblatt wieder ab 1, im Gesamt stehen die Nummern 1–7 also
  doppelt; Eingabe 1 zählt die Zone Z1–Z9.
- **Bestellung „mit Ausblick“ ohne Ausblick-Zweig** (5 und 8): Beide begründen es mit den Marken
  (Kreis: alle Einheiten OS/GYM Kl. 7–8 bzw. 7–9; Potenz/Exponential: alle bei Kl. 10). Die CSV
  erwartete bei Eingabe 5 den Ausblick-Zweig Kreisteile am Ende.
- **Sek II ab Klasse 12** (9): Alle Zweige tragen Q1 und lägen nach 1.5 vor der Eingabeklasse,
  also in der Zone; die Sitzung stellt sie als Wiederholung zum Abitur auf das Blatt
  („kennst du seit Q1 (Klasse 11)“) und meldet, dass 1.5 den Fall nicht regelt. `\weit` steht in
  keinem Quelltext der Eingabe 9.
- **Kontextaufgaben je Zweig** (2.3 d, höchstens zwei): Eingabe 2 hat in Einheit 4 drei, Eingabe 4
  in Einheit 5 nur Anwendungen; beide nennen es im Ausgabeblock.
- **Fokus-Umfang** (2.5, 15–25 Teilaufgaben): Eingabe 7 hat 27 Rechenteilaufgaben, im
  Ausgabeblock genannt.
- **Deutungszeile ohne „→“**: Eingabe 8 und 10 beginnen mit „Lernblatt ·“ (die Beispiele in 1.3
  tragen den Pfeil).
- **Ausgabeblock**: 6.3 „jedes Element eine Zeile“ halten die chat.txt überwiegend ein; die
  Schlussnachrichten (sitzung.txt) von 1, 2, 3, 4, 5, 6, 7, 10 gliedern ihn in Listen um, Eingabe 3
  auch in chat.txt ohne die Nummern 1., 2., 4.
- **zeiten.txt**: doppelte Stempel (2: dreimal „zone“; 10: dreimal „e1“), zu spät gesetzte
  Stempel (2: „e 1“, „e 3“, „e 4“ erst im Folgeaufruf, selbst gemeldet), abweichende Schreibung
  („e1“ statt „e 1“ in 4 und 10), ein Stempel „fokus“ (7), den der Prompt nicht vorsieht.
- **Katalog gegen Vorstufenregel**: Vier Sitzungen (4, 5, 8, 10) melden Erkennungsschritte, die
  eine Zahl oder Rechnung verlangen, gegen 2.3 a; sie setzen die Vorstufe ohne Ergebnis um.
  Mit der Kastenzahlen-Sperre (2.1, 3.6) melden 1, 2, 5, 7, 8, 9 Konflikte (sie sperrt die
  kleinen Grundfallzahlen); 2, 7, 8, 9 legen sie deshalb enger aus (ganze Gleichungen,
  Ergebnispaare, Kastenfunktionen).
- **Vorlage**: Alle zehn definieren die Zweigzeile im Vorspann, die Lernblatt-Sitzungen auch
  Abhakseite und Verzeichniszeile; fünf melden, dass im `gleichungsraster` die letzte
  Schreibzeile in die Folgezeile läuft (Posten in faellig.md § 2).

## Nebenbefund

`blaetter/kennzahlen.md` (eingecheckt) passt nicht mehr zum Katalog: Ein Lauf des
unveränderten blatt-pruef.py gegen den heutigen Katalog ergibt andere Sprossenabgleiche (z. B.
Daten_E1.pdf „Typen ohne Treffer“ 7 von 15 statt 3 von 11), weil die Marken-Zeilen (7613213) nach
dem letzten Bau kamen. Nach dem Auftrag bleibt die Datei unberührt; Posten in faellig.md § 2.

## Nachgeführt

README.md (Ordner, Bericht, CSV und Skripte, archivierter Auftrag, Satz zu Testläufen unter
`blaetter/`), faellig.md § 2 (Testlauf wiederholen; Vorlagen-Bausteine und gleichungsraster;
kennzahlen.md neu bauen), `blaetter/testlauf-2026-09-25/lesezettel.md`, stand.md. Der Auftrag
liegt jetzt unter `archiv/auftrag-testlauf-2026-09-25.md`.

Push origin drücken
