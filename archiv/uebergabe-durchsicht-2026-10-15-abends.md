# Übergabe verbessereBlaetter – 2026-10-15 abends (Chat „Durchsicht P10“, Opus)

Eigene Datei, weil zwei Chats nebeneinander laufen; die Übergabe des
Chats „Bau“ ist uebergabe.md. Nach plan.md Linie 8 kein eigener
nächster Schritt; Entscheidungen nur aus plan.md (§ 10, 15.10. l, o,
p).

## 1 Ziel

Die 47 Kommentare des Lehrers zur Mappe P10 Blatt für Blatt
beantworten und entscheiden lassen; umgesetzt wird gesammelt in
Schritt C.

## 2 Arbeitsgrundlage

- plan.md § 7 (Absatz „Durchsicht P10“ mit Stand 15.10. abends),
  § 10 (15.10. l, o, p).
- Kommentare mit Stelle: aufgabenbank
  bau/durchsicht/kommentare-mappe-2026-10-15.csv (Seite, Kennung,
  Rechteck, markierter Text, Kommentar). Das kommentierte PDF:
  aufgabenbank-privat bau/mappe/2026-10-15/
  mappe-p10-kommentiert-lehrer.pdf (334 S., Seiten wie in der Mappe
  vom 15.10. mittags).
- Antworten je Blatt: aufgabenbank bau/durchsicht/pg10.json,
  pg20.json, pg30.json (Marke + Text je Kommentar, Reihenfolge wie
  in der CSV).
- Ansicht: `python3 -I werkzeuge/kommentare.py <pdf> <ordner>`
  (Ausschnitte k-<seite>-<nr>.png), dann `python3 -I
  werkzeuge/durchsicht.py bau/durchsicht/pg40.json <ordner>
  <aus.html>`; als Artifact „Durchsicht P10“ veröffentlichen
  (gleicher Dateipfad = gleiche Adresse nur im selben Chat; im
  neuen Chat entsteht eine neue).
- Regeln in global.md seit 15.10.: Kommentiertes PDF, Zeigen
  (Ausschnitt, eine Spalte, nummeriert), Fragezeichen = Frage mit
  knappem Urteil.

## 3 Arbeitsstand

- Durchgesehen: PG10 Winkel (16), PG20 Symmetrie (6), PG30 Vierecke
  (2). Offen: PG40 Flächen (S. 23–32, 7), PG50 Pythagoras (S. 33,
  5), PG60 sin, cos, tan (S. 41–43, 6), PG70 Sinussatz (S. 50, 2),
  PG80 Netz (S. 57, 1), PG90 Volumen (S. 64–65, 3) – laut CSV.
- Noch nicht beim Lehrer: Bauauftrag für den Bestell-Chat (sechs
  Lücken), Blatt „Stimmt das? Begründe.“.
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Woche 41 % (Anzeige 15.10. ≈ 20:30, aus Chat Bau), Reset Mo
  18:00. Dieser Chat: nur Skripte und Chat, kein Agent; nicht
  gesondert gemessen.
- Lehrer: kleiner Bildschirm; eine Frage je Nachricht, Wege mit
  Namen; je Blatt eine Ansicht.
- Fakten, die der Lehrer korrigiert hat: Basisteil bis 2027 MIT
  Hilfsmitteln (msa/msa.md, hilfsmittelfrei erst Muster 2028);
  Regine S. 24/25 „Vierecke“ nennt keine Symmetrieachsen –
  Stichworte der Formelsammlung vor dem Nennen nachsehen.

## 5 Offen und Verworfenes

- Offen, in plan.md § 7 gelistet: Layout Lösungsblatt (Weg A „wie
  Buch“ / B „entschlackt“ – Lehrer will darüber reden, nicht
  entscheiden), Form der Begriffs-Einzeiler, Name PG10 „Winkel aus
  Winkeln“, Regel „Mehr aufs Blatt, solange zwei Seiten“, Namen
  „Mehr · Winkel“ / „Lösungen · Winkel“ (Vorschlag).
- Verworfen: „Winkel ohne Längen“ (verlangt ein Gegenstück);
  „Symmetrie und Eigenschaften“ (Lehrer); ganze Seiten neben den
  Kommentaren (hilft am kleinen Bildschirm nicht).

## 6 Nächster Arbeitsschritt

plan.md § 7, Absatz „Durchsicht P10“ (Stand 15.10. abends).
