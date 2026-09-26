# mk_protokoll.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv
import re, glob, os, zipfile
from pypdf import PdfReader

def txt(pdf):
    os.system(f'pdftotext -layout -enc UTF-8 "{pdf}" _tmp.txt')
    return open('_tmp.txt', encoding='utf-8').read()

def grafiken(quellen):
    n = 0
    for q in quellen:
        s = open(q, encoding='utf-8').read()
        n += len(re.findall(r'\\begin\{ksys\}', s)) + len(re.findall(r'\\ableitungspaar', s))
    return n

EINH = ['e1_a.tex', 'e2_a.tex', 'e3_a.tex', 'e4_a.tex', 'e5_a.tex']
DATEIEN = [('Kurvenuntersuchung_KennstDuSchon.pdf', ['zone_a.tex']),
           ('Kurvenuntersuchung_Lernblatt.pdf', EINH),
           ('Kurvenuntersuchung_Gesamt.pdf', ['zone_a.tex'] + EINH),
           ('Kurvenuntersuchung_Loesungen.pdf', ['zone_l.tex'] + [e.replace('_a', '_l') for e in EINH])]

zaehl = []
for pdf, q in DATEIEN:
    t = txt(pdf); seiten = len(PdfReader(pdf).pages)
    if 'Loesungen' in pdf:
        nr = sorted(set(int(m) for m in re.findall(r'(?m)^\s*(\d+)\) ', t)))
        zaehl.append(f'{pdf}: Nummern mit Lösung {len(nr)} ({nr[0]}–{nr[-1]}), Lösungsgrafiken {grafiken(q)}, Seiten {seiten}')
    else:
        hn = re.findall(r'(?m)^\s*(\d+)\. Ich', t)
        body = t.split('Das kann ich\n')[0] if 'abhak' in ''.join(q) else t
        ta = len(re.findall(r'(?:^|\s)([a-l])\) ', t.rsplit('Das kann ich', 1)[0]))
        zaehl.append(f'{pdf}: Hauptnummern {len(hn)} ({hn[0]}–{hn[-1]}), Teilaufgaben {ta}, Grafiken {grafiken(q)}, Seiten {seiten}')
    if pdf.endswith(('Lernblatt.pdf', 'Gesamt.pdf')):
        v = re.search(r'\\verzeichniszeile\{(.*)\}\s*$', open(pdf.replace('.pdf', '.tex'), encoding='utf-8').read(), re.M).group(1)
        v = re.sub(r'\\verz\{[^}]*\}\{([^}]*)\}', r'\1', v).replace(' \\verztrenn ', ' • ')
        zaehl.append(f'  Verzeichniszeile: {v}')

# Hauptnummern mit Titel aus der Abhakseite (wortgleich aus den Quelltexten erzeugt)
hn_zeilen = []
for z in open('abhaken.tex', encoding='utf-8').read().splitlines():
    m = re.match(r'\\abhakgruppe\{(?:\\normalfont\\itshape )?(.*)\}$', z)
    if m: hn_zeilen.append(('  ' if 'itshape' in z else '') + m.group(1) + ':'); continue
    m = re.match(r'\\abhak\{(\d+)\}\{(.*)\}$', z)
    if m: hn_zeilen.append(f'    {m.group(1)}. {m.group(2)}')

zeiten = {}
for z in open('zeiten.txt', encoding='ascii').read().split('\n'):
    if z.strip():
        k, v = z.rsplit(' ', 1); zeiten[k] = int(v)
t0 = zeiten['t0']
def d(k): return f'{zeiten[k] - t0} s' if k in zeiten else 'fehlt'

