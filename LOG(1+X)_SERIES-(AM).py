# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:12:24 2026

@author: user3
"""

#log(1+x)'s Taylor series
import math

n=int(input("Enter number of terms: "))
x=float(input("Enter the value of x[mod(x)<1]): "))

i=1
s=0

while i<=n:
    t=pow(-1,i+1)*pow(x,i)/(i)
    s=s+t
    print(i,t,s)
    i=i+1
    
print(f"log({1+x})={s}")

print("from module",math.log(1+x))
