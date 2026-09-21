# -*- coding: utf-8 -*-
"""
tragfaehigkeit.py v0.1 · 21.09.2026 · Tragfähigkeit der Themen aus den Blatt-0-Abschnitten

Der Katalog misst bisher nur Prüfungslast (Zeilen je Thema, themen.csv). Eine
zweite, davon unabhängige Achse ist die Tragfähigkeit: wie oft ein Thema von
anderen Einträgen unter „### Voraussetzungen (Blatt 0)“ gebraucht wird. Themen
mit hoher Tragfähigkeit und niedriger Last werden nie Stundenthema, kosten aber
Zeit in jeder Stunde, in der sie fehlen – für den Blattbau ist das die
Reihenfolgefrage (Auftrag Tragfähigkeit, 21.09.2026).

Was gezählt wird: je Eintrag katalog/*.md (ohne _* und index.md) der Abschnitt
„### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift; darin jeder
Verweis der Form <name>.md, mit oder ohne Einheitsangabe („kombinatorik.md
Einheit 2“). Ein Eintrag zählt je genanntem Thema einmal, gleich wie oft er es
nennt. Selbstverweise zählen nicht. Verweise auf Dateien, die kein
Katalogeintrag sind, werden gesammelt und getrennt ausgewiesen, nicht
verworfen. Keine Gewichtung (nicht nach Einheit, nicht nach Profil).

Was die Messung nicht sieht: Sie misst, was in unseren Blatt-0-Abschnitten
steht, also die eigene Schreibsorgfalt, nicht den Unterricht. Nennt ein Eintrag
seine Voraussetzungen in Wortform („[Thema Lineare Gleichungen, Einheit 2]“,
die Form der Sek-I-Einträge der ersten Bauphase), zählt hier nichts. Deshalb
weist die Ausgabe die Messlücken aus, und _pruef_struktur.py führt ihre Größe
als Kennzahl 7 (Einträge ohne Verweis in Blatt 0; importiert messe() von hier).

Schreibt katalog/_tragfaehigkeit.md:
  Kopf        – Stand-Zeile (Datum, kurzer Hash des HEAD-Commits), Zählregel.
  Tabelle A   – Nachfrage: Thema, Zahl der Einträge, die es voraussetzen, eigene
                Katalogzeilen (Summe der Spalte zeilen in themen.csv), Namen der
                Nachfrager; absteigend, bei Gleichstand alphabetisch; alle Einträge,
                auch die ohne Nachfrage.
  Tabelle B   – Einstiegshürde: Thema, Zahl seiner eigenen Voraussetzungen und
                ihre Namen; nur Einträge mit mindestens einem Verweis – für die
                übrigen ist die Hürde nicht null, sondern ungemessen (Messlücken).
  Messlücken  – Einträge ohne Verweis im Blatt-0-Abschnitt (mit der Zahl ihrer
                Nennungen in Wortform als Hinweis), Einträge ohne Abschnitt,
                Verweise auf Dateien, die kein Katalogeintrag sind.
  Absatz      – die Schwäche der Messung.
Zwei Läufe hintereinander erzeugen dieselbe Datei bis auf die Stand-Zeile.
Ändert keinen Katalogeintrag – Lücken werden berichtet, nicht gestopft.

Aufruf aus der Repo-Wurzel (nach jeder Katalogänderung, vor dem Commit):
  python werkzeuge/tragfaehigkeit.py
"""
import collections
import csv
import datetime
import io
import os
import re
import subprocess
import sys

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Wurzel; Skript liegt in werkzeuge/
VERSION = "tragfaehigkeit.py v0.1"
KATALOG_ORDNER = "katalog"
KONKORDANZ = "themen.csv"
AUSGABE = "_tragfaehigkeit.md"  # in katalog/
ABSCHNITT = re.compile(r"^### Voraussetzungen \(Blatt 0\)[^\n]*\n(.*?)(?=^### |^## |\Z)", re.S | re.M)
# <name>.md, auch in Klammern oder Backticks; ein Pfad davor (rohdaten/x.md) wird mitgenommen und macht
# den Verweis zu einem Nicht-Katalogverweis.
VERWEIS = re.compile(r"(?<![\w.-])((?:[\w.-]+/)*)([A-Za-z0-9_][\w-]*)\.md\b")
# Heuristik für Nennungen in Wortform: das Wort „Thema“ vor einem großgeschriebenen Themennamen
# („[Thema Lineare Gleichungen, Einheit 2]“); Dateiverweise sind kleingeschrieben und treffen nicht.
WORTFORM = re.compile(r"(?<![\w-])Thema [A-ZÄÖÜ]")


