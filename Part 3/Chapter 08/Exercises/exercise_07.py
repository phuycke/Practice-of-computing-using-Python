#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def evens(n : int) -> list:
    return list(range(2, n*2+1, 2))

#%%
    
print(evens(5))