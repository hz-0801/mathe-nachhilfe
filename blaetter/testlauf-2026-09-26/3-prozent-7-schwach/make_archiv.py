# make_archiv.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3)
import re, glob, zipfile, subprocess, os

ZIP = "Prozentrechnung_2026-09-26_protokoll.zip"

# --- Kopf ---
sty2 = open("mathblatt.sty", encoding="utf-8").read().splitlines()[1]
vorlage = re.search(r"Version\s+(\S+)", sty2).group(1)
stand = open("prozentrechnung.md", encoding="utf-8").read().splitlines()[1]

DEUTUNG = ("→ Lernblatt · Kl. 7, Standpunkt Oberschule (Gymnasium als Zusatz) · mit Wiederholung, ohne Ausblick "
           "(Thema im Register der Blätter) · Einheit 1 „Prozente als Anteile“ (OS Kl. 6) liegt in der Zone · 4 Zweige · "
           "Zone aus 7 Fertigkeiten und dem Fehler-Paar (Nr. 1–11)")

def zweigzeilen():
    out = []
    for n in range(1, 5):
        s = open(f"e{n}_a.tex", encoding="utf-8").read()
        kopf = re.search(r"\\einheitenkopf\[[^\]]*\]\[[^\]]*\]\{([^}]*)\}", s).group(1)
        zz = re.search(r"\\zweigzeile\{(.*)\}\s*$", s, re.M).group(1).replace("Nr.~", "Nr. ")
        out.append((kopf, zz))
    return out

PLAN = "\n".join(f"{k.replace('Einheit ', '').replace(' von 4', '')}: {z}" for k, z in zweigzeilen())
PLANFRAGE = "Alle Zweige, oder welche? (alle · Nummern · ein Typ für den Fokus)"

AUSGABE = [
    "Zone: Einheit 1 des Eintrags (Prozente als Anteile, Marke OS Kl. 6) steht als Fertigkeit in der Zone (Nr. 1–3 mit der Grundvorstellung), nicht als Zweig; kein Ausblick-Zweig, weil das Register der Blätter das Thema führt.",
    "Zone: Grundvorstellung auf drei Hauptnummern verteilt (Nr. 1 ablesen, Nr. 2 einzeichnen, Nr. 3 von 10 % auf das Ganze), weil es drei Antwortformen sind.",
    "Geteilte Hauptnummern: 15/16, 18/19, 24/25, 44/45.",
    "Zwischensprossen: Nr. 16 d (erst kürzen, dann erweitern), Nr. 17 b (Teil als Dezimalzahl), Nr. 26 b (Ganzes unter 100, 1 % als Dezimalzahl), Nr. 37 b (Rest zu 100 % zuerst bilden).",
    "Prüfungshöhe nicht in der letzten Verfahrens-Hauptnummer: Einheit 2 in Nr. 29 (P10 2021 OS), weil Nr. 30 (über 100 %) eine eigene Fertigkeit ist; Einheit 4 in Nr. 47 (P10 2026 FOR) und Nr. 51 (P10 2025 OS), weil die Kette dort nach Form zerfällt.",
    "Typ „Mehrwertsteuer in Euro“ (Einheit 2) steht in keiner Kette und ist die Anwendung Nr. 33.",
    "Im Quelltext definiert: \\abhakverf (kursive Verfahrenszeile auf der Abhakseite über \\abhakgruppe), weil die Vorlage nur eine Gruppenebene kennt.",
    "Vorlage: Kopfzeile der Zone doppelt („Prozentrechnung · Kennst du schon · Kennst du schon“); \\dreieckrw setzt immer die Eckpunktnamen A, B, C (Nr. 51, gegen 3.6); Streifen in \\swz ragen 2–12 pt über den Satzspiegel (Overfull hbox).",
    "Stempel „e 2“ in eigenem Aufruf direkt nach der Durchsicht gesetzt, nicht im Prüfaufruf.",
    "Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (Fertigkeiten und Erkennungsschritte), Für schwache Schüler (Sprossen, Grundvorstellung), Typische Fehler, Prüfungsform/Zielmarke, Merkkasten (bei schwach am Zweigende); nicht gebraucht Verortung. Befunde: Einheit 1 trägt OS Kl. 6, zwei ihrer Typen aber [OS 7] – bei Kl. 7 Oberschule fällt sie in die Zone, obwohl Typen neu sind; die Ketten „Prozentsatz“ und „Grundwert“ nennen als Vorstufe Streifenaufgaben mit Zahlergebnis (als Verfahrens-Hauptnummern Nr. 14 und 35 gesetzt); Kettenlücken Kürzen vor dem Erweitern (Einheit 2) und Rest zu 100 % (Einheit 4). Spannen: Einheit 5 „OS Kl. 7–8“ bei Eingabeklasse 7 als „neu in diesem Jahr oder erst in Klasse 8 – je nach Buch“ aufgelöst (die Regel „neu oder schon bekannt“ passt an der unteren Grenze nicht); Typ „Prozentsatz über 100 %“ [OS 7–8] als „je nach Buch erst in Klasse 8“; Typklammern [OS 9] Faktor, [OS 10] Steigung, [OS 7] Brutto/Netto am Titel.",
    f"Protokoll-Archiv: {ZIP}",
]

