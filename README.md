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

## Rapport du projet

Le rapport est réalisé avec Jupiter Notebook. Il est disponible dans le dossier `rapport`.
Pour avoir l'affichage des automates au sein du rapport, nous avons utilisé la bibliothèque `IPython` en particulier la fonction `display` et la fonction `Image`. 

```python

from IPython.display import display, Image

# Pour afficher un automate (exemple)
display(Image(filename='automate.png'))

```

Si nous éxécutons le code ci-dessus dans un notebook, nous aurons l'affichage de l'automate. Par contre, si nous exécutons le code dans un fichier python, nous n'aurons pas l'affichage de l'automate mais la ligne suivante dans la console : 

```bash
<IPython.core.display.Image object>
```

## Les différents fichiers/dossiers

- `automate.py` : contient la classe `Automate` qui permet de modéliser un automate. Cette contient les méthode permettant de travailler sur un automate. 
- `etat.py` : contient la classe `Etat` qui permet de modéliser un état.
- `transition.py` : contient la classe `Transition` qui permet de modéliser une transition.
- Le dossier `partie1` contient les fichiers suivants :
    - `modelisation.py` : contient les pour la modélisation d'un automate. Mais aussi l'importation et l'exportation d'un automate.
- Le dossier `partie2` contient les fichiers suivants :
    - Dossier `Union` : contient les fichiers de test pour l'union de deux automates.
    - Dossier `Concatenation` : contient les fichiers de test pour la concaténation de deux automates.
    - Dossier `Repetition` : contient les fichiers de test pour la répétition d'un automate.
## Les différentes classes

### Classe `Etat`

La classe `Etat` permet de modéliser un état. Elle a les attributs suivants :
- `nom` : un nom d'état
- `initial` : un booléen indiquant si l'état est initial
- `terminal` : un booléen indiquant si l'état est terminal

### Classe `Transition`

La classe `Transition` permet de modéliser une transition. Elle a les attributs suivants :
- `depart` : l'état de départ de la transition
- `symbole` : le ou les symbole(s) de la transition
- `arrivee` : l'état d'arrivée de la transition

### Classe `Automate`

La classe `Automate` permet de modéliser un automate. Elle a les attributs suivants :
-  `etats` : une liste d'états (instances de la classe `Etat`)
- `alphabet` : un ensemble de symboles
- `transitions` : une liste de transitions (instances de la classe `Transition`)

## Partie 1 : Modélisation d'un automate

### 1.1. Modélisation d'un automate

Pour modéliser un automate, nous utilisons la classe `Automate`, la classe `Etat` et la classe `Transition` (déjà présenté ci-dessus).

1. Initialisation de l'automate : on crée une instance de la classe `Automate` et on y ajoute l'alphabet de l'automate lors de l'initialisation. 
```python
alphabet={'a', 'b', 'c'}	
automate = Automate(alphabet)
```
2. Ajout d'états : on crée des instances de la classe `Etat` et on les ajoute à l'automate. Les paramètres de la classe `Etat` sont le nom de l'état, un booléen indiquant si l'état est terminal et un booléen indiquant si l'état est initial. 
```python
automate.ajouter_etat(Etat('q0', True, False))
```	
3. Ajout de transitions : on crée des instances de la classe `Transition` et on les ajoute à l'automate. Les paramètres de la classe `Transition` sont l'état de départ, le ou les symbole(s) de la transition et l'état d'arrivée. 
```python
automate.ajouter_transition(Transition('q0', 'a', 'q1'))
```

Notre automate est maintenant créé. Mais nous ne pouvons pas encore l'afficher. 

### 1.2. Affichage de l'automate

Pour obtenir une image, nous allons convertir notre automate en dot et ensuite en png. Nous utilisons la bibliothèque `graphviz`. 

```python
# Convertir l'automate en dot
automate.to_dot()

# Convertir le fichier dot en png
automate.to_png("automate")
```
La méthode `to_dot` retourne une chaîne de caractères représentant l'automate au format dot. La méthode `to_png` crée un fichier png représentant l'automate.

On n'est pas obligé de passer par la méthode `to_dot` pour afficher l'automate. On peut directement passer par la méthode `to_png` qui va appeler la méthode `to_dot` pour nous. 

Pour afficher l'automate, nous utilisons la fonction `display` de la bibliothèque `IPython`. 

Pour voir le résultat, il suffit d'ouvir le fichier `automate.png` qui a été créé.


### 1.3 Importation / Export d'un automate

- `export` : est une fonction qui permet d'exporter un Automate et prend en paramètre l'automate à exporter (self) et le nom du fichier. 
La fonction crée un fichier avec le nom donné si celui n'existe pas. Sinon elle modifie le fichier. 
La structure du fichier d'exportation est la suivante : 
    - Ligne 1 : Alphabet de l'automate
    - Ligne 2 : États de l'automate
    - Ligne 3 : États initiaux 
    - Ligne 4 : États terminaux
    - A partir de la ligne 5, nous retrouvons les transition avec la structure suivante : `état départ` `symbols` `état fin`

- `importation` : est une fonction qui permet d'importer un automate depuis un fichier texte et prend en paramètre le nom du fichier texte. 
La fonction rempli d'abord les variables qui vont nous permettre de créer l'automate. Pour cela elle suit la logique expliqué précédement. 
Une fois cela effectué, elle crée un nouvel automate qu'elle retourne. 

La paricularité de la fonction 'importation' est qu'elle est défini en dehors de la classe `Automate`. 

**Exemple d'utilisation**

```python
# Exporter un automate
automate.export("automate.txt")

# Importer un automate
automate = importation("automate.txt")
```


### 1.4 Exemple d'automate

Voici un exemple de modélisation d'un automate. Le code de cette exemple est disponible dans le fichier `partie1/modelisation.py`. 



## Les problèmes rencontrés

### Problème 1 : Le choix de la structure de données

Nous avons commencé le projet en utilisant la structure de données suivante ; 
- Une classe `Automate` qui contenait les éléments suivant 
    - une liste pour l'alphabet
    - un set pour les états
    - un set pour les états initiaux
    - un set pour les états terminaux
    - un dictionnaire pour les transitions

Au début (partie 1 et 2), nous avons réussi à nous en sortir, mais nous avons rencontré des problèmes lors de la déterminisation de l'automate. Après avoir cherché des solutions pour résoudre le problème. N'en trouvant pas, nous avons décidé de changer de structure de données en utilisant trois classes différentes : `Automate`, `Etat` et `Transition`.