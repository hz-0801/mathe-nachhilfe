# Übergabe verbessereBlaetter – 2026-10-01 (Chat 30.09. abends bis 01.10. mittags)

Vorherige Übergabe: archiv/uebergabe-2026-09-30b.md.

## 1 Ziel

Der bestmögliche Themenkatalog, die Aufgabenbank und die Prompts,
damit aus wenigen Wörtern druckfertige Blätter entstehen. Maßstab
ist ziel.md (28.09.) mit den Revisionen vom 01.10. (§ 4); Leitbild:
ein Blatt für alle Schüler, aus der Bank zusammengesetzt, der Chat
deutet, setzt und ergänzt.

## 2 Arbeitsgrundlage

- aufgabenbank: `bau/terme/muster-2026-10-01/muster4.tex` und
  `.pdf` – das Zielblatt (Form und Aufbau des Lernblatts, Beschluss
  des Lehrers 01.10.); `bericht.md` dort (Abschnitte Muster 1–4,
  Vorschlagsliste 30 Katalogsprossen, Zählung Bank/geändert/neu).
  `werkzeuge/zusammenbau.py` v1.2 (Lernblatt-Rezept nach vier
  Läufen, TER-L4 bis TER-L7; baut noch nicht nach Muster 4);
  `werkzeuge/zusammenbau.md` v1.2; `bau/regal/ich-kann.csv` mit
  Spalte `titel`; `bau/layout-befunde.md` mit Abschnitt „Befunde
  des Lehrers 01.10.“. Bank unverändert 15 351 Zeilen; Mappe terme
  mit Blattfolge (Katalog bbcf2d4).
- mathe-nachhilfe: `katalog/terme.md` mit Zeile „Blattfolge:
  2, 3, 4, 1“ (cd23bd9, PR #1 gemergt), `katalog/_vorlage.md` mit
  der optionalen Zeile; ziel.md 28.09. – noch ohne die Revisionen
  aus § 4 (Posten).
- Bank-Prompt v5.0 (Test 01.10.): im Chat als Block ausgegeben,
  als Projektanweisung im neuen Projekt „erzeugeBlatt(Bank)“ des
  Lehrers; noch nicht im Repo blattbau (Posten). Erster Test
  „terme“: 7 Seiten, 113 Teilaufgaben (69 Bank, 44 neu), 118
  Proben, 0 Fehler; Archiv `Terme_2026-10-01_protokoll.zip` beim
  Lehrer (neu.jsonl mit den 44 erfundenen Zeilen).
- blattbau unverändert: unterrichtsblatt.md v4.4, pruefungsblatt.md
  v0.15 bleiben eingefroren als Reserve (Beschluss 30.09.).
- anweisungen: projekt-verbessereBlaetter.md 2026-09-30,
  kandidaten.md 2026-09-30b (zwei neue Kandidaten in § 4, noch
  nicht eingetragen).

## 3 Arbeitsstand

Erledigt 30.09. abends bis 01.10.:
- Vier Skriptläufe am Lernblatt-Rezept (v0.9–v1.2: Mengen, Satz
  wie Kompetenzblatt, Auftrag einmal, Ich-kann-Titel, dann wieder
  weg; Zweigzeile weg; Test, Prüfe dich, Kästen, Dichteregeln).
  Ergebnis: Layoutregeln lösen das Blatt nicht; die Ursache lag
  in Katalog (feine Leiter, Decke P10 FOR) und fehlendem Ermessen
  des Skripts.
- Musterblatt Terme von Hand (vier Fassungen, Muster 4 ist Ziel):
  Blatt 0 halbe Seite; sechs Einheiten (Zusammenfassen, Malnehmen,
  Klammern, Ausklammern, Termwerte, Aufstellen); Merkkasten je
  Einheit (Fall – Beispiel – Ergebnis fett, „Wichtig“ als Rechnung);
  je Verfahren eine Nummer von leicht bis schwer, hinten Marken
  „P10 ’25“/„GYM“; a) vorgerechnet nur, wo es den Weg zeigt;
  Abschluss (drei Teilaufgaben) nur bei Einheiten mit mehreren
  Verfahren; „Zum Schluss“ (je Einheit eine, zwei markierte);
  Lösungen hinten, nur Ergebnis, „falsch → Nr. n“; Kopf nur Thema,
  Fuß „Seite n von m“.
