# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:49:52 2021

@author: MUKKIL
"""
def lar(x,y,z):
    lar=x
    if lar<y:
        lar=y
    if lar<z:
        lar=z
    return lar  
    
a,b,c=list(map(int, input("Enter 3 numbers  sperated by ,: ").split(",")))
print("The largest number is : ",lar(a,b,c))