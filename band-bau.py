# -*- coding: utf-8 -*-
"""
band-bau.py v0.3 · 18.09.2026 · Sammelband je Prüfungsart aus den Originalseiten

Baut aus den Heftdateien unter hefte/<profil>/ und der Strukturliste <profil>-band.csv
einen durchsuchbaren PDF-Band mit Titelblatt, Inhaltsverzeichnis, Register aus dem
Katalog, durchlaufender Seitenzahl und Lesezeichen; dazu je Heft ein Einzelheft mit
den Kolumnentiteln und Bandseitenzahlen des Bands. Ausgabe nach baende/ (per
.gitignore lokal). Aufruf: python band-bau.py fhr. Anleitung: band-anleitung.md.

Änderungen gegenüber 0.2 (Nachtrag zum Musterband, 18.09.2026): fhr vorspann_seiten
13 statt 20 (Entscheidung des Lehrers: Vorrat acht weitere Jahrgänge statt sechzehn,
fünf Reserveseiten statt zwölf); Hefte damit ab Bandseite 14. Sonst unverändert.

Änderungen gegenüber 0.1 (Nachbesserungen am Musterband, 18.09.2026):
- Register steht im Vorspann direkt hinter dem Inhaltsverzeichnis; die Reserveseiten
  folgen dahinter. Messung mit duplizierten Jahrgängen (18.09.2026, Typenliste um 30 %
  je acht Jahrgänge wachsend): 8 Jahrgänge brauchen 1 + 3 + 4 = 8 Seiten, 16 Jahrgänge
  13, 24 Jahrgänge 17; main() meldet die lineare Schätzung je Bau.
- Sprungmarken sichtbar: Seitenzahlen in Inhalt, Register und Seitenkarte in gedecktem
  Blau (BLAU), Linkrahmen bleiben aus; übriger Text unverändert.
- Auf jeder Heftseite neben dem Kolumnentitel die klickbare Marke „▲ Inhalt" zurück zum
  Inhaltsverzeichnis, gleiche Grundlinie und Randprüfung wie der Aufdruck.
- Hinweisseite: Zeile zum Rücksprung im Betrachter (Alt+Pfeil links, Cmd+ö) und
  Herkunftszeile (Repo, Commit mit Datum, Stand der Arbeitskopie, Baudatum).
- Einzelhefte nach baende/<profil>-einzeln/<jahr>-<papier>.pdf mit denselben
  Kolumnentiteln und Bandseitenzahlen (Seitenlabels = Bandseiten), ohne die Marke.

Entscheidungen (Auftrag „Musterband fhr", 18.09.2026):
- Originalseiten, kein Neusatz; eine Bandseite = eine Heftseite; Hefte vollständig
  und in ihrer Reihenfolge, damit Heftseite → Bandseite je Heft ein fester Offset ist.
- Bandseite = PDF-Seitenindex (Titelblatt = 1), damit die Zahlen aus Inhalt und
  Register direkt im Druckdialog gelten. Seitenlabels werden entsprechend gesetzt.
- Hefte aufsteigend nach Jahrgang; der Vorspann hat eine feste Seitenreserve
  (KONFIG vorspann_seiten), damit ein angehängter Jahrgang bestehende Bandseiten
  und gedruckte Registerseiten nicht verschiebt. Reicht die Reserve nicht mehr,
  bricht das Skript ab und verlangt einen höheren Wert.
- Kolumnentitel (Heft, Abschnitt, Bandseite) als kleiner Aufdruck im oberen Rand;
  vorher wird jede Seite gerendert und geprüft, ob der Rand frei ist. Ist er belegt,
  rutscht der Aufdruck auf dieser Seite nach unten; ist auch der untere Rand belegt,
  entfällt er dort. Seiteninhalt bleibt unverändert.
- Register aus dem Katalog: Leitidee → Thema → Typ (Zuordnung nach der Typenliste)
  → Fundstellen mit Bandseite der Aufgabe und, getrennt gekennzeichnet, Bandseite des
  Erwartungshorizonts. Kursiv = Vorkommen als Nebentyp. Alle Einträge klickbar.
  Die Zuordnung zu Themen und Typen geschieht in der Erfassung, nicht hier: ein Heft
  ohne Katalogzeilen steht im Band, aber nicht im Register (konzept.md § 7).
- Hinweise je Heft (Arbeitszeit, Hilfsmittel, Datum, BE) stehen in der Strukturliste
  und stammen aus dem Repo, nicht aus den Heften.

Strukturliste <profil>-band.csv (Semikolon, gequotet, UTF-8; Kopf
ebene;kennung;titel;datei;von;bis;hinweis; Seiten sind Heftseiten ab 1):
  Ebene 1 Jahrgang, Ebene 2 Heft (datei, von/bis = ganzes Heft, hinweis),
  Ebene 3 Abschnitt eines Hefts. Konventionen, die dieses Skript nutzt:
  Katalog-ids beginnen mit „<heftkennung>-"; die Aufgabenkennung „<heft>-<aufgabe>"
  ist Präfix der ids ihrer Teilaufgaben; der Erwartungshorizont einer Aufgabe hat die
  Kennung „<heft>-<aufgabe>-eh" und erscheint im Inhalt auf der Aufgabenzeile.
  **Die Abschnittszeilen (Ebene 3) werden von <profil>-band-struktur.py aus Katalog
  und Seitentext erzeugt. Ändert sich der Katalog (Seiten, Aufgaben, neue Hefte),
  ist die Liste damit neu zu erzeugen – Abschnittszeilen nicht von Hand pflegen.**
  Ebenen 1 und 2 (Reihenfolge, Titel, Hinweiszeile) bleiben beim Neuerzeugen
  erhalten und dürfen von Hand geändert werden; Ausgabeformat und Seitenzählung des
  Bands stehen nicht in der Liste, sondern hier in KONFIG.

Bibliotheken: pypdf (Zusammenführen, Lesezeichen, Links, Seitenlabels), reportlab
(Vorspann, Register, Aufdruck), pypdfium2 + Pillow (Randprüfung durch Rendern).
Auf dem Rechner des Lehrers: LibreOffice-Python mit PYTHONPATH auf einen
pip-Zielordner (CLAUDE.md); git wird für die Herkunftszeile gesucht (PATH, sonst
GitHub Desktop).
"""
import csv
import datetime as dt
import glob
import io
import logging
import os
import re
import subprocess
import sys
from collections import OrderedDict, defaultdict
from pathlib import Path

