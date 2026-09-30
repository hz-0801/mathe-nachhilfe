# Übergabe verbessereBlaetter – 2026-09-30 (Chat 29.09. 08:14 bis 30.09. 01:00; Nachträge 30.09. vormittags und mittags)

Vorherige Übergabe: archiv/uebergabe-2026-09-29.md (früh).

## 1 Ziel

Der bestmögliche Themenkatalog, die Aufgabenbank und die Prompts,
damit aus wenigen Wörtern druckfertige Blätter entstehen. Maßstab
ist ziel.md (28.09.); Leitbild: ein Blatt für alle Schüler, aus der
Bank zusammengesetzt, Chat als Schalter.

## 2 Arbeitsgrundlage

- mathe-nachhilfe: ziel.md (28.09., unverändert); katalog/ auf
  f038ccb (sieben Änderungen vom 29.09., § 3); faellig.md (Posten
  aus dem Tag in § 2, Messwerte Kontingent); bericht-katalog-
  nachzug.md (Liste der 24 Einträge, alle erledigt).
- aufgabenbank auf 11d6a36 (Nachbesserungen 30.09. mittags, § 3): bank.md 29b (fünfte Fassung:
  Vorstufen 0, −1, −2; eine Prüfungssprosse je Kette mit allen
  Originalen; Musterbeispiel muster.md; Körperregel beim Nachzug;
  Dublette = ein Original); auftrag-eintrag.md 29e; werkzeuge/
  bank-pruef.py v0.10 (`--katalog` aus der Mappe); werkzeuge/
  punkte-nachziehen.py (ids nach Nachzug); werkzeuge/einmalig/
  (Umbauskripte der Nachzüge); bank/<eintrag>/stand.md je Eintrag
  mit Entscheidungen und Befunden vom 29.09.
- anweisungen: projekt-verbessereBlaetter.md 28c, kandidaten.md
  2026-09-30 (vier neue Kandidaten, § 4).
- blattbau unverändert: unterrichtsblatt.md v4.4, pruefungsblatt.md
  v0.15.
- TER-S1, TER-S2 weiter nur im alten Chat (Lehrer).

## 3 Arbeitsstand

Erledigt 29.09.:
- Vorstufen-Lauf über die vorhandenen Schreibform-Notizen der
  DDR-Bücher (61 Notizen, Vier-Fragen-Prüfstein): sieben
  Katalogänderungen in fünf Einträgen – terme E4 Vorstufe
  „Zerlegen mit vorgegebenem Faktor“ (vor „Faktor vorgegeben“),
  prozentrechnung E4 Sprosse „nur ein Prozent bestimmen“,
  bruchrechnung E3 Sprosse „Stammbruch von einem Bruch“ (Vorrat)
  und Kastenzeile 3 · 2/5 = 3/1 · 2/5, tangente E1 Vorstufe „nur
  den Anstieg“, stammfunktion E2 „nur einsetzen“ als Vorstufe vor
  den Grundfall (d78032a, f038ccb).
- Prüfstein terme als Unteragent (217 495 Token), danach alle 23
  übrigen Einträge in vier Schüben (4, 6, 6, 7 Agenten parallel,
  Opus; 1,08 / 1,66 / 1,68 / 2,11 Mio Token). Alle 24 Einträge auf
  Katalog 29.09., bank.md 29b, Pflichtformen P1–P8, Päckchen,
  muster.md; Prüfskript `--katalog` überall 0/0. Bank: 73 Ordner,
  15 294 Zeilen.
- bank/_punkte.csv nach jedem Schub nachgezogen (ids umbenannt,
  neue Urteile durch kleine Opus-Agenten: 12, 62, 34); Gegenprobe
  bestanden.
- Regeln aus den Befunden der Schübe in bank.md, Vorlage und
  Prüfskript (§ 4).
- Kontingent gemessen (§ 4).

