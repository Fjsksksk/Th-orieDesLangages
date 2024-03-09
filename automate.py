from graphviz import Digraph

class Automate:

    """
        La fonction __init__ permet de créer un automate avec un alphabet donné.
        paramètres:
            - alphabet: l'alphabet de l'automate
            - self : l'automate
    """
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.etats = set()
        self.initiaux = set()
        self.terminaux = set()
        self.transitions = {}

    """
        La fonction ajouter_etat permet d'ajouter un état à l'automate.
        paramètres:
            - etat: l'état à ajouter
            - est_initial: indique si l'état est initial
            - est_terminal: indique si l'état est terminal
    """
    def ajouter_etat(self, etat, est_initial=False, est_terminal=False):
        self.etats.add(etat)
        if est_initial:
            self.initiaux.add(etat)
        if est_terminal:
            self.terminaux.add(etat)

    """
        La fonction ajouter_transition permet d'ajouter une transition à l'automate.
        paramètres:
            - source: l'état source de la transition
            - symboles: les symboles de la transition (une liste)
            - destination: l'état destination de la transition
    """
    def ajouter_transition(self, source, symboles, destination):
        if source not in self.etats or destination not in self.etats:
            raise ValueError("État source ou destination invalide")
        for symbole in symboles:
            if symbole not in self.alphabet:
                raise ValueError("Symbole non présent dans l'alphabet")
        if source not in self.transitions:
            self.transitions[source] = {}
        if tuple(symboles) in self.transitions[source]:
            raise ValueError("Transition déjà définie pour ces symboles")
        self.transitions[source][tuple(symboles)] = destination

    """
        La fonction destination_transition permet de récupérer l'état destination d'une transition à partir d'un état source et d'un symbole.
        paramètres:
            - source: l'état source de la transition
            - symboles: les symboles de la transition
    
        retourne:
            - l'état destination de la transition si elle existe, None sinon
    """
    def destination_transition(self, source, symboles):
        return self.transitions.get(source, {}).get(tuple(symboles))

    """
        La fonction __str__ permet d'afficher l'automate.
        retourne:
            - une chaîne de caractères représentant l'automate
    """
    def __str__(self):
        result = "Alphabet: " + str(self.alphabet) + "\n"
        result += "Etats: " + str(self.etats) + "\n"
        result += "Etats initiaux: " + str(self.initiaux) + "\n"
        result += "Etats terminaux: " + str(self.terminaux) + "\n"
        result += "Transitions:\n"
        for source, transitions in self.transitions.items():
            for symboles, destination in transitions.items():
                result += f"     {source} --({', '.join(symboles)})--> {destination}\n"
        return result
    
    """
        La fonction to_dot permet de générer une représentation graphique de l'automate au format DOT.
        retourne:
            - une chaîne de caractères représentant l'automate au format DOT
    """
    def to_dot(self):
        dot = Digraph()
        dot.attr(rankdir='LR')
        for etat in self.etats:
            if etat in self.initiaux:
                dot.node(etat, shape='point')
            if etat in self.terminaux:
                dot.node(etat, shape='doublecircle')
            dot.node(etat)
        for source, transitions in self.transitions.items():
            for symboles, destination in transitions.items():
                dot.edge(source, destination, label=', '.join(symboles))
        return dot

    """
        La fonction to_png permet de générer une représentation graphique de l'automate au format PNG.
        paramètres:
            - filename: le nom du fichier PNG à générer
    """
    def to_png(self, filename):
        dot = self.to_dot()
        dot.render(filename, format='png', cleanup=True)

    
    

                

## test ##

# Création d'un automate avec un alphabet {'a', 'b', 'c','d'}
automate = Automate({'a', 'b', 'c','d'})

# Ajout des états avec indication des états initiaux et terminaux
automate.ajouter_etat('1', est_initial=True)
automate.ajouter_etat('2')
automate.ajouter_etat('3', est_terminal=True)
automate.ajouter_etat('4')

# Ajout des transitions
automate.ajouter_transition('1', ['a'], '2')
automate.ajouter_transition('2', ['b', 'c'], '3')
automate.ajouter_transition('2', ['d'], '4')
automate.ajouter_transition('4', ['a'], '3')
automate.ajouter_transition('4', ['b'], '2')

# Affichage de l'automate
print(automate)
#print(automate.to_dot())
automate.to_png('automate')



