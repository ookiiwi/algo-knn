# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:39:23 2021

@author: zhadrami
"""

from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

iris_data = []
iris_type = []

def ChargeFichierTris():
    global iris_data
    global iris_type

    with open("iris.csv", mode='r') as f:
        f.readline()
        iris_type = [x.strip("\n") for x in f.readline().split(',')]

        for i in f:
                petal_length, petal_width, spece = i.split(',')
                iris_data.append((float(petal_length), float(petal_width), int(spece)))

def Distance(xa, xb, ya, yb):
    return sqrt((xb-xa)**2 + (yb-ya)**2)

def ListeDesDistances(x, y):
    distances = []
    for i in range(len(iris_data)):
        d = Distance(iris_data[i][0], x, iris_data[i][1], y)
        distances.append((d, iris_data[i][2]))

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

def FormatForPlot(l):
    x = [[]]
    y = [[]]
    
    l.sort(key=lambda t: t[2])

    for i in range(len(l)):
        j = l[i][2]

        if j > len(x)-1:
            x.append([])
            y.append([])
        x[j].append(l[i][0])
        y[j].append(l[i][1])
        
    return x, y

def update(val):
    k = sliderk.val
    longueur = sliderx.val
    largeur = slidery.val
    ptk.set_offsets((longueur, largeur))

    prediction = TypeDUnIris(largeur, longueur, k)
    txt="Résultat : "+iris_type[prediction]
    res.set_text(txt)

#valeurs
longueur=2
largeur=0.75
k=3
#fin valeurs

ChargeFichierTris()
x, y = FormatForPlot(iris_data)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

plt.axis('equal')
plt.scatter(x[0], y[0], color='g', label=iris_type[0])
plt.scatter(x[1], y[1], color='r', label=iris_type[1])
plt.scatter(x[2], y[2], color='b', label=iris_type[2])
ptk = plt.scatter(longueur, largeur, color='k')
plt.legend()

res = plt.text(3,0.1, '', fontsize=12) #init text

axcolor = 'lightgoldenrodyellow'
axk = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axx = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
axy = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

sliderk = Slider(axk, 'k', 1, 10, k, valstep=1)
sliderx = Slider(axx, 'x', 0, 10, longueur)
slidery = Slider(axy, 'y', 0, 10, largeur)
sliderk.on_changed(update)
sliderx.on_changed(update)
slidery.on_changed(update)

update(1)
plt.show()