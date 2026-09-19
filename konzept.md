# KONZEPT – Arbeitsblätter aus alten Prüfungen
Stand 19.09.2026 · maßgebliche Grundlage; getroffene Entscheidungen werden ohne neuen Anlass nicht wieder aufgerollt

## 1 Ziel

Ein Nachhilfeschüler wird über Wochen gezielt auf die schriftliche Prüfung P10 Mathematik (Brandenburg, FOR-Niveau = MSA) vorbereitet. Grundlage sind die alten Prüfungen: Sie zeigen, welche Aufgabentypen vorkommen, in welcher Sprache und auf welcher Höhe. Aus ihnen entstehen immer wieder neue, druckfertige Arbeitsblätter zu einzelnen Typen oder Themen. Am Ende kann der Schüler eine vollständige Originalprüfung lösen.

Erfolgskriterium eines Blatts: Der Schüler löst danach Aufgaben dieses Typs auf Prüfungshöhe selbständig, und der Lehrer sieht am Blatt, an welcher Stufe er hängt.

## 2 Bausteine

Hier steht, warum es einen Baustein gibt. Wann man welche Datei öffnet, sagt README.md; Umbenennungen und Daten stehen in § 10 und in namensschema.md.

    Kern (katalog-prompt.md)           eine Erfassungsmethode für alle Prüfungen, damit jede Zeile jeder Prüfung gleich gebaut ist und der Blattbau eine einzige Quelle hat (§ 1)
    Profil (<kennung>.md)              je Prüfung das, was an ihr hängt – Quellen, Aufbau, Kürzel, Themenliste; bei Widerspruch gilt es vor dem Kern (Entscheidung 12)
    Katalog, Typenliste, Prüfungsliste je Profil   Fakten je Teilaufgabe, Typvokabular, Erfassungsstand – je Profil getrennt, weil Vokabular und Häufigkeit nie über Profile hinweg gelten (Entscheidungen 11–15)
    Bau-Skript (<profil>-bau.py)       prüft und schreibt; kein Katalog wird von Hand geschrieben, kein Profil ist ohne Selbstprüfung vollständig (Entscheidung 33)
    abitur-vokabular.md, abitur-typen.csv, abitur-abgleich.py   das Geteilte der Familie abi, weil abi und iqb dieselben Fertigkeiten prüfen (Entscheidungen 25, 26)
    abi-<zielprüfung>-geltung.md       Geltung je Zielprüfung, weil sie am Träger und Niveau hängt, nicht an der Zeile (Entscheidung 30)
    <profil>-vorgaben.md               amtliche Vorgaben mit Jahrescheck, vom Katalog getrennt, weil der ihn nicht liest (Entscheidung 19; abi-vorgaben.md für abi und iqb)
    <profil>-quellen.md                Verzeichnis der Hefte statt einer Ablage der Hefte; iqb erzeugt seine Liste (iqb-quellen.csv, .py), weil 624 Kennungen nicht von Hand zu pflegen sind
    <kennung>-typenbibliothek.md, .py  aus dem Katalog abgeleitet, nie editiert; der Erzeuger hält die Zählweise als Code fest (fhr; msa noch nicht)
    namensschema.md                    eine Benennung, die einen zweiten Träger derselben Prüfungsart verträgt (Entscheidung 32)
    hefte/, hefte-md/, korpus/, baende/, iqb-pdf/   lokal, nicht im Repo: Verlagsmaterial, Korpus, Sammelbände und Cache (.gitignore); pdf/ als Archiv der Hefte ist nicht angelegt (§ 6)
    pruefungsblatt.md, unterrichtsblatt.md, mathblatt.sty, blatt-konzept.md, CHANGELOG.md   der Blattbau, ein eigenes Projekt im selben Repo (blatt-konzept.md § 5); Masterfassungen hier, die Projektanweisungen sind Kopien
    faellig.md                         Handlungen mit Termin oder Auslöser und dem, bei dem sie liegen – getrennt von § 6, weil eine Entscheidung einen Grund des Wartens hat und eine Handlung einen Auslöser; kein Posten in beiden (Pflegeregel CLAUDE.md § 3)
    band-bau.py, <profil>-band-struktur.py, <profil>-band.csv, band-anleitung.md   Sammelband je Prüfungsart aus den Originalseiten mit Register aus dem Katalog, weil eine Katalogzeile ihre Fundstelle (Heft, Seite) nur nennt und der Band sie an einer festen, druckbaren Bandseite aufschlagbar macht; liest Katalog und Hefte, ändert nichts – anderes Projekt wie der Blattbau, Familienname band- (namensschema.md); Ausgabe baende/ lokal
    korpus-bau.py, korpus-protokoll.md   macht die Hefte aller vier Profile durchsuchbar, weil der Katalog keinen Volltext hält (§ 3 dieser Datei, Kern § 3) und die Erfassung selbst nur ein Bruchteil der Hefte je Profil abdeckt; rein maschinell (Text und Ganzseitenrender, kein Modell-Lesen), damit der ganze Bestand in vertretbarer Zeit läuft – anderes Projekt, Familienname korpus- (namensschema.md); liest die Heftordner, ändert nichts; Ausgabe korpus/ lokal
    README.md, CLAUDE.md               Landkarte und Arbeitsanweisung; begründet wird nur hier

Seit dem 19.09.2026 liegen die Dateien in Ordnern: je Profil einer (msa/, fhr/, abitur/ für abi und iqb zusammen), dazu katalog/ (Themenkatalog), quellen/, werkzeuge/ und archiv/; übergreifende Regeln in der Wurzel. Die Dateinamen mit Präfix sind geblieben, damit Querverweise stimmen (Entscheidung 32 gilt für die Namen weiter; die flache Ablage ist aufgehoben, weil sie bei 73 Dateien den Überblick kostete). Die Landkarte ist README.md, sonst nichts. Blattbau (Prompts, Vorlage) liegt im eigenen Repo blattbau.

Ablage: Repo hz-0801/mathe-nachhilfe (bis 2026-09-07 pruefungskatalog; öffentlich, damit curl ohne Anmeldung liest). Die Basis-URL steht an sieben Stellen – in den vier Profilen (§ 2), im Prüfungsblatt-Prompt (2.1, 4.6) und im Unterrichtsblatt-Prompt (4.6) –, die bei anderer Ablage geändert werden. Claude liest per curl und schreibt seit dem 13.09.2026 im Repo, der Lehrer pusht (Entscheidung 22). Geschrieben wird nur beim Aufbau und einmal im Jahr (§ 7).

## 3 Themenkatalog

Der Themenkatalog beschreibt den Stoff, nicht ein Blatt. Je Thema hält er fest, was
dazugehört und in welcher Reihenfolge man es lernt: Lerneinheiten, Voraussetzungen,
Grundvorstellung, typische Fehler, Merkkasten. Er wird einmal recherchiert und belegt
(Rahmenlehrplan, Lehrwerksgliederung, Förderliteratur, Prüfungsoriginale) und ist an
einer Stelle prüfbar und korrigierbar.

Beide Prompts lesen dieselbe Datei und nehmen daraus, was ihnen fehlt:

- Der Unterrichtsblatt-Prompt bekommt die didaktische Struktur, die er sonst in jedem Lauf neu
  erfindet – Stoffauswahl, Reihenfolge, Niveau. Er erfindet dann nur noch Zahlen und
  Kontexte.
- Der Prüfungsblatt-Prompt bekommt die Gliederung in Lerneinheiten, die der Prüfungskatalog
  nicht hat: Er kennt Typen und Originale, aber keine Lernreihenfolge.

Arbeitsteilung mit dem Prüfungskatalog: Der Themenkatalog sagt, **was** gelernt wird,
der Prüfungskatalog **wie hoch**. Die Decke einer Kette kommt immer aus dem
Prüfungskatalog der jeweiligen Prüfungsart; der Themenkatalog setzt keine Decke.

Daraus folgt, dass ein Eintrag prüfungsartübergreifend gilt. Die Lerneinheiten zu einem
Thema sind dieselben, ob der Schüler P10, FHR oder Abitur schreibt – verschieden ist nur
die oberste Sprosse. Ein Thema bekommt deshalb einen Eintrag, nicht einen je Profil.

Offen: Die vorhandenen Sek-I-Einträge führen Sprossen. Gemeint ist die Lernreihenfolge,
nicht die Teilaufgabenfolge eines Hefts – die baut der Prüfungsblatt-Prompt aus den Originalen
(blatt-konzept.md §3). Ob die Trennung in der Praxis hält, entscheidet der erste
Testlauf: Bisher ist kein Blatt aus einem Katalogeintrag gebaut worden.

Die Themenkonkordanz `themen.csv` verbindet die Themennamen der vier Prüfungskataloge
mit den Einträgen des Themenkatalogs. Regel: Ein Sek-I-Thema ist kanonisch, wenn Sek II
denselben Stoff fortführt (Daten, Wahrscheinlichkeit, LGS); ein Sek-II-Thema bleibt
eigen, wenn es ein neues Konzept einführt.

## 4 Entscheidungen

Je Entscheidung stehen seit dem 17.09.2026 (Auftrag D, Teil 5) zwei Zeilen
darunter: **Zahl** – die tragende Zahl mit Fundstelle, oder „keine", wenn die
Entscheidung eine Setzung ist –, und **Kippt bei** – der Befund, bei dem sie
zu überdenken wäre. Die Entscheidungen 27–31 sind dabei aus den Profilen
nachgetragen; sie waren seit dem 14.09.2026 dort festgehalten, hier nicht.

1. Die Einheit ist der Aufgabentyp, nicht die Aufgabe. Ein Typ ist eine Fertigkeit, die man als Einheit übt. Das Original ist Muster und Messlatte.
    Zahl: Vorkommen je Typ – fhr 3,61 (487 Vorkommen über typ und typ_neben auf 135 Typen, fhr.md § 9), Abitur 1,69 Zeilen je Typ (2237 Zeilen auf 1323 Typen, abitur-abgleich.py Lauf 23); im Abitur ist die Einheit für den Blattbau deshalb der Schnittwert (Entscheidung 24), der Typ bleibt Feinetikett.
    Kippt bei: einer Prüfungsart, in der auch der Schnittwert unter etwa 1,5 Zeilen bleibt – dann trägt keine Einheit eine Kette aus mehreren Originalen, und das Blatt müsste vom Thema ausgehen.
2. Auf dem Blatt gibt es drei Sorten Aufgaben: hinführende (leichter, eigene Struktur), die Originalfassung (Struktur und Wortlaut des Originals, neue Werte, leicht umformuliert) und weitere Varianten desselben Typs (gleiche Struktur, anderer Kontext). Struktur ändern nie – dann ist es ein anderer Typ. Auffüllende Aufgaben nach didaktischem Bedarf.
    Zahl: keine – Setzung der Blattform (blatt-konzept.md); bisher kein Blatt aus einer Katalogzeile gebaut (§ 3, Offen).
    Kippt bei: Testblättern, in denen hinführende Aufgaben ohne Katalogzeile nicht baubar sind oder die Originalfassung den Schüler ohne Hinführung überfordert – dann braucht der Katalog Zeilen für hinführende Aufgaben, die er nach Entscheidung 11 nicht hat.
3. Decke ist das Original. Über das Prüfungsniveau geht kein Blatt hinaus.
    Zahl: fhr 29 von 135 Typen ohne Vorkommen ab 2023, darunter beide Fundstellen des Themas Erwartungswert (fhr.md § 9) – deshalb ist die Decke das Original mit den meisten Merkmalen, nicht das jüngste.
    Kippt bei: einem Formatwechsel, der den Bestand entwertet (P10 ab 2028: hilfsmittelfreier Teil, 50 statt 60 BE, msa-vorgaben.md) – dann kommt die Decke aus Musteraufgaben, nicht aus dem Bestand.
4. Progression je Typ: hinführen, Anker, halten – nach dem Muster der Progressionsregeln aus dem Unterrichtsblatt-Prompt (jede Hauptnummer beginnt leicht, endet auf Prüfungshöhe).
    Zahl: keine – übernommen aus dem Unterrichtsblatt-Prompt (Progressionsregeln), ohne Messung.
    Kippt bei: Testblättern, bei denen die Progression je Typ nicht trägt (zu wenige Originale je Typ: fhr 37 von 135 Typen mit genau einem Vorkommen, 49 nie Haupttyp; fhr-typenbibliothek.md).
