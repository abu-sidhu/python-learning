# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 21:39:03 2021

@author: MUKKIL
"""
mark=[12,34,10,23]
sum=0
for i in mark:
    sum+=i
else:
    print("Complete")
print(sum)

#while
n=int(input('Enter the number limit  '))
sum1=0
i=1
while i<=n:
    sum1+=i
    i+=1
print('The sum is', sum1)

#break
name='abhinav'
for x in name:
    if x=='i':
        break
    print(x)
print('\n\n')   

#continue
for x in name:
    if x=='i':
        continue
    print(x)