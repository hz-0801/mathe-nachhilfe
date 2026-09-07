mathblatt.sty – Anleitung (Stufe 3)
Gehört zu Vorlagenversion 2026-09-07a. Die Version steht in Zeile 2 der `mathblatt.sty`. Weichen beide ab, gilt die Vorlage: Makros, die sie nicht kennt, benutzt du nicht, und du meldest die Abweichung in einer Zeile im Ausgabeblock.
 
Datei `mathblatt.sty` neben die .tex-Datei legen, `\usepackage{mathblatt}` im Kopf. Kompilieren mit `xelatex` (nicht pdflatex): nur so sind Umlaute, ß, € und die Textextraktion sauber, weil im Sandbox keine Type-1-T1-Schriften liegen. Das Modell schreibt nur Inhalt; Ränder, Karogrößen, Fluchten, Kopf- und Fußzeile sind fest.
 
Schreibweisen: Kompiliert wird mit xelatex, deshalb schreibst du Umlaute, ß, € und deutsche
Anführungszeichen direkt in den Quelltext. `\ss`, `\euro`, `\"a` und `\glqq` sind weder nötig noch
zuverlässig. Bei Zahlen mit Dezimalkomma in Mathematik `$0{,}5$` schreiben, damit der Abstand stimmt. In den Grafikmakros gibst du Koordinaten und Werte dagegen mit Dezimalpunkt an (`2.5`); die Achsenbezifferung setzt die Vorlage selbst mit Komma. Das Prozentzeichen schreibst du im Text immer als `\%`, auch in `\achtung` und in Aufgabentexten – ein nacktes `%` macht den Rest der Zeile zum Kommentar und der Fehler erscheint erst Zeilen später. Einheiten im Mathemodus mit `\,` davor (`$240\,€$`); ohne den Abstand klebt die Einheit an der Zahl.
 
Beschriftungen: Alle Label-Argumente der Grafikmakros – `\gerade`, `\parabel`, `\funktion`, `\punkt`,
`\steigungsdreieck`, `\dreieck`, `\rpunkt`, `\rvektor`, `\rgerade`, `\rebene`, die Körper, die Analysis-Makros – werden vom Makro selbst in Mathematik gesetzt. Du
übergibst also `g`, `g_1`, `\alpha`, nicht `$g$`. Ausnahme sind die Achsentitel `xlabel`/`ylabel` im
`ksys`: die stehen im Textmodus, dort schreibst du `t in min` direkt und Mathematik mit Dollarzeichen.
 
Grundgerüst
 
```
\blattfuss{Lineare Funktionen}{Lernblatt Teil 1 von 3}   → Thema · Bezeichnung unten links, Seite unten rechts
\blattkopf{...}{...} / \blattkopf*{...}{...}{$\star$ = ...}  → Alternative: oben links; mit * dazu Legende unten links, Text im dritten Argument
\weit                                                    → weitere Zeilen im Aufgabenteil (ein Drittel); Begleitteil und Hilfe-Seite setzen selbst auf eng zurück
\uebersichtskasten[<Leitgrafik>]{<Formelzeilen>}          Sternlegende nicht hier, sondern über \blattkopf*
\begin{aufgabe}{Text} ... \end{aufgabe}            → nummeriert, bleibt auf einer Seite
\begin{teile} \teil ... \steil ... \end{teile}     → a), ☆b)
\begin{geruest} \gz{a}{$y=2x+3$}{\feld{m}\feld{n}} \gzs{b}{...}{...} \end{geruest}
\feld{W} → „W = ___"; \leerfeld → „___" ohne Bezeichner (nie \feld{} – das ergibt „= ___")
\feld{m}  \feldl{y}  \punktfeld  \janein  \kreuz{Text}      \janein ohne Argument → „☐ ja ☐ nein"; andere Beschriftungen mit \kreuz{A}\kreuz{B} – ein \janein[...] gibt es nicht
\mnliste[9]{2x+3, 5x-1, ...}            m und n je Gerade, eine Zeile statt geruest
\nullstellenliste[7]{x-4, 2x-6, ...}    x_0 je Gerade
\punktprobenliste[7]{2x-1/A(3|5), ...}  Punktprobe mit ja/nein
\begleitteil   \erg{3}{a) ... | b) ...}
\hilfeseite    \verfahren{Name} \begin{schritte} \schritt ... \achtung{...} \end{schritte}
```
 
In `geruest` wird ein Aufgabentext, der breiter als der Satzspiegel minus 6 cm ist, umbrochen; die Felder bleiben in der Flucht. Die drei Listenmakros ersetzen den `geruest`-Block bei den häufigsten Aufgabentypen und sparen etwa drei Viertel des Quelltextes. Einträge werden mit Komma getrennt, das Dezimalkomma als `0{,}5` geschrieben, damit es nicht als Trenner gilt. Das optionale Argument ist die Nummer der ersten Sternaufgabe; ohne Angabe gibt es keine Sterne. Der Term steht ohne `y =`, das setzt das Makro. Bei `\punktprobenliste` trennt ein Schrägstrich Term und Punkt. Für Typen ohne passendes Listenmakro bleibt `geruest`.
 
Innerhalb einer Hauptnummer läuft die Buchstabenzählung über alle `teile`-, `teilezwei`-, `geruest`-Blöcke und Listenmakros weiter: Du kannst einen `teile`-Block beenden, Text oder eine Grafik setzen und mit einem neuen `teile`-Block bei d) fortfahren. Erst die nächste `\begin{aufgabe}` beginnt wieder bei a). Das optionale Argument der Listenmakros zählt in dieser Reihenfolge: `[7]` setzt ab dem siebten Buchstaben (g) den Stern, auch wenn die Liste erst bei d) beginnt.
 