def eintraege(katalog):
    """Dateinamen ohne .md aller Einträge: katalog/*.md ohne führenden Unterstrich und ohne index.md."""
    return sorted(n[:-3] for n in os.listdir(katalog)
                  if n.endswith(".md") and not n.startswith("_") and n != "index.md")


def blatt0(text):
    """Text des Abschnitts „### Voraussetzungen (Blatt 0)“ oder None, wenn der Eintrag ihn nicht hat."""
    m = ABSCHNITT.search(text)
    return m.group(1) if m else None


def zeilen_je_thema(pfad):
    """kanonisch -> Summe der Spalte zeilen aus themen.csv (Prüfungslast); None, wenn die Datei fehlt."""
    if not os.path.exists(pfad):
        return None
    summe = collections.Counter()
    with io.open(pfad, encoding="utf-8-sig", newline="") as fh:
        for z in csv.DictReader(fh, delimiter=";"):
            summe[z["kanonisch"].strip()] += int(z["zeilen"] or 0)
    return summe


def messe(katalog, konkordanz=None):
    """Alle Größen der Messung als Wörterbuch; Listen und Mengen sortiert, damit die Ausgabe deterministisch ist.

    eintraege        – alle gemessenen Einträge
    nachfrage        – Thema -> sortierte Liste der Einträge, die es unter Blatt 0 nennen (ohne Selbstverweis)
    voraussetzungen  – Eintrag -> sortierte Liste der Themen, die er unter Blatt 0 nennt (nur Katalogeinträge)
    ohne_verweis     – Einträge mit Abschnitt, aber ohne einen Verweis auf einen anderen Katalogeintrag
    ohne_abschnitt   – Einträge ohne den Abschnitt
    unbekannt        – Verweisziel (wie geschrieben) -> sortierte Liste der Einträge, die es nennen
    wortform         – Eintrag -> Zahl der Nennungen in Wortform (Heuristik WORTFORM)
    zeilen           – Thema -> eigene Katalogzeilen aus themen.csv (None, wenn themen.csv fehlt)
    """
    namen = eintraege(katalog)
    vorhanden = set(namen)
    nachfrage = collections.defaultdict(set)
    voraussetzungen = {}
    unbekannt = collections.defaultdict(set)
    wortform = {}
    ohne_verweis, ohne_abschnitt = [], []
    for name in namen:
        with io.open(os.path.join(katalog, name + ".md"), encoding="utf-8") as fh:
            abschnitt = blatt0(fh.read())
        if abschnitt is None:
            ohne_abschnitt.append(name)
            continue
        wortform[name] = len(WORTFORM.findall(abschnitt))
        ziele = set()
        for pfad, ziel in VERWEIS.findall(abschnitt):
            if pfad or ziel not in vorhanden:
                unbekannt[pfad + ziel + ".md"].add(name)
            elif ziel != name:
                ziele.add(ziel)
        voraussetzungen[name] = sorted(ziele)
        if not ziele:
            ohne_verweis.append(name)
        for ziel in ziele:
            nachfrage[ziel].add(name)
    return {
        "eintraege": namen,
        "nachfrage": {t: sorted(q) for t, q in nachfrage.items()},
        "voraussetzungen": voraussetzungen,
        "ohne_verweis": ohne_verweis,
        "ohne_abschnitt": ohne_abschnitt,
        "unbekannt": {z: sorted(q) for z, q in unbekannt.items()},
        "wortform": wortform,
        "zeilen": zeilen_je_thema(konkordanz) if konkordanz else None,
    }


def tabelle_a(m):
    """[(thema, zahl_nachfrager, nachfrager)] absteigend nach Zahl, bei Gleichstand alphabetisch; alle Einträge."""
    reihen = [(t, len(m["nachfrage"].get(t, [])), m["nachfrage"].get(t, [])) for t in m["eintraege"]]
    return sorted(reihen, key=lambda r: (-r[1], r[0]))


def tabelle_b(m):
    """[(thema, zahl_voraussetzungen, voraussetzungen)] absteigend, bei Gleichstand alphabetisch; nur Einträge mit Verweis."""
    reihen = [(t, len(v), v) for t, v in m["voraussetzungen"].items() if v]
    return sorted(reihen, key=lambda r: (-r[1], r[0]))


