#!/usr/bin/env python3
"""Wortsuche in der Textfassung der LISUM-Planungshilfen (seit 10e).

Warum das Skript nötig ist: `quellen/lisum-planungshilfen-7bis10.txt` ist die
pdftotext-Fassung eines zweispaltigen Dokuments. pdftotext trennt Wörter am
Zeilenende, und die Fortsetzung steht *nicht* am Anfang der Folgezeile, weil
dort zuerst die andere Spalte gedruckt wird. Beispiel Zeile 906/907:

    ... Summen in Zähler oder Nen-
    Mathematikwerkzeugen)                       ner)

Ein `grep "Nenner"` meldet hier null Treffer. Jedes Nulltreffer-Protokoll, das
mit einer einfachen Wortsuche erstellt wurde, ist deshalb unbelegt.

Das Skript sucht jedes Wort zweimal: ganz in einer Zeile, und als Trennung
„Anfang-“ am Zeilenende mit „Rest“ als Wortanfang in einer der beiden
Folgezeilen. Die Bedingung „Wortanfang“ hält Fehlalarme heraus
(„Exponen-“ + „Zehnerpotenzen“ zählt nicht als „Nenner“).

Aufruf im Ordner katalog/, die Quelle wird eine Ebene darüber erwartet:

    python3 _suche_quelle.py Nenner Kehrwert Bruchrechnung
    python3 _suche_quelle.py --datei ../quellen/andere.txt Wort

Ausgabe je Wort: Trefferzahl und die Fundstellen als (Zeilennummer, Art).
Für Wortgruppen mit Leerzeichen wird nur die ungetrennte Form gefunden – dort
das tragende Einzelwort suchen und den Kontext von Hand prüfen.
"""
import io, re, sys, os

QUELLE = "../quellen/quelle-lisum-planungshilfen-7bis10.txt"


def lade(pfad):
    if not os.path.exists(pfad):
        sys.exit(f"Quelle nicht gefunden: {pfad}")
    return io.open(pfad, encoding="utf-8").read().split("\n")


def worte(zeile):
    return re.findall(r"[^\W\d_]+", zeile.lower(), re.UNICODE)


def suche(wort, zeilen):
    wl = wort.lower()
    treffer = []
    for i, z in enumerate(zeilen):
        if wl in z.lower():
            treffer.append((i + 1, "ganz"))
    for i, z in enumerate(zeilen):
        s = z.rstrip()
        if not s.endswith("-"):
            continue
        for k in range(2, len(wl)):
            a, b = wl[:k], wl[k:]
            if not s.lower().endswith(a + "-"):
                continue
            for j in (i + 1, i + 2):
                if j < len(zeilen) and any(t.startswith(b) for t in worte(zeilen[j])):
                    treffer.append((i + 1, f"getrennt {a}-/{b}"))
                    break
    return treffer


if __name__ == "__main__":
    args = sys.argv[1:]
    pfad = QUELLE
    if args and args[0] == "--datei":
        pfad, args = args[1], args[2:]
    if not args:
        sys.exit(__doc__)
    zeilen = lade(pfad)
    for w in args:
        t = suche(w, zeilen)
        print(f"{w:26s} {len(t):3d}  {t[:8]}")
