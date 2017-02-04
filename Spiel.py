from Spielfeld import SpielFeld
from random import randint


class Spieler:
    def __init__(self, Name, Spielfigur, Anfangsgeld, AnfangsPos):
        self.figur = Spielfigur
        self.geld = Anfangsgeld
        self.pos = AnfangsPos
        self.name = Name
        self.AnzahlinBesitz = [0] * 9

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
        position = SpielFeld.Feld[self.pos]
        besitzer = position.Besitzer()

        # Gucken ob das Feld kaufbar ist (HausKarten, Werke und Bahnhoefe)
        if position.Kaufbar() == True:
            # wenn das Feld noch keinem gehoert wird entschieden ob gekauft werden soll
            if besitzer == "":
                self.Kaufentscheidung()

            # wenn das Feld einem selbst gehoert und bebaubar ist wird entschieden, ob ein Haus gebaut werden soll
            elif besitzer == self.name and position.Bebaubar() is True:
                # ueberprufen ob man alle 3 Felder besitzt so dass man bauen kann
                if self.AnzahlinBesitz[position.farbe] == neuesSpiel.feldhaeufigkeiten[position.farbe]:
                    # man kann nur 4 Haeuser und 1 Hotel haben, also insgesamt 5 Mal bauen
                    if position.Haeuser < 5:
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
                        if position.kartentyp == "Werk":
                            Miete = position.Mieten(self.wurf, i.AnzahlinBesitz)

                        elif position.kartentyp == "Bahnhof":
                            Miete = position.Mieten(i.AnzahlinBesitz[0])

                        else:
                            Miete = position.Mieten()
                            if self.AnzahlinBesitz[position.farbe] == neuesSpiel.feldhaeufigkeiten[
                                position.farbe] and position.Haeuser == 0:
                                Miete = Miete * 2

                        # Bezahlen der Miete, Abziehen der Miete vom eigenen Konto
                        i.Geldaendern(Miete)
                        self.Geldaendern(-(Miete))
                        break

    def Kaufentscheidung(self):
        position = SpielFeld.Feld[self.pos]
        if randint(1, 2) == 1:
            position.gekauft(self.name)
            self.geld -= position.preis
            self.AnzahlinBesitz[position.farbe] += 1

    def Bauentscheidung(self):
        position = SpielFeld.Feld[self.pos]
        if randint(1, 2) == 1:
            position.Bauen()
            self.Geldaendern(-position.baukosten)

    def Wuerfeln(self):
        wuerfel1 = randint(1, 6)
        wuerfel2 = randint(1, 6)
        self.wurf = wuerfel1 + wuerfel2
        laenge = len(SpielFeld.Feld)
        self.Positionaendern(self.wurf)
        # Ueberpruefen ob es ein Pasch ist
        if wuerfel1 == wuerfel2:
            self.Wuerfeln()
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
        self.feldhaeufigkeiten = [4, 2, 2, 3, 3, 3, 3, 3, 3, 2]

    # die verschiedenen Spieler spielen solange bis der Sieger fest steht
    def Schleife(self):
        Gewinnerstehtnichtfest = True
        while Gewinnerstehtnichtfest:
            for i in self.spiel:
                i.Wuerfeln()
                i.Feldchecken()
                print("Name:", i.name)
                print("Geld:", i.Geld())
                # print()
                if i.geld < 1000:
                    print(i.name, "ist aus dem Spiel")
                    del self.spiel[self.spiel.index(i)]
                if len(self.spiel) == 1:
                    Gewinnerstehtnichtfest = False
        print()
        print(self.spiel[0].name, "ist der Gewinner mit ", self.spiel[0].geld, "Euro")


# Setup
neuesSpiel = Spiel(["Spieler1", "Spieler2", "Spieler3", "Spieler4"], 10000, 1)
neuesSpiel.Schleife()
