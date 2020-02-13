#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

from itertools import permutations

def permute_string(string = str):
    
    [print("".join(p)) for p in permutations(string)]
    
permute_string("abc")
