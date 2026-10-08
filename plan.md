# Plan – Blätter aus der Bank

Stand 08.10.2026 · gilt (Ja des Lehrers 08.10.).
Ersetzt faellig.md § 0 als Plan. Übergaben nennen nur noch
Meilenstein und Schritt aus dieser Datei.

## 0 Wie dieser Plan gilt

- Jeder Chat beginnt mit dem Abgleich: Meilenstein, Schritt, was seit
  dem letzten Abgleich passiert ist, ob wir im Budget liegen.
  Mindestens einmal am Tag.
- Gearbeitet wird nur, was im Plan steht. Was nicht drinsteht, kommt
  in § 6 „Später“ – nicht in eine neue Regel, nicht in einen Lauf.
- Ändern darf den Plan nur der Lehrer. Vorher: große Linien (§ 2)
  vorlesen, Änderung mit Grund in § 7 eintragen.
- Eine Bemerkung des Lehrers zu einem Blatt ist eine Richtung, keine
  Regel. Regeln entstehen gesammelt am Ende eines Meilensteins, aus
  Befunden an mehreren Blättern. Ausnahme: Handwerksfehler (falsche
  Zahl, Satzfehler) werden sofort behoben.

## 1 Ziel

Der Lehrer tippt im Projekt erzeugeBlatt(Bank) wenige Wörter und
bekommt in wenigen Minuten ein gutes, druckfertiges Blatt – für den
Unterricht und für die Prüfung. Zuerst P10 (FOR/EBR), dann Abitur
Grundkurs. Die Aufgaben kommen aus einer vollständigen, geprüften Bank.

## 2 Große Linien (fest)

1. Die Bank ist die Quelle. Kein Blatt erfindet Aufgaben, außer als
   Notweg; neue Aufgaben gehen geprüft in die Bank.
2. Ein Objekt je Thema: der Katalogeintrag mit seinen Einheiten. Was neu
   gebraucht wird, wird ein Feld darin, nie eine neue Datei. Zuordnung,
   Zuschnitt, Handgriffe und Kapitel sind Sichten, die ein Skript aus
   Katalog und Bank erzeugt.
3. Ein Bauprogramm setzt jedes Blatt (Unterricht, P10, Abitur). Der
   Chat bestellt nur.
4. Eine Regeldatei: aufgabenbank `bau/bauregeln.md`. Aufbau, Reihenfolge,
   Auswahl und Didaktik, wie sie bis Montag 05.10. verallgemeinert
   waren, sind der Rahmen. Ein einzelnes Blatt ändert keine Regel; weicht
   ein Blatt vom Rahmen ab, wird mit dem Lehrer gesprochen.
5. Der Lehrer urteilt über das Ganze und an Stichproben, nicht an
   jedem Blatt.
6. Fertig heißt messbar fertig (Abnahme je Meilenstein, `tafel.md`).
7. Das Kontingent ist die Grenze: jeder Lauf mit Schätzung vorher und
   Ablesen nachher; sparsam, aber Doppelarbeit wird in Kauf genommen,
   wenn sie Wartezeit spart (Lehrer 08.10.).

## 3 Weichen (entschieden 08.10.)

W1 Ein Bauprogramm: `pruefheft.py` ist die Basis; `zusammenbau.py`
   wird nicht weiterentwickelt; Bank-Prompt v5.8 bleibt Notweg.
W2 Steckbrief geht im Katalog auf: seine eigenen Inhalte (Arten,
   Gruppen, Reihenfolge, Zwischenfragen) werden Felder der
   Katalog-Einheit; Merkkasten, Formel, Fehler stehen dort schon.
W3 Regeln vom 07.10.: werden gegen den Stand Montag 05.10. 18:00
   verglichen; jede Umkehrung entscheidet der Lehrer einzeln.
W4 Reihenfolge: Vereinheitlichen (an P10 und Sek II zugleich), dann
   P10 vollständig, dann Anschluss erzeugeBlatt(Bank), dann Unterricht,
   dann Abitur-Blätter. Sek-II-Daten werden parallel gefüllt.

## 4 Meilensteine

M1 Fundament
- Plan, Fortschrittstafel (erledigt 08.10.).
- Regelvergleich Montag 05.10. 18:00 ↔ heute (W3) – erledigt 08.10.:
  acht Umkehrungen (aus bauregeln-streichliste.md), alle wie 07.10.
  bestätigt, Fuß ohne Tipp. Der Rahmen ist bauregeln.md, Stand 07.10.
- Probelauf im Projekt erzeugeBlatt(Bank) – erledigt 08.10.: Opus, drei
  Klone, xelatex da, sympy fehlte (pip, 12 s), Fokus Pythagoras gebaut
  (5 S. + 2 S. Lösungen, 0 Fehler), 58 s gesamt. Der Weg geht.
- Abnahme: erfüllt 08.10. – M1 abgeschlossen.

M2 Vereinheitlichen
- Katalog-Einheit bekommt die Felder aus W2; die zwei Steckbriefe
  ziehen in pythagoras.md und prozentrechnung.md um.
