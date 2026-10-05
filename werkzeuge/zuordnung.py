#!/usr/bin/env python3
"""Zuordnung Prüfungsheft (P10) <-> Aufgabenbank, Zählung je Stufe, je Kapitel.

Verallgemeinerung von werkzeuge/prozent-zuordnung.py (Stand 2026-10-05);
die Ausgabe für Prozent ist byteidentisch mit der des alten Skripts.

Aufruf (aus der Wurzel von mathe-nachhilfe):
    python3 werkzeuge/zuordnung.py KAPITEL [--bank PFAD] [--aus DATEI] [--zeige]
    KAPITEL: prozent, lineare, quadratische, dreiecke, daten,
             wahrscheinlichkeit, koerper, flaechen, wachstum,
             gleichungssysteme (Kapitel aus msa/skript-zuschnitt-p10.csv)
Eingaben:
    --bank  Klon von hz-0801/aufgabenbank (Vorgabe ../aufgabenbank);
            gelesen werden bank/<eintrag>/e*.jsonl der Einträge des Kapitels
    msa/<kapitel>-zusatz.jsonl  Zusatzaufgaben für Stufen ohne Bank-Sprosse
            (Eintrag „<kapitel>-zusatz“, kette = Name der Stufe)
    Stufen, echte Teilaufgaben, Sprossen-Zuordnung und Kern-Urteil stehen
    als Daten in diesem Skript (KAPITEL; Muster (eintrag, sprosse,
    filter): filter None = alle Zeilen, Liste von Original-Kennungen,
    oder Liste von Varianten „v1“ …; viertes Glied 'inner' = die Sprosse
    ist innermathematisch, jede Zeile zählt; im Muster „(i)“).
Ausgabe: msa/zuordnung-<kapitel>.csv (oder --aus), Spalten
    stufe;kern;katalog_ids;bank_sprossen;anzahl_echt;anzahl_bank;ziel;fehlen;kern_grund
    anzahl_bank zählt Bank- und Zusatzaufgaben; ziel 12 bei Kern, sonst 6
    (Beschluss 05.10.); fehlen = max(0, ziel - echt - anzahl_bank).
    --zeige druckt je Stufe die gewählten und die nicht gezählten Zeilen.

Echte Teilaufgaben: die Kennungen der Stufe im Zuschnitt 2022–2026 (ids
und neben) und die Katalogzeilen 2014–2021 (msa-katalog-basis/-kontext),
deren typ oder typ_neben denselben Handgriff nennt (Urteil je Stufe,
Liste in den Daten).

Zählregel (Beschluss 05.10.: neu zählt nur, was der Schüler nicht durch
Erinnern lösen kann): Eine Sprosse ist zugeordnet, wenn sie denselben
Handgriff ohne Gerüst verlangt (kein Streifen, keine Vorform, kein
vorgegebener Teilschritt, keine „gemischt“-Sprosse, außer die Stufe ist
selbst die Mischung); Prüfungshöhe-Sprossen nur mit den Originalen der
Stufe ([...] im Muster). Innermathematische Aufgaben (Text ohne Zahlen und
Formeln kürzer als 40 Zeichen, oder Sprosse als innermathematisch
markiert, weil die Zahlen in Term oder Grafik stehen) zählen je Zeile. Eine Sachaufgabe zählt
nicht, wenn ihr Gerippe (Zahlen, Formeln, Prüfkennung und Ankreuzoptionen
entfernt) zu mindestens 70 % mit dem einer schon gezählten Aufgabe der
Stufe übereinstimmt (difflib.SequenceMatcher ratio >= 0.7) – „nur andere
Zahlen im selben Text“.
Nur Standardbibliothek.
"""
import argparse,collections,difflib,glob,json,os,re,sys
MN=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK=os.path.join(os.path.dirname(MN),'aufgabenbank')
KAPITEL={}
# ---- Daten je Kapitel (Stand 2026-10-05) ----
#@DATEN@
def _i(e,*ss): return [(e,s,None,'inner') for s in ss]
def _a(e,*ss): return [(e,s,None) for s in ss]
P='prozentrechnung';Z='zinsrechnung'
KAPITEL['prozent']=dict(eintraege=[P,Z],stufen=[
 ('Prozent und Anteil umwandeln',['2022-OS-B1f','2020-OS-B1a'],[(P,'e1-k1-s3',None),(P,'e1-k1-s6',None),(P,'e1-k1-s8',['2020-OS-B1a','2022-OS-B1f'])]),
 ('Prozentwert',['2026-FOR-B1a','2014-OS-B1a','2017-OS-B1b','2021-OS-B1c','2019-OS-K5a','2015-OS-K2a'],[(P,'e3-k1-s6',None),(P,'e3-k1-s7',None),(P,'e3-k1-s11',None),(P,'e3-k2-s1',None),(P,'e3-k3-s4',None)]),
 ('Prozentsatz',['2023-OS-K6a','2018-OS-K7a','2015-OS-K7c'],[(P,'e2-k3-s5',None),(P,'e2-k3-s6',None),(P,'e2-k3-s7',None),(P,'e2-k3-s9',None),(P,'e2-k5-s4',None)]),
 ('Grundwert',['2023-OS-B1b','2025-OS-B1a'],[(P,'e4-k2-s5',None),(P,'e4-k2-s6',None),(P,'e4-k2-s8',None),(P,'e4-k3-s4',None)]),
 ('Erhöhung und Veränderung in Prozent',['2024-OS-B1e','2022-OS-K4b','2026-FOR-K3c','2016-OS-K2c','2021-OS-K5a','2020-OS-K2d','2015-OS-K2b','2020-OS-K4c'],[(P,'e5-k2-s3',None),(P,'e5-k2-s4',None),(P,'e5-k2-s5',None),(P,'e5-k2-s6',None),(P,'e5-k2-s8',None),(P,'e5-k2-s9',['2026-FOR-K3c','2022-OS-K4b','2016-OS-K2c','2024-OS-B1e','2015-OS-K2b']),(P,'e5-k3-s4',None)]),
 ('Aussagen prüfen',['2023-OS-K6b','2025-OS-K4b','2017-OS-K2b','2019-OS-K5b'],[(P,'e1-k1-s8',['2023-OS-K6b','2019-OS-K5b','2017-OS-K2b','2021-OS-K5b']),(P,'e1-k3-s4',None),(P,'e5-k2-s7',None),(P,'e5-k2-s9',['2025-OS-K4b'])]),
 ('Prozent aus einer berechneten Fläche',['2023-OS-K5c'],[]),
 ('Zinsen und Zinssatz',['2014-OS-B1e','2014-OS-K3a','2015-OS-B1e'],[(Z,'e1-k1-s1',None),(Z,'e1-k1-s4',None),(Z,'e1-k1-s5',None),(Z,'e1-k1-s6',None),(Z,'e1-k1-s7',None),(Z,'e1-k1-s12',None)]),
 ('Zinseszins und Guthabentabelle',['2014-OS-K3b','2014-OS-K3c'],[(Z,'e2-k1-s4',None),(Z,'e2-k1-s6',None),(Z,'e2-k1-s11',None),(Z,'e2-k2-s1',None),(Z,'e2-k4-s3',None)]),
],kern={
 'Prozent und Anteil umwandeln':('ja','Basisteil 2020 und 2022 (Niveau I), Bank-Einheit 1 mit Grundfall, Grundlage aller Prozentaufgaben'),
 'Prozentwert':('ja','6 echte Teilaufgaben 2014–2026, fast jedes Jahr im Basisteil (Niveau I), Bank-Einheit 3 mit Grundfall'),
 'Prozentsatz':('ja','3 echte (2015, 2018, 2023, Niveau I/II), Bank-Einheit 2 mit Grundfall, trägt Aussagen prüfen und Diagramme'),
 'Grundwert':('ja','Basisteil 2023 und 2025 (Niveau I), Bank-Einheit 4 mit Grundfall'),
 'Erhöhung und Veränderung in Prozent':('ja','8 echte, die meisten der Prüfung (Niveau I/II), Bank-Einheit 5 mit Grundfall'),
 'Aussagen prüfen':('nein','4 echte, aber Niveau II und nur als Prüfungshöhe auf Prozentsatz gesetzt (keine eigene Kette mit Grundfall)'),
 'Prozent aus einer berechneten Fläche':('nein','1 echte (2023, Sternchen, Niveau III), Nebenthema aus der Geometrie'),
 'Zinsen und Zinssatz':('nein','3 echte, zuletzt 2015, seit 2016 nicht geprüft, Zuschnitt 2022–2026 führt keine Zins-Stufe'),
 'Zinseszins und Guthabentabelle':('nein','2 echte, nur 2014 (Niveau II)'),
})
L='lineare-funktionen';Q='quadratische-funktionen'
KAPITEL['lineare']=dict(eintraege=[L,Q],stufen=[
 ('erkennen und ablesen',['2025-OS-B1f','2024-OS-B1i','2016-OS-B1c','2019-OS-K2a','2019-OS-K2b','2019-OS-K2c'],[(L,'e2-k5-s1',None,'inner'),(L,'e2-k5-s2',None,'inner'),(L,'e2-k5-s3',None,'inner'),(L,'e2-k5-s4',None,'inner'),(L,'e2-k5-s5',None,'inner'),(L,'e2-k5-s6',None,'inner')]),
 ('aus Gleichung zeichnen',['2024-OS-K3a','2026-FOR-K5a','2022-OS-K3a','2021-OS-K2a'],[(L,'e2-k4-s5',None,'inner'),(L,'e2-k4-s6',None,'inner'),(L,'e2-k4-s7',None,'inner'),(L,'e2-k4-s8',None,'inner')]),
 ('durch zwei Punkte, Gleichung ablesen',['2025-OS-K5a','2017-OS-K5a','2015-OS-K4d'],[(L,'e4-k2-s1',None,'inner'),(L,'e4-k1-s3',None,'inner'),(L,'e4-k1-s4',None,'inner'),(L,'e4-k1-s5',None,'inner'),(L,'e4-k1-s6',['v1','v2','v5','v6'],'inner'),(L,'e4-k1-s6',['v3','v4']),(L,'e4-k4-s4',None)]),
 ('zeichnen und Aussagen prüfen',['2023-OS-K4a','2021-OS-K2b'],[(L,'e2-k6-s1',None,'inner'),(L,'e2-k7-s2',None,'inner'),(L,'e4-k4-s2',None,'inner'),(L,'e3-k2-s7',['2023-OS-K4a','2021-OS-K2b'])]),
 ('ankreuzen',['2023-OS-B1i'],[(L,'e3-k2-s5',None,'inner'),(L,'e3-k2-s7',['2023-OS-B1i'])]),
 ('rechnerisch an Gerade und Parabel',['2026-FOR-K5b','2024-OS-K3c','2017-OS-K5b'],[(L,'e3-k2-s7',['2026-FOR-K5b','2017-OS-K5b','2019-OS-K2a','2021-OS-K6d','2022-OS-K3a']),(Q,'e1-k1-s4',None),(Q,'e3-k1-s2',None),(Q,'e4-k1-s14',None)]),
 ('Endwert berechnen',['2022-OS-K6a','2021-OS-K6a'],[(L,'e5-k1-s3',None),(L,'e5-k4-s4',None),(L,'e5-k1-s5',['2022-OS-K6a','2021-OS-K6a'])]),
 ('Graph zum Tarif zuordnen',['2023-OS-K3a','2016-OS-K6a'],[(L,'e5-k2-s1',None),(L,'e5-k1-s5',['2023-OS-K3a','2016-OS-K6a'])]),
 ('Gleichung aufstellen und rückwärts rechnen',['2022-OS-K6b','2016-OS-K6c','2021-OS-K6c','2021-OS-K6d','2021-OS-K7a'],[(L,'e5-k1-s1',None),(L,'e5-k1-s2',None),(L,'e5-k3-s1',None),(L,'e5-k4-s1',None),(L,'e1-k1-s8',None),(L,'e5-k1-s5',['2022-OS-K6b','2016-OS-K6c','2021-OS-K7a'])]),
 ('Tarife vergleichen',['2023-OS-K3b','2016-OS-K6b'],[(L,'e5-k1-s4',None),(L,'e5-k4-s2',None),(L,'e5-k1-s5',['2023-OS-K3b','2016-OS-K6b'])]),
],kern={
 'erkennen und ablesen':('ja','6 echte 2016–2025, Basisteil 2016, 2024, 2025 (Niveau I), Bank-Kette Ablesen mit Grundfall'),
 'aus Gleichung zeichnen':('ja','4 echte (2021, 2022, 2024, 2026), fast jedes Jahr Einstieg der Funktionsaufgabe, Bank-Kette Graph zeichnen mit Grundfall'),
 'durch zwei Punkte, Gleichung ablesen':('ja','3 echte (2015, 2017, 2025), Bank-Kette Gleichung bestimmen mit Grundfall'),
 'zeichnen und Aussagen prüfen':('nein','2 echte (2021, 2023), Aussagen zu Eigenschaften nur als Zusatz zum Zeichnen, keine eigene Kette mit Grundfall'),
 'ankreuzen':('nein','1 echte (Basisteil 2023), Punktprobe ist Kern der rechnerischen Stufe'),
 'rechnerisch an Gerade und Parabel':('ja','3 echte (2017, 2024, 2026), Bank-Kette Funktionswert mit Grundfall, Punktprobe trägt auch Quadratische'),
 'Endwert berechnen':('nein','2 echte (2021, 2022), Teilschritt der Sachkette, Grundfall der Kette ist das Aufstellen'),
 'Graph zum Tarif zuordnen':('nein','2 echte (2016, 2023), nur Zuordnen, keine eigene Kette mit Grundfall'),
 'Gleichung aufstellen und rückwärts rechnen':('ja','5 echte (2016, 2021 dreimal, 2022), Bank-Kette Anwendung mit Grundfall (Gleichung ankreuzen)'),
 'Tarife vergleichen':('nein','2 echte (2016, 2023), Niveau II, als Prüfungshöhe auf die Anwendungskette gesetzt'),
})
QF='quadratische-funktionen';QG='quadratische-gleichungen'
KAPITEL['quadratische']=dict(eintraege=[QF,QG],stufen=[
 ('Wertetabelle zuordnen',['2026-FOR-B1e','2015-OS-K4b'],[(QF,'e1-k1-s8',None,'inner'),(QF,'e1-k1-s12',None,'inner'),(QF,'e1-k2-s3',None,'inner'),(QF,'e1-k1-s13',None),(QF,'e1-k1-s14',None)]),
 ('Scheitelpunkt ablesen',['2022-OS-K3b','2026-FOR-K5c','2021-OS-B1d','2020-OS-K3a','2018-OS-K5b','2017-OS-K5c'],[(QF,'e2-k1-s1',None,'inner'),(QF,'e2-k1-s2',None,'inner'),(QF,'e2-k1-s3',None,'inner'),(QF,'e3-k1-s6',None,'inner')]),
 ('Punkt auf der Parabel prüfen',['2024-OS-K3c','2020-OS-K3b','2020-OS-K3c','2014-OS-K7a','2018-OS-K5a'],[(QF,'e1-k1-s4',None,'inner'),(QF,'e3-k1-s2',None,'inner'),(QF,'e4-k1-s14',None,'inner')]),
 ('Scheitelpunktform angeben',['2023-OS-K4b','2025-OS-K5b','2016-OS-B1g','2018-OS-K5c','2020-OS-K3d','2017-OS-K5e','2015-OS-B1i','2018-OS-K5d'],[(QF,'e2-k1-s6',None,'inner'),(QF,'e2-k1-s7',None,'inner'),(QF,'e2-k1-s8',None,'inner'),(QF,'e2-k1-s9',None,'inner'),(QF,'e2-k1-s10',None,'inner'),(QF,'e2-k1-s11',None,'inner'),(QF,'e3-k1-s7',None,'inner'),(QF,'e3-k1-s11',None,'inner'),(QF,'e2-k1-s16',None),(QF,'e2-k1-s17',None),(QF,'e2-k1-s18',None),(QF,'e3-k1-s12',None)]),
 ('Parabel skizzieren',['2024-OS-K3b'],[(QF,'e2-k1-s4',None,'inner'),(QF,'e1-k1-s9',None,'inner')]),
 ('Lage zweier Parabeln ohne Rechnung begründen',['2026-FOR-K5d','2014-OS-K7b'],[(QF,'e2-k1-s12',None,'inner'),(QF,'e4-k1-s15',None,'inner'),(QF,'e4-k1-s2',None,'inner')]),
 ('Lösung prüfen',['2025-OS-B1h'],[(QG,'e1-k2-s12',None,'inner'),(QG,'e2-k1-s5',None,'inner'),(QG,'e3-k3-s13',None,'inner'),(QG,'e2-k1-s12',['2025-OS-B1h'])]),
 ('Nullstellen berechnen',['2025-OS-K5c','2020-OS-K3e','2017-OS-K5d'],[(QF,'e4-k1-s1',None,'inner'),(QF,'e4-k1-s3',None,'inner'),(QF,'e4-k1-s4',None,'inner'),(QF,'e4-k1-s5',None,'inner'),(QF,'e4-k1-s6',None,'inner'),(QF,'e4-k1-s7',None,'inner'),(QF,'e4-k1-s21',None),(QG,'e3-k3-s19',['2025-OS-K5c','2020-OS-K3e','2017-OS-K5d'])]),
 ('x zu gegebenem y',['2023-OS-K4c'],[(QF,'e4-k1-s8',None,'inner'),(QF,'e4-k1-s22',None),(QG,'e3-k3-s19',['2023-OS-K4c'])]),
 ('Gerade und Parabel gleichsetzen',['2022-OS-K3c','2024-OS-K3d','2021-OS-K2c'],[(QF,'e4-k1-s9',None,'inner'),(QF,'e4-k1-s10',None,'inner'),(QF,'e4-k1-s11',None,'inner'),(QF,'e4-k1-s12',None,'inner'),(QF,'e4-k1-s13',None,'inner'),(QF,'e4-k1-s20',None),(QG,'e3-k4-s1',None,'inner'),(QG,'e3-k3-s19',['2022-OS-K3c','2024-OS-K3d','2021-OS-K2c'])]),
],kern={
 'Wertetabelle zuordnen':('nein','2 echte (2015, Basisteil 2026), Zuordnen als Prüfungsform auf der Kette Normalparabel, Grundfall ist das Ausfüllen'),
 'Scheitelpunkt ablesen':('ja','6 echte 2017–2026, fast jedes Jahr (Niveau I), Bank-Kette Scheitelpunktform mit Grundfall'),
 'Punkt auf der Parabel prüfen':('nein','5 echte (2014, 2018, 2020 zweimal, 2024), aber Teilschritt (Einsetzen), keine eigene Kette mit Grundfall; Kern in Lineare'),
 'Scheitelpunktform angeben':('ja','8 echte 2015–2025 (mit Verschieben und Spiegeln), Bank-Kette Scheitelpunktform mit Grundfall'),
 'Parabel skizzieren':('nein','1 echte (2024)'),
 'Lage zweier Parabeln ohne Rechnung begründen':('nein','2 echte (2014, 2026), Niveau III, keine eigene Kette'),
 'Lösung prüfen':('nein','1 echte (Basisteil 2025)'),
 'Nullstellen berechnen':('ja','3 echte (2017, 2020, 2025), Bank-Kette Nullstellen und Schnittpunkte mit Grundfall, p-q-Formel trägt auch Gleichsetzen'),
 'x zu gegebenem y':('nein','1 echte (2023)'),
 'Gerade und Parabel gleichsetzen':('ja','3 echte (2021, 2022, 2024), jedes zweite Jahr letzte Funktionsteilaufgabe, auf der Kette Nullstellen und Schnittpunkte mit Grundfall'),
})
PY='pythagoras';TR='trigonometrie';WD='winkel-dreiecke';SY='symmetrie-abbildungen'

