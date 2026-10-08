# Übergabe verbessereBlaetter – 2026-10-09 (Chat 08./09.10., Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-07b.md.

## 1 Ziel

Der Lehrer bestellt im Projekt erzeugeBlatt(Bank) mit wenigen Wörtern und
bekommt in Minuten ein gutes Blatt, Unterricht und Prüfung, zuerst P10 und
Abitur GK. Maßgeblich ist `plan.md`.

## 2 Arbeitsgrundlage – beim Chatstart in dieser Folge

0. `plan.md` – der Plan (große Linien, Zweck der Blätter, Meilensteine,
   § 5 „Jetzt“ mit Richtung Serie und offener Liste). Abgleich nach § 0 dort.
1. `tafel.md` – Fortschrittstafel (neu bauen: `python3 werkzeuge/tafel.py
   --bank ../aufgabenbank`); Abnahmen in `abnahme.csv`.
2. Prüfungsgliederung `msa/gliederung/`, `abitur/gliederung/` (Format
   `msa/gliederung/README.md`, Stand `msa/gliederung-stand.md`); Leser
   `werkzeuge/gliederung.py`, Sichten `werkzeuge/gliederung-sichten.py`.
3. aufgabenbank `bau/bauregeln.md` (Regelrahmen Stand 07.10., bestätigt 08.10.).
4. aufgabenbank `werkzeuge/pruefheft.py` (liest die Gliederung) und das
   Prüfstein-Heft `bau/pruefheft/pruefstein-2026-10-09/kurvenuntersuchung-normal/`.
5. aufgabenbank `eingang/` – Protokolle der Blatt-Chats (erzeugeBlatt(Bank)
   v5.8 läuft parallel im Unterricht); gesammelt auswerten, keine Sofortregel.

## 3 Arbeitsstand

Erledigt 08./09.10.: Plan angelegt und entschieden (W1–W4, Entscheidung A:
Bank + Katalog + Prüfungsgliederung); Regelrahmen geprüft (W3); Probelauf im
Blatt-Projekt (58 s, Pythagoras); Fortschrittstafel; Prüfungsgliederung als
Datei je Kapitel, Steckbriefe aufgegangen, Programm liest sie (Fokusblätter
wortgleich); Abitur-GK-Zuordnung aller neun Kapitel; Bank:
ableitungsgraph-und-funktionsgraph gefüllt (102), Prüffehler 0, Lücke Netz
gefüllt; Kurvenuntersuchung als Sek-II-Prüfstein gebaut (31 S.).
Lehrer zur Kurvenuntersuchung: liest ab Nr. 7 nicht weiter – Erkennfragen
ohne Bezug (Nr. 4 Ball ≙ Nr. 6 Ofen nicht erkannt), 52-mal „Gegeben ist …“,
nur Teilaufgaben, zu lang. Daraus Zweck der Blätter und Richtung Serie.

Nicht umgesetzt (Konsistenz): ziel.md (Sorten, Länge § 1, Steckbrief-
Verweise) und bauregeln.md (2.2, 1.2, 3.10, 9.1) folgen erst nach den
Proben (offene Liste in plan.md § 5). Säulendiagramm lesen: 2 fehlen.

Messwerte: Woche 30 → 33 %, Fable 7 → 12 % für fünf Agenten (zusammen
1,1 Mio Token); Chat selbst kaum messbar.

## 4 Verbindliche Entscheidungen

- plan.md gilt; ändern nur der Lehrer, vorher große Linien vorlesen.
- Bemerkungen des Lehrers sind Richtungen; eine Richtung ist ein Satz
  (Zweck); Mittel am Blatt. Keine Regel aus einem einzelnen Blatt.
- Zweck: Prüfungsblatt bereitet so effizient wie möglich auf die echten
  Prüfungsaufgaben vor; ein Blatt ist so lang, wie sein Zweck es braucht.
- Stark-Heft (P10, Abitur) und Bildungsserver (FHR) halten die Originale;
  unser Blatt ist die Brücke dorthin.

## 5 Offen und Verworfenes

- Layout-Befunde gesammelt (keine Regel): Koordinatensystem nur so groß wie
  die Werte; Tabelle und Gitter nebeneinander (Platz); Erkennfragen aus der
  Lage der folgenden Aufgaben statt fremder Beispiele.
- Verworfen: Vorschlag B (Katalog nach Prüfungsstufen umbauen); Steckbrief als
  eigenes Objekt; Wiederkehr in der Serie (vorerst, beißt sich mit schmal).

## 6 Nächster Arbeitsschritt

1. Programmfehler beheben, die gegen geltende Regeln verstoßen: Zählung im
   Stufenkopf weg (1.3), Fuß nur Ergebnisse (6.2), kurzer Kopf mit
   Prüfungsverb statt „Gegeben ist die in ℝ definierte …“; dazu Lücke
   Säulendiagramm. Ein Agent, Schätzung 0,3 Mio, Go des Lehrers einholen.
2. Proben der Serie: Einstiegsseite Kurvenuntersuchung, Portion 1
   Kurvenuntersuchung (Prüfung, Grundvorstellung je Abschnitt), Portion 1
   eines P10-Lernblatts. Dem Lehrer zeigen; offene Liste am Blatt entscheiden.
Modell: Opus im Chat; Agenten Opus, Urteilsarbeit Fable (Fable-Kontingent
verfällt Montag 18:00).
