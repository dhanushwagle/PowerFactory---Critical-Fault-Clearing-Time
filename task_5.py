# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:44:45 2021

@author: Lenovo
"""

# plotting 

import matplotlib.pyplot as plt

x = [0.1777, 0.2802, 0.3938, 0.4827, 0.5562]
y = [0.845, 2.1125, 4.225, 6.3375, 8.45]

plt.plot(x,y,'o-')
plt.title('Rotational Inertia vs Critical Clearing Time')
plt.xlabel('time (sec)')
plt.ylabel('Inertia (MJoule/MVA)')
plt.grid('on')
plt.show()