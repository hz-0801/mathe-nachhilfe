#!/usr/bin/env python3
"""Zuordnung der Unterkapitel aus sa-roh.csv zu Katalogeintraegen (Sek I).
Regeln: REGELN (Titel-Stichwort -> Eintrag, Einheit nach Unterregeln),
erste passende Regel gewinnt. Wege:
  titel    - Titel trifft eine Regel
  kapitel  - Unterkapitel ohne Treffer, Mehrheitseintrag seines Kapitels
  rahmen   - Kapitelrahmen (Oeffner, Vermischtes, Zusammenfassung, Test,
             Streifzug ohne Treffer) -> Eintrag des naechsten Unterkapitels
             (Oeffner: folgendes, sonst vorangehendes) im selben Band
  kein     - ausdruecklich kein Katalogeintrag (KEIN) oder nichts gefunden
Ausgaben: sa-zuordnung.csv (je Zeile), sa-seiten.csv, sa-seiten.md."""
import csv, re, collections

KEIN_STARK = r'taschenrechner|systematisches probieren|rückwärts|logik|algorithm|folgen|bewerbung|aufgabenpraktikum|knobel|mindmap|präsentier|partnerarbeit|gruppenarbeit|ich-du-wir|einem text|symbole|vorwort|digitale|geometrie-software|^themen$|tabellenkalkulation$|ta bellen kalkulation'
SEK2 = r'sekante|differenzenquotient|ableitung|änderungsrate|differentialrechnung|polynomdivision|globalverhalten|extrem.*wendepunkt|ganzrational|wendepunkt'
KEIN = r'taschenrechner|problem|probier|rückwärts|schätzen|schätz|logik|algorithm|folgen|beruf|alltag|aufgabenpraktikum|mathematik in|knobel|lernen lernen|methoden|präsentier|mindmap|wiederhol.*grundschul|partnerarbeit|gruppenarbeit|ich-du-wir|einem text|symbole|computer(?!.*(zins|funktion|term|daten|statist|pythag|kredit))'

