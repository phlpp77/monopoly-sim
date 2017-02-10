from random import randint

class HausKarten:
    def __init__(self, Preis, Mieten, Baukosten, Farbe):
        self.preis = Preis
        self.mieten = Mieten
        self.baukosten = Baukosten
        self.farbe = Farbe

        self.Haeuser = 0
        self.besitzer = ""
        self.kartentyp = "Haus"


    @staticmethod
    def Kaufbar():
        return True


    @staticmethod
    def Bebaubar():
        return True


    def Besitzer(self):
        return self.besitzer


    def gekauft(self, Kaeufer):
        self.besitzer = Kaeufer


    def returnHaeuser(self):
        return self.Haeuser


    def Bauen(self):
        self.Haeuser += 1


    def Mieten(self):
        return self.mieten[self.Haeuser]



class nichtHaus:
    # Alle besonderen Felder, die nicht käuflich zu erwerben sind
    # hierbei wird nur der typ übergeben, um unnötige Klassen zu vermeiden
    def __init__(self, Typ):
        self.typ = Typ
        self.kartentyp = "anderes"


    @staticmethod
    def Bebaubar():
        return False


    @staticmethod
    def Kaufbar():
        return False


    def Besitzer(self):
        if self.typ == "Einkommenssteuer" or self.typ == "Zusatzsteuer":
            return "Staat"
        else:
            return ""


    def Mieten(self):
        if self.typ == "Einkommenssteuer":
            return 200
        elif self.typ == "Zusatzsteuer":
            return 100



class Werke(HausKarten):
    def __init__(self):
        self.preis = 150
        self.besitzer = ""
        self.kartentyp = "Werk"
        self.farbe = 1


    @staticmethod
    def Bebaubar():
        return False


    def Mieten(self, Wurf, Anzahl):
        if Anzahl == 1:
            return Wurf * 10
        else:
            return Wurf * 4



class Bahnhoefe(HausKarten):
    def __init__(self):
        self.preis = 200
        self.besitzer = ""
        self.kartentyp = "Bahnhof"
        self.farbe = 0


    @staticmethod
    def Bebaubar():
        return False


    def Mieten(self, AnzahlimBesitz):
        if AnzahlimBesitz == 1:
            return 25
        elif AnzahlimBesitz == 2:
            return 50
        elif AnzahlimBesitz == 3:
            return 100
        else:
            return 200


''''
class Stapelkarten():

    def ereignis1():
        self.Geldaendern(-250)

    def ereignis2():
        self.Geldaendern(400)

    global ereignisliste
    ereignisliste = [ereignis1(), ereignis2()]


    def gemeinschaft1(self):
        self.Geldaendern(200)

    def gemeinschaft2(self):
        self.pos = 3

    global gemeinschaftsliste
    gemeinschaftsliste = [gemeinschaft1(), gemeinschaft2()]

'''