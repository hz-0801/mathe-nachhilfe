# archiv.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3).
import re, glob, os, zipfile

THEMA_DATEI = 'TermeBinomischeFormeln'
DATUM = '2026-09-26'
TEILE = ['zone', 'e1', 'e2', 'e3', 'e4', 'e5']

def zeile2(datei):
    return open(datei, encoding='utf-8').read().splitlines()[1].strip()

def lies(teil):
    src = open(f'{teil}_a.tex', encoding='utf-8').read()
    lang = re.search(r'\\einheitenkopf\[\w+\]\[[^\]]*\]\{([^}]*)\}', src).group(1)
    zz = re.search(r'\\zweigzeile\{([^}]*)\}', src)
    n = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', src).group(1))
    titel = []
    for m in re.finditer(r'\\verfahren\{([^}]*)\}|\\begin\{aufgabe\}\{((?:[^{}]|\{[^{}]*\})*)\}', src):
        if m.group(1) is not None:
            titel.append(f'   [{m.group(1)}]')
        else:
            n += 1
            titel.append(f'   {n}. {m.group(2)}')
    return lang, (zz.group(1) if zz else ''), titel

def zaehle(pdf_txt, loesung=False):
    t = open(pdf_txt, encoding='utf-8').read()
    seiten = [s for s in t.split('\f') if s.strip()]
    if loesung:
        nrs = re.findall(r'(?m)^\s*(\d+)\)', t)
        return f'{len(nrs)} Nummern mit Lösung, {len(seiten)} Seiten'
    hn = re.findall(r'(?m)^\s*(\d+)\. Ich', t)
    abh = re.findall(r'(?m)^\s*\S?\s*(\d+)\.\s+Ich', t)
    hn_n = len(hn) - (len(abh) - len(hn)) if False else len(set(hn))
    ta = re.findall(r'(?:^|\s)([a-k])\)\s', t)
    return f'{hn_n} Hauptnummern, {len(ta)} Teilaufgaben', len(seiten)

def grafiken(teile):
    n = 0
    for tl in teile:
        s = open(f'{tl}_a.tex', encoding='utf-8').read()
        n += len(re.findall(r'\\rechteck\[|\\flaechenbild\{', s))
    return n

# --- Zeiten
st = {}
for z in open('zeiten.txt', encoding='ascii').read().split('\n'):
    if z.strip():
        k, v = z.rsplit(' ', 1)
        st[k] = int(v)
t0 = st['t0']
zeiten = [f"Zone: {st['zone'] - t0} s", f"Weiter: {st['weiter'] - t0} s"]
for i in range(1, 6):
    zeiten.append(f"E {i}: {st[f'e {i}'] - t0} s")
zeiten += [f"Lernblatt: {st['lernblatt'] - t0} s", f"Gesamt: {st['gesamt'] - t0} s", f"Lösungen: {st['loesungen'] - t0} s"]

DEUTUNG = ('→ Lernblatt · Einträge terme.md und binomische-formeln.md · mit Wiederholung · '
           'mit Ausblick: kein Zweig nach Kl. 8 · 5 Zweige · Terme Einheit 1 und 2 (GYM Kl. 6–7) in der Zone · '
           'Zone aus 7 Fertigkeiten und dem Fehler-finden-Paar')

plan = []
zweige_prot = []
for tl in TEILE[1:]:
    lang, zz, titel = lies(tl)
    plan.append(f'{lang}: {zz}')
    zweige_prot.append(f'{lang}\n  Zweigzeile: {zz}\n' + '\n'.join(titel))
zlang, _, ztitel = lies('zone')