# (eintrag, muster, [(untermuster, einheit), ...])
REGELN = [
    ('trigonometrische-funktionen', r'sinusfunktion|kosinusfunktion|bogenmaß|bogenmass|einheitskreis|periodisch|trigonometrische funktion|sinuskurve|sinus- und kosinusfunktion|winkel am einheitskreis',
     [(r'einheitskreis|bogenma', '1'), (r'parameter|streck|verschieb|y ?= ?a', '3'), (r'periodisch|modell', '4'), (r'funktion|kurve', '2')]),
    ('trigonometrie', r'sinus|kosinus|tangens|trigonometr|steigungswinkel',
     [(r'sinussatz|kosinussatz|beliebige', '4'), (r'figur|anwend|sach|berechnungen an|vermessung|körper', '3'), (r'winkel', '2'), (r'.', '1')]),
    ('pythagoras', r'pythagoras|hypotenuse|kathete|höhensatz|satzgruppe|pythagoreisch|knotenseil',
     [(r'umkehr|kathete', '2'), (r'anwend|sach|körper|figur|raum|ebene', '3'), (r'.', '1')]),
    ('quadratische-gleichungen', r'quadratische gleichung|p-?q-formel|pq-formel|lösungsformel|nullprodukt|vieta|quadratische ergänzung|mitternacht|diskriminante|reinquadratisch|gemischtquadratisch',
     [(r'nullprodukt|vieta|faktor', '3'), (r'p-?q|lösungsformel|ergänzung|normalform|mitternacht|diskrim|gemischt', '2'), (r'sach|anwend', '4'), (r'.', '1')]),
    ('quadratische-funktionen', r'quadratische funktion|parabel|scheitel|faktorisierte form|allgemeine form|optimierung|quadratische zusammenh|quadratische zuordn',
     [(r'scheitel|verschieb', '2'), (r'normalform|allgemeine', '3'), (r'nullstell|schnittpunkt|schnitt', '4'), (r'.', '1')]),
    ('zinsrechnung', r'zins|kredit|sparen|girokonto|ratenkauf|tilgung|sparplan|geld leihen',
     [(r'zinseszins|sparplan|mehrere jahre|tilgung|kredit', '2'), (r'.', '1')]),
    ('potenz-exponentialfunktionen', r'exponential|exponentiell|wachstum|zerfall|halbwert|verdopplung|potenzfunktion|logarithm|abnahme(prozesse|vorgänge)',
     [(r'lineares und exponentielles|linear.*exponent|vergleich', '1'), (r'potenzfunktion', '5'), (r'halbwert|verdopp', '4'), (r'faktor|tabelle', '2'), (r'.', '3')]),
    ('lineare-gleichungssysteme', r'gleichungssystem|lgs|gleichsetz|einsetzungs|einsetzverf|additionsverfahren|zwei variablen|zwei unbekannten|drei variablen|zwei gleichungen',
     [(r'drei', '5'), (r'addition', '3'), (r'einsetz|gleichsetz', '2'), (r'sach|anwend', '4'), (r'.', '1')]),
    ('binomische-formeln', r'binomisch|summen multipl|multiplikation von summen|multiplizieren von summen|summe mal summe|faktorisieren|produkte von summen|multiplikation zweier summen',
     [(r'binomisch', '2'), (r'faktoris', '3'), (r'.', '1')]),
    ('reelle-zahlen', r'näherungswert|irrational|reelle|zahlbereich|zahlenbereich|intervallschachtel|potenzgesetz|wurzelgesetz|rationale exponent|n-te wurzel|rechnen mit wurzeln|rechnen mit potenzen|wurzelterm|potenzen mit (negativ|ganz|rational)|näherungsverfahren|heron',
     [(r'näherungsw|irrational|reell|bereich|intervall|näherung|heron', '1'), (r'wurzel|exponent', '3'), (r'potenz', '2')]),
    ('symmetrie-abbildungen', r'erweiterung des koordinatensystems|koordinatensystem',
     [(r'.', '1')]),
    ('rationale-zahlen', r'^(?!.*(bruch|brüch|dezimal))(einführung der |enführung der )?(addition|subtraktion|multiplikation|division|addieren|subtrahieren|multiplizieren|dividieren)\b|rechengesetz|rechenvorteil|distributivgesetz|verbindung der rechenarten|rational|negative zahl|ganze ?zahl|ganzen zahl|zahlengerade|betrag|gegenzahl|zustandsänder|zu- und abnahm|zunahme und abnahme|vorzeichen|vorrangregel|grundrechenarten|celsius',
     [(r'sach|anwend', '4'), (r'multipl|divid|potenz|verbindung|grundrechen|rechengesetz|vorrang|alle', '3'), (r'addier|subtrah|zustand|zunahme|abnahme|zu- und', '2'), (r'.', '1')]),
    ('potenzen-wurzeln', r'potenz|wissenschaftliche schreib|quadratwurzel|kubikwurzel|wurzel|quadrieren|quadratzahl|große zahlen|kleine zahlen|sehr große|sehr kleine',
     [(r'zehner|schreibweise|große|kleine', '2'), (r'wurzel|quadrier', '3'), (r'.', '1')]),
    ('strahlensaetze', r'maßstab|massstab|ähnlich|strahlensatz|strahlensätze|zentrische streckung|vergrößer|verkleiner|vierstreckensatz|streckung',
     [(r'strahlens|vierstrecken', '3'), (r'ähnlich|streckung', '2'), (r'.', '1')]),
    ('prozentrechnung', r'prozent|promille|grundwert|rabatt|skonto|mehrwertsteuer|brutto|netto|sonderangebot',
     [(r'veränder|zunahme|abnahme|erhöh|vermehrt|vermindert|mehr als 100|über 100|änderung', '5'), (r'prozentsatz', '2'), (r'prozentwert', '3'), (r'grundwert', '4'), (r'schreibweise|anteil|prozente|brüche|bruch|darstell|begriff', '1'), (r'.', '')]),
    ('wahrscheinlichkeit', r'wahrscheinlich|zufall|laplace|baumdiagramm|pfadregel|ereignis|ergebnis|kombinat|zählprinzip|simulation|mehrstufig|zweistufig|würfeln|glücks|roulette|urne|zurücklegen|summenregel|kombinieren|gewinnchanc|produktregel',
     [(r'ohne zurück', '4'), (r'baum|pfad|mehrstufig|zweistufig|produktregel', '3'), (r'kombin|zähl|ergebnismeng|ergebnisse', '1'), (r'.', '2')]),
    ('daten', r'lagemaß|streumaß|stichprobe|daten|diagramm|häufigkeit|statistik|statistisch|mittelwert|median|modalwert|boxplot|quartil|spannweite|kenngröße|kennwert|histogramm|umfrage|erhebung|vierfelder|mittlere|streuung|arithmetisch|zentralwert|schaubild',
     [(r'vierfelder', '7'), (r'boxplot|quartil|beurteil|irreführ|manipul', '5'), (r'klasse|histogramm', '6'), (r'lagemaß|streumaß|mittel|median|modal|kenn|spannweite|zentral|arithm|streuung|abweichung', '4'), (r'kreisdiagramm|streifen', '3'), (r'säulen|balken|linien|diagramm|schaubild', '2'), (r'.', '1')]),
    ('pyramide-kegel-kugel', r'pyramide|kegel|kugel',
     [(r'pyramide', '1'), (r'kegel', '2'), (r'kugel', '3')]),
    ('winkel-dreiecke', r'umkreis|inkreis|thales|thaies|kongruen|konstru',
     [(r'kongruen|konstru', '4'), (r'.', '5')]),
    ('kreis', r'kreis(?!diagramm)|kreiszahl|kreisausschnitt|kreisbogen|kreisring|tangente|\bpi\b|π',
     [(r'ausschnitt|bogen|ring|teil|sektor', '3'), (r'fläche|inhalt', '2'), (r'umfang|kreiszahl|\bpi\b|π', '1'), (r'.', '')]),
    ('koerper', r'zylinder|prisma|prismen|quader|würfel|körper|schrägbild|netz|zweitafel|oberfläche|volumen|hohlkörper|platonisch|raumvorstell|masse von',
     [(r'zylinder', '4'), (r'prism', '3'), (r'quader|würfel', '2'), (r'zusammengesetzt', '5'), (r'netz|schrägbild|darstell|zweitafel|erkennen|beschreib|raumvorst|herstell', '1'), (r'.', '')]),
    ('flaechen', r'fläche|umfang|parallelogramm|trapez|drachen|raute|vieleck|rechteck|quadrat(?!isch|wurzel|zahl)|zusammengesetzte figur|figuren',
     [(r'parallelogramm', '2'), (r'trapez|drachen|raute', '4'), (r'dreieck', '3'), (r'zusammengesetzt|vieleck|figuren', '5'), (r'rechteck|quadrat|umfang', '1'), (r'.', '')]),
    ('lineare-funktionen', r'lineare funktion|proportionale funktion|steigung|geradengleichung|gleichung einer geraden|funktionsgleichung|nullstelle|geraden|funktion',
     [(r'proportionale funktion', '1'), (r'gleichung einer geraden|geradengleichung|durch zwei|bestimm|aufstell', '4'), (r'nullstell|punkt|wert|probe|liegt', '3'), (r'anwend|sach|modell', '5'), (r'steigung|graph|zeichn|m ?x|mx|lineare funktion', '2'), (r'.', '')]),
    ('winkel-dreiecke', r'senkrecht|winkel|dreieck|viereck|kongruen|konstru|mittelsenkrechte|halbierende|höhen|parallele|geodreieck|geometrische grundbegriffe|kongruent',
     [(r'konstru|kongruen', '4'), (r'mittelsenk|halbier|höhen|besondere linien', '5'), (r'summe|formen|arten|viereck|eigenschaft|innenwinkel|vielecke', '3'), (r'senkrecht|geraden|parallel|scheitel|stufen|wechsel|schnittpunkt', '2'), (r'messen|zeichn|grundbegriff', '1'), (r'.', '')]),
    ('symmetrie-abbildungen', r'symmetr|spiegel|drehung|verschiebung|abbildung|parkett|ornament',
     [(r'achsen', '2'), (r'.', '3')]),
    ('zuordnungen', r'zuordnung|proportional|dreisatz|proportionalitätsf|quotientengleich|produktgleich|füllkurve|verhältnisgleich|proportionen',
     [(r'direkt und indirekt|und antiprop|und indirekt|erkennen|grenzen|vermischt|modellieren mit', '4'), (r'antiprop|indirekt|produktgleich', '3'), (r'proportional|dreisatz|quotient|verhältnis', '2'), (r'.', '1')]),
    ('lineare-gleichungen', r'gleichung|äquivalenz|umform|waage|ungleichung|formeln|umstellen|zahlenrätsel|lösen von',
     [(r'sach|aufstell|text|rätsel', '4'), (r'beide|klammer|bruch|nenner', '3'), (r'äquivalenz|umform|umstell|formel', '2'), (r'waage|verstehen|probe|probieren', '1'), (r'.', '')]),
    ('terme', r'term|ausklammer|ausmultiplizier|klammer|variable|zusammenfass',
     [(r'ausklammer', '4'), (r'ausmultipl|klammer', '3'), (r'zusammenfass|ordnen|addier', '1'), (r'multipl|produkt', '2'), (r'wert|berechn|einsetz', '5'), (r'aufstell|beschreib', '6'), (r'.', '')]),
    ('bruchrechnung', r'(brüche|bruch|dezimal).*(addi|subtra|multipl|divi|vervielfach|teilen)|(addi|subtra|multipl|divi|vervielfach|teilen).*(brüche|bruch|dezimal)',
     [(r'dezimal.*(multipl|divi|vervielf|teilen)|(multipl|divi|vervielf|teilen).*dezimal', '4'), (r'dezimal', '2'), (r'multipl|divi|vervielf|teilen', '3'), (r'.', '1')]),
    ('brueche-dezimalzahlen', r'brüche|bruch|dezimal|anteil|runden',
     [(r'kürz|erweiter', '2'), (r'vergleich|ordnen|runden', '5'), (r'dezimal', '4'), (r'.', '1')]),
    ('einheiten', r'einheit|größen|maßeinheit|längen|zeitspanne|gewicht',
     [(r'zeit', '2'), (r'.', '')]),
]


