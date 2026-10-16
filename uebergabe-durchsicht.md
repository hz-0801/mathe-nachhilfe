# Übergabe verbessereBlaetter – 2026-10-16 mittags (Chat „Durchsicht P10 3“, Opus)

Eigene Datei, weil zwei Chats nebeneinander laufen; die Übergabe des
Chats „Bau“ ist uebergabe.md. Vorherige: archiv/uebergabe-durchsicht-
2026-10-16-morgens.md. Nach plan.md Linie 8 kein eigener nächster
Schritt; Entscheidungen nur aus plan.md (§ 10, 15.10. l–y, 16.10.
a–m).

## 1 Ziel

Alle P10-Blätter vom Lehrer kommentieren lassen, jeden Kommentar
beantworten und entscheiden lassen; umsetzen, sobald ein Block
entschieden ist, damit der Lehrer die Wirkung beim Weiterlesen sieht.

## 2 Arbeitsgrundlage

- plan.md § 7 (Absatz „Durchsicht P10“, Stand 16.10. mittags – dort
  die Folge (1)–(3)), § 10 (16.10. a–m), § 8 (Messwerte).
- Regeln: gemeinsam.md „Form der Lösung“ (16.10. l, m); Prüfskript
  aufgabenbank werkzeuge/loesung-pruef.py (meldet 0); der Setzer
  (werkzeuge/pruefheft.py) setzt P10 nur, wenn es nichts meldet.
- Stand der Blätter: aufgabenbank bau/pruefung/2026-10-16/<ordner>/pdf/
  (<Kennung>-blatt, -loesung, -mehr); Mappe aufgabenbank-privat
  bau/mappe/2026-10-16/mappe-p10.pdf (280 S., ohne Lösungen).
  Neusatz: `python3 werkzeuge/neusatz-p10.py --datum <d> [--nur …]`,
  dann `python3 werkzeuge/mappe-p10.py --datum <d> --ohne-neubau`
  (zusammen ≈ 25 min, im Hintergrund laufen lassen).
- Durchsicht: Kommentare bau/durchsicht/kommentare-mappe-2026-10-15.csv
  (Geometrie), kommentare-mappe-2026-10-16.csv (PA10),
  kommentare-loesung-pg50-2026-10-16.csv; Antworten pg10–pg90.json,
  pa10.json. Werkzeug: `python3 -I werkzeuge/kommentare.py <pdf>
  <ordner>`, dann `python3 -I werkzeuge/durchsicht.py <json> <ordner>
  <aus.html>`; als Artifact „Durchsicht P10“ veröffentlichen.

## 3 Arbeitsstand

- Durchgesehen und entschieden: Geometrie PG10–PG90, Lineare PA10.
- Umgesetzt (Schritt C Sparfassung): Setzer v0.18 (A, B, C; Kästchen
  ohne Buchstaben; „Mehr: n“; Mehr als eigene Datei; Lösungsblatt;
  Formelkasten, Kern, Begriff; Bruch), Daten Geometrie und Lineare
  (Namen, Figuren als ein Blatt, Skizzen, Lineare ohne Gerade und
  Parabel), Lösungen in neuer Form (162 Mehr-/Katalogzeilen, 33
  Einstiegs-Lösungen).
- Offen zur Umsetzung: 16.10. m (Lösungszeile) – noch nicht gebaut.
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Woche 46 % (Anzeige 16.10. morgens), Fable 24 %, Reset Mo 18:00.
  Schritt C: Agenten 0,57 Mio, Runde ≤ 2 Punkte (zweiter Chat lief
  parallel). Lösungen neu: Agent 0,28 Mio (nicht gesondert gemessen).
- Agenten halten die Schrittgrenze nicht (102 statt 60, 70 statt
  60) – Teile kleiner schneiden.
- Lehrer: kleiner Bildschirm; eine Frage je Nachricht, Wege mit
  Namen; Bilder helfen; „denke mit“ – ganzen Bestand durchsehen, bevor
  Folgepunkte kommen; vor Festlegungen nachsehen, was schon gilt
  (16.10.: Lösungsregeln standen seit 03.–06.10. fest und wurden nicht
  eingehalten). Lehrer arbeitet in UTC+2.
- Das Zusammensetzen läuft ohne Modell: fertiges Blatt < 1 s, frisch
  gesetzt ≈ 30 s; das Lösungsformat ist durch den Setzer gesperrt.

## 5 Offen und Verworfenes

- Offen: Platz neben großen Koordinatensystemen nur teilweise behoben
  (bis 25 % verkleinert); Antwort rutscht bei sehr großen Systemen
  noch darunter. Lineare nach dem Neusatz 5 Seiten – Teilen erst nach
  Durchsicht prüfen (16.10. h).
- Später (Lehrer 16.10.): Lösungsform auch fürs Abitur.
- Verworfen: zweite Spalte ganz weg (16.10., Weg B); Abschnittsköpfe in
  der Lösung; „je Handgriff eine Zeile“ (ersetzt durch m).

## 6 Nächster Arbeitsschritt

plan.md § 7, Absatz „Durchsicht P10“ (Stand 16.10. mittags, Folge
(1)–(3)).
