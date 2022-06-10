# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 21:59:02 2021

@author: MUKKIL
"""

#Number divisible by 5

#num = list(map(int,input("Enter the numbers followed by space:  ").split(" ")))
num = list(map(int,input("Enter the numbers followed by ,:  ").split(",")))
print("numbers which divisible by 5 are ", end=" ")
num=set(num)
for i in num:
    if i%5==0:
        print(i, end=" ")