- Bank-Prompt v5.0 geschrieben und vom Lehrer getestet (oben).
- Katalog: Blattfolge-Zeile für terme und Vorlage.
- Messwerte Kontingent: Woche 54 % (30.09. abends) → 58 % (01.10.
  mittags) für drei Skriptläufe à 0,4 Mio und den Chat; Fable 48 →
  51 % nur durch den Chat. Fortgesetzte Agenten (SendMessage an
  denselben Agenten) kosteten deutlich weniger als neue (Muster 2–3
  je unter 0,1 Mio geschätzt, Muster 4 als neuer Agent 0,14 Mio).

Nicht erledigt: Katalog Terme neu schneiden; Bank-Nachzug aus
Muster und Test; Skript auf Muster 4; Prompt v5.1; Nachzug der 48;
Gegenlese; kandidaten.md.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter, soweit hier nichts anderes steht.

- Drei Prompts (30.09.): Bank-Prompt als Alltagsprompt (eigenes
  Projekt), die alten beiden eingefroren als Reserve ohne Bank;
  kein Umbau der alten Prompts mehr.
- Bank-Prompt baut im Chat von Hand nach Muster 4 (01.10.): Bank-
  zeilen holen, Blatt setzen, Fehlendes erfinden, nachrechnen,
  PDF; Erfundenes als neu.jsonl im Protokoll-Archiv, der Nachzug
  übernimmt es (kein Rückschreiben aus dem Blatt-Chat, bis das
  Schreibrecht gemessen ist). Das Skript ist der spätere
  Kostensparer, nicht die Voraussetzung.
- Revisionen an ziel.md (Lehrer 01.10., in ziel.md noch
  nachzutragen): keine Zeitmarken, keine Zweigzeile, kein
  Inhaltsverzeichnis, kein „Ich kann“ in Titeln; Marken „P10 ’JJ“,
  „GYM“ (Sek II „Abi ’JJ“, „LK“, „FHR ’JJ“) statt Stern und
  Niveauwörtern; kein Test am Kopf, dafür „Zum Schluss“; Abschluss
  je Einheit mit mehreren Verfahren; Fehler finden nur auf Zuruf;
  Vorstufen nur in „schwach“; Regelfall ist die grobe Leiter,
  „schwach“ die feine; a) vorgerechnet statt Beispielkasten, nur
  wo es den Weg zeigt; Merkkasten im Regelfall auf dem Blatt,
  Form Fall – Beispiel – Ergebnis, Inhalt aus dem Katalog (der
  Lehrer pflegt den Text dort; Pflegeläufe fassen ihn nicht an);
  Lösungen nur Ergebnis, hinten, eine Datei je Bestellung;
  Textaufgaben sparsam (je Kette eine, dazu Anwendung).
- Bestellwörter (01.10.): „schwach“ (Form), „stark“ (Leiter
  angehoben), „gemischt“ (nur Zum-Schluss-Aufgaben als Zettel),
  „ohne blatt 0“, „mit lösungsweg“, „mit fehler-finden“, „mit
  sachaufgaben“; „mehr“ bleibt Wiederholung mit neuen Zahlen.
- Katalog Terme (01.10.): sechs Einheiten – Zusammenfassen,
  Malnehmen, Klammern auflösen, Ausklammern, Termwerte, Aufstellen;
  je Kette Leiter bis Gymnasialniveau (30 Sprossen aus
  bericht.md); Kennzeichnung, welche Sprossen Stufen des Regelfalls
  sind; Merkkasten kurz. Bank-Kennungen wandern dabei (Nachzug).
- Terme Prüfstein-Befund: Die Bank endet überall an der Lehrwerk-
  Grundhöhe; die obere Hälfte fehlt in allen Sek-I-Einträgen.
  Regel für den Nachzug: Leiter bis Gymnasialniveau; drei, vier
  Muster als Prüfstein (Prozent, lineare Funktionen, ein Sek-II-
  Thema), nicht je Eintrag ein Muster.
