# Buchstufen P10

Angelegt 12.10.2026 nach pruefung.md § 5 „Stufen wie im Buch, leere
bleiben sichtbar“ und „Handreichung P10“ (Lehrer 12.10.).

## Zweck

Die Stufenliste je P10-Kapitel kommt aus Lehrbuch und Rahmenlehrplan,
nicht nur aus den Prüfungen; gefüllt wird sie aus den Prüfungen. Was die
Prüfung nie fragt, soll der Lehrer sehen: eine Zeile mit leerer Spalte
`jahre` heißt in der Handreichung „nicht geprüft seit 2016“; auf dem
Blatt steht sie nicht. Stufen heißen nach dem Gesuchten, in
Schülersprache (pruefung.md „Stufen heißen nach dem Gesuchten“,
gemeinsam.md „Namen“). Keine Stufe über Niveaustufe G.

## Spalten (`buchstufen-p10.csv`, Semikolon, UTF-8)

- `kapitel` – Schlüssel wie `gliederung/<kapitel>.md`.
- `einheit` – Abschnitt (Zuschnitt) der Gliederung; Stufen der
  Gliederung ohne Zuschnitt stehen in der nächstliegenden Einheit.
- `folge` – Reihenfolge im Kapitel, wie im Buch (1, 2, …).
- `stufe` – Name nach dem Gesuchten.
- `stufe_gliederung` – Stufe der Gliederung bzw. der Zuordnung, deren
  Originale die Zeile trägt; leer, wenn keine Gliederungsstufe passt.
  Eine Gliederungsstufe kann auf mehrere Buchstufen verteilt sein
  (z. B. „Gerade zeichnen und ablesen“ → zeichnen · Gleichung ablesen ·
  Nullstelle); die Teilung folgt dem Katalog-`typ` der Originale.
  „gemischt, ohne Überschrift je Aufgabe“ (Zuordnung) heißt in der
  Gliederung „erst entscheiden, dann rechnen“.
- `jahre` – Prüfungsjahre 2016–2026 der Hauptplätze, jüngstes zuerst
  (OS und FOR; Hauptplätze = `katalog_ids` der Zuordnung ohne
  `nebenplaetze`). Bei der Schlussstufe „erst entscheiden, dann
  rechnen“ (nur Nebenplätze) die Originale der Gliederung. Bei Zeilen
  ohne `stufe_gliederung` die Originale aus dem Katalog, die keinen
  P10-Hauptplatz haben (z. B. Winkel an Parallelen, Halbwertszeit).
  Leer = nie geprüft.
- `quelle` – RLP-Niveaustufe (Teil C Mathematik 2023,
  `quellen/quelle-rlp-teil-c-mathematik-2023.txt`, Zitate in den
  Katalogeinträgen) und Lehrwerk-Abschnitt „Fundamente <Klasse>,
  <Abschnitt>“ (Cornelsen, Fundamente der Mathematik, Ausgabe B
  Berlin-Brandenburg ab 2024, Inhaltsverzeichnisse in
  `quellen/quelle-cornelsen-fundamente-bb-ausgabeb2024-*.txt`);
  Trenner „ · “.

## Leser

Die Handreichung P10 (Landkarte je Kapitel mit Häufigkeitswort, Jahren
und „nicht geprüft“) und später der Setzer. Die Datei wird von Hand
gepflegt; ändern sich Stufen der Gliederung oder kommt ein neues Heft,
werden `stufe_gliederung` und `jahre` nachgezogen.
