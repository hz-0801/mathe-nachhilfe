# R3 – Konzept- und Regeldateien: was gilt, was sich widerspricht, was doppelt ist

Gelesen: die Konzept- und Regeldateien des Auftrags, dazu plan.md, uebergabe.md; Stichproben README, pythagoras.md, befunde.md, pruefheft.md, bankblatt.md.

Gezählt: Katalog 74 Einträge (29 Sek I, 44 Sek II), 276 Lerneinheiten, Gewicht 56 Kern / 2 Rand. Bank 74 Ordner, 372 jsonl, 16 743 Zeilen (13 720 e<n>, 2 177 Zone, 784 Basis, 117 weg.jsonl, 15 ruht). Je e/zone-Zeile 19 Pflichtfelder; gefüllt: antwort 47 %, pruef 78 %, original 20 % (3 271), grafik 18 %, loesungsgrafik 3 %; pflicht 2 676, herkunft 828; **bild 0** (seit 06.10. in bank.md, nie gesetzt). Nicht in bank.md: ergebnis/tipp/ist_original/verfremdung/vorstufe (nur _basis, Prüfskript v0.14), schritte/fehlerstelle (weg.jsonl, ohne hoehe), form „rechnung“ (79), „raster“ (38). Prüfkennung „(P10 2023 OS)“ steht in 2 523 von 2 542 Originalzeilen im Aufgabentext; bauregeln 6.4 will sie als Randmarke. Katalogfeld kurzloesung (Lösungsquelle laut bauregeln 8.4): msa 393/418, abi 499/887, gym/fhr/iqb 0.

## 1 Entscheidungen

| Entscheidung | Datum | Grund | gilt noch? | Widerspruch / Doppel mit | Beleg |
|---|---|---|---|---|---|
| Blätter durch Auswahl aus der Bank | 26.09. | Chat baut jedes Mal anders | ja (plan Linie 1); **unklar** seit 08.10.: „Bau von unten gescheitert“, A/B offen | konzept E10 „nur aus dem Katalog“ | ziel § 1; plan § 2; uebergabe § 4–5 |
| Eine Regeldatei bauregeln.md | 07.10. | Regeln in sechs Dateien | ja | bank.md hält Blattregeln weiter (Prüfkennung am Satzende, Punkte, loesung-Blattform, Option schwach, Zettelrezept); pruefheft.py nennt beschluesse-06.10. (nur noch Stub) als Regelquelle | bank.md Z. 167, 420, 505; pruefheft.md Kopf |
| Länge: so lang wie der Zweck | 08./09.10. | „kurz“ machte Blätter dünn | ja | ziel § 1 „Richtung: kurz (Bauregeln 1.2)“ | bauregeln 1.2; plan § 5 |
| Blatt = Lerneinheit | 08.10. | Lehrwerksfolge | ja | ziel § 1 „Baum“: ein Blatt zeigt alle Zweige eines Themas; ziel § 3 „alle Zweige des Teils“ | begriffe; bauregeln 3.1 |
| Ein Blatt für alle, kein Dialog über die Lage | 28.09. | Schalter fragt nur den Teil | **unklar**: Einstieg unten/oben (Versuch 08.10.), drei Durchgänge (Richtung), Option „schwach“ (ziel § 6, bank.md), `--art schwach` (Programm) | vier Fassungen einer Stellschraube | ziel § 1; bauregeln § 9; plan § 5 |
| Blattsorten | 07.–08.10. | Bestellbaum | ja (bauregeln 2.2) | ziel § 3–4 ohne Prüfungsblatt/„mehr“; blatt-konzept § 2 Themenheft/Basisheft/Vorbereitung/Probeprüfung; konzept E40 „sieben Themenhefte“; Basiszettel nur bank.md | vier Listen |
| Reihenfolge aus dem Katalog; Kern/Rand ist Marke | 08.10. | Gliederung ordnet nicht | ja | konzept E38 Blattregel „Kern vorn, Rand am Ende“; Kern-Kriterium E38 (Prüfung verlangt) ≠ bauregeln 3.3 (Häufigkeit / Verlagsmarke) | plan § 5; bauregeln 2.4, 3.3 |
| Kein Merkkasten; Beispiel grau als a) | 08.10. | Regelzwang | ja | ziel § 6 „Merkkasten am Ende“; Musterbeispiel „ruht“ dreifach | bauregeln 1.5 |
| Punkte nur beim Prüfstein des Prüfungshefts | 06.–07.10. | – | ja | bank.md „Prüfungsheft **und Prüfungs-Fokus**“ | bauregeln 6.4 |
| Herkunft als Marke, Originalliste am Ende | 06.–08.10. | Stark-Heft | ja | konzept E5, blatt-konzept § 6 „keine Quelle im Heft“, „Stern = Niveaumarke“ | bauregeln 6.4–6.5 |
| Original im Lernblatt nur als beste Aufgabe; Pflicht nur Prüfungsblatt | 09.10. | Prüfstein Hypotenuse | ja | konzept E3 „Decke ist das Original“, E40 „Original vorn als Test“; blatt-konzept § 3/6 Deckenwahl, „verfremdet ist Standard“ (E40 revidiert es, Datei nicht nachgezogen) | ziel § 3; bauregeln 4.1, 4.9 |
| Lösungen: Ergebnis fett, Ansatz ⇒ Wert, kein Antwortsatz | 05.–06.10. | Eichung | ja | bank.md loesung verlangt Antwortsatz und Probe-Zeile – zwei Formen in einem Feld; konzept E6, blatt-konzept § 6 Dreiteilung | bauregeln 8; bank.md |
| Leiterregeln (Rückwärts, Misch, krumm oben) | 02.10. | Duden-Abgleich | ja | fünfmal gleichlautend: konzept E38, ziel § 6, bank.md (2×), katalog/_vorlage.md | – |
| Themenkatalog setzt keine Decke | 12.09. | Decke aus Prüfung | nein, ersetzt: ziel § 3 „Katalog setzt Höhe nach Lehrwerk“; 1 381 Bankzeilen hoehe pruefung | konzept § 3 | ziel § 3 |
| Vorrang der Dateien | laufend | – | **widersprüchlich**: konzept „maßgeblich“; blatt-konzept „gilt bei Widerspruch“; ziel „beide ordnen sich unter“; bauregeln „über ihr plan.md“; plan nennt ziel.md nicht | fünf Köpfe | Kopfzeilen |
| Erfassung (Kern, Profile) | bis 05.10. | – | ja | CLAUDE.md Z. 3 „flach in der Wurzel“ gegen § 1; E22 „Lehrer pusht“ | CLAUDE.md |
| Mengen je Kette: Grundfall 5, Ziel 12 je Kern-Stufe | 29.09./05.10. | zwei Durchgänge mit Check, Rückblick | **unklar**: Bedarf rechnet mit Blattteilen, die es nicht mehr gibt; Katalog „(4×)“ gegen Bank 5 (Befund K-010); uebergabe § 6 „nicht übernehmen: Grundfall vier- bis fünfmal“ | bauregeln 4.7 „jede Sorte einmal“ | bank.md Mengen |

