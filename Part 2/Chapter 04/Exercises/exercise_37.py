#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

input1 = str(input("Input 1: "))
input2 = str(input("Input 2: "))

if len(input1) == len(input2):
    print("Both strings are equally long")
elif len(input1) > len(input2):
    print("Longest input: ", input1)
else:
    print("Longest input: ", input2)
