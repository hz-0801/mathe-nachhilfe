# Gliederung Körper (P10)

Prüfung: msa
Kapitel: koerper
Gebiet: Geometrie
Name: Körper
Folge: 3
Bank: koerper | pyramide-kegel-kugel
Katalog: katalog/koerper.md | katalog/pyramide-kegel-kugel.md
Anzeigenamen: Volumen und Oberfläche = Volumen und Oberfläche

Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026): Kapitel → Stufe → Bankaufgaben, Originale,
didaktische Felder. Erzeugt daraus: zuordnung-<kapitel>.csv (werkzeuge/zuordnung.py), die
Zuschnitt-CSV und handgriffe-p10.csv (werkzeuge/gliederung-sichten.py). Stand der Daten: zuordnung.py
und Zuschnitt vom 08.10.2026, Steckbriefe vom 07.10.2026.

## Stufen

### Volumen direkt
- **Anzeigename:** Volumen berechnen
- **Schülerfrage:** Welche Formel brauchst du? Schreibe nur die Formel auf, rechne nicht.
- **Schülerfrage-Fälle:** Konservendose, 7 cm hoch, Radius 3,5 cm = V = π · r² · h | Fußball, Durchmesser 22 cm = V = 4/3 · π · r³ | Zelt, 4 m lang, Vorderseite ein Dreieck = V = G · h | Eistüte, Radius 3 cm, Höhe 12 cm = V = 1/3 · π · r² · h
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** a) Zylinder; b) Kugel; c) Prisma; d) Kegel
- **Kern:** ja – 7 echte 2014–2026, fast jedes Jahr (Niveau I), Bank-Ketten Quader, Prisma, Zylinder, Pyramide, Kegel, Kugel mit Grundfall
- **Originale:** 2026-FOR-B1f 2022-OS-K2b 2023-OS-K5b 2026-FOR-K2a 2021-OS-K4a 2016-OS-K3c 2014-OS-K5a
- **Bank:** koerper-e2-k1-s1(i) koerper-e2-k1-s2(i) koerper-e3-k1-s1(i) koerper-e3-k1-s2(i) koerper-e3-k1-s3(i) koerper-e3-k1-s4(i) koerper-e3-k1-s5(i) koerper-e3-k1-s6(i) koerper-e4-k2-s1(i) koerper-e4-k2-s2(i) koerper-e4-k2-s3(i) koerper-e4-k2-s4(i) pyramide-kegel-kugel-e1-k5-s1(i) pyramide-kegel-kugel-e1-k5-s2(i) pyramide-kegel-kugel-e1-k5-s3(i) pyramide-kegel-kugel-e1-k5-s4(i) pyramide-kegel-kugel-e2-k2-s1(i) pyramide-kegel-kugel-e2-k2-s2(i) pyramide-kegel-kugel-e2-k2-s3(i) pyramide-kegel-kugel-e2-k2-s4(i) pyramide-kegel-kugel-e3-k1-s1(i) pyramide-kegel-kugel-e3-k1-s2(i) pyramide-kegel-kugel-e3-k1-s3(i) pyramide-kegel-kugel-e3-k1-s4(i) koerper-e2-k1-s10 koerper-e4-k2-s13 pyramide-kegel-kugel-e3-k1-s18[2016-OS-K3c]
- **Verwechselbar:** Mantelfläche mit Kosten
- **Zuschnitt:** Volumen und Oberfläche

### Restvolumen
- **Anzeigename:** Restvolumen
- **Schülerfrage:** Welcher Körper ist außen, welcher innen? Schreibe nur den Ansatz auf: groß minus klein.
- **Schülerfrage-Fälle:** Tennisball in einer Würfelschachtel = V(Würfel) − V(Kugel) | Kegel in einer zylinderförmigen Verpackung = V(Zylinder) − V(Kegel) | Rohr: Außenzylinder und Innenzylinder = V(außen) − V(innen)
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** außen ist immer der Körper, in dem der andere steckt
- **Kern:** nein – 1 echte (2024)
- **Originale:** 2024-OS-K4c
- **Bank:** koerper-e5-k1-s5 koerper-e5-k1-s11 koerper-e4-k2-s5 pyramide-kegel-kugel-e3-k1-s13
- **Zuschnitt:** Volumen und Oberfläche

