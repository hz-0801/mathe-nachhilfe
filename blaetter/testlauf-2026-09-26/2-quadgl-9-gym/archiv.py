# -*- coding: utf-8 -*-
# Schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3, Punkt 4).
import io, re, glob, zipfile, os

zeiten = [l.split() for l in io.open('zeiten.txt', encoding='ascii').read().splitlines() if l.strip()]
st = {' '.join(z[:-1]): int(z[-1]) for z in zeiten}
t0 = st['t0']
sty2 = io.open('mathblatt.sty', encoding='utf-8').read().splitlines()[1].lstrip('% ').strip()
stand = io.open('quadratische-gleichungen.md', encoding='utf-8').read().splitlines()[1].strip()

ZWEIGE = []
for d in ['e1_a.tex', 'e2_a.tex', 'e3_a.tex', 'e4_a.tex']:
    t = io.open(d, encoding='utf-8').read()
    kopf = re.search(r'\\einheitenkopf\[[^\]]*\]\{([^}]*)\}', t).group(1)
    zeile = re.search(r'\\zweigzeile\{(.*)\}', t).group(1)
    ZWEIGE.append((kopf, zeile.replace('$', '').replace('x^2', 'x²')))

abh = io.open('abhaken.tex', encoding='utf-8').read()
hn = []
for m in re.finditer(r'\\abhakgruppe\{(.*)\}|\\abhak\{(\d+)\}\{(.*)\}', abh):
    if m.group(1):
        hn.append('  ' + m.group(1).replace('$', '').replace('x^2', 'x²'))
    else:
        hn.append('    %s. %s' % (m.group(2), m.group(3).replace('$', '').replace('x^2', 'x²')))

VZ_L = '1 Wurzelziehen und Lösbarkeit (Nr. 12–23) • 2 Satz vom Nullprodukt (Nr. 24–31) • 3 Normalform und p-q-Formel (Nr. 32–44) • 4 Sachaufgaben (Nr. 45–49) • Das kann ich'
VZ_G = 'Kennst du schon (Nr. 1–11) • ' + VZ_L

