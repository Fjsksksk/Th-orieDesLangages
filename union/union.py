## imporye la classe automate présent au chemin ../automate.py

## chemin vers le fichier automate.py
import sys
sys.path.append('../')
from automate import Automate, union


import os
from IPython.display import display, Image


# Création de l'automate 1

automate1 = Automate({'a', 'b', 'd'})

# Ajout des états avec indication des états initiaux et terminaux
automate1.ajouter_etat('start')
automate1.ajouter_etat('start', est_initial=True)
automate1.ajouter_etat('start2')
automate1.ajouter_etat('start2', est_initial=True)
automate1.ajouter_etat('0')
automate1.ajouter_etat('1')
automate1.ajouter_etat('1')
automate1.ajouter_etat('2')
automate1.ajouter_etat('3')
automate1.ajouter_etat('3', est_terminal=True)

# Ajout des transitions
automate1.ajouter_transition('start', [], '0')
automate1.ajouter_transition('0', ['b'], '0')
automate1.ajouter_transition('0', ['a'], '1')
automate1.ajouter_transition('1', ['a','b'], '2')
automate1.ajouter_transition('start2', [], '2')
automate1.ajouter_transition('2', ['d'], '3')

# Création de l'automate 2

automate2 = Automate({'a', 'b'})

# Ajout des états avec indication des états initiaux et terminaux
automate2.ajouter_etat('start1')
automate2.ajouter_etat('start1', est_initial=True)
automate2.ajouter_etat('0')
automate2.ajouter_etat('1')
automate2.ajouter_etat('1', est_terminal=True)

# Ajout des transitions
automate2.ajouter_transition('start1', [], '0')
automate2.ajouter_transition('0', ['a'], '1')
automate2.ajouter_transition('1', ['b'], '1')

# Suppressions des images précédentes
if os.path.exists('union1.png'):
    os.remove('union1.png')
if os.path.exists('union2.png'):
    os.remove('union2.png')
if os.path.exists('union.png'):
    os.remove('union.png')


automate1.to_png('union1')
print('automate1')
display(Image('union1.png'))
automate2.to_png('union2')
print('automate2')
display(Image('union2.png'))

# Union des deux automates
print("\n\n")
print("Union des deux automates :\n")
automate = union(automate1, automate2)
print(automate)
automate.to_png('union')
print('\n Résultat de l\'union des deux automates :')
display(Image('union.png'))



