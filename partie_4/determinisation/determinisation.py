import sys
sys.path.append('../../')
from automate import Automate

import os

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

automate1.to_png('automate1_non_deterministe.png')

automate1.completer().to_png('automate1_complet.png')

# Vérification de la déterminisation
est_deterministe= automate1.est_deterministe()
print(f"L'automate est déterministe : {est_deterministe}")

# Déterminisation de l'automate
automate1_determinise = automate1.determiniser()
automate1_determinise.to_png('automate1_determinise.png')
print("Automate déterminisé")
