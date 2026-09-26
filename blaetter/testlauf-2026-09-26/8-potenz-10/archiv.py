# archiv.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (ein Aufruf)
import glob, os, re, subprocess, zipfile

THEMA = "PotenzUndExponentialFkt"
DATUM = "2026-09-26"
os.environ["PATH"] = os.path.expandvars(r"%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64;") + os.environ["PATH"]

def lies(p):
    return open(p, encoding="utf-8").read()

sty2 = lies("mathblatt.sty").splitlines()[1].lstrip("% ").strip()
kat2 = lies("potenz-exponentialfunktionen.md").splitlines()[1].strip()

# --- Zählung aus der Textextraktion der Kompilate ---
def text(pdf):
    return subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", pdf, "-"], capture_output=True).stdout.decode("utf-8")

def seiten(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True).stdout.decode("utf-8", "replace")
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))

def grafiken(quellen):
    n = 0
    for q in quellen:
        t = lies(q)
        n += len(re.findall(r"\\begin\{ksys\}", t)) + len(re.findall(r"\\leeresgitter\{", t))
    return n

def zaehle_aufgaben(pdf, quellen):
    t = text(pdf)
    # Abhakseite nicht mitzählen
    t = t.split("Das kann ich\nKennst du schon")[0] if "Das kann ich\nKennst du schon" in t else t
    teile_ab = re.split(r"\n\s*Das kann ich\s*\n", t)
    t = teile_ab[0]
    haupt = len(re.findall(r"(?m)^\s*\d{1,2}\. (?:Ich|$)", t))
    teil = len(re.findall(r"(?:(?<=\s)|^)[a-l]\)\s", t))
    return haupt, teil, grafiken(quellen), seiten(pdf)

zeilen_zaehl = []
for pdf, quellen, name in [
    (THEMA + "_KennstDuSchon.pdf", ["zone_a.tex"], "Zone"),
    (THEMA + "_Lernblatt.pdf", ["e%d_a.tex" % i for i in range(1, 6)], "Lernblatt"),
    (THEMA + "_Gesamt.pdf", ["zone_a.tex"] + ["e%d_a.tex" % i for i in range(1, 6)], "Gesamt")]:
    h, tl, g, s = zaehle_aufgaben(pdf, quellen)
    zeilen_zaehl.append("%s (%s): %d Hauptnummern, %d Teilaufgaben, %d Grafiken (ksys/Gitter, aus dem Quelltext gezählt), %d Seiten" % (name, pdf, h, tl, g, s))
tl = text(THEMA + "_Loesungen.pdf")
nl = sorted(set(int(x) for x in re.findall(r"(?m)^\s*(\d{1,2})\)", tl)))
zeilen_zaehl.append("Lösungen (%s): Lösungen zu %d Nummern (%d–%d), %d Seiten" % (THEMA + "_Loesungen.pdf", len(nl), nl[0], nl[-1], seiten(THEMA + "_Loesungen.pdf")))
verz_l = lies("verz_lernblatt.tex").strip()
verz_g = lies("verz_gesamt.tex").strip()

# --- Zeiten ---
st = {}
for z in lies("zeiten.txt").splitlines():
    if z.strip():
        k, v = z.rsplit(" ", 1)
        st[k] = int(v)
t0 = st["t0"]
def dz(k):
    return ("%d s" % (st[k] - t0)) if k in st else "Stempel fehlt"
zeiten = ["Zone: " + dz("zone"), "Weiter: " + dz("weiter") + " (kein Klick im Testlauf; Stempel des ersten Aufrufs nach der Zone)"]
for i in range(1, 6):
    zeiten.append("E %d: %s" % (i, dz("e %d" % i)))
zeiten += ["Lernblatt: " + dz("lernblatt"), "Gesamt: " + dz("gesamt"), "Lösungen: " + dz("loesungen")]