DATEIEN = ["Prozentrechnung_KennstDuSchon.pdf", "Prozentrechnung_Lernblatt.pdf", "Prozentrechnung_Gesamt.pdf",
           "Prozentrechnung_Loesungen.pdf", ZIP]

# --- Hauptnummern mit Titel aus abhaken.tex ---
abh = open("abhaken.tex", encoding="utf-8").read()
titel = re.findall(r"\\abhak\{(\d+)\}\{(.*)\}", abh)
gruppen = {}
for n, t in titel:
    n = int(n)
    g = "Zone" if n <= 11 else "E1" if n <= 23 else "E2" if n <= 33 else "E3" if n <= 41 else "E4"
    gruppen.setdefault(g, []).append(f"  {n}. {t.replace(chr(92) + '%', '%')}")

# --- Zählung ---
zaehl = subprocess.run(["python" if False else os.environ.get("PYEXE", "python"), "zaehl.py"], capture_output=True, text=True, encoding="utf-8").stdout

# --- Zeiten ---
st = {}
for z in open("zeiten.txt", encoding="ascii").read().splitlines():
    k, v = z.rsplit(" ", 1)
    st[k] = int(v)
t0 = st["t0"]
zeiten = [f"Zone: {st['zone'] - t0} s"] + [f"E {n}: {st[f'e {n}'] - t0} s" for n in range(1, 5)] + \
         [f"Lernblatt: {st['lernblatt'] - t0} s", f"Gesamt: {st['gesamt'] - t0} s", f"Lösungen: {st['loesungen'] - t0} s",
          f"Weiter: {st['weiter'] - t0} s (Stempel des Weiter-Schritts; keine Wartezeit, der Testlauf baut ohne Halt durch)"]

