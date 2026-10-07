# Überblick 07.10.2026 – wo das Projekt steht

Bestandsaufnahme aus allen Ziel-, Beschluss-, Plan- und Berichtsdateien der
drei Repos (sechs Leser, je Datei vollständig gelesen; Fundstellen in
Klammern). Zweck: Grundlage für den nächsten Chat, damit nichts neu
hergeleitet wird, was schon entschieden ist.

## 1 Ziel (seit 22.09. im Kern gleich)

Der Lehrer sagt in wenigen Worten, was er braucht, und hat nach wenigen
Minuten ein gutes, druckfertiges Blatt – jedes Thema Kl. 8 bis Abitur,
Schulstoff und Prüfungsvorbereitung (P10, FHR, Abitur). Quelle sind die
Prüfungen, der RLP und die Lehrwerke; nichts wird geraten. Blätter
entstehen durch Auswahl aus der Aufgabenbank; ein Programm setzt, der Chat
ist der Schalter (Linie 26.09., ziel.md § 1). Prüfungsblätter: wer das
Blatt zu einem Thema durchgearbeitet hat, löst die echten Teilaufgaben der
letzten fünf Jahre; „wirksam statt umfangreich“ (offen.html „Skript – was es
leisten soll“, fest 04.10.).

## 2 Was da ist (gezählt)

- Bank: 72 Einträge, 13 612 Aufgaben (+ 784 Basis, 2 177 Zone), alle mit
  Zweitlesung; 2 496 Originalzeilen.
- Themenkatalog: 73 Einträge (29 Sek I, 44 Sek II).
- P10: Zuschnitt 28 Abschnitte in 10 Kapiteln (davon 6 nur Basisteil),
  80 Stufen in den Zuordnungen; je Stufe Zuordnung, Wortlaut, Rückblick;
  140 herausgelöste Aufgaben (42 Stufen); 1 502 fremde Aufgaben; 211
  Erkennen-Sätze; gekürzte Fassungen nur für 2 Abschnitte (19 Zeilen).
- Abitur GK: Zuschnitt 52 Abschnitte (Entwurf), Daten nur für
  Kurvenuntersuchung. LK und FHR: erfasst, aber ohne Zuschnitt.
- Steckbriefe: 2 (Grundwert, Pythagoras) – je ein Zuschnitt-Abschnitt; es
  fehlen 26 für P10 (6 davon Basisteil), 52 für Abitur GK.
- Programme: zusammenbau.py (Lernblatt, Zettel, Hefte, Kompetenzblatt;
  letzter Lauf 01.10.), pruefheft.py v0.5 (Prüfungsheft, Fokusblatt;
  07.10.). Bestellbäume für P10, Abitur, FHR (offen.html, 03./04.10.).
- Prompts: bankblatt.md v5.7 im Repo, im Projekt läuft v5.4 (seit 03.10.);
  unterrichtsblatt.md v4.4, pruefungsblatt.md v0.15 eingefroren.

## 3 Was nicht stimmt (Diagnose)

1. **Der Schalter wurde nie gebaut.** Seit 28.09. steht „Schalter-Prompt“
   bzw. „Blatt-Chat ruft nur auf“ als nächster Schritt (Übergaben 28.09.–
   30.09.; offen.html 05.10. Plan Schritt 4). Kein Blatt-Chat ruft ein
   Programm auf; der Blatt-Chat setzt jedes Blatt von Hand nach muster4.tex
   (alle sechs Protokolle in eingang/). Darum kommt keine Verbesserung der
   Werkstatt in der Stunde an, und jedes Blatt wird neu verhandelt.
2. **Drei Bauwege, drei Wortschätze.** zusammenbau.py, pruefheft.py und der
   Bank-Prompt bauen dasselbe verschieden; Blattsorten heißen in offen.html
   Original / Original neu / Skript (Prüfungsheft), in ziel.md Themenheft /
   Basisheft / Fokus / Probeprüfung, in bauregeln.md Fokusblatt /
   Prüfungsheft / allgemeines Blatt / „mehr“.
3. **Kreisläufe statt Fortschritt.** Merkkasten, Beispiel, Blatt 0/Rückblick,
   Länge, Kennzeichnung, Bedienung, „schwach“ wurden je vier- bis sechsmal
   umgedreht (Übergaben 19.09.–07.10.). Ursache: Regeln entstehen im
   Gespräch statt an benutzten Blättern, und Beschlüsse landen nicht dort,
   wo sie wirken (von den Übergaben selbst achtmal genannt).
