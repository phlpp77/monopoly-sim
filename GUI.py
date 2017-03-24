from Spieler import Spieler
from Spielfeld import Spielfeld
from tkinter import *
from tkinter import messagebox
import time
import pygame
import threading
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
        Label(self.hauptfenster, text="Spieleranzahl").grid(row=4)
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

    def auswertungstext(self, durchschnitt):
        endtext = (
            "Gewinner haben durchschnittlich", round(durchschnitt, 2), "Euro, in einem Spiel mit",
            self.wdh, "Runden und einem Startkapital von", self.sk, "Euro bekommen.\nDas Spiel wurde an Feldnummer",
            self.sp, "gestartet.")
        messagebox.showerror("ENDE", endtext)

        # Label(self.hauptfenster, text=endtext).grid(row=6, column=1)


class Animation:
    def __init__(self, spieleranzahl):
        # Variablen definieren
        spielerbilder = ["gfx/figur0.gif", "gfx/figur1.gif", "gfx/figur2.gif", "gfx/figur3.gif", "gfx/figur4.gif",
                         "gfx/figur5.gif"]
        self.positionen = [(100, 100), (200, 200), (300, 300), (400, 400)]

        # Initialisieren vom Fenster
        pygame.init()
        self.spielfeld = pygame.display.set_mode((1000, 1000))
        # Hintergrund anzeigen
        self.hintergrund = pygame.image.load("gfx/spielfeld.gif")
        self.spielfeld.blit(self.hintergrund, (0, 0))

        #  Spielerbilder laden
        self.spieler = []
        for i in range(spieleranzahl):
            bild = pygame.image.load(spielerbilder[i])
            self.spieler.append(pygame.image.load(spielerbilder[i]))
            self.spielfeld.blit(self.spieler[-1], (0, 0))
        pygame.display.flip()
        print(self.spieler)

    def pos_aendern(self, figur, endpos):
        feld = self.spielfeld
        spieler = self.spieler
        figur = spieler[figur]
        endpos = self.positionen[endpos]

        # aktuelle Koordinatenherausfinden
        figur_koor = figur.get_rect()
        koords = x, y = figur_koor.x, figur_koor.y
        # an Position der Figur wird der Hintergrund überschrieben
        feld.blit(self.hintergrund, (0, 0), pygame.Rect(x, y, 50, 50))

        # falls eine andere Figur noch da war wird diese wieder hervorgehoben
        for i in spieler:
            rec = i.get_rect()
            andere_koords = x1, y1 = rec.x, rec.y
            if spieler.index(i) != spieler.index(figur) and x1 == x and y1 == y1:
                feld.blit(i, andere_koords)
        feld.blit(figur, endpos)
        pygame.display.flip()


class Spiel:
    def __init__(self, spieler, startgeld, startpos):
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
