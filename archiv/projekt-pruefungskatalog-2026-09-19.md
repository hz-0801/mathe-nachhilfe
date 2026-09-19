# Projekt Prüfungskatalog – Archivdurchsicht

Projekt: Prüfungskatalog · Zeitraum 06.09.2026 – 19.09.2026 · 13 Chats ·
Durchsicht 19.09.2026

Gelesen wurden `README.md`, `konzept.md` und `blatt-konzept.md` (Stand
19.09.2026) sowie alle 13 Chats des Projekts. Die Profile, Prüfungslisten,
`katalog-prompt.md`, `CLAUDE.md` und die Befunddateien wurden **nicht** gelesen;
wo ein Fund unten dort stehen könnte, ist das vermerkt.

## 1 Warum dieses Projekt entstand

**Ziel** (Projektanweisung § 1): Die Aufgaben vergangener Abschlussprüfungen
Teilaufgabe für Teilaufgabe beschreiben – gegeben, gesucht, Verfahren,
Aufgabentyp –, damit aus den Typen später Arbeitsblätter gebaut werden können.
Maßstab jeder Zeile ist der Nachbau-Test. Der Blattbau selbst gehört
ausdrücklich nicht dazu.

**Anlass: nicht ausdrücklich festgehalten, nur ableitbar.** Das Projekt enthält
keinen Gründungschat. Der älteste Chat (06.09.2026) beginnt mitten in der
Arbeit mit der Frage, ob sich die Erfassung vollautomatisieren lässt; der
zweitälteste ist der Einstieg ins Abiturprofil, „msa mit github 8" trägt die
Nummer 8 einer Reihe, die außerhalb dieses Projekts lief. Die Erfassung war
also schon im Gang, als das Projekt angelegt wurde: Es entstand als
Arbeitsraum für die Ausweitung von msa auf die übrigen Prüfungsarten, nicht am
Anfang der Sache. Der übergeordnete Zweck – Prüfungsvorbereitung eines
Nachhilfeschülers auf P10 – steht nur in `konzept.md` § 1, nicht in den Chats.

**Status: Ziel erreicht, mit benannten Lücken.** Alle vier Profile sind erfasst
und maschinell geprüft: 2883 Katalogzeilen in fünf Dateien, 1643 Typen in drei
Listen, vier Bau-Skripte mit Selbstprüfung (Stand der Selbstprüfung
17.09.2026). msa und fhr schöpfen den verfügbaren Bestand aus, iqb ist nach dem
Abbruchkriterium ausgereizt, bei abi fehlen Berlin 2026 (nicht beschaffbar) und
2017-be-gk. Letzter Chat: 19.09.2026.

**Abgelöst wurde das Projekt nicht**, es hat zwei Abspaltungen: der Blattbau
(eigenes Projekt, seit dem 19.09.2026 eigenes Repo `blattbau`) und
`erstellePrüfungssammlung()` – Heftkorpus, OCR und Sammelbände –, dessen
Übergabe im letzten Chat dieses Projekts geschrieben wurde. Die Erfassung
selbst läuft nur noch als Jahresroutine (`konzept.md` § 7).

## 2 Was in den Chats steht und im Repo fehlt

**06.09.2026 – Vollautomatische Erfassung verworfen.** Eine Agentenschleife
(Skript füttert die API mit Katalogstand plus nächstem Heft, Asserts prüfen,
Commit, nächstes Heft) ist machbar, schafft aber die zwei Kontrollpunkte ab,
auf denen die Qualität beruht: die Prüfung der Ankeraufgabe gegen das Original
und die Etikettenentscheidung. Grund im Kern: Typenkonsistenz ist kumulativ –
ein falsch angelegter Typ in Zeile 50 verzerrt jede spätere
Ähnlichkeitsentscheidung und fällt erst auf, wenn der ganze Lauf durch ist.
Dasselbe Argument schließt Batch-Parallelität aus, weil jeder Aufruf den
vollen Typenstand braucht. `konzept.md` § 5 führt den Punkt nicht.

**07.09.2026 – Wann die Abiturprüfung gemeinsam gestellt wird.** Die
bindenden MBJS-Rundschreiben begrenzen die gemeinsame Aufgabenstellung bis
einschließlich Prüfungsjahr 2020 auf Berliner Leistungskurse und Brandenburger
Kurse auf erhöhtem Anforderungsniveau; erst das Rundschreiben vom 04.12.2020
(Prüfungsjahr 2021) lässt diese Eingrenzung fallen. Das erklärt, warum die
Archivseite 2011–2018 für Brandenburg nur das erhöhte Niveau führt. Vorbehalt
aus dem Chat: „weitgehend gemeinsam" heißt nicht identisch, und warum der
Wortlaut genau 2020/21 kippte, ist nicht belegt. Kann in `abi.md` § 10–11
stehen; in `konzept.md` steht es nicht, und am 12.09.2026 war die Frage „auf
welcher Vereinbarung beruht das gemeinsame Aufgabenwerk" noch als offen
geführt.

**12.09.2026 – `beispiel_id` bedeutet nicht, was der Name nahelegt.** Bei
zusammengeführten Typen trägt das Feld die id des aufnehmenden Typs, nicht die
älteste Fundstelle; „erste Fundstelle" ist mehrdeutig, weil nicht chronologisch
erfasst wurde. Das ist eine Leseregel für den Kern, nicht für ein Profil.

