# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:04:53 2018

@author: Jarnd
"""


import matplotlib.pyplot as plt
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'],'size' : 12})
#rc('text', usetex = True)

def plot_city(chi,pnames):
    d2 = np.shape(chi)[0]
    _x = np.arange(d2)
    _y = np.arange(d2)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    ztot = np.reshape(np.asarray(chi), -1)
    
    zreal = np.real(ztot)
    zimag = np.imag(ztot)
    bottom = np.zeros_like(zreal)
    width = depth = 0.5
    zlim = [-0.0,np.max(zreal)]
    
    fig1 = plt.figure(figsize=(12, 9))
    
    ax1 = fig1.add_subplot(211, projection = '3d')
    
    
    ax1.bar3d(x, y, bottom, width, depth, zreal, shade=True)
    ax1.set_zlim(zlim)
    
    
    plt.xticks(np.arange(0.5,d2+0.5,1),pnames, rotation=55)
    plt.yticks(np.arange(0.5,d2+0.5,1),pnames, rotation=-60)
#    ax1.set_xlabel(r'$B_{m}$',labelpad=20)
    ax1.set_xlabel(r'$\leftarrow B_{m} \rightarrow$',labelpad=25)
    ax1.set_ylabel(r'$\leftarrow B_{n} \rightarrow$',labelpad=20) 
    ax1.xaxis.label.set_fontsize(18)
    ax2 = fig1.add_subplot(212, projection = '3d')
    ax2.bar3d(x, y, bottom, width, depth, zimag, shade=True)
    ax2.set_zlim(zlim)
    
    plt.xticks(np.arange(0.5,d2+0.5,1),pnames, rotation=55)
    plt.yticks(np.arange(0.5,d2+0.5,1),pnames, rotation=-60)
    
    #plt.xlabel('B_{m}',1)
    plt.show()