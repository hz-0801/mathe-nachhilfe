# Übergabe verbessereBlaetter – 2026-10-01b (Chat 01.10. nachmittags bis abends)

Vorherige Übergabe: archiv/uebergabe-2026-10-01.md.

## 1 Ziel

Der bestmögliche Themenkatalog, die Aufgabenbank und die Prompts,
damit aus wenigen Wörtern druckfertige Blätter entstehen. Maßstab
ist ziel.md (28.09.) mit den Revisionen vom 01.10. (Übergabe
2026-10-01 § 4, dort noch nicht nachgetragen); Leitbild: ein Blatt
für alle Schüler, aus der Bank zusammengesetzt, der Chat deutet,
setzt und ergänzt. Neu seit heute: Blätter sollen schnell aus der
Bank kommen, und was ein Blatt-Chat neu erfindet, landet nach
Prüfung in der Bank (Lehrer 01.10.).

## 2 Arbeitsgrundlage

- mathe-nachhilfe: `katalog/terme.md` mit sechs Einheiten
  (Zusammenfassen, Malnehmen, Klammern auflösen, Ausklammern,
  Termwerte, Aufstellen; Commits 84abe58 und 9e85c1e) – 81
  Sprossen, 68 davon „(Stufe)“ (Regelfall), Merkkästen in der
  Muster-4-Form; `katalog/_terme-zuordnung-2026-10-01.md` – die
  Tabelle alt → neu, auf der der Bank-Nachzug aufsetzt (Bank-
  Kennungen hängen noch an der alten Gliederung).
- aufgabenbank unverändert: `bau/terme/muster-2026-10-01/muster4.tex`
  (Zielblatt), `bericht.md` dort, `werkzeuge/zusammenbau.py` v1.2
  (kennt Muster 4 nicht), Bank 15 351 Zeilen.
- Bank-Prompt v5.0: nur als Projektanweisung in erzeugeBlatt(Bank),
  nicht im Repo blattbau.
- anweisungen: `projekt-verbessereBlaetter.md` 2026-10-01,
  `kandidaten.md` 2026-10-01.

## 3 Arbeitsstand

Erledigt 01.10. nachmittags bis abends:
- Katalog Terme umgebaut (Opus-Agent, 0,24 Mio Token; Schätzung
  war 0,15). Alle 30 Sprossen der Vorschlagsliste eingeordnet, alle
  110 Teilaufgaben von Muster 4 finden eine Stufe. Folgeänderung
  als fortgesetzter Agent: P10 ’25 (2025-GYM-B2a) als Prüfungshöhe
  der Kette Zusammenfassen statt Termwerte (Lehrer: Option B).
- Schreibweg gemessen: Diese Cloud-Sitzung hatte kein Schreibrecht
  auf die Repos (Proxy 403; nachträgliches Anhängen abgelehnt),
  obwohl alle Repos von hz-0801 für Claude mit Schreibrecht
  freigegeben sind. Ersatzweg eingerichtet: Ordner
  `mathe-nachhilfe` auf dem Rechner freigegeben, Patch per
  `git am` dort eingespielt, Push durch den Lehrer. Push aus der
  abgeschotteten Rechner-Umgebung geht nicht (keine GitHub-
  Anmeldung dort).
- Messwerte: Woche 58 % (mittags) → 64 % (vor dem Agenten), Fable
  51 → 61 % allein durch diesen Chat bis dahin; Stand nach den
  Agenten nicht abgelesen.

Nicht erledigt: Bank-Nachzug Terme; Prompt v5.1; Skript auf
Muster 4; Nachzug der 48; ziel.md-Revisionen; Verweise anderer
Einträge auf die alten Terme-Nummern.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter, soweit hier nichts anderes steht.

- Schreibrecht hat eine Sitzung nur, wenn das Repo beim Start
  gewählt wurde (Messwert 01.10.). Der Werkstatt-Chat wird deshalb
  in der Desktop-App mit Repo `mathe-nachhilfe` gestartet; erster
  Handgriff im neuen Chat ist ein Mess-Commit (eine Zeile in
  faellig.md) mit Push durch Claude, und ein zweiter nach
  `aufgabenbank`. Gelingt das nicht: Patch-Weg wie oben, Push durch
  den Lehrer; Ordnerfreigabe über den Dialog, den Claude auslöst.
- Blatt-Chats laufen nicht mehr als gewöhnlicher Projekt-Chat (der
  kann nicht einmal lesen: Sperre „externer Code“ am 01.10.),
  sondern als Sitzung mit Repo `aufgabenbank` im Projekt
  erzeugeBlatt(Bank). Prompt v5.1 schreibt dann selbst ins Repo:
  Blatt und Protokoll nach `blaetter/` (Annahme: Ablage wie
  einsortieren.py sie baut), neu erfundene Aufgaben nach
  `bank/<eintrag>/eingang.jsonl` – nie direkt in `e<n>.jsonl`.
  Ein Agent der Werkstatt prüft den Eingang (Prüfskript, Dubletten,
  Sprosse aus dem Katalog), der Chat sagt in zwei, drei Sätzen,
  was dazukommt, der Lehrer sagt ja, der Agent übernimmt. Lehrer
  01.10.: „in Bank schreiben, beurteilt“.