5. Keine Quellenangabe im Heft, auch nicht im Begleitteil; Herkunft (Jahr, Aufgabe) nur im Protokoll-Archiv (blatt-konzept.md v0.4).
    Zahl: keine – Setzung.
    Kippt bei: dem Wunsch des Lehrers, am Blatt den Rückweg ins Original zu haben; dann genügt das Protokoll-Archiv nicht mehr.
6. Lösungen nach Aufgabensorte: Basis → Ergebnis; Kontext → Ergebnis mit Zwischenergebnissen; Original → knapper Lösungsweg mit Stichwort je Schritt, kein Text. Ergebnisse prüft das Skript, Lösungswege sind ungeprüft und deshalb knapp. Punkte stehen im Katalog (blatt-konzept.md v0.2).
    Zahl: keine – Setzung nach blatt-konzept.md v0.2; Skriptprüfung der Ergebnisse ist im Katalog Regel (Kern § 3 d), Lösungswege bleiben ungeprüft.
    Kippt bei: einer Skriptprüfung, die auch Lösungswege prüft – dann dürfen Lösungswege länger werden.
7. Kein Log je Schüler. Wiederholung steuert der Lehrer; jedes Blatt hat neue Werte, eine ungeplante Wiederholung schadet nicht.
    Zahl: keine – Setzung.
    Kippt bei: mehr als einem Schüler je Prüfungsart oder bei Wiederholungen, die dem Lehrer entgehen.
8. Keine Reserveprüfung. Für den Abschlusstest nimmt der Lehrer die Prüfung, die er am wenigsten verwendet hat.
    Zahl: Bestand je Prüfungsart – msa 12 Hefte (msa-pruefungen.md), fhr 16, abi 16, iqb 37 Stapel; genug, um eines auszusparen, ohne es festzulegen.
    Kippt bei: einer Prüfungsart mit weniger als drei Heften.
9. Häufigkeit ist Auskunft, keine Priorität und kein Filter. Ein einziges Vorkommen ist ein vollwertiger Typ. Der Rahmenlehrplan setzt den Rahmen dessen, was kommen kann; er ist Hintergrund, keine Quelle für Typen.
    Zahl: fhr 37 von 135 Typen genau einmal, 49 mehrfach, 49 nie Haupttyp (fhr-typenbibliothek.md; korrigiert 19.09.2026, vorher stand hier 49 einmal); Abitur 1,69 Zeilen je Typ – die Mehrheit der Typen hätte bei einer Häufigkeitsschwelle keine Zeile.
    Kippt bei: Abgleichläufen, die regelmäßig mehr als ein Zehntel der Einmaltypen zusammenziehen – dann wären Einmaltypen Erfassungsartefakte, keine Fertigkeiten (bisher: Lauf 12 938 → 875 als Umstellung, sonst 0–9 je Lauf, abi-pruefungen.md § 5).
10. Katalog vor Blatt: Alle Hefte werden einmal vollständig erfasst; Blätter entstehen nur aus dem Katalog. Die Hefte selbst holt der Blatt-Prompt nur für Wortlaut oder Bild einer Ankeraufgabe.
    Zahl: Markdown-Prüfung 529 von 529 Teilaufgaben strukturgleich mit dem Katalog, 451 Ergebnisse nachgerechnet, 2 Abweichungen (abi-pruefungen.md § 4, Teil 1 des Auftrags C) – der Katalog trägt alles Strukturelle, das Heft wird nur für Wortlaut und Bild gebraucht.
    Kippt bei: einem Blattbau, der regelmäßig über die Ankeraufgabe hinaus ins Heft muss – dann wäre der Katalog unvollständig, nicht das Blatt falsch.
11. Der Katalog erfasst Fakten, nicht Nutzung: Zeile = kleinste Einheit mit eigener Punktangabe; Fakten getrennt von Deutung; Nachbau-Test als Erfolgskriterium; kein Volltext, sondern Verweis plus Strukturbeschreibung. Spätere Wünsche sind Umsortieren, im Ausnahmefall ein Nachtragslauf für ein Feld, nie ein Neustart.
    Zahl: dieselben 529 von 529 und 2 von 451 (Entscheidung 10); Nachtragsläufe für ein Feld: Lauf 5 (Trägerbindung), 14/15/18/23 (Poolverweise), 20 (Vorrang des Amtlichen), 22 (afb_amtlich) – nie ein Neustart.
    Kippt bei: einem Nachbau-Test, der beim ersten Blattbau an mehr als jeder zehnten Zeile scheitert; dann fehlt ein Feld, nicht eine Zeile.
12. Kern und Profil getrennt. Erstes Profil: msa (P10 Brandenburg, Niveau FOR). Zweites Profil abi (Abitur Brandenburg) folgt nach den MSA-Heften in eigenem Chat; Dateinamen mit Präfix abi-. Weitere Profile erst bei Bedarf; Vokabular und Häufigkeit gelten nie über Profile hinweg.
    Zahl: ergänzt durch Entscheidung 25 – abi und iqb teilen Vokabular und Typenliste (348 von 1323 Typen in beiden Katalogen, Selbstprüfung 17.09.2026); über Prüfungsarten hinweg bleibt es bei getrennten Listen (befund-typenlisten.md § 4: 16 von 26 gemeinsamen Fertigkeiten gleich geschnitten, 8 verschieden).
    Kippt bei: einem Themenkatalog (§ 3), der gleiche Themennamen über alle Prüfungsarten braucht – dann Vorschlag 3 in befund-typenlisten.md § 3; die Typen bleiben auch dann getrennt.
13. Vokabular in drei Ebenen: Leitidee und Thema fest im Profil (aus Rahmenlehrplan, Fachbrief-Inhaltsliste, Lehrwerkgliederung), Typ wächst aus den Heften in msa-typen.csv, Abgleichlauf nach dem letzten Heft. Der Lehrer sieht die fertige Typenliste einmal durch; das ist optional.
    Zahl: Abitur 3 Sachgebiete, 49 Themen, 1323 Typen, 8 Themen mit Gegenstandsklassen (abitur-vokabular.md); Zeilen mit „ersatzweise" 0 in den letzten Stapeln (iqb-pruefungen.md § 2, Schwelle 10 %).
    Kippt bei: mehr als 10 % Zeilen mit „ersatzweise" in einem Lauf – dann passt die Themenliste nicht, nicht die Erfassung (SCHWELLEN in den Bau-Skripten).
14. Zwei Katalogdateien, Basis und Kontext, gleiches Schema; eine Typenliste. Grund, neu gefasst am 17.09.2026 (Auftrag G): Die früheren Kippbedingungen – ein msa-bau.py, msa über Kern v0.3 hinaus – sind eingetreten (msa-bau.py v0.1 seit Auftrag E, Kern v0.9), die Umstellung auf eine Datei wie abi wartet trotzdem: Sie hängt am Umbau von Prüfungsblatt- und Unterrichtsblatt-Prompt (§ 6, Tokenverbrauch). Erst danach steht fest, ob der Prompt je Blatttyp eine Katalogdatei holt (dann tragen zwei Dateien) oder immer beide (dann ist die Trennung nur Aufwand). Solange bleibt es bei zwei Dateien; die Entscheidung bleibt offen, die Zusammenlegung ist nicht ausgeführt.
    Zahl: msa 126 Basis- und 267 Kontextzeilen in zwei Dateien; abi und iqb eine Datei mit Feld block (abi.md § 2: eine zweite Datei legte dieselbe Information zweimal ab).
    Kippt bei: dem Umbau von Prüfungsblatt- und Unterrichtsblatt-Prompt – holt der Prompt danach immer beide Dateien, wird eine Datei wie abi daraus (namensschema.md § 5); holt er je Blatttyp eine, bleiben zwei. Bis dahin keine Änderung.
15. Dateiform CSV mit Semikolon; Durchsicht über eine Prüftabelle im Chat, nicht in der Datei.
    Zahl: 2883 Katalogzeilen in fünf CSV-Dateien ohne Lesefehler; Koordinaten mit Semikolon (fhr.md § 4) sind gequotet unschädlich.
    Kippt bei: Feldinhalten mit Zeilenumbruch oder einem Leser, der nicht CSV-konform trennt.
16. Ergebnisse sind eigene Rechnung, per Skript geprüft; Unsicheres trägt „?". Amtliche Lösungen gibt es im Profil msa nur für die Musteraufgaben 2028; für die FHR-Prüfung enthalten die veröffentlichten Lehrerhefte den Erwartungshorizont (2026-09-07).
    Zahl: Pool und fhr mit amtlichem Erwartungshorizont, jede Abweichung der eigenen Rechnung vermerkt (0 unbestätigte in 37 Stapeln); msa und abi eigene Rechnung – Markdown-Prüfung 2 Abweichungen in 451 nachgerechneten Ergebnissen (0,4 %, beide Rundung oder Wortlaut).
    Kippt bei: einer Fehlerquote eigener Rechnungen über 1 % oder einer amtlichen Quelle für msa – dann gilt dort Kern § 3 d „amtliche Lösung vorhanden".
17. Skizzen werden nicht übernommen, sondern aus dem Feld skizze mit der Vorlage neu gezeichnet; das Original-PDF ist Referenz. Foto und technische Zeichnung: Nachbau mit zeichenbarer Figur, Originalausschnitt nur als Notlösung.
    Zahl: 94 Abbildungen im Markdown-Korpus als Referenz (abi-pruefungen.md § 4); Feld skizze in jeder Zeile mit Material (Kern § 5).
    Kippt bei: einem Blattbau, der aus dem Feld skizze keine zeichenbare Figur baut – dann muss das Feld genauer werden, nicht das Original hinein.
18. Bestand: Oberschulhefte 2014–2026 und Musteraufgaben 2028. Gymnasialhefte nicht (seit 2025/26 keine P10 am Gymnasium).
    Zahl: 12 Hefte, 393 Zeilen, 185 Typen (msa-pruefungen.md, msa-typen.csv); Gymnasium seit 2025/26 ohne P10 (msa-vorgaben.md).
    Kippt bei: einem Gymnasialschüler mit zentraler Klassenarbeit (90 min, 35 BE) – das wäre eine neue Prüfungsart (§ 8), nicht ein Nachtrag.
19. Amtliche Vorgaben (Fachbriefe, Rundschreiben) werden gesondert in msa-vorgaben.md geführt, mit einem jährlichen Check als eigenem Schritt. Der Katalog-Prompt liest sie nicht.
    Zahl: Corona-Ausschlüsse 2021–2023 (msa-vorgaben.md) sind Vorgabe, kein Trend; der Katalog liest sie nicht.
    Kippt bei: Vorgaben, die den Katalog filtern müssen – dann werden sie Geltung (Teil 2 des Auftrags D zeigt den Weg: eine Datei je Zielprüfung, von den Skripten gelesen).
20. Die PDF-Pipeline aus dem Unterrichtsblatt-Prompt (mathblatt.sty, xelatex, Skriptprüfung, Ausgabeblock) bleibt für die Blätter.
    Zahl: keine – Setzung (Blattbau).
    Kippt bei: einem Wechsel der Vorlage oder der Umgebung, die Code ausführt (§ 6, Tokenverbrauch).
21. Versteckte Leistungen in einer Einheit bleiben eine Zeile; alle Leistungen werden in gesucht, ergebnis, format, typ und typ_neben erfasst; Punkte werden nicht geschätzt aufgeteilt.
    Zahl: 2018-bb-ea 22 von 60 Typen nur in typ_neben (abi.md § 7); Punkte nie geteilt, Aufteilung wörtlich in bemerkung.
    Kippt bei: einem Blattbau, der Nebenleistungen als eigene Ankeraufgaben braucht – ein Typ ohne Haupttyp-Vorkommen hat keine Decke; bisher wird die Ankeraufgabe auf die Teilleistung zugeschnitten (abi.md § 7).
22. Arbeitsweise Schritt für Schritt: Claude liefert Dateien mit Pfad und Namen, der Lehrer legt sie ab und meldet sich; dann nennt Claude den nächsten Schritt. Aufwendige Aktionen werden vorher angekündigt.
    Zahl: keine. Seit dem 13.09.2026 (CLAUDE.md) arbeitet Claude im Repo: ein Commit je Heft, Stapel oder Lauf nach bestandener Selbstprüfung, Push beim Lehrer – die Ablage durch den Lehrer entfällt, die Ankündigung aufwendiger Aktionen bleibt.
    Kippt bei: einer Umgebung ohne Repo-Zugriff – dann wieder Dateien mit Pfad und Namen.