AUSGABE = [
    '1. Abweichungen: keine Planfrage (Klassenarbeit, 1.3) – das „alle“ der Eingabe ist gegenstandslos · Zone und Rest in einem Durchgang (unbeaufsichtigt, „weiter“ aus der Eingabe) · Zwischensprossen: Nr. 12 k Variable mal Klammer (gebraucht für die Probe in Einheit 2), Nr. 24 Klammer mit zwei Variablen als eigene Hauptnummer mit Grundfall · Höhe ohne Original nach der Zielmarke des Eintrags: Nr. 13 g, 17 j, 25 j, 42 j · geteilte Hauptnummer: 32/33 · Original 2022-OS-K3c (Scheitelpunktform mit Gerade gleichsetzen) nicht verwendet, es braucht quadratische Gleichungen (Kl. 9); Nr. 33 f trägt 2022-GYM-B2b, Nr. 34 d 2017-OS-K5d, Nr. 37 c 2019-GYM-B1f · im Vorspann definierter Baustein: \\flaechenbild (Rechteck mit geteilten Seiten und vier Teilflächen, Nr. 27, 38, 39) · Vorlage: Kopfzeile des Zone-PDFs trägt „Kennst du schon“ doppelt',
    '2. Katalog: gebraucht Lerneinheiten, Marken, Typen, Voraussetzungen, Erkennungsschritte, Sprossen, Typische Fehler, Prüfungsform und Zielmarke beider Einträge; nicht gebraucht Merkkasten (kein „mit kasten“), Grundvorstellung (nicht schwach), Verortung (die Nachbarthemen – Scheitelpunktform, Produktform – stehen schon als Sprossen in der Kette) · Befunde: die Erkennungsschritte „Ist das ein Quadrat? … Wurzel daneben schreiben“ und „Passt das Mittelglied? … doppeltes Produkt bilden“ (binomische-formeln.md, vor Einheit 3) verlangen ein Ergebnis – auf dem Blatt ohne Ergebnis umgesetzt (Nr. 40 ankreuzen, Nr. 41 unterstreichen), das Ausrechnen liegt in Nr. 42 · Voraussetzung „Scheitelpunktform lesen“ (Kl. 9) für Kl. 8 am Gymnasium nicht vorhanden; entfällt, weil der Nachweis 2017-OS-K5d rein algebraisch gestellt ist · Produktform gleich null und quadratische Ergänzung (RLP H) stehen in Einheit 3 ohne GYM-Typklammer, obwohl sie am Gymnasium nach Kl. 8 liegen · Spannen: terme.md Einheit 3 und 4 und binomische-formeln.md Einheit 1 (GYM Kl. 7–8) → „neu oder schon bekannt – je nach Buch“; terme.md Einheit 1 (GYM 6–7) und 2 (GYM 7) → Zone; Typklammern [GYM 8] (Minusklammer, Zahl mal Klammer, Zusammenfassen mit zwei Variablen) → „(neu in diesem Jahr)“ am Titel von Nr. 12 und 23',
    f'3. Protokoll-Archiv: {THEMA_DATEI}_{DATUM}_protokoll.zip',
]

DATEIEN = [f'{THEMA_DATEI}_KennstDuSchon.pdf', f'{THEMA_DATEI}_Lernblatt.pdf', f'{THEMA_DATEI}_Gesamt.pdf', f'{THEMA_DATEI}_Loesungen.pdf']

# --- protokoll.txt
P = []
P.append('Prompt: Unterrichtsblatt-Prompt v4.4')
P.append('Modell: Opus 5.5')
P.append('Vorlage: ' + zeile2('mathblatt.sty').lstrip('% ').split(' (')[0])
P.append('Katalog: terme.md, ' + zeile2('terme.md'))
P.append('Katalog: binomische-formeln.md, ' + zeile2('binomische-formeln.md'))
P.append('Bestellung: mit Wiederholung · mit Ausblick (kein Ausblick-Zweig: alle Marken bei oder vor Kl. 8)')
P.append('Standpunkt: Kl. 8, Gymnasium')
P.append('')
P.append('Zweige (gebaut, 5; abgewählt: keine; Ausblick: keiner; in der Zone statt als Zweig: terme.md Einheit 1 und 2):')
P.append(f'{zlang} (Zone)\n' + '\n'.join(ztitel))
P += zweige_prot
P.append('')
P.append('Zählung aus der Textextraktion der Kompilate (Grafiken aus dem Quelltext):')
for datei, txt, teile, loes in [(DATEIEN[0], 'zone.txt', ['zone'], False), (DATEIEN[1], 'lernblatt.txt', TEILE[1:], False),
                                (DATEIEN[2], 'gesamt.txt', TEILE, False), (DATEIEN[3], 'loesungen.txt', [], True)]:
    if loes:
        P.append(f'{datei}: {zaehle(txt, True)}')
    else:
        z, s = zaehle(txt)
        P.append(f'{datei}: {z}, {grafiken(teile)} Grafiken, {s} Seiten')
