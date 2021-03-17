from math import sqrt

class Iris:
    def __init__(self, longueur, largeur, espece):
        self.petal_length = longueur
        self.petal_width = largeur
        self.spece = espece

#agregat permettant acces var de n'importe quel fichier
class IrisData:
    iris_infos = []
    iris_type = []

def ChargeFichierIris():
    with open("iris.csv", mode='r') as f:
        f.readline()
        IrisData.iris_type = [x.strip("\n") for x in f.readline().split(',')]

        for i in f:
                petal_length, petal_width, spece = i.split(',')
                IrisData.iris_infos.append(Iris(float(petal_length), float(petal_width), int(spece)))

def Distance(xa, xb, ya, yb):
    return sqrt((xb-xa)**2 + (yb-ya)**2)

def ListeDesDistances(x, y):
    """
    Calcul la distance entre chaque points dans IrisData.iris_infos et le point donné.

    Retourne une liste [(distance, espece), ...]
    """

    distances = []
    for i in range(len(IrisData.iris_infos)):
        d = Distance(IrisData.iris_infos[i].petal_length, x, IrisData.iris_infos[i].petal_width, y)
        distances.append((d, IrisData.iris_infos[i].spece))

    return distances

def TypeDUnIris(largeur, longueur, k):
    l = ListeDesDistances(longueur, largeur)
    l.sort()
    cnt = {}

    if k >= len(l):
        print("Error : k is too high.")
        k = len(l)

    for i in range(k):
        cnt[l[i][1]] = 1 if not cnt.get(l[i][1]) else cnt.get(l[i][1]) + 1

    sorted(cnt.items(), key=lambda it: it[1])
    return list(cnt)[0]
