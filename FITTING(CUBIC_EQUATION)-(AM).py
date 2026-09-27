# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 12:05:39 2026

@author: user3
"""

print("The equation is y = mx**3 + c")
x=[-3.00,-2.33,-1.67,-1.00,-0.33,0.33,1.00,1.67,2.33,3.00]
y=[-27.40,-10.22,-0.56,3.80,4.96,5.04,6.20,10.56,20.12,37.28]
n1=(len(x))
n2=(len(y))

sx=0
sy=0
sxy=0
wsx=0
sx2=0

for i in range(0,n1):
    z=pow(x[i],3)
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

import numpy as np 
from matplotlib import pyplot as plt 

plt.scatter(x,y,marker='*',color='red',label="scatter")

X=np.linspace(-3.5,3.5,100)
Y=m*X**3+c

plt.plot(X,Y,color='green',label="line")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("X-Y graph")
plt.grid(True)
plt.legend()
plt.show()