# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:53:32 2020

@author: Lenovo
"""
from numpy.random import randint
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math

"""محاسبه كلاسيفاير بر اساس ماتريس كواريانس و ميانگين"""
x = sp.Symbol("x")
y = sp.Symbol("y")

mean_c1 = np.matrix([[1], [1]])
cov_c1 = np.matrix([[1, 0], [0, 1]])

mean_c2 = np.matrix([[4], [4]])
cov_c2 = np.matrix([[4, 0], [0, 8]])
pw1=0.2
pw2=0.8

X=np.matrix([[x],[y]])
A1=math.log(np.linalg.det(cov_c1))
A2=X-mean_c1
A3=np.linalg.inv(cov_c1)
A4=A2.T*A3*A2

B1=math.log(np.linalg.det(cov_c2))
B2=X-mean_c2
B3=np.linalg.inv(cov_c2)
B4=B2.T*B3*B2

g1=-A1-0.5*(A4)+math.log(pw1)
g2=-B1-0.5*(B4)+math.log(pw2)
tabe=g1-g2

print( " the classifier line is: ","0 =", sp.simplify((tabe[0,0])/3))

""" پلات كردن خط كلاسيفاير"""

y=np.linspace(-2.5351,3.67,10000)
x=np.linspace(0,0,10000)
x2=np.linspace(0,0,10000)
for i in range (0,9999):
    x[i]=math.sqrt ( abs(- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i] + 1.35981384722661)/0.125)
    x2[i]=-math.sqrt( abs(- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i] + 1.35981384722661)/0.125)
    
plt.plot(x,y)
plt.axis('equal')
plt.show() 

plt.plot(x2,y)
plt.axis('equal')
plt.show() 

"""تابع كلاسيفاير"""

def classifier_2B(x,y):
    c=0
    if x>=0 :
        if x-math.sqrt(abs (- 0.145833333333333*y**2 + 0.166666666666667*y+1.35981384722661)/0.125)<0:
            c=1
        elif x-math.sqrt(abs (- 0.145833333333333*y**2 + 0.166666666666667*y+1.35981384722661)/0.125)>0:
            c=2
        elif x-math.sqrt( abs(- 0.145833333333333*y**2 + 0.166666666666667*y+1.35981384722661)/0.125)==0:
            c=randint(0, 2, 1)
    elif x<0 :
        if x+math.sqrt( abs(- 0.145833333333333*y**2 + 0.166666666666667*y+1.35981384722661)/0.125)<0:
            c=1
        elif x+math.sqrt(abs (- 0.145833333333333*y**2 + 0.166666666666667*y+1.35981384722661)/0.125)>0:
            c=2
        elif x+math.sqrt( abs(- 0.145833333333333*y**2 + 0.166666666666667*y+1.35981384722661)/0.125)==0:
            c=randint(0, 2, 1)
      
                
    return c
