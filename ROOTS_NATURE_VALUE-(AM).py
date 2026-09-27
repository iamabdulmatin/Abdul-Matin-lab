# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:00:07 2026

@author: WELCOME
"""

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

D=b**2-4*a*c
r=-b/(2*a)

if D<0:
    i=pow(-D,0.5)/(2*a)
    print("Imaginary and Unequal")
    print(f"Roots are:{r}+{i}j and {r}-{i}j")
else:
    real_part=pow(D,0.5)/(2*a)
    if D>0:
        print("Real and Unequal")
        print(f"Roots are:{r+real_part} and {r-real_part}")
    else:
        print("Real and Equal")
        print(f"Root is:{r}")
            
            
     