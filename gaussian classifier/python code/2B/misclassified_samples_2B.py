# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:53:35 2020

@author: Lenovo
"""


import gaussian_generator_2B as gg
import math

def misclassified_samples(c,x,y):
    misclassified_number=0
    mismosavi=0
    for i in range(0,99999):
        if c==1 :
            if x[i]>=0:
                if x[i]-math.sqrt( abs(- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i]+1.35981384722661)/0.125)>0:
                    misclassified_number=misclassified_number+1
                elif x[i]-math.sqrt( abs(- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i]+1.35981384722661)/0.125)==0:
                    mismosavi=mismosavi+1
                    
            elif x[i]<0:
                if x[i]+math.sqrt(abs (- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i]+1.35981384722661)/0.125)>0:
                    misclassified_number=misclassified_number+1
                elif x[i]+math.sqrt(abs (- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i]+1.35981384722661)/0.125)==0:
                    mismosavi=mismosavi+1

        elif c==2:
            if x[i]>=0:
                if x[i]-math.sqrt( abs(- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i]+1.35981384722661)/0.125)<0:
                    misclassified_number=misclassified_number+1
                elif x[i]-math.sqrt( abs(- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i]+1.35981384722661)/0.125)==0:
                    mismosavi=mismosavi+1
            elif x[i]<0:
                if x[i]+math.sqrt(abs (- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i]+1.35981384722661)/0.125)<0:
                    misclassified_number=misclassified_number+1
                elif x[i]+math.sqrt( abs(- 0.145833333333333*y[i]**2 + 0.166666666666667*y[i]+1.35981384722661)/0.125)==0:
                    mismosavi=mismosavi+1
      
    return mismosavi
                
ms1=misclassified_samples(1,gg.x1,gg.y1)
