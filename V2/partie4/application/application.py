import sys
sys.path.append('../../')
from automate import Automate
import os
from IPython.display import Image, display


if os.path.exists("catho.png"):
    os.remove("catho.png")

#Liste contenant l'alphabet de a à z
alphabet = [chr(i) for i in range(97, 123)]

# Liste contenant les numéros de 1 à 9
chiffres = [str(i) for i in range(1, 10)]

symbole = ['.', '-','@']

alphabet_global = alphabet + chiffres + symbole

# Création de l'automate
catho = Automate(alphabet_global)

catho.ajouter_etat("prenom", initial=True)
catho.ajouter_etat("nom")
catho.ajouter_etat("numero")


for i in range(1, 17):
    catho.ajouter_etat(str(i))
    if i == 16:
        catho.ajouter_etat(str(i), terminal=True)


#Ajout des transitions
transitions1 = alphabet 
transitions1.append("-")
catho.ajouter_transition("prenom", transitions1, "prenom")
catho.ajouter_transition("prenom", ".", "nom")
catho.ajouter_transition("nom", transitions1, "nom")
catho.ajouter_transition("nom", chiffres, "numero")
catho.ajouter_transition("numero", chiffres, "numero")
catho.ajouter_transition("numero", "@", "1")
catho.ajouter_transition("nom", "@", "1")

#Ajout pour lacatholille.fr
phrases = "lacatholille.fr"
for i in range(1, 16):
    catho.ajouter_transition(str(i), phrases[i-1], str(i+1))


catho.to_png("catho")

print("Automate de l'adresse mail de la catho")
display(Image("catho.png"))

print("\n\n")

verif1="clement.szewczyk@lacatholille.fr"
print("Mot à vérifier : ", verif1)
print(catho.accepte_mot(verif1))

verif2="pierre-jean.toto@lacatholille.fr"
print("Mot à vérifier : ", verif2)
print(catho.accepte_mot(verif2))

verif3="toto.titi2@lacatholille.fr"
print("Mot à vérifier : ", verif3)
print(catho.accepte_mot(verif3))

verif4="carlos-emanuelle@lacatholille.fr"
print("Mot à vérifier : ", verif4)
print(catho.accepte_mot(verif4))