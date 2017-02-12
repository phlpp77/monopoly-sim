from Spiel import Spieler
from Spielfeld import SpielFeld
from tkinter import *
from tkinter import messagebox

class GUI:
    # Definition von den Spielern und anderen Variablen
    def __init__(self):
        # Fenster erstellen
        root = Tk()
        self.hauptfenster = Frame(root)
        self.hauptfenster.pack()
        root.title("Monopoly Simulation")
        # Fenster mittig zentrieren
        w = 1280
        h = 720
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.config(bg='lightgrey')
        # Einleitung
        label = Label(self.hauptfenster, text="Bitte die Simulation von Monopoly konfigurieren, bevor diese gestartet wird.")
        label.grid(row=0, columnspan=2)
        # Konfiguration
        Label(self.hauptfenster, text="Startkapital").grid(row=1)
        Label(self.hauptfenster, text="Startposition").grid(row=2)
        sk = Entry(self.hauptfenster)
        sp = Entry(self.hauptfenster)
        sk.grid(row=1, column=1)
        sp.grid(row=2, column=1)
        Label(self.hauptfenster, text="Spierleranzahl").grid(row=3)
        sa = Scale(self.hauptfenster, from_=2, to=6, orient=HORIZONTAL)
        sa.grid(row=3, column=1)
        # Start / Überprüfung der Werte
        start = Button(master=self.hauptfenster, text="Simulation starten", fg="white", command=self.starten(sk, sp, sa), bg="black")
        start.grid(row=4, columnspan=2)
        root.mainloop()

    def starten(self, sk, sp, sa):
        if sk == "":
            messagebox.showerror("FAIL", "Wähle bitte ein Startkapital!")
        ske = sk.get().strip()
        sk = int(ske)
        if sk.get() < 1 or sk.get() > 100000 or sk.get() == "":
            messagebox.showerror("FAIL", "Wähle ein passendes Startkapital (zwischen 1 und 100.000)")
        """
        try:
            int(ske)
            zahl = True
        except ValueError:
            zahl = False
            messagebox.showerror("FAIL", "Wähle bitte eine Zahl!")
            """





    def Spiel(self, spieler, Startgeld, StartPos):
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


neuesSpiel = GUI()
#neuesSpiel.Schleife()

# ["Spieler1", "Spieler2", "Spieler3", "Spieler4"], 1500, 0