SCHRITTE = """1 · Prompt unterrichtsblatt.md lesen, Teil 1 (Zeilen 1–754)
2 · Prompt lesen, Teil 2 (Zeilen 755–1448)
3 · Stempel t0 (allein)
4 · curl Themenregister und Register der Blätter (1.2)
5 · Suche im Register nach „quadratisch“
6 · Register der Blätter lesen: Thema geführt (nullstellen, 22.09., quadratische-gleichungen.md) → ohne Ausblick
7 · Suche nach quadratische-gleichungen.md im Register
8 · Registerzeilen 30–32 ausgeben (Datei wählen)
9 · curl Eintrag quadratische-gleichungen.md in Datei
10 · Eintrag lesen, Zeilen 1–110
11 · curl mathblatt.sty und Anleitung_mathblatt.md (4.5)
12 · Eintrag lesen, Zeilen 111–150 (Prüfungsform, Zielmarke; Offene Punkte und Prüfliste mitgelesen, nicht verwendet)
13 · Anleitung lesen, Zeilen 1–275
14 · Anleitung lesen, Zeilen 276–391
15 · pruef.py schreiben (alle Teile, Sperrliste)
16 · pruef.py korrigieren: frei erfundener Sperreintrag „3+x^2“ entfernt (Skriptfehler)
17 · pruef.py korrigieren: Sonderfall dazu entfernt
18 · zone_a.tex schreiben
19 · zone_l.tex schreiben
20 · Rahmendatei QuadratischeGlg_KennstDuSchon.tex schreiben
21 · Prüfrahmen probe_l.tex schreiben (Lösungsdateien einzeln kompilieren)
22 · Zone: pruef.py zone (0 Abweichungen), kompilieren, Log, rendern
23 · Zone Seite 1 ansehen (erste Seite, erster Einsatz der Vorlage)
24 · Zone Seite 2 ansehen
25 · Zone Seite 3 ansehen: Titel Nr. 10 „Ich kann x ausklammern.“ – x nicht als Mathematik gesetzt
26 · Korrektur zone_a.tex: Titel Nr. 10 mit $x$
27 · Zone neu kompilieren (2 Läufe), Log leer, Stempel zone
28 · e1_a.tex schreiben
29 · e1_l.tex schreiben
30 · Prüfrahmen probe_a.tex schreiben
31 · E1: pruef.py e1 (0 Abweichungen), kompilieren, Log, Seitenfüllung, rendern
32 · E1 Seite 2 ansehen (Nr. 15 allein, Restfläche; Nr. 16 passt nicht dazu)
33 · E1 Seite 4 ansehen (Ablesegrafik Nr. 18)
34 · Ausschnitt der Grafik Nr. 18 vergrößert rendern
35 · Ausschnitt ansehen: Label „y = 2“ sitzt am Schnittpunkt (3|2) der Parabel
36 · Korrektur e1_a.tex: \\gerade[4.4] statt [4] für y = 2
37 · E1 neu kompilieren, Log leer, Ausschnitt rendern, Stempel e 1
38 · Ausschnitt ansehen: Label frei
39 · e2_a.tex schreiben
40 · e2_l.tex schreiben
41 · E2: pruef.py e2 (0 Abweichungen), kompilieren, Log, Seitenfüllung, rendern
42 · E2 Seite 3 ansehen (Nr. 28–31, Rechnungen der Fehleraufgaben)
43 · Stempel e 2
44 · e3_a.tex schreiben
45 · e3_l.tex schreiben
46 · E3: pruef.py e3 (0 Abweichungen), kompilieren, Log, Seitenfüllung, rendern
47 · E3 Seite 2 ansehen (Nr. 35 allein, etwa zwei Drittel gefüllt; Nr. 36 passt nicht dazu)
48 · E3 Seite 6 ansehen (Nr. 40 allein, ebenso)
49 · E3 Seite 8 ansehen (Ablesegrafik Nr. 44)
50 · Stempel e 3
51 · e4_a.tex schreiben
52 · e4_l.tex schreiben
53 · probe_a.tex mit Vorspann-Baustein \\rechteckrand
54 · E4: pruef.py e4 (0 Abweichungen), kompilieren, Log, rendern
55 · E4 Seite 2 ansehen (Skizzen Nr. 47)
56 · E4 Seite 1 ansehen: Nr. 46 d) Feld „Zahlen:“ bricht in eine eigene Zeile um
57 · Korrektur e4_a.tex: \\\\ vor „Gleichung:“ in Nr. 46 d)
58 · E4 neu kompilieren, Log leer, Textprobe, Stempel e 4
59 · abhaken_bau.py schreiben (Abhakseite wortgleich aus den Quelltexten)
60 · Rahmendatei QuadratischeGlg_Lernblatt.tex schreiben
61 · Rahmendatei QuadratischeGlg_Gesamt.tex schreiben
62 · Rahmendatei QuadratischeGlg_Loesungen.tex schreiben
63 · kompilat_pruef.py schreiben (Nummern, Kopfzeilen, Linkziele, Abhakseite)
64 · Lernblatt: abhaken.tex erzeugen, 2 Läufe, Log, Kompilatprüfung, Stempel lernblatt
65 · Abhakseite als Text ausgeben: Prüfskript hatte die Zeilenform „□ 1. Ich …“ nicht erkannt (Skriptfehler, Seite vollständig)
66 · kompilat_pruef.py korrigieren (Muster der Abhakzeile)
67 · Lernblatt-Abhakseite nachgeprüft (1–49, 0 Befunde); Gesamt: 2 Läufe, Log, Kompilatprüfung (0 Befunde), Stempel gesamt
68 · Lösungen: 2 Läufe, Log, 49 Nummern mit Lösung, Stempel loesungen
69 · Zählung der Zone, Zeiten und Vorlagenversion ausgeben
70 · archiv.py schreiben
71–74 · archiv.py ergänzen (vier Edit-Aufrufe): Chattext und Ausgabeblock ins Skript statt in eine Hilfsdatei (chat.txt muss im Zip-Aufruf entstehen), Schrittliste, Schrittzahl
75 · archiv.py: protokoll.txt, chat.txt, Archiv"""

