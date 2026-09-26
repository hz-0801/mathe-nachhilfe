Modell der Auftragssitzung: Claude Opus 5.5 (claude-opus-5-5) · Modell der Blattsitzungen: Sub-Agent mit model „opus“, laut Sitzungsprotokoll und protokoll.txt aller zehn Sitzungen Opus 5.5 (claude-opus-5-5)

# Bericht Testlauf des Unterrichtsblatt-Prompts v4.4, 26.09.2026

Auftrag: `archiv/auftrag-testlauf-2026-09-26.md` (Grundlage `werkzeuge/testlauf-auftrag.md`).
Prompt: `hz-0801/blattbau/unterrichtsblatt.md` v4.4, Commit 36b7b12, Zeile 1 „# UNTERRICHTSBLATT v4.4 –
PROMPT FÜR LERNBLATT UND FOKUS“, Kopie `blaetter/testlauf-2026-09-26/unterrichtsblatt-v4.4.md` (79429 Byte,
byteidentisch mit ../blattbau). Katalog live von raw.githubusercontent.com (origin/main 68a6401, Katalog
lokal gleich). Vorlage in allen Sitzungen mathblatt.sty 2026-09-28a. Datum des Laufs 2026-09-26 (Start
19:23 laut Get-Date); die letzte Eingabe endete nach Mitternacht, alle Namen tragen das Startdatum.

Commits: f957238 Teil 0, c3e9781 Teil 1, e3d3ed2 · 652c0bb · b04f85c · 61266dd · 6c99d97 · 46dd53b ·
d0b0bb4 · e6cc682 · f07f6c0 · cf61ad8 je Eingabe (1–10), e185b4a Teil 3, dazu der Commit dieses Berichts.

## Je Teil, was geändert ist

- **Teil 0** (f957238): `werkzeuge/testlauf-eingaben.csv` Spalte „prueft“ bei Eingabe 5 und 6 nach dem
  Auftrag ersetzt; `werkzeuge/testlauf-auftrag.md`: „v4.3“ an drei Stellen durch „die Version aus Zeile 1
  von unterrichtsblatt.md, die der Auftrag nennt“, Pfad der Beigabe
  `%LocalAppData%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude-code\<version>\claude.exe`,
  Spalte „Aufrufe (Umgebung)“ in Teil 4 verlangt, Änderungsvermerk im Kopf; `faellig.md` Posten Werkzeug 1
  und 3 nach § 4. Der Auftrag selbst (`auftrag-testlauf.md`) wurde mit eingecheckt, damit Teil 4 ihn mit
  `git mv` verschieben kann. Zwei Fehler meines Edits in der CSV, erst in Teil 4 bemerkt und dort behoben
  (Entscheidung 8).
- **Teil 1** (c3e9781): Prompt geholt (Zeile 1 v4.4), Werkzeuge geprüft (xelatex MiKTeX-XeTeX 4.16,
  pdftotext, pdfinfo, pdftoppm, Python 3.12.10, curl 8.21.0; sympy 1.14.0 und pypdf 6.19.0 per
  `pip --target` in den Scratchpad), Ordner und `stand.md`; `werkzeuge/testlauf-ablage.py` v0.2 nimmt die
  Prompt-Version als Argument.
- **Teil 2** (zehn Commits): je Eingabe ein Sub-Agent, nacheinander; Ablage mit `testlauf-ablage.py`,
  `sitzung.txt` und `aufrufe.txt` mit dem neuen `werkzeuge/testlauf-verlauf.py` aus dem Sitzungsprotokoll.
- **Teil 3** (e185b4a): `kennzahlen.md` aus `blatt-pruef.py --testlauf … --ausgabe …`, Zusatzzählung
  (`testlauf-messen.py` v0.2), Tabelle v44-pruefung, Vergleich v4.3 gegen v4.4 und Gegenproben (neu:
  `werkzeuge/testlauf-pruefung.py`). `blaetter/kennzahlen.md` unberührt (Hash vor und nach gleich).