ZWEIGE = [
    ("Einheit 1 von 5 · Lineares und exponentielles Wachstum unterscheiden",
     "Hier lernst du, lineares und exponentielles Wachstum an Tabelle, Text und Graph zu unterscheiden · neu in diesem Jahr · P10 oft · baut auf: Punkte eintragen, gleicher Betrag je Schritt, Erhöhen um p %", "e1_a.tex"),
    ("Einheit 2 von 5 · Wachstumsfaktor und Wachstumstabelle",
     "Hier lernst du, aus einem Prozentsatz den Wachstumsfaktor zu bilden und Wachstumstabellen zu ergänzen · neu in diesem Jahr · P10 oft · baut auf: Differenz oder Quotient (Einheit 1), Erhöhen um p %, Quotient zweier Werte", "e2_a.tex"),
    ("Einheit 3 von 5 · Exponentialfunktion aufstellen und auswerten",
     "Hier lernst du, eine Wachstumsgleichung N(t) = N₀ · qᵗ aufzustellen, zu deuten und damit Werte und Schwellen zu berechnen · neu in diesem Jahr · P10 · baut auf: Wachstumsfaktor und Tabelle (Einheit 2), Potenz mit dem Taschenrechner", "e3_a.tex"),
    ("Einheit 4 von 5 · Verdopplungs- und Halbwertszeit",
     "Hier lernst du, die Zeit zu bestimmen, nach der sich ein Wert verdoppelt oder halbiert hat · neu in diesem Jahr · P10 · baut auf: Wachstumstabelle (Einheit 2), Wachstumsgleichung (Einheit 3), Werte am Graphen ablesen", "e4_a.tex"),
    ("Einheit 5 von 5 · Potenzfunktionen mit natürlichem Exponenten",
     "Hier lernst du Potenzfunktionen wie y = x³ und y = x⁴ kennen: Wertetabelle, Graph, Symmetrie und Funktionswerte · neu in diesem Jahr (am Gymnasium schon seit Klasse 9) · keine P10-Aufgabe · baut auf: Potenz mit dem Taschenrechner, Punkte eintragen, Normalparabel", "e5_a.tex"),
]

def titel(q):
    t = lies(q)
    n = int(re.search(r"\\setcounter\{aufgabe\}\{(\d+)\}", t).group(1))
    out = []
    for m in re.finditer(r"\\begin\{aufgabe\}\{(.*?)\}\n", t):
        n += 1
        out.append("  %d. %s" % (n, m.group(1).replace("$x$", "x")))
    return out

