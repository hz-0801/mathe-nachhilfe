# archiv.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3)
import glob, os, re, subprocess, zipfile

def text(pdf):
    return subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", pdf, "-"], capture_output=True).stdout.decode("utf-8")

def seiten(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True).stdout.decode("utf-8", "replace")
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))

GRAFIK = r"\\(saeulenab|liniendia|balkenab|kreisleer|kreissektor|kreisdiagrammleer|streifen|winkelstrahl)\b|\\begin\{boxplots\}"

def grafiken(quellen):
    n = 0
    for q in quellen:
        src = "\n".join(l for l in open(q, encoding="utf-8").read().splitlines() if not l.lstrip().startswith("%"))
        n += len(re.findall(GRAFIK, src))
    return n

def zaehle(pdf, quellen, loesung=False):
    t = text(pdf)
    z = f"{pdf}: {seiten(pdf)} Seiten"
    if loesung:
        nr = sorted({int(m) for m in re.findall(r"^\s*(\d+)\)", t, re.M)})
        return z + f", Lösungen zu {len(nr)} Nummern ({nr[0]}–{nr[-1]})"
    haupt = re.findall(r"^\s*(\d+)\.\s+Ich", t, re.M)
    teil = re.findall(r"(?:^|\s)([a-j])\)\s", t, re.M)
    return z + (f", {len(haupt)} Hauptnummern ({haupt[0]}–{haupt[-1]}), {len(teil)} Teilaufgaben "
                f"(Regex „Buchstabe + Klammer“ über die Textextraktion; die Zeilenlabels a)–c) des Boxplot-Rasters in Nr. 33 zählen mit), "
                f"{grafiken(quellen)} Grafiken (aus dem Quelltext gezählt, Textextraktion zeigt keine Grafiken)")

def verzeichnis(pdf):
    zeilen = text(pdf).splitlines()
    z = [l.strip() for l in zeilen[1:6] if l.strip()]
    return " ".join(z[:2])

stempel = {}
for l in open("zeiten.txt", encoding="ascii").read().split("\n"):
    if l.strip():
        k, v = l.rsplit(" ", 1)
        stempel[k] = int(v)
t0 = stempel["t0"]
def dt(k): return f"{stempel[k] - t0} s" if k in stempel else "Stempel fehlt"

EINGABE = "daten 7 – Antworten auf Planfrage und Zone: sek i, alle; baue ohne Halt bis zum Ausgabeblock durch"
DEUTUNG = ("→ Lernblatt · Kl. 7, Standpunkt Oberschule (Gymnasium als Zusatz) · Sek I: Einheit 6 und die Sek-II-Zeilen weggelassen · "
           "mit Wiederholung, ohne Ausblick (das Register führt daten seit 22.09.): Einheit 7 Vierfeldertafel (Kl. 9) nicht gebaut · "
           "Einheit 1, 2 und 4 (Marke vor Kl. 7) als Fertigkeiten in der Zone · 2 Zweige · Zone aus 9 Fertigkeiten und dem Fehler-finden-Paar (Nr. 1–11)")
PLAN = [
    "Einheit 1 von 2 · Streifen- und Kreisdiagramm: Hier lernst du, Anteile als Streifen und als Kreisdiagramm darzustellen · neu oder schon bekannt – je nach Buch (am Gymnasium schon seit Klasse 6) · P10 oft · baut auf: Prozentsatz (Nr. 1–2), relative Häufigkeit (Nr. 3), Winkel (Nr. 5–6), Längen (Nr. 7)",
    "Einheit 2 von 2 · Diagramme beurteilen und Boxplot: Hier lernst du, Aussagen zu Diagrammen zu prüfen, Täuschungen zu erkennen und Boxplots zu lesen · neu oder schon bekannt – je nach Buch (am Gymnasium neu in diesem Jahr) · P10 · baut auf: Säulendiagramme lesen (Nr. 4), Kenngrößen (Nr. 8), Bruchteile (Nr. 9), Prozentsatz (Nr. 1)",
]
PLANFRAGE = ("Planfrage: keine – die Klasse 7 löst die Stufe (Sek I), der Plan hat weniger als vier Zweige. "
             "Antwort aus der Eingabe: „sek i, alle“ – deckt sich mit dem Plan (Sek I, alle Zweige).")
