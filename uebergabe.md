# Übergabe verbessereBlaetter – 2026-10-01c (Chat 01.10. abends)

Vorherige Übergabe: archiv/uebergabe-2026-10-01b.md.

## 1 Ziel

Der bestmögliche Themenkatalog, die Aufgabenbank und die Prompts,
damit aus wenigen Wörtern druckfertige Blätter entstehen – schnell
und günstig, Qualität vor beidem (Lehrer 01.10.). Maßstab ist
ziel.md (28.09.) mit den Revisionen vom 01.10. (archiv/uebergabe-
2026-10-01.md § 4, dort noch nicht nachgetragen). Neu seit heute
abend: Vollständigkeit und richtige Reihenfolge der Aufgaben sind
für jeden Eintrag zu ermitteln und vom Lehrer zu bestätigen, bevor
weiter gebaut wird; nichts wird mehr nach hinten geschoben (Lehrer
01.10.: „ich will, dass Lücken oder ungeeignete Reihenfolge vorher
abgeräumt werden – überall, nicht nur Terme“).

## 2 Arbeitsgrundlage

- mathe-nachhilfe: `katalog/` 74 Einträge; `katalog/terme.md` sechs
  Einheiten (9e85c1e); Lehrwerksquellen für den Abgleich:
  `quellen/lehrwerke-inhalt-bericht-2026-09.md` (acht Reihen mit
  Inhaltsverzeichnissen aus der DNB), `quellen/lehrwerke-fundliste.md`,
  `quellen/altlehrwerke-formen.md` (DDR-Bände, nach Eintrag
  gegliedert, bisher nur auf Form gelesen), `quellen/altlehrwerke-
  fundliste.md`; `befund-schwach-blatt-2026-09-24.md`,
  `befund-foerderhefte-2026-09-24.md`.
- aufgabenbank: Bank terme auf sechs Einheiten, 369 Zeilen, Mappe
  auf 9e85c1e (Commits 5e8baab…4493f71); `bank.md` sechste Fassung
  (Feld `herkunft`); `werkzeuge/bank-pruef.py` v0.13b; Eingänge
  `eingang/terme-2026-10-01` bis `-01d` (vier Blätter, Protokolle
  mit Übernahmeblöcken); `zusammenbau.py` v1.2 (kennt Muster 4
  nicht); `bau/terme/muster-2026-10-01/muster4.tex` Zielblatt.
- blattbau: `bankblatt.md` v5.3 (dde10c7, f5c60a1) = Projekt-
  anweisung in erzeugeBlatt(Bank); `pruefungsblatt.md` v0.15 (nie im
  Register, nicht an die Bank angebunden); CHANGELOG mit v5.0–5.3.
- anweisungen: `projekt-verbessereBlaetter.md` 2026-10-01 – darin
  ist die Schreibrecht-Erklärung überholt (siehe § 4); Nachzug als
  Datei in diesem Umzug.

## 3 Arbeitsstand

Erledigt 01.10. abends:
- Schreibweg geklärt: Nicht der Sitzungsstart entscheidet, sondern
  der Berechtigungsmodus. Auf „Auto“ lehnt der Filter das Anhängen
  eines Repos ab; auf „Manuell“ fragt eine Karte, ein Klick, danach
  schreibt der Chat und jeder Agent aus ihm (gemessen an drei
  Repos). Patch-Weg über den Rechner nur noch Rückfall.
- Kette Blatt-Chat → Bank steht: v5.1 legt Blatt und Erfindungen in
  `eingang/`, v5.2 hängt das Repo als ersten Schritt an und
  übernimmt die Erfindungen selbst in die Bank (Option A, Lehrer),
  v5.3 hat den Abschnitt „schwach“ (Formregeln aus ziel.md § 2).
- Bank-Nachzug Terme (Opus-Agent, 0,35 Mio): 239 → 354 Zeilen,
  31 aus Blatt 1, dann 15 aus Blatt 2 → 369; 0 Abweichungen.
