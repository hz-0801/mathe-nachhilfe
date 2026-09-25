# archiv.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3), in einem Aufruf.
import glob
import re
import zipfile

from pypdf import PdfReader

THEMA = 'QuadratischeGlg'
DATEIEN = [f'{THEMA}_KennstDuSchon.pdf', f'{THEMA}_Lernblatt.pdf', f'{THEMA}_Gesamt.pdf', f'{THEMA}_Loesungen.pdf']

EINGABE = 'quadratische gleichungen 9 oberschule'
DEUTUNG = ('→ Lernblatt · mit Wiederholung und Ausblick (das Register der Blätter führt das Thema nicht, nur das '
           'Blatt „nullstellen“) · 3 Zweige, 1 Ausblick (Satz vom Nullprodukt: Oberschule erst Kl. 10) · '
           'Zone aus 8 Fertigkeiten')
PLAN = [
    'Einheit 1 · Wurzelziehen und Lösbarkeit – Hier lernst du, Gleichungen mit x² durch Wurzelziehen zu lösen und '
    'zu sagen, wie viele Lösungen sie haben · neu in diesem Jahr, je nach Buch erst Klasse 10 (am Gymnasium je nach '
    'Buch schon seit Klasse 8) · P10 · baut auf: Quadrieren, Quadratwurzeln, lineare Gleichungen, Einsetzen, '
    'Scheitelpunktform',
    'Einheit 2 · Normalform und p-q-Formel – Hier lernst du, eine quadratische Gleichung zu ordnen, zu normieren und '
    'mit der p-q-Formel zu lösen · neu in diesem Jahr, je nach Buch erst Klasse 10 · P10 oft · baut auf: '
    'Wurzelziehen und Lösbarkeit (Einheit 1), Terme ordnen, Ausmultiplizieren und binomische Formeln',
    'Einheit 3 · Sachaufgaben – Hier lernst du, zu einer Sachaufgabe eine quadratische Gleichung aufzustellen, sie '
    'zu lösen und die passende Lösung auszuwählen · neu in diesem Jahr, je nach Buch erst Klasse 10 · keine '
    'P10-Aufgabe · baut auf: Wurzelziehen und Lösbarkeit (Einheit 1), Normalform und p-q-Formel (Einheit 2), '
    'Gleichungen aufstellen',
    'Ausblick: Einheit 4 · Satz vom Nullprodukt – Hier lernst du, Gleichungen, bei denen ein Produkt null ist, ohne '
    'Formel zu lösen · kommt nächstes Jahr (am Gymnasium je nach Buch schon seit Klasse 8) · P10 · baut auf: '
    'Normalform und p-q-Formel (Einheit 2), Ausmultiplizieren und Ausklammern, Einsetzen',
]
PLANFRAGE = 'Alle Zweige, oder welche? (alle · Nummern · ein Typ für den Fokus)'
ANTWORT = 'alle'
ZONEZEILE = 'Weiter baut Einheit 1 bis 4, Gesamt und Lösungen.'

AUSGABE = [
    '1. Ausblick-Zweig Satz vom Nullprodukt (Katalog-Einheit 2, Oberschule Kl. 10) steht zuletzt; darum fehlt das '
    'Nullprodukt in der Vorstufe „Welche Form?“ (Nr. 11) und in „Lösungsweg wählen“ (Nr. 17), Produkt gleich Zahl '
    'läuft in Nr. 17b über die Formel · Zone eigens gezählt (Z1–Z9), Lernblatt ab Nr. 1 · geteilte Hauptnummern: '
    '14/16 (p-q-Formel – weiter), 24/25 (Rechteckaufgabe – weiter) · Zwischensprossen: Nr. 4d Minus vor x², '
    'Nr. 8b Gleichung mit genau einer Lösung angeben, Nr. 14e/f „p negativ“ und „q negativ“ getrennt · Höhe nach '
    'Lehrwerk: Einheit 3 (keine P10-Aufgabe), Nr. 25b · im Vorspann definiert: \\zweigzeile, \\abhakkopf/\\abhak '
    '(Abhakseite), \\vzeile (Verzeichniszeile mit Link) · Vorlage: gleichungsraster setzt die letzte Schreibzeile '
    'einer Reihe auf die nächste Zeile, \\\\[3mm] wirkt nicht; im Aufruf mit einer Leerzeile (\\rule{0pt}{2mm} & \\\\) '
    'nach jeder Reihe ausgeglichen, die Zone ist danach neu gesetzt · Nullfall x² = 0 aus Kasten 1 nur als '
    '5x² = 0 und 3x² + 5 = 5.',
    '2. Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (Fertigkeiten, Erkennungsschritte), '
    'Sprossen, Typische Fehler, Prüfungsform/Zielmarke; Merkkasten nur als Sperrliste, Verortung und '
    'Grundvorstellung nicht gebraucht · gefehlt/Konflikt: Typklammer p-q-Formel [OS 10] gegen die Einheitenmarke '
    'OS 9–10 (gesetzt als „kommt je nach Buch erst nächstes Jahr“ an Nr. 14); Vorstufe „Welche Form?“ und Typ '
    '„Lösungsweg wählen“ der Einheit 3 setzen Einheit 2 voraus, die an der Oberschule erst Kl. 10 kommt; Kasten 1 '
    'sperrt x² = 0, das der Nullfall braucht · Spannen: Einheiten 1, 3, 4 „OS Kl. 9–10“ bei Eingabeklasse 9 = frühe '
    'Grenze → „neu in diesem Jahr, je nach Buch erst Klasse 10“ (die Formel „neu oder schon bekannt“ passt an der '
    'frühen Grenze nicht); GYM 8–9 der Einheiten 1 und 2 → „am Gymnasium je nach Buch schon seit Klasse 8“; „nicht '
    'für alle“ ohne Wirkung, weil es keine frühere Klasse nennt.',
    f'4. Protokoll-Archiv: {THEMA}_2026-09-25_protokoll.zip',
]

