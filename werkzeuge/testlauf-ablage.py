#!/usr/bin/env python3
r"""testlauf-ablage.py – Ergebnis einer Blattsitzung im Testlaufordner ablegen (v0.1, 25.09.2026)

Auftrag: archiv/auftrag-testlauf-<datum>.md, Teil 2 Schritt 2–3 und 5.

  python werkzeuge/testlauf-ablage.py <arbeitsordner der sitzung> <blaetter/testlauf-<datum>/<nr>-<kurzname>>

Kopiert alle PDFs aus dem Arbeitsordner in den Zielordner und entpackt dort das
Protokoll-Archiv (*_protokoll.zip; Unterordner des Archivs bleiben erhalten). Das Zip selbst
kommt nicht ins Repo: .gitattributes behandelt *.zip als Text (eol=lf), ein eingechecktes
Archiv wäre danach kaputt; es bleibt im Arbeitsordner. Fehlt das
Archiv, bleibt, was da ist; Hilfsdateien der Sitzung (Renderbilder, .aux, Textauszüge)
werden nicht übernommen. sitzung.txt schreibt die Auftragssitzung selbst.

Danach die Prüfung aus Teil 2 Schritt 3 und die Zählung aus Schritt 5, auf der Konsole:
  PDF Gesamt/Fokus   mindestens ein PDF mit „Gesamt“ oder „Fokus“ im Namen
  Prompt-Zeile       protokoll.txt enthält die Zeile „Prompt: Unterrichtsblatt-Prompt v4.3“
  Werkzeugaufrufe    höchste Schrittnummer im Abschnitt „Werkzeugaufrufe“ oder „Schritte“ (auch
                     „… (Schritt · Anlass)“) von protokoll.txt (Zeilen „n. …“, „n …“, „n.–m. …“,
                     „n–m …“ bis zur nächsten Leerzeile); ersatzweise m aus „Korrekturrunden: k von m
                     Schritten“; über 60 = Befund
Ergebnis „fertig“, wenn beide Prüfungen bestehen, sonst „offen“ mit Grund.
"""

import re
import shutil
import sys
import zipfile
from pathlib import Path

PROMPTZEILE = 'Prompt: Unterrichtsblatt-Prompt v4.3'


def werkzeugaufrufe(prot):
    if not prot.exists():
        return None
    zeilen = prot.read_text(encoding='utf-8', errors='replace').split('\n')
    hoechst, drin = None, False
    for z in zeilen:
        if z.startswith(('Werkzeugaufrufe', 'Schritte')) or '(Schritt · Anlass)' in z:
            drin = True
            continue
        if drin:
            if not z.strip():
                if hoechst is not None:
                    break
                continue
            m = re.match(r'^\s*(\d+)\.?(?:\s*[–-]\s*(\d+)\.?)?\s', z)
            if m:
                n = int(m.group(2) or m.group(1))
                hoechst = n if hoechst is None else max(hoechst, n)
    if hoechst is None:
        for z in zeilen:
            m = re.match(r'^Korrekturrunden:\s*\d+\s+von\s+(\d+)', z)
            if m:
                return int(m.group(1))
    return hoechst


def pruefe(ziel):
    pdfs = sorted(p.name for p in ziel.rglob('*.pdf'))
    blatt = [p for p in pdfs if 'gesamt' in p.lower() or 'fokus' in p.lower()]
    prots = sorted(ziel.rglob('protokoll.txt'))
    prot = prots[0] if prots else ziel / 'protokoll.txt'
    zeile = prot.exists() and any(z.strip() == PROMPTZEILE
                                  for z in prot.read_text(encoding='utf-8', errors='replace').split('\n'))
    gruende = []
    if not blatt:
        gruende.append('kein PDF mit „Gesamt“ oder „Fokus“ im Namen')
    if not prot.exists():
        gruende.append('protokoll.txt fehlt')
    elif not zeile:
        gruende.append(f'protokoll.txt ohne Zeile „{PROMPTZEILE}“')
    return pdfs, blatt, prot, gruende


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    quelle, ziel = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    ziel.mkdir(parents=True, exist_ok=True)
    for pdf in sorted(quelle.glob('*.pdf')):
        shutil.copy2(pdf, ziel / pdf.name)
    archive = sorted(quelle.glob('*_protokoll.zip'))
    for zp in archive:
        with zipfile.ZipFile(zp) as z:
            z.extractall(ziel)
    pdfs, blatt, prot, gruende = pruefe(ziel)
    aufrufe = werkzeugaufrufe(prot)
    print(f'Archiv: {", ".join(a.name for a in archive) or "fehlt"}')
    print(f'PDFs: {", ".join(pdfs) or "keine"}')
    print(f'Gesamt/Fokus: {", ".join(blatt) or "keins"}')
    print(f'protokoll.txt: {prot.relative_to(ziel) if prot.exists() else "fehlt"}')
    print(f'Werkzeugaufrufe laut protokoll.txt: {aufrufe if aufrufe is not None else "nicht gezählt"}'
          + (' – über 60 (Befund)' if aufrufe and aufrufe > 60 else ''))
    print('Ergebnis: ' + ('fertig' if not gruende else 'offen – ' + '; '.join(gruende)))


if __name__ == '__main__':
    main()
