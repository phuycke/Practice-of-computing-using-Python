#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def mirror(pair):
    if type(pair) != list   and \
        type(pair) != str   and \
         type(pair) != tuple:
              raise ValueError("Wrong type.\nPlease provide a str, list or set.")
    
    assert len(pair) >= 2
    
    return pair[0], pair[-1]

#%%

print(mirror("test"))
print(mirror((1, 2, 3, 5)))
print(mirror(5))