SCHRITTE = '''1 Arbeitsverzeichnis prüfen · vorhanden, leer
2 Stempel t0
3 Themenregister und Blätterregister holen · beide erreichbar
4 Register durchsuchen · Eintrag quadratische-gleichungen.md; Blatt „nullstellen“ nutzt ihn, Thema selbst nicht geführt
5 Blätterregister lesen · 4 Blätter
6 Registerzeile suchen · Datei bestätigt
7 Eintrag, mathblatt.sty, Anleitung holen · alle drei erreichbar, Vorlage 2026-09-22h
8 Eintrag lesen, Teil 1 · Struktur, Sprossen, Fehler (Datei ganz eingelesen; Status, Offene Punkte, Prüfliste nicht verwendet)
9 Eintrag lesen, Teil 2 · Prüfungsform, Zielmarken
10 Anleitung lesen · Makros
11 Vorlage nach Zählern durchsuchen · Zähler aufgabe für Z-Zählung der Zone
12 Vorlage Z. 60–310 gelesen · Umgebung aufgabe, Felder (Abweichung von 4.5 „nicht lesen“, nur zur Diagnose)
13 Vorlage Z. 1–60 gelesen · Versionszeile
14 zone_a.tex schreiben
15 zone_l.tex schreiben
16 zone.tex schreiben
17 pruef.py schreiben (Zone, Sperrliste aus Kasten/Beispiel/Original/Fehlern)
18 pruef.py: Import ergänzt
19 Zone prüfen, kompilieren, rendern · 0 Abweichungen; Stempel zone
20 Zone Seite 1 ansehen
21 Zone Seite 2 ansehen
22 Stempel weiter
23 e1_a.tex schreiben
24 e1_l.tex schreiben
25 pruef.py: x^2 = 0 aus Sperrliste (Nullfall unvermeidbar)
26 pruef.py: Einheit 1
27 einheit.tex (Prüfrahmen je Einheit) schreiben
28 E1 prüfen, kompilieren · „9d Kasten/Original: (x+1)^2=16 ABWEICHUNG Gleichung x^2 + 2x - 15 = 0“
29 E1 Seitenfüllung aus Textextraktion
30 E1 Seite 3 ansehen · Geradenlabels „y =“ abgeschnitten
31 E1 Seite 1 ansehen · gleichungsraster: Schreibzeile auf der Folgezeile, Nr. 3e Feld umbrochen
32 E1 Seite 2 ansehen · dasselbe bei Nr. 4, 5
33 E1 Seite 4 ansehen · dasselbe bei Nr. 9
34 Ausschnitt 150 dpi · Überlappung bestätigt
35 Rasterreihen mit \\\\[3mm] (Zone, E1)
36 Nr. 3e Feld in eigene Zeile
37 Nr. 7 xmax=6, Labels bei x = 4,2
38 Nr. 9d → (x+5)^2 = 4
39 Lösung 9d
40 pruef.py 9d
41 Aufruf abgewiesen (Remove-Item mit \\input im Befehl)
42 E1 neu · 0 Abweichungen; \\\\[3mm] ohne Wirkung
43 E1 Seite 3 ansehen · Labels lesbar
44 E1 Seite 2 ansehen · Überlappung bleibt
45 test_raster.tex, Varianten A–C
46 Test kompilieren
47 Test ansehen · Überhang in allen drei Varianten
48 test_raster.tex, Varianten D–E
49 Test kompilieren
50 Test ansehen · Leerzeile mit Strut (D) behebt es
51 Leerzeile in Zone und E1, E1 neu · 5 Seiten, keine Warnung; Stempel e 1
52 E1 Seite 2 ansehen · Abstand in Ordnung
53 E1 Seite 4 ansehen · Grafik in Ordnung
54 e2_a.tex schreiben
55 Nr. 17: Original als \\gl mit Raster
56 Nr. 18: b) und c) als \\gl mit Raster
57 e2_l.tex schreiben
58 pruef.py: Einheit 2
59 E2 prüfen, kompilieren · „15 Bsp Kasten/Original: 3x^2-6x=9 ABWEICHUNG Gleichung (x-2)^2 - 4 = -2x + 3“, „12a … ABWEICHUNG Gleichung x(x+5) = -6“
60 E2 Seite 2 ansehen
61 E2 Seite 4 ansehen
62 E2 Seite 5 ansehen
63 E2 Seite 6 ansehen · Geradenlabel g im Text nicht erklärt
64 Beispiel Nr. 15 → 2x^2 + 12x = 32
65 Nr. 12a → x^2 + 7x + 10 = 0
66 Geradenlabel leer
67 Nr. 18c Funktionen g und h (f schon in Nr. 17)
68 Lösung 12a
69 pruef.py 12a
70 pruef.py Beispiel 15
71 pruef.py 12a Sperrliste
72 E2 neu · 0 Abweichungen; Stempel e 2
73 E2 Seite 7 ansehen
74 e3_a.tex schreiben
75 Nr. 24: Beispiel und Aufgabenrechteck getrennt
76 e3_l.tex schreiben
77 pruef.py: Einheit 3
78 pruef.py: Seitenlängen mit d aus dem Text
79 E3 prüfen, kompilieren · 0 Abweichungen
80 E3 Seite 1 ansehen · „oder − 12“: Minus nach Text als Rechenzeichen gesetzt
81 E3 Seite 2 ansehen · dasselbe bei −9 und −8
82 Minus als {-12}, {-9}, {-8}
83 E3 neu · Stempel e 3
84 Nr. 18c: h → k (h ist Zylinderhöhe in Nr. 4e)
85 Nr. 18a: A und B statt S (S ist der Scheitel)
86 Lösung 18
87 e4_a.tex schreiben
88 e4_l.tex schreiben
89 pruef.py: Einheit 4
90 E2 und E4 prüfen · 0 und 0 Abweichungen; Kompilieren in der Schleife: „I/O Error: Couldn't open file 'e4_pruef.pdf'“ (Jobname nicht ersetzt)
91 E2 und E4 kompilieren · keine Warnung
92 E4 Seite 2 ansehen
93 E2 Seite 6 ansehen · A(…|…), B(…|…) in Ordnung
94 E4 Seite 1 ansehen
95 Stempel e 4
96 rahmen.py schreiben (Abhakseite wortgleich aus den Quelltexten, Verzeichnis aus dem Kompilat)
97 rahmen.py: Zone nur im Gesamt suchen
98 lernblatt.tex schreiben
99 rahmen.py: Makronamen ohne Ziffern
100 lernblatt.tex: Makronamen
101 gesamt.tex schreiben
102 loesungen.tex schreiben
103 Abhakseite (42 Nummern) und Lernblatt · Gegenprobe Verzeichnis OK; Stempel lernblatt
104 Lernblatt Verzeichnis und Abhakseite rendern
105 Abhakseite ansehen
106 Gesamt · Gegenprobe OK, 6 Links; Stempel gesamt
107 Lösungen · 42 Nummern mit Lösung; Stempel loesungen
108 Lösungen Seite 1 ansehen · „3 = 4 (fA)“ als Gleichung gesetzt
109 ≠ in Z4 und Nr. 6; Lösungen und Zone-PDF neu
110 Zone-PDF ansehen
111 Zählung aus der Textextraktion
112 archiv.py schreiben
113 protokoll.txt, chat.txt, Archiv'''


