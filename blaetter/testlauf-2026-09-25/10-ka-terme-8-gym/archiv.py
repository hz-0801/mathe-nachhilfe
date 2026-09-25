# -*- coding: utf-8 -*-
# archiv.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (ein Aufruf).
import io, re, os, glob, zipfile, subprocess

THEMA = 'TermeBinomischeFormeln'
DATUM = '2026-09-25'

def lies(d):
    return io.open(d, encoding='utf-8').read()

# ---------------------------------------------------------------- Zweige
ZWEIGE = [
 ('Einheit 1 von 5 · Klammern auflösen (terme.md, Einheit 3)', 'Hier lernst du, Klammern mit Plus, Minus oder einer Zahl davor aufzulösen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Terme zusammenfassen, Malnehmen mit Vorzeichen'),
 ('Einheit 2 von 5 · Ausklammern (terme.md, Einheit 4)', 'Hier lernst du, einen gemeinsamen Faktor vor die Klammer zu ziehen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Zahl mal Klammer (Einheit 1)'),
 ('Einheit 3 von 5 · Summe mal Summe (binomische-formeln.md, Einheit 1)', 'Hier lernst du, Terme mit zwei Variablen zusammenzufassen und zwei Klammern miteinander malzunehmen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Klammern auflösen (Einheit 1), Terme zusammenfassen, Terme malnehmen'),
 ('Einheit 4 von 5 · Binomische Formeln (binomische-formeln.md, Einheit 2)', 'Hier lernst du, Quadrate von Klammern mit den drei binomischen Formeln auszumultiplizieren · neu in diesem Jahr · P10 · baut auf: Summe mal Summe (Einheit 3), Minusklammer (Einheit 1), Quadratzahlen'),
 ('Einheit 5 von 5 · Faktorisieren (binomische-formeln.md, Einheit 3)', 'Hier lernst du, eine Summe mit einer binomischen Formel in ein Produkt zu verwandeln · neu in diesem Jahr (an der Oberschule je nach Buch bis Klasse 10) · keine P10-Aufgabe · baut auf: binomische Formeln (Einheit 4), Ausklammern (Einheit 2)'),
]

