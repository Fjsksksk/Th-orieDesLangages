import sys
sys.path.append('../../')
from automate import Automate, concatenation

import os
from IPython.display import display, Image


#Suppression des images précédentes
if os.path.exists('conca1.png'):
    os.remove('conca1.png')
if os.path.exists('conca2.png'):
    os.remove('conca2.png')
if os.path.exists('conca.png'):
    os.remove('conca.png')

    
# Création de l'automate 1
automate1 = Automate({'a', 'b'})


automate1.ajouter_etat('0', initial=True)
automate1.ajouter_etat('1', terminal=True)
automate1.ajouter_etat('2', terminal=True)

# Ajout des transitions
automate1.ajouter_transition('0', ['a'], '1')
automate1.ajouter_transition('1', ['b'], '1')
automate1.ajouter_transition('0', ['b'], '2')

# Création de l'automate 2

automate2 = Automate({'a', 'b'})


automate2.ajouter_etat('0', initial=True)
automate2.ajouter_etat('1', initial=True)
automate2.ajouter_etat('2', terminal=True)

# Ajout des transitions
automate2.ajouter_transition('0', ['a'], '2')
automate2.ajouter_transition('1', ['b'], '2')




print('Automate 1:')
automate1.to_png('conca1')
display(Image('conca1.png'))

print('Automate 2:')
automate2.to_png('conca2')
display(Image('conca2.png'))

print("\n\n")

# Concatenation des deux automates
print("Concatenation des deux automates :\n")
automate = concatenation(automate1, automate2)
print(automate)
automate.to_png('conca')
display(Image('conca.png'))



