# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:57:09 2021

@author: MUKKIL
"""

#prime number check

num=int(input("Enter the number : "))

if num<0:
    print(num,"Can't be a prime number by definition!!")
elif num==0 or num==1:
    print(num,"is neither prime nor composite  ")
elif num==2:
    print(num,"is the first prime number !!! ")
else:
    for x in range(2, num):
        if num % x ==0:
            print(num, "is not a prime number!!")
            prime=False
            break
        else:
            prime= True
    if prime:
        print(num, "is a prime number!!!")