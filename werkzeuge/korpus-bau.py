# -*- coding: utf-8 -*-
"""
korpus-bau.py v0.2 · 18.09.2026 · rein maschineller Markdown-Korpus

Baut aus den Heftdateien unter hefte/<profil>/ (rekursiv, mit sonstiges/) je
Datei eine Markdown-Datei unter korpus/<profil>/<relpfad ohne .pdf>.md:
Kopf (Kennung, Seiten, Quelle, Erzeugungsdatum, Werkzeug), dann je Seite eine
Überschrift "## Seite n" mit dem unveränderten pypdf-Text und, ausnahmslos,
einem Ganzseitenrender als PNG unter korpus/<profil>/bilder/<relpfad>/seite-n.png
(kein Zuschnitt, keine Auswahl je Seite – siehe korpus-protokoll.md § 0: die
verlässliche Erkennung "hat diese Seite eine Abbildung" ohne Ansehen der Seite
ist nicht robust zu automatisieren, darum wird jede Seite gerendert).

ARBEITET OHNE MODELL-LESEN: Es werden keine Seiten angesehen, kein Text von
Hand geglättet oder ergänzt. Der Text ist die rohe pypdf-Extraktion, so wie
sie kommt (auch wenn Formeln oder Tabellenlayout verunstaltet herauskommen –
das ist keine Abweichung, sondern die Grenze der Extraktion; siehe
Schlussbericht in korpus-protokoll.md).

Neustart: `--bauen` überspringt jede Datei, deren Zieldatei schon existiert.
Scheitert eine Datei, wird sie übersprungen, der Grund protokolliert, der
Lauf läuft weiter (kein Abbruch der Etappe wegen einer Datei).

Aufruf:
  python korpus-bau.py <msa|fhr|abi|iqb> --status
      zeigt offene/fertige Dateien, ohne zu schreiben.
  python korpus-bau.py <msa|fhr|abi|iqb> --bauen [--etappe N] [--limit N]
      baut den Korpus für die offenen Dateien des Profils (optional auf eine
      Etappe eingeschränkt – 2: abi amtlich 2011-2018, 3: abi-OCR-Dateien;
      msa/fhr sind immer Etappe 1, iqb immer Etappe 4) und trägt je Datei
      eine Zeile in korpus-protokoll.md ein (append_protokoll_zeile).
  python korpus-bau.py abi --ocr [--limit N]
      führt ocrmypdf (deutsch) über die acht Bildscan-Verlagshefte 2022-2025
      aus, Ausgabe als <datei>-ocr.pdf neben dem Original (Original bleibt
      unverändert); Etappe 3 baut den Korpus danach aus diesen -ocr.pdf mit
      --bauen --etappe 3.
"""
import datetime
import io
import os
import re
import subprocess
import sys

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Umbau 2026-09-19: Repo-Wurzel; Skript liegt in werkzeuge/
VERSION = "korpus-bau.py v0.2"

PROFILE_QUELLEN = {
    "msa": "hefte/msa",
    "fhr": "hefte/fhr",
    "abi": "hefte/abi",
    "iqb": "hefte/iqb",
}

# Etappe 2 (abi amtlich 2011-2018, 44 Dateien): alle hefte/abi/*.pdf außer den
# Verlagsheften ab 2019 und den drei STARK-Alternativfassungen 2016-2018.
ABI_VERLAG_AB_2019 = {
    "2019-be-gk.pdf", "2020-be-gk.pdf", "2021-be-gk.pdf",
    "2022-bebb-gk.pdf", "2022-bebb-lk.pdf", "2023-bebb-gk.pdf", "2023-bebb-lk.pdf",
    "2024-bebb-gk.pdf", "2024-bebb-lk.pdf", "2025-bebb-gk.pdf", "2025-bebb-lk.pdf",
    "2026-bb-ea.pdf", "2026-bb-gk.pdf",
}
# Die acht Bildscan-Verlagshefte (Etappe 3, Grundlage für die OCR).
ABI_BILDSCANS = {
    "2022-bebb-gk.pdf", "2022-bebb-lk.pdf", "2023-bebb-gk.pdf", "2023-bebb-lk.pdf",
    "2024-bebb-gk.pdf", "2024-bebb-lk.pdf", "2025-bebb-gk.pdf", "2025-bebb-lk.pdf",
}


def abi_amtlich_filter(rel):
    if rel.startswith("sonstiges/"):
        return False  # keine Aufgabenhefte (Bildungsstandards, Rahmenlehrplan, Prüfungsschwerpunkte)
    if rel in ABI_VERLAG_AB_2019:
        return False
    if rel.endswith("-stark.pdf"):
        return False
    return True


def abi_ocr_ausgabe_filter(rel):
    return rel.endswith("-ocr.pdf")


ETAPPEN_FILTER = {
    1: {"msa": None, "fhr": None},
    2: {"abi": abi_amtlich_filter},
    3: {"abi": abi_ocr_ausgabe_filter},
    4: {"iqb": None},
}


def _pypdf():
    import pypdf
    return pypdf


def _pdfium():
    import pypdfium2
    return pypdfium2