Erledigt 30.09. vormittags (Chat auf Fable, zwei Opus-Agenten,
0,41 Mio Token; Woche 41 % vorher und nachher):
- aufgabenbank 4bb1bd6: bank-pruef.py v0.11 – Formprobe P1–P8 als
  eigene Rubrik (nicht Abweichung, nicht Warnung), Punkte „(4; 1)“
  gelesen, Winkel „rund 37°“ als Ergebnisstelle, Zeile „Urteile:
  ja/nein/richtig/…“ je Eintrag; Bericht werkzeuge/bericht-pruef-
  v0.11-2026-09-30.md (vollständige Formprobe-Liste je Eintrag).
  Befund: die 24 nachgezogenen Einträge haben 0–4 Hinweise, die 48
  übrigen 10–40 (882 gesamt) – Formprobe bestätigt den Nachzug.
  Ausgangswert über alle 72 war nicht 0/0: 315 Abweichungen mit
  --katalog, alle in nicht nachgezogenen Einträgen (quadratische-
  gleichungen 195, symmetrie-abbildungen 39, gleichungen-loesen 21,
  bedingte/grenzwerte/hypothesentests je 12, scharen 10), dazu 6
  alte ohne Katalog (binomische-formeln 4× „grafik leer“,
  weg.jsonl in lineare-gleichungen und quadratische-funktionen).
- aufgabenbank 1393253: Körperregel der Sperre (§ 4), bank.md
  Stand 2026-09-30, bank-pruef.py v0.12; 122 von 124 Punkt-
  Treffern weg, 317 / 2 / 882 über 72 Einträge. Zwei bleiben als
  Gegenlese-Posten (§ 5).

Erledigt 30.09. mittags (Chat auf Fable, ein Opus-Agent, 0,16 Mio
Token; Lehrer wählte „zweiten Weg“: erst Nachbesserungen, Katalog-
auftrag, Schalter-Prompt, volle Gegenlese danach):
- aufgabenbank 5c1bf5a: antwort-Gerüst „__“ statt \leerfeld in 455
  Zeilen (sechs Einträge), Skript werkzeuge/einmalig/leerfeld-
  antwort-2026-09-30.py. 959fd16: skalarprodukt e1 s1 v5 Gerüst mit
  Urteilsfeld; geraden-e3-k1-s4-v1 Würfel Kante 3 (4 und 6 kollidieren
  mit Mappe); zufallsexperimente-e2-k1-s0-v4 Paar (4; 6). 11d6a36:
  „Begründe, ohne genau zu rechnen“ in den acht Einheiten (je die
  P6-Zeile umgeschrieben, kein Urteil gekippt). Prüfskript: geraden
  und zufallsexperimente 0/0, Formprobe kurvenuntersuchung 4 → 0,
  prozentrechnung 4 → 1, tangente 1 → 0.

Nicht erledigt: Gegenlese der Nachzüge (Posten faellig.md);
Schalter-Prompt; pruefungsblatt.md 1.1; K2, K3, K5 (jetzt mit
Beleg), K6, K7; Katalogbefunde aus den stand.md-Dateien (unten).

## 4 Verbindliche Entscheidungen (29.09.)

Frühere Übergaben gelten weiter (archiv/).

- Vorstufen: die Vorstufe vor dem Grundfall ist Sprosse 0, weitere
  davor −1, −2 (id s-1); der Grundfall ist immer 1 (bank.md).
- Je Verfahrenskette genau eine Prüfungssprosse, die letzte, mit
  allen Originalen der Katalogzeile (je Original zwei Zeilen, ohne
  Original drei). Grund: das Blatt zieht „was die Prüfung fragt“.
- Musterbeispiel: bank/<eintrag>/muster.md, je Verfahrenskette ein
  Abschnitt (Annahme statt „einmal je Eintrag“ in ziel.md, weil
  jedes Blatt am Grundfall seiner Einheit beginnt); Form Schritt |
  Zeile, Bausteine setzt der Zusammenbau (layout 55).
- Sperre: Terme, Zahlenpaare, Gleichungen aus Kasten, Typischen
  Fehlern und Originalen; einzelne Kastenzahlen sind frei (sie sind
  der Stoff). Merkkasten bleibt „nur auf Zuruf“ (ziel.md).
- Nachzug eines bestehenden Ordners: Übernahme geht vor der
  Körperregel; Zeilen bleiben wortgleich, auch wenn der
  Sprossentext länger wurde, solange die Aufgabe dieselbe bleibt;
  Pflichtformen werden durch Umschreiben hergestellt, nicht
  ergänzt; Schrittnamen nur in neuen und umgeschriebenen Lösungen.
- Pooldublette zählt als ein Original (Kennung, die in der Mappe
  zuerst steht); gilt für Neues, der Bestand bleibt bis zur
  Gegenlese.