KAPITEL['dreiecke']=dict(eintraege=[PY,TR,WD,SY],stufen=[
 ('Gleichung aufstellen',['2022-OS-B1g','2024-OS-B1f','2026-FOR-B1j','2021-OS-B1h','2017-OS-B1d'],_i(PY,'e1-k2-s6','e1-k2-s7','e1-k2-s8','e1-k5-s4','e2-k3-s5','e2-k6-s4')),
 ('Kathete oder Hypotenuse direkt',['2022-OS-K5a','2024-OS-K6a','2026-FOR-K4a','2022-OS-K2c','2020-OS-K7a','2019-OS-K3a','2016-OS-K7b'],_i(PY,'e1-k2-s1','e1-k2-s2','e1-k2-s3','e1-k2-s4','e1-k2-s5','e2-k3-s1','e2-k3-s2','e2-k3-s3','e2-k3-s6')+_a(PY,'e1-k2-s10','e2-k3-s7','e1-k5-s3','e2-k6-s3')+[(PY,'e1-k2-s15',['2020-OS-K7a']),(PY,'e2-k3-s12',['2022-OS-K5a','2024-OS-K6a']),(PY,'e3-k2-s19',['2022-OS-K2c'])]),
 ('Dreieck erst in Figur oder Körper finden',['2026-FOR-K2c','2025-OS-K4a','2025-OS-K2a','2018-OS-K6d','2019-OS-K2d'],_i(PY,'e3-k2-s1','e3-k2-s2','e3-k2-s3','e3-k2-s4','e3-k2-s5','e3-k2-s6','e3-k2-s7','e3-k2-s8','e3-k2-s9','e3-k2-s10','e3-k2-s11','e3-k2-s12','e3-k2-s16','e3-k2-s17')+_a(PY,'e3-k2-s13','e3-k2-s14','e3-k2-s15','e3-k4-s3')+[(PY,'e3-k2-s19',['2026-FOR-K2c','2018-OS-K6d','2019-OS-K2d']),(PY,'e1-k2-s15',['2025-OS-K4a'])]),
 ('Seitenverhältnis benennen',['2025-OS-B1g','2020-OS-B1c','2020-OS-B1j','2019-OS-B1h','2018-OS-B1g','2017-OS-B1j'],_i(TR,'e1-k3-s1','e1-k3-s2','e1-k4-s1','e1-k3-s12')+[(TR,'e1-k3-s17',['2020-OS-B1c','2020-OS-B1j','2025-OS-B1g'])]),
 ('Winkel berechnen',['2022-OS-K5b','2024-OS-K6b','2026-FOR-K4b','2020-OS-K5b','2019-OS-K3b'],_i(TR,'e2-k1-s1','e2-k1-s2','e2-k1-s3','e2-k1-s4','e2-k1-s5','e2-k1-s6','e2-k1-s8','e2-k1-s9','e2-k1-s10')+_a(TR,'e2-k1-s7','e2-k4-s3')+[(TR,'e2-k1-s12',['2022-OS-K5b','2024-OS-K6b','2026-FOR-K4b','2019-OS-K3b'])]),
 ('Seite berechnen',['2022-OS-K5d','2026-FOR-K4c','2023-OS-K7b','2021-OS-K3a','2021-OS-K3b','2018-OS-K4d','2017-OS-K4b','2016-OS-K7c'],_i(TR,'e1-k3-s4','e1-k3-s5','e1-k3-s6','e1-k3-s7','e1-k3-s8','e1-k3-s9','e1-k3-s10','e1-k3-s11','e1-k3-s13','e1-k3-s14','e3-k1-s1','e3-k1-s2','e3-k1-s3')+_a(TR,'e1-k3-s15','e1-k7-s3','e3-k1-s8')+[(TR,'e1-k3-s17',['2022-OS-K5d','2021-OS-K3a','2021-OS-K3b','2017-OS-K4b']),(TR,'e3-k1-s19',['2026-FOR-K4c','2023-OS-K7b','2018-OS-K4d','2016-OS-K7c'])]),
 ('gemischt, ohne Überschrift je Aufgabe',['2022-OS-K5a','2022-OS-K5b','2024-OS-K6a','2024-OS-K6b','2026-FOR-K4a','2026-FOR-K4b'],_i(PY,'e2-k3-s11')+_i(TR,'e2-k1-s11','e4-k1-s16','e3-k1-s14')+_a(PY,'e3-k2-s18')),
 ('Seite berechnen (Sinussatz)',['2024-OS-K6d','2025-OS-K4c','2021-OS-K3c','2020-OS-K7c','2019-OS-K3c','2018-OS-K4c','2017-OS-K4c','2015-OS-K5c','2014-OS-K2b'],_i(TR,'e4-k1-s1','e4-k1-s2','e4-k1-s3','e4-k1-s4','e4-k1-s5','e4-k1-s6','e4-k1-s7','e4-k1-s9','e4-k2-s3')+_a(TR,'e4-k1-s10','e4-k1-s17')),
 ('Eigenschaft erkennen',['2026-FOR-B1c','2016-OS-B1e'],_i(WD,'e3-k2-s10')+_i(SY,'e2-k5-s1')),
 ('Winkelsumme',['2022-OS-K5c','2023-OS-K2a','2026-FOR-B1i','2021-OS-B1i','2018-OS-K4b','2017-OS-K4a','2015-OS-K5b'],_i(WD,'e3-k2-s1','e3-k2-s2','e3-k2-s4','e3-k2-s5','e3-k2-s6','e3-k2-s7','e3-k2-s11','e3-k4-s3')+_a(WD,'e2-k2-s9')),
 ('gleichschenkliges Dreieck',['2023-OS-B1g','2023-OS-K7a'],_i(WD,'e3-k2-s3','e3-k2-s8')+[(WD,'e3-k2-s13',['2023-OS-B1g'])]),
 ('rechten Winkel begründen',['2025-OS-K2c'],_i(WD,'e3-k2-s9','e5-k1-s8')+_i(PY,'e2-k3-s9')+_a(WD,'e5-k1-s11')+[(WD,'e3-k2-s13',['2025-OS-K2c']),(PY,'e2-k3-s12',['2025-OS-K2c'])]),
 ('Symmetrieachsen zählen',['2022-OS-B1i','2025-OS-K2a','2021-OS-B1j'],_i(SY,'e2-k2-s2','e2-k2-s3','e2-k2-s4','e2-k2-s5','e2-k2-s6','e2-k2-s7','e2-k2-s8')+_a(SY,'e2-k2-s11','e2-k2-s12')),
],kern={
 'Gleichung aufstellen':('ja','5 echte, Basisteil 2017, 2021, 2022, 2024, 2026 (Niveau I), Bank-Kette Hypotenuse mit Grundfall'),
 'Kathete oder Hypotenuse direkt':('ja','7 echte 2016–2026 (Niveau I/II), Bank-Ketten Hypotenuse und Kathete mit Grundfall'),
 'Dreieck erst in Figur oder Körper finden':('ja','5 echte (2018, 2019, 2025 zweimal, 2026), Bank-Kette Figuren und Körper mit Grundfall'),
 'Seitenverhältnis benennen':('ja','6 echte, Basisteil 2017–2020 und 2025 (Niveau I), Grundfall der Bank-Kette Seite berechnen'),
 'Winkel berechnen':('ja','5 echte (2019, 2020, 2022, 2024, 2026), Bank-Kette Winkel berechnen mit Grundfall'),
 'Seite berechnen':('ja','8 echte 2016–2026, Bank-Ketten Seite berechnen und Teildreiecke mit Grundfall'),
 'gemischt, ohne Überschrift je Aufgabe':('nein','Form der Stufe (Mischung), die echten sind dieselben wie bei Pythagoras und Winkel; Mischsprossen der Bank'),
 'Seite berechnen (Sinussatz)':('ja','9 echte 2014–2025, fast jedes Jahr (Niveau II), Bank-Kette Sinussatz mit Grundfall'),
 'Eigenschaft erkennen':('nein','2 echte (Basisteil 2016, 2026), Ankreuzen als Sprosse der Kette Winkelsumme'),
 'Winkelsumme':('ja','7 echte 2015–2026 (Niveau I), Bank-Kette Winkelsumme mit Grundfall'),
 'gleichschenkliges Dreieck':('nein','2 echte, nur 2023'),
 'rechten Winkel begründen':('nein','1 echte (2025), Begründen auf mehreren Wegen (Winkelsumme, Umkehrung, Thales)'),
 'Symmetrieachsen zählen':('ja','3 echte, Basisteil 2021 und 2022, Kontext 2025 (Niveau I), Bank-Kette Symmetrieachsen bestimmen mit Grundfall'),
})
DA='daten'

