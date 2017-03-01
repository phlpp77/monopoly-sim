from GUI import *


class SpielStarten:
    gui = GUI()
    gui.erstellen()
    if testV == 1:
        print("t = 1")
    '''
    if gui.erstellen() is True:
        sp = gui.getStartPos()
        sk = gui.getStartKap()
        sa = gui.getSpielerAnzahl()
        sw = gui.getWdh()
        s = []
        for i in range(1, sa + 1):
            s.append("Spieler" + str(i))
        spiel = Spiel(s, sk, sp)
    '''