from pypdf import PdfReader
r = PdfReader("LinFkt_Lernblatt.pdf")
pg = {p.indirect_reference.idnum: i+1 for i, p in enumerate(r.pages)}
dests = {}
for name, d in r.named_destinations.items():
    try:
        dests[name] = pg.get(d.page.idnum if hasattr(d.page, 'idnum') else d.page.indirect_reference.idnum)
    except Exception as e:
        dests[name] = str(e)
for a in r.pages[0].get('/Annots', []):
    o = a.get_object()
    act = o.get('/A')
    if act is not None:
        d = act.get_object().get('/D')
        print('Link ->', d, '-> Seite', dests.get(str(d)))
    elif o.get('/Dest') is not None:
        print('Dest', o.get('/Dest'), dests.get(str(o.get('/Dest'))))
