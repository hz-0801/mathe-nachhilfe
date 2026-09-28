# Auftrag: Katalog-Nachzug aus den Urteilen vom 28.09.2026

Modell: Opus. Code-Tab, Ordner mathe-nachhilfe; der Nachbarordner
aufgabenbank wird in Teil 4 beschrieben (dort läuft keine zweite
Sitzung). Kein Push; die letzte Zeile des Berichts ist „Push origin
drücken“ – für beide Repos.

## Ausgangslage

Der Chat verbessereBlaetter hat am 28.09. abends alle 73 Funde aus
vorschlag-einbindung-2026-09-28.md beurteilt. Die Urteile stehen in
urteil-einbindung-2026-09-28.md (A angenommen, Ä geändert
angenommen, N abgelehnt; die acht Fälle unter „Offen“ sind
entschieden, das Urteil steht bei jedem Fund). Der Wortlaut jeder
Änderung steht in vorschlag-einbindung-2026-09-28.md unter „Ort“
und „Vorschlag“; wo das Urteil Ä sagt, gilt die Änderung aus der
Urteilsdatei vor dem Wortlaut der Vorschlagsdatei. Dieser Auftrag
setzt alles um, was A oder Ä trägt, in den Katalog (Teil 1–2), in
den Prüfungskatalog (Teil 3) und in die Regeldateien der
Aufgabenbank (Teil 4). Teil D und E der Urteilsdatei (ziel.md,
Prompts) sind nicht Gegenstand dieses Auftrags.

Was schon umgesetzt ist (nicht wiederholen): die fünf quer-Funde
Sek I (aufgabenbank f6420f0); Katalogbefund 3–8 und die Urteile vom
26.09. (Commits 72a01d3, ca7939b, 6c51f79).

Zeilennummern in der Vorschlagsdatei beziehen sich auf den Stand
808fd7c; seither ist der Katalog verändert. Suche jede Stelle über
den Sprossentext, nicht über die Zeilennummer.

## Standdatei

stand-katalog-nachzug.md in der Wurzel: nach jedem Teil eine Zeile
„Teil n erledigt, Commit <hash>“ oder „Teil n offen: <Grund>“;
Uhrzeit aus Get-Date. Ein Neustart liest sie und macht beim ersten
nicht erledigten Teil weiter. Commit je Teil, Commit-Nachricht über
`commit -F` aus einer UTF-8-Datei.

## Schritte

Teil 1 – Katalog Sek I (Teil A und die zwei K1-Funde aus Teil B)

1. Lies urteil-einbindung-2026-09-28.md ganz und
   vorschlag-einbindung-2026-09-28.md Teil A und Teil B.
2. Für jeden Fund mit A oder Ä in Teil A (lineare-gleichungen,
   binomische-formeln, brueche-dezimalzahlen, prozentrechnung,
   terme, rationale-zahlen, bruchrechnung) und die zwei K1-Funde
   in Teil B (prozentrechnung „Überschläge beurteilen“ – nach dem
   Urteil keine Sprosse, dafür nichts im Katalog; pythagoras.md
   Vorstufe der Kette Umkehrung „Satz und Umkehrung
   unterscheiden“, ebenso in winkel-dreiecke.md, wo die Kette
   dort liegt): die Sprosse, Vorstufe oder Frage an der genannten
   Stelle der Kette einfügen, in der Form des Eintrags (Pfeil-
   kette, Vorstufe mit „(Vorstufe)“, „(4×)“ bleibt am Grundfall).
3. Sonderfälle nach der Urteilsdatei:
   - binomische-formeln: keine neue Sprosse; die Vorstufe der
     Kette Faktorisieren bekommt die dritte Frage „Welche davon
     können gar kein Binom sein? – streichen“, die Sprosse „kein
     Binom erkennen und begründen“ heißt „kein Binom begründen“.
     Die Formelgestalt ist keine Katalogzeile (Lösungsform, Bank).
   - brueche-dezimalzahlen Einheit 5: Vorstufe wird „Wo
     entscheidet es sich?“ (Stelle nennen, kein Zeichen setzen);
     „Nullen anhängen“ wird eigene Sprosse direkt vor „verschieden
     viele Stellen“.
   - rationale-zahlen: nur die Sprosse „nur das Vorzeichen“ (das
     Antwortgerüst und das Teilprodukt sind Bank).
   - bruchrechnung Dividieren: Kontrolle als Sprosse nach dem
     Grundfall (Überschneidung 1 der Vorschlagsdatei).