SCHRITTE = """1 · Read unterrichtsblatt.md Zeilen 1–754 · Prompt lesen
2 · Read unterrichtsblatt.md Zeilen 755–1448 · Prompt zu Ende lesen
3 · PowerShell · Zeitstempel t0
4 · PowerShell curl · Themenregister und Register der Blätter holen (1.2)
5 · Grep · Register nach potenz/exponential durchsuchen (Ausgabe zu groß für die Anzeige)
6 · Grep · Zeile potenz-exponentialfunktionen im Register suchen
7 · Read · Register der Blätter lesen (Thema nicht geführt → mit Ausblick)
8 · PowerShell · Registerzeile des Themas ausgeben (lange Zeile)
9 · PowerShell curl · Eintrag potenz-exponentialfunktionen.md holen und speichern
10 · Read · Eintrag Zeilen 1–92
11 · Read · Eintrag Zeilen 93–151 (Offene Punkte und Prüfliste mitgelesen, da im selben Leseschritt)
12 · PowerShell curl · mathblatt.sty und Anleitung_mathblatt.md holen
13 · Read · Anleitung Zeilen 1–275
14 · Read · Anleitung Zeilen 276–391
15 · PowerShell · Vorrechnung der Aufgabenwerte – Ergebnis: SyntaxError (Anführungszeichen von python -c in PowerShell verschluckt)
16 · Write · vorrechnung.py
17 · PowerShell · vorrechnung.py ausführen (Zahlenwahl)
18 · Write · zone_a.tex
19 · Write · zone_l.tex
20 · Write · pruef.py (Zone)
21 · Write · Rahmen PotenzUndExponentialFkt_KennstDuSchon.tex
22 · Write · probe_l.tex (Prüfrahmen Lösungen)
23 · PowerShell · Zone: pruef.py (0 Abweichungen), kompilieren, Log, Text; Stempel zone
24 · Edit · Korrektur: Kopfzeile „Potenz- und Exponentialfunktionen · Kennst du schon · Kennst du schon“ doppelt – Versuch mit leerer Blattbezeichnung
25 · PowerShell · neu kompilieren, Seiten 1–2 rendern – Ergebnis „· ·“, Versuch verworfen
26 · Edit · Blattbezeichnung zurück auf „Kennst du schon“
27 · Read · Render Zone Seite 1
28 · Read · Render Zone Seite 2 – Nr. 6 d) Zeile sichtbar gedehnt vor den drei Feldern
29 · Edit · zone_a.tex Nr. 6 d): \\\\ vor die Felder
30 · PowerShell · Zone neu kompilieren (Zone fertig)
31 · PowerShell · Stempel weiter
32 · Write · e1_a.tex
33 · Write · e1_l.tex
34 · Edit · pruef.py Einheit 1
35 · Edit · pruef.py Zeile 28a entfernt (Größenordnung als Sonderprüfung)
36 · Edit · pruef.py Sonderprüfungen einhängen
37 · Edit · e1_l.tex 28a: „viele Millionen Kilometer“ → „fast 10 000 km“ (Skript: ≈ 9900 km)
38 · Write · probe_a.tex (Prüfrahmen Aufgaben, mit \\leeresgitter)
39 · Write · pruefe_einheit.ps1 (Prüfen, Kompilieren, Log, Seitenzählung, Rendern)
40 · PowerShell · E1 prüfen (0 Abweichungen), kompilieren, 7 Seiten rendern
41 · Read · Render E1 Seite 1
42 · Read · Render E1 Seite 3
43 · Read · Render E1 Seite 4 – Label J fehlt im Fisch-Graphen (\\funktion-Label am rechten Rand verschwunden)
44 · Read · Render E1 Seite 5 – Nr. 23 allein auf der Seite (331 Zeichen, überwiegend leer)
45 · Read · Render E1 Seite 6
46 · PowerShell · Korrektur E1: Labels J und E als \\node, Nr. 23 ymax 900 → 500; neu prüfen (0 Abweichungen, 6 Seiten)
47 · Read · Render E1 Seite 4 (Nr. 22 und 23 zusammen)
48 · Read · Render E1 Seite 3
49 · Edit · pruefe_einheit.ps1: Parameter Stempel
50 · Edit · pruefe_einheit.ps1: alte Renders löschen, Stempel setzen
51 · Write · e2_a.tex
52 · Write · e2_l.tex
53 · Edit · pruef.py Einheit 2
54 · PowerShell · E2 prüfen (0 Abweichungen); Stempel e 2 – Log: „! Missing $ inserted“, „! Display math should end with $$“ (leere Zeitangabe in \\wertetabelle)
55 · PowerShell · Korrektur E2: leere x-Einträge als {\\;}; neu prüfen, Seiten 2–3 rendern
56 · Read · Render E2 Seite 3
57 · Read · Render E2 Seite 2
58 · Write · e3_a.tex
59 · Write · e3_l.tex
60 · Edit · pruef.py Einheit 3
61 · PowerShell · E3 prüfen (0 Abweichungen); Stempel e 3 – Anweisung „auf zwei Nachkommastellen“ passt nicht zu Einwohnern (44 f); Seite 3 mit 588 Zeichen überwiegend leer
62 · PowerShell · Korrektur E3: Anweisung „runde erst am Ende sinnvoll“, \\clearpage vor Nr. 47; neu prüfen
63 · Write · e4_a.tex
64 · Write · e4_l.tex
65 · Edit · pruef.py Einheit 4
66 · PowerShell · E4 prüfen (0 Abweichungen), rendern; Stempel e 4 – Log: „! LaTeX Error: There's no line here to end.“ (2×, \\\\ nach \\wertetabelle in Nr. 55)
67 · Read · Render E4 Seite 1 – Nr. 51 d) gedehnt in teilezwei
68 · Read · Render E4 Seite 2 – Nr. 54 e), f) gedehnt in teilezwei
69 · PowerShell · Korrektur E4: Nr. 51 und 54 in teile, Nr. 55 Text vor Tabelle; neu prüfen
70 · Write · e5_a.tex
71 · Write · e5_l.tex
72 · Edit · pruef.py Einheit 5
73 · PowerShell · E5 prüfen (0 Abweichungen), rendern; Stempel e 5 – \\punktprobenliste setzt „C(−3| − 27)“ mit Binärabstand
74 · Read · Render E5 Seite 2
75 · Read · Render E5 Seite 3 – Labels A und B in Nr. 65 überlagert
76 · PowerShell · Korrektur E5: negative Koordinaten geklammert, Labels in Nr. 65 als \\node; neu prüfen
77 · Read · Render E5 Seite 3
78 · Read · Render E5 Seite 1
79 · Write · gen_abhaken.py (Abhakseite und Verzeichniszeilen aus den Quelltexten)
80 · Write · Rahmen Lernblatt
81 · Write · Rahmen Gesamt
82 · Write · Rahmen Lösungen
83 · PowerShell · Abhakseite erzeugen, Lernblatt zweimal kompilieren, Kopfzeilen und Nummern prüfen; Stempel lernblatt
84 · PowerShell · Gesamt zweimal kompilieren, Abhakseite prüfen; Stempel gesamt
85 · PowerShell · Lösungen kompilieren, Nummern 1–69 prüfen; Stempel loesungen
86 · Write · archiv.py
87 · PowerShell · protokoll.txt, chat.txt schreiben und Archiv packen"""
KORR = [24, 25, 26, 29, 30, 46, 55, 62, 69, 76]
n_schritte = len(SCHRITTE.splitlines())