KAPITEL['daten']=dict(eintraege=[DA],stufen=[
 ('Minimum, Maximum, Spannweite',['2026-FOR-K3a','2024-OS-K2a','2023-OS-K6c','2022-OS-K4a','2021-OS-K5a','2020-OS-K2d','2019-OS-B1i','2014-OS-K4a','2014-OS-K4b'],_a(DA,'e4-k1-s1','e4-k1-s2','e4-k1-s9','e4-k1-s8')),
 ('Median',['2024-OS-B1h','2015-OS-B1f'],_a(DA,'e4-k1-s4','e4-k1-s5')),
 ('Mittelwert',['2026-FOR-K3b','2024-OS-K2b','2021-OS-B1f','2017-OS-B1h','2016-OS-B1a','2020-OS-K2c','2015-OS-K7a'],_a(DA,'e4-k1-s6','e4-k1-s7','e4-k1-s10','e4-k1-s11','e4-k1-s12','e4-k4-s4','e6-k2-s3')),
 ('rückwärts: fehlender Wert',['2022-OS-B1d'],_a(DA,'e4-k1-s13','e6-k2-s4')),
 ('Aussagen prüfen, Auswirkung erklären',['2025-OS-K6a','2025-OS-K6c'],_a(DA,'e4-k1-s14','e4-k1-s15','e4-k1-s16','e4-k3-s1','e4-k4-s2')),
 ('Winkel berechnen und beschriften',['2022-OS-K4d','2024-OS-K2c','2017-OS-K2c','2021-OS-K5b'],_a(DA,'e3-k1-s5','e3-k1-s6','e3-k1-s8','e3-k1-s9','e3-k1-s10','e3-k1-s4','e3-k3-s4')+[(DA,'e3-k1-s12',['2017-OS-K2c','2024-OS-K2c'])]),
 ('aus Prozent darstellen',['2025-OS-K6b','2018-OS-K3c'],_a(DA,'e3-k1-s2','e3-k1-s3','e3-k3-s3')+[(DA,'e3-k1-s12',['2025-OS-K6b'])]),
 ('ergänzen',['2026-FOR-K3d','2023-OS-K6d','2020-OS-K2a','2018-OS-K3a'],_a(DA,'e2-k2-s7','e2-k2-s8','e2-k2-s9','e2-k2-s12','e2-k3-s1','e2-k4-s3')),
 ('Aussage prüfen',['2022-OS-K4c','2018-OS-K3d','2019-OS-K5c'],_a(DA,'e5-k1-s1','e5-k1-s2','e5-k1-s3','e5-k1-s4','e5-k1-s5','e5-k1-s7','e5-k1-s8','e5-k4-s4')+[(DA,'e5-k1-s11',['2018-OS-K3d','2019-OS-K5c'])]),
 ('falschen Eindruck erklären',['2026-FOR-K3e','2014-OS-K3d'],_a(DA,'e5-k1-s6','e5-k1-s9','e5-k3-s1','e5-k4-s1','e5-k4-s2')+[(DA,'e5-k1-s11',['2026-FOR-K3e'])]),
],kern={
 'Minimum, Maximum, Spannweite':('ja','9 echte 2014–2026, fast jedes Jahr Einstieg der Datenaufgabe (Niveau I), Bank-Kette Kenngrößen mit Grundfall'),
 'Median':('nein','2 echte (Basisteil 2015, 2024), Sprosse der Kette Kenngrößen'),
 'Mittelwert':('ja','7 echte 2015–2026 (Niveau I/II), Bank-Kette Kenngrößen'),
 'rückwärts: fehlender Wert':('nein','1 echte (Basisteil 2022)'),
 'Aussagen prüfen, Auswirkung erklären':('nein','2 echte, nur 2025 (Niveau II/III)'),
 'Winkel berechnen und beschriften':('ja','4 echte (2017, 2021, 2022, 2024), Bank-Kette Anteile darstellen mit Grundfall'),
 'aus Prozent darstellen':('nein','2 echte (2018, 2025)'),
 'ergänzen':('ja','4 echte (2018, 2020, 2023, 2026), Bank-Kette Diagramme lesen mit Grundfall'),
 'Aussage prüfen':('ja','3 echte (2018, 2019, 2022), Bank-Kette Beurteilen mit Grundfall (Aussage mit einem Wert prüfen)'),
 'falschen Eindruck erklären':('nein','2 echte (2014, 2026), Niveau III, eine Sprosse der Kette Beurteilen'),
})
WK='wahrscheinlichkeit'
KAPITEL['wahrscheinlichkeit']=dict(eintraege=[WK],stufen=[
 ('Ergebnisse aufzählen',['2025-OS-K3a','2020-OS-K6a','2017-OS-B1f'],_a(WK,'e1-k1-s1','e1-k1-s3','e1-k1-s6','e1-k1-s7','e1-k2-s1','e1-k3-s3')),
 ('Wahrscheinlichkeit angeben',['2024-OS-K5a','2026-FOR-K6a','2019-OS-K6a','2018-OS-K7b','2017-OS-K6a','2016-OS-K5c','2016-OS-K5d','2014-OS-K6a','2016-OS-B1f','2015-OS-B1a','2014-OS-B1b','2014-OS-B1d'],_a(WK,'e2-k3-s1','e2-k3-s2','e2-k3-s3','e2-k3-s4','e2-k3-s5','e2-k3-s6','e2-k3-s10','e2-k3-s12','e2-k3-s13','e2-k4-s1','e2-k6-s3')),
 ('Baum ergänzen',['2024-OS-K5b','2026-FOR-K6b','2020-OS-K6c','2019-OS-K6b','2015-OS-K7d','2014-OS-K6b'],_a(WK,'e3-k3-s1','e3-k3-s2','e3-k3-s11','e3-k4-s3','e4-k1-s2','e4-k1-s6')),
 ('Pfadregel',['2025-OS-K3b','2025-OS-K3c','2020-OS-K6b','2014-OS-K6c'],_a(WK,'e3-k3-s3','e3-k3-s4','e3-k3-s5','e3-k3-s8','e3-k3-s9','e3-k4-s4')),
 ('ohne Zurücklegen',['2024-OS-K5c','2019-OS-K6c','2018-OS-K7c'],_a(WK,'e4-k1-s1','e4-k1-s3','e4-k1-s4','e4-k1-s5','e4-k1-s7','e4-k1-s9','e4-k1-s10','e4-k2-s4')),
 ('Gegenereignis',['2026-FOR-K6c'],_a(WK,'e3-k3-s6','e3-k3-s7','e2-k3-s7')),
 ('Zufallsgerät entwerfen',['2025-OS-K3d','2026-FOR-K6d','2019-OS-B1g','2018-OS-B1j'],_a(WK,'e2-k3-s9','e3-k3-s10','e2-k3-s8')),
],kern={
 'Ergebnisse aufzählen':('ja','3 echte (2017, 2020, 2025), Einstieg der Zufallsaufgabe (Niveau I), Bank-Kette Zählen mit Grundfall'),
 'Wahrscheinlichkeit angeben':('ja','12 echte 2014–2026, fast jedes Jahr Basis und Kontext (Niveau I), Bank-Kette Einstufig mit Grundfall'),
 'Baum ergänzen':('ja','6 echte 2014–2026 (Niveau I/II), Bank-Kette Mit Zurücklegen mit Grundfall (Baum zeichnen)'),
 'Pfadregel':('ja','4 echte (2014, 2020, 2025 zweimal), Bank-Kette Mit Zurücklegen'),
 'ohne Zurücklegen':('ja','3 echte (2018, 2019, 2024, Niveau II), Bank-Kette Ohne Zurücklegen mit Grundfall'),
 'Gegenereignis':('nein','1 echte (2026)'),
 'Zufallsgerät entwerfen':('nein','4 echte (2018, 2019, 2025, 2026), aber Niveau II/III und nur Sprossen ohne eigene Kette mit Grundfall'),
})
KO='koerper';PK='pyramide-kegel-kugel'
KAPITEL['koerper']=dict(eintraege=[KO,PK],stufen=[
 ('Volumen direkt',['2026-FOR-B1f','2022-OS-K2b','2023-OS-K5b','2026-FOR-K2a','2021-OS-K4a','2016-OS-K3c','2014-OS-K5a'],_i(KO,'e2-k1-s1','e2-k1-s2','e3-k1-s1','e3-k1-s2','e3-k1-s3','e3-k1-s4','e3-k1-s5','e3-k1-s6','e4-k2-s1','e4-k2-s2','e4-k2-s3','e4-k2-s4')+_i(PK,'e1-k5-s1','e1-k5-s2','e1-k5-s3','e1-k5-s4','e2-k2-s1','e2-k2-s2','e2-k2-s3','e2-k2-s4','e3-k1-s1','e3-k1-s2','e3-k1-s3','e3-k1-s4')+_a(KO,'e2-k1-s10','e4-k2-s13')+[(PK,'e3-k1-s18',['2016-OS-K3c'])]),
 ('rückwärts: Radius oder Höhe aus Volumen',['2022-OS-K2d','2023-OS-K5d'],_i(KO,'e2-k1-s6','e3-k1-s10','e4-k2-s10','e4-k2-s11','e2-k3-s1')+_i(PK,'e1-k5-s13','e2-k2-s11','e2-k2-s12','e3-k1-s12')+_a(KO,'e4-k2-s15')),
 ('Restvolumen',['2024-OS-K4c'],_a(KO,'e5-k1-s5','e5-k1-s11','e4-k2-s5')+_a(PK,'e3-k1-s13')),
 ('Mantelfläche mit Kosten',['2026-FOR-K2b','2018-OS-K6b'],_i(KO,'e4-k2-s6','e4-k2-s7')+_i(PK,'e2-k2-s7','e2-k2-s8','e1-k5-s7')+_a(PK,'e2-k2-s13','e1-k5-s15')),
 ('vergleichen und urteilen',['2026-FOR-K2d','2021-OS-K4b'],_a(KO,'e4-k2-s14','e4-k3-s2')+_a(PK,'e2-k2-s14','e2-k2-s16','e3-k1-s15','e1-k5-s14','e2-k3-s2')),
 ('Netz erkennen',['2022-OS-K2a','2016-OS-B1j','2018-OS-B1i','2017-OS-B1c'],_a(KO,'e1-k1-s1','e1-k1-s3','e1-k1-s4','e1-k5-s3','e1-k5-s4','e4-k2-s8')+_a(PK,'e2-k2-s10')+[(KO,'e1-k1-s10',['2016-OS-B1j'])]),
 ('Netz mit Maßen skizzieren',['2023-OS-K5a','2020-OS-K5a','2019-OS-K4a','2014-OS-K5b'],_a(KO,'e1-k1-s5','e3-k1-s9','e3-k2-s4','e4-k3-s4')+_a(PK,'e1-k5-s11')),
 ('Körper im Schrägbild skizzieren',['2024-OS-K4b','2015-OS-K6b'],_a(KO,'e1-k1-s6','e1-k1-s7','e1-k4-s1')+_a(PK,'e1-k5-s12','e2-k2-s9','e1-k6-s3','e2-k3-s3','e3-k1-s6')),
],kern={
 'Volumen direkt':('ja','7 echte 2014–2026, fast jedes Jahr (Niveau I), Bank-Ketten Quader, Prisma, Zylinder, Pyramide, Kegel, Kugel mit Grundfall'),
 'rückwärts: Radius oder Höhe aus Volumen':('nein','2 echte (2022, 2023 mit Stern), Niveau II/III, Sprossen ohne eigenen Grundfall'),
 'Restvolumen':('nein','1 echte (2024)'),
 'Mantelfläche mit Kosten':('nein','2 echte (2018, 2026)'),
 'vergleichen und urteilen':('nein','2 echte (2021, 2026), Niveau III'),
 'Netz erkennen':('ja','4 echte, Basisteil 2016–2018, Kontext 2022 (Niveau I), Bank-Kette Körper und Netze mit Grundfall'),
 'Netz mit Maßen skizzieren':('nein','4 echte (2014, 2019, 2020, 2023), aber nur Sprossen ohne eigene Kette mit Grundfall'),
 'Körper im Schrägbild skizzieren':('nein','2 echte (2015, 2024)'),
})
FL='flaechen';KR='kreis'
KAPITEL['flaechen']=dict(eintraege=[FL,KR],stufen=[
 ('Formel oder Term zur Figur',['2022-OS-B1e','2024-OS-B1c','2025-OS-B1i','2019-OS-B1e','2014-OS-B1g'],_i(FL,'e1-k2-s8','e3-k1-s6','e1-k5-s4','e3-k4-s4')+_i(KR,'e2-k2-s1')),
 ('Grundfigur berechnen',['2026-FOR-B1h','2024-OS-K4a','2023-OS-K2b','2025-OS-K2b','2016-OS-K3b','2015-OS-K5d','2015-OS-K6c','2019-OS-K4c'],_i(FL,'e1-k2-s1','e1-k2-s2','e1-k2-s3','e1-k2-s4','e2-k1-s1','e2-k1-s2','e2-k1-s3','e3-k1-s1','e3-k1-s2','e3-k1-s3','e3-k1-s4','e4-k1-s1','e4-k1-s2','e4-k1-s4','e4-k1-s5')+_i(KR,'e1-k2-s1','e1-k2-s2','e1-k2-s3','e2-k1-s1','e2-k1-s2','e2-k1-s3')+_a(KR,'e2-k1-s8')),
 ('rückwärts: Seite aus Fläche',['2023-OS-B1c','2020-OS-B1d','2018-OS-B1f','2020-OS-K7b','2014-OS-K5c','2014-OS-K5d'],_i(FL,'e1-k2-s5','e1-k2-s6','e1-k2-s7','e2-k1-s5','e3-k1-s5','e4-k1-s3','e4-k3-s1')+_i(KR,'e1-k2-s4','e1-k2-s5','e2-k1-s6')+_a(FL,'e1-k2-s9','e3-k1-s7','e4-k1-s6')),
 ('Figur erst zerlegen oder Strecke erst berechnen',['2022-OS-K5e','2023-OS-K2c','2025-OS-B1e','2018-OS-K6a','2017-OS-K3a','2017-OS-K3b'],_i(FL,'e5-k1-s1','e5-k1-s2','e5-k1-s3','e5-k1-s4','e5-k1-s5','e5-k1-s6','e1-k3-s1','e4-k2-s1')+_i(KR,'e3-k1-s5','e3-k1-s6','e3-k1-s8')+_a(FL,'e5-k1-s7')+[(KR,'e3-k1-s11',['2025-OS-B1e'])]),
 ('Anteil in Prozent (Verschnitt)',['2023-OS-K5c'],_a(FL,'e5-k3-s1')),
],kern={
 'Formel oder Term zur Figur':('ja','5 echte, Basisteil 2014, 2019, 2022, 2024, 2025 (Niveau I), Sprossen in jeder Figurenkette'),
 'Grundfigur berechnen':('ja','8 echte 2015–2026 (Niveau I), Bank-Ketten Rechteck, Parallelogramm, Dreieck, Trapez, Kreis mit Grundfall'),
 'rückwärts: Seite aus Fläche':('ja','6 echte, Basisteil 2018, 2020, 2023, Kontext 2014 und 2020, Rückwärtssprossen in jeder Figurenkette'),
 'Figur erst zerlegen oder Strecke erst berechnen':('ja','6 echte (2017 zweimal, 2018, 2022, 2023, 2025), Bank-Kette Zusammengesetzte Figuren mit Grundfall'),
 'Anteil in Prozent (Verschnitt)':('nein','1 echte (2023, Sternchen, Niveau III); dieselbe Stufe wie Prozent „Prozent aus einer berechneten Fläche“'),
})
# ---- Ende Daten ----

