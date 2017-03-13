from Karten import *


class Spielfeld:
    # ---Listen für Häuser---
    kaufpreise = [60, 60, 100, 100, 120, 140, 140, 160, 180, 180, 200, 220, 220, 240, 260, 260, 280, 300, 300, 320, 350,
                  400]
    mieten = [[2, 10, 30, 90, 160, 250], [4, 20, 60, 180, 320, 450], [6, 30, 90, 270, 400, 550],
              [6, 30, 90, 270, 400, 550], [8, 40, 100, 300, 450, 600], [10, 50, 150, 450, 625, 750],
              [10, 50, 150, 450, 625, 750], [12, 60, 180, 500, 700, 900], [14, 70, 200, 550, 750, 950],
              [14, 70, 200, 550, 750, 950], [16, 80, 220, 600, 800, 1000], [18, 90, 250, 700, 875, 1050],
              [18, 90, 250, 700, 875, 1050], [20, 100, 300, 750, 925, 1100], [22, 110, 330, 800, 975, 1150],
              [22, 110, 330, 800, 975, 1150], [24, 120, 360, 850, 1025, 1200], [26, 130, 390, 900, 1100, 1275],
              [26, 130, 390, 900, 1100, 1275], [28, 150, 450, 1000, 1200, 1400], [35, 175, 500, 1100, 1300, 1500],
              [50, 200, 600, 1400, 1700, 2000]]
    # Baukosten
    bkosten = [50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 150, 150, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200]
    # "Farben" der Felder
    farben = [2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9]
    feldhaeufigkeiten = [4, 2, 2, 3, 3, 3, 3, 3, 3, 2]

    # ---Liste für NichtHäuser---
    typen = ["Los", "Gemeinschaftsfeld", "Einkommenssteuer", "Ereignisfeld", "Gefaengnis", "Gemeinschaftsfeld",
             "Frei Parken", "Ereignisfeld", "Ins Gefaengnis", "Gemeinschaftsfeld", "Ereignisfeld", "Zusatzsteuer"]
    # --- Liste über der iteriert wird, um zu wissen, wielcher Typ von Straße wo hin gehört
    strassenliste = [3, 0, 3, 0, 3, 1, 0, 3, 0, 0, 3, 0, 2, 0, 0, 1, 0, 3, 0, 0, 3, 0, 3, 0, 0, 1, 0, 0, 2, 0, 3, 0, 0,
                     3, 0, 1, 3, 0, 3, 0]

    feld = []
    counter = [0] * 2
    for i in strassenliste:
        if i == 0:
            c = counter[0]
            feld.append(HausKarten(kaufpreise[c], mieten[c], bkosten[c], farben[c]))
            counter[0] += 1
        elif i == 1:
            feld.append(Bahnhoefe())
        elif i == 2:
            feld.append(Werke())
        else:
            feld.append(NichtHaus(typen[counter[1]]))
            counter[1] += 1
