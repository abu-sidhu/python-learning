# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:55:49 2022

@author: Sidhiq
"""

kases = int(input())
for kase in range(kases):
    N = int(input())
    result = 1
    for i in range(1, N + 1):
        result = result * i
    print (result)