# Schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3) – im selben Aufruf
import re, subprocess, zipfile, glob, os
from pypdf import PdfReader

def txt(pdf):
    return subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, '-'], capture_output=True).stdout.decode('utf-8')

def zaehle(pdf, grafiken, loesung=False):
    t = txt(pdf)
    seiten = len(PdfReader(pdf).pages)
    if loesung:
        n = len(set(re.findall(r'(?m)^\s*(\d+)\)', t)))
        return f"{pdf}: Nummern mit Lösung {n}, Seiten {seiten}"
    t2 = "\n".join(z for z in t.splitlines() if '□ ' not in z[:3] and not re.match(r'^\s*□\s*\d', z))
    hn = len(re.findall(r'(?m)^\s*\d+\. \S', t2))
    teil = len(re.findall(r'(?m)(?:^|\s{2,}|\s)([a-l])\)\s', t2))
    return f"{pdf}: Hauptnummern {hn}, Teilaufgaben {teil}, Grafiken {grafiken}, Seiten {seiten}"

z = {k: int(v) for k, v in (l.rsplit(' ', 1) for l in open('zeiten.txt', encoding='ascii').read().splitlines())}
t0 = z['t0']
zeiten = [f"Zone: {z['zone'] - t0} s", f"Weiter: {z['weiter'] - t0} s (Stempel des simulierten Klicks)"]
zeiten += [f"E {n}: {z['e ' + str(n)] - t0} s" for n in (1, 2, 3, 4)]
zeiten += [f"Lernblatt: {z['lernblatt'] - t0} s", f"Gesamt: {z['gesamt'] - t0} s", f"Lösungen: {z['loesungen'] - t0} s"]

sty2 = open('mathblatt.sty', encoding='utf-8').read().splitlines()[1]
stand = open('quadratische-gleichungen.md', encoding='utf-8').read().splitlines()[1]
verz_l = re.search(r'\\verzeichniszeile\{(.*)\}', open('QuadratischeGlg_Lernblatt.tex', encoding='utf-8').read()).group(1)
verz_g = re.search(r'\\verzeichniszeile\{(.*)\}', open('QuadratischeGlg_Gesamt.tex', encoding='utf-8').read()).group(1)
titel = []
for f in ['zone_a.tex', 'e1_a.tex', 'e2_a.tex', 'e3_a.tex', 'e4_a.tex']:
    s = open(f, encoding='utf-8').read()
    titel.append(f"[{f}] " + " | ".join(re.findall(r'\\begin\{aufgabe\}\{(.*)\}\r?\n', s)))

ZWEIGE = """Zweige:
Einheit 1 von 4 · Wurzelziehen und Lösbarkeit (gebaut, Nr. 12–23): Hier lernst du, Gleichungen wie x² = c durch Wurzelziehen zu lösen und zu sagen, ob es zwei, eine oder keine Lösung gibt · neu in diesem Jahr, je nach Buch bis Klasse 10 (am Gymnasium schon in Klasse 8 oder 9) · P10 · baut auf: Quadrieren, Wurzel ziehen, lineare Gleichungen, Scheitelpunktform
Einheit 2 von 4 · Normalform und p-q-Formel (gebaut, Nr. 24–39): Hier lernst du, jede quadratische Gleichung zu ordnen und mit der p-q-Formel zu lösen · neu in diesem Jahr, je nach Buch bis Klasse 10 · P10 oft · baut auf: Wurzelziehen (Einheit 1), Ausmultiplizieren, Terme ordnen
Einheit 3 von 4 · Sachaufgaben (gebaut, Nr. 40–46): Hier lernst du, Zahlenrätsel und Flächenaufgaben mit quadratischen Gleichungen zu lösen · neu in diesem Jahr, je nach Buch bis Klasse 10 · keine P10-Aufgabe · baut auf: Wurzelziehen (Einheit 1), p-q-Formel (Einheit 2)
Ausblick Einheit 4 von 4 · Satz vom Nullprodukt (gebaut, Nr. 47–55): Hier lernst du, Gleichungen in Produktform mit dem Satz vom Nullprodukt zu lösen · kommt nächstes Jahr (am Gymnasium schon in Klasse 8 oder 9) · P10 · baut auf: Ausklammern, lineare Gleichungen, p-q-Formel (Einheit 2)
Abgewählt: keine. Zone Kennst du schon: Nr. 1–11."""

