from Spielfeld import SpielFeld
from random import randint
from random import shuffle


class Spieler:
    def __init__(self, Name, Spielfigur, Anfangsgeld, AnfangsPos):
        self.figur = Spielfigur
        self.geld = Anfangsgeld
        self.pos = AnfangsPos
        self.name = Name
        self.wurf = 0
        self.AnzahlinBesitz = [0] * 10
        self.imGefaengnis = False
        self.gefaengnisfrei = 0

    def Geld(self):
        return self.geld

    def Geldaendern(self, Betrag):
        self.geld += Betrag

    def Positionaendern(self, neuePos):
        self.pos += neuePos

    def Feldchecken(self):
        # um unnoetigen Code zu verhindern werden oft gebrauchte Funktionen als Variablen abgespeichert
        position = SpielFeld.Feld[self.pos]
        besitzer = position.Besitzer()

        # Gucken ob das Feld kaufbar ist (HausKarten, Werke und Bahnhoefe)
        if position.Kaufbar() is True:
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
                    # Wenn der Spieler gefunden wurde:
                    if i.name == besitzer:

                        # Unterscheidung zwischen Werken, Bahnhoefen und normalen Haeusern, weil jeder Typ andere
                        # Argumente für die Mieten() Methode braucht
                        if position.kartentyp == "Werk":
                            miete = position.Mieten(self.wurf, i.AnzahlinBesitz)

                        elif position.kartentyp == "Bahnhof":
                            miete = position.Mieten(i.AnzahlinBesitz[0])

                        else:
                            miete = position.Mieten()
                            farbe = position.farbe
                            haeuser = position.Haeuser
                            if self.AnzahlinBesitz[farbe] == neuesSpiel.feldhaeufigkeiten[farbe] and haeuser == 0:
                                miete *= 2

                        # Bezahlen der Miete, Abziehen der Miete vom eigenen Konto
                        i.Geldaendern(miete)
                        self.Geldaendern(-miete)
                        break

        # wenn das Feld nicht kaufbar ist, ist es eine Sonderkarte
        else:
            typ = position.typ
            if typ == "Ins Gefaengnis":
                self.pos = 9
                self.imGefaengnis = True

            # nachdem man ins Gefaengnis kommt darf man sofort probieren raus zu kommen
            if typ == "Gefaengnis" and self.imGefaengnis is True:
                self.GefaengnisWuerfeln()

            # auf Frei Parken kriegt man alle Abgaben aus den Steuern und Ereignis/Gemeinschaftskarten
            elif typ == "Frei Parken":
                self.Geldaendern(neuesSpiel.abgaben)
                neuesSpiel.abgaben = 0

            elif typ == "Einkommenssteuer":
                self.Geldaendern(-200)
                neuesSpiel.abgaben += 200
            elif typ == "Zusatzsteuer":
                self.Geldaendern(-100)
                neuesSpiel.abgaben += 100

            # wenn man auf Los kommt kriegt man 2x den ueblichen Betrag
            elif typ == "Los":
                self.Geldaendern(200)

            elif typ == "Ereignisfeld":
                global ekartenzaehler
                global ereignisliste

                # Ereignisstapel
                def ereignis0(self):
                    self.Positionaendern(-3)

                def ereignis1(self):
                    self.Geldaendern(-15)

                def ereignis2(self):
                    self.Geldaendern(50)

                def ereignis3(self):
                    self.rueckevor(11)

                def ereignis4(self):
                    self.rueckevor(0)

                def ereignis5(self):
                    self.rueckevor(39)

                def ereignis6(self):
                    self.gefaengnisfrei += 1

                def ereignis7(self):
                    self.renovieren()

                def ereignis8(self):
                    self.rueckevor(11)

                def ereignis9(self):
                    self.rueckevor(15)

                def ereignis10(self):
                    self.Geldaendern(150)

                def ereignis11(self):
                    self.insGefaengnis()

                def ereignis12(self):
                    self.Geldaendern(-20)

                def ereignis13(self):
                    self.Geldaendern(100)

                # um die ereignisliste nur ein Mal zu deklarieren
                if 'ereignisliste' not in globals():
                    ereignisliste = [ereignis0(self), ereignis1(self), ereignis2(self), ereignis3(self),
                                     ereignis4(self), ereignis5(self), ereignis6(self), ereignis7(self),
                                     ereignis8(self), ereignis9(self), ereignis10(self), ereignis11(self),
                                     ereignis12(self), ereignis13(self)]
                    # die Liste weird gemischt
                    shuffle(ereignisliste)
                    ekartenzaehler = 0

                # wenn man alle Karten durch hat werden sie neu gemischt
                if ekartenzaehler > len(ereignisliste) - 1:
                    ekartenzaehler = 0
                    shuffle(ereignisliste)
                ereignisliste[ekartenzaehler]
                ekartenzaehler += 1

            elif typ == "Gemeinschaftsfeld":
                global gemeinschaftsliste
                global gkartenzaehler

                # Gemeinschaftsstapel
                def gemeinschaft0(self):
                    self.Geldaendern(200)

                def gemeinschaft1(self):
                    self.Geldaendern(-100)

                def gemeinschaft2(self):
                    self.Geldaendern(10)

                def gemeinschaft3(self):
                    self.Geldaendern(20)

                def gemeinschaft4(self):
                    self.Geldaendern(-10)

                def gemeinschaft5(self):
                    self.Geldaendern(-50)

                def gemeinschaft6(self):
                    self.Geldaendern(25)

                def gemeinschaft7(self):
                    self.rueckevor(0)

                def gemeinschaft8(self):
                    self.rueckevor(1)

                def gemeinschaft9(self):
                    self.gefaengnisfrei += 1

                def gemeinschaft10(self):
                    self.Geldaendern(10)

                def gemeinschaft11(self):
                    self.Geldaendern(-50)

                def gemeinschaft12(self):
                    self.Geldaendern(100)

                def gemeinschaft13(self):
                    self.insGefaengnis()

                def gemeinschaft14(self):
                    self.Geldaendern(100)

                # um die gemeinschftsliste nur ein Mal zu deklarieren
                if 'gemeinschaftsliste' not in globals():
                    gemeinschaftsliste = [gemeinschaft0(self), gemeinschaft1(self), gemeinschaft2(self),
                                          gemeinschaft3(self), gemeinschaft4(self), gemeinschaft5(self),
                                          gemeinschaft6(self), gemeinschaft7(self), gemeinschaft8(self),
                                          gemeinschaft9(self), gemeinschaft10(self), gemeinschaft11(self),
                                          gemeinschaft12(self), gemeinschaft13(self), gemeinschaft14(self)]
                    # die Liste weird gemischt
                    shuffle(gemeinschaftsliste)
                    gkartenzaehler = 0

                # wenn man alle Karten durch hat werden sie neu gemischt
                if ekartenzaehler > len(ereignisliste) - 1:
                    ekartenzaehler = 0
                    shuffle(ereignisliste)
                ereignisliste[ekartenzaehler]
                ekartenzaehler += 1

    def Kaufentscheidung(self):
        position = SpielFeld.Feld[self.pos]
        if randint(1, 100) <= 50:
            self.Kaufen()

        elif self.AnzahlinBesitz[position.farbe] == neuesSpiel.feldhaeufigkeiten[position.farbe] - 1:
            self.Kaufen()
        # wenn man schon 1 Strasse besitzt ist die Wahrscheinlichkeit hoeher dass man Strassen gleicher Farbe kauft
        elif self.AnzahlinBesitz[position.farbe] == 1:
            if randint(1, 100) <= 80:
                self.Kaufen()

    def Kaufen(self):
        position = SpielFeld.Feld[self.pos]
        position.gekauft(self.name)
        self.geld -= position.preis
        self.AnzahlinBesitz[position.farbe] += 1

    def Bauentscheidung(self):
        position = SpielFeld.Feld[self.pos]
        if randint(1, 100) == 90:
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

    def GefaengnisWuerfeln(self):
        i = 0
        self.imGefaengnis = True

        # man hat pro Runde 3 Versuche um aus dem Gefaengnis zu kommen
        while i < 3 and self.imGefaengnis is True:
            wurf1 = randint(1, 6)
            wurf2 = randint(1, 6)
            # man kommt nur frei wenn man einen Pasch wuerfelt
            if wurf1 == wurf2:
                self.Positionaendern(wurf1 + wurf2)
                self.Wuerfeln()
                self.imGefaengnis = False
                i += 1

        if self.imGefaengnis is True and self.gefaengnisfrei > 0:
            self.imGefaengnis = False
            self.gefaengnisfrei -= 1
            self.Wuerfeln()

    def insGefaengnis(self):
        self.pos = 10
        self.imGefaengnis = True

    def rueckevor(self, endPos):
        # wenn die Endposition hinter einem liegt muss man ueber Los und 200 einziehen
        if endPos > self.pos:
            self.Geldaendern(200)
        self.pos = endPos

    def renovieren(self):
        for i in SpielFeld.Feld:
            if i.Besitzer() == self.name:
                if i.kartentyp == "Haus":
                    # wenn man 6 Haueser gebaut hat ist es effektiv ein Hotel, sonst sind es nur Haeuser
                    if i.Haeuser > 5:
                        self.Geldaendern(i.Haeuser * 25)
                    else:
                        self.Geldaendern(100)


