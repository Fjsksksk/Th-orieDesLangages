# TheorieDesLangages

## Introduction


## Les différents fichiers

- `automate.py` : contient la classe `Automate` qui permet de modéliser un automate. Cette contient les méthode permettant de travailler sur un automate.
- `partie1.py` : contient les tests de la classe `Automate` et les tests des méthodes de la classe `Automate` pour la partie 1 du projet.


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

- `to_dot` : une méthode de la classe `Automate` qui retourne une chaîne de caractères représentant l'automate au format dot
- `to_png` : une méthode de la classe `Automate` qui crée un fichier png représentant l'automate

### 1.3 Importation / Export d'un automate

Les méthodes d'importation et d'export sont défini en dehors de la classe `Automate`.

- `exporter_automate` : est une fonction qui permet d'exporter un Automate et prend en paramètre l'automate à exporter et le nom du fichier. 
La fonction crée un fichier avec le nom donné si celui n'existe pas. Sinon elle modifie le fichier. 
La structure du fichier d'exportation est la suivante : 
    - Ligne 1 : Alphabet de l'automate
    - Ligne 2 : États de l'automate
    - Ligne 3 : États initiaux 
    - Ligne 4 : États terminaux
    - A partir de la ligne 5, nous retrouvons les transition avec la structure suivante : `état départ` `symbols` `état fin`

- `importer_automate` : est une fonction qui permet d'importer un automate depuis un fichier texte et prend en paramètre le nom du fichier texte. 
La fonction rempli d'abord les variables qui vont nous permettre de créer l'automate. Pour cela elle suit la logique expliqué précédement. 
Une fois cela effectué, elle crée un nouvel automate qu'elle retourne. 

## Partie 2 : 

### 2.1. Union de deux automates

La méthode `union` du fichier `automate.py` permet de réaliser l'union de deux automates.

**Alphabet** : L'alphabet de l'automate résultant est l'union des alphabets des deux automates plus un symbole supplémentaire, `une chaine vide`. Celui-ci permettra de réaliser des transitions vide.

**États** : 
- Dans un premier temps, nous procédons à un renommage des états des deux automates pour éviter les conflits.
- Ensuite, nous ajoutons un nouvel état initial et un état pour distribuer l'état initial aux anciens états initiaux des deux automates.

**Transitions et Etat Terminaux** :
- Nous ajoutons les transitions et les états terminaux des deux automates à l'automate résultant.
- Ajout de la transition vide entre le nouvel état initial et le nouvel état de distribution de l'état initial.
- Ajout de la transition vide entre les anciens état initiaux des deux automates et l'état temporaire

**Problème** : Nous avons un problème sur le fait que l'on pouvait ajouter une seul destination via notre méthode `ajouter_transition`. Or avec notre méthode `union` nous avons besoin de pouvoir ajouter plusieurs destinations. Lors de l'éxécution de la méthode `union` l'ajout se réalise correctement mais en écrasant l'ancien ajout. 

Pour cela, nous avons modifié la méthode `ajouter_transition` pour qu'elle puisse ajouter plusieurs destinations. 
Maintenant, nous avons le résultat attendu.

