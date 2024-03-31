import sys
sys.path.append('../')
from automate import Automate, importation
from IPython.display import Image, display
import os

# Suppression des images précédentes
if os.path.exists('Modelisation1.png'):
    os.remove('Modelisation1.png')
if os.path.exists('modelisation2.png'):
    os.remove('modelisation2.png')
if os.path.exists('modelisation1.txt'):
    os.remove('modelisation1.txt')

automat1 = Automate(['a', 'b', 'c', 'd'])

automat1.ajouter_etat('1', initial=True)
automat1.ajouter_etat('2')
automat1.ajouter_etat('3', terminal=True)
automat1.ajouter_etat('4')

automat1.ajouter_transition('1', ['a','b'], '2')
automat1.ajouter_transition('2', 'b', '3')
automat1.ajouter_transition('3', 'c', '4')
automat1.ajouter_transition('4', 'd', '1')

print("Automate 1\n")

print(automat1)

print("Automate 1 au format dot\n")

print(automat1.to_dot())
print("Automate 1 au format png\n")
automat1.to_png('Modelisation1')
display(Image(filename='Modelisation1.png'))
print("Automate 1 exporté dans modelisation1.txt\n")
automat1.export('modelisation1.txt')

print(" \n\n")
print("Automate 2 importé depuis modelisation1.txt\n")
automat2 = importation('modelisation1.txt')
print("Automate 2\n")
print(automat2)
print("Automate 2 au format png\n")
automat2.to_png('modelisation2')
display(Image(filename='modelisation2.png'))

