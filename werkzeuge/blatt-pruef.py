#!/usr/bin/env python3
r"""blatt-pruef.py – Kennzahlen je Blatt unter blaetter/ (v0.3, 27.09.2026; v0.2 25.09.2026; v0.1 26.09.2026)

v0.3 (Auftrag Nacht 2026-09-27, Teil 8): Bausteine der Vorlage Stufe 5 – \swfrage zählt als Teilaufgabe
(Liste TEILZAEHLER); für Blätter, die \zweigzeile, die Umgebung abhakseite, \abhak, \verzeichniszeile, \verz oder
\swfrage tragen, drei weitere Kennzahlen je Blatt:
 10 Zweigzeilen je Einheitenkopf: „Einheitenköpfe n · Zweigzeilen m“ (Einheitenkopf = \einheitenkopf u. a. mit
    „Einheit n …“ oder „·“ im Text; „Inhalt“, „Das kennst du schon“, „Das kann ich“ zählen als weitere Köpfe),
    dazu die Zahl der \swfrage.
 11 Abhakseite: ja, wenn \begin{abhakseite} vorkommt; Zahl der Zeilen = Zahl der \abhak.
 12 Verzeichniszeile: ja, wenn \verzeichniszeile oder \verz vorkommt; Zahl der Einträge = Zahl der \verz.
    Dazu die Zuordnung Einheitenkopf → Lerneinheit, wie Kennzahl 9 sie trifft (unten), und ein Vermerk, wenn
    kein Kopf eine Lerneinheit trifft.
Die Zuordnung Einheitenkopf → Lerneinheit läuft über den Titel (Text hinter dem letzten „·“, ohne
Sprungmarken und ohne eine Ich-Form am Anfang wie „Ich kann“), nie über die Blattnummer „Einheit n von m“ –
die ist die Nummer im Blatt, nicht im Katalog. Blätter ohne diese Bausteine messen und schreiben sich
byteidentisch wie in v0.2 (geprüft am 27.09.2026 an allen 22 PDFs unter blaetter/).

Misst für jedes abgelegte Blatt, was die Befunde vom 24.09.2026 von Hand gezählt
haben (befund-schwach-blatt-2026-09-24.md), damit zwei Läufe desselben Themas
verglichen werden können. Ändert nichts außer blaetter/kennzahlen.md.

Aufruf (Arbeitsordner beliebig; das Skript sucht die Repo-Wurzel über seinen Ort):
  python werkzeuge/blatt-pruef.py          baut blaetter/kennzahlen.md neu (alle Blätter)
  python werkzeuge/blatt-pruef.py <pfad>   misst nur ein Blatt – eine PDF-Datei unter
                                           blaetter/<thema>/<datum>/pdf/ oder einen
                                           Blattordner blaetter/<thema>/<datum>/ – und gibt
                                           die Kennzahlen auf der Konsole aus;
                                           kennzahlen.md bleibt dabei unverändert

Eingabe: je Ordner blaetter/<thema>/<datum>/ jede PDF-Datei unter pdf/ mit der
gleichnamigen tex-Datei unter src/ (Groß-/Kleinschreibung egal; \input wird
aufgelöst). Register blaetter/index.md (Prompt-Version, Katalogeintrag), die
Katalogeinträge katalog/<name>.md. Werkzeuge pdfinfo und pdftotext (poppler): im
PATH oder im MiKTeX-Ordner %LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64.

Lesarten (was gezählt wird; Nummern = Kennzahlen des Auftrags):
 1  Seiten: pdfinfo „Pages“. Aufgabenseiten: die Seiten vor der Seite mit der
    Überschrift „Ergebnisse“ (\begleitteil); ohne Begleitteil alle Seiten.
 2  Hauptnummer = \begin{aufgabe}; ihre Nummer zählt das Skript wie die Vorlage
    (\setcounter{aufgabe}{n} setzt, \begleitteil setzt auf 0). Teilaufgaben = höchster
    Stand des Buchstabenzählers in der Hauptnummer (\teil, \steil, \tz, \stz, \gl,
    \sgl, \gz, \gzs, je Eintrag der Listenmakros \mnliste, \nullstellenliste,
    \punktprobenliste; \setcounter{teil}{n} setzt ihn) – oder, wenn größer, die Zahl
    der Buchstabenmarken „a)“ am Zeilenanfang des Quelltexts (Teilaufgaben, die in
    einer Tabelle stehen und den Zähler nicht bewegen).
 3  Seite einer Hauptnummer = Seite des pdftotext-Texts (-layout, Seitentrennung
    durch Seitenvorschub), auf der die Zeile „N. <Titelanfang>“ steht (N wie unter 2,
    Titelanfang nur aus Buchstaben und Ziffern verglichen). Ihre Teilaufgaben zählen
    auf der Seite, auf der sie beginnt (die Vorlage hält eine Hauptnummer auf einer
    Seite).
 4  Titel = erster Satz des Arguments von \begin{aufgabe}: bis „.“, „?“ oder „!“ vor
    Leerraum oder Ende (z. B., d. h., u. a., Nr., S., ca., bzw. brechen nicht);
    TeX-Befehle entfernt, „--“ als „–“, Leerraum zusammengezogen, der schließende
    Punkt weggelassen („?“ und „!“ bleiben). Form:
    „Kurzname – Formwort“ = zwei nichtleere Teile um einen Gedankenstrich (Muster
    v4.2, unterrichtsblatt.md 2.3 e); „Ich kann …“ = Titel beginnt mit „Ich kann“;
    sonst „anderes“.
 5  Darstellungen: Makros und Umgebungen der Vorlage mathblatt.sty (Version
    2026-09-22h, ../blattbau) je Kategorie nach DARSTELLUNG unten; jedes Makro, dessen
    Name mit „streifen“ beginnt, zählt als Streifen, auch ein blatteigenes
    (\streifenfeld). Freies TikZ (\begin{tikzpicture}) zählt als Skizze.
 6  Antwortform: Raster = \gl/\sgl (Schreibzeilen je Gleichung: eigenes Argument,
    sonst das des gleichungsraster, sonst 2) und \schreibzeilen{n}, gezählt in
    Zeilen; Antwortlinie = \leerfeld, \feld, \feldl, \dsleer, \leerzelle, \punktfeld
    und das blatteigene \pfeld; Kasten = Ankreuzkästchen \kreuz, \janein (je zwei
    Kästchen), \square; „nichts“ = keins davon. Ein blatteigenes Makro (Definition im
    Quelltext oder in src/*.sty) zählt mit den Antwortfeldern seines Rumpfs
    (\streifenfeld trägt ein \leerfeld).
 7  Merkkasten = \uebersichtskasten, \merkkasten oder \begin{tcolorbox} im Quelltext;
    Position „vor“, „zwischen“ oder „nach“ den Aufgaben nach der Stellung im
    Quelltext.
 8  Fachwörter: Abschnitt „### Merkkasten“ des Katalogeintrags. Fett gesetzte
    Begriffe (**…**); fehlen sie, die Begriffe vor einem Doppelpunkt: in den
    Kastenzeilen (genau vier Leerzeichen Einzug; die tiefer eingerückten
    Beispielzeilen nicht) je Satz das Stück vor dem ersten Doppelpunkt, wenn es mit
    einem Buchstaben beginnt, keine Ziffer und kein „=“ enthält und höchstens fünf
    Wörter hat; Klammerzusätze gestrichen; ausgenommen die Kastenmarken
    „Formelsammlung“, „Auswendig (Teil A)“, „Quelle“. Erstes Auftreten = erste
    Hauptnummer, in deren Titel oder Text (TeX-Befehle entfernt) die Wörter des
    Begriffs in dieser Folge als Wortanfänge stehen (Stamm wie unter 9).
 9  Sprossenabgleich: Typen = die mit „·“ getrennten Stücke der Zeilen „Einheit n:“
    im Abschnitt „### Typen je Lerneinheit“; getrennt wird auch an „—“ und am
    Satzende, nie in Klammern und nie an einem Malpunkt in einer Formel (V = π · r² · h;
    Zerlegung seit 26.09.2026 aus werkzeuge/pruefungswort-belege.py übernommen, damit
    beide Werkzeuge dieselben Typen sehen); ein Vorspann bis zu einem Doppelpunkt mit Marke
    („Sek II …, Haupttypen …:“, „Deutung:“, „Dazu:“) wird abgelöst, „kein …typ“ ist
    kein Typ. Typen hinter „— Sek II“ und in Einheiten mit „(Sek II)“ im Titel
    tragen die Marke [Sek II] und zählen nicht in „ohne Treffer“ (ziel.md § 3:
    unter Klasse 11 keine Sek-II-Einheit; alle Blätter bisher Sek I).
    Kern = Text ohne Klammerzusätze, vor dem ersten Doppelpunkt. Kernwörter = Wörter
    aus Buchstaben mit mindestens drei Zeichen außer den Füllwörtern (FUELLWORT).
    Stamm = kleingeschrieben, ab sechs Zeichen ohne die letzten zwei, bei fünf ohne
    das letzte. Treffer = jeder Stamm des Kerns steht als Wortanfang in derselben
    Hauptnummer (Titel oder Text); Teiltreffer = mindestens einer (genannt wird die
    erste Hauptnummer mit den meisten Stämmen und die fehlenden Kernwörter).
    „Ohne Treffer“ zählt die Typen ohne vollen
    Treffer in den Einheiten, die das Blatt baut – erkannt am Einheitenkopf
    („… · <Titel>“; \einheitenkopf, \einheitskopf, \blattunter) gegen den Titel der
    Lerneinheit (Text vor „ – “): gleich, wenn mindestens zwei Drittel der Kernwörter
    des längeren Titels im anderen als Wortanfang stehen; ohne erkannten Kopf alle
    Einheiten. Nennt der Quelltext „Blatt 0“ und ist keine Einheit erkannt, trägt die
    Datei nur Blatt 0 und Kennzahl 9 entfällt. Ein Typ ohne Kernwort gilt als „nicht
    prüfbar“.

Testlauf (v0.2, 25.09.2026, Auftrag Testlauf des Unterrichtsblatt-Prompts):
  python werkzeuge/blatt-pruef.py --testlauf blaetter/testlauf-<datum> [--ausgabe <datei>]
misst in jedem Unterordner <nr>-<kurzname>/ die PDFs nach dem Namensschema des Prompts
(unterrichtsblatt.md 4.5) mit „_Gesamt“ oder „_Fokus“ im Namen, ohne „Loesungen“ – nicht die
Zwischenkompilate der Sitzung (gesamt.pdf, probe_e1.pdf …). Der Ordner ist flach: Quelltexte, protokoll.txt und PDFs liegen
nebeneinander. Quelltext = gleichnamige tex-Datei, sonst die tex-Datei, deren Name das
Blattwort nach dem letzten „_“ ist (gesamt.tex, fokus*.tex), sonst die tex-Datei mit
\blattkopf{…}{<Blattwort>…}. Prompt und Katalogeintrag stehen nicht im Register, sondern
in protokoll.txt des Ordners (Zeile „Prompt:“; je Zeile „Katalog:“ der Name direkt dahinter –
nicht die Namen, die die Stand-Zeile des Eintrags nebenbei nennt; ein Blatt aus zwei Einträgen
hat zwei solche Zeilen). Spalte „Thema“ = Unterordner, „Datum“ = Testlaufordner.
  --ausgabe <datei>  schreibt die Kennzahlen dorthin statt nach blaetter/kennzahlen.md
                     (auch ohne --testlauf).

Register: Der Katalogeintrag steht in der Spalte „Katalog“ von blaetter/index.md.
Endet die Zelle auf „und“ (einsortieren.py übernimmt nur die erste Zeile des
Protokollfelds), liest das Skript die Fortsetzungszeilen von „Katalog:“ in
src/protokoll.txt dazu. Maßgeblich ist der Eintrag im heutigen katalog/.
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
BLAETTER = WURZEL / 'blaetter'
KATALOG = WURZEL / 'katalog'
AUSGABE = BLAETTER / 'kennzahlen.md'

# Kategorie je Makro oder Umgebung (mathblatt.sty 2026-09-22h)
DARSTELLUNG = {
    'Tabelle': ['sachtabelle', 'wertetabelle', 'wertetabelleleer', 'vierfeldertafel',
                'ENV:dreisatz', 'ENV:tabular'],
    'Skizze': ['dreieck', 'dreieckrw', 'viereck', 'parallelogramm', 'rechteck', 'trapez',
               'raute', 'drachen', 'quader', 'zylinder', 'prismadreieck', 'pyramide',
               'kegel', 'kugel', 'netzquader', 'netzwuerfel', 'netzpyramide',
               'netzzylinder', 'geradenkreuzung', 'parallelenpaar', 'winkel',
               'winkelstrahl', 'strahlensatz', 'ENV:kreis', 'ENV:tikzpicture'],
    'Koordinatensystem': ['ENV:ksys', 'ENV:ksys3', 'ableitungspaar'],
    'Balken': ['saeulen', 'saeulenab', 'balkenab', 'histogramm'],
    'sonstige': ['liniendia', 'kreisdiagramm', 'kreisdiagrammleer', 'kreisleer',
                 'kreissektor', 'ENV:boxplots', 'baumzwei', 'baumdrei', 'baumdreigleich',
                 'binomialverteilung', 'normalverteilung', 'zahlenstrahl',
                 'ENV:zahlengerade', 'bruchkreis', 'bruchrechteck', 'termbaum',
                 'einheitskreis'],
}
KATEGORIEN = ['Streifen', 'Tabelle', 'Skizze', 'Koordinatensystem', 'Balken', 'sonstige']
MAKRO_KAT = {m: k for k, ms in DARSTELLUNG.items() for m in ms}

ANTWORTLINIE = ['leerfeld', 'feld', 'feldl', 'dsleer', 'leerzelle', 'punktfeld', 'pfeld']
TEILZAEHLER = ['teil', 'steil', 'tz', 'stz', 'gl', 'sgl', 'gz', 'gzs', 'swfrage']   # swfrage: Vorlage Stufe 5 (v0.3)
LISTENMAKROS = ['mnliste', 'nullstellenliste', 'punktprobenliste']
KOPFMAKROS = ['einheitenkopf', 'einheitskopf', 'blattunter']
KASTENMARKEN = ('Formelsammlung', 'Auswendig', 'Quelle')

# Vorlage Stufe 5 (v0.3, Namen aus dem Auftrag Nacht 2026-09-27, Teil 8; ../blattbau/mathblatt.sty trug am
# 27.09.2026 noch Version 2026-09-22h ohne diese Bausteine)
ZWEIGZEILE = 'zweigzeile'                   # \zweigzeile{Fertigkeit · Zeitmarke · Prüfungswort} unter \einheitenkopf
ABHAKSEITE = ('abhakseite', 'abhak')        # \begin{abhakseite} … \abhak{nr}{titel} … \end{abhakseite}
VERZEICHNIS = ('verzeichniszeile', 'verz')  # \verzeichniszeile mit \verz{label}{text}
# Titel eines Einheitenkopfs = Text hinter dem letzten „·“ („Einheit 3 von 5 · Titel“: die Blattnummer davor ist
# nicht die Katalognummer und zählt nicht); eine Ich-Form am Anfang (v4.3: „Ich kann …“) wird abgelöst.
ICH_FORM = re.compile(r'^Ich\s+(?:kann|erkenne|finde|weiß)\s+', re.I)
KEIN_EINHEITENKOPF = ('Das kann ich',)      # Kopf der Abhakseite

FUELLWORT = set('''
aber alle allen aller alles also als am an auch auf aus bei beim beide beiden bis dann
das dass dem den denn der deren des dessen die diese diesem diesen dieser dieses doch
durch ein eine einem einen einer eines erst etwa für gegen genau hier ihre im immer in
ist jede jedem jeden jeder jedes kein keine keinem keinen keiner mal man mehr mit nach
nicht noch nur oder ohne sich sind statt über um und unter vom von vor warum was welche
welchem welchen welcher welches wenn wie wird zu zum zur zwei drei vier zwischen
'''.split())

ABKUERZUNGEN = ['z. B.', 'd. h.', 'u. a.', 'Nr.', 'S.', 'ca.', 'bzw.', 'vgl.', 'evtl.']


# ---------------------------------------------------------------- Werkzeuge

def werkzeug(name):
    pfad = shutil.which(name)
    if pfad:
        return pfad
    lad = os.environ.get('LOCALAPPDATA', '')
    kandidat = Path(lad) / 'Programs' / 'MiKTeX' / 'miktex' / 'bin' / 'x64' / (name + '.exe')
    if kandidat.exists():
        return str(kandidat)
    sys.exit(f'{name} nicht gefunden (PATH oder MiKTeX-Ordner)')


def pdf_seiten(pdf):
    aus = subprocess.run([werkzeug('pdfinfo'), str(pdf)], capture_output=True).stdout
    m = re.search(rb'^Pages:\s+(\d+)', aus, re.M)
    return int(m.group(1)) if m else None


def pdf_text(pdf):
    aus = subprocess.run([werkzeug('pdftotext'), '-layout', '-enc', 'UTF-8', str(pdf), '-'],
                         capture_output=True).stdout.decode('utf-8', 'replace')
    seiten = aus.split('\f')
    if seiten and not seiten[-1].strip():
        seiten = seiten[:-1]
    return seiten


# ---------------------------------------------------------------- TeX lesen

def ohne_kommentar(text):
    zeilen = []
    for z in text.split('\n'):
        m = re.search(r'(?<!\\)%', z)
        zeilen.append(z[:m.start()] if m else z)
    return '\n'.join(zeilen)


def lies_tex(pfad, tiefe=0):
    text = ohne_kommentar(pfad.read_text(encoding='utf-8'))
    if tiefe > 5:
        return text

    def ersetze(m):
        name = m.group(1).strip()
        if not name.endswith('.tex'):
            name += '.tex'
        ziel = pfad.parent / name
        return lies_tex(ziel, tiefe + 1) if ziel.exists() else ''
    return re.sub(r'\\input\{([^}]*)\}', ersetze, text)


def klammer(text, pos):
    """Inhalt der geschweiften Klammer ab text[pos] == '{'; gibt (inhalt, ende) zurück."""
    assert text[pos] == '{'
    tiefe = 0
    for i in range(pos, len(text)):
        c = text[i]
        if c == '\\':
            continue
        if c == '{' and (i == 0 or text[i - 1] != '\\'):
            tiefe += 1
        elif c == '}' and text[i - 1] != '\\':
            tiefe -= 1
            if tiefe == 0:
                return text[pos + 1:i], i + 1
    return text[pos + 1:], len(text)


def argumente(text, pos, n):
    """n Pflichtargumente ab pos (optionale [..] und * davor überspringen)."""
    args = []
    while len(args) < n:
        while pos < len(text) and text[pos] in ' \t\n*':
            pos += 1
        if pos < len(text) and text[pos] == '[':
            ende = text.find(']', pos)
            pos = ende + 1
            continue
        if pos < len(text) and text[pos] == '{':
            inhalt, pos = klammer(text, pos)
            args.append(inhalt)
        else:
            break
    return args, pos


def zu_text(tex):
    """TeX grob in Lesetext: Befehle weg, Argumente bleiben."""
    t = tex.replace('--', '–').replace('\\\\', ' ').replace('\\%', '%')
    t = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'\1/\2', t)
    t = re.sub(r'\\[,;:! ]', ' ', t)
    t = t.replace('~', ' ').replace('^2', '²').replace('^3', '³')
    t = re.sub(r'\\(cdot)\b', '·', t)
    t = re.sub(r'\\(approx)\b', '≈', t)
    t = re.sub(r'\\(rightarrow)\b', '→', t)
    t = re.sub(r'\\begin\{[^}]*\}|\\end\{[^}]*\}', ' ', t)
    t = re.sub(r'\\[A-Za-z]+\*?', ' ', t)
    t = re.sub(r'[{}$]', '', t)
    t = re.sub(r'\[[^\]]{0,12}\]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def erster_satz(text):
    geschuetzt = text
    for i, abk in enumerate(ABKUERZUNGEN):
        geschuetzt = geschuetzt.replace(abk, f'\x00{i}\x00')
    m = re.search(r'[.?!](?=\s|$)', geschuetzt)
    satz = geschuetzt[:m.end()] if m else geschuetzt
    for i, abk in enumerate(ABKUERZUNGEN):
        satz = satz.replace(f'\x00{i}\x00', abk)
    return satz.strip()


def titelform(titel):
    if titel.startswith('Ich kann'):
        return 'Ich kann'
    teile = re.split(r'\s+–\s+', titel, maxsplit=1)
    if len(teile) == 2 and teile[0].strip() and teile[1].strip(' .?!'):
        return 'Kurzname – Formwort'
    return 'anderes'


def norm(text):
    return re.sub(r'[^0-9a-zäöüß]', '', text.lower().replace('^', ''))


# ---------------------------------------------------------------- Blatt zerlegen

def zerlege(tex):
    """Liefert Hauptnummern, Merkkästen, Einheitenköpfe und Begleitteil-Lage."""
    ereignisse = []   # (pos, art, daten)
    for m in re.finditer(r'\\begin\{aufgabe\}', tex):
        arg, ende = argumente(tex, m.end(), 1)
        e = tex.find('\\end{aufgabe}', ende)
        ereignisse.append((m.start(), 'aufgabe', (arg[0] if arg else '', tex[ende:e])))
    for m in re.finditer(r'\\setcounter\{aufgabe\}\{(\d+)\}', tex):
        ereignisse.append((m.start(), 'setze', int(m.group(1))))
    for m in re.finditer(r'\\begleitteil\b', tex):
        ereignisse.append((m.start(), 'begleit', None))
    for m in re.finditer(r'\\(uebersichtskasten|merkkasten)\b|\\begin\{tcolorbox\}', tex):
        ereignisse.append((m.start(), 'kasten', None))
    for m in re.finditer(r'\\(' + '|'.join(KOPFMAKROS) + r')\*?(?=[\s{])', tex):
        arg, _ = argumente(tex, m.end(), 1)
        if arg:
            # v0.3: Sprungmarken im Kopf (\hypertarget{e1}{}, \label{…}) gehören nicht zum Text
            ereignisse.append((m.start(), 'kopf', zu_text(re.sub(r'\\(?:hypertarget|label)\{[^{}]*\}(?:\{\})?', '', arg[0]))))
    ereignisse.sort(key=lambda x: x[0])

    nummer = 0
    hauptnummern, kaesten, koepfe = [], [], []
    begleit = False
    for pos, art, daten in ereignisse:
        if art == 'setze':
            nummer = daten
        elif art == 'begleit':
            nummer = 0
            begleit = True
        elif art == 'aufgabe':
            nummer += 1
            hauptnummern.append({'nr': nummer, 'pos': pos, 'arg': daten[0],
                                 'rumpf': daten[1], 'begleit': begleit})
        elif art == 'kasten':
            kaesten.append(pos)
        elif art == 'kopf':
            koepfe.append(daten)
    hauptnummern = [h for h in hauptnummern if not h['begleit']]
    return hauptnummern, kaesten, koepfe, begleit


def teilaufgaben(rumpf):
    stand, hoechst = 0, 0
    muster = r'\\(setcounter)\{teil\}\{(\d+)\}|\\(' + '|'.join(TEILZAEHLER + LISTENMAKROS) + r')(?![A-Za-z])'
    for m in re.finditer(muster, rumpf):
        if m.group(1):
            stand = int(m.group(2))
        elif m.group(3) in LISTENMAKROS:
            arg, _ = argumente(rumpf, m.end(), 1)
            stand += len(listeneintraege(arg[0])) if arg else 0
        else:
            stand += 1
        hoechst = max(hoechst, stand)
    marken = set(re.findall(r'(?m)^\s*([a-z])\)\s', rumpf))
    return max(hoechst, len(marken))


def listeneintraege(text):
    eintraege, tiefe, akt = [], 0, ''
    for c in text:
        if c == '{':
            tiefe += 1
        elif c == '}':
            tiefe -= 1
        if c == ',' and tiefe == 0:
            eintraege.append(akt)
            akt = ''
        else:
            akt += c
    if akt.strip():
        eintraege.append(akt)
    return [e for e in eintraege if e.strip()]


def darstellungen(rumpf):
    gefunden = {}
    for m in re.finditer(r'\\begin\{([A-Za-z0-9]+)\}|\\([A-Za-z]+)(?![A-Za-z])', rumpf):
        if m.group(1):
            name, schluessel = m.group(1), 'ENV:' + m.group(1)
        else:
            name = schluessel = m.group(2)
        if not m.group(1) and name.startswith('streifen'):
            kat = 'Streifen'
        else:
            kat = MAKRO_KAT.get(schluessel)
        if kat:
            gefunden.setdefault(kat, []).append(name)
    return gefunden


def eigene_makros(tex, src):
    """Blatteigene Makros (\\newcommand, \\NewDocumentCommand im Quelltext und in src/*.sty):
    Name → Rumpf der Definition."""
    texte = [tex] + [ohne_kommentar(p.read_text(encoding='utf-8')) for p in sorted(src.glob('*.sty'))]
    makros = {}
    for t in texte:
        for m in re.finditer(r'\\(?:re)?newcommand\*?\s*\{?\\([A-Za-z]+)\}?', t):
            pos = m.end()
            while pos < len(t) and t[pos] in ' \t\n':
                pos += 1
            while pos < len(t) and t[pos] == '[':
                pos = t.find(']', pos) + 1
            if pos < len(t) and t[pos] == '{':
                makros[m.group(1)] = klammer(t, pos)[0]
        for m in re.finditer(r'\\(?:New|Declare)DocumentCommand\s*\{?\\([A-Za-z]+)\}?', t):
            args, _ = argumente(t, m.end(), 2)
            if len(args) == 2:
                makros[m.group(1)] = args[1]
    return makros


def zaehle_antwort(rumpf):
    linien = sum(len(re.findall(r'\\' + n + r'(?![A-Za-z])', rumpf)) for n in ANTWORTLINIE)
    kasten = (len(re.findall(r'\\kreuz(?![A-Za-z])', rumpf))
              + 2 * len(re.findall(r'\\janein(?![A-Za-z])', rumpf))
              + len(re.findall(r'\\square(?![A-Za-z])', rumpf)))
    return linien, kasten


def antwortform(rumpf, eigene=None):
    raster = 0
    standard = 2
    m = re.search(r'\\begin\{gleichungsraster\}\[(\d+)\]', rumpf)
    if m:
        standard = int(m.group(1))
    for m in re.finditer(r'\\s?gl(?![A-Za-z])(\[(\d+)\])?', rumpf):
        raster += int(m.group(2)) if m.group(2) else standard
    for m in re.finditer(r'\\schreibzeilen\{(\d+)\}', rumpf):
        raster += int(m.group(1))
    linien, kasten = zaehle_antwort(rumpf)
    for name, koerper in (eigene or {}).items():
        if name in ANTWORTLINIE or name in ('kreuz', 'janein'):
            continue
        n = len(re.findall(r'\\' + name + r'(?![A-Za-z])', rumpf))
        if n:
            l, k = zaehle_antwort(koerper)
            linien += n * l
            kasten += n * k
    teile = []
    if raster:
        teile.append(f'Raster {raster} Zeilen')
    if linien:
        teile.append(f'Antwortlinie ×{linien}')
    if kasten:
        teile.append(f'Kasten ×{kasten}')
    return ' · '.join(teile) if teile else 'nichts'


# ---------------------------------------------------------------- Katalog

def abschnitt(text, kopf):
    m = re.search(r'^### ' + re.escape(kopf) + r'[^\n]*\n(.*?)(?=^### |^## |\Z)', text, re.S | re.M)
    return m.group(1) if m else ''


def stamm(wort):
    w = wort.lower()
    if len(w) >= 6:
        return w[:-2]
    if len(w) == 5:
        return w[:-1]
    return w


def woerter(text):
    return re.findall(r'[A-Za-zÄÖÜäöüß]+', text)


def fachwoerter(eintrag_text):
    """[(Begriff, Einheit)] und die Art (fett / vor Doppelpunkt)."""
    teil = abschnitt(eintrag_text, 'Merkkasten')
    einheit = None
    fett, begriffe = [], []
    for zeile in teil.split('\n'):
        m = re.match(r'^Einheit (\d+)', zeile)
        if m:
            einheit = int(m.group(1))
        fett += [(f.strip(), einheit) for f in re.findall(r'\*\*([^*]+)\*\*', zeile)]
    if fett:
        return list(dict.fromkeys(fett)), 'fett'
    einheit = None
    for zeile in teil.split('\n'):
        m = re.match(r'^Einheit (\d+)', zeile)
        if m:
            einheit = int(m.group(1))
        if not re.match(r'^ {4}\S', zeile):
            continue
        for satz in re.split(r'(?<=[.;])\s+', zeile.strip()):
            if ':' not in satz:
                continue
            vorn = satz.split(':', 1)[0].strip()
            vorn = re.sub(r'\s*\([^)]*\)', '', vorn).strip()
            if not vorn or not vorn[0].isalpha() or re.search(r'[0-9=]', vorn):
                continue
            if vorn.startswith(KASTENMARKEN) or len(vorn.split()) > 5:
                continue
            begriffe.append((vorn, einheit))
    return list(dict.fromkeys(begriffe)), 'vor Doppelpunkt'


def lerneinheiten(eintrag_text):
    teil = abschnitt(eintrag_text, 'Lerneinheiten')
    einheiten = {}
    for m in re.finditer(r'^(\d+)\.\s+(.+?)(?:\s+–\s+|$)', teil, re.M):
        einheiten[int(m.group(1))] = m.group(2).strip()
    return einheiten


_PW = None


def typen(eintrag_text):
    """{Einheit: [(Typ, Sek-II-Zusatz ja/nein)]}. Die Zerlegung der Typenzeilen übernimmt
    werkzeuge/pruefungswort-belege.py (typen_des_eintrags: Trennung an „·“, „—“ und am Satzende
    außerhalb von Klammern, Malpunkte in Formeln wie „V = π · r² · h“ trennen nicht, Platzhalter
    „kein …typ“ fallen weg). Sek-II-Zusatz = Typ hinter „— Sek II“ oder in einer Sek-II-Einheit
    eines Sek-I-Eintrags; in einem Sek-II-Eintrag (ohne Abschnitt „Prüfungsform (P10)“) zählt jeder Typ."""
    global _PW
    if _PW is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location('pruefungswort_belege', Path(__file__).parent / 'pruefungswort-belege.py')
        _PW = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_PW)
    sek2_eintrag = '### Prüfungsform (P10)' not in eintrag_text
    return {n: [(t['text'], t['sek2'] and not sek2_eintrag) for t in liste]
            for n, liste in _PW.typen_des_eintrags(eintrag_text, sek2_eintrag).items()}


def kernwoerter(text):
    return [w for w in woerter(text) if len(w) >= 3 and w.lower() not in FUELLWORT]


def ohne_klammern(text):
    alt = None
    while alt != text:
        alt = text
        text = re.sub(r'\([^()]*\)', ' ', text)
    return text


def kernstaemme(typ):
    kern = ohne_klammern(typ).split(':', 1)[0]
    return [(w, stamm(w)) for w in kernwoerter(kern)]


def hat_staemme(staemme, textwoerter):
    return [s for s in staemme if any(w.startswith(s) for w in textwoerter)]


def folge_treffer(begriff, textwoerter):
    ws = [stamm(w) for w in woerter(begriff)]
    if not ws:
        return False
    for i in range(len(textwoerter) - len(ws) + 1):
        if all(textwoerter[i + k].startswith(ws[k]) for k in range(len(ws))):
            return True
    return False


# ---------------------------------------------------------------- Register

def register():
    zeilen = (BLAETTER / 'index.md').read_text(encoding='utf-8').split('\n')
    stand = zeilen[1].strip() if len(zeilen) > 1 else ''
    eintraege = {}
    for z in zeilen:
        if not z.startswith('| ') or z.startswith('| Thema') or z.startswith('|---'):
            continue
        zellen = [c.strip() for c in z.strip('|').split(' | ')]
        if len(zellen) < 8:
            continue
        pfad = zellen[7].rstrip('/')
        eintraege[pfad] = {'prompt': zellen[2], 'katalog': zellen[5]}
    return stand, eintraege


def katalognamen(zelle, ordner):
    namen = re.findall(r'([a-z0-9-]+)\.md', zelle)
    quelle = 'Register'
    if zelle.rstrip().endswith(' und'):
        prot = ordner / 'src' / 'protokoll.txt'
        if prot.exists():
            zeilen = prot.read_text(encoding='utf-8', errors='replace').split('\n')
            for i, z in enumerate(zeilen):
                if z.startswith('Katalog:'):
                    block = [z] + [y for y in zeilen[i + 1:i + 6] if y.startswith(' ')]
                    namen = re.findall(r'([a-z0-9-]+)\.md', ' '.join(block))
                    quelle = 'Register (Zelle endet auf „und“) + src/protokoll.txt'
                    break
    return list(dict.fromkeys(namen)), quelle


def version(prompt):
    m = re.search(r'v\d+(\.\d+)*', prompt)
    return m.group(0) if m else prompt


# ---------------------------------------------------------------- Messen

def messe(pdf, ordner, reg, testlauf=None):
    """testlauf: None oder {'src', 'thema', 'datum', 'eintrag', 'tex'} aus testlauf_blaetter()."""
    if testlauf:
        thema, datum, src = testlauf['thema'], testlauf['datum'], testlauf['src']
        r = testlauf['eintrag']
        tex_pfad = testlauf['tex']
    else:
        thema, datum, src = ordner.parent.name, ordner.name, ordner / 'src'
        schluessel = f'blaetter/{thema}/{datum}'
        r = reg.get(schluessel, {'prompt': '?', 'katalog': ''})
        texdateien = {p.stem.lower(): p for p in src.glob('*.tex')}
        tex_pfad = texdateien.get(pdf.stem.lower())
    k = {'thema': thema, 'datum': datum, 'datei': pdf.name, 'prompt': version(r['prompt']),
         'tex': tex_pfad.name if tex_pfad else None, 'seiten': pdf_seiten(pdf)}
    if testlauf:
        k['texort'] = ''
    if not tex_pfad:
        k['fehlt_tex'] = True
        return k
    tex = lies_tex(tex_pfad)
    eigene = eigene_makros(tex, src)
    hns, kaesten, koepfe, begleit = zerlege(tex)
    seiten_text = pdf_text(pdf)
    k['hauptnummern'] = hns
    k['koepfe'] = koepfe

    # Aufgabenseiten
    aufgabenseiten = len(seiten_text)
    if begleit:
        for i, s in enumerate(seiten_text):
            if re.search(r'(?m)^\s*Ergebnisse\s*$', s):
                aufgabenseiten = i
                break
    k['aufgabenseiten'] = aufgabenseiten

    # je Hauptnummer
    seite, offset = 0, 0
    for h in hns:
        h['titel'] = re.sub(r'\.$', '', zu_text(erster_satz(h['arg'])).rstrip())
        h['form'] = titelform(h['titel'])
        h['teil'] = teilaufgaben(h['rumpf'])
        h['darst'] = darstellungen(h['rumpf'])
        h['antwort'] = antwortform(h['rumpf'], eigene)
        h['text'] = zu_text(h['arg'] + ' ' + h['rumpf'])
        h['woerter'] = [w.lower() for w in woerter(h['text'])]
        anfang = norm(h['titel'])[:10]
        gefunden = None
        for versuch in (True, False):
            p, o = seite, offset
            while p < len(seiten_text) and gefunden is None:
                for m in re.finditer(r'(?m)^\s*' + str(h['nr']) + r'\.\s+(.*)$', seiten_text[p][o:]):
                    if not versuch or norm(m.group(1)).startswith(anfang):
                        gefunden = (p, o + m.end())
                        break
                p, o = p + 1, 0
            if gefunden:
                break
        if gefunden:
            h['seite'] = gefunden[0] + 1
            seite, offset = gefunden
        else:
            h['seite'] = None

    # Merkkästen
    pos_hn = [h['pos'] for h in hns]
    k['kaesten'] = []
    for pos in kaesten:
        if not pos_hn or pos < min(pos_hn):
            k['kaesten'].append('vor den Aufgaben')
        elif pos > max(pos_hn):
            k['kaesten'].append('nach den Aufgaben')
        else:
            vor = max(h['nr'] for h in hns if h['pos'] < pos)
            k['kaesten'].append(f'zwischen den Aufgaben (nach Nr. {vor})')

    # Katalog
    if 'namen' in r:
        namen, quelle = r['namen'], 'protokoll.txt des Testlaufordners'
    else:
        namen, quelle = katalognamen(r['katalog'], ordner)
    k['katalog'] = namen
    k['katalogquelle'] = quelle
    k['fachwoerter'] = []
    k['typen'] = []
    for name in namen:
        pfad = KATALOG / f'{name}.md'
        if not pfad.exists():
            k['fachwoerter'].append((name, None, 'Eintrag fehlt', None, None))
            continue
        et = pfad.read_text(encoding='utf-8')
        begriffe, art = fachwoerter(et)
        for b, einheit in begriffe:
            erst = next((h['nr'] for h in hns if folge_treffer(b, h['woerter'])), None)
            k['fachwoerter'].append((name, b, art, erst, einheit))
        einheiten = lerneinheiten(et)
        gebaut = set()
        for kopf in koepfe:
            rest = ICH_FORM.sub('', kopf.split('·')[-1].strip())
            rest_st = [stamm(w) for w in kernwoerter(rest)]
            rest_w = [w.lower() for w in woerter(rest)]
            for n, titel in einheiten.items():
                t_st = [stamm(w) for w in kernwoerter(titel)]
                t_w = [w.lower() for w in woerter(titel)]
                if not t_st or not rest_st:
                    continue
                gemeinsam = max(len(hat_staemme(t_st, rest_w)), len(hat_staemme(rest_st, t_w)))
                if gemeinsam * 3 >= 2 * max(len(t_st), len(rest_st)):
                    gebaut.add(n)
                    k.setdefault('kopftreffer', {}).setdefault(kopf, []).append(f'{name} {n}')
        for n, liste in sorted(typen(et).items()):
            for typ, sek2 in liste:
                paare = kernstaemme(typ)
                if not paare:
                    k['typen'].append((name, n, n in gebaut, typ, 'nicht prüfbar', None, [], sek2))
                    continue
                st = [s for _, s in paare]
                bester, bestnr, fehlt = 0, None, [w for w, _ in paare]
                for h in hns:
                    da = hat_staemme(st, h['woerter'])
                    if len(da) > bester:
                        bester, bestnr = len(da), h['nr']
                        fehlt = [w for w, s in paare if s not in da]
                if bester == len(st):
                    urteil = 'Treffer'
                elif bester > 0:
                    urteil = 'Teiltreffer'
                else:
                    urteil = 'kein Treffer'
                k['typen'].append((name, n, n in gebaut, typ, urteil, bestnr, fehlt, sek2))
        k.setdefault('gebaut', {})[name] = sorted(gebaut)
    k['nur_blatt0'] = (not any(k.get('gebaut', {}).values())
                       and bool(re.search(r'Blatt 0', tex)))
    k['stufe5'] = stufe5(tex, koepfe)
    return k


def stufe5(tex, koepfe):
    """Bausteine der Vorlage Stufe 5 (v0.3): Zweigzeilen, Abhakseite, Verzeichniszeile, Schwach-Teilaufgaben.
    None, wenn das Blatt keinen davon trägt (dann bleibt die Ausgabe wie in v0.2)."""
    zweig = len(re.findall(r'\\' + ZWEIGZEILE + r'(?![A-Za-z])', tex))
    abhakseite = bool(re.search(r'\\begin\{' + ABHAKSEITE[0] + r'\}', tex))
    abhak = len(re.findall(r'\\' + ABHAKSEITE[1] + r'(?![A-Za-z])', tex))
    verzzeile = len(re.findall(r'\\' + VERZEICHNIS[0] + r'(?![A-Za-z])', tex))
    verz = len(re.findall(r'\\' + VERZEICHNIS[1] + r'(?![A-Za-z])', tex))
    sw = len(re.findall(r'\\swfrage(?![A-Za-z])', tex))
    if not (zweig or abhakseite or abhak or verzzeile or verz or sw):
        return None
    # Einheitenkopf = Kopf mit Blattnummer „Einheit n …“ oder Mittelpunkt; Köpfe wie „Inhalt“, „Das kennst du
    # schon“ (Zone) oder „Das kann ich“ (Abhakseite) stehen getrennt
    einheitenkoepfe = [kp for kp in koepfe if kp.strip() not in KEIN_EINHEITENKOPF
                       and (re.search(r'\bEinheit\s+\d', kp) or '·' in kp)]
    weitere = [kp for kp in koepfe if kp not in einheitenkoepfe]
    return {'koepfe': len(einheitenkoepfe), 'zweig': zweig, 'abhakseite': abhakseite, 'abhak': abhak,
            'verzzeile': verzzeile, 'verz': verz, 'swfrage': sw, 'kopfliste': einheitenkoepfe,
            'weitere': list(dict.fromkeys(weitere))}


# ---------------------------------------------------------------- Ausgabe

def je_seite(k, feld):
    werte = [0] * k['aufgabenseiten']
    for h in k['hauptnummern']:
        if h['seite'] and h['seite'] <= len(werte):
            werte[h['seite'] - 1] += 1 if feld == 'hn' else h['teil']
    return ' · '.join(str(w) for w in werte)


def zusammen(k):
    hns = k.get('hauptnummern', [])
    if k.get('fehlt_tex'):
        return None
    if not hns:
        return {'hn': '–', 'ta': '–', 'hns': '–', 'tas': '–', 'form': '–', 'letzte': '–', 'ohne': '–'}
    formen = {}
    for h in hns:
        formen[h['form']] = formen.get(h['form'], 0) + 1
    form = ' · '.join(f'{f} {formen.get(f, 0)}' for f in ['Kurzname – Formwort', 'Ich kann', 'anderes'])
    mit = [h for h in hns if h['darst']]
    letzte = f"Nr. {mit[-1]['nr']} ({', '.join(k2 for k2 in KATEGORIEN if k2 in mit[-1]['darst'])})" if mit else 'keine'
    gezaehlt = [t for t in k['typen'] if (t[2] or not any(k['gebaut'].values()))
                and t[4] != 'nicht prüfbar' and not t[7]]
    if k['nur_blatt0']:
        ohne = '– (nur Blatt 0)'
    elif not k['typen']:
        ohne = '–'
    else:
        ohne_n = sum(1 for t in gezaehlt if t[4] != 'Treffer')
        bezug = 'gebaute Einheiten' if any(k['gebaut'].values()) else 'alle Einheiten'
        ohne = f'{ohne_n} von {len(gezaehlt)} ({bezug})'
    return {'hn': str(len(hns)), 'ta': str(sum(h['teil'] for h in hns)),
            'hns': je_seite(k, 'hn'), 'tas': je_seite(k, 'ta'), 'form': form,
            'letzte': letzte, 'ohne': ohne}


def abschnitt_md(k):
    z = abschnitt_md_basis(k)
    s5 = k.get('stufe5')
    if not s5:
        return z
    # v0.3: Kennzahlen 10–12 nur für Blätter mit Bausteinen der Vorlage Stufe 5 (ältere Blätter unverändert)
    if z and z[-1] == '':
        z = z[:-1]
    z.append(f"10. Zweigzeilen je Einheitenkopf: Einheitenköpfe {s5['koepfe']} · Zweigzeilen {s5['zweig']}"
             + (f"; Schwach-Teilaufgaben (\\swfrage): {s5['swfrage']}" if s5['swfrage'] else '') + '.')
    z.append(f"11. Abhakseite: {'ja' if s5['abhakseite'] else 'nein'}"
             + (f", {s5['abhak']} Zeilen (\\abhak)" if s5['abhak'] else '') + '.')
    z.append(f"12. Verzeichniszeile: {'ja' if s5['verzzeile'] or s5['verz'] else 'nein'}"
             + (f", {s5['verz']} Einträge (\\verz)" if s5['verz'] else '') + '.')
    treffer = k.get('kopftreffer', {})
    if s5['kopfliste']:
        teile = []
        for kp in s5['kopfliste']:
            ziel = treffer.get(kp)
            teile.append(f"„{kp}“ → " + (', '.join(f'Einheit {x}' for x in dict.fromkeys(ziel)) if ziel
                                          else 'ohne Treffer'))
        z.append('Einheitenkopf → Lerneinheit (Titel gegen Titel, Wortstamm; die Blattnummer zählt nicht): '
                 + '; '.join(dict.fromkeys(teile)) + '.')
        if not any(k.get('gebaut', {}).values()):
            z.append('Vermerk: kein Einheitenkopf trifft eine Lerneinheit – Kennzahl 9 zählt gegen alle Einheiten.')
    if s5['weitere']:
        z.append('Weitere Köpfe (keine Einheit): ' + '; '.join(f'„{kp}“' for kp in s5['weitere']) + '.')
    z.append('')
    return z


def abschnitt_md_basis(k):
    z = [f"### {k['thema']} · {k['datum']} · {k['datei']}", '']
    if k.get('fehlt_tex'):
        z += [f"Keine gleichnamige tex-Datei unter src/; gemessen nur die Seiten: {k['seiten']}.", '']
        return z
    hns = k['hauptnummern']
    z.append(f"Quelltext: {k.get('texort', 'src/')}{k['tex']} (mit \\input) · Prompt {k['prompt']} · "
             f"Katalog: {', '.join(n + '.md' for n in k['katalog']) or '–'} ({k['katalogquelle']})")
    z.append('')
    art = 'Aufgaben' if hns else 'Ergebnisse (keine Hauptnummer)'
    z.append(f"1. Seiten: {k['seiten']} (Aufgabenseiten {k['aufgabenseiten']}; {art}).")
    if not hns:
        z += ['2.–9. entfallen: die Datei enthält keine Hauptnummer.', '']
        return z
    z.append(f"2. Hauptnummern: {len(hns)}; Teilaufgaben: {sum(h['teil'] for h in hns)}.")
    z.append(f"3. Hauptnummern je Seite: {je_seite(k, 'hn')}; Teilaufgaben je Seite: {je_seite(k, 'ta')}"
             + (' (Hauptnummer ohne Seitenfund: ' + ', '.join(str(h['nr']) for h in hns if not h['seite']) + ')'
                if any(not h['seite'] for h in hns) else '') + '.')
    z.append('4.–6. je Hauptnummer:')
    z.append('')
    z.append('| Nr. | Seite | Teilaufg. | Titel | Form | Darstellungen | Antwortform |')
    z.append('|---|---|---|---|---|---|---|')
    for h in hns:
        d = ' · '.join(f"{kat} ({', '.join(h['darst'][kat])})" for kat in KATEGORIEN if kat in h['darst']) or '–'
        z.append(f"| {h['nr']} | {h['seite'] or '?'} | {h['teil']} | {h['titel'].replace('|', '/')} "
                 f"| {h['form']} | {d} | {h['antwort']} |")
    z.append('')
    mit = [h for h in hns if h['darst']]
    if mit:
        letzte = {kat: max(h['nr'] for h in hns if kat in h['darst']) for kat in KATEGORIEN
                  if any(kat in h['darst'] for h in hns)}
        z.append(f"5. Letzte Hauptnummer mit Darstellung: Nr. {mit[-1]['nr']}; je Kategorie: "
                 + ', '.join(f'{kat} Nr. {n}' for kat, n in letzte.items()) + '.')
    else:
        z.append('5. Letzte Hauptnummer mit Darstellung: keine.')
    if k['kaesten']:
        z.append(f"7. Merkkästen: {len(k['kaesten'])} – " + '; '.join(k['kaesten']) + '.')
    else:
        z.append('7. Merkkästen: 0.')
    if k['fachwoerter']:
        art = k['fachwoerter'][0][2]
        z.append(f"8. Fachwörter ({art}) und erstes Auftreten:")
        z.append('')
        z.append('| Eintrag | Kasten der Einheit | Begriff | erste Hauptnummer |')
        z.append('|---|---|---|---|')
        for name, b, a, erst, einheit in k['fachwoerter']:
            z.append(f"| {name} | {einheit or '–'} | {b if b else a} | {('Nr. ' + str(erst)) if erst else '–'} |")
        z.append('')
    else:
        z.append('8. Fachwörter: keine gefunden.')
    if k['nur_blatt0']:
        z += ['9. Sprossenabgleich: entfällt – die Datei trägt nur Blatt 0 (keine Lerneinheit erkannt).', '']
        return z
    z.append('9. Sprossenabgleich (Typen je Lerneinheit):')
    z.append('')
    for name in k['katalog']:
        gruppen = {}
        for t in k['typen']:
            if t[0] == name:
                gruppen.setdefault((t[1], t[2]), []).append(t)
        for (n, geb), liste in sorted(gruppen.items()):
            def marke(t):
                return '[Sek II] ' if t[7] else ''
            treffer = [f"{marke(t)}{t[3]} (Nr. {t[5]})" for t in liste if t[4] == 'Treffer']
            teil = [f"{marke(t)}{t[3]} (Nr. {t[5]}; fehlt: {', '.join(t[6])})"
                    for t in liste if t[4] == 'Teiltreffer']
            kein = [marke(t) + t[3] for t in liste if t[4] == 'kein Treffer']
            np = [marke(t) + t[3] for t in liste if t[4] == 'nicht prüfbar']
            zeile = f"- {name}, Einheit {n} ({'gebaut' if geb else 'nicht gebaut'}): "
            stuecke = []
            if treffer:
                stuecke.append('Treffer: ' + '; '.join(treffer))
            if teil:
                stuecke.append('Teiltreffer: ' + '; '.join(teil))
            if kein:
                stuecke.append('kein Treffer: ' + '; '.join(kein))
            if np:
                stuecke.append('nicht prüfbar: ' + '; '.join(np))
            z.append(zeile + ' – '.join(stuecke) + '.')
    s = zusammen(k)
    z.append('')
    z.append(f"Typen ohne Treffer: {s['ohne']}.")
    z.append('')
    return z


def alle_blaetter():
    ordner = sorted(p for p in BLAETTER.glob('*/*') if p.is_dir() and (p / 'pdf').is_dir())
    paare = []
    for o in ordner:
        for pdf in sorted((o / 'pdf').glob('*.pdf'), key=lambda p: p.name.lower()):
            paare.append((pdf, o))
    return paare


def testlauf_protokoll(ordner):
    """Prompt-Zeile und Katalognamen aus protokoll.txt eines Testlauf-Unterordners."""
    prot = ordner / 'protokoll.txt'
    prompt, namen = '?', []
    if not prot.exists():
        return {'prompt': prompt, 'katalog': '', 'namen': namen}
    zeilen = prot.read_text(encoding='utf-8', errors='replace').split('\n')
    for z in zeilen:
        if z.startswith('Prompt:') and prompt == '?':
            prompt = z.split(':', 1)[1].strip()
        m = re.match(r'Katalog:\s*([a-z0-9-]+)(\.md)?', z)
        if m and (m.group(2) or (KATALOG / f'{m.group(1)}.md').exists()):
            namen.append(m.group(1))
    return {'prompt': prompt, 'katalog': '', 'namen': list(dict.fromkeys(namen))}


def testlauf_tex(pdf, ordner):
    tex = {p.stem.lower(): p for p in ordner.glob('*.tex')}
    stamm_pdf = pdf.stem.lower()
    if stamm_pdf in tex:
        return tex[stamm_pdf]
    wort = stamm_pdf.rsplit('_', 1)[-1]
    if 'fokus' in stamm_pdf and 'fokus' not in tex:
        wort = 'fokus'
    for s, p in sorted(tex.items()):
        if s == wort or (wort == 'fokus' and s.startswith('fokus') and not s.endswith(('_a', '_l'))
                         and 'loesung' not in s):
            return p
    blatt = 'Fokus' if 'fokus' in stamm_pdf else pdf.stem.rsplit('_', 1)[-1]
    for s, p in sorted(tex.items()):
        inhalt = p.read_text(encoding='utf-8', errors='replace')
        if re.search(r'\\blattkopf\{[^}]*\}\{' + re.escape(blatt), inhalt):
            return p
    return None


def testlauf_blaetter(wurzel):
    """[(pdf, ordner, testlauf-Angaben)] für alle Gesamt- und Fokus-PDFs eines Testlaufordners."""
    def nr(p):
        m = re.match(r'(\d+)', p.name)
        return (int(m.group(1)) if m else 10 ** 6, p.name)
    tripel = []
    for o in sorted((p for p in wurzel.iterdir() if p.is_dir()), key=nr):
        eintrag = testlauf_protokoll(o)
        for pdf in sorted(o.glob('*.pdf'), key=lambda p: p.name.lower()):
            if re.search(r'_(Gesamt|Fokus)', pdf.name) and 'Loesungen' not in pdf.name:
                tripel.append((pdf, o, {'src': o, 'thema': o.name, 'datum': wurzel.name,
                                        'eintrag': eintrag, 'tex': testlauf_tex(pdf, o)}))
    return tripel


def baue(paare, reg, stand, testlauf=False):
    if testlauf:
        messungen = [messe(pdf, o, reg, t) for pdf, o, t in paare]
    else:
        messungen = [messe(pdf, o, reg) for pdf, o in paare]
    herkunft = ('Testlauf: Prompt und Katalog je Ordner aus protokoll.txt' if testlauf
                else f'Register: blaetter/index.md ({stand})')
    z = ['# Blätter – Kennzahlen je Blatt',
         'Abgeleitet von `werkzeuge/blatt-pruef.py`, nie von Hand ändern.',
         f'{herkunft}; {len(messungen)} PDF-Dateien in '
         f'{len({(m["thema"], m["datum"]) for m in messungen})} Blattordnern. Lesarten im Skriptkopf.',
         '',
         '## Vergleichstabelle',
         '',
         '| Thema | Datum | Prompt | Datei | Seiten | Hauptnummern | Teilaufgaben | Hauptnummern je Seite '
         '| Teilaufgaben je Seite | Titelform | letzte Darstellung | Typen ohne Treffer |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for k in messungen:
        s = zusammen(k)
        if s is None:
            z.append(f"| {k['thema']} | {k['datum']} | {k['prompt']} | {k['datei']} (ohne tex) | {k['seiten']} "
                     '| – | – | – | – | – | – | – |')
            continue
        datei = k['datei'] + ('' if k['hauptnummern'] else ' (Ergebnisse)')
        z.append(f"| {k['thema']} | {k['datum']} | {k['prompt']} | {datei} | {k['seiten']} | {s['hn']} "
                 f"| {s['ta']} | {s['hns']} | {s['tas']} | {s['form']} | {s['letzte']} | {s['ohne']} |")
    z += ['', '## Je Blatt', '']
    for k in messungen:
        z += abschnitt_md(k)
    return '\n'.join(z).rstrip('\n') + '\n', messungen


def main():
    stand, reg = register()
    argv = sys.argv[1:]
    ausgabe = AUSGABE
    if '--ausgabe' in argv:
        i = argv.index('--ausgabe')
        ausgabe = Path(argv[i + 1]).resolve()
        del argv[i:i + 2]
    if '--testlauf' in argv:
        i = argv.index('--testlauf')
        wurzel = Path(argv[i + 1]).resolve()
        tripel = testlauf_blaetter(wurzel)
        if not tripel:
            sys.exit(f'kein Gesamt- oder Fokus-PDF unter {wurzel}')
        text, messungen = baue(tripel, reg, stand, testlauf=True)
        with open(ausgabe, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print(f'{ausgabe} geschrieben: {len(messungen)} PDF-Dateien.')
        return
    if argv:
        ziel = Path(argv[0]).resolve()
        if ziel.is_file():
            paare = [(ziel, ziel.parent.parent)]
        else:
            paare = [(p, ziel) for p in sorted((ziel / 'pdf').glob('*.pdf'), key=lambda p: p.name.lower())]
        if not paare:
            sys.exit(f'kein Blatt unter {ziel}')
        for pdf, o in paare:
            print('\n'.join(abschnitt_md(messe(pdf, o, reg))))
        return
    text, messungen = baue(alle_blaetter(), reg, stand)
    with open(ausgabe, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print(f'{ausgabe} geschrieben: {len(messungen)} PDF-Dateien.')


if __name__ == '__main__':
    main()
