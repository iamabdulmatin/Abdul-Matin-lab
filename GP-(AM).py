# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:12:24 2026

@author: user3
"""

a = float(input("Enter first term (a): "))
r = float(input("Enter common ratio (r): "))
n = int(input("Enter number of terms (n): "))

i = 1
s = 0

while i <= n:
    t = a*r**(i-1)
    print(f"Term {i} = {t}")
    
    s = s + t
    i = i + 1

print("Sum of GP series =", s)

    