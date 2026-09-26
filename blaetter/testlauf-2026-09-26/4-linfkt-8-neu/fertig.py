# fertig.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (ein Aufruf)
import re, subprocess, zipfile, glob, os

def txt(pdf):
    return subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, '-'], capture_output=True).stdout.decode('utf-8')

def seiten(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True).stdout.decode('utf-8', 'replace')
    return int(re.search(r'Pages:\s+(\d+)', out).group(1))

def grafiken(texs):
    n = 0
    for t in texs:
        n += open(t, encoding='utf-8').read().count('\\begin{ksys}')
    return n

einh = ['e1_a.tex', 'e2_a.tex', 'e3_a.tex', 'e4_a.tex', 'e5_a.tex']
zaehl = []
for pdf in ['LinFkt_Lernblatt.pdf', 'LinFkt_Gesamt.pdf']:
    t = txt(pdf)
    hn = len(re.findall(r'(?m)^\s*\d{1,2}\. Ich', t))
    ta = len(re.findall(r'(?m)(?:^|\s)[a-h]\)\s', t.split('Das kann ich\n')[0] if False else t))
    zaehl.append(f'{pdf}: Hauptnummern {hn}, Teilaufgaben {ta} (Buchstaben in der Textextraktion, einschließlich Abhakseite 0), '
                 f'Grafiken {grafiken(einh)} Koordinatensysteme, Seiten {seiten(pdf)}')
t = txt('LinFkt_Loesungen.pdf')
nl = sorted(set(int(m) for m in re.findall(r'(\d{1,2})\)\s+(?:a\)|zum|Anfangswert)', t)))
zaehl.append(f'LinFkt_Loesungen.pdf: Nummern mit Lösung {len(nl)} (1–53), Grafiken 0, Seiten {seiten("LinFkt_Loesungen.pdf")}')

verz = open('verzeichnis.tex', encoding='utf-8').read().strip()
verz_klar = re.sub(r'\\verz\{[^}]*\}\{([^}]*)\}', r'\1', verz).replace('\\verztrenn', '·').replace('\\verzeichniszeile{', '')[:-1]

st = {}
for z in open('zeiten.txt', encoding='ascii').read().splitlines():
    teile = z.rsplit(' ', 1)
    st[teile[0]] = int(teile[1])
t0 = st['t0']
zeiten = ['Zone: kein Stempel (ohne Zone, Bestellung „nur das Neue“)', 'Weiter: kein Stempel (kein Halt, Bau in einem Durchgang)']
for k in ['e 1', 'e 2', 'e 3', 'e 4', 'e 5', 'lernblatt', 'gesamt', 'loesungen']:
    name = {'lernblatt': 'Lernblatt', 'gesamt': 'Gesamt', 'loesungen': 'Lösungen'}.get(k, 'E ' + k[2:])
    zeiten.append(f'{name}: {st[k] - t0} s')

sty2 = open('mathblatt.sty', encoding='utf-8').read().splitlines()[1].lstrip('% ').strip()
stand = open('lineare-funktionen.md', encoding='utf-8').read().splitlines()[1].strip()

