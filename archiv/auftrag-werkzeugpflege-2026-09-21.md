# Auftrag: Zwei Messfehler beheben, sechs Posten eintragen

## Ausgangslage

Der Lauf vom 21.09. („Blatt 0: Dateiverweise nachgetragen",
cfa4723) hat 136 Klammern der Form ` (name.md)` in die
Blatt-0-Abschnitte eingefügt. Zwei Werkzeuge messen seitdem falsch,
beide Male, weil ihre Lesart die neue Schreibform nicht kennt. Kein
Eintrag ist betroffen; es geht um die Werkzeuge und um die
abgeleiteten Dateien.

Dazu sechs Befunde aus den drei Prüfläufen, die bisher nirgends als
Posten stehen und sonst verloren gehen.

## Schritte

### Teil A – verweis-pruef.py, Prüfung 2

1. In `werkzeuge/verweis-pruef.py` die Lesart „Einheitenangabe
   direkt hinter einem Verweis" erweitern. Bisher darf zwischen
   `<name>.md` und dem Wort „Einheit" nur Leerraum, Komma oder eine
   öffnende Klammer stehen. Neu sind zusätzlich zugelassen: eine
   schließende Klammer und der Klammerinhalt, der dem Dateinamen
   folgt. Die drei Formen, die jetzt treffen müssen:
   – `Thema Terme (terme.md), Einheit 2.`
   – `Kreis (kreis.md) Einheit 2.`
   – `Lineare Funktionen (lineare-funktionen.md, Blatt 0)` –
     hier folgt keine Einheitenangabe, die Zeile darf also auch
     nicht fälschlich eine zuordnen.
   Sonst bleibt die Lesart unverändert; was bisher als „nicht
   eindeutig zuordenbar" galt, gilt weiter so.
2. Die Messweise und den Abschnitt „Schwäche der Messung" in der
   Ausgabedatei an die neue Lesart anpassen. Skriptversion auf
   v0.2, mit einer Zeile, was sich geändert hat.

### Teil B – tragfaehigkeit.py, Wortform-Heuristik

3. In `werkzeuge/tragfaehigkeit.py` zählt eine Nennung der Form
   „Thema " vor einem Großbuchstaben weiterhin als Nennung in
   Wortform, auch wenn direkt dahinter der Dateiverweis steht.
   Neu: Folgt dem Titel unmittelbar ` (<name>.md`, ist es keine
   Nennung in Wortform mehr, sondern ein Verweis. Alles andere
   bleibt.
4. Messweise und „Schwäche der Messung" anpassen, Skriptversion
   auf v0.2 mit einer Zeile zur Änderung.

### Teil C – Neu rechnen

5. `werkzeuge/tragfaehigkeit.py`, `werkzeuge/verweis-pruef.py` und
   `werkzeuge/blatt0-belege.py` laufen lassen; die drei
   abgeleiteten Dateien werden mit committet. Dass sich in
   `katalog/_blatt0-belege.md` nur die Stand-Zeile ändert, ist
   erwartet – ändert sich dort mehr, melden und nicht committen.

### Teil D – Sechs Posten in faellig.md § 2