def gerippe(t):
  t=re.sub(r'\(P10[^)]*\)','',t)
  t=re.sub(r'\$[^$]*\$','#',t)
  t=re.sub(r'\d[\d\\,.{}]*','#',t)
  t=re.sub(r'\\kreuz\{[^}]*\}','',t)
  return re.sub(r'\s+',' ',t).strip()[:120]
def innermath(t):
  g=gerippe(t)
  return len(re.sub(r'[#\\{}()%€\s.,:;?]','',g))<40
def lade(kap,K):
  A=[]
  for e in K['eintraege']:
    for f in sorted(glob.glob(os.path.join(BANK,'bank',e,'e*.jsonl'))):
      for l in open(f): A.append(json.loads(l))
  zus=os.path.join(MN,'msa',kap+'-zusatz.jsonl')
  try:
    for l in open(zus): A.append(json.loads(l))
  except FileNotFoundError: pass
  return A
def gleich(a,b):
  return difflib.SequenceMatcher(None,gerippe(a),gerippe(b)).ratio()>=0.7
def passt(d,e,pre,orig,*_):
  if d['eintrag']!=e or not d['id'].startswith(e+'-'+pre+'-v'): return False
  if orig is None: return True
  oid=(d.get('original') or {}).get('id')
  vs=[o for o in orig if o.startswith('v')]
  if vs: return ('v'+d['id'].rsplit('-v',1)[1]) in vs
  return oid in orig
