from GUI import *


class SpielStarten:
    gui = GUI()
    gui.erstellen()
    startbar = gui.startbar()
    print(startbar)

    if startbar is True:
        sp = gui.getStartPos()
        sk = gui.getStartKap()
        sa = gui.getSpielerAnzahl()
        sw = gui.getWdh()
        s = []
        for i in range(1, sa + 1):
            s.append("Spieler" + str(i))
        spiel = Spiel(s, sk, sp)
        Auswertung(spiel, gui)

class Auswertung:
    def __init__(self, spiel, gui):
        auswertungsliste = []
        if sw > 1:
            for i in range(sw - 1):
                auswertungsliste.append(spiel.schleife())
        endtext = (
        "Gewinner haben durchschnittlich", round(gui.durchschnitt(auswertungsliste), 2), "Euro, in einem Spiel mit",
        wdh, "Runden und einem Startkapital von", sk, "Euro bekommen.\nDas Spiel wurde an Feldnummer",
        sp, "gestartet.")

        Label(gui.hauptfenster, text=endtext).grid(row=6, column=1)
        gui.hauptfenster.update()