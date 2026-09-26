# mkprotokoll.py – schreibt protokoll.txt und chat.txt und packt das Archiv (ein Aufruf)
import re, os, zipfile, glob

def lies(p):
    return open(p, encoding='utf-8').read()

# ---------- Kopf ----------
sty2 = open('mathblatt.sty', encoding='utf-8').read().splitlines()[1].lstrip('% ').strip()
stand = lies('kreis.md').splitlines()[1]
kopf = [
 'Prompt: Unterrichtsblatt-Prompt v4.4',
 'Modell: Claude Opus 5.5 (claude-opus-5-5)',
 f'Vorlage: {sty2}',
 f'Katalog: kreis.md, {stand}',
 'Bestellung: mit Ausblick (dazu mit Wiederholung: Zone)',
 'Standpunkt: Kl. 8, Oberschule (Gymnasium als Zusatz; Marken beider Schulformen gleich)',
]

# ---------- Zweige ----------
zweige = ['', 'Zweige:']
for d in ['e1_a.tex', 'e2_a.tex', 'e3_a.tex']:
    s = lies(d)
    kopfz = re.search(r'\\einheitenkopf\[[^\]]*\]\[[^\]]*\]\{([^}]*)\}', s).group(1)
    zz = re.search(r'\\zweigzeile\{(.*)\}', s).group(1)
    zweige.append(f'gebaut: {kopfz} – {zz}')
    nr = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', s).group(1))
    for m in re.finditer(r'\\begin\{aufgabe\}\{(.*)\}\s*$', s, re.M):
        nr += 1
        zweige.append(f'  {nr}. {m.group(1)}')
zweige.append('abgewählt: keine (Planfrage entfällt, 3 Zweige)')
zweige.append('Ausblick: keiner – alle Marken bei oder vor Kl. 8 (E1, E2 Kl. 7–8; E3 Kl. 7–9)')
s = lies('zone_a.tex'); nr = 0
zweige.append('Zone (Kennst du schon):')
for m in re.finditer(r'\\begin\{aufgabe\}\{(.*)\}\s*$', s, re.M):
    nr += 1
    zweige.append(f'  {nr}. {m.group(1)}')

# ---------- Zählung aus der Textextraktion ----------
GRAF = r'\\begin\{kreis\}|\\kreissektor|\\winkel\[|\\winkelstrahl|\\zeichenplatz|\\zylinder|\\kreisleer|\\kreisdiagramm'
def graf(dateien):
    return sum(len(re.findall(GRAF, lies(d))) for d in dateien)
def seiten(txt):
    return len([p for p in txt.split('\f') if p.strip()])
def zaehle(pdftxt, quellen):
    t = lies(pdftxt)
    hn = len(re.findall(r'(?m)^\s*\d+\. Ich', t))
    ta = len(re.findall(r'(?<![\w)])[a-h]\) ', t))
    return hn, ta, graf(quellen), seiten(t)
zaehl = ['', 'Zählung aus der Textextraktion:']
for pdf, txt, q in [('Kreis_KennstDuSchon.pdf', 'zone.txt', ['zone_a.tex']),
                    ('Kreis_Lernblatt.pdf', 'lernblatt.txt', ['e1_a.tex', 'e2_a.tex', 'e3_a.tex']),
                    ('Kreis_Gesamt.pdf', 'gesamt.txt', ['zone_a.tex', 'e1_a.tex', 'e2_a.tex', 'e3_a.tex'])]:
    hn, ta, g, sz = zaehle(txt, q)
    zaehl.append(f'{pdf}: {hn} Hauptnummern, {ta} Teilaufgaben, {g} Grafiken, {sz} Seiten')
t = lies('loesungen.txt')
nrn = sorted({int(x) for x in re.findall(r'(?<![\w,.])(\d{1,2})\) ', t) if 1 <= int(x) <= 43})
zaehl.append(f'Kreis_Loesungen.pdf: Lösungen zu {len(nrn)} Nummern ({nrn[0]}–{nrn[-1]}), '
             f'{len(re.findall(r"kreisdiagramm", lies("e3_l.tex")))} Grafik, {seiten(t)} Seiten')
