from automate import Automate

# Création d'un automate avec un alphabet {'a', 'b', 'c','d'}
automate = Automate({'a', 'b', 'c','d'})

# Ajout des états avec indication des états initiaux et terminaux
automate.ajouter_etat('1', est_initial=True)
automate.ajouter_etat('2')
automate.ajouter_etat('3', est_terminal=True)
automate.ajouter_etat('4')

# Ajout des transitions
automate.ajouter_transition('1', 'a', '2')
automate.ajouter_transition('2', 'b', '3')
automate.ajouter_transition('3', 'c','4')
automate.ajouter_transition('3', 'd','4')
automate.ajouter_transition('3', 'b', '3')

# Affichage de l'automate
print(automate)
print(automate.to_dot())
automate.to_png('automate_simple')