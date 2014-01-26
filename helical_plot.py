#!/usr/bin/env python

'''Analyze helical scan equations'''

import pickle
import pylab

f = open('positions.pck')
positions = pickle.load(f)
f.close()

def plot_line():
    import matplotlib as mpl
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    import matplotlib.pyplot as plt

    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #x = [position['PhiZ'] for position in positions]
    x = [position['PhiZ'] for position in positions]
    y = [position['PhiY'] for position in positions]
    z = [100 * (position['SamX']**2 + position['SamY']**2)**0.5 for position in positions]
    #y = [position['SamX'] for position in positions]
    #z = [position['PhiX'] for position in positions]
    #theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    #z = np.linspace(-2, 2, 100)
    #r = z**2 + 1
    #x = r * np.sin(theta)
    #y = r * np.cos(theta)
    ax.plot(x, y, z, label='helical scan curve')
    ax.legend()

    plt.show()
    
plot_line()