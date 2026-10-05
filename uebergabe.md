# Übergabe verbessereBlaetter – 2026-10-06 (Chat 05./06.10., Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-05.md.

Erster Handgriff im neuen Chat: `offen.html` mit SendUserFile (display
„render“) schicken. Die Beschlüsse vom 05./06.10. stehen dort in den
oberen Listenpunkten „Befunde am Prozent-Probeheft“, „„schwach“ fest“,
„„schwach“, Serie, Lieferung“, „Ziel und Plan „schnell ein gutes
Blatt““, „Lösungsblatt: Inhalt und Darstellung“. Wenn der Lehrer etwas
beurteilen soll: Ausschnitt rendern und rechts zeigen (SendUserFile,
render), nicht nur beschreiben.

## 1 Ziel

Am Stundenanfang in wenigen Minuten ein gutes Blatt – Prüfungsmaterial
(P10, Abitur GK) oder allgemeines Blatt. Weg: Daten je Teilaufgabe
vollständig, ein Bauprogramm setzt auf Bestellung, der Blatt-Chat ruft
nur auf. Nichts wird endgültig gebaut; Regeländerung = neu bauen.

## 2 Arbeitsgrundlage

- `offen.html` – maßgeblich für alle Beschlüsse 04.–06.10.
- Bauprogramm Prüfungsheft: aufgabenbank `werkzeuge/pruefheft.py`
  (+ `pruefheft.md`), Ausgaben `bau/pruefheft/` (vier Prozent-Fassungen
  vom 05.10., Stand vor den Beschlüssen vom 06.10.); Vorlage blattbau
  `mathblatt.sty` 2026-10-05b (Abschnitt P, `\sv`).
- Daten Prozent: `msa/wortlaut-eigen-prozent.csv` (eigener Wortlaut,
  31 Teilaufgaben, abbildung, zwischenfragen), `msa/zuordnung-*.csv`
  (alle P10-Kapitel ↔ Bank-Sprossen, Skript `werkzeuge/zuordnung.py`),
  `msa/prozent-zusatz.jsonl`.
- Kataloge: P10 2014–2026 und Abitur GK 2017–2026 mit kurzloesung,
  zwischenergebnis (Trenner „ ; “), neben, stichwoerter, abhaengig_von;
  Beitabellen in archiv/; `katalog-prompt.md` 0.10.
- Regeldateien nachgezogen bis Stand 05.10. abends: `ziel.md` (§ 2
  Lösungen, schwach), `bank.md` (achte Fassung, 12/6), `bankblatt.md`
  v5.5, `bau/layout-befunde.md` (Befund Lösungsblatt 05.10.).
- Befunde: `befund-punkte-eichung-2026-10-05.md`,
  `befund-bestand-2026-10-05.md`.
- Original-Wortlaut liegt nur auf dem Rechner des Lehrers
  (`~/mathe/mathe-nachhilfe/hefte-md/`, P10 2014–2026, Abitur 2022–2026);
  Ordner hefte und hefte-md waren für diese Sitzung freigegeben.

## 3 Arbeitsstand

Erledigt 05./06.10.: Beitabellen in den Katalog (Option B); Vorrat P10
2014–2021 und Abitur GK 2017–2021; Punkte-Eichung; Bestandsaufnahme;
Zuordnung aller P10-Kapitel mit Auffüllen auf 12/6 (fehlten nur 11);
Regeln Stand 05.10. nachgezogen; Bauprogramm gebaut, Prozent in vier
Fassungen; Urteil des Lehrers am Probeheft.

Beschlossen 06.10. (Wortlaut offen.html), noch NICHT in Regeldateien,
Bauprogramm und Prompt:
- Eine Leiter für alle Blätter: Vorstufen zuerst (normal zwei, schwach
  alle von unten), Reihenfolge glatt vor krumm, wenig Text vor viel,
  eine Frage vor zwei, Prüfungshöhe zuletzt; Zahlen unten im Kopf
  rechenbar, Mitte glatt mit Taschenrechner, oben wie in der Prüfung;
  „eine leichte Aufgabe zu viel schadet keinem“. Heranführen = Leiter
  unten verlängern; Zwischenfragen nur bei Mehrschritt-Aufgaben.
- Je Stufe kleine Gruppen nach Form (rechnen, Sachaufgabe, Ankreuzen,
  Vergleich); „weitere dieser Art“ nur innerhalb einer Gruppe.
- Satz: Aufgaben untereinander mit Rechenplatz nach Schrittzahl;
  Übersicht vorn entfällt; Überschrift = Stufenname mit Bezeichnung
  („Grundwert G“), kein „neu:“, dahinter grau „in 3 der letzten 5
  Prüfungen“ / „selten geprüft“; Aufgabenzeile: grau „P10 ’26“ links,
  Nummer, Aufgabe, Punkte rechts; Aufgabenbild als ein Wort („Tarif“)
  am Gruppenanfang; Formel einmal an der Aufgabe, ab der sie gebraucht
  wird; Darstellungen (DZLM) bei den Vorstufen, nach oben verschwindend.
