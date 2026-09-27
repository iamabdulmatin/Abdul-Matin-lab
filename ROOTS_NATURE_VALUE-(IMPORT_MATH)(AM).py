# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:07:32 2026

@author: WELCOME
"""
        
import math
        
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

D=b**2-4*a*c

if D>0:
    root1=(-b+math.sqrt(D))/(2*a)
    root2=(-b-math.sqrt(D))/(2*a)
    print("Real and Unequal")
    print(f"Roots are:{root1} and {root2}")
elif D==0:
    root=-b/(2*a)
    print("Real and Equal")
    print(f"Root:{root}")
else:
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(-D)/(2*a)
    print("Imaginary and Unequal")
    print(f"Roots are:{real_part}+{imaginary_part}j and {real_part}-{imaginary_part}j")