logging.disable(logging.CRITICAL)  # pypdf-Warnungen zu Schriften der Hefte unterdrücken
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import ArrayObject, NameObject, NumberObject
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

HIER = Path(__file__).resolve().parent
VERSION = "band-bau.py v0.3"

KONFIG = {
    "fhr": dict(
        titel="Fachhochschulreife Mathematik · Land Brandenburg",
        untertitel="Prüfungshefte {von}–{bis} · Sammelband",
        praefix="FHR",
        struktur="fhr-band.csv",
        kataloge=["fhr-katalog.csv"],
        typen="fhr-typen.csv",
        ausgabe="baende/fhr-band.pdf",
        einzeln="baende/fhr-einzeln",
        vorspann_seiten=13,  # Titel 1 + Inhalt 3 + Register 4 + Reserve 5 (band-anleitung.md § 5)
        leitideen=["Differentialrechnung", "Integralrechnung", "Stochastik", "Grundlagen"],
        hinweise=[
            "Zentrale schriftliche Prüfung zum Erwerb der Fachhochschulreife, Fach Mathematik. "
            "Je Heft drei voneinander unabhängige, mehrteilige Aufgaben mit Praxisbezug, alle zu bearbeiten; "
            "70 Bewertungseinheiten, Arbeitszeit 180 Minuten.",
            "Hilfsmittel: Formelsammlung, Nachschlagewerk zur Rechtschreibung, Taschenrechner ohne "
            "Programmierbarkeit, Grafik, numerisches Differenzieren oder Integrieren und ohne automatisches "
            "Gleichungslösen (kein CAS). Nichtganzzahlige Ergebnisse auf zwei Dezimalstellen gerundet.",
            'Die Hefte sind „Unterlagen für die Lehrkraft": auf jede Aufgabenseite folgt unmittelbar ihr '
            "Erwartungshorizont, ab 2022 meist mit Gutachtenbogen am Ende. Angaben nach fhr.md und den "
            "Prüfungsschwerpunkten des MBJS (Stand 2026/27, 2027/28); die Hefte selbst nennen sie nicht.",
        ],
        quelle="Bildungsserver Berlin-Brandenburg, Verzeichnis Fachoberschule_BB/Pruefungsaufgaben; "
               "lokale Heftdateien hefte/fhr/<jahr>-<papier>.pdf",
    ),
}

# Seitengeometrie des Vorspanns und Registers (A4)
BREITE, HOEHE = A4
RAND_L, RAND_R, RAND_O, RAND_U = 50, 50, 56, 50
GRAU = 0.4
BLAU = (0.16, 0.32, 0.55)  # gedecktes Blau für Sprungmarken (Seitenzahlen, Marke)

# Aufdruck: oben (Vorzug) und unten (Ausweg); geprüft wird, ob der Streifen (PDF-y von…bis) leer ist.
# Maß der Hefte (gemessen 18.09.2026): Kopfzeile beginnt 2019–2021 bei y = 813,5, ab 2022 bei 805;
# der Aufdruck mit Grundlinie 826 und 7,5 pt liegt bei y ≈ 824–832, also 5,6 mm unter der Blattkante.
STEMPEL_OBEN = dict(streifen=(819, 842), basis=826)
STEMPEL_UNTEN = dict(streifen=(3, 16), basis=6.5)
STEMPEL_GROESSE = 7.5
STEMPEL_X = (42, 553)  # links / rechts
MARKE = "▲ Inhalt"     # Rücksprungmarke zum Inhaltsverzeichnis (Bandseite 2)
MARKE_ABSTAND = 14     # Abstand zwischen Marke und Bandseitenzahl
WEISS = 240  # Grauwert, ab dem ein Pixel als leer gilt


# ---------------------------------------------------------------- Schriften
def schriften():
    """Arial aus dem Windows-Schriftenordner einbetten (volle Zeichenabdeckung), sonst Helvetica."""
    ordner = Path(r"C:\Windows\Fonts")
    dateien = {"Arial": "arial.ttf", "Arial-Bold": "arialbd.ttf", "Arial-Italic": "ariali.ttf",
               "Arial-BoldItalic": "arialbi.ttf"}
    if all((ordner / d).exists() for d in dateien.values()):
        for name, d in dateien.items():
            pdfmetrics.registerFont(TTFont(name, str(ordner / d)))
        pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic",
                                      boldItalic="Arial-BoldItalic")
        return dict(normal="Arial", fett="Arial-Bold", kursiv="Arial-Italic")
    return dict(normal="Helvetica", fett="Helvetica-Bold", kursiv="Helvetica-Oblique")


def breite(text, font, groesse):
    return pdfmetrics.stringWidth(text, font, groesse)


def umbrechen(text, font, groesse, maxbreite):
    """Wortumbruch; gibt Zeilen zurück."""
    zeilen, aktuell = [], ""
    for wort in text.split():
        probe = (aktuell + " " + wort).strip()
        if breite(probe, font, groesse) <= maxbreite or not aktuell:
            aktuell = probe
        else:
            zeilen.append(aktuell)
            aktuell = wort
    if aktuell:
        zeilen.append(aktuell)
    return zeilen


def kuerzen(text, font, groesse, maxbreite):
    if breite(text, font, groesse) <= maxbreite:
        return text
    while text and breite(text + "…", font, groesse) > maxbreite:
        text = text[:-1]
    return text.rstrip() + "…"


def blau(c):
    c.setFillColorRGB(*BLAU)


def schwarz(c):
    c.setFillGray(0)


# ---------------------------------------------------------------- Eingaben
def strukturliste(pfad):
    with open(pfad, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f, delimiter=";", quotechar='"')
        if r.fieldnames != ["ebene", "kennung", "titel", "datei", "von", "bis", "hinweis"]:
            raise SystemExit(f"{pfad.name}: unerwartete Kopfzeile {r.fieldnames}")
        zeilen = [z for z in r if z["kennung"]]
    return zeilen


def katalog(pfade):
    zeilen = []
    for p in pfade:
        with open(p, encoding="utf-8", newline="") as f:
            zeilen.extend(csv.DictReader(f, delimiter=";", quotechar='"'))
    return zeilen