schritte = """1 Read unterrichtsblatt.md Teil 1 · Anleitung lesen
2 Read unterrichtsblatt.md Teil 2 · Anleitung bis zur letzten Zeile
3 PowerShell · Arbeitsverzeichnis, Stempel t0
4 PowerShell curl · Themenregister und Register der Blätter (1.2)
5 Grep · Themenregister nach „linear“ (Ausgabe zu lang für die Anzeige)
6 Grep · Register der Blätter suchen
7 Read · Register der Blätter lesen: lineare Funktionen noch nicht gebaut
8 PowerShell curl · Eintrag lineare-funktionen.md
9 Read · Eintrag ganz lesen
10 PowerShell curl · mathblatt.sty und Anleitung (4.5)
11 Read · Anleitung Teil 1
12 Read · Anleitung Teil 2
13 Write · einheit.tex (Prüfrahmen je Einheit)
14 Write · einheit_l.tex (Prüfrahmen Lösungen)
15 Write · e1_a.tex
16 Write · e1_l.tex
17 Write · pruef.py mit Einheit 1
18 Edit · pruef.py, Prüfzeile 4g sauber modelliert
19 PowerShell · pruef e1, Kompilieren, Rendern, Log
20 Read · Seite E1-1: Tabellen in teilezwei überlappen (Overfull 19–27 pt, \\wertetabelle zu breit)
21 Read · Seite E1-2
22 Read · Seite E1-3: Nr. 4 fast eine ganze Seite hoch, −2.5 mit Dezimalpunkt in \\wertetabelle
23 Read · Seite E1-4: Log „There's no line here to end.“ bei Nr. 6 (\\\\ nach \\wertetabelle)
24 Edit · Korrektur: Nr. 1 in teile statt teilezwei
25 Edit · Korrektur: Nr. 4 geteilt (4/5), Tabelle ohne Dezimalwert
26 Edit · Korrektur: Nr. 6 (jetzt 7) ohne \\\\ nach der Tabelle
27 Write · e1_l.tex neu nummeriert
28 Edit · pruef.py neu nummeriert
29 PowerShell · Prüfung und Kompilat E1, Stempel e 1
30 PowerShell · PIL vorhanden? (nein)
31 Read · Seite E1-1
32 Read · Seite E1-3
33 Read · Seite E1-4
34 Read · Lösungen E1
35 Edit · Lösungen E1: (1|{-2}) statt binärem Minus
36 Write · e2_a.tex
37 Write · e2_l.tex
38 Edit · pruef.py Einheit 2
39 PowerShell · pruef e2 bricht ab („'BooleanTrue' object has no attribute 'evalf'“), Kompilat E2
40 Edit · Korrektur Skript: Vergleich von Wahrheitswerten
41 PowerShell · pruef e2 und e1 erneut: 0 Abweichungen
42 Read · Seite E2-1
43 Read · Seite E2-2
44 Read · Seite E2-3
45 Read · Seite E2-4: Labels 3 und 4 von Nr. 17 übereinander, Label 1 fehlt
46 Read · Seite E2-5
47 PowerShell · Ausschnitte vergrößern
48 Read · Ausschnitt Nr. 17
49 Read · Ausschnitt Nr. 12
50 Edit · Korrektur \\gerade-Labelstellen in Nr. 17
51 PowerShell · Kompilat E2, Stempel e 2
52 Read · Ausschnitt Nr. 17 nach Korrektur
53 Write · e3_a.tex
54 Write · e3_l.tex
55 Edit · pruef.py Einheit 3
56 PowerShell · pruef e3, Kompilat E3
57 Read · Seite E3-1
58 Read · Seite E3-2
59 Read · Seite E3-3: \\punktfeld setzt selbst „S(…|…)“, „S_y = S(…)“ doppelt
60 Read · Seite E3-4
61 Edit · Korrektur Nr. 28 ohne S_y/S_x
62 Edit · Korrektur Anweisung Nr. 25 (y statt f)
63 Edit · Korrektur Nr. 25 g) in derselben Schreibweise
64 Edit · Lösungen E3: Buchstaben der geteilten Nummer 27 (a–c) und Nr. 28
65 Edit · Lösungen E2: Buchstaben der geteilten Nummer 15 (a–d)
66 Edit · Lösungen E1: Buchstaben der geteilten Nummer 5 (a–c)
67 PowerShell · pruef.py Schlüssel an die Buchstaben angepasst
68 PowerShell · pruef e1–e3, Kompilat E3, Stempel e 3
69 Read · Seite E3-3 nach Korrektur
70 Write · e4_a.tex
71 Write · e4_l.tex
72 PowerShell · Korrektur vor dem Kompilieren: Nr. 36 a) ergab y = 3x + 1 (Original 2021-OS-K2a), Werte getauscht; Nr. 42 a) angepasst
73 PowerShell · Korrektur Nr. 39 c) (Zahlen des Fehlermusters 3x + 2 vermieden)
74 Edit · pruef.py Einheit 4
75 PowerShell · pruef e4, Kompilat E4
76 Read · Seite E4-1
77 Read · Seite E4-2
78 Read · Seite E4-3
79 Read · Seite E4-4
80 Read · Seite E4-5
81 PowerShell · Ausschnitte vergrößern
82 Read · Ausschnitt Nr. 34: Labels t und r übereinander, t sehr steil
83 Read · Ausschnitt Nr. 35 (leer, falscher Ausschnitt)
84 PowerShell · Korrektur Gerade t in Nr. 34, Prüfung, Kompilat, Stempel e 4
85 Read · Ausschnitt Nr. 34 nach Korrektur
86 Write · e5_a.tex
87 Write · e5_l.tex
88 PowerShell · Korrektur vor dem Kompilieren: Tarif-Buchstaben A/B/C (Kollision mit Punkten A, B der Einheit 4) durch Namen ersetzt
89 Edit · pruef.py Einheit 5
90 PowerShell · pruef e5, Kompilat E5
91 Read · Seite E5-1: Zeilen vor \\leerfeld sichtbar gedehnt (Nr. 47 a, c)
92 Read · Seite E5-2
93 Read · Seite E5-3: Nr. 53 allein auf der Seite (unter einem Drittel gefüllt)
94 PowerShell · Korrekturaufruf abgelehnt (Pfadschutz meldete „Remove-Item on system path '\\quad' is blocked“)
95 Read · e5_a.tex Zeilen 34–73
96 Edit · Korrektur Nr. 47 a): \\\\ vor dem Feld
97 Edit · Korrektur Nr. 47 c): \\\\ vor dem Feld
98 Edit · Korrektur Nr. 49: Grafik und Teilaufgaben nebeneinander
99 PowerShell · Kompilat E5: 2 Seiten
100 Read · Seite E5-2 nach Korrektur
101 Read · Seite E5-1 nach Korrektur
102 PowerShell · pruef e5, Stempel e 5, Titelliste für die Abhakseite
103 Write · abhaken.tex
104 Write · verzeichnis.tex
105 Write · lernblatt.tex
106 Write · gesamt.tex
107 Write · loesungen.tex
108 Edit · Nr. 3: Geradenname g in Mathematik
109 PowerShell · Lernblatt zweimal kompiliert, Kopfzeilen und Nummern je Seite, Stempel lernblatt
110 PowerShell · Seiten rendern, Sprungziele der Verzeichniszeile prüfen
111 Read · Lernblatt Seite 1
112 Read · Lernblatt Seite 22 (Das kann ich)
113 Read · Lernblatt Seite 23 (Das kann ich)
114 PowerShell · Gesamt zweimal kompiliert, Kopfzeilen, Nummern 1–53 lückenlos, Stempel gesamt
115 PowerShell · Lösungen kompiliert, 53 Nummern mit Lösung, Stempel loesungen
116 Read · Lösungen Seite 1
117 Write · chat.txt (Entwurf)
118 Write · fertig.py
119 PowerShell · fertig.py: protokoll.txt, chat.txt, Archiv"""