def quell_dateien(profil, nur=None):
    wurzel = os.path.join(HIER, PROFILE_QUELLEN[profil])
    treffer = []
    for dirpath, _, dateien in os.walk(wurzel):
        for d in sorted(dateien):
            if not d.lower().endswith(".pdf"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, d), wurzel).replace("\\", "/")
            if nur and not nur(rel):
                continue
            treffer.append(rel)
    return sorted(treffer)


def ziel_md(profil, relpfad):
    ohne_ext = relpfad[:-4] if relpfad.lower().endswith(".pdf") else relpfad
    return os.path.join(HIER, "korpus", profil, ohne_ext + ".md")


def status(profil, nur=None):
    pypdf = _pypdf()
    quell_wurzel = os.path.join(HIER, PROFILE_QUELLEN[profil])
    fertig, offen = [], []
    for rel in quell_dateien(profil, nur):
        ziel = ziel_md(profil, rel)
        if os.path.exists(ziel):
            fertig.append(rel)
            continue
        pdf_pfad = os.path.join(quell_wurzel, rel)
        try:
            r = pypdf.PdfReader(pdf_pfad)
            seiten = len(r.pages)
        except Exception as e:
            seiten = f"Fehler: {e}"
        offen.append((rel, seiten))
    print(f"Profil {profil}: {len(fertig)} fertig, {len(offen)} offen (von {len(fertig) + len(offen)})")
    for rel, seiten in offen:
        print(f"  offen: {rel} · {seiten} Seiten")
    return fertig, offen


# ------------------------------------------------------------- Korpusbau