- **Teil 4** (dieser Commit): `lesezettel.md` (`testlauf-lesezettel.py` v0.2), dieser Bericht, README
  (Ordner, Bericht, Skripte, Auftrag im Archiv), `faellig.md` § 2 (die zwei Posten des Auftrags, ein Posten
  zur CSV-Zeile 3, Auslöser eingetreten an zwei Posten, Zusatz Zonen-Kopfzeile am Posten Vorlage Stufe 7),
  Auftrag nach `archiv/auftrag-testlauf-2026-09-26.md`. `kennzahlen.md` ist in diesem Commit neu gebaut
  (Punkt g erkennt jetzt auch fehlende Stempel, Punkt e auch klein geschriebene Rahmendateien).

## Bauweise

**Ersatzweg.** Der Regelweg ist seit dem 25.09. technisch da: Die Beigabe (Version 2.1.281) liegt unter
dem neuen Pfad, der Probeaufruf `claude -p "Antworte mit OK" --model opus` antwortete „OK“ (Exitcode 0),
`--append-system-prompt[-file]`, `--dangerously-skip-permissions`, `--model` und `--output-format
stream-json` sind bekannt. Das Startskript für die zehn Blattsitzungen (`claude -p` mit
`--append-system-prompt-file` und `--dangerously-skip-permissions`) hat aber der Berechtigungsklassifikator
der Auftragssitzung abgelehnt („Create Unsafe Agents“). Eine Umgehung (andere Optionen, anderes Werkzeug)
wäre dasselbe Ergebnis auf anderem Weg gewesen; ich habe keine versucht. Damit galt der Regelweg als nicht
verfügbar. Soll er beim nächsten Lauf gehen, braucht die Auftragssitzung dafür eine Freigabe des Lehrers
(Berechtigungsregel in den Einstellungen).

Je Eingabe ein Sub-Agent (general-purpose, model opus), Nachricht nach `werkzeuge/testlauf-umgebung.md`:
Teil 1 Verweis auf die Promptkopie im Scratchpad mit der Anweisung, sie ganz zu lesen und nach ihr zu
arbeiten, Teil 2 Umgebung (Windows, PowerShell, Pfade, Arbeitsverzeichnis im Scratchpad, Repo nicht
anfassen, keine Sub-Agenten), Teil 3 die Eingabezeile mit „ – Antworten auf Planfrage und Zone:
<antworten>; baue ohne Halt bis zum Ausgabeblock durch“. Keine Nachricht wurde von der API abgelehnt.
Die Sitzungen liefen nacheinander; die nächste startete erst nach Ablage und Commit der vorigen.

## Ergebnis je Eingabe

Zeit = t0 bis zum letzten Stempel in `zeiten.txt`. „Aufrufe (Umgebung)“ = Werkzeugaufrufe im
Sitzungsprotokoll des Sub-Agenten (`~/.claude/projects/…/subagents/agent-<id>.jsonl`, gezählt von
`testlauf-verlauf.py`, Liste in `aufrufe.txt` je Ordner); die Zahl stimmt bei allen zehn mit „tool_uses“
in der Endmeldung der Laufzeitumgebung überein und enthält den Übergabeaufruf der Schlussnachricht
(`SubagentHandback`, je Sitzung einer). „Dauer (Umgebung)“ aus derselben Endmeldung.

| Nr. | Kurzname | Anläufe | Ergebnis | Werkzeugaufrufe laut protokoll.txt | Aufrufe (Umgebung) | Seiten Gesamt | Zeit laut zeiten.txt | Dauer (Umgebung) |
|---|---|---|---|---|---|---|---|---|
| 1 | quadgl-9-os | 1 | fertig | 78 (über 60) | 80 | 26 | 26,1 min | 29,0 min |
| 2 | quadgl-9-gym | 1 | fertig | 76 (über 60) | 77 | 23 | 26,1 min | 29,5 min |
| 3 | prozent-7-schwach | 1 | fertig | 107 (über 60) | 109 | 37 | 22,4 min | 26,2 min |
| 4 | linfkt-8-neu | 1 | fertig | 119 (über 60) | 120 | 23 | 27,0 min | 29,8 min |
| 5 | kreis-8-ausblick | 1 | fertig | 95 (über 60) | 97 | 15 | 20,8 min | 26,5 min |
| 6 | daten-7 | 1 | fertig | 55 | 58 | 18 | 18,6 min | 22,9 min |
| 7 | nullstellen-fokus | 1 | fertig | 37 | 39 | 8 (Fokus) | 8,8 min | 11,6 min |
| 8 | potenz-10 | 1 | fertig | 87 (über 60) | 88 | 24 | 26,8 min | 29,3 min |
| 9 | kurven-12-be | 1 | fertig | 80 (über 60) | 82 | 19 | 28,9 min | 33,3 min |
| 10 | ka-terme-8-gym | 1 | fertig | 80 (über 60) | 81 | 22 | 24,1 min | 27,0 min |

