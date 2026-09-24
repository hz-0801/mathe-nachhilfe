# dnb-sru.py – Suche in der Deutschen Nationalbibliothek (SRU) und
# Liste der Treffer mit ISBN, Jahr, Titel und Inhaltsverzeichnis-Link.
# Aufruf: python dnb-sru.py '<CQL-Abfrage>'
# Beispiele: 'tit="Fundamente der Mathematik" and jhr=2025'
#            'num=9783060428175'
# Ausgabe je Treffer: IDN | Jahr | ISBN | Titel | TOC:ja/-
# TOC-PDF: https://d-nb.info/<IDN>/04
import sys, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

q = sys.argv[1]
url = ("https://services.dnb.de/sru/dnb?version=1.1"
       "&operation=searchRetrieve&recordSchema=MARC21-xml"
       "&maximumRecords=100&query=" + urllib.parse.quote(q))
x = urllib.request.urlopen(url, timeout=60).read()
ns = {'m': 'http://www.loc.gov/MARC21/slim',
      's': 'http://www.loc.gov/zing/srw/'}
root = ET.fromstring(x)
print('###', q, '| Treffer:',
      root.findtext('.//s:numberOfRecords', namespaces=ns))
for rec in root.findall('.//m:record', ns):
    def f(tag, code):
        return [sf.text or '' for df in
                rec.findall(f"m:datafield[@tag='{tag}']", ns)
                for sf in df.findall(f"m:subfield[@code='{code}']", ns)]
    idn = rec.findtext("m:controlfield[@tag='001']", namespaces=ns)
    title = ' '.join(f('245', 'a') + f('245', 'b') + f('245', 'n')
                     + f('245', 'p') + f('490', 'a'))
    isbn = f('020', 'a')
    year = f('264', 'c')
    toc = [u for u in f('856', 'u') if u.endswith('/04')]
    print(f" {idn} | {year[:1]} | {isbn[:1]} | {title[:120]} | "
          f"TOC:{'ja' if toc else '-'}")
