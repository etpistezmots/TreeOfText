# Tree of Text

###### Visualisation d'arbre à la mode "HyperBase" (logiciel d'analyse textuelle)
###### Connection à ITOL (Interface Tree of Life) pour mettre en page ces arbres.

## Presentation

Hyperbase permet de visualiser des distances entre des textes
ou des regroupements de textes sous forme d'arbre.
C'est ici exactement la même chose en partant d'un résultat type Document-Term-Matrix.
En effet, le chargement des textes dans Hyperbase peut être un peu lourd.

HyperBaseWeb permet de charger beaucoup plus facilement des textes
mais pour l'instant, l'interface ne réalise des arbres qu'avec la distance
de Jaccard classique et avec la méthode de Ward pour les regroupements

Ici, possibilité de choisir pour le calcul de la distance :
   - Labbe, Jaccard, JaccardBrunet
  
et pour les méthodes de regroupements :
   - Ward, UGPMA, neighborjoining (très proche de la méthode utilisée par HyperBase)

Le code permet de rajouter facilement d'autres méthodes si nécessaire

Deux prévisualisations sont possibles : sous forme de phylogramme (classique) ou sous forme circulaire

Il peut avoir des chevauchements dans la prévisualisation (surtout sous la forme circulaire)
mais cela donne une première idée du résultat obtenu.

Si les résultats sont intéressants, le programme propose une exportation
sous ITOL (http://itol.embl.de/) pour mettre en forme les graphs.

## Utilisation

ATTENTION : Le programme a été testé sous Ubuntu avec Firefox.
En cas d'autre navigateur, il faudra au moins changer la fin de WriteScriptJs.
Si vous utlisez ubuntu et firefox, il vous faudra télécharger geckodriver :
https://github.com/mozilla/geckodriver/releases
et après décompression, le placer dans votre dossier TreeOfText

Si vous ne voulez pas vous embeter avec selenium, geckodriver
commenter les lignes 89,91,94 à 96
et faites les exports à la main si nécessaire dans ITOL

Quelques librairies python sont nécessaires :
wx, scipy, skbio, pandas, itertools, selenium (si export automatique vers itol)

Les données en entrée sont sous la forme d'un tableau lexical en csv:
- en ligne : les termes
- en colonnes : les docs ou ensembles de docs
(vois ex dans dossier Data, ici mes ensembles de docs sont des Epoque X Revue.
A étant une revue et E étant une autre revue)

Si le module d'export "OnItol" ne marche pas,
vous pouvez faire le copier-coller du resultat Newick
par vous-même en ouvrant ITOL à la main.


## Remerciements

Laurent Vanni, Dominique Labbe et Ken-ichi Ueda (http://bl.ocks.org/kueda/1036776)

## Auteur

Max Beligné







