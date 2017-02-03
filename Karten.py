class HausKarten:
    def __init__(self, Preis, Mieten, Baukosten):
        self.preis = Preis
        self.mieten = Mieten
        self.baukosten = Baukosten

        self.Haeuser = 0
        self.besitzer = ""
        self.kartentyp = "Haus"

    def Kaufbar(self):
        return True

    def Bebaubar(self):
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


class nichtHaus():
    def __init__(self, Typ):
        self.typ = Typ
        self.kartentyp = "anderes"

    def Bebaubar(self):
        return False

    def Kaufbar(self):
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

    def Bebaubar(self):
        return False

    def Mieten(self, Wurf, BesitzervonAllen):
        if BesitzervonAllen:
            return (Wurf * 10)
        else:
            return (Wurf * 4)

class Bahnhoefe(HausKarten):
    def __init__(self):
        self.preis = 200
        self.besitzer = ""
        self.kartentyp = "Bahnhof"

        def Bebaubar(self):
            return False

        def Mieten(self, AnzahlImBesitz):
            if AnzahlImBesitz == 1:
                return 25
            elif AnzahlImBesitz == 2:
                return 50
            elif AnzahlImBesitz == 3:
                return 100
            elif AnzahlImBesitz == 4:
                return 200