Jede Eingabe hat ein PDF „Gesamt“ bzw. „Fokus“ und eine protokoll.txt mit der Zeile „Prompt:
Unterrichtsblatt-Prompt v4.4“; kein zweiter Anlauf, keine Eingabe offen. Die Zählgrenze 60 überschreiten
acht Anläufe (Befundzeile im Lesezettel).

## Gegenproben mit Ist-Wert

1. **„Eingabe 1 und 2: dieselben Zweige, verschiedene Zeitmarken (katalog/quadratische-gleichungen.md,
   Marken Einheit 2: OS Kl. 10, GYM Kl. 8–9).“** Ist: dieselben vier Zweige nach Titel (Wurzelziehen und
   Lösbarkeit, Satz vom Nullprodukt, Normalform und p-q-Formel, Sachaufgaben); die Zeitmarke unterscheidet
   sich bei allen vier. Satz vom Nullprodukt: Eingabe 1 „Ausblick E4 · kommt nächstes Jahr (am Gymnasium
   schon in Klasse 8 oder 9) · P10“, Eingabe 2 „E2 · neu oder schon bekannt – je nach Buch (an der
   Oberschule erst Kl. 10) · P10“. Stimmt. Dabei: Eingabe 1 baut „mit Ausblick“, Eingabe 2 „ohne
   Ausblick“ – beide lesen dieselbe Registerzeile verschieden (Abweichungen, erster Punkt).
2. **„Eingabe 4: kein PDF ‚KennstDuSchon‘.“** Ist: LinFkt_Gesamt.pdf, LinFkt_Lernblatt.pdf,
   LinFkt_Loesungen.pdf (dazu zehn Prüfkompilate e1_test.pdf …), kein KennstDuSchon. Stimmt.
3. **„Eingabe 5: Deutungszeile nennt ‚mit Ausblick‘ ohne Zweig (CSV nach Teil 0).“** Ist: „→ Lernblatt
   · Kl. 8, Oberschule als Standpunkt (Gymnasium mit gleichen Marken) · mit Wiederholung · mit Ausblick:
   kein Zweig nach Kl. 8 · 3 Zweige · Zone aus 6 Fertigkeiten“; Ausblick-Zweige im PDF: 0. Stimmt.
4. **„Eingabe 8: ein Zweig mit ‚Potenzfunktion‘ und ‚keine P10-Aufgabe‘.“** Ist: „Einheit 5 von 5 ·
   Potenzfunktionen mit natürlichem Exponenten“, Zweigzeile „… · neu in diesem Jahr (am Gymnasium schon
   seit Klasse 9) · keine P10-Aufgabe · baut auf: Potenz mit dem Taschenrechner, Punkte eintragen,
   Normalparabel“. Stimmt.
5. **„Eingabe 9: kein Zweig liegt in der Zone; die Zweige tragen eine Zeitmarke mit ‚Q1‘
   (unterrichtsblatt.md v4.4, 1.5).“** Ist: fünf Zweige im PDF bei fünf Lerneinheiten im Eintrag; die Zone
   (Nr. 1–8) trägt nur Voraussetzungen (Ablesen, Gleichungen lösen, Ableiten, Punktprobe, Skizzieren,
   Ableitung deuten); Zeitmarken viermal „kennst du seit Q1“, einmal „kennst du seit Q1 oder Q2 – je nach
   Buch“ (Einheit 4). Stimmt. (v4.3: alle Zweige als Wiederholung, Zeitmarke „kennst du seit Q1 (Klasse
   11)“.)
