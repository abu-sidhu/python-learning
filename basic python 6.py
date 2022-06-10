# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:16:06 2021

@author: MUKKIL
"""
print('enter 10 numbers')
num_li=[]
for i in range(1, 11):
    num_li.append(int(input()))
for i in range(0, 10):
    #  print(num_li[i])    
    if num_li[i] == num_li[0]:
        print("Current Number", num_li[0], 'Previous Number', 0 ,'Sum:', num_li[0])
    else:
        print("Current Number", num_li[i], 'Previous Number', num_li[i-1] ,'Sum:', num_li[i]+num_li[i-1])
    