ZWEIGE = """Zweige (alle gebaut, keiner abgewählt, kein Ausblick-Zweig):
  Zone Kennst du schon (Nr. 1–8): 6 Fertigkeiten des Abschnitts Voraussetzungen, dazu Fehler finden (Nr. 3) und die gleichartige Rechenaufgabe (Nr. 4)
  Einheit 1 von 5 · Monotonie und erste Ableitung – Hier lernst du, am Vorzeichen der Ableitung abzulesen und am Term nachzuweisen, wo ein Graph steigt oder fällt · kennst du seit Q1 · Abitur GK · baut auf: Gleichungen lösen, Ableitungen bilden (Nr. 2–5)
  Einheit 2 von 5 · Extrempunkte – Hier lernst du, Hoch-, Tief- und Sattelpunkte zu berechnen und an einer gegebenen Stelle nachzuweisen, auch den größten Wert am Rand · kennst du seit Q1 · Abitur GK · baut auf: Monotonie (Einheit 1), Gleichungen lösen, Ableitungen bilden, Funktionswerte (Nr. 2–6)
  Einheit 3 von 5 · Krümmung und Wendepunkte – Hier lernst du, mit der zweiten Ableitung Krümmung und Wendepunkte zu bestimmen und an einer gegebenen Stelle nachzuweisen · kennst du seit Q1 · Abitur GK · baut auf: Extrempunkte (Einheit 2), Gleichungen lösen, Ableitungen bilden (Nr. 2–5)
  Einheit 4 von 5 · Graph und Ableitungsgraph – Hier lernst du, vom Graphen von f auf den Graphen von f' zu schließen und umgekehrt und Graphen aus Eigenschaften zu skizzieren · kennst du seit Q1 oder Q2 – je nach Buch · Abitur GK · baut auf: Einheit 1 bis 3, Ableitung als Steigung (Nr. 8)
  Einheit 5 von 5 · Kurvenuntersuchung im Sachzusammenhang – Hier lernst du, Sachfragen in Hoch-, Tief- und Wendepunkte zu übersetzen und die Ergebnisse mit Einheit zu deuten · kennst du seit Q1 · Abitur GK · baut auf: Einheit 1 bis 4, Ableitung als Änderungsrate (Nr. 8)"""

