# archiv.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3, Punkt 4)
import zipfile, re, glob, os

stempel = {}
for z in open('zeiten.txt', encoding='ascii').read().split('\n'):
    if z.strip():
        k, v = z.rsplit(' ', 1); stempel[k] = int(v)
fokus_s = stempel['fokus'] - stempel['t0']

sty2 = open('mathblatt.sty', encoding='utf-8').read().split('\n')[1]
vorlage = re.search(r'Version (\S+)', sty2).group(1)
stand = open('quadratische-funktionen.md', encoding='utf-8').read().split('\n')[1]
stand = re.match(r'Status: (.*?) · Stufe', stand).group(1)

def txt(n): return open(n + '.txt', encoding='utf-8').read()
fok, loe = txt('QuadratischeFkt_Fokus_Nullstellen'), txt('QuadratischeFkt_Fokus_Nullstellen_Loesungen')
hn = len(re.findall(r'^\s*\d+\. Ich ', fok, re.M))
ta = len(re.findall(r'(?:^|\s)[a-e]\) ', fok))
fs = len(re.findall(r'^\s*\d+\)\s', loe, re.M))
seiten_f, seiten_l = fok.count('\f') + (0 if fok.endswith('\f') else 1), loe.count('\f') + (0 if loe.endswith('\f') else 1)

TITEL = """  1 Ich kann die Nullstelle einer Geraden berechnen. (Zone)
  2 Ich kann Zahlen quadrieren, auch negative Zahlen. (Zone)
  3 Ich kann eine Quadratwurzel ziehen und runden. (Zone)
  4 Ich kann eine Gleichung der Form x² = Zahl lösen. (Zone)
  5 Ich kann eine quadratische Gleichung mit der p-q-Formel lösen. (Zone)
  6 Ich erkenne, welche Gleichung die Nullstellen liefert. (Vorstufe)
  Nullstellen aus der Scheitelpunktform
  7 Ich kann die Nullstellen aus der Scheitelpunktform berechnen.
  8 Ich kann die Nullstellen aus der Scheitelpunktform berechnen – weiter.
  9 Ich kann die Nullstellen einer gestreckten Parabel berechnen.
  10 Ich kann Nullstellen aus der Scheitelpunktform berechnen, die keine ganzen Zahlen sind. (Prüfungshöhe P10 2017 OS)
  11 Ich finde den Fehler bei Nullstellen aus der Scheitelpunktform.
  12 Ich kann am Scheitel begründen, wie viele Nullstellen eine Parabel hat.
  Nullstellen mit der p-q-Formel
  13 Ich kann die Nullstellen mit der p-q-Formel berechnen.
  14 Ich kann die Nullstellen mit der p-q-Formel berechnen – weiter.
  15 Ich kann die Nullstelle berechnen, wenn die Parabel die x-Achse nur berührt.
  16 Ich kann mit der p-q-Formel zeigen, dass eine Parabel keine Nullstelle hat.
  17 Ich kann die Nullstellen berechnen, wenn vor x² eine Zahl steht. (Prüfungshöhe P10 2020 OS)
  18 Ich kann mit der p-q-Formel Nullstellen berechnen, die keine ganzen Zahlen sind. (Prüfungshöhe P10 2025 OS)
  19 Ich finde den Fehler bei Nullstellen mit der p-q-Formel."""

SCHRITTE = """  1 Read · Anleitung unterrichtsblatt.md lesen, Zeilen 1–754
  2 Read · Anleitung lesen, Zeilen 755–1448
  3 PowerShell · Arbeitsverzeichnis prüfen, Stempel t0 (allein)
  4 PowerShell · Themenregister und Register der Blätter holen (1.2); Ausgabe zu groß, in Datei ausgelagert
  5 Grep · ausgelagerte Ausgabe nach quadratische-*/Register durchsuchen
  6 PowerShell · Registerzeilen quadratische-funktionen/-gleichungen und Blätter-Register anzeigen
  7 PowerShell · Eintrag quadratische-funktionen.md holen
  8 Read · Eintrag lesen, Zeilen 1–100
  9 Read · Eintrag lesen, Zeilen 100–141 (bis Dateiende; Offene Punkte und Prüfliste dabei mitgelesen)
  10 PowerShell · mathblatt.sty und Anleitung_mathblatt.md holen (4.5)
  11 Read · Anleitung_mathblatt.md, Zeilen 1–275
  12 Read · Anleitung_mathblatt.md, Zeilen 276–391
  13 Write · zone_a.tex
  14 Write · zone_l.tex
  15 Write · e4_a.tex
  16 Edit · e4_a.tex, Anweisung 18 c umformuliert (vor dem ersten Kompilat)
  17 Write · e4_l.tex
  18 Write · pruef.py
  19 Write · Rahmendatei QuadratischeFkt_Fokus_Nullstellen.tex
  20 Write · Rahmendatei QuadratischeFkt_Fokus_Nullstellen_Loesungen.tex
  21 PowerShell · pruef.py zone und e4 (je 0 Abweichungen), xelatex beider Rahmen, Log, pdftotext, Seiten rendern; Log: „Package hyperref Warning: Rerun to get /PageLabels entry.“
  22 Read · Textextraktion Fokus: Nummern, Seitenumbruch, Seitenfüllung
  23 Read · Seite 2 (Vorstufe, Rechenplatz, Raster)
  24 Read · Seite 4: „f“ im Text der Anweisungen 10 c aufrecht statt mathematisch gesetzt
  25 Read · Seite 1 (Zone)
  26 Read · Seite 8 (Fehler finden p-q)
  27 Edit · e4_a.tex 10 c: „Funktion f“ → $f$
  28 Edit · e4_a.tex 17 d: „Funktion f“ → $f$
  29 Edit · e4_a.tex 18 c: „Funktion f“ → $f$, Anweisung gestrafft
  30 PowerShell · beide Rahmen zweimal kompiliert (hyperref-Rerun), Log sauber, pdftotext, Lösungsseite gerendert, Stempel fokus
  31 Read · Lösungsseite
  32 Write · archiv.py
  33 Write · ausgabeblock.txt
  34 Edit · archiv.py, Schrittliste ergänzt
  35 Edit · archiv.py, Zeile Korrekturrunden
  36 Edit · archiv.py, Schrittliste nachgezogen
  37 PowerShell · archiv.py: protokoll.txt, chat.txt, Archiv"""