def zeiten():
    z = {}
    for l in open('zeiten.txt', encoding='ascii'):
        k, v = l.rsplit(' ', 1)
        z[k] = int(v)
    t0 = z['t0']
    out = [f"Zone: {z['zone'] - t0} s", f"Weiter: {z['weiter']} (Stempel), {z['weiter'] - t0} s nach t0"]
    for n in range(1, 5):
        out.append(f"E {n}: {z[f'e {n}'] - t0} s")
    out += [f"Lernblatt: {z['lernblatt'] - t0} s", f"Gesamt: {z['gesamt'] - t0} s", f"Lösungen: {z['loesungen'] - t0} s"]
    return out


def zaehlung(pdf, grafiken):
    txt = pdf.replace('.pdf', '.txt')
    t = open(txt, encoding='utf-8').read()
    seiten = len(PdfReader(pdf).pages)
    if 'Loesungen' in pdf:
        n = len(re.findall(r'(?m)^\s*(Z?\d+)\) ', t))
        return f'{pdf}: Nummern mit Lösung {n}, Seiten {seiten}'
    hn = len(re.findall(r'(?m)^\s*Z?\d+\. Ich', t))
    ta = len(re.findall(r'(?m)(?:^|\s)[a-z]\) ', t))
    return f'{pdf}: Hauptnummern {hn}, Teilaufgaben {ta}, Grafiken {grafiken}, Seiten {seiten}'