def zaehle2(kap,K,A,zeige=False):
  out=[]
  for name,echt,maps in K['stufen']:
    sel=[]
    inn=set()
    for m in maps:
      for d in A:
        if passt(d,*m) and d not in sel:
          sel.append(d)
          if len(m)>3 and m[3]=='inner': inn.add(d['id'])
    sel+=[d for d in A if d['eintrag']==kap+'-zusatz' and d['kette']==name]
    inn|={d['id'] for d in sel if d.get('innermath')}
    reps=[];n=0;art=collections.Counter()
    if zeige: print('##',name)
    for d in sel:
      if d['id'] in inn or innermath(d['aufgabe']):
        n+=1; art['inner']+=1
        if zeige: print('   inner:',d['id'])
        continue
      if any(gleich(d['aufgabe'],r['aufgabe']) for r in reps):
        if zeige: print('   gleich:',d['id'])
        continue
      reps.append(d);n+=1;art['sach']+=1
      if zeige: print('   sach:',d['id'])
    out.append((name,echt,len(sel),n,art))
  return out
def muster(maps):
  t=[]
  for m in maps:
    e,pre,orig=m[:3]
    s=f'{e}-{pre}'
    if orig: s+='['+','.join(orig)+']'
    if len(m)>3 and m[3]=='inner': s+='(i)'
    t.append(s)
  return ' '.join(t)