- Zuordnung, Zuschnitt, Handgriffe werden Sichten (Skript), keine
  gepflegten Dateien.
- Bauprogramm liest Katalog und Bank.
- Abnahme: drei Blätter – Fokus Pythagoras und Fokus Grundwert (wie
  07.10. oder nur dort anders, wo der Lehrer es will) und ein Blatt
  Kurvenuntersuchung (Abitur: lange Kette, Graphen).

M3 P10 vollständig
- Felder aus W2 für alle P10-Einheiten, in Runden; selbst geprüft,
  Lehrer sieht eine Sammelliste.
- Neubau aller zehn Kapitel-Hefte und der Fokusblätter.
- Abnahme: Prüfskript ohne Fehler; je Kapitel eine Seite beim Lehrer;
  je Kapitel ein Einsatz in der Stunde, Befunde gesammelt.

M4 Anschluss erzeugeBlatt(Bank)
- Neue Projektanweisung: Bestellung deuten (Bestellbaum offen.html),
  Programm aufrufen, sonst Notweg v5.8.
- Abnahme: „Pythagoras P10“ liefert im Blatt-Projekt das Blatt in
  wenigen Minuten; drei weitere Bestellungen.

M5 Unterricht für die P10-Themen
- „Vollständig“ je Thema: Katalog auf Vollständigkeit und Reihenfolge
  geprüft und vom Lehrer bestätigt; Prüfskript ohne Meldung.
- Abnahme: je Thema ein Lernblatt über erzeugeBlatt(Bank).

M6 Abitur Grundkurs
- Felder aus W2 für die Abitur-Einheiten, Hefte, Lernblätter – wie
  M3 bis M5.

Parallel ab jetzt: Sek-II-Daten (sparsam, in kleinen Läufen)
- Leeren Eintrag ableitungsgraph-und-funktionsgraph füllen.
- Abitur-GK-Zuschnitt prüfen und zuordnen wie bei P10.
- Mehr Aufgaben mit Graphen in den Analysis-Einträgen.

## 5 Jetzt

Meilenstein M2. Halt vor dem Umbau – Planfrage an den Lehrer (08.10. nachts):

Befund Abgleich Zuordnung ↔ Katalog: Von 80 P10-Stufen liegen 38 in einer
Katalog-Einheit, 22 über mehrere Einheiten eines Eintrags, 19 über mehrere
Einträge (z. B. „Grundfigur berechnen“: flaechen e1–e4 und kreis; „Volumen
direkt“: koerper und pyramide-kegel-kugel), 1 ohne Bankaufgabe. Der
Katalog gliedert nach Lernweg, die Prüfung nach Aufgabentyp; beides ist
berechtigt. Damit trägt Linie 2 („Kapitel = Liste von Katalog-Einheiten“)
und W2 („Steckbrief geht in die Katalog-Einheit“) nicht.
Vorschlag A (empfohlen): Bankaufgabe ist das Atom; zwei Gliederungen
darüber – Katalog (Lernweg, Unterricht) und je Prüfungsart eine
Prüfungsgliederung (Kapitel → Stufe → Bankaufgaben und Originale). Zuschnitt,
Handgriffe und Steckbrief gehen in der Prüfungsgliederung auf (Felder an
der Stufe); Merkkasten und Fehler werden aus dem Katalog verwiesen, nicht
kopiert. Fünf gepflegte Objekte werden drei. Vorschlag B: Katalog so
umbauen, dass Einheiten den Prüfungsstufen folgen – bricht den Lernweg,
großer Umbau; nicht empfohlen.
Bis zur Entscheidung läuft nur, was unter A und B gleich bleibt
(Bankaufgaben, Abitur-Zuordnung).

## 6 Später (nicht jetzt)

Folgebaum der Kennung · Serie mit Wiederkehr · Musterbeispiel ·
Formelsammlung sichten · Darstellungen nach DZLM · FHR und LK ·
Boden unter Klasse 8 · Verschmelzung der Prompts · mündliche Prüfung.

## 7 Änderungen

- 08.10.2026 (c): W3 entschieden – Übersicht vorn entfällt, Zählung nur
  Schlusszeile, Gruppen eingerückt, Auswahl im Fokusblatt, Bündel/Rahmen/
  Anhang fallen, Richtung kurz, Zwischenfragen als Richtung, Fuß nur
  Ergebnisse ohne Tipp (Lehrer 08.10.).

- 08.10.2026 (b): Vereinheitlichen als große Linie (ein Objekt je Thema);
  W2 neu: Steckbrief geht im Katalog auf; Sek II als Prüfstein (Kurven-
  untersuchung) und Sek-II-Daten parallel; Meilensteine neu M1–M6
  (Lehrer: „wir legen jetzt fest“).
- 08.10.2026: Plan angelegt, W1–W4 nach Empfehlung entschieden (Lehrer:
  „annehmbar“); ersetzt faellig.md § 0 vom 07.10. (Plan „Schalter“) und
  nimmt den Plan „P10 fertig“ vom 06.10. wieder auf.
