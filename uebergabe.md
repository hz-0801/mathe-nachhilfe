# Übergabe verbessereBlaetter – 2026-10-14 vormittags (Chat „start 32“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-13-mitternacht.md. Nach
plan.md Linie 8 nennt diese Übergabe keinen eigenen nächsten
Schritt. Entscheidungen nur aus plan.md (§ 10, 14.10.2026 a–e).

## 1 Ziel

P10 fertig: Der Lehrer bestellt mit wenigen Wörtern und bekommt
schnell gute Blätter aus Daten, ohne Modell beim Setzen (plan.md
§ 1). Schüler bekommen die Bestellkarte und die Blätter auf Zuruf;
das Gesamtheft ist das Prüfstück des Lehrers.

## 2 Arbeitsgrundlage

- plan.md § 7 (Absatz „14.10. vormittags erledigt … Jetzt“), § 10
  (14.10. a–e), § 8 (Messwerte).
- Daten: mathe-nachhilfe msa/gliederung/*.md – Anzeigenamen,
  „Kennung neu“ (PG10 … PS50, Lernfolge), Feld „Regine: S. n“,
  Heranführungen. Sammlung: aufgabenbank bau/heranfuehrungen-p10.md.
- Skripte (aufgabenbank werkzeuge/): pruefheft.py v0.13 (Setzer),
  bestellkarte.py (Karte je Gebiet; Folge noch als Liste im
  Skript), gesamtheft.py (Karte alt + alle Blätter, ohne Lösungen;
  Ordnerliste im Skript). mathe-nachhilfe
  werkzeuge/anzeigenamen-pruef.py (prüft noch gegen das veraltete
  pruefung.md § 2).
- Blätter: aufgabenbank bau/pruefung/2026-10-14/<ordner>/ (19),
  bestellkarte.pdf (3 S.), gesamtheft-p10.pdf (alter Stand vor den
  neuen Namen). Neusatz: Schleife über die Liste EINHEITEN in
  werkzeuge/gesamtheft.py (kapitel, einheit, ordner),
  `python3 werkzeuge/pruefheft.py --kapitel <k> --art p --einheit
  "<e>"`, Ausgabe nach bau/pruefung/<datum>/<ordner>/, Ordner
  bau/pruefheft/*-p-*-<datum> danach löschen; Register-Pfade auf
  bau/pruefung/<datum>/<ordner> umstellen.
- Tafelwerk: aufgabenbank-privat formelsammlung/regine-sek1.md
  (Paetec Sek I, S. 5–43, Seitenregister); duden-sek1.md daneben.
- Basis: Original-Basisteile aller 14 Hefte privat
  basis-originale.jsonl, gesetzt per `zusammenbau.py --zettel
  original --heft <jahr>-<papier>`; Basiszettel BAS-Z1–Z10
  (bau/zettel/); zurückgestellt (plan.md § 9).

## 3 Arbeitsstand

- Erledigt 14.10.: Regine-Abschrift; Heranführungen als Daten (45
  Stufen mit Einstieg, 29 leer); Pythagoras getrennt; Probe HK32
  Grundwert, K9X2 Kenngrößen (Seitenfrage + Erkennen); Gesamtheft;
  Bestellkarte; Abschnittsnamen neu und Lernfolge; Fallbeschreibung
  neben Skizze entfernt (Setzer v0.13).
- Lehrer hat die Namen auf der Karte gesehen; geändert nur
  Punktprobe und „Gerade und Parabel“.
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Woche 26 % (Anzeige 14.10. morgens), Fable 24 %, Reset Montag
  18:00. Nachtpaket: Agenten 0,80 Mio Opus-Token ≈ 1 Punkt
  (Schätzregel ≈ 0,9 Mio je Punkt hält).
- Der Lehrer ist ungehalten über Kommentare auf Gedrucktem und über
  Behauptungen, etwas gebe es nicht (Basisblätter): vor jeder
  solchen Aussage register.csv, bau/, aufgabenbank-privat
  durchsuchen.
- Uhrzeit: Lehrer arbeitet in UTC+2.

## 5 Offen und Verworfenes

- Lineare endet mit „Gerade und Parabel“, die Parabel kommt erst
  zwei Blätter später (Lernfolge); Lehrer nicht entschieden.
- Prozent vor Grundwert: Folge der zwei Prozent-Blätter nicht
  geprüft (Umwandeln vorn, Prozentwert/Grundwert danach).
- Volumen und Oberfläche: Stufenfolge (Formeln umstellen vor
  Oberfläche) nicht nach dem Muster Flächen.
- Basisteil auf der Karte: nach Jahr, jüngstes zuerst, Kennung PB25
  (Vorschlag, zurückgestellt).
- Verworfen: Basiszettel nach Gebiet ordnen (Basisteil ist gemischt
  wie in der Prüfung).

## 6 Nächster Arbeitsschritt

plan.md § 7 (Folge „14.10. vormittags erledigt … Jetzt“, Schritt 1).