def typenliste(pfad):
    typen = {}
    with open(pfad, encoding="utf-8", newline="") as f:
        for z in csv.DictReader(f, delimiter=";", quotechar='"'):
            typen[z["typ"]] = (z["leitidee"], z["thema"])
    return typen


def erste_zahl(text):
    m = re.search(r"\d+", text)
    return int(m.group()) if m else None


def herkunft():
    """Repo, Commit (Kurzhash, Datum) und Stand der Arbeitskopie über git; ohne git: unbekannt."""
    kandidaten = ["git"] + sorted(glob.glob(os.path.expandvars(
        r"%LOCALAPPDATA%\GitHubDesktop\app-*\resources\app\git\cmd\git.exe")))
    for git in kandidaten:
        try:
            def g(*args):
                return subprocess.run([git, "-C", str(HIER)] + list(args), capture_output=True, text=True,
                                      encoding="utf-8", check=True).stdout
            commit = g("rev-parse", "--short=7", "HEAD").strip()
            datum = g("log", "-1", "--format=%cs").strip()
            url = g("remote", "get-url", "origin").strip()
            repo = re.sub(r"\.git$", "", re.sub(r"^.*github\.com[:/]", "", url)) or url
            # Porcelain-Zeilen „XY Pfad": die ersten zwei Zeichen sind der Status, das Leerzeichen davor zählt
            status = [z for z in g("status", "--porcelain").splitlines() if z.strip()]
            geaendert = sorted(z[3:].strip() for z in status)
            return dict(repo=repo, commit=commit, datum=datum, geaendert=geaendert)
        except (OSError, subprocess.CalledProcessError):
            continue
    return dict(repo="unbekannt (git nicht gefunden)", commit="unbekannt", datum="", geaendert=[])


def herkunftszeile(h, baudatum):
    if h["geaendert"]:
        stand = (f"Arbeitskopie beim Bau mit {len(h['geaendert'])} nicht committeten Änderungen "
                 f"({', '.join(h['geaendert'][:6])}{', …' if len(h['geaendert']) > 6 else ''})")
    else:
        stand = "Arbeitskopie beim Bau ohne nicht committete Änderungen"
    return (f"Herkunft: Repo {h['repo']}, Commit {h['commit']}"
            + (f" vom {h['datum']}" if h["datum"] else "") + f"; {stand}. Gebaut am {baudatum} mit {VERSION}. "
            "Ein Ausdruck ist auf dem aktuellen Stand, wenn Commit und Baudatum zum Repo passen.")


# ---------------------------------------------------------------- Seitenplan
class Plan:
    """Bandseiten aller Einheiten. Hefte laufen ab vorspann_seiten + 1 in Listenreihenfolge;
    im Vorspann liegen Titelblatt (1), Inhalt (ab 2), Register (ab register_ab, nach dem Inhalt
    gesetzt) und Reserveseiten."""

    def __init__(self, liste, k):
        self.vorspann = k["vorspann_seiten"]
        self.jahrgaenge = []           # (kennung, titel, erste Bandseite)
        self.hefte = OrderedDict()     # kennung → dict(titel, datei, seiten, offset, hinweis, abschnitte)
        self.seite_titel = {}          # Bandseite → (heftkennung, abschnittstitel)
        self.register_ab = None        # wird nach dem Satz des Inhalts gesetzt
        band = self.vorspann
        heft = None
        for z in liste:
            e = z["ebene"]
            if e == "1":
                self.jahrgaenge.append([z["kennung"], z["titel"], None])
            elif e == "2":
                pfad = HIER / z["datei"]
                if not pfad.exists():
                    raise SystemExit(f"Heftdatei fehlt: {z['datei']}")
                n = len(PdfReader(str(pfad)).pages)
                if int(z["von"]) != 1 or int(z["bis"]) != n:
                    raise SystemExit(f"{z['kennung']}: Liste nennt Seiten {z['von']}–{z['bis']}, Datei hat {n}")
                heft = dict(kennung=z["kennung"], titel=z["titel"], datei=pfad, seiten=n, offset=band,
                            hinweis=z["hinweis"], abschnitte=[])
                self.hefte[z["kennung"]] = heft
                if self.jahrgaenge and self.jahrgaenge[-1][2] is None:
                    self.jahrgaenge[-1][2] = band + 1
                band += n
            elif e == "3":
                if heft is None or not z["kennung"].startswith(heft["kennung"] + "-"):
                    raise SystemExit(f"Abschnitt {z['kennung']} ohne passendes Heft davor")
                von, bis = int(z["von"]), int(z["bis"])
                if not (1 <= von <= bis <= heft["seiten"]):
                    raise SystemExit(f"{z['kennung']}: Seiten {von}–{bis} außerhalb des Hefts")
                a = dict(kennung=z["kennung"], titel=z["titel"], von=heft["offset"] + von, bis=heft["offset"] + bis)
                heft["abschnitte"].append(a)
                for s in range(a["von"], a["bis"] + 1):
                    self.seite_titel[s] = (heft["kennung"], a["titel"])
            else:
                raise SystemExit(f"Unbekannte Ebene {e} bei {z['kennung']}")
        self.heftseiten = band - self.vorspann
        self.bandende = band
        # Abschnittslücken: jede Heftseite soll einem Abschnitt gehören (Kolumnentitel)
        for h in self.hefte.values():
            for s in range(h["offset"] + 1, h["offset"] + h["seiten"] + 1):
                self.seite_titel.setdefault(s, (h["kennung"], ""))

    def heft_zu_id(self, id_):
        treffer = [k for k in self.hefte if id_.startswith(k + "-")]
        return max(treffer, key=len) if treffer else None

    def abschnitt(self, kennung):
        for h in self.hefte.values():
            for a in h["abschnitte"]:
                if a["kennung"] == kennung:
                    return a
        return None


# ---------------------------------------------------------------- Vorspann
def anzeige(kennung):
    return kennung.replace("-", " ")


def absaetze(c, absatz_liste, font, groesse, y, zeilenhoehe=12.5, absatzabstand=4):
    for absatz in absatz_liste:
        for zeile in umbrechen(absatz, font, groesse, BREITE - RAND_L - RAND_R):
            c.drawString(RAND_L, y, zeile); y -= zeilenhoehe
        y -= absatzabstand
    return y