SCHRITTE = [
 'Arbeitsverzeichnis ansehen (Glob) · leer',
 't0-Stempel · Beginn des Baus',
 'Themenregister und Blattregister holen · Ausgabe zu groß, in Datei abgelegt',
 'Register nach terme/binomisch durchsuchen · Zeilen 26 und 30',
 'Registerzeilen ausgeben · terme.md und binomische-formeln.md gewählt',
 'Blattregister lesen · Thema nicht geführt → Bestellung mit Ausblick (kein Zweig nach Kl. 8)',
 'Einträge terme.md und binomische-formeln.md holen · je eine Datei',
 'Eintrag binomische-formeln.md lesen',
 'Eintrag terme.md lesen',
 'Vorlage und Anleitung holen · Version 2026-09-22h',
 'Anleitung lesen',
 'Vorlage: Zählername der Hauptnummern suchen · aufgabe',
 'Vorlage: Ausschnitt Z. 100–299 lesen · Umgebung aufgabe, gleichungsraster, Einheitenkopf ohne zweite Zeile',
 'zone_a.tex schreiben',
 'zone_l.tex schreiben',
 'Rahmen KennstDuSchon schreiben',
 'check.tex (Prüfsatz je Einheit) schreiben',
 'pruef.py mit Zone schreiben',
 'Zone rechnen, kompilieren, rendern, zone-Stempel · 0 Abweichungen, 1 Seite, Kastentreffer x^2+3x als Teilstring von 2x^2+3x gewertet (kein Kastenterm)',
 'Zone Seite 1 ansehen · in Ordnung',
 'Zone Lösungsseite ansehen · in Ordnung',
 'e1_a.tex schreiben',
 'e1_l.tex schreiben',
 'pruef.py: Einheit 1 ergänzt',
 'weiter-Stempel; Einheit 1 rechnen, kompilieren, rendern · 0 Abweichungen; Kastentreffer „-(x-4)“ im Beispiel 9 − (x − 4)',
 'e1 Seite 1 ansehen · gleichungsraster: letzte Schreiblinie läuft durch den Text der nächsten Zeile',
 'e1 Seite 2 ansehen · dasselbe bei Nr. 11 und 12',
 'e1 Seite 3 ansehen · „gleichwertig."Hat – ASCII-Schlusszeichen verschluckt das Leerzeichen',
 'Ausschnitt vergrößert rendern · Raster Nr. 10',
 'Ausschnitt ansehen',
 'zweiten Ausschnitt rendern',
 'zweiten Ausschnitt ansehen · Linie liegt auf c) 10 + (x − 6)',
 'Korrektur e1: Rasterzeilen \\\\[3mm], Beispiel 9 − (x − 2), Anführungszeichen',
 'pruef.py: Beispiel 12B angepasst',
 'e1 neu kompilieren · \\\\[3mm] wirkt nicht, Überlappung bleibt',
 'e1 Seite 2 ansehen · Überlappung bleibt',
 'e1 Seite 3 ansehen · Überlappung bleibt bei Nr. 13',
 'Korrektur per Python-Einzeiler · von der Sandbox abgewiesen (Pfadprüfung), nichts geändert',
 'Korrektur e1: \\\\[3mm] → \\\\ \\noalign{\\vspace{5mm}}',
 'e1 neu kompilieren, e1-Stempel · 0 Abweichungen, 4 Seiten',
 'e1 Seite 2 ansehen · Abstand in Ordnung',
 'e1 Seite 3 ansehen · in Ordnung',
 'e2_a.tex schreiben',
 'e2_l.tex schreiben',
 'pruef.py: Einheit 2 ergänzt',
 'pruef.py: ggT-Prüfung vereinfacht',
 'pruef.py: Funktion ggt ergänzt',
 'Einheit 2 rechnen, kompilieren, rendern, e2-Stempel · 0 Abweichungen, 3 Seiten; Kastentreffer nur Teilstrings über Termgrenzen',
 'pruef.py: Kastenprüfung trennt Terme mit |',
 'e2 Seite 1 ansehen · in Ordnung',
 'e2 Seite 2 ansehen · in Ordnung',
 'e3_a.tex schreiben',
 'e3_l.tex schreiben',
 'e3_l.tex: Nr. 24 Buchstaben a–e statt f–j',
 'pruef.py: Einheit 3 ergänzt',
 'Einheit 3 rechnen, kompilieren, rendern, e3-Stempel · 0 Abweichungen, 4 Seiten; Kastentreffer nur Teilstrings',
 'e3 Seite 1 ansehen · in Ordnung',
 'e3 Seite 2 ansehen · in Ordnung',
 'e3 Seite 3 ansehen · Flächenbild in Ordnung',
 'e4_a.tex schreiben',
 'e4_a.tex: a und b im Text als Mathematik',
 'e4_l.tex schreiben',
 'pruef.py: Einheit 4 ergänzt',
 'Einheit 4 rechnen, kompilieren, e4-Stempel · 0 Abweichungen; Kastentreffer (x+5)^2 in 2·(x + 5)^2',
 'Korrektur e4: 2·(x + 5)^2 → 4·(x − 1)^2 in Aufgabe, Lösung, pruef.py',
 'Einheit 4 neu, e4-Stempel · 0 Abweichungen, keine Kastentreffer, 5 Seiten',
 'e4 Seite 1 ansehen · in Ordnung',
 'e4 Seite 2 ansehen · in Ordnung',
 'e4 Seite 3 ansehen · in Ordnung',
 'e4 Seite 4 ansehen · Flächenbild in Ordnung',
 'e5_a.tex schreiben',
 'e5_l.tex schreiben',
 'pruef.py: Einheit 5 und Doppelprüfung ergänzt',
 'pruef.py: quadrat_von',
 'pruef.py: mittelglied_passt bereinigt',
 'pruef.py: Ausgabe der Doppelprüfung',
 'Einheit 5 rechnen, kompilieren, rendern, e5-Stempel · 1 Abweichung 46a: Skript zog die Wurzel ohne Positivannahme (Skriptfehler)',
 'pruef.py: 46a mit positivem w',
 'pruef.py e5 neu, e5-Stempel · 0 Abweichungen, keine doppelten Aufgabenterme',
 'e5 Seite 1 ansehen · in Ordnung',
 'e5 Seite 2 ansehen · Nr. 43 b: Feld nach „(x + 4)^2+“ umbrochen, Zeile gedehnt',
 'e5 Seite 3 ansehen · in Ordnung',
 'Korrektur e5: Gleichung von 43 b in eigene Zeile',
 'abhaken.tex schreiben',
 'Rahmen Lernblatt schreiben',
 'Rahmen Gesamt schreiben',
 'Rahmen Lösungen schreiben',
 'verz.py schreiben',
 'Lernblatt: Platzhalter, kompilieren, Verzeichnis, kompilieren, prüfen, lernblatt-Stempel · Verzeichnis und Links in Ordnung, 18 Seiten, Abhakseite auf zwei Seiten',
 'Lernblatt Seite 1 ansehen · Verzeichnis in Ordnung',
 'Lernblatt Seite 17 ansehen · Abhakseite läuft über',
 'Lernblatt Seite 18 ansehen',
 'Lernblatt Seite 15 ansehen · Nr. 43 b in Ordnung',
 'abhaken.tex: parskip 0 (Anfang)',
 'abhaken.tex: Gruppe schließen',
 'Lernblatt neu, lernblatt-Stempel · noch 18 Seiten',
 'Rahmen Lernblatt/Gesamt: \\abhak ohne parbox',
 'Korrektur per PowerShell · von der Sandbox abgewiesen (Pfadprüfung), nichts geändert',
 'Rahmen Lernblatt: \\par innerhalb von \\small',
 'Rahmen Gesamt: \\par innerhalb von \\small',
 'Lernblatt neu, lernblatt-Stempel · 17 Seiten, Verzeichnis und Links in Ordnung',
 'Abhakseite ansehen · eine Seite',
 'Gesamt: Platzhalter, kompilieren, Verzeichnis, kompilieren, prüfen, gesamt-Stempel · 18 Seiten, Verzeichnis und Links in Ordnung',
 'Lösungen kompilieren, rendern, loesungen-Stempel · 3 Seiten, 46 Nummern mit Lösung',
 'Lösungen Seite 1 ansehen · in Ordnung',
 'Lösungen Seite 3 ansehen · in Ordnung',
 'Zählung aus der Textextraktion · siehe oben',
 'zeiten.txt lesen',
 'archiv.py schreiben',
 'archiv.py: Inhalt von chat.txt ergänzt',
 'ausgabeblock.txt schreiben (Quelle für chat.txt)',
 'archiv.py: diese Schrittliste ergänzt',
 'protokoll.txt, chat.txt schreiben und Archiv packen',
]
KORREKTUR = [33, 34, 35, 38, 39, 40, 54, 61, 66, 67, 79, 80, 84, 95, 96, 97, 98, 99, 100, 101, 102]

