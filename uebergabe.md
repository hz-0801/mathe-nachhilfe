# Übergabe 2026-09-19b

## 1 Ziel

Ein geprüfter Themenkatalog, aus dem Unterrichtsblatt- und
Prüfungsblatt-Prompt Arbeitsblätter bauen, statt je Thema selbst zu
planen. Sek I liegt vor; Sek II folgt über die Prüfungskataloge fhr, abi
und iqb, verbunden durch die Themenkonkordanz. Der Lehrer erledigt jetzt
das Zeitintensive und Formunabhängige; der Testlauf mit einem gebauten
Blatt ist bewusst verschoben.

## 2 Arbeitsgrundlage

- GitHub `hz-0801/mathe-nachhilfe`, Commit a84231a (19.09.2026). Ordner
  `msa/`, `fhr/`, `abitur/` (abi und iqb), `katalog/` (Themenkatalog
  Sek I, 29 Einträge, Stand 11j), `quellen/`, `werkzeuge/`, `archiv/`.
  Wurzel: `README.md` (einzige Landkarte), `CLAUDE.md`,
  `katalog-prompt.md`, `konzept.md`, `blatt-konzept.md`, `faellig.md`,
  `themen.csv` (neu).
- `themen.csv` – Themenkonkordanz, lange Form: je Zeile ein Profilthema
  (kanonisch, stufe, profil, leitidee, thema, zeilen, typen, bemerkung).
  73 kanonische Themen: 31 Sek I (29 Katalogdateien plus
  `funktionen-allgemein` und `kombinatorik` ohne Datei), 42 Sek II.
  Prüfung: `python werkzeuge/themen-pruef.py` nach jeder Katalogänderung.
- `werkzeuge/themen-inventar.md` – gezähltes Inventar aller Themennamen
  je Profil; abgeleitet, Vorstufe der Konkordanz.
- GitHub `hz-0801/blattbau`, Commit 0e1ec2d: `unterrichtsblatt.md`
  (vorher masterprompt), `pruefungsblatt.md` (vorher pruefungsprompt),
  `mathblatt.sty`, Anleitung, Changelog.
- Prüfungskataloge (Zeilen / Themen, aus den Katalogen gezählt):
  msa 393 / 32 (Basis und Kontext zusammen), fhr 253 / 28, abi 794 / 44,
  iqb 1443 / 47.
- Claude Code im Code-Tab der Desktop-App, Ordner `mathe-nachhilfe`,
  Modell Opus; Aufträge als Textblock nach dem Muster der
  Projektanweisung, GitHub Desktop für Push.

## 3 Arbeitsstand

Stufe 0 abgeschlossen. Themeninventar gebaut (Commit 84e0cf1),
Konkordanz im Chat entschieden, `themen.csv` eingespielt und mit
`themen-pruef.py` gegen die Kataloge geprüft (vier Prüfungen bestanden,
Gegenprobe mit verfälschter Kopie schlägt an). `konzept.md` § 3 hat einen
Schlussabsatz zur Konkordanz und zur Sek-I/II-Regel. README ergänzt.

Befund aus dem Inventar: abi und iqb sind über `abitur-vokabular.md`
schon konkordant (43 von 44 abi-Themen wortgleich in iqb); die eigentliche
Arbeit war fhr → abitur-Vokabular (28 → 12) und msa → `katalog/`
(32 → 24).

Arbeitsfluss geändert: Aufträge gehen als ein Textblock samt Datendateien
in den Code-Tab; keine Downloads, kein Ziehen. Projektanweisung und
globale Anweisung entsprechend angepasst (Textblock, Zeilen ≤ 72 Zeichen,
Endzeile nach jedem Block, geänderte Aufträge immer vollständig).

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Reihenfolge des Lehrers vom 19.09.: erst Prüfungskataloge,
  Themenkonkordanz, Rohdateien je Thema; formabhängige Arbeit (fertige
  Sek-II-Einträge, Kastenform) später. Testlauf verschoben; nicht wieder
  darauf drängen.
- Themenkatalog ist Stoffbeschreibung, kein Bauplan (`konzept.md` § 3).
  Ein Eintrag je Thema, prüfungsartübergreifend.