SCHRITTE = """1 · Read unterrichtsblatt.md Z. 1–754 · Anleitung lesen
2 · Read unterrichtsblatt.md Z. 755–1448 · Anleitung zu Ende lesen
3 · PowerShell · Arbeitsverzeichnis anlegen, Stempel t0 (allein)
4 · PowerShell · Themenregister und Register der Blätter per curl geholt
5 · Grep katalog_index.md · Sek-II-Zeilen suchen (Ausgabe über 30 KB)
6 · Read katalog_index.md Z. 36–85 · Sek-II-Tabelle lesen, Datei kurvenuntersuchung.md gewählt
7 · PowerShell · Register der Blätter ausgeben: Thema nicht geführt → mit Ausblick
8 · PowerShell · Eintrag kurvenuntersuchung.md per curl geholt
9 · Read Eintrag Z. 1–81 · Eintrag lesen
10 · Read Eintrag Z. 82–121 · Eintrag lesen
11 · Read Eintrag Z. 122–165 · Eintrag zu Ende lesen
12 · PowerShell · mathblatt.sty und Anleitung_mathblatt.md per curl geholt
13 · Read Anleitung Z. 1–275 · Bausteine lesen
14 · Read Anleitung Z. 276–391 · Bausteine zu Ende lesen
15 · mark_chapter · Kapitelmarke der Sitzung
16 · Write zone_a.tex · Zone geschrieben
17 · PowerShell · Korrektur zone_a: Tangente hieß t, t ist in f) die Zeit → s; Punkt C fehlte im Bild
18 · Write zone_l.tex · Lösungen Zone
19 · Write pruef.py · Prüfskript für alle Einheiten (Teil zone)
20 · Write Kurvenuntersuchung_KennstDuSchon.tex · Rahmendatei Zone
21 · PowerShell · pruef.py zone (0 Abweichungen), xelatex Zone und Prüfrahmen Lösungen, Log, Rendern
22 · Read zone-1.png · Seite mit Ablesegrafik Nr. 1
23 · Read zone-3.png · Seite mit Zeichenflächen Nr. 7
24 · Read zone-4.png · Seite mit Ablesegrafik Nr. 8
25 · Read zone-2.png · Seite 2 (Gleichungsraster, Punktprobe)
26 · Read zonel-1.png · Lösungsgrafik Nr. 7
27 · PowerShell · Korrektur, vom Werkzeug abgelehnt (Remove-Item auf PNG-Muster als Systempfad gewertet), nichts geändert
28 · PowerShell · Korrektur Zone: Kopfzeile „Kennst du schon · Kennst du schon“ (Kurzform leer gesetzt), Nr. 7 drei Zeichenflächen zu hoch (ymax 5 → 4), Nr. 8 Labels q und s überlagert (Tangente von C nach A verlegt, Lösung d) −2)
29 · PowerShell · Test Kopfzeile mit leerem Blatt-Argument: „Kurvenuntersuchung · · Kennst du schon“ – verworfen, Kurzform „Kennst du schon“ zurück
30 · PowerShell · Zone final kompiliert, Stempel zone
31 · Read zonec-4.png · geänderte Seite Nr. 8
32 · Write e1_a.tex · Einheit 1
33 · Write e1_l.tex · Lösungen Einheit 1
34 · Edit pruef.py · Teil e1
35 · PowerShell · Stempel weiter, pruef.py e1: 2 Abweichungen (Skriptfehler: Randnullstelle t = 0 als Grenze gezählt; Vorzeichenfolgen sortiert verglichen), xelatex, Textextraktion
36 · PowerShell · Korrektur: gerade Anführungszeichen als „…“ gesetzt (babel-Kurzbefehl schluckte das Leerzeichen: „monoton.”Hat“), Minus nach | als {-} („T (3 | − 1)“), pruef.py geordneter Vergleich; 0 Abweichungen; Stempel e 1
37 · Write e2_a.tex · Einheit 2
38 · Write e2_l.tex · Lösungen Einheit 2
39 · PowerShell · Lösung 21a: Beispiel f(x) = x³ (Kastenfunktion) durch x³ + 1 ersetzt
40 · Edit pruef.py · Teil e2
41 · Edit pruef.py · 19e prüfte einen Tiefpunkt mit, der nicht auf dem Blatt steht – auf die gefragte Stelle beschränkt
42 · PowerShell · pruef.py e2 (0 Abweichungen), xelatex, Log, Textextraktion
43 · PowerShell · Seite 1 rendern (Vorstufen), Stempel e 2
44 · Read e2v-1.png · Vorstufen Nr. 15/16
45 · Write e3_a.tex · Einheit 3
46 · Write e3_l.tex · Lösungen Einheit 3
47 · Edit pruef.py · Teil e3
48 · PowerShell · pruef.py 27a zählte Nullstellen statt Vorzeichenwechsel (Skriptfehler); Zone Nr. 8f W(t) → V(t), weil W der Wendepunkt ist; pruef.py e3 (0 Abweichungen), xelatex, Log
49 · Write e4_a.tex · Einheit 4
50 · Write e4_l.tex · Lösungen Einheit 4
51 · Edit pruef.py · Teil e4
52 · PowerShell · Stempel e 3 (verspätet, siehe Zeiten), pruef.py e4 (0 Abweichungen), xelatex, Log, alle Seiten rendern
53 · Read e4v-1.png · Ablesegrafiken Nr. 29/30
54 · Read e4v-2.png · Zeichenflächen Nr. 31
55 · Read e4v-3.png · Zeichenflächen Nr. 32, Ablesegrafik Nr. 33
56 · Read e4v-4.png · Ablesegrafik Nr. 36
57 · Read e4v-5.png · Lösungsgrafiken Nr. 31/32
58 · PowerShell · Korrektur Nr. 31: zweite Wertetabelle mit \\qquad eingerückt und versetzt → untereinander; karo=0.8 am \\ableitungspaar gesetzt
59 · Read e4w-2.png · geänderte Seite Nr. 31
60 · Write e5_a.tex · Einheit 5
61 · Write e5_l.tex · Lösungen Einheit 5
62 · Edit pruef.py · Teil e5
63 · PowerShell · Stempel e 4 (verspätet), pruef.py e5 bricht ab: „AttributeError: 'BooleanTrue' object has no attribute 'evalf'“ (Skriptfehler 44c), xelatex, Log
64 · PowerShell · pruef.py 44c korrigiert, e5: 0 Abweichungen
65 · Read e5v-1.png · Ablesegrafik Nr. 38
66 · PowerShell · Korrektur Nr. 37e: Antwortfeld „Nummer“ brach in eigene Zeile um → Aufgabentext gekürzt; xelatex; Stempel e 5
67 · Write gen_abhak.py · Abhakseiten wortgleich aus den Quelltexten
68 · PowerShell · gen_abhak.py: Nummernbereiche 1–8 · 9–14 · 15–22 · 23–28 · 29–36 · 37–44
69 · PowerShell · Rahmendateien Lernblatt, Gesamt, Lösungen geschrieben
70 · PowerShell · Zone neu kompiliert (Änderung V(t)), Lernblatt zweimal xelatex, Kopfzeilen, Nummernfolge; Stempel lernblatt
71 · PowerShell · Gesamt zweimal xelatex, Kopfzeilen je Seite, Nummernfolge 1–44; Stempel gesamt
72 · PowerShell · Abhakseiten des Gesamt rendern
73 · Read gesabh-18.png · Abhakseite
74 · Read ges-01.png · Seite 1 Gesamt mit Verzeichniszeile
75 · PowerShell · Lösungen zweimal xelatex, Nummern 1–44, Kopfzeilen, Sprungziele der Verzeichniszeilen mit pypdf geprüft; Stempel loesungen
76 · Write mk_protokoll.py · Protokoll, chat.txt und Archiv
77 · Edit mk_protokoll.py · chat.txt direkt im Skript statt aus einer Vorlagendatei
78 · Edit mk_protokoll.py · Ausgabeblock direkt im Skript; Schrittliste nachgeführt
79 · PowerShell · mk_protokoll.py: Teilaufgaben im Lernblatt und Gesamt als 0 gezählt – der Schnitt „Das kann ich“ traf schon die Verzeichniszeile
80 · PowerShell · Zählung korrigiert (Schnitt an der letzten Stelle), protokoll.txt, chat.txt und Archiv neu"""

