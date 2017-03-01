from GUI import *


class SpielStarten:
    gui = GUI()
    if gui.starten():
        sp = gui.getStartPos()
        sk = gui.getStartKap()
        sa = gui.getSpielerAnzahl()
        sw = gui.getWdh()
        s = []
        for i in range(1, sa + 1):
            s.append("Spieler" + str(i))
        spiel = Spiel(s, sk, sp)