23. Eigenes Profil iqb für den Aufgabenpool des IQB (2026-09-13), nach dem Muster von fhr: gleicher Kern, eigenes Profil, eigene Katalogdatei, eigene Typenliste. Grund: Der Pool ist länderneutral und passt nicht in das abi-Kürzel Jahr-Land-Niveau. Der Pool liefert Typen und eicht über den Standardbezug die Schätzung des Anforderungsbereichs (niveau_geschaetzt); die Landeshefte bleiben das Formatmodell. Zusammengeführt wird über die Typen, nicht über die Dateien. Reihenfolge: Prüfungsteil A vollständig, dann Teil B. Einheit des Laufs ist der Stapel (Prüfungsteil eines Pooljahrs auf einem Niveau); die Qualitätsschranke sitzt im Bau-Skript (Schwellenwerte für „?", neue Typen, fehlende Themen), nicht im Urteil des Lehrers, der keine Berichte liest. afb_amtlich trägt alle im Standardbezug vorkommenden Bereiche; die Eichung vergleicht mit dem höchsten.
    Zahl: Poolquote der Landeshefte (BE wortgleich im Pool, abi-pruefungen.md § 2) – GK 2018 22 %, 2019 19 %, 2020 8 %, 2021 20 %, 2022 39 %, 2023 16 %, 2024 35 %, 2025 80 %, 2026 80 %; LK 2022 45 %, 2023 48 %, 2024 61 %, 2025 69 %, 2026 77 %; Eichung über den Poolbestand 1357 von 1442 (94 %); Landesverwendung 344 Dubletten, 24 abgewandelte (Lauf 23).
    Kippt bei: einer Poolquote dauerhaft unter 20 % (die Länder verlassen den Pool) – dann wären die Landeshefte wieder Typenquelle erster Ordnung und der Pool nur Eichmaß.
24. Schnitt für Teil A des Pools: Thema × Gegenstandsklasse × Handlung (2026-09-13). Grund: Der Typ nach Kern § 6 ist für die Kurzaufgaben des Teils A so fein, dass fast jede Zeile ihr eigenes Etikett trägt (1,1 Zeilen je Typ nach sechs Stapeln, Wiederverwendung im Niveau 3–7 %); das Thema allein wirft Ungleiches zusammen (Matrizen: Verflechtung, Übergangsprozesse, Matrizenalgebra). Die Zwischenstufe – so hieß der Schnitt in der Messung vom 13.09.2026 – trennt diese Fälle (Messung 13.09.2026: 114 Werte auf 197 Zeilen, Wiederverwendung im Niveau 38–47 %) und bündelt, was als Kette taugt. Umsetzung ohne neues Feld: Die Gegenstandsklasse steht als Präfix vor dem Doppelpunkt im Typnamen, die Klassenliste je Thema in iqb.md § 6; Themen, die selbst der Gegenstand sind, führen keine Klasse; die Handlung kommt aus format. Der Typ nach Kern § 6 bleibt als Feinetikett hinter dem Präfix; Umbenennungen und Zusammenziehungen laufen über iqb-abgleich.py (Kern § 9). Der Kern bleibt unverändert; für den Blattbau in Teil A zählt der Schnitt, nicht das Feinetikett.
    Zahl: 1,73 Zeilen je Schnittwert gegen 1,08 je Typ (Bestand 197 Zeilen, iqb-pruefungen.md § 4 „Zwischenstufe durchgerechnet"; grober Schnitt Thema × Handlung 2,37); Wiederverwendung im Niveau 38–47 % gegen 3–7 %; heute je Teil-B-Stapel 20–53 Werte, in den ersten beiden Stapeln 68–71 % der Zeilen auf bekannten Werten, seitdem 81–98 % (iqb-pruefungen.md § 2).
    Kippt bei: einem Bestand, in dem der Schnittwert selbst auf unter 1,3 Zeilen fällt, oder Testblättern, die das Feinetikett als Kette brauchen.
25. Gemeinsame Typenliste für abi und iqb, abi auf dem Schnitt nach Entscheidung 24 (2026-09-15). Grund: Die Messung (befund-abi-iqb-typen.md) zeigte, dass 92 % der abi-Zeilen auf Schnittwerten liegen, die der Pool schon hat, und 36 % der abi-Typen ein inhaltsgleiches iqb-Gegenstück haben; die Landeshefte ab 2019 (Stark-Scans) nehmen Poolaufgaben auf. Umsetzung: abitur-vokabular.md als eine Quelle für Sachgebiete, Themenliste, Geltungstabelle, Gegenstandsklassen und Handlungen (abi.md und iqb.md verweisen darauf und führen nur Profilspezifisches); abitur-typen.csv als gemeinsame Typenliste mit beispiel_id in einem der beiden Kataloge; die Kataloge bleiben getrennt (abi-katalog.csv, iqb-katalog.csv); abitur-abgleich.py zieht beide Kataloge mit; abi-bau.py auf dem Stand von iqb-bau.py (Präfixregel, Schwellen, Eichung, Vollständigkeit). Pool-Teilaufgaben in Landesheften bekommen eine eigene abi-Zeile mit geteiltem Typ und dem Verweis „Dublette von: <iqb-id>" in bemerkung – kein bloßer Verweis ohne Zeile, kein neues Feld im Kern. Umstellungslauf 12: 938 → 875 Typen, 75 abi-Zeilen und 5 iqb-Zeilen umetikettiert (abi-pruefungen.md § 4). Der Kern bleibt unverändert; seine Sätze „Leitidee und Thema stehen im Profil" gelten über den Verweis des Profils.
    Zahl: 92 % der abi-Zeilen auf Pool-Schnittwerten, 36 % der abi-Typen mit iqb-Gegenstück (befund-abi-iqb-typen.md, 15.09.2026); heute 348 von 1323 Typen in beiden Katalogen, 344 Landeszeilen mit „Dublette von:" (Selbstprüfung und Lauf 23, 17.09.2026).
    Kippt bei: einem Anteil geteilter Typen unter 10 % (Landeshefte ohne Poolanteil) – dann wäre die Liste zwei Listen in einer.
26. Zeilenthema = Typthema für abi und iqb, Schnitt über das Thema des Typs (2026-09-16). Grund: 21 Zeilen (13 abi, 8 iqb) trugen ein anderes Thema als ihr Typ; der Schnitt des Gesamtbestands hing damit von der gezählten Spalte ab (189 gegen 183 Werte) – sechs Werte Unterschied bei einem Abbruchkriterium, dessen Schwelle bei fünf liegt. Tragen Zeile und Typ verschiedene Themen, ist eines von beiden falsch; der Schnittwert ist dann nicht definiert. Umsetzung: Lauf 13 von abitur-abgleich.py löst die 21 Fälle auf (18 Zeilen folgen dem Typ, drei Typen wechseln das Thema, ihre Zeilen folgen), beide Bau-Skripte erzwingen die Gleichheit für neue Zeilen und im Bestand, abitur-abgleich.py prüft sie nach jedem Lauf; die Regel steht in abitur-vokabular.md § 4. Die Teil-B-Reihen (grundlegend 7/3/2/2, erhöht 9/0/7/4/3) sind nachgerechnet und unverändert, keine Abbruchentscheidung kippt. Kern v0.4 zieht nur Text nach (Vokabulardatei vorgesehen, Etikettenänderungen im Abgleichlauf, Handlung je format in § 5, Markierungen in bemerkung); msa und fhr bleiben unberührt, fhr behält seine Regel Punkt-Schwerpunkt (fhr.md § 6). Fortgeschrieben am 17.09.2026 (Auftrag G): Der Kern v0.9 setzt Zeilenthema = Typthema als Regel mit Vorbehalt für das Profil (§ 6); msa behält die eigene Regel „Thema der Aufgabenstellung" (msa.md § 6) – entschieden, nicht offen. Die Zeile trägt dort das Thema, unter dem die Aufgabe im Heft steht, der Typ das seiner ersten Fundstelle; ein Blatt für ein msa-Thema findet seine Zeilen über das Zeilenthema.
    Zahl: 21 Zeilen (13 abi, 8 iqb) mit anderem Thema als ihr Typ; Schnitt 189 gegen 183 Werte je nach Spalte – Differenz 6 bei einer Abbruchschwelle von 5 (abi-pruefungen.md § 4, Lauf 13). msa: 42 von 393 Zeilen weichen vom Typthema ab (17.09.2026).
    Kippt bei: Zeilen, die zwei Themen gleichwertig tragen, häufiger als die „ersatzweise"-Schwelle (10 %); bisher 0 seit Lauf 13, weil beide Skripte die Gleichheit erzwingen. Für die msa-Regel: ein Leser, der das Zeilenthema profilübergreifend auswertet – dann müsste msa der Kernregel folgen.
27. MMS/CAS als Delta zum WTR-Zweig (2026-09-15, iqb.md § 7; für abi: abi.md § 3, CAS und MMS sind dieselbe Sache unter wechselndem Namen). Die Fassung ohne MMS ist der Hauptzweig; ein MMS-Stapel erfasst nur die nicht wortgleichen Dateien und zählt nicht in die Abbruchreihe.
    Zahl: Delta-Messung 2026-ga-B-mms 1 neuer Schnittwert in der Geltung, 2026-ea-B-mms 0, 2025-ea-B-mms 0 (iqb.md § 6, iqb-pruefungen.md § 4); 69 % der MMS-Zeilen auf Schnittwerten der WTR-Fassung, 3 von 7 Dateien wortgleich (iqb.md § 7).
    Kippt bei: einem MMS-Stapel mit fünf oder mehr neuen Schnittwerten in der Geltung – dann wäre MMS ein eigener Zweig, kein Delta.
28. Abbruchkriterium der Erfassung (2026-09-14, iqb.md § 6): je Stapel die Zahl neuer Schnittwerte innerhalb der Geltung; unter fünf heißt ausgereizt, der Rest ist Reserve. Reserve-Stapel werden nur für Landesheftverweise geöffnet (Entscheidung 29).
    Zahl: Teil A ausgereizt nach 18 Stapeln; Teil B grundlegend 7 → 3 → 2 → 2, erhöht 9 → 0 → 7 → 4 → 3 (iqb.md § 6); die für Landesheftverweise geöffneten Reserve-Stapel brachten 0, 1, 0, 1 neue Werte (2020-ga-B, 2021-ga-B, 2025-ea-B-mms, 2019-ga-B; iqb-pruefungen.md § 4).
    Kippt bei: einem Reserve-Stapel mit fünf oder mehr neuen Werten – dann war die Reihe nicht ausgereizt und die Reserve ist zu öffnen; ebenso bei einer neuen Zielprüfung (§ 9), gegen die die Reihe neu zu rechnen ist.
29. Vormerkung als Übergangszustand und Reserve für Landesheftverweise (2026-09-16, abi.md § 7, iqb.md § 7): Eine Poolaufgabe aus einem nicht erfassten Stapel wird im Landesheft als „Poolaufgabe (nicht erfasst): <id>" vorgemerkt, der Stapel darf dafür erfasst werden, ohne dass das Abbruchkriterium fällt, und ein Abgleichlauf stellt den Vermerk auf „Dublette von:" oder „Abgewandelt von:" um. Seit dem 17.09.2026 (Auftrag D, Teil 7) als Regel: eine Vormerkung überlebt keinen Auftrag – der Reserve-Stapel wird im selben Auftrag erfasst, der anschließende Abgleichlauf stellt um (abi.md § 7, iqb.md § 7, CLAUDE.md § 2).
    Zahl: 35 Vormerkungen aus fünf Heften (Auftrag B), alle in Auftrag C aufgelöst – vier Reserve-Stapel, 23 Dubletten, 12 abgewandelte (abi-pruefungen.md § 4, Lauf 23); Landesverwendung insgesamt 344 Dubletten, 24 abgewandelte.
    Kippt bei: einem Landesheft mit Poolanteil aus einem Stapel, der nicht erfasst werden darf oder kann – dann bliebe die Vormerkung dauerhaft, und der Verweis bräuchte eine dritte Form.
30. Geltung je Zielprüfung (2026-09-16 Geltung je Heft, gemeinsame Hefte bebb gegen beide Spalten; 2026-09-17 eine Datei je Zielprüfung, Auftrag D Teil 2): Geltung ist eine Eigenschaft des Themas, nicht der Zeile; das Profil nennt seine Zielprüfungen, die Bau-Skripte lesen die Dateien und zählen die Zeilen außerhalb.
    Zahl: außerhalb der Geltung im Bestand – abi be-gk 101, be-lk 5, bb-gk 96, bb-ea 0 von 794 Zeilen; iqb be-gk 316, be-lk 168, bb-gk 314, bb-ea 166 von 1443 (Selbstprüfung 17.09.2026); die Spalten je Niveau unterscheiden sich nur bei der hypergeometrischen Verteilung.
    Kippt bei: Prüfungsschwerpunkten, die ein stark belegtes Thema (mehr als ein Zehntel der Zeilen) für ein Land streichen, oder bei einer Simulation, die einen Prüfungsteil braucht, den es in der Zielprüfung nicht mehr gibt – dann reicht die thematische Geltung nicht, und die strukturelle Geltung (abitur-vokabular.md § 3, Vorschlag; nicht entschieden) wird nötig.
31. Vorrang des Amtlichen und Maßstab der Schätzung (2026-09-17, Kern § 5 v0.6 und v0.7): Die eigene Schätzung wird nicht an den amtlichen Bereich angepasst; eine übernommene Schätzung und eine wortgleiche Dublette folgen ihm. Die Eichung ist in jedem Profil Kennzahl, Schranke (85 %) nur für Poolstapel; bei Landesheften ist sie ausgesetzt.
    Zahl: Landesschätzungen mit amtlichem Bereich 22 von 41 (54 %) gegen 94 % im Pool (abi-pruefungen.md § 4, Lauf 20; abi.md § 7); heute Pool 1357 von 1442 (94 %), Landeshefte 323 von 344 (93 %, geerbt) bei 450 Zeilen ohne Maßstab.
    Kippt bei: einer Pool-Eichung unter 85 % über den Bestand (dann ist die Schätzregel des Kerns nachzujustieren) oder einer Landes-Eichung, die bei mindestens 100 eigenen Zeilen mit Maßstab 85 % erreicht (dann kann die Schranke für abi zurück).
32. Dateibenennung (2026-09-17, Auftrag F; namensschema.md § 2–4): Variante B. Die Kurzkennungen msa, fhr, abi, iqb bleiben als Aliasse der Vollform – msa = msa-bb, fhr = fhr-bb, abi = abi-bebb, iqb = abi-iqb –, und der Familienname abitur- steht für die Familie abi (abitur-typen.csv, abitur-vokabular.md, abitur-abgleich.py). Jedes Profil trägt sein Präfix (msa seit dem 17.09.2026: msa-typen.csv, msa-katalog-basis.csv, msa-katalog-kontext.csv, msa-pruefungen.md, msa-vorgaben.md; git mv, Inhalt unverändert), Befunde tragen befund- (befund-abi-iqb-typen.md, befund-repo-bestand.md). Neue Dateien und neue Profile tragen die Vollform nach namensschema.md § 2 (abi-ni.md, abi-ni-ga-geltung.md); die bestehenden Aliasse werden dafür nicht nachträglich umbenannt. Variante A (Vollform durchgängig) ist aufgeschoben, nicht verworfen.
    Zahl: Variante B rund 145 Verweise (nachgezogen am 17.09.2026: 149 in 21 Dateien, keine Katalogzeile), Variante A rund 1 200 (namensschema.md § 4; 18 davon in Katalogzeilen, nur per Abgleichlauf änderbar).
    Kippt bei: einem zweiten Träger zu einer bestehenden Prüfungsart (abi-ni neben abi-bebb) oder einer zweiten Schulform (msa-bb-gym neben msa-bb-os) – dann ist der Alias mehrdeutig (namensschema.md § 3 (4)) und Variante A neu zu prüfen, mit dem dann größeren Bestand.
33. Selbstprüfung als Bedingung eines vollständigen Profils (2026-09-17, Auftrag F; Kern § 7, CLAUDE.md § 3): Ein Profil gilt als unvollständig, solange sein Bau-Skript keine Selbstprüfung bei leerer Zeilenliste kennt – den Lauf, der den ganzen Bestand nach Kern § 5 und § 7 prüft und nichts schreibt. Befund dahinter: msa hatte bis zum 17.09.2026 kein Bau-Skript (Erfassung im Chat unter Kern v0.3), fhr-bau.py bis v0.2 keine Selbstprüfung; 646 Katalogzeilen (msa 393, fhr 253) waren nie maschinell gegen Kern und Profil geprüft. Nachgerüstet in Auftrag E, Punkt 6 (msa-bau.py v0.1, fhr-bau.py v0.3); beide Bestände bestanden auf Anhieb – die Regel sichert nicht einen gefundenen Fehler, sondern dass ein Bestand überhaupt prüfbar ist.
    Zahl: 646 von 2883 Katalogzeilen (22 %) bis zum 17.09.2026 ohne maschinelle Prüfung, danach 0 Fehler (Auftrag E, Punkt 6); heute vier Bau-Skripte mit Selbstprüfung über 2883 Zeilen.
    Kippt bei: keinem Befund – Setzung; zu überdenken nur, wenn ein Bestand ohne Skript entsteht (Erfassung im Chat wie msa bis 2026-09-05) und das Nachrüsten mehr kostet als ein Neubau.
34. Keine Sortierung der Typenlisten (2026-09-17; Vorschlag 5 aus befund-typenlisten.md § 3, abgelehnt): fhr-typen.csv und abitur-typen.csv bleiben in Anlagereihenfolge – neue Typen werden angehängt, Abgleichläufe schreiben die Reihenfolge unverändert zurück; nur msa-typen.csv ist nach Leitidee, Thema, Typ sortiert (Typen-Check 05.09.2026, vor den Skripten). Grund: Ein Sortierlauf kostet die byteidentischen Reruns aus dem HEAD-Stand, derzeit das stärkste Prüfmittel – nach einer Sortierung ist kein früherer Heft-, Stapel- oder Abgleichlauf mehr gegen den heutigen Stand byteidentisch wiederholbar, und der Sortierlauf selbst hätte einen unlesbaren Diff. Der Nutzen (Diff-Lesbarkeit, gleiche Themen beieinander) wiegt das nicht auf.
    Zahl: 1458 Typenzeilen (fhr 135, abitur 1323), die nur ihre Reihenfolge änderten; 23 Abgleichläufe und alle Heft- und Stapelläufe, deren Rerun die Reihenfolge voraussetzt (befund-typenlisten.md § 3).
    Kippt bei: einem Prüfmittel, das die byteidentischen Reruns ersetzt (etwa ein Vergleich auf Zeilenmengen statt Bytes), oder wenn der Lehrer die Reihenfolge zum Lesen braucht – dann ein eigener Sortierlauf mit neuem Rerun-Anker.
35. IQB-Geltung (2026-09-19, Übergabe 19b Punkt 3): Der IQB-Pool ist für das Profil abi voll maßgeblich, für fhr nicht. Grund abi: Auf Grundlage von KMK-Beschlüssen werden auf Basis der Bildungsstandards für die Allgemeine Hochschulreife ländergemeinsame Abituraufgabenpools entwickelt, koordiniert vom IQB, für Mathematik seit Prüfungsjahr 2017; Brandenburg entnimmt seit 2017 dem Pool Aufgaben für die landeseigene Abiturprüfung, ausgewählt passend zu den in Berlin und Brandenburg eingeführten Aufgabenformaten und Prüfungsschwerpunkten, und der Pool wirkt normierend auf landeseigene Prüfungsaufgaben und Oberstufenklausuren (Fachbrief Mathematik Brandenburg Nr. 3). Seit der KMK-Ländervereinbarung vom 15.10.2020 verändern die Länder entnommene Poolaufgaben nicht mehr, sondern vereinheitlichen nur Struktur, Hilfsmittel und Bewertung; die Auswahl-Einschränkung bilden allein die Geltungsdateien abi-*-geltung.md ab. Grund fhr: Die FOSFHRV Brandenburg bindet die Prüfungsanforderungen an die vom Ministerium genehmigten curricularen Vorgaben, das ist der RLP FOS 2019; die zentralen FHR-Prüfungen laufen seit 2010/11 landeseigen, einen IQB-Pool für die FHR gibt es nicht, und der RLP FOS nennt die Bildungsstandards für die Allgemeine Hochschulreife (KMK 18.10.2012) nur als Bezugspunkt. fhr-Einträge stützen sich deshalb auf RLP FOS 2019 und den fhr-Katalog; IQB-Dokumente sind dort keine Vorgabe.
    Zahl: keine – gestützt auf amtliche Quellen (IQB-Abituraufgabenpools, Fachbrief Mathematik Brandenburg Nr. 3, FOSFHRV Brandenburg), keine Messung.
    Kippt bei: einer Änderung des Poolverfahrens durch die KMK, einer Änderung der Entnahmepraxis durch Brandenburg oder einer FHR-Vorgabe, die einen IQB-Bezug einführt.
36. Sek-II-Eintragsform (2026-09-19): Sek-II-Einträge übernehmen den Sek-I-Aufbau aus katalog/_quellen.md mit drei Anpassungen. (1) Prüfungsform: statt P10-Typen die Typen aus den Rohdateien, je Profil getrennt (fhr, abi, iqb), mit der Geltung aus Entscheidung 35; der Eintrag setzt weiterhin keine Decke. (2) Das Feld „Für schwache Schüler" bleibt: Mindeststoff aus dem GK-Kernbereich je Kurshalbjahr (Q-Phase), der Niveaustufe H (E-Phase) bzw. dem RLP FOS (fhr); die Grundvorstellungs-Prüfung für Blatt 0 aus den Eingangsvoraussetzungen je Leitidee des RLP GOST Teil C Kap. 3.1; die Sprossen je Verfahrenstyp aus Lehrwerksgliederung und Rohdatei. (3) Quellenfolge: RLP GOST BB/BE 2022 samt Anlage ohne Hilfsmittel, RLP FOS 2019, Lehrwerksgliederung LS-AA (Einführungs- und Qualifikationsphase), abitur-vokabular.md für die Namen, die Rohdatei als Prüfungsbeleg; IQB-Begleitdokumente nur, wo abi/iqb betroffen ist. Drei neue Förderquellen: MaCo (DZLM, Förderbausteine, auch für die Sek-I-Pflege), BASICS (Springer 2020, Diagnose- und Förderstruktur am Übergang in die Oberstufe; nur Struktur, inhaltlich immer gegen die Eingangsvoraussetzungen des RLP GOST prüfen), COSH (Mindestanforderungskatalog Schule-Hochschule als Mindeststoff-Referenz für fhr, nachrangig für abi). Rangfolge der Absicherung: amtlich vor breit erprobt (MSK, MaCo) vor einzelerprobt (BASICS) vor Ermessen; jede Ermessensstelle wird als solche gekennzeichnet. MSK bleibt Primärquelle, wo es Bausteine hat; MaCo füllt geprüft dessen Lücken; wo beides fehlt, bleibt die Kennzeichnung „eigene Formulierung nach RLP und P10/Rohdatei". Straffung (2026-09-19): Die Prüfungsform enthält keinen eigenen Zuordnungs-Absatz; die Profillisten tragen je Typ die Einheitsnummer mit in der Klammer hinter der Zeilenzahl, Form „(17, E2)"„ (bei Typen unter einem „je 1:"-Präfix nur „(Ek)", weil die Zeilenzahl im Präfix steht)" – die Zuordnung steht damit genau zweimal im Eintrag: unter „Typen je Lerneinheit" und in den Profillisten. Grund: Der Pilot nannte jeden Typnamen dreimal.
    Zahl: keine – Strukturentscheidung.
    Kippt bei: der erste Testlauf zeigt, dass die Prompts die Felder nicht wie vorgesehen nutzen können, oder die MaCo-Lizenz lässt keine Übernahme zu (dann nur Strukturübernahme wie bei MSK).

## 5 Verworfen

- Häufigkeitsschwelle und „Kerntypen": schließt aus, was die Prüfung trotzdem bringen kann.
- Reserveprüfung: Wiedererkennung bei neuen Werten klein, Bestand endlich.
- Log je Schüler: Schreibaufwand bei jeder Sitzung, Nutzen gering.
- Live-Analyse der Hefte je Blatt: langsam, teuer, jedes Mal anders kategorisiert.
- Virtuelle Unterzeilen mit geschätzten Punkten: Deutung im Faktenfeld.
- Volltext im Katalog: Kopie aller Hefte, sprengt Kontext und Projekt.
- Markdown-Tabelle als Katalog: bei 37 Feldern nicht lesbar.
- Ein Prompt für alle Prüfungen ohne Profil: verliert die konkreten Regeln, die Zeilen gut machen.
- Google Drive als Ablage: möglich, aber Dateien laufen bei jeder Sitzung durch den Kontext; Aktualisieren über den Konnektor ungetestet. Bleibt Alternative, falls das Hochladen zu lästig wird.

## 6 Offen

Stand 17.09.2026. Je Punkt: was offen ist und worauf es wartet. Was hier
steht, steht nur hier; die Profile wiederholen es nicht.

- **Variante A des Namensschemas** (Vollform durchgängig, namensschema.md § 4;
  Entscheidung 32): aufgeschoben – wartet auf einen zweiten Träger zu einer
  bestehenden Prüfungsart oder eine zweite Schulform; erst dann wird der
  Alias mehrdeutig.
- **Entscheidung 14, msa-Katalogdateien** (Basis und Kontext getrennt):
  Zusammenlegung zu einer Datei wie abi – wartet auf den Umbau von Prüfungs-
  und Unterrichtsblatt-Prompt; erst danach steht fest, ob der Prompt je Blatttyp eine
  Katalogdatei holt oder immer beide.
- **Vorschlag 1 aus befund-typenlisten.md § 3, Statuswerte** (ein Vokabular
  für das Feld status, „gültig" entfällt): nur mit einer Leseregel im Kern,
  die sagt, wer den Wert setzt und liest – sonst wäre das Feld zu streichen;
  nicht entschieden.
- **Vorschlag 2, Verb am Ende** (25 verblose Typnamen, msa 5 und fhr 20): Kern
  § 6 ist berichtigt (alle Beispiele tragen eine Handlung, Auftrag E); die
  Umbenennung der 25 Typen samt 129 Katalogzeilen ist nicht entschieden.
- **Vorschlag 3, Themennamen** (gleiche Sache, gleicher Themenname über die
  Profile): wartet auf den prüfungsartübergreifenden Themenkatalog (§ 3), der
  nicht beschlossen ist – ohne ihn gibt es keinen Nutzen, der die 151
  betroffenen Katalogzeilen rechtfertigt.
- **Abbruchkriterium abi** (Gegenstück zum Stapelkriterium in iqb.md § 6 für
  Landeshefte): unverändert offen, seit Auftrag D nicht entschieden.
- **Strukturelle Geltung** (abitur-vokabular.md § 3, Vorschlag nach
  Jahrgangsklassen; Entscheidung 30 nennt sie als Kippbedingung): unverändert
  offen, nicht entschieden.
- **Nachbau-Test je Blatt nie ausprobiert**: bisher kein Blatt aus einer
  Katalogzeile gebaut (Entscheidungen 2, 10, 11; Prüfungsblatt-Prompt v0.15 liegt
  vor) – gehört ins Blattbau-Projekt.
- **Prüfungsjahr des Schülers**: Annahme 2027 (aktuelles Format). Bei 2028
  rücken hilfsmittelfreier Teil und Musteraufgaben nach vorn (msa-vorgaben.md).
- **PDF-Archiv** (pdf/, § 2): nicht angelegt; die Hefte werden je Lauf vom
  Bildungsserver geholt, abi ab 2019 aus hefte/ (lokal).
- **Profil abi: Schülerart am Oberstufenzentrum** klären (berufliches
  Gymnasium oder Fachoberschule); unverändert offen.
- **Ablageort**: Repo hz-0801/mathe-nachhilfe mit Basis-URL in den vier
  Profilen (§ 2); vom Lehrer nicht ausdrücklich bestätigt, seit dem 07.09.2026
  in Gebrauch.
- **Tokenverbrauch und Plattformunabhängigkeit** (festgehalten 17.09.2026):
  Der größte Einzelposten im laufenden Betrieb ist nicht der Katalog, sondern
  der Unterrichtsblatt-Prompt (rund 25.000 Zeichen, je Blatt vollständig gelesen) und
  das Ansehen gerenderter Seiten. Ein Umbau, der Nachschlagbares aus dem
  Prompt in Dateien auslagert, würde Token sparen und den Prompt weniger
  modellgebunden machen; die Formate des Katalogs sind bereits
  anbieterneutral, die Bindung liegt im Prompt und in der Umgebung, die Code
  ausführt. Gehört ins Blattbau-Projekt; Entscheidung 14 wartet darauf.

## 7 Jahresroutine – ein neuer Jahrgang im bestehenden Profil

Stand 17.09.2026, abgeleitet aus dem, was in den vier Prüfungslisten je Heft
und Stapel tatsächlich geschehen ist (abi-pruefungen.md § 5, iqb-pruefungen.md
§ 5, msa-pruefungen.md § 3, fhr-pruefungen.md Änderungslog) und aus den
Jahreschecks in `<profil>-vorgaben.md` § 4. Regeln stehen in CLAUDE.md, im
Kern und im Profil; hier steht nur die Reihenfolge.

**Reihenfolge und warum.** Zuerst der Vorgabencheck, dann die Erfassung:
Geänderte Prüfungsschwerpunkte ändern die Geltung (abi/iqb: die
Geltungsdateien, fhr: die Markierung der Themenliste), und gegen die Geltung
zählt das Abbruchkriterium (iqb.md § 6) – ein Stapel, der vor dem Check
erfasst wird, wird gegen die alte Geltung gemessen. Ein Formatwechsel ändert
außerdem KONFIG, Kürzel und Felder, bevor eine Zeile geschrieben wird.

**Je Profil, in dieser Reihenfolge:**

1. **Vorgabencheck** nach `<profil>-vorgaben.md` § 4 – msa: Fachbrief und
   Rundschreiben (msa-vorgaben.md); fhr: Prüfungsschwerpunkte des neuen
   Schuljahrs und Rundschreiben (fhr-vorgaben.md; beim ersten Check zuerst
   Schritt 0 dort, der den Vorbehalt im Kopf auflöst); abi und iqb:
   Prüfungsschwerpunkte beider Länder und beider Niveaus, Rundschreiben
   (abi-vorgaben.md). Ergebnis: eine Zeile in § 2 der Vorgaben-Datei mit den
   Änderungen gegen das Vorjahr; Themenliste nur über den Bericht ändern.
2. **Quelle beschaffen und eintragen** – msa und fhr: Heft vom Bildungsserver
   mit curl (Adresse in msa-pruefungen.md § 1 bzw. fhr-pruefungen.md,
   Quelle), Dateiname, Seiten und Status „nicht erfasst" in die Heftliste;
   abi: Landeshefte ab 2019 sind nicht veröffentlicht – Verlagsband des
   Jahrgangs (abi-quellen.md § 5, Beschaffungstabelle), Scan unter hefte/,
   Zeile in abi-quellen.md § 8 (Jahr, Land, Niveau, Rechnerfassung, Seiten,
   Textebene), papier-Kürzel nach abi.md § 4, Zeile in abi-pruefungen.md § 2;
   iqb: `python iqb-quellen.py` erneuert iqb-quellen.csv aus der
   IQB-Übersicht und dem Scan der neuen Dateien (Kennungen dürfen nur
   hinzukommen), die neuen Stapel in iqb-pruefungen.md § 2 eintragen.
3. **KONFIG des Bau-Skripts** – msa, fhr, abi: jahr, papier, datei, seiten,
   soll je Aufgabe aus den BE-Tabellen des Hefts (abi: soll_teil1 nur bei
   bb-ea); iqb: stapel und soll je Kennung aus der BE-Summe. Zuerst eine
   Feldprobe (probe: True bei abi und iqb), die nichts schreibt.
4. **Lauf** – ein Heft oder ein Stapel je Lauf, vollständig: Text
   extrahieren, jede Aufgabenseite rendern, ZEILEN und NEUE_TYPEN füllen,
   jedes Ergebnis per Skript nachrechnen, dann `python <profil>-bau.py`; bei
   einem Fehler wird nichts geschrieben. abi: vor dem Bau die Aufgaben gegen
   den Pool halten („Dublette von:" mit dem Typ der Poolzeile; Vormerkung
   nur, wenn der Stapel noch fehlt – dann den Stapel im selben Auftrag
   erfassen, Entscheidung 29).
5. **Abgleichlauf** – abi und iqb nach jedem Heft und Stapel über
   abitur-abgleich.py (Lauf N, Kern § 9), Liste alt → neu in § 5 der
   Prüfungsliste; msa und fhr nach dem letzten Heft des Jahrgangs als
   Typen-Check über den Bestand (msa 05.09.2026, fhr 12.09.2026), über ein
   Skript, das Typenliste und Katalog zugleich umstellt – für beide liegt
   keines im Repo; Feldkorrekturen an msa-typen.csv laufen über
   TYPEN_KORREKTUR in msa-bau.py.
6. **Selbstprüfung und Rerun** – alle betroffenen Bau-Skripte mit leerem
   ZEILEN (nach einem Abgleichlauf beide Skripte der Familie abi); dann den
   Lauf aus dem HEAD-Stand in einer frischen Kopie wiederholen, byteidentisch
   (Heftlauf, Stapellauf, Abgleichlauf – Entscheidung 34).
7. **Commit** – einer je Heft, Stapel oder Abgleichlauf, erst nach 6; Push
   beim Lehrer.
8. **Prüfungsliste fortschreiben** – Status „erfasst JJJJ-MM-TT, n Zeilen",
   Kennzahlen in § 2 (abi: Poolquote, Geltung, Zeilen ohne Maßstab; iqb:
   Eichung, neue Schnittwerte in der Geltung, Landesverwendung), Befunde in
   § 4, Logzeile in § 5; im Profil Themenlücken und Versionszeile, bei abi/iqb
   Änderungen an Themen oder Klassen nur in abitur-vokabular.md.
9. **Typenbibliothek neu ableiten**, wo es eine gibt: fhr
   `python fhr-typenbibliothek.py` nach jeder Katalogänderung; msa, abi und
   iqb haben keine (§ 2).
10. **Band neu bauen**, wo es einen gibt (fhr seit 18.09.2026): Strukturliste
    erzeugen, dann `band-bau.py <profil>` – erst erfassen, dann bauen
    (band-anleitung.md, Regel in § 6 dort).

**Nur abi und iqb.**

- **Geltungsdateien gegen die neuen Prüfungsschwerpunkte:** je Zielprüfung
  `abi-<zielprüfung>-geltung.md` § 1 Thema ja/nein, § 2 ausgeschlossene
  Aufgabenformen, § 3 Rechnerfassung nachziehen. Nennen die Schwerpunkte ein
  Thema, das die Liste nicht hat, kommt es in abitur-vokabular.md § 2 und in
  jede Geltungsdatei (die Bau-Skripte verlangen Vollständigkeit, § 9 Punkt 2).
  Eine neue Zielprüfung ist § 9, kein Jahrgang.
- **Abbruchreihe gegen die Zielprüfung nachrechnen:** das Kriterium (iqb.md
  § 6, unter fünf neue Schnittwerte in der Geltung je Stapel) zählt gegen die
  Geltung; hat der Check sie geändert, ist die Reihe je Niveau neu zu
  rechnen, bevor Reserve-Stapel geschlossen bleiben (§ 9 Punkt 3,
  Entscheidung 28).
- **Neuer Pooljahrgang:** nach iqb-quellen.py je Niveau die Stapel Teil A
  (grundlegend vor erhöht) und Teil B WTR erfassen; MMS-Stapel sind Delta und
  werden je Niveau an einem Stapel gemessen (Entscheidung 27). Erst die
  Poolstapel des Jahrgangs, dann die Landeshefte: Die fünf Hefte des
  Auftrags B kamen vor ihren Stapeln und hinterließen 35 Vormerkungen, die
  Auftrag C mit vier Reserve-Stapeln und Abgleichlauf 23 schließen musste
  (Entscheidung 29).

**Sonderfälle je Profil.**

- fhr: der erste Jahrescheck prüft zuerst die Herkunft der Angaben in
  fhr-vorgaben.md (Schritt 0 dort) und streicht dann den Vorbehalt.
- msa: die Musteraufgaben 2028 FOR sind nicht erfasst (msa-pruefungen.md § 2);
  sie tragen Erwartungshorizont und Anforderungsbereiche, dann gilt afb_amtlich
  und die Eichung wird Kennzahl (msa.md § 4, Kern § 5). EBR-Hefte bleiben
  zurückgestellt, solange kein EBR-Schüler da ist.
- abi: Berlin 2026 ist ohne Band und ohne Veröffentlichung nicht beschaffbar
  (abi-quellen.md § 5); CAS-Fassungen sind Nachtrag nach WTR.

**Abgrenzung.** Ein *Jahrgang* ist alles, was mit einer neuen Zeile in der
Heftliste und einem neuen soll in KONFIG erfasst werden kann – auch bei
verändertem Aufbau, gewechseltem Landeskürzel oder neuer Rechnerfassung (§ 8,
„Woran man merkt"). Eine *neue Prüfung* nach § 8 liegt vor, wenn Träger,
Prüfungsart, Schulform oder die Quellenlage mit ihrer Ergebnisregel wechseln;
eine *andere Zielprüfung bei gleichem Bestand* ist § 9. Ein *Formatwechsel*
innerhalb des Profils wird an den Kippt-bei-Zeilen in § 4 geprüft: P10 ab
2028 (hilfsmittelfreier Teil, 50 statt 60 BE, msa-vorgaben.md) kippt
Entscheidung 3 – die Decke kommt dann aus den Musteraufgaben, nicht aus dem
Bestand – und verlangt KONFIG, Kürzel MUSTER-FOR und hilfsmittel „nein" im
hilfsmittelfreien Teil (msa.md § 3–4); das Abitur 2027 (Teil A mit Gruppe 1
und 2, abi-vorgaben.md § 2) ändert Struktur und Geltung, nicht die Felder.

*Verlauf bis 17.09.2026, eingefroren:* Entwurf von Kern, Profil msa und
Dateien (05.09.2026); Probelauf mit den Heften 2025, 2026 FOR und 2024 (89
Zeilen), EBR zurückgestellt; Typenliste nach drei Heften festgezogen, die
übrigen MSA-Hefte 2023 bis 2014 erfasst und nach dem letzten Heft
abgeglichen (185 Typen); Profil fhr (12.09.), abi (12.09.) und iqb (13.09.,
Teil A in 22 Stapeln, dann Teil B); Prüfungsblatt-Prompt seit dem 06.09.2026,
Blattbau als eigenes Projekt.

## 8 Eine neue Prüfung aufnehmen

Reihenfolge für ein neues Profil (Beispiel in namensschema.md § 2:
Niedersachsen, Abitur, grundlegendes Niveau – Profil abi-ni). Stand
17.09.2026 (Auftrag D, Teil 4); die Erfahrung dahinter sind die vier Profile
msa, fhr, abi, iqb und ihre Prüfungslisten.

**Zuerst zu klären, in dieser Reihenfolge** – jede Antwort bestimmt eine
Kennung oder eine Regel des Profils:

1. **Träger (Land oder Institution).** Wer stellt die Prüfung, wer
   veröffentlicht Hefte, Lösungen und Vorgaben? Amtliches Länderkürzel als
   Träger-Baustein (namensschema.md § 2); ein länderübergreifender Pool ist
   ein Träger ohne Land (iqb). Ein gemeinsames Werk zweier Länder ist ein
   Profil mit beiden Kürzeln (bebb), auch wenn die Länder verschieden daraus
   zusammenstellen.
2. **Schulform.** Hängt der Inhalt von der Schulform ab (P10: Oberschule
   gegen Gymnasium; Fachoberschule)? Nur dann kommt die Schulform in die
   Kennung; sonst weggelassen (Entscheidung 18: msa nur Oberschule).
3. **Niveau.** Kennt die Prüfung Niveaus, und wie trägt das Heft sie – im
   selben Heft mit Kennzeichnung (msa bis 2025: Sternchen, Feld stern), in
   getrennten Heften (abi: gk/lk, Feld papier) oder gar nicht (fhr)? Das
   Niveau-Kürzel ist das des Trägers, nicht vereinheitlicht.
4. **Zielprüfung(en).** Für welche Prüfung(en) soll der Katalog Material
   liefern? Je Zielprüfung eine Geltungsdatei aus den amtlichen
   Schwerpunkten (Themen ja/nein, ausgeschlossene Aufgabenformen,
   Rechnerfassung; abitur-vokabular.md § 3, Teil 2 des Auftrags D).
   **Zulässige Ausnahme – Prüfungsart ohne Geltung nach Land oder Schulform**
   (Auftrag D Teil 2 Punkt 6, festgehalten 17.09.2026, Auftrag E Punkt 7):
   Eine Geltungsdatei je Zielprüfung ist nur dort nötig, wo dieselbe
   Themenliste je Träger oder Schulform verschieden gilt und ein Skript oder
   der Blattbau danach filtert. Gibt es keine amtlichen Schwerpunkte (msa:
   „prüfungsrelevant ist der Rahmenlehrplan", msa-vorgaben.md), gibt es keine
   Geltung – die ganze Themenliste gilt. Binden die Schwerpunkte Themen nur an
   Prüfungsjahrgänge, nicht an Land oder Schulform (fhr: Markierung (27)/(28)
   in fhr.md § 6, ein Träger, eine Schulform, ein Niveau), bleibt die
   Markierung in der Themenliste; eine Geltungsdatei wäre eine
   Ein-Spalten-Tabelle, die kein Skript liest. Beide Profile bleiben deshalb
   ohne Geltungsdatei, bis ein zweiter Träger oder eine zweite Schulform
   hinzukommt oder ein Skript die Geltung braucht – dann gilt die Regel.
5. **Quellenlage.** Liegen die Hefte amtlich vor (Bildungsserver), nur im
   Verlag (STARK, lokal unter hefte/, nicht im Repo) oder gar nicht?
   Gibt es einen amtlichen Erwartungshorizont (fhr, iqb: Kern § 3 d
   „amtliche Lösung vorhanden", ergebnis mit „(amtlich)", afb_amtlich
   möglich) oder nicht (msa, abi: eigene Rechnung, Schätzung ohne Maßstab)?
   Das entscheidet die Ergebnisregel, die Eichung (Kern § 5: Kennzahl oder
   Schranke) und ob eine Quellenliste erzeugt werden muss (iqb-quellen.py).
6. **Rechnerfassung.** Gibt es Parallelfassungen (WTR/CAS/MMS)? Dann ist die
   Fassung ohne MMS der Hauptzweig und jede andere ein Delta, das je Niveau
   an einem Stapel gemessen wird (Entscheidung 27); Kürzel als Suffix
   (-cas, -mms).
7. **Aufbau der Hefte.** Teile (Feld block), Aufgabenstamm, Punktangaben
   je Buchstabe (Zeilenregel Kern § 4), Wahlaufgaben, Punktschlüssel je
   Jahrgang (abi.md § 11). Daraus folgen KONFIG des Bau-Skripts (soll je
   Aufgabe) und das id-Muster.
8. **Leitideen und Themenliste.** Aus Lehrplan, Schwerpunkten und
   Lehrwerksgliederung (Entscheidung 13). Gleiche Prüfungsart wie ein
   vorhandenes Profil → dessen Vokabular und Typenliste teilen (§ 9); andere
   Prüfungsart → eigene Listen, die vorhandenen als Muster (befund-typenlisten.md).

**Welche Dateien entstehen, in dieser Reihenfolge** (Namen nach
namensschema.md § 2 in der Vollform, Entscheidung 32; die vier bestehenden
Profile behalten ihre Kurzkennungen als Aliasse – msa = msa-bb, fhr = fhr-bb,
abi = abi-bebb, iqb = abi-iqb –, die Familie abi ihren Namen abitur- in
abitur-typen.csv, abitur-vokabular.md und abitur-abgleich.py):

1. `<profil>.md` – das Profil: Prüfung, Ablage und Quellen, Aufbau, Kürzel
   und Werte, Leitideen, Themenliste, Zeile „Zielprüfungen:", Besonderheiten
   beim Erfassen, Beispielzeilen (nach dem ersten Heft aus dem Katalog),
   Offenes. Vorlage: iqb.md (mit Erwartungshorizont) oder abi.md (ohne).
2. `<profil>-quellen.md` – Verzeichnis, Dateinamen, papier-Kürzel,
   Seitenzahlen, lokaler Heftordner; bei großen Quellen dazu
   `<profil>-quellen.csv` mit Erzeuger `<profil>-quellen.py`.
3. `<zielprüfung>-geltung.md` je Zielprüfung (Frage 4; entfällt in der dort
   genannten Ausnahme); jedes Thema der Liste braucht eine Zeile, die
   Bau-Skripte prüfen das.
4. `<profil>-vorgaben.md` – amtliche Vorgaben mit Jahrescheck (Entscheidung
   19); bei gleicher Prüfungsart in die Familiendatei (abi-vorgaben.md).
5. `<profil>-bau.py` – aus dem jüngsten Bau-Skript: alles unter „QUELLEN
   UND PRÜFUNG" übernehmen, Konstanten (KAT, TYP, VOKABULAR, PROFIL,
   GELTUNG_DATEI, ANDERE_KATALOGE) setzen, profilspezifische Prüfungen
   (id-Muster, Kürzel, Pflichtfelder) anpassen; die Selbstprüfung bei leerem
   ZEILEN gehört von Anfang an dazu – ohne sie ist das Profil unvollständig
   (Entscheidung 33, Kern § 7). Zuerst eine Feldprobe: ein Heft mit probe =
   True, nichts geschrieben (abi.md § 7, iqb.md § 7).
6. `<profil>-katalog.csv`, `<familie>-typen.csv` (neu oder geteilt) und
   `<profil>-pruefungen.md` (Heftliste, Kennzahlen, Befunde, Änderungslog)
   entstehen mit dem ersten Heft; Selbstprüfung und byteidentischer Rerun
   aus dem HEAD-Stand vor dem Commit (CLAUDE.md § 3).
7. Abgleichlauf über `<familie>-abgleich.py` nach dem letzten Heft bzw.
   nach jedem Stapel (Kern § 9); bei geteilter Liste zieht er alle Kataloge
   der Familie mit.
8. Nachführen: CLAUDE.md § 1 (Regelwerk und Arbeitsdateien), konzept.md
   § 2 (Baustein) und § 4 (Entscheidung mit Grund), README.md.

**Was aus dem Bestand wiederverwendbar ist:**

- Der Kern (katalog-prompt.md) vollständig: Zeilenregel, 37 Felder,
  Formvokabular, Markierungen, Prüfung, Abgleichlauf. Er ist
  prüfungsunabhängig; ein Profil darf ihm widersprechen, ändert ihn aber
  nicht.
- Die Typenliste weitgehend, wenn die Prüfungsart dieselbe ist: ein neues
  Abiturprofil teilt abitur-typen.csv und abitur-vokabular.md (Entscheidung
  25; die Bildungsstandards sind dieselben, Länderunterschiede liegen in der
  Geltung, nicht in den Typen). Bei anderer Prüfungsart eigene Liste, aber
  die vorhandenen als Muster für Namen und Definitionen: 16 von 26
  Fertigkeiten, die in zwei der drei heutigen Listen vorkommen, sind gleich
  geschnitten (befund-typenlisten.md § 4).
- Die Bau-Skripte im Kern (Laden, Schreiben, Zeilenprüfung, Typenprüfung,
  Selbstprüfung, Kennzahlen), die Regeln der Selbstprüfung und des Reruns,
  die Struktur der Prüfungslisten (§ 2 Liste, § 4 Befunde, § 5 Log).
- Der Themenkatalog (§ 3), weil er prüfungsartübergreifend ist.
- Die Werkzeuge außerhalb des Repos (befund-repo-bestand.md § 3) als Muster; sie
  werden je Sitzung neu geschrieben.
- **Gar nicht: die Geltung.** Sie hängt am Träger und am Niveau; auch bei
  gleicher Prüfungsart und gleicher Themenliste sind die ja/nein-Werte neu
  aus den Schwerpunkten des Trägers zu lesen. Ebenso wenig: Vorgaben
  (landeseigen), Quellenverzeichnis, Prüfungsstruktur und Bewertungsschlüssel
  (abi.md § 11), Kürzel und id-Muster.

**Woran man merkt, dass ein neues Profil nötig ist** statt eines neuen
Jahrgangs im vorhandenen:

- Anderer Träger bei gleicher Prüfungsart (Niedersachsen neben
  Berlin/Brandenburg): eigene Zielprüfungen, eigene Quellen, eigenes
  Kürzel im papier – Profil.
- Andere Prüfungsart oder andere Schulform mit anderem Inhalt (P10 Gymnasium
  neben Oberschule): eigene Themenliste – Profil.
- Andere Quellenlage mit anderer Ergebnisregel (amtlicher
  Erwartungshorizont vorhanden oder nicht): andere Regeln für ergebnis,
  afb_amtlich, Eichung – Profil. Das war der Grund für das Profil iqb neben
  abi (Entscheidung 23): länderneutral, mit Erwartungshorizont, eigenes
  Kennungsmuster.
- Dagegen bleibt es ein Jahrgang im vorhandenen Profil, wenn nur der Aufbau
  wechselt (Corona-Aufbau 2021–2023, Bewertungsschlüssel 2024/2025,
  Strukturbruch 2018/2019: alles in abi über papier, KONFIG und abi.md
  § 11), wenn das Land-Kürzel im selben Aufgabenwerk wechselt (bebb →
  bb/be 2026) oder wenn eine Rechnerfassung hinzukommt (Suffix, Delta).
- Probe: Braucht die neue Sache eine eigene Geltungsdatei, ein eigenes
  id-Muster oder eine andere Ergebnisregel? Dann Profil. Braucht sie nur
  neue Zeilen in der Heftliste und ein neues soll in KONFIG? Dann
  Jahrgang.

## 9 Andere Zielprüfung bei gleichem Bestand

Fall: der Schüler zieht in ein anderes Bundesland oder wechselt den
Schultyp, die Prüfungsart bleibt (Abitur). Der Bestand – Kataloge,
Typenliste, Vokabular – ist eine Sammlung von Fakten über Hefte und
Poolaufgaben und ändert sich dadurch nicht. Was sich ändert, ist die
Geltung.

1. **Typenkatalog bleibt.** abi-katalog.csv, iqb-katalog.csv,
   abitur-typen.csv, abitur-vokabular.md § 1, § 2, § 4 unverändert; kein
   Abgleichlauf nötig.
2. **Geltungsdateien neu anlegen:** je neuer Zielprüfung eine
   `<zielprüfung>-geltung.md` (etwa abi-ni-ga-geltung.md) aus den
   Schwerpunkten des neuen Trägers – § 1 Themen ja/nein für jedes Thema der
   Liste, § 2 ausgeschlossene Aufgabenformen, § 3 Rechnerfassung. Nennen die
   Schwerpunkte ein Thema, das die Liste nicht hat, kommt es nach
   abitur-vokabular.md § 2 und bekommt in jeder Geltungsdatei aller
   Zielprüfungen eine Zeile (die Bau-Skripte verlangen Vollständigkeit);
   die alten Dateien tragen dort „nein".
3. **Profile verweisen auf die neuen Dateien:** die Zeile „Zielprüfungen:"
   in abi.md § 6 und iqb.md § 6 nennt die neuen Zielprüfungen – zusätzlich
   oder statt der alten. Die Bau-Skripte lesen die Zeile; die Kennzahl
   „außerhalb der Geltung" und das Abbruchkriterium (neue Schnittwerte
   innerhalb der Geltung, iqb.md § 6) rechnen dann gegen die neue Geltung.
   Reserve-Stapel, die für die alte Geltung ausgereizt waren, können für
   die neue wieder Neues liefern – die Reihe ist gegen die neue Zielprüfung
   nachzurechnen, bevor die Reserve geschlossen bleibt.
4. **Der Blattbau filtert nach der neuen Geltung** (Thema nach § 1,
   Zeile nach § 2); die Eichung ist unberührt, sie hängt am Pool.
5. **Was neu erfasst werden muss:** die Landeshefte des neuen Trägers, wenn
   sie als Formatmodell und Typenquelle gebraucht werden – das ist ein neues
   Profil nach § 8 (abi-ni), das die Typenliste teilt; der Pool (iqb) gilt
   für jedes Land. Die alten Landeshefte (abi) bleiben Typenquelle, sind
   aber kein Formatmodell der neuen Prüfung mehr.
6. **Was nicht mitzieht:** Prüfungsstruktur und Bewertungsschlüssel (abi.md
   § 11), Vorgaben (abi-vorgaben.md), Quellenverzeichnis – alles
   trägergebunden; die alten Geltungsdateien bleiben liegen, solange die
   alte Zielprüfung noch gebraucht wird, sonst werden sie aus der Zeile
   „Zielprüfungen:" gestrichen und können gelöscht werden.

## 10 Änderungen

- 2026-09-19: Entscheidung 4 und 9 – fhr-Zahl korrigiert (37 statt 49 Typen mit genau einem Vorkommen; Zählung aus fhr-katalog.csv, Fund des Projektarchivs Katalog). Verweis fhr.md § 9 durch fhr-typenbibliothek.md ersetzt, weil § 9 die Zahl nicht mehr führt.
- 2026-09-19: Umbau auf Ordner (README.md, § 2 Absatz Ablage). Blattbau in eigenes Repo ausgelagert; Befunde, namensschema.md und Werkstattzettel nach archiv/; Themenkatalog (29 Einträge, 11j) erstmals ins Repo unter katalog/; Bau-Skripte laufen im Profilordner, katalog-prompt.md über ../. CLAUDE.md § 1 durch Verweis auf README ersetzt, Landkarte-Regel auf README beschränkt.
- 2026-09-18 (Auftrag Korpus und OCR, Etappen 1–4 und Abschluss): korpus-bau.py
  angelegt – rein maschineller Korpus (pypdf-Text je Seite, Ganzseitenrender
  ohne Modell-Lesen) unter `korpus/<profil>/`, Baustein mit Grund in § 2.
  Etappe 1 (msa+fhr, 52 Dateien) und Etappe 2 (abi amtlich 2011–2018, 44
  Dateien) vollständig; Etappe 4 (iqb, 624 von 624 echten Kennungen)
  vollständig, eine Altlast-Datei außerhalb iqb-quellen.csv protokolliert.
  Etappe 3 (OCR der acht Bildscan-Verlagshefte) blockiert: kein
  Tesseract/Ghostscript ohne Administratorrechte installierbar (faellig.md
  § 3). Der Auftrag korrigierte sich selbst nach dem ersten Anlauf: sechs
  msa-Hefte waren im Modell-gelesenen Format hefte-md/ erfasst worden (Zweck
  Katalogprüfung), bevor klargestellt wurde, dass Durchsuchbarkeit
  maschinelle Extraktion ohne Modell-Lesen verlangt – die sechs Dateien
  bleiben unter hefte-md/ liegen (korpus-protokoll.md § 0, § 1). namensschema.md
  v0.5 (Familienname korpus-), README und CLAUDE.md § 1 (Sammelbände-Block)
  nachgezogen.
- 2026-09-18 (Auftrag Korpus und OCR, Etappe 0): Landkarte-Pflegeregel gesetzt – als Zusatz
  zur README-Regel und als Punkt in CLAUDE.md § 3, in der Fassung aus dem Bericht zum
  Nachtrag Musterband (Punkt 5): wer eine Datei anlegt, umbenennt oder aus dem Repo nimmt,
  trägt das im selben Commit in README, CLAUDE.md § 1, § 2 hier und namensschema.md ein,
  soweit betroffen. band-bau.py v0.4 und band-anleitung.md v0.2: Reservemeldung in
  freien Reserveseiten, derselben Größe wie die Abbruchgrenze; die lineare
  Jahrgangsschätzung („etwa 5", gemessen acht) entfällt.
- 2026-09-18 (Nachtrag zum Musterband): § 7 Schritt 10 auf eine Verweiszeile gekürzt, die
  Regel (Zuordnung in der Erfassung, Register aus der Katalogdatei, erst erfassen, dann bauen)
  steht in voller Länge in band-anleitung.md § 6; § 2 Baustein Sammelband mit Grund. README
  Block „Sammelbände – anderes Projekt", CLAUDE.md § 1, namensschema.md v0.4 (Familienname
  band-); band-bau.py v0.3 (Vorspann 13 Seiten, Vorrat acht Jahrgänge).
- 2026-09-18 (Nachbesserungen am Musterband fhr): § 7 Schritt 10 Band neu bauen –
  Strukturliste (`<profil>-band-struktur.py`), Band (`band-bau.py <profil>`), Regel „erst
  erfassen, dann bauen" (Register aus der Katalogdatei; nicht erfasste Hefte stehen im Band,
  nicht im Register). band-bau.py v0.2, fhr-band-struktur.py v0.1, fhr-band.csv und
  baende/ (.gitignore) sind seit diesem Commit im Repo.
- 2026-09-18 (Auftrag O, Punkt 5 und 6): faellig.md angelegt – Handlungen mit Termin oder
  Auslöser und Zuständigkeit, abgegrenzt gegen § 6 (Entscheidungen mit Grund des Wartens);
  Baustein mit Grund in § 2, Pflegeregel in CLAUDE.md § 3, Einstieg im README.
- 2026-09-17 (Auftrag M, Punkt 2): § 2 auf Baustein und Grund gekürzt (13 Bausteinzeilen
  statt 30); Zweckangaben stehen im README, Umbenennungen und Daten hier in § 10 und in
  namensschema.md; befund-stichtag-2026-09-17.md aus der Liste (Befund, kein Baustein).
  Berichtigt: die Basis-URL steht an sieben Stellen, nicht an vier (die vier Profile,
  Prüfungsblatt-Prompt 2.1 und 4.6, Unterrichtsblatt-Prompt 4.6); Ablage-Absatz auf Entscheidung 22 (Claude
  schreibt im Repo, der Lehrer pusht).
- 2026-09-17 (Auftrag J, Punkt 3): § 7 von „Ablauf" (Projektchronik) zur Jahresroutine
  je Profil – Reihenfolge Vorgabencheck vor Erfassung, neun Schritte je Heft und
  Stapel, Besonderheiten abi/iqb (Geltungsdateien, Abbruchreihe, Pooljahrgang),
  Sonderfälle, Abgrenzung Jahrgang / neue Prüfung / Formatwechsel; die Chronik zu
  einem eingefrorenen Absatz verdichtet, weil msa.md § 6 und msa-pruefungen.md § 3 auf
  § 7 verweisen.
- 2026-09-17 (Auftrag J, Punkt 2): befund-repo-stand-2026-09-17.md →
  befund-stichtag-2026-09-17.md (git mv, Inhalt unverändert), damit der Stichtagsbefund
  beim schnellen Lesen von befund-repo-bestand.md zu unterscheiden ist; Verweise in
  README und § 2 nachgezogen, ältere Einträge hier tragen den neuen Namen.
- 2026-09-17 (Auftrag I, Punkt 3): befund-stichtag-2026-09-17.md als eingefrorener
  Stichtagsbefund gekennzeichnet (§ 0 dort, README, § 2 hier); Einstieg bleiben CLAUDE.md
  und konzept.md.
- 2026-09-17 (Auftrag I, Punkt 2): Vorschlag 5 (Sortierung der Typenlisten) aus § 6
  nach § 4 als Entscheidung 34 – abgelehnt, mit Grund (byteidentische Reruns) und
  Kippbedingung.
- 2026-09-17 (Auftrag H, Punkt 4): befund-stichtag-2026-09-17.md angelegt (Stand des Repos
  als Grundlage für einen neuen Chat); § 2 Bausteine und README ergänzt.
- 2026-09-17 (Auftrag H, Punkt 2): § 6 Offen neu gefasst – je Punkt eine Zeile mit
  dem Grund des Wartens (Variante A, Entscheidung 14, Vorschläge 1/2/3/5 aus
  befund-typenlisten.md, Abbruchkriterium abi, strukturelle Geltung, Nachbau-Test);
  erledigte Punkte gestrichen (Blatt-Prompt begonnen: pruefungsblatt.md; Quellen
  und Erwartungshorizonte abi/iqb geprüft: abi-quellen.md, iqb-quellen.md).
- 2026-09-17 (Auftrag G, Punkt 4): Entscheidung 26 fortgeschrieben – msa behält die
  eigene Regel Zeilenthema „Thema der Aufgabenstellung" (entschieden; 42 von 393
  Zeilen weichen vom Typthema ab; kippt bei profilübergreifender Auswertung).
  Entscheidung 14 mit neuem Grund: Kippbedingungen eingetreten, die Zusammenlegung
  der msa-Katalogdateien wartet auf den Umbau von Prüfungsblatt- und Unterrichtsblatt-Prompt; bis
  dahin zwei Dateien (offen).
- 2026-09-17 (Auftrag G, Punkt 3): fhr-vorgaben.md angelegt (Entscheidung 19, Muster
  msa-vorgaben.md); § 2 Bausteine ergänzt.
- 2026-09-17 (Auftrag F, Punkte 4–7): Entscheidung 32 Dateibenennung (Variante B,
  Kurzkennungen als Aliasse der Vollform, neue Dateien und Profile in Vollform;
  § 2 und § 8 entsprechend); Entscheidung 33 Selbstprüfung als Bedingung eines
  vollständigen Profils mit dem Befund 646 nie maschinell geprüfte Zeilen (Kern v0.9
  § 7, CLAUDE.md § 3). Kern v0.9 § 6 Zeilenthema = Typthema mit Vorbehalt für das
  Profil, § 5 Eichung nur bei amtlichen Anforderungsbereichen (Vorschläge aus
  Auftrag E, Punkt 2; msa.md v0.5 und fhr.md v1.8 nennen ihre Regel). .gitignore
  geprüft: keine umbenannten Pfade, unverändert.
- 2026-09-17 (Auftrag F, Punkt 3): abi-iqb-typen.md → befund-abi-iqb-typen.md (Kopfvermerk:
  Messung vor Abgleichlauf 12, die gemessenen Dateien existieren nicht mehr) und
  repo-bestand.md → befund-repo-bestand.md (namensschema.md § 2, Muster befund-<gegenstand>);
  nichts gelöscht, Verweise in § 4 und § 8 nachgezogen.
- 2026-09-17 (Auftrag F, Punkt 2): abgleich.py → abitur-abgleich.py (Familienname wie
  abitur-typen.csv; git mv, Inhalt unverändert); Verweise in § 2, § 4 und § 10 nachgezogen.
- 2026-09-17 (Auftrag F, Punkt 1): Dateien des Profils msa mit Präfix msa- (typen.csv →
  msa-typen.csv, katalog-basis.csv → msa-katalog-basis.csv, katalog-kontext.csv →
  msa-katalog-kontext.csv, pruefungen.md → msa-pruefungen.md, vorgaben.md →
  msa-vorgaben.md; git mv, Inhalt unverändert); Verweise in § 2, § 4 und § 7 nachgezogen.
- 2026-09-17 (Auftrag E, Punkt 7): § 8 Frage 4 – zulässige Ausnahme „Prüfungsart
  ohne Geltung nach Land oder Schulform" (msa, fhr) mit Begründung aus
  Auftrag D Teil 2; Dateiliste Punkt 3 verweist darauf.
- 2026-09-17 (Auftrag E, Punkt 4): Begriffe – Klasse statt Unterklasse, Feinetikett statt Feintyp, Schnitt statt Typenschnitt (Entscheidungen 24, 25), Schätzung des Anforderungsbereichs statt Niveauschätzung (23), WTR-Fassung statt WTR-Zwilling (27).
- 2026-09-17 (Auftrag D, Teil 7): Entscheidung 29 um die Regel „eine Vormerkung
  überlebt keinen Auftrag" ergänzt (abi.md v0.24, iqb.md v1.11, CLAUDE.md); § 6
  offener Punkt Tokenverbrauch und Plattformunabhängigkeit aufgenommen, ohne
  Bearbeitung.
- 2026-09-17 (Auftrag D, Teil 5): § 4 je Entscheidung „Zahl" (tragende Zahl mit
  Fundstelle) und „Kippt bei"; Entscheidungen 27–31 (MMS als Delta,
  Abbruchkriterium, Vormerkung und Reserve, Geltung je Zielprüfung, Vorrang
  des Amtlichen und Maßstab der Schätzung) aus den Profilen nachgetragen.
- 2026-09-17 (Auftrag D, Teil 4): § 8 Eine neue Prüfung aufnehmen (Fragen,
  Dateien in Reihenfolge, Wiederverwendbares, Profil oder Jahrgang) und § 9
  Andere Zielprüfung bei gleichem Bestand; Änderungen sind jetzt § 10.
- 2026-09-15: Entscheidung 25 – gemeinsame Typenliste abitur-typen.csv und
  gemeinsames Vokabular abitur-vokabular.md für abi und iqb, abitur-abgleich.py über
  beide Kataloge, Umstellungslauf 12 (938 → 875 Typen). §2 Bausteine ergänzt.
- 2026-09-13: Entscheidung 24 – Schnitt Thema × Gegenstandsklasse × Handlung für
  Teil A des Pools, Gegenstandsklasse als Präfix im Typnamen, Abgleichlauf über
  iqb-abgleich.py (183 → 174 Typen).
- 2026-09-13: Entscheidung 23 – Profil iqb für den IQB-Aufgabenpool, Stapel als
  Laufeinheit, Qualitätsschranke im Skript. §2 Bausteine um die Profile fhr, abi, iqb
  und abi-vorgaben.md ergänzt. Ablauf §7: 4b Profil iqb, Teil A zuerst.
- 2026-09-12: §3 Themenkatalog aufgenommen – Zweck, Leser, Arbeitsteilung mit dem
  Prüfungskatalog, Geltung über die Prüfungsarten hinweg. Bis dahin war der Themenkatalog
  im Repo nirgends beschrieben. Folgeabschnitte umnummeriert (3–7 → 4–8).
- 2026-09-12: Baustein Typenbibliothek je Profil (Ausgabe und erzeugendes Skript); für fhr angelegt,
  nachdem dessen Katalog vollständig war. Die Deckenwahl darin ist als vorläufige Rechnung gekennzeichnet,
  solange die Merkmalsfrage offen ist (blatt-konzept.md § 7).
- 2026-09-05: angelegt.
- 2026-09-05: Probelauf abgeschlossen. EBR zurückgestellt, Profil abi vorgemerkt (Entscheidung 12 ergänzt). Typen-Check: drei Bruchteil-Typen zusammengelegt, Flächen-/Umfangsterm → „Term zu Figur zuordnen“, „Wahrscheinlichkeit zweistufig“ in unabhängig/ohne Zurücklegen getrennt, Mittelpunktswinkel als Baustein vermerkt; alle Typen auf „gültig“. Kern §1: Dateinamen nach Profil.
- 2026-09-05: Typen-Check nach Heften 2023–2019: 147 → 141 Typen, alle „gültig“. Zusammengelegt: Winkel im Trapez/Parallelogramm → „Winkel im Viereck berechnen“; Wahrscheinlichkeit zwei-/dreistufig → „… mehrstufig unabhängig“ und „… mehrstufig ohne Zurücklegen“ (Stufenzahl in gegeben/schritte); Flächenformel Dreieck/Rechteck angeben + Term zu Figur zuordnen → „Term zu Figur angeben“ (Leistung in format); Flächeninhalt Dreieck über Höhe → „Flächeninhalt Dreieck berechnen“ (Vorarbeit in typ_neben). Umbenannt: Lineare Kostenfunktion aufstellen → „Lineare Funktion aus Sachverhalt aufstellen“ (gegen „Lineare Gleichung aus Sachverhalt aufstellen“ abgegrenzt); Endwert linearer Zunahme → „… Veränderung“; Bruch in Prozent umwandeln → „Prozent und Anteil umwandeln“; Zehnerpotenz Exponent bestimmen → „Zehnerpotenzschreibweise umwandeln“; Säulendiagramm ergänzen → „Säulen- oder Balkendiagramm ergänzen“. Definitionen erweitert: Gleichung im Sachzusammenhang deuten (Bestandteile benennen), Term zu Sachtext zuordnen (auch Gleichungen), Proportionale Zuordnung Dreisatz (Abgrenzung zu Zeit aus Weg und Geschwindigkeit), Zufallsgerät entwerfen (Thema jetzt Wahrscheinlichkeit einstufig). Lösung durch Einsetzen prüfen: Thema Lineare Gleichungen. Getrennt gelassen: Gleichung/Graph zu Tarif zuordnen, Geradengleichung zu Graph zuordnen, Graph nach Eigenschaft auswählen (vier verschiedene Richtungen); Nullstelle berechnen vs. am Graphen ablesen. Zwei „?“ in gesucht (2026-FOR-K5b, 2024-OS-K3c) umformuliert.
- 2026-09-05: Typen-Check nach Heften 2018–2014 (Abgleichlauf): 193 → 185 Typen, alle „gültig“, msa-typen.csv nach Leitidee (Lehrplanreihenfolge), Thema, Typ sortiert. Zusammengelegt: Zeit aus Weg und Geschwindigkeit + Dauer aus Menge und Durchsatz → „Dauer aus Menge und Rate berechnen“ (Gegenrichtung „Geschwindigkeit aus Weg und Zeit berechnen“ bleibt: andere Formelrichtung, wie bei Fläche/Seite); Verdopplungszeit am Graphen + Halbwertszeit aus Tabelle → „Verdopplungs- oder Halbwertszeit bestimmen“; Teilstrecke berechnen + Weglänge aus Teilstrecken → „Strecke aus Teilstrecken berechnen“; Körper zu Netz zuordnen + Körper im Schrägbild benennen → „Körper aus Netz oder Schrägbild benennen“; Jahreszinsen berechnen → „Prozentwert berechnen“, Zinssatz berechnen → „Prozentsatz berechnen“ (Zinsvokabular ist Kontext, Thema Zinsrechnung behält Guthabentabelle und Zinseszins). Gelöscht (Leistung steht in format bzw. bemerkung): „Lösungsweg beschreiben“ (2015-OS-K5d jetzt Flächeninhalt Dreieck berechnen, format Begründung – wie Mantellinie 2018-OS-K6d) und „Ergebnis sinnvoll runden“ (Konvention: Vermerk in bemerkung, kein Typ). Umbenannt: Teilwinkel berechnen → „Winkel aus Teilwinkeln berechnen“; Term zu Sachtext zuordnen → „Term zu Sachtext angeben“ (Angeben, Auswählen, Richtig/Falsch in format; 2016-OS-B1b hierher, Abgrenzung zu Lineare Gleichung aus Sachverhalt); Volumenterm zu Körper prüfen → „Term zu Körper angeben“ (parallel zu Term zu Figur angeben); Zahl zu Ungleichung angeben → „Zahl zu Bedingung angeben“ (auch „zwischen“, Abgrenzung zu Mitte zweier Zahlen); Masse aus Volumen berechnen → „Masse aus Volumen und Dichte berechnen“ (Gegenrichtung zu Volumen aus Masse und Dichte, getrennt wie bei Fläche/Seite). Definitionen erweitert: Wachstumstabelle ergänzen (Abnahme, fehlende Zeitangabe, Abgrenzung Guthabentabelle), Zufallsgerät entwerfen (Anzahl berechnen ohne Zeichnung), Graph zu Tarif zuordnen (lineare Tarife), Parabel verschieben (nur Scheitel), Wert aus Diagramm ablesen (Funktionsgraph im Sachzusammenhang), Flächeninhalt Dreieck (Rechenweg beschreiben), Proportionale Zuordnung Dreisatz (Abgrenzung Rate). Thema geändert: Mantelfläche Prisma berechnen → Volumen und Oberfläche (wie Mantelfläche Zylinder/Kegel). Belassen: Restfläche/Restvolumen, Mantellinie Kegel unter Pythagoras, Große Zahl mit Zehnerpotenz multiplizieren, Parabelgleichung zu Graph zuordnen, Zeitpunkt für Schwellenwert (schrittweise, anders als Ablesen). Typ_neben „Flächeninhalt Rechteck berechnen“ an 2018-OS-K6a und 2017-OS-K3b ergänzt. Prozessnotizen in bemerkung von neun Zeilen bereinigt, Fakten unverändert. 37 Katalogzeilen umetikettiert.
- 2026-09-06: Entscheidung 6 (Lösungen) an blatt-konzept.md v0.2 angeglichen.
- 2026-09-06: Basis-URL steht auch im Blatt-Prompt (§2). blatt-prompt.md v0.1 angelegt.
- 2026-09-06: Nr. 5 Herkunft → Protokoll; §2 blatt-prompt nur als Projektanweisung.
- 2026-09-07: §2 Prüfungsblatt-Prompt (`pruefungsblatt.md`, vorher blatt-prompt) und Unterrichtsblatt-Prompt mit Masterfassung im Repo, CHANGELOG.md; Aufteilung nach Quelle (blatt-konzept.md §5). Entscheidung 16 ergänzt: FHR-Lehrerhefte enthalten den Erwartungshorizont. Repo umbenannt in mathe-nachhilfe; Vorlage und Anleitung aus dem Vorlagen-Repo hierher, ein Repo für alles; Basis-URL an vier Stellen umgestellt.