4. Schreibform: Sprossen und Vorstufen sind außerhalb der
   Belegklammern ziffernfrei (Kastenzahlen-Sperre,
   katalog/_pruef_katalog.py). Beispiele aus der Vorschlagsdatei
   (20 − x = 13; 6x + 15 = 3 · (__ + __); 60 € sind 10 %) werden
   in Worte gesetzt, wie der Katalog es macht („zwanzig minus x
   gleich dreizehn“, „Faktor drei vorgegeben“), oder als Form
   ohne Zahl beschrieben („x steht hinter dem Minus“). Der Sinn
   der Sprosse bleibt.
5. Je geändertem Eintrag eine Zeile im Kopf unter den Änderungen:
   „- Änderungen <Datum aus Get-Date> (Urteile vom 28.09.): …“ mit
   den eingefügten Sprossen in Stichworten und dem Verweis
   „urteil-einbindung-2026-09-28.md“.
6. Prüfung: katalog/_pruef_katalog.py je geändertem Eintrag und
   katalog/_pruef_struktur.py; keine neuen Treffer gegenüber dem
   Stand vor dem Teil (vorher einmal laufen lassen und die Ausgabe
   aufheben). Ein neuer Treffer wird behoben, nicht das Skript.
7. Commit „Katalog-Nachzug Teil 1: Sek I aus den Urteilen vom
   28.09.“; Standdatei.

Teil 2 – Katalog Sek II (Teil C, alle 23 K1-Funde)

8. Für jeden K1-Fund in Teil C mit A oder Ä die Sprosse, Vorstufe
   oder Kontrollzeile an der genannten Stelle einfügen; Regeln
   wie in Teil 1 (Schritt 2, 4, 5). Sonderfälle:
   - extremalprobleme Randmaximum: als Vorrat, Klammerform
     „(Vorrat)“ wie im Eintrag üblich.
   - ableitung-und-aenderungsrate: Sprosse „Tangente mit dem
     Lineal anlegen, Steigung am Steigungsdreieck messen, dann
     rechnen und vergleichen“ mit dem Zusatz „(Grafik)“.
   - geraden Einheit 3: der Merkkasten wird zur Vier-Fall-Tafel
     (Richtungsvektoren parallel? ja/nein × gemeinsamer Punkt?
     ja/nein → identisch, echt parallel, schneidend, windschief),
     in der Kastenform des Eintrags; die Vorstufe am Quader dazu.
   - lagebeziehungen und abstaende: Kontrollzeilen („Kontrolle:
     Schnittpunkt in die Ebenengleichung einsetzen“, „Probe: der
     Lotfußpunkt erfüllt die Ebenengleichung“) als Schlusszeile der
     genannten Sprossen, keine eigene Sprosse.
9. Prüfung wie Schritt 6; Commit „Katalog-Nachzug Teil 2: Sek II
   aus den Urteilen vom 28.09.“; Standdatei.

Teil 3 – Prüfungskatalog

10. msa/msa-katalog-gym.csv, Zeile 2025-GYM-K5d: typ_neben von
    „Mantellinie Kegel bestimmen“ auf „Pythagoras Hypotenuse“
    (Urteil vom 26.09., Abschnitt 3 von
    katalog/_vorschlaege-2026-09-27.md; der Typ steht in
    msa/msa-typen.csv). Sonst nichts an der Zeile ändern; CSV-
    Form (Anführungszeichen, Trennzeichen, Zeilenende) wie die
    Nachbarzeilen. Gegenprobe: Zeilenzahl der Datei vorher und
    nachher gleich, alle anderen Zeilen byteweise unverändert
    (Vergleich mit git diff: genau eine geänderte Zeile).
11. Commit „Katalog-Nachzug Teil 3: 2025-GYM-K5d Nebentyp“;
    Standdatei.

