# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:09:01 2021

@author: MUKKIL
"""
#fibonacci series
limit= int(input("Enter a number limit "))
i=1
j=0
add=0
if limit<0:
    print("The fibonacci series starts from 0")
else:
    print("The fibonacci series till the limit given is ",j,end="  ")
    while add<=limit:
        add=i+j
        i=j
        j=add
        if add<=limit:    
            print(add,end="  ")