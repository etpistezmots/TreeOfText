# -*- coding: utf-8 -*-

def Labbe(MatEntree,col1,col2):
    '''
    Complute la distance entre deux colonnes selon méthode Labbé
    http://images.math.cnrs.fr/La-classification-des-textes.html
    '''

    # calcul intermédiaire de valeur absolue de F(A) - E(A)
    MatEntree["distanceint"] = abs(MatEntree[col1] - MatEntree[col2])

    # calcul de la distance
    distance = MatEntree["distanceint"].sum() / (MatEntree[col2].sum() + MatEntree[col1].sum())

    return distance


def JaccardBrunet(MatEntree):
    '''
    Idem : amélioration méthode Jaccard par Brunet
    https://journals.openedition.org/corpus/30
    '''
    # https://journals.openedition.org/corpus/30
    # https://stackoverflow.com/questions/26053849/counting-non-zero-values-in-each-column-of-a-dataframe-in-python

    # ens voc A : dans la matrice, combien de ligne !=0 en A
    A = MatEntree.TermeSpeA()
    # ens voc B : dans la matrice, combien de ligne !=0 en B
    B = MatEntree.TermeSpeB()
    # ens commun :dans la matrice, combien de ligne !=0 en A et en B
    AB = MatEntree.TermesEnCommun()

    distance = ((A-AB)/A) + ((B-AB)/B)

    return distance


def Jaccard(MatEntree):
    '''
    https://fr.wikipedia.org/wiki/Indice_et_distance_de_Jaccard
    '''
    # ens voc : dans la matrice (les lignes qu'avec des O ont été préalablement enlevé)
    V = MatEntree.EnsembleVoc()
    # ens commun :dans la matrice, combien de ligne !=0 en A et en B
    AB = MatEntree.TermesEnCommun()

    distance = 1- (AB / V)

    return distance


