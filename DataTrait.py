# -*- coding: utf-8 -*-
import pandas as pd


class MatriceCarre :
    """
    Pour stocker la matrice des distances
    """

    def __init__(self, listindex, dtype):
        self.Ori = pd.DataFrame(index=listindex, columns=listindex, dtype=dtype)
        self.Ori = self.Ori.fillna(0)  # with 0s rather than NaNs

    def Remplissage(self,col,ligne,value):
        self.Ori.at[col, ligne] = value
        self.Ori.at[ligne, col] = value



class DataReduce :
    """
    Sert à travailler plus spécifiquement sur deux colonnes : Col1 et Col2
    En faisant toutes les combinaisons de colonnes, on peut remplir la matrice des distances
    """

    def __init__(self, MatriceDepart, col1, col2):
        self.col1 = col1
        self.col2 = col2
        self.reduit = MatriceDepart[[col1,col2]]

    def RemoveRowAll0(self):
        self.reduit = self.reduit[(self.reduit.T != 0).any()]

    def CompareCol(self):
        '''
        Sert juste à definir la plus petite et plus grande colonne
        Pour la méthode de Labbe
        '''
        colmin = ""
        colmax = ""
        MarqueurEgalite = False

        TotalCol1 = self.reduit[self.col1].sum()
        TotalCol2 = self.reduit[self.col2].sum()

        if TotalCol1 < TotalCol2:
            colmin = self.col1
            colmax = self.col2
        if TotalCol2 < TotalCol1:
            colmin = self.col2
            colmax = self.col1
        if TotalCol1 == TotalCol2:
            MarqueurEgalite = True
        return colmin,colmax,MarqueurEgalite


    def PretraitLabe(self,colmin,colmax):
        '''
        Prétraitement seulement nécessaire à la méthode Labbé
        https://journals.openedition.org/corpus/31     
        '''

        # calcul pour chaque mot d'un produit en croix
        # comme si le plus gros corpus avait le nombre de mots du petit corpus.
        rapport = self.reduit[colmin].sum() / self.reduit[colmax].sum()
        self.reduit["E(labbe)"] = self.reduit[colmax] * rapport

        # enleve les termes pas présent dans texte plus court et dont E(i) < 1
        # attention le ~ inverse le True en False

        self.reduit = self.reduit[~(self.reduit[colmin] == 0 & (self.reduit["E(labbe)"] < 1))]

        return self.reduit


    ############# Petites fonctions spécifiques (voir distance.py) ###############

    def EnsembleVoc(self):
        return self.reduit.shape[0]

    def TermesEnCommun(self):
        ## https://stackoverflow.com/questions/26053849/counting-non-zero-values-in-each-column-of-a-dataframe-in-python
        CalculCommun = (self.reduit.astype(bool).ix[:,0] & self.reduit.astype(bool).ix[:,1]).sum(axis=0)
        return CalculCommun

    def TermeSpeA(self):
        # voir ref ci dessus
        return self.reduit.astype(bool).sum(axis=0)[0]

    def TermeSpeB(self):
        # voir ref ci dessus
        return self.reduit.astype(bool).sum(axis=0)[1]










