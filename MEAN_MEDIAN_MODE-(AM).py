# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:10:40 2026

@author: WELCOME
"""

"""c=0

while c<n:
    i=0
    while i<(n-c-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
        print(i,l)
        i+=1
    c+=1
    print()    
print(l)"""
 
from collections import Counter as cn

x=[1,3.33,70,65,32,25,2.5]
n=len(x)
x.sort()
print(f"sorted list:{x}")

s=0
for i in range(n):
    s=s+x[i]     
a=s/n
    
print(f"Mean:\n{round(a,4)}")

if n%2==0:
    b=(x[int(n/2)]+x[int((n/2)-1)])/2 
else:
    b=x[int(n/2)]
    
print(f"Median:\n{round(b,4)}")

    
m=3*b-2*a  
print(f"Mode:\n{round(m,4)}")  

xc=x.count(65)
print(xc)

c=cn(x)

# Get the single most common element and its frequency
most_common_element, count=c.most_common(1)[0]  
print(f"Most_Common_Element:{most_common_element} (Appears {count} times)")
    
    