Alles, was zur Hauptnummer gehört – Teilaufgaben, Wertetabelle, Koordinatensystem –, steht zwischen `\begin{aufgabe}` und `\end{aufgabe}`; nur dann hält der Umbruch die Nummer zusammen. Passt sie nicht mehr auf die Seite, rückt sie als Ganzes weiter. Ist eine einzelne Nummer höher als eine Seite, bricht sie doch und meldet das als `Package mathblatt Warning` im Log.
 
Wertetabelle
 
```
\wertetabelle{x}{y}{-2,-1,0,1,2}              leer
\wertetabelle[7,4,1,-2,-5]{x}{f(x)}{-2,-1,0,1,2}   gefüllt (Begleitteil)
\wertetabelle[,4,,-2,-5]{x}{f(x)}{-2,-1,0,1,2}     teilweise gefüllt: leerer Eintrag = leeres Feld (ab 2026-09-06e)
\wertetabelleleer{x}{y}{5}                    Schüler legt selbst an
```
 
Koordinatensystem 2D
 
```
\begin{ksys}[xmin=-4,xmax=4,ymin=-5,ymax=5]            Zeichenfläche (Karo 8 mm)
\begin{ksys}[xmin=-5,xmax=5,ymin=-5,ymax=5,ablesen]    Ablesegrafik (Karo 6 mm)
\begin{ksys}[...,klein]                                Lösungsgrafik (Karo 3,5 mm)
\begin{ksys}[leit]                                     Leitgrafik im Übersichtskasten (Karo 6 mm, −3..3, etwa 4 cm)
\begin{ksys}[xmin=0,xmax=30,ymin=0,ymax=240,xstep=5,ystep=40,xlabel=t in min,ylabel=W in l]
  \gerade{2}{-1}{g}   \gerade[1.5]{2}{-1}{g}   \punkt{2}{3}{A}   \steigungsdreieck{0}{-1}{2}
  \parabel{1}{-1}{-2}{p}      y = a(x-d)^2+e
  \funktion{0.5*\x^2-2}{f}    \funktionab{1/\x}{f}{0.2}{4}
\end{ksys}
```
 
`karo` ist die Kantenlänge einer Gitterzelle in cm, nicht der Maßstab. Den Maßstab je Achse rechnet die Vorlage aus `karo` und `xstep`/`ystep` selbst aus. Für ungleiche Achsen genügen deshalb `xstep` und `ystep`; `karo` bleibt weg und die Zellen bleiben 8 mm. `xstep`/`ystep` steuern Gitter, Bezifferung und Maßstab gemeinsam – ein eigener Feinschritt fürs Gitter ist nicht vorgesehen. Die Achsenzahlen passt die Vorlage selbst an: unter Karo 6 mm werden sie kleiner gesetzt, und wenn die breiteste Zahl nicht in ein Karo passt, steht nur jede zweite (bei Bedarf dritte) Zahl, immer von 0 aus gezählt – bei `xstep=0.5` also die ganzen Zahlen. Das Gitter bleibt dabei vollständig. `[leit]` ergibt ein etwa 4 cm großes System für den Übersichtskasten; weitere Schlüssel dahinter überschreiben es (`[leit,ymax=5]`). Achsenbeschriftungen stehen im Textmodus: `xlabel=t in min` schreibt sich direkt, für Mathematik `xlabel=$x$` (so auch die Voreinstellung).
 
In `\funktion` und `\funktionab` heißt die Variable `\x` mit Backslash: `\funktion{0.5*\x^2-2}{f}`. Ein `x` ohne Backslash bricht die Kompilierung ab (`Unknown function 'x'`). Potenzen schreibst du direkt als `\x^2`, `\x^3`; die Vorlage setzt `\x` geklammert ein, negative x werden richtig gerechnet. Das Label von `\funktion`, `\funktionab` und `\parabel` sitzt an der ersten Stelle vom rechten Rand aus, an der der Graph in der Zeichenfläche liegt; verlässt der Graph rechts die Fläche, rückt es nach links nach. Liegt der Graph im ganzen Bereich außerhalb, fehlt das Label und das Log meldet `Package mathblatt Warning`. Leeres Label `{}` lässt das Label weg, auch bei `\gerade`.

Bei `\gerade` lässt sich die Stelle des Labels als optionales Argument setzen: `\gerade[1.5]{2}{-1}{g}` beschriftet die Gerade bei $x=1{,}5$. Liegt der Punkt dort außerhalb der Zeichenfläche, rückt die Vorlage das Label von selbst an den Rand, an dem die Gerade das Bild verlässt (ab 2026-09-07a; vorher konnte es unsichtbar wegfallen). Liegen mehrere Geraden in einem System, ziehst du die Labels damit auseinander, statt die Aufgabenwerte zu ändern. Fällt die gewählte Stelle aus der Zeichenfläche, rückt das Label automatisch an den Rand.
 
Zwei Systeme nebeneinander: `\end{ksys}\ksysabstand\begin{ksys}...`. Alle Grafiken – `ksys`, `\kreisdiagramm`, `\saeulen`, `\histogramm`, `\boxplots`, Baumdiagramme, Körper – stehen in einem eigenen Absatz: Leerzeile davor und danach. Auf derselben Zeile hängt die Grafik unter den Text, und was danach kommt (etwa `\leerfeld`), steht neben ihr statt darunter. Drei Systeme: zwei nebeneinander, Leerzeile, das dritte.
 
