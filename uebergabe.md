# Übergabe verbessereBlaetter – 2026-10-03b (Chat 03.10., Fable)

Vorherige Übergabe: archiv/uebergabe-2026-10-03.md.

## 1 Ziel

Schnell gute Blätter für die Stunde; Schwerpunkt P10 2027, zuerst
Aufgabe 1 (Basis). Drei Zettelsorten, alle aus dem Skript, nichts
im Chat erzeugt: unverändertes Originalblatt (Heftseiten),
Original-Zettel in unserer Form mit Lösungsstreifen, selbst gebauter
Basiszettel (normal und schwach). Der Gesamtablauf einer
P10-Vorbereitung (Basis, Themenhefte, Probeprüfung, Schluss mit
Originalen) ist noch nicht entschieden; bis dahin wird am Skript
gearbeitet und keine Sorte gestrichen.

## 2 Arbeitsgrundlage

- aufgabenbank (main): `werkzeuge/zusammenbau.py` v1.8 (Rezept
  Zettel v0.10: `--zettel basis [--schwach] --nummer n`; Original-
  Zettel `--zettel original --heft <jahr>-<papier>`); Basisvorrat
  `bank/_basis/` 784 Zeilen (vorrat.py → jsonl, nie von Hand),
  `schwierigkeit.csv` (Stufe 1–3 je Typ, Urteil des Lehrers,
  Entwurf vom Chat „grob passend"), `typen.csv`, `stand.md`;
  `bau/layout-befunde.md` Befund 16 (rechter Winkel);
  `bau/zettel/abgleich-2026-10-03.md`.
- aufgabenbank-privat (main, privat, hängt als zweite Karte):
  `basis-originale.jsonl` (Wortlaut Aufgabe 1 in Du-Form; bisher
  2026 FOR, 10 Zeilen), `stand.md` (je Heft eine Zeile),
  `hefte/` (14 Hefte), `heftseiten/<jahr>-<papier>-aufgabe1.pdf`
  (14 zugeschnittene Originalblätter). Das Skript erwartet das Repo
  neben aufgabenbank (oder `PRIVAT=<ordner>`) und schreibt
  Original-Zettel nur dorthin.
- blattbau (main): `mathblatt.sty` 2026-10-03c (rechter Winkel als
  Bogen mit Punkt, `\rwbei{A|B|C}` vor `\dreieck`, `\kaestchen`,
  Dreiecklabels vom Schwerpunkt weg); `Anleitung_mathblatt.md`;
  `bankblatt.md` v5.4.
- mathe-nachhilfe: `msa/msa-katalog-basis.csv` (136 Teilaufgaben,
  Gegenprobe für Lösung und Typ), `msa/handreichung-p10-2027.*`,
  faellig.md.
- Privat, nie im Repo: `Schuelerliste-privat.md` (Projektdatei in
  erzeugeBlatt(Bank)); Wortlaut der Originale nur in
  aufgabenbank-privat.

## 3 Arbeitsstand

Erledigt 03.10.: Basiszettel ins Skript nach der Vorlage vom 03.10.
(v1.5–v1.7: Form der Vorlage, Vorrat 777→784 mit 78 markierten
Originalen, 66 Vorstufen, 36 Tipps; Sortierung nach
schwierigkeit.csv, erste zwei Aufgaben Stufe 1; höchstens drei
Ankreuzen, Optionen untereinander; Figur rechts auf Aufgabenhöhe,
Felder voll lang; schwach mit Vorstufe statt Tipp; 6–10 bzw. 5–8
Aufgaben, kein Ziel 10; keine Hilfsmittelzeile); Original-Zettel
als Probe 2026 FOR (v1.8, eine Seite 12pt, Lösungen gegen Katalog
geprüft); Block 0: Hefte und Heftseiten aller 14 Jahrgänge im
privaten Repo. Lehrer hat acht Basiszettel (v1.7) und die Probe
gesehen: Form trägt.
Messwerte 03.10. mittags: Woche 85 %, Fable 87 %; Reset Montag
18:00. Agentenläufe heute: v1.5-Abschluss im Chat, v1.6 0,30 Mio,
v1.7 0,17 Mio, Probe 2026 FOR 0,20 Mio (Opus, Wochenkontingent).

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter, soweit hier nichts anderes steht.

- Du-Form überall, auch in Originalen (03.10.).
- Rechter Winkel immer Viertelkreisbogen mit Punkt, nie Quadrat;
  in jeder rechtwinkligen Figur markiert (Layoutbefund 16).
- Ankreuzen: Optionen untereinander, höchstens vier, bei
  Symmetrieachsen drei (03.10.; die zwölf Symmetrie-Varianten mit
  sechs Optionen sind noch zu kürzen).
- Keine feste Aufgabenzahl; eine Seite ist Ziel, 12pt Untergrenze;
  Original-Zettel, der nicht passt, bekommt eine Rückseite, nie
  weniger Teilaufgaben.
- Was erlaubt ist (Hilfsmittel), steht nicht auf dem Zettel.
- „Leicht" ist das Urteil des Lehrers je Typ (schwierigkeit.csv),
  nicht aus Höhe, Form oder Häufigkeit ableitbar.
- Schwach = Stufe statt Häufigkeit (drei Aufgaben Stufe 1, Stufe 3
  nur mit Vorstufe, mindestens zwei Originale mit Marke) – vom
  Lehrer „erstmal zugelassen", im Skript noch nicht umgesetzt.
- Lösungsstreifen: Voreinstellung mit Streifen; „ohne" auf Zuruf
  (Schalter noch zu bauen, Rückseite „Nr – Lösung" gibt es).
- Original-Zettel: Heftreihenfolge, keine Sortierung, keine
  Jahresmarke je Zeile, Jahr im Kopf; Figuren wie im Heft, auch
  mit rohem TikZ (nur im privaten Repo erlaubt).
- Fokusblätter für die sieben häufigen schweren Typen (Term zu
  Figur, Prozentwert, Termwert, Winkelfunktion, Lineare Gleichung,
  Pythagoras-Gleichung, Term zu Sachtext) auf Zuruf, nicht auf
  Vorrat; Rezept `--fokus` vorhanden.
- Projektdateien anderer Projekte ersetzt der Chat nicht (Browser
  scheitert an Login und Freigabe je Klick, Messwert 03.10.);
  deshalb liegt nichts Veränderliches als Projektdatei –
  mathblatt.sty und Anleitung kommen aus blattbau. Lehrer löscht
  die beiden Projektdateien in erzeugeBlatt(Bank) einmal (offen).
- Kontingent: Der Lehrer entscheidet über den Verbrauch; der Chat
  nennt Zahlen und Schätzungen, hält nichts zurück.
- Modellwahl nächste Phase: Opus im Chat und für Agenten.

## 5 Offene Punkte und Verworfenes

- Löschen der Projektdateien mathblatt.sty und
  Anleitung_mathblatt.md in erzeugeBlatt(Bank) (Lehrer).
- Handy: ob die Repo-Karte in der Handy-App erscheint, ist
  ungemessen; erster Blatt-Chat vom Handy ist der Messwert.
- Gesamtablauf P10 (Basis, Themenhefte nach Handreichung,
  Probeprüfung, Schluss mit Originalen) – entscheiden, bevor eine
  Zettelsorte gestrichen wird.
- Skript: schwach nach Stufe (oben), Streifen-Schalter, Symmetrie
  drei Optionen, Eintragsaufgabe statt Ankreuzen bei Zahlen.
- Kerntypen-Regel 30 % bleibt nur als Log-Hinweis (Übergang).
- Verworfen: Original-Zettel mit Vorstufen gemischt (verwischt
  Prüfung und Übung); Stufe aus Höhe/Form/Häufigkeit ableiten
  (zweimal gescheitert); Projektdateien über den Browser
  ersetzen.

## 6 Nächster Arbeitsschritt

Ein Opus-Agent, tokensparend: alle 13 offenen Hefte in einem Lauf
erfassen (einmal lesen, alles ableiten – kein Skriptumbau, keine
Vorlage lesen, nur je Heft `heftseiten/<heft>.pdf` als Text und
Bild, 10 Zeilen nach dem Feldschema von basis-originale.jsonl,
Lösung und Typ gegen msa-katalog-basis.csv), Standdatei
`aufgabenbank-privat/stand.md` nach jedem Heft fortschreiben,
Commit je Heft, Push am Ende und nach jedem vierten Heft; nach
zwei Fehlversuchen an einem Heft „offen mit Grund", nächstes Heft.
Danach ohne Modell: `--zettel original` für alle 14 Hefte bauen,
Seitenzahl je Zettel in den Bericht. Geschätzt 0,45–0,6 Mio Token
(Messwert Probe: 0,08 Mio je Heft ohne Skriptarbeit). Vorher
Anzeige ablesen, nachher wieder. Dann dem Lehrer zwei
Original-Zettel verschiedener Jahrgänge zeigen und die Sorten
„unverändertes Originalblatt / Original-Zettel / Basiszettel" am
Tisch erproben.
