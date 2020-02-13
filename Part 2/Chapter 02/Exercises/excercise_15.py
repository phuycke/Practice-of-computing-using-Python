#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

import math

#%%

def is_prime(number = int):
    if number < 0:
        return -1
    if number <= 2:
        return True
    if not number % 2:
        return False
    for i in range(3, int(math.sqrt(number)), 2):
        if not number % i:
            return False
    return True

#%%
    
print(is_prime(37))