AUSGABE = [
    "Abweichungen: kein Ausblick-Zweig (alle Marken bei Kl. 10 oder davor) · geteilte Hauptnummern: 23/24, 34/35/36, 58/59 · im Vorspann definiert: \\leeresgitter (leeres Karo ohne Bezifferung für Nr. 25 „Achseneinteilung wählen“) · Einheit 5: Kette, Fehler finden und Decke nach Lehrwerk-Konvention (Eintrag ohne Sprossen, Fehler und Zielmarke, keine P10-Aufgabe) · Zwischensprosse 33 f (Wachstumsrate aus zwei nicht benachbarten Werten über q²) · Logarithmus (Vorrat) als oberste Sprosse 54 h · Kopfzeile der Zonen-Datei trägt „Kennst du schon“ doppelt (Kurzform der Vorlage zusätzlich zur Blattbezeichnung) · Zeiten: Stempel „e 1“ fehlt (nicht im Prüfaufruf gesetzt), „weiter“ ohne Klick",
    "Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (Fertigkeiten und Erkennungsschritte), Sprossen, Typische Fehler, Prüfungsform/Zielmarke; nicht gebraucht Merkkasten, Verortung, Grundvorstellung; gefehlt: Einheit 5 ohne Sprossen, Typische Fehler, Zielmarke und Blatt-0-Fertigkeit · Befund: Erkennungsschritte „Differenz oder Quotient?“ und „Welcher Schritt ist null?“ verlangen Zahlen – als Vorstufe ohne Ergebnis gesetzt (Nr. 14 mit vorgedruckten Differenzen und Quotienten, Nr. 40 nur Startjahr und Zieljahr markieren), das Rechnen steht in Nr. 16/17 und 44 f · keine Marke mit Spanne; Einheit 5 (OS 10 · GYM 9) als „neu in diesem Jahr (am Gymnasium schon seit Klasse 9)“; „nicht für alle“-Zusätze ohne Klassenzahl (Sekundo LVL/Zusatzstoff) nicht auf dem Blatt",
    "Protokoll-Archiv: %s_%s_protokoll.zip" % (THEMA, DATUM),
]
DATEIEN = [THEMA + "_KennstDuSchon.pdf", THEMA + "_Lernblatt.pdf", THEMA + "_Gesamt.pdf", THEMA + "_Loesungen.pdf"]

