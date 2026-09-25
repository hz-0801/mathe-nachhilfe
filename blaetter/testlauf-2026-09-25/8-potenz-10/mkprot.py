# mkprot.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3)
import re, subprocess, zipfile, glob, os

THEMA = 'PotenzExponentialFkt'
ARCHIV = f'{THEMA}_2026-09-25_protokoll.zip'
PDFS = {'Zone': f'{THEMA}_KennstDuSchon.pdf', 'Lernblatt': f'{THEMA}_Lernblatt.pdf',
        'Gesamt': f'{THEMA}_Gesamt.pdf', 'Lösungen': f'{THEMA}_Loesungen.pdf'}
QUELLEN = {'Zone': ['zone_a.tex'], 'Lernblatt': [f'e{i}_a.tex' for i in range(1, 6)],
           'Gesamt': ['zone_a.tex'] + [f'e{i}_a.tex' for i in range(1, 6)], 'Lösungen': ['e5_l.tex']}

def text(pdf, s=None):
    arg = ['pdftotext', '-layout', '-enc', 'UTF-8']
    if s: arg += ['-f', str(s), '-l', str(s)]
    return subprocess.run(arg + [pdf, '-'], capture_output=True, text=True, encoding='utf-8').stdout

def seiten(pdf):
    return int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))

def grafiken(dateien):
    n = 0
    for d in dateien:
        t = open(d, encoding='utf-8').read()
        n += len(re.findall(r'\\begin\{ksys\}', t)) + len(re.findall(r'\\leeresgitter\{', t))
    return n

zeilen = []
for name, pdf in PDFS.items():
    t = text(pdf); s = seiten(pdf)
    if name == 'Lösungen':
        nrs = re.findall(r'^\s*(\d+)\)', t, re.M)
        zeilen.append(f'{name} ({pdf}): Nummern mit Lösung {len(nrs)} (1–51) · Grafiken {grafiken(QUELLEN[name])} · Seiten {s}')
    else:
        # Abhakseiten nicht mitzählen
        auf = ''.join(text(pdf, i) for i in range(1, s + 1) if 'Das kann ich' not in text(pdf, i) or i == 1)
        hn = re.findall(r'^\s*(\d+)\. Ich', auf, re.M)
        ta = re.findall(r'(?:^|\s)[a-z]\) ', auf)
        zeilen.append(f'{name} ({pdf}): Hauptnummern {len(hn)} ({hn[0]}–{hn[-1]}) · Teilaufgaben {len(ta)} '
                      f'(Buchstaben a) … in der Textextraktion, Verweise wie „für f)“ mitgezählt) · '
                      f'Grafiken {grafiken(QUELLEN[name])} (aus den Quelltexten: ksys, leere Gitter) · Seiten {s}')
verz = {}
for art in ('lernblatt', 'gesamt'):
    v = open(f'{art}_toc.tex', encoding='utf-8').read()
    verz[art] = [re.sub(r'\\hyperlink\{[^}]*\}\{(.*)\}\\par\\smallskip', r'\1', l) for l in v.strip().splitlines()]

z = {}
for l in open('zeiten.txt').read().split('\n'):
    if l.strip():
        k, v = l.rsplit(' ', 1); z.setdefault(k, []).append(int(v))
t0 = z['t0'][0]
dt = lambda k: z[k][-1] - t0

prot = f'''Prompt: Unterrichtsblatt-Prompt v4.3
Modell: Claude Opus 5.5 (claude-opus-5-5)
Vorlage: Version 2026-09-22h
Katalog: potenz-exponentialfunktionen.md, Status: gegengelesen bis auf [FS] (2026-09-11i, vierzehnter Gegenlese-Block, Solo; Entwurf 2026-09-09d, Zitierform der LISUM-Zeile am 10e vereinheitlicht)
Bestellung: mit Wiederholung · mit Ausblick (Thema nicht im Register der Blätter; kein Zweig mit späterer Marke)
Standpunkt: Kl. 10, Oberschule (keine Schulform genannt; Gymnasium als Zusatz)

Zweige (gebaut, alle nach Planfrage „alle“; abgewählt: keine; Ausblick: keiner)
Einheit 1 · Lineares und exponentielles Wachstum unterscheiden – Hier lernst du, an Tabellen, Texten und Graphen zu erkennen, ob ein Wert linear oder exponentiell wächst · neu in diesem Jahr · P10 oft · baut auf: Zunahme um denselben Betrag, Erhöhen um Prozent mit einer Dezimalzahl, Punkte im Koordinatensystem
Einheit 2 · Wachstumsfaktor und Wachstumstabelle – Hier lernst du, aus dem Prozentsatz den Wachstumsfaktor zu bilden und eine Wachstumstabelle mit ihm fortzuschreiben · neu in diesem Jahr · P10 oft · baut auf: Einheit 1, Prozentwert und Prozentsatz, Zinseszins, Quotient zweier Werte
Einheit 3 · Exponentialfunktion aufstellen und auswerten – Hier lernst du, eine Gleichung für ein Wachstum aufzustellen und damit Werte und Zeitpunkte zu berechnen · neu in diesem Jahr · P10 · baut auf: Einheit 2, Potenz mit dem Taschenrechner, Zinseszins
Einheit 4 · Verdopplungs- und Halbwertszeit – Hier lernst du, die Zeit zu bestimmen, nach der sich ein Wert verdoppelt oder halbiert hat · neu in diesem Jahr · P10 · baut auf: Einheit 3, Wertetabelle und Graph lesen, Potenz mit dem Taschenrechner
Einheit 5 · Potenzfunktionen mit natürlichem Exponenten – Hier lernst du Funktionen wie y = x³ und y = x⁴ kennen: Wertetabelle, Graph und Eigenschaften · neu in diesem Jahr (am Gymnasium schon seit Klasse 9) · keine P10-Aufgabe · baut auf: Einheit 3, Normalparabel, Punkte im Koordinatensystem

Hauptnummern mit Titel
'''
for datei in ['zone_a.tex'] + [f'e{i}_a.tex' for i in range(1, 6)]:
    pass
