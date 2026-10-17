# Übergabe verbessereBlaetter – 2026-10-17 (Chat „Durchsicht P10 5“, Opus)

Eigene Datei, weil mehrere Chats nebeneinander laufen (Bau:
uebergabe.md; Bau 4: Schulbuch-Register). Vorherige: archiv/
uebergabe-durchsicht-2026-10-16-mittag-4.md. Nach plan.md Linie 8
kein eigener nächster Schritt; Entscheidungen nur aus plan.md § 10
(16.10. o; 17.10. a–d).

## 1 Ziel

P10-Prüfungsblätter in der Form „Kapitelblatt“ fertig und bestellbar,
gebaut ohne Modell aus Zuordnung und Wortlaut; danach Abitur GK in
derselben Form.

## 2 Arbeitsgrundlage

- Eigene Dateien und Regel gegen Überschneidung: plan.md § 7
  „Überblick – jetzt bis Mo 19.10.“, Absatz „Dateien je Strom“, C.

- plan.md § 7 (Absatz „Jetzt Durchsicht/P10, in dieser Folge (Lehrer
  17.10.)“), § 10 17.10. (d) mit den Listen „gilt weiter“/„ersetzt“.
- Muster: aufgabenbank bau/kapitel/2026-10-17/quadratische/ (blatt,
  loesung, je Abschnitt A, B, B1, B2, C, D Blatt und Lösung), Setzer
  werkzeuge/kapitelblatt.py (`python3 werkzeuge/kapitelblatt.py
  --kapitel quadratische --datum <d>`), Daten mathe-nachhilfe
  msa/kapitel-p10/quadratische.csv (aus msa/buchkapitel-p10.csv).
- Register der Schulbücher: aufgabenbank-privat buecher/ (Jesse
  fertig, 1 045 Aufgaben; Felder handgriff, darstellung, frage,
  antwortform, schwere). Baut der Chat Bau 4.
- Kommentare des Lehrers: aufgabenbank bau/durchsicht/
  durchsicht-3-funktionen/, durchsicht-3b-funktionen/ (kommentare.csv).
- Prüfskripte: werkzeuge/loesung-pruef.py (0), regel-pruef.py (alte
  Blattform; Kern entfernt).

## 3 Arbeitsstand

- Erledigt 16./17.10.: Pflichtteile in alte Blätter ab PA20 (Setzer,
  Daten, regel-pruef 0 ab PA20); Lehrer beanstandete die Form
  grundsätzlich → Kapitelblatt (17.10. b–d), Muster PA30 mit neun
  Satzpunkten des Lehrers (Graph oben bündig, Text in der Zeile der
  Nummer, Karo neben dem Graph, „*“ = nur FOR, PA30, x₁; x₂ in einer
  Zeile, je Abschnitt Blatt und Lösung). PA30: Blatt 9 S., B1 2, B2 3.
- Bestimmungsschlüssel quadratisch (Chat 17.10., nicht in Daten):
  1 zwei Graphen, gemeinsame Punkte → Schnittpunkte; 2 gesucht x →
  Quadratische Gleichungen; 3 Scheitelpunkt → B1; 4 Gleichung → B2;
  5 y/Punkt/Tabelle → Punkte und Funktionswerte; zuletzt Gesuchtes
  entscheidet; wahr/falsch nach Mehrheit. Weicht von
  buchkapitel-p10.csv ab bei 2026-FOR-K5d (→ D) und 2025-OS-K5b,
  2023-OS-K4b (nicht teilen, ganz B2) – noch nicht umgesetzt.
- Lehrer hat dem Chat Bau 4 gesagt (oder sagt es): zuerst Duden 9
  („Buch_Mathe_Kl9.pdf“, „Wissen – Üben – Testen 9“), dann „10. 1–4“.
- Keine Agenten laufen. Alte P10-Blätter bleiben bestellbar;
  bestellen-test 46/49 (rot: PG10/PG20/PG40/PG80/PG90 ohne
  Tafelwerk-Feld – mit der neuen Form nicht mehr nachziehen).

## 4 Verbindliche Entscheidungen und Rahmen

- plan.md § 10 17.10. (a) kein Kern/Formelkasten, Tafelwerk nennen
  oder Seite fragen; (b) wortgleich einmal, Jahre in der Marke; (c)
  Abschnitte = Buchkapitel + fester Abschnitt „Punkte und
  Funktionswerte“ (Versuch); (d) Kapitelblatt, je Abschnitt höchstens
  ein Begriff und ein Einstieg (Weg B), Rechenraum voll.
- Marken „(16.10. n)“ in den Gliederungen ab PA20 und in
  mehr-p10/handgriffe meinen plan.md 16.10. (o) (Eintrag wurde beim
  Zusammenführen umbenannt; 16.10. (n) ist „Lösungen der Originale“).
- Messwerte: Woche 48 → 51 % (17.10. morgens) für Pflichtteile und
  Muster (Agenten ≈ 1,0 Mio); danach zwei Sonnet-Nachaufträge 0,14 +
  0,19 Mio, Anzeige nicht abgelesen. Reset Mo 18:00.
- Lehrer: kleiner Bildschirm, UTC+2 (die Uhr des Arbeitsrechners
  geht nicht nach seiner Zeit – Uhrzeit von ihm oder get_device_info
  nehmen). Muster und Stichprobe statt jedes Blatt (Linie 6);
  Satzfehler prüfen Skript und Kritiker, nicht er.

## 5 Offen und Verworfenes

- Offen: Übersetzung Register-Merkmale ↔ Katalogfeld „gesucht“;
  Mischaufgaben (Aussagen prüfen, Flächenanteil) je Gebiet;
  Kandidat für kandidaten.md „beschlossen = erst umgesetzt, wenn
  Regeldatei und Skript es tragen“ – Lehrer hat nicht entschieden.
- Verworfen: Abschnitte nach Handgriff/„gesucht aus gegeben“ als
  Hauptordnung (bleibt nur Reihenfolge innerhalb); Teile aus
  Originalen herauslösen; Mehr als eigene Datei; Kern; Formelkasten;
  B auf 3 Seiten durch Aufgaben nebeneinander (B1/B2 einzeln bestellt).

## 6 Nächster Arbeitsschritt

plan.md § 7, Absatz „Jetzt Durchsicht/P10, in dieser Folge (Lehrer
17.10.)“.
