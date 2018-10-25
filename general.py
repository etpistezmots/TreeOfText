# -*- coding: utf-8 -*-

import wx
import os
from DataTrait import MatriceCarre, DataReduce
from distance import Labbe, Jaccard, JaccardBrunet
from regroupement import Neigborjoin, Ward, Ugpma
import itertools
import pandas as pd


############ FONCTIONS POUR CHOISIR FICHIER DE TRAVAIL  ##############

def WorkFile(parent):

    ShowMessage("Pour info !",
                "DTM au format CSV \n")

    # Va ouvrir une boite de dialogue permettant de choisir le fichier
    parent.PathData = ChooseWorkFile(parent)

    # affiche le nouveau fichier
    parent.custum1.SetLabel(parent.PathData)



def ChooseWorkFile(parent):
    dlg = wx.FileDialog(parent, "Choix du fichier")
    file = ""
    if dlg.ShowModal() == wx.ID_OK:
        file = dlg.GetPath()
    dlg.Destroy()
    return file

def ShowMessage(titre, txt):
    wx.MessageBox(txt, titre,
                  wx.OK | wx.ICON_INFORMATION)



##################  PROGRAMME ############################


def Start(parent):

    # Import des données

    Data = pd.read_csv(parent.PathData, sep=";", index_col=[0])

    print("La tête de votre matrice ressemble à ça en entrée :")
    print(Data.head())

    # Création d'une matrice carrée vide qui va stocker résultat
    # ligne et colonne correspondent aux noms des colonnes de la matrice précédente
    # definition du format de travail : 4 chiffres après la virgule

    column = list(Data)
    StockResult = MatriceCarre(column,"float")
    pd.options.display.float_format = '${:,.4f}'.format

    # itère sur toutes les combinaisons de 2 noms de colonne
    # A chaque fois, on va calculer la distance entre ces deux colonnes

    for x in itertools.combinations(column, 2):

        print("Travail sur la combinaison :")
        print(x)

        # réduction de mon tableau à ces éléments
        Reduction = DataReduce(Data,x[0],x[1])
        # enlève les lignes avec que des 0
        Reduction.RemoveRowAll0()



        ################ DIFFERENTS CALCUL DE DISTANCE ###################

        if parent.ChoixDist == "Labbe":

            # Comparaison des différentes colonnes
            colmin, colmax, MarqueurEgalite = Reduction.CompareCol()
            print("la plus petite colonne est : " + colmin)

            if MarqueurEgalite:

                # exceptionnelement pas besoin de prétraitement
                # bon dans ce cas, les attributs colmin et colmax sont mal choisis
                # car TotalCol1 = TotalCol2 (voir Data.DataReduce Compare Col)
                DistLabbe = Labbe(Reduction, colmin, colmax)
                print("La distance " + parent.ChoixDist + " calculée est " + str(DistLabbe) + '\n')

                # Remplissage de la matrice carre
                StockResult.Remplissage(x[0], x[1], DistLabbe)

            else:
                # Dans ce cas qui est la cas général (très rare que TotalCol1 == TotalCol2)
                # prétraitement pour rendre taille comparable
                ReduitTransform = Reduction.PretraitLabe(colmin, colmax)

                DistLabbe = Labbe(ReduitTransform,colmin,"E(labbe)")
                print("La distance " + parent.ChoixDist + " calculée est " + str(DistLabbe) + '\n')

                # Remplissage de la matrice carre
                StockResult.Remplissage(x[0], x[1], DistLabbe)



        if parent.ChoixDist == "JaccardBrunet":

            DistJaccardBrunet = JaccardBrunet(Reduction)
            print("La distance " + parent.ChoixDist + " calculée est " + str(DistJaccardBrunet) + '\n')
            StockResult.Remplissage(x[0], x[1], DistJaccardBrunet)



        # serait plus simple d'utiliser directement scipy sur le tableau général
        # mais permet de comprendre comment est calculé
        # notamment différence avec JaccardBrunet (voir distance.py)
        if parent.ChoixDist == "Jaccard":
            DistJaccard = Jaccard(Reduction)
            print("La distance " + parent.ChoixDist + " calculée est " + str(DistJaccard) + '\n')
            StockResult.Remplissage(x[0], x[1], DistJaccard)


    # Matrice de fin
    ResultMatriceFin = StockResult.Ori
    print("VOTRE MATRICE DE DISTANCE EST :")
    print(ResultMatriceFin)
    print('\n')


    ################ DIFFERENTS REGROUPEMENTS ###################

    resultfin= ""

    if parent.ChoixRegroup =="Neigborjoin":
        resultfin = Neigborjoin(ResultMatriceFin)
        print("VOTRE RESULTAT AU FORMAT NEWICK EST :")
        print(resultfin)
        parent.ResultInterface.Clear()
        parent.ResultInterface.WriteText(resultfin)
        parent.Result = resultfin

    if parent.ChoixRegroup =="Ward":
        resultfin = Ward(ResultMatriceFin)
        print("VOTRE RESULTAT AU FORMAT NEWICK EST :")
        print(resultfin)
        parent.ResultInterface.Clear()
        parent.ResultInterface.WriteText(resultfin)
        parent.Result = resultfin

    if parent.ChoixRegroup =="Ugpma":
        resultfin = Ugpma(ResultMatriceFin)
        print("VOTRE RESULTAT AU FORMAT NEWICK EST :")
        print(resultfin)
        parent.ResultInterface.Clear()
        parent.ResultInterface.WriteText(resultfin)
        parent.Result = resultfin


