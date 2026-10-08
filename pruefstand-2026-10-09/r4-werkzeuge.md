# Prüfstand 09.10.2026 – Leser 4: Werkzeuge, Prompts, echter Betrieb

Grundlage: alle `.py` unter `aufgabenbank/werkzeuge/` und
`mathe-nachhilfe/werkzeuge/`, `blattbau/` (bankblatt.md ganz, die beiden
alten Prompts in Gliederung, README, CHANGELOG, Anleitung), `aufgabenbank/
eingang/`, `bau/register.csv`, `bau/hefte-einzel/`, `anweisungen/projekt-
verbessereBlaetter.md`, `kandidaten.md` (Messwerte). Hinweis zur Belegbarkeit:
alle vier Klone sind flach (shallow), die Historie beginnt am 07.10. (mathe-
nachhilfe, aufgabenbank) bzw. 19./22.09. (anweisungen, blattbau). „Zuletzt
geändert 2026-10-07“ heißt deshalb nur „seit dem Erstcommit des Klons
unverändert“; das wahre Alter steht im Docstring.

## Teil 1 – Entscheidungen

| Entscheidung | Datum | Grund | gilt noch? | Widerspruch / Doppel | Beleg |
|---|---|---|---|---|---|
| Drei Prompts als Projektanweisung: Unterrichtsblatt (v4.4), Prüfungsblatt (v0.15), Bankblatt (v5.8) | 26.09. / 17.09. / 07.10. | je Blattsorte ein Chat-Projekt | unklar: plan.md W1 nennt nur pruefheft.py als Basis und v5.8 als „Notweg“; ub/pb werden nirgends mehr als Betriebsweg genannt, nur als Steinbruch (uebergabe § 6) | Projektanweisung § „Vom Repo in den Betrieb“ beschreibt weiter alle drei als laufend | blattbau README; plan.md § 3 W1; uebergabe.md § 6 |
| Bauregeln haben Vorrang vor dem Bank-Prompt; Prompt ist Kurzfassung | 07.10. (v5.8) | eine Regeldatei statt Doppelung | ja, aber v5.8 zitiert Nummern der Fassung bis 07.10. („Bauregeln 3.10, 6.6–6.8, 6.13, 1.4, 6.4, 3.5, 3.2“); bauregeln.md wurde am 08.10. neu nummeriert (§ 3 ist jetzt „Übersicht und Serie“) | pruefheft.py zitiert ebenfalls alte Nummern (3.12, 3.2, 3.3, 3.4, 3.6, 2.1) | bankblatt.md Z. 78–89, 100–103, 148; bauregeln.md; archiv/bauregeln-bis-2026-10-07.md; uebergabe § 3 „nicht nachgezogen“ |
| Blatt-Chat trägt Erfundenes selbst in die Bank ein, ohne Rückfrage (Option A) | 01.10. (v5.2) | 44 erfundene Aufgaben blieben im Archiv; Karte kam erst nach 9 min | ja im Prompt; in der Praxis: von 6 Blättern wurden 31+15+?+2+7+12 Zeilen übernommen, 1+11+17+8+7 als Dublette verworfen | plan.md § 2 Linie: Bank „Steinbruch“ (Option B) würde das Eintragen zur Nebensache machen | CHANGELOG v5.2; Protokolle eingang/* |
| Ein Bauprogramm: pruefheft.py Basis, zusammenbau.py (7 826 Zeilen) nicht weiterentwickelt | 08.10. | zwei Programme für dasselbe | ja | zusammenbau.py ist das meistgenannte Skript (54 Dateien) und trägt alle Rezepte L/F/S/K/H/Z/P des Registers; pruefheft.py kennt nur Prüfhefte und Fokus | plan.md W1; register.csv |
| Mappe statt Quellen lesen (mappe.py) | 26.09. | Lesen ist Kostentreiber (10 $ je 275 Aufgaben) | ja für bankblatt.md („mappen/<eintrag>.md“); offen, ob pruefheft.py/Katalog-Gliederung die Mappe noch brauchen | 92 Nennungen, aber seit 07.10. kein Mappenbau belegt | kandidaten.md Z. ~480; bankblatt.md Z. 58 |
| Testlauf je Prompt-Version mit fester Eingabeliste (testlauf-*.py, blatt-pruef.py, einsortieren.py) | 25./26.09. | Regeltest des Unterrichtsblatt-Prompts | nein, faktisch: letzter Testlauf 26.09., blaetter/index.md hat 6 Zeilen (letzte 24.09.), kein Blatt seit v4.4 abgelegt | Projektanweisung beschreibt den Testlauf als „Regeltest einer Version“ | blaetter/index.md; archiv/auftrag-testlauf-2026-09-26.md |
| Repo mit Schreibzugang als erster Schritt des Blatt-Chats (Karte, Modus Manuell) | 01.10. | Karte kam zu spät | ja | – | bankblatt.md „Erster Schritt“; Projektanweisung |
| Schülerliste privat, nur Nummer außerhalb des Chats | 03.10. (v5.4) | Datenschutz | ja; gebaut.csv hat 2 Zeilen (S06, S02) | faellig: Liste soll nach aufgabenbank-privat wandern | bankblatt.md „Name“; eingang/gebaut.csv |
| „schwach“ ändert Form, nicht Auswahl | 01.10. (v5.3) | Lehrer: „wenig Unterschied“ | ersetzt durch „Einstieg unten/oben“ (Versuch 08.10.) – der Prompt v5.8 kennt das Wort nicht | bankblatt § „schwach“ ↔ uebergabe § 4 | CHANGELOG v5.3; uebergabe.md § 4 |
| Exakt vor gerundet (exakt.py, exakt-prozent.py) | 06.10. | Beschluss 24 | ja (bauregeln 5.1) | – | exakt.py Kopf |
| Prüfungsgliederung ist das gepflegte Objekt; zuordnung-*.csv, zuschnitt, handgriffe sind erzeugte Sichten (Entscheidung A) | 08.10. | Daten lagen im Skript | ja; gliederung-extrakt.py ist einmaliger Lauf, der noch im Werkzeugordner liegt | prozent-zuordnung.py ist durch zuordnung.py ersetzt (byteidentisch), wird aber noch in 4 Dateien genannt | gliederung*.py, zuordnung.py v2 |
| Modell Opus Regelfall, Fable nur auf Wunsch, Sonnet nie im Chat | 26.09. | Vergleiche gleichauf, Kontingente knapp | unklar: Protokolle zeigen Fable 5.1 (01.10., vier Blätter) und Opus 5.5 (05./06.10.); dieser Leser läuft auf Fable | – | Protokolle; Projektanweisung § Modellwahl |

## Teil 2 – Ideen, die liegen blieben

| Idee | wann | warum liegen geblieben | Beleg |
|---|---|---|---|
| Duden-9-Eingang: 255 Aufgabenentwürfe aus 10 Kapiteln, 20 Skripte mit Sitzungspfaden | 02.10. | nicht benutzt: „nicht in die Bank übernommen“, wartet auf Katalognachzug; danach kein Commit mehr dazu | eingang/duden9-2026-10-02/protokoll.md |
| Regal: Plan aller Kompetenzblätter (regal.py, bau/regal/) | 28.09. | nicht benutzt seit zusammenbau.py eingefroren; Rezept K zuletzt 28.09. (5 Blätter) | regal.py Kopf; register.csv |
| Bandbau, Korpus, FHR-Band (band-bau.py, korpus-bau.py, fhr-band-struktur.py, zwtrenner.py) | 18./19.09. | unbekannt; brauchen `hefte/` am Rechner, kein Nachfolgeauftrag | Docstrings; konzept.md |
| Klassen-/Prüfungswort-/Sek-II-Belege mit Datendateien (6 Skripte, 7 100 Zeilen) | 26./27.09. | nicht benutzt: Katalogmarken fertig gebaut (marken-bau.py), seither keine Nachtaufträge | nacht-bericht-2026-09-2x.md |
| Testlauf-Kette (5 Skripte) und einsortieren.py | 25./26.09. | vergessen: kein Lauf nach dem Wechsel auf die Bank (26.09. Linie) | blaetter/testlauf-2026-09-26 |
| Ertrag je Typ, Themeninventar, Tragfähigkeit, gym-vergleich, typen-abgleich | 19.–24.09. | Beschluss (Phase Katalogbau abgeschlossen); einmalige Messungen | README mathe-nachhilfe |
| 20 Nachzug-Skripte `einmalig/nachzug-*-2026-09-29.py` (13 000 Zeilen) | 29.09. | erledigt, nie wieder aufgerufen; 9 davon in keiner .md genannt | grep |
| Vielfalt-Messung (vielfalt.py, vielfalt-p10) und Aufräumposten „182 Kopien“ | 06.10. | Posten offen in faellig.md | faellig.md § 2 |
| Punkte-Eichung (Faustregel Zwischenergebnisse) | 05.10. | einmaliger Befund, keine Folge | befund-punkte-eichung-2026-10-05.md |
| Handy-Start eines Blatt-Chats, Projektdateien im Aufgaben-Projekt löschen, pruefungsblatt-Projektanweisung nachziehen (seit 17.09. „defekt“) | 17.09.–03.10. | liegen beim Lehrer in faellig.md § 1 | faellig.md Z. 178–182 |
| Selbstlernheft Kl. 11 ohne Bank (hefte-einzel) als Beleg für Weg B | 08.10. | nicht liegen geblieben, aber auch nirgends im Plan: kein Register-Eintrag, kein Werkzeug, Skript im Scratchpad | uebergabe § 5; plan.md (keine Nennung) |

## Teil 3 – Befunde zur Komplexität

**3.1 Echter Betrieb (eingang/).** Sechs Blätter im Unterricht bestellt,
alle zwischen 01.10. und 06.10., alle mit dem Bank-Prompt, kein einziges
mit dem Prüfungsblatt- oder dem Unterrichtsblatt-Prompt: terme (4× am 01.10.,
davon 2× „schwach“ in zwei Lesarten, Fable 5.1, v5.1/v5.3), Einsetzungs-
verfahren für S06 „schwach, dichtes Blatt 0“ mit Zuruf „keine p10!“ (05.10.,
Opus, v5.4), Lineare Funktionen für S02 „10 klasse p10“ (06.10., Opus,
v5.4). Umfang 7–23 Seiten, 68–169 Teilaufgaben; das „schwach“-Blatt mit
23 Seiten ist die Ausnahme, die der Lehrer am 01.10. mit „wenig Unterschied“
quittierte. Dauer steht in keinem Protokoll (Vermutung: v5.x verlangt keine
Zeitstempel mehr, v3.29 hatte sie); belegt sind nur „Karte nach neun
Minuten“ (CHANGELOG v5.2), 58 s für ein Programmheft Pythagoras (plan.md M1)
und 21 min + Kritik + Nachbesserung für das Selbstlernheft ohne Bank
(uebergabe § 5). Was schiefging, steht in den Protokollen selbst: jedes
Blatt baute eigene Satzmakros nach (\rk, \rfr, \sz, \malkreuz, \eb …), weil
Vorlage und Anleitung die Formen nicht kennen; Bankstand wechselte während
des Baus (c); 40 % der Erfindungen fielen als Dubletten; bank-pruef.py
meldet Altlasten (173 bzw. 158 Abweichungen vor der Übernahme), sodass die
„0 Abweichungen“-Regel des Prompts nicht prüfbar ist. Lehrerurteile sind nur
indirekt belegt (CHANGELOG-Anlässe), das Feld „Befunde“ im Protokoll gibt
es erst seit v5.8 und ist noch leer. gebaut.csv: 2 Zeilen.

**3.2 Register.** 92 Blätter, davon 61 am 28.09. (Rezepte P 30, H 13,
Z 10, K 5, L 2, F 1), 23 Prüfhefte „PH“ am 06.10., 7 Lernblätter gesamt,
3 Fokus; nach dem 07.10. nichts. Die Kennungsregel (drei Zeichen gegen das
Register) der Bauregeln 6.3 passt nicht zum Schema des Registers (PRZ-L1,
KUR-PH1). Das Selbstlernheft vom 08.10. fehlt im Register.

**3.3 Prompts.** bankblatt.md (2 552 Wörter) ist in Betrieb und ruft auf:
Repo-Werkzeug, Raw-URLs (katalog/index.md, blattbau/mathblatt.sty,
Anleitung), `bank-pruef.py <eintrag> --katalog`, sympy, xelatex; liest
Mappe, Bank, stand.md, muster4.tex, eingang/, bauregeln.md,
msa/herausgeloest-p10.csv, msa/fremd/, Schuelerliste-privat.md. Er nennt
sieben alte Bauregel-Nummern (s. Teil 1) und beschreibt in ~190 Zeilen
Aufbau, Lösungen, „schwach“, obwohl er sich zur Kurzfassung erklärt – doppelt
mit bauregeln.md § 4–8. unterrichtsblatt.md (10 631 Wörter, v4.4, 26.09.)
und pruefungsblatt.md (6 849 Wörter, v0.15, 17.09.) rufen curl auf
katalog/*.md bzw. msa/msa-*.csv auf und verlangen `pruef.py`-Archive;
pruefungsblatt.md Z. 2 nennt noch mathe-nachhilfe als Masterrepo (README
„bekannte Abweichung“ seit 19.09.). Die Anleitung (7 660 Wörter, „Stufe 6“,
Vorlagenversion 2026-10-06) hat 18 Abschnitte; der Prüfheft-Abschnitt P
der Vorlage ist in der Gliederung nicht als eigener Abschnitt sichtbar.
CHANGELOG führt vier Kapitel (Bank, Vorlage, masterprompt, pruefungsprompt)
mit Datumsreihen bis 05.09. – 3 547 Wörter, die niemand zum Bauen liest.

**3.4 Projektanweisung (3 102 Wörter).** Zu komplex, gemessen am Ziel
„wenige Wörter → drei PDFs in 3 min“: Rund 1 100 Wörter (§ Arbeitsteilung,
Handy, PowerShell, Web-Sitzungen, geplante Aufgaben) regeln Wege, die laut
Bestand seit dem 28.09. nicht benutzt werden (Cloud-Guthaben 0 €, kein
Testlauf, keine Nachtaufträge seit 28.09., Code-Tab-Blöcke mit `=====
Datei n`). § „Vom Repo in den Betrieb“ beschreibt den Testlauf-Zyklus und
einsortieren.py als Regelweg; plan.md kennt beides nicht. Rolle („Katalog
und die beiden Prompts“) und Repo-Liste (drei Repos, tatsächlich vier plus
aufgabenbank-privat) sind veraltet; plan.md, bauregeln.md, pruefheft.py,
gliederung/ kommen nicht vor, obwohl uebergabe.md sie als maßgeblich nennt.
Chatstart liest ziel.md zuerst, uebergabe sagt „maßgeblich ist plan.md“.
Zum Modell: Anweisung sagt Opus; die Praxis am 01.10. lief auf Fable.
Vorschlag: Projektanweisung auf Rolle, Chatstart (plan.md, uebergabe,
tafel), Umgang, Modell je Messwert und Umzug kürzen; Wege, die den Rechner
brauchen, in eine Datei `anweisungen/wege.md` archivieren, die nur bei
Bedarf gelesen wird.

**3.5 kandidaten.md Messwerte (16 Treffer).** Tragend für das Ziel: Lesen
ist der Kostentreiber (1 Mio Token für 340 KB; 10 $ je 275 Aufgaben), enge
Agenten kosten ≈ 0,5–0,7 Mio Token je Wochenpunkt (09.10.), Opus-Agenten
schonen die Woche (05.10.), Bilder kosten Kontext (07.10.), „Prüfungsstufe =
Einheit“ traf nur 38/80 (08.10.). Die Karten-Regel „nur Manuell“ (01.10.)
und „Abrechnung ist Messwert“ (28.09.) sind doppelt in Projektanweisung und
kandidaten.md.

**3.6 Skripte.** 83 Dateien, 68 000 Zeilen; 27 davon einmalig (13 000
Zeilen), 9 ohne jede Nennung. Was ein neuer Agent übersehen würde: dass
zusammenbau.py eingefroren ist (steht nur in plan.md W1), dass
prozent-zuordnung.py und gliederung-extrakt.py erledigt sind, dass die
Testlauf-Kette tot ist. Tabelle (Datum = Docstring, da Klon flach; „genannt“
= Zahl der .md/.py/.csv-Dateien der vier Repos mit dem Dateinamen):

| Skript | Zweck | Zeilen | zuletzt | genannt | Vorschlag |
|---|---|---|---|---|---|
| ab/pruefheft.py | Prüfungsheft/Fokus aus Daten, ohne Modell | 5192 | 08.10. | 22 | behalten (Basis W1) |
| ab/abbildung.py | TikZ aus Feld abbildung, von pruefheft gerufen | 2312 | 07.10. | 4 | behalten |
| ab/bank-pruef.py | Prüfung der Bank v0.14 | 1963 | 08.10. | 220 | behalten; Altlasten-Meldungen bereinigen |
| ab/zusammenbau.py | LaTeX aus Bank, Rezepte L/F/S/K/H/Z/P | 7826 | 07.10. | 54 | archivieren (W1), Register-Spalte bleibt |
| ab/steckbrief.py | liest Fokus-Blöcke der Gliederung | 302 | 08.10. | 11 | behalten |
| ab/mappe.py | Mappe je Eintrag | 442 | 07.10. | 92 | behalten, solange v5.8 Notweg |
| ab/befunde.py, duplikate.py | Sammeln aus stand.md; Dubletten | 569/434 | 07.10. | 2/4 | zusammenlegen mit bank-pruef.py |
| ab/punkte.py, punkte-nachziehen.py | Punkte der Originale | 210/112 | 07.10. | 5/18 | behalten |
| ab/regal.py | Plan Kompetenzblätter | 391 | 28.09. | 2 | archivieren |
| ab/vielfalt.py | Vielfalt der P10-Hefte | 515 | 06.10. | 4 | behalten bis Aufräumposten |
| ab/einmalig/* (27) | Nachzüge 29./30.09. | 13 000 | 29.09. | 0–5 | archivieren |
| mn/gliederung.py, -sichten.py | Gliederung lesen, Sichten bauen | 189/80 | 08.10. | 5/28 | behalten |
| mn/gliederung-extrakt.py | einmaliger Umzug 08.10. | 227 | 08.10. | 3 | archivieren |
| mn/zuordnung.py | Zuordnung Heft↔Bank v2 | 214 | 08.10. | 34 | behalten |
| mn/prozent-zuordnung.py | Vorgänger, byteidentisch | 122 | 05.10. | 4 | archivieren |
| mn/tafel.py | Fortschrittstafel M1 | 227 | 08.10. | 4 | behalten |
| mn/skript-zuschnitt.py, skript-filter-mass.py | Zuschnitt prüfen / Filtermaß | 136/77 | 04.10. | 9/3 | zuschnitt: zusammenlegen mit gliederung-sichten; filter-mass archivieren |
| mn/vorrat-pruef.py, vorrat-sympy-* (3) | Beitabellen, sympy-Kontrolle P10/Abi | 101+3553 | 04./05.10. | 7/1–3 | behalten (Gegenprobe) |
| mn/exakt.py, exakt-prozent.py | exakt vor gerundet | 215/55 | 06.10. | 0/1 | archivieren (gelaufen) |
| mn/zwtrenner.py | Trennzeichen zwischenergebnis | 108 | 05.10. | 5 | archivieren |
| mn/handreichung-abi.py, -reihenfolge.py | Daten Handreichungen | 151/88 | 03.10. | 5/2 | behalten |
| mn/baum-offen.py | Bestellbaum offen.html | 91 | 03.10. | 6 | behalten (plan M? Bestellung) |
| mn/bestand.py | Zählung Bank/Katalog | 140 | 05.10. | 3 | zusammenlegen mit tafel.py |
| mn/punkte-eichung.py | Faustregel-Quote | 66 | 05.10. | 1 | archivieren |
| mn/blatt-pruef.py | Kennzahlen je Blatt v0.5 | 1136 | 05.10. | 51 | archivieren mit Testlauf-Kette |
| mn/testlauf-*.py (5) | Testlauf v4.x | 1147 | 26.09. | 3–7 | archivieren |
| mn/einsortieren.py | Protokoll-Zip nach blaetter/ | 209 | 22.09. | 23 | archivieren |
| mn/klassen-belege*.py, klassen-ermessen.py, pruefungswort-belege*.py, sek2-ordnung-belege*.py, marken-bau.py | Katalogmarken aus Lehrwerken | 7 937 | 26./27.09. | 5–25 | archivieren (gelaufen; marken-bau behalten, falls Marken nachziehen) |
| mn/blatt0-belege.py, tragfaehigkeit.py, verweis-pruef.py, themen-pruef.py | Katalogprüfungen v0.2 | 2 419 | 20./21.09. | 15/20/22/33 | verweis-pruef und themen-pruef behalten (Prüfung), Rest archivieren |
| mn/rohdatei-bau.py | Rohdatei je Thema | 272 | 19.09. | 91 | archivieren (Katalog steht) |
| mn/band-bau.py, fhr-band-struktur.py, korpus-bau.py | Bände/Korpus aus hefte/ | 1 427 | 18.09. | 5/5/5 | archivieren (Rechner-Weg) |
| mn/ertrag.py, themen-inventar.py, gym-vergleich.py, typen-abgleich.py, cas-vergleich.py | Messungen Katalogphase | 1 324 | 19.–28.09. | 3–13 | archivieren |
| mn/dnb-sru.py | DNB-Suche | 33 | – | 16 | behalten (Quellen) |

Vermutung, nicht Beleg: Die Nennungszahl misst Erwähnung, nicht Aufruf; ein
Aufruf-Protokoll gibt es nur für bank-pruef.py (Protokolle) und
pruefheft.py (register.csv).