protokoll = f"""Prompt: Unterrichtsblatt-Prompt v4.4
Modell: Claude Opus 5.5 (claude-opus-5-5)
Vorlage: {vorlage}
Katalog: quadratische-funktionen.md, Status: {stand}
Bestellung: mit Wiederholung (Fokus: kurze Zone als erste Seite)
Standpunkt: absolut (ohne Klasse, ohne Schulform; Oberschule Standpunkt, Gymnasium Zusatz)

Zweige:
  gebaut (Fokus): Einheit 4 · Nullstellen und Schnittpunkte berechnen
    Zweigzeile: Hier lernst du, die Nullstellen einer Parabel zu berechnen · ab Kl. 10 (am Gymnasium ab Kl. 9) · P10 oft · baut auf: Nr. 1–5
    Fokustyp: Nullstellen (aus der Scheitelpunktform durch Wurzelziehen und aus der Normalform mit der p-q-Formel)
  nicht auf dem Blatt (Fokus): Einheit 1 Normalparabel und Streckfaktor, Einheit 2 Scheitelpunktform, Einheit 3 Normalform; aus Einheit 4 die Typen Argument zu Funktionswert, Schnittpunkte Gerade–Parabel, Punktprobe als Schnittpunkt-Nachweis, Gerade ohne gemeinsamen Punkt, Schnittpunkte zweier Parabeln
  Ausblick: keiner (Fokus)
Hauptnummern:
{TITEL}

Zählung aus der Textextraktion:
  QuadratischeFkt_Fokus_Nullstellen.pdf: {hn} Hauptnummern, {ta} Teilaufgaben, 0 Grafiken, {seiten_f} Seiten
  QuadratischeFkt_Fokus_Nullstellen_Loesungen.pdf: Lösungen zu {fs} Nummern, 0 Grafiken, {seiten_l} Seite(n)
  Verzeichniszeile: keine (Fokus)

Schritte (Werkzeugaufrufe):
{SCHRITTE}

Vorlage: fehlende Bausteine · keine
Vorlage: Warnungen aus dem Log · keine nach dem zweiten Lauf (erster Lauf: hyperref Rerun to get /PageLabels entry)
Korrekturrunden: 1 von 37 Schritten
Fokus: {fokus_s} s
Weiter: entfällt (kein Halt, Planfrage und Zone im Testlauf aus der Eingabe beantwortet)
"""

AUSGABE = open('ausgabeblock.txt', encoding='utf-8').read().strip()
chat = f"""Eingabe des Lehrers:
nullstellen – Antworten auf Planfrage und Zone: quadratische-funktionen; baue ohne Halt bis zum Ausgabeblock durch

Erste Antwort:
→ Fokus Nullstellen · ohne Klasse, Marken absolut
Gemeint ist: quadratische-funktionen – Nullstellen einer Parabel aus Scheitelpunktform und Normalform (Einheit 4) · quadratische-gleichungen – quadratische Gleichungen lösen (Wurzelziehen, p-q-Formel, Lösbarkeit)

Antwort des Lehrers auf die Planfrage: quadratische-funktionen

Zweite Antwort:
→ Fokus Nullstellen · quadratische-funktionen, Einheit 4 · ohne Klasse, Marken absolut · Zone aus 5 Fertigkeiten
QuadratischeFkt_Fokus_Nullstellen.pdf
QuadratischeFkt_Fokus_Nullstellen_Loesungen.pdf
QuadratischeFkt_2026-09-26_protokoll.zip
{AUSGABE}
"""
open('protokoll.txt', 'w', encoding='utf-8').write(protokoll)
open('chat.txt', 'w', encoding='utf-8').write(chat)

name = 'QuadratischeFkt_2026-09-26_protokoll.zip'
dateien = sorted(set(glob.glob('*.pdf') + glob.glob('*.tex') + glob.glob('*.log') + glob.glob('pruef_out_*.txt'))) + [
    'pruef.py', 'mathblatt.sty', 'Anleitung_mathblatt.md', 'quadratische-funktionen.md',
    'zeiten.txt', 'protokoll.txt', 'chat.txt', 'archiv.py', 'ausgabeblock.txt']
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as z:
    for d in dateien:
        z.write(d)
print(protokoll)
print(name, len(dateien), 'Dateien')
