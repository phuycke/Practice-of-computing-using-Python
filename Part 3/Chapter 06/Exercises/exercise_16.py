#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def common_multiples(X = int, 
                     Y = int, 
                     Z = int):
    
    common = list(set(list(range(X, Z+1, X))).intersection(list(range(Y, Z+1, Y))))
    common.sort()
    
    print("Common multiples of {} and {}".format(X, Y))
    [print("{0:2d}. {1: >8d}".format(i+1, common[i])) for i in range(len(common))]
    

common_multiples(7, 10, 1000)