# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:15:44 2021

@author: MUKKIL


n=int (input('enter the no of rows '))
print("Full Pyramid Pattern of Stars (*): ")
for i in range(n):
  #  print(i)
    for s in range(-n-1, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()
 """   
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
   # for space in range(1, (rows-i)+1):   #For star pyramid
     #   print(end=" ")
   
    while k!=(i):
        print("*", end=" ")
        k += 1
   
    k = 0
    print()