- Vier Blätter Terme gebaut (alle auf Fable, nicht Opus):
  Regelfall v5.1 (101 Teilaufgaben, 32 neu), schwach v5.1 (138, 26
  neu), Regelfall v5.1 (93, 36 neu), schwach v5.3 (23 Seiten, 169,
  20 neu, 17 davon Dubletten). Befunde in § 5.
- Messwerte: Woche 68 %, Fable 69 % (abends, vor dem letzten
  Agenten); Anzeige rechnet „leer am Samstag“ hoch.

Nicht erledigt: alles in § 6; Prüfungsheft; Skript auf Muster 4;
Nachzug der 48; ziel.md-Revisionen; Verweise auf alte Terme-Nummern.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter, soweit hier nichts anderes steht.

- Vor dem Bauen: Für jeden Katalogeintrag werden Vollständigkeit
  (nichts fehlt, was Lehrwerke, DDR-Bände, RLP und Prüfungen üben)
  und Reihenfolge der Sprossen ermittelt und vom Lehrer bestätigt;
  erst danach füllt die Bank den Eintrag. Das ist ein fester Schritt
  der Katalog-Prüfliste, kein Posten in faellig.md. Die Nachzüge
  der 48 Einträge warten darauf. (Lehrer 01.10. abends.)
- Schreibrecht: Werkstatt- und Blatt-Chats laufen im
  Berechtigungsmodus „Manuell“, bis die Repo-Karte bestätigt ist;
  danach darf der Modus zurück auf „Auto“. Ersetzt die Regel
  „Repo beim Start wählen“ (01.10. mittags).
- Übernahme ohne Rückfrage: Der Blatt-Chat trägt seine Erfindungen
  selbst in die Bank ein (Prüfskript, Dubletten, Sprosse, Feld
  herkunft); der Lehrer streicht, was ihm auf dem Blatt nicht
  gefällt. Die Regel „Lehrer sagt ja vor der Übernahme“ ist
  aufgehoben (Option A, Lehrer 01.10.).
- Eingangsordner: `eingang/<eintrag>-<datum>/` ist Beleg (PDF,
  Quelltext, neu.jsonl, Protokoll), keine Quelle; Blätter werden
  dort nicht zur Bank.
- Blatt-Chats laufen mit Opus; heute liefen alle vier auf Fable
  (Protokoll), das zahlt doppelt.
- Kontingent: Rest der Woche nur Kleines; Großes ab Montag 18:00.
  Kein Zukauf.
- Modellwahl nächste Phase: Lehrwerks-Abgleich als Opus-Agenten in
  Schüben (Lesen ist der Kostentreiber: Inhaltsverzeichnisse, nicht
  Seiten); Urteil je Eintrag im Chat mit dem Lehrer.

## 5 Offene Punkte und Verworfenes

Befunde aus den vier Blättern (01.10.):
- Erfinden statt Suchen: Der Blatt-Chat erfindet Aufgaben, die die
  Bank an derselben Stufe hat (Blatt 3: 36 von 93 neu bei 369
  Bankzeilen; Blatt 4: 17 von 19 Erfindungen Dubletten). Regel für
  v5.4: je Sprosse zuerst alle Bankzeilen, erfinden nur bei leerer
  Sprosse oder wenn alle Zeilen schon auf dem Blatt stehen.
- „schwach“ v5.3 ergibt 23 Seiten: „keine Sprosse fällt weg“ mal
  „Dichte ein Drittel“. Darstellung neben Dezimalvorzahlen sinnlos,
  Rechenplatz ohne Bezug zur Schrittzahl. Vorschlag: schwach baut
  eine Einheit je Blatt (wie DZLM-Bausteine), Darstellung nur bei
  ganzzahligen Vorzahlen, Rechenplatz nach Schrittzahl; Lehrer
  entscheidet.