**12.09.2026 – Koordinaten in msa mit „|".** `msa.md` schreibt Koordinaten mit
demselben Zeichen, das im Dateiformat den Mehrfachwert trennt. Als Vorschlag
zur Nachbesserung gemeldet, nicht ausgeführt, seitdem nie wieder aufgegriffen.

**12.09.2026 – Arbeitszeit Grundkurs ungeklärt.** 285 Minuten laut
Prüfungsschwerpunkten 2027 gegen 255 Minuten aus einem früheren Fachbrief. Als
„ungeklärt, folgenlos" abgelegt und nie geklärt.

**14.09.2026 – Skill „abi-heft-erfassen" verworfen.** Am 12.09.2026 noch als
nächster Arbeitsschritt vorgesehen, zwei Tage später fallengelassen, weil
`CLAUDE.md` den Ablauf bereits enthält. Nicht in § 5.

**14.09.2026, bestätigt 19.09.2026 – keine Parallelarbeit im selben Klon.**
Zwei gleichzeitige Läufe machen Selbstprüfung und byteidentischen Rerun
wertlos, weil beide auf einem bekannten Einzelstand aufsetzen müssen. Ein
Worktree auf eigenem Branch wäre für den Abi-Strang möglich, für zwei
iqb-Stapel nicht – die gemeinsame Typenliste koppelt sie. Nicht eingerichtet
und nirgends festgehalten; Entscheidung 34 begründet den Rerun, nennt diese
Folge aber nicht.

**17.09.2026 – Übergaben sollen Zahlen nicht wiederholen.** Die damalige
Übergabe nannte 1443, 794 und 1323, obwohl die Regel Bestandszahlen an genau
einer Stelle vorschreibt. Empfehlung: künftige Übergaben verweisen auf
Commit-SHA und Prüfungsliste, weil Zahlen und Dateinamen nach einer
Umbenennung lautlos veralten. Nicht entschieden.

**17.09.2026 – die Arbeitsweise des Chat-Strangs steht nur in Übergaben.**
Anlass: Ein neuer Chat übernahm den Strang und arbeitete anders, weil die
Übergabe den Stand beschrieb, nicht die Führung. Nachgereicht als Textblock –
nach jedem Bericht bewerten, was trägt, was schwach ist, was sich widerspricht;
den nächsten Auftrag vollständig im Codeblock; Entscheidungen mit Empfehlung
vorlegen statt zurückfragen; fehlende Zahlen benennen; ungepushte Commits jedes
Mal nennen. Weder im Repo noch in der Projektanweisung.

**19.09.2026 – Vorkommen je Typ, je Profil gezählt.** msa 2,9, fhr 3,6, abi
1,5, iqb 1,4; bei abi und iqb kommen vier von fünf Typen genau einmal vor. Die
gemeinsame Typenliste senkt die Zahl der Einmal-Typen von 1330 (getrennt
gezählt) auf 870 – damit ist Entscheidung 25 belegt und nicht nur plausibel.
Folgerung aus dem Chat: Für abi liefert der Katalog keine Häufigkeit, aus der
sich ableiten ließe, was eine Prüfung prägt; das Gewichtungsmittel, das msa
hat, fällt dort weg. `konzept.md` Entscheidung 1 nennt nur 3,61 für fhr und
1,69 Zeilen je Typ fürs Abitur, nicht die Verteilung je Profil.

**19.09.2026 – `typ_neben` wird je Profil verschieden benutzt.** Typen je
Zeile: fhr 1,9, msa 1,4, abi 1,1, iqb 1,03; bei iqb ist das Feld praktisch tot,
bei fhr ist jeder dritte Typ (49 von 135) nie Haupttyp. Ursache ist die
Erfassung – vier Läufe, vier Auffassungen davon, wann ein zweiter Typ zu nennen
ist –, nicht die Prüfung; profilübergreifende Auswertungen vergleichen
Ungleiches.

**19.09.2026 – Entscheidung 9 trägt eine falsche Zahl.** Sie nennt „fhr 49 von
135 Typen genau einmal" und verweist dafür auf `fhr.md` § 9; dieselbe Zahl mit
demselben Verweis steht in der Kippt-bei-Zeile von Entscheidung 4. `fhr.md` § 9
führt die Zahl nicht mehr – beide Verweise gehen ins Leere. Die Zählung aus
`fhr-katalog.csv` (19.09.2026) ergibt: 37 Typen genau einmal Haupttyp, 49
mehrfach, 49 nie. Die 49 ist die Zahl der Typen, die nie Haupttyp sind – zwei
verschiedene Mengen unter einem Etikett. Richtig ist 37, Quelle künftig
`fhr-typenbibliothek.md`. Die Begründungen der Entscheidungen 4 und 9 werden
dadurch nicht falsch, aber ihre tragende Zahl ist kleiner als angegeben.

## 3 Repo-Stand

Nicht vollständig: nachzutragen sind vier verworfene Wege und eine Arbeitsregel
in `konzept.md` § 5 (Vollautomatik, Skill „abi-heft-erfassen", Parallelarbeit
im Klon), zwei nie beantwortete Punkte in § 6 (Koordinaten mit „|" in msa,
Arbeitszeit GK 285/255 min), die Zahlen je Profil und der `typ_neben`-Befund
in § 4 bei den Entscheidungen 1 und 25, die Berichtigung 49 → 37 in den
Entscheidungen 4 und 9 samt neuem Quellenverweis auf `fhr-typenbibliothek.md`
statt auf `fhr.md` § 9, die `beispiel_id`-Regel
in `katalog-prompt.md` und der Rundschreiben-Befund in `abi.md`, sofern er
dort nicht schon steht.
