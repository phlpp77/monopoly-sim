from Karten import *

class SpielFeld:
    #Haeuser
    Badstrasse = HausKarten(60, [2, 10, 30, 90, 160, 250], 50)
    Turmstrasse = HausKarten(60, [4, 20, 60, 180, 320, 450], 50)
    Chausseestrasse = HausKarten(100, [6, 3, 90, 270, 400, 550], 50)
    Elisenstrasse = HausKarten(100, [6, 30, 90, 270, 400, 550], 50)
    Poststrasse = HausKarten(120, [8, 40, 100, 300, 450, 600], 50)
    Seestrasse = HausKarten(140, [10, 50, 150, 450, 625, 750], 100)
    Hafenstrasse = HausKarten(140, [10, 50, 150, 450, 625, 750], 100)
    NeueStrasse = HausKarten(160, [12, 60, 180, 500, 700, 900], 100)
    MuenchnerStrasse = HausKarten(180, [14, 70, 200, 550, 750, 950], 100)
    WienerStrasse = HausKarten(180, [14, 70, 200, 550, 750, 950], 100)
    BerlinerStrasse = HausKarten(200, [16, 80, 220, 600, 800, 1000], 150)
    Theaterstrasse = HausKarten(220, [18, 90, 250, 700, 875, 1050], 150)
    Museumsstrasse = HausKarten(220, [18, 90, 250, 700, 875, 1050], 150)
    Opernplatz = HausKarten(240, [20, 100, 300, 750, 925, 1100], 150)
    Lessingstrasse = HausKarten(260, [22, 110, 330, 800, 975, 1150], 150)
    Schillerstrasse = HausKarten(260, [22, 110, 330, 800, 975, 1150], 150)
    Goethestrasse = HausKarten(280, [24, 120, 360, 850, 1025, 1200], 150)
    Rathausplatz = HausKarten(300, [26, 130, 390, 900, 1100, 1275], 200)
    Hauptstrasse = HausKarten(300, [26, 130, 390, 900, 1100, 1275], 200)
    Bahnhofstrasse = HausKarten(320, [28, 150, 450, 1000, 1200, 1400], 200)
    Parkstrasse = HausKarten(350, [35, 175, 500, 1100, 1300, 1500], 200)
    Schlossallee = HausKarten(400, [50, 200, 600, 1400, 1700, 2000], 200)
    #Bahnhoefe
    Suedbahnhof = HausKarten(200, [25], 0)
    Westbahnhof = HausKarten(200, [25], 0)
    Nordbahnhof = HausKarten(200, [25], 0)
    Hauptbahnhof = HausKarten(200, [25], 0)
    #Werke
    Elektrizitaetswerk = Werke()
    Wasserwerk = Werke()
    #nichtHaus Karten
    Ereignisfeld = nichtHaus("Ereignisfeld")
    Gemeinschaftsfeld = nichtHaus("Gemeinschaftsfeld")
    Einkommenssteuer = nichtHaus("Einkommenssteuer")
    Zusatzsteuer = nichtHaus("Zusatzsteuer")
    Los = nichtHaus("Los")
    Gefaengnis = nichtHaus("Gefaengnis")
    FreiParken = nichtHaus("Frei Parken")
    InsGefaengnis = nichtHaus("Ins Gefaengnis")

    # alle Karten in eine Liste packen
    Feld = [Badstrasse, Gemeinschaftsfeld, Turmstrasse, Einkommenssteuer, Suedbahnhof, Chausseestrasse, Ereignisfeld,
            Elisenstrasse, Poststrasse, Gefaengnis, Seestrasse, Elektrizitaetswerk, Hafenstrasse, NeueStrasse,
            Westbahnhof, MuenchnerStrasse, Gemeinschaftsfeld, WienerStrasse, BerlinerStrasse, FreiParken,
            Theaterstrasse, Ereignisfeld, Museumsstrasse, Opernplatz, Nordbahnhof, Lessingstrasse, Schillerstrasse,
            Wasserwerk, Goethestrasse, InsGefaengnis, Rathausplatz, Hauptstrasse, Gemeinschaftsfeld, Bahnhofstrasse,
            Hauptbahnhof, Ereignisfeld, Parkstrasse, Zusatzsteuer, Schlossallee]