def head_kurz():
    """Kurzer Hash des HEAD-Commits: git, sonst aus .git gelesen (git liegt hier nicht im PATH)."""
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=HIER, capture_output=True,
                              text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    try:
        head = io.open(os.path.join(HIER, ".git", "HEAD"), encoding="utf-8").read().strip()
        if head.startswith("ref: "):
            ref = head[5:]
            pfad = os.path.join(HIER, ".git", *ref.split("/"))
            if os.path.exists(pfad):
                return io.open(pfad, encoding="utf-8").read().strip()[:7]
            for zeile in io.open(os.path.join(HIER, ".git", "packed-refs"), encoding="utf-8"):
                if zeile.strip().endswith(" " + ref):
                    return zeile.split()[0][:7]
        return head[:7]
    except OSError:
        return "unbekannt"


NICHT_DURCHSUCHT = {"hefte", "hefte-md", "korpus", "baende", "iqb-pdf", "__pycache__"}  # lokal, nicht im Repo (.gitignore)


def fundort(dateiname):
    """Wo eine Datei liegt, die kein Katalogeintrag ist: Ordner relativ zur Wurzel, oder None."""
    basis = os.path.basename(dateiname)
    treffer = []
    for wurzel, ordner, dateien in os.walk(HIER):
        ordner[:] = sorted(o for o in ordner if not o.startswith(".") and o not in NICHT_DURCHSUCHT)
        if basis in dateien:
            treffer.append(os.path.relpath(wurzel, HIER).replace(os.sep, "/"))
    return sorted(treffer) or None


