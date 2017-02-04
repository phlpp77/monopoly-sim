from Karten import *


class SpielFeld:
    # Haeuser
    Badstrasse = HausKarten(60, [2, 10, 30, 90, 160, 250], 50, 1)
    Turmstrasse = HausKarten(60, [4, 20, 60, 180, 320, 450], 50, 1)
    Chausseestrasse = HausKarten(100, [6, 3, 90, 270, 400, 550], 50, 2)
    Elisenstrasse = HausKarten(100, [6, 30, 90, 270, 400, 550], 50, 2)
    Poststrasse = HausKarten(120, [8, 40, 100, 300, 450, 600], 50, 2)
    Seestrasse = HausKarten(140, [10, 50, 150, 450, 625, 750], 100, 3)
    Hafenstrasse = HausKarten(140, [10, 50, 150, 450, 625, 750], 100, 3)
    NeueStrasse = HausKarten(160, [12, 60, 180, 500, 700, 900], 100, 3)
    MuenchnerStrasse = HausKarten(180, [14, 70, 200, 550, 750, 950], 100, 4)
    WienerStrasse = HausKarten(180, [14, 70, 200, 550, 750, 950], 100, 4)
    BerlinerStrasse = HausKarten(200, [16, 80, 220, 600, 800, 1000], 150, 4)
    Theaterstrasse = HausKarten(220, [18, 90, 250, 700, 875, 1050], 150, 5)
    Museumsstrasse = HausKarten(220, [18, 90, 250, 700, 875, 1050], 150, 5)
    Opernplatz = HausKarten(240, [20, 100, 300, 750, 925, 1100], 150, 5)
    Lessingstrasse = HausKarten(260, [22, 110, 330, 800, 975, 1150], 150, 6)
    Schillerstrasse = HausKarten(260, [22, 110, 330, 800, 975, 1150], 150, 6)
    Goethestrasse = HausKarten(280, [24, 120, 360, 850, 1025, 1200], 150, 6)
    Rathausplatz = HausKarten(300, [26, 130, 390, 900, 1100, 1275], 200, 7)
    Hauptstrasse = HausKarten(300, [26, 130, 390, 900, 1100, 1275], 200, 7)
    Bahnhofstrasse = HausKarten(320, [28, 150, 450, 1000, 1200, 1400], 200, 7)
    Parkstrasse = HausKarten(350, [35, 175, 500, 1100, 1300, 1500], 200, 8)
    Schlossallee = HausKarten(400, [50, 200, 600, 1400, 1700, 2000], 200, 8)
    # Bahnhoefe
    Suedbahnhof = Bahnhoefe()
    Westbahnhof = Bahnhoefe()
    Nordbahnhof = Bahnhoefe()
    Hauptbahnhof = Bahnhoefe()
    # Werke
    Elektrizitaetswerk = Werke()
    Wasserwerk = Werke()
    # nichtHaus Karten
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
