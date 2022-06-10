# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 19:26:38 2021

@author: MUKKIL
"""

#identity
num=23
print(type(num) is int)
print(type(num) is not int)
print(type(num) == int) # similar to 'is'
print(type(20) != int) # similar to 'is not'

#membership

name=["John", "Raj", 'Ram']
name1=name.copy()
print('John' in name)
print("ram"not in name)
print(name in name)
print(name is name1)
print(name == name1)

#assignment

a=3
a+=4
print(a)
a>>=2
print(a)
a<<=1
print(a)