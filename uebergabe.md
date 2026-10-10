# Übergabe verbessereBlaetter – 2026-10-10 spät nachts (Chat „start 23“, Opus → Fable 5.1)

Vorherige Übergabe: archiv/uebergabe-2026-10-10d.md. Nach plan.md
Linie 8 nennt diese Übergabe keinen eigenen nächsten Schritt.
Entscheidungen nur aus plan.md (§ 3 Linien, § 11 Register).

## 1 Ziel

P10 fertig, ohne Abitur und Schulstoff aus den Augen zu verlieren: Der
Lehrer bestellt mit wenigen Wörtern und bekommt schnell gute, kurze
Blätter (plan.md § 1).

## 2 Arbeitsgrundlage

- plan.md – Ziel, Linien, § 7 „Jetzt“, § 11 Register.
- pruefung.md – Entwurf der Datei der Sorte Prüfung (aus offen.html und
  den Prüfungsteilen von bauregeln.md; § 2 der festgelegte
  P10-Zuschnitt; § 9 was aus offen.html nicht übernommen wurde und
  warum). Gilt erst nach „gilt“ des Lehrers; bis dahin offen.html.
- gemeinsam.md – Entwurf der gemeinsamen Datei (Rest von bauregeln.md
  plus G-Zeilen aus § 11). Gilt erst nach „gilt“; bis dahin
  bauregeln.md.
- msa/gliederung/*.md – Quelle des Zuschnitts; daraus erzeugen
  werkzeuge/gliederung-sichten.py die CSV und werkzeuge/
  skript-zuschnitt.py p10 die Übersicht msa/skript-zuschnitt-p10.md.
  CSV und Übersicht nie von Hand ändern.
- msa/befund-zuschnitt-{daten,geometrie,funktionen}-2026-10-10.md –
  Befunde der Fable-Kritiker, eingearbeitet; Beleg.

## 3 Arbeitsstand

Abgeschlossen in diesem Chat:
- plan.md § 7 Schritt 2 zur Hälfte: Entwürfe pruefung.md und
  gemeinsam.md geschrieben; P10-Zuschnitt an allen drei Gebieten
  gegen die echten Aufgaben 2022–2026 geprüft, korrigiert und vom
  Lehrer festgelegt (27 Einheiten, Einheit = Handgriff = Blatt).
- Offen in Schritt 2: der Lehrer liest pruefung.md und gemeinsam.md
  und sagt „gilt“ (oder nennt Änderungen); dann offen.html und
  bauregeln.md ablösen (Hinweiszeile oben, Archiv nach Schritt 3).
- Danach Schritt 3 (Bestand ordnen).

## 4 Rahmen

- Kontingent (Anzeige 10.10. spät): Woche 78 %, Fable 42 %; „geht
  Montag Morgen aus, Reset 18:00“. Lehrer 10.10.: Fable bis Montag
  18:00 wie Opus verbrauchen, sinnvoll (Lesart des Chats: bis auf
  etwa 10 % Rest); dieser Chat lief deshalb ab der Mitte auf Fable
  5.1.
- Messwert: enger Fable-Kritiker je Gebiet mit zwei Prüffragen ≈
  0,13 Mio Token, 2½ min, Befund 20 Zeilen, brauchbar;
  ≈ 0,25 Mio Fable je Fable-Punkt und je Wochenpunkt (plan.md § 8).
- Repo mathe-nachhilfe mit Schreibzugang angehängt (Modus Manuell,
  eine Karte); Klon unter /home/claude/mathe-nachhilfe. Die anderen
  Repos nur lesend unter /tmp.
- Fehler dieses Chats, nicht wiederholen: eine erzeugte Datei
  (skript-zuschnitt-p10.csv) direkt geändert statt ihre Quelle; ein
  Agent hat es nachgezogen.

## 5 Offen und Verworfenes

- Schlussstufe „erst entscheiden, dann rechnen“ hat vier statt sieben
  Nebenplätze (Skript lässt keinen Nebenplatz im eigenen Abschnitt
  zu); belassen.
- Stolpersteine für den Bau stehen in pruefung.md § 2 (Normalform
  vor Gleichsetzen, Winkelsumme vor Sinussatz, Baum-Sprossen vor
  „Baum ergänzen“, Länge Blatt Prozent).
- Offen aus voriger Übergabe unverändert: Bestellen in
  Alltagswörtern; „ein Blatt für alle“ Ende M3; Bauen nach Bedarf
  der aktiven Schüler; Projektanweisung erzeugeBlatt(Bank) als
  Verweis.
- Verworfen: eigenes Blatt „Pythagoras oder Winkelfunktion“ (die
  Prüfung führt selbst: a) Pythagoras, b) Winkel); Punktprobe als
  Stufe in Gerade/Parabel (Kopf-Schritt ist Einsetzen, wäre doppelt).

## 6 Nächster Arbeitsschritt

plan.md § 7 „Jetzt“.
