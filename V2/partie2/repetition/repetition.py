import sys
sys.path.append('../../')
from automate import Automate, repetition

import os
from IPython.display import display, Image

#Automate 1

automate1 = Automate({'a', 'b'})

automate1.ajouter_etat('0', initial=True)
automate1.ajouter_etat('1', initial=True)
automate1.ajouter_etat('2', terminal=True)

automate1.ajouter_transition('0', ['a'], '2')
automate1.ajouter_transition('1', ['b'], '2')

print('Automate 1:')
automate1.to_png('repet1')
display(Image('repet1.png'))

print("\n\n")

# Repetition de l'automate 1
print("Repetition de l'automate 1 :\n")
automate = repetition(automate1)
print(automate)
automate.to_png('repet')