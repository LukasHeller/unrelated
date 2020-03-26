# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:42:21 2018

@author: lheller
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

kilo = 10**3

sand1 = np.array([22.4, 53, 15.7, 3.8, 1.7])/100
sand2 = np.array([28, 35, 18, 8, 8])/100
sand3 = np.array([34, 64, 2, 0.01, 0.01])/100
#sand3 = np.array([32, 49, 24, 3, 0.1])/100

sand1 = sand1/sand1.sum()
sand2 = sand2/sand2.sum()
sand3 = sand3/sand3.sum()

soll = np.array([30, 42, 22, 5, 1])/100
soll = soll/soll.sum()

jahresmenge = 41*kilo

num = 101
x = np.linspace(0,1,num)

#%%

leftover = np.zeros([num, num])
best  = [10000,10000] 
diffsum = 1000000

for k,perc1 in enumerate(x):
    for j, perc2 in enumerate(x):
        mix = perc2*sand1 + (1-perc2)*(perc1*sand2 + (1-perc1)*sand3)
        nadeloer = (mix/soll).argmin()
        temp = mix/mix[nadeloer]*soll[nadeloer]
        temp = temp/soll
        diff = (temp-1)*soll
        leftover[j,k] = diff.sum()
        if diff.sum() < diffsum:
            diffsum = diff.sum()
            best[:] = [perc1,perc2] 


#%%
x_2d, y_2d = np.meshgrid(x, x)
fig = plt.figure()
#ax = plt.pcolormesh(x_2d[0:200,800:1000], y_2d[0:200,800:1000], leftover[0:200,800:1000], norm=colors.LogNorm())
ax = plt.pcolormesh(x_2d, y_2d, leftover, norm=colors.LogNorm())
plt.contour(x_2d, y_2d, np.log(leftover), 10, colors = 'k')
plt.colorbar(ax)
plt.gca().set_aspect("equal") # x- und y-Skala im gleichen Maßstaab
plt.xlabel('a')
plt.ylabel('b')
#plt.xlim([0.9,1])
#plt.ylim([0,0.1])
plt.show()

#fig = plt.figure(1)
#plt.plot(x, leftover)       