def baue_datei(profil, relpfad):
    """Baut die Korpus-Markdown-Datei für eine Quelldatei. Liefert
    (seiten, zeichen, abbildungen) oder wirft eine Exception (vom Aufrufer
    abgefangen und protokolliert)."""
    pypdf = _pypdf()
    pdfium = _pdfium()
    quell_pfad = os.path.join(HIER, PROFILE_QUELLEN[profil], relpfad)
    ohne_ext = relpfad[:-4] if relpfad.lower().endswith(".pdf") else relpfad
    ziel = ziel_md(profil, relpfad)
    bild_ordner_rel = f"bilder/{ohne_ext}"
    bild_ordner_abs = os.path.join(HIER, "korpus", profil, bild_ordner_rel)

    r = pypdf.PdfReader(quell_pfad)
    n = len(r.pages)
    pdf_bild = pdfium.PdfDocument(quell_pfad)
    if len(pdf_bild) != n:
        raise RuntimeError(f"Seitenzahl pypdf ({n}) != pypdfium2 ({len(pdf_bild)})")

    os.makedirs(bild_ordner_abs, exist_ok=True)
    teile = []
    zeichen = 0
    abbildungen = 0
    for i in range(n):
        seite_nr = i + 1
        try:
            text = r.pages[i].extract_text() or ""
        except Exception as e:
            text = f"(Text nicht extrahierbar: {e})"
        zeichen += len(text)
        bild_datei = f"seite-{seite_nr}.png"
        bitmap = pdf_bild[i].render(scale=150 / 72)
        bild = bitmap.to_pil().convert("RGB")
        bild.save(os.path.join(bild_ordner_abs, bild_datei))
        abbildungen += 1
        teile.append(
            f"## Seite {seite_nr}\n\n{text}\n\n![Seite {seite_nr}]({bild_ordner_rel}/{bild_datei})\n"
        )

    kopf = (
        f"# Korpus (maschinell): {relpfad}\n\n"
        f"Profil `{profil}` · Kennung `{ohne_ext}` · Seiten {n} · "
        f"Quelle `hefte/{profil}/{relpfad}` · "
        f"Erzeugt {datetime.date.today().isoformat()} mit {VERSION} (pypdf, pypdfium2).\n\n"
        "Rein maschinell: Text unveraendert aus pypdf.extract_text() je Seite, "
        "Ganzseitenrender (150 DPI) ohne Auswahl oder Zuschnitt. Kein Modell-Lesen, "
        "keine Glaettung, keine Ergaenzung – siehe korpus-protokoll.md.\n\n"
        "---\n\n"
    )
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    with io.open(ziel, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(kopf + "\n".join(teile))
    return n, zeichen, abbildungen


# ------------------------------------------------------------- Protokoll

def append_protokoll_zeile(section_heading, zeile):
    """Fuegt `zeile` (eine fertige Markdown-Tabellenzeile, beginnend mit '|')
    als letzte Zeile der Tabelle unter der Ueberschrift `section_heading`
    (z. B. '## 2 korpus/ Etappe 1 ...') in korpus-protokoll.md ein."""
    pfad = os.path.join(HIER, "werkzeuge", "korpus-protokoll.md")
    with io.open(pfad, encoding="utf-8") as fh:
        zeilen = fh.readlines()
    start = None
    for idx, z in enumerate(zeilen):
        if z.rstrip("\n") == section_heading:
            start = idx
            break
    if start is None:
        raise RuntimeError(f"Abschnitt nicht gefunden: {section_heading}")
    # Tabellenkopf und Trennzeile suchen, dann ans Ende der Tabelle springen
    i = start + 1
    while i < len(zeilen) and not zeilen[i].startswith("|"):
        i += 1
    if i >= len(zeilen):
        raise RuntimeError(f"Keine Tabelle unter {section_heading} gefunden")
    i += 2  # Kopfzeile + Trennzeile
    while i < len(zeilen) and zeilen[i].startswith("|"):
        i += 1
    zeilen.insert(i, zeile.rstrip("\n") + "\n")
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        fh.writelines(zeilen)


ETAPPE_SECTION = {
    1: "## 2 korpus/ Etappe 1 – msa und fhr (52 Dateien)",
    2: "## 3 korpus/ Etappe 2 – abi amtlich 2011–2018 (44 Dateien)",
    3: "## 4 korpus/ Etappe 3 – OCR der acht Bildscans + Korpus (8 Dateien)",
    4: "## 5 korpus/ Etappe 4 – iqb (624 Dateien)",
}


def etappe_von(profil):
    if profil in ("msa", "fhr"):
        return 1
    if profil == "iqb":
        return 4
    return None  # abi: per --etappe angeben


def bauen(profil, etappe=None, limit=None):
    if etappe is None:
        etappe = etappe_von(profil)
    if etappe is None:
        raise SystemExit("Profil abi: --etappe 2 oder --etappe 3 angeben")
    nur = ETAPPEN_FILTER.get(etappe, {}).get(profil)
    section = ETAPPE_SECTION[etappe]
    verarbeitet = uebersprungen = fehlgeschlagen = 0
    for rel in quell_dateien(profil, nur):
        ziel = ziel_md(profil, rel)
        if os.path.exists(ziel):
            continue
        if limit is not None and verarbeitet + fehlgeschlagen >= limit:
            break
        t0 = datetime.datetime.now()
        try:
            n, zeichen, abb = baue_datei(profil, rel)
            dauer = (datetime.datetime.now() - t0).total_seconds()
            print(f"  erfasst: {rel} ({n} Seiten, {zeichen} Zeichen, {abb} Bilder, {dauer:.1f} s)")
            append_protokoll_zeile(
                section,
                f"| {profil}/{rel} | erfasst | {n} | {zeichen} | {abb} | {dauer:.1f} s |",
            )
            verarbeitet += 1
        except Exception as e:
            print(f"  FEHLER: {rel}: {e}")
            append_protokoll_zeile(section, f"| {profil}/{rel} | fehlgeschlagen | – | – | – | {e} |")
            fehlgeschlagen += 1
    print(f"Profil {profil}, Etappe {etappe}: {verarbeitet} erfasst, {fehlgeschlagen} fehlgeschlagen, "
          f"{uebersprungen} übersprungen in diesem Lauf.")


# ------------------------------------------------------------- OCR (Etappe 3)

def ocr_bildscans(limit=None):
    """ocrmypdf --language deu über die acht Bildscan-Verlagshefte; Ausgabe
    als <datei>-ocr.pdf neben dem Original, Original bleibt unveraendert."""
    wurzel = os.path.join(HIER, "hefte", "abi")
    n = 0
    for rel in sorted(ABI_BILDSCANS):
        if limit is not None and n >= limit:
            break
        quelle = os.path.join(wurzel, rel)
        ziel = os.path.join(wurzel, rel[:-4] + "-ocr.pdf")
        if os.path.exists(ziel):
            print(f"  vorhanden, uebersprungen: {rel}")
            continue
        if not os.path.exists(quelle):
            print(f"  FEHLT: {quelle}")
            continue
        print(f"  OCR: {rel} -> {os.path.basename(ziel)} ...")
        t0 = datetime.datetime.now()
        try:
            r = subprocess.run(
                [sys.executable, "-m", "ocrmypdf", "--language", "deu", "--skip-text", quelle, ziel],
                capture_output=True, text=True, encoding="utf-8", errors="replace",
            )
            dauer = (datetime.datetime.now() - t0).total_seconds()
            if r.returncode != 0:
                print(f"    FEHLER (rc={r.returncode}): {r.stderr[-2000:]}")
            else:
                print(f"    fertig in {dauer:.0f} s")
                n += 1
        except Exception as e:
            print(f"    FEHLER: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in PROFILE_QUELLEN:
        raise SystemExit(f"Aufruf: python korpus-bau.py <{'|'.join(PROFILE_QUELLEN)}> [--status|--bauen [--etappe N] [--limit N]]")
    profil = sys.argv[1]
    rest = sys.argv[2:]

    def opt(name, default=None, typ=str):
        if name in rest:
            v = rest[rest.index(name) + 1]
            return typ(v)
        return default

    if not rest or rest[0] == "--status":
        etappe = opt("--etappe", None, int)
        nur = ETAPPEN_FILTER.get(etappe, {}).get(profil) if etappe else None
        status(profil, nur)
    elif rest[0] == "--bauen":
        bauen(profil, etappe=opt("--etappe", None, int), limit=opt("--limit", None, int))
    elif rest[0] == "--ocr":
        ocr_bildscans(limit=opt("--limit", None, int))
    else:
        raise SystemExit(f"unbekannte Option: {rest[0]}")