- Rückblick vorn auf jedem Blatt/jeder Portion; erste Portion =
  Grundlagen, eine Aufgabe je Voraussetzung, mind. drei (schwach zwei
  je Voraussetzung). Portion darf nach einer Gruppe enden.
- Seitenfuß für alle Blätter, ohne Ausnahme: Kontrollwert, Tipp nur als
  Ansatz. Lösungsdatei ohne Punkte. Ergebnisse exakt zuerst, dann ≈.
- Eigene Aufgaben im Prüfungsheft: unten, Lücken, Ersatz, selten
  geprüft; nie oben, nie Prüfstein, nie als Prüfung getarnt.
- Fokusblatt (Nachlieferung) beginnt ganz unten. Prüfstein: ganze
  echte Aufgabe aus den letzten fünf Jahren, ohne Nummer.

Messwerte: Opus-Agenten ≈ 0,5 Mio Token je Wochenpunkt (zwei Läufe:
423 000 → Woche 0 → 1 %, 496 000 → 1 → 2 %); Fable ≈ 185 000.
Letzter abgelesener Stand 05.10. abends: Woche 2 %, Fable 0 %; danach
liefen Bauprogramm und Zuordnung (≈ 635 000 Token) – nicht abgelesen.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Inhalt fest („ein Blatt für alle“, eine Leiter je Thema mit Kern),
  Lieferung ist Stellschraube (Portion, Vorstufen, Gerüst).
- „schwach“ = Leiter beginnt weiter unten, Blatt 0 dicht, Raster,
  Gerüst gegeben/gesucht/Formel nur bei Formel-Aufgaben, Lösung
  „Wort + Ansatz ⇒ Wert“. Stoff und Höhe gleich; nichts wird
  ausgeschlossen (Schwache fragen auch nach Prozent).
- Katalog und Bank werden verbunden (Zuordnungstabellen), nicht
  zusammengeführt. Ziel 12 Aufgaben je Kern-Stufe, 6 sonst; neu zählt
  nur, was man nicht durch Erinnern löst.
- Begriffe: „Bauprogramm“ = Werkzeug; „Prüfungsheft“ = Heftart (früher
  „Skript“).
- Revisionsschranke: Beschlüsse nur neu aufmachen, wenn ein Blatt oder
  Messwert dagegen spricht; Einfälle auf die Liste in offen.html.
- Ton: Vorschläge als Frage, nicht als Schlussstrich (Lehrer 05.10.).

## 5 Offene Punkte und Verworfenes

- Offen: schlankes Modell (Standardblatt, „schwach“ einziger Zusatz,
  Nachliefern per Fokus) – Lehrer tendiert dazu, keine Sonderfälle;
  Anrede Sie/Du (unwichtig, Wahl offen); Layout-Gespräch Prüfungsheft;
  Form der Lösungsdatei an Analysis prüfen; Kopf der Aufgabe braucht
  ein Datenfeld; Vorspann/Abbildung/Optionen als getypte Felder
  (Datenformat-Erkenntnisse im Bericht des Bauprogramms, stand.md);
  Trenner „ ; “ kollidiert mit „; “ im Eintrag; Kern-Urteile dünn bei
  Gleichungssystemen.
- Verworfen: Zusammenführen Katalog/Bank (Verwaltung); „leichte Punkte“
  als Bestellung/Ordnung und Ziel „bestehen“ je Schüler (zu viele
  Sonderfälle); Übersicht/Stichwortverzeichnis vorn (liest keiner);
  „mit lösungsweg“ (Rechenweg nie gebraucht); Fehlerhinweise auf dem
  Lösungsblatt; Zerlegung einer Ein-Schritt-Aufgabe in Zwischenfragen
  (Nr. 6: das Problem ist das Zuordnen, nicht das Rechnen); Leitaufgabe
  = echte Prüfungsaufgabe vorn.

## 6 Nächster Arbeitsschritt

Nach Ablesen der Nutzungsanzeige: ein Lauf (Opus) zieht die Beschlüsse
vom 06.10. nach – Regeldateien (ziel.md, bank.md, bankblatt.md → v5.6,
layout-befunde.md), Bauprogramm (Leiter, Gruppen, Satz, Rückblick, Fuß,
Lösungsdatei, Zahlenregel, exakte Werte per sympy in kurzloesung) – und
baut das Prozent-Heft und das Fokusblatt Grundwert neu; parallel
Probeheft Abitur GK Kurvenuntersuchung (Lösungsdatei an Analysis
prüfen). Danach zeigt der Chat dem Lehrer die Seiten rechts. bankblatt
erst als v5.6 an den Lehrer (Chat-Block für erzeugeBlatt(Bank)).
Modell: Opus im Chat und für Agenten.
