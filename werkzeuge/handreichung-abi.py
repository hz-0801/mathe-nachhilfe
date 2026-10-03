"""Daten für die Abitur-Handreichungen GK und LK (v0.1, 03.10.2026).

Die Themen sind die Themenknöpfe des Abitur-Baums (offen.html,
werkzeuge/baum-offen.py); jede Themenbezeichnung des Katalogs gehört zu
genau einem Knopf (KNOPF unten). Gezählt werden alle angebotenen BE der
Hefte 2022–2026 (Teil A und Teil B, beide Wahlwege) aus
abitur/abi-katalog.csv. „jedes Jahr“ = der Knopf hat in allen fünf
Heften Punkte. Schreibt abitur/handreichung-abi-daten.md.
Schreibt außerdem abitur/handreichung-abi-gk-2027.tex und -lk-2027.tex
(eine Seite nach dem Muster der P10-Handreichung); die Themenliste darin
kommt aus KNOPF, damit Handreichung und Baum dieselben Namen tragen.
Abgeleitet, nie von Hand ändern. Aufruf aus der Wurzel:
python werkzeuge/handreichung-abi.py
"""
import csv, os, collections

W = os.path.join(os.path.dirname(__file__), '..')
HEFTE = {'GK': ['2022-bebb-gk', '2023-bebb-gk', '2024-bebb-gk', '2025-bebb-gk', '2026-bb-gk'],
         'LK': ['2022-bebb-lk', '2023-bebb-lk', '2024-bebb-lk', '2025-bebb-lk', '2026-bb-ea']}

# Gebiet -> Knopf -> Themen des Katalogs (Reihenfolge = Lernreihenfolge)
KNOPF = {
    'Analysis': {
        'Ableitung + Tangente': ['Ableitung und Änderungsrate', 'Ableitungsregeln',
                                 'Tangente, Normale, Schnittwinkel'],
        'Kurvenuntersuchung': ['Kurvenuntersuchung', 'Funktionsklassen und Eigenschaften',
                               'Grenzwerte und Verhalten im Unendlichen', 'Gleichungen lösen',
                               'Ableitungsgraph und Funktionsgraph', 'Extremalprobleme',
                               'Rekonstruktion von Funktionsgleichungen', 'Umkehrfunktion',
                               'Trigonometrische Funktionen'],
        'Integral': ['Flächeninhalt durch Integration', 'Stammfunktion und Hauptsatz',
                     'Rekonstruktion von Beständen', 'Integrationsregeln',
                     'Uneigentliche Integrale', 'Rotationsvolumen'],
        'Scharen': ['Funktionsscharen und Ortskurven'],
    },
    'Stochastik': {
        'Baumdiagramm + bedingte Wahrscheinlichkeit': [
            'Baumdiagramm und Pfadregeln', 'Vierfeldertafel', 'Bedingte Wahrscheinlichkeit und Bayes',
            'Unabhängigkeit', 'Zufallsexperimente und Urnenmodelle',
            'Ereignisse und Mengenoperationen', 'Kombinatorik'],
        'Binomialverteilung': ['Binomialverteilung', 'Kenngrößen von Verteilungen',
                               'Hypergeometrische Verteilung', 'Zufallsgrößen und Verteilungen'],
        'Testen': ['Hypothesentests', 'Normalverteilung und Sigma-Regeln', 'Konfidenzintervalle'],
    },
    'Geometrie': {
        'Punkte, Flächen, Körper': ['Punkte und Strecken im Koordinatensystem',
                                    'Flächeninhalt und Volumen im Raum',
                                    'Vektoren und Rechenoperationen'],
        'Geraden + Ebenen': ['Geraden', 'Ebenen', 'Lagebeziehungen', 'Schnittmengen',
                             'Spiegelung', 'Linearkombination und lineare Abhängigkeit'],
        'Winkel + Abstände': ['Skalarprodukt und Winkel', 'Orthogonalität', 'Abstände'],
        'Scharen': ['Scharen von Geraden und Ebenen'],
    },
}
KOPF = {
    'GK': dict(titel='Abitur · Mathematik GK', zeit='285 Minuten', a='100 Minuten'),
    'LK': dict(titel='Abitur · Mathematik LK', zeit='330 Minuten', a='110 Minuten'),
}
TEX = r'''\documentclass[12pt]{extarticle}
\usepackage[a4paper,left=2.8cm,right=2.8cm,top=2.2cm,bottom=2cm]{geometry}
\usepackage{amsmath,xcolor,enumitem,amssymb}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlist{leftmargin=1.4em,itemsep=3pt,topsep=4pt}
\newcommand{\abschnitt}[1]{\par\vspace{18pt}{\large\bfseries #1}\par\vspace{5pt}}
\newcommand{\jj}{\,$\bullet$}
\begin{document}
{\LARGE\bfseries TITEL}\hfill{\small\color{gray}Stand Oktober 2026}
\abschnitt{Termin}
Mittwoch, 5.\,Mai 2027, ZEIT (Berlin)
\abschnitt{Zwei Teile}
\begin{tabular}{@{\hspace{1.4em}}l@{\hspace{1em}}l@{}}
\textbf{Teil A} & kurze Aufgaben \textbf{ohne} Taschenrechner und Formelsammlung,\\
 & Abgabe spätestens nach ABGABE\\[3pt]
\textbf{Teil B} & große Aufgaben \textbf{mit} Hilfsmitteln, Analysis mit Wahl\\
\end{tabular}
\abschnitt{Mitbringen}
Taschenrechner (wie im Unterricht: WTR oder MMS/CAS), Formelsammlung des IQB, Geodreieck
\abschnitt{In dieser Reihenfolge lernen}
{\small Anteil an allen Punkten der Prüfungen 2022--2026 \quad $\bullet$ kam jedes Jahr dran}\par\vspace{6pt}
\begin{minipage}{12cm}
LISTE\end{minipage}
\par\vspace{8pt}
{\small Die Hälfte aller Punkte kommt aus der Analysis. Ihr Kern -- Nullstellen, Extrem- und Wendepunkte -- kommt jedes Jahr; vor der Prüfung gezielt wiederholen.}
\abschnitt{Alte Prüfungen zum Üben}
Stark-Band Abitur 2027 (KURS): Prüfungen 2022--2025 mit Lösungen, 2026 online.
\end{document}
'''