6. **„Eingabe 7: Zweigkopf ohne ‚von‘ (v4.4, 2.5).“** Ist: S. 2 „Einheit 4 · Nullstellen und
   Schnittpunkte berechnen“, kein „von“. Stimmt.

## Tabelle v44-pruefung

Aus `blaetter/testlauf-2026-09-26/kennzahlen.md` (Lesarten im Kopf von `werkzeuge/testlauf-pruefung.py`;
Quelltext = Rahmendatei des Gesamt- bzw. Fokus-PDFs mit allen `\input`).

| Eingabe | a) \rechenplatz | a) beispiel (Soll 0) | b) Seite „Inhalt“ (Soll nein) | b) \verzeichniszeile (Soll ja) | c) Nummern durchlaufend (Soll ja) | c) „Z1“ (Soll nein) | d) \verfahren | d) \anweisung | e) Nachbau (Soll 0) | f) „→“ (Soll ja) | g) zeiten.txt (Soll ja) | h) P10-Marken / mit Papier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1-quadgl-9-os | 10 | 0 | nein | Gesamt ja · Lernblatt ja | ja (Zone 1–11, 1–55) | nein | 12 | 11 | 0 | ja | ja | 8 / 8 |
| 2-quadgl-9-gym | 13 | 0 | nein | Gesamt ja · Lernblatt ja | ja (Zone 1–11, 1–49) | nein | 11 | 7 | 0 | ja | nein (fehlt: weiter) | 7 / 7 |
| 3-prozent-7-schwach | 3 | 0 | nein | Gesamt ja · Lernblatt ja | ja (Zone 1–11, 1–54) | nein | 18 | 4 | 0 | ja | ja | 5 / 5 |
| 4-linfkt-8-neu | 6 | 0 | nein | Gesamt ja · Lernblatt ja | ja (keine Zone, 1–53) | nein | 22 | 2 | 0 | ja | ja | 16 / 16 |
| 5-kreis-8-ausblick | 0 | 0 | nein | Gesamt ja · Lernblatt ja | ja (Zone 1–9, 1–43) | nein | 9 | 14 | 0 | ja | ja | 3 / 3 |
| 6-daten-7 | 1 | 0 | nein | Gesamt ja · Lernblatt ja | ja (Zone 1–11, 1–37) | nein | 5 | 9 | 0 | ja | ja | 5 / 5 |
| 7-nullstellen-fokus | 2 | 0 | nein | Fokus nein (kein Soll) | ja (Zone 1–5, 1–19) | nein | 2 | 4 | 0 | ja | ja | 3 / 3 |
| 8-potenz-10 | 0 | 0 | nein | Gesamt ja · Lernblatt ja | ja (Zone 1–12, 1–69) | nein | 9 | 14 | 0 | ja | nein (fehlt: e 1) | 11 / 11 |
| 9-kurven-12-be | 0 | 0 | nein | Gesamt ja · Lernblatt ja | ja (Zone 1–8, 1–44) | nein | 10 | 29 | 0 | ja | ja | 0 / 0 (Sek II) |
| 10-ka-terme-8-gym | 10 | 0 | nein | Gesamt ja · Lernblatt ja | ja (Zone 1–9, 1–48) | nein | 8 | 45 | 0 | ja | ja | 3 / 3 |

Zu e): Kein Blatt definiert einen Baustein neu, dessen Name in der Anleitung steht. Eigene Definitionen
mit anderem Namen (Auskunft, je Blatt in kennzahlen.md): 1 `\quadratrand`, 2 `\rechteckrand`, 3
`\abhakverf` (zweite Gruppenebene der Abhakseite), 4 `\vgruppe` (dasselbe), 5 `\zeichenplatz` und
`\zonekopf` (Ersatz für den Zonenkopf), 8 `\leeresgitter`, 9 `\zonekurz`, 10 `\flaechenbild`; dazu `\def\mitzone`
in 1 und 3 als Schalter. Zu h): Das Papier steht an allen 61 P10-Marken; Eingabe 2 schreibt überall „FOR“
(im Ausgabeblock: „Papier der OS-Originale als FOR angenommen“), die übrigen Sek-I-Blätter „OS“ (bei
Originalen mit FOR- oder GYM-Kennung diese).

