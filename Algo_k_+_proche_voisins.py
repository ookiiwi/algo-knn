# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:39:23 2021

@author: zhadrami
"""

import pandas
from math import sqrt
import matplotlib.pyplot as plt

iris_data = [[]]

def ClassementDesDistances(t):
    """
    Tri par insertion
    """

    i = 0
    j = 1
    k = 0
    
    while j < len(t):
        i = j-1
        k = t[j]
        
        while i >= 0 and t[i][1] > k[1]:
            t[i+1] = t[i]
            i -= 1
            
        t[i+1] = k
        j += 1

def ChargeFichierTris():
    global iris_data

    with open("iris.csv", mode='r') as f:
        for i in f:
            try:
                petal_length, petal_width, spece = i.split(',')

                if len(iris_data)-1 < int(spece):
                    iris_data.append([])

                iris_data[int(spece)].append((float(petal_length), float(petal_width)))
            except:     #ignore premiere ligne du fichier
                pass

def Distance(xa, xb, ya, yb):
    return sqrt((xb-xa)**2 + (yb-ya)**2)

def ListeDesDistances(x, y):
    distances = []
    for i in range(len(iris_data)):
        for j in range(len(iris_data[i])):
            d = Distance(iris_data[i][j][0], x, iris_data[i][j][1], y)
            distances.append((i, d))

    return distances

def TypeDUnIris(largeur, longueur, k):
    l = ListeDesDistances(longueur, largeur)
    cnt = [0]
    ClassementDesDistances(l)

    for i in range(k):
        try:
            if l[i][0]+1 >= len(cnt):
                cnt.append(0)

            cnt[l[i][0]] += 1
        except IndexError:
            print("Error : k is too high")
            break

    cnt.sort()
    return l[len(cnt)-1][0]

def FormatForPlot(l):
    x = [[]]
    y = [[]]

    for i in range(len(l)):
        for j in range(len(l[i])):
            x[i].append(l[i][j][0])
            y[i].append(l[i][j][1])
        x.append([])
        y.append([])

    return x, y

#valeurs
longueur=2.5
largeur=0.75
k=3
#fin valeurs

ChargeFichierTris()
x, y = FormatForPlot(iris_data)

plt.axis('equal')
plt.scatter(x[0], y[0], color='g', label='setosa')
plt.scatter(x[1], y[1], color='r', label='versicolor')
plt.scatter(x[2], y[2], color='b', label='virginica')
plt.scatter(longueur, largeur, color='k')
plt.legend()

prediction = TypeDUnIris(largeur, longueur, k)

#Affichage résultats
txt="Résultat : "
if prediction==0:
  txt=txt+"setosa"
if prediction==1:
  txt=txt+"versicolor"
if prediction==2:
  txt=txt+"virginica"
plt.text(3,0.5, f"largeur : {largeur} cm longueur : {longueur} cm", fontsize=12)
plt.text(3,0.3, f"k : {k}", fontsize=12)
plt.text(3,0.1, txt, fontsize=12)
#fin affichage résultats

plt.show()