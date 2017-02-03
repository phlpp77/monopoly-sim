from Spielfeld import SpielFeld
from random import randint


class Spieler:
    def __init__(self, Name, Spielfigur, Anfangsgeld, AnfangsPos):
        self.figur = Spielfigur
        self.geld = Anfangsgeld
        self.pos = AnfangsPos
        self.name = Name

    def Geld(self):
        return self.geld

    def Geldaendern(self, Betrag):
        self.geld = self.geld + Betrag

    def Position(self):
        return self.pos

    def Positionaendern(self, neuePos):
        self.pos += neuePos

    def Feldchecken(self):
        position = self.Position()
        feld = SpielFeld.Feld[position]
        besitzer = feld.Besitzer()
        #print(besitzer)
        if feld.Kaufbar() == True:
            if besitzer == "":
                self.Kaufentscheidung()
            elif besitzer == self.name and feld.Bebaubar == True:
                self.Bauentscheidung()
            else:
                for i in neuesSpiel.spiel:
                    if i.name == besitzer:
                        if SpielFeld.Feld[position].kartentyp == "Werk":
                            if SpielFeld.Elektrizitaetswerk.Besitzer() == SpielFeld.Wasserwerk.Besitzer():
                                Miete = SpielFeld.Feld[position].Mieten(self.wurf, True)
                            else:
                                Miete = SpielFeld.Feld[position].Mieten(self.wurf, False)
                        else:
                            Miete = SpielFeld.Feld[position].Mieten()
                        i.Geldaendern(Miete)
                        self.Geldaendern(Miete)
                        break

    def Kaufentscheidung(self):
        if randint(1, 2) == 1:
            SpielFeld.Feld[self.pos].gekauft(self.name)
            self.geld -= SpielFeld.Feld[self.pos].preis
            #print("Kauf!")

    def Bauentscheidung(self):
        if randint(1, 2) == 1:
            print("Haus gebaut")
            SpielFeld.Feld[self.pos].Bauen()
            self.Geldaendern(-(SpielFeld.Feld[self.pos].baukosten))

    def Wuerfeln(self):
        wuerfel1 = randint(1, 6)
        wuerfel2 = randint(1, 6)
        self.wurf = wuerfel1 + wuerfel2
        laenge = len(SpielFeld.Feld)
        if wuerfel1 == wuerfel2:
            self.Wuerfeln()
        self.Positionaendern(self.wurf)
        if self.pos >= laenge:
            self.Positionaendern(-laenge)
            self.geld += 200


# die verschiedenen Spieler spielen solange bis der Sieger fest steht
class Spiel:
    def __init__(self, spieler, Startgeld, StartPos):
        self.spiel = []
        for i in spieler:
            i = Spieler(i, 1, Startgeld, StartPos)
            self.spiel.append(i)

    def Schleife(self):
        # spielFeld=SpielFeld()
        Gewinnerstehtnichtfest = True
        while Gewinnerstehtnichtfest:
            for i in self.spiel:
                i.Wuerfeln()
                i.Feldchecken()
                #print("Name:", i.name)
                #print("Geld:", i.Geld())
                #print("Position:", i.Position())


# Setup
neuesSpiel = Spiel(["Spieler1", "Spieler2", "Spieler3", "Spieler4"], 10000, 1)
neuesSpiel.Schleife()
