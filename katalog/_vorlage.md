# [Thema]
Status: leer · Stufe: [Sek I / GOST / FOS] · Bildungsgänge: [...] · gegengelesen: nein
(Werte seit 10f: `nein` · `bis auf [FS]` · `ja`. Der mittlere Wert heißt: die Gegenlese ist durch, es fehlt nur noch der Abgleich der Kasten-Abschnittsverweise mit der Formelsammlung, geführt in `_formelsammlung.md`.)

### Verortung
[Klassen, RLP-Niveaustufen mit Zitat der Inhaltszeile, Leitidee, Lehrwerkskapitel mit Lerneinheiten und Stunden] [RLP] [LS]

### Lerneinheiten
1. [Name – Inhalt in einem Satz] (Kl.) ← Eingabe „[stichwort]" · Gewicht: [Kern/Rand] – [Halbsatz mit Beleg oder Grund] (ohne Marke keine Gewicht-Angabe)
2. …
(Gewicht seit 02.10.2026 abends, konzept.md Entscheidung 38: eine Marke, keine Zahlen. Kern – die Prüfung verlangt die Einheit (P10 bei Sek I, Abitur/FHR bei Sek II), als eigener Typ oder als Schritt im Lösungsweg von Originalen anderer Einträge; der Halbsatz nennt den Beleg knapp („in der P10 als eigener Typ“, „im Lösungsweg der P10-Parabelaufgaben“). Rand – die Einheit ist ganz Vorrat oder nur Gymnasium und hat keinen Prüfungsbezug; der Halbsatz nennt den Grund. Alles andere bekommt keine Marke (Unterrichtsgrundlagen ohne eigenen Prüfungstyp sind nicht Rand). Belege: Abschnitt „Prüfungsform“, für den Lösungsweg die Felder verfahren und schritte der Prüfungskataloge (per Skript durchsuchen); die Zählungen in `_gewicht/` sind Beleg, kein Pflichtmaß. Blattregel: Wo Zweige nicht aufeinander aufbauen, stehen Kern-Zweige vorn, Rand-Zweige am Ende; innerhalb einer Kette bleibt die Leiter. Die Marke ordnet, sie streicht nichts; der Lehrer korrigiert eine falsche Marke auf Zuruf.)
Blattfolge: n, n, … (optional; Reihenfolge der Einheiten auf dem Lernblatt; fehlt sie, gilt die Katalogreihenfolge)
Eingabe „[thema]" ohne Zusatz → [Dialog / direkt Einheit n].

### Lernweg
Je Lerneinheit ein Block, entsteht beim Bau nach aufgabenbank
`bau/bauauftrag.md` (plan.md, 09.10.2026); fehlt er, ist die Einheit noch
nicht gebaut.

#### Lerneinheit <n> – <Name in Schülersprache>
Stand: <Datum> · Kennung <K> · Kritiker: <durch/Befunde> · Lehrer: <–/Stichprobe gut>
Ziel: <Prüfungsaufgabe oder Höhe, auf die der Weg führt>

| Schritt | Was der Schüler begreift | Stolperstelle | Aufgaben (Bank-ids, erste = Regel, weitere = neue Zahlen) |
|---|---|---|---|
| L<n>-1 | … | … | id, id |

### Typen je Lerneinheit
Einheit 1: [Typ · Typ · … in Lehrbuchreihenfolge; Fehler finden · Begründen am Ende]
Einheit 2: …

