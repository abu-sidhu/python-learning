# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 13:41:18 2021

@author: MUKKIL
"""
#data types
#number
num=12
print(id(num))
num=34
print(id(num), '\n', type(num))
m=.0124
print(type(m))
c=1+2j
print(type(c))


#string

title='python programming'
print(len(title))
print(title.upper())
print(title.lower())
print(title.capitalize())
ne_title=title.replace( 'programming', 'strings')
print(ne_title)
print(title.count('m')) #to count 'm' in title
print(title.count('py'))
print(title[3:12])