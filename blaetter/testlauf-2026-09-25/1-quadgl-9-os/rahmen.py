# rahmen.py – Abhakseite aus den Aufgabenquelltexten (wortgleich) und Verzeichnis aus dem Kompilat.
#   python rahmen.py abhaken                      -> abhaken.tex
#   python rahmen.py bau <rahmen.tex> <jobname>   -> 1. Lauf, Seiten per Textextraktion, <jobname>_seiten.tex, 2 weitere Läufe
import re
import subprocess
import sys

TEILE = [('zone_a.tex', 'Das kennst du schon', 'zone'), ('e1_a.tex', 'Einheit 1 · Wurzelziehen und Lösbarkeit', 'e1'),
         ('e2_a.tex', 'Einheit 2 · Normalform und p-q-Formel', 'e2'), ('e3_a.tex', 'Einheit 3 · Sachaufgaben', 'e3'),
         ('e4_a.tex', 'Ausblick Einheit 4 · Satz vom Nullprodukt', 'e4')]
# Kennung im Kompilat: Zweigkopf der jeweiligen Einheit
KOPF = {'zone': 'Das kennst du schon', 'e1': 'Einheit 1 von 4', 'e2': 'Einheit 2 von 4', 'e3': 'Einheit 3 von 4',
        'e4': 'Ausblick Einheit 4 von 4', 'abhaken': 'Das kann ich'}


def titel(datei):
    """(Nummer, Ich-kann-Satz) je Hauptnummer; Satz = erster Satz des aufgabe-Arguments ohne Zeitmarke"""
    t = open(datei, encoding='utf-8').read()
    start = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', t).group(1))
    zone = 'Z\\arabic' in t
    out = []
    for i, m in enumerate(re.finditer(r'\\begin\{aufgabe\}\{', t), start=1):
        s = t[m.end():]
        # erster Satz: bis zum ersten Punkt außerhalb von $...$
        tiefe, mathe, j = 0, False, 0
        while j < len(s):
            ch = s[j]
            if ch == '$':
                mathe = not mathe
            elif ch == '.' and not mathe and (j + 1 == len(s) or s[j + 1] in ' }'):
                break
            j += 1
        satz = s[:j + 1]
        satz = re.sub(r' \(kommt[^)]*\)', '', satz)
        nr = f'Z{start + i}' if zone else str(start + i)
        out.append((nr, satz))
    return out


def abhaken():
    z = ['% Abhakseite „Das kann ich“ – erzeugt von rahmen.py aus den Aufgabenquelltexten',
         '\\clearpage', '\\hypertarget{abhaken}{}\\einheitenkopf{Das kann ich}',
         '{\\small Hake ab, was du kannst.\\par}\\medskip']
    for datei, kopf, _ in TEILE:
        z.append(f'\\abhakkopf{{{kopf}}}')
        for nr, satz in titel(datei):
            z.append(f'\\abhak{{{nr}}}{{{satz}}}')
    open('abhaken.tex', 'w', encoding='utf-8').write('\n'.join(z) + '\n')
    print(len([l for l in z if l.startswith('\\abhak{')]), 'Hauptnummern auf der Abhakseite')


def lauf(tex, job):
    subprocess.run(['xelatex', '-interaction=nonstopmode', f'-jobname={job}', tex], stdout=subprocess.DEVNULL)


def seiten(job):
    subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', f'{job}.pdf', f'{job}.txt'])
    s = open(f'{job}.txt', encoding='utf-8').read().split('\f')
    s = [p for p in s if p.strip()] if s and not s[-1].strip() else s
    return s


def bau(tex, job):
    open(f'{job}_seiten.tex', 'w', encoding='utf-8').write('')
    lauf(tex, job)
    lauf(tex, job)
    s = seiten(job)
    anfang = {}
    mit_zone = '\\input{zone_a}' in open(tex, encoding='utf-8').read()
    for k, kopf in KOPF.items():
        if k == 'zone' and not mit_zone:
            continue
        for i, p in enumerate(s[1:], start=2):
            if kopf in p:
                anfang[k] = i
                break
    folge = sorted(anfang, key=anfang.get)
    defs = []
    for n, k in enumerate(folge):
        a = anfang[k]
        e = anfang[folge[n + 1]] - 1 if n + 1 < len(folge) else len(s)
        txt = f'Seite {a}' if a == e else f'Seiten {a}–{e}'
        name = {'zone': 'Szone', 'e1': 'Seins', 'e2': 'Szwei', 'e3': 'Sdrei', 'e4': 'Svier', 'abhaken': 'Sabhaken'}[k]
        defs.append(f'\\def\\{name}{{{txt}}}')
        print(job, k, txt)
    open(f'{job}_seiten.tex', 'w', encoding='utf-8').write('\n'.join(defs) + '\n')
    lauf(tex, job)
    lauf(tex, job)
    # Gegenprobe: Seiten im Endkompilat unverändert
    s2 = seiten(job)
    for k in folge:
        ok = KOPF[k] in s2[anfang[k] - 1]
        print(job, 'Gegenprobe', k, 'Seite', anfang[k], 'OK' if ok else 'ABWEICHUNG')
    print(job, 'Seiten gesamt', len(s2))


if __name__ == '__main__':
    if sys.argv[1] == 'abhaken':
        abhaken()
    else:
        bau(sys.argv[2], sys.argv[3])
