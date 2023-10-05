# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:39:23 2021

@author: zhadrami
"""

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from .iris_utils import ChargeFichierIris, TypeDUnIris, IrisData
import pandas as pd
import numpy as np

def FormatForPlot(l):
    """
    Formate une liste `[Iris(x,y,s), ... ]` au format ([[x, ...], ...] ,[[y, ...], ...])
    """

    lst = l
    x = [[]]
    y = [[]]
    
    lst.sort(key=lambda i: i.spece)

    for i in range(len(l)):
        j = l[i].spece

        if j >= len(x):
            x.append([])
            y.append([])
        x[j].append(l[i].petal_length)
        y[j].append(l[i].petal_width)
        
    return x, y

def main():
    #valeurs
    longueur=2
    largeur=0.75
    k=3

    ChargeFichierIris()
    x, y = FormatForPlot(IrisData.iris_infos)

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)
    plt.axis('equal')

    # interpolation lineaire des couleurs entre rouge et violet
    c = pd.Series([0xFF0000, 1000,np.nan, 0x800080])
    c = [hex(int(c)) for c in c.interpolate()]

    for i in range(len(IrisData.iris_type)):
        plt.scatter(x[i], y[i], color='#' + str(c[i])[2:] , label=IrisData.iris_type[i])

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

    def update(val):
        k = sliderk.val
        longueur = sliderx.val
        largeur = slidery.val
        ptk.set_offsets((longueur, largeur))
    
        prediction = TypeDUnIris(largeur, longueur, k)
        txt="Résultat : "+IrisData.iris_type[prediction]
        res.set_text(txt)

    sliderk.on_changed(update)
    sliderx.on_changed(update)
    slidery.on_changed(update)

    update(1)
    plt.show()