## v4.3 gegen v4.4

Aus der Vergleichstabelle in `kennzahlen.md` (links Lauf 25.09., parallel; rechts dieser Lauf, nacheinander):
Die Seitenzahl des Gesamt- bzw. Fokus-PDFs ist bei sieben Eingaben gestiegen (am stärksten Eingabe 2 von 16
auf 23 und Eingabe 1 von 22 auf 26), bei Eingabe 4 und 9 um eine Seite gesunken, bei Eingabe 6 gleich
geblieben. Die Zahl der Hauptnummern ist bei neun Eingaben gestiegen (Eingabe 8 von 51 auf 69, Eingabe 1 von
42 auf 55) und bei Eingabe 9 von 47 auf 44 gesunken. Die Werkzeugaufrufe laut protokoll.txt summieren sich
auf 814 gegen 859, die laut Umgebung auf 831 gegen 1011; der Abstand zwischen beiden Zählungen liegt je
Sitzung bei 1 bis 3 gegen bis zu 56 am 25.09. Acht Sitzungen überschreiten die Zählgrenze 60 (am 25.09.
sieben). Die Zeit laut zeiten.txt ist bei neun Eingaben kürzer, bei Eingabe 4 länger (27,0 gegen 26,5 min).
Die heutige Fassung von blatt-pruef.py zählt bei Eingabe 3 des 25.09. 173 statt 34 Teilaufgaben (Schwach-
Zähler seit v0.4); der Vergleich 34 → 185 ist deshalb kein Vergleich gleicher Messung.

## Was der Auftrag nicht regelte, und wie entschieden

1. **Regelweg abgelehnt** → Ersatzweg (Bauweise). Der Probeaufruf ohne `--dangerously-skip-permissions`
   lief; die Ablehnung betraf den Start der Blattsitzungen.
2. **Nachricht an die Sub-Agenten** wortgleich nach `testlauf-umgebung.md` wie am 25.09., damit die Läufe
   vergleichbar bleiben; die Eingabezeile steht als dritter Teil und endet wie verlangt.
3. **„Aufrufe (Umgebung)“** aus dem Sitzungsprotokoll des Sub-Agenten, nicht aus der Ausgabedatei
   (`tasks/<id>.output` blieb wie am 25.09. leer). Neues Skript `werkzeuge/testlauf-verlauf.py`, Liste je
   Ordner in `aufrufe.txt`. Der Übergabeaufruf der Schlussnachricht zählt mit, weil die Laufzeitumgebung
   ihn mitzählt.
4. **`sitzung.txt`** = alle Textblöcke der Sitzung und die Schlussnachricht aus dem Sitzungsprotokoll
   (am 25.09. nur die Schlussnachricht). Bei Eingabe 3 kam die Schlussnachricht nur als Übergabeaufruf; das
   Skript nimmt sie seitdem mit, `sitzung.txt` von 1 und 2 wurde damit neu erzeugt (Commit b04f85c).
5. **Arbeitsverzeichnis im Scratchpad**, ins Repo PDFs und entpacktes Archiv, keine Zips (wie am 25.09.).
6. **Messwerkzeuge.** Die Punkte a)–h) und die sechs Gegenproben misst ein neues Skript
   (`testlauf-pruefung.py`); `testlauf-messen.py` v0.2 erkennt den Fokus-Kopf ohne „von“ und lässt mit
   `--ohne-gegenproben` seine drei alten Gegenproben weg (am Lauf vom 25.09. misst v0.2 wortgleich wie
   v0.1, geprüft); `testlauf-lesezettel.py` v0.2 findet den Ausgabeblock auch ohne Überschrift unter der
   letzten Dateizeile (v4.4-Sitzungen schreiben keine) und schreibt die Prüfpunkte, die ihr Soll verfehlen.
   Lesarten: b) „Inhalt“ als eigene Zeile im Text oder Kopf im Quelltext; c) Nummern aus der
   Textextraktion ohne Abhakseite, Zone aus der Verzeichniszeile; e) Namen = alle `\name` und
   Umgebungen der Anleitung, geprüft in den Rahmen- und Einheitsdateien; g) auch fehlende Stempel zählen
   (Prompt 6.3: jeder Stempel genau einmal), „zone“ und „weiter“ nur mit Zone.
