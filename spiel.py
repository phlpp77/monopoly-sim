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
        if sw > 1:
            for i in range(sw-1):
                spiel.__init__(s, sk, sp)
