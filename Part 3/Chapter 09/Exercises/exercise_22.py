#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# make the dictionary
d = dict(zip(list(range(0, 10)), ["zero", "one", "two", "three", "four", 
                                  "five", "six", "seven", "eight", "nine"]))

# ask the number and print its translation
in_str = str(input("Your number:\n"))
[print(d[int(l)], end = " ") for l in in_str]