class Spiel:
    # Definition von den Spielern und anderen Variablen
    def __init__(self, spieler, Startgeld, StartPos):
        self.spiel = []
        # alle Teilnehmer in eine Liste eintragen
        for i in spieler:
            i = Spieler(i, 1, Startgeld, StartPos)
            self.spiel.append(i)
        self.feldhaeufigkeiten = [4, 2, 2, 3, 3, 3, 3, 3, 3, 2]
        self.abgaben = 0

    def Schleife(self):
        # die verschiedenen Spieler spielen solange bis der Sieger fest steht
        Gewinnerstehtnichtfest = True
        while Gewinnerstehtnichtfest:
            for i in self.spiel:
                if i.imGefaengnis is False:
                    i.Wuerfeln()
                i.Feldchecken()
                # print("Name:", i.name)
                # print("Geld:", i.Geld())
                # print()

                # wenn Spieler unter 1 Euro hat wird er aus Spiel entfernt und seine Strassen wieder kaufbar gemacht
                if i.geld < 1:
                    print(i.name, "ist aus dem Spiel")
                    for x in SpielFeld.Feld:
                        if x.kartentyp != "anderes":
                            if x.besitzer == i.name:
                                x.besitzer = ""
                                x.Haeuser = 0
                    del self.spiel[self.spiel.index(i)]

                # wenn nur noch 1 Spieler im Spiel ist ist das Spiel zuende, die Schleife wird beendet
                if len(self.spiel) == 1:
                    Gewinnerstehtnichtfest = False

        print()
        print(self.spiel[0].name, "ist der Gewinner mit", self.spiel[0].geld, "Euro")


# Setup
neuesSpiel = Spiel(["Spieler1", "Spieler2", "Spieler3", "Spieler4"], 1500, 0)
neuesSpiel.Schleife()
