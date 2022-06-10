# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:23:48 2021

@author: MUKKIL
"""
#list

teacher_list=['remya','John','Abhi','Raj',2]
print(teacher_list[0])
print(teacher_list[-1])
print(teacher_list[-2])
print(teacher_list)
print(teacher_list[0:2])
teacher_list[3]='Nandu'
print(teacher_list[0:4])
print(len(teacher_list))
print(teacher_list.count('John'))
print(teacher_list.count('Jo'))#will search for whole string, so output= 0

teacher_list.append('Geetha')
print(teacher_list.append('Geetha'))# print not works but add geetha again
print(teacher_list.insert(2,'Hiran'))# print not works but insert hiran in 3rd
print(teacher_list)
teacher_list.remove('Geetha')
print(teacher_list)
teacher_list.remove("Geetha")
teacher_list.pop(-1)
print(teacher_list.sort())# print not works but sort, since all are 'string'
print(teacher_list)
list2=['gouri', 'nithya']
teacher_list.append(list2)
teacher_list.extend(list2)
print(teacher_list)
teacher_list.pop(-3)
print(teacher_list)