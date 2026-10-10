# Übergabe verbessereBlaetter – 2026-10-10 (Chat 09./10.10., Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-09.md. Nach plan.md Linie 8
nennt diese Übergabe keinen eigenen nächsten Schritt: maßgeblich ist
plan.md § 7 („Jetzt“).

## 1 Ziel

Der Lehrer will bessere, andere und mehr Aufgaben in Katalog und Bank,
aus denen ein Setzer ohne Modell gute Blätter macht (plan.md § 1).

## 2 Arbeitsgrundlage

- plan.md (mathe-nachhilfe) § 7 „Jetzt“: Stufen der Ketten füllen.
- Maß für Aufgaben: aufgabenbank bau/proben/2026-10-10/vorlage-holger/
  (README nennt jede Nummer mit den Worten des Lehrers).
- Maß für Blätter: M74 (bau/proben/2026-10-09/hypotenuse-berechnen/, ohne
  Nr. 2/3) und T6B (`werkzeuge/setzer.py --kennung T6B --sorte tisch-alt`).
- Gerüst: Stufenketten der Bank (bank/<thema>/e<n>.jsonl, Felder
  kette/sprosse/sprosse_text; z. B. pythagoras e1 Kette „Hypotenuse“ 0–15),
  Musterbeispiele bank/<thema>/muster.md.
- Befunde: aufgabenbank bau/befunde-M3.md, letzter Block (10.10.).

## 3 Arbeitsstand

- Runde 1 (09.10.): 9 Blätter (Pythagoras, Prozent) nach altem Auftrag,
  Lehrer: M74 „ziemlich gut“, T6B „nah an früher“.
- Runde 2 (09./10.10.): 38 Einheiten „P10 oft“ nach Musterauftrag, je mit
  Fable-Kritiker und Nachbesserung; gedriftet (gröber, weniger Aufgaben,
  Hinweise in Aufgaben, Ziel je Abschnitt). Aufgaben bleiben als Vorrat.
- Setzer: drei Sorten (selbst, tisch, tisch-alt) aus denselben Daten;
  Felder erklaerung, stufe; Layout-Zeilen „Layout: voll“, „Grau:“;
  T6B byte-gleich. Kennung reservieren (`--reserviere`).
- Nachrüst-Test H7U (Hypotenuse): Versuch 2 „besser“; danach Lehrer-
  Vorlage von Hand gesetzt.
- bau/bauauftrag.md ist der Stand nach dem Nachrüst-Test (Musterauftrag +
  Stellschrauben) – für das Füllen der Stufen nicht geprüft.

## 4 Verbindliche Entscheidungen und Rahmen

- Linien entscheidet der Lehrer, Kleinigkeiten der Chat (ein Satz).
- Lehrer 10.10.: keine neuen Regeln aus Einzelbefunden; Wünsche als Befund
  sammeln, Regel erst nach Wiederholung und mit seiner Zustimmung.
- Lernblätter nur neue Aufgaben; Original nur Vorbild, kein Muss.
- Keine Rätsel-/Herleitungsbilder (Kästchen-Quadrate).
- Kein Blatt an den Lehrer ohne unabhängigen Bildvergleich mit dem Maß
  (Fable-Prüfer); Selbsturteil der Bau-Agenten reicht nicht.
- Messwerte: Woche 42 → 48 (Runde 1) → 68 (Runde 2) → 69 % (Test);
  Fable 18 → 20 → 32 %; ≈ 0,75 Mio Opus-Token je Wochenpunkt; Einheit
  Runde 2 ≈ 0,4 Mio inkl. Kritik. Reset Montag 18:00.
- Agenten: eigener Arbeitsordner /root/work/<x>, Hilfsskripte dort,
  Kritiker startet der Chat (Unteragenten können keine starten).

## 5 Offen und Verworfenes

- Offen für den Lehrer: Klasse Brüche E1 (7 statt 5), Terme-Folge,
  Kosinussatz nur Vorrat, Form des Tischblatts (Setzer).
- Verworfen: Musterauftrag als alleiniger Bauauftrag (Agenten erfinden
  den Aufbau jedes Mal neu → Drift, nicht wiederholbar); Regeln nach jeder
  Welle in die Aufträge schreiben; „höchstens 6 Seiten“.

## 6 Nächster Arbeitsschritt

plan.md § 7 „Jetzt“.
