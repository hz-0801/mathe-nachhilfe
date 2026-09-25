# links.py – prüft, auf welche Seite jeder Verzeichnislink der ersten Seite zeigt
import sys
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
seite_von = {p.indirect_reference.idnum: i + 1 for i, p in enumerate(r.pages)}
dests = {}
for name, d in r.named_destinations.items():
    dests[name] = seite_von.get(d.page.idnum if hasattr(d.page, 'idnum') else d.page.indirect_reference.idnum)
p1 = r.pages[0]
for a in p1.get('/Annots', []) or []:
    a = a.get_object()
    ziel = a.get('/Dest') or (a.get('/A') or {}).get('/D')
    print(f"Link -> {ziel} -> Seite {dests.get(str(ziel))}")
