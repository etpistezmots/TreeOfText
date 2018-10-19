from skbio import DistanceMatrix
from skbio.tree import nj
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import linkage, dendrogram
import scipy.spatial.distance as ssd
from matplotlib import pyplot as plt

def Neigborjoin(Matrice):

    ids = list(Matrice)
    dm = DistanceMatrix(Matrice, ids)

    tree = nj(dm)
    print(tree.ascii_art())
    print('\n')

    newick_str = nj(dm, result_constructor=str)

    return newick_str


def Ward(Matrice):

    # recu des noms
    ids = list(Matrice)

    # Use distance Matrix in scypy
    #https://stackoverflow.com/questions/18952587/use-distance-matrix-in-scipy-cluster-hierarchy-linkage
    Matrice = ssd.squareform(Matrice.as_matrix())

    Z = linkage(Matrice,method="ward")

    # serait facile à afficher
    ''''
    fig = plt.figure(figsize=(25, 10))
    dn = dendrogram(Z)
    plt.show()'''

    # petite manip ci dessous pour obtenir format newick comme précedemment
    # permet d'utiliser ITOL pour la mise en page

    tree = hierarchy.to_tree(Z, False)

    newick_str = getNewick(tree, "", tree.dist, ids)
    return newick_str



def getNewick(node, newick, parentdist, leaf_names):
    if node.is_leaf():
        return "%s:%.3f%s" % (leaf_names[node.id], parentdist - node.dist, newick)
    else:
        if len(newick) > 0:
            newick = "):%.3f%s" % (parentdist - node.dist, newick)
        else:
            newick = ");"
        newick = getNewick(node.get_left(), newick, node.dist, leaf_names)
        newick = getNewick(node.get_right(), ",%s" % (newick), node.dist, leaf_names)
        newick = "(%s" % (newick)
        return newick