### Mantelfläche mit Kosten
- **Anzeigename:** Mantelfläche und Kosten
- **Schülerfrage:** Welche Fläche wird bezahlt? Schreibe hin: Mantel, Grundfläche oder ganze Oberfläche.
- **Schülerfrage-Fälle:** Die Außenmauer eines runden Turms wird gestrichen = Mantel | Ein Kegeldach wird mit Ziegeln gedeckt = Mantel | Eine Geschenkbox (Quader) wird rundum mit Papier beklebt = ganze Oberfläche | Der Boden eines runden Beckens wird gefliest = Grundfläche
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** bezahlt wird, was bearbeitet wird: Mauer und Dach sind Mäntel, Papier rundum ist die ganze Oberfläche, der Boden die Grundfläche
- **Kern:** nein – 2 echte (2018, 2026)
- **Originale:** 2026-FOR-K2b 2018-OS-K6b
- **Bank:** koerper-e4-k2-s6(i) koerper-e4-k2-s7(i) pyramide-kegel-kugel-e2-k2-s7(i) pyramide-kegel-kugel-e2-k2-s8(i) pyramide-kegel-kugel-e1-k5-s7(i) pyramide-kegel-kugel-e2-k2-s13 pyramide-kegel-kugel-e1-k5-s15
- **Verwechselbar:** Volumen direkt
- **Zuschnitt:** Volumen und Oberfläche

### rückwärts: Radius oder Höhe aus Volumen
- **Anzeigename:** Radius oder Höhe aus dem Volumen
- **Schülerfrage:** Gegeben ist das Volumen. Kreuze an, wo du am Ende eine Wurzel ziehen musst.
- **Schülerfrage-Fälle:** Zylinder: V und h bekannt, r gesucht = ja | Zylinder: V und r bekannt, h gesucht = nein | Würfel: V bekannt, Kante a gesucht = ja | Quader: V, a und b bekannt, c gesucht = nein
- **Schülerfrage-Form:** kreuz:Wurzel
- **Schülerfrage-Weg:** a) r steht im Quadrat, c) a hoch drei; bei b) und d) nur teilen
- **Kern:** nein – 2 echte (2022, 2023 mit Stern), Niveau II/III, Sprossen ohne eigenen Grundfall
- **Originale:** 2022-OS-K2d 2023-OS-K5d
- **Bank:** koerper-e2-k1-s6(i) koerper-e3-k1-s10(i) koerper-e4-k2-s10(i) koerper-e4-k2-s11(i) koerper-e2-k3-s1(i) pyramide-kegel-kugel-e1-k5-s13(i) pyramide-kegel-kugel-e2-k2-s11(i) pyramide-kegel-kugel-e2-k2-s12(i) pyramide-kegel-kugel-e3-k1-s12(i) koerper-e4-k2-s15
- **Zuschnitt:** Volumen und Oberfläche

### vergleichen und urteilen
- **Anzeigename:** vergleichen und urteilen
- **Schülerfrage:** Wie oft so groß wird das Volumen? Schätze, ohne zu rechnen.
- **Schülerfrage-Fälle:** Zylinder, die Höhe wird verdoppelt = 2 | Zylinder, der Radius wird verdoppelt = 4 | Kugel, der Radius wird verdoppelt = 8 | Würfel, die Kante wird verdreifacht = 27
- **Schülerfrage-Form:** linie:-mal so groß
- **Schülerfrage-Weg:** h steht einfach; r im Quadrat; r hoch drei; a hoch drei
- **Kern:** nein – 2 echte (2021, 2026), Niveau III
- **Originale:** 2026-FOR-K2d 2021-OS-K4b
- **Bank:** koerper-e4-k2-s14 koerper-e4-k3-s2 pyramide-kegel-kugel-e2-k2-s14 pyramide-kegel-kugel-e2-k2-s16 pyramide-kegel-kugel-e3-k1-s15 pyramide-kegel-kugel-e1-k5-s14 pyramide-kegel-kugel-e2-k3-s2
- **Zuschnitt:** Volumen und Oberfläche

### Netz erkennen
- **Kern:** ja – 4 echte, Basisteil 2016–2018, Kontext 2022 (Niveau I), Bank-Kette Körper und Netze mit Grundfall
- **Originale:** 2022-OS-K2a 2016-OS-B1j 2018-OS-B1i 2017-OS-B1c
- **Bank:** koerper-e1-k1-s1 koerper-e1-k1-s3 koerper-e1-k1-s4 koerper-e1-k5-s3 koerper-e1-k5-s4 koerper-e4-k2-s8 pyramide-kegel-kugel-e2-k2-s10 koerper-e1-k1-s10[2016-OS-B1j]
- **Zuschnitt:** Netz und Schrägbild

### Netz mit Maßen skizzieren
- **Kern:** nein – 4 echte (2014, 2019, 2020, 2023), aber nur Sprossen ohne eigene Kette mit Grundfall
- **Originale:** 2023-OS-K5a 2020-OS-K5a 2019-OS-K4a 2014-OS-K5b
- **Bank:** koerper-e1-k1-s5 koerper-e3-k1-s9 koerper-e3-k2-s4 koerper-e4-k3-s4 pyramide-kegel-kugel-e1-k5-s11
- **Zuschnitt:** Netz und Schrägbild