Koordinatensystem 3D (Kavalierprojektion)
 
```
\begin{ksys3}                                                     Oberstufe: x_1, x_2, x_3; Karo 5 mm
\begin{ksys3}[x1min=-2,x1max=6,x2min=-3,x2max=6,x3min=-2,x3max=5]   Voreinstellung; Bereiche ganzzahlig
\begin{ksys3}[xyz]                                                Sek I: Achsen x, y, z
\begin{ksys3}[...,x1schritt=2]                                    x1 nur bei 2, 4, 6 beziffert
\begin{ksys3}[leit]                                               Leitgrafik im Übersichtskasten: Karo 4 mm, alle Achsen 0..2
  \rpunkt{4}{4}{4}{A}                    Punkt mit Lot: entlang x1, dann parallel x2, dann parallel x3
  \rpunkt[below right]{6}{-2}{-1}{C}     Labelposition wie bei TikZ-Knoten (Voreinstellung above right)
  \rpunkt*{1}{1.5}{1.5}{S}               Punkt ohne Lot: Durchstoß-, Schnitt-, Spurpunkt
  \rvektor{2,4,3}{\vec a}                Ortsvektor vom Ursprung, Label in der Pfeilmitte
  \rvektorab[below]{1,1,0}{4,5,2}{\vec u}   Pfeil von A nach B; optionales Argument = Labelposition
  \rgerade{0,-2,1}{1,1,0.5}{g}           Stützpunkt, Richtungsvektor; läuft bis zum Rand des Achsenbereichs
  \rgerade[-1:1.5]{3,1,-1}{0,1,2}{h}     Parameterbereich t = −1 … 1,5 statt Rand; Label am Ende bei t max
  \rebene{4}{6}{3}{E}                    Spurdreieck aus den Achsenabschnitten x1 = 4, x2 = 6, x3 = 3
  \rebenepar{1,1,1}{2,1,0}{0,2,2}{F}     Parallelogramm: Stützpunkt, zwei Spannvektoren (werden als Pfeile gezeichnet)
  \rebenepar*{0,0,3}{4,0,1}{0,5,0}{D}    Sternform: Fläche ohne Spannvektorpfeile (Dach, Wand, Glasscheibe)
  \rquader{1,1,0}{3}{4}{2}               Quader: Ecke mit den kleinsten Koordinaten, Kanten a (x1), b (x2), c (x3)
  \rpyramide{1,3,0}{2}{3}{2,4.5,4}       Rechteckpyramide: Ecke, Grundkanten a (x1), b (x2), Spitze als Tripel
\end{ksys3}
```
 
x₂ waagerecht, x₃ senkrecht, x₁ unter 45° nach links unten mit halber Länge. Bildpunkt von (x₁|x₂|x₃) auf dem Papier ist (x₂ − ½x₁ | x₃ − ½x₁) in cm; eine Einheit sind 2 Karos, eine Einheit x₁ eine Karodiagonale. Alle drei Achsen sind beziffert, die Zahlen an x₁ stehen unter dem Teilstrich. Das 5-mm-Gitter legt die Umgebung am Ende hinter die gesamte gezeichnete Fläche; Punkte außerhalb der Achsbereiche liegen deshalb trotzdem auf Karo, die Achsen enden dann aber vor ihnen – Bereiche so wählen, dass alle Punkte darin liegen. `karo` ist wie bei `ksys` die Kantenlänge einer Gitterzelle in cm und bleibt bei 0.5.
 
`\rpunkt` zeichnet erst das Lot, dann den Punkt; das Label steht im Mathemodus. Koordinaten mit Dezimalpunkt (`2.5`). Negative Koordinaten in Labels und Aufgabentexten als `C(6|{-2}|{-1})` schreiben, sonst setzt LaTeX Binärabstände um das Minus. Um den Ursprung liegen die Zahlen dreier Achsen dicht beieinander; bei Karo 5 mm und x₁ bis 6 ist das lesbar, bei längerem x₁-Bereich `x1schritt=2` setzen.
 
Punkte und Vektoren der Vektor-, Geraden- und Ebenenmakros stehen als Tripel `{x1,x2,x3}` in einem Argument; nur `\rpunkt` und `\rebene` haben getrennte Argumente. Der Stützvektor einer Geraden oder Ebene ist nicht Teil des Makros – bei Bedarf `\rvektor{1,1,1}{\vec p}` davorsetzen. Vektorlabels sitzen in der Pfeilmitte; liegt die Mitte nahe einer Achse, kollidiert das Label mit der Bezifferung – dann die Position im optionalen Argument ändern (`[below right]`, `[above left]`). Ebenenlabels sitzen in der Flächenmitte; das optionale Argument nimmt Knotenoptionen wie `[above right]`. `\rebenepar` zeigt die Spannvektoren als Pfeile (Parameterform erklären), `\rebenepar*` nur die Fläche (ein Objekt im Raum: Dach, Wand). Eckpunkte setzt du mit `\rpunkt*` dazu.

`\rgerade` ohne Parameterbereich endet genau dort, wo die Gerade den Bereich x1min..x1max, x2min..x2max, x3min..x3max verlässt. Verlässt sie ihn über die x₁-Grenze, endet sie mitten im Bild – dann `x1max` vergrößern oder den Bereich als `[tmin:tmax]` vorgeben. Liegt die Gerade ganz außerhalb, warnt das Log (`Package mathblatt Warning`) und zeichnet t = −1 … 3. Richtungsvektoren, die ein Vielfaches von (2|1|1) sind, haben in dieser Projektion kein Bild (Gerade erscheint als Punkt) – solche Aufgabenwerte vermeiden. Das Spurdreieck braucht drei Achsenabschnitte; Ebenen parallel zu einer Achse zeichnest du als `\rebenepar` oder mit freiem TikZ.

