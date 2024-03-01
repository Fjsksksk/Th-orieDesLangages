# TheorieDesLangages
Projet 2024 S2

 Partie1 : Modélisation d’un automate | fonctionnelle mais manque l'option avec plusieurs lettres (4 --(d,c)--> 3)

fonction ajouter transition multi :
    - Reconnait bien quand il y a deux symbole 
    ```
    automate.ajouter_transition_multi('3', 'ba', '3')
    3 --(b)--> ['3']
    3 --(a)--> ['3']
    ```
    - Il faut faire en sorte qui li les deux

 La fonction ajouter transition multi n'est pas encore compatible avec la conversion en dot