4. **Feste Beschlüsse werden übersehen.** offen.html stand in keiner
   Übergabe als Grundlage. Am 07.10. dadurch neu hergeleitet oder
   umgekehrt: Auswahl „wirksam statt umfangreich, jüngere Jahre stärker“
   (fest 04.10.); Fundstellen „immer“, weil viele Schüler das Stark-Heft
   haben (fest 04.10.) – am 07.10. gestrichen; Prüfstein am Ende jedes
   P10-Themas (fest 04.10.) – im Fokusblatt nicht vorhanden.

## 4 Widersprüche, die der Lehrer entscheiden muss

| Punkt | fest bzw. früher | heute (bauregeln.md 07.10.) |
|---|---|---|
| Fundstelle | „immer Fundstelle“, am Ende (Jahr · Aufgabe · Teilaufgabe), Stark-Heft (offen.html, fest 04.10.) | nur Jahresmarke, kein Hinweis (1.4, 6.4, 2.1) |
| Prüfstein | ganze echte Aufgabe am Ende jedes P10-Themas (fest 04.10.) | Fokusblatt ohne; Punkte nur beim Prüfstein des Prüfungshefts (2.1, 6.4) |
| Umfang | alle Teilaufgaben eines Handgriffs auf dem Blatt (vorläufig 04.10.) | Auswahl je Sorte, Rest auf „mehr“ (2.1) |
| Hilfen im Fuß | Kontrollwert → Tipp → Lösung gestuft (fest 04.10.) | nur Ergebnisse, kein Tipp (6.2) |
| Bedienung | Bestellbäume mit Knöpfen (offen.html) | Kurzbefehle, Knöpfe erst nach echten Stunden (9.1) |
| GYM | 53 herausgelöste GYM-Aufgaben mit „nach P10“ (herausgeloest-p10.csv) | GYM wie fremde Länder, ohne „P10“ (2.5) |
| Zählfenster | Zuschnitt 2022–26, Handreichung 2020–26 | Schlusszeile seit 2014 (3.12) |

Außerdem nicht nachgezogen: ziel.md § 3 („Fokus: jede Sprosse zwei- bis
dreimal“, „oberste Sprosse verfremdet“) und § 4 (Heftsorten); bankblatt.md
weicht in rund zwölf Punkten von bauregeln.md ab; uebergabe.md nennt
archivierte Dateien als maßgeblich.

## 5 Liegen geblieben (Auswahl der gewichtigen)

- Schalter / Blatt-Chat ruft Programm (seit 28.09.).
- bankblatt v5.5–5.7 nie als Projektanweisung eingesetzt; Projektdateien im
  Blatt-Projekt nicht bereinigt.
- Abitur- und FHR-Bäume, Vereinheitlichung je Stufe (offen.html 04.10.,
  Stufen 3–7 „prüfen“).
- Formelsammlung sichten (111 Kastenzeilen in 29 Einträgen ungeprüft).
- Darstellung je Handgriff (DZLM) „vor dem Neubau der übrigen P10-Kapitel“.
- 182 Bank-Kopien, 484 schwache Sprossen (vielfalt 06.10.).
- Vollständigkeit/Reihenfolge der 74 Einträge (nur 16 gegen Duden geprüft).
- Bauskripte für handgriffe/herausgelöst nur im Scratchpad.
- Geplante Aufgaben: Abrechnung nie gemessen.

## 6 Weg (Vorschlag, wenige große Schritte)

1. **Zusammenführen statt Neues:** ein Wortschatz für Blattsorten (aus
   offen.html, ergänzt um Fokusblatt), die Widersprüche aus § 4 einmal
   entscheiden, ziel.md und bauregeln.md danach nachziehen.
2. **Den Schalter bauen:** ein Eingang für alle Programme; der Blatt-Chat
   deutet die Bestellung (Bestellbaum) und ruft auf. Prüfstein: im
   Blatt-Projekt liefert „Pythagoras P10“ in zwei Minuten das Blatt vom
   07.10.
3. **Serie:** Steckbriefe für die 26 fehlenden P10-Abschnitte in Runden zu
   etwa zehn (Agent), mit gekürzten Fassungen; Blätter selbst geprüft, der
   Lehrer schickt je Runde eine Sammelliste. Danach Abitur GK (52), FHR,
   Unterrichtsblätter über denselben Weg.
4. **Arbeitsweise:** Beschlüsse in offen.html/bauregeln.md sind bindend, bis
   der Lehrer sie ändert; keine Regel aus einem Gespräch ohne Blatt; jede
   Entscheidung landet im selben Schritt in der Datei, die wirkt; jede
   Übergabe nennt offen.html und diesen Überblick als Grundlage.