SCHRITTE = """Werkzeugaufrufe (Schritt · Anlass):
1 · Read unterrichtsblatt.md Zeilen 1–754 · Anleitung lesen
2 · Read unterrichtsblatt.md ab 755 · Anleitung bis zur letzten Zeile lesen
3 · PowerShell: Arbeitsverzeichnis anlegen, Stempel t0 · Zeitmessung (im selben Aufruf wie das Anlegen des Verzeichnisses)
4 · PowerShell: curl Themenregister und Register der Blätter · Katalog holen (1.2)
5 · Grep in der gespeicherten Ausgabe · Zeile quadratische-gleichungen und Register finden
6 · PowerShell: Index- und Registerzeilen ausgeben · Datei wählen, Register prüfen (Blatt „nullstellen“ vom 22.09. ist anderes Thema)
7 · PowerShell: curl katalog/quadratische-gleichungen.md · Eintrag holen
8 · Read Eintrag Zeilen 1–110 · Eintrag lesen
9 · Read Eintrag ab 111 · Eintrag lesen (dabei versehentlich auch Offene Punkte und Prüfliste mitgelesen, nicht verwendet)
10 · PowerShell: curl mathblatt.sty und Anleitung_mathblatt.md · Vorlage holen (4.5; Anleitung als Datei gespeichert, weil die Ausgabe zu lang ist)
11 · Read Anleitung Zeilen 1–275 · Makros
12 · Read Anleitung ab 276 · Makros
13 · Write zone_a.tex · Zone
14 · Write zone_l.tex · Lösungen Zone
15 · Edit zone_l.tex · Zuordnungszeile als Absatz statt \\zweigzeile
16 · Write QuadratischeGlg_KennstDuSchon.tex · Rahmendatei Zone
17 · Write pruef.py · Prüfskript (Abschnitt zone, Sperrprüfung)
18 · PowerShell: pruef zone, xelatex, pdftoppm · Prüfung Zone
19 · PowerShell: Abweichungen anzeigen · pruef meldete 8a ABWEICHUNG
20 · Edit pruef.py · Skriptfehler: sympy wertete 4*(x+2) zu 4x+8 aus (evaluate=False)
21 · Read zone_p-1.png · Seite ansehen (erste Nutzung der Makros)
22 · Read zone_p-2.png · Seite ansehen
23 · Read zone_p-3.png · Seite ansehen
24 · PowerShell: Korrektur · \\punktfeld setzt „S(“ selbst, sichtbar „SS(“; Kopfzeile „Kennst du schon · Kennst du schon“ mit leerem Blattnamen probiert
25 · PowerShell: Korrektur · leerer Blattname ergab „Quadratische Gleichungen · · Kennst du schon“, zurückgesetzt; Stempel zone
26 · Read zone_q-2.png · geänderte Seite ansehen
27 · Write e1_a.tex · Einheit 1
28 · PowerShell: Antwortfelder Nr. 23 auf \\leerfeld[m] · Stempel weiter
29 · Write e1_l.tex · Lösungen Einheit 1
30 · Edit pruef.py · Abschnitt e1
31 · Write testrahmen.tex · Prüfrahmen je Einheit (nicht übergeben)
32 · PowerShell: abgelehnt · Remove-Item mit dem Argument \\input vom Werkzeug gesperrt
33 · PowerShell: Prüfrahmen je Einheit, pruef e1, xelatex · Sperrprüfung: 15a x² − 4 = 5 entspricht x² = 9 (Grundvorstellung)
34 · Read e1_p-2.png · Seite ansehen
35 · Read e1_p-5.png · Ablesegrafik Nr. 18
36 · Read e1_p-6.png · Zylinder Nr. 23
37 · PowerShell: Korrektur · Nr. 15 neue Gleichungen; Nr. 18 Labels y = … über der Achsenbezifferung (xmax 4, Label bei x = 3); Nr. 23 b Zeile gedehnt, Feld in eigene Zeile
38 · PowerShell: Korrektur · Nr. 23 a doppelte Gleichung x² = 64 (auch Nr. 21 a) → 121 m²; Lösungen: x₁, ≈, ≠, π fehlen im Textfont
39 · Write fix_uni.py · Unicode in Lösungen durch Mathematik ersetzen
40 · Read e1_q-5.png · geänderte Seite ansehen
41 · Read e1_q-6.png · geänderte Seite ansehen
42 · PowerShell: fix_uni, Neukompilat, Stempel e 1
43 · Write e2_a.tex · Einheit 2
44 · Write e2_l.tex · Lösungen Einheit 2
45 · Edit fix_uni.py · Indizes an S₁, S₂
46 · Edit pruef.py · Abschnitt e2
47 · PowerShell: pruef e2, xelatex, Seitenkarte · Prüfung Einheit 2
48 · Read e2_p-5.png · Fehlgriff (Dateiname bei zehn Seiten zweistellig)
49 · Read e2_p-9.png · Fehlgriff (Dateiname)
50 · Read e2_p-05.png · Seitenhöhe Nr. 30
51 · Read e2_p-09.png · Ablesegrafik Nr. 39
52 · Write e3_a.tex · Einheit 3
53 · Write e3_l.tex · Lösungen Einheit 3
54 · Edit testrahmen.tex · fehlender Baustein \\quadratrand im Vorspann
55 · Edit pruef.py · Abschnitt e3
56 · PowerShell: Stempel e 2, pruef e3, xelatex · Prüfung Einheit 3
57 · Read e3_p-1.png · Rechteck-Skizze Nr. 43
58 · Read e3_p-2.png · Skizzen Nr. 44: Label „2 cm“ liegt auf dem Rahmen
59 · Write e4_a.tex · Ausblick Einheit 4
60 · Write e4_l.tex · Lösungen Einheit 4
61 · PowerShell: Korrektur · Nr. 55 c „zweite Lösung“ unklar; \\quadratrand Label „2 cm“ nach links außen
62 · Edit pruef.py · Abschnitt e4
63 · PowerShell: Neukompilat Einheit 3, Stempel e 3, pruef e4, xelatex · Sperrprüfung: 52a x² + 5x + 6 = 0 entspricht Original x·(x + 5) = −6
64 · Read e3_q-2.png · geänderte Seite ansehen
65 · PowerShell: Korrektur · Nr. 52 a → x² + 8x + 15 = 0; pruef e4 null Abweichungen; Stempel e 4
66 · Write abhaken.tex · Abhakseite
67 · Write QuadratischeGlg_Lernblatt.tex · Rahmendatei
68 · Write QuadratischeGlg_Gesamt.tex · Rahmendatei
69 · Write QuadratischeGlg_Loesungen.tex · Rahmendatei
70 · Write check_blatt.py · Prüfung Kompilat (Nummern, Kopfzeilen, Sprungziele, Abhakseite, Füllung)
71 · PowerShell: Lernblatt und Gesamt je zweimal xelatex, Stempel lernblatt und gesamt, check_blatt · Abhak-Zählung im Skript fand 0 (Muster „□ n.“ nicht erfasst)
72 · PowerShell: Abhakseite als Text, Seiten rendern · Muster klären
73 · PowerShell: check_blatt korrigiert · Abhakseite 44 bzw. 55 Einträge gleich den Hauptnummern
74 · Read lb_p-01.png · Verzeichniszeile und Zweigkopf
75 · Read ge_p-25.png · Abhakseite
76 · PowerShell: Lösungen zweimal xelatex, Stempel loesungen, Zählung, Titelgleichheit Abhakseite
77 · Write archiv.py · Protokoll und Archiv
78 · PowerShell: archiv.py · protokoll.txt, chat.txt, Zip"""

