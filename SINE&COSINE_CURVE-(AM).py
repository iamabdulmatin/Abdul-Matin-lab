# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:14:32 2026

@author: user3
"""

import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,100)
y1=np.sin(x)
y2=np.cos(x)

fig,(ax1,ax2)=plt.subplots(2,1)

#sine wave

ax1.plot(x,y1,color="red")
ax1.set_title("sine wave")
ax1.grid(True)

#cosine wave

ax2.plot(x,y2,color="blue")
ax2.set_title("cosine wave")
ax2.grid(True)

plt.tight_layout()
plt.show()