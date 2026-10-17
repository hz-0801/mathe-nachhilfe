# Übergabe verbessereBlaetter – 2026-10-17 (Chat „Bau 4“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-16-bau3.md. Nach
plan.md Linie 8 kein eigener nächster Schritt. Entscheidungen nur
aus plan.md § 10 (16.10. n; 17.10. e, f – Kennungen nach der
Umnummerierung durch den Chat Durchsicht). Daneben läuft der Chat
„Durchsicht P10“ (uebergabe-durchsicht.md).

## 1 Ziel

P10 fertig und verbessert, Abitur GK aus Daten; dazu Bücher als
durchsuchbare PDFs in Drive und je Schulbuch ein Register (Aufgaben,
Aufbau, Frageformen, Katalog-Zuordnung) als Vorrat für Prüfungs- und
allgemeine Blätter.

## 2 Arbeitsgrundlage

- plan.md § 7 „Jetzt Durchsicht/P10“ (17.10. d), Punkt 1: Chat Bau
  erfasst die Schulbücher als Register, zuerst Duden 9
  („Buch_Mathe_Kl9.pdf“, OneDrive/Desktop/bücher scanns), dann die
  übrigen (Reihenfolge im Stand Bau 4 dort).
- aufgabenbank-privat buecher/ablauf.md: fester Ablauf je Buch
  (Seiten, Register mit Sonnet je ~12 S., Katalog-Zuordnung, PDF mit
  Lesezeichen, Ablage); buecher/register-auftrag.md (19 Felder, mit
  operator und frageform); buecher/README.md.
- Werkzeuge (aufgabenbank-privat werkzeuge/): buch-durchsuchbar.py
  (Seiten, quer/kopfstehend erkannt), buchregister.py (bau, pruef,
  such, aufbau, katalog <id>), buch-lesezeichen.py (Lesezeichen,
  Inhalt, Fuß aus dem Register), buch-aufgabe.py (Ausschnitt bei
  vergessenem Buch), pruefungsbuch.py (Buch P10, qpdf).

## 3 Arbeitsstand

- Erledigt 16./17.10.: Lösungen aller 14 P10-Hefte (--streng 0),
  Buch „P10 Originalprüfungen“ in Drive; Jesse (Cornelsen
  Fundamente 10, 2 Bände) und Sekundo 10 (Westermann, 1 Datei) in
  Drive Mathe/Bücher; Register jesse (1 045 Aufgaben, ohne
  frageform) und sekundo10 (960 Aufgaben); katalog.csv für beide.
- Offen: Duden 9 – nächster Lauf, Go des Lehrers noch nicht erteilt.
  Dabei ein Skript für die Schritte ohne Modell (ablauf.md 1 und 4)
  schreiben, Duden 9 ist der erste Fall (vermutlich digitales PDF:
  Seiten mit pdftoppm, Text eventuell schon vorhanden). Schätzung
  1,5–2 Punkte, Skript ≈ 0,3.
- Offen: die vier Fragen aus aufgabenbank bau/befunde-M5.md (Abitur:
  4 Seiten, Ende des Blatts, Rechenraum, ’26 · A1.3) – am Anfang
  des neuen Chats vorlegen, einfache Sprache, eine je Nachricht
  (plan.md § 7, spätestens Mo 19.10.).
- Offen beim Lehrer: Jesse neu scannen (je Seite; S. 40/41, 164/165,
  236–238), dann ein Buch statt zwei Bände (plan.md § 9).
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Woche 54 % (17.10. mittags, mit Nebenchat), Reset Mo 18:00.
  Bau 4 gesamt 49 → 54 %: Lösungen und Buch P10 ≈ 1, Jesse ≈ 2,
  Sekundo ≈ 2 Punkte. Faustwert ≈ 1 Punkt je 90 Buchseiten (Sonnet,
  ~10 000 Agenten-Token je Seite, meist Cache).
- Kein Wortlaut aus Schulbüchern wird gesammelt (Claude lehnt die
  Abschrift ab; Sonnet-Agenten ebenso). Erlaubt und gewollt:
  Merkmale, Stichwort und Frageform in eigenen Worten, Aufgaben auf
  Abruf als Ausschnitt oder „nach <Buch> S. n/k“ mit anderen Zahlen.
- Rechner: Dateien einzeln holen; große Dateien nach Drive über
  SendUserFile und dann device_commit_files mit fileUuid; Ablage
  höchstens 30 MB je Datei. Meldet die Brücke „nicht verbunden“,
  einmal neu versuchen und dem Lehrer die Meldung wörtlich nennen.
- Lehrer arbeitet in UTC+2; will tokensparend arbeiten.

## 5 Offen und Verworfenes

- Verworfen: Abschrift ganzer Bücher (auch nur P10-Kapitel); Buch-PDF
  aus kleineren Bildern (Formeln unscharf) – stattdessen Bände.
- msa/gliederung/*.md und uebergabe-durchsicht.md tragen noch „16.10.
  n“ für die Durchsicht-Entscheidung, die in plan.md jetzt 16.10. o
  heißt; nicht angefasst (Fassung der Blätter hängt an den Daten) –
  Sache des Chats Durchsicht.

## 6 Nächster Arbeitsschritt

plan.md § 7 („Jetzt Durchsicht/P10“, Punkt 1; Stand Bau 4).