def titelblatt_bauen(plan, k, f, inhalt_seiten, register_seiten, herk):
    """Bandseite 1: Titel, Hinweise zur Prüfung, Zum Band, Seitenkarte. Gibt (PDF-Bytes, Links)."""
    puffer = io.BytesIO()
    c = canvas.Canvas(puffer, pagesize=A4)
    links = []
    jahre = [j[0] for j in plan.jahrgaenge]
    untertitel = k["untertitel"].format(von=jahre[0], bis=jahre[-1]) if jahre else k["untertitel"]
    baudatum = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    reserve = plan.vorspann - 1 - inhalt_seiten - register_seiten

    y = HOEHE - 150
    c.setFont(f["fett"], 20); c.drawString(RAND_L, y, k["titel"]); y -= 28
    c.setFont(f["normal"], 14); c.drawString(RAND_L, y, untertitel); y -= 20
    c.setFont(f["normal"], 9); c.setFillGray(GRAU)
    c.drawString(RAND_L, y, f"{len(plan.hefte)} Hefte, {plan.heftseiten} Heftseiten · erzeugt am "
                 f"{baudatum[:10]} mit {VERSION} · nur für den eigenen Gebrauch")
    schwarz(c); y -= 34
    c.setFont(f["fett"], 11); c.drawString(RAND_L, y, "Hinweise zur Prüfung"); y -= 16
    c.setFont(f["normal"], 9.5)
    y = absaetze(c, k["hinweise"], f["normal"], 9.5, y)
    y -= 10
    c.setFont(f["fett"], 11); c.drawString(RAND_L, y, "Zum Band"); y -= 16
    c.setFont(f["normal"], 9.5)
    zum_band = [
        "Bandseite = PDF-Seite (dieses Titelblatt ist Seite 1). Die Zahlen aus Inhalt und Register gelten "
        'deshalb unmittelbar im Druckdialog („von Seite bis Seite").',
        f"Inhaltsverzeichnis ab Seite 2, Register ab Seite {plan.register_ab} ({register_seiten} Seiten), "
        f"dann {reserve} Reserveseiten für spätere Jahrgänge, Hefte ab Seite {plan.vorspann + 1} bis Seite "
        f"{plan.bandende}. Lesezeichen und Einträge sind klickbar; Seitenzahlen in Blau sind Sprungmarken.",
        "Jede Heftseite ist unverändert übernommen; oben am Rand steht klein Heft, Abschnitt und Bandseite, "
        f"daneben die Marke „{MARKE}\" zurück zum Inhaltsverzeichnis. Heftseite → Bandseite ist je Heft ein fester "
        "Offset (Tabelle unten).",
        "Zurück zur Stelle vor einem Sprung geht es im Betrachter: Acrobat und Edge/Chrome Alt+Pfeil links, "
        "Vorschau (macOS) Cmd+ö. Ein Rücksprung-Link im PDF selbst ist nicht möglich.",
        'Register: Leitidee → Thema → Typ → Fundstellen „Heft Teilaufgabe: Aufgabenseite (EH Seite des '
        'Erwartungshorizonts)"; kursiv = Vorkommen als Nebentyp. Zuordnung nach der Typenliste des Katalogs; '
        "ein Heft ohne Katalogzeilen steht im Band, aber nicht im Register.",
        f"Quelle der Hefte: {k['quelle']}.",
        herkunftszeile(herk, baudatum),
    ]
    y = absaetze(c, zum_band, f["normal"], 9.5, y)
    y -= 10
    c.setFont(f["fett"], 11); c.drawString(RAND_L, y, "Hefte und Bandseiten"); y -= 15
    # Seitenkarte: zwei Spalten, bei mehr Heften drei oder vier (dann kurz „(+Offset)"), damit sie auf das
    # Titelblatt passt; Maßstab 24 Jahrgänge (48 Hefte) bei 14 Zeilen je Spalte.
    hefte = list(plan.hefte.values())
    for spalten in (2, 3, 4):
        reihen = (len(hefte) + spalten - 1) // spalten
        if y - reihen * 11.5 >= RAND_U:
            break
    else:
        raise SystemExit("Titelblatt: die Seitenkarte passt nicht mehr auf die Seite – Text kürzen oder "
                         "Seitenkarte auf eine eigene Seite legen")
    spaltenbreite = (BREITE - RAND_L - RAND_R) / spalten
    for i, h in enumerate(hefte):
        sp, re_ = divmod(i, reihen)
        x = RAND_L + sp * spaltenbreite
        yy = y - re_ * 11.5
        von, bis = h["offset"] + 1, h["offset"] + h["seiten"]
        t1, t2 = anzeige(h["kennung"]) + "   ", f"S. {von}–{bis}"
        t3 = f"   (Heftseite + {h['offset']})" if spalten == 2 else f"   (+{h['offset']})"
        c.setFont(f["normal"], 8.5)
        schwarz(c); c.drawString(x, yy, t1)
        x2 = x + breite(t1, f["normal"], 8.5)
        blau(c); c.drawString(x2, yy, t2)
        x3 = x2 + breite(t2, f["normal"], 8.5)
        schwarz(c); c.drawString(x3, yy, t3)
        links.append((0, (x, yy - 2, x3 + breite(t3, f["normal"], 8.5), yy + 8), von))
    c.showPage()
    c.save()
    return puffer.getvalue(), links