vz_lb = re.search(r'\\verzeichniszeile\{(.*)\}', open('lernblatt.tex', encoding='utf-8').read()).group(1)
vz_ge = re.search(r'\\verzeichniszeile\{(.*)\}', open('gesamt.tex', encoding='utf-8').read()).group(1)
klar = lambda v: re.sub(r'\\verz\{\w+\}\{([^}]*)\}', r'\1', v).replace(r' \verztrenn ', ' • ')
P.append('Verzeichniszeile Lernblatt: ' + klar(vz_lb))
P.append('Verzeichniszeile Gesamt: ' + klar(vz_ge))
P.append('')
P.append('Schritte (Schritt · Anlass):')
SCHRITTE = [
    'Read unterrichtsblatt.md Teil 1 · Anleitung lesen',
    'Read unterrichtsblatt.md Teil 2 · Anleitung bis zur letzten Zeile',
    'PowerShell · Arbeitsverzeichnis, Stempel t0 (allein)',
    'PowerShell · katalog/index.md und blaetter/index.md holen',
    'Grep · Register nach terme/binomische durchsuchen (Ausgabe zu groß für die Anzeige)',
    'PowerShell · Registerzeilen terme.md, binomische-formeln.md und Blätterregister anzeigen (Thema nicht gebaut → mit Ausblick)',
    'PowerShell · Einträge terme.md und binomische-formeln.md holen (Klassenarbeit, zwei Themen)',
    'Read terme.md · Eintrag lesen',
    'Read binomische-formeln.md · Eintrag lesen',
    'PowerShell · mathblatt.sty und Anleitung_mathblatt.md holen',
    'Read Anleitung Teil 1 · Makronamen',
    'Read Anleitung Teil 2 · Makronamen bis zum Ende',
    'Write test_bausteine.tex · Probe: Titel mit \\anweisung, Kreuzzeile, \\rechteck, Flächenbild, \\erg, Abhakgruppe kursiv',
    'PowerShell · Probe kompilieren und rendern',
    'Read test_b-1.png · Probe ansehen',
    'Read test_b-2.png · Probe ansehen',
    'Write zone_a.tex · Zone Aufgaben',
    'Write zone_l.tex · Zone Lösungen',
    'Write pruef.py · Prüfskript, Teil zone',
    'Write zone.tex · Rahmen Zone',
    'Write probe.tex · Prüfrahmen je Einheit (Aufgaben und Lösungen)',
    'PowerShell · pruef zone (0 Abweichungen), Probe zone; Korrektur nötig: -jobname=$j ohne Anführungszeichen nicht ersetzt, Datei „$j.pdf“; Stempel zone dabei verfrüht geschrieben',
    'PowerShell · Dateiliste (Ursache $j.*)',
    'PowerShell · $j.* gelöscht, verfrühten Stempel zone entfernt, Zone neu kompiliert, Stempel zone',
    'Read zone_s-1.png · Zone Seite 1',
    'Read zone_s-2.png · Zone Seite 2',
    'Write e1_a.tex · Einheit 1 Aufgaben',
    'Write e1_l.tex · Einheit 1 Lösungen',
    'Edit pruef.py · Teil e1',
    'PowerShell · Stempel weiter; pruef e1 (0), Probe e1, Stempel e 1',
    'Read e1_s-1.png · Einheit 1 Seite 1',
    'Read e1_s-2.png · Einheit 1 Seite 2',
    'Read e1_s-3.png · Einheit 1 Seite 3 (Skizze)',
    'Write e2_a.tex · Einheit 2 Aufgaben',
    'Write e2_l.tex · Einheit 2 Lösungen',
    'Edit e2_a.tex · \\clearpage aus der Einheitsdatei in die Rahmen verlegt',
    'Edit pruef.py · Teil e2',
    'Edit pruef.py · Produktprüfung unausgewertet parsen (6*(x+1) wird sonst ausmultipliziert)',
    'PowerShell · pruef e2 (0), Probe e2, Stempel e 2',
    'Read e2_s-1.png · Einheit 2 Seite 1',
    'Read e2_s-2.png · Einheit 2 Seite 2 (Skizze)',
    'PowerShell · Korrektur Nr. 20: Schulhof „4x m breit“ ergab 40 m breit und 25 m lang – lang/breit getauscht',
    'Write e3_a.tex · Einheit 3 Aufgaben',
    'Write e3_l.tex · Einheit 3 Lösungen',
    'Edit pruef.py · Teil e3',
    'PowerShell · pruef e3 (0), Probe e3, Stempel e 3',
    'Read e3_s-1.png · Einheit 3 Seite 1',
    'Read e3_s-3.png · Einheit 3 Seite 3',
    'Read e3_s-4.png · Einheit 3 Seite 4 (Flächenbild, Skizze)',
    'PowerShell · Korrektur: Titel Nr. 27 brach „entste-hen“ – gekürzt; Felder Nr. 22 und Nr. 10 standen nicht in einer Flucht (\\hfill in teile) – in geruest; e3 und e1 neu kompiliert',
    'Read e3_k-1.png · geänderte Seite',
    'Read e1_k-1.png · geänderte Seite',
    'Write e4_a.tex · Einheit 4 Aufgaben',
    'Write e4_l.tex · Einheit 4 Lösungen',
    'Edit pruef.py · Teil e4',
    'Edit pruef.py · Erkennung dritte Formel vereinfacht (Skriptfehler vor dem Lauf)',
    'PowerShell · pruef e4: 1 Abweichung 29c (Skript: False, Blatt: True), Probe e4',
    'PowerShell · Skript untersucht: unausgewertete Klammern (y - 1*2) werden nicht gleich erkannt',
    'Edit pruef.py · ist_quadrat vergleicht über neu geparste Faktoren (Skript falsch modelliert)',
    'PowerShell · pruef e4 (0), Stempel e 4',
    'Read e4_s-2.png · Einheit 4 Seite 2',
    'Read e4_s-3.png · Einheit 4 Seite 3',
    'Read e4_s-4.png · Einheit 4 Seite 4 (Flächenbilder)',
    'Read e4_s-1.png · Einheit 4 Seite 1 (Kreuzzeilen)',
    'Write e5_a.tex · Einheit 5 Aufgaben',
    'Write e5_l.tex · Einheit 5 Lösungen',
    'Edit pruef.py · Teil e5',
    'Edit pruef.py · Quadrat-Erkennung vereinfacht (vor dem Lauf)',
    'PowerShell · pruef e5 (0), Probe e5, Stempel e 5',
    'Read e5_s-1.png · Einheit 5 Seite 1',
    'Read e5_s-4.png · Einheit 5 Seite 4 (Skizze)',
    'Write bau_rahmen.py · Abhakseite, Verzeichniszeilen und Rahmen aus den Quelltexten',
    'PowerShell · Rahmen erzeugt, Lernblatt zweimal kompiliert, Nummernfolge und Kopfzeilen geprüft, Stempel lernblatt',
    'Read lb_s-01.png · Lernblatt Seite 1 (Verzeichniszeile)',
    'Read lb_e-19.png · Abhakseite',
    'PowerShell · Gesamt zweimal kompiliert, Nummernfolge 1–48 und Kopfzeilen geprüft, Stempel gesamt',
    'PowerShell · Lösungen kompiliert, 48 Lösungsnummern, Abhakzeilen 48/39, Stempel loesungen',
    'Read lo_s-1.png · Lösungen Seite 1',
    'Write archiv.py · Protokoll, Chat, Archiv',
    'PowerShell · archiv.py: protokoll.txt, chat.txt, Zip',
]
for i, s in enumerate(SCHRITTE, 1):
    P.append(f'{i} · {s}')
