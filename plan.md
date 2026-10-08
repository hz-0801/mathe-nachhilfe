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
2. Ein Bauprogramm setzt jedes Blatt. Der Chat bestellt nur.
3. Eine Regeldatei: aufgabenbank `bau/bauregeln.md`. Prompt und
   Programm schreiben keine eigenen Regeln ab.
4. Der Lehrer urteilt über das Ganze und an Stichproben, nicht an
   jedem Blatt.
5. Fertig heißt messbar fertig (Abnahme je Meilenstein, § 4).
6. Das Kontingent ist die Grenze: jeder Lauf mit Schätzung vorher und
   Ablesen nachher; große Läufe in Runden.

## 3 Weichen (entschieden 08.10., Empfehlungen des Chats angenommen)

W1 Bauweg. Empfehlung: `pruefheft.py` wird das eine Bauprogramm (jüngster
   Stand, liest Bank, Zuschnitt und Steckbriefe). `zusammenbau.py` wird
   nicht mehr weiterentwickelt; das Lernblatt kommt als zweiter Eingang
   ins selbe Programm (Meilenstein 4). Der Bank-Prompt v5.8 bleibt
   Notweg für alles, was das Programm noch nicht kann.
W2 Steckbrief (Lehrer-Plan „P10 fertig“ 06.10.). Empfehlung: bleibt –
   einer je Abschnitt des P10-Zuschnitts, Format eingefroren wie in
   `katalog/steckbrief/README.md`. Kein weiteres Feld ohne Planänderung.
W3 Regeln vom 07.10. (rund 40 Beschlüsse, Zusammenfassung auf
   bauregeln.md). Empfehlung: gelten; einmal prüfen, ob beim
   Zusammenfassen etwas Bewährtes verloren ging (alte Dateien gegen
   bauregeln-streichliste.md).
W4 Reihenfolge Unterricht/Prüfung. Empfehlung: erst P10 Prüfung ganz
   (M2), dann der Anschluss an erzeugeBlatt(Bank) (M3), dann
   Unterricht für die P10-Themen (M4), dann Abitur GK (M5).

## 4 Meilensteine

M1 Fundament
- Weichen W1–W4 entschieden; Plan gilt (erledigt 08.10.); Übergabe
  und Projektanweisung verbessereBlätter nennen diese Datei zuerst.
- Fortschrittstafel als Skript aus dem Repo: je Thema und je
  P10-Abschnitt der Stand (Katalog geprüft · Bank voll · Steckbrief ·
  Blatt gebaut · abgenommen).
- Prüfung W3 (Regeln verloren?).
- Technischer Probelauf im echten Projekt erzeugeBlatt(Bank): kann der
  Chat die Repos holen, LaTeX nutzen, `pruefheft.py` laufen lassen?
  Eine Nachricht des Lehrers.
- Abnahme: Tafel steht, Probelauf ja/nein mit Zeit.

M2 P10 Prüfung vollständig
- Steckbriefe für alle Abschnitte des Zuschnitts, in Runden; je Runde
  selbst geprüft, Lehrer sieht eine Sammelliste.
- Neubau aller zehn Kapitel-Hefte und der Fokusblätter mit dem
  heutigen Regelstand.
- Abnahme: Prüfskript ohne Fehler; Lehrer sieht je Kapitel eine Seite;
  je Kapitel ein Einsatz in der Stunde, Befunde gesammelt.

M3 Anschluss erzeugeBlatt(Bank)
- Neue Projektanweisung: Bestellung deuten (Bestellbaum offen.html),
  Programm aufrufen, sonst Notweg v5.8.
- Abnahme: „Pythagoras P10“ liefert im Blatt-Projekt das Blatt in
  wenigen Minuten; drei weitere Bestellungen aus dem Bestellbaum.

M4 Unterricht für die P10-Themen
- „Vollständig“ je Thema: Katalog auf Vollständigkeit und Reihenfolge
  geprüft und vom Lehrer bestätigt; jede Leiterstufe mit genug
  Aufgaben; keine Kopien; Prüfskript ohne Meldung.
- Lernblatt als zweiter Eingang im Bauprogramm.
- Abnahme: je Thema ein Lernblatt über erzeugeBlatt(Bank).

M5 Abitur Grundkurs
- Zuschnitt prüfen, Vorrat, Steckbriefe, Hefte; Bank Sek II
  vollständig – dieselben Schritte wie M2–M4.

## 5 Jetzt

Meilenstein M1, Schritt: Fortschrittstafel bauen.

## 6 Später (nicht jetzt)

Folgebaum der Kennung · Serie mit Wiederkehr · Musterbeispiel ·
Formelsammlung sichten · Darstellungen nach DZLM · FHR und LK ·
Boden unter Klasse 8 · Verschmelzung der Prompts · mündliche Prüfung.

## 7 Änderungen

- 08.10.2026: Plan angelegt, W1–W4 nach Empfehlung entschieden (Lehrer:
  „annehmbar“); ersetzt faellig.md § 0 vom 07.10. (Plan „Schalter“) und
  nimmt den Plan „P10 fertig“ vom 06.10. wieder auf.