- Regel für Zurufe (01.10.): Ein Zuruf, der in einer Web-Sitzung
  landen kann, sagt „Commit auf main, kein Branch, kein PR“; ein
  PR-Merge lässt sich aus dieser Sitzung nicht ausführen (Sperre).
- Kandidaten für kandidaten.md (Lehrer 01.10.): „Knöpfe, die
  Claude selbst drücken kann (Merge, Push, Fetch), drückt Claude;
  der Lehrer bekommt nur Handgriffe, die eine Sitzung nicht
  ausführen kann.“ – „Erst Exemplar, dann Regel gilt auch für
  Layout: ein von Hand gesetztes Musterblatt vor jeder Regelrunde;
  jedes Blatt ganz ansehen, bevor es der Lehrer bekommt.“ –
  „Fortgesetzte Agenten statt neue: ein Agent, der die Dateien
  schon kennt, kostet je Folgelauf einen Bruchteil.“
- Modellwahl: Katalog- und Bankaufträge als Opus-Agenten aus dem
  Chat, Muster-Läufe ebenso; Blatt-Chats Opus.

## 5 Offene Punkte und Verworfenes

- Skript v1.2 kennt Muster 4 nicht (Kopf/Fuß, Abschluss, Zum
  Schluss, Marken, Kasten-Form, a) nur mit Weg, Rabatt-Anwendung
  zurück in Nr. 14); Spaltenbreite der Felder nach dem zweit-
  längsten Term; bei ≥ 2 Verfahren Rechenketten getrennt.
- Prompt v5.0: Satz „Begründen und Anwendung gehören in den
  Abschluss“ fehlt; Notbehelf „höchstens acht Teilaufgaben je
  Nummer“ bis der Katalog Stufen markiert; Abwechslung im
  Abschluss (Zuordnen, Welcher Term ist falsch, Figur) statt
  dreimal Textaufgabe; Prompt als `bankblatt.md` v5.0 nach
  blattbau (Schreibzugriff auf blattbau aus der Sitzung einmal
  anlegen); Wiederholbarkeit: 44 erfundene Zeilen je Lauf anders,
  bis die Bank sie hat.
- Mappe terme nennt als Katalogstand bbcf2d4 (Merge-Commit).
- Alte Posten aus 2026-09-30b bleiben: Zusammenbau „kein P10-
  Stoff“, Bausteine, Prüfskript v0.13, Katalog klein, Gegenlese,
  funktionsklassen CAS, K2–K7, Nachzug der 48 ab Montag 18:00.

Verworfen: Layoutregeln am Skript ohne Muster (vier Läufe, kein
Fortschritt im Urteil des Lehrers); Kompetenzblatt als Grundeinheit
des Lernblatts (Lehrer: Lernblatt/Fokus/Blatt 0 sind die Begriffe);
Test am Kopf der Einheit und „Für Schnelle“ (ersetzt durch Leiter
mit Marken und Zum Schluss); graue Kästen; Zeitmarke, Zweigzeile,
Inhaltsverzeichnis, „Ich kann“; Fehler finden als Pflicht.

## 6 Nächster Arbeitsschritt

1. Katalogauftrag Terme (Opus-Agent, eigener Klon, Repo
   mathe-nachhilfe): sechs Einheiten nach § 4, die 30 Sprossen aus
   bericht.md eingeordnet, Merkkasten je Einheit auf Kurzform,
   Stufen des Regelfalls markiert (Form der Markierung im Auftrag
   festlegen, z. B. „(Stufe)“ an der Sprosse); Commit auf main.
   Dann Bank-Nachzug terme (aufgabenbank): Kennungen auf die neuen
   Einheiten, die 51 Muster-4-Zeilen und die 44 Zeilen aus
   neu.jsonl des Tests (Lehrer liefert das Archiv) als Bankzeilen,
   Prüfskript 0/0, Mappe neu. Vorher Nutzungsanzeige.
2. Prompt v5.1 (Abschnitt § 5), als Block für das Projekt und als
   Datei nach blattbau.
3. Danach: Skript auf Muster 4; Nachzug der 48 ab Montag mit der
   Regel „Leiter bis Gymnasialniveau“; ziel.md-Revisionen
   nachtragen; kandidaten.md.
