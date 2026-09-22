# -*- coding: utf-8 -*-
"""
einsortieren.py v0.2 · 22.09.2026 · Blattablage aus den Quellordnern nach blaetter/

Verarbeitet jedes *protokoll*.zip (Muster ohne Anker am Namensende, weil
Browser einer erneuten Ladung " (1)" anhängen) in QUELLORDNER: liest
protokoll.txt aus dem Archiv (Prompt, Modell, Vorlage, Katalog), leitet Thema
und Datum ab und legt das Blatt unter blaetter/<thema>/<datum>/ ab (pdf/ mit
allen .pdf, src/ mit den Quelltexten). Existiert der Zielordner schon, wird
das Archiv nicht verarbeitet und gemeldet. Verarbeitete Archive wandern nach
eingang/erledigt/, keines wird gelöscht. Danach wird blaetter/index.md aus
allen Ordnern unter blaetter/ neu geschrieben (aus src/protokoll.txt jedes
Blatts, nicht aus einem Zwischenspeicher).

Thema: Dateiname aus der Katalog-Zeile ohne Pfad und ohne .md; fehlt die Zeile
oder steht dort "nicht erreichbar", der Archivname vor dem ersten Unterstrich,
klein geschrieben. Datum: der Teil JJJJ-MM-TT des Archivnamens.

Aufruf: python einsortieren.py (aus der Repo-Wurzel, ohne Argumente).
"""
import re
import shutil
import sys
import zipfile
from datetime import date
from itertools import groupby
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
EINGANG = WURZEL / "eingang"
ERLEDIGT = EINGANG / "erledigt"
BLAETTER = WURZEL / "blaetter"

QUELLORDNER = [
    Path.home() / "Downloads",
    Path.home() / "OneDrive" / "Downloads",
    Path.home() / "OneDrive" / "blatt-eingang",
]

FELD_PREFIXE = {
    "Prompt:": "prompt",
    "Modell:": "modell",
    "Vorlage:": "vorlage",
    "Katalog:": "katalog",
}

SRC_MUSTER = [
    re.compile(r"^.+\.tex$"),
    re.compile(r"^eigene\.sty$"),
    re.compile(r"^pruef_.+\.py$"),
    re.compile(r"^pruef_out.*\.txt$"),
    re.compile(r"^protokoll\.txt$"),
    re.compile(r"^chat\.txt$"),
    re.compile(r"^zeiten\.txt$"),
    re.compile(r"^katalog_.+\.md$"),
]

NICHT_UEBERNOMMEN = {"mathblatt.sty", "anleitung_mathblatt.md"}


def ist_src_datei(name: str) -> bool:
    if name.lower().endswith(".log") or name.lower() in NICHT_UEBERNOMMEN:
        return False
    return any(m.match(name) for m in SRC_MUSTER)


def lies_protokoll_felder(text: str) -> dict:
    felder = {schluessel: "" for schluessel in FELD_PREFIXE.values()}
    for zeile in text.splitlines():
        zeile = zeile.strip()
        for prefix, schluessel in FELD_PREFIXE.items():
            if zeile.startswith(prefix):
                felder[schluessel] = zeile[len(prefix):].strip()
    return felder


def dateiname_aus_katalogfeld(katalog_wert: str) -> str:
    pfadteil = katalog_wert.split(",", 1)[0].strip()
    return pfadteil.split("/")[-1].strip()


def thema_aus_katalogfeld(katalog_wert: str, archivname: str) -> str:
    if katalog_wert and "nicht erreichbar" not in katalog_wert:
        dateiname = dateiname_aus_katalogfeld(katalog_wert)
        if dateiname.endswith(".md"):
            return dateiname[:-3]
    return archivname.split("_", 1)[0].lower()


def katalog_kurz(katalog_wert: str) -> str:
    if not katalog_wert:
        return ""
    dateiname = dateiname_aus_katalogfeld(katalog_wert)
    teile = katalog_wert.split(",", 1)
    rest = teile[1].strip() if len(teile) > 1 else ""
    return f"{dateiname}, {rest}" if rest else dateiname


def datum_aus_name(archivname: str) -> str:
    treffer = re.search(r"\d{4}-\d{2}-\d{2}", archivname)
    return treffer.group(0) if treffer else ""