`\rquader` und `\rpyramide` zeichnen nur die Kanten, verdeckte gestrichelt; der Betrachter steht in Richtung (2|1|1), sichtbar sind also die Flächen mit den größten Koordinaten, beim Quader sind die drei Kanten an der angegebenen Ecke verdeckt. Labels und Eckpunkte setzt du mit `\rpunkt*` (z. B. `\rpunkt*[below left]{4}{1}{0}{A}`), Höhen oder Diagonalen mit freiem TikZ (`\draw[dashed] (2.5,3,0) -- (2.5,3,4);`). Bei der Pyramide gilt: Grundfläche liegt in der Ebene x3 = Eckpunkt-x3, die Spitze darf beliebig liegen, auch schräg; negative Kantenlängen sind erlaubt und drehen die Richtung um. Ein Standardsystem fasst einen Quader mit Kanten bis etwa 4 und eine kleine Pyramide daneben, mehr nicht.

Innerhalb von `ksys3` gelten Raumkoordinaten. Was die Vorlage nicht als Makro hat, zeichnest du mit gewöhnlichem TikZ, z. B. `\draw[dashed] (1,2,0) -- (3,4,2);`; die Projektion übernimmt die Umgebung. Ein Standardsystem ist rund 13 cm breit, zwei nebeneinander passen nicht. `[leit]` ergibt ein etwa 4 cm großes System für den Übersichtskasten; weitere Schlüssel dahinter überschreiben es (`[leit,x2max=3]`). Nicht mit den Körpern auf ein Blatt (andere Blickrichtung, siehe unten).
 
Geometrie und Körper (Maße in cm)
 
```
\dreieckrw{4}{3}{a}{b}{c}                          rechtwinklig bei C
\dreieck{(0,0)}{(5,0)}{(1.5,3)}{a}{b}{c}{\alpha}{\beta}{\gamma}
\quader{4}{2}{3}{a}{b}{c}   \zylinder{1.2}{3}{r}{h}   \prismadreieck{4}{2.5}{2}{g}{h}{l}
\pyramide{4}{3}{3.5}{a}{b}{h}      Rechteckpyramide: Grundkanten a (vorn), b (Tiefe), Höhe h; quadratisch mit a = b
\kegel{1.5}{3}{r}{h}{s}            Radius, Höhe; Labels r, h, s (Mantellinie)
\kugel{1.5}{r}                     Radius
```
 
Kreis und Winkelfiguren

```
\begin{kreis}[2]                     Radius in cm (Voreinstellung 2)
  \mittelpunkt{M}                    \kreispunkt{110}{B}   \kreispunkt[above right]{110}{B}
  \radius{40}{r}                     \durchmesser{0}{d}    \sehne{200}{340}{s}
  \tangente{300}{t}                  Tangente im Randpunkt, rechter Winkel markiert
  \sektor{30}{110}{\alpha}           \bogen{30}{110}{b}
\end{kreis}
\geradenkreuzung{35}{\alpha}{\beta}{\gamma}{\delta}    zwei Geraden durch einen Punkt
\parallelenpaar{60}{\alpha}{\beta}{\gamma}{\delta}     zwei Parallelen mit Schnittgerade
\winkel{40}{\alpha}   \winkel[4]{40}{\alpha}           einzelner Winkel, Schenkellänge in cm
```

Winkel am Kreis (in der `kreis`-Umgebung): `\mittelpunktswinkel{200}{340}{\mu}` zeichnet die Schenkel von M zu den Randpunkten bei 200° und 340° mit Bogen an M; `\umfangswinkel{200}{340}{100}{\gamma}` die Sehnen vom Punkt bei 100° zu den beiden Randpunkten mit Bogen am Scheitel. Liegen die beiden Randpunkte einander gegenüber (Differenz 180°), setzt `\umfangswinkel` statt des Bogens die Rechtwinkelmarke – der Satz des Thales, den Durchmesser dazu mit `\durchmesser`. Die Punkte A, B, C beschriftest du mit `\kreispunkt`; das Makro zeichnet nur Linien, Bogen und den Scheitelpunkt. Immer wird der kleinere der beiden Winkel markiert. Das Label von `\mittelpunkt` und der Bogen des Mittelpunktswinkels liegen dicht beieinander; bei Bedarf `\mittelpunkt{}`.

Alle Winkel stehen in Grad und werden gegen den Uhrzeigersinn ab der Waagerechten gezählt: `\radius{40}{r}` zeigt nach rechts oben, `\radius{270}{r}` nach unten. Ein Sektor läuft vom ersten zum zweiten Winkel, ebenfalls gegen den Uhrzeigersinn. Die Labels von `\radius`, `\durchmesser` und `\sehne` stehen neben der Linie (Radius im Uhrzeigersinn daneben, Durchmesser darüber, Sehne außen). Soll ein Radius zu einem Sektor gehören, leg ihn auf einen Rand des Sektors, nicht in die Mitte, sonst stoßen r und Winkellabel zusammen. Der Kreis selbst hat kein Gitter; die Umgebung nimmt genau einen Kreis auf, mehrere Kreise setzt du nebeneinander mit `\hspace`.

