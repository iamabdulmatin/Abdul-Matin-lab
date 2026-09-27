# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:46:18 2026

@author: WELCOME
"""

import math

n=int(input("Enter number of terms: "))
a=float(input("Enter the value of a: "))

fractions_list=[]
values_list=[]

i=1
s=0

while i<=n:
    f=math.pow(a,i)
    v=math.factorial(i)
    t=f/v
    
    print(f"({a}**{i})/{i}!")
    
    fractions_list.append(f"{f}/{v}")
    values_list.append(str(round(t,4)))
    s=s+t
    i=i+1
    
fractions_string="+".join(fractions_list)
values_string="+".join(values_list)
   
print(f"{fractions_string}={values_string}={round(s,4)}") 










    
"""i=1
s=0
f=1

while i<=n:
    f=f*i
    t=pow(a,i)/(f)
    print(f"({a}**{i})/{i}!",)
    s=s+t
    i=i+1
    
print("sum=",s)"""