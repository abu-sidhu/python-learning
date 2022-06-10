# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:24:49 2021

@author: MUKKIL
"""

a,b,c = input("Enter three numbers followed by space : ").split()
a=int(a)
b=int(b)
c=int(c)
print("First number :",a)
print("Second number :",b)
print("Third number :",c)
if a == b == c:
    print("Entered numbers are equal!!!")
elif a<=b and a<c:
    print(a," is smallest")
elif b<a and b<c:
    print(b," is smallest")
else:
    print(c," is smallest")