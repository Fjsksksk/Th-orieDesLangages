
class Transition:

    def __init__(self, depart, symbole, arrivee):
        self.depart = depart
        self.symbole = symbole
        self.arrivee = arrivee

    def __str__(self):
        return f"{self.depart} --{self.symbole}--> {self.arrivee}"
    