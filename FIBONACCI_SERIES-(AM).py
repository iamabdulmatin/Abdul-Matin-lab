# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:34:41 2026

@author: user3
"""

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
terms=int(input("Number of terms:"))

for i in range(terms):
    num3=num1+num2
    print(f"Step:{i+1}={num1}")
    num1=num2
    num2=num3
    
    
    

























"""n=int(input("Enter number of terms: "))

i=0
t=0
s=1
A=0
while i<n:
    print(t)
    A+=t
    next_term=t+s
    t=s
    s=next_term
    i+=1
print()
print(f"A={A}")"""