## 2 Ideen, die liegen blieben

| Idee | wann | warum | Beleg |
|---|---|---|---|
| Zonenverweis „hängst du hier → Fokus“ | 28.09. | dreifach: offen (ziel § 5), „fällt“ (Streichliste), „Später“ (plan § 6) | – |
| Klasse je Einheit aus Inhaltsverzeichnissen | 28.09. | erledigt (Marken in jedem Eintrag), steht noch als offen | ziel § 5; pythagoras.md Z. 12 |
| „oft“-Schwelle; 22 Sprossen ohne Original; MAKOS-Folge | 28.09. | Daten da, nie entschieden / Lauf nie gestartet / unbekannt | ziel § 5 |
| Verschmelzung der Prompte, Boden Kl. 5–7, mündlich, Kursart | 22.–28.09. | Beschluss „Später“; Prompts durch Programm überholt | ziel § 5; plan § 6 |
| Merkmalsfrage; Zip-Regression, Nachbartypen, Heft A | 09.–12.09. | durch E40 gegenstandslos / vergessen | blatt-konzept § 7 |
| Sechs Posten konzept § 6 (Variante A, Statuswerte, E14 …) | 17.09. | „wartet auf …“ – Auslöser nie geprüft | konzept § 6 |
| Wiedervorlagen E38 (zehn Blätter), E40 (Jan. 2027) | 02.10. | niemand zählt | konzept § 4 |
| Parallelaufgaben per sympy, „zuerst Prozent“ | 05.10. | nicht benutzt (keine Spur) | bank.md Mengen |
| Basiszettel-Rezept, Original-Zettel | 02.–03.10. | hängen an zusammenbau.py (W1 stillgelegt) | bank.md; plan W1 |
| Punkte-Urteile umfang ganz/teil | 28.09. | Punkte nur noch am Prüfstein – Urteil ohne Abnehmer | bank.md Punkte |
| Musterbeispiel (24 muster.md) | 29.09. | ruht; graues a) nach 1.5 kommt nicht aus der Bank | bauregeln 1.5 |
| befunde.md (635 Befunde; Gruppe 1 in 51 Einträgen) | 27.09. | nicht neu gebaut, Bank bis 08.10. geändert; Erkennungsschritt in bank.md weiter geregelt | befunde.md Kopf |
| „Sorte“ = Sprosse | 08.10. | in 4.7 und uebergabe entschieden, in begriffe § 3 „nicht entschieden“ | begriffe § 3 |
| Formelsammlung sichten, DZLM, 182 Kopien, 484 schwache Sprossen | 06.–07.10. | nur in ueberblick § 5, nicht in plan § 6 | ueberblick § 5 |

