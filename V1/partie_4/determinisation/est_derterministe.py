import sys
sys.path.append('../../')
from automate import Automate
from IPython.display import display, Image

import os


print("Automate 1:")
## Création de l'automate 1 non déterministe

automate1 = Automate({'a', 'b', 'd'})

# Ajout des états avec indication des états initiaux et terminaux
automate1.ajouter_etat('start')
automate1.ajouter_etat('start', est_initial=True)
automate1.ajouter_etat('start2')
automate1.ajouter_etat('start2', est_initial=True)
automate1.ajouter_etat('0')
automate1.ajouter_etat('1')
automate1.ajouter_etat('2')
automate1.ajouter_etat('2', est_terminal=True)

# Ajout des transitions
automate1.ajouter_transition('start', [], '0')
automate1.ajouter_transition('start2', [], '1')
automate1.ajouter_transition('0', ['a','b'], '0')
automate1.ajouter_transition('0', ['b'], '1')
automate1.ajouter_transition('1', ['a','b'], '2')
automate1.ajouter_transition('2', ['a','b'], '2')

automate1.to_png('est_deterministe1')

display(Image('est_deterministe1.png'))
# Vérification de la déterminisation
est_deterministe= automate1.est_deterministe()
print(f"L'automate est déterministe : {est_deterministe}")


print("\n\n")
print("Essayons avec l'automate2 :")

## Création de l'automate 2 non déterministe

automate2 = Automate({'a', 'b', 'd'})

# Ajout des états avec indication des états initiaux et terminaux
automate2.ajouter_etat('start')
automate2.ajouter_etat('start', est_initial=True)
automate2.ajouter_etat('start2')
automate2.ajouter_etat('start2', est_initial=True)
automate2.ajouter_etat('0')
automate2.ajouter_etat('1')
automate2.ajouter_etat('2')
automate2.ajouter_etat('2', est_terminal=True)

# Ajout des transitions
automate2.ajouter_transition('start', [], '0')
automate2.ajouter_transition('start2', [], '1')
automate2.ajouter_transition('0', ['a'], '0')
automate2.ajouter_transition('0', ['b'], '1')
automate2.ajouter_transition('1', ['a','b'], '2')
automate2.ajouter_transition('2', ['a','b'], '2')

automate2.to_png('est_deterministe2')

display(Image('est_deterministe2.png'))
# Vérification de la déterminisation
est_deterministe2= automate2.est_deterministe()
print(f"L'automate est déterministe : {est_deterministe2}")