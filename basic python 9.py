# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:07:09 2021

@author: MUKKIL
"""

#reverse list
num=list(map(int, input("Enter numbers seperated by , :").split(",")))

for i in range(1,len(num)+1):
    print(num[-i], end=" ")