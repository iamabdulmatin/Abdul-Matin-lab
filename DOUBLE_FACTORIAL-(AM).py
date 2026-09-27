# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:23:28 2026

@author: user3
"""
a=int(input("Enter a:"))

i=1
t=1

if a%2==0:
    i=2
else:
    i=1

while i<=a:
    x=t
    t=t*i
    print(f"Step:{x}*{i}={t}")
    i=i+2
    
