#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def exercise_43(string = str):
    L = list(string)
    L.sort()
    return "".join(L)

result = exercise_43(string = "appelsap")
print(result)