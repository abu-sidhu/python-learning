# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:55:47 2021

@author: MUKKIL
"""

#character count
wor=input('Enter a string value:  ')
"""s=set(wor)
s="".join(s)
print(s)""" #without order
t=""
for j in wor:
    if j in t:
        continue
    else:
        t+=j
#print(t)
for j in t:
    if j is t[-1]:
        print(j,'=',wor.count(j))
    else:
        print(j,'=',wor.count(j),end=",")
   