- Unveränderliches (mathblatt.sty, Anleitung_mathblatt.md,
  muster4.tex) kommt als Projektdatei nach erzeugeBlatt(Bank), damit
  kein Code über das Netz geladen werden muss (Annahme, bis ein
  Blatt-Chat sie bestätigt).
- Katalog Terme: P10 ’25 steht oben in der Kette Zusammenfassen
  (Option B); Termwerte endet ohne Prüfungsmarke. Vorstufen sind
  Stufe, wo Muster 4 sie zeigt (Nr. 5 a/b); die Regel „Vorstufen
  nur in schwach“ gilt für die übrigen.
- Kontingent: kein Zukauf als Plan. Zukauf wird zu API-Preisen
  abgerechnet (support.claude.com, Artikel 12429409) und bringt je
  Token schätzungsweise ein Fünftel bis ein Zehntel der Abo-
  Leistung; nur als Reserve, wenn eine Woche am Freitag leer ist.
  Plan: Rest dieser Woche Bank-Nachzug Terme und Prompt v5.1; ab
  Montag 18:00 der Nachzug der 48 in Schüben mit Ablesen.
- Modellwahl: Katalog-, Bank- und Prompt-Aufträge als Opus-Agenten
  aus dem Chat; Mechanik (Verweise umnummerieren) Sonnet; Blatt-
  Chats Opus. Fortgesetzte Agenten vor neuen.
- Kandidaten für kandidaten.md: eingetragen (2026-10-01).

## 5 Offene Punkte und Verworfenes

- Sieben Einträge verweisen noch auf die alten Terme-Nummern
  („terme.md Einheit 1“ in index.md, lineare-funktionen,
  prozentrechnung, lineare-gleichungen, kreis; „Einheit 2“ in
  reelle-zahlen, binomische-formeln). Kleiner Sonnet-Auftrag mit
  der Zuordnungsdatei.
- `werkzeuge/marken-bau.py` darf für terme erst laufen, wenn
  `_klassen-belege.md` und `_pruefungswort-belege.md` sechs
  Einheiten führen; die Marken-Zeilen sind von Hand übertragen.
- Terme: Malnehmen S8/S9 liegen über der alten Zielmarke ohne GYM
  (Muster zeigt es so); 2022-GYM-B2b ohne Sprossen-Marke
  (binomische Formel darin); Kastenprüfer meldet weiter die
  Blatt-0-Beispiele „3 − 7“ und „3 · (−4)“.
- Prompt v5.1 (zu den Posten aus 2026-10-01 § 5): Leseweg in
  Stufen (Raw-URL als Text, Clone nur mit Shell, bei Sperre
  Dateiliste statt Frage); Mappenname aus dem Katalog; Schreiben
  ins Repo nach § 4; „Begründen und Anwendung in den Abschluss“;
  Abwechslung im Abschluss; als `bankblatt.md` nach blattbau.
- neu.jsonl des Terme-Tests (44 Zeilen): liegt beim Lehrer im
  Archiv `Terme_2026-10-01_protokoll.zip`, noch nicht im Repo.
- Alte Posten bleiben: Skript v1.2 auf Muster 4; Mappe terme nennt
  Katalogstand bbcf2d4; Zusammenbau „kein P10-Stoff“; Bausteine;
  Prüfskript v0.13; Katalog klein; Gegenlese; funktionsklassen CAS;
  K2–K7; ziel.md-Revisionen; kandidaten-Durchsicht.

Verworfen heute: Weg 2 des Blatt-Chats (ohne Bank und Stilpaket
bauen) – widerspricht dem Ziel, erfundene Aufgaben trotz Bank;
Zukauf als Weg zum Fertigwerden – zu teuer je Token; zweites
Max-Konto – zwei getrennte Welten, Bedingungen ungeklärt.

## 6 Nächster Arbeitsschritt

1. Mess-Commit aus dem neuen Chat (eine Zeile in faellig.md,
   Push durch Claude); dann `aufgabenbank` anhängen und ebenso
   messen. Vorher Nutzungsanzeige ablesen.
2. Bank-Nachzug Terme (Opus-Agent, eigener Klon aufgabenbank):
   Kennungen nach `_terme-zuordnung-2026-10-01.md` auf die sechs
   Einheiten, die 51 Muster-4-Zeilen und die 44 Zeilen aus
   neu.jsonl (Lehrer legt das Archiv in den Chat) als Bankzeilen,
   Prüfskript 0/0, Mappe neu, Commit und Push durch den Agenten.
3. Prompt v5.1 (§ 5) als Block für erzeugeBlatt(Bank) und als
   `bankblatt.md` nach blattbau; dazu die Projektdateien (§ 4).
4. Danach: Verweise-Auftrag (Sonnet), Skript auf Muster 4, Nachzug
   der 48 ab Montag 18:00.