def main(kap,pfad,zeige=False):
  K=KAPITEL[kap]
  A=lade(kap,K);res=zaehle2(kap,K,A,zeige)
  zl=['stufe;kern;katalog_ids;bank_sprossen;anzahl_echt;anzahl_bank;ziel;fehlen;kern_grund']
  for (name,echt,maps),(n2,e2,roh,n,art) in zip(K['stufen'],res):
    k,g=K['kern'][name];ziel=12 if k=='ja' else 6
    zus=sum(1 for d in A if d['eintrag']==kap+'-zusatz' and d['kette']==name)
    bs=(muster(maps)+(f' msa/{kap}-zusatz.jsonl({zus})' if zus else '')).strip()
    zl.append(f'{name};{k};{" ".join(echt)};{bs or "–"};{len(echt)};{n};{ziel};{max(0,ziel-len(echt)-n)};{g}')
  open(pfad,'w',encoding='utf-8').write('\n'.join(zl)+'\n')
  if zeige: print('\n'.join(zl))

if __name__=='__main__':
  ap=argparse.ArgumentParser()
  ap.add_argument('kapitel',choices=sorted(KAPITEL))
  ap.add_argument('--bank',default=BANK)
  ap.add_argument('--aus')
  ap.add_argument('--zeige',action='store_true')
  a=ap.parse_args();BANK=a.bank
  main(a.kapitel,a.aus or os.path.join(MN,'msa',f'zuordnung-{a.kapitel}.csv'),a.zeige)