Bei `\geradenkreuzung` liegt $\alpha$ rechts oben, $\beta$ links oben, $\gamma$ links unten (Scheitelwinkel zu $\alpha$), $\delta$ rechts unten. Bei `\parallelenpaar` gehören $\alpha$ und $\beta$ zur oberen Kreuzung, $\gamma$ und $\delta$ zur unteren, jeweils rechts oben und links oben; $\alpha$ und $\gamma$ sind damit Stufenwinkel, $\beta$ und $\delta$ ebenso. Die Parallelen werden so lang gezeichnet, dass beide Schnittpunkte darauf liegen, auch bei flachen Winkeln.

Vierecke, Netze, Strahlensatz (Maße in cm)

```
\viereck[seiten={a,b,c,d},diagonalen,hoehe,winkel]{(0,0)}{(5,0)}{(6,3)}{(1.5,3.5)}   Ecken A, B, C, D gegen den Uhrzeigersinn
\parallelogramm[seiten={a,b,a,b},hoehe,winkel={\alpha,\beta,,}]{4}{2.5}{60}       a, b, Winkel alpha
\rechteck[achsen=beide]{4}{2.5}       \trapez[hoehe=h]{5}{3}{2.5}   a unten, c oben (mittig), h
\raute[achsen=diagonalen,diagonalen]{4}{2.5}   Diagonalen e (waagerecht), f
\drachen[achsen=senkrecht,diagonalen]{4}{3}{0.35}   e senkrecht, f quer, t = Anteil von e bis zur Querdiagonale
\netzquader{3}{1.5}{2}{a}{b}{c}   \netzwuerfel{1.5}{a}   \netzpyramide{2.5}{2}{a}{h_s}   \netzzylinder{1}{2.5}{r}{h}
\strahlensatz[strecken={2,3,,5}]{2}{5}{35}          V-Figur: ZA, ZA', Winkel zwischen den Strahlen
\strahlensatz[x,strecken={2,4,a,b}]{2}{4}{30}       X-Figur
\strahlensatz[punkte={Z,A,B,C,D},faktor=1.5]{2}{4}{90}
```

`\viereck` nimmt vier Ecken als Koordinaten wie `\dreieck`; alle Zusätze sind Schlüssel: `punkte={A,B,C,D}` ist voreingestellt (`punkte=` lässt sie weg), `seiten={a,b,c,d}` beschriftet AB, BC, CD, DA, `diagonalen` zeichnet beide gestrichelt mit e (AC) und f (BD) – andere Labels als `diagonalen={e,}` –, `hoehe` fällt das Lot von D auf AB mit Rechtwinkelmarke und Label h (`hoehe=h_a` für ein anderes), `winkel` setzt Bögen mit α bis δ (`winkel={\alpha,,,\delta}` für eine Auswahl, immer der kleinere Winkel), `achsen=senkrecht|waagerecht|beide|diagonalen|alle` zeichnet Symmetrieachsen strichpunktiert durch die Figurenmitte bzw. durch die Diagonalen. Die Achsen werden nicht geprüft – bei einem allgemeinen Viereck zeichnet `achsen=beide` trotzdem zwei Linien. Die fünf Sonderformen sind nur Abkürzungen für Koordinaten und nehmen dieselben Schlüssel; beim Trapez liegt c mittig über a (gleichschenklig), beim Drachen liegt A unten und C oben auf der Symmetrieachse.

Netze: Umriss dick, Faltkanten dünn. `\netzquader` legt das Kreuz mit der Vorderfläche a × c in der Mitte, links und rechts b × c, oben und unten a × b, die Rückfläche rechts außen; Labels an der unteren Klappe (a), an der linken Fläche (b, c). Die Pyramide ist quadratisch mit Seitenhöhe h_s, gestrichelt im unteren Dreieck. Der Zylinder zeigt das Mantelrechteck 2πr × h mit den beiden Deckkreisen oben links und unten links und dem Hinweis u = 2πr unter dem Rechteck. Ein Quadernetz mit a = 3 ist rund 9 cm breit; zwei Netze passen nebeneinander, wenn die Kanten klein bleiben.

`\strahlensatz` zeichnet zwei Strahlen von Z mit den Parallelen durch A und A′ (Abstände ZA und ZA′ auf dem ersten Strahl, Winkel dazwischen); B und B′ liegen auf dem zweiten Strahl mit ZB = faktor · ZA (Voreinstellung 1,3). `[x]` legt A und A′ auf verschiedene Seiten von Z (X-Figur). `strecken` beschriftet in der V-Figur ZA, AA′, AB, A′B′, in der X-Figur ZA, ZA′, AB, A′B′ – leere Einträge bleiben frei; Zahlen wie `2` oder `3{,}5` gehen direkt, es sind Mathelabels. `punkte` ersetzt die fünf Punktnamen in der Reihenfolge Z, A, B, A′, B′.

Leere Beschriftung `{}` lässt das Label weg – in allen Makros dieses Abschnitts und bei den Körpern. Beim Prisma ist `h` die Höhe des Grunddreiecks; sie wird als gestrichelte Linie mit Rechtwinkelmarke in der Vorderfläche gezeichnet, das Label steht rechts daneben. Beim Zylinder liegt `r` auf der gestrichelten Radiuslinie in der Deckfläche. Pyramide und Kegel zeigen die Höhe gestrichelt mit Fußpunkt und Rechtwinkelmarke, das Label `h` steht links davon; beim Kegel liegt `r` auf der Radiuslinie der Grundfläche, `s` an der rechten Mantellinie. Bei der Pyramide werden verdeckte Kanten aus den Maßen bestimmt – bei flachen Pyramiden ist die linke Seitenfläche sichtbar, dann ist die hintere linke Kante durchgezogen; das ist richtig. Die Körper sind in Kavalierprojektion mit der Tiefe nach rechts oben gezeichnet – das ist eine andere Blickrichtung als beim räumlichen Koordinatensystem, deshalb gehören Körper und 3D-System nicht nebeneinander auf ein Blatt.
 