AUSGABE = """Abweichung: kein Zweig abgewählt, kein Ausblick-Zweig (alle Marken Q1 bzw. Q1/2); LK-Stoff weggelassen – Sprossen „genau einen Tiefpunkt über die streng monotone Ableitung“, „Extremstelle einer Logarithmusfunktion“, „zweiten Wendepunkt über die Punktsymmetrie“, „Wendepunkt über den Vorzeichenwechsel von f'' aus der Kettenregel“ und die Typen an Sinus-, Logarithmus- und Scharfunktionen, deshalb Prüfungshöhe Nr. 19 aus IQB 2026 grundlegend statt der LK-Zielmarke; kein Rechenplatz (Sek II); geteilte Hauptnummer Nr. 17/18; Einheit 1 bis 3 mit je zwei, Einheit 5 mit vier Verfahrensüberschriften; Zwischensprosse Nr. 40 b (stärkste Abnahme an einer e-Funktion); keine Bausteine im Vorspann, keine vereinfachten Grafiken; Zeitstempel „weiter“, „e 3“ und „e 4“ verspätet gesetzt (protokoll.txt).
Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen (6 Fertigkeiten → Zone Nr. 1–8, 3 Erkennungsschritte → Vorstufen Nr. 15, 16, 37), Sprossen, Typische Fehler, Prüfungsform und Zielmarke; nicht gebraucht Merkkasten, Grundvorstellung, Verortung; Befunde: die Ketten von Einheit 1 und 4 beginnen mit einer „Vorstufe“, die Erkennungsschritte nennen aber keine vor Einheit 1 und 4 (nicht gebaut, die Grundvorstellung trägt Zone Nr. 8); 26 von 76 Haupttypen (Einzeltypen, 8 davon erhöht oder LK) haben keine eigene Sprosse – „jeder Typ eine Sprosse“ ist bei 76 Typen nicht einlösbar, die Ketten tragen die häufigen; die eine Kette von Einheit 5 läuft über vier Formen; die Stand-Zeile trägt Nachzüge vom 28. und 29.09.2026, nach dem Bautag; Spanne nur in Einheit 4 („BE Q1/2“ → „kennst du seit Q1 oder Q2 – je nach Buch“); Prüfungswort aus „GK · Abitur GK · Abitur LK“ als „Abitur GK“.
Vorlage: Kopfzeile der Zonen-Datei doppelt („Kurvenuntersuchung · Kennst du schon · Kennst du schon“), eine leere Kurzform lässt ein „·“ am Ende stehen.
Protokoll-Archiv: Kurvenuntersuchung_2026-09-26_protokoll.zip
"""

