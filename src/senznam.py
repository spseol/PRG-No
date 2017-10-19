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