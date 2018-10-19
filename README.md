# Tree of Text

###### Visualisation d'arbre à la mode "HyperBase" (logiciel d'analyse textuelle)
###### Connection à "Interface Tree of Life" : interface Web pour mettre en page ces arbres.

## Presentation

Hyperbase permet de visualiser des distances entre des textes
ou des regroupements de textes sous forme d'arbre.
C'est ici exactement la même chose en partant d'un résultat type Document-Term-Matrix.
En effet, le chargement des textes dans Hyperbase peut être un peu lourd.

HyperBaseWeb permet de charger beaucoup plus facilemet des textes
mais pour l'instant, l'interface ne réalise des arbres qu'avec la distance
de Jaccard classique et avec la méthode de Ward pour les regroupements

Ici, possibilité de choisir pour le calcul de la distance :
   - Labbe, Jaccard, JaccardBrunet
et pour les méthodes de regroupements :
   - Ward, neighborjoining (très proche de la méthode utilisée par HyperBase)

Le code permet de rajouter facilement d'autres méthodes si nécessaire

La sortie obtenue est de type Newick
L'idée est de copier-coller directement cette sortie dans ITOL : https://itol.embl.de/
pour mettre en page les résultats (Onglet Upload --> copier la sortie dans la fenêtre "Tree text
--> Upload)

Il y a un module (ConnectItol) qui permet de faire la connexion directement
en decommentant la fin du code de main.py.
Toutefois, il vous faut pour cela utiliser firefox, selenium.
Il faudra aussi télécharger le module "geckodriver" et préciser le chemin d'entrée dans le module.
De plus, le code est assez dépendant de la structure de la page Web qui par définition peut changer.
Donc autant dire que pour une utilisation ponctuelle, vous avez plus vite fait de faire à la main
l'ouverture du site et le copier-coller du dernier résultat obtenu dans votre console

## Utilisation

Quelques librairies python sont nécessaires :
scipy, skbio, pandas, itertools, (selenium, tkinter pour le lien automatique avec itol)

Il faut préciser les trois variables au début de main.py.

Suivant vos données de départ,
il vous faudra surement un peu adapter data.py (methode PretraitFormatDefault)

## Remerciements

Laurent Vanni et Dominique Labbe

## Auteur

Max Beligné







