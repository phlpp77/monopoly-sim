from GUI import *


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
            # self.gui.spielanimation(len(s))
            i = 0
            while i <= sw:
                self.spiel.__init__(s, sk, sp)
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
                # self.gui.spielfeldpos_aendern(spiel.index(i), i.getPos())
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
        geld = spiel[0].geld
        self.spiel.spielerzurücksetzen(spiel[0].name)
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
