
class Etat:
    def __init__(self, nom, terminal=False, initial=False):
        self.nom = nom
        self.terminal = terminal
        self.initial = initial

    def __str__(self):
        return self.nom
    
    def __eq__(self, other):
        return self.nom == other.nom
    
    