# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:12:24 2026
@author: user3
"""


import math

n=int(input("Enter number of terms: "))
th=int(input("Enter the value of th(in degree): "))

x=math.radians(th)

print("--- SINE SERIES ---")

i=1
t=x
s=t

print(f"Term {i}: Value = {t}, Current Sum = {s}")

while i<n:
    t=(-1)*t*pow(x,2)/(2*i*(2*i+1))
    s=s+t
    print(f"Term {i+1}: Value = {t}, Current Sum = {s}")
    i=i+1
    
print(f"Calculated sin({th}) = {s}")
print(f"Actual math.sin(x) = {math.sin(x)}\n")

print("--- COSINE SERIES ---")

i=1
t=1
s=t

print(f"Term {i}: Value = {t}, Current Sum = {s}")

while i<n:
    t=(-1)*t*pow(x,2)/((2*i-1)*(2*i))
    s=s+t
    print(f"Term {i+1}: Value = {t}, Current Sum = {s}")
    i=i+1
    
print(f"Calculated cos({th}) = {s}")
print(f"Actual math.cos(x) = {math.cos(x)}")
    