- Konkordanz-Regel: Ein Sek-I-Thema ist kanonisch, wenn Sek II denselben
  Stoff fortführt (daten, wahrscheinlichkeit, lineare-gleichungssysteme,
  kombinatorik); ein Sek-II-Thema bleibt eigen, wenn es ein neues Konzept
  einführt (Binomialverteilung, Bayes, Unabhängigkeit, Hypothesentest).
  Namensreferenz Sek I: Dateinamen in `katalog/`; Sek II:
  `abitur/abitur-vokabular.md`. Lange Form, Zahlen aus den Katalogen.
- `themen.csv` wird nur über Chat-Entscheidung geändert; Claude Code
  prüft, ändert nicht.
- Ermessensfälle der Konkordanz stehen in Spalte `bemerkung`; die drei
  mit Gewicht: `wahrscheinlichkeit` fasst 11 Profilthemen; fhr „Größen und
  Einheiten" → `einheiten` trotz gemischter Typen; fhr „Körpervolumen aus
  Grundfläche und Länge" → `flaecheninhalt-durch-integration`.
- Repo-Struktur, Landkarte-Regel, lokale Ausgabeordner: wie 19a.
- Formelsammlung, Kastenkriterium, LISUM-Nachfolger, kommerzielle
  Nutzung: wie 19a, unverändert.
- Modelle: Fable für Urteilsarbeit im Chat (der Lehrer schaltet es im
  Modellwähler um), Opus für Claude Code.

## 5 Offene Punkte und verworfene Ansätze

Offen, Lehrer:

1. Kastenform (Abschnittsverweis, Zahlenbeispiele, Nachschlagewerk oder
   Merkhilfe; Folgen für `_formelsammlung.md` und [FS]).
2. Mechanik-Punkte Sek I (A4 breit/eng, Prüflisten, Zeilen 10 und 11).
3. IQB-Regel für Brandenburg und FHR belegen (vor dem Sek-II-Schritt).

Offen, Werkstatt:

4. Themenebene ist zu grob, wo `katalog/` feiner schneidet als der msa:
   `kreis`, `pyramide-kegel-kugel`, `bruchrechnung`, `binomische-formeln`,
   `strahlensaetze`, `reelle-zahlen`, `trigonometrische-funktionen` haben
   kein Profilthema; ihre Aufgaben stecken in `flaechen`, `koerper`,
   `terme` und anderen. Das Rohdatei-Skript muss dort über `typ` oder
   `stichwoerter` filtern; Regel noch nicht festgelegt.
5. `funktionen-allgemein` und `kombinatorik` haben keine Katalogdatei –
   Lücke im Themenkatalog, entscheiden, ob Einträge entstehen.
6. Zwei Themen stehen nur in Typenlisten, nicht in Katalogen (fhr
   „Grundlagen / Gleichungen lösen", abitur „Analysis / Lineare
   Gleichungssysteme", beide nur typ_neben); nicht in `themen.csv`.
7. MzDuF-Download nicht gefunden; `katalog/_quellen.md` alter Name der
   Planungshilfen; Cornelsen unter [FS] unbelegt – wie 19a.

Verworfen:

- Skript schlägt Zusammenführungen vor – Namen ohne Stringähnlichkeit,
  Urteilsarbeit gehört in den Chat.
- Typenzahl je Profil aus den Typenlisten – `abitur-typen.csv` trennt abi
  und iqb nicht; aus den Katalogen gezählt.
- Breite Form der Konkordanz – Aliasfelder mehrwertig, jedes Skript müsste
  sie zerlegen.
- Sek-II-Themen durchgehend eigen – widerspricht `konzept.md` § 3.
- Aufträge als Datei zum Ziehen – ersetzt durch Textblock.
- Weitere aus 19a: P10-Formelblatt, Erklärquellen neben Serlo, Kasten nur
  bei vergessbarer Formel, Trennung Bruchaddition/-multiplikation, eigener
  Themenkatalog je Prüfungsart, Shell-Skript zum Einspielen.

## 6 Nächster Arbeitsschritt

Stufe 1, Rohdatei je Thema. Zuerst im Chat festlegen, was eine Rohdatei
ist: welche Katalogfelder je Zeile, Ordnung (Profil, Jahr, Typ), ob die
Typendefinitionen aus den Typenlisten dazukommen, Ablageort (lokal wie
`baende/` oder im Repo), und die Filterregel für Punkt 4. Dann ein
Auftrag: `werkzeuge/rohdatei-bau.py` liest `themen.csv` und die fünf
Kataloge und schreibt je kanonischem Thema eine Markdown-Datei. Erst
danach Sek-II-Einträge.
