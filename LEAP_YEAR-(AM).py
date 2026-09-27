# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:16:15 2026

@author: user3
"""

def fun(y):
    if y%400==0:
        print(f"{y} is a leap year")
    elif y%100==0:
        print(f"{y} is not a leap year")
    elif y%4==0:
        print(f"{y} is a leap year")
    else:
        print(f"{y} is not a leap year")
      
fun(1900)        
fun(2000)