prot = []
prot += ['Prompt: Unterrichtsblatt-Prompt v4.4', 'Modell: Claude Opus 5.5 (claude-opus-5-5)', f'Vorlage: {sty2}',
         f'Katalog: lineare-funktionen.md, {stand}', 'Bestellung: nur das Neue', 'Standpunkt: Klasse 8, Oberschule (Gymnasium gleich)', '']
prot += ['Zweige (gebaut, alle fünf; abgewählt: keine; Ausblick: keiner):']
for f, bereich in zip(einh, ['1–9', '10–21', '22–33', '34–44', '45–53']):
    s = open(f, encoding='utf-8').read()
    kopf = re.search(r'\\einheitenkopf\[[^]]*\]\[[^]]*\]\{(.*)\}', s).group(1)
    zz = re.search(r'\\zweigzeile\{(.*)\}', s).group(1)
    prot.append(f'{kopf} (Nr. {bereich}) – {zz}')
    for m in re.finditer(r'\\begin\{aufgabe\}\{(.*?)(?:\\newline.*)?\}\s*$', s, re.M):
        prot.append('   ' + m.group(1))
prot += ['', 'Zählung aus der Textextraktion:'] + zaehl + ['Verzeichniszeile (Lernblatt und Gesamt): ' + verz_klar, '']
prot += ['Schritte (Schritt · Anlass):'] + schritte.splitlines() + ['']
prot += ['Vorlage: fehlende Bausteine keine · Warnungen aus dem Log: keine Package mathblatt Warning; Overfull \\hbox 4,4 pt (Nr. 12, kleine Systeme) und 5,9 pt (Nr. 49, Achsentitel neben der Grafik)',
         'Befunde zur Vorlage: \\punktfeld setzt „S(…|…)“ mit S; \\wertetabelle ist für teilezwei zu breit; \\wertetabelle setzt Dezimalwerte mit Punkt.',
         'Korrekturrunden: 8 von 119 Schritten']
prot += zeiten
open('protokoll.txt', 'w', encoding='utf-8').write('\n'.join(prot) + '\n')

chat = open('chat.txt', encoding='utf-8').read()
open('chat.txt', 'w', encoding='utf-8').write(chat)

name = 'LinFkt_2026-09-26_protokoll.zip'
dateien = sorted(set(glob.glob('*.pdf') + glob.glob('*.tex') + glob.glob('*.log') + glob.glob('pruef_out_*.txt') +
                     ['pruef.py', 'mathblatt.sty', 'Anleitung_mathblatt.md', 'lineare-funktionen.md', 'zeiten.txt',
                      'protokoll.txt', 'chat.txt', 'fertig.py', 'linkcheck.py']))
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as z:
    for d in dateien:
        z.write(d)
print(name, len(dateien), 'Dateien')
print('\n'.join(zaehl))
print('\n'.join(zeiten))