SCHRITTE = """1 · Read unterrichtsblatt.md Teil 1 · Anleitung lesen
2 · Read unterrichtsblatt.md Teil 2 · Anleitung bis zur letzten Zeile lesen
3 · PowerShell · Arbeitsverzeichnis anlegen, Themenregister und Register der Blätter holen (1.2)
4 · Grep · Register nach „prozent“ durchsuchen (Abrufausgabe zu groß, ausgelagert)
5 · Read · Register der Blätter lesen – Bestellung klären (Thema geführt → ohne Ausblick)
6 · PowerShell · Stempel t0
7 · PowerShell · Eintrag prozentrechnung.md, mathblatt.sty und Anleitung holen
8 · Read · Eintrag lesen
9 · Read · Anleitung Teil 1
10 · Read · Anleitung ab Zeile 420 – leer (Datei hat 391 Zeilen)
11 · Read · Anleitung Teil 2
12 · Write · zone_a.tex
13 · Write · zone_l.tex
14 · Write · pruef.py (Zone)
15 · Write · Rahmendatei Zone
16 · Write · Rahmendatei Lösungen (vorläufig)
17 · PowerShell · pruef zone, Zone und Lösungen kompilieren, Log, rendern → 0 Abweichungen, 8 Seiten
18–25 · Read · Zone Seiten 1–8 ansehen (erster Lauf, Bausteine \\swz, \\swa, Streifen, Stellenwerttafel, Zahlenstrahl, Dreisatz)
26 · PowerShell · Textextraktion: Dezimalkomma geprüft (sah im Render wie Punkt aus) → Komma korrekt
27 · Edit · zone_a Nr. 5: vorbelegte Stellenwerttafel schmaler als die mit \\leerzelle, verrutscht → Zellen mit \\makebox
28 · Edit · zone_a Nr. 11: dasselbe
29 · PowerShell · Zone neu kompilieren (2 Läufe), Seite 4 rendern, Stempel zone
30 · Read · Zone Seite 4 ansehen
31 · PowerShell · Stempel weiter
32 · Write · e1_a.tex
33 · Write · e1_l.tex
34 · Edit · pruef.py Einheit 1
35 · Write · Rahmendatei Lernblatt (vorläufig, bindet vorhandene Einheiten ein)
36 · PowerShell · pruef e1, kompilieren, rendern → 0 Abweichungen; Overfull 23–27 pt bei Streifen mit „Ganzes: ___“
37–43 · Read · Lernblatt Seiten 1–7 ansehen
44 · Edit · e1_a: Lücke im Zähler als \\rule wirkte wie doppelter Bruchstrich → \\hspace
45 · Edit · e1_a: Streifenlabel „Ganzes: ___“ ragte über den Rand (Overfull hbox 23–27 pt) → nur Schreiblinie
46 · PowerShell · neu kompilieren, Seite 4–5 rendern, Stempel e 1
47 · Read · Seite 4 ansehen
48 · Write · e2_a.tex
49 · Write · e2_l.tex
50 · Edit · pruef.py Einheit 2
51 · PowerShell · pruef e2, kompilieren, rendern → 0 Abweichungen
52 · PowerShell · Namen der gerenderten Seiten auflisten
53–58 · Read · Seiten 8–13 ansehen
59 · PowerShell · Stempel e 2
60 · Write · e3_a.tex
61 · Edit · e3_a: Prüfungshöhe Nr. 38 d als \\swz statt teile mit \\rechenplatz (Rechenplatz ist Gerüstplatz des Lehrers)
62 · Write · e3_l.tex
63 · Edit · pruef.py Einheit 3
64 · PowerShell · pruef e3, kompilieren, rendern → 0 Abweichungen
65–70 · Read · Seiten 14–19 ansehen
71 · Edit · e3_a: Seite 19 trug nur den Merkkasten (unter 1/3 gefüllt) → \\clearpage vor Nr. 41
72 · PowerShell · neu kompilieren, Seite 19 rendern, Stempel e 3
73 · Read · Seite 19 ansehen
74 · Write · e4_a.tex
75 · Edit · e4_a Nr. 50 b: Darstellung auf den alten Wert als Ganzes umgestellt
76 · Write · e4_l.tex
77 · Edit · pruef.py Einheit 4
78 · PowerShell · pruef e4, kompilieren, rendern → 0 Abweichungen
79–86 · Read · Seiten 20–27 ansehen
87 · Edit · e4_a Nr. 51 a: \\dreieckrw beschriftete „100 m“ an der Höhe → Labels getauscht
88 · Edit · e4_a Nr. 51 b: dasselbe
89 · PowerShell · neu kompilieren, Seite 25 rendern, Stempel e 4
90 · Read · Seite 25 ansehen
91 · Write · abhaken.tex (Handform, Zweige und Verfahren)
92 · Write · Rahmendatei Lernblatt mit Verzeichniszeile
93 · PowerShell · Lernblatt kompilieren (2 Läufe), Textextraktion, rendern, Stempel lernblatt
94–96 · Read · Lernblatt Seite 1, 28, 29 ansehen (Verzeichniszeile, Abhakseite)
97 · Write · Rahmendatei Gesamt
98 · PowerShell · Gesamt kompilieren (2 Läufe), Textextraktion, Stempel gesamt
99 · Read · Gesamt Seite 1 ansehen
100 · Write · Rahmendatei Lösungen
101 · PowerShell · Lösungen kompilieren (2 Läufe), Textextraktion, Stempel loesungen
102 · Read · Lösungen Seite 1 ansehen
103 · Write · zaehl.py
104 · PowerShell · Zählung aus der Textextraktion, Seitenfüllung, Kopfzeilen
105 · PowerShell · Sprungziele der Verzeichniszeile mit pypdf gegen die Einheitenköpfe geprüft
106 · Write · make_archiv.py
107 · PowerShell · protokoll.txt und chat.txt schreiben, Archiv packen"""

