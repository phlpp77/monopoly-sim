class HausKarten:
    def __init__(self, preis, mieten, baukosten, farbe):
        self.preis = preis
        self.mieten = mieten
        self.baukosten = baukosten
        self.farbe = farbe

        self.haeuser = 0
        self.besitzer = ""
        self.kartentyp = "Haus"

    @staticmethod
    def kaufbar():
        return True

    @staticmethod
    def bebaubar():
        return True

    def besitzer_abrufen(self):
        return self.besitzer

    def gekauft(self, kaeufer):
        self.besitzer = kaeufer

    def haeuser_abrufen(self):
        return self.haeuser

    def bauen(self):
        self.haeuser += 1

    def mieten_abrufen(self):
        return self.mieten[self.haeuser]


class NichtHaus:
    # Alle besonderen Felder, die nicht käuflich zu erwerben sind
    # hierbei wird nur der typ übergeben, um unnötige Klassen zu vermeiden
    def __init__(self, typ):
        self.typ = typ
        self.kartentyp = "anderes"

    @staticmethod
    def bebaubar():
        return False

    @staticmethod
    def kaufbar():
        return False

    def besitzer_abrufen(self):
        if self.typ == "Einkommenssteuer" or self.typ == "Zusatzsteuer":
            return "Staat"
        else:
            return ""

    def mieten_abrufen(self):
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
    def bebaubar():
        return False

    def mieten_abrufen(self, wurf, anzahl):
        if anzahl == 1:
            return wurf * 10
        else:
            return wurf * 4


class Bahnhoefe(HausKarten):
    def __init__(self):
        self.preis = 200
        self.besitzer = ""
        self.kartentyp = "Bahnhof"
        self.farbe = 0

    @staticmethod
    def bebaubar():
        return False

    def mieten_abrufen(self, anzahl_in_besitz):
        if anzahl_in_besitz == 1:
            return 25
        elif anzahl_in_besitz == 2:
            return 50
        elif anzahl_in_besitz == 3:
            return 100
        else:
            return 200
