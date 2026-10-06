# Handgriffe je P10-Teilaufgabe

Stand 2026-10-06 (Auftrag K). Datei: `msa/handgriffe-p10.csv`
(id;hauptplatz;ganz_auch;zwischenschritt;begruendung). Grundlage der
Beschlüsse N2.5–N2.7 (`aufgabenbank/bau/pruefheft/beschluesse-2026-10-06b.md`):
Fokusblatt, graue Zeile „steckt auch in …“ und Zählung B im Stufenkopf.

## Inhalt

- Eine Zeile je Teilaufgabe 2014–2026 (OS, EBR, FOR, GYM), die mindestens
  eine Stufe der Zuordnungsdateien `msa/zuordnung-*.csv` braucht: 479
  Zeilen (327 OS/EBR/FOR, 152 GYM). Teilaufgaben ohne P10-Stufe (Einheiten,
  Zehnerpotenzen, Terme, Kombinatorik …) fehlen.
- Stufen heißen `kapitel:stufe` wie in den Zuordnungsdateien; mehrere mit
  „ | “ getrennt.
- `hauptplatz`: die Stufe, unter der die Aufgabe im Prüfungsheft ganz
  steht. Steht die Aufgabe in `katalog_ids` einer Zuordnung, ist es diese
  Stufe (bei mehreren die zum `typ` passende); sonst die Stufe zum `typ`.
  Leer, wenn der `typ` keiner P10-Stufe entspricht (dann trägt die Zeile
  nur Zwischenschritte).
- `ganz_auch`: Stufen, deren Handgriff die ganze Aufgabe ist, obwohl
  anders etikettiert (Beschluss N2.6: Kästchen-Aufgaben 2022-OS-B1a,
  2023-OS-B1d = Prozentwert; Zinsen 2014/2015 = Prozentwert/Prozentsatz;
  „gemischt“ der Dreiecke). Die Aufgabe steht dort ganz.
- `zwischenschritt`: Stufen, die die Aufgabe nur unterwegs braucht. Quelle:
  `typ_neben` und `verfahren`/`zwischenergebnis`; ein Rechenweg, den
  `verfahren` nur als Alternative nennt, zählt nicht.
- `begruendung`: woher Hauptplatz und Zwischenschritt kommen; Urteile im
  Wortlaut.
- EBR-Zwillinge 2026 (wortgleich mit FOR) übernehmen die Zeile des
  FOR-Teils; GYM-Teile 2015–2019 Basis, die wortgleich mit OS sind, ebenso
  („GYM-Zwilling von …“).

## Regeln, nach denen entschieden wurde

- typ → Stufe über eine feste Tabelle; vier typen hängen am `thema`
  (Punktprobe, Funktionswert, Eigenschaften eines Graphen, Gleichung im
  Sachzusammenhang deuten).
- Lösung durch Einsetzen prüfen (lineare Gleichung 2018, 2022) gilt ganz
  als „Lösung prüfen“ der Quadratischen: gleicher Handgriff.
- Veränderung in Prozent (2016, 2022, 2026) enthält den Prozentsatz als
  Zwischenschritt (Muster `beispiel-zwischenschritt.html`, Beispiel 2);
  Erhöhung um 20 % (2015-OS-K2b, 2024-OS-B1e) den Prozentwert.
- Gleichsetzen Gerade/Parabel und x zu gegebenem y enthalten „Nullstellen
  berechnen“ (p-q-Formel) als Zwischenschritt.
- „Dreieck erst in Figur finden“ enthält Pythagoras schon im Namen; kein
  eigener Zwischenschritt.

## Gegenprobe (Auftrag K)

- Prozentwert 2022–2026 (ohne GYM): 2022-OS-B1a (ganz), 2023-OS-B1d (ganz),
  2024-OS-B1e (Zwischenschritt), 2026-FOR-B1a (Hauptplatz) = vier Jahre.
  Stimmt.
- Grundwert direkt: nur 2023-OS-B1b und 2025-OS-B1a; Bruch-Grundwert als
  Zwischenschritt: 2019-OS-B1g/2019-GYM-B1g (Bruch-Grundwert 4 : 2/3,
  derselbe Basisteil) und 2017-GYM-K4c (8 cm sind 93 %). Stimmt.

## Pflege

Die Datei ist Urteilsarbeit und wird von Hand gepflegt (Werkzeug dieses
Laufs nur im Scratchpad, weil der Schreibbereich kein eigenes Skript
vorsah). `werkzeuge/zuordnung.py` liest sie und baut daraus
`jahre_letzte5` und `nebenplaetze` der Zuordnungsdateien.
