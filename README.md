# Projet Théorie des langages

## Introduction
Le projet a lieu dans le cadre du cours de théories des langages réalisé au Semestre 2 de la deuixème année de Licence Sciences du Numérique. 
Il a été réalisé par Candice Giami et Clément Szewczyk. 

L'objectif du projet est d'implémenter une bibliotèque de fonction sur les automates en **python**. 

Les étapes du projet : 
- modélisation d’un automate.
- de charger la description d’un automate sous forme d’un fichier texte (texte brut, json, xml…) dont vous définirez
le format
- de sauvegarder la description d’un automate sous forme d’un fichier texte dont le format respecte celui en lecture
- d’afficher l’automate à l’écran ou de générer un fichier image.
- Réaliser des opérations élémentaires sur les automates (union, concaténation et répétition)
- Synchroniser un automate (suppression des 𝜖-transitions) **(BONUS)**
- Construire un automate à partir d’une expression régulière **(BONUS)**
- Compléter/Déterminiser/Minimiser un automate
- Reconnaitre une adresse mail à l’aide d’un automate

Les étapes sont découpé en 4 parties :
1. Modélisation d'un automate
2. Opérations sur les automates
3. Expressions régulières verd Automates (Bonus)
4. Finalisation



## Les différents fichiers

- `automate.py` : contient la classe `Automate` qui permet de modéliser un automate. Cette contient les méthode permettant de travailler sur un automate. Il contient également les méthodes permettant de réaliser des opérations sur les automates (union, concaténation, répétition) ainsi que l'exportation et l'importation d'un automate.
- `partie1.py` : contient les tests de la classe `Automate` et les tests des méthodes de la classe `Automate` pour la partie 1 du projet.`
- `union/union.py`: contient le fichier de test pour la méthode `union` du fichier `Automate`
- `concatenation/concatenation.py`: contient le fichier de test pour la méthode `concatenation` du fichier `Automate`
- `partie_4/determinisation/determinisation.py`: contient le fichier de test pour la méthode `determinisation` du fichier `Automate`



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

### 1.4 Exemple d'automate


## Partie 2 : Opérations sur les automates

### 2.1. Union de deux automates

#### 2.1.1 Méthode 'union'
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
#### 2.1.2 Exemple d'utilisation

### 2.2 Concaténation de deux automates. 

#### 2.2.1

La méthode `concatenation` du fichier `automate.py` permet de réaliser la concaténation de deux automates. 

**Alphabet** : L'alphabet de l'automate résultant est l'union des alphabets des deux automates plus un symbole supplémentaire, `une chaine vide`. Celui-ci permettra de réaliser des transitions vide.

**Etats** :
- Dans un premier temps, nous procédons à un renommage des états des deux automates pour éviter les conflits.
- Ensuite, nous ajoutons un nouvel état initial et un état pour distribuer l'état initial aux anciens états initiaux des deux automates.

**Transitions et Etat Terminaux** :
- Nous ajoutons les transitions et les états terminaux des deux automates à l'automate de la concaténation.
- Ajout de la transition vide entre les anciens état terminaux de l'automate 1 et l'état temporaire. 
- Ajout de la transition vide entre l'état temporaire et les anciens états initiaux de l'automate 2.

### 2.3 Répétion d'un automate 

#### 2.3.1 Méthode `repetition`

#### 2.3.2 Exemple d'utilisation


## Partie 4 : Finalisation

### 4.1 Compléter un automate

### 4.2 Déterminisation d'un automate

- Fonction `est_déterministe` de la classe `Àutomate` permet de savoir si un automate est déterministe. Si oui, elle retourne `True`, sinon, elle retourne `False`

**Algorithme de déterminisation** :
1. Création d'un automate vide
2. Création de l'état initial de l'automate déterministe
    - L'état initial de l'automate déterministe est l'ensemble des états atteignables à partir de l'état initial de l'automate non déterministe
3. Création de la table de transition

    - structure de la table de transition : 
        - clé : état de l'automate non déterministe
        - n colonnes : symboles de l'alphabet
    - 1ère ligne : état initial de l'automate non déterministe
    - 2eme et n lignes : états de l'automate non déterministe provenant de la table de transition

4. Interprétation de la table de transition

    - Pour chaque état de la table de transition, on crée un état dans l'automate déterministe

5. Création des états terminaux de l'automate déterministe

    - Un état de l'automate déterministe est terminal si au moins un des états de l'automate non déterministe qu'il représente est terminal

```python
# Regarde les différente transitions de l'état
                for etat in etats_a_explorer[0]:
                    # pour chaque état regarde les symboles associé a des transition
                    for symboles, destinations in self.transitions.get(etat, {}).items():
                        # regarde les symboles 
                        for symbole in symboles:
                            # regarde les destinations
                            for destination in destinations:
                                if symbole not in transitions:
                                    transitions[symbole] = set()
                                transitions[symbole].add(destination)
                                etats_a_explorer.append(destination)
```
    