### Körper im Schrägbild skizzieren
- **Kern:** nein – 2 echte (2015, 2024)
- **Originale:** 2024-OS-K4b 2015-OS-K6b
- **Bank:** koerper-e1-k1-s6 koerper-e1-k1-s7 koerper-e1-k4-s1 pyramide-kegel-kugel-e1-k5-s12 pyramide-kegel-kugel-e2-k2-s9 pyramide-kegel-kugel-e1-k6-s3 pyramide-kegel-kugel-e2-k3-s3 pyramide-kegel-kugel-e3-k1-s6
- **Zuschnitt:** Netz und Schrägbild

## Plätze der Originale

Jede Teilaufgabe 2014–2026 (OS, EBR, FOR, GYM) mit ihrem Hauptplatz (Stufe, deren Handgriff die
ganze Teilaufgabe ist), „ganz auch“ (die ganze Aufgabe ist dieser Handgriff, obwohl anders
etikettiert) und Zwischenschritt; Stufen anderer Kapitel mit „kapitel:“. Erzeugt daraus:
msa/handgriffe-p10.csv (werkzeuge/gliederung-sichten.py).

| id | Hauptplatz | Ganz auch | Zwischenschritt | Begründung |
|---|---|---|---|---|
| 2014-GYM-K5c | Volumen direkt |  | dreiecke:Dreieck erst in Figur oder Körper finden | Hauptplatz nach typ „Volumen Kegel berechnen“. Kegelhöhe über Pythagoras im Kegel |
| 2014-OS-K5a | Volumen direkt |  |  | Hauptplatz nach typ „Volumen Prisma berechnen“ |
| 2014-OS-K5b | Netz mit Maßen skizzieren |  |  | Hauptplatz nach typ „Netz eines Prismas vervollständigen“ |
| 2015-GYM-K4b |  |  | Mantelfläche mit Kosten; dreiecke:Dreieck erst in Figur oder Körper finden | Hauptplatz außerhalb der P10-Stufen. Mantellinie über Pythagoras im Kegel |
| 2015-OS-K6b | Körper im Schrägbild skizzieren |  |  | Hauptplatz nach typ „Körperskizze beschriften“ |
| 2016-GYM-B1j | Netz erkennen |  |  | GYM-Zwilling von 2016-OS-B1j |
| 2016-GYM-K5b |  |  | Volumen direkt; flaechen:Grundfigur berechnen | Hauptplatz außerhalb der P10-Stufen. Fläche des gleichseitigen Dreiecks |
| 2016-OS-B1j | Netz erkennen |  |  | Hauptplatz nach typ „Gegenfläche im Würfelnetz bestimmen“ |
| 2016-OS-K3c | Volumen direkt |  |  | Hauptplatz nach typ „Volumen Kugel berechnen“ |
| 2017-GYM-B1c | Netz erkennen |  |  | GYM-Zwilling von 2017-OS-B1c |
| 2017-GYM-K4a | rückwärts: Radius oder Höhe aus Volumen |  |  | Hauptplatz nach typ „Höhe eines Zylinders aus Volumen berechnen“ |
| 2017-GYM-K4c | rückwärts: Radius oder Höhe aus Volumen |  | prozent:Grundwert | Hauptplatz nach typ „Grundkante aus Volumen berechnen“. Zwischenschritt aus typ_neben |
| 2017-OS-B1c | Netz erkennen |  |  | Hauptplatz nach typ „Körper aus Netz oder Schrägbild benennen“ |
| 2018-GYM-B1i | Netz erkennen |  |  | GYM-Zwilling von 2018-OS-B1i |
| 2018-GYM-K3c | Volumen direkt |  |  | Hauptplatz nach typ „Volumen Prisma berechnen“ |
| 2018-OS-B1i | Netz erkennen |  |  | Hauptplatz nach typ „Körper aus Netz oder Schrägbild benennen“ |
| 2018-OS-K6b | Mantelfläche mit Kosten |  |  | Hauptplatz nach typ „Mantelfläche Zylinder berechnen“ |
| 2019-GYM-K3c | rückwärts: Radius oder Höhe aus Volumen |  |  | Hauptplatz nach typ „Höhe eines Zylinders aus Volumen berechnen“ |
| 2019-GYM-K4a | Körper im Schrägbild skizzieren |  |  | Hauptplatz nach typ „Körper im Schrägbild darstellen“ |
| 2019-GYM-K4b | Mantelfläche mit Kosten |  | dreiecke:Dreieck erst in Figur oder Körper finden | Hauptplatz nach typ „Mantelfläche einer Pyramide berechnen“. Seitenhöhe über Pythagoras in der Pyramide |
| 2019-OS-K4a | Netz mit Maßen skizzieren |  |  | Hauptplatz nach typ „Netz eines Prismas vervollständigen“ |
| 2019-OS-K4b | Mantelfläche mit Kosten |  |  | Hauptplatz nach typ „Mantelfläche Prisma berechnen“. nicht in katalog_ids der Zuordnung |
| 2020-GYM-K4d |  |  | Volumen direkt | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2020-GYM-K5b |  |  | Volumen direkt | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2020-GYM-K5c | Körper im Schrägbild skizzieren |  |  | Hauptplatz nach typ „Körper im Schrägbild darstellen“ |
| 2020-GYM-K5d |  |  | Volumen direkt | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2020-OS-K5a | Netz mit Maßen skizzieren |  |  | Hauptplatz nach typ „Netz eines Prismas vervollständigen“ |
| 2021-GYM-K5a |  |  | Volumen direkt | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2021-OS-K4a | Volumen direkt |  |  | Hauptplatz nach typ „Volumen Zylinder berechnen“ |
| 2021-OS-K4b | vergleichen und urteilen |  |  | Hauptplatz nach typ „Volumenänderung bei doppeltem Radius begründen“ |
| 2022-GYM-K4c |  |  | Mantelfläche mit Kosten | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2022-GYM-K4d |  |  | Volumen direkt | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2022-OS-K2a | Netz erkennen |  | Netz mit Maßen skizzieren | Hauptplatz nach typ „Netz eines Zylinders erkennen“. Zwischenschritt aus typ_neben |
| 2022-OS-K2b | Volumen direkt |  |  | Hauptplatz nach typ „Volumen Zylinder berechnen“ |
| 2022-OS-K2d | rückwärts: Radius oder Höhe aus Volumen |  |  | Hauptplatz nach typ „Radius eines Zylinders aus Volumen berechnen“ |
| 2023-GYM-K4a | Volumen direkt |  |  | Hauptplatz nach typ „Volumen Zylinder berechnen“ |
| 2023-OS-K5a | Netz mit Maßen skizzieren |  |  | Hauptplatz nach typ „Mantelfläche Zylinder als Netz skizzieren“ |
| 2023-OS-K5b | Volumen direkt |  |  | Hauptplatz nach typ „Volumen Zylinder berechnen“ |
| 2023-OS-K5d | rückwärts: Radius oder Höhe aus Volumen |  |  | Hauptplatz nach typ „Höhe eines Zylinders aus Volumen berechnen“ |
| 2024-OS-K4b | Körper im Schrägbild skizzieren |  |  | Hauptplatz nach typ „Körper in Schrägbild skizzieren“ |
| 2024-OS-K4c | Restvolumen |  | Volumen direkt | Hauptplatz nach typ „Restvolumen berechnen“. Zwischenschritt aus typ_neben |
| 2025-GYM-K5b | Körper im Schrägbild skizzieren |  |  | Hauptplatz nach typ „Körper im Schrägbild darstellen“ |
| 2025-GYM-K5c | Volumen direkt |  | prozent:Prozentwert | Hauptplatz nach typ „Volumen Prisma berechnen“. 80 % des Volumens |
| 2025-GYM-K5d | Mantelfläche mit Kosten |  | dreiecke:Kathete oder Hypotenuse direkt | Hauptplatz nach typ „Mantelfläche Prisma berechnen“. Zwischenschritt aus typ_neben |
| 2026-EBR-B1f | Volumen direkt |  |  | EBR-Zwilling von 2026-FOR-B1f |
| 2026-EBR-K2a | Volumen direkt |  |  | EBR-Zwilling von 2026-FOR-K2a |
| 2026-EBR-K2b | Mantelfläche mit Kosten |  |  | EBR-Zwilling von 2026-FOR-K2b |
| 2026-FOR-B1f | Volumen direkt |  |  | Hauptplatz nach typ „Volumen Würfel berechnen“ |
| 2026-FOR-K2a | Volumen direkt |  |  | Hauptplatz nach typ „Volumen Zylinder berechnen“ |
| 2026-FOR-K2b | Mantelfläche mit Kosten |  |  | Hauptplatz nach typ „Mantelfläche Kegel berechnen“ |
| 2026-FOR-K2d | vergleichen und urteilen |  |  | Hauptplatz nach typ „Volumen Kegel und Zylinder vergleichen“ |