sty2 = open('mathblatt.sty', encoding='utf-8').read().split('\n')[1].strip()
stand = open('kurvenuntersuchung.md', encoding='utf-8').read().split('\n')[1].strip()

P = []
P.append('Prompt: Unterrichtsblatt-Prompt v4.4')
P.append('Modell: Claude Opus 5.5')
P.append('Vorlage: ' + sty2)
P.append('Katalog: kurvenuntersuchung.md, ' + stand)
P.append('Bestellung: mit Wiederholung · mit Ausblick (Register der Blätter führt das Thema nicht; kein Ausblick-Zweig, alle Marken Q1 bzw. Q1/2)')
P.append('Standpunkt: Kl. 12 Berlin (Q3/Q4), Gymnasium, Abitur-Gang, Grundkurs')
P.append('')
P.append(ZWEIGE)
P.append('')
P.append('Hauptnummern mit Titel:')
P += hn_zeilen
P.append('')
P.append('Zählung je Datei (Textextraktion der Kompilate; Grafiken = Koordinatensysteme aus den Quelltexten):')
P += zaehl
P.append('')
P.append('Schritte (Schritt · Anlass):')
P.append(SCHRITTE)
P.append('')
P.append('Vorlage: fehlende Bausteine · Warnungen aus dem Log: keine · keine (keine Package-mathblatt-Warnung, keine Overfull-Box in Zone, Einheiten, Lernblatt, Gesamt, Lösungen). Befund: Kopfzeile der Zonen-Datei lautet „Kurvenuntersuchung · Kennst du schon · Kennst du schon“ – eine leere Kurzform ergibt „Kurvenuntersuchung · Kennst du schon ·“, ein leeres Blatt-Argument „Kurvenuntersuchung · · Kennst du schon“.')
P.append('Korrekturrunden: 12 von 80 Schritten (17, 27, 28, 29, 36, 39, 41, 48, 58, 64, 66, 80)')
P.append(f'Zone: {d("zone")}')
P.append(f'Weiter: {d("weiter")} (kein Klick – unbeaufsichtigter Testlauf; gesetzt im ersten Aufruf der Einheitenphase, nach dem Schreiben von e1_a/e1_l)')
for i in range(1, 6): P.append(f'E {i}: {d("e " + str(i))}')
P.append(f'Lernblatt: {d("lernblatt")}')
P.append(f'Gesamt: {d("gesamt")}')
P.append(f'Lösungen: {d("loesungen")}')
P.append('Zeitenhinweis: „e 3“ und „e 4“ stehen nicht im Aufruf, der die Einheit fertig geprüft hat (48 bzw. 58/59), sondern am Anfang des jeweils nächsten Prüfaufrufs (52 bzw. 63); sie enthalten damit das Schreiben der Folgeeinheit. Nichts nachgetragen oder rekonstruiert.')
open('protokoll.txt', 'w', encoding='utf-8').write('\n'.join(P) + '\n')

