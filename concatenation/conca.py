import sys
sys.path.append('../')
from automate import Automate, concatenation

import os


# Création de l'automate 1
automate1 = Automate({'a', 'b'})

# Ajout des états avec indication des états initiaux et terminaux
automate1.ajouter_etat('start')
automate1.ajouter_etat('start', est_initial=True)
automate1.ajouter_etat('0')
automate1.ajouter_etat('1')
automate1.ajouter_etat('1', est_terminal=True)
automate1.ajouter_etat('2')
automate1.ajouter_etat('2', est_terminal=True)

# Ajout des transitions
automate1.ajouter_transition('start', [], '0')
automate1.ajouter_transition('0', ['a'], '1')
automate1.ajouter_transition('1', ['b'], '1')
automate1.ajouter_transition('0', ['b'], '2')

# Création de l'automate 2

automate2 = Automate({'a', 'b'})

# Ajout des états avec indication des états initiaux et terminaux
automate2.ajouter_etat('start1')
automate2.ajouter_etat('start1', est_initial=True)
automate2.ajouter_etat('start2')
automate2.ajouter_etat('start2', est_initial=True)

automate2.ajouter_etat('0')
automate2.ajouter_etat('1')
automate2.ajouter_etat('2', est_terminal=True)

# Ajout des transitions
automate2.ajouter_transition('start1', [], '0')
automate2.ajouter_transition('start2', [], '1')
automate2.ajouter_transition('0', ['a'], '2')
automate2.ajouter_transition('1', ['b'], '2')




automate1.to_png('conca1')
automate2.to_png('conca2')

# Concaténation des deux automates
automate = concatenation(automate1, automate2)
automate.to_png('conca')