7. **Vergleichstabelle**: links die Werte aus den eingefrorenen Dateien, wie verlangt; die Abweichung der
   heutigen Messung (Eingabe 3) steht unter der Tabelle. Zusätzlich die Umgebungszahl beider Läufe.
8. **CSV nach Teil 0 berichtigt.** Mein Edit in Teil 0 hatte das Leerzeichen nach „genannt ist,“ in
   Zeile 6 verloren, und der Wortlaut für Zeile 5 enthält „; “ – das ist der Spaltentrenner der CSV, das
   Feld zerfiel in zwei Spalten. In Teil 4 berichtigt: Leerzeichen gesetzt, Feld 5 in CSV-Anführungszeichen
   (Inhalt wortgleich, `csv` liest zehn Zeilen mit fünf Spalten). Zeile 3 trägt denselben Fehler seit dem
   25.09. („; keine Sprosse fehlt gegenüber dem Katalog“ landet in einer sechsten Spalte, der Lesezettel
   zeigt das Stück nicht); nicht geändert („sonst nichts an der CSV“), Posten in `faellig.md` § 2.
9. **Irrläufer**: Eingabe 5 legte zwei leere Dateien in der Repo-Wurzel an (`Kreis_KennstDuSchon.tex`,
   `zone_a.tex`, 21:39:58); nicht committet, in den Scratchpad verschoben (nicht gelöscht).
10. **Dateien schreiben**: `stand.md` und Commit-Nachrichten mit `WriteAllText` (UTF-8 ohne BOM), die
    übrigen Dateien mit dem Write- und Edit-Werkzeug; jede geschriebene Datei auf BOM und CR geprüft (keine).
    Commit-Nachrichten mit „…“ über eine Datei aus dem Write-Werkzeug, weil das typografische
    Anführungszeichen den PowerShell-String beendet.
11. **Über Mitternacht**: Ende der Eingabe 10 um 00:00 des 27.09.; Ordner, Bericht und Archivname tragen
    das Startdatum 2026-09-26.
12. **faellig.md**: außer den zwei verlangten Posten der CSV-Posten (Punkt 8), „Auslöser eingetreten“ an
    den Posten Übersichtsblatt-Prüfstein und Blatt-Chat (beide warten auf den Testlauf v4.4) und ein Zusatz
    am Posten Vorlage Stufe 7 (Zonen-Kopfzeile). Der wiederkehrende Posten „Testlauf wiederholen“ bleibt.

## Abweichungen des Sitzungsverhaltens vom Prompt

- **Register der Blätter verschieden gelesen** (1.1): `blaetter/index.md` führt „nullstellen“ vom 22.09.
  aus quadratische-gleichungen.md. Eingabe 1 liest „Register führt das Thema nicht“ und baut mit Ausblick
  (Satz vom Nullprodukt als Ausblick-Zweig), Eingabe 2 liest „Register führt das Thema“ und baut ohne.
  Eingabe 3 und 6 bauen ohne Ausblick, weil das Register ihr Thema führt; 5, 8, 9, 10 nennen „mit
  Ausblick: kein Zweig nach Kl. n“.
- **Planfrage**: Die Umfangsfrage steht mit der Antwort aus der Eingabe bei 1, 2, 3, 4, 8 und 9; keine bei
  5 und 6 (weniger als vier Zweige) und 10 (Klassenarbeit); Eingabe 7 stellt die Eintragsfrage und nimmt
  die Antwort. Eingabe 6 stellt keine Stufenfrage (wie die CSV jetzt erwartet). Eingabe 9 stellt Umfangs-
  und Bildungsgangfrage zugleich, liest „gymnasium, gk“ als Bildungsgang und nimmt für den Umfang den
  Rückfall „alle“ (wie am 25.09.).
- **Bau angehalten, Rückfall ohne Katalog**: keiner.
- **Eintrag über 2.1 hinaus gelesen**: 1, 2, 7 und 8 lasen „Offene Punkte“ und „Prüfliste“ mit (selbst
  gemeldet); 8 übernahm daraus die Schreibweise N(t) = N₀ · qᵗ.