def baue(m, stand):
    """Text von _tragfaehigkeit.md."""
    n = len(m["eintraege"])
    a, b = tabelle_a(m), tabelle_b(m)
    zeilen = m["zeilen"]
    out = []
    w = out.append
    w("# Tragfähigkeit der Themen – Nachfrage in Blatt 0")
    w(f"Stand {stand}.")
    w(f"Erzeugt von `werkzeuge/{VERSION.replace(' ', '` (')}) aus den Blatt-0-Abschnitten der Einträge; "
      "abgeleitet, nie von Hand ändern. Der Katalog misst sonst nur Prüfungslast (Zeilen je Thema); "
      "hier steht die zweite Achse: wie oft ein Thema von anderen Einträgen gebraucht wird.")
    w("")
    w(f"Gemessen: {n} Einträge (`katalog/*.md` ohne `_*` und `index.md`); je Eintrag der Abschnitt "
      "„### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift, darin die Verweise der Form `<name>.md`, "
      "mit oder ohne Einheitsangabe. Ein Eintrag zählt je genanntem Thema einmal, gleich wie oft er es nennt; "
      "Selbstverweise zählen nicht; keine Gewichtung nach Einheit oder Profil. "
      "Zeilen = eigene Katalogzeilen, Summe der Spalte `zeilen` in `themen.csv` (Prüfungslast).")
    w("")
    w("## A Nachfrage – wie oft ein Thema vorausgesetzt wird")
    w("Absteigend nach der Zahl der nachfragenden Einträge, bei Gleichstand alphabetisch; alle Einträge, "
      "auch die ohne Nachfrage. Hohe Nachfrage bei niedriger Zeilenzahl heißt: das Thema wird nie Stundenthema, "
      "kostet aber Zeit in jeder Stunde, in der es fehlt.")
    w("")
    w("| Thema | Nachfrager | Zeilen | Nachfrager (Namen) |")
    w("|---|---|---|---|")
    for thema, zahl, quellen in a:
        z = "–" if zeilen is None else str(zeilen.get(thema, 0))
        w(f"| {thema} | {zahl} | {z} | {', '.join(quellen) or '–'} |")
    w("")
    w("## B Einstiegshürde – wie viele Themen ein Eintrag voraussetzt")
    w("Absteigend nach der Zahl der eigenen Voraussetzungen, bei Gleichstand alphabetisch – so viel muss ein "
      "Blatt 0 zu diesem Thema abdecken. Nur Einträge mit mindestens einem Verweis; für die "
      f"{len(m['ohne_verweis']) + len(m['ohne_abschnitt'])} übrigen ist die Hürde nicht null, sondern ungemessen "
      "(siehe Messlücken).")
    w("")
    w("| Thema | Voraussetzungen | Voraussetzungen (Namen) |")
    w("|---|---|---|")
    for thema, zahl, ziele in b:
        w(f"| {thema} | {zahl} | {', '.join(ziele)} |")
    w("")
    w("## Messlücken")
    w("Was die Messung nicht sieht – berichtet, nicht gestopft (kein Eintrag wird vom Werkzeug geändert).")
    w("")
    ov = m["ohne_verweis"]
    w(f"Einträge ohne Verweis der Form `<name>.md` im Blatt-0-Abschnitt: {len(ov)} von {n}. "
      "In Klammern die Nennungen in Wortform („Thema …“ vor einem Großbuchstaben, Heuristik) – "
      "die Nachfrage, die diese Einträge stellen, fehlt in Tabelle A ganz.")
    for name in ov:
        k = m["wortform"].get(name, 0)
        w(f"- {name} ({k} {'Nennung' if k == 1 else 'Nennungen'} in Wortform)")
    if not ov:
        w("- keine")
    gemischt = sorted((name, k) for name, k in m["wortform"].items() if k and name not in ov)
    w("")
    if gemischt:
        w(f"Einträge mit Dateiverweisen, die daneben Themen in Wortform nennen ({len(gemischt)}; auch diese Nennungen "
          "zählen nicht): " + ", ".join(f"{name} ({k})" for name, k in gemischt) + ".")
    else:
        w("Kein Eintrag mit Dateiverweisen nennt daneben Themen in Wortform.")
    w("")
    oa = m["ohne_abschnitt"]
    w(f"Einträge ohne Abschnitt „### Voraussetzungen (Blatt 0)“: {len(oa)}.")
    for name in oa:
        w(f"- {name}")
    w("")
    ub = m["unbekannt"]
    w(f"Verweise auf Dateien, die kein Katalogeintrag sind: {len(ub)}.")
    for ziel in sorted(ub):
        ort = fundort(ziel)
        lage = f"liegt in {', '.join(ort)}/" if ort else "keine Datei dieses Namens im Repo"
        w(f"- {ziel} ← {', '.join(ub[ziel])} ({lage})")
    if not ub:
        w("- keine")
    w("")
    w("## Schwäche der Messung")
    w("Die Zahlen messen, was in unseren Blatt-0-Abschnitten steht – also unsere eigene Sorgfalt beim Schreiben, "
      "nicht den Unterricht. Wo ein Eintrag seine Voraussetzungen sauber als Dateiverweise aufgelistet hat, "
      "steigen die Zahlen seiner Nachbarn; wo er sie in Wortform nennt oder weglässt, fehlen sie hier. "
      "Als Rangliste taugt die Messung, als Absolutwert nicht. Die Messlücken oben zeigen, wo sie blind ist.")
    w("")
    return "\n".join(out)


def main():
    katalog = os.path.join(HIER, KATALOG_ORDNER)
    m = messe(katalog, os.path.join(HIER, KONKORDANZ))
    stand = f"{datetime.date.today().isoformat()}, Katalog auf Commit {head_kurz()}"
    text = baue(m, stand)
    pfad = os.path.join(katalog, AUSGABE)
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    n = len(m["eintraege"])
    a, b = tabelle_a(m), tabelle_b(m)
    print(f"{VERSION}: {n} Einträge gemessen, {sum(1 for r in a if r[1])} Themen nachgefragt, "
          f"{sum(len(v) for v in m['voraussetzungen'].values())} Verweise; {KATALOG_ORDNER}/{AUSGABE} geschrieben "
          f"({text.count(chr(10))} Zeilen).")
    print("Tabelle A, die zehn obersten (Thema · Nachfrager · Zeilen):")
    for thema, zahl, _ in a[:10]:
        z = "–" if m["zeilen"] is None else m["zeilen"].get(thema, 0)
        print(f"  {zahl:3d} · {z:>4} · {thema}")
    print("Tabelle B, die fünf obersten (Thema · Voraussetzungen):")
    for thema, zahl, _ in b[:5]:
        print(f"  {zahl:3d} · {thema}")
    print(f"Messlücken: {len(m['ohne_verweis'])} Einträge ohne Verweis, {len(m['ohne_abschnitt'])} ohne Abschnitt, "
          f"{len(m['unbekannt'])} Verweise auf Dateien, die kein Katalogeintrag sind.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