p = []
p.append('Prompt: Unterrichtsblatt-Prompt v4.4')
p.append('Modell: Claude Opus 5.5 (claude-opus-5-5)')
p.append('Vorlage: ' + sty2)
p.append('Katalog: quadratische-gleichungen.md, ' + stand)
p.append('Bestellung: mit Wiederholung (ohne Ausblick: Register der Blätter führt das Thema; kein Zweig nach Kl. 9)')
p.append('Standpunkt: Kl. 9, Gymnasium')
p.append('')
p.append('Zweige (gebaut 4 von 4, abgewählt keiner, Ausblick keiner):')
for k, z in ZWEIGE:
    p.append('  ' + k)
    p.append('    ' + z)
p.append('Hauptnummern mit Titel:')
p += hn
p.append('')
p.append('Zählung aus der Textextraktion der Kompilate (Teilaufgaben: Zeilen mit Buchstabe, heuristisch):')
p.append('  QuadratischeGlg_KennstDuSchon.pdf: 11 Hauptnummern, 51 Teilaufgaben, 0 Grafiken, 3 Seiten')
p.append('  QuadratischeGlg_Lernblatt.pdf: 38 Hauptnummern, 162 Teilaufgaben, 4 Grafiken (Nr. 18 und 44 Ablesegrafik, Nr. 47 Rechteck und Rechteck mit Rand), 21 Seiten')
p.append('    Verzeichniszeile: ' + VZ_L)
p.append('  QuadratischeGlg_Gesamt.pdf: 49 Hauptnummern, 213 Teilaufgaben, 4 Grafiken, 23 Seiten')
p.append('    Verzeichniszeile: ' + VZ_G)
p.append('  QuadratischeGlg_Loesungen.pdf: 49 Nummern mit Lösung, 0 Grafiken, 3 Seiten')
p.append('')
p.append('Schritte (Schritt · Anlass):')
p += ['  ' + s for s in SCHRITTE.splitlines()]
p.append('')
p.append('Vorlage: fehlende Bausteine · Warnungen aus dem Log – fehlend: Rechteck mit Rand (\\rechteckrand, im Vorspann von Lernblatt und Gesamt definiert, Nr. 47 f); Warnungen: keine')
i = p.index('  71–74 · archiv.py ergänzen (vier Edit-Aufrufe): Chattext und Ausgabeblock ins Skript statt in eine Hilfsdatei (chat.txt muss im Zip-Aufruf entstehen), Schrittliste, Schrittzahl')
p[i] = p[i].replace('71–74', '71–75').replace('(vier', '(fünf')
p[i + 1] = p[i + 1].replace('75 ·', '76 ·')
p.append('Korrekturrunden: 3 von 76 Schritten (Schritte 26, 36, 57; dazu 3 Korrekturen an Prüfskripten, Schritte 16, 17, 66)')
p.append('Zone: %d s' % (st['zone'] - t0))
for n in '1234':
    p.append('E %s: %d s' % (n, st['e ' + n] - t0))
p.append('Weiter: kein Stempel – Testlauf ohne Gegenüber, der Bau lief ohne Halt nach der Zone weiter')
p.append('Lernblatt: %d s' % (st['lernblatt'] - t0))
p.append('Gesamt: %d s' % (st['gesamt'] - t0))
p.append('Lösungen: %d s' % (st['loesungen'] - t0))
io.open('protokoll.txt', 'w', encoding='utf-8').write('\n'.join(p) + '\n')