ab = open('abhaken.tex', encoding='utf-8').read()
for m in re.finditer(r'\\textbf\{([^}]*)\}|\\abhak\{(\d+)\}\{(.*)\}', ab):
    if m.group(1): prot += f'{m.group(1)}\n'
    else: prot += f'  {m.group(2)}. {m.group(3)}\n'
prot += '\nZählung je Datei (Textextraktion des Kompilats)\n' + '\n'.join(zeilen) + '\n'
prot += '\nVerzeichnis Lernblatt (wortgleich)\n' + '\n'.join(verz['lernblatt']) + '\n'
prot += '\nVerzeichnis Gesamt (wortgleich)\n' + '\n'.join(verz['gesamt']) + '\n'
prot += '''
Werkzeugaufrufe (Schritt · Anlass)
1 · Zeitstempel t0
2 · Themenregister und Register der Blätter geholt (curl) – Thema potenz-exponentialfunktionen.md, im Register der Blätter nicht geführt → mit Ausblick
3–4 · Registerzeilen gelesen (Ausgabe über 30 KB, Datei durchsucht)
5 · Katalogeintrag geholt und gelesen (2 Leseschritte)
6 · mathblatt.sty und Anleitung_mathblatt.md geholt; Anleitung gelesen
7–9 · Makronamen und -definitionen der Vorlage nachgeschlagen (einheitenkopf, ksys-Schlüssel, punktfeld, wertetabelleleer)
10–12 · zone_a.tex, zone_l.tex, pruef.py geschrieben
13 · Korrektur Zone (vor dem Kompilieren): Punkt A(1|20) → A(1|50) (Sperrzahl 20)
14 · pruef.py berichtigt (Kontrollwert frühes Runden), zone.tex geschrieben
15 · Zone gerechnet und kompiliert – Korrekturrunde: pruef meldet „Sperrzahlen im Aufgabenquelltext: 1,5“ (Nr. 8 e); xelatex lief nicht: PowerShell setzte -jobname=$j wörtlich
16 · Korrektur: 1,5 % → 1,8 % in Nr. 8 e, xelatex direkt aufgerufen
17–18 · build.py geschrieben; Zone gerechnet, kompiliert, gerendert: 0 Abweichungen, Log ohne Warnung (Stempel „zone“)
19 · Korrekturrunde Zone: Nr. 4 Punktfelder „A( ___ | ___ )“ im \\leerfeld brechen in teilezwei um; \\wertetabelleleer zeigt nur eine schmale Spalte; Einheit „l“ bei \\leerfeld[l] liest sich als 1 → \\punktfeldn im Vorspann, \\sachtabelle mit \\leerzelle, „Liter“
20–22 · lernblatt.tex (Rahmen), e1_a.tex, e1_l.tex geschrieben; pruef.py um e1 und Sperrliste erweitert
23 · E1 gerechnet und kompiliert (Stempel „weiter“) – Korrekturrunde: „Package mathblatt Warning: Hauptnummer 15 ist hoeher als eine Seite und wird umbrochen“; „Overfull \\hbox (29.28885pt too wide) in paragraph at lines 120--121“; Sperrzahlen 30 (Nr. 11 e) und 54 (Fehltreffer aus 0.54\\linewidth); Graphenlabels II/III am rechten Rand abgeschnitten; Nr. 13 Felder ohne Flucht; Nr. 14 Kreuze umbrochen
24 · Korrektur E1: Systeme in Nr. 14/15 verkleinert (x bis 4 bzw. 6), Labelstelle gesetzt, Nr. 13 in geruest, Nr. 11 e 4; 40; 400; 4 000, Jonas-Zitat als Absatz statt \\rechnung, Sperrscan ohne Befehlsargumente
25 · Korrekturrunde E1: „Overfull \\hbox (29.28885pt too wide) in paragraph at lines 120--121“ (ksys in minipage 0.44) → minipage 0.52/0.46; danach Log ohne Warnung
26–27 · e2_a.tex, e2_l.tex geschrieben, pruef.py um e2 erweitert (Stempel „e 1“ im nächsten Aufruf)
28 · E2 gerechnet und kompiliert: 0 Abweichungen, Log ohne Warnung, keine Grafikseite
29–31 · e3_a.tex, e3_l.tex, pruef.py e3 (Stempel „e 2“ im nächsten Aufruf)
32 · E3 gerechnet und kompiliert – Korrekturrunde: „! Dimension too large.“ (\\zahlenstrahl mit xmin=2018)
33 · Korrektur E3: Zeitleiste als \\sachtabelle 2019–2027; Log: Overfull \\hbox 3,25 pt im geruest Nr. 29 (hingenommen)
34–37 · e4_a.tex, Tabellenwerte 625/706 berichtigt, Startwert der E-Auto-Grafik 1,6 statt 1,5 (Sperrzahl), e4_l.tex, pruef.py e4
38 · E4 gerechnet und kompiliert (Stempel „e 3“) – Korrekturrunde: „39a 5 · 80.454287 · 80,4 · ABWEICHUNG“; Sperrzahlen 20, 20, 30 (Tabellenköpfe 0–20 und „30 Tage“)
39 · Korrektur E4: Lösung 80,5; Tabellenköpfe 0; 4; 8; 12; 16 und 0; 9; 18; 27; 36; „vier Wochen (28 Tage)“ → 0 Abweichungen
40–43 · e5_a.tex, Zeichenfläche bis y = 16, e5_l.tex, pruef.py e5 (Stempel „e 4“)
44 · E5 gerechnet und kompiliert – Korrekturrunde: Nr. 47 Label I nicht erkennbar, Kreuze in Nr. 47 e umbrochen, Nr. 48 teilezwei gedrängt
45 · Korrektur E5: Labelstelle 1,25, Kreuze in neue Zeile, Nr. 48 als teile
46 · Ausschnitt Nr. 47 bei 150 dpi gerendert: Label I vorhanden
47–50 · gen.py (Abhakseite, Verzeichnisse), gesamt.tex, loesungen.tex geschrieben
51 · Abhakseite erzeugt, Lernblatt zweimal kompiliert, Verzeichnis aus der Textextraktion, zweiter Lauf stabil (Stempel „e 5“, „lernblatt“)
52 · Gesamt zweimal kompiliert, Verzeichnis stabil, Links geprüft (Stempel „gesamt“)
53 · Lösungen kompiliert, Nummern 1–51 geprüft, Hauptnummern im Gesamt 1–51 durchlaufend (Stempel „loesungen“)
54 · mkprot.py geschrieben
55 · alle pruef-Läufe wiederholt (Endstand), protokoll.txt, chat.txt, Archiv

Vorlage: fehlende Bausteine · \\zweigzeile (zweite Zeile des Einheitenkopfs), \\punktfeldn (Punktfeld mit Punktnamen), \\leeresgitter (Gitter ohne Bezifferung für „Achseneinteilung wählen“), \\langzelle (lange Schreiblinie in \\sachtabelle), \\abhak (Abhakzeile) – alle im Vorspann der Rahmendateien; Warnungen aus dem Log · Overfull \\hbox (3.25053pt too wide) in paragraph at lines 21--26 (e3_a.tex, geruest Nr. 29), sonst keine
'''
prot += f'''Korrekturrunden: 9 von 55 Schritten
Zone: {dt('zone')} s (letzter von zwei Stempeln „zone“; der erste stammt aus dem fehlgeschlagenen Kompilieraufruf; die Punktfeld-Korrektur lag nach dem Stempel)
Weiter: {z['weiter'][0]} (unbeaufsichtigter Lauf, keine Wartezeit; Stempel {dt('weiter')} s nach t0)
E 1: {dt('e 1')} s
E 2: {dt('e 2')} s
E 3: {dt('e 3')} s
E 4: {dt('e 4')} s
E 5: {dt('e 5')} s
Lernblatt: {dt('lernblatt')} s
Gesamt: {dt('gesamt')} s
Lösungen: {dt('loesungen')} s
Hinweis: Die Stempel „e n“ stehen jeweils im ersten Aufruf nach der bestandenen Prüfung der Einheit (Stempel eine Aufrufrunde später).
'''
open('protokoll.txt', 'w', encoding='utf-8').write(prot)

chat = open('chat_vorlage.txt', encoding='utf-8').read()
open('chat.txt', 'w', encoding='utf-8').write(chat)

with zipfile.ZipFile(ARCHIV, 'w', zipfile.ZIP_DEFLATED) as zf:
    muster = ['*.pdf', '*.tex', '*.log', 'pruef.py', 'pruef_out_*.txt', 'mathblatt.sty', 'Anleitung_mathblatt.md',
              'potenz-exponentialfunktionen.md', 'zeiten.txt', 'protokoll.txt', 'chat.txt', 'build.py', 'gen.py',
              'linkcheck.py', 'mkprot.py']
    namen = sorted({f for m in muster for f in glob.glob(m)})
    for f in namen: zf.write(f)
print(ARCHIV, len(namen), 'Dateien')
print('\n'.join(zeilen))
