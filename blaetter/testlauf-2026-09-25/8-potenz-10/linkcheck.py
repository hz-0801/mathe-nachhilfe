import pypdf, sys
for f in ['PotenzExponentialFkt_Lernblatt.pdf', 'PotenzExponentialFkt_Gesamt.pdf']:
    r = pypdf.PdfReader(f)
    ziele = {}
    for name, d in r.named_destinations.items():
        ziele[name] = r.get_destination_page_number(d) + 1
    p = r.pages[0]
    links = []
    for a in p.get('/Annots', []) or []:
        a = a.get_object()
        if a.get('/Subtype') == '/Link':
            d = a.get('/Dest') or (a.get('/A') or {}).get('/D')
            links.append(str(d))
    print(f, 'Links S.1:', [(l, ziele.get(l)) for l in links])
