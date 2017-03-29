from GUI import *
from Spieler import *
from time import sleep


class SpielStarten:
    def __init__(self):
        self.auswertungsliste = []

        self.gui = GUI()
        self.gui.erstellen()
        startbar = self.gui.startbar()
        # self.animation = Animation()

        if startbar is True:
            sp = self.gui.getStartPos()
            sk = self.gui.getStartKap()
            sa = self.gui.getSpielerAnzahl()
            sw = self.gui.getWdh()
            res = self.gui.getResolution()
            self.zeit = self.gui.getZeit()
            # print(self.gui.getWdh())
            spieler = [i for i in range(sa)]
            # um das Spielfenster kleiner zu öffnen die übergebene Zahl zur Animation verringern
            self.animation = Animation(sa, res)
            self.spiel = Spiel(spieler, sk, sp)
            # self.animation.figuren_erstellen(sa)

            # self.animation.setDaemon(True)
            # self.animation.run()

            i = 1
            while i <= sw:
                self.spiel.__init__(spieler, sk, sp)
                self.auswertungsliste.append(self.schleife())
                i += 1

            print("Durchschnittlich wurde das Spiel mit", Auswertung.durchschnitt(self.auswertungsliste), "beendet.")

    def schleife(self):
        spiel = self.spiel.spiel
        gewinnerstehtnichtfest = True
        # Spielschleife wird ausgeführt solange mehr als ein Spieler noch drin ist
        while gewinnerstehtnichtfest:
            # jeder for-schleifen-zyklus ist eine Runde aller Spieler
            for i in spiel:
                # Wenn Spieler nicht im Gefängnis ist wird gewürfelt
                i.im_gefaengnis is False and i.wuerfeln()
                sleep(self.zeit)
                self.animation.pos_aendern(spiel.index(i), i.pos)
                # print("hat gewürfelt")
                # self.animation.spielfeldpos_aendern(spiel.index(i), i.get_pos())
                i.feldchecken(self.spiel.spiel)
                # wenn Spieler unter 1 Euro hat wird er aus dem Spiel entfernt und seine Strassen wieder kaufbar gemacht
                if i.geld < 1:
                    # print(i.name, "ist aus dem Spiel")
                    self.spiel.spielerzurücksetzen(i.name)
                    del spiel[spiel.index(i)]
            # wenn nur noch 1 Spieler im Spiel ist wird die Schleife beendet
            if len(spiel) == 1:
                gewinnerstehtnichtfest = False
        print("Spieler", spiel[0].name, "gewinnt mit", spiel[0].geld)
        geld = spiel[0].geld
        self.spiel.spielerzurücksetzen(spiel[0].name)
        print("Das Spiel hätte", round(spiel[0].get_spielzeit("h"), 2), "Stunden gebraucht")
        del spiel[0]
        return geld


class Auswertung:
    # Methode um aus einem Array den Durchschnittswert zu bilden
    @staticmethod
    def durchschnitt(liste):
        return liste[0] if len(liste) == 1 else int(sum(liste) / len(liste))

    # Methode um aus einem Array den Median zu bilden
    @staticmethod
    def median(liste):
        mitte = (len(liste) - 1) / 2
        return liste[int(mitte)] if mitte.is_integer() else int((liste[int(mitte)] + liste[int(mitte + 1)]) / 2)


SpielStarten()