P.append('')
P.append('Vorlage: fehlende Bausteine · Warnungen aus dem Log: \\flaechenbild (Rechteck mit geteilten Seiten) · keine')
P.append(f'Korrekturrunden: 6 von {len(SCHRITTE)} Schritten (Zone-Jobname, Nr. 20 lang/breit, Nr. 27 Titel und Fluchten Nr. 10/22, pruef.py Produktprüfung, pruef.py 29c, pruef.py Formel- und Quadraterkennung vor dem Lauf)')
P += zeiten
P.append('Hinweis: der Stempel zone wurde im ersten, gescheiterten Zonenlauf verfrüht geschrieben und vor dem erfolgreichen Lauf entfernt; die Datei trägt nur den Stempel des fertigen Laufs.')
open('protokoll.txt', 'w', encoding='utf-8').write('\n'.join(P) + '\n')

# --- chat.txt
C = []
C.append('Eingabe: klassenarbeit terme binomische formeln 8 gymnasium – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch')
C.append('')
C.append(DEUTUNG)
C += plan
C.append('')
C.append('Planfrage: keine (Klassenarbeit: Umfangs- und Stufenfrage entfallen); Antwort aus der Eingabe „alle“ – gegenstandslos')
C.append('Rückfragen: keine')
C.append('')
C.append(DATEIEN[0])
C.append('Weiter baut Einheit 1 bis 5, Gesamt und Lösungen.')
C.append('weiter (aus der Eingabe)')
C.append('')
C += DATEIEN[1:]
C.append(f'{THEMA_DATEI}_{DATUM}_protokoll.zip')
C += AUSGABE
open('chat.txt', 'w', encoding='utf-8').write('\n'.join(C) + '\n')

# --- Archiv
name = f'{THEMA_DATEI}_{DATUM}_protokoll.zip'
muster = ['*.pdf', '*.tex', '*.log', 'pruef.py', 'pruef_out_*.txt', 'bau_rahmen.py', 'archiv.py', 'mathblatt.sty',
          'Anleitung_mathblatt.md', 'terme.md', 'binomische-formeln.md', 'katalog_index.md', 'blaetter_index.md',
          'zeiten.txt', 'protokoll.txt', 'chat.txt']
dateien = sorted({f for m in muster for f in glob.glob(m)})
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in dateien:
        z.write(f)
print(name, len(dateien), 'Dateien')
print('\n'.join(P[-12:]))
