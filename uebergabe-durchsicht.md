# Übergabe verbessereBlaetter – 2026-10-16 Mittag (Chat „Durchsicht P10 4“, Opus)

Eigene Datei, weil zwei Chats nebeneinander laufen; die Übergabe des
Chats „Bau“ ist uebergabe.md. Vorherige: archiv/uebergabe-durchsicht-
2026-10-16-mittags.md. Nach plan.md Linie 8 kein eigener nächster
Schritt; Entscheidungen nur aus plan.md (§ 10, 15.10. l–y, 16.10.
a–m; § 7 Bau Punkt 1).

## 1 Ziel

Alle P10-Blätter vom Lehrer kommentieren lassen, jeden Kommentar
beantworten und entscheiden lassen; umsetzen, sobald ein Block
entschieden ist, damit der Lehrer die Wirkung beim Weiterlesen sieht.

## 2 Arbeitsgrundlage

- plan.md § 7 (Absatz „Durchsicht P10“, Stand 16.10. Mittag), § 10
  (16.10. a–m), § 8 (Messwerte).
- Regeln: gemeinsam.md „Form der Lösung“ (16.10. l, m); Prüfskript
  aufgabenbank werkzeuge/loesung-pruef.py (meldet 0, prüft auch,
  was links gedruckt wird); Stichwörter aufgabenbank
  bau/stichworte-p10.csv (54: 34 Ankreuzen, 20 Einstieg).
- Satz: blattbau mathblatt.sty 16n (lzaufg/\lzz: Nummer dicht,
  Punktlinie, Ansatz ab halber Breite linksbündig, Handgriffe mit
  „;“); pruefheft.py setzt Lösung und Mehr-Lösung damit.
- Stand der Blätter: aufgabenbank bau/pruefung/2026-10-16/<ordner>/
  pdf/; Mappe aufgabenbank-privat bau/mappe/2026-10-16/mappe-p10.pdf.
  Neusatz: `python3 werkzeuge/neusatz-p10.py --datum <d> [--nur …]`,
  dann `python3 werkzeuge/mappe-p10.py --datum <d> --ohne-neubau`
  (zusammen ≈ 25 min, im Hintergrund).
- Durchsicht: Kommentare und Antworten in aufgabenbank
  bau/durchsicht/ (pg10–pg90.json, pa10.json); Werkzeuge
  kommentare.py, durchsicht.py (Artifact „Durchsicht P10“).

## 3 Arbeitsstand

- Erledigt 16.10. Mittag: Lösungszeile (16.10. m) in Setzer,
  Vorlage, Daten, Prüfskript; Neusatz und Mappe (letzter Lauf
  gestartet aus einem Agenten-Klon /home/claude/ag-lz, pusht selbst).
  Lehrer: „für Pythagoras passt es“.
- Chat Bau hat am 16.10. die Katalog-Lösungsfelder neu gefasst
  (Commits 58b6c52, 9e63a8a, 7189138); der letzte Neusatz lief mit
  dem Katalog davor. Vor der Mappe ab PA20 prüfen und ggf. neu setzen.
- Befunde: aufgabenbank bau/befunde-M3.md, Abschnitt „Lösungen nach
  der Lösungszeile“ (Prozent: Wörter rechts, Wiederholung, ≈ ohne
  exakt – Prüfskript fängt es nicht).
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Anzeige 16.10. Mittag: Woche 48 %, Fable 24 %, Reset Mo 18:00.
  Runde Lösungszeile: Sonnet-Agent 0,16 Mio, Schätzung 0,3 Punkte,
  gemessen 46 → 48 % mit parallelem Chat Bau und Chat-Antworten.
- Regel: Chat-Antworten mitschätzen, Anzeige vor dem Start abfragen.
- Modell setzt Claude beim Start des Agenten; Aufwand nur über den
  Chat (modelle.md § 7). Mechanik auf Sonnet reicht, Urteil im Chat.
- Agenten-Ausgaben ansehen: der Sonnet-Agent setzte den Ansatz
  rechtsbündig und auf zwei Zeilen, Spaltenbreite falsch – im Chat
  nachgebessert.
- Lehrer: kleiner Bildschirm; eine Frage je Nachricht, Wege mit
  Namen; Bilder helfen; vor Festlegungen nachsehen, was schon gilt;
  UTC+2.
- Lösungsblätter der Originale (Buch P10) baut der Chat Bau (plan.md
  § 7 Bau 1); hier nur Skript-Lösungen (andere Zahlen).

## 5 Offen und Verworfenes

- Offen: Platz neben großen Koordinatensystemen nur teilweise behoben;
  Lineare 5 Seiten – Teilen erst nach Durchsicht (16.10. h).
- Später (Lehrer 16.10.): Lösungsform auch fürs Abitur.
- Verworfen: zweite Spalte ganz weg (16.10., Weg B); Abschnittsköpfe in
  der Lösung; „je Handgriff eine Zeile“ (ersetzt durch m); Ansatz
  rechtsbündig.

## 6 Nächster Arbeitsschritt

plan.md § 7, Absatz „Durchsicht P10“ (Stand 16.10. Mittag).
