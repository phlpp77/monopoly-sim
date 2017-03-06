from Spielfeld import spielfeld
from random import randint
from random import shuffle


class Spieler:
    def __init__(self, name, anfangsgeld, anfangs_pos):
        self.geld = anfangsgeld
        self.pos = anfangs_pos
        self.name = name
        self.wurf = 0
        self.anzahl_in_besitz = [0] * 10
        self.im_gefaengnis = False
        self.gefaengnisfrei = 0

    def getPos(self):
        return self.pos

    def geldaendern(self, betrag):
        self.geld += betrag

    def positionaendern(self, neue_pos):
        self.pos += neue_pos

    def feldchecken(self, spiel):
        # um unnoetigen Code zu verhindern werden oft gebrauchte Funktionen als Variablen abgespeichert
        self.spiel = spiel
        position = spielfeld.feld[self.pos]
        besitzer = position.besitzer_abrufen()

        # Gucken ob das feld kaufbar ist (HausKarten, Werke und Bahnhoefe)
        if position.kaufbar() is True:
            # wenn das feld noch keinem gehoert wird entschieden ob gekauft werden soll
            if besitzer == "":
                self.kaufentscheidung()

            # wenn das feld einem selbst gehoert und bebaubar ist wird entschieden, ob ein Haus gebaut werden soll
            elif besitzer == self.name and position.bebaubar() is True:
                # ueberprufen ob man alle 3 felder besitzt so dass man bauen kann
                if self.anzahl_in_besitz[position.farbe] == spielfeld.feldhaeufigkeiten[position.farbe]:
                    # man kann nur 4 haeuser und 1 Hotel haben, also insgesamt 5 Mal bauen
                    if position.haeuser < 5:
                        self.bauentscheidung()

            # feld gehoert dem Spieler aber ist nicht bebaubar, also wird nichts unternommen
            elif besitzer == self.name:
                pass

            # feld gehoert anderem Spieler
            else:
                # nachgucken welchem Spieler das feld gehoert
                for i in self.spiel.spiel:
                    # Wenn der Spieler gefunden wurde:
                    if i.name == besitzer:

                        # Unterscheidung zwischen Werken, Bahnhoefen und normalen haeusern, weil jeder Typ andere
                        # Argumente für die Mieten() Methode braucht
                        if position.kartentyp == "Werk":
                            miete = position.mieten_abrufen(self.wurf, i.anzahl_in_besitz)

                        elif position.kartentyp == "Bahnhof":
                            miete = position.mieten_abrufen(i.anzahl_in_besitz[0])

                        else:
                            miete = position.mieten_abrufen()
                            farbe = position.farbe
                            haeuser = position.haeuser
                            if self.anzahl_in_besitz[farbe] == spielfeld.feldhaeufigkeiten[farbe] and haeuser == 0:
                                miete *= 2

                        # Bezahlen der Miete, Abziehen der Miete vom eigenen Konto
                        i.geldaendern(miete)
                        self.geldaendern(-miete)
                        break

        # wenn das feld nicht kaufbar ist, ist es eine Sonderkarte
        else:
            typ = position.typ
            if typ == "Ins Gefaengnis":
                self.pos = 10
                self.im_gefaengnis = True

            # nachdem man ins Gefaengnis kommt darf man sofort probieren raus zu kommen
            if typ == "Gefaengnis" and self.im_gefaengnis is True:
                self.gefaengniswuerfeln()

            # auf Frei Parken kriegt man alle Abgaben aus den Steuern und Ereignis/Gemeinschaftskarten
            elif typ == "Frei Parken":
                self.geldaendern(self.spiel.abgaben)
                self.spiel.abgaben = 0

            elif typ == "Einkommenssteuer":
                self.geldaendern(-200)
                self.spiel.abgaben += 200
            elif typ == "Zusatzsteuer":
                self.geldaendern(-100)
                self.spiel.abgaben += 100

            # wenn man auf Los kommt kriegt man 2x den ueblichen Betrag
            elif typ == "Los":
                self.geldaendern(200)

            elif typ == "Ereignisfeld":
                global ekartenzaehler
                global ereignisliste

                # Ereignisstapel
                def ereignis0(self):
                    self.positionaendern(-3)

                def ereignis1(self):
                    self.geldaendern(-15)

                def ereignis2(self):
                    self.geldaendern(50)

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
                    self.geldaendern(150)

                def ereignis11(self):
                    self.ins_gefaengnis()

                def ereignis12(self):
                    self.geldaendern(-20)

                def ereignis13(self):
                    self.geldaendern(100)

                # um die ereignisliste nur ein Mal zu deklarieren
                if 'ereignisliste' not in globals():
                    ereignisliste = [ereignis0, ereignis1, ereignis2, ereignis3, ereignis4, ereignis5, ereignis6,
                                     ereignis7, ereignis8, ereignis9, ereignis10, ereignis11, ereignis12, ereignis13]
                    # die Liste weird gemischt
                    shuffle(ereignisliste)
                    ekartenzaehler = 0

                # wenn man alle Karten durch hat werden sie neu gemischt
                if ekartenzaehler > len(ereignisliste) - 1:
                    ekartenzaehler = 0
                    shuffle(ereignisliste)
                ereignisliste[ekartenzaehler](self)
                ekartenzaehler += 1

            elif typ == "Gemeinschaftsfeld":
                global gemeinschaftsliste
                global gkartenzaehler

                # Gemeinschaftsstapel
                def gemeinschaft0(self):
                    self.geldaendern(200)

                def gemeinschaft1(self):
                    self.geldaendern(-100)

                def gemeinschaft2(self):
                    self.geldaendern(10)

                def gemeinschaft3(self):
                    self.geldaendern(20)

                def gemeinschaft4(self):
                    self.geldaendern(-10)

                def gemeinschaft5(self):
                    self.geldaendern(-50)

                def gemeinschaft6(self):
                    self.geldaendern(25)

                def gemeinschaft7(self):
                    self.rueckevor(0)

                def gemeinschaft8(self):
                    self.rueckevor(1)

                def gemeinschaft9(self):
                    self.gefaengnisfrei += 1

                def gemeinschaft10(self):
                    self.geldaendern(10)

                def gemeinschaft11(self):
                    self.geldaendern(-50)

                def gemeinschaft12(self):
                    self.geldaendern(100)

                def gemeinschaft13(self):
                    self.ins_gefaengnis()

                def gemeinschaft14(self):
                    self.geldaendern(100)

                # um die gemeinschftsliste nur ein Mal zu deklarieren
                if 'gemeinschaftsliste' not in globals():
                    gemeinschaftsliste = [gemeinschaft0, gemeinschaft1, gemeinschaft2, gemeinschaft3, gemeinschaft4,
                                          gemeinschaft5, gemeinschaft6, gemeinschaft7, gemeinschaft8, gemeinschaft9,
                                          gemeinschaft10, gemeinschaft11, gemeinschaft12, gemeinschaft13,
                                          gemeinschaft14]
                    # die Liste weird gemischt
                    shuffle(gemeinschaftsliste)
                    gkartenzaehler = 0

                # wenn man alle Karten durch hat werden sie neu gemischt
                if gkartenzaehler > len(gemeinschaftsliste) - 1:
                    gkartenzaehler = 0
                    shuffle(gemeinschaftsliste)
                gemeinschaftsliste[gkartenzaehler](self)
                gkartenzaehler += 1

    def kaufentscheidung(self):
        position = spielfeld.feld[self.pos]
        if randint(1, 100) <= 50:
            self.kaufen()

        elif self.anzahl_in_besitz[position.farbe] == spielfeld.feldhaeufigkeiten[position.farbe] - 1:
            self.kaufen()
        # wenn man schon 1 Strasse besitzt ist die Wahrscheinlichkeit hoeher dass man Strassen gleicher Farbe kauft
        elif self.anzahl_in_besitz[position.farbe] == 1:
            if randint(1, 100) <= 80:
                self.kaufen()

    def kaufen(self):
        position = spielfeld.feld[self.pos]
        position.gekauft(self.name)
        self.geld -= position.preis
        self.anzahl_in_besitz[position.farbe] += 1

    def bauentscheidung(self):
        position = spielfeld.feld[self.pos]
        if randint(1, 100) == 90:
            position.bauen()
            self.geldaendern(-position.baukosten)

    def wuerfeln(self):
        wuerfel1 = randint(1, 6)
        wuerfel2 = randint(1, 6)
        self.wurf = wuerfel1 + wuerfel2
        laenge = len(spielfeld.feld)
        self.positionaendern(self.wurf)
        # Ueberpruefen ob es ein Pasch ist
        if wuerfel1 == wuerfel2:
            self.wuerfeln()
        if self.pos >= laenge:
            self.positionaendern(-laenge)
            self.geld += 200

    def gefaengniswuerfeln(self):
        i = 0
        self.im_gefaengnis = True

        # man hat pro Runde 3 Versuche um aus dem Gefaengnis zu kommen
        while i < 3 and self.im_gefaengnis is True:
            wurf1 = randint(1, 6)
            wurf2 = randint(1, 6)
            # man kommt nur frei wenn man einen Pasch wuerfelt
            if wurf1 == wurf2:
                self.positionaendern(wurf1 + wurf2)
                self.wuerfeln()
                self.im_gefaengnis = False
                i += 1

        if self.im_gefaengnis is True and self.gefaengnisfrei > 0:
            self.im_gefaengnis = False
            self.gefaengnisfrei -= 1
            self.wuerfeln()

    def ins_gefaengnis(self):
        self.pos = 9
        self.im_gefaengnis = True

    def rueckevor(self, endpos):
        # wenn die Endposition hinter einem liegt muss man ueber Los und 200 einziehen
        if endpos > self.pos:
            self.geldaendern(200)
        self.pos = endpos

    def renovieren(self):
        for i in spielfeld.feld:
            if i.besitzer_abrufen() == self.name:
                if i.kartentyp == "Haus":
                    # wenn man 6 Haueser gebaut hat ist es effektiv ein Hotel, sonst sind es nur haeuser
                    if i.haeuser > 5:
                        self.geldaendern(i.haeuser * 25)
                    else:
                        self.geldaendern(100)
