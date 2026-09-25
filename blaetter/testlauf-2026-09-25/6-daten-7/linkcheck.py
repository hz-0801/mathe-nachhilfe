from pypdf import PdfReader
import re
for f in ["Daten_Lernblatt.pdf", "Daten_Gesamt.pdf"]:
    r = PdfReader(f)
    dests = {}
    for name, d in r.named_destinations.items():
        dests[name] = r.get_destination_page_number(d) + 1
    p0 = r.pages[0]
    out = []
    for a in p0.get("/Annots", []):
        a = a.get_object()
        if a.get("/Subtype") == "/Link":
            d = a.get("/Dest") or (a.get("/A") or {}).get("/D")
            out.append((str(d), dests.get(str(d))))
    print(f, out)