def regel(t):
    s = t.lower()
    d = s.replace(' ', '')
    if re.search(KEIN_STARK, s):
        return 'kein Eintrag', ''
    if re.search(SEK2, s) or re.search(SEK2, d):
        return 'kein Eintrag (Sek-II-Stoff)', ''
    for e, rx, sub in REGELN:
        if re.search(rx, s) or re.search(rx, d):
            for srx, ein in sub:
                if re.search(srx, s) or re.search(srx, d):
                    return e, ein
            return e, ''
    if re.search(KEIN, s):
        return 'kein Eintrag', ''
    return None, ''


def main():
    rows = list(csv.DictReader(open('sa-roh.csv', encoding='utf-8'), delimiter=';'))
    for r in rows:
        r['eintrag'], r['einheit'], r['weg'] = '', '', ''
        r['s'] = int(r['seiten']) if r['plausibel'] == 'ja' and r['seiten'] else 0
        r['p'] = int(r['start']) if r['start'] else None
    bands = collections.defaultdict(list)
    for r in rows:
        bands[(r['reihe'], r['klasse'])].append(r)
    for key, B in bands.items():
        inh = [r for r in B if r['art'] not in ('kapitel', 'anhang')]
        for r in inh:
            if r['art'] in ('uk', 'streifzug'):
                e, ein = regel(r['titel'])
                if e:
                    r['eintrag'], r['einheit'], r['weg'] = e, ein, 'titel'
        # Kapitelmehrheit fuer Unterkapitel ohne Treffer
        maj = {}
        for k in set(r['kapitel'] for r in inh):
            c = collections.Counter()
            for r in inh:
                if r['kapitel'] == k and r['weg'] == 'titel' and r['eintrag'] != 'kein Eintrag':
                    c[r['eintrag']] += r['s'] or 1
            if c and k:
                maj[k] = c.most_common(1)[0][0]
        for r in inh:
            if r['art'] == 'uk' and not r['weg']:
                prev = [x for x in inh if x['weg'] == 'titel' and not x['eintrag'].startswith('kein') and x['p'] is not None and r['p'] is not None and x['p'] < r['p']]
                if r['kapitel'] in maj:
                    r['eintrag'], r['weg'] = maj[r['kapitel']], 'kapitel'
                elif prev:
                    r['eintrag'], r['weg'] = max(prev, key=lambda x: x['p'])['eintrag'], 'nachbar'
                else:
                    r['eintrag'], r['weg'] = 'kein Eintrag', 'kein'
        # Rahmen: naechstes Unterkapitel mit Eintrag
        seq = sorted([r for r in inh if r['p'] is not None], key=lambda r: r['p'])
        for i, r in enumerate(seq):
            if r['weg']:
                continue
            fw = [x for x in seq[i + 1:] if x['weg'] in ('titel', 'kapitel', 'nachbar') and not x['eintrag'].startswith('kein')]
            bw = [x for x in reversed(seq[:i]) if x['weg'] in ('titel', 'kapitel', 'nachbar') and not x['eintrag'].startswith('kein')]
            src = (fw or bw) if r['art'] == 'oeffner' else (bw or fw)
            if src:
                r['eintrag'], r['weg'] = src[0]['eintrag'], 'rahmen'
            else:
                r['eintrag'], r['weg'] = 'kein Eintrag', 'kein'
    with open('sa-zuordnung.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh, delimiter=';')
        w.writerow(['reihe', 'klasse', 'kapitel', 'titel', 'start', 'seiten', 'art', 'plausibel', 'eintrag', 'einheit', 'weg'])
        for r in rows:
            w.writerow([r[k] for k in ['reihe', 'klasse', 'kapitel', 'titel', 'start', 'seiten', 'art', 'plausibel', 'eintrag', 'einheit', 'weg']])
    # Aggregation
    agg = collections.defaultdict(lambda: [0, 0])  # (eintrag, einheit, reihe, klasse) -> [direkt, mit rahmen]
    for r in rows:
        if r['art'] in ('kapitel', 'anhang') or not r['eintrag']:
            continue
        ein = r['einheit'] if r['weg'] == 'titel' else ''
        k = (r['eintrag'], ein, r['reihe'], r['klasse'])
        if r['weg'] in ('titel', 'kapitel', 'nachbar') or r['eintrag'].startswith('kein'):
            agg[k][0] += r['s']
        agg[k][1] += r['s']
    with open('sa-seiten.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh, delimiter=';')
        w.writerow(['eintrag', 'einheit', 'reihe', 'klasse', 'seiten', 'seiten_mit_rahmen'])
        for k in sorted(agg):
            w.writerow(list(k) + agg[k])
    return rows, agg


if __name__ == '__main__':
    rows, agg = main()
    c = collections.Counter(); z = collections.Counter(); wg = collections.Counter()
    for r in rows:
        if r['art'] == 'uk':
            c[r['reihe']] += 1
            z[r['reihe']] += not r['eintrag'].startswith('kein') and r['eintrag'] != ''
            wg[r['weg']] += 1
    for k in c:
        print(k, c[k], 'zugeordnet', z[k], round(100 * z[k] / c[k]))
    print(wg)
