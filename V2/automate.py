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
                nom = "init"+etat.nom
                dot.node(nom, shape='point')
                dot.edge(nom, etat.nom, label='')
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

    def etat_poubelle(self):
        self.ajouter_etat('poubelle')
        for symbole in self.alphabet:
            if symbole == '':
                continue
            self.ajouter_transition('poubelle', symbole, 'poubelle')



    def completer(self):
        self.alphabet.add('')
        self.ajouter_etat('poubelle')
        for etat in self.etats:
            # Liste des symboles de transition pour l'état
            symboles = []
            for transition in self.transitions:
                if transition.depart == etat.nom:
                    symbole = transition.symbole
                    for s in symbole:
                        symboles.append(s)
            
            alphabet = list(self.alphabet)
            
            for symbole in alphabet:
                if symbole == '':
                    continue
                if symbole not in symboles:
                    self.ajouter_transition(etat.nom, symbole, 'poubelle')
                    etat_poubelle = True
            
        return self
    
    def est_deterministe(self):
        for etat in self.etats:
            symboles = []
            for transition in self.transitions:
                if transition.depart == etat.nom:
                    symbole = transition.symbole
                    for s in symbole:
                        symboles.append(s)
            for symbole in symboles:
                if symboles.count(symbole) > 1:
                    return False
        return True
    
    def table_transition_determinisation(self):
        # Création de la table de transition
        table = {}
        
        #liste des états initiaux
        etats_initiaux = []
        for etat in self.etats:
            if etat.initial:
                etats_initiaux.append(etat.nom)
        etats_initiaux.sort()
        tuple_etats_initiaux = tuple(etats_initiaux)

        etat_a_traiter = [tuple_etats_initiaux]
        etat_traiter = []

        while etat_a_traiter:
            etat = etat_a_traiter.pop()
            if etat in etat_traiter:
                continue
            etat_traiter.append(etat)
            etat_en_cours = []
            for e in etat:
                etat_en_cours.append(e)
            for symbole in self.alphabet:
                if symbole == '':
                    continue
                etats_arrivee = []
                for etat_courant in etat:
            
                    for transition in self.transitions:
                        if transition.depart == etat_courant and symbole in transition.symbole:
                           
                            if transition.arrivee not in etats_arrivee:
                                etats_arrivee.append(transition.arrivee)
                # On trie les états par ordre alphabétique ou croissant
                etats_arrivee.sort()
                tuple_etats_arrivee = tuple(etats_arrivee)

                #Ajout de la transition à la table
                if etat not in table:
                    table[etat] = {}
                table[etat][symbole] = tuple_etats_arrivee
                
                


                
                if not tuple_etats_arrivee:
                    
                    continue
                
                if tuple_etats_arrivee not in etat_a_traiter:

                    etat_a_traiter.append(tuple_etats_arrivee)

                    continue

                else : 

                    continue


       
        return table
    
    def afficher_table(self):
        table = self.table_transition_determinisation()
        for etat in table:
            print(etat, table[etat])


    
    def determiniser(self):
        # Création de l'automate déterminisé
        automate_determinise = Automate(self.alphabet)
        # Création de la table de transition
        table = self.table_transition_determinisation()
        
        #liste des états initiaux
        etats_initiaux = []
        for etat in self.etats:
            if etat.initial:
                etats_initiaux.append(etat.nom)
        etats_initiaux.sort()

        #liste des états terminaux
        etats_terminaux = []
        for etat in self.etats:
            if etat.terminal:
                etats_terminaux.append(etat.nom)
        etats_terminaux.sort()
        # création des états
        init = True
        i = 0
        for etats in table:
            if i != 0:
                init = False
            term = False
            taille = len(etats)
            for etat in etats:
                if etat in etats_terminaux:
                    term = True
            automate_determinise.ajouter_etat(str(etats), term, init)
            i += 1
            
            
        # Création des transitions
        for etat in table:
            for symbole in self.alphabet:
                if symbole == '':
                    continue
                if symbole not in table[etat]:
                    continue
                etat_depart = [etat][0]
                etat_arrivee = table[etat][symbole]
                if etat_arrivee != ():

                    transition = Transition(str(etat_depart), symbole, str(etat_arrivee))
                    automate_determinise.transitions.append(transition)
                else:
                    continue
        


        return automate_determinise





        
        
        
    
               

    

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




