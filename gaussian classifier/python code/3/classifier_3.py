# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:35:33 2020

@author: Lenovo
"""
from numpy.random import randint
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.Symbol("x")
y = sp.Symbol("y")


"""" پلات كردن خط كلاسيفاير"""

x=np.linspace(-10,10,1000)
y=-x+5
plt.plot(x,y)
plt.axis('equal')
plt.show() 
def classifier_3(x,y):
    c=0
    if y>-x+5:
        c=2
    if y<-x+5:
        c=1
    elif y==-x+5:
        c=randint(0, 2, 1)
      
                
    return c