Teil 4 – Regeldateien der Aufgabenbank (Nachbarordner
aufgabenbank; git pull --rebase dort zuerst)

12. bank.md:
    - „Mengen je Kette“: die drei fehler-Zeilen einer Einheit
      tragen verschiedene Formen (Schülerrechnung mit Fehler;
      fehlerfreie Vorlage; Serie „welche Ergebnisse können nicht
      stimmen“ oder Prüfzahl bei Gleichungen); die drei
      begruenden-Zeilen ebenso (Begründe, warum …; Aussagenserie
      wahr/falsch; Personenaussage zum häufigsten Fallstrick).
      Dazu die Pflichtelemente P1–P8 aus Teil B im Wortlaut der
      Vorschlagsdatei als je einen Punkt unter „Regeln für den
      Inhalt“ (P9, P10 nicht).
    - „Regeln für den Inhalt“, Fehler-finden: eine der drei
      Zeilen darf vier Rechnungen untereinander zeigen, genau eine
      falsch (Teil A brueche-dezimalzahlen; dieselbe Form wie P2 –
      einmal formulieren).
    - Urteilsfragen: etwa gleich viele Ja- und Nein-Lösungen;
      Urteil als erstes Wort der Lösung; eine der drei begruenden
      ohne Rechnung.
    - Feld loesung: Sachaufgabe endet mit Antwortsatz mit Einheit;
      Begründen nennt die Regel beim Namen.
    - Analytische Geometrie: Sprossen einer Kette am selben Körper
      mit festen Eckpunkten, je Variante ein Körper; das ergänzt
      den Päckchen-Punkt (Satz „was in Sek II gleich bleibt, klärt
      der erste Sek-II-Bank-Auftrag“ durch diese Regel ersetzen).
    - rationale-zahlen: Antwortgerüst „Vorzeichen: __ Betrag: __
      Ergebnis: __“ nur in den ersten zwei Varianten der Sprossen
      „Zeichen zusammenfassen gemischt“ (e2) und „plus mal minus“
      (e3) – als Regelzeile in bank.md, die Bankzeilen selbst
      ändert der Bank-Auftrag des Eintrags.
    - tangente-normale-schnittwinkel e4 Grundfall: fester Punkt,
      Winkel aus allen Lagen, 90° als Begründung „keine Steigung“
      – als Zeile in bank/tangente-normale-schnittwinkel/stand.md
      unter „Offene Punkte“, nicht in bank.md.
13. bau/sprachlauf/regeln.md:
    - Regel 6 drei Satzformen dazu: „Prüfen einer fremden
      Rechnung“, „Aussagen beurteilen“, „Ergebnisse prüfen“, und
      „Falschergebnis erklären“ (Wortlaut Vorschlagsdatei Teil B
      und quer Sek II).
    - Regel 7: Quantoren in Alltagswörtern (immer, jede, nie, es
      gibt, sicher – nicht stets, sämtliche, niemals, gewiss).
    - Neue Regel 13 Sek II: Die Frage nennt genau, was gesucht ist
      (Stelle, Funktionswert, Punkt; Winkel gegen die positive
      x-Achse oder Schnittwinkel; Wert des Integrals oder Inhalt
      der Fläche). Maßstab für Sek II: ein schwacher Schüler des
      Grundkurses.
    - Regel 12 (Schrittnamen) um die Bedingungsform Sek II
      ergänzen: „Nebenbedingung:“, „Bedingung f''(x) = 0:“; das
      Urteil steht in derselben Zeile wie die Einsetzung.
14. bau/layout-befunde.md, neue Nummern ab 56:
    - Merkkasten mit Fällen als Tafel statt Sätzen (2×2-Fälle;
      Neues gegen Bekanntes in zwei Spalten) – Ergänzung zu 54.
    - Aussagenserie: je Aussage eine Teilaufgabe a), b), c) mit
      Schreibzeile, kein Kästchen; Urteil als erstes Wort.
    - Jede Fertigkeit endet mit mindestens einer Aufgabe aus
      fehler oder begruenden zu ihren Sprossen, nicht gesammelt
      am Blattende.
    - Formelgestalt als Zwischenzeile der Lösung beim Faktorisieren
      (binomische-formeln: (2x)² + 2·2x·3 + 3² vor der Klammer).