- Punkte: verlangt die Bankzeile mehr als das Original, ist sie
  „ganz“; nach jedem Nachzug punkte-nachziehen.py, dann Urteile.
- Prüfskript: pruef "" bei pflicht fehler erlaubt (P1-Serie);
  \janein-Lösung beginnt mit ja/nein; „Zeichne nichts“ ist kein
  Zeichenauftrag; \int, \sum, \lim und Co. erlaubt.
- Agentenläufe: je Eintrag ein eigener Klon (/tmp/bank-<eintrag>),
  Zwischendateien nie im geteilten Scratchpad; Umbauskripte nach
  werkzeuge/einmalig/; bis sieben Agenten parallel ohne
  Push-Konflikt (Messwert 29.09.).
- Kontingent (Messwerte Nutzungsanzeige, Woche seit Montag 18:00):
  8 % nach Katalog-Nachzug und terme, 12 % nach Schub 1, 18 % nach
  Schub 2, 28 % nach Schub 3, 39 % nach Schub 4 (Nebenchat lief
  mit). Rund 1–1,5 % je Bank-Eintrag, etwa 3,5–5 % je Million
  Token. Fable 21 % für diesen Chat. Die Hochrechnung der Anzeige
  („geht Freitag aus“) ist deren Schätzung aus dem Tagestempo.
- Körperregel der Sperre (30.09., Lehrer): ein einzelnes
  Zahlenpaar oder Tripel als Punkt ist frei, auch wenn es in
  Original oder Kasten steht; gesperrt sind zwei oder mehr Punkte
  derselben Quelle in einer Zeile. Grund: die Mappen enthalten
  1 156 Originalpunkte, Einzelsperre macht kleine Zahlen unmöglich,
  und ein Punkt ist keine Kopie. Die von einem Agenten eingeführte
  Ausnahme „Punkte aus 0, 1, −1 frei“ ist gestrichen. Gleichungen,
  Terme, Ergebnisse, Anteil/Produkt-Paare unverändert.
- Messwerte 30.09.: 0,28 + 0,13 Mio Token Agenten bewegten die
  Wochenanzeige nicht (41 % → 41 %).
- Seitenlauf über die DDR-Bände (jede Musterlösung eines Kapitels
  lesen) nur bei Blatt-Befund für einen Eintrag, nie über alle
  Bände (faellig.md).
- Kandidaten in kandidaten.md (Stand 2026-09-30, 22b1f02), vier
  Blöcke; Kurzform: (a) Hinweise im Kopf eines Agenten-
  Auftrags müssen aus der Quelle stammen, die der Agent selbst
  liest (Mappe), nicht aus einer Zählung des Chats – der Hinweis
  zu ebenen war falsch, der Agent hat richtig die Mappe genommen.
  (b) Parallele Agenten je in einem eigenen Klon, Zwischendateien
  nie im Scratchpad. (c) Musterlösungen alter Lehrwerke sind eine
  Quelle für Vorstufen: je Zeile der Lösung die vier Fragen (nicht
  Sprosse; als Aufgabe stellbar; eigenes Fehlerbild; Sturzstelle).

## 5 Offene Punkte

- Gegenlese aller 24 nachgezogenen Einträge (40–70 neue oder
  umgeschriebene Zeilen je Eintrag); die gegenlese.md/gegenlese2.md
  in den Ordnern zeigen auf alte ids. Dabei die Nachbesserungen aus
  den stand.md-Dateien: skalarprodukt e1 s1 v5 (Antwortfeld deckt
  die Beurteilung nicht), zufallsexperimente übernommene Zeilen mit
  „P = \leerfeld“ in antwort, binomische-formeln e1 Vorstufe ohne
  Baustein (Pfeile), Bestandszeilen mit Poolkennung (ebenen,
  lagebeziehungen, tangente).
- Die Posten aus v0.11/v0.12 (ohne genau zu rechnen, geraden-Würfel,
  Würfelpaar) sind erledigt (30.09. mittags); die umgeschriebenen
  Zeilen gehören in die Gegenlese.
- Urteilsbalance mit Zahlen (bericht-pruef-v0.11): gesamt ja 337 /
  nein 364; P2 102 von 102 „Richtig“ (Formfolge, Regel „etwa halb“
  passt für P2 nicht); P6 ja 24 / nein 95; 105 P8-Lösungen setzen
  das Urteil nicht an den Anfang. Entscheidung offen.
