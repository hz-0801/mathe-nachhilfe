# Übergabe verbessereBlaetter – 2026-10-10 abends (Chat „start 20“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-10.md. Nach plan.md Linie 8
nennt diese Übergabe keinen eigenen nächsten Schritt: maßgeblich ist
plan.md § 7 („Jetzt“).

## 1 Ziel

P10 am Katalog fertigbekommen, ohne die Verallgemeinerung (Abitur,
Schulstoff) aus den Augen zu verlieren. Der Lehrer bestellt mit wenigen
Wörtern und bekommt schnell gute, kurze Blätter (plan.md § 1).

## 2 Arbeitsgrundlage

- plan.md § 7 „Jetzt“: Bestand ordnen, zwei Sorten mit je festem Stand.
- Baum P10 Skript (fest 03./04.10.): offen.html, Abschnitt
  „Entscheidungsbäume“ – Ast → Kapitel → Handgriff; was das Skript
  leisten soll.
- aufgabenbank bau/bauregeln.md: Übersicht und Serie (§ 3), Kennung (3.5,
  6.3), Fuß (6.2), Reihenfolge (2.4).
- Alte Prompts (blattbau unterrichtsblatt.md v4.4, pruefungsblatt.md
  v0.15) als Beispiel für „fester Stand in einer Datei“.

## 3 Arbeitsstand

Rahmen vom Lehrer heute: Zwei Sorten getrennt halten, jede mit festem
Stand in einer Datei; das Zusammenlegen beider Prompts machte die Arbeit
schwerer. Das Repository ist verwirrend, der Chat hat den Überblick
verloren. Erst ordnen, dann bauen.

Gefunden in den letzten Tagen, soll bleiben:

Gilt für beide Sorten (Technik):
- Bestellen über den Baum: zeigen statt beschreiben.
- Kennung mit Register: was auf dem Blatt stand ist bekannt; Ändern auf
  Zuruf; Folgebaum (weiter, mehr, leichter, Lösung, hängt bei Nr.) –
  beschlossen, nicht gebaut.
- Kurze Einheiten: ein Eintrag der Übersicht ist ein Blatt; Portionen
  (werkzeuge/pruefheft.py --portion), Vorrat für „mehr“.
- Übersicht vorn (bauregeln § 3); gesetzt bisher nur für Lernblätter
  (setzer.py), nicht für Prüfungshefte.
- Ergebnisse kopfüber im Fuß, Kennung grau, Niveau im Kopf.
- Aufgabe und Treppe getrennt (bank.md „Aufgaben ohne Treppe“).
- Bildvergleich vor Abgabe; keine Regel aus Einzelbefunden; messen.

Nur Allgemein (Schulstoff): Ordnung aus dem Katalog; Lehrer-Vorlage
Hypotenuse (aufgabenbank bau/proben/2026-10-10/vorlage-holger/: ein Verb,
Schwierigkeit in der Figur, Falle statt Tipp, erkennen → aufstellen →
rechnen, Päckchen mit grauem a), Sache steigend); Maß M74/T6B;
Selbstlernform wie das Heft für Marlene (Übersicht mit „kann ich“,
Formeln, je Abschnitt wenig Text); kein Fehler-finden, keine Rätselbilder.

Nur Prüfung: Baum P10 (10 Kapitel, Handgriffe); echte Aufgaben nach
Handgriff, leicht → schwer; „kommt das dran?“; Fundstellen; gestufte
Hilfen; Marke „P10 ’24“; am Ende das Original ganz. Brücke zum Allgemeinen:
je Handgriff „lernst du in“ (Lerneinheit des Katalogs).

Bestand:
- P10-Skripthefte aus der Bank, 06.10., zehn Kapitel normal und schwach,
  Portionen (aufgabenbank bau/pruefheft/, 70 PDFs) – kein Lehrerurteil.
- Drei Hefte nach altem Unterrichtsprompt (heute, Messung): blaetter/
  alter-prompt-2026-10-10/ (LGS Kl. 9, Körper Kl. 9, Integration Kl. 12).
- Füllprobe Kathete: aufgabenbank bank/pythagoras/a2.jsonl (55 Aufgaben),
  Treppe treppe-e2-vorlage.md, merkmale.md, bau/fuellauftrag.md; bank-pruef
  prüft a*.jsonl. Angehalten: Stufe 1 verfehlte die Absicht der Vorlage
  („Finde die Hypotenuse“ – nicht „H oder K?“; das gehört in eine
  Mischstufe).

## 4 Verbindliche Entscheidungen und Rahmen

- Linien entscheidet der Lehrer; keine Regel aus Einzelbefunden.
- Weg 3 (Bücher scannen) ruht; Duden WÜT 9 ist schon im Katalog
  abgeglichen (katalog/_abgleich-duden9-kap*.md).
- Messwerte 10.10.: Heft nach altem Prompt ≈ 0,28 Mio Token, 45–75 min;
  Woche 70 → 75 % für drei Hefte (≈ 2,5 Punkte je Opus-Heft), Fable
  33 → 39 % für ein Heft. Füllprobe 0,13 Mio, Fable-Kritik 0,09 Mio.
  Stand am Ende: Woche 75 %, Fable 39 %; Reset Montag 18:00.
- Unteragenten: Repos unter /root, nicht /home/claude.

## 5 Offen und Verworfenes

- Offen: „Lage erfragen“ (Bestellung fragt die Lage des Schülers) –
  Lehrer 10.10.: so nicht zutreffend; Form ungeklärt.
- Offen: Urteil des Lehrers zu den P10-Skriptheften (Prozent normal und
  Portion 1 gesehen, nicht beurteilt).
- Offen: Arbeitsformen neben „Kreise ein“ (beschriften, nachfahren,
  zuordnen, selbst skizzieren) – Befund, kein Umbau.
- Verworfen: Prüfungshefte nach altem Prüfungsprompt v0.15 – er folgt
  nicht dem Baum (36 Katalogthemen, erfundene Leitern).

## 6 Nächster Arbeitsschritt

plan.md § 7 „Jetzt“.