- Lücken im Katalog Terme gegen die DDR-Bände (altlehrwerke-formen.md,
  Abschnitt terme): Division von Produkten (10x : 5x), Division von
  Summen durch Monome, Beweisführungen mit Variablen, Umkehrformen
  („Ergänze den linken Term so, dass …“), Bruchterme (Gym 9). Grund:
  RLP, P10 und LISUM nennen Division nicht; die DDR-Bände wurden nur
  auf Form gelesen. Gilt vermutlich für weitere Einträge → § 6.
- Lage der Prüfungssprosse: Katalog Terme stellt sie in vier Ketten
  vor GYM- und Abschluss-Sprossen, bank.md verlangt sie als letzte;
  der Agent folgte bank.md. Entscheidung offen (zwei Optionen:
  Katalog ändern oder bank.md „Prüfungssprosse = letzte“ lockern).
- Eingänge ohne Übernahme: `eingang/terme-2026-10-01c/neu.jsonl`
  (36 Zeilen, v5.1) ist nicht übernommen; nach dem Abgleich (§ 6)
  prüfen, nicht vorher (sonst Dubletten).
- bank.md: Prüfungshöhe mitten in der Kette; e3 k3/k4 Grundfälle
  ohne Päckchen; Einheit 5 ohne Pflichtelemente (stand.md terme).
- Prüfungsheft: pruefungsblatt.md v0.15 baut aus dem Prüfungs-
  katalog, nie gelaufen; nach ziel.md § 4 künftig Zusatz am
  Bank-Prompt (Prüfungssprossen und Originale in Heftform).
  Gespräch mit dem Lehrer steht aus (nach diesem Umzug gewünscht).
- Alte Posten bleiben: Skript v1.2 auf Muster 4; Verweise auf alte
  Terme-Nummern (Sonnet); marken-bau.py terme; ziel.md-Revisionen;
  Projektdateien in erzeugeBlatt(Bank) (Annahme: liegen, nicht
  bestätigt); K2–K7; Gegenlese; kandidaten-Durchsicht.
- Zwei Hilfszweige `_messtest` in mathe-nachhilfe und aufgabenbank
  (Löschen aus der Sitzung nicht erlaubt); der Lehrer kann sie auf
  GitHub löschen.

Verworfen heute: Patch-Weg als Regelweg (Dialoge je Commit);
nächtliche Sammelübernahme (Option B – Zeitverzug, Cloud-Guthaben
ungemessen); Vorab-Füllen der Bank nach Themenplan (25 Schüler,
Bedarf unbekannt – die Bank wächst mit den Blättern).

## 6 Nächster Arbeitsschritt

1. Abgleich Vollständigkeit und Reihenfolge, alle 74 Einträge, in
   Schüben ab Montag 18:00 (Opus-Agenten, je Schub etwa zehn
   Einträge): Quellen sind die Inhaltsverzeichnisse der acht
   Lehrwerksreihen (lehrwerke-inhalt-bericht-2026-09.md, DNB-
   Verzeichnisse d-nb.info/<IDN>/04), die DDR-Bände (altlehrwerke-
   formen.md, -fundliste.md), RLP-Zeilen und Prüfungskatalog. Je
   Eintrag eine Datei `katalog/_abgleich-<eintrag>.md`: Tabelle
   „im Lehrwerk, nicht im Katalog“ mit Quelle und Vorschlag
   (Sprosse, Einheit, Stelle), Tabelle „Reihenfolge weicht ab“ mit
   Begründung, Tabelle „im Katalog, in keiner Quelle“. Der Chat
   erzählt dem Lehrer je Eintrag in wenigen Sätzen, was dem Schüler
   fehlen würde; der Lehrer bestätigt je Zeile; dann Katalog
   nachziehen, dann Bank. Beginn mit terme (Division u. a., § 5),
   dann die Einträge mit Blättern (prozentrechnung, daten,
   quadratische-gleichungen), dann der Rest.
2. Zugleich, klein: bankblatt.md v5.4 (Bank vor Erfinden; schwach
   je Einheit, falls der Lehrer zustimmt) – Block für
   erzeugeBlatt(Bank) und Commit nach blattbau.
3. Danach Gespräch Prüfungsheft (§ 5), dann Skript auf Muster 4.
