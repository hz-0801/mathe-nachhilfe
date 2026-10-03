# Übergabe verbessereBlaetter – 2026-10-03c (Chat 03.10., Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-03b.md.

Erster Handgriff im neuen Chat: `offen.html` (Wurzel dieses Repos)
mit SendUserFile, display „render“, an den Lehrer schicken – die
Liste steht dann rechts neben dem Chat. Der Lehrer arbeitet mit
ihr; Scrollen im Chat lehnt er ab. Ändert sich ein Punkt: Datei
anpassen, neu schicken, committen.

## 1 Ziel

Schnell gute Blätter für die Stunde, für P10 2027 zuerst, aber so
gebaut, dass Abitur GK/LK und FHR nur neue Daten brauchen, keinen
neuen Bau. Nächste Phase: die Bedienung – ein Prompt für Schulstoff
und Prüfung, am PC und am Handy.

## 2 Arbeitsgrundlage

- `offen.html` – Liste der offenen Punkte (maßgeblich für die
  Reihenfolge der Arbeit).
- aufgabenbank-privat (main): `basis-originale.jsonl` 136 Zeilen,
  Aufgabe 1 aller 14 Hefte 2014–2026 (Du-Form, gegen
  msa-katalog-basis.csv geprüft, 0 Lösungsabweichungen);
  `stand.md`; `werkzeuge/sammlung.py` (alle Original-Zettel als
  ein PDF mit klickbarem Inhalt, Lesezeichen, „↑ Inhalt“);
  `werkzeuge/onenote-testseite.py` (ruht).
- aufgabenbank (main): `werkzeuge/zusammenbau.py` v1.8 –
  `--zettel original --heft <JAHR>-<PAPIER>` (Papier groß) mit
  `--vorlage <blattbau>/mathblatt.sty --pdf --ohne-register --aus
  <ordner>` und `PRIVAT=<aufgabenbank-privat>`; ohne
  `--ohne-register` schreibt es bau/register.csv im öffentlichen
  Repo fort.
- blattbau: `bankblatt.md` v5.4 (nur Klasse 8–10, keine
  Prüfungssorten), `mathblatt.sty`.
- Schülerliste: `Schuelerliste-privat.md` als Projektdatei in
  erzeugeBlatt(Bank) (Nummer, Klasse, Schulform, Prüfung).

## 3 Arbeitsstand

Erledigt 03.10. nachmittags: Erfassungslauf (Opus-Agent, 0,25 Mio
Token, Anzeige vorher und nachher Woche 86 %, Fable 88 % –
Messwert: unter einem Punkt); 14 Original-Zettel gebaut, 13 auf
einer Seite, 2021 mit Rückseite; fünf Datenzeilen setzbar gemacht
(2025 d Exponent als Kästchen, 2023 g und 2015 i zweite Lücke als
Linie, 2022 d, 2019 e); Sammlung als ein PDF an den Lehrer.
OneNote-Notizbuch getestet und vom Lehrer abgebrochen (faellig § 2,
ruht). Damit gibt es alle drei Zettelsorten (Originalblatt,
Original-Zettel, Basiszettel).

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter, soweit hier nichts anderes steht.

- Ein Prompt für Schulstoff und Prüfung (bestätigt 03.10.; heute
  noch drei Prompts – unterrichtsblatt, pruefungsblatt, bankblatt).
- Der Lehrer ist der einzige Anwender: keine Sammlung von
  Beispielbestellungen als Vorarbeit.
- Alles muss am Handy und am PC gehen.
- Offene Punkte stehen rechts (offen.html), nicht im Chatverlauf.
- Agenten holen mathblatt.sty nicht per Raw-URL (Sicherheitsprüfung
  lehnt ab, Messwert 03.10.); der Chat klont blattbau und gibt den
  Pfad mit.
- Original-Zettel: Fehler im Satz werden in der Datenzeile behoben,
  nicht im Skript, solange es um einzelne Zeilen geht.
- Modellwahl nächste Phase: Opus im Chat und für Agenten.

## 5 Offene Punkte und Verworfenes

Die Liste steht in offen.html; hier nur, was dort nicht steht:

- Vorschlag des Chats zur Bedienung, noch nicht bestätigt:
  Schülerliste sagt die Prüfung (P10, Abitur GK/LK, keine), das
  Bestellwort die Sorte (Thema → Lernblatt; „Basis“, „Original
  <Jahr>“, „Probe“ → Prüfungssorte); Rückfrage nur bei
  doppeldeutigem Wort. Kein fester Schalter je Schüler, weil ein
  P10-Schüler auch Schulstoff braucht. Knöpfe nur, wenn der Lehrer
  sie für Blatt-Chats ausdrücklich zulässt (globale Regel: keine
  Auswahlknöpfe).
- Aufgabenliste (TaskCreate) erscheint beim Lehrer nicht –
  deshalb offen.html.
- Verworfen: OneNote als Ausgabe (03.10., ruht); Liste echter
  Bestellungen (Lehrer einziger Anwender).

## 6 Nächster Arbeitsschritt

offen.html zeigen. Dann Punkt 1 „Bedienung festlegen“: den
Vorschlag aus § 5 dem Lehrer vorlegen (bestätigen oder ändern),
danach ausarbeiten, wie der eine Prompt Schülerliste und Bestellwort
in einen Aufruf von zusammenbau.py übersetzt – zuerst für die drei
Zettelsorten, die es schon gibt.
