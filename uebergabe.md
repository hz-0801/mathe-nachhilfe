# Übergabe verbessereBlaetter – 2026-10-07b (Chat 07.10., Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-07.md.

## 1 Ziel

Der Lehrer sagt in wenigen Worten, was er braucht, und hat in wenigen
Minuten ein gutes Blatt – jedes Thema Kl. 8 bis Abitur, Schulstoff und
Prüfung. Ein Programm setzt aus Bank und Steckbrief, der Chat ist der
Schalter (Linie 26.09., ziel.md § 1). Jetzt: den Schalter bauen, dann die
Steckbriefe in Serie.

## 2 Arbeitsgrundlage – beim Chatstart in dieser Folge lesen

1. `ueberblick-2026-10-07.md` (mathe-nachhilfe) – Bestandsaufnahme aller
   Ziel-, Beschluss- und Plandateien: Ziel, Bestand (gezählt), Diagnose,
   Widersprüche, Weg. Vor jeder größeren Entscheidung.
2. `offen.html` (mathe-nachhilfe) – Bestellbäume P10/Abitur/FHR,
   „Skript – was es leisten soll“ (fest 04.10.), Durchgang nach Stufe.
   Was dort „fest“ steht, gilt, bis der Lehrer es ändert.
3. aufgabenbank `bau/bauregeln.md` – die einzige Datei mit Bauregeln
   (Abschnitt 0 Pflege, 11 Offen und Erprobtes); Zuordnung alt → neu in
   `bau/bauregeln-streichliste.md`.
4. aufgabenbank `eingang/` – Protokolle der Blatt-Chats seit dem letzten
   Werkstatt-Chat (ab v5.8 mit Abschnitt „Befunde“ des Lehrers): zuerst
   lesen und auswerten, sie sind das Testmaterial.
5. `ziel.md` (nur Ziel und Sorten), `faellig.md` § 0 (Plan).
6. Steckbriefe `katalog/steckbrief/` (Grundwert, Pythagoras; Format in
   README.md mit Teil 5 „Arten“ und Feld „Schritte“).
7. Bauprogramm aufgabenbank `werkzeuge/pruefheft.py` v0.5 (Fokus aus
   Steckbrief: Auswahl je Sorte ab vier Seiten, zwei Spalten, Abruf,
   Erkennen je Art, Rechnen-Fall, Schlusszeile letzte fünf Jahre);
   Aufruf mit `--bb` auf den blattbau-Klon.

## 3 Arbeitsstand

Erledigt 07.10.:
- Bauregeln aus sechs Dateien (rund 250 Regeln) in eine Datei (55 Regeln,
  seitdem ergänzt); ziel.md auf Ziel und Sorten gekürzt; bank.md verweist.
- Fokus Pythagoras nach Sichtung neu: 5 S., 17 Aufgaben (vorher 9 S.,
  27); Fokus Grundwert neu: 2 S., 10 Aufgaben mit Abruf der Formel und
  Art „Mit einem Bruch“ (aufgabenbank bau/pruefheft/fokus-2026-10-07/).
- Überblick über alle Dateien (sechs Fable-Leser), Widersprüche
  entschieden: Fundstellen-Liste am Blattende (1.4), Prüfstein nur im
  Prüfungsheft (2.2), Bestellbaum als Eingang + Folgebaum der Kennung
  vorläufig (9.1), GYM-Marke (2.5, 53 Datenzeilen umgestellt),
  Zählfenster letzte fünf Jahre + zuletzt (3.12), fünf Blattsorten.
- Bank-Prompt v5.8 im Repo blattbau (Bauregeln haben Vorrang, Fokus-
  Zusatz, Befunde ins Protokoll); als Chat-Block an den Lehrer gegeben.

Nicht umgesetzt: Programm kennt die Fundstellen-Liste am Blattende noch
nicht (1.4); Prüfungsheft-Grundform G2; Lernblatt-Programm
(zusammenbau.py) auf Regelstand 01.10.

Messwerte: Chat mit Bauprogramm-Umbau und allen Neubauten im Chat: Woche
25 → 26 %, Sitzung 2 % – Arbeit im Chat ist billig. Sechs Fable-Leser
(zusammen rund 1,7 Mio Token laut Zählern): Woche 26 → 29 %, Fable 0 →
7 %. Teuer sind Agentenläufe mit vielen Werkzeugaufrufen.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Beschlüsse in offen.html (fest) und bauregeln.md sind bindend, bis der
  Lehrer sie ändert; vor einer neuen Regel nachsehen, ob es sie gibt.
- Ideen des Lehrers sind zuerst Richtungen („eher“), Regeln nur auf sein
  „immer/nie“ oder nach einem Befund am Blatt; jede Richtung am nächsten
  Blatt prüfen. Didaktik eher aus Vorbildern und Urteil, Regeln vor allem
  fürs Handwerk.
- Arbeitsweise am Blatt: Claude prüft jedes Blatt selbst (Handwerk und
  „Was tut der Schüler, kann er dabei etwas falsch machen?“), bevor der
  Lehrer es sieht; der Lehrer schickt seine Befunde gesammelt in einer
  Nachricht; Claude setzt in einem Gang um und fragt nur bei echten
  didaktischen Entscheidungen.
- Fünf Blattsorten: Original, Original neu, Prüfungsheft, Fokus,
  Lernblatt.
- Betrieb bis zum Schalter: Lernblatt Kl. 8–10 → erzeugeBlatt(Bank) v5.8;
  Oberstufe-Schulstoff → alter Unterrichtsblatt-Prompt als Notbehelf;
  P10 → fertige Fokusblätter und Prüfungshefte aus der Aufgabenbank,
  weitere über die Werkstatt; Prüfungsblatt-Prompt nicht mehr benutzen.
- Lehrer will keine Kleinteiligkeit: große Linien, Ergebnis am Blatt.

## 5 Offene Punkte und Verworfenes

- Folgebaum der Kennung: tiefe Diskussion steht aus (Idee: „mehr“ beginnt
  mit kleinem Test, weil die Aufgaben schon bearbeitet wurden).
- Projektanweisung verbessereBlätter: Chatstart um ueberblick, offen.html
  und eingang/ ergänzen (bis dahin trägt es diese Übergabe).
- Bestätigen, dass v5.8 im Blatt-Projekt eingesetzt und die Projektdateien
  mathblatt.sty/Anleitung entfernt sind.
- Weiteres offen: bauregeln.md § 11; ueberblick § 5.
- Verworfen: QR-Code; Merkkasten im Fokus; vorgelegte falsche Rechnung als
  Regel (nur eigene Form, wo die P10 den Typ hat); sofortiger Schalter-Umbau
  am 07.10. (Programm deckt nur zwei Handgriffe, Technik ungemessen).

## 6 Nächster Arbeitsschritt

Erst eingang/ auf neue Protokolle prüfen. Dann den Schalter beginnen:
Probelauf, ob ein Blatt-Chat im Projekt die Repos klonen, LaTeX nutzen und
`pruefheft.py` für „Pythagoras P10“ laufen lassen kann (Zeit messen);
danach Entwurf des Schalters (Bestellbaum → Programm, sonst Ausnahmeweg
v5.8). Modell: Opus im Chat; Agenten nur klein geschnitten, Fable darf
verbraucht werden.