- **Aufrufzahl**: Der Aufrufplan (2.7) rechnet mit etwa 16 Aufrufen für fünf Einheiten; acht Sitzungen
  brauchten 76–119 laut Protokoll. protokoll.txt führt jetzt fast jeden Aufruf (Abstand zur Umgebung 1–3).
- **zeiten.txt** (6.3): Eingabe 2 setzt keinen Stempel „weiter“, Eingabe 8 keinen „e 1“; Eingabe 1 setzt
  t0 im selben Aufruf wie das Anlegen des Verzeichnisses und „weiter“ als Simulation; Eingabe 4 setzt „e 1“
  vor der Sichtprüfung, 5 und 8 kompilieren die Zone nach dem Stempel „zone“ neu, 9 setzt „weiter“, „e 3“,
  „e 4“ verspätet, 3 setzt „e 2“ in einem eigenen Aufruf, 10 entfernte einen zu früh gesetzten Stempel
  „zone“ aus der Datei (6.3: „nie nachgetragen“; hier wurde nachträglich gelöscht). Kein Stempel doppelt,
  keiner ohne Leerzeichen.
- **Bausteine im Vorspann**: acht Sitzungen definieren eigene Makros (Tabelle oben); keines baut einen
  Baustein der Anleitung nach. Zwei ersetzen den Zonenkopf, weil `\einheitenkopf[zone][Kennst du schon]`
  die Kopfzeile verdoppelt („… · Kennst du schon · Kennst du schon“, in sieben von acht Zonen-PDFs so
  übergeben); zwei bauen eine zweite Gruppenebene der Abhakseite (`\abhakverf`, `\vgruppe`).
- **Verfahrensüberschrift** (2.3 b): Eingabe 4 setzt vor die Pflichtelemente jedes Zweigs die
  Zwischenzeile „Prüfen, begründen, anwenden“ (selbst gemeldet: „keine Verfahrensüberschrift im Sinn von
  2.3 b“); daher 22 `\verfahren`.
- **Prüfungshöhe nicht in der letzten Verfahrens-Hauptnummer** (2.4 c): Eingabe 3 (Einheit 2 und 4) und 5
  (Einheit 3) setzen das Original in eine frühere Nummer und begründen es mit dem Formzerfall der Kette.
- **Halbseitenmaß** (2.3 g): Eingabe 1 (Nr. 14, 15, 27–31) und 2 (Nr. 15, 35, 36, 40) lassen Nummern von
  etwa zwei Dritteln Seitenhöhe ungeteilt und nennen es.
- **Papier an der Prüfungsmarke** (3.6): Eingabe 2 schreibt „FOR“, wo die übrigen „OS“ schreiben, und
  meldet, der Eintrag nenne für die OS-Originale kein Papierkürzel.
- **Typen ohne Sprosse** (2.3, 5.1 b): Eingabe 9 meldet 26 von 76 Haupttypen ohne eigene Sprosse, „bei 76
  Typen nicht einlösbar“.
- **Sonstiges**: Eingabe 9 meldet, die Stand-Zeile des Eintrags trage Nachzüge vom 28. und 29.09.2026, also
  nach dem Bautag; bei Eingabe 9 lehnte das Werkzeug ein `Remove-Item` auf PNG-Dateien im
  Arbeitsverzeichnis ab (nichts verloren); Eingabe 5 schrieb zwei leere Dateien in die Repo-Wurzel
  (Entscheidung 9).
- **Ausgabeblock** (6.1, 6.3 „jedes Element eine Zeile“): In chat.txt steht er bei allen zehn ohne
  Überschrift unter den Dateinamen; 2, 7, 8 und 10 fassen mehrere Elemente mit „·“ in eine Zeile (bis zu
  acht je Zeile), die übrigen schreiben überwiegend je Element eine Zeile. Die Schlussnachrichten von 1, 2,
  5, 7, 8 und 9 hängen einen ausdrücklich so bezeichneten Abschnitt für den Aufrufer an, 3, 6 und 10 einen
  Absatz mit Ablageort und Prüfergebnis (vom Umgebungsteil nicht verlangt).

Push origin drücken
