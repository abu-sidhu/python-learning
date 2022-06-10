# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:33:06 2021

@author: MUKKIL


#area of circle
import math
r=int(input('Radius= '))
print('Area of Circle with radius,',r, '=', math.pi*r**2)


#input
name=input('Enter the name: ')
roll=input('Enter the roll number: ') 
mark=input('Enter the mark: ')

print('\nName: ', name, '\nRoll No: ', roll, '\nMark: ',mark)
"""
#largest number from list

num_li=[]
lim=int(input('enter the limit of numbers : '))
print("Enter the numbers  : ")
for i in range(1, lim+1):
    num_li.append(int(input("\n" )))
lar=0
for i in num_li:
    if i>lar:
        lar=i
print('The largest number is :', lar)