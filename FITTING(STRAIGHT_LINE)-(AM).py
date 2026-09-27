# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:30:46 2026

@author: user3
"""

print("The straigt line equation is y = mx + c")
x=[1,2,3,4,5,6,7,8,9]
y=[1,2,3,4,5,6,7,8,9]

n1=(len(x))
n2=(len(y))

sx=0
sy=0
sxy=0
wsx=0
sx2=0

for i in range(0,n1):
    z=x[i]
    sx=sx+z
    sy=sy+y[i]
    sxy=sxy+(z*y[i])
    sx2=sx2+(z**2)
wsx=sx**2
    
print(sx,sy,sxy,sx2,wsx)
denominator = (n1 * sx2) - wsx

m = (n1 * sxy - sx * sy) / denominator
c = (sy * sx2 - sx * sxy) / denominator

print(c,m)    

from matplotlib import pyplot as plt
import numpy as np

plt.title("Python Plot")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.scatter(x, y,color="red", marker="*")

X=np.linspace(-1,10,100)
Y=m*X+c
plt.plot(X,Y,color='blue')

plt.legend()
plt.show()
