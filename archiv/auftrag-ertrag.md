# Auftrag: Ertrag je Typ, Profil msa

Modell: Sonnet (reine Mechanik).

## Ausgangslage

Repo hz-0801/mathe-nachhilfe, Stand Commit 3a56a7b. ziel.md § 5
nennt als offenen Posten: „Ertrag je Typ: Skript aus
msa-typen.csv (Jahrgänge, BE, block, schritte), Schwelle für
„selten" am Ergebnis setzen." Der Ertrag ordnet im Blattbau die
Typen (ziel.md § 2: „die Typen stehen nach Ertrag") und bestimmt,
welche Sprossen die Option „schwach" weglässt. Die Schwelle setzt
der Lehrer am Ergebnis; dieser Auftrag liefert die Zahlen.

Daten: msa/msa-katalog-basis.csv (126 Zeilen) und
msa/msa-katalog-kontext.csv (267 Zeilen), Trennzeichen Semikolon,
alle Felder in Anführungszeichen, UTF-8. Relevante Felder: id,
jahr, block (Basis/Kontext), punkte, niveau_geschaetzt, thema,
typ, typ_neben (Pipe-getrennt, kann leer sein), schritte.
Typenliste msa/msa-typen.csv (185 Zeilen; Felder typ, leitidee,
thema, definition, beispiel_id, status).

Gegenprobe aus katalog/prozentrechnung.md, Abschnitt
„Prüfungsform (P10)": Thema „Prozentrechnung" hat 22 Zeilen mit
diesem CSV-Thema, 38 von 780 Punkten, Jahrgänge 2014 bis 2026
ohne Lücke, Niveau I dreizehnmal, Niveau II neunmal, Niveau III
nie. „Prozentwert berechnen" hat 4 Hauptzeilen mit Thema
Prozentrechnung (2014-OS-B1a, 2017-OS-B1b, 2021-OS-B1c,
2026-FOR-B1a) und weitere mit anderem Thema.

## Schritte

1. Schreibe werkzeuge/ertrag.py. Es liest beide msa-Kataloge und
   msa-typen.csv, ändert nichts an ihnen und schreibt zwei
   Dateien: msa/msa-ertrag.csv und msa/msa-ertrag.md. Je Typ aus
   msa-typen.csv (Spalte typ) berechnet es:
   - zeilen_haupt: Katalogzeilen mit typ = Typ
   - zeilen_neben: Zeilen, in deren typ_neben der Typ steht
   - jahre_haupt: Zahl verschiedener jahr-Werte der Hauptzeilen
   - jahre_gesamt: dasselbe über Haupt- und Nebenzeilen
   - erster, letzter: kleinstes und größtes jahr (Haupt und Neben)
   - punkte_haupt: Summe punkte der Hauptzeilen
   - punkte_anteil: punkte_haupt geteilt durch die Punktsumme
     beider Kataloge, auf 0,1 % gerundet
   - basis, kontext: Hauptzeilen je block
   - niveau_I, niveau_II, niveau_III: Hauptzeilen je
     niveau_geschaetzt
   - schritte_mittel: Mittel der Hauptzeilen-Werte schritte, auf
     eine Dezimalstelle; nicht numerische Werte werden ausgelassen
     und gezählt (schritte_fehlt)
   - thema, leitidee, status aus msa-typen.csv
   - ertrag: die Sortiergröße – punkte_haupt, bei Gleichstand
     jahre_gesamt, dann zeilen_haupt
   Ein typ-Wert oder typ_neben-Wert der Kataloge, der in
   msa-typen.csv fehlt, kommt als Zeile mit status „nicht in
   typen.csv" dazu und in den Bericht.
2. msa-ertrag.md hat diese Form: Kopfzeile mit Stand (Datum,
   Commit), Zählregel in drei Sätzen, Gesamtzahlen (Zeilen,
   Punkte, Typen mit Hauptzeile, Typen nur als Nebentyp, Typen
   ohne Vorkommen), die Zeile „abgeleitet von werkzeuge/ertrag.py,
   nie von Hand ändern". Dann Tabelle A: alle Typen nach ertrag
   absteigend mit Rang und allen Spalten oben. Tabelle B: je thema
   (nach Punktsumme des Themas absteigend) die Typen des Themas in
   Ertragsfolge. Tabelle C: Verteilung als Hilfe für die Schwelle
   „selten" – für punkte_haupt, jahre_gesamt und zeilen_haupt je
   die Werte, unter denen 10 %, 25 %, 50 % der Typen mit
   Hauptzeile liegen, und die Zahl der Typen mit jahre_gesamt ≤ 2.
   Liste D: Typen ohne Hauptzeile (nur Nebentyp) und Typen ohne
   Vorkommen, je mit Thema.
3. Führe das Skript aus. Gegenprobe im Skript selbst, als
   Ausgabe am Ende des Laufs, kein Abbruch: Zeilen mit thema
   „Prozentrechnung" = 22, deren Punktsumme = 38, Punktsumme
   beider Kataloge = 780, Zahl verschiedener jahr-Werte im Thema
   Prozentrechnung = 13, Hauptzeilen „Prozentwert berechnen" mit
   Thema Prozentrechnung = 4. Jede Abweichung steht im Bericht mit
   dem tatsächlichen Wert; das Skript wird dann nicht angepasst,
   um die Zahl zu treffen – die Abweichung ist der Befund.
4. README.md: Unter „msa/" nach der Zeile zu msa-vorgaben.md eine
   Zeile für msa-ertrag.md und msa-ertrag.csv (Zweck: Ertrag je
   Typ, Sortiergröße, Verteilung für die Schwelle „selten";
   abgeleitet, nie von Hand ändern). Unter „werkzeuge/" eine
   Zeile für ertrag.py. Unter „Wo fange ich an" nach der Zeile zu
   faellig.md eine Zeile für befund-testlauf-2026-09-22.md
   (Befund des ersten Katalog-Testlaufs mit den Beschlüssen, die
   den Prompt v4.0 tragen). Sonst nichts in der README.
5. python werkzeuge/themen-pruef.py ausführen; Rückgabewert im
   Bericht.
6. Verschiebe auftrag-ertrag.md nach archiv/. Commit mit der
   Nachricht „Ertrag je Typ (msa): werkzeuge/ertrag.py,
   msa/msa-ertrag.md; Befund Testlauf 2026-09-22".

## Prüfungen

- Die Summe punkte_haupt über alle Typen ist gleich der
  Punktsumme beider Kataloge (jede Zeile hat genau einen typ).
- Die Summe zeilen_haupt ist 393.
- Kein Typ hat jahre_haupt > zeilen_haupt.
- msa-ertrag.csv hat genauso viele Datenzeilen wie Tabelle A.
- Die fünf Zahlen der Gegenprobe (Schritt 3).

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann: die
fünf Zahlen der Gegenprobe mit Soll und Ist; die Gesamtzahlen
aus dem Kopf von msa-ertrag.md; Tabelle C wortgleich; die Zahl
der Typen in Liste D; typ-Werte, die in msa-typen.csv fehlen;
Rückgabewert von themen-pruef.py; Abweichungen und Annahmen mit
Grund; die Commit-Kennung. Nichts gelöscht, nichts außer den
genannten Dateien geändert – oder was doch. Letzte Zeile:
„Push origin drücken".

## Regeln

Keine Rückfragen: Bei Unklarheit triffst du die naheliegende
Annahme und nennst sie im Bericht. Die Kataloge, die Typenliste
und der Ordner katalog/ werden nicht angefasst. Nichts wird
gelöscht. Werte kommen nur aus den CSVs, nichts wird ergänzt oder
geschätzt. Dateien UTF-8 mit LF. Das Skript läuft aus der
Repo-Wurzel mit python werkzeuge/ertrag.py und braucht nur die
Standardbibliothek.
