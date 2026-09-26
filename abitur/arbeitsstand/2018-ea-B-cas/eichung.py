# -*- coding: utf-8 -*-
"""Eichung 2018-ea-B-cas mit der Funktion eichung() aus abitur/iqb-bau.py (aus abitur/ starten).
Je Zeile: blinde Schätzung, Spalte Anforderungsbereich des Standardbezugs, Herkunft (eigen / übernommen aus der
WTR-Zeile / eigen, nicht blind), Schätzung nach der Prüfung der Abweichungen mit Regel. Schreibt nichts."""
import importlib.util, io, os, sys
sys.stdout.reconfigure(encoding="utf-8")
spec = importlib.util.spec_from_file_location("iqbbau", os.path.join(os.getcwd(), "iqb-bau.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

# (id-Suffix, blind, AB amtlich, Herkunft, nach Prüfung, Regel der Korrektur)
D = {
 "AnalysisCAS1": [("1a","I","I"),("1b","II","I"),("1c","II","I"),("1d","II","II"),("1e","III","II"),("1f","III","III"),
                  ("1g","II","III","e","III","(d) wie 2025MgrundlegendBAGLAA2WTR2-1d: vorgegebene Ansätze als Verbindungsvektoren/Steigungen und als Rechtwinkligkeitsbedingung deuten"),
                  ("2a","I","I"),("2b","I","II"),("2c","II","II"),("3a","II","II"),("3b","II","II"),("3c","II","II"),("4","III","III")],
 "AnalysisCAS2": [("1a","II","I"),("1b","II","I"),("1c","II","III"),("1d","III","III"),("1e","II","II"),("1f","III","III"),
                  ("2a","II","I"),("2b","II","II"),("2c","I","II"),("2d","II","II"),("2e","II","II"),("2f","II","II"),
                  ("2g","II","III","e","III","(a): Bedingung „unabhängig davon, ob mit f oder g ermittelt“ erst in g(240) = f(240), g'(240) = f'(240) übersetzen; die Ausnahme „in einer vorigen Teilaufgabe“ gehört zu (b)")],
 "AnalysisCAS3": [("1a","I","I"),("1b","I","I"),("1c","II","II"),("1d","II","III"),("1e","III","III"),("1f","III","II"),("1g","I","I"),("1h","III","III"),
                  ("2a","I","I"),("2b","III","II","e","II","Ausnahme zu (a): „bis zu einer Höhe von 25 m über der Fahrbahn“ gibt die Grenze y = 37 wörtlich vor"),
                  ("2c","II","II"),("2d","II","II"),("2e","II","II"),("2f","III","III")],
 "AGLAA1CAS1": [("1a","II","II"),("1b","III","II","e","II","kein Eintrag (a)–(e); negative Anzahl als Widerspruch ist die einfache Deutung (Typ 2026-ga-B-mms: II)"),
                ("1c","II","I","e","I","Grundregel: eine Rechnung mit der Inversen, Anteile nur Division (Typ 2021-ga-B: I)"),
                ("1d","II","II"),("1e","I","I"),("1f","II","II"),
                ("1g","II","III","e","III","(a) wie 2018MgrundlegendBAGLAA1WTR-1g (gleicher Typ): „Bereich des Anteils“ erst in einen in p linearen Term mit Randwerten übersetzen"),
                ("1h","III","III")],
 "AGLAA1CAS2": [("1a","I","I"),("1b","I","I"),("1c","II","II"),("2a","I","I"),("2b","II","III"),("2c","II","II"),("3a","II","III"),
                ("3b","III","II","e","II","Prinzip: der Dreiwochenrhythmus steht in der zu beurteilenden Aussage, der Sonderfall N^3 = 1,35 · E ist nicht erst zu finden ((b) nur bei gefundenem Sonderfall)")],
 "AGLAA2CAS1": [("1a","II","II"),("1b","I","I"),("1c","II","II"),("1d","II","II"),("1e","I","I"),("1f","II","III")],
 "AGLAA2CAS2": [("1a","II","I","e","I","Grundregel wie beim Typ (2023-ga-B, 2017-ga-B: I): Schnitt einer Kantengeraden mit der Achse ist eine Rechnung, A folgt aus der Symmetrie"),
                ("1b","II","I"),("1c","II","II"),("1d","II","II"),("1e","II","II"),
                ("1f","II","III","e","III","(a)/Prinzip: die Bedingung „Schatten auf dem Untergrund“ ist erst als Vergleich von Kantenneigung und Lichteinfall zu finden"),
                ("1g","II","III")],
 "StochastikCAS1": [("1a","I","I"),("1b","II","III"),("1c","II","II"),
                    ("1d","II","III","u","III","Vorrang des Amtlichen (Kern § 5): aus 2018MerhoehtBStochastikWTR1-1d übernommene Schätzung"),
                    ("2a","I","I","u"),("2b","II","II","u"),("2c","II","II","n")],
 "StochastikCAS2": [("1a","I","I"),("1b","II","III"),("2a","II","II"),("2b","II","II"),("3a","I","I"),("3b","II","II"),("4a","II","II"),("4b","III","III")],
}
def zeilen(nach):
    out = []
    for datei, liste in D.items():
        for t in liste:
            suf, blind, ab = t[0], t[1], t[2]
            herk = t[3] if len(t) > 3 else "e"
            wert = (t[4] if len(t) > 4 else blind) if nach else blind
            out.append({"id": f"2018MerhoehtB{datei}-{suf}", "block": "B", "afb_amtlich": ab,
                        "bemerkung": f"Standardbezug: … AB amtlich: {ab}.", "niveau_geschaetzt": wert, "_h": herk})
    return out
for nach, titel in ((False, "Erster vollständiger Lauf (blind, vor jeder Korrektur)"), (True, "Nach Prüfung der Abweichungen")):
    z = zeilen(nach)
    t, abw, g = m.eichung(z)
    te, _, ge = m.eichung([x for x in z if x["_h"] in "en"])
    tu, _, gu = m.eichung([x for x in z if x["_h"] == "u"])
    tb, _, gb = m.eichung([x for x in z if x["_h"] == "e"])
    print(f"{titel}: {t} von {g} ({100 * t / g:.1f} %); eigene {te} von {ge}, davon blind {tb} von {gb}; übernommene {tu} von {gu}")
    if nach:
        print("Verbleibende Abweichungen:")
        for a in abw:
            print("  ", a)
print("Korrekturen:")
for datei, liste in D.items():
    for t in liste:
        if len(t) > 5:
            print(f"  {datei}-{t[0]}: {t[1]} → {t[4]} (AB {t[2]}); {t[5]}")
amt = [t[2] for l in D.values() for t in l]
print("AB-Spalte:", {k: amt.count(k) for k in ("I", "II", "III")}, "Zeilen", len(amt))
