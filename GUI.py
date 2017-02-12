from Spiel import Spieler
from Spielfeld import SpielFeld
from tkinter import *


class GUI:
    # Definition von den Spielern und anderen Variablen
    def __init__(self, spieler, Startgeld, StartPos):
        # Fenster erstellen
        root = Tk()
        self.hauptfenster = Frame(root)
        root.title("Monopoly Simulation")
        root.geometry("1280x720")
        # Fenster mittig zentrieren
        w = 1280
        h = 720
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.config(bg='lightgrey')

        label = Label(self.hauptfenster, text="bla")
        self.hauptfenster.pack()
        label.pack()
        root.mainloop()

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
                i.Feldchecken(neuesSpiel)
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


neuesSpiel = GUI(["Spieler1", "Spieler2", "Spieler3", "Spieler4"], 1500, 0)
neuesSpiel.Schleife()
