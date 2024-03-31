import sys
sys.path.append('../../')
from automate import Automate
import os
from IPython.display import Image, display
## Création de l'automate 1 non déterministe
print("Création de l'automate 1 non complet")
automate1 = Automate({'a', 'b', 'd'})


automate1.ajouter_etat('0', initial=True)
automate1.ajouter_etat('1')
automate1.ajouter_etat('2', terminal=True)

# Ajout des transitions
automate1.ajouter_transition('0', ['b'], '1')
automate1.ajouter_transition('1', ['a','b'], '2')
automate1.ajouter_transition('2', ['a','b'], '2')

if os.path.exists('completer.png'):
    os.remove('completer.png')
if os.path.exists('completer1.png'):
    os.remove('completer1.png')

print("Automate 1 non complet")
automate1.to_png('completer')
display(Image('completer.png'))

print("Automate 1 complet")
automate1.completer()
automate1.to_png('completer1')
display(Image('completer1.png'))