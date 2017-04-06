from Spieler import Spieler
from Spielfeld import Spielfeld
from tkinter import *
from tkinter import messagebox
import time
import pygame
import threading
from os import system
from platform import system as platform
import os


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
        w = 500
        h = 300
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
                      text="Dies ist eine Monopoly-Simulation. Hier können die Parameter geändert werden.")
        label.grid(row=0, columnspan=2)

        # Konfiguration
        # Inputfelder für startkapital, startposition und Anzahl der wiederholungen
        Label(self.hauptfenster, text="Startkapital").grid(row=1)
        Label(self.hauptfenster, text="Startposition").grid(row=2)
        Label(self.hauptfenster, text="Anzahl simulierter Spiele").grid(row=3)
        self.sk = Entry(self.hauptfenster)
        self.sp = Entry(self.hauptfenster)
        self.wdh = Entry(self.hauptfenster)
        self.sk.grid(row=1, column=1)
        self.sp.grid(row=2, column=1)
        self.wdh.grid(row=3, column=1)
        # Standartmäßiger Inputfeldtext
        self.sk.insert(END, "500")
        self.sp.insert(END, "0")
        self.wdh.insert(END, "2")

        # Schieberegler fuer Anzahl der Spieler (2-6)
        Label(self.hauptfenster, text="Anzahl der Spieler").grid(row=4)
        self.sa = Scale(self.hauptfenster, from_=2, to=6, orient=HORIZONTAL)
        self.sa.grid(row=4, column=1)
        self.sa.set(4)

        # Schieberegler für die Skalierung der Spielfeldanzeige
        Label(self.hauptfenster, text="Anzeigenskalierung in %").grid(row=5)
        self.res = Scale(self.hauptfenster, from_=1, to_=100, orient=HORIZONTAL)
        self.res.grid(row=5, column=1)
        self.res.set(50)

        # Schieberegler für die Geschwindigkeit
        Label(self.hauptfenster, text="Anzeigengeschwindigkeit").grid(row=6)
        self.zeit = Scale(self.hauptfenster, from_=1.5, to_=0, orient=HORIZONTAL, resolution=0.1)
        self.zeit.grid(row=6, column=1)
        self.zeit.set(0.0)

        # Schieberegler für die Geschwindigkeit
        self.buyrng = BooleanVar()
        Label(self.hauptfenster, text="Kaufentscheidung").grid(row=7)
        Radiobutton(self.hauptfenster,
                    text="zufällig",
                    padx=20,
                    variable=self.buyrng,
                    value=True).grid(row=7, column=1)
        Radiobutton(self.hauptfenster,
                    text="Immer kaufen",
                    padx=20,
                    variable=self.buyrng,
                    value=False).grid(row=7, column=2)

        # Start / Überprüfung der Werte
        start = Button(master=self.hauptfenster, text="Simulation starten", command=self.starten, bg="green")
        start.grid(row=7, columnspan=2)
        self.root.bind('<KeyPress-Return>', self.enter_starten)
        self.root.bind("<Escape>", self.esc)
        self.root.mainloop()

    # TK legt beim Keypress noch metadaten bei, die zu TypeErrors führen, deshab werden sie hier fallen gelassen
    def enter_starten(self, x):
        self.starten()

    def starten(self):
        # Prüfung des Startkapitals
        startbar = 0
        self.sk = self.sk.get()
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
        self.sp = self.sp.get()
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
        self.wdh = self.wdh.get()
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

        self.sa = self.sa.get()
        self.res = self.res.get()
        self.zeit = self.zeit.get()
        self.buyrng = self.buyrng.get()

        if startbar == 3:
            self.root.destroy()
            self.startbarabfrage = True

    def esc(self, x):
        self.root.destroy()

    def startbar(self):
        return self.startbarabfrage

    def get_start_pos(self):
        return self.sp

    def get_start_kap(self):
        return self.sk

    def get_wdh(self):
        return self.wdh

    def get_anzahl(self):
        return self.sa

    def get_resolution(self):
        return self.res

    def get_zeit(self):
        return self.zeit

    def get_buyrng(self):
        return self.buyrng


