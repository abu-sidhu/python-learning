# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:08:47 2021

@author: MUKKIL
"""
#multiplication table
def mult(n):
    for i in range(1, 11):
       print(i,'*',n,'=' ,i*n)
       
num=int(input( 'Enter the number for multiplication table  '))
mult(num)