def zaehlung():
    zeilen = []
    for f, art in [(f'{THEMA}_KennstDuSchon.pdf', 'Zone'), (f'{THEMA}_Lernblatt.pdf', 'Lernblatt'),
                   (f'{THEMA}_Gesamt.pdf', 'Gesamt'), (f'{THEMA}_Loesungen.pdf', 'Lösungen')]:
        t = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', f, '-'], capture_output=True).stdout.decode('utf-8')
        s = [p for p in t.split('\f') if p.strip()]
        if art == 'Lösungen':
            nrs = sorted(set(int(x) for x in re.findall(r'(?m)^\s*(\d+)\)', t)))
            zeilen.append(f'{f}: {len(nrs)} Nummern mit Lösung (1–46), Grafiken 0, Seiten {len(s)}')
            continue
        aufgabenteil = t.rsplit('Das kann ich', 1)[0] if art != 'Zone' else t
        haupt = sorted(set(int(x) for x in re.findall(r'(?m)^\s*(\d+)\.\s+Ich', aufgabenteil)))
        teil = len(re.findall(r'(?<![\w(])[a-j]\)\s', t))
        graf = 0 if art == 'Zone' else 2
        zeilen.append(f'{f}: Hauptnummern {len(haupt)} ({haupt[0]}–{haupt[-1]}), Teilaufgaben {teil}, '
                      f'Grafiken {graf} (Flächenbilder Nr. 26 und 37; dazu Sachtabellen Nr. 11 und 39), Seiten {len(s)}'
                      if art != 'Zone' else
                      f'{f}: Hauptnummern {len(haupt)} ({haupt[0]}–{haupt[-1]}), Teilaufgaben {teil}, Grafiken 0, Seiten {len(s)}')
    return zeilen