zaehl.append('Verzeichniszeile Lernblatt: 1 Kreisumfang (Nr. 10–21) • 2 Kreisfläche (Nr. 22–32) • 3 Kreisteile (Nr. 33–43) • Das kann ich')
zaehl.append('Verzeichniszeile Gesamt: Kennst du schon (Nr. 1–9) • 1 Kreisumfang (Nr. 10–21) • 2 Kreisfläche (Nr. 22–32) • 3 Kreisteile (Nr. 33–43) • Das kann ich')

# ---------- Schritte ----------
schritte = '''Schritte (Werkzeugaufruf · Anlass → Ergebnis):
1 · Read unterrichtsblatt.md Z. 1–754 · Anleitung lesen → gelesen
2 · Read unterrichtsblatt.md Z. 755–1448 · Anleitung zu Ende lesen → gelesen
3 · PowerShell · Arbeitsverzeichnis anlegen, katalog/index.md und blaetter/index.md holen → Ausgabe in Datei umgeleitet (122 KB)
4 · Grep „kreis“ im Themenregister · Eintrag wählen → kreis.md (Sek I, Kl. 7–8 / 8–9)
5 · Grep Überschriften · Register der Blätter finden → Zeile 278
6 · Read Register der Blätter · Thema schon gebaut? → Kreis nicht geführt
7 · PowerShell curl kreis.md · Eintrag holen → 19911 Byte
8 · Read kreis.md · Eintrag lesen → 3 Einheiten, 6 Fertigkeiten, 4 Erkennungsschritte
9 · PowerShell · Stempel t0 → gesetzt
10 · PowerShell curl mathblatt.sty und Anleitung_mathblatt.md · Vorlage holen → Version 2026-09-28a
11 · Read Anleitung Z. 1–275 · Makronamen → gelesen
12 · Read Anleitung Z. 276–391 · Makronamen → gelesen
13 · Write probe.tex · Probe der Kreis-Bausteine (kreis, sektor, kreissektor, winkel, winkelstrahl, sachtabelle, eigener Zeichenplatz)
14 · PowerShell · Probe kompilieren und rendern → fehlerfrei, 2 Seiten
15 · Read probe-1.png · Sichtprüfung → \\kreissektor 3,6 cm breit (fünf nicht in einer Zeile), \\sektor in kreis färbt grau; Kopfzeile Zone verdoppelt
16 · PowerShell · gerenderte Probeseiten auflisten → 2
17 · Read probe-2.png · Sichtprüfung Tabelle, Kreuze, \\kreisleer → brauchbar
18 · Write zone_a.tex · Zone Nr. 1–9
19 · Write zone_l.tex · Lösungen Zone
20 · Write pruef.py · Prüfskript (Zone)
21 · Write Kreis_KennstDuSchon.tex · Rahmen Zone
22 · PowerShell · pruef zone, Zone kompilieren, rendern → 0 Abweichungen; Log: „Overfull \\hbox (18.22049pt too wide) in paragraph at lines 19--24“, „Overfull \\hbox (71.66432pt too wide) in paragraph at lines 100--106“; Kopfzeile „Kreis · Kennst du schon ·“
23 · Read zone-2.png · Sichtprüfung Winkel → gut
24 · Read zone-3.png · Sichtprüfung Winkelstrahlen, Nr. 9 → Prozentfelder rechts abgeschnitten (geruest), 110°-Schenkel läuft in den linken Rand
25 · PowerShell · Korrektur per .NET-Ersetzung → fehlgeschlagen (relativer Pfad), nichts geschrieben
26 · Edit zone_a.tex · Korrektur Overfull Z. 19–24: Einheitenwechsel von Nr. 2 d als \\anweisung
27 · Edit zone_a.tex · Korrektur Nr. 8 c: 100° statt 110° (Schenkel im Satzspiegel)
28 · Edit zone_a.tex · Korrektur Overfull Z. 100–106: Nr. 9 von geruest nach teile
29 · Edit Kreis_KennstDuSchon.tex · Korrektur Kopfzeile: Kurzform über \\zonekurz
30 · Edit zone_l.tex · Lösung 8 c auf 100°
31 · PowerShell · Zone neu kompilieren, Stempel zone → fehlerfrei; Kopfzeile jetzt „Kreis · · Kennst du schon“
32 · Edit zone_a.tex · Korrektur Kopfzeile: \\zonekopf statt \\einheitenkopf
33 · Edit Kreis_KennstDuSchon.tex · \\zonekopf als Untertitel, Kopfzeile „Kreis · Kennst du schon“
34 · PowerShell · Zone neu kompilieren und rendern → Kopfzeile richtig, keine Warnung
35 · Read zone-3.png · Sichtprüfung Nr. 9 → e) Feld bricht mitten in der Zeile um
36 · Edit zone_a.tex · Korrektur Nr. 9 e: Felder in eigener Zeile
37 · PowerShell · Stempel weiter, Zone neu kompilieren → fehlerfrei (Zone übergeben)
38 · Write e1_a.tex · Einheit 1 Nr. 10–21
39 · Edit e1_a.tex · Korrektur vor dem Kompilieren: „Kreis A/B“ kollidiert mit A = Fläche; Titel ohne „u : d“
40 · Write e1_l.tex · Lösungen Einheit 1
41 · Edit pruef.py · Einheit 1 ergänzt
42 · Edit pruef.py · Aufrufliste
43 · Edit pruef.py · Vergleich für Wortantworten (Ankreuzen)
44 · Write einheit_pruef.tex · Prüfrahmen je Einheit mit \\zeichenplatz
45 · PowerShell · pruef e1, kompilieren (2×), rendern → 0 Abweichungen, keine Warnung, 4 Seiten
46 · Read e1p-1.png · Sichtprüfung Nr. 10 Figur → gut
47 · Read e1p-2.png · Sichtprüfung Kreise, Zeichenflächen, Tabelle → gut
48 · Read e1p-3.png · Sichtprüfung Zylinder → gut
49 · PowerShell · Stempel e 1
50 · Write e2_a.tex · Einheit 2 Nr. 22–32
51 · Write e2_l.tex · Lösungen Einheit 2
52 · Edit pruef.py · Einheit 2 ergänzt
53 · Edit pruef.py · Aufrufliste
54 · Edit einheit_pruef.tex · auf e2_a
55 · PowerShell · pruef e2, kompilieren (2×), rendern → 0 Abweichungen, keine Warnung, 3 Seiten
56 · Read e2p-1.png · Sichtprüfung → Nr. 24 in teilezwei gedehnt („Viertelkreis, r = 12 cm:“ über die Zelle verteilt)
57 · Read e2p-2.png · Sichtprüfung Tabelle, Fehlerrechnungen → gut
58 · Edit e2_a.tex · Korrektur Nr. 24: teilezwei → teile
59 · PowerShell · Einheit 2 neu kompilieren, Stempel e 2 → fehlerfrei
60 · Write e3_a.tex · Einheit 3 Nr. 33–43
61 · Write e3_l.tex · Lösungen Einheit 3
62 · Edit pruef.py · Einheit 3 ergänzt
63 · Edit pruef.py · Aufrufliste
64 · Edit einheit_pruef.tex · auf e3_a
65 · PowerShell · pruef e3, kompilieren (2×), rendern → 0 Abweichungen, keine Warnung, 3 Seiten
66 · Read e3p-1.png · Sichtprüfung Sektoren, Glücksrad → Graufärbung bei 60 dpi fraglich
67 · Read e3p-2.png · Sichtprüfung → gut
68 · Read e3p-3.png · Sichtprüfung → Nr. 43 a/b Felder gedehnt, „zu Fuß“ getrennt
69 · PowerShell · Ausschnitt Nr. 33 mit 110 dpi rendern
70 · Read e3zoom-1.png · Graufärbung → vorhanden
71 · Edit e3_a.tex · Korrektur Nr. 43: Felder in eigener Zeile, „zu~Fuß“
72 · PowerShell · Einheit 3 neu kompilieren, Stempel e 3 → fehlerfrei
73 · Write bau.py · Abhakseite und Verzeichniszeilen aus den Quelltexten
74 · Write Kreis_Lernblatt.tex · Rahmen
75 · Write Kreis_Gesamt.tex · Rahmen
76 · Write Kreis_Loesungen.tex · Rahmen
77 · PowerShell · bau.py, Lernblatt kompilieren (2×), Stempel lernblatt → Bereiche 10–21, 22–32, 33–43; 12 Seiten, keine Warnung
78 · Read lb-11.png · Sichtprüfung Abhakseite → vollständig, 4 Zeilen auf Seite 12
79 · PowerShell · Seitenfüllung Lernblatt → S. 4 und S. 7 unter einem Drittel, je eine Hauptnummer, Seite davor voll → kein Befund
80 · PowerShell · Gesamt kompilieren (2×), Stempel gesamt → 15 Seiten, Nummern 1–43 lückenlos, keine Warnung
81 · PowerShell · Lösungen kompilieren (2×), Stempel loesungen, rendern → 2 Seiten, keine Warnung
82 · Read lsg-1.png · Sichtprüfung Lösungen → gut
83 · Read lsg-2.png · Sichtprüfung Lösungsgrafik → gut
84 · Write mkprotokoll.py · Protokoll, Chat und Archiv
85 · Edit mkprotokoll.py · Korrektur der Zeile Korrekturrunden (Zählung falsch)
86 · Edit mkprotokoll.py · Schrittliste ergänzt
87 · Edit mkprotokoll.py · Zählausdruck für Teilaufgaben bereinigt
88 · Edit mkprotokoll.py · Schrittliste an die tatsächlichen Aufrufe angepasst
89 · Edit mkprotokoll.py · Zeile Korrekturrunden nachgezogen
90 · Edit mkprotokoll.py · Ende der Schrittliste nachgezogen
91 · Edit mkprotokoll.py · Zeile Korrekturrunden nachgezogen
92 · Edit mkprotokoll.py · Gesamtzahl der Schritte aus der Schrittliste gezählt
93 · Edit mkprotokoll.py · Ende der Schrittliste nachgezogen
94 · Write chat_quelle.txt · Chattext wortgleich
95 · PowerShell · mkprotokoll.py → protokoll.txt, chat.txt, Archiv'''