### Voraussetzungen (Blatt 0)
Fertigkeiten:
- [Fertigkeit – wofür (Einheit)] [Quelle]
Erkennungsschritte (Vorstufe, eigene Aufgabe auf Blatt 0, eine Anweisung je Aufgabe):
- [„Anweisung" – vor Einheit n]

### Merkkasten
Einheit n:
    [Name der Regel]: [Regel in einem Satz Schülersprache]      [1–3 Zahlenbeispiele]
    Formelsammlung: [Abschnitt] [FS]
Quelle: [Serlo-URL], sinngemäß.

### Typische Fehler
- [Fehler mit Beispiel] [Quelle]

### Für schwache Schüler
Mindeststoff (D/E) [RLP]: [welche Einheiten/Typen]
Grundvorstellung (Blatt 0) [MO, INKL]: [eine Aufgabe, die die Vorstellung prüft, nicht die Fertigkeit]
Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [INKL, LS, FD]:
- [Typ]: Grundfall (4×) → [Merkmal] → [Merkmal] → … → Rückwärts: [...] → Gemischt: [...] → Prüfungshöhe: [...]
Leiterregeln (seit 02.10.2026, konzept.md Entscheidung 38): Jede Kette hat vor der Prüfungshöhe eine Rückwärtssprosse (vom Ergebnis zur Aufgabe: Gleichung aus Lösungen bilden, Größe aus dem Ergebnis zurückrechnen, Term zu einer gegebenen Eigenschaft wählen) und eine Mischsprosse (Aufgaben ohne Vorsortierung – der Schüler entscheidet, welches Verfahren oder welcher Fall vorliegt). Krumme Zahlen (Dezimal, Bruch, negativ, gemischte Einheiten) stehen auf den oberen Sprossen, für alle Schüler und ohne [GYM]; unten bleiben die Zahlen glatt. Sparsam (Lehrer 02.10.): je Kette höchstens eine Sprosse mit krummen Zahlen am Ende der Kette, auf dem Blatt eine Aufgabe daraus; die Bank hält die Sollmenge als Auswahl; auf dem Blatt „schwach“ nur auf Zuruf. Hat der Typ keine sinnvolle Umkehrung, steht unter „Offene Punkte“ eine Zeile mit Grund statt einer erzwungenen Sprosse.
Marken an einer Sprosse: „(Vorrat)“ heißt: nicht Mindeststoff (Prüfliste unten). „(kein P10-Stoff)“ heißt: regulärer Schulstoff, nicht Teil der P10-Vorbereitung; das Prüfungsheft lässt die Sprosse aus, das Unterrichtsblatt führt sie (Entscheidung 30.09.2026, binomische-formeln.md Einheit 2, dritte Formel).

### Prüfungsform
[P10-Typen aus typen.csv mit Zuordnung zu Einheiten; bei GOST: IQB-Pool/Prüfungsschwerpunkte; bei FOS: FHR-Schwerpunkte]
Zuordnung: Einheit 1 – [Typname, Typname]; Einheit 2 – [Typname]; Einheit 3 – kein Typ; …
(Pflichtzeile, von `_pruef_struktur.py` erzwungen. Typnamen wörtlich aus typen.csv. **Jede** Einheit des Eintrags muss vorkommen – Einheiten ohne Typ ausdrücklich als „kein Typ“; Sammelformen wie „Einheit 2 bis 4 – kein Typ“ sind erlaubt. Seit 10g prüft das Skript auch die Vollständigkeit, vorher nur, dass die Zeile da ist.)
Zielmarke: Einheit 1 – [Prüfungshöhe in einem Satz, mit Original-id]; Einheit 2 – … ; für Einheiten ohne Original: „kein P10-Original; Marke nach RLP [Stufe] und LISUM-PH Jg. [n]“ mit der belegenden Zeile.
(Pflichtzeile. Seit 10h gilt: Die Prosa über der Zuordnungszeile und die Zuordnungszeile selbst müssen dasselbe sagen – wo ein Typ in einer anderen Datei liegt oder ein Original von einer anderen Datei geführt wird, gehört der Verweis in beide. Führt ein Eintrag einen Typ nur mit, weil typen.csv ihn seinem Thema zuweist, während Lerneinheit und Kette woanders stehen, schreibt er das ausdrücklich als „keiner Einheit dieses Eintrags zugeordnet“ – sonst lesen sich zwei Dateien wie zwei Besitzansprüche auf denselben Typ.)

### Offene Punkte des Eintrags
- [alles, was [FD]/[FS]/[MO] trägt oder unverifiziert ist]

## Prüfliste (vor Status „gegengelesen")
- [ ] Jeder Verfahrenstyp hat Sprossen; Grundfall zuerst, Prüfungshöhe zuletzt, je Sprosse ein Merkmal.
- [ ] Rückwärts- und Mischsprosse je Kette vor der Prüfungshöhe (oder Grund unter „Offene Punkte“); krumme Zahlen sparsam am Ende der Kette (höchstens eine Sprosse); Gewicht je Einheit: Kern oder Rand mit Halbsatz, sonst keine Marke (Regel 02.10.2026 abends).
- [ ] Kastenzahlen kommen in keiner Sprosse und keinem Beispiel vor.
- [ ] Mindeststoff (D/E) markiert; Rest ist Vorrat.
- [ ] Grundvorstellungs-Aufgabe für Blatt 0 vorhanden.
- [ ] Jeder Prüfungstyp einer Lerneinheit zugeordnet.
- [ ] Jedes Original des Themas kommt **in diesem Eintrag** vor, **mit seiner id in der Prüfungsform** und nicht nur als Beschreibung (10j), und jeder Typ hat wenigstens ein Hauptoriginal – sonst ausdrücklich vermerken (seit 10h; `_pruef_struktur.py` zählt die Lücke als Kennzahl 5, `-v` listet die ids). Seit 10i zählt Kennzahl 6 zusätzlich die Originale, die zwar irgendwo, aber nicht in der Datei ihres CSV-Themas stehen – eine Nennung in einer Fehlerzeile eines fremden Eintrags genügt Kennzahl 5, aber nicht der Gliederungsregel.
- [ ] Kein Verlagstext übernommen; Serlo/ZUM mit Quellenzeile.
- [ ] Notation Berlin-Brandenburg (f(x) = m·x + n, Strich, wA/fA).
- [ ] [FD]/[FS]/[MO]-Angaben in „Offene Punkte" gelistet.

## Gliederungsregeln (beschlossen 2026-09-08, Thema Prozentrechnung)
- Stufe-D-Stoff, der in Berlin/Brandenburg Grundschule ist, für die Oberschule 7–8 aber regulär (Index: D–E), ist eine eigene Lerneinheit mit Blatt 0 und Hauptblatt – nicht Blatt-0-Stoff der nächsten Einheit. Blatt 0 bleibt bei Fertigkeiten, Erkennungsschritten und Grundvorstellung, je eine Aufgabe.
- Jede Lerneinheit steht in genau einer Datei; andere Einträge verweisen (Zinsen → zinsrechnung.md, Dreisatz → zuordnungen.md, Prozent als Anteil → prozentrechnung.md). Ein P10-Typ gehört zur Datei seines Themas in typen.csv.
- Weicht das CSV-Thema eines Originals vom typen.csv-Thema seines Typs ab, bestimmt typen.csv die Datei des Typs, das Original wird bei seinem CSV-Thema geführt, und die Datei des Typs nennt es in einer Klausel ihrer Prüfungsform. Die vollständige Fallliste steht in `index.md`, ebenso die maschinenlesbare Zuordnung CSV-Thema → Datei, aus der Kennzahl 6 rechnet. Die Regel gilt in beide Richtungen und wird auch dann angewendet, wenn der Typ dadurch kein Original in der eigenen Prüfungsform behält (zuordnungen.md Einheit 1 seit 10g, „Mantelfläche Prisma berechnen“ seit 10h).

## Arbeitsablauf je Thema (Kopie aus index.md)
1 RLP-Zeilen des Themas zitieren (Stufe, Mindeststoff) · 2 Stoffverteilungsplan Lehrwerk: Lerneinheiten, Reihenfolge · 3 LISUM-Planungshilfen (aus `quellen/`, kein neuer Abruf): Zeitumfang, Jahrgang, Differenzierungsform, Standardbeispiele, Begriffe – Reihenliste über `grep -n "^ \+Jahrgangsstufe .*Mathematik: "` (einundzwanzig Reihen; ein Muster mit vier festen Leerzeichen übersieht eine), Wortsuchen und jedes Nulltreffer-Protokoll über `_suche_quelle.py`, weil die zweispaltige Textfassung getrennte Wörter sonst als Nulltreffer meldet; Suchwortliste vor der Suche aufschreiben und vollständig ins Protokoll übernehmen · 4 Förderheft/Inklusionsmaterial: Sprossen, Grundvorstellung · 5 Serlo/ZUM: Merkkasten · 6 Formelsammlung: Notation, Abschnitt · 7 Prüfungsquelle: Typen je Einheit; je Typ die vollständige Liste seiner Haupt- **und** Nebentyp-Originale ziehen und gegen den Eintrag halten (seit 10h) – dabei das Feld `typ_neben` am **senkrechten Strich** trennen, nicht am Komma, sonst bleiben die 24 Originale mit mehreren Nebentypen stumm unentdeckt (Befund 10i); meldet ein Auszug über mehrere Originale null Nebentypen, ist das ein Verdachtsfall und kein Ergebnis ; wo ein Original oder ein Typ in einer anderen Datei liegt, die Klausel in **beide** Einträge schreiben – Kennzahl 6 prüft die Datei, nicht die Klausel (10j) · 8 Fachdidaktik: Fehler · 9 Prüfliste (Kastenzahlen und P10-Zuordnung mit `_pruef_katalog.py`, Struktur mit `_pruef_struktur.py`) · 10 offene Punkte des Eintrags durch das Prüfraster ziehen (Kiste D in `_fragen.md`); was danach eine echte Entscheidungsfrage bleibt, kommt zusätzlich als Marke ins Register `_fragen.md` · 11 Status setzen, Quellenprotokoll in `_quellenprotokoll.md` ergänzen.

Prüfraster vor jeder neuen Frage (Kiste D in `_fragen.md`): 1. Steht im Eintrag schon eine Wahl, an die nur ein „klären“ angehängt wurde? 2. Steht die Regel schon unter Abschnitt 4 der Übergabe? 3. Geht es um Belegtiefe statt um Richtigkeit? 4. Setzt die Frage eine Arbeitsteilung Katalog/Prompt voraus, die so nicht beschlossen ist? Viermal nein – dann ist es eine echte Frage.