def verz(name):
    out = []
    for z in lies(f'verz_{name}.tex').splitlines():
        m = re.match(r'\\verzzeile\{[^}]*\}\{(.*)\}$', z)
        if m:
            out.append('  ' + m.group(1))
    return out

def zeiten():
    st = {}
    for z in lies('zeiten.txt').split():
        pass
    paare = [l.split() for l in lies('zeiten.txt').splitlines() if l.strip()]
    for k, v in paare:
        st[k] = int(v)          # letzter Stempel je Wort gilt (nach Korrekturen)
    t0 = st['t0']
    z = [f'Zone: {st["zone"] - t0} s', f'Weiter: {st["weiter"]} (Stempel; {st["weiter"] - t0} s nach t0 – unbeaufsichtigter Lauf, keine Wartezeit)']
    for i in range(1, 6):
        z.append(f'E {i}: {st["e" + str(i)] - t0} s')
    z += [f'Lernblatt: {st["lernblatt"] - t0} s', f'Gesamt: {st["gesamt"] - t0} s', f'Lösungen: {st["loesungen"] - t0} s']
    return z

def hauptnummern():
    gruppen = []
    for z in lies('abhaken.tex').splitlines():
        m = re.match(r'\\abhakgruppe\{(.*)\}', z)
        if m:
            gruppen.append((m.group(1), []))
        m = re.match(r'\\abhak\{(\d+)\}\{(.*)\}', z)
        if m:
            gruppen[-1][1].append(f'    {m.group(1)}. {m.group(2)}')
    return gruppen

stand_t = lies('terme.md').splitlines()[1]
stand_b = lies('binomische-formeln.md').splitlines()[1]
sty2 = lies('mathblatt.sty').splitlines()[1].lstrip('% ').strip()

P = []
P.append('Prompt: Unterrichtsblatt-Prompt v4.3')
P.append('Modell: Opus 5.5 (claude-opus-5-5)')
P.append(f'Vorlage: {sty2}')
P.append(f'Katalog: terme.md, {stand_t}')
P.append(f'Katalog: binomische-formeln.md, {stand_b}')
P.append('Bestellung: mit Wiederholung · mit Ausblick (Register der Blätter führt das Thema nicht; kein Zweig liegt nach Kl. 8, Ausblick leer)')
P.append('Standpunkt: Kl. 8, Gymnasium (Klassenarbeit terme + binomische Formeln)')
P.append('')
P.append('Zweige (gebaut, alle):')
for kopf, zeile in ZWEIGE:
    P.append(f'  {kopf}')
    P.append(f'    {zeile}')
P.append('Abgewählt: keine. Ausblick: keiner. In der Zone (Wiederholung): terme.md Einheit 1 (GYM Kl. 6–7) und Einheit 2 (GYM Kl. 7).')
P.append('')
P.append('Hauptnummern mit Titel:')
for g, nrs in hauptnummern():
    P.append(f'  {g}')
    P.extend(nrs)
P.append('')
P.append('Zählung aus der Textextraktion:')
P.extend('  ' + z for z in zaehlung())
P.append('  Verzeichnis Lernblatt (wortgleich):')
P.extend(verz('lernblatt'))
P.append('  Verzeichnis Gesamt (wortgleich):')
P.extend(verz('gesamt'))
P.append('')
P.append('Werkzeugaufrufe (Schritt · Anlass):')
for i, s in enumerate(SCHRITTE, 1):
    P.append(f'  {i:3d} · {s}')