ZONEZEILE = "Weiter baut Einheit 1 bis 2, Gesamt und Lösungen."
DATEIEN = ["Daten_KennstDuSchon.pdf", "Daten_Lernblatt.pdf", "Daten_Gesamt.pdf", "Daten_Loesungen.pdf"]
ARCHIV = "Daten_2026-09-26_protokoll.zip"
AUSGABE = open("ausgabeblock.txt", encoding="utf-8").read().strip().splitlines()

TITEL = {}
for q in ["zone_a.tex", "e1_a.tex", "e2_a.tex"]:
    for m in re.finditer(r"\\begin\{aufgabe\}\{(.*)\}\s*$", open(q, encoding="utf-8").read(), re.M):
        TITEL.setdefault(q, []).append(m.group(1).replace("\\,", " ").replace("\\%", "%"))

SCHRITTE = """1 · Read unterrichtsblatt.md Z. 1–754 · Anleitung lesen (Systemanweisung)
2 · Read unterrichtsblatt.md Z. 755–1448 · Anleitung zu Ende lesen
3 · PowerShell · Arbeitsverzeichnis anlegen, Stempel t0
4 · PowerShell curl · Themenregister und Register der Blätter holen (1.2)
5 · Grep · Ausgabe zu lang (122 KB): Zeile „daten“ und Register der Blätter suchen
6 · PowerShell · Registerzeile daten.md und Blätter-Register ausgeben (daten seit 2026-09-22 gebaut → ohne Ausblick)
7 · PowerShell curl · Eintrag daten.md holen
8 · Read · daten.md Z. 1–103
9 · Read · daten.md Z. 104–200
10 · PowerShell curl · mathblatt.sty und Anleitung_mathblatt.md holen, Version Zeile 2 geprüft (2026-09-28a, gleich der Anleitung)
11 · Read · Anleitung Z. 1–275
12 · Read · Anleitung Z. 276–391
13 · Write · zone_a.tex
14 · Edit · zone_a.tex: Grad-Zeichen im Mathemodus ($360°$) vorsorglich in den Text gesetzt
15 · Write · zone_l.tex
16 · Write · Daten_KennstDuSchon.tex (Rahmen)
17 · Write · pruef.py (Zone, Einheit 1, Einheit 2)
18 · PowerShell · pruef.py zone (0 Abweichungen), xelatex ×2, pdftoppm, Stempel zone
19 · Read · Daten_KennstDuSchon.pdf S. 1–4 ansehen
20 · PowerShell · Korrektur: schließendes ASCII-Anführungszeichen vor Punkt verschluckt („nein. Anteil“ in Nr. 3 e, 11 b) → Unicode-Anführungszeichen
21 · Edit · Korrektur Nr. 5 e: Teilaufgabe in der teilezwei-Zelle sichtbar gedehnt („ein   Fünftel   des   Vollkreises“) → teile
22 · Edit · Korrektur Nr. 11 a: Feld umbrochen, Zeile sichtbar gedehnt → Feld in eigener Zeile
23 · Write · e1_a.tex
24 · Write · e1_l.tex
25 · Write · pruef_einheit.tex (Prüfrahmen je Einheit: Aufgaben und Lösungen)
26 · PowerShell · Stempel weiter, Zone neu kompiliert, pruef.py e1 (0 Abweichungen), xelatex ×2 Einheit 1
27 · Read · pruef_e1.pdf S. 1–7 ansehen
28 · PowerShell · Korrektur: „≈“ fehlt im Textfont der Lösungen (16 j, 21 d: „360° 138,5°“) → $\\approx$
29 · Write · e2_a.tex
30 · Edit · e2_a.tex Nr. 32 (damals 31): Quartile-Zelle für teilezwei zu lang, vor dem Kompilieren in teile
31 · Write · e2_l.tex
32 · Edit · pruef.py: Prüfzeile Kino (damals 30c) verglich Skript mit Skript statt mit dem Blattwert
33 · PowerShell · Einheit 1 neu (≈ per pdftotext geprüft), Stempel e 1, pruef.py e2 (0 Abweichungen), xelatex ×2 Einheit 2; Log: Overfull \\hbox (25.01337pt too wide) zweimal, Overfull \\hbox (14.37802pt too wide)
34 · Read · pruef_e2.pdf S. 1–8 ansehen
35 · Edit · Korrektur Nr. 29: Overfull \\hbox 25pt bei \\liniendia in zwei Spalten, und \\liniendia normiert die Höhe – gedehnte Achse über ystep nicht sichtbar → ymax 6 gegen 1,6, breite=0.9
36 · Edit · Korrektur Nr. 30: Hauptnummer mit zwei Grafiken über eine halbe Seite → geteilt in 30 und 31 „– weiter“ (Original in 31)
37 · Edit · Korrektur Nr. 32: Overfull \\hbox 14pt bei \\begin{boxplots} (xstep 0,1), Achsenzahlen winzig → Weiten in cm, xstep 10
38 · PowerShell · e2_l.tex umnummeriert (31–37), Lösungen 29 b und 32 angepasst
39 · PowerShell · pruef.py umnummeriert, Boxplotwerte in cm
40 · PowerShell · Korrektur pruef.py: Umnummerierung hatte die Kino-Zeilen auf 32a geschoben → 31a
41 · PowerShell · pruef.py e2 (0 Abweichungen), xelatex Einheit 2, Log ohne Overfull, Nummern 25–37 per pdftotext, Seiten 4–6 gerendert
42 · Read · pruef_e2.pdf S. 4–6 ansehen
43 · Write · abhaken.tex
44 · Write · Daten_Lernblatt.tex
45 · Write · Daten_Gesamt.tex
46 · Write · Daten_Loesungen.tex
47 · PowerShell · Stempel e 2, Lernblatt ×2, Stempel lernblatt, Gesamt ×2, Stempel gesamt, Lösungen, Stempel loesungen; Nummern, Kopfzeilen, Verzeichniszeile per pdftotext
48 · Read · Daten_Gesamt.pdf S. 1 (Verzeichniszeile, Zone)
49 · Read · Daten_Loesungen.pdf S. 1–2
50 · Read · Daten_Gesamt.pdf S. 18 (Abhakseite)
51 · Read · Daten_KennstDuSchon.pdf S. 2–4 (nach Korrektur 21/22 geänderte Seiten)
52 · Write · archiv.py
53 · Write · ausgabeblock.txt
54 · Edit · Korrektur e1_l.tex: Lösung 21 mit c)/d) beschriftet, auf dem Blatt beginnt Nr. 21 bei a)
55 · PowerShell · Lösungen neu kompiliert (Stempel loesungen bleibt aus Schritt 47), archiv.py: protokoll.txt, chat.txt, Zählung, Zip"""

