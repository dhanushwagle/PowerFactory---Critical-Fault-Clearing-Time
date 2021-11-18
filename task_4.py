# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:27:28 2021

@author: Lenovo
"""

# plotting 

import matplotlib.pyplot as plt

x = [0.5667, 0.5799, 0.6060, 0.6350, 0.6703, 0.7095, 0.7573, 1, 1]
y = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 5.0, 10.0]

plt.plot(x,y,'o-')
plt.title('Fault resistance vs Critical Clearing Time')
plt.xlabel('time(sec)')
plt.ylabel('Resistance(ohm)')
plt.grid('on')
plt.show()