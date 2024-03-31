import sys
sys.path.append('../../')
from automate import Automate
from IPython.display import Image, display

import os

if os.path.exists('automate1_non_deterministe.png'):
    os.remove('automate1_non_deterministe.png')
if os.path.exists('automate1_determinise.png'):
    os.remove('automate1_determinise.png')

## Création de l'automate 1 non déterministe

automate1 = Automate({'a', 'b', 'd'})

# Ajout des états avec indication des états initiaux et terminaux

automate1.ajouter_etat('0', initial=True)
automate1.ajouter_etat('1')
automate1.ajouter_etat('2', terminal=True)

# Ajout des transitions
automate1.ajouter_transition('0', ['a','b'], '0')
automate1.ajouter_transition('0', ['b'], '1')
automate1.ajouter_transition('1', ['a','b'], '2')
automate1.ajouter_transition('2', ['a','b'], '2')

automate1.to_png('automate1_non_deterministe')

table = automate1.afficher_table()