sty2 = open("mathblatt.sty", encoding="utf-8").read().splitlines()[1].strip()
stand = open("daten.md", encoding="utf-8").read().splitlines()[1][:160]

P = []
P += ["Prompt: Unterrichtsblatt-Prompt v4.4", "Modell: Claude Opus 5.5 (claude-opus-5-5)",
      f"Vorlage: {sty2}", f"Katalog: daten.md, {stand} …",
      "Bestellung: mit Wiederholung (ohne Ausblick: das Register der Blätter führt daten)",
      "Standpunkt: Kl. 7, Oberschule (Gymnasium als Zusatz), Sek I", ""]
P += ["Zweige:", "gebaut: " + PLAN[0], "gebaut: " + PLAN[1],
      "in der Zone (Marke vor Kl. 7): Einheit 1 Häufigkeiten (OS Kl. 5–6) → Nr. 3 · Einheit 2 Säulen-, Balken- und Liniendiagramme (OS Kl. 5–6) → Nr. 4 · Einheit 4 Kenngrößen (OS Kl. 6) → Nr. 8",
      "weggelassen: Einheit 6 Kenngrößen aus Häufigkeitstabellen und Klassen (Sek II) · Einheit 7 Vierfeldertafel (OS Kl. 9, GYM Kl. 9–10) – Ausblick nicht bestellt",
      "abgewählt: keine", ""]
