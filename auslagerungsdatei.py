#Alte Tk Animation

def __init__(self):
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

    GUIThread.__init__(self)


def figuren_erstellen(self, anzahl):
    # Figuren konfigurieren
    figuren = [PhotoImage(file="gfx/figur0.gif"), PhotoImage(file="gfx/figur1.gif"),
               PhotoImage(file="gfx/figur2.gif"), PhotoImage(file="gfx/figur3.gif"),
               PhotoImage(file="gfx/figur4.gif"), PhotoImage(file="gfx/figur5.gif")]
    for x in range(0, anzahl):
        self.spielerfiguren.append(self.canvas.create_image(402, 855, image=figuren[x + 1]))
        print("Spieler: {} id: {} koordinaten: {}".format(x, self.spielerfiguren[x],
                                                          self.canvas.coords(self.spielerfiguren[x])))


def run(self):
    print("Starte Animation")
    self.root.mainloop()


# Figuren auf eine neue Position verschieben
def __pos_aendern(self, figur, endkoordinaten):
    x = endkoordinaten[0] - self.canvas.coords(self.spielerfiguren[figur])[0]
    y = endkoordinaten[1] - self.canvas.coords(self.spielerfiguren[figur])[1]
    self.canvas.move(self.spielerfiguren[figur], x, y)
    self.root.update()


def spielfeldpos_aendern(self, figur, endpos):
    print(figur)
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

# Spiel starten alt


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

# Alte Threading Klasse

class GUIThread(threading.Thread):
    def __init__(self):
        self._stop = False
        threading.Thread.__init__(self)

    def run(self):
        pass

    def stop(self):
        self._stop = True