zaehl = [zaehle('QuadratischeGlg_KennstDuSchon.pdf', 0), zaehle('QuadratischeGlg_Lernblatt.pdf', 6),
         zaehle('QuadratischeGlg_Gesamt.pdf', 6), zaehle('QuadratischeGlg_Loesungen.pdf', 0, loesung=True)]

prot = [
    "Prompt: Unterrichtsblatt-Prompt v4.4",
    "Modell: Claude Opus 5.5 (claude-opus-5-5)",
    "Vorlage: " + sty2.lstrip('% ').strip(),
    "Katalog: quadratische-gleichungen.md, " + stand,
    "Bestellung: mit Wiederholung · mit Ausblick",
    "Standpunkt: Kl. 9, Oberschule",
    "",
    ZWEIGE,
    "",
    "Hauptnummern mit Titel:",
    *titel,
    "",
    "Zählung aus der Textextraktion der Kompilate:",
    *zaehl,
    "Verzeichniszeile Lernblatt: " + verz_l,
    "Verzeichniszeile Gesamt: " + verz_g,
    "",
    SCHRITTE,
    "",
    "Vorlage: fehlende Bausteine · \\quadratrand (Quadrat mit Rand, Nr. 44; im Vorspann von Lernblatt, Gesamt und Prüfrahmen) · Warnungen aus dem Log: keine (keine Package mathblatt Warning, keine Overfull-Box)",
    "Korrekturrunden: 13 von 78 Schritten",
    *zeiten,
]
open('protokoll.txt', 'w', encoding='utf-8').write("\n".join(prot) + "\n")