vorlage = ['', 'Vorlage: fehlende Bausteine · Warnungen aus dem Log',
 'fehlende Bausteine: \\zeichenplatz (leere Zeichenfläche mit vorgegebenem Mittelpunkt M zum Kreiszeichnen), im Vorspann von Lernblatt, Gesamt und Prüfrahmen; '
 'Zone-Untertitel \\zonekopf im Vorspann der Zone-Rahmendatei, weil \\einheitenkopf mit Kurzform die Kopfzeile verdoppelt („Kreis · Kennst du schon · Kennst du schon“) und mit leerer Kurzform einen leeren Punkt setzt („Kreis · · Kennst du schon“ bzw. „Kreis · Kennst du schon ·“)',
 'Warnungen aus dem Log: in den Endfassungen keine; unterwegs zwei Overfull \\hbox in zone_a.tex (behoben)']

# ---------- Zeiten ----------
z = {}
for zeile in lies('zeiten.txt').splitlines():
    teile = zeile.split()
    z[' '.join(teile[:-1])] = int(teile[-1])
t0 = z['t0']
zeit = ['', f"Korrekturrunden: 26 von {len(schritte.splitlines()) - 1} Schritten (25–34, 36–37, 39, 58–59, 71–72, 85–93; 85–93 betreffen nur das Protokoll)",
        f"Zone: {z['zone'] - t0} s (Stempel vor zwei Kopfzeilen-Korrekturen gesetzt; Zone endgültig bei „weiter“)",
        f"Weiter: {z['weiter'] - t0} s",
        f"E 1: {z['e 1'] - t0} s (Stempel im Aufruf nach der Sichtprüfung)",
        f"E 2: {z['e 2'] - t0} s", f"E 3: {z['e 3'] - t0} s",
        f"Lernblatt: {z['lernblatt'] - t0} s", f"Gesamt: {z['gesamt'] - t0} s", f"Lösungen: {z['loesungen'] - t0} s",
        'Wartezeit auf „weiter“: keine (unbeaufsichtigter Testlauf, Antwort in der Eingabe)']

prot = '\n'.join(kopf + zweige + zaehl + [''] + [schritte] + vorlage + zeit) + '\n'
open('protokoll.txt', 'w', encoding='utf-8').write(prot)

# ---------- chat.txt ----------
chat = lies('chat_quelle.txt')
open('chat.txt', 'w', encoding='utf-8').write(chat)

# ---------- Archiv ----------
name = 'Kreis_2026-09-26_protokoll.zip'
muster = ['*.pdf', '*.tex', '*.log', 'pruef.py', 'pruef_out_*.txt', 'bau.py', 'mkprotokoll.py', 'mathblatt.sty',
          'Anleitung_mathblatt.md', 'kreis.md', 'zeiten.txt', 'protokoll.txt', 'chat.txt']
dateien = sorted({f for m in muster for f in glob.glob(m)})
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for f in dateien:
        zf.write(f)
print(prot)
print(name, len(dateien), 'Dateien')
