## chemin vers le fichier automate.py
import sys
sys.path.append('../../')
from automate import Automate

import os
from IPython.display import display, Image

""" Exemple d'automate à minimiser
automate = Automate({'a', 'b'})

automate.ajouter_etat('0', initial=True)
automate.ajouter_etat('1')
automate.ajouter_etat('2', terminal=True)
automate.ajouter_etat('3', terminal=True)

automate.ajouter_transition('0', ['b'], '0')
automate.ajouter_transition('0', ['a'], '1')
automate.ajouter_transition('1', ['a'], '1')
automate.ajouter_transition('1', ['b'], '2')
automate.ajouter_transition('2', ['a'], '3')
automate.ajouter_transition('2', ['b'], '2')
automate.ajouter_transition('3', ['a'], '3')
automate.ajouter_transition('3', ['b'], '2')
"""

automate = Automate({'a', 'b'})

automate.ajouter_etat('1', initial=True, terminal=True)
automate.ajouter_etat('2')
automate.ajouter_etat('3')
automate.ajouter_etat('4', terminal=True)

automate.ajouter_transition('1', ['b'], '1')
automate.ajouter_transition('1', ['a'], '2')
automate.ajouter_transition('2', ['a'], '2')
automate.ajouter_transition('2', ['b'], '4')
automate.ajouter_transition('4', ['b'], '4')
automate.ajouter_transition('4', ['a'], '3')
automate.ajouter_transition('3', ['a'], '3')
automate.ajouter_transition('3', ['b'], '1')


if os.path.exists('minimisation.png'):
    os.remove('minimisation.png')
if os.path.exists('minimisation_2.png'):
    os.remove('minimisation_2.png')

print("Automate avant minimisation")
automate.to_png('minimisation')
display(Image('minimisation.png'))
automate2 = automate.minimiser()
print("Automate après minimisation")
automate2.to_png('minimisation_2')
display(Image('minimisation_2.png'))

