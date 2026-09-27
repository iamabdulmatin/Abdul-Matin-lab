# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 09:43:39 2026

@author: WELCOME
"""

a = float(input("Enter first term (a): "))
d = float(input("Enter common difference (d): "))
n = int(input("Enter number of terms (n): "))

i = 1
s = 0

while i <= n:
    t = a + (i - 1) * d
    print(f"Term {i} = {t}")
    
    s = s + t
    i = i + 1

print("Sum of AP series =", s)

    