def verzeichnis(pdf):
    t = open(pdf.replace('.pdf', '.txt'), encoding='utf-8').read().split('\f')[0]
    return [l.strip() for l in t.splitlines() if '·' in l and 'Quadratische Gleichungen' not in l]


def links(pdf):
    p = PdfReader(pdf).pages[0]
    an = p.get('/Annots')
    an = an.get_object() if an is not None else []
    return len(an)


prot = ['Prompt: Unterrichtsblatt-Prompt v4.3',
        'Modell: Claude Opus 5.5 (claude-opus-5-5)',
        'Vorlage: 2026-09-22h',
        'Katalog: quadratische-gleichungen.md, Status: gegengelesen bis auf [FS] (2026-09-11h, dreizehnter '
        'Gegenlese-Block; Entwurf 2026-09-08i, LISUM-Planungshilfen am 10e nachgetragen)',
        'Bestellung: mit Wiederholung · mit Ausblick',
        'Standpunkt: Kl. 9, Oberschule',
        '',
        'Zweige (gebaut, keiner abgewählt, einer als Ausblick):']
prot += ['  ' + p for p in PLAN]
prot += ['', 'Hauptnummern je Zweig (Titel):']
abh = open('abhaken.tex', encoding='utf-8').read()
gruppen = re.split(r'\\abhakkopf\{', abh)[1:]
for g in gruppen:
    kopf = g.split('}')[0]
    prot.append('  ' + kopf + ':')
    for nr, satz in re.findall(r'\\abhak\{([^}]*)\}\{(.*)\}\s*$', g, flags=re.M):
        prot.append(f'    {nr}. {satz}')
prot += ['', 'Zählung aus der Textextraktion (Grafiken aus dem Quelltext: ksys in Nr. 7 und 18, Rechteck-Skizze in Nr. 24):']
prot.append('  ' + zaehlung(DATEIEN[0], 0))
prot.append('  ' + zaehlung(DATEIEN[1], 3))
prot.append('  ' + zaehlung(DATEIEN[2], 3))
prot.append('  ' + zaehlung(DATEIEN[3], 0))
for pdf in DATEIEN[1:3]:
    prot.append(f'  Verzeichnis {pdf} ({links(pdf)} Links):')
    prot += ['    ' + l for l in verzeichnis(pdf)]
prot += ['', 'Werkzeugaufrufe (Schritt · Anlass):'] + ['  ' + l for l in SCHRITTE.splitlines()]
prot += ['', 'Vorlage: fehlende Bausteine · \\zweigzeile (zweite Zeile des Einheitenkopfs), \\abhakkopf und \\abhak '
         '(Abhakseite), \\vzeile (Verzeichniszeile mit Link); Befund gleichungsraster: Zeilentiefe ohne die letzte '
         'Schreibzeile (Überhang auf die Folgezeile, auch ohne \\weit) · Warnungen aus dem Log: keine '
         '(keine Package mathblatt Warning, keine Overfull-Box)',
         'Korrekturrunden: 9 von 113 Schritten']
prot += zeiten()
open('protokoll.txt', 'w', encoding='utf-8').write('\n'.join(prot) + '\n')

chat = ['Eingabe des Lehrers:', EINGABE, '', 'Deutungszeile und Plan:', DEUTUNG] + PLAN + \
       ['', 'Planfrage: ' + PLANFRAGE, 'Antwort: ' + ANTWORT, '', 'Nach der Zone:', DATEIEN[0], ZONEZEILE,
        '', 'Übergebene Dateien:'] + DATEIEN + ['', 'Ausgabeblock:'] + AUSGABE
open('chat.txt', 'w', encoding='utf-8').write('\n'.join(chat) + '\n')

name = f'{THEMA}_2026-09-25_protokoll.zip'
muster = ['*.pdf', '*.tex', '*.log', 'pruef.py', 'pruef_out_*.txt', 'rahmen.py', 'archiv.py', 'mathblatt.sty',
          'Anleitung_mathblatt.md', 'quadratische-gleichungen.md', 'zeiten.txt', 'protokoll.txt', 'chat.txt']
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as z:
    n = 0
    for m in muster:
        for f in sorted(glob.glob(m)):
            z.write(f)
            n += 1
print(name, n, 'Dateien')
print('\n'.join(prot[-12:]))
