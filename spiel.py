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
            print(Auswertung.durchschnitt(self.auswertungsliste))
            print(Auswertung.median(self.auswertungsliste))
            self.gui.auswertungstext(Auswertung.durchschnitt(self.auswertungsliste))

    def schleife(self):
        spiel = self.spiel.spiel
        gewinnerstehtnichtfest = True
        # Spielschleife wird ausgeführt solange mehr als ein Spieler noch drin ist
        while gewinnerstehtnichtfest:
            # jeder for-schleifen-zyklus ist eine Runde aller Spieler
            for i in spiel:
                if i.im_gefaengnis is False:
                    i.wuerfeln()
                i.feldchecken(self.spiel)
                # wenn Spieler unter 1 Euro hat wird er aus dem Spiel entfernt und seine Strassen wieder kaufbar gemacht
                if i.geld < 1:
                    print(i.name, "ist aus dem Spiel")
                    for x in spielfeld.feld:
                        if x.kartentyp != "anderes":
                            if x.besitzer == i.name:
                                x.besitzer = ""
                                x.Haeuser = 0
                    del spiel[spiel.index(i)]
            # wenn nur noch 1 Spieler dri ist wird die Schleife beendet
            if len(spiel) == 1:
                gewinnerstehtnichtfest = False
        print("Spieler", spiel[0].name, "gewinnt mit", spiel[0].geld)
        return spiel[0].geld


class Auswertung:
    # Methode um aus einem Array den Durchschnittswert zu bilden
    @staticmethod
    def durchschnitt(liste):
        summe = 0
        if len(liste) == 1:
            return liste[0]
        else:
            for i in liste:
                summe += i
            return summe / (len(liste) - 1)

    # Methode um aus einem Array den Median zu bilden
    @staticmethod
    def median(liste):
        mitte = (len(liste) - 1) / 2
        if mitte.is_integer():
            return liste[int(mitte)]
        else:
            return (liste[int(mitte)] + liste[int(mitte + 1)]) / 2


SpielStarten()
