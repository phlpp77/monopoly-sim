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
        self.geld += Betrag

    def Position(self):
        return self.pos

    def Positionaendern(self, neuePos):
        self.pos += neuePos

    def Feldchecken(self):
        # um unnoetigen Code zu verhindern werden oft gebrauchte Funktionen als Variablen abgespeichert
        position = self.Position()
        feld = SpielFeld.Feld[position]
        besitzer = feld.Besitzer()

        # Gucken ob das Feld kaufbar ist (HausKarten, Werke und Bahnhoefe)
        if feld.Kaufbar() == True:
            # wenn das Feld noch keinem gehoert wird entschieden ob gekauft werden soll
            if besitzer == "":
                self.Kaufentscheidung()

            # wenn das Feld einem selbst gehoert und bebaubar ist wird entschieden, ob ein Haus gebaut werden soll
            elif besitzer == self.name and feld.Bebaubar() == True:
                # man kann nur 4 Haeuser und 1 Hotel haben, also 5 Mal bauen
                if feld.Haeuser < 5:
                    self.Bauentscheidung()

            # Feld gehoert dem Spieler aber ist nicht bebaubar, also wird nichts unternommen
            elif besitzer == self.name:
                pass

            # Feld gehoert anderem Spieler
            else:
                # nachgucken welchem Spieler das Feld gehoert
                for i in neuesSpiel.spiel:
                    if i.name == besitzer:
                        # Unterscheidung zwischen Werken, Bahnhoefen und normalen Haeusern, weil jeder Typ andere
                        # Argumente für die Mieten() Methode braucht
                        if SpielFeld.Feld[position].kartentyp == "Werk":
                            #nachschauen ob man Besitzer von beiden Werken ist, da die Miete davon abhaengt
                            if SpielFeld.Elektrizitaetswerk.Besitzer() == SpielFeld.Wasserwerk.Besitzer():
                                Miete = SpielFeld.Feld[position].Mieten(self.wurf, True)
                            else:
                                Miete = SpielFeld.Feld[position].Mieten(self.wurf, False)
                        elif SpielFeld.Feld[position].kartentyp == "Bahnhof":
                            Miete = feld.Mieten(1)
                        else:
                            Miete = SpielFeld.Feld[position].Mieten()

                        #Bezahlen der Miete, Abziehen der Miete vom eigenen Konto
                        i.Geldaendern(Miete)
                        self.Geldaendern(-(Miete))
                        break

    def Kaufentscheidung(self):
        if randint(1, 2) == 1:
            SpielFeld.Feld[self.pos].gekauft(self.name)
            self.geld -= SpielFeld.Feld[self.pos].preis

    def Bauentscheidung(self):
        if randint(1, 2) == 1:
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



class Spiel:
    # Definition von den Spielern und anderen Variablen
    def __init__(self, spieler, Startgeld, StartPos):
        self.spiel = []
        for i in spieler:
            i = Spieler(i, 1, Startgeld, StartPos)
            self.spiel.append(i)

    # die verschiedenen Spieler spielen solange bis der Sieger fest steht
    def Schleife(self):
        Gewinnerstehtnichtfest = True
        while Gewinnerstehtnichtfest:
            for i in self.spiel:
                i.Wuerfeln()
                i.Feldchecken()
                print("Name:", i.name)
                print("Geld:", i.Geld())
                print()


# Setup
neuesSpiel = Spiel(["Spieler1", "Spieler2", "Spieler3", "Spieler4"], 10000, 1)
neuesSpiel.Schleife()
