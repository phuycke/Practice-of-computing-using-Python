#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

for i in range(10, 100):
    if str(i**2)[-2:] == str(i):
        print(i)
        break