- Katalogbefunde aus den stand.md-Dateien (für den nächsten
  Katalogauftrag): binomische-formeln Verweis auf quadratische-
  gleichungen Einheit 2/3; lineare-gleichungen Z. 32 „vor Einheit 1
  und 2“; Erkennungsschritt, der eine Vorstufe wiederholt – bank.md
  „derselbe Handgriff“ ist zu weich, drei Agenten haben nach
  Ermessen entschieden (vektoren, binomialverteilung, abstaende);
  flaecheninhalt neun Kennungen an Prüfungssprossen ohne Mappen-
  eintrag; funktionsklassen 30 CAS-Originale 2017/2018 an keiner
  Sprosse; stammfunktion e2-Vorstufe nennt 2025-bebb-lk-B2.2b, das
  an der Ableitungssprosse liegt; terme e1 ohne Begründen, e3 ohne
  Anwendung (Typenzeile).
- Prüfskript prüft die Pflichtformen P1–P8 nicht (alle Agenten):
  Formprobe je Einheit (drei verschiedene fehler-, drei begruenden-
  Formen) als v0.11, sobald die Gegenlese die Formen bestätigt hat.
- Sperre trifft in der Raumgeometrie jede Körperecke einzeln gegen
  alle Tripel der Mappe (abstaende, skalarprodukt, geraden, ebenen):
  Körper mit kleinen Zahlen sind schwer zu finden; Regel prüfen, ob
  Tripel nur als Körper (drei Ecken zusammen) gesperrt werden.
- Prüfskript erkennt Punkte in der Originalschreibweise „(4; 1)“
  nicht (tangente); Winkel „rund …°“ nicht als Ergebnisstelle.
- Urteilsbalance Ja/Nein: P6 fällt fast immer Nein, P2 immer
  „Richtig“ – die Regel „etwa halb“ ist je Einheit nicht haltbar;
  entweder je Eintrag zählen oder streichen.
- blattbau: Bausteine „Figur aus zwei Rechtecken“ (terme) und
  „Pfeile jedes mit jedem“ (binomische-formeln).
- Schalter-Prompt nach ziel.md; pruefungsblatt.md 1.1; Vorlage:
  Zonen-Kopfzeile doppelt, Textfont-Zeichen.
- winkel-dreiecke.md Z. 125 (Umkehrung) offen, keine Kette.

Verworfen: Einzelzahl-Probe der Kastenzahlen (Stoff, nicht
Beispiel); Verzicht auf den Merkkasten (bleibt „auf Zuruf“, eine
Zeile im Schalter, Formelsammlungsform für Nachschlagen); P9, P10
und die übrigen aus archiv/uebergabe-2026-09-29.md.

## 6 Nächster Arbeitsschritt

Modell: Opus 5.5 (Fable auf Wahl des Lehrers). Läufe als
Unteragenten aus dem Chat, je Eintrag eigener Klon.

Reihenfolge seit 30.09. mittags („zweiter Weg“, Lehrer): Die volle
Gegenlese der 24 Einträge (5–7 % der Woche je Schub, vier Schübe)
wartet, bis der Schalter-Prompt steht und zeigt, was die Bank
wirklich braucht; Woche stand am 30.09. 08:40 bei 41 %.

1. Katalogauftrag aus den Befunden in § 5 (Erkennungsschritt-Regel
   schärfen, flaecheninhalt neun Kennungen, funktionsklassen 30
   CAS-Originale, stammfunktion e2-Vorstufe, terme Typenzeile,
   binomische-formeln und lineare-gleichungen Verweise) als ein
   Opus-Agent; Katalogänderungen legt der Chat dem Lehrer vor.
2. Schalter-Prompt nach ziel.md; pruefungsblatt.md 1.1 im selben
   Zug.
3. Gegenlese-Lauf über die 24 nachgezogenen Einträge (Muster
   27./28.09., nur neue und umgeschriebene Zeilen, mit den
   Nachbesserungen aus § 5), sechs bis sieben Agenten je Schub,
   vor jedem Schub Nutzungsanzeige ablesen; erst nach dem Schalter
   oder in der neuen Woche.