15. Commit in aufgabenbank „Regeln aus den Urteilen vom 28.09.:
    Pflichtformen, Sek-II-Körper, Satzformen, Tafel-Merkkasten“;
    Standdatei in mathe-nachhilfe.

Teil 5 – Abschluss

16. urteil-einbindung-2026-09-28.md: unter der Kopfzeile eine
    Zeile „umgesetzt am <Datum>, Commits <hashes> (Teil 1–4);
    nicht umgesetzt: Teil D/E (ziel.md, Prompts) – Chat“.
17. faellig.md: Posten „Katalog terme: Fertigkeit ‚Term durch
    Zahl teilen‘ (K5)“ prüfen – ist sie in terme.md nach diesem
    Auftrag vorhanden, streichen und in § 4 eintragen; sonst
    stehen lassen. Neuer Posten in § 2: „aufgabenbank: Bank-
    Aufträge je geändertem Eintrag (Liste aus dem Bericht dieses
    Auftrags) nach auftrag-eintrag.md; erst Prüfstein
    lineare-gleichungen, dann parallel“, Auslöser „Abrechnung
    gemessen“, bei Chat.
18. README.md: urteil-einbindung-2026-09-28.md und
    stand-katalog-nachzug.md in der Landkarte eintragen; die noch
    fehlenden Dateien aus quellen/ (Posten in faellig.md § 2)
    im selben Zug.
19. Diesen Auftrag nach archiv/auftrag-katalog-nachzug-<Datum aus
    Get-Date>.md verschieben (Kopie plus git rm des Originals,
    kein Löschen außerhalb von git), Standdatei ebenso nach
    archiv/stand-katalog-nachzug-<Datum>.md; Commit „Katalog-
    Nachzug Teil 5: Abschluss“.

## Prüfungen

- Nach Teil 1 und 2: Zahl der eingefügten Sprossen je Eintrag
  gegen die Urteilsdatei (Sek I 12 Sprossen/Vorstufen plus die
  Vorstufenfrage binomische-formeln und die Umbenennung; Sek II
  22 Sprossen und 3 Kontrollzeilen, eine Kastenform). Abweichung
  ist ein Befund im Bericht, kein Grund zum Weglassen.
- _pruef_katalog.py und _pruef_struktur.py ohne neue Treffer.
- Teil 3: genau eine geänderte Zeile im diff.
- Teil 4: bank-pruef.py wird nicht berührt; kein Bankordner wird
  geändert außer der einen stand.md-Zeile.

## Bericht (bericht-katalog-nachzug.md in der Wurzel, committet
im Abschluss-Commit)

Erste Zeile: Modell, mit dem der Auftrag lief. Dann je Teil:
geänderte Dateien, Zahl der Sprossen, Abweichungen vom Wortlaut
der Vorschlagsdatei mit Grund (Ziffernfreiheit, Kettenform,
Kollision mit einer seit 808fd7c geänderten Stelle), Entscheidungen
ohne Regel. Liste der Katalogeinträge, die einen Bank-Auftrag
brauchen (jeder Eintrag mit neuer Sprosse), plus alle 72 Einträge
für die Pflichtformen P1–P8 als eigener Posten. Letzte Zeile:
„Push origin drücken“ (mathe-nachhilfe und aufgabenbank).

## Regeln

- PowerShell: kein Heredoc, kein sed; Dateien mit
  [System.IO.File]::WriteAllText und UTF8Encoding($false); Commit-
  Nachrichten mit Umlaut über commit -F aus einer UTF-8-Datei;
  Python nur %LocalAppData%\Programs\Python\Python312\python.exe;
  git über die git.exe von GitHub Desktop mit -c core.pager=cat.
- Nichts löschen außer über git rm/mv; nichts außerhalb der
  genannten Dateien ändern; werkzeuge/ und Marken nicht anfassen
  (neue Sprossen bekommen keine Marken; marken-bau.py läuft nicht).
- Zählgrenzen statt Zeitgrenzen; nach zwei Anläufen an einer
  Stelle: „offen mit Grund“ in der Standdatei, nächster Teil.
- Kein Push. Keine Rückfragen.
