#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def my_min(L = list):
    assert len(L) > 0
    if len(L) == 1:
        return L[0]
    else:
        minimum = L[0]
        for i in range(1, len(L)):
            if L[i] < minimum:
                minimum = L[i]
        return minimum

def my_max(L = list):
    assert len(L) > 0
    if len(L) == 1:
        return L[0]
    else:
        maximum = L[0]
        for i in range(1, len(L)):
            if L[i] > maximum:
                maximum = L[i]
        return maximum
    
min_test = my_min(L = [9, 17, 3, 8, 87, 0, 25])
max_test = my_max(L = [9, 17, 3, 8, 87, 0, 25])

print(min_test)
print(max_test)