from Spiel import Spieler
from Spielfeld import spielfeld
from tkinter import *
from tkinter import messagebox


class GUI:
    # Definition von den Spielern und anderen Variablen
    def __init__(self):
        # Fenster erstellen
        root = Tk()
        self.hauptfenster = Frame(root)
        self.hauptfenster.pack()
        root.lift()
        root.attributes("-topmost", True)
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
        label = Label(self.hauptfenster,
                      text="Bitte die Simulation von Monopoly konfigurieren, bevor diese gestartet wird.")
        label.grid(row=0, columnspan=2)
        # Konfiguration
        Label(self.hauptfenster, text="Startkapital").grid(row=1)
        Label(self.hauptfenster, text="startposition").grid(row=2)
        global sk
        sk = Entry(self.hauptfenster)
        global sp
        sp = Entry(self.hauptfenster)
        sk.grid(row=1, column=1)
        sp.grid(row=2, column=1)
        Label(self.hauptfenster, text="Spierleranzahl").grid(row=3)
        global sa
        sa = Scale(self.hauptfenster, from_=2, to=6, orient=HORIZONTAL)
        sa.grid(row=3, column=1)
        # Start / Überprüfung der Werte
        start = Button(master=self.hauptfenster, text="Simulation starten", command=self.starten, fg="white",
                       bg="black")
        start.grid(row=4, columnspan=2)
        root.mainloop()

    def starten(self):
        # Prüfung des Startkapitals
        startbar = 0
        self.sk = sk.get()
        if self.sk == "":
            messagebox.showerror("FAIL", "Wähle bitte ein Startkapital!")
        else:
            ske = self.sk.strip()
            try:
                self.sk = int(ske)
                if self.sk < 1 or self.sk > 100000:
                    messagebox.showerror("FAIL", "Wähle ein passendes Startkapital (zwischen 1 und 100.000)")
                else:
                    startbar += 1
            except ValueError:
                messagebox.showerror("FAIL", "Wähle bitte eine Zahl (Startkapital)!")
        # Prüfung der startposition
        self.sp = sp.get()
        if self.sp == "":
            messagebox.showerror("FAIL", "Wähle bitte ein startposition!")
        else:
            ske = self.sp.strip()
            try:
                self.sp = int(ske)
                if self.sp < 0 or self.sp > 39:
                    messagebox.showerror("FAIL", "Wähle ein passendes startposition (zwischen 0 und 39)")
                else:
                    startbar += 1
            except ValueError:
                messagebox.showerror("FAIL", "Wähle bitte eine Zahl (startposition)!")
        if startbar == 2:
            anzahl = sa.get()
            spieler = []
            for i in range(1, anzahl + 1):
                spieler.append("Spieler" + str(i))
            startgeld = self.sk
            startpos = self.sp
            neues_spiel = Spiel(spieler, startgeld, startpos)
            neues_spiel.schleife()


class Spiel:
    def __init__(self, spieler, startgeld, startpos):
        self.spiel = []
        # alle Teilnehmer in eine Liste eintragen
        for i in spieler:
            i = Spieler(i, startgeld, startpos)
            self.spiel.append(i)
        self.feldhaeufigkeiten = [4, 2, 2, 3, 3, 3, 3, 3, 3, 2]
        self.abgaben = 0

    def schleife(self):
        # die verschiedenen Spieler spielen solange bis der Sieger fest steht
        gewinnerstehtnichtfest = True
        while gewinnerstehtnichtfest:
            for i in self.spiel:
                if i.im_gefaengnis is False:
                    i.wuerfeln()
                i.feldchecken(self)
                # print("Name:", i.name)
                # print("Geld:", i.Geld())
                # print()

                # wenn Spieler unter 1 Euro hat wird er aus Spiel entfernt und seine Strassen wieder kaufbar gemacht
                if i.geld < 1:
                    print(i.name, "ist aus dem Spiel")
                    for x in spielfeld.feld:
                        if x.kartentyp != "anderes":
                            if x.besitzer == i.name:
                                x.besitzer = ""
                                x.Haeuser = 0
                    del self.spiel[self.spiel.index(i)]

                # wenn nur noch 1 Spieler im Spiel ist ist das Spiel zuende, die Schleife wird beendet
                if len(self.spiel) == 1:
                    gewinnerstehtnichtfest = False

        print(self.spiel[0].name, "ist der Gewinner mit", self.spiel[0].geld, "Euro")
        print()


nSpiel = GUI()
