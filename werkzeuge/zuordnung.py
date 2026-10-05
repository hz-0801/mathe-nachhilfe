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
def _i(e,*ss): return [(e,s,None,'inner') for s in ss]
def _a(e,*ss): return [(e,s,None) for s in ss]
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
