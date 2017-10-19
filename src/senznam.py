#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:01:42 2017

@author: nozka
"""

import random

i = 0
while i < 10:
    print(i, ':', random.randint(0,100))
    i = i + 1
    
for i in 0, 1, 2, 3, 4, 5, 6, 7, 8, 9:
    print(i, ':', random.randint(0,100))
    
for _ in range(10):
    print(random.randint(0,100))
    

seznam = []
for _ in range(100):
    seznam.append(random.randint(0,100))
print(seznam)

# krátce
sude_mocniny = [i*i for i in range(30) if i % 2 == 0]
# dlouze
sude_mocniny = []
for i in range(30):
    if i % 2 == 0:
        sude_mocniny.append(i*i)
print(sude_mocniny)

length = len
# Aritmetický průměr
soucet = 0
for cislo in seznam:
    soucet += cislo
print(soucet / len(seznam))

print(sum(seznam)/len(seznam))

"""
udělám si seznam náhodných  čísel a vypíšu 
ty co jsou dělitelné 7
"""

seznam = [random.randint(0,100) for _ in range(100)]
for i in seznam:
    if i % 7 == 0:
        print(i)
        