class Animation:
    def __init__(self, spieleranzahl, prozent, startzeit):
        pygame.init()
        # Variablen definieren
        spielerbilder = ["gfx/figur0.png", "gfx/figur1.png", "gfx/figur2.png", "gfx/figur3.png", "gfx/figur4.png",
                         "gfx/figur5.png"]
        # um das Spielfeld variabel skalieren zu können wird die self.positionen Liste in jedem Durchgang neu erstellt
        prozent /= 100
        width = pygame.display.Info().current_h - 50
        width = int(width * prozent)
        steps = width / 11
        self.positionen = []
        self.spieler_größe = int(50 * prozent)
        self.zeit = startzeit
        versch = int(0.5 * self.spieler_größe)

        for i in reversed(range(11)):
            self.positionen.append((int((steps / 2 + i * steps) - versch), int((10.5 * steps) - versch)))
        for i in reversed(range(10)):
            self.positionen.append((int((steps / 2) - versch), int((steps / 2 + i * steps) - versch)))
        for i in range(1, 10):
            self.positionen.append((int((steps / 2 + i * steps) - versch), int((0.5 * steps) - versch)))
        for i in range(10):
            self.positionen.append((int((10.5 * steps) - versch), int((steps / 2 + i * steps) - versch)))

        # Initialisieren vom Fenster
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        self.spielfeld = pygame.display.set_mode((width, width))
        pygame.display.set_caption("Monopoly-Simulation")
        # Hintergrund anzeigen
        self.hintergrund = pygame.image.load("gfx/spielfeld.png")
        self.hintergrund = pygame.transform.scale(self.hintergrund, (width, width))
        self.spielfeld.blit(self.hintergrund, (0, 0))

        #  Spielerbilder laden
        self.spieler = []
        self.pos = []
        for i in range(spieleranzahl):
            self.spieler.append(pygame.image.load(spielerbilder[i]))
            rect = self.spieler[i].get_rect()
            rect.x = 25
            rect.y = 25
            rect.move(50, 50)
            rect.centerx = 15
            rect.centery = 15
            self.spieler[-1] = pygame.transform.scale(self.spieler[-1], (self.spieler_größe, self.spieler_größe))
            self.spielfeld.blit(self.spieler[-1], self.positionen[0])
            self.pos.append(self.positionen[0])
        pygame.display.flip()

    def loading_spielerbilder(self):
        pass

    def pos_aendern(self, figur, endpos):
        feld = self.spielfeld
        spieler = self.spieler
        self.pos[figur] = self.positionen[endpos]

        # Geschwindigkeitsaenderung registrieren
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.zeit += 0.1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.zeit -= 0.1
                if self.zeit <= 0:
                    self.zeit = 0

        # Hintergrund wird hervorgeholt um die Spielfiguren zu verdecken
        feld.blit(self.hintergrund, (0, 0))
        i = 0
        while i < len(spieler):
            feld.blit(spieler[i], self.pos[i])
            i += 1
        pygame.display.flip()

    def haeuser_anzeigen(self):
        for i in Spielfeld.feld:
            if i.typ != "anderes":
                if i.haeuser > 0 and i.haueser < 6:
                    pos = Spielfeld.feld.index(i)
                    for haus in i.haeuser:
                        self.spielfeld.blit()
                        pos = self.positionen[pos] / i.haeuser

    def spielerentfernen(self, name):
        del self.spieler[name]

    def stop(self):
        pygame.quit()


class Spiel:
    def __init__(self, spieler, startgeld, startpos, buyrng):
        self.spiel = []
        # alle Teilnehmer in eine Liste eintragen
        for i in spieler:
            i = Spieler(i, startgeld, startpos, buyrng)
            self.spiel.append(i)

    @staticmethod
    def spielerzurücksetzen(name):
        for x in Spielfeld.feld:
            if x.kartentyp != "anderes":
                if x.besitzer == name:
                    x.besitzer = ""
                    x.Haeuser = 0