for q, kopf in [("zone_a.tex", "Zone Kennst du schon"), ("e1_a.tex", "Einheit 1 von 2 · Streifen- und Kreisdiagramm"), ("e2_a.tex", "Einheit 2 von 2 · Diagramme beurteilen und Boxplot")]:
    start = {"zone_a.tex": 1, "e1_a.tex": 12, "e2_a.tex": 25}[q]
    P.append(kopf + ":")
    P += [f"  {start + i}. {t}" for i, t in enumerate(TITEL[q])]
P.append("")
P += ["Zählung (Textextraktion der Kompilate):",
      zaehle("Daten_KennstDuSchon.pdf", ["zone_a.tex"]),
      zaehle("Daten_Lernblatt.pdf", ["e1_a.tex", "e2_a.tex"]),
      zaehle("Daten_Gesamt.pdf", ["zone_a.tex", "e1_a.tex", "e2_a.tex"]),
      zaehle("Daten_Loesungen.pdf", [], loesung=True),
      "Verzeichniszeile Lernblatt: " + verzeichnis("Daten_Lernblatt.pdf"),
      "Verzeichniszeile Gesamt: " + verzeichnis("Daten_Gesamt.pdf"), ""]
P += ["Schritte (Schritt · Anlass):"] + SCHRITTE.splitlines() + [""]
P += ["Vorlage: fehlende Bausteine · Warnungen aus dem Log – fehlende Bausteine: keine; Warnungen: Overfull \\hbox in Einheit 2 (Nr. 29, Nr. 32), behoben; in den übergebenen Dateien keine Package-mathblatt-Warnung und kein Overfull",
      "Korrekturrunden: 12 von 55 Schritten",
      f"Zone: {dt('zone')}", f"Weiter: {dt('weiter')} (kein Klick – der Testlauf baut ohne Halt durch; der Stempel markiert den Übergang)",
      f"E 1: {dt('e 1')}", f"E 2: {dt('e 2')}", f"Lernblatt: {dt('lernblatt')}", f"Gesamt: {dt('gesamt')}", f"Lösungen: {dt('loesungen')}"]
open("protokoll.txt", "w", encoding="utf-8").write("\n".join(P) + "\n")

C = ["Eingabe des Lehrers:", EINGABE, "", DEUTUNG] + PLAN + ["", PLANFRAGE, "Rückfragen: keine", "",
     "Daten_KennstDuSchon.pdf", ZONEZEILE, "", *DATEIEN[1:], ARCHIV, "", "Ausgabeblock:", *AUSGABE, "",
     "Übergebene Dateien: " + ", ".join(DATEIEN) + ", " + ARCHIV]
open("chat.txt", "w", encoding="utf-8").write("\n".join(C) + "\n")

dateien = sorted(set(glob.glob("*.pdf") + glob.glob("*.tex") + glob.glob("*.log") + glob.glob("pruef_out_*.txt")
                     + ["pruef.py", "mathblatt.sty", "Anleitung_mathblatt.md", "daten.md", "zeiten.txt",
                        "protokoll.txt", "chat.txt", "archiv.py", "ausgabeblock.txt"]))
with zipfile.ZipFile(ARCHIV, "w", zipfile.ZIP_DEFLATED) as z:
    for d in dateien:
        z.write(d)
print("\n".join(P[-10:]))
print(zaehle("Daten_Gesamt.pdf", ["zone_a.tex", "e1_a.tex", "e2_a.tex"]))
print(ARCHIV, len(dateien), "Dateien,", os.path.getsize(ARCHIV), "Bytes")
