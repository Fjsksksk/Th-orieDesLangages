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
        if tuple(symboles) not in self.transitions[source]:
            self.transitions[source][tuple(symboles)] = set()  # Utilisation d'un ensemble pour stocker les destinations multiples
        self.transitions[source][tuple(symboles)].add(destination)

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
            elif etat in self.terminaux:
                dot.node(etat, shape='doublecircle')
            else:
                dot.node(etat)

        for source, transitions in self.transitions.items():
            for symboles, destinations in transitions.items():
                for destination in destinations:
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

        """
        La fonction supprimer_etat permet de supprimer un état de l'automate, ainsi que toutes les transitions associées à cet état.
        paramètres:
            - etat: l'état à supprimer
    """
    def supprimer_etat(self, etat):
        # Vérifier si l'état existe dans l'automate
        if etat not in self.etats:
            raise ValueError("L'état spécifié n'existe pas dans l'automate")

        # Supprimer l'état de la liste des états
        self.etats.remove(etat)

        # Supprimer l'état des états initiaux et terminaux s'il est présent
        self.initiaux.discard(etat)
        self.terminaux.discard(etat)

        # Créer une copie des transitions pour éviter les erreurs de taille pendant l'itération
        transitions_copy = self.transitions.copy()

        # Supprimer toutes les transitions liées à cet état
        for source, transitions in transitions_copy.items():
            if source == etat:
                del self.transitions[source]  # Supprimer toutes les transitions partant de cet état
            else:
                for symboles, destinations in transitions.items():
                    self.transitions[source][symboles] = {dest for dest in destinations if dest != etat}

        # Supprimer toutes les transitions arrivant à cet état
        self.transitions = {source: {symboles: destinations for symboles, destinations in transitions.items() if etat not in destinations} for source, transitions in self.transitions.items()}

    '''
    La fonction completer permet de compléter un automate.
    ajouter un etat puit
    pour chaque etat de l'automate
        pour chaque symbole de l'alphabet
            si il n'existe pas de transition de l'etat avec le symbole
                ajouter une transition de l'etat avec le symbole vers l'etat puit
    '''
    def completer(self):
        print("Compléter l'automate")
        self.ajouter_etat('puit')
        
        print(self.etats)

        
        for etat in self.etats:
            #si l'etat est initial on passe le reste
            print("ETAT : ", etat)
            if etat in self.initiaux:
                print("EST INITIAL : ")
                print('-------------------------')
                continue
            if etat== 'puit':
                print("EST PUIT : ")
                self.ajouter_transition('puit', self.alphabet, 'puit')
                print('-------------------------')
                continue
            
            symbole_list = []
            transitions = self.transitions.get(etat, {})
            print("TRANSITIONS : ", transitions)
            # Récupère les symboles de transition de l'état
            for symboles, destinations in transitions.items():
                for symbole in symboles:
                    symbole_list.append(symbole)
            print("SYMBOLS : ", symbole_list)
            for element in self.alphabet:
                if element not in symbole_list:
                    print("ELEMENT non présent: ", element)
                    self.ajouter_transition(etat, [element], 'puit')
            print('-------------------------')

        return self

    
    
    """
    La fonction est_deterministe permet de vérifier si un automate est déterministe.
    Il ne peut pas y avoir deux transitions sortantes d'un même état avec le même symbole.
    retourne:
        - True si l'automate est déterministe, False sinon
    """
    def est_deterministe(self):
        # Parcours les états de l'automate
        for source, transitions in self.transitions.items():
            # Pour chaque état stock les symboles de transition dans une liste
            symboles_list = []
            # Parcours les transitions de chaque état
            for symboles, destinations in transitions.items():
                # Ajoute les symboles de transition dans la liste
                for symbole in symboles:
                    # Si le symbole est déjà présent dans la liste, l'automate n'est pas déterministe
                    if symbole in symboles_list:
                        return False
                    else:
                        symboles_list.append(symbole)
        return True
        
    
    def determiniser(self):
        print("Déterminisation")
        # Vérifie si l'automate est déjà déterministe
        if self.est_deterministe():
            return self

        # Création d'un nouvel automate déterministe
        automate_deterministe = Automate(self.alphabet)

        # Ajout du symbole vide à l'alphabet de l'automate déterministe
        automate_deterministe.alphabet.add('')

       
        
        return automate_deterministe

    



"""
    La fonction exporter_automate permet d'exporter un automate dans un fichier texte.
    paramètres:
        - automate: l'automate à exporter
        - filename: le nom du fichier
"""
def exporter_automate(automate, filename):
    with open(filename, 'w') as file:
        # Écriture de l'alphabet
        file.write(' '.join(automate.alphabet) + '\n')
        
        # Écriture des états
        file.write(' '.join(automate.etats) + '\n')
        
        # Écriture des états initiaux
        file.write(' '.join(automate.initiaux) + '\n')
        
        # Écriture des états terminaux
        file.write(' '.join(automate.terminaux) + '\n')
        
        # Écriture des transitions
        for source, transitions in automate.transitions.items():
            for symboles, destination in transitions.items():
                file.write(f"{source} {' '.join(symboles)} {destination}\n")