def inhalt_bauen(plan, k, f):
    """Inhaltsverzeichnis (ab Bandseite 2). Gibt (PDF-Bytes, Links relativ zur ersten Inhaltsseite, Seitenzahl)."""
    puffer = io.BytesIO()
    c = canvas.Canvas(puffer, pagesize=A4)
    links = []
    X_TITEL, X_SEITE, X_EH = RAND_L + 18, BREITE - RAND_R - 105, BREITE - RAND_R
    seite_idx = 0
    y = None

    def kopf(fortsetzung):
        nonlocal y
        c.setFont(f["fett"], 14)
        c.drawString(RAND_L, HOEHE - RAND_O - 4, "Inhalt" + (" (Fortsetzung)" if fortsetzung else ""))
        c.setFont(f["normal"], 7.5); c.setFillGray(GRAU)
        c.drawRightString(X_SEITE, HOEHE - RAND_O - 4, "Seite")
        c.drawRightString(X_EH, HOEHE - RAND_O - 4, "Erwartungshorizont")
        schwarz(c)
        y = HOEHE - RAND_O - 28

    def neue_seite():
        nonlocal seite_idx
        c.showPage(); seite_idx += 1
        kopf(True)

    def platz(hoehe):
        if y - hoehe < RAND_U:
            neue_seite()

    kopf(False)
    for jahr in plan.jahrgaenge:
        hefte_j = [h for h in plan.hefte.values() if h["kennung"].startswith(jahr[0] + "-")]
        platz(60)
        y -= 6
        c.setFont(f["fett"], 11); c.drawString(RAND_L, y, jahr[1])
        if jahr[2]:
            links.append((seite_idx, (RAND_L, y - 2, RAND_L + breite(jahr[1], f["fett"], 11), y + 9), jahr[2]))
        y -= 15
        for h in hefte_j:
            platz(24 + 11 * (len(h["abschnitte"]) + 1))
            von, bis = h["offset"] + 1, h["offset"] + h["seiten"]
            c.setFont(f["fett"], 9.5)
            kopfzeile = f"{anzeige(h['kennung'])}  ·  {h['titel']}"
            c.drawString(RAND_L, y, kopfzeile)
            blau(c); c.drawRightString(X_SEITE, y, f"{von}–{bis}"); schwarz(c)
            links.append((seite_idx, (RAND_L, y - 2, X_SEITE, y + 8), von))
            y -= 10.5
            if h["hinweis"]:
                c.setFont(f["normal"], 7.5); c.setFillGray(GRAU)
                c.drawString(RAND_L, y, kuerzen(h["hinweis"], f["normal"], 7.5, X_EH - RAND_L))
                schwarz(c); y -= 11
            eh = {a["kennung"][:-3]: a for a in h["abschnitte"] if a["kennung"].endswith("-eh")}
            for a in h["abschnitte"]:
                if a["kennung"].endswith("-eh"):
                    continue
                c.setFont(f["normal"], 9)
                titel = kuerzen(a["titel"], f["normal"], 9, X_SEITE - X_TITEL - 40)
                c.drawString(X_TITEL, y, titel)
                bereich = str(a["von"]) if a["von"] == a["bis"] else f"{a['von']}–{a['bis']}"
                blau(c); c.drawRightString(X_SEITE, y, bereich); schwarz(c)
                links.append((seite_idx, (X_TITEL, y - 2, X_SEITE, y + 8), a["von"]))
                e = eh.get(a["kennung"])
                if e:
                    text = str(e["von"]) if e["von"] == e["bis"] else f"{e['von']}–{e['bis']}"
                    blau(c); c.drawRightString(X_EH, y, "EH " + text); schwarz(c)
                    links.append((seite_idx, (X_EH - breite("EH " + text, f["normal"], 9), y - 2, X_EH, y + 8), e["von"]))
                y -= 11
            y -= 5
    c.showPage()
    c.save()
    return puffer.getvalue(), links, seite_idx + 1


def reserve_bauen(n, f):
    puffer = io.BytesIO()
    c = canvas.Canvas(puffer, pagesize=A4)
    for _ in range(n):
        c.setFont(f["normal"], 8); c.setFillGray(GRAU)
        c.drawCentredString(BREITE / 2, HOEHE / 2, "Reserve für Inhaltsverzeichnis und Register späterer Jahrgänge – "
                            "die Bandseiten der Hefte bleiben so beim Anhängen stabil.")
        schwarz(c); c.showPage()
    c.save()
    return puffer.getvalue()


# ---------------------------------------------------------------- Register
def register_daten(plan, zeilen, typen, k):
    """Register: Leitidee → Thema → Typ → [Fundstellen]; Fundstelle = dict(text, seite, eh, neben)."""
    reihenfolge = {l: i for i, l in enumerate(k["leitideen"])}
    reg = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    nicht_im_band, ohne_typ = [], []
    heftfolge = {h: i for i, h in enumerate(plan.hefte)}
    for z in zeilen:
        heft = plan.heft_zu_id(z["id"])
        if heft is None:
            nicht_im_band.append(z["id"]); continue
        s = erste_zahl(z["seite"])
        if s is None:
            nicht_im_band.append(z["id"] + " (keine Seite)"); continue
        band = plan.hefte[heft]["offset"] + s
        eh = plan.abschnitt(f"{heft}-{z['aufgabe']}-eh")
        fund = dict(heft=heft, text=f"{anzeige(heft)} {z['aufgabe']}{z['teilaufgabe']}", seite=band,
                    eh=eh["von"] if eh else None,
                    sortier=(heftfolge[heft], z["aufgabe"], z["teilaufgabe"]))
        for i, typ in enumerate([z["typ"]] + [t for t in z["typ_neben"].split("|") if t]):
            if typ in typen:
                leit, thema = typen[typ]
            elif i == 0:
                leit, thema = z["leitidee"], z["thema"]; ohne_typ.append(f"{z['id']}: {typ}")
            else:
                ohne_typ.append(f"{z['id']}: Nebentyp {typ}"); continue
            reg[leit][thema][typ].append(dict(fund, neben=(i > 0)))
    sortiert = OrderedDict()
    for leit in sorted(reg, key=lambda l: (reihenfolge.get(l, 99), l)):
        sortiert[leit] = OrderedDict()
        for thema in sorted(reg[leit], key=str.casefold):
            sortiert[leit][thema] = OrderedDict()
            for typ in sorted(reg[leit][thema], key=str.casefold):
                sortiert[leit][thema][typ] = sorted(reg[leit][thema][typ], key=lambda x: x["sortier"])
    return sortiert, nicht_im_band, ohne_typ