verz_l = re.search(r"\\verzeichniszeile\{(.*)\}", open("Prozentrechnung_Lernblatt.tex", encoding="utf-8").read()).group(1)
verz_g = re.search(r"\\verzeichniszeile\{(.*)\}", open("Prozentrechnung_Gesamt.tex", encoding="utf-8").read()).group(1)

prot = []
prot += ["Prompt: Unterrichtsblatt-Prompt v4.4", "Modell: Claude Opus 5.5 (claude-opus-5-5)", f"Vorlage: {vorlage}",
         f"Katalog: prozentrechnung.md, {stand}", "Bestellung: mit Wiederholung (ohne Ausblick)",
         "Standpunkt: Kl. 7, Oberschule (Gymnasium als Zusatz); Option schwach", ""]
prot += ["Zweige (gebaut, alle nach Planfrage „alle“; abgewählt: keine; Ausblick: keiner; Katalog-Einheit 1 in der Zone):"]
for (k, z), g in zip(zweigzeilen(), ["E1", "E2", "E3", "E4"]):
    prot += [f"{k}", f"  {z}"] + gruppen[g]
prot += ["Zone „Das kennst du schon“:"] + gruppen["Zone"] + [""]
prot += ["Zählung aus der Textextraktion:", zaehl.strip(),
         f"Verzeichniszeile Lernblatt: {verz_l}", f"Verzeichniszeile Gesamt: {verz_g}", ""]
prot += ["Werkzeugaufrufe (Schritt · Anlass):", SCHRITTE, ""]
prot += ["Vorlage: fehlende Bausteine · keine; im Quelltext definiert: \\abhakverf (Hilfsbefehl über \\abhakgruppe) · Warnungen aus dem Log: keine „Package mathblatt Warning“; Overfull \\hbox 2–12 pt an Streifen in \\swz (rechte Spalte schmaler als 10 cm + Label); hyperref „Rerun“ nur im ersten Lauf", ""]
prot += ["Korrekturrunden: 4 von 8 Schritten (Zone, E1, E3, E4; E2, Lernblatt, Gesamt, Lösungen ohne)"] + zeiten
open("protokoll.txt", "w", encoding="utf-8").write("\n".join(prot) + "\n")

chat = []
chat += ["Eingabe des Lehrers:", "prozentrechnung 7 schwach – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch", ""]
chat += [DEUTUNG, PLAN, PLANFRAGE, "Antwort: alle", ""]
chat += ["Prozentrechnung_KennstDuSchon.pdf", "Weiter baut Einheit 1 bis 4, Gesamt und Lösungen.", "Antwort: weiter (aus der Eingabe)", ""]
chat += ["Ausgabeblock:"] + AUSGABE + ["", "Übergebene Dateien:"] + DATEIEN
open("chat.txt", "w", encoding="utf-8").write("\n".join(chat) + "\n")

pack = sorted(set(glob.glob("*.pdf") + glob.glob("*.tex") + glob.glob("*.log") + glob.glob("pruef_out_*.txt") +
                  ["pruef.py", "zaehl.py", "make_archiv.py", "mathblatt.sty", "Anleitung_mathblatt.md", "prozentrechnung.md",
                   "zeiten.txt", "protokoll.txt", "chat.txt"]))
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for f in pack:
        z.write(f)
print("\n".join(prot[-10:]))
print(f"{ZIP}: {len(pack)} Dateien")