Stochastik
 
```
\baumzwei{R/0.4,B/0.6}{R/0.4,B/0.6}{R/0.4,B/0.6}    zweistufig, Wahrscheinlichkeiten
\baumzwei{R/,B/}{R/,B/}{R/,B/}                      leere Felder zum Eintragen
\saeulen{Mo/12,Di/7,Mi/9}{16}{4}{Anzahl}            Werte, ymax, ystep, Achsentitel
\saeulen{Mo/,Di/,Mi/}{16}{4}{Anzahl}                nur Achsen (Schüler zeichnet)
```
 
`\baumzwei` trägt genau zwei Äste je Stufe; ein dritter Eintrag in der ersten Stufe wird ohne Folgestufe gezeichnet. Wahrscheinlichkeiten stehen im Mathemodus, Dezimalkomma also als `0{,}4`, Brüche als `\frac{2}{5}`.

```
\baumdreigleich{R/0{,}4,B/0{,}6}                                   dreistufig, alle Stufen gleich (mit Zurücklegen)
\baumdrei{S1}{S2 nach 1. Ast}{S2 nach 2. Ast}{S3 nach 1-1}{S3 nach 1-2}{S3 nach 2-1}{S3 nach 2-2}
\baumdrei{R/\frac{2}{5},B/\frac{3}{5}}{R/\frac{1}{4},B/\frac{3}{4}}{R/,B/}{R/,B/}{R/,B/}{R/,B/}{R/,B/}
\kreisdiagramm{Bus 40 \%/40, Rad 25 \%/25, Auto 20 \%/20, zu Fuß 15 \%/15}
\kreisdiagramm[1.2]{A/3, B/5, /2}       Radius in cm (Voreinstellung 1,8); leeres Label = Sektor ohne Text
\kreisdiagramm{}                         leerer Kreis mit Mittelpunkt (Schüler zeichnet)
\kreissektor{135}{135°}                  Kreis mit einem grauen Sektor von 135° ab oben, Label im Sektor
\vierfeldertafel{A}{B}{20,30,50,10,40,50,30,70,100}   zeilenweise B, nicht B, Summe; leere Einträge frei
\vierfeldertafel{A}{B}{}                 alle Felder leer
\binomialverteilung{10}{0.3}                                  Stabdiagramm P(X=k), k = 0..n
\binomialverteilung[von=15,bis=35,markiere=15:22]{50}{0.5}    Ausschnitt, Stäbe 15..22 dunkel
\binomialverteilung[ymax=0.4,ystep=0.1]{5}{0.7}               y-Achse selbst gesetzt
\normalverteilung{0}{1}                                       Dichtekurve, x-Achse in Schritten von sigma
\normalverteilung[von=90,bis=110]{100}{10}                    Fläche grau; nur von oder nur bis = einseitig
\normalverteilung[xstep=10,karo=0.5]{50}{15}
```

`\baumdrei` hat sieben Listen: erste Stufe, zweite Stufe nach dem ersten und zweiten Ast, dritte Stufe nach den vier Pfaden in der Reihenfolge 1-1, 1-2, 2-1, 2-2. Bei gleichen Wahrscheinlichkeiten auf allen Stufen genügt `\baumdreigleich` mit einer Liste. Zwei Äste je Stufe; der Baum ist rund 8 cm breit und 5,5 cm hoch, zwei nebeneinander passen.