P.append('')
P.append('Vorlage: fehlende Bausteine · \\zweigkopf (Zweigzeile als zweite Zeile unter \\einheitenkopf*, mit Sprungziel), '
         '\\flaechenbild (Rechteck in vier Teilflächen, Nr. 26 und 37), \\abhak und \\abhakgruppe (Abhakseite), '
         '\\verzzeile (Verzeichniszeile mit Link) – alle im Vorspann der Rahmendateien. '
         'Befund gleichungsraster: die letzte Schreiblinie einer Zeile liegt auf dem Text der nächsten Zeile; '
         '\\\\[3mm] wirkt nicht, je Zeile \\\\ \\noalign{\\vspace{5mm}} gesetzt.')
P.append('Warnungen aus dem Log: keine (keine Package mathblatt Warning, keine Overfull-Box, keine Fehler)')
P.append(f'Korrekturrunden: {len(KORREKTUR)} von {len(SCHRITTE)} Schritten')
P.append('Zeiten (letzter Stempel je Wort):')
P.extend('  ' + z for z in zeiten())

io.open('protokoll.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(P) + '\n')

CHAT = '''Eingabe des Lehrers:
klassenarbeit terme binomische formeln 8 gymnasium – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch

Deutungszeile:
Lernblatt · Klassenarbeit aus zwei Einträgen: terme.md (Einheit 3–4) und binomische-formeln.md (Einheit 1–3) · mit Wiederholung, Ausblick leer (kein Zweig nach Kl. 8) · 5 Zweige · Zone aus 6 Fertigkeiten, darin terme.md Einheit 1–2

Plan:
Einheit 1 · Klammern auflösen: Hier lernst du, Klammern mit Plus, Minus oder einer Zahl davor aufzulösen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Terme zusammenfassen, Malnehmen mit Vorzeichen
Einheit 2 · Ausklammern: Hier lernst du, einen gemeinsamen Faktor vor die Klammer zu ziehen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Zahl mal Klammer (Einheit 1)
Einheit 3 · Summe mal Summe: Hier lernst du, Terme mit zwei Variablen zusammenzufassen und zwei Klammern miteinander malzunehmen · neu oder schon bekannt – je nach Buch · keine P10-Aufgabe · baut auf: Klammern auflösen (Einheit 1), Terme zusammenfassen, Terme malnehmen
Einheit 4 · Binomische Formeln: Hier lernst du, Quadrate von Klammern mit den drei binomischen Formeln auszumultiplizieren · neu in diesem Jahr · P10 · baut auf: Summe mal Summe (Einheit 3), Minusklammer (Einheit 1), Quadratzahlen
Einheit 5 · Faktorisieren: Hier lernst du, eine Summe mit einer binomischen Formel in ein Produkt zu verwandeln · neu in diesem Jahr (an der Oberschule je nach Buch bis Klasse 10) · keine P10-Aufgabe · baut auf: binomische Formeln (Einheit 4), Ausklammern (Einheit 2)

Planfrage: entfällt (Klassenarbeit, 1.3). Antwort aus der Eingabe: „alle“ – deckt sich mit dem Plan.
Rückfragen: keine.

Nach der Zone: TermeBinomischeFormeln_KennstDuSchon.pdf
Weiter baut Einheit 1 bis 5, Gesamt und Lösungen.
Antwort aus der Eingabe: weiter (ohne Halt durchgebaut)

Übergebene Dateien:
TermeBinomischeFormeln_KennstDuSchon.pdf
TermeBinomischeFormeln_Lernblatt.pdf
TermeBinomischeFormeln_Gesamt.pdf
TermeBinomischeFormeln_Loesungen.pdf
TermeBinomischeFormeln_2026-09-25_protokoll.zip

Ausgabeblock:
''' + lies('ausgabeblock.txt')
io.open('chat.txt', 'w', encoding='utf-8', newline='\n').write(CHAT)

name = f'{THEMA}_{DATUM}_protokoll.zip'
dateien = sorted(set(glob.glob('*.pdf') + glob.glob('*.tex') + glob.glob('*.log') + glob.glob('pruef*.py')
                     + glob.glob('pruef_out_*.txt') + ['verz.py', 'archiv.py', 'mathblatt.sty', 'Anleitung_mathblatt.md',
                     'terme.md', 'binomische-formeln.md', 'zeiten.txt', 'protokoll.txt', 'chat.txt']))
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for d in dateien:
        zf.write(d)
print(name, len(dateien), 'Dateien')
print('\n'.join(P[-12:]))
