# TheorieDesLangages

## Introduction



## Partie 1 : Modélisation d'un automate


### 1.1. Modélisation d'un automate

Création d'une classe `Automate` qui permet de modéliser un automate. La classe a les attributs suivants :
- `etats` : un ensemble d'états
- `alphabet` : un ensemble de symboles
- `transitions` : un dictionnaire dont les clés sont des couples (état, symbole) et les valeurs sont des ensembles d'états
- `etat_initiaux` : un ensemble d'états
- `etats_finaux` : un ensemble d'états

La classe a les méthodes suivantes :

- `_init_` : le constructeur qui initialise les attributs de la classe
- `ajouter_etat` : une méthode qui ajoute un état à l'automate
- `ajouter_transition` : une méthode qui ajoute une transition à l'automate
-  `destination_transition` : une méthode qui retourne l'ensemble des états atteignables à partir d'un état donné avec un symbole donné
- `__str__` : une méthode qui retourne une chaîne de caractères représentant l'automate


### 1.2. Génération fichier dot et png

- `to_dot` : une méthode qui retourne une chaîne de caractères représentant l'automate au format dot
- `to_png` : une méthode qui crée un fichier png représentant l'automate