def verarbeite_archiv(zip_pfad: Path) -> None:
    archivname = zip_pfad.stem
    with zipfile.ZipFile(zip_pfad) as zf:
        namen = [n for n in zf.namelist() if not n.endswith("/")]
        protokolle = [n for n in namen if Path(n).name == "protokoll.txt"]
        if not protokolle:
            print(f"{zip_pfad.name}: kein protokoll.txt im Archiv – nicht verarbeitet")
            return
        felder = lies_protokoll_felder(zf.read(protokolle[0]).decode("utf-8"))

        thema = thema_aus_katalogfeld(felder["katalog"], archivname)
        datum = datum_aus_name(zip_pfad.name)
        ziel = BLAETTER / thema / datum
        if ziel.exists():
            print(f"{zip_pfad.name}: {ziel} existiert schon – nicht verarbeitet")
            return

        ziel_pdf = ziel / "pdf"
        ziel_src = ziel / "src"
        ziel_pdf.mkdir(parents=True)
        ziel_src.mkdir(parents=True)

        n_pdf = n_src = 0
        for n in namen:
            basisname = Path(n).name
            if not basisname:
                continue
            if basisname.lower().endswith(".pdf"):
                (ziel_pdf / basisname).write_bytes(zf.read(n))
                n_pdf += 1
            elif ist_src_datei(basisname):
                (ziel_src / basisname).write_bytes(zf.read(n))
                n_src += 1

    shutil.move(str(zip_pfad), str(ERLEDIGT / zip_pfad.name))
    print(f"{thema}\t{datum}\t{n_pdf} PDFs\t{n_src} src-Dateien")


def schreibe_index() -> None:
    zeilen = []
    for thema_ordner in sorted(p for p in BLAETTER.iterdir() if p.is_dir()):
        for datum_ordner in sorted(p for p in thema_ordner.iterdir() if p.is_dir()):
            protokoll_pfad = datum_ordner / "src" / "protokoll.txt"
            felder = {schluessel: "" for schluessel in FELD_PREFIXE.values()}
            if protokoll_pfad.exists():
                felder = lies_protokoll_felder(protokoll_pfad.read_text(encoding="utf-8"))
            pdf_ordner = datum_ordner / "pdf"
            pdfs = sorted(p.name for p in pdf_ordner.glob("*.pdf")) if pdf_ordner.exists() else []
            zeilen.append({
                "thema": thema_ordner.name,
                "datum": datum_ordner.name,
                "prompt": felder["prompt"],
                "modell": felder["modell"],
                "vorlage": felder["vorlage"],
                "katalog": katalog_kurz(felder["katalog"]),
                "dateien": " · ".join(pdfs),
                "pfad": f"blaetter/{thema_ordner.name}/{datum_ordner.name}/",
            })

    zeilen.sort(key=lambda z: z["thema"])
    geordnet = []
    for _, gruppe in groupby(zeilen, key=lambda z: z["thema"]):
        geordnet.extend(sorted(gruppe, key=lambda z: z["datum"], reverse=True))

    heute = date.today().isoformat()
    einheit = "Blatt" if len(geordnet) == 1 else "Blätter"
    text = [
        "# Blätter – Register",
        f"Stand {heute}, {len(geordnet)} {einheit}.",
        "Abgeleitet von `werkzeuge/einsortieren.py`, nie von Hand ändern.",
        "",
        "| Thema | Datum | Prompt | Modell | Vorlage | Katalog | Dateien | Pfad |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for z in geordnet:
        text.append(
            f"| {z['thema']} | {z['datum']} | {z['prompt']} | {z['modell']} | "
            f"{z['vorlage']} | {z['katalog']} | {z['dateien']} | {z['pfad']} |"
        )

    (BLAETTER / "index.md").write_text("\n".join(text) + "\n", encoding="utf-8", newline="\n")
    print(f"Index: {len(geordnet)} Blätter")


def main() -> None:
    EINGANG.mkdir(exist_ok=True)
    ERLEDIGT.mkdir(exist_ok=True)
    BLAETTER.mkdir(exist_ok=True)
    if not QUELLORDNER[-1].exists():
        QUELLORDNER[-1].mkdir(parents=True)

    archive = []
    for ordner in QUELLORDNER:
        if ordner.exists():
            archive.extend(sorted(ordner.glob("*protokoll*.zip")))

    if not archive:
        print("kein Archiv im Eingang")
    for zip_pfad in archive:
        verarbeite_archiv(zip_pfad)

    schreibe_index()


if __name__ == "__main__":
    sys.exit(main())