"""
    La fonction importer_automate permet d'importer un automate à partir d'un fichier texte.
    paramètres:
        - filename: le nom du fichier
    retourne:
        - l'automate importé
"""
def importer_automate(filename):
    #Vérifie si le fichier existe
    try:
        open(filename, 'r')
    except FileNotFoundError:
        print("Le fichier n'existe pas")
        return

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
            automate.ajouter_etat(etat, est_initial, est_terminal)
        
        # Lecture des transitions
        for line in file:
            source, *symboles, destination = line.split()
            automate.ajouter_transition(source, symboles, destination)
        
        return automate





"""
    La fonction union permet de réaliser une union entre deux automates.
    paramètres:
        - automate1: le premier automate
        - automate2: le deuxième automate
    retourne:
        - l'automate résultant de l'union
"""

def union(automate1, automate2):
    # Création d'un nouvel automate pour l'union
    union_automate = Automate(set.union(automate1.alphabet, automate2.alphabet))
    # Ajout du symbole vide à l'alphabet de l'union
    union_automate.alphabet.add('')

    # Ajout des états en renommant les états si nécessaire pour éviter les conflits
    for etat in automate1.etats:
        union_automate.ajouter_etat("A1_" + etat)
    for etat in automate2.etats:
        union_automate.ajouter_etat("A2_" + etat)

    # Ajout de l'état initial pour l'union
    union_automate.ajouter_etat("Initial", est_initial=True)

    # Ajout de l'état temporaire
    union_automate.ajouter_etat("temporaire")

    # Ajout des transitions et des états terminaux
    for source, transitions in automate1.transitions.items():
        for symboles, destinations in transitions.items():
            for destination in destinations:
                union_automate.ajouter_transition("A1_" + source, symboles, "A1_" + destination)
    for source, transitions in automate2.transitions.items():
        for symboles, destinations in transitions.items():
            for destination in destinations:
                union_automate.ajouter_transition("A2_" + source, symboles, "A2_" + destination)

    #parcours les transitions des états initiaux de l'automate 1
    for source, transitions in automate1.transitions.items():
        for symboles, destinations in transitions.items():
            for destination in destinations:
                if source in automate1.initiaux:
                    union_automate.ajouter_transition("temporaire", symboles, "A1_" + destination)

    #parcours les transitions des états initiaux de l'automate 2
    for source, transitions in automate2.transitions.items():
        for symboles, destinations in transitions.items():
            for destination in destinations:
                if source in automate2.initiaux:
                    union_automate.ajouter_transition("temporaire", symboles, "A2_" + destination)
    
    # Suppression des états initiaux de l'automate 1 et 2
    for etat_initial in automate1.initiaux:
        union_automate.supprimer_etat("A1_" + etat_initial)
    for etat_initial in automate2.initiaux:
        union_automate.supprimer_etat("A2_" + etat_initial)
        

    # Ajout de la transition epsilon de l'état initial de l'union vers l'état temporaire
    union_automate.ajouter_transition("Initial", [''], "temporaire")

    # Ajout des états terminaux de l'automate 1 et 2
    for etat_terminal in automate1.terminaux:
        union_automate.ajouter_etat("A1_" + etat_terminal, est_terminal=True)
    for etat_terminal in automate2.terminaux:
        union_automate.ajouter_etat("A2_" + etat_terminal, est_terminal=True)
        

    return union_automate






# Fonction permettant de faire la concaténation de deux automates

def concatenation(automate1, automate2):
    # Création d'un nouvel automate pour la concaténation
    automate_concatene = Automate(automate1.alphabet.union(automate2.alphabet))

    # Ajout du symbole vide à l'alphabet de la concaténation
    automate_concatene.alphabet.add('')

    # Ajout des états en renommant les états si nécessaire pour éviter les conflits
    for etat in automate1.etats:
        #Si l'état est initial, on le laisse initial
        if etat in automate1.initiaux:  
            automate_concatene.ajouter_etat("A1_" + etat, est_initial=True)
        automate_concatene.ajouter_etat("A1_" + etat)
    for etat in automate2.etats:
        automate_concatene.ajouter_etat("A2_" + etat)



    # Ajout des transitions et des états terminaux
    for source, transitions in automate1.transitions.items():
        for symboles, destinations in transitions.items():
            for destination in destinations:
                automate_concatene.ajouter_transition("A1_" + source, symboles, "A1_" + destination)
    for source, transitions in automate2.transitions.items():
        for symboles, destinations in transitions.items():
            for destination in destinations:
                automate_concatene.ajouter_transition("A2_" + source, symboles, "A2_" + destination)
    
    # Ajout état temporaire
    automate_concatene.ajouter_etat("temporaire")

    # Ajout des transition vide de l'automate 1 vers état temporaire
    for etat_terminal in automate1.terminaux:
        automate_concatene.ajouter_transition("A1_" + etat_terminal, [''], "temporaire")

   #parcours les transitions des états initiaux de l'automate 2
    for source, transitions in automate2.transitions.items():
        for symboles, destinations in transitions.items():
            for destination in destinations:
                if source in automate2.initiaux:
                    automate_concatene.ajouter_transition("temporaire", symboles, "A2_" + destination)
    
    # Suppression des états initiaux de l'automate 2
    for etat_initial in automate2.initiaux:
        automate_concatene.supprimer_etat("A2_" + etat_initial)

    #ajout des états terminaux de l'automate 2
    for etat_terminal in automate2.terminaux:
        automate_concatene.ajouter_etat("A2_" + etat_terminal, est_terminal=True)
    
    return automate_concatene