Beim `\kreisdiagramm` bestimmen die Werte nur die Winkel; ob du Prozent oder absolute Zahlen gibst, ist gleich. Was am Sektor stehen soll, schreibst du selbst ins Label, im Textmodus (`Bus 40 \%`). Die Sektoren beginnen oben und laufen im Uhrzeigersinn, in vier wechselnden Grautönen. Die Labels stehen außen; bei vielen kleinen Sektoren nebeneinander überlappen sie, dann `{}` und eine Legende im Text. Sektoren über 50 % sind seit 2026-09-06a möglich. Ein einzelner grauer Sektor mit Winkelangabe (Aufgabe „Anteil des Sektors"): `\kreissektor`.

Die `\vierfeldertafel` nimmt die Merkmale A (Spalten) und B (Zeilen); die Gegenereignisse setzt sie selbst mit Überstrich. Die neun Werte stehen zeilenweise: erst die Zeile B (A, nicht A, Summe), dann nicht B, dann die Summenzeile. Alle neun Kommas müssen stehen, auch wenn Einträge leer bleiben. Werte im Mathemodus, Dezimalkomma als `0{,}2`.

`\binomialverteilung` rechnet P(X=k) selbst. Ohne Schlüssel läuft k von 0 bis n und die y-Achse passt sich dem größten Wert an. Ab n > 25 zeigt die Vorlage nur die k mit P(X=k) ≥ 0,0005 und meldet den Bereich im Log; mit `von`/`bis` legst du ihn selbst fest. Ein Stab ist ein Karo breit (0,5 cm), mehr als 30 Stäbe passen nicht in die Zeile. `markiere=a:b` färbt die Stäbe a bis b dunkel, etwa für P(X ≤ 3) oder P(15 ≤ X ≤ 22). Die Werte stehen nicht an den Stäben; wer sie braucht, setzt eine Tabelle daneben.

`\normalverteilung` zeichnet die Dichtekurve über μ ± 3,5σ, die x-Achse in Schritten von σ ab dem ersten Vielfachen von `xstep` im Bereich, das Maximum ist vier Karos hoch, eine y-Achse mit Zahlen gibt es nicht. Bei krummen σ (6,5) werden die Achsenzahlen krumm (149,5; 156; …), dann `xstep` auf einen runden Wert setzen. Mit `von`/`bis` färbst du eine Fläche; fehlt eine Grenze, geht die Fläche bis zum Rand. Für z-Werte `\normalverteilung{0}{1}`.

Boxplot und Histogramm

```
\begin{boxplots}[xmin=0,xmax=20,xstep=2,xlabel=Punkte]
  \bp{4,7,9,13,18}{Klasse 8a}    Minimum, unteres Quartil, Median, oberes Quartil, Maximum
  \bp{}{Klasse 8b}               leere Werte: nur Zeile und Label, Schüler zeichnet selbst
\end{boxplots}
\histogramm[ymax=10,ystep=2,xstep=10,ylabel=$h$]{0:10/4, 10:20/9, 20:30/6}
\histogramm[dichte,ymax=1,ystep=0.2,xstep=10,ylabel=Dichte]{0:10/4, 10:20/9, 20:40/6}
\histogramm[ymax=8,ystep=2,xstep=5]{0:5/, 5:10/, 10:15/}     ohne Werte: Achsen und Klassengrenzen
\histogramm[titel=Histogramm I,ymax=10,ystep=2,xstep=10]{...}   Titel im Textmodus über dem Diagramm
```

Die Boxplots einer Umgebung teilen sich eine Achse und stehen in der Reihenfolge der `\bp`-Zeilen von unten nach oben; das Label steht links außerhalb und im Textmodus, `\bp{...}{Klasse 8a}` also ohne Dollarzeichen. Liegt ein Wert außerhalb von `xmin`..`xmax`, zeichnet die Vorlage ihn trotzdem und meldet es als `Package mathblatt Warning`.

Beim `\histogramm` schreibst du jede Klasse als `von:bis/Höhe`, durch Komma getrennt; die Klassen müssen aneinandergrenzen und aufsteigend stehen. Ohne `dichte` ist die Höhe die Häufigkeit – das passt nur bei gleich breiten Klassen. Bei ungleichen Breiten setzt du `dichte`: dann teilt die Vorlage die angegebene Häufigkeit durch die Klassenbreite, und die Fläche entspricht der Häufigkeit. Lässt du die Höhe weg (`0:10/`), entstehen nur Achsen, Gitter und Klassengrenzen.

`karo`, `xstep` und `ystep` wirken bei beiden wie beim `ksys`: `karo` ist die Kantenlänge einer Gitterzelle (0,5 cm), `xstep`/`ystep` der Wert je Zelle. `xlabel` und `ylabel` stehen im Textmodus. Die Achsenzahlen werden wie beim `ksys` automatisch verkleinert und ausgedünnt.
 
Analysis (im ksys, `\ableitungspaar` freistehend)

```
\ableitungspaar[xmin=-3,xmax=3,ymin=-2,ymax=4,ymin2=-4,ymax2=4,ablesen]{0.5*\x^2-1}{f}{\x}{f'}
\ableitungspaar[...]{\x^3-3*\x}{f}{}{f'}         unteres System leer: Schüler zeichnet f'
\flaeche{\x^2-4*\x+3}{1}{3}{A}                   Fläche zwischen Graph und x-Achse von 1 bis 3
\flaechezwischen{-\x^2+2*\x+3}{\x+1}{-1}{2}{A}   Fläche zwischen zwei Graphen
\tangentean{0.5*\x^2}{1}{t}                      Tangente in x0 = 1 mit Steigungsdreieck
\tangentean*{0.5*\x^2}{1}{t}                     ohne Steigungsdreieck
\tangentean[\frac{3}{2}]{0.5*\x^2}{1.5}{t}       Steigungstext selbst gesetzt
\hochpunkt{-1}{2}{H}   \tiefpunkt{1}{-2}{T}   \wendepunkt{0}{0}{W}   \wendepunkt[-3]{0}{0}{W}
\asymptote{x=2}{}   \asymptote{y=1}{y=1}   \asymptote{y=0.5*\x}{a}
```

`\ableitungspaar` setzt zwei Systeme mit gleicher x-Achse untereinander, oben f, unten f′, Ursprünge bündig. Die Schlüssel gelten für beide; `ymin2`, `ymax2`, `ystep2`, `ylabel2` überschreiben den y-Bereich des unteren Systems. Ein leerer Term lässt das jeweilige System leer. Beide Terme gibst du selbst an – die Vorlage leitet nicht ab. Das Paar ist etwa doppelt so hoch wie ein einzelnes System; mit `ablesen` bleibt Platz für Text daneben.

`\flaeche` färbt die Fläche zwischen Graph und x-Achse grau, `\flaechezwischen` die zwischen zwei Graphen; Flächen unterhalb der Achse und mit Vorzeichenwechsel werden genauso gefärbt, ohne Unterscheidung. Das Label steht in der Mitte der Fläche (bei schmalen Flächen ragt es heraus, dann `{}` und Text daneben). Die Graphen selbst zeichnest du mit `\funktion` oder `\gerade` dazu – die Fläche hat nur einen dünnen Rand.

`\tangentean` bestimmt die Steigung numerisch aus dem Term, zeichnet die Tangente wie `\gerade` (Label am Rand), markiert den Berührpunkt und legt ein Steigungsdreieck an: 1 nach rechts, m senkrecht, Steigungstext mit zwei Nachkommastellen (1,5; −2; 0,33). Für exakte Werte (Brüche, Wurzeln) gibst du den Text im optionalen Argument vor. Liegt x0 nahe am rechten Rand, kippt das Dreieck nach links. Das Dreieck ist an 1 Einheit gebunden: bei `xstep` größer 1 wird es sehr klein, dann `\tangentean*`.

`\hochpunkt` und `\tiefpunkt` setzen Punkt und Label über bzw. unter dem Punkt, `\wendepunkt` rechts oben; mit optionaler Steigung `[m]` zeichnet `\wendepunkt` ein kurzes gestricheltes Stück der Wendetangente, `[0]` für den Sattelpunkt. Die Koordinaten gibst du an – die Vorlage rechnet keine Extremstellen.

`\asymptote` nimmt `x=Wert` (senkrecht) oder `y=Term` (waagerecht oder schräg, Term in `\x`) und zeichnet gestrichelt über die ganze Zeichenfläche. Der Graph selbst wird bei einer Polstelle in zwei Stücken mit `\funktionab` gezeichnet, links und rechts der Lücke; das zweite Stück bekommt ein leeres Label.

Zahlen und Algebra

```
\zahlenstrahl{-3/A, 1.5/B, 4/}                                  Punkte mit Label (leer = nur Markierung)
\zahlenstrahl[xmin=0,xmax=2,xstep=0.25,karo=0.7]{0.5/\frac12}   karo = cm je Schritt
\zahlenstrahl{}                                                 nur die Gerade
\begin{zahlengerade}[xmin=-4,xmax=6]
  \intervall{-2}{3}{[-2;3]}        geschlossen (volle Enden)
  \intervallo[2]{1}{5}{]1;5[}      offen (leere Enden); [2] = zweite Zeile, wenn sich Intervalle überschneiden
  \intervall*[3]{-3}{0}{}          links offen, rechts geschlossen;  \intervallo*  links geschlossen, rechts offen
  \intervallo*[4]{2}{}{x \ge 2}    Grenze leer = Pfeil ins Unendliche
\end{zahlengerade}
\bruchkreis{3}{8}   \bruchkreis[0.8]{1}{3}   \bruchkreis{0}{6}      Teile gefüllt/gesamt; [r] Radius in cm
\bruchrechteck{3}{8}   \bruchrechteck[3]{2}{5}                      [Breite] in cm, Höhe 1 cm
\termbaum{+}{3x}{\tb{\cdot}{2}{y}}           Kinder sind Text (Blatt) oder \tb{Knoten}{Kind}{Kind}
\termbaum{}{\tb{}{5}{x}}{\tb{}{}{}}          leere Knoten = Felder zum Eintragen
```

Der Zahlenstrahl setzt die Zahlen mit Komma und dünnt sie wie das `ksys` aus, wenn sie nicht in einen Schritt passen. Punkte und Labels stehen oben, Labels im Mathemodus. `zahlengerade` ist die Umgebung dahinter: darin liegen die Intervalle als dicke Striche über der Achse, Zeile 1 direkt darüber, weitere Zeilen mit dem optionalen Argument. Ungleichungen (`x < -1`, `x \ge 2`) sind Intervalle mit leerer Grenze. Die Grenzen selbst schreibst du mit Dezimalpunkt.

Im `\termbaum` stehen alle Knoten im Mathemodus (`\cdot`, `\frac{d}{2}`, `x^2`); die Tiefe ist frei, ab vier Ebenen werden die Blätter eng. Der Baum ist nur binär.

Trigonometrie

```
\einheitskreis{50}                Einheitskreis mit Punkt P, Radius, Winkel alpha, sin und cos als Strecken
\einheitskreis[karo=1.5]{140}     Radius in cm (Voreinstellung 2)
\einheitskreis[ohne]{230}         nur Punkt, Radius und Winkel (Schüler trägt sin/cos ein)
\begin{ksys}[trigo]               x von -pi/2 bis 2pi in pi/2-Schritten (Karo 1 cm), y von -2 bis 2
  \sinus{1}{1}{f}                 a*sin(b*x)      \kosinus{2}{0.5}{g}   a*cos(b*x)
  \hochpunkt{1.5708}{1}{H}        Stellen in Bogenmaß als Dezimalzahl: pi/2 = 1.5708, pi = 3.1416, 2pi = 6.2832
\end{ksys}
\begin{ksys}[trigo,xmax=12.5664,ymin=-3,ymax=3]   bis 4pi (vier Nachkommastellen, sonst fehlt die letzte Zahl)
```

`trigo` ist ein Stil des `ksys` wie `leit`: weitere Schlüssel dahinter überschreiben ihn. Er setzt die x-Zahlen als Vielfache von π (`\tfrac{\pi}{2}`, `\pi`, `\tfrac{3\pi}{2}`); das funktioniert nur mit `xstep=1.5708` oder ganzen Vielfachen davon. Der Einheitskreis beschriftet immer mit α, sin α, cos α und P – für Aufgaben mit konkreten Werten steht die Gradzahl im Aufgabentext.

Noch nicht in Stufe 3
 
Zweitafelprojektion; im 3D-System Spurgeraden, Ebenen ohne Achsenabschnitte, Kegel/Kugel/Zylinder. Die Bausteinliste Stufe 3 ist damit abgearbeitet.
