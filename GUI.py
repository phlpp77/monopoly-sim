from Spieler import Spieler
from Spielfeld import Spielfeld
from tkinter import *
from tkinter import messagebox
import time
from os import system
from platform import system as platform


class GUI:
    # Definition von den Spielern und anderen Variablen
    def __init__(self):
        self.startbarabfrage = False
        # Fenster erstellen
        self.root = Tk()
        self.hauptfenster = Frame(self.root)

    def erstellen(self):
        self.hauptfenster.pack()
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.focus_force()
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
        if platform() == 'Darwin':
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

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
        # Standartmäßiger Inputfeldtext
        sk.insert(END, "1500")
        sp.insert(END, "0")
        wdh.insert(END, "2")
        # Schieberegler fuer Anzahl der Spieler (2-6)
        Label(self.hauptfenster, text="Spierleranzahl").grid(row=4)
        global sa
        sa = Scale(self.hauptfenster, from_=2, to=6, orient=HORIZONTAL)
        sa.grid(row=4, column=1)
        sa.set(4)
        # Start / Überprüfung der Werte
        start = Button(master=self.hauptfenster, text="Simulation starten", command=self.starten, fg="white",
                       bg="black")
        start.grid(row=5, columnspan=2)
        self.root.bind('<KeyPress-Return>', self.enter_starten)
        self.root.mainloop()

    # TK legt beim Keypress noch metadaten bei, die zu TypeErrors führen, deshab werden sie hier fallen gelassen
    def enter_starten(self, x):
        self.starten()

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

        self.sa = sa.get()

        if startbar == 3:
            self.root.destroy()
            self.startbarabfrage = True

    def startbar(self):
        return self.startbarabfrage

    def getStartPos(self):
        return self.sp

    def getStartKap(self):
        return self.sk

    def getWdh(self):
        return self.wdh

    def getSpielerAnzahl(self):
        return self.sa

    '''
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
        '''

    def auswertungstext(self, durchschnitt):
        endtext = (
            "Gewinner haben durchschnittlich", round(durchschnitt, 2), "Euro, in einem Spiel mit",
            self.wdh, "Runden und einem Startkapital von", self.sk, "Euro bekommen.\nDas Spiel wurde an Feldnummer",
            self.sp, "gestartet.")
        messagebox.showerror("ENDE", endtext)

        # Label(self.hauptfenster, text=endtext).grid(row=6, column=1)

    def spielanimation(self, anzahl):
        self.root = Tk()
        self.spielerfiguren = []
        # Testpositionen für das ganze Spielfeld (40 Positionen)
        self.positionen = [[402, 855], [955, 494], [912, 77], [927, 440], [191, 798], [151, 501], [956, 843],
                           [851, 635], [985, 137], [480, 163], [294, 222], [681, 336], [10, 700], [360, 559],
                           [833, 937], [500, 126], [154, 776], [845, 538], [1, 83], [109, 242], [467, 614], [537, 191],
                           [543, 315], [482, 736], [737, 80], [554, 451], [575, 673], [966, 120], [389, 839],
                           [267, 392], [965, 152], [803, 777], [821, 306], [317, 890], [586, 316], [162, 564],
                           [142, 347], [759, 578], [694, 669]]
        # Tk setup
        self.Spielfeld = Frame(self.root)
        spielfeld = PhotoImage(file="gfx/spielfeld.gif")
        width = spielfeld.width()
        height = spielfeld.height()
        self.canvas = Canvas(self.root, bg="black", width=width, height=height)
        self.canvas.pack()

        # Spielfeld konfigurieren
        self.canvas.create_image(width / 2, height / 2, image=spielfeld)
        # Figuren konfigurieren
        figuren = [PhotoImage(file="gfx/figur0.gif"), PhotoImage(file="gfx/figur1.gif"),
                   PhotoImage(file="gfx/figur2.gif"), PhotoImage(file="gfx/figur3.gif"),
                   PhotoImage(file="gfx/figur4.gif"), PhotoImage(file="gfx/figur5.gif")]
        for x in range(1, anzahl + 1):
            self.spielerfiguren.append(self.canvas.create_image(402, 855, image=figuren[x]))
        print(self.canvas.coords(self.spielerfiguren[1]))
        self.root.mainloop()

    # Figuren auf eine neue Position verschieben
    def __pos_aendern(self, figur, endkoordinaten):
        x = endkoordinaten[0] - self.canvas.coords(self.spielerfiguren[figur])[0]
        y = endkoordinaten[1] - self.canvas.coords(self.spielerfiguren[figur])[1]
        self.canvas.move(self.spielerfiguren[figur], x, y)
        self.root.update()

    def spielfeldpos_aendern(self, figur, endpos):
        print(self.canvas.coords(self.spielerfiguren[figur]))
        anfangspos = self.positionen.index(self.canvas.coords(self.spielerfiguren[figur]))
        if endpos > anfangspos:
            for i in range(anfangspos, endpos):
                self.__pos_aendern(figur, self.positionen[i])
                time.sleep(0.1)
        else:
            for i in range(anfangspos, len(Spielfeld.feld) - 1):
                self.__pos_aendern(figur, self.positionen[i])
                time.sleep(0.1)
            for i in range(endpos):
                self.__pos_aendern(figur, self.positionen[i])
                time.sleep(0.1)


class Spiel:
    def __init__(self, spieler, startgeld, startpos):
        self.abgaben = 0
        self.spiel = []
        # alle Teilnehmer in eine Liste eintragen
        for i in spieler:
            i = Spieler(i, startgeld, startpos)
            self.spiel.append(i)

    @staticmethod
    def spielerzurücksetzen(name):
        for x in Spielfeld.feld:
            if x.kartentyp != "anderes":
                if x.besitzer == name:
                    x.besitzer = ""
                    x.Haeuser = 0
