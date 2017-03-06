from GUI import *
from Spielfeld import spielfeld


class SpielStarten:
    def __init__(self):
        self.auswertungsliste = []
        self.gui = GUI()
        self.gui.erstellen()
        startbar = self.gui.startbar()

        if startbar is True:
            sp = self.gui.getStartPos()
            sk = self.gui.getStartKap()
            sa = self.gui.getSpielerAnzahl()
            sw = self.gui.getWdh()
            s = [i for i in range(1, sa + 1)]
            self.spiel = Spiel(s, sk, sp)
            for i in range(sw):
                self.spiel.__init__(s, sk, sp)
                self.auswertungsliste.append(self.schleife())
            # self.gui.auswertungstext(Auswertung.durchschnitt(self.auswertungsliste))
            print(Auswertung.durchschnitt(self.auswertungsliste))

    def schleife(self):
        spiel = self.spiel.spiel
        gewinnerstehtnichtfest = True
        #print('Spieler', len(spiel))
        self.gui.spielanimation(len(spiel))
        # Spielschleife wird ausgeführt solange mehr als ein Spieler noch drin ist
        while gewinnerstehtnichtfest:
            # jeder for-schleifen-zyklus ist eine Runde aller Spieler
            for i in spiel:
                # Wenn Spieler nicht im Gefängnis ist wird gewürfelt
                i.im_gefaengnis is False and i.wuerfeln()
                self.gui.spielfeldpos_aendern(i, Spieler.getPos(i))
                i.feldchecken(self.spiel)
                # wenn Spieler unter 1 Euro hat wird er aus dem Spiel entfernt und seine Strassen wieder kaufbar gemacht
                if i.geld < 1:
                    print(i.name, "ist aus dem Spiel")
                    self.spiel.spielerzurücksetzen(i.name)
                    del spiel[spiel.index(i)]
            # wenn nur noch 1 Spieler im Spiel ist wird die Schleife beendet
            if len(spiel) == 1:
                gewinnerstehtnichtfest = False
        print("Spieler", spiel[0].name, "gewinnt mit", spiel[0].geld)
        return spiel[0].geld


class Auswertung:
    # Methode um aus einem Array den Durchschnittswert zu bilden
    @staticmethod
    def durchschnitt(liste):
        return liste[0] if len(liste) == 1 else sum(liste) / (len(liste) - 1)

    # Methode um aus einem Array den Median zu bilden
    @staticmethod
    def median(liste):
        mitte = (len(liste) - 1) / 2
        return liste[int(mitte)] if mitte.is_integer() else (liste[int(mitte)] + liste[int(mitte + 1)]) / 2


SpielStarten()
