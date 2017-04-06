from GUI import *
from Spieler import *
from time import sleep


class SpielStarten:
    def __init__(self):
        self.auswertungsliste = []

        self.gui = GUI()
        self.gui.erstellen()
        startbar = self.gui.startbar()

        if startbar is True:
            # Variablen definieren
            g = self.gui
            sp, sk, buyrng = g.get_start_pos(), g.get_start_kap(), g.get_buyrng()
            self.sa, self.sw, self.res, self.zeit = g.get_anzahl(), g.get_wdh(), g.get_resolution(), g.get_zeit()
            self.namenliste, self.geldliste, self.stundenliste = [], [], []
            spieler = [i for i in range(self.sa)]
            # um das Spielfenster kleiner zu öffnen die übergebene Zahl zur Animation verringern
            self.buyrng = True
            self.spiel = Spiel(spieler, sk, sp, buyrng)

            i = 1
            while i <= self.sw:
                self.spiel.__init__(spieler, sk, sp, buyrng)
                self.auswertungsliste.append(self.schleife())
                print("Spiel", i, "beendet.")
                i += 1

            Auswertung(self.sw, self.geldliste, self.stundenliste, self.namenliste)

    def schleife(self):
        spiel = self.spiel.spiel
        self.animation = Animation(self.sa, self.res, self.zeit)
        gewinnerstehtnichtfest = True
        # Spielschleife wird ausgeführt solange mehr als ein Spieler noch drin ist
        while gewinnerstehtnichtfest:
            # jeder for-schleifen-zyklus ist eine Runde aller Spieler
            for i in spiel:
                # Wenn Spieler nicht im Gefängnis ist wird gewürfelt
                i.im_gefaengnis is False and i.wuerfeln()
                sleep(self.animation.zeit)
                self.animation.pos_aendern(spiel.index(i), i.pos)
                i.feldchecken(self.spiel.spiel)
                # wenn Spieler unter 1 Euro hat wird er aus dem Spiel entfernt und seine Strassen wieder kaufbar gemacht
                if i.geld < 1:
                    # print(i.name, "ist aus dem Spiel")
                    self.spiel.spielerzurücksetzen(i.name)
                    self.animation.spielerentfernen(spiel.index(i))
                    del spiel[spiel.index(i)]
            # wenn nur noch 1 Spieler im Spiel ist wird die Schleife beendet
            if len(spiel) == 1:
                gewinnerstehtnichtfest = False

        self.namenliste.append(spiel[0].name)
        self.geldliste.append(spiel[0].geld)
        self.stundenliste.append(round(spiel[0].get_spielzeit(), 2))
        geld = spiel[0].geld
        self.spiel.spielerzurücksetzen(spiel[0].name)
        self.animation.stop()
        del spiel[0]
        return geld


class Auswertung:
    def __init__(self, sw, geldliste, stundenliste, namenliste):
        # Variablen definieren
        self.sw, self.geldliste, self.stundenliste, self.namenliste = sw, geldliste, stundenliste, namenliste
        # PyGame schließen
        pygame.quit()
        # Fenster erstellen
        self.root = Tk()
        self.auswertungsfenster = Frame(self.root)
        self.auswertungsfenster.pack()
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.focus_force()
        self.root.title("Monopoly Simulation - Auswertung")

        # Fenster mittig zentrieren
        w = 800
        h = 75 + self.sw * 25
        if sw > 30:
            h = 100
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.root.config(bg='lightgrey')
        if platform() == 'Darwin':
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

        Label(self.auswertungsfenster, text=("Auswertung", "der", self.sw, "simulierten", "Spiele:"),
              font="Verdana 14 bold").grid(row=0, columnspan=2)
        zeit = self.zeiten(self.durchschnitt_zeit(self.stundenliste))
        # Einzelwerte der simulierten Spiele anzeigen
        # um das Fenster klein zu halten werden nur maximal 30 Ergebnisse angezeigt
        if sw < 30:
            for i in range(1, sw + 1):
                zeiten = self.zeiten(self.stundenliste[i - 1])
                Label(self.auswertungsfenster, text=(
                    "-", "Das", str(i) + ".", "Spiel", "wurde", "durch", "Spieler", self.namenliste[i - 1], "mit",
                    self.geldliste[i - 1], "Euro", "gewonnen.")).grid(row=i, column=0, columnspan=3)
                Label(self.auswertungsfenster, text=(
                    "Es", "hätte", zeiten[0], "Stunden", "und", zeiten[1], "Minuten" "in", "der", "Wirklichkeit",
                    "gedauert.")).grid(row=i, column=3, columnspan=3)
        else:
            # alle Werte als CSV ausgeben
            file = open("Auswertung.csv", "w")
            file.write("Geld; Stunden; Minuten")
            file.write("\n")
            for i in range(sw):
                zeiten = self.zeiten(self.stundenliste[i])
                text = str(self.geldliste[i]) + "; " + str(zeiten[0]) + "; " + str(zeiten[1])
                file.write(text)
                file.write("\n")
            file.close()


        # Durchschnittswerte anzeigen
        Label(self.auswertungsfenster, text=(
            "Durchschnittlich", "wurden", "die", "Spiele", "mit", self.durchschnitt(self.geldliste), "Euro",
            "gewonnen.")).grid(row=self.sw + 2, column=0, columnspan=3)
        Label(self.auswertungsfenster, text=(
            "Sie", "hätten", "durchschnittlich", zeit[0], "Stunden", "und", zeit[1], "Minuten", "gedauert.")).grid(
            row=self.sw + 2, column=3, columnspan=3)
        # Buttons
        Button(self.auswertungsfenster, text="Beenden", command=self.root.destroy, bg="red").grid(row=self.sw + 3)
        Button(self.auswertungsfenster, text="Erneut Starten", command=self.neustart, bg="green").grid(row=self.sw + 3,
                                                                                                       column=1)
        self.root.bind('<KeyPress-Return>', self.neustart_enter)
        self.root.bind("<Escape>", self.enter_destroy)
        self.root.mainloop()

    def enter_destroy(self, x):
        self.root.destroy()

    def neustart_enter(self, x):
        self.neustart()

    def neustart(self):
        self.root.destroy()
        SpielStarten()

    # Methode um aus einem Array den Durchschnittswert zu bilden
    @staticmethod
    def durchschnitt(liste):
        return liste[0] if len(liste) == 1 else int(sum(liste) / len(liste))

    @staticmethod
    def durchschnitt_zeit(liste):
        return liste[0] if len(liste) == 1 else "{0:.2f}".format(sum(liste) / len(liste))

    # Methode um aus einem Array den Median zu bilden
    @staticmethod
    def median(liste):
        mitte = (len(liste) - 1) / 2
        return liste[int(mitte)] if mitte.is_integer() else int((liste[int(mitte)] + liste[int(mitte + 1)]) / 2)

    @staticmethod
    def zeiten(zeit):
        stunden, minuten = divmod(float(zeit), 1)
        return (int(stunden), int(60 * minuten))


SpielStarten()
