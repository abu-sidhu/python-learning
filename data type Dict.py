# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:45:51 2021

@author: MUKKIL
"""

#dictionary


employee={'name':'John','em_id':'E012',"Join_y":2019}
print(employee)
print(employee['name'])
print(employee.get('em_id'))
employee['em_id']='E0134'
employee['last_co']="infosys"
print(employee)
del employee['last_co']
print(len(employee))
empl=employee.copy()