CHAT = """Eingabe: quadratische gleichungen 9 oberschule – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch

→ Lernblatt · mit Wiederholung · mit Ausblick (Register führt das Thema nicht; „nullstellen“ vom 22.09. ist ein anderes Blatt) · 3 Zweige, 1 Ausblick · Zone aus 8 Fertigkeiten
Einheit 1 · Wurzelziehen und Lösbarkeit: Hier lernst du, Gleichungen wie x² = c durch Wurzelziehen zu lösen und zu sagen, ob es zwei, eine oder keine Lösung gibt · neu in diesem Jahr, je nach Buch bis Klasse 10 (am Gymnasium schon in Klasse 8 oder 9) · P10 · baut auf: Quadrieren, Wurzel ziehen, lineare Gleichungen, Scheitelpunktform
Einheit 2 · Normalform und p-q-Formel: Hier lernst du, jede quadratische Gleichung zu ordnen und mit der p-q-Formel zu lösen · neu in diesem Jahr, je nach Buch bis Klasse 10 · P10 oft · baut auf: Wurzelziehen (Einheit 1), Ausmultiplizieren, Terme ordnen
Einheit 3 · Sachaufgaben: Hier lernst du, Zahlenrätsel und Flächenaufgaben mit quadratischen Gleichungen zu lösen · neu in diesem Jahr, je nach Buch bis Klasse 10 · keine P10-Aufgabe · baut auf: Wurzelziehen (Einheit 1), p-q-Formel (Einheit 2)
Ausblick: Einheit 4 · Satz vom Nullprodukt: Hier lernst du, Gleichungen in Produktform mit dem Satz vom Nullprodukt zu lösen · kommt nächstes Jahr (am Gymnasium schon in Klasse 8 oder 9) · P10 · baut auf: Ausklammern, lineare Gleichungen, p-q-Formel (Einheit 2)
Alle Zweige, oder welche? (alle · Nummern · ein Typ für den Fokus)
Antwort: alle

QuadratischeGlg_KennstDuSchon.pdf
Weiter baut Einheit 1 bis 4, Gesamt und Lösungen.
Antwort: weiter

QuadratischeGlg_Lernblatt.pdf
QuadratischeGlg_Gesamt.pdf
QuadratischeGlg_Loesungen.pdf
QuadratischeGlg_2026-09-26_protokoll.zip
Ausblick: Satz vom Nullprodukt (OS erst Kl. 10) steht als Einheit 4 am Ende; die Wahl des Lösungswegs in Einheit 2 (Nr. 24, 36) kommt deshalb ohne Nullprodukt aus.
Geteilt: Nr. 27/28 (p-q-Formel, Grundfall und weiter); Nr. 14, 15 und 27–31 stehen mit Rechenplatz und Raster je allein auf ihrer Seite (etwa zwei Drittel Seite), nicht weiter geteilt.
Im Vorspann definiert: \\quadratrand (Quadrat mit Rand, Nr. 44) – Kandidat für die Vorlage.
Zone: Fertigkeit „Ausklammern, Ausmultiplizieren, binomische Formeln“ als zwei Nummern (7, 8); Fehler-Paar 10/11 zur binomischen Formel.
Höhe nach Lehrwerk: Einheit 3 hat kein P10-Original (Prüfungshöhe Nr. 44 b).
Vorlage: Kopfzeile der Zone-Datei doppelt („Kennst du schon · Kennst du schon“); x₁, ≈, ≠, π fehlen im Textfont der Lösungen und stehen dort als Mathematik.
Zeiten gemessen; „weiter“ ist im Testlauf ohne Gegenüber simuliert.
Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen, Sprossen, Typische Fehler, Prüfungsform/Zielmarke; nicht gebraucht Merkkasten, Grundvorstellung, Verortung · Befund: „Was sind p und q?“ und „durch welche Zahl teilen?“ verlangen Zahlen – Vorstufen Nr. 25/26 ohne Ergebnis, Ablesen in Nr. 27 · Befund: die Sperre nennt nur wörtliche Gleichungen, x² + 5x + 6 = 0 ist 2025-OS-B1h in Normalform, x² − 4 = 5 die umgestellte Grundvorstellung · Spannen OS Kl. 9–10 (Einheit 1–3) als „neu in diesem Jahr, je nach Buch bis Klasse 10“ (Eingabeklasse = Untergrenze, „neu oder schon bekannt“ passt nicht); Typklammer p-q-Formel [OS 10] als „(je nach Buch erst in Klasse 10)“ an Nr. 27.
Protokoll-Archiv: QuadratischeGlg_2026-09-26_protokoll.zip
"""
open('chat.txt', 'w', encoding='utf-8').write(CHAT)

name = 'QuadratischeGlg_2026-09-26_protokoll.zip'
dateien = (glob.glob('*.pdf') + glob.glob('*.tex') + glob.glob('*.log') + ['pruef.py', 'fix_uni.py', 'check_blatt.py', 'archiv.py']
           + glob.glob('pruef_out_*.txt') + ['mathblatt.sty', 'Anleitung_mathblatt.md', 'quadratische-gleichungen.md',
                                           'zeiten.txt', 'protokoll.txt', 'chat.txt'])
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for d in sorted(set(dateien)):
        if os.path.exists(d):
            zf.write(d)
print(name, len(zf.namelist()) if False else len(set(dateien)), "Dateien")
print("\n".join(zaehl))
print("\n".join(zeiten))
