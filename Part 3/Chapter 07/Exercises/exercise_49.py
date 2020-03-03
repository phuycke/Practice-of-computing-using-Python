#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%


def add_frac(frac1 = tuple, frac2 = tuple):
    assert len(frac1) == len(frac2) == 2
    assert frac1[1]   == frac2[1]
    
    return (frac1[0] + frac2[0], frac1[1] + frac2[1])


def multiply_frac(frac1 = tuple, frac2 = tuple):
    assert len(frac1) == len(frac2) == 2
    
    return (frac1[0] * frac2[0], frac1[1] * frac2[1])


res = add_frac((1, 2), (4, 2))
print(res)

res = multiply_frac((1, 3), (1, 4))
print(res)