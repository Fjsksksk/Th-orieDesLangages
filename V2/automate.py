from etat import Etat
from transition import Transition
from graphviz import Digraph


class Automate:

    def __init__(self, alphabet):
        self.etats = []
        self.alphabet = alphabet
        self.transitions = []

    def ajouter_etat(self, nom, terminal=False, initial=False):
        etat = Etat(nom, terminal, initial)
        self.etats.append(etat)

    def ajouter_transition(self, depart, symbole, arrivee ):
        #utilise la classe Transition pour creer une transition
        transition = Transition(depart, symbole, arrivee)
        self.transitions.append(transition)
    

    def affichage_transition(self):
        for transition in self.transitions:
            print(transition[0], transition[1], self.transitions[transition])

    def __str__(self):
            result = "Alphabet: " + str(self.alphabet) + "\n"
            result += "Etats: " + ", ".join(str(etat) for etat in self.etats) + "\n"
            result += "Etats terminaux: " + ", ".join(str(etat) for etat in self.etats if etat.terminal) + "\n"
            result += "Etat initial: " + str([etat for etat in self.etats if etat.initial][0]) + "\n"
            result += "Transitions: \n"
            # Affiche la liste des transitions en utilisant la str de la classe Transition
            for transition in self.transitions:
                result += str(transition) + "\n"
                
            return result
    
    def to_dot(self):
        dot = Digraph()
        dot.attr(rankdir='LR')
        for etat in self.etats:
            if etat.initial:
                #ajout etat initial avec transition vide vers l'etat
                dot.node('init', shape='point')
                dot.edge('init', etat.nom)
            if etat.terminal:
                dot.node(etat.nom, shape='doublecircle')
            dot.node(etat.nom)
        
        for transition in self.transitions:
            depart = transition.depart
            symbole = transition.symbole
            arrivee = transition.arrivee
            if type(symbole) == list:
                symbole = ','.join(symbole)
            dot.edge(depart, arrivee, label=symbole)
        
        return dot
    
    def to_png(self, filename):
        dot = self.to_dot()
        dot.render(filename, format='png', cleanup=True)

    def export(self, filename):
        with open(filename, 'w') as f:
            # Ecriture de l'alphabet
            f.write(' '.join(self.alphabet) + '\n')

            # Ecriture des états juste le nom
            f.write(' '.join([etat.nom for etat in self.etats]) + '\n')

            # Ecriture des états initiaux
            f.write(' '.join([etat.nom for etat in self.etats if etat.initial]) + '\n')

            # Ecriture des états terminaux
            f.write(' '.join([etat.nom for etat in self.etats if etat.terminal]) + '\n')

            # Ecriture des transitions
            for transition in self.transitions:
                depart = transition.depart
                symbole = transition.symbole
                arrivee = transition.arrivee
                if type(symbole) == list:
                    symbole = ' '.join(symbole)
                f.write(f"{depart} {symbole} {arrivee}\n")

def importation(filename):
    # Vérifie si le fichier existe
    try:
        open(filename, 'r')
    except FileNotFoundError:
        print("Le fichier n'existe pas")
        return None

    with open(filename, 'r') as file:
        # Lecture de l'alphabet
        alphabet = set(file.readline().split())

        # Lecture des états
        etats = set(file.readline().split())

        # Lecture des états initiaux
        initiaux = set(file.readline().split())
        # Lecture des états terminaux
        terminaux = set(file.readline().split())
        
        # Création de l'automate
        automate = Automate(alphabet)
        for etat in etats:
            est_initial = etat in initiaux
            est_terminal = etat in terminaux
            automate.ajouter_etat(etat, est_terminal, est_initial)

        # Lecture des transitions
        for line in file:
            elements = line.split()
            source = elements[0]
            symboles = elements[1:-1]  # Récupérer tous les symboles sauf le dernier
            destination = elements[-1]
            automate.ajouter_transition(source, symboles, destination)

    return automate
            
            


        


    