## chemin vers le fichier automate.py
import sys
sys.path.append('../../')
from automate import Automate

import os
from IPython.display import display, Image



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

if os.path.exists('automate_cherche.png'):
    os.remove('automate_cherche.png')


automate2 = automate.minimiser()
print("Recherche dans l'automate suivant")
automate2.to_png('automate_cherche')
display(Image('automate_cherche.png'))

print("L'automate accepte-t-il le mot 'abba' ?")
print(automate2.accepte_mot('abba'))
print("L'automate accepte-t-il le mot 'abbb' ?")
print(automate2.accepte_mot('abbb'))
print("L'automate accepte-t-il le mot 'bba' ?")
print(automate2.accepte_mot('bba'))
