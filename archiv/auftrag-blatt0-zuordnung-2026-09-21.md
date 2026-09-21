# Auftrag: 20 Zuordnungen eintragen, Geltungsbefund ablegen

## Ausgangslage

Nach den Läufen cfa4723 und f6e5fc5 tragen 162 Blatt-0-Zeilen einen
Dateiverweis. Kennzahl 9 steht bei 43 Fertigkeitszeilen ohne Ziel.
Von diesen 43 wurden 19 vom Lehrer als zuordenbar entschieden: Die
Fertigkeit steht in einem vorhandenen Katalogeintrag, die Zeile sagt
es nur nicht. Dazu kommt die eine Zeile, die beim letzten Lauf
gemeldet und nicht angefasst wurde (`zinsrechnung.md` 27, Posten in
`faellig.md` § 2).

`ersetzungen-blatt0-zuordnung.txt` enthält diese 20 Zeilen als
fertige Ersetzungen. Anders als bei den beiden Läufen zuvor wird
hier nicht nur ein Dateiname in eine vorhandene Nennung eingesetzt,
sondern ein ganzer Satz „Thema … (datei.md), Einheit n." angefügt.
Die Zuordnung ist entschieden; du ersetzt, du urteilst nicht.

Dazu legt dieser Auftrag den Befund der Geltungsrecherche ab, die
als Posten in `faellig.md` § 2 steht.

## Schritte

1. `ersetzungen-blatt0-zuordnung.txt` einlesen. Die Datei ist in
   Blöcke zu je fünf Zeilen gegliedert, getrennt durch `----`:
   `DATEI <name>`, `ZEILE <nummer>`, `ALT <text>`, `NEU <text>`.
   Der Text beginnt jeweils nach dem ersten Leerzeichen des
   Schlüsselworts und läuft bis zum Zeilenende; er kann selbst
   senkrechte Striche, Klammern und Anführungszeichen enthalten.
   Die Einträge liegen in `katalog/`.
2. Je Block: In `katalog/<DATEI>` die Zeile `<ZEILE>` aufsuchen und
   dort den Text `ALT` durch `NEU` ersetzen. Drei Bedingungen, alle
   müssen gelten – sonst nichts ändern, Block überspringen und
   melden:
   – die Zeilennummer existiert,
   – die Zeile ist zeichengenau gleich `ALT` (bei `zinsrechnung.md`
     27: `ALT` kommt genau einmal in der Zeile vor),
   – die Zeile liegt im Abschnitt „### Voraussetzungen (Blatt 0)"
     vor der Zwischenzeile „Erkennungsschritte…".
3. `werkzeuge/tragfaehigkeit.py`, `werkzeuge/verweis-pruef.py` und
   `werkzeuge/blatt0-belege.py` laufen lassen; die drei abgeleiteten
   Dateien werden mit committet.
4. `befund-geltung-2026-09-21.md` bleibt in der Wurzel liegen. In
   `faellig.md` den Posten zur gebündelten Geltungsrecherche
   (Matrizen, Konfidenzintervalle) aus § 2 streichen und mit dem
   heutigen Datum nach § 4 übertragen, mit Verweis auf die neue
   Befunddatei. Ebenso den Posten zu `zinsrechnung.md` 27.
5. Aus dem Befund zwei neue Posten in `faellig.md` § 2 anlegen,
   Wortlaut frei, Inhalt genau:
   – **P10-Struktur ab 2026:** Die Brandenburger Prüfung am Ende
     der Jahrgangsstufe 10 wird ab 2026 nicht mehr als integrierte
     Arbeit geschrieben; Sternchenaufgaben entfallen, EBR und FOR
     bekommen getrennte Arbeiten (40 bzw. 60 BE, je 135 Minuten).
     Der msa-Typenkatalog ist aus Heften mit Sternchen gebaut;
     Zeilenzuordnung und Niveaukonzept sind daraufhin zu prüfen.
     Auslöser: Erscheinen der ersten Hefte nach neuem Muster; bei
     Claude. Fundstelle: `befund-geltung-2026-09-21.md` § 3.
   – **Zwei neue Inhalte auf Niveaustufe G:** Sinussatz in
     beliebigen Dreiecken sowie Lösbarkeit und Lösungsvielfalt
     quadratischer Gleichungen der Typen ax²+n=b und ax²+bx+n=0.
     Betrifft `trigonometrie.md` und `quadratische-gleichungen.md`.
     Auslöser: nächste Pflege dieser Einträge; bei Claude.
     Fundstelle: `befund-geltung-2026-09-21.md` § 3.
6. Auftrag und Ersetzungsliste nach `archiv/` verschieben
   (`archiv/auftrag-blatt0-zuordnung-2026-09-21.md`,
   `archiv/ersetzungen-blatt0-zuordnung-2026-09-21.txt`).
7. Committen mit der Nachricht
   „Blatt 0: 20 Zuordnungen eingetragen, Geltungsbefund abgelegt".

## Prüfungen

- 20 Ersetzungen ausgeführt, keine übersprungen. Jede übersprungene
  Zeile ist ein Abbruchgrund für Schritt 3: erst melden.
- `git diff --stat` nennt genau acht Dateien unter `katalog/`
  (bruchrechnung, lineare-funktionen, lineare-gleichungen,
  prozentrechnung, rationale-zahlen, terme, zinsrechnung,
  zuordnungen) plus die drei abgeleiteten Dateien, `faellig.md` und
  die neue Befunddatei.
- In jeder der 19 neuen Zeilen ist ausschließlich ein Satz der Form
  ` Thema … (name.md), Einheit n.` eingefügt, sonst nichts; bei
  `terme.md` 26 ohne Einheitsangabe, bei `zinsrechnung.md` 27 nur
  ein Dateiname in Klammern.
- Kennzahl 9 fällt von 43 auf 23. Kennzahl 7 bleibt 1 von 73.
  Kennzahl 8 Gruppe (c) bleibt 16.
- „Einträge mit Dateiverweisen, die daneben Themen in Wortform
  nennen" fällt in den Messlücken von `_tragfaehigkeit.md` von 1
  auf 0.
- Die Zahl der direkt zugeordneten Einheitenangaben in Prüfung 2
  steigt von 497. Jede Einheitsnummer, die größer ist als die
  Zieldatei Einheiten hat, wird berichtet und nicht berichtigt;
  bekannt und unverändert ist der Fall in
  `lineare-gleichungssysteme.md` Zeile 117.
- `python katalog/_pruef_struktur.py` und
  `python werkzeuge/themen-pruef.py` laufen durch.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann Zahl der
ausgeführten und übersprungenen Ersetzungen, `git diff --stat`, das
Ergebnis der Prüfungen, die neuen Werte von Kennzahl 9 und
Prüfung 2, die beiden neuen Posten im Wortlaut. Abweichungen und
Annahmen. Letzte Zeile: „Push origin drücken".

## Regeln

Nur die 20 genannten Stellen anfassen. Keinen Satz umformulieren,
keine Quellenklammer anfassen, keine Zeile hinzufügen oder löschen.
An `befund-geltung-2026-09-21.md` nichts ändern – die Datei wird
abgelegt, nicht bearbeitet. Passt eine Ersetzung nicht, melden statt
anpassen.

Modell: Sonnet (reine Mechanik, alle Lesarten sind entschieden).
