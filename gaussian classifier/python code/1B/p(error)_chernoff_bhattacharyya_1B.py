# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:35:39 2020

@author: Lenovo
"""

import math 
import numpy as np
import matplotlib.pyplot as plt

mean_c1 = np.matrix([[1], [1]])
cov_c1 = np.matrix([[1, 0], [0, 1]])

mean_c2 = np.matrix([[4], [4]])
cov_c2 = np.matrix([[1, 0], [0, 1]])
pw1=0.2
pw2=0.8
def perror_chernoff_bound(B):
    
    
    A1=(B*(1-B))/2
    A2=(mean_c2-mean_c1).T
    A3=np.linalg.inv((B*cov_c1)+((1-B)*cov_c2))
    A4=mean_c2-mean_c1
    A5=(B*cov_c1)+((1-B)*cov_c2)
    A6=np.linalg.det(cov_c1)**B
    A7=np.linalg.det(cov_c2)**(1-B)    
    S=(np.linalg.det(A5)) / ((A6)+(A7)) 
    K= (  (A1)*(A2)*(A3)*(A4)  ) +  (0.5*math.log(S))
    A8=(pw1**B)*(pw2**(1-B))
    pe= A8*math.exp(-(K))

    return pe

""" for test:
B=0.6
pe= perror_chernoff_bound(B)
print(pe)
"""

B=np.linspace(0,1,10000)
pe=B.copy()

for i in range (0,9999):
    pe[i]= perror_chernoff_bound(B[i])
    
pe_bhattacharyya=perror_chernoff_bound(0.5)
   
minpe=min(pe)
Bi=np.where(pe == minpe)
minB=B[Bi]

print("min B in is:",B[Bi[0][0]])
print("so the p(error) for this B by chernoff bound is :",min(pe))
print("p(error) when B=0.5 by bhattacharyya bound is:",pe_bhattacharyya)

plt.plot(B,pe)
plt.axis('equal')
plt.xlabel("B")
plt.ylabel("p(error)")
plt.show()