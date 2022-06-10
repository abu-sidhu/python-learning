# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 20:46:45 2021

@author: MUKKIL
"""

#copy from tuple

tuple1 = (11, 22, 33, 44, 55, 66)
li=list(tuple1)
tu=[]
for i in li:
    if i == 44:
        tu.append(44)
        
    elif i== 55:
         tu.append(55)
copied_tuple=tuple(tu)
print("copied_tuple =  ", copied_tuple)