p = []
p += ["Prompt: Unterrichtsblatt-Prompt v4.4", "Modell: Opus 5.5 (claude-opus-5-5)", "Vorlage: " + sty2,
      "Katalog: potenz-exponentialfunktionen.md, " + kat2, "Bestellung: mit Wiederholung · mit Ausblick (kein Ausblick-Zweig: alle Marken bei Kl. 10 oder davor)",
      "Standpunkt: Kl. 10, Oberschule (ohne Schulform in der Eingabe; Gymnasium als Zusatz)", ""]
p += ["Zweige (gebaut: alle 5; abgewählt: keine; Ausblick: keiner):"]
p += ["Zone · Kennst du schon"] + titel("zone_a.tex")
for kopf, zz, q in ZWEIGE:
    p += [kopf, "  Zweigzeile: " + zz] + titel(q)
p += ["", "Zählung aus der Textextraktion:"] + zeilen_zaehl
p += ["Verzeichniszeile Lernblatt: " + verz_l, "Verzeichniszeile Gesamt: " + verz_g, ""]
p += ["Werkzeugaufrufe (Schritt · Anlass):"] + SCHRITTE.splitlines() + [""]
p += ["Vorlage: fehlende Bausteine · \\leeresgitter (leeres Achsenkreuz mit Karo ohne Bezifferung, für „Achseneinteilung wählen“); Warnungen aus dem Log · keine Package-mathblatt-Warnung; Kopfzeile der Zonen-Datei doppelt „Kennst du schon · Kennst du schon“", ""]
p += ["Korrekturrunden: %d von %d Schritten (Schritte %s)" % (len(KORR), n_schritte, ", ".join(map(str, KORR)))] + zeiten
open("protokoll.txt", "w", encoding="utf-8").write("\n".join(p) + "\n")

c = ["Eingabe: potenz-exponentialfunktionen 10 – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch", "",
     "→ Lernblatt · Kl. 10 Oberschule, Gymnasium als Zusatz · mit Wiederholung · mit Ausblick: kein Zweig nach Kl. 10 · 5 Zweige · Zone aus 8 Fertigkeiten"]
for kopf, zz, q in ZWEIGE:
    c += [kopf + " — " + zz]
c += ["Alle Zweige, oder welche? (alle · Nummern · ein Typ für den Fokus)", "Antwort: alle", "",
      THEMA + "_KennstDuSchon.pdf", "Weiter baut Einheit 1 bis 5, Gesamt und Lösungen.", "Antwort: weiter (aus der Eingabe)", ""]
c += DATEIEN[1:] + AUSGABE
open("chat.txt", "w", encoding="utf-8").write("\n".join(c) + "\n")

muster = ["*.pdf", "*.tex", "*.log", "pruef.py", "pruef_out_*.txt", "mathblatt.sty", "Anleitung_mathblatt.md",
          "potenz-exponentialfunktionen.md", "zeiten.txt", "protokoll.txt", "chat.txt", "gen_abhaken.py", "pruefe_einheit.ps1", "vorrechnung.py", "archiv.py"]
name = "%s_%s_protokoll.zip" % (THEMA, DATUM)
with zipfile.ZipFile(name, "w", zipfile.ZIP_DEFLATED) as z:
    gesehen = set()
    for m in muster:
        for f in sorted(glob.glob(m)):
            if f not in gesehen:
                z.write(f)
                gesehen.add(f)
print(name, len(gesehen), "Dateien")
print("\n".join(zeilen_zaehl))
print("\n".join(zeiten))
