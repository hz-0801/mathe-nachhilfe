# Übergabe verbessereBlaetter – 2026-10-09 (Chat 08./09.10., Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-08b.md. Nach plan.md Linie 8
nennt diese Übergabe keinen eigenen nächsten Schritt: maßgeblich ist
plan.md § 7 („Jetzt“).

## 1 Ziel

plan.md § 1: Der Lehrer bestellt mit wenigen Wörtern und bekommt in höchstens
3 Minuten drei PDFs, die ein guter Didaktiker so bauen würde – zuerst P10,
dann Abitur GK.

## 2 Arbeitsgrundlage

Einstieg über CLAUDE.md (beide Repos). Rangfolge: mathe-nachhilfe plan.md →
aufgabenbank bau/bauregeln.md → bau/bauauftrag.md → bank.md → begriffe.md.
Belege: pruefstand-2026-10-09/ (vier Leserberichte, Planentwurf), aufgabenbank
bau/befunde-M2.md, befund-selbstlernheft-2026-10-09.md.

## 3 Arbeitsstand

- M0 (K4W „Hypotenuse“, Lehrer „besser“), M1 (Plan, Einstieg, Bauauftrag,
  Felder; Haiku-Abnahme) und M2 (T6B „Kathete berechnen“ von einem Agenten
  nach Bauauftrag gebaut, 41 min, ≈ 0,23 Mio Token + Kritiker; Lehrer
  „insgesamt gut“; werkzeuge/setzer.py setzt T6B in 3,7 s) sind erledigt.
- Ende M2 eingearbeitet: „Für wen du baust“, je Schritt Formel, Beispiel,
  leichtere und gleichwertige Aufgaben (nur Bank), Thema-Weg je Thema,
  Mischen in der folgenden Einheit, Originalliste nur auf Prüfungsblättern,
  Selbstlernheft als Sorte beschrieben (Wahl offen).
- Archiviert: ziel.md, faellig.md, blatt-konzept.md, layout-befunde,
  Streichliste, drei Vorschläge vom 27./28.09. (Stubs verweisen).

## 4 Verbindliche Entscheidungen und Rahmen

- plan.md gilt (Lehrer 09.10.: „plan gilt“); ändern nur der Lehrer.
- Der Lehrer will nur die Linien entscheiden; Kleinigkeiten entscheidet der
  Chat und sagt sie in einem Satz.
- **Token sparen, vom Ende her gedacht (Lehrer 09.10.):** Das
  Wochenkontingent ist knapp. Rückwärts rechnen: Ende = jede Bestellung ohne
  Modell aus Lernweg + Bank. Jeder Token muss Daten erzeugen, die der Setzer
  nutzt; Lesen nur, was im Bau landet. Messwert: eine gebaute Einheit ≈
  0,3–0,4 Mio Token ≈ 1 Wochenpunkt; 54 P10-Kerneinheiten ≈ 55 Punkte;
  dazu Abitur GK. Darum: Runden je Woche planen und nach jeder Runde
  ablesen; Bau-Agent Opus, Kritiker kurz (Fable, ≤ 400 Wörter), Prüfungen
  mit Skripten, Abnahme-Checks mit Haiku; keine Leser-Runden über den
  Bestand mehr; Chat kurz halten und früh umziehen; Setzer statt Modell.
- Abo kann verlängert werden, wenn geliefert wird.
- Messwerte 09.10.: fünf Fable-Leser + Kritiker ≈ 1,4 Mio → Woche +4,
  Fable +6 Punkte; M2 (Bau + Setzer) ≈ 0,4 Mio → Woche +1. Stand 09.10.
  mittags: Woche 42 %, Fable 18 %; Reset Montag 18:00.

## 5 Offen und Verworfenes

- Feld `satz` doppelt aufgabe/loesung; setzer.py setzt die Originalliste noch
  auf Lernblättern – beides in der ersten Setzerrunde von M3 beheben.
- Projektanweisung (3 100 Wörter, davon ~1 100 über tote Wege) ist gekürzt:
  anweisungen/projekt-verbessereBlaetter.md, Stand 2026-10-09 – der Lehrer
  ersetzt sie im Claude-Projekt.
- Verworfen: K4W nachträglich zerlegen (wird in M3 neu gebaut); Leser-Runde
  „alles neu lesen“ wiederholen; Bau auf jede Bestellung als Regelweg (bleibt
  Notweg für persönliche Hefte).

## 6 Nächster Arbeitsschritt

plan.md § 7 „Jetzt“: M3 Runde 1 – zwei Agenten nebeneinander: Pythagoras
ganz (Hypotenuse neu, Umkehrung, Das Dreieck erst finden, Thema-Weg) und
Prozentrechnung; Schätzung 2–3 Mio Token; vorher Ablesen, danach Ablesen;
Lehrer sieht eine Stichprobe. Modell: Opus im Chat und für Bau-Agenten.