C = """Eingabe des Lehrers:
kurvenuntersuchung 12 berlin – Antworten auf Planfrage und Zone: gymnasium, gk; baue ohne Halt bis zum Ausgabeblock durch

→ Lernblatt · Q3/Q4 in Berlin, Zeitmarken ab Q1 · mit Wiederholung · mit Ausblick: kein Zweig nach Kl. 12 · 5 Zweige · Zone aus 6 Fertigkeiten
Einheit 1 · Monotonie und erste Ableitung: Hier lernst du, am Vorzeichen der Ableitung abzulesen und am Term nachzuweisen, wo ein Graph steigt oder fällt · kennst du seit Q1 · Abitur GK · baut auf: Gleichungen lösen, Ableitungen bilden
Einheit 2 · Extrempunkte: Hier lernst du, Hoch-, Tief- und Sattelpunkte zu berechnen und an einer gegebenen Stelle nachzuweisen, auch den größten Wert am Rand · kennst du seit Q1 · Abitur GK · baut auf: Monotonie (Einheit 1), Gleichungen lösen, Ableitungen bilden, Funktionswerte
Einheit 3 · Krümmung und Wendepunkte: Hier lernst du, mit der zweiten Ableitung Krümmung und Wendepunkte zu bestimmen und an einer gegebenen Stelle nachzuweisen · kennst du seit Q1 · Abitur GK · baut auf: Extrempunkte (Einheit 2), Gleichungen lösen, Ableitungen bilden
Einheit 4 · Graph und Ableitungsgraph: Hier lernst du, vom Graphen von f auf den Graphen von f' zu schließen und umgekehrt und Graphen aus Eigenschaften zu skizzieren · kennst du seit Q1 oder Q2 – je nach Buch · Abitur GK · baut auf: Einheit 1 bis 3, Ableitung als Steigung
Einheit 5 · Kurvenuntersuchung im Sachzusammenhang: Hier lernst du, Sachfragen in Hoch-, Tief- und Wendepunkte zu übersetzen und die Ergebnisse mit Einheit zu deuten · kennst du seit Q1 · Abitur GK · baut auf: Einheit 1 bis 4, Ableitung als Änderungsrate
Alle Zweige, oder welche? (alle · Nummern · ein Typ für den Fokus)
Schüler ist am: Gymnasium · OSZ (Abitur) · FOS

Antwort des Lehrers (aus der Eingabe): gymnasium, gk; baue ohne Halt bis zum Ausgabeblock durch

→ Lernblatt · Gymnasium, Abitur-Gang GK · alle 5 Zweige (Umfang nicht genannt: Rückfall) · LK-Sprossen weggelassen
Kurvenuntersuchung_KennstDuSchon.pdf
Weiter baut Einheit 1 bis 5, Gesamt und Lösungen.

Weitere Rückfragen: keine

Kurvenuntersuchung_Lernblatt.pdf
Kurvenuntersuchung_Gesamt.pdf
Kurvenuntersuchung_Loesungen.pdf
Kurvenuntersuchung_2026-09-26_protokoll.zip

""" + AUSGABE
open('chat.txt', 'w', encoding='utf-8').write(C)

name = 'Kurvenuntersuchung_2026-09-26_protokoll.zip'
muster = ['*.pdf', '*.tex', '*.log', 'pruef.py', 'pruef_out_*.txt', 'mathblatt.sty', 'Anleitung_mathblatt.md',
          'kurvenuntersuchung.md', 'zeiten.txt', 'protokoll.txt', 'chat.txt', 'gen_abhak.py', 'mk_protokoll.py']
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as z:
    for m in muster:
        for f in sorted(glob.glob(m)):
            z.write(f)
print(open('protokoll.txt', encoding='utf-8').read()[-1400:])
print(name, len(zipfile.ZipFile(name).namelist()), 'Dateien')