CHAT = """Eingabe des Lehrers:
quadratische gleichungen 9 gymnasium – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch

→ Lernblatt · mit Wiederholung, ohne Ausblick (Register führt das Thema; kein Zweig nach Kl. 9) · 4 Zweige · Zone aus 8 Fertigkeiten
Einheit 1 von 4 · Wurzelziehen und Lösbarkeit: {z1}
Einheit 2 von 4 · Satz vom Nullprodukt: {z2}
Einheit 3 von 4 · Normalform und p-q-Formel: {z3}
Einheit 4 von 4 · Sachaufgaben: {z4}
Alle Zweige, oder welche? (alle · Nummern · ein Typ für den Fokus)
Antwort: alle

QuadratischeGlg_KennstDuSchon.pdf
Weiter baut Einheit 1 bis 4, Gesamt und Lösungen.
Antwort: (Testlauf ohne Halt, Bau lief weiter)

QuadratischeGlg_Lernblatt.pdf
QuadratischeGlg_Gesamt.pdf
QuadratischeGlg_Loesungen.pdf
QuadratischeGlg_2026-09-26_protokoll.zip
{block}
"""
BLOCK = """1. Abweichungen: ohne Ausblick, weil das Register der Blätter das Thema schon führt (alle Marken liegen ohnehin bei oder vor Kl. 9) · Baustein im Vorspann von Lernblatt und Gesamt: \\rechteckrand (Beet mit Weg, Nr. 47 f) · Höhe nach Lehrwerk: Einheit 4 (kein P10-Original, Zielmarke LS-AA Kl. 9 II 6) · Nr. 15, 35, 36 und 40 sind etwa zwei Drittel Seite hoch (unter dem Maß von zwölf Teilaufgaben, daher nicht geteilt), ihre Seiten tragen Restfläche · keine geteilten Hauptnummern, keine Zwischensprossen · Papier der OS-Originale als „FOR“ angenommen · Kopfzeile der Zone zeigt „Kennst du schon“ doppelt (Blattname und Kurzform der Vorlage) · kein Weiter-Stempel (Testlauf ohne Halt)
2. Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (8 Fertigkeiten; 7 Erkennungsschritte als Nr. 12, 13, 24, 32, 33, 34, 45), Sprossen, Typische Fehler, Prüfungsform und Zielmarke; nicht gebraucht Merkkasten, Grundvorstellung, Verortung · Befunde: der Erkennungsschritt „Zwei, eine oder keine?“ braucht den Fall rechts null, x² = 0 ist aber Kastengleichung (ausgewichen auf 5x² = 0); die Prüfungshöhe von Einheit 1 (2021-OS-K7c) enthält „Gleichung ohne Lösung angeben“, das die Kette davor als eigene Sprosse führt (hier verfremdet als „rechte Seite ändern“); der Typ „Quadrat mit Rand (Vorrat)“ hat keine Sprosse in der Kette (in Nr. 47 f als Beet mit Weg gebaut); Einheit 3 führt vier Originale, das Blatt trägt je Hauptnummer eine Prüfungshöhe (2020-OS-K3e in Nr. 29, 2023-OS-K4c in Nr. 41, 2022-OS-K3c in Nr. 44; 2025-OS-K5c und 2017-OS-K5d nicht verwendet); der Eintrag nennt für die OS-Originale kein Papierkürzel · Spannen: Einheit 1 und 2 GYM Kl. 8–9 → „neu oder schon bekannt – je nach Buch“; Oberschul-Zusatz bei Einheit 1, 3, 4 „je nach Buch Kl. 9 oder 10“, bei Einheit 2 „erst Kl. 10“
4. Protokoll-Archiv: QuadratischeGlg_2026-09-26_protokoll.zip"""
io.open('ausgabeblock.txt', 'w', encoding='utf-8').write(BLOCK + '\n')
chat = CHAT.format(z1=ZWEIGE[0][1], z2=ZWEIGE[1][1], z3=ZWEIGE[2][1], z4=ZWEIGE[3][1], block=BLOCK)
io.open('chat.txt', 'w', encoding='utf-8').write(chat)

name = 'QuadratischeGlg_2026-09-26_protokoll.zip'
dateien = sorted(set(glob.glob('*.pdf') + glob.glob('*.tex') + glob.glob('*.log') + glob.glob('pruef_out_*.txt') +
                     ['pruef.py', 'kompilat_pruef.py', 'abhaken_bau.py', 'archiv.py', 'mathblatt.sty',
                      'Anleitung_mathblatt.md', 'quadratische-gleichungen.md', 'zeiten.txt', 'protokoll.txt',
                      'chat.txt']))
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as z:
    for d in dateien:
        z.write(d)
print(name, len(dateien), 'Dateien', os.path.getsize(name), 'Byte')
print(open('protokoll.txt', encoding='utf-8').read()[-900:])
