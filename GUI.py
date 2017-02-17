from Spiel import Spieler
from Spielfeld import spielfeld
from tkinter import *
from tkinter import messagebox
import time

class GUI:
    # Definition von den Spielern und anderen Variablen
    def __init__(self):
        # Fenster erstellen
        self.root = Tk()
        self.hauptfenster = Frame(self.root)
        self.hauptfenster.pack()
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.title("Monopoly Simulation")
        # Fenster mittig zentrieren
        w = 1280
        h = 720
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.root.config(bg='lightgrey')

        # Einleitung
        label = Label(self.hauptfenster,
                      text="Bitte die Simulation von Monopoly konfigurieren, bevor diese gestartet wird.")
        label.grid(row=0, columnspan=2)

        # Konfiguration
        # Inputfelder für startkapital, startposition und Anzahl der wiederholungen
        Label(self.hauptfenster, text="Startkapital").grid(row=1)
        Label(self.hauptfenster, text="Startposition").grid(row=2)
        Label(self.hauptfenster, text="Anzahl Wdh").grid(row=3)
        global sk
        sk = Entry(self.hauptfenster)
        global sp
        sp = Entry(self.hauptfenster)
        global wdh
        wdh = Entry(self.hauptfenster)
        sk.grid(row=1, column=1)
        sp.grid(row=2, column=1)
        wdh.grid(row=3, column=1)
        # Schieberegler fuer Anzahl der Spieler (2-6)
        Label(self.hauptfenster, text="Spierleranzahl").grid(row=4)
        global sa
        sa = Scale(self.hauptfenster, from_=2, to=6, orient=HORIZONTAL)
        sa.grid(row=4, column=1)
        # Start / Überprüfung der Werte
        start = Button(master=self.hauptfenster, text="Simulation starten", command=self.starten, fg="white",
                       bg="black")
        start.grid(row=5, columnspan=2)
        self.root.mainloop()

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

        # Prüfung der Startposition
        self.sp = sp.get()
        if self.sp == "":
            messagebox.showerror("FAIL", "Wähle bitte ein Startposition!")
        else:
            ske = self.sp.strip()
            try:
                self.sp = int(ske)
                if self.sp < 0 or self.sp > 39:
                    messagebox.showerror("FAIL", "Wähle eine passende Startposition (zwischen 0 und 39)")
                else:
                    startbar += 1
            except ValueError:
                messagebox.showerror("FAIL", "Wähle bitte eine Zahl (Startposition)!")

        # Prüfung der Wiederholungen
        self.wdh = wdh.get()
        if self.wdh == "":
            messagebox.showerror("FAIL", "Wähle bitte die Anzahl der Wiederholungen")
        else:
            ske = self.wdh.strip()
            try:
                self.wdh = int(ske)
                if self.wdh < 1:
                    messagebox.showerror("FAIL", "Wähle bitte Wiederholungen über 1!")
                else:
                    startbar += 1
            except ValueError:
                messagebox.showerror("FAIL", "Wähle bitte eine Zahl (Wiederholungen)!")

        if startbar == 3:
            anzahl = sa.get()
            spieler = []
            for i in range(1, anzahl + 1):
                spieler.append("Spieler" + str(i))
            startgeld = self.sk
            startpos = self.sp
            anzahl_wdh = 0
            auswertungsliste = []
            while anzahl_wdh < self.wdh:
                neues_spiel = Spiel(spieler, startgeld, startpos)
                auswertungsliste.append(neues_spiel.schleife())
                anzahl_wdh += 1
            spielanimation(anzahl)

            endtext = ("Gewinner haben durchschnittlich", round(self.durchschnitt(auswertungsliste), 2), "Euro, in einem Spiel mit", self.wdh, "Runden und einem Startkapital von", self.sk, "Euro bekommen.\nDas Spiel wurde an Feldnummer", self.sp, "gestartet.")

            Label(self.hauptfenster, text=endtext).grid(row=6, column=1)

    # Methode um aus einem Array den Durchschnittswert zu bilden
    def durchschnitt(self, auswertungsliste):
        summe = 0
        for i in auswertungsliste:
            summe += i
        return summe/(len(auswertungsliste)-1)

    def spielanimation(self, anzahl):
        self.spielerfiguren = []
        self.positionen = []
        # Tk setup
        self.spielfeld = Frame(self.root)
        spielfeld = PhotoImage(file="spielfeld.gif")
        width = spielfeld.width()
        height = spielfeld.height()
        self.canvas = Canvas(self.spielfeld, bg="black", width=width, height=height)
        self.canvas.pack()

        # Spielfeld konfigurieren
        canvas_spielfeld = self.canvas.create_image(width / 2, height / 2, image=spielfeld)
        canvas_spielfeld.pack()
        # Figuren konfigurieren
        figuren = [PhotoImage(file="figur0.gif"), PhotoImage(file="figur1.gif"), PhotoImage(file="figur2.gif"),
                   PhotoImage(file="figur3.gif"), PhotoImage(file="figur4.gif"), PhotoImage(file="figur5.gif")]
        for x in range(1, anzahl + 1):
            self.spielerfiguren.append(self.canvas.create_image(width * 0.937, height * 0.5937, image=figuren[x]))

    # Figuren auf eine neue Position verschieben
    def pos_aendern(self, figur, endkoordinaten):
        x = endkoordinaten[0] - self.canvas.coords(self.spielerfiguren[figur])[0]
        y = endkoordinaten[1] - self.canvas.coords(self.spielerfiguren[figur])[1]
        self.canvas.move(self.spielerfiguren[figur], x, y)
        self.root.update()

    def spielfeldpos_aendern(self, figur, endpos):
        anfangspos = self.positionen.index(self.canvas.coords(self.spielerfiguren[figur]))
        if endpos > anfangspos:
            for i in range(anfangspos, endpos):
                self.pos_aendern(figur, self.positionen[i])
                time.sleep(0.1)
        else:
            for i in range(anfangspos, len(spielfeld.feld) - 1):
                self.pos_aendern(figur, self.positionen[i])
                time.sleep(0.1)
            for i in range(endpos):
                self.pos_aendern(figur, self.positionen[i])
                time.sleep(0.1)


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
                    GUI.spielfeldpos_aendern(self.spiel.index(i), i.pos)
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
        return self.spiel[0].geld


nSpiel = GUI()