6. Je eine Zeile nach dem Muster des Abschnitts (was · Auslöser
   oder Termin · bei wem · Fundstelle). Wortlaut frei, Inhalt
   genau:
   – **fhr-Zeile fehlt:** `fhr/fhr-typen.csv` führt das Thema
     „Gleichungen lösen", `themen.csv` hat dazu keine fhr-Zeile.
     Welche der beiden Dateien recht hat, ist offen – entscheidet
     ein Blick in `fhr.md` und die erfassten Hefte. Auslöser: die
     Erweiterung des Prüfungsblatt-Prompts auf fhr; bei Claude.
     Fundstelle: `katalog/_verweise.md` Prüfung 3 (d).
   – **28 Namensabweichungen:** H1-Überschrift und `thema`-Werte
     weichen in 27 Fällen voneinander ab, elf davon systematisch
     bei den fhr-Titeln, vierzehn ohne jede Übereinstimmung. Ob
     Absicht (Sammelthema) oder Schlamperei, ist ungeklärt.
     Auslöser: Entscheidung über die Zielform der Einträge; bei
     Claude. Fundstelle: `katalog/_verweise.md` Prüfung 3 (b).
   – **231 Verweise in Werkstattdateien:** Katalogeinträge
     verweisen 94-mal auf `konzept.md` und 52-mal auf
     `faellig.md`. Zu klären ist, in welchen Abschnitten sie
     stehen – steht so etwas in Verortung oder Blatt 0, liest ein
     Prompt künftig Entscheidungsprotokolle mit. Auslöser: Umbau
     der Prompte; bei Claude. Fundstelle: `katalog/_verweise.md`
     Prüfung 1 Gruppe (b).
   – **270 Paare ohne Gegenrichtung:** Wenn A das Thema B in
     Blatt 0 nennt, nennt B den Eintrag A in 270 von 465 Fällen
     nirgends. Ob die Gegenrichtung nötig ist, hängt daran, ob
     Blatt 0 nur rückwärts („was setzt das Thema voraus") oder
     auch vorwärts („wo wird es gebraucht") aufgelöst wird.
     Auslöser: diese Entscheidung beim Promptumbau; bei Claude.
     Fundstelle: `katalog/_verweise.md` Prüfung 4.
   – **Sechs RLP-Zitate nicht wörtlich:** Die Zitate in den
     Quellenklammern stehen gebeugt oder gekürzt im Eintrag und
     sind deshalb im RLP-Text nicht auffindbar. Solange das so
     ist, lässt sich keine Klammer maschinell gegen den RLP
     auflösen. Auslöser: die nächste Pflege der betroffenen
     Einträge; bei Claude. Fundstelle: `katalog/_blatt0-belege.md`
     (Abweichungen und Annahmen des Laufs).
   – **MSK-Bausteinliste lückenhaft:** Die Einträge zitieren
     Codes (B2B, D1A, S4, S5, N, B), zu denen
     `katalog/_quellen.md` keinen Bausteintitel führt. Mit
     vollständiger Liste ließe sich die Schicht unterhalb des
     Katalogs genauer beschreiben; Lizenz ist geklärt (nur
     Struktur). Auslöser: Entscheidung, ob der Katalog einen
     Boden bekommt; bei Claude. Fundstelle:
     `katalog/_blatt0-belege.md`, MSK-Bestandteile.

### Teil E – Abschluss

7. Auftrag nach `archiv/auftrag-werkzeugpflege-2026-09-21.md`
   verschieben, committen mit der Nachricht
   „Werkzeugpflege: Lesarten nach der Klammerform, sechs Posten".

## Prüfungen

- Teil A: Die Zahl der direkt zugeordneten Einheitenangaben steigt
  von 360 auf etwa 470. Bleibt sie bei 360, greift die neue Lesart
  nicht. Wie viele Nummern größer sind als die Zieldatei Einheiten
  hat, ist offen – bisher waren es null, aber die 112 neuen Zeilen
  sind nie geprüft worden. Jeder Treffer wird berichtet, keiner
  wird berichtigt.
- Teil B: In den Messlücken von `_tragfaehigkeit.md` fällt
  „Einträge mit Dateiverweisen, die daneben Themen in Wortform
  nennen" von 29 auf 8 oder in dessen Nähe. Bleibt es bei 29,
  greift die Änderung nicht.
- Unverändert bleiben müssen: Kennzahl 7 (1 von 73), Kennzahl 8
  Gruppe (c) (16 Verweise auf fehlende Dateien), Kennzahl 9
  (93 von 463 in 23 Einträgen), die Zahl der Blatt-0-Kanten (465)
  und die Nachfragezahlen der Tabelle A. Weicht eine davon ab, hat
  eine der beiden Änderungen mehr getroffen als gewollt – melden,
  nicht anpassen.
- `git diff --stat` nennt zwei Skripte, drei abgeleitete Dateien
  und `faellig.md`. Kein Eintrag unter `katalog/`, keine Zeile in
  `themen.csv`.
- `python katalog/_pruef_struktur.py` und
  `python werkzeuge/themen-pruef.py` laufen durch.
- Zwei Läufe je Werkzeug erzeugen dieselbe Datei.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann die beiden
Zahlen aus Teil A und B vor und nach der Änderung, die fünf Zahlen,
die gleich bleiben mussten, und – falls Prüfung 2 jetzt zu große
Einheitsnummern findet – diese Fälle vollständig mit Eintrag,
Zeile, Ziel und Nummer. Dazu `git diff --stat`, Abweichungen und
Annahmen. Letzte Zeile: „Push origin drücken".

## Regeln

Keinen Katalogeintrag anfassen. Keine Zahl anpassen, damit eine
Prüfung aufgeht. Findet Prüfung 2 falsche Einheitsnummern, sind das
Befunde für den Lehrer, keine Korrekturaufgabe.

Modell: Opus (beide Änderungen sind Lesarten).
