# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:57:27 2020

@author: Lenovo
"""
from numpy.random import randint
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

"""محاسبه كلاسيفاير بر اساس ماتريس كواريانس و ميانگين"""
x = sp.Symbol("x")
y = sp.Symbol("y")

mean_c1 = np.matrix([[1], [1]])
cov_c1 = np.matrix([[1, 0], [0, 1]])

mean_c2 = np.matrix([[4], [4]])
cov_c2 = np.matrix([[1, 0], [0, 1]])


w = mean_c1 - mean_c2
X= np.matrix([[x], [y]])
X0=(mean_c1 + mean_c2)/2
tabe=w.T*(X-X0)

print( " the classifier line is: ","0 =", sp.simplify((tabe[0,0])/3))

"""" پلات كردن خط كلاسيفاير"""

x=np.linspace(-10,10,1000)
y=-x+5
plt.plot(x,y)
plt.axis('equal')
plt.show() 
def classifier_1A(x,y):
    c=0
    if y>-x+5:
        c=2
    if y<-x+5:
        c=1
    elif y==-x+5:
        c=randint(0, 2, 1)
      
                
    return c