def tex(kurs, p, j, ges):
    li = []
    for g, ks in KNOPF.items():
        pg = sum(p[(g, k)] for k in ks)
        li.append(f'\\textbf{{{g}}} \\hfill \\textbf{{{100*pg/ges:.0f}\\,\\%}}\\phantom{{\\jj}}\\par')
        li.append('\\begin{enumerate}[label=\\arabic*.,leftmargin=1.8em,itemsep=2pt]')
        for k in ks:
            if p[(g, k)]:
                m = '\\jj' if len(j[(g, k)]) == 5 else '\\phantom{\\jj}'
                li.append(f'\\item {k} \\hfill {100*p[(g,k)]/ges:.0f}\\,\\%{m}')
        li.append('\\end{enumerate}\\vspace{4pt}')
    k = KOPF[kurs]
    t = (TEX.replace('TITEL', k['titel']).replace('ZEIT', k['zeit']).replace('ABGABE', k['a'])
         .replace('KURS', 'Grundkurs' if kurs == 'GK' else 'Leistungskurs').replace('LISTE', '\n'.join(li) + '\n'))
    open(os.path.join(W, 'abitur', f'handreichung-abi-{kurs.lower()}-2027.tex'), 'w', encoding='utf-8').write(t)


ZU = {t: (g, k) for g, ks in KNOPF.items() for k, ts in ks.items() for t in ts}


def main():
    r = list(csv.DictReader(open(os.path.join(W, 'abitur', 'abi-katalog.csv'), encoding='utf-8'),
                            delimiter=';'))
    o = ['# Abitur-Handreichung – Daten je Themenknopf', '',
         'Abgeleitet von `werkzeuge/handreichung-abi.py` (v0.1); nie von Hand ändern. '
         'Angebotene BE 2022–2026, Teil A und B, beide Wahlwege; Knöpfe wie im Abitur-Baum.', '']
    for kurs, hefte in HEFTE.items():
        z = [x for x in r if x['papier'] in hefte]
        ges = sum(int(x['punkte'] or 0) for x in z)
        p = collections.Counter(); pa = collections.Counter(); j = collections.defaultdict(set)
        fremd = collections.Counter()
        for x in z:
            if x['thema'] not in ZU:
                fremd[x['thema']] += int(x['punkte'] or 0); continue
            g, k = ZU[x['thema']]
            p[(g, k)] += int(x['punkte'] or 0); j[(g, k)].add(x['papier'])
            if x['block'] == 'A':
                pa[(g, k)] += int(x['punkte'] or 0)
        o += [f'## {kurs} ({ges} BE in fünf Heften)', '',
              '| Gebiet | Knopf | Anteil | jedes Jahr | davon ohne Hilfsmittel |', '|---|---|---|---|---|']
        for g, ks in KNOPF.items():
            pg = sum(p[(g, k)] for k in ks)
            o.append(f'| **{g}** | | **{100*pg/ges:.0f} %** | | |')
            for k in ks:
                if p[(g, k)] == 0:
                    continue
                o.append(f'| | {k} | {100*p[(g,k)]/ges:.0f} % | {"•" if len(j[(g,k)]) == 5 else ""} '
                         f'| {100*pa[(g,k)]/p[(g,k)]:.0f} % |')
        tex(kurs, p, j, ges)
        summe = sum(p.values()) + sum(fremd.values())
        o += ['', f'Gegenprobe: zugeordnet {sum(p.values())} BE + ohne Knopf {sum(fremd.values())} BE '
              f'= {summe} BE (Soll {ges}).']
        if fremd:
            o.append('Ohne Knopf: ' + ', '.join(f'{t} ({n} BE)' for t, n in fremd.most_common()))
        o.append('')
    open(os.path.join(W, 'abitur', 'handreichung-abi-daten.md'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
    print('\n'.join(o))


if __name__ == '__main__':
    main()
