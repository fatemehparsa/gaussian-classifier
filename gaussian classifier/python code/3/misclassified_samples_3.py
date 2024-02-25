# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:35:31 2020

@author: Lenovo
"""
import gaussian_generator_2B as gg

def misclassified_samples(c,x,y):
    misclassified_number=0
    mismosavi=0
    for i in range(0,99999):
        if c==1 :
            if y[i]>-x[i]+5:
                misclassified_number=misclassified_number+1
            elif y[i]==-x[i]+5:
                mismosavi=mismosavi+1
        elif c==2:
            if y[i]<-x[i]+5:
                misclassified_number=misclassified_number+1
            elif y[i]==-x[i]+5:
                mismosavi=mismosavi+1  
                
    return round((mismosavi/2)+misclassified_number)
                

ms1=misclassified_samples(1,gg.x1,gg.y1)
ms2=misclassified_samples(2,gg.x2,gg.y2)
mst=ms1+ms2

print(" c1 misclassified number is: " ,ms1 )

print(" c2 misclassified number is: " ,ms2 )

print(" c2 misclassified number is: " ,mst )