# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:32:47 2026

@author: user3
"""

import math

def f(x):
    y=x*math.tan(x)-x
    return y

def df(x):
    dy=math.tan(x)+x*pow(math.cos(x),-2)-1
    return dy

while True:
    xo=float(input("Initial guess xo: "))
    fxo=f(xo)
    dfxo=df(xo)
    if dfxo==0:
        print("Wrong guess,Retry:")
        continue
    else:
        break
    
print(f"xo={round(xo,4)},f(xo)={round(fxo,4)},df(xo)={round(dfxo,4)}")
    
t=0.001 #Tolerance
c=1     #Count

while True:
    xn=xo-(f(xo)/df(xo))
    fxn=f(xn)
    
    print(f"Iteration{c}:xn={round(xn,4)},fxn={round(fxn,4)}")
    
    if abs(fxn)<t:
       print(f"Solution is xo={round(xn,4)}")
                                              #print(f"Value of the function at xo {fxn}")
                                              #print(f"Number of Iteration is {c}")
       break
    else:
       xo=xn
       c=c+1
       #print(c)
       continue
   
    
       
        