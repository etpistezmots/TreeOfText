from data import DataOri, MatriceCarre, DataReduce
from distance import Labbe, Jaccard, JaccardBrunet
from regroupement import Neigborjoin, Ward
from ConnectItol import InterfaceMinimale, VersItol
import itertools
import pandas as pd



# Chemin des données par default
DefaultPath = __file__[0:len(__file__)-7] +"Data/tableafcm.csv"


########### VARIABLES A PRECISER  #######################

# Localisation des données
PathData = DefaultPath

# Choix du calcul de la distance
    # Labbe, JaccardBrunet ou Jaccard:
ChoixDist = "Jaccard"

# Choix de la méthode de regroupement
    # Neigborjoin ou Ward
ChoixRegroup = "Ward"


##################  PROGRAMME ############################

# Import des données et prétraitement
# A adapter suivant la situtation (voir data Classe DataOri
# --> créer votre méthode de Prétaitement adaptée à vos données
# Appelez là à la place de PretraitFormatDefault()
# Le "print" juste après vous permet de vérifier

DataBrut = DataOri(PathData)
DataNet = DataBrut.PretraitFormatDefault()

print("La tête de votre matrice ressemble à ça en entrée :")
print(DataNet.head())

# Création d'une matrice carrée vide qui va stocker résultat
# ligne et colonne correspondent aux noms des colonnes de la matrice précédente
# definition du format de travail : 4 chiffres après la virgule

column = list(DataNet)
StockResult = MatriceCarre(column,"float")
pd.options.display.float_format = '${:,.4f}'.format

# itère sur toutes les combinaisons de 2 noms de colonne
# A chaque fois, on va calculer la distance entre ces deux colonnes

for x in itertools.combinations(column, 2):

    print("Travail sur la combinaison :")
    print(x)

    # réduction de mon tableau à ces éléments
    Reduction = DataReduce(DataNet,x[0],x[1])
    # enlève les lignes avec que des 0
    Reduction.RemoveRowAll0()



    ################ DIFFERENTS CALCUL DE DISTANCE ###################

    if ChoixDist == "Labbe":

        # Comparaison des différentes colonnes
        colmin, colmax, MarqueurEgalite = Reduction.CompareCol()
        print("la plus petite colonne est : " + colmin)

        if MarqueurEgalite:

            # exceptionnelement pas besoin de prétraitement
            # bon dans ce cas, les attributs colmin et colmax sont mal choisis
            # car TotalCol1 = TotalCol2 (voir Data.DataReduce Compare Col)
            DistLabbe = Labbe(Reduction, colmin, colmax)
            print("La distance " + ChoixDist + " calculée est " + str(DistLabbe) + '\n')

            # Remplissage de la matrice carre
            StockResult.Remplissage(x[0], x[1], DistLabbe)

        else:
            # Dans ce cas qui est la cas général (très rare que TotalCol1 == TotalCol2)
            # prétraitement pour rendre taille comparable
            ReduitTransform = Reduction.PretraitLabe(colmin, colmax)

            DistLabbe = Labbe(ReduitTransform,colmin,"E(labbe)")
            print("La distance " + ChoixDist + " calculée est " + str(DistLabbe) + '\n')

            # Remplissage de la matrice carre
            StockResult.Remplissage(x[0], x[1], DistLabbe)

    if ChoixDist == "JaccardBrunet":

        DistJaccardBrunet = JaccardBrunet(Reduction)
        print("La distance " + ChoixDist + " calculée est " + str(DistJaccardBrunet) + '\n')
        StockResult.Remplissage(x[0], x[1], DistJaccardBrunet)


    # serait plus simple d'utiliser directement scipy sur le tableau général
    # mais permet de comprendre comment est calculé
    # notamment différence avec JaccardBrunet (voir distance.py)
    if ChoixDist == "Jaccard":
        DistJaccard = Jaccard(Reduction)
        print("La distance " + ChoixDist + " calculée est " + str(DistJaccard) + '\n')
        StockResult.Remplissage(x[0], x[1], DistJaccard)


# Matrice de fin
ResultMatriceFin = StockResult.Ori
print("VOTRE MATRICE DE DISTANCE EST :")
print(ResultMatriceFin)
print('\n')


################ DIFFERENTS REGROUPEMENTS ###################

resultfin= ""

if ChoixRegroup=="Neigborjoin":
    resultfin =Neigborjoin(ResultMatriceFin)
    print("VOTRE RESULTAT AU FORMAT NEWICK EST :")
    print(resultfin)

if ChoixRegroup=="Ward":
    resultfin = Ward(ResultMatriceFin)
    print("VOTRE RESULTAT AU FORMAT NEWICK EST :")
    print(resultfin)



############ CONNEXION AUTO à ITOL #########################

'''
pathgecko = "/home/max/Téléchargements/geckodriver"

Encours = VersItol(resultfin,pathgecko)
# Fin propre
InterfaceMinimale()
Encours.quit()
print("Au revoir")
'''


