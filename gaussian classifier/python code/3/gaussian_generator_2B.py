# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:53:27 2020

@author: Lenovo
"""
import numpy as np
import matplotlib.pyplot as plt

"""توليد سمپل هاي گوسي تصادفي و پلات كردن آنها"""
def gaussian_generator_f():
    
    global x1,x2,y1,y2
    
    mean_c1 =(1, 1)
    cov_c1 =[[1, 0], [0, 1]]

    mean_c2 = (4, 4)
    cov_c2 =[[4, 0], [0, 8]]
    
    x1, y1 = np.random.default_rng().multivariate_normal(mean_c1, cov_c1, 100000).T
    x2, y2 = np.random.default_rng().multivariate_normal(mean_c2, cov_c2, 100000).T


gaussian_generator_f()


plt.plot(x2 , y2, 'x')
plt.axis('equal')
plt.xlabel("x")


plt.plot(x1 , y1,  'x')
plt.axis('equal')
plt.ylabel("y")