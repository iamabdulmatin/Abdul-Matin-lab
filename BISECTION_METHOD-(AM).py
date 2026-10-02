# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:27:18 2026

@author: WELCOME
"""

import math 

def f(x):return x*math.tan(x)-x

while True:
    xl=float(input("lower limit xl: "))
    xu=float(input("upper limit xu: "))
    fxl=f(xl)
    fxu=f(xu)

    if fxl*fxu>0:
      print("WNONG ENTRY,continue...")
      continue
    else:
      break
    
print(f"Initial guess of lower limit:{xl},f(xl)={round(fxl,4)}")
print(f"Initial guess of upper limit:{xu},f(xu)={round(fxu,4)}")
print()

t=0.001
i=1

while True:
    xm=(xl+xu)/2
    fxm=f(xm)
    print(f"Iteration={i},xm={round(xm,4)},f(xm)={round(fxm,4)}")
    #print(i,xm,fxm)
    
    if abs(fxm)<t:
        break
    elif fxu*fxm>0:
         xu=xm
                        #continue
    else:
        xl=xm
                        #fxl = fxm
    i=i+1
    continue

print(f"The Final solution is:xm={round(xm,4)}")
print(f"Total Iteration is:{i}")