def union(automate1, automate2):
    #Union des alphabets
    alphabet = automate1.alphabet.union(automate2.alphabet)
    automate_union = Automate(alphabet)
    # Ajout du symbole vide
    alphabet.add('')

    #Renommer les états de l'automate 1 et 2
    for etat in automate1.etats:
        etat.nom = 'A1_' + etat.nom
    for etat in automate2.etats:
        etat.nom = 'A2_' + etat.nom

    # Ajout d'un état initial
    automate_union.ajouter_etat('initial', initial=True)

    # Transforme les états initiaux en état non initial avec une transition epsilon vers l'état initial
    for etat in automate1.etats:
        if etat.initial:
            etat.initial = False
            automate_union.ajouter_transition('initial', '', etat.nom)
    for etat in automate2.etats:
        if etat.initial:
            etat.initial = False
            automate_union.ajouter_transition('initial', '', etat.nom)
    
    # Ajout des états de l'automate 1 et 2
    for etat in automate1.etats:
        if (etat not in automate_union.etats):
            automate_union.etats.append(etat)
    for etat in automate2.etats:
        if (etat not in automate_union.etats):
            automate_union.etats.append(etat)

    # Ajout des transitions de l'automate 1 et 2 en les renommant
    for transition in automate1.transitions:
        depart = 'A1_' + transition.depart
        arrivee = 'A1_' + transition.arrivee
        automate_union.ajouter_transition(depart, transition.symbole, arrivee)
    for transition in automate2.transitions:
        depart = 'A2_' + transition.depart
        arrivee = 'A2_' + transition.arrivee
        automate_union.ajouter_transition(depart, transition.symbole, arrivee)  
    return automate_union





def concatenation(automate1, automate2):
    
    #Union des alphabets
    alphabet = automate1.alphabet.union(automate2.alphabet)
    #ajout du symbole vide
    alphabet.add('')

    #Renommer les états de l'automate 1 et 2
    for etat in automate1.etats:
        etat.nom = 'A1_' + etat.nom
    for etat in automate2.etats:
        etat.nom = 'A2_' + etat.nom
    
    
    #Ajout de l'automate 1
    automate_concat = Automate(alphabet)
    #Ajout etat temporaire
    automate_concat.ajouter_etat('temporaire')
    for etat in automate1.etats:
        #Si l'etat est terminal, on le rend non terminal
        if etat.terminal:
            etat.terminal = False
            # transition vers temporaire
            automate_concat.ajouter_transition(etat.nom, '', 'temporaire')
        automate_concat.etats.append(etat)
    for transition in automate1.transitions:
        depart = 'A1_' + transition.depart
        arrivee = 'A1_' + transition.arrivee
        automate_concat.ajouter_transition(depart, transition.symbole, arrivee)

    #Ajout de l'automate 2
    for etat in automate2.etats:
        if etat.initial:
            etat.initial = False
            # transition de temporaire vers l'etat initial
            automate_concat.ajouter_transition('temporaire', '',etat.nom)
        automate_concat.etats.append(etat)
    for transition in automate2.transitions:
        depart = 'A2_' + transition.depart
        arrivee = 'A2_' + transition.arrivee
        automate_concat.ajouter_transition(depart, transition.symbole, arrivee)

    return automate_concat



    
def repetition(automate):
    #Fonction permettant de transformer un automate en une répétition de celui-ci
    automate_repetition = Automate(automate.alphabet)
    #Ajout du symbole vide
    automate_repetition.alphabet.add('')
    #Ajout de l'etat initial
    automate_repetition.ajouter_etat('initial', initial=True)
    #Renommer les états
    for etat in automate.etats:
        etat.nom = 'R_' + etat.nom
    #Ajout des états de l'automate
    for etat in automate.etats:
        automate_repetition.etats.append(etat)
    #Ajout de l'etat initial
    automate_repetition.etats.append(Etat('initial', initial=True))
    #Ajout des transitions
    for etat in automate.etats:
        if etat.initial:
            automate_repetition.ajouter_transition('initial', '', etat.nom)
        if etat.terminal:
            automate_repetition.ajouter_transition(etat.nom, '', 'initial')
        for transition in automate.transitions:
            depart = 'R_' + transition.depart
            arrivee = 'R_' + transition.arrivee
            automate_repetition.ajouter_transition(depart, transition.symbole, arrivee)
    return automate_repetition




            
            


        


    