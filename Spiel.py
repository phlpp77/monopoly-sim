from Spielfeld import SpielFeld
from random import randint



class Spieler:
    def __init__(self, Name, Spielfigur, Anfangsgeld, AnfangsPos):
        self.figur = Spielfigur
        self.geld = Anfangsgeld
        self.pos = AnfangsPos
        self.name = Name
        self.wurf = 0
        self.AnzahlinBesitz = [0] * 10
        self.imGefaengnis = False


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

                # Ereignisstapel
                def ereignis1(self):
                    self.Geldaendern(-250)

                def ereignis2(self):
                    self.Geldaendern(400)

                global ereignisliste
                ereignisliste = [ereignis1(self), ereignis2(self)]

                # Ablagestapel
                altelisteEreignis = []
                # ziehene einer Karte aus der Liste
                ereignis = randint(0, 9)

                # eigentliches Ziehen der Karten und Ausführen; Karten werden auf den Ablagestapel gelegt
                def ziehen():
                    ereignisliste[ereignis]
                    altelisteEreignis.append(ereignisliste[ereignis])
                    ereignisliste.remove(ereignisliste[ereignis])

                # prüfen, ob der Kartenstapel noch so groß wie die Zahl ist, dann wird gezogen
                if ereignis < len(ereignisliste):
                    ziehen()
                # wenn nicht, wird die nächste Karte tiefere genommen
                else:
                    while ereignis > len(ereignisliste):
                        ereignis -= 1
                    # da sie jetzt erst gleich groß ist und der Index ein tiefer sein muss nochmal, dann kann auch
                    # gezogen werden
                    ereignis -= 1
                    ziehen()

                # Ablagestapel wieder ins Spiel bringen, wenn der Stapel leer ist
                if not ereignisliste:
                    ereignisliste = altelisteEreignis
                    altelisteEreignis = []

            elif typ == "Gemeinschaftsfeld":

                # Gemeinschaftsstapel
                def gemeinschaft1(self):
                    self.Geldaendern(200)

                def gemeinschaft2(self):
                    self.pos = 3

                global gemeinschaftsliste
                gemeinschaftsliste = [gemeinschaft1(self), gemeinschaft2(self)]

                # Ablagestapel
                altelisteGemeinschaft = []
                # ziehene einer Karte aus der Liste
                gemeinschaft = randint(0, 9)

                # eigentliches Ziehen der Karten und Ausführen; Karten werden auf den Ablagestapel gelegt
                def ziehen():
                    gemeinschaftsliste[gemeinschaft]
                    altelisteGemeinschaft.append(gemeinschaftsliste[gemeinschaft])
                    gemeinschaftsliste.remove(gemeinschaftsliste[gemeinschaft])

                # prüfen, ob der Kartenstapel noch so groß wie die Zahl ist, dann wird gezogen
                if gemeinschaft < len(gemeinschaftsliste):
                    ziehen()
                # wenn nicht, wird die nächste Karte tiefere genommen
                else:
                    while gemeinschaft > len(gemeinschaftsliste):
                        gemeinschaft -= 1
                    # da sie jetzt erst gleich groß ist und der Index ein tiefer sein muss nochmal, dann kann auch
                    # gezogen werden
                    gemeinschaft -= 1
                    ziehen()

                # Ablagestapel wieder ins Spiel bringen, wenn der Stapel leer ist
                if not gemeinschaftsliste:
                    gemeinschaftsliste = altelisteGemeinschaft
                    altelisteGemeinschaft = []


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
