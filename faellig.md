# FÄLLIG – Handlungen mit Termin oder Auslöser

Stand 18.09.2026 · angelegt in Auftrag O, Punkt 5 · gilt für alle Profile

**Abgrenzung.** konzept.md § 6 führt offene *Entscheidungen* mit dem Grund des
Wartens; diese Datei führt *Handlungen* mit Termin oder Auslöser und mit der
Angabe, bei wem sie liegen. Kein Posten steht in beiden. Bestandszahlen stehen
hier nicht (Prüfungslisten, befund-quellenbestand-2026-09-18.md). Nichts ist
neu erhoben: Termine und Auslöser stammen aus den genannten Fundstellen; wo
keine Fundstelle einen Zeitpunkt belegt, steht „Auslöser unbekannt" oder
„unbelegt".

**Pflege** (CLAUDE.md § 3): Wer einen Posten erledigt, streicht ihn im selben
Commit hier und trägt ihn mit Datum in § 4 ein; wer einen neuen Posten
bemerkt, trägt ihn hier ein, statt ihn im Bericht zu lassen.

Je Posten eine Zeile: was · Auslöser oder Termin · bei wem · Fundstelle.

## 1 Jährlich wiederkehrend (Jahresroutine, konzept.md § 7)

Reihenfolge je Profil: erst Vorgabencheck, dann Quelle, dann Lauf (konzept.md
§ 7). Die Jahreszahlen nennen den nächsten Jahrgang; die Zeile gilt jedes Jahr.

**msa**