## 3 Befunde zur Komplexität

**Doppelt.** Leiterregeln fünfmal; Lösungsform in vier Dateien; Prüfkennung im Text (bank.md) gegen Randmarke (6.4), _basis mit dritter Regel; Einstieg/schwach in vier Dateien; Blattsorten in vier Listen; Punkte zweimal verschieden. Vorschlag: Blattregeln aus bank.md nach bauregeln oder streichen; Fassungsgeschichte → archiv; Leiterregeln nur in bank.md und _vorlage.md.

**Brüchige Verweise.** bauregeln.md zweimal umnummeriert (07., 08.10.). bank.md zitiert „5.1 Zahlen wachsen“ (jetzt 4.2/5.2), „4.1–4.3 Herkunft“ (4.9), „8.1 schwach“ (§ 9); ziel.md „2.1 Fokus schmal“ (jetzt drei PDFs); bankblatt.md v5.8 und pruefheft.py Nummern vom 07.10. bzw. archivierte Listen; die Streichliste zeigt bis auf den letzten Absatz auf die Nummern vom 07.10. Vorschlag: Streichliste, Beschluss-Stubs, layout-befunde.md → archiv; Verweise einmal nachziehen; Regeln mit Namen zitieren.

**Niemand liest mehr.** blatt-konzept.md (12.09.: eigener MSA-Prompt, Probeprüfung, Merkmalsfrage) – kein Verweis aus plan, bauregeln, bank.md. konzept.md § 1–3, E1–E10, E38-Blattregel, E40 beschreiben Blattbau vom September („Prompt erfindet Zahlen“); § 7–9, E11–E37 bleiben für die Erfassung nötig. CLAUDE.md gilt nur der Erfassung, wird aber von jedem Agenten zuerst geladen, nennt weder plan.md noch Bank. README-Einstieg listet über 30 Dateien; befunde.md 195 KB, Stand 27.09. Vorschlag: blatt-konzept → archiv; konzept auf Erfassung zurückschneiden, Blatt-Entscheidungen als „ersetzt durch bauregeln“ markieren; CLAUDE.md Kopf mit Verweis auf plan/bauregeln/bank.md; README-Einstieg auf fünf Dateien; befunde.md neu bauen oder archivieren.

**ziel.md.** § 1–4 stecken großteils in plan § 1–2 und bauregeln § 1–2; nur hier stehen Zeitachse, Bestellung (Wiederholung/Ausblick), Prüfungsheft themenweise/prüfungsweise, Profile. Vorschlag: ziel.md in plan.md aufgehen lassen; Bestelloptionen als Schalterliste in bauregeln § 2.

**Begriffe:**
- Kette = Leiter = Verfahrenstyp (bank.md) = Art (bauregeln 4.6) = Zweig (ziel § 1).
- Sprosse = Sorte (begriffe, 4.7) = „Stufe“ in bauregeln 4.2 und bank.md „Kern-Stufe“ – während begriffe Stufe = Handgriff der Gliederung setzt und ziel „Stufe“ als Schulstufe nimmt.
- Handgriff: Prüfungsstufe (begriffe, gliederung), Rechenschritt (bauregeln 8.2, katalog-prompt), Entscheidung beim Erkennungsschritt (bank.md).
- Kern: Gewichtsmarke (Katalog), Kern-Stufe (bank.md), Häufigkeit (3.3), katalog-prompt.md.
- Lerneinheit = Einheit = Unterkapitel = Blatt = Teil; „Abschnitt“ ist in plan ein Handgriff, in bauregeln 4.6 eine Art.
- Typ: Etikett (Katalog) – bank.md „Verfahrenstyp“ = Kette, ziel „Leiter je Aufgabentyp“.
Vorschlag: begriffe.md als einzige Wortliste; bauregeln 4.2 Stufe → Sprosse, 4.6 Art → Kette, 8.2 Handgriff → Schritt; bank.md Kern-Stufe → Grundfall; E38-Blattregel streichen.

**Was ein neuer Agent übersähe:** Felder außerhalb von bank.md (weg.jsonl, _basis, form rechnung/raster); „bild“ leer, obwohl plan § 5 Aufgabenbilder als Sek-II-Frage führt; Prüfkennung im Aufgabentext; `--art schwach`, „Einstieg“, „Option schwach“ sind eine Sache; E38 „Kern vorn“ gegen den Plan; plan § 5/§ 7 datieren „09.10.“, laut Übergabe irrtümlich.

Vermutung ist nur „nicht benutzt“ in § 2 (sympy, Basiszettel, Punkte-Urteile): fehlende Spuren im Repo, kein Beschluss.
