# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:17:52 2021

@author: MUKKIL
"""
"""
row=int(input("Enter number of rows of star pyramid: "))
li=[]
for i in range(0, row):
    li.append('*')
    print(*li)
"""


row=int(input('Enter the number of rows:'))
for i in range(1,row+1):
  print(' '*(row-i),"* "*i)