class Setzer:
    """Zweispaltiger Satz mit Seitenumbruch für das Register; merkt sich Linkrechtecke."""

    def __init__(self, c, f, titel):
        self.c, self.f, self.titel = c, f, titel
        self.spalten = 2
        self.abstand = 18
        self.spaltenbreite = (BREITE - RAND_L - RAND_R - self.abstand * (self.spalten - 1)) / self.spalten
        self.seite = 0
        self.links = []  # (Seitenindex im Register, Rechteck, Ziel-Bandseite)
        self.spalte = -1
        self.y = 0
        self.neue_spalte()

    @property
    def x(self):
        return RAND_L + self.spalte * (self.spaltenbreite + self.abstand)

    def neue_spalte(self):
        self.spalte += 1
        if self.spalte >= self.spalten or self.seite == 0:
            if self.seite > 0:
                self.c.showPage()
            self.seite += 1
            self.spalte = 0
            self.c.setFont(self.f["fett"], 14)
            self.c.drawString(RAND_L, HOEHE - RAND_O - 4, self.titel + (" (Fortsetzung)" if self.seite > 1 else ""))
            if self.seite == 1:
                self.c.setFont(self.f["normal"], 7.5); self.c.setFillGray(GRAU)
                self.c.drawRightString(BREITE - RAND_R, HOEHE - RAND_O - 4,
                                       "Fundstelle: Heft Teilaufgabe: Aufgabenseite (EH Erwartungshorizont) · kursiv = Nebentyp")
                schwarz(self.c)
        self.y = HOEHE - RAND_O - 28

    def platz(self, hoehe):
        """Spaltenwechsel, wenn die Höhe nicht mehr passt; True, wenn gewechselt wurde."""
        if self.y - hoehe < RAND_U:
            self.neue_spalte()
            return True
        return False

    def zeile(self, text, font, groesse, einzug=0, grau=0, abstand_vor=0):
        self.y -= abstand_vor
        for t in umbrechen(text, font, groesse, self.spaltenbreite - einzug):
            self.platz(groesse + 3)
            self.c.setFont(font, groesse); self.c.setFillGray(grau)
            self.c.drawString(self.x + einzug, self.y, t)
            schwarz(self.c)
            self.y -= groesse + 3

    def fundstellen(self, funde, groesse=7.5, einzug=8):
        """Fundstellen fließend setzen; Zahl und EH-Angabe werden verlinkt (blau)."""
        trenner = "   "
        zeilenhoehe = groesse + 2.5
        self.platz(zeilenhoehe)
        self.y -= 1
        x = self.x + einzug
        for i, fu in enumerate(funde):
            font = self.f["kursiv"] if fu["neben"] else self.f["normal"]
            teile = [(fu["text"] + ": ", None), (str(fu["seite"]), fu["seite"])]
            if fu["eh"]:
                teile += [(" (EH ", None), (str(fu["eh"]), fu["eh"]), (")", None)]
            gesamt = sum(breite(t, font, groesse) for t, _ in teile)
            if x + gesamt > self.x + self.spaltenbreite and x > self.x + einzug:
                self.y -= zeilenhoehe
                self.platz(zeilenhoehe)
                x = self.x + einzug
            self.c.setFont(font, groesse)
            for t, ziel in teile:
                b = breite(t, font, groesse)
                if ziel:
                    blau(self.c)
                    self.links.append((self.seite - 1, (x - 1, self.y - 2, x + b + 1, self.y + groesse), ziel))
                self.c.drawString(x, self.y, t)
                schwarz(self.c)
                x += b
            x += breite(trenner, font, groesse)
        self.y -= zeilenhoehe


def register_bauen(reg, f):
    puffer = io.BytesIO()
    c = canvas.Canvas(puffer, pagesize=A4)
    s = Setzer(c, f, "Register")
    # platz() hält Überschriften mit dem Folgenden zusammen: Leitidee + Thema + Typ + eine Fundstellenzeile
    for leit, themen in reg.items():
        s.platz(80)
        s.zeile(leit, f["fett"], 11, abstand_vor=8)
        for thema, typen in themen.items():
            s.platz(58)
            s.zeile(thema, f["fett"], 8.5, abstand_vor=5)
            for typ, funde in typen.items():
                s.platz(36)
                s.zeile(typ, f["normal"], 8, einzug=4, abstand_vor=1.5)
                s.fundstellen(funde)
    c.showPage(); c.save()
    return puffer.getvalue(), s.links, s.seite


# ---------------------------------------------------------------- Randprüfung und Aufdruck
def rand_pruefen(plan):
    """Rendert jede Heftseite und prüft, ob der obere (sonst der untere) Streifen frei ist.
    Ergebnis: Bandseite → 'oben' | 'unten' | None. Der Streifen reicht über die ganze Breite des
    Aufdrucks einschließlich der Marke."""
    import pypdfium2 as pdfium
    lage = {}
    for h in plan.hefte.values():
        pdf = pdfium.PdfDocument(str(h["datei"]))
        for i in range(h["seiten"]):
            seite = pdf[i]
            b = seite.get_size()
            if abs(b[0] - BREITE) > 2 or abs(b[1] - HOEHE) > 2:
                raise SystemExit(f"{h['kennung']} S. {i + 1}: Format {b} ist nicht A4 hoch")
            img = seite.render(scale=1).to_pil().convert("L")
            band = h["offset"] + i + 1
            gewaehlt = None
            for name, st in (("oben", STEMPEL_OBEN), ("unten", STEMPEL_UNTEN)):
                y0, y1 = st["streifen"]
                # Bild-y läuft von oben; PDF-y von unten
                ausschnitt = img.crop((STEMPEL_X[0] - 6, int(HOEHE - y1), STEMPEL_X[1] + 6, int(HOEHE - y0)))
                if ausschnitt.getextrema()[0] >= WEISS:
                    gewaehlt = name; break
            lage[band] = gewaehlt
    return lage


def aufdruck_bauen(plan, k, f, lage, mit_marke):
    """Ein Overlay je Heftseite mit Kolumnentitel (links Heft und Abschnitt, rechts Bandseite, davor bei
    mit_marke die Marke zurück zum Inhalt); leere Seite, wo kein Rand frei ist.
    Gibt (PDF-Bytes, Marken: Bandseite → Rechteck der Marke)."""
    puffer = io.BytesIO()
    c = canvas.Canvas(puffer, pagesize=A4)
    marken = {}
    for h in plan.hefte.values():
        for i in range(h["seiten"]):
            band = h["offset"] + i + 1
            wo = lage.get(band)
            if wo:
                basis = (STEMPEL_OBEN if wo == "oben" else STEMPEL_UNTEN)["basis"]
                heft, abschnitt = plan.seite_titel[band]
                c.setFont(f["normal"], STEMPEL_GROESSE); c.setFillGray(GRAU)
                rechts = f"Band S. {band}"
                b_rechts = breite(rechts, f["normal"], STEMPEL_GROESSE)
                b_marke = breite(MARKE, f["normal"], STEMPEL_GROESSE) + MARKE_ABSTAND if mit_marke else 0
                links = f"{k['praefix']} {anzeige(heft)}" + (f"  ·  {abschnitt}" if abschnitt else "")
                links = kuerzen(links, f["normal"], STEMPEL_GROESSE,
                                STEMPEL_X[1] - STEMPEL_X[0] - b_rechts - b_marke - 20)
                c.drawString(STEMPEL_X[0], basis, links)
                c.drawRightString(STEMPEL_X[1], basis, rechts)
                if mit_marke:
                    x = STEMPEL_X[1] - b_rechts - b_marke
                    blau(c); c.drawString(x, basis, MARKE)
                    marken[band] = (x - 2, basis - 2.5, x + breite(MARKE, f["normal"], STEMPEL_GROESSE) + 2,
                                    basis + STEMPEL_GROESSE + 1)
                schwarz(c)
            c.showPage()
    c.save()
    return puffer.getvalue(), marken


# ---------------------------------------------------------------- Zusammenbau
def link_setzen(writer, seite_idx, rect, ziel_band):
    """Interner Link; das Ziel wird als Seitenreferenz geschrieben (pypdf bis 6.18 ließ in /Dest den
    Seitenindex als Zahl stehen, was nicht jeder Betrachter auflöst)."""
    ann = writer.add_annotation(page_number=seite_idx,
                                annotation=Link(rect=rect, target_page_index=ziel_band - 1, border=[0, 0, 0]))
    dest = ann.get("/Dest")
    if isinstance(dest, ArrayObject) and isinstance(dest[0], NumberObject):
        ann[NameObject("/Dest")] = ArrayObject([writer.pages[ziel_band - 1].indirect_reference, *dest[1:]])


def heftseiten_anfuegen(writer, plan, aufdruck_pdf, lage, nur_heft=None):
    """Heftseiten (alle Hefte oder eines) mit Overlay in den Writer; frische Reader je Aufruf,
    weil merge_page die Seite des Readers verändert."""
    aufdruck = PdfReader(io.BytesIO(aufdruck_pdf))
    for h in plan.hefte.values():
        if nur_heft and h is not nur_heft:
            continue
        rd = PdfReader(str(h["datei"]))
        for i, p in enumerate(rd.pages):
            box = p.mediabox
            if float(box.left) != 0 or float(box.bottom) != 0:
                raise SystemExit(f"{h['kennung']} S. {i + 1}: MediaBox-Ursprung {box} ungleich (0, 0)")
            band = h["offset"] + i + 1
            if lage.get(band):
                p.merge_page(aufdruck.pages[band - plan.vorspann - 1])
            writer.add_page(p)


def einzelhefte_bauen(plan, k, aufdruck_ohne_marke, lage, titel_band):
    """Je Heft eine Datei baende/<profil>-einzeln/<jahr>-<papier>.pdf mit Kolumnentiteln und
    Bandseitenzahlen; Seitenlabels = Bandseiten, Lesezeichen je Abschnitt."""
    ordner = HIER / k["einzeln"]
    ordner.mkdir(parents=True, exist_ok=True)
    dateien = []
    for h in plan.hefte.values():
        w = PdfWriter()
        heftseiten_anfuegen(w, plan, aufdruck_ohne_marke, lage, nur_heft=h)
        n = len(w.pages)
        for a in h["abschnitte"]:
            w.add_outline_item(a["titel"], a["von"] - h["offset"] - 1)
        w.set_page_label(0, n - 1, style="/D", start=h["offset"] + 1)
        w.add_metadata({
            "/Title": f"{k['praefix']} {anzeige(h['kennung'])} · {h['titel']} – Bandseiten "
                      f"{h['offset'] + 1}–{h['offset'] + n} aus: {titel_band}",
            "/Subject": f"Einzelheft aus dem Sammelband {k['ausgabe']}; Seitenzahlen = Bandseiten",
            "/Creator": VERSION,
        })
        w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
        ziel = ordner / (h["kennung"].lower() + ".pdf")
        with open(ziel, "wb") as out:
            w.write(out)
        if len(PdfReader(str(ziel)).pages) != h["seiten"]:
            raise SystemExit(f"Einzelheft {ziel.name}: Seitenzahl weicht ab")
        dateien.append(ziel)
    return dateien


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in KONFIG:
        raise SystemExit(f"Aufruf: python band-bau.py <{'|'.join(KONFIG)}>")
    profil = sys.argv[1]
    k = KONFIG[profil]
    f = schriften()

    liste = strukturliste(HIER / k["struktur"])
    plan = Plan(liste, k)
    zeilen = katalog([HIER / p for p in k["kataloge"]])
    typen = typenliste(HIER / k["typen"])
    herk = herkunft()

    print(f"Band {profil}: {len(plan.hefte)} Hefte, {plan.heftseiten} Heftseiten, Vorspann {plan.vorspann} Seiten, "
          f"Hefte ab S. {plan.vorspann + 1}; Katalog {len(zeilen)} Zeilen, Typenliste {len(typen)} Typen; "
          f"Herkunft {herk['repo']} {herk['commit']}"
          + (f" ({len(herk['geaendert'])} nicht committete Änderungen)" if herk["geaendert"] else ""))

    # Randprüfung
    lage = rand_pruefen(plan)
    oben = sum(1 for v in lage.values() if v == "oben")
    unten = [s for s, v in lage.items() if v == "unten"]
    keiner = [s for s, v in lage.items() if v is None]
    print(f"Randprüfung: oberer Rand frei auf {oben} von {len(lage)} Seiten"
          + (f"; Aufdruck unten auf S. {unten}" if unten else "")
          + (f"; kein Aufdruck auf S. {keiner}" if keiner else ""))

    # Vorspann: Inhalt und Register zuerst setzen (Seitenzahlen stehen auf dem Titelblatt)
    inhalt_pdf, inhalt_links, inhalt_seiten = inhalt_bauen(plan, k, f)
    reg, nicht_im_band, ohne_typ = register_daten(plan, zeilen, typen, k)
    register_pdf, register_links, register_seiten = register_bauen(reg, f)
    plan.register_ab = 2 + inhalt_seiten
    reserve = plan.vorspann - 1 - inhalt_seiten - register_seiten
    if reserve < 0:
        raise SystemExit(f"Inhalt ({inhalt_seiten}) und Register ({register_seiten}) brauchen "
                         f"{1 + inhalt_seiten + register_seiten} Seiten, Vorspann hat {plan.vorspann} – "
                         f"KONFIG vorspann_seiten erhöhen (verschiebt alle Bandseiten).")
    titel_pdf, titel_links = titelblatt_bauen(plan, k, f, inhalt_seiten, register_seiten, herk)
    reserve_pdf = reserve_bauen(reserve, f)
    aufdruck_pdf, marken = aufdruck_bauen(plan, k, f, lage, mit_marke=True)
    aufdruck_ohne_pdf, _ = aufdruck_bauen(plan, k, f, lage, mit_marke=False)

    writer = PdfWriter()
    for teil in (titel_pdf, inhalt_pdf, register_pdf, reserve_pdf):
        for p in PdfReader(io.BytesIO(teil)).pages:
            writer.add_page(p)
    if len(writer.pages) != plan.vorspann:
        raise SystemExit(f"Vorspann hat {len(writer.pages)} Seiten statt {plan.vorspann}")
    heftseiten_anfuegen(writer, plan, aufdruck_pdf, lage)
    gesamt = len(writer.pages)
    if gesamt != plan.bandende:
        raise SystemExit(f"Seitenzahl {gesamt} passt nicht zum Plan ({plan.bandende})")

    # Lesezeichen
    writer.add_outline_item("Titel und Hinweise", 0)
    writer.add_outline_item("Inhalt", 1)
    writer.add_outline_item("Register", plan.register_ab - 1)
    for jahr in plan.jahrgaenge:
        el_j = writer.add_outline_item(jahr[1], (jahr[2] or 1) - 1)
        for h in plan.hefte.values():
            if not h["kennung"].startswith(jahr[0] + "-"):
                continue
            el_h = writer.add_outline_item(f"{anzeige(h['kennung'])} · {h['titel']}", h["offset"], parent=el_j)
            for a in h["abschnitte"]:
                writer.add_outline_item(a["titel"], a["von"] - 1, parent=el_h)
    writer.page_mode = "/UseOutlines"

    # Links: Titelblatt (Index 0), Inhalt (ab 1), Register (ab register_ab − 1), Marken auf den Heftseiten
    for idx, rect, ziel in titel_links:
        link_setzen(writer, idx, rect, ziel)
    for idx, rect, ziel in inhalt_links:
        link_setzen(writer, 1 + idx, rect, ziel)
    for idx, rect, ziel in register_links:
        link_setzen(writer, plan.register_ab - 1 + idx, rect, ziel)
    for band, rect in marken.items():
        link_setzen(writer, band - 1, rect, 2)

    # Seitenlabels = Bandseite (Voreinstellung wäre dieselbe Zählung; ausdrücklich gesetzt)
    writer.set_page_label(0, gesamt - 1, style="/D")

    jahre = [j[0] for j in plan.jahrgaenge]
    titel_band = f"{k['titel']} – {k['untertitel'].format(von=jahre[0], bis=jahre[-1])}"
    writer.add_metadata({
        "/Title": titel_band,
        "/Subject": f"Sammelband {profil}: {len(plan.hefte)} Hefte, Originalseiten mit Inhalt und Register; "
                    f"Repo {herk['repo']}, Commit {herk['commit']}"
                    + (" (Arbeitskopie mit Änderungen)" if herk["geaendert"] else ""),
        "/Creator": VERSION,
    })

    ziel = HIER / k["ausgabe"]
    ziel.parent.mkdir(parents=True, exist_ok=True)
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    with open(ziel, "wb") as out:
        writer.write(out)

    # Rücklesen
    rd = PdfReader(str(ziel))
    if len(rd.pages) != gesamt:
        raise SystemExit("Rücklesen: Seitenzahl weicht ab")
    einzeln = einzelhefte_bauen(plan, k, aufdruck_ohne_pdf, lage, titel_band)

    n_jahrgaenge = len(plan.jahrgaenge)
    je_jahrgang = (inhalt_seiten + register_seiten) / n_jahrgaenge if n_jahrgaenge else 0
    print(f"Geschrieben: {ziel.relative_to(HIER)} · {gesamt} Seiten ({ziel.stat().st_size / 1e6:.1f} MB) · "
          f"Inhalt {inhalt_seiten} Seiten ab S. 2, Register {register_seiten} Seiten ab S. {plan.register_ab}, "
          f"Reserve {reserve} Seiten, {len(titel_links) + len(inhalt_links) + len(register_links)} Links im Vorspann, "
          f"{len(marken)} Marken auf Heftseiten")
    print(f"Reserve: Inhalt und Register brauchen {inhalt_seiten + register_seiten} Seiten für {n_jahrgaenge} Jahrgänge "
          f"({je_jahrgang:.2f} je Jahrgang); {reserve} Reserveseiten tragen nach linearer Rechnung etwa "
          f"{int(reserve / je_jahrgang) if je_jahrgang else 0} weitere Jahrgänge (Messung: band-anleitung.md § 5)")
    print(f"Einzelhefte: {len(einzeln)} Dateien nach {k['einzeln']}/ (Seitenlabels = Bandseiten)")
    print("Seitenkarte (Heft: Bandseiten, Offset):")
    for h in plan.hefte.values():
        print(f"  {anzeige(h['kennung'])}: S. {h['offset'] + 1}–{h['offset'] + h['seiten']} (+{h['offset']})")
    vork = sum(len(fu) for th in reg.values() for ty in th.values() for fu in ty.values())
    print(f"Register: {len(reg)} Leitideen, {sum(len(t) for t in reg.values())} Themen, "
          f"{sum(len(ty) for th in reg.values() for ty in th.values())} Typen, {vork} Fundstellen")
    if nicht_im_band:
        print(f"Katalogzeilen ohne Heft im Band ({len(nicht_im_band)}): {', '.join(nicht_im_band[:10])}"
              + (" …" if len(nicht_im_band) > 10 else ""))
    if ohne_typ:
        print(f"Typen nicht in der Typenliste ({len(ohne_typ)}): {'; '.join(ohne_typ[:10])}")


if __name__ == "__main__":
    main()
