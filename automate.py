class Automate:
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.etats = set()
        self.initiaux = set()
        self.terminaux = set()
        self.transitions = {}

    def ajouter_etat(self, etat, est_initial=False, est_terminal=False):
        self.etats.add(etat)
        if est_initial:
            self.initiaux.add(etat)
        if est_terminal:
            self.terminaux.add(etat)

    def ajouter_transition(self, source, symbole, destination):
        if source not in self.etats or destination not in self.etats:
            raise ValueError("État source ou destination invalide")
        if symbole not in self.alphabet:
            raise ValueError("Symbole non présent dans l'alphabet")
        if source not in self.transitions:
            self.transitions[source] = {}
        if symbole in self.transitions[source]:
            raise ValueError("Transition déjà définie pour ce symbole")
        self.transitions[source][symbole] = destination

    def symbole_transition(self, source, destination):
        for symbole, dest in self.transitions.get(source, {}).items():
            if dest == destination:
                return symbole
        return None

    def destination_transition(self, source, symbole):
        return self.transitions.get(source, {}).get(symbole)

    def __str__(self):
        result = "Alphabet: " + str(self.alphabet) + "\n"
        result += "Etats: " + str(self.etats) + "\n"
        result += "Etats initiaux: " + str(self.initiaux) + "\n"
        result += "Etats terminaux: " + str(self.terminaux) + "\n"
        result += "Transitions:\n"
        for source, transitions in self.transitions.items():
            for symbole, destination in transitions.items():
                result += f"     {source} --({symbole})--> {destination}\n"
        return result



## test ##

# Création d'un automate avec un alphabet {'a', 'b', 'c','d'}
automate = Automate({'a', 'b', 'c','d'})

# Ajout des états avec indication des états initiaux et terminaux
automate.ajouter_etat('1', est_initial=True)
automate.ajouter_etat('2')
automate.ajouter_etat('3', est_terminal=True)
automate.ajouter_etat('4')

# Ajout des transitions
automate.ajouter_transition('1', 'a', '2')
automate.ajouter_transition('1', 'b', '1')
automate.ajouter_transition('2', 'b', '3')
automate.ajouter_transition('3', 'c','4')
automate.ajouter_transition('3', 'd','4')

# Affichage de l'automate
print(automate)