| Was | Auslöser oder Termin | Bei wem | Fundstelle |
|---|---|---|---|
| Vorgabencheck: neuesten Fachbrief Mathematik Brandenburg (Nr. 11) und Rundschreiben des MBJS lesen, Zeile in § 2 der Vorgaben-Datei | Fachbrief zum Schuljahresbeginn (Reihe belegt: Nr. 9 08/2025, Nr. 10 08/2026 – erwartet 08/2027); Rundschreiben aus der Sandbox nicht erreichbar | Claude (Check), Lehrer (Rundschreiben, falls nötig) | msa-vorgaben.md § 1, § 2, § 4 |
| Heft 2027 FOR holen, in die Heftliste eintragen, erfassen; EBR bleibt zurückgestellt | Prüfung 04.05.2027 (Fachbrief 10); Veröffentlichung auf der Jahresseite: Zeitpunkt unbelegt (Heft 2026 lag vor dem 05.09.2026 vor) | Lehrer (Anweisung „weiter"), Claude (Lauf) | msa-quellen.md § 1, msa-pruefungen.md § 2, konzept.md § 7 Sonderfälle |
| Typen-Check über den Bestand nach dem letzten Heft des Jahrgangs | Heft erfasst | Claude | konzept.md § 7 Punkt 5, msa-pruefungen.md § 3 |

**fhr**

| Was | Auslöser oder Termin | Bei wem | Fundstelle |
|---|---|---|---|
| Vorgabencheck: Prüfungsschwerpunkte Mathematik des nächsten Schuljahrs (2028/29) und Rundschreiben des MBJS lesen, Zeile in § 2; Schwerpunktmarkierung der Themenliste nachziehen | Prüfungsschwerpunkte erscheinen im Ordner Pruefungsschwerpunkte/ – Zeitpunkt unbelegt (2026/27 und 2027/28 lagen am 18.09.2026 vor); Rundschreiben belegt für 2026: MBJS_RS_07-26 vom 25.06.2026 | Claude | fhr-vorgaben.md § 1, § 4; fhr.md § 6 |
| Hefte 2027 (zwei Vorschläge) holen, in die Heftliste eintragen, erfassen | Prüfung Mai/Juni (2026: 05.06.2026); Veröffentlichung der Lehrerhefte: Zeitpunkt unbelegt (Hefte 2026 lagen vor dem 12.09.2026 vor) | Lehrer (Anweisung), Claude (Lauf) | fhr-quellen.md § 1, fhr-pruefungen.md |
| Typen-Check über den Bestand nach dem letzten Heft des Jahrgangs; danach `python fhr-typenbibliothek.py` | Heft erfasst; jede Katalogänderung | Claude | konzept.md § 7 Punkt 5 und 9, fhr-pruefungen.md |

**abi**

| Was | Auslöser oder Termin | Bei wem | Fundstelle |
|---|---|---|---|
| Vorgabencheck: Prüfungsschwerpunkte 2028 beider Länder und beider Niveaus und Rundschreiben des MBJS lesen, Zeile in § 2; danach die vier Geltungsdateien nachziehen | „wenn die Prüfungsschwerpunkte des nächsten Jahrgangs erscheinen" (abi-vorgaben.md § 4) – Zeitpunkt unbelegt; Brandenburg 2028 lag am 18.09.2026 lokal vor (hefte/abi/sonstiges/), Berlin 2028 nicht | Claude | abi-vorgaben.md § 1, § 4; konzept.md § 7 „Nur abi und iqb" |
| STARK-Band zum Abitur 2028 (GK und LK) beschaffen, Hefte 2027 als Scan oder PDF unter hefte/abi/, Zeile in abi-quellen.md § 8 und abi-pruefungen.md § 2, erfassen (Berlin und Brandenburg seit 2026 getrennt) | Erscheinen des Bandes – Zeitpunkt unbelegt (Band 2027 lag im September 2026 vor) | Lehrer (Beschaffung), Claude (Lauf) | abi-quellen.md § 5, § 8; konzept.md § 7 Punkt 2 |
| Amtliche Veröffentlichung eines neuen Jahrgangs | kein Auslöser: der Bildungsserver veröffentlicht 2011–2018, danach nichts | – | abi-quellen.md § 1 |

**iqb**

| Was | Auslöser oder Termin | Bei wem | Fundstelle |
|---|---|---|---|
| Neuen Pooljahrgang 2027 aufnehmen: `python iqb-quellen.py hefte/iqb` (Kennungen dürfen nur hinzukommen), Stapel in iqb-pruefungen.md § 2, Teil A grundlegend vor erhöht, Teil B WTR, MMS als Delta | Veröffentlichung des Pools „nach der Prüfung" (abi-quellen.md § 4) – Zeitpunkt unbelegt (Pool 2026 lag am 13.09.2026 vor) | Claude | iqb-quellen.md, konzept.md § 7 „Neuer Pooljahrgang" |
| Abbruchreihe je Niveau gegen die Zielprüfung nachrechnen | Vorgabencheck abi hat die Geltung geändert | Claude | konzept.md § 7 „Nur abi und iqb", iqb.md § 6 |

## 2 Einmalig, mit Auslöser

| Was | Auslöser oder Termin | Bei wem | Fundstelle |
|---|---|---|---|
| Vorbehalt in fhr-vorgaben.md auflösen: Schritt 0 des Jahreschecks – Herkunft der Angaben gegen Prüfungsschwerpunkte, Rundschreiben und Rahmenlehrplan halten, Abweichungen berichtigen, Vorbehalt streichen | erster Jahrescheck fhr (§ 1); die Papiere 2026/27, 2027/28 und MBJS_RS_07-26 liegen seit Auftrag N lokal (hefte/fhr/sonstiges/), der Schritt ist also jederzeit ausführbar | Claude | fhr-vorgaben.md Kopf und § 4 Schritt 0; konzept.md § 7 Sonderfälle |
| Vorbehalt in abi-quellen.md § 5 auflösen: Angaben des Lehrers zu den Verlagsbänden gegen die Bände prüfen | Auslöser unbekannt (kein Termin festgelegt; die Bände liegen beim Lehrer) | Lehrer (Bände vorlegen oder bestätigen), Claude (Prüfung) | abi-quellen.md Vorbehalt unter der Versionszeile, § 5 |
| CAS-Nachtrag 2017/2018: sechs CAS-Hefte (2017-be-gk-cas, 2017-be-lk-cas, 2017-bb-ea-cas, 2018 entsprechend) nach der Regel in abi.md § 7 (eigene Zeile nur für abweichende Teilaufgaben) | Anweisung des Lehrers; Bedingung „nach den WTR-Heften" ist seit 12.09.2026 erfüllt. Für die Berliner CAS-Hefte ist die Abgrenzung nicht entschieden (abi.md § 9) | Lehrer (Anweisung), Claude (Lauf) | abi.md § 7; abi-pruefungen.md § 2 („zurückgestellt – Nachtrag nach WTR") |
| Formatwechsel P10 ab 2028: Musteraufgaben 2028 FOR erfassen (Fachbrief 10, S. 20–31; lokal nicht gesichert), KONFIG, Kürzel MUSTER-FOR, hilfsmittel „nein" im hilfsmittelfreien Teil, afb_amtlich, Eichung wird Kennzahl; Entscheidung 3 kippt (Decke aus den Musteraufgaben) | Schüler mit Prüfungsjahr 2028 (Annahme heute 2027, konzept.md § 6) oder das erste Heft 2028 | Lehrer (Anweisung), Claude (Lauf) | msa-vorgaben.md § 2 „ab 2028", msa.md § 3–4, msa-pruefungen.md § 2, konzept.md § 7 Abgrenzung und Entscheidung 3 |
| Berlin 2026 (be-gk, be-lk) beschaffen und erfassen | falls je beschaffbar: kein STARK-Heft, keine Veröffentlichung, keine andere Quelle bekannt | Lehrer (Quelle) | abi-quellen.md § 5, abi-pruefungen.md § 3 |
| 2017-be-gk erfassen (Berliner Grundkurs 2017, WTR) | Anweisung des Lehrers („2017 be-gk"); die Datei liegt vor (hefte/abi/2017-be-gk.pdf, Bildungsserver) – der Auftrag O nennt sie „falls je beschaffbar", beschaffbar ist sie | Lehrer (Anweisung), Claude (Lauf) | abi-pruefungen.md § 2 („nicht erfasst"), abi-quellen.md § 2, § 8 |
| 2017-be-lk und 2018-be-lk: die eigenen Aufgaben (drei bzw. zwei, nicht wortgleich mit bb-ea) erfassen | Anweisung des Lehrers; ob überhaupt, hängt am Abbruchkriterium abi (Entscheidung offen, konzept.md § 6) | Lehrer (Anweisung), Claude (Lauf) | abi-pruefungen.md § 2 („teilweise abgedeckt") |
| Standard-Cache von iqb-quellen.py von iqb-pdf/ auf hefte/iqb/ umstellen und README, konzept.md § 2, .gitignore nachziehen (der Ordner iqb-pdf/ ist nicht angelegt, der Cache liegt seit Auftrag N unter hefte/iqb/) | nächster Lauf von iqb-quellen.py (neuer Pooljahrgang, § 1) oder Anweisung des Lehrers; bis dahin Aufruf mit Argument `hefte/iqb` | Claude | namensschema.md § 1 (Zeile Heftdateien), befund-quellenbestand-2026-09-18.md § 6 |

## 3 Liegt beim Lehrer

| Was | Auslöser oder Termin | Bei wem | Fundstelle |
|---|---|---|---|
| Projektanweisung des Aufgaben-Projekts auf pruefungsprompt.md v0.15 nachziehen – die alte Kopie holt typen.csv, katalog-basis.csv, katalog-kontext.csv, die es seit dem Push nicht mehr gibt; das Projekt ist bis dahin defekt | sofort (seit 17.09.2026 fällig) | Lehrer | CHANGELOG.md (2026-09-17 v0.15), pruefungsprompt.md 2.1, konzept.md § 2 („Projektanweisungen sind Kopien") |
| Projektanweisung des Masterprompt-Projekts auf masterprompt.md v3.35 nachziehen (inhaltlich gleich v3.34, nur Versionszeile) | bei der nächsten Änderung am Masterprompt, spätestens dann | Lehrer | CHANGELOG.md (2026-09-17 v3.35) |
| Backup von hefte/ und hefte-md/ anlegen: 929,8 MB unter hefte/ ohne dubletten/ (dazu 32,6 MB dubletten/), hefte-md/ 1,9 MB – einzige Sammlung, nicht im Repo, nicht vom Push erfasst | sofort; danach nach jeder Erweiterung (§ 1) | Lehrer | befund-quellenbestand-2026-09-18.md § 2, § 7; befund-heftkorpus-2026-09-17.md § 2 (Größe hefte-md/); .gitignore |
| hefte/dubletten/ löschen (byteidentische Zweitstücke, Liste dubletten.md dort) und die 83 Zweitstücke im Download-Ordner des Lehrers – beides nur, wenn gewollt | nach dem Backup | Lehrer | befund-quellenbestand-2026-09-18.md § 7, hefte/dubletten/dubletten.md |
| Push: die lokalen Commits seit origin/main (Auftrag O, sechs Commits nach Abschluss) | nach jedem Auftrag | Lehrer | konzept.md § 2 (Entscheidung 22: der Lehrer pusht), § 7 Punkt 7 |

## 4 Erledigt

Beim Anlegen leer. Je Zeile: Datum · was · wer.

| Datum | Was | Wer |
|---|---|---|
