#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

# know where to start
start = 0
for i in range(100, 1000):
    if i % 17 == 0:
        start = i
        break

# print all multiples of 17 starting from start
for i in range(start, 1000, 17):
    print(i)