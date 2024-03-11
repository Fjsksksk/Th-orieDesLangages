from automate import *


# Création d'un automate avec un alphabet {'a', 'b', 'c','d'}
automate1 = Automate({'a', 'b', 'c','d'})

# Ajout des états avec indication des états initiaux et terminaux
automate1.ajouter_etat('1', est_initial=True)
automate1.ajouter_etat('2')
automate1.ajouter_etat('3', est_terminal=True)
automate1.ajouter_etat('4')

# Ajout des transitions
automate1.ajouter_transition('1', ['a'], '2')
automate1.ajouter_transition('2', ['b'], '3')
automate1.ajouter_transition('2', ['d', 'c'], '4')
automate1.ajouter_transition('4', ['a'], '3')
automate1.ajouter_transition('4', ['b'], '2')

# Affichage de l'automate
print("Automate 1:")
print(automate1)

# Affichage de l'automate en format dot
print("Automate 1 en format dot:")
print(automate1.to_dot())

# Conversion de l'automate en image
print("Conversion de l'automate 1 en image:")
automate1.to_png('automate1')

# Exportation de l'automate
print("Exportation de l'automate 1:")
exporter_automate(automate1, 'automate1.txt')

# Création automate2
print("Création de l'automate 2:")
print("Importation de l'automate 1:")
automate2 = importer_automate('automate1.txt')

# Modification de l'automate2
print("Modification de l'automate 2:")
automate2.ajouter_etat('5')
automate2.ajouter_transition('3', ['c'], '5')
automate2.ajouter_transition('5', ['d'], '4')

# Affichage de l'automate2
print("Automate 2:")
print(automate2)

# Affichage de l'automate2 en format dot
print("Automate 2 en format dot:")
print(automate2.to_dot())

# Conversion de l'automate2 en image
print("Conversion de l'automate 2 en image:")
automate2.to_png('automate2')

# Exportation de l'automate2
print("Exportation de l'automate 2:")
exporter_automate(automate2, 'automate2.txt')




