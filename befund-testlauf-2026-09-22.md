# Befund Testlauf 2026-09-22 – erstes Lernblatt aus dem Katalog

Lauf: Prozentrechnung, Projekt erzeugeUnterrichtsblatt(), Prompt
v3.34 (im Projekt lag nicht v3.35), Modell Opus 5. Eingabe: Raw-
URL von katalog/prozentrechnung.md als maßgebliche Quelle, Lernblatt
mit Blatt 0, drei Dateien. Ergebnis: Blatt 0 (11 Hauptnummern,
3 Seiten), Lernblatt Teil 1 von 3 (Einheit 1 und 2, 6 Haupt-
nummern), Gesamt; 511 s. Fachlich fehlerfrei.

## 1 Befunde gegen ziel.md

1. Der Eintrag trägt. Tragendes Feld ist „Für schwache Schüler",
   Sprossen je Verfahrenstyp: das Blatt folgt der Kette eins zu
   eins. Gelesen wurden Verortung (Kl. 7), Lerneinheiten,
   Typen je Lerneinheit, Voraussetzungen, Merkkasten (wörtlich),
   Typische Fehler, Prüfungsform (Zielmarke). Nicht gelesen:
   Status, Offene Punkte, Prüfliste – richtig.
2. Schnitt: Der Prompt schnitt wegen seines Budgets (sechs
   Hauptnummern, fünf Seiten) in drei Teile; ziel.md § 1 kennt
   keine Teile.
3. Blatt 0 zu breit: alle fünf Erkennungsschritte drauf, auch die
   zu Einheit 4 und 5; Aufgabe 9 führte Prozentwert, Prozentsatz,
   Grundwert ein, bevor das Blatt sie lehrt. Dahinter ein
   Konflikt: Der Katalogabschnitt schickt Erkennungsschritte auf
   Blatt 0, Prompt 2.1 macht sie zur Vorstufe der Hauptnummer,
   ziel.md nennt Blatt 0 „eine Stufe zurück".
4. Verfremdung: Aufgabe 6a war 2018-OS-K7a mit Originalzahlen
   und -kontext (2 von 16 Pfannkuchen, 2 : 14), ohne Jahr. Quelle
   war „Typische Fehler", das die Originalzahlen nennt.
5. Kettenlücken in Teil 1: „Umkehrung: zu einem Prozentsatz ein
   Zahlenpaar" fehlte; die höhere Marke der Einheit 1 (eine von
   zwei Tabellenaussagen falsch) fehlte.
6. Dreisatz: Eintrag sagt „in einer Tabelle", der Chat setzte
   keine Tabelle.
7. Anweisungen gebündelt („(a–d) … (e–h) … (i–k)"): Muster der
   Aufgabe-1-Regel des Prompts, von Blatt 0 geerbt.
8. Sterne, Legende, Kasten, Hilfe-Seite: aus dem alten Prompt,
   kein neuer Befund.
9. Beispiele: Der Chat bildet eigene Beispiele mit eigenen
   Zahlen; der Merkkasten wird als Beispielquelle nicht gebraucht.
10. Bauzeit: Blatt 0 nach etwa 5,5 min (mit 404-Umweg und drei
    babel-Korrekturen), Teil 1 danach in 2 min. Die Vorabausgabe
    bringt drei bis fünf Minuten.
11. Betrieb: Projektanweisung war v3.34; deren Vorlagen-URL zeigt
    auf mathe-nachhilfe, mathblatt.sty liegt in blattbau (404,
    Ersatzlayout).

## 2 Beschlüsse (Lehrer, 22.09.2026)

- A: ein Lernblatt, alle Einheiten des Katalogs, kein Budget,
  kein Schnitt; Bau und Ausgabe in Reihe – Blatt 0, je Einheit
  ein PDF, am Ende Lernblatt und Gesamt mit Verzeichnis der
  Einheiten (nur wenn mehr als eine Einheit; nie auf Blatt 0,
  Fokus, Probeprüfung).
- Blatt 0: nur Fertigkeiten, je eine Hauptnummer mit eigener
  Anweisung; Reihenfolge nach erster Verwendung („– Einheit n"),
  bei Gleichstand Lehrplanfolge; Erkennungsschritte ins Haupt-
  blatt als Vorstufe der Einheit, vor der sie stehen.
- Aufgabennamen: jede Hauptnummer trägt Einheitstitel plus
  Formwort des Prompts; gemischte Aufgaben „Gemischt". Ob die
  Einheitstitel Schülersprache sind, wird nach Lauf 2 geprüft
  (271 Titel, Sek I zuerst).
- Verfremdung mit Jahr; keine Zahl aus Kasten, Beispiel oder
  Original in einer Teilaufgabe.
- Anweisung gilt für die unmittelbar folgenden Teilaufgaben.
- Dreisatz als zweispaltiges Schema, nie als Doppelpunktzeile;
  Doppelpunkt als Geteiltzeichen bleibt.
- Hilfe-Seite fällt; Kasten nur auf „mit kasten"; „Lernblatt
  kurz" und Testformat entfallen (ziel.md § 3).
- Leerer Kasten zum Selbstausfüllen: nicht entschieden, einmal
  auf Zuruf bauen.
- Vorgehen: Prompt v4.0 gebaut (Abschnitt 0–2 neu, 3–6 ange-
  passt), als Projektanweisung eingesetzt; Ablage in blattbau
  nach Lauf 2 mit Befund.

## 3 Befunde für den Katalog (nicht geändert)

- Von 62 Einträgen mit Einheitsangabe in den Fertigkeitszeilen
  sind 14 nach erster Verwendung sortiert, 48 nicht. Der Prompt
  sortiert selbst; Umsortieren ist nicht nötig.
- Blatt-0-Umfang: Median sechs Fertigkeiten, vier Erkennungs-
  schritte; 31 von 72 Einträgen haben elf oder mehr Zeilen.
  Prozentrechnung (6 + 5) ist der Normalfall.
- „Typische Fehler" nennt Originalzahlen; Verfremdung ist Regel
  des Prompts, nicht des Katalogs.
- Abschnittsname „Voraussetzungen (Blatt 0)" führt weiter die
  Erkennungsschritte, die nicht mehr auf Blatt 0 gehen; der
  Prompt liest sie dort als Vorstufe. Umbenennen erst, wenn
  Lauf 2 die Regel bestätigt.
- Zwei Befunddateien der Wurzel (befund-geltung-2026-09-21.md,
  befund-inkonsistenzen-2026-09-21.md) stehen nicht in README.md.

## 4 Nächster Schritt

Lauf 2: Prozentrechnung mit v4.0, Eingabe „prozentrechnung".
Auswertung: Reihe und Zeiten je Einheit, Blatt 0 aus sechs
Fertigkeiten, Vorstufen, Titel, Verzeichnis, Verfremdung mit